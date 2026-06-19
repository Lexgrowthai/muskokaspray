#!/usr/bin/env python3
"""
clean_urls.py — Switch entire site to clean URLs (no .html extension).

Changes:
  1. vercel.json: cleanUrls: false → true
  2. All relative href="page.html" → href="page" in HTML files
  3. All canonical / og:url / twitter references: strip .html
  4. All JSON-LD url / @id / item fields: strip .html
  5. sitemap.xml: strip .html from every <loc>
  6. seo_helpers.py: update SITE slug handling note

Homepage canonical stays https://lexscale.ai (no change needed).
"""

import re, os, json, glob

BASE = os.path.dirname(os.path.abspath(__file__))

def read(f):   return open(os.path.join(BASE, f), encoding="utf-8").read()
def write(f, c):
    open(os.path.join(BASE, f), "w", encoding="utf-8").write(c)
    return True

changed = []

# ─── helpers ──────────────────────────────────────────────────────────────────

def strip_html_ext(s):
    """Remove .html from the END of a URL path segment."""
    return re.sub(r'\.html\b', '', s)

def clean_relative_hrefs(html):
    """Convert href="page.html" → href="page" for relative (non-http) links."""
    def replace(m):
        href = m.group(1)
        # Skip: external URLs, anchors, mailto, non-html files
        if href.startswith(('http', 'mailto:', '#', '//')):
            return m.group(0)
        # Only strip from .html files
        if href.endswith('.html'):
            return f'href="{href[:-5]}"'
        return m.group(0)
    return re.sub(r'href="([^"]*)"', replace, html)

def clean_absolute_lexscale_urls(html):
    """Strip .html from all https://lexscale.ai/... URLs (canonical, OG, JSON-LD)."""
    return re.sub(r'(https://lexscale\.ai/[^"<\s]*)\.html\b', r'\1', html)

def clean_action_urls(html):
    """Fix any form action="page.html" relative refs."""
    def replace(m):
        val = m.group(1)
        if not val.startswith('http') and val.endswith('.html'):
            return f'action="{val[:-5]}"'
        return m.group(0)
    return re.sub(r'action="([^"]*)"', replace, html)

# ─── 1. vercel.json ───────────────────────────────────────────────────────────
print("[1/4] Updating vercel.json ...")
vcfg = json.loads(read("vercel.json"))
vcfg["cleanUrls"] = True
write("vercel.json", json.dumps(vcfg, indent=2) + "\n")
changed.append("vercel.json")
print("  ✓ cleanUrls: true")

# ─── 2 & 3 & 4. All HTML files ────────────────────────────────────────────────
print("\n[2/4] Patching all HTML files ...")
html_files = sorted(glob.glob(os.path.join(BASE, "*.html")))
html_changed = 0

for fpath in html_files:
    fname = os.path.basename(fpath)
    original = read(fname)
    html = original

    # Relative hrefs: href="page.html" → href="page"
    html = clean_relative_hrefs(html)

    # Absolute lexscale.ai URLs (canonical, og:url, twitter, JSON-LD)
    html = clean_absolute_lexscale_urls(html)

    # Form actions (contact.html form action)
    html = clean_action_urls(html)

    if html != original:
        write(fname, html)
        html_changed += 1
        changed.append(fname)

print(f"  → {html_changed} HTML files updated")

# ─── 4. sitemap.xml ───────────────────────────────────────────────────────────
print("\n[3/4] Updating sitemap.xml ...")
sm = read("sitemap.xml")
sm_new = re.sub(r'(https://lexscale\.ai/[^<]*)\.html', r'\1', sm)
if sm_new != sm:
    write("sitemap.xml", sm_new)
    changed.append("sitemap.xml")
    locs_fixed = sm.count('.html')
    print(f"  ✓ {locs_fixed} URLs cleaned")
else:
    print("  — no changes needed")

# ─── 5. seo_helpers.py — update head_block slug note + FOOTER hrefs ───────────
print("\n[4/4] Updating seo_helpers.py ...")
sh = read("seo_helpers.py")
sh_new = sh

# Strip .html from all relative href strings inside NAV / FOOTER constants
# These are in triple-quoted strings — same regex works
sh_new = re.sub(r'href="([a-z][^"]*?)\.html"', lambda m: f'href="{m.group(1)}"', sh_new)

# Strip .html from lexscale.ai absolute URLs
sh_new = re.sub(r'(https://lexscale\.ai/[^"<\s]*)\.html\b', r'\1', sh_new)

# Update the head_block docstring slug example
sh_new = sh_new.replace(
    'slug="filename.html",          # e.g. "ai-seo-for-law-firms.html"; "" for homepage',
    'slug="ai-seo-for-law-firms",   # slug WITHOUT .html (e.g. "about", "ai-seo-for-law-firms"); "" for homepage'
)

# Update the assert/canonical builder — strip .html if accidentally passed
# Add a normalise step to head_block
old_canonical_line = '    canonical = SITE if not slug else f"{SITE}/{slug}"'
new_canonical_line = '    slug = slug.removesuffix(".html")  # tolerate either form\n    canonical = SITE if not slug else f"{SITE}/{slug}"'
sh_new = sh_new.replace(old_canonical_line, new_canonical_line, 1)

if sh_new != sh:
    write("seo_helpers.py", sh_new)
    changed.append("seo_helpers.py")
    print("  ✓ seo_helpers.py updated")
else:
    print("  — no changes needed")

# ─── Verify ───────────────────────────────────────────────────────────────────
print("\n=== Verification ===")
remaining = 0
for fpath in glob.glob(os.path.join(BASE, "*.html")):
    html = open(fpath).read()
    # .html in hrefs/canonicals/og tags (not in comments or stylesheet links)
    hits = re.findall(r'(?:href|content|canonical)="[^"]*\.html"', html)
    # Exclude external non-lexscale hrefs (e.g. fonts.googleapis.com is not .html anyway)
    for h in hits:
        if 'lexscale' in h or not h.startswith('href="http'):
            remaining += 1

sm_remaining = read("sitemap.xml").count('.html')
print(f"  .html remaining in HTML link attributes: {remaining}")
print(f"  .html remaining in sitemap.xml:          {sm_remaining}")
print(f"  vercel.json cleanUrls: {json.loads(read('vercel.json'))['cleanUrls']}")

print(f"\n✅ Done. {len(changed)} files modified.")
