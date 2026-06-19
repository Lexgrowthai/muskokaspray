#!/usr/bin/env python3
"""
seo_upgrade.py — Comprehensive SEO architecture upgrade for all LexScale.ai pages.
Patches metadata, JSON-LD structured data, and generates sitemap.xml + robots.txt.
"""

import re, os

SITE = "https://lexscale.ai"
OG_IMG = "https://lexscale.ai/og-image.png"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def read(f):
    with open(os.path.join(BASE_DIR, f), encoding="utf-8") as fh:
        return fh.read()

def write(f, content):
    with open(os.path.join(BASE_DIR, f), "w", encoding="utf-8") as fh:
        fh.write(content)
    print(f"  ✓ {f}")

def inject_after_viewport(html, snippet):
    """Insert snippet right after the viewport meta tag."""
    pattern = r'(<meta name="viewport"[^/]*/?>)'
    if re.search(pattern, html):
        return re.sub(pattern, r'\1\n' + snippet, html, count=1)
    # fallback: after <head>
    return re.sub(r'(<head[^>]*>)', r'\1\n' + snippet, html, count=1)

def replace_or_inject_title(html, new_title):
    if re.search(r'<title>', html):
        return re.sub(r'<title>[^<]*</title>', f'<title>{new_title}</title>', html, count=1)
    return inject_after_viewport(html, f'<title>{new_title}</title>')

def remove_existing_meta_tags(html, names):
    """Remove existing meta/link tags to avoid duplication before re-injecting."""
    for name in names:
        # property meta (og:*)
        html = re.sub(rf'<meta\s+property="{re.escape(name)}"[^>]*/?>[\s]*', '', html)
        # name meta (twitter:*, description, etc.)
        html = re.sub(rf'<meta\s+name="{re.escape(name)}"[^>]*/?>[\s]*', '', html)
    return html

def remove_existing_canonical(html):
    html = re.sub(r'<link\s+rel="canonical"[^>]*/?>[\s]*', '', html)
    return html

def remove_existing_robots(html):
    html = re.sub(r'<meta\s+name="robots"[^>]*/?>[\s]*', '', html)
    return html

def remove_existing_ld_json(html):
    """Remove all existing ld+json blocks so we can re-inject clean ones."""
    html = re.sub(r'<script\s+type="application/ld\+json"[^>]*>.*?</script>\s*', '', html, flags=re.DOTALL)
    return html

def build_meta_block(title, description, keywords, canonical, og_type="website", schemas=None):
    """Build a complete SEO meta block."""
    kw_line = f'\n<meta name="keywords" content="{keywords}"/>' if keywords else ''
    schema_lines = ''
    if schemas:
        for s in schemas:
            schema_lines += f'\n<script type="application/ld+json">{s}</script>'
    return f'''<title>{title}</title>
<meta name="description" content="{description}"/>{kw_line}
<link rel="canonical" href="{canonical}"/>
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"/>
<meta property="og:type" content="{og_type}"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{description}"/>
<meta property="og:url" content="{canonical}"/>
<meta property="og:image" content="{OG_IMG}"/>
<meta property="og:site_name" content="LexScale.ai"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{title}"/>
<meta name="twitter:description" content="{description}"/>
<meta name="twitter:image" content="{OG_IMG}"/>{schema_lines}'''

def patch_page(filename, title, description, keywords, slug, og_type="website", schemas=None):
    """Full patch: replace title + inject all SEO meta after viewport."""
    html = read(filename)

    # Remove existing duplicate tags
    html = remove_existing_meta_tags(html, [
        'description','keywords','robots',
        'og:type','og:title','og:description','og:url','og:image','og:site_name',
        'twitter:card','twitter:title','twitter:description','twitter:image',
    ])
    html = remove_existing_canonical(html)
    html = remove_existing_robots(html)
    html = remove_existing_ld_json(html)

    # Remove existing title so the block's title is the only one
    html = re.sub(r'<title>[^<]*</title>\s*', '', html)

    canonical = f"{SITE}/{slug}" if slug else SITE
    block = build_meta_block(title, description, keywords, canonical, og_type, schemas)

    # Inject after viewport meta
    vp_pattern = r'(<meta name="viewport"[^/]*/?>)'
    if re.search(vp_pattern, html):
        html = re.sub(vp_pattern, r'\1\n' + block, html, count=1)

    write(filename, html)

# ─── JSON-LD Schema helpers ───────────────────────────────────────────────────

def org_schema():
    return '''{
  "@context":"https://schema.org",
  "@type":"Organization",
  "@id":"https://lexscale.ai/#organization",
  "name":"LexScale.ai",
  "url":"https://lexscale.ai",
  "logo":"https://lexscale.ai/og-image.png",
  "description":"AI-powered growth systems exclusively for law firms. Helping attorneys rank on Google, appear in AI Overviews, and get cited by ChatGPT, Gemini, and Perplexity.",
  "foundingDate":"2013",
  "areaServed":{"@type":"Place","name":"United States and Canada"},
  "knowsAbout":["Law Firm Marketing","AI SEO","Legal Website Design","AI Receptionist for Law Firms","AI Chatbot for Law Firms","ChatGPT Visibility","Entity SEO"],
  "sameAs":["https://lexscale.ai"]
}'''

def website_schema():
    return '''{
  "@context":"https://schema.org",
  "@type":"WebSite",
  "@id":"https://lexscale.ai/#website",
  "name":"LexScale.ai",
  "url":"https://lexscale.ai",
  "description":"AI solutions exclusively for law firms — SEO, websites, receptionists, chatbots, and AI search visibility.",
  "publisher":{"@id":"https://lexscale.ai/#organization"},
  "potentialAction":{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https://lexscale.ai/?s={search_term_string}"},"query-input":"required name=search_term_string"}
}'''

def webpage_schema(name, desc, url, page_type="WebPage"):
    return f'''{{
  "@context":"https://schema.org",
  "@type":"{page_type}",
  "@id":"{url}#webpage",
  "name":"{name}",
  "description":"{desc}",
  "url":"{url}",
  "isPartOf":{{"@id":"https://lexscale.ai/#website"}},
  "publisher":{{"@id":"https://lexscale.ai/#organization"}}
}}'''

def breadcrumb_schema(items):
    elements = []
    for i, (name, url) in enumerate(items, 1):
        elements.append(f'''{{"@type":"ListItem","position":{i},"name":"{name}","item":"{url}"}}''')
    return f'''{{
  "@context":"https://schema.org",
  "@type":"BreadcrumbList",
  "itemListElement":[{",".join(elements)}]
}}'''

def service_schema(name, desc, url):
    return f'''{{
  "@context":"https://schema.org",
  "@type":"Service",
  "@id":"{url}#service",
  "name":"{name}",
  "description":"{desc}",
  "provider":{{"@id":"https://lexscale.ai/#organization"}},
  "url":"{url}",
  "areaServed":{{"@type":"Place","name":"United States and Canada"}},
  "audience":{{"@type":"Audience","name":"Law Firms and Attorneys"}}
}}'''

def article_schema(title, desc, url, date_pub):
    return f'''{{
  "@context":"https://schema.org",
  "@type":"Article",
  "@id":"{url}#article",
  "headline":"{title}",
  "description":"{desc}",
  "url":"{url}",
  "datePublished":"{date_pub}",
  "dateModified":"2026-06-19",
  "author":{{"@id":"https://lexscale.ai/#organization"}},
  "publisher":{{"@id":"https://lexscale.ai/#organization"}},
  "isPartOf":{{"@id":"https://lexscale.ai/#website"}}
}}'''

def collection_schema(name, desc, url):
    return f'''{{
  "@context":"https://schema.org",
  "@type":"CollectionPage",
  "@id":"{url}#webpage",
  "name":"{name}",
  "description":"{desc}",
  "url":"{url}",
  "isPartOf":{{"@id":"https://lexscale.ai/#website"}},
  "publisher":{{"@id":"https://lexscale.ai/#organization"}}
}}'''

def about_schema():
    return '''{
  "@context":"https://schema.org",
  "@type":"AboutPage",
  "@id":"https://lexscale.ai/about.html#webpage",
  "name":"About LexScale.ai — AI Growth Systems for Law Firms",
  "description":"LexScale.ai combines 10+ years of legal marketing experience with cutting-edge AI to help law firms rank on Google, appear in AI Overviews, and convert more clients.",
  "url":"https://lexscale.ai/about.html",
  "isPartOf":{"@id":"https://lexscale.ai/#website"},
  "publisher":{"@id":"https://lexscale.ai/#organization"}
}'''

# ─── 1. index.html ────────────────────────────────────────────────────────────
print("\n[1/8] Patching index.html ...")
patch_page(
    "index.html",
    title="LexScale.ai — AI Growth Systems for Law Firms",
    description="AI SEO, AI receptionists, AI chatbots, and AI website design built exclusively for law firms. Rank on Google, appear in AI Overviews, and get cited by ChatGPT, Gemini & Perplexity.",
    keywords="AI for law firms, law firm AI SEO, AI receptionist for attorneys, AI chatbot for lawyers, law firm website design, ChatGPT for law firms, legal AI marketing",
    slug="",
    og_type="website",
    schemas=[org_schema(), website_schema(), webpage_schema(
        "LexScale.ai — AI Growth Systems for Law Firms",
        "AI SEO, AI receptionists, AI chatbots, and AI website design built exclusively for law firms.",
        SITE
    )]
)

# ─── 2. about.html ────────────────────────────────────────────────────────────
print("\n[2/8] Patching about.html ...")
patch_page(
    "about.html",
    title="About LexScale.ai — AI Growth Systems Built for Law Firms",
    description="LexScale.ai combines 10+ years of legal marketing expertise with cutting-edge AI to help law firms rank on Google, appear in AI Overviews, and convert more clients.",
    keywords="about LexScale.ai, law firm AI marketing agency, legal marketing experts, AI growth for attorneys",
    slug="about.html",
    og_type="website",
    schemas=[
        about_schema(),
        org_schema(),
        breadcrumb_schema([("Home", SITE), ("About", f"{SITE}/about.html")])
    ]
)

# ─── 3. Service pages ─────────────────────────────────────────────────────────
print("\n[3/8] Patching service pages ...")

services = [
    {
        "file": "ai-website-design-for-law-firms.html",
        "title": "AI Website Design for Law Firms | LexScale.ai",
        "desc": "AI-powered law firm websites designed to rank on Google, appear in AI Overviews, and convert visitors into clients. Custom designs built for attorneys across North America.",
        "keywords": "AI website design for law firms, law firm website design, attorney website, legal website SEO, law firm web design agency",
        "slug": "ai-website-design-for-law-firms.html",
        "name": "AI Website Design for Law Firms",
    },
    {
        "file": "ai-seo-for-law-firms.html",
        "title": "AI SEO for Law Firms | Rank on Google & AI Overviews | LexScale.ai",
        "desc": "AI SEO built exclusively for law firms. Rank on Google, appear in AI Overviews, and get cited by ChatGPT, Gemini, and Perplexity. Legal SEO services across North America.",
        "keywords": "AI SEO for law firms, law firm SEO, attorney SEO, legal SEO services, Google rankings for lawyers, AI Overviews for law firms",
        "slug": "ai-seo-for-law-firms.html",
        "name": "AI SEO for Law Firms",
    },
    {
        "file": "ai-receptionist-for-law-firms.html",
        "title": "AI Receptionist for Law Firms | 24/7 Legal Intake | LexScale.ai",
        "desc": "Never miss a client call again. Our AI receptionist answers 24/7, qualifies leads, books consultations, and integrates with your practice management software.",
        "keywords": "AI receptionist for law firms, virtual receptionist for attorneys, legal intake automation, 24/7 answering service for lawyers",
        "slug": "ai-receptionist-for-law-firms.html",
        "name": "AI Receptionist for Law Firms",
    },
    {
        "file": "ai-chatbot-for-law-firms.html",
        "title": "AI Chatbot for Law Firms | Convert Website Visitors | LexScale.ai",
        "desc": "AI chatbots built for law firm websites. Qualify leads 24/7, answer legal questions, and book consultations automatically. Increase conversions without increasing staff.",
        "keywords": "AI chatbot for law firms, law firm chatbot, legal chatbot, attorney chatbot, AI lead generation for lawyers",
        "slug": "ai-chatbot-for-law-firms.html",
        "name": "AI Chatbot for Law Firms",
    },
]

for svc in services:
    url = f"{SITE}/{svc['slug']}"
    patch_page(
        svc["file"],
        title=svc["title"],
        description=svc["desc"],
        keywords=svc["keywords"],
        slug=svc["slug"],
        og_type="website",
        schemas=[
            webpage_schema(svc["name"], svc["desc"], url),
            service_schema(svc["name"], svc["desc"], url),
            breadcrumb_schema([("Home", SITE), (svc["name"], url)])
        ]
    )

# ─── 4. Hub pages ─────────────────────────────────────────────────────────────
print("\n[4/8] Patching hub pages ...")

hubs = [
    {
        "file": "chatgpt.html",
        "title": "ChatGPT for Law Firms — AI Visibility Guides | LexScale.ai",
        "desc": "The complete resource hub for law firms on ChatGPT visibility. Learn how to rank in ChatGPT, earn citations, and win clients from AI search — 12 expert guides.",
        "keywords": "ChatGPT for law firms, law firm ChatGPT visibility, AI search for attorneys, get cited by ChatGPT",
        "slug": "chatgpt.html",
        "name": "ChatGPT for Law Firms",
        "parent": None,
    },
    {
        "file": "google-gemini.html",
        "title": "Google Gemini for Law Firms — AI Visibility Hub | LexScale.ai",
        "desc": "How law firms can appear in Google Gemini AI responses. Guides on entity optimization, structured data, and AI Overviews for attorneys.",
        "keywords": "Google Gemini for law firms, Gemini AI for attorneys, law firm AI visibility, Google AI Overviews",
        "slug": "google-gemini.html",
        "name": "Google Gemini for Law Firms",
        "parent": None,
    },
    {
        "file": "perplexity.html",
        "title": "Perplexity AI for Law Firms — Visibility & Citations | LexScale.ai",
        "desc": "How law firms get cited and recommended by Perplexity AI. Guides on optimizing your firm's presence for AI-powered answer engines.",
        "keywords": "Perplexity AI for law firms, Perplexity citations for attorneys, AI answer engine optimization for lawyers",
        "slug": "perplexity.html",
        "name": "Perplexity AI for Law Firms",
        "parent": None,
    },
    {
        "file": "ai-seo.html",
        "title": "AI SEO for Law Firms — Strategy Hub | LexScale.ai",
        "desc": "Complete AI SEO strategy guides for law firms. Learn topical authority, entity SEO, local AI search, and how to rank in Google AI Overviews.",
        "keywords": "AI SEO for lawyers hub, law firm SEO strategy, entity SEO for attorneys, topical authority law firm",
        "slug": "ai-seo.html",
        "name": "AI SEO Strategy Hub",
        "parent": None,
    },
    {
        "file": "ai-receptionists.html",
        "title": "AI Receptionists for Law Firms — Complete Guide Hub | LexScale.ai",
        "desc": "Everything law firms need to know about AI receptionists. Guides on intake automation, revenue impact, 24/7 coverage, and choosing the right AI receptionist.",
        "keywords": "AI receptionist hub for law firms, legal intake automation guides, virtual receptionist for attorneys",
        "slug": "ai-receptionists.html",
        "name": "AI Receptionists for Law Firms Hub",
        "parent": None,
    },
    {
        "file": "ai-chatbots.html",
        "title": "AI Chatbots for Law Firms — Complete Guide Hub | LexScale.ai",
        "desc": "Everything law firms need to know about AI chatbots. Guides on lead conversion, intake qualification, ROI, and choosing the right chatbot for your practice.",
        "keywords": "AI chatbot hub for law firms, law firm chatbot guides, legal lead generation chatbot",
        "slug": "ai-chatbots.html",
        "name": "AI Chatbots for Law Firms Hub",
        "parent": None,
    },
    {
        "file": "entity-seo.html",
        "title": "Entity SEO for Law Firms — Knowledge Graph & AI Visibility Hub | LexScale.ai",
        "desc": "Master entity SEO for law firms. Guides on schema markup, knowledge panels, structured data, and entity optimization to rank in Google and AI search engines.",
        "keywords": "entity SEO for law firms, knowledge graph for lawyers, schema markup for attorneys, structured data legal",
        "slug": "entity-seo.html",
        "name": "Entity SEO for Law Firms Hub",
        "parent": None,
    },
    {
        "file": "ai-websites.html",
        "title": "AI Website Design for Law Firms — Strategy Hub | LexScale.ai",
        "desc": "Complete guides on AI-powered law firm websites. Learn conversion optimization, SEO structure, speed performance, and mobile-first design for attorneys.",
        "keywords": "AI website design hub for law firms, law firm website guides, attorney website SEO, legal website conversion",
        "slug": "ai-websites.html",
        "name": "AI Websites for Law Firms Hub",
        "parent": None,
    },
]

for hub in hubs:
    url = f"{SITE}/{hub['slug']}"
    breadcrumbs = [("Home", SITE), (hub["name"], url)]
    patch_page(
        hub["file"],
        title=hub["title"],
        description=hub["desc"],
        keywords=hub["keywords"],
        slug=hub["slug"],
        og_type="website",
        schemas=[
            collection_schema(hub["name"], hub["desc"], url),
            breadcrumb_schema(breadcrumbs)
        ]
    )

# ─── 5. Pre-existing ChatGPT/Gemini article pages ─────────────────────────────
print("\n[5/8] Patching pre-existing articles ...")

old_articles = [
    {
        "file": "chatgpt-for-law-firms.html",
        "title": "ChatGPT for Law Firms: Why Being Found on ChatGPT Matters | LexScale.ai",
        "desc": "Discover why ChatGPT visibility is essential for law firms. Learn how AI search is changing legal marketing and how to position your firm to be recommended by AI.",
        "keywords": "ChatGPT for law firms, law firm ChatGPT visibility, AI search legal marketing",
        "slug": "chatgpt-for-law-firms.html",
        "cat": "ChatGPT for Law Firms",
        "cat_slug": "chatgpt.html",
        "date": "2025-01-10",
    },
    {
        "file": "google-gemini-for-law-firms.html",
        "title": "Google Gemini for Law Firms: Get Recommended by Google AI | LexScale.ai",
        "desc": "How law firms can appear in Google Gemini AI responses. Optimize your firm's entity presence, structured data, and content to rank in Google's AI search.",
        "keywords": "Google Gemini for law firms, law firm Gemini visibility, Google AI for attorneys",
        "slug": "google-gemini-for-law-firms.html",
        "cat": "Google Gemini for Law Firms",
        "cat_slug": "google-gemini.html",
        "date": "2025-01-12",
    },
    {
        "file": "why-chatgpt-matters-for-law-firms.html",
        "title": "Why ChatGPT Matters for Law Firms in 2025 | LexScale.ai",
        "desc": "ChatGPT now influences how potential clients find attorneys. Learn why law firms must optimize for AI recommendations and how to start today.",
        "keywords": "ChatGPT for lawyers, why ChatGPT matters law firms, AI search attorneys",
        "slug": "why-chatgpt-matters-for-law-firms.html",
        "cat": "ChatGPT for Law Firms",
        "cat_slug": "chatgpt.html",
        "date": "2025-01-15",
    },
    {
        "file": "how-chatgpt-finds-and-recommends-law-firms.html",
        "title": "How ChatGPT Finds and Recommends Law Firms | LexScale.ai",
        "desc": "Understand the mechanics behind ChatGPT law firm recommendations. Learn what signals ChatGPT uses to select and cite attorneys in its responses.",
        "keywords": "how ChatGPT recommends law firms, ChatGPT citations for lawyers, AI recommendations for attorneys",
        "slug": "how-chatgpt-finds-and-recommends-law-firms.html",
        "cat": "ChatGPT for Law Firms",
        "cat_slug": "chatgpt.html",
        "date": "2025-01-18",
    },
    {
        "file": "chatgpt-seo-for-lawyers.html",
        "title": "ChatGPT SEO for Lawyers: Optimize for AI Search | LexScale.ai",
        "desc": "A practical ChatGPT SEO guide for law firms. Optimize your content, structured data, and entity presence to earn citations and recommendations from ChatGPT.",
        "keywords": "ChatGPT SEO for lawyers, optimize law firm for ChatGPT, AI SEO attorneys",
        "slug": "chatgpt-seo-for-lawyers.html",
        "cat": "ChatGPT for Law Firms",
        "cat_slug": "chatgpt.html",
        "date": "2025-01-22",
    },
    {
        "file": "how-law-firms-can-rank-in-chatgpt.html",
        "title": "How Law Firms Can Rank in ChatGPT | LexScale.ai",
        "desc": "Step-by-step strategies for law firms to appear in ChatGPT responses. Build authority, earn citations, and position your firm as the AI-recommended choice.",
        "keywords": "rank in ChatGPT law firm, law firm ChatGPT ranking, appear in ChatGPT attorney",
        "slug": "how-law-firms-can-rank-in-chatgpt.html",
        "cat": "ChatGPT for Law Firms",
        "cat_slug": "chatgpt.html",
        "date": "2025-01-25",
    },
    {
        "file": "chatgpt-vs-google-search-for-lawyers.html",
        "title": "ChatGPT vs Google Search for Lawyers: Key Differences | LexScale.ai",
        "desc": "How ChatGPT and Google Search differ for law firm visibility. Understand how to optimize for both AI and traditional search to capture every client touchpoint.",
        "keywords": "ChatGPT vs Google for lawyers, AI search vs Google law firm, attorney search engine visibility",
        "slug": "chatgpt-vs-google-search-for-lawyers.html",
        "cat": "ChatGPT for Law Firms",
        "cat_slug": "chatgpt.html",
        "date": "2025-01-28",
    },
    {
        "file": "chatgpt-citations-explained.html",
        "title": "ChatGPT Citations Explained: How Law Firms Earn AI References | LexScale.ai",
        "desc": "What are ChatGPT citations and how do law firms earn them? Learn the exact signals and content strategies that get your firm cited as an authoritative source.",
        "keywords": "ChatGPT citations for law firms, earn ChatGPT citations attorney, AI citations legal",
        "slug": "chatgpt-citations-explained.html",
        "cat": "ChatGPT for Law Firms",
        "cat_slug": "chatgpt.html",
        "date": "2025-02-01",
    },
    {
        "file": "best-practices-optimizing-law-firm-websites-for-chatgpt.html",
        "title": "Best Practices for Optimizing Law Firm Websites for ChatGPT | LexScale.ai",
        "desc": "Proven best practices for making your law firm website ChatGPT-friendly. From structured data to content depth, learn what signals AI search engines reward.",
        "keywords": "optimize law firm website for ChatGPT, ChatGPT website optimization attorney, AI-friendly law firm website",
        "slug": "best-practices-optimizing-law-firm-websites-for-chatgpt.html",
        "cat": "ChatGPT for Law Firms",
        "cat_slug": "chatgpt.html",
        "date": "2025-02-05",
    },
    {
        "file": "common-mistakes-law-firms-make-with-ai-search.html",
        "title": "Common Mistakes Law Firms Make with AI Search | LexScale.ai",
        "desc": "Avoid the top AI search mistakes law firms make. From missing structured data to thin content, discover what's keeping your firm out of ChatGPT, Gemini, and Perplexity.",
        "keywords": "law firm AI search mistakes, ChatGPT mistakes for lawyers, AI visibility errors law firm",
        "slug": "common-mistakes-law-firms-make-with-ai-search.html",
        "cat": "ChatGPT for Law Firms",
        "cat_slug": "chatgpt.html",
        "date": "2025-02-08",
    },
    {
        "file": "how-ai-search-is-changing-legal-marketing.html",
        "title": "How AI Search Is Changing Legal Marketing | LexScale.ai",
        "desc": "AI search is reshaping how clients find law firms. Discover how ChatGPT, Gemini, and Perplexity are changing legal marketing and what smart firms are doing about it.",
        "keywords": "AI search changing legal marketing, ChatGPT legal marketing, AI impact on law firm marketing",
        "slug": "how-ai-search-is-changing-legal-marketing.html",
        "cat": "ChatGPT for Law Firms",
        "cat_slug": "chatgpt.html",
        "date": "2025-02-12",
    },
    {
        "file": "future-of-chatgpt-and-legal-marketing.html",
        "title": "The Future of ChatGPT and Legal Marketing | LexScale.ai",
        "desc": "Where is ChatGPT taking legal marketing? Explore emerging trends in AI search, what law firms must do to stay competitive, and how the landscape will evolve by 2026.",
        "keywords": "future of ChatGPT legal marketing, AI search future law firms, legal marketing trends 2025",
        "slug": "future-of-chatgpt-and-legal-marketing.html",
        "cat": "ChatGPT for Law Firms",
        "cat_slug": "chatgpt.html",
        "date": "2025-02-15",
    },
]

for art in old_articles:
    url = f"{SITE}/{art['slug']}"
    cat_url = f"{SITE}/{art['cat_slug']}"
    patch_page(
        art["file"],
        title=art["title"],
        description=art["desc"],
        keywords=art["keywords"],
        slug=art["slug"],
        og_type="article",
        schemas=[
            article_schema(art["title"], art["desc"], url, art["date"]),
            breadcrumb_schema([("Home", SITE), (art["cat"], cat_url), (art["title"].split("|")[0].strip(), url)])
        ]
    )

# ─── 6. New insight articles (25 files) ───────────────────────────────────────
print("\n[6/8] Patching 25 new insight articles ...")

new_articles = [
    # AI SEO category
    ("ai-seo-for-law-firms-complete-guide.html", "AI SEO for Law Firms: The Complete 2025 Guide | LexScale.ai", "The definitive guide to AI SEO for law firms. Learn how to rank on Google, appear in AI Overviews, and get cited by ChatGPT, Gemini, and Perplexity in 2025.", "AI SEO guide for law firms, law firm SEO 2025, AI search optimization attorneys", "ai-seo-for-law-firms-complete-guide.html", "AI SEO", "ai-seo.html", "2025-03-01"),
    ("ai-seo-vs-traditional-seo-lawyers.html", "AI SEO vs Traditional SEO for Lawyers: Key Differences | LexScale.ai", "How AI SEO differs from traditional SEO for law firms. Understand what changed, what still matters, and how to balance both strategies for maximum visibility.", "AI SEO vs traditional SEO lawyers, law firm SEO differences, AI search vs Google attorneys", "ai-seo-vs-traditional-seo-lawyers.html", "AI SEO", "ai-seo.html", "2025-03-05"),
    ("how-google-ai-overviews-affect-law-firms.html", "How Google AI Overviews Affect Law Firms | LexScale.ai", "Google AI Overviews are reshaping how potential clients find attorneys. Learn how to appear in AI Overviews and protect your firm's search visibility.", "Google AI Overviews for law firms, AI Overviews attorneys, SGE for lawyers", "how-google-ai-overviews-affect-law-firms.html", "AI SEO", "ai-seo.html", "2025-03-08"),
    ("topical-authority-for-law-firms.html", "Topical Authority for Law Firms: Rank Higher with Content Strategy | LexScale.ai", "Build topical authority that makes your law firm the go-to resource for AI and Google. Learn content clustering, silo architecture, and semantic SEO for attorneys.", "topical authority law firms, law firm content strategy, semantic SEO attorneys", "topical-authority-for-law-firms.html", "AI SEO", "ai-seo.html", "2025-03-12"),
    ("local-ai-seo-for-law-firms.html", "Local AI SEO for Law Firms: Dominate Your Market | LexScale.ai", "Local AI SEO strategies that help law firms dominate their geographic market. Optimize for local AI search, Google Business Profile, and geo-specific AI recommendations.", "local AI SEO law firms, local SEO for attorneys, law firm local search", "local-ai-seo-for-law-firms.html", "AI SEO", "ai-seo.html", "2025-03-15"),
    # AI Receptionists
    ("what-is-an-ai-receptionist-for-law-firms.html", "What Is an AI Receptionist for Law Firms? | LexScale.ai", "Everything law firms need to know about AI receptionists. What they do, how they work, and how they compare to traditional answering services for attorneys.", "what is AI receptionist law firm, AI receptionist for attorneys, virtual receptionist lawyers", "what-is-an-ai-receptionist-for-law-firms.html", "AI Receptionists", "ai-receptionists.html", "2025-03-18"),
    ("ai-receptionist-vs-human-receptionist.html", "AI Receptionist vs Human Receptionist for Law Firms | LexScale.ai", "Compare AI receptionists vs human receptionists for law firms. Cost, availability, accuracy, and client experience — which is right for your practice?", "AI receptionist vs human receptionist law firm, attorney receptionist comparison, legal intake AI vs human", "ai-receptionist-vs-human-receptionist.html", "AI Receptionists", "ai-receptionists.html", "2025-03-22"),
    ("how-ai-receptionists-increase-law-firm-revenue.html", "How AI Receptionists Increase Law Firm Revenue | LexScale.ai", "AI receptionists directly increase law firm revenue by capturing missed calls, qualifying leads 24/7, and booking more consultations. See the numbers.", "AI receptionist law firm revenue, attorney AI receptionist ROI, AI intake revenue for lawyers", "how-ai-receptionists-increase-law-firm-revenue.html", "AI Receptionists", "ai-receptionists.html", "2025-03-25"),
    ("never-miss-a-call-law-firm.html", "Never Miss a Client Call: AI Solutions for Law Firms | LexScale.ai", "Law firms miss up to 40% of calls. AI receptionists ensure every lead is captured 24/7. Learn how to stop losing clients to unanswered phones.", "never miss a call law firm, AI answering service for attorneys, 24/7 legal intake", "never-miss-a-call-law-firm.html", "AI Receptionists", "ai-receptionists.html", "2025-03-28"),
    ("ai-receptionist-intake-automation.html", "AI Receptionist & Intake Automation for Law Firms | LexScale.ai", "Automate your law firm's entire intake process with AI. From first call to booked consultation, AI receptionists handle qualification, scheduling, and CRM entry automatically.", "AI intake automation law firm, law firm intake automation, attorney intake AI", "ai-receptionist-intake-automation.html", "AI Receptionists", "ai-receptionists.html", "2025-04-01"),
    # AI Chatbots
    ("ai-chatbot-for-law-firm-website.html", "AI Chatbot for Law Firm Websites: Convert More Visitors | LexScale.ai", "Add an AI chatbot to your law firm website and convert more visitors into consultations. 24/7 lead qualification, appointment booking, and FAQ answering for attorneys.", "AI chatbot for law firm website, law firm website chatbot, attorney website chat", "ai-chatbot-for-law-firm-website.html", "AI Chatbots", "ai-chatbots.html", "2025-04-05"),
    ("how-ai-chatbots-convert-legal-leads.html", "How AI Chatbots Convert Legal Leads for Law Firms | LexScale.ai", "AI chatbots convert more legal website visitors into clients. Learn the exact strategies and chatbot flows that maximize lead conversion for law firms.", "AI chatbot convert legal leads, law firm chatbot conversion, attorney chatbot leads", "how-ai-chatbots-convert-legal-leads.html", "AI Chatbots", "ai-chatbots.html", "2025-04-08"),
    ("ai-chatbot-vs-live-chat-lawyers.html", "AI Chatbot vs Live Chat for Law Firms: Which Wins? | LexScale.ai", "AI chatbot vs live chat for lawyers — compare cost, availability, conversion rates, and client experience to find the best solution for your law firm.", "AI chatbot vs live chat lawyers, law firm chatbot comparison, attorney live chat vs AI", "ai-chatbot-vs-live-chat-lawyers.html", "AI Chatbots", "ai-chatbots.html", "2025-04-12"),
    ("ai-chatbot-intake-qualification.html", "AI Chatbot Intake & Lead Qualification for Law Firms | LexScale.ai", "Use AI chatbots to qualify legal leads before they reach your team. Automated intake questions, case screening, and lead scoring for law firms.", "AI chatbot intake qualification law firm, legal lead qualification chatbot, attorney intake chatbot", "ai-chatbot-intake-qualification.html", "AI Chatbots", "ai-chatbots.html", "2025-04-15"),
    ("ai-chatbot-roi-for-law-firms.html", "AI Chatbot ROI for Law Firms: Is It Worth It? | LexScale.ai", "Calculate the true ROI of an AI chatbot for your law firm. Revenue captured from missed leads, time saved on intake, and cost comparison vs. traditional live chat.", "AI chatbot ROI law firms, law firm chatbot return on investment, attorney chatbot value", "ai-chatbot-roi-for-law-firms.html", "AI Chatbots", "ai-chatbots.html", "2025-04-18"),
    # Entity SEO
    ("what-is-entity-seo-for-law-firms.html", "What Is Entity SEO for Law Firms? | LexScale.ai", "Entity SEO helps law firms build a strong presence in Google's Knowledge Graph and AI search engines. Learn what entity SEO is and why it matters for attorneys.", "entity SEO for law firms, what is entity SEO attorney, knowledge graph law firm", "what-is-entity-seo-for-law-firms.html", "Entity SEO", "entity-seo.html", "2025-04-22"),
    ("schema-markup-for-lawyers-guide.html", "Schema Markup for Lawyers: The Complete Guide | LexScale.ai", "Schema markup for law firms explained. Learn how to implement LegalService, Attorney, FAQPage, and BreadcrumbList schema to boost Google rankings and AI visibility.", "schema markup for lawyers, law firm schema markup, attorney structured data, legal JSON-LD", "schema-markup-for-lawyers-guide.html", "Entity SEO", "entity-seo.html", "2025-04-25"),
    ("attorney-knowledge-panel-optimization.html", "Attorney Knowledge Panel Optimization Guide | LexScale.ai", "How to claim, optimize, and maintain your law firm's Google Knowledge Panel. Build entity authority and appear as the trusted source in AI and Google search.", "attorney knowledge panel, law firm Google Knowledge Panel, attorney entity optimization", "attorney-knowledge-panel-optimization.html", "Entity SEO", "entity-seo.html", "2025-04-28"),
    ("local-business-schema-law-firms.html", "Local Business Schema for Law Firms: Complete Setup Guide | LexScale.ai", "Implement LocalBusiness and LegalService schema markup for your law firm to dominate local search, Google Maps, and AI-powered local recommendations.", "local business schema law firms, LegalService schema, law firm local SEO schema", "local-business-schema-law-firms.html", "Entity SEO", "entity-seo.html", "2025-05-01"),
    ("entity-seo-vs-keyword-seo.html", "Entity SEO vs Keyword SEO for Law Firms | LexScale.ai", "Entity SEO vs keyword SEO for law firms — which drives more clients? Learn how to combine both strategies for maximum Google and AI search visibility.", "entity SEO vs keyword SEO law firms, attorney SEO strategy, law firm entity vs keyword", "entity-seo-vs-keyword-seo.html", "Entity SEO", "entity-seo.html", "2025-05-05"),
    # AI Websites
    ("ai-website-design-for-law-firms-guide.html", "AI Website Design for Law Firms: The Complete Guide | LexScale.ai", "Everything law firms need to know about AI-powered website design. SEO architecture, conversion optimization, speed, and mobile design for attorneys.", "AI website design guide law firms, law firm website guide, attorney website design 2025", "ai-website-design-for-law-firms-guide.html", "AI Websites", "ai-websites.html", "2025-05-08"),
    ("law-firm-website-conversion-optimization.html", "Law Firm Website Conversion Optimization Guide | LexScale.ai", "Turn more website visitors into consultations with proven conversion optimization strategies for law firm websites. CTAs, trust signals, speed, and UX that converts.", "law firm website conversion optimization, attorney website conversion, legal website CRO", "law-firm-website-conversion-optimization.html", "AI Websites", "ai-websites.html", "2025-05-12"),
    ("law-firm-website-speed-performance.html", "Law Firm Website Speed & Performance Optimization | LexScale.ai", "Website speed directly impacts law firm rankings and conversions. Learn how to optimize your attorney website for Core Web Vitals, PageSpeed, and fast load times.", "law firm website speed, attorney website performance, legal website Core Web Vitals", "law-firm-website-speed-performance.html", "AI Websites", "ai-websites.html", "2025-05-15"),
    ("mobile-first-law-firm-website.html", "Mobile-First Law Firm Website Design Guide | LexScale.ai", "Most legal clients search on mobile. Learn how to build or optimize a mobile-first law firm website that ranks on Google and converts visitors into clients.", "mobile-first law firm website, mobile attorney website, law firm mobile SEO", "mobile-first-law-firm-website.html", "AI Websites", "ai-websites.html", "2025-05-18"),
    ("law-firm-website-seo-structure.html", "Law Firm Website SEO Structure: Architecture That Ranks | LexScale.ai", "Build a law firm website SEO structure that Google and AI search engines love. Silo architecture, internal linking, URL structure, and page hierarchy for attorneys.", "law firm website SEO structure, attorney website architecture, legal website SEO hierarchy", "law-firm-website-seo-structure.html", "AI Websites", "ai-websites.html", "2025-05-22"),
]

for art in new_articles:
    fname, title, desc, kw, slug, cat, cat_slug, date = art
    url = f"{SITE}/{slug}"
    cat_url = f"{SITE}/{cat_slug}"
    patch_page(
        fname,
        title=title,
        description=desc,
        keywords=kw,
        slug=slug,
        og_type="article",
        schemas=[
            article_schema(title, desc, url, date),
            breadcrumb_schema([("Home", SITE), (cat, cat_url), (title.split("|")[0].strip(), url)])
        ]
    )

# ─── 7. sitemap.xml ───────────────────────────────────────────────────────────
print("\n[7/8] Writing sitemap.xml ...")

all_pages = [
    # Core pages
    ("", "1.0", "weekly"),
    ("about.html", "0.8", "monthly"),
    # Service pages
    ("ai-website-design-for-law-firms.html", "0.9", "monthly"),
    ("ai-seo-for-law-firms.html", "0.9", "monthly"),
    ("ai-receptionist-for-law-firms.html", "0.9", "monthly"),
    ("ai-chatbot-for-law-firms.html", "0.9", "monthly"),
    # Hub pages
    ("chatgpt.html", "0.8", "weekly"),
    ("google-gemini.html", "0.8", "weekly"),
    ("perplexity.html", "0.8", "weekly"),
    ("ai-seo.html", "0.8", "weekly"),
    ("ai-receptionists.html", "0.8", "weekly"),
    ("ai-chatbots.html", "0.8", "weekly"),
    ("entity-seo.html", "0.8", "weekly"),
    ("ai-websites.html", "0.8", "weekly"),
    # Old articles
    ("chatgpt-for-law-firms.html", "0.7", "monthly"),
    ("google-gemini-for-law-firms.html", "0.7", "monthly"),
    ("why-chatgpt-matters-for-law-firms.html", "0.7", "monthly"),
    ("how-chatgpt-finds-and-recommends-law-firms.html", "0.7", "monthly"),
    ("chatgpt-seo-for-lawyers.html", "0.7", "monthly"),
    ("how-law-firms-can-rank-in-chatgpt.html", "0.7", "monthly"),
    ("chatgpt-vs-google-search-for-lawyers.html", "0.7", "monthly"),
    ("chatgpt-citations-explained.html", "0.7", "monthly"),
    ("best-practices-optimizing-law-firm-websites-for-chatgpt.html", "0.7", "monthly"),
    ("common-mistakes-law-firms-make-with-ai-search.html", "0.7", "monthly"),
    ("how-ai-search-is-changing-legal-marketing.html", "0.7", "monthly"),
    ("future-of-chatgpt-and-legal-marketing.html", "0.7", "monthly"),
    # New insight articles
    ("ai-seo-for-law-firms-complete-guide.html", "0.7", "monthly"),
    ("ai-seo-vs-traditional-seo-lawyers.html", "0.7", "monthly"),
    ("how-google-ai-overviews-affect-law-firms.html", "0.7", "monthly"),
    ("topical-authority-for-law-firms.html", "0.7", "monthly"),
    ("local-ai-seo-for-law-firms.html", "0.7", "monthly"),
    ("what-is-an-ai-receptionist-for-law-firms.html", "0.7", "monthly"),
    ("ai-receptionist-vs-human-receptionist.html", "0.7", "monthly"),
    ("how-ai-receptionists-increase-law-firm-revenue.html", "0.7", "monthly"),
    ("never-miss-a-call-law-firm.html", "0.7", "monthly"),
    ("ai-receptionist-intake-automation.html", "0.7", "monthly"),
    ("ai-chatbot-for-law-firm-website.html", "0.7", "monthly"),
    ("how-ai-chatbots-convert-legal-leads.html", "0.7", "monthly"),
    ("ai-chatbot-vs-live-chat-lawyers.html", "0.7", "monthly"),
    ("ai-chatbot-intake-qualification.html", "0.7", "monthly"),
    ("ai-chatbot-roi-for-law-firms.html", "0.7", "monthly"),
    ("what-is-entity-seo-for-law-firms.html", "0.7", "monthly"),
    ("schema-markup-for-lawyers-guide.html", "0.7", "monthly"),
    ("attorney-knowledge-panel-optimization.html", "0.7", "monthly"),
    ("local-business-schema-law-firms.html", "0.7", "monthly"),
    ("entity-seo-vs-keyword-seo.html", "0.7", "monthly"),
    ("ai-website-design-for-law-firms-guide.html", "0.7", "monthly"),
    ("law-firm-website-conversion-optimization.html", "0.7", "monthly"),
    ("law-firm-website-speed-performance.html", "0.7", "monthly"),
    ("mobile-first-law-firm-website.html", "0.7", "monthly"),
    ("law-firm-website-seo-structure.html", "0.7", "monthly"),
]

sitemap_lines = ['<?xml version="1.0" encoding="UTF-8"?>',
'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for slug, priority, freq in all_pages:
    url = SITE if not slug else f"{SITE}/{slug}"
    sitemap_lines.append(f'''  <url>
    <loc>{url}</loc>
    <lastmod>2026-06-19</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>''')
sitemap_lines.append('</urlset>')
write("sitemap.xml", "\n".join(sitemap_lines))

# ─── 8. robots.txt ────────────────────────────────────────────────────────────
print("\n[8/8] Writing robots.txt ...")
write("robots.txt", """User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: anthropic-ai
Allow: /

Sitemap: https://lexscale.ai/sitemap.xml
""")

print("\n✅ SEO upgrade complete!")
