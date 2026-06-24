#!/usr/bin/env python3
"""
LexScale.ai Content Validator — Phase 3 Publishing Safeguard
Usage:
  python validate_content.py <file.html>               # validate a single page
  python validate_content.py --hub insights/foo.html   # validate hub + sync check
  python validate_content.py --all                     # validate every HTML page
  python validate_content.py --sync-hub insights/foo.html  # add missing cards to hub
"""

import os
import re
import sys
import glob
from pathlib import Path

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://lexscale.ai"
INSIGHTS_DIR = os.path.join(ROOT, "insights")

# ── helpers ──────────────────────────────────────────────────────────────────

def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def hub_for_article(article_path):
    """Return the hub .html path for an article, or None if article is a hub."""
    rel = os.path.relpath(article_path, ROOT)
    parts = rel.replace("\\", "/").split("/")
    # insights/<category>/<slug>.html → hub = insights/<category>.html
    if len(parts) == 3 and parts[0] == "insights":
        return os.path.join(ROOT, "insights", parts[1] + ".html")
    return None

def articles_on_disk(category_dir):
    """Return list of .html files in a hub's category directory."""
    return sorted(glob.glob(os.path.join(category_dir, "*.html")))

def articles_in_hub(hub_html):
    """Return set of relative hrefs found in art-card links inside hub."""
    hrefs = set()
    for m in re.finditer(r'<a\s+href="([^"]+)"\s+class="art-card', hub_html):
        hrefs.add(m.group(1))
    return hrefs

def slug_from_path(path):
    return "/" + os.path.relpath(path, ROOT).replace("\\", "/")

# ── validators ───────────────────────────────────────────────────────────────

def validate_file(path):
    issues = []
    html = read(path)
    rel = os.path.relpath(path, ROOT).replace("\\", "/")
    is_hub = re.match(r"^insights/[^/]+\.html$", rel)
    is_article = re.match(r"^insights/[^/]+/[^/]+\.html$", rel)
    is_home = rel == "index.html"

    # title
    titles = re.findall(r"<title>(.+?)</title>", html, re.DOTALL)
    if len(titles) != 1:
        issues.append(f"TITLE: expected 1, found {len(titles)}")
    else:
        t = titles[0].strip()
        if not (20 <= len(t) <= 70):
            issues.append(f"TITLE length {len(t)} (want 20–70): {t[:60]}")

    # meta description
    desc = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', html)
    if not desc:
        issues.append("META DESC: missing")
    else:
        d = desc.group(1)
        if not (100 <= len(d) <= 165):
            issues.append(f"META DESC length {len(d)} (want 100–165): {d[:60]}...")

    # canonical
    if not re.search(r'<link\s+rel="canonical"', html):
        issues.append("CANONICAL: missing")

    # robots
    if not re.search(r'<meta\s+name="robots"', html):
        issues.append("ROBOTS: missing")

    # OG tags
    for og in ["og:title", "og:description", "og:url", "og:image", "og:site_name"]:
        if f'property="{og}"' not in html:
            issues.append(f"OG: missing {og}")

    # Twitter tags
    for tw in ["twitter:card", "twitter:title", "twitter:description", "twitter:image"]:
        if f'name="{tw}"' not in html:
            issues.append(f"TWITTER: missing {tw}")

    # H1
    h1s = re.findall(r"<h1[\s>]", html, re.IGNORECASE)
    if len(h1s) != 1:
        issues.append(f"H1: expected 1, found {len(h1s)}")

    # JSON-LD
    if not re.search(r'<script\s+type="application/ld\+json"', html):
        issues.append("JSON-LD: no schema blocks found")

    # BreadcrumbList (not required on homepage)
    if not is_home and "BreadcrumbList" not in html:
        issues.append("SCHEMA: BreadcrumbList missing")

    # FAQPage on hubs
    if is_hub and "FAQPage" not in html:
        issues.append("SCHEMA: FAQPage missing on hub page")

    # images alt
    imgs = re.findall(r"<img\s[^>]+>", html, re.IGNORECASE)
    for img in imgs:
        if "alt=" not in img:
            issues.append(f"IMG ALT: missing on <img {img[:60]}...>")

    # internal links
    internal = re.findall(r'href="[^"#]*\.html[^"]*"', html)
    if len(internal) < 5:
        issues.append(f"INTERNAL LINKS: only {len(internal)} (need ≥5)")

    # sitemap check
    sitemap_path = os.path.join(ROOT, "sitemap.xml")
    if os.path.exists(sitemap_path):
        sitemap = read(sitemap_path)
        slug = rel
        if slug not in sitemap and slug.lstrip("/") not in sitemap:
            issues.append(f"SITEMAP: {rel} not found in sitemap.xml")

    # hub-specific: stat bar count matches disk
    if is_hub:
        cat_dir = os.path.join(INSIGHTS_DIR, re.match(r"^insights/(.+)\.html$", rel).group(1))
        if os.path.isdir(cat_dir):
            disk_count = len(articles_on_disk(cat_dir))
            stat_match = re.search(r'class="stat-num">(\d+)</div>\s*<div[^>]*class="stat-lbl">in-depth', html)
            if stat_match:
                bar_count = int(stat_match.group(1))
                if bar_count != disk_count:
                    issues.append(f"STAT BAR: shows {bar_count} but {disk_count} articles on disk")
            else:
                issues.append("STAT BAR: could not find article count element")

        # hub: all disk articles must appear as cards
        in_hub = articles_in_hub(html)
        for art_path in articles_on_disk(cat_dir) if os.path.isdir(cat_dir) else []:
            art_rel = "/" + os.path.relpath(art_path, ROOT).replace("\\", "/")
            if art_rel not in in_hub:
                issues.append(f"HUB CARD MISSING: {art_rel}")

    # article: must link back to parent hub
    if is_article:
        m = re.match(r"^insights/([^/]+)/[^/]+\.html$", rel)
        if m:
            hub_slug = f"/insights/{m.group(1)}.html"
            if hub_slug not in html:
                issues.append(f"BACK LINK: article doesn't link to parent hub {hub_slug}")

    return issues


def sync_hub(hub_path):
    """Add missing article cards to a hub page and fix stat bar count."""
    html = read(hub_path)
    rel = os.path.relpath(hub_path, ROOT).replace("\\", "/")
    m = re.match(r"^insights/(.+)\.html$", rel)
    if not m:
        print(f"Not a hub file: {hub_path}")
        return

    cat = m.group(1)
    cat_dir = os.path.join(INSIGHTS_DIR, cat)
    if not os.path.isdir(cat_dir):
        print(f"Category directory not found: {cat_dir}")
        return

    disk_files = articles_on_disk(cat_dir)
    in_hub = articles_in_hub(html)
    missing = []
    for art_path in disk_files:
        art_rel = "/" + os.path.relpath(art_path, ROOT).replace("\\", "/")
        if art_rel not in in_hub:
            missing.append(art_path)

    if not missing:
        print(f"✓ {rel}: all {len(disk_files)} articles present in hub")
        return

    print(f"Adding {len(missing)} missing cards to {rel}...")
    for art_path in missing:
        art_html = read(art_path)
        art_rel = "/" + os.path.relpath(art_path, ROOT).replace("\\", "/")

        # extract title and description
        title_m = re.search(r"<title>(.+?)</title>", art_html, re.DOTALL)
        raw_title = title_m.group(1).strip() if title_m else os.path.basename(art_path)
        title = re.sub(r"\s*\|\s*LexScale\.ai\s*$", "", raw_title)

        desc_m = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', art_html)
        desc = desc_m.group(1)[:120] + "…" if desc_m and len(desc_m.group(1)) > 120 else (desc_m.group(1) if desc_m else "")

        card = f'''
      <a href="{art_rel}" class="art-card">
        <div class="art-card-top">
          <div class="art-cat-badge">{cat.replace("-", " ").title()}</div>
        </div>
        <h3 class="art-title">{title}</h3>
        <p class="art-desc">{desc}</p>
        <div class="art-card-footer">
          <div class="art-meta">LexScale.ai Editorial</div>
          <span class="art-read-link">Read article →</span>
        </div>
      </a>'''

        # inject before last </div> in last art-group grid
        last_grid_close = html.rfind('</div>\n      </div>\n    </div>', 0, html.find('hub-faq-section') if 'hub-faq-section' in html else len(html))
        if last_grid_close == -1:
            last_grid_close = html.rfind('</div>', 0, len(html) - 200)
        insert_pos = html.rfind('</div>', 0, last_grid_close)
        if insert_pos != -1:
            html = html[:insert_pos] + card + "\n      " + html[insert_pos:]
            print(f"  + {art_rel}")

    # fix stat bar
    disk_count = len(disk_files)
    html = re.sub(
        r'(class="stat-num">)\d+(</div>\s*<div[^>]*class="stat-lbl">in-depth)',
        lambda mo: mo.group(1) + str(disk_count) + mo.group(2),
        html
    )

    with open(hub_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✓ {rel}: added {len(missing)} cards, stat bar → {disk_count}")


# ── entry point ──────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]

    if not args or args[0] == "--help":
        print(__doc__)
        return

    if args[0] == "--all":
        pages = glob.glob(os.path.join(ROOT, "**/*.html"), recursive=True)
        failed = 0
        for p in sorted(pages):
            issues = validate_file(p)
            rel = os.path.relpath(p, ROOT)
            if issues:
                print(f"\n✗ {rel}")
                for i in issues:
                    print(f"  {i}")
                failed += 1
            else:
                print(f"✓ {rel}")
        print(f"\n{'All pages valid.' if not failed else str(failed) + ' page(s) have issues.'}")
        sys.exit(1 if failed else 0)

    if args[0] == "--sync-hub":
        if len(args) < 2:
            print("Usage: --sync-hub insights/<category>.html")
            sys.exit(1)
        sync_hub(os.path.join(ROOT, args[1]))
        return

    if args[0] == "--hub":
        target = os.path.join(ROOT, args[1]) if len(args) > 1 else None
        if not target:
            print("Usage: --hub insights/<category>.html")
            sys.exit(1)
        issues = validate_file(target)
        rel = os.path.relpath(target, ROOT)
        if issues:
            print(f"✗ {rel}")
            for i in issues:
                print(f"  {i}")
            sys.exit(1)
        else:
            print(f"✓ {rel}: all checks passed")
        return

    # single file
    target = os.path.join(ROOT, args[0]) if not os.path.isabs(args[0]) else args[0]
    if not os.path.exists(target):
        print(f"File not found: {target}")
        sys.exit(1)
    issues = validate_file(target)
    rel = os.path.relpath(target, ROOT)
    if issues:
        print(f"✗ {rel}")
        for i in issues:
            print(f"  {i}")
        sys.exit(1)
    else:
        print(f"✓ {rel}: all checks passed")


if __name__ == "__main__":
    main()
