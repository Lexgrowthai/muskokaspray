#!/usr/bin/env python3
"""Patch 30 root-level pages missing robots, OG/Twitter tags, and BreadcrumbList schema."""
import os, re, json

BASE = '/home/user/muskokaspray'
SITE = 'https://lexscale.ai'

# Map slug → (parent_label, parent_url) for breadcrumbs
PARENTS = {
    # AI Chatbot cluster
    'ai-chatbot-for-law-firm-website': ('AI Chatbot for Law Firms', f'{SITE}/ai-chatbot-for-law-firms'),
    'ai-chatbot-intake-qualification': ('AI Chatbot for Law Firms', f'{SITE}/ai-chatbot-for-law-firms'),
    'ai-chatbot-roi-for-law-firms': ('AI Chatbot for Law Firms', f'{SITE}/ai-chatbot-for-law-firms'),
    'ai-chatbot-vs-live-chat-lawyers': ('AI Chatbot for Law Firms', f'{SITE}/ai-chatbot-for-law-firms'),
    'ai-chatbots': ('Home', SITE),
    'how-ai-chatbots-convert-legal-leads': ('AI Chatbot for Law Firms', f'{SITE}/ai-chatbot-for-law-firms'),

    # AI Receptionist cluster
    'ai-receptionist-intake-automation': ('AI Receptionist for Law Firms', f'{SITE}/ai-receptionist-for-law-firms'),
    'ai-receptionist-vs-human-receptionist': ('AI Receptionist for Law Firms', f'{SITE}/ai-receptionist-for-law-firms'),
    'ai-receptionists': ('Home', SITE),
    'how-ai-receptionists-increase-law-firm-revenue': ('AI Receptionist for Law Firms', f'{SITE}/ai-receptionist-for-law-firms'),
    'never-miss-a-call-law-firm': ('AI Receptionist for Law Firms', f'{SITE}/ai-receptionist-for-law-firms'),
    'what-is-an-ai-receptionist-for-law-firms': ('AI Receptionist for Law Firms', f'{SITE}/ai-receptionist-for-law-firms'),

    # AI SEO cluster
    'ai-seo-for-law-firms-complete-guide': ('AI SEO for Law Firms', f'{SITE}/ai-seo-for-law-firms'),
    'ai-seo-vs-traditional-seo-lawyers': ('AI SEO for Law Firms', f'{SITE}/ai-seo-for-law-firms'),
    'ai-seo': ('Home', SITE),
    'how-google-ai-overviews-affect-law-firms': ('AI SEO for Law Firms', f'{SITE}/ai-seo-for-law-firms'),
    'local-ai-seo-for-law-firms': ('AI SEO for Law Firms', f'{SITE}/ai-seo-for-law-firms'),

    # AI Website cluster
    'ai-website-design-for-law-firms-guide': ('AI Website Design', f'{SITE}/ai-website-design-for-law-firms'),
    'ai-websites': ('Home', SITE),
    'law-firm-website-conversion-optimization': ('AI Website Design', f'{SITE}/ai-website-design-for-law-firms'),
    'law-firm-website-seo-structure': ('AI Website Design', f'{SITE}/ai-website-design-for-law-firms'),
    'law-firm-website-speed-performance': ('AI Website Design', f'{SITE}/ai-website-design-for-law-firms'),
    'mobile-first-law-firm-website': ('AI Website Design', f'{SITE}/ai-website-design-for-law-firms'),

    # Entity SEO cluster
    'attorney-knowledge-panel-optimization': ('AI SEO for Law Firms', f'{SITE}/ai-seo-for-law-firms'),
    'entity-seo-vs-keyword-seo': ('AI SEO for Law Firms', f'{SITE}/ai-seo-for-law-firms'),
    'entity-seo': ('Home', SITE),
    'local-business-schema-law-firms': ('AI SEO for Law Firms', f'{SITE}/ai-seo-for-law-firms'),
    'schema-markup-for-lawyers-guide': ('AI SEO for Law Firms', f'{SITE}/ai-seo-for-law-firms'),
    'topical-authority-for-law-firms': ('AI SEO for Law Firms', f'{SITE}/ai-seo-for-law-firms'),
    'what-is-entity-seo-for-law-firms': ('AI SEO for Law Firms', f'{SITE}/ai-seo-for-law-firms'),
}

FAILING = list(PARENTS.keys())

ROBOTS = '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"/>'
OG_IMAGE = f'<meta property="og:image" content="{SITE}/og-image.png"/>'
OG_SITENAME = '<meta property="og:site_name" content="LexScale.ai"/>'

patched = 0
errors = []

for slug in FAILING:
    fname = slug + '.html'
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        errors.append(f"NOT FOUND: {fname}")
        continue

    with open(path) as f:
        html = f.read()

    # Extract existing title for breadcrumb name
    title_m = re.search(r'<title>(.*?)\s*\|\s*LexScale\.ai</title>', html)
    page_name = title_m.group(1).strip() if title_m else slug.replace('-', ' ').title()

    # Extract existing og:description for twitter
    og_desc_m = re.search(r'<meta property="og:description" content="([^"]+)"', html)
    og_desc = og_desc_m.group(1) if og_desc_m else ''

    # Extract existing title value for twitter
    og_title_m = re.search(r'<meta property="og:title" content="([^"]+)"', html)
    og_title = og_title_m.group(1) if og_title_m else page_name

    # Canonical URL (clean, no .html)
    page_url = f"{SITE}/{slug}"

    # Fix canonical if it has .html
    html = re.sub(
        r'<link rel="canonical" href="https://lexscale\.ai/[^"]*\.html"/>',
        f'<link rel="canonical" href="{page_url}"/>',
        html
    )

    # ── robots meta ──
    if 'name="robots"' not in html:
        html = html.replace(
            '<link rel="canonical"',
            f'{ROBOTS}\n<link rel="canonical"'
        )

    # ── og:url, og:image, og:site_name (insert after og:type if present, else after og:description) ──
    if 'og:url' not in html:
        og_url_tag = f'<meta property="og:url" content="{page_url}"/>'
        # Insert after og:type or og:description
        for after_tag in ['og:type"', 'og:description"']:
            m = re.search(rf'<meta property="{after_tag}[^>]*/>', html)
            if m:
                html = html[:m.end()] + f'\n{og_url_tag}' + html[m.end():]
                break

    if 'og:image' not in html:
        # Insert after og:url
        m = re.search(r'<meta property="og:url"[^>]*/>', html)
        if m:
            html = html[:m.end()] + f'\n{OG_IMAGE}' + html[m.end():]

    if 'og:site_name' not in html:
        m = re.search(r'<meta property="og:image"[^>]*/>', html)
        if m:
            html = html[:m.end()] + f'\n{OG_SITENAME}' + html[m.end():]

    # ── twitter tags ──
    if 'twitter:card' not in html:
        tw_block = (
            f'<meta name="twitter:card" content="summary_large_image"/>\n'
            f'<meta name="twitter:title" content="{og_title}"/>\n'
            f'<meta name="twitter:description" content="{og_desc}"/>\n'
            f'<meta name="twitter:image" content="{SITE}/og-image.png"/>'
        )
        # Insert after og:site_name or before fonts link
        m = re.search(r'<meta property="og:site_name"[^>]*/>', html)
        if m:
            html = html[:m.end()] + f'\n{tw_block}' + html[m.end():]
        else:
            html = html.replace('<link href="https://fonts.googleapis', f'{tw_block}\n<link href="https://fonts.googleapis', 1)

    # ── BreadcrumbList schema ──
    if 'BreadcrumbList' not in html:
        parent_label, parent_url = PARENTS.get(slug, ('Home', SITE))

        if parent_label == 'Home':
            # 2-level breadcrumb
            bc = {
                "@context": "https://schema.org",
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE},
                    {"@type": "ListItem", "position": 2, "name": page_name, "item": page_url}
                ]
            }
        else:
            # 3-level breadcrumb
            bc = {
                "@context": "https://schema.org",
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE},
                    {"@type": "ListItem", "position": 2, "name": parent_label, "item": parent_url},
                    {"@type": "ListItem", "position": 3, "name": page_name, "item": page_url}
                ]
            }

        bc_script = f'<script type="application/ld+json">{json.dumps(bc, ensure_ascii=False)}</script>'

        # Insert after existing JSON-LD block(s)
        last_ld = list(re.finditer(r'</script>', html))
        # Find last JSON-LD closing tag
        ld_closes = [m for m in re.finditer(r'</script>', html)
                     if 'application/ld+json' in html[max(0, m.start()-500):m.start()]]
        if ld_closes:
            ins = ld_closes[-1].end()
            html = html[:ins] + f'\n{bc_script}' + html[ins:]
        else:
            html = html.replace('</head>', f'{bc_script}\n</head>', 1)

    with open(path, 'w') as f:
        f.write(html)

    patched += 1
    print(f"✓ {fname}")

print(f"\nPatched {patched}/{len(FAILING)} files")
if errors:
    print("ERRORS:", errors)
