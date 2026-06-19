#!/usr/bin/env python3
"""
migrate_insights.py — Restructure Insights pages into /insights/ URL silos.

Creates insights/{category}/{article}.html copies with:
  - Updated canonical + og:url
  - Updated BreadcrumbList JSON-LD
  - All internal hrefs converted to absolute paths
  - Nav Insights dropdown links updated to /insights/...

Also:
  - Adds 301 redirects to vercel.json
  - Adds new /insights/... URLs to sitemap.xml
  - Updates root service/home pages' nav Insights links
"""

import os, re, json, glob, shutil

BASE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://lexscale.ai"

# ── Category map: hub_file → {slug, articles} ────────────────────────────────
CATEGORIES = {
    "chatgpt": {
        "hub": "chatgpt.html",
        "articles": [
            "chatgpt-for-law-firms.html",
            "how-chatgpt-finds-and-recommends-law-firms.html",
            "how-law-firms-can-rank-in-chatgpt.html",
            "chatgpt-seo-for-lawyers.html",
            "chatgpt-citations-explained.html",
            "chatgpt-vs-google-search-for-lawyers.html",
            "future-of-chatgpt-and-legal-marketing.html",
            "best-practices-optimizing-law-firm-websites-for-chatgpt.html",
            "why-chatgpt-matters-for-law-firms.html",
        ],
    },
    "google-gemini": {
        "hub": "google-gemini.html",
        "articles": ["google-gemini-for-law-firms.html"],
    },
    "perplexity": {
        "hub": "perplexity.html",
        "articles": [
            "what-is-perplexity-ai-for-law-firms.html",
            "how-perplexity-ai-ranks-law-firms.html",
            "how-to-rank-in-perplexity-ai.html",
        ],
    },
    "ai-seo": {
        "hub": "ai-seo.html",
        "articles": [
            "ai-seo-for-law-firms-complete-guide.html",
            "ai-seo-vs-traditional-seo-lawyers.html",
            "common-mistakes-law-firms-make-with-ai-search.html",
            "how-ai-search-is-changing-legal-marketing.html",
            "how-google-ai-overviews-affect-law-firms.html",
            "local-ai-seo-for-law-firms.html",
        ],
    },
    "ai-receptionists": {
        "hub": "ai-receptionists.html",
        "articles": [
            "ai-receptionist-intake-automation.html",
            "ai-receptionist-vs-human-receptionist.html",
            "what-is-an-ai-receptionist-for-law-firms.html",
            "how-ai-receptionists-increase-law-firm-revenue.html",
            "never-miss-a-call-law-firm.html",
        ],
    },
    "ai-chatbots": {
        "hub": "ai-chatbots.html",
        "articles": [
            "ai-chatbot-for-law-firm-website.html",
            "ai-chatbot-intake-qualification.html",
            "ai-chatbot-roi-for-law-firms.html",
            "ai-chatbot-vs-live-chat-lawyers.html",
            "how-ai-chatbots-convert-legal-leads.html",
        ],
    },
    "entity-seo": {
        "hub": "entity-seo.html",
        "articles": [
            "entity-seo-vs-keyword-seo.html",
            "what-is-entity-seo-for-law-firms.html",
            "attorney-knowledge-panel-optimization.html",
            "local-business-schema-law-firms.html",
            "schema-markup-for-lawyers-guide.html",
            "topical-authority-for-law-firms.html",
        ],
    },
    "ai-websites": {
        "hub": "ai-websites.html",
        "articles": [
            "ai-website-design-for-law-firms-guide.html",
            "law-firm-website-conversion-optimization.html",
            "law-firm-website-seo-structure.html",
            "law-firm-website-speed-performance.html",
            "mobile-first-law-firm-website.html",
        ],
    },
}

# Build a flat lookup: old_slug → new_path  (no .html, no leading /)
SLUG_MAP = {}
for cat, info in CATEGORIES.items():
    hub_slug = info["hub"].replace(".html", "")
    SLUG_MAP[hub_slug] = f"insights/{cat}"
    for art in info["articles"]:
        art_slug = art.replace(".html", "")
        SLUG_MAP[art_slug] = f"insights/{cat}/{art_slug}"

def read(path):
    return open(path, encoding="utf-8").read()

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(content)

def update_canonical(html, new_slug):
    """Replace canonical and og:url with new absolute URL."""
    new_url = f"{SITE}/{new_slug}"
    html = re.sub(
        r'<link rel="canonical" href="[^"]*"/>',
        f'<link rel="canonical" href="{new_url}"/>',
        html
    )
    html = re.sub(
        r'(<meta property="og:url" content=")[^"]*(")',
        rf'\g<1>{new_url}\g<2>',
        html
    )
    return html

def update_breadcrumb(html, cat, cat_label, article_slug=None, article_title=None):
    """Patch BreadcrumbList JSON-LD to reflect new /insights/cat[/article] path."""
    cat_url = f"{SITE}/insights/{cat}"

    if article_slug and article_title:
        new_bc = [
            {"@type": "ListItem", "position": 1, "name": "Home",    "item": SITE},
            {"@type": "ListItem", "position": 2, "name": "Insights", "item": f"{SITE}/insights"},
            {"@type": "ListItem", "position": 3, "name": cat_label,  "item": cat_url},
            {"@type": "ListItem", "position": 4, "name": article_title,
             "item": f"{cat_url}/{article_slug}"},
        ]
    else:
        new_bc = [
            {"@type": "ListItem", "position": 1, "name": "Home",    "item": SITE},
            {"@type": "ListItem", "position": 2, "name": "Insights", "item": f"{SITE}/insights"},
            {"@type": "ListItem", "position": 3, "name": cat_label,  "item": cat_url},
        ]

    new_bc_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": new_bc,
    }, indent=2)

    # Replace existing BreadcrumbList block
    html = re.sub(
        r'<script type="application/ld\+json">\s*\{[^}]*"BreadcrumbList"[\s\S]*?</script>',
        f'<script type="application/ld+json">\n{new_bc_json}\n</script>',
        html
    )
    return html

def make_hrefs_absolute(html, new_path_prefix):
    """
    Convert all relative href="slug" to href="/absolute/path".
    new_path_prefix e.g. "insights/chatgpt" (no leading /)
    """
    def replace_href(m):
        href = m.group(1)
        # Skip already-absolute, external, anchor, mailto
        if href.startswith(('http', '/', '#', 'mailto:')):
            return m.group(0)
        # Skip empty or just a dot
        if not href or href in ('.', './'):
            return m.group(0)

        slug = href.rstrip('/')

        # Is slug in our migration map?
        if slug in SLUG_MAP:
            return f'href="/{SLUG_MAP[slug]}"'

        # Is it a known service/root page? Keep as absolute root path
        root_pages = {
            "index", "", "about", "contact", "privacy",
            "ai-seo-for-law-firms", "ai-chatbot-for-law-firms",
            "ai-receptionist-for-law-firms", "ai-website-design-for-law-firms",
        }
        if slug in root_pages:
            return f'href="/{slug}"' if slug else 'href="/"'

        # Otherwise prefix with current page's parent path
        return f'href="/{new_path_prefix}/{slug}"'

    return re.sub(r'href="([^"]*)"', replace_href, html)

# ── Category display labels ───────────────────────────────────────────────────
CAT_LABELS = {
    "chatgpt":         "ChatGPT for Law Firms",
    "google-gemini":   "Google Gemini for Law Firms",
    "perplexity":      "Perplexity AI for Law Firms",
    "ai-seo":          "AI SEO for Law Firms",
    "ai-receptionists":"AI Receptionists for Law Firms",
    "ai-chatbots":     "AI Chatbots for Law Firms",
    "entity-seo":      "Entity SEO for Law Firms",
    "ai-websites":     "AI Websites for Law Firms",
}

# ── Extract page title for breadcrumb ────────────────────────────────────────
def extract_title(html):
    m = re.search(r'<title>([^<]*)</title>', html)
    if not m:
        return ""
    t = m.group(1)
    # Strip brand suffix
    t = re.sub(r'\s*[\|·—]\s*LexScale\.ai\s*$', '', t).strip()
    return t

# ── 1. Create insights directory structure and copy files ─────────────────────
print("=== Creating insights/ files ===")
redirects = []
new_sitemap_urls = []

for cat, info in CATEGORIES.items():
    cat_label = CAT_LABELS[cat]
    insights_dir = os.path.join(BASE, "insights", cat)
    os.makedirs(insights_dir, exist_ok=True)

    # Hub page
    hub_src = os.path.join(BASE, info["hub"])
    if os.path.exists(hub_src):
        html = read(hub_src)
        new_slug = f"insights/{cat}"
        html = update_canonical(html, new_slug)
        html = update_breadcrumb(html, cat, cat_label)
        html = make_hrefs_absolute(html, f"insights/{cat}")
        # Write to insights/{cat}.html (not inside the subdir — at insights/ level)
        dest = os.path.join(BASE, "insights", f"{cat}.html")
        write(dest, html)
        print(f"  ✓ hub: insights/{cat}.html")
        redirects.append({
            "source": f"/{cat}",
            "destination": f"/insights/{cat}",
            "permanent": True
        })
        new_sitemap_urls.append((f"insights/{cat}", "0.8", "monthly"))
    else:
        print(f"  ✗ MISSING hub: {info['hub']}")

    # Article pages
    for art_file in info["articles"]:
        art_src = os.path.join(BASE, art_file)
        if not os.path.exists(art_src):
            print(f"  ✗ MISSING article: {art_file}")
            continue
        html = read(art_src)
        art_slug = art_file.replace(".html", "")
        new_slug = f"insights/{cat}/{art_slug}"
        title = extract_title(html)
        html = update_canonical(html, new_slug)
        html = update_breadcrumb(html, cat, cat_label, art_slug, title)
        html = make_hrefs_absolute(html, f"insights/{cat}")
        dest = os.path.join(insights_dir, art_file)
        write(dest, html)
        print(f"  ✓ article: insights/{cat}/{art_file}")
        redirects.append({
            "source": f"/{art_slug}",
            "destination": f"/insights/{cat}/{art_slug}",
            "permanent": True
        })
        new_sitemap_urls.append((f"insights/{cat}/{art_slug}", "0.7", "monthly"))

# ── 2. Update vercel.json with 301 redirects ──────────────────────────────────
print("\n=== Updating vercel.json ===")
vcfg_path = os.path.join(BASE, "vercel.json")
vcfg = json.loads(read(vcfg_path))
existing = {r["source"] for r in vcfg.get("redirects", [])}
new_redirects = [r for r in redirects if r["source"] not in existing]
vcfg.setdefault("redirects", []).extend(new_redirects)
write(vcfg_path, json.dumps(vcfg, indent=2) + "\n")
print(f"  ✓ Added {len(new_redirects)} redirects to vercel.json")

# ── 3. Add new URLs to sitemap.xml ───────────────────────────────────────────
print("\n=== Updating sitemap.xml ===")
import datetime
today = datetime.date.today().isoformat()
sm_path = os.path.join(BASE, "sitemap.xml")
sm = read(sm_path)
added_sm = 0
for (slug, priority, freq) in new_sitemap_urls:
    url = f"{SITE}/{slug}"
    if f"<loc>{url}</loc>" not in sm:
        entry = f"""  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>"""
        sm = sm.replace("</urlset>", entry + "\n</urlset>")
        added_sm += 1
write(sm_path, sm)
print(f"  ✓ Added {added_sm} URLs to sitemap.xml")

# ── 4. Update nav Insights links in ALL root HTML files ──────────────────────
print("\n=== Updating nav Insights links in root pages ===")
# Pattern: href="chatgpt" → href="/insights/chatgpt" (hub slugs only)
hub_slugs = {info["hub"].replace(".html", ""): cat for cat, info in CATEGORIES.items()}

root_html_files = sorted(glob.glob(os.path.join(BASE, "*.html")))
updated_nav = 0
for fpath in root_html_files:
    html = read(fpath)
    original = html
    for hub_slug, cat in hub_slugs.items():
        # Only update nav/dropdown hrefs — use context to be safe
        # Match href="chatgpt" but not href="chatgpt-for-law-firms" (service page)
        html = re.sub(
            rf'href="{re.escape(hub_slug)}"',
            f'href="/insights/{cat}"',
            html
        )
    # Also update article hrefs that appear in cards on hub pages
    for cat, info in CATEGORIES.items():
        for art_file in info["articles"]:
            art_slug = art_file.replace(".html", "")
            html = re.sub(
                rf'href="{re.escape(art_slug)}"',
                f'href="/insights/{cat}/{art_slug}"',
                html
            )
    if html != original:
        write(fpath, html)
        updated_nav += 1

print(f"  ✓ Updated nav/article links in {updated_nav} root pages")

# ── 5. Verification ───────────────────────────────────────────────────────────
print("\n=== Verification ===")
insight_files = glob.glob(os.path.join(BASE, "insights", "**", "*.html"), recursive=True)
print(f"  Total files in insights/: {len(insight_files)}")
vcfg_final = json.loads(read(vcfg_path))
print(f"  Total redirects in vercel.json: {len(vcfg_final.get('redirects', []))}")
sm_final = read(sm_path)
print(f"  /insights/ URLs in sitemap: {sm_final.count('/insights/')}")

# Check a sample file
sample = os.path.join(BASE, "insights", "chatgpt", "chatgpt-for-law-firms.html")
if os.path.exists(sample):
    s = read(sample)
    can = re.search(r'<link rel="canonical" href="([^"]*)"', s)
    print(f"  Sample canonical: {can.group(1) if can else 'NOT FOUND'}")

print("\n✅ Migration complete")
