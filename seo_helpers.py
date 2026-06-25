#!/usr/bin/env python3
"""
seo_helpers.py — Reusable SEO architecture for LexScale.ai static HTML site.

Import this module in any page-generation script. Every function here maps
directly to a requirement in CLAUDE.md. Never write inline schema or meta
tags in generator scripts — use these helpers instead.

Usage
-----
from seo_helpers import (
    head_block,          # complete <head> SEO block
    article_schema,      # JSON-LD for insight articles
    service_schema,      # JSON-LD for service pages
    faq_schema,          # JSON-LD FAQPage
    breadcrumb_schema,   # JSON-LD BreadcrumbList
    collection_schema,   # JSON-LD CollectionPage (hub pages)
    validate_page,       # audit a rendered HTML string
    add_to_sitemap,      # append a URL to sitemap.xml
    NAV, FOOTER, STICKY, MODAL, CSS,  # shared layout blocks
)
"""

import json, re, os, datetime

# ─── Site constants ────────────────────────────────────────────────────────────
SITE    = "https://lexscale.ai"
OG_IMG  = "https://lexscale.ai/og-image.png"
YEAR    = datetime.date.today().year
BRAND   = "LexScale.ai"
BASE    = os.path.dirname(os.path.abspath(__file__))

# ─── Schema builders ──────────────────────────────────────────────────────────

def _ld(obj: dict) -> str:
    """Render a dict as a <script type="application/ld+json"> block."""
    return f'<script type="application/ld+json">\n{json.dumps(obj, ensure_ascii=False, indent=2)}\n</script>'


def org_schema() -> str:
    return _ld({
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": f"{SITE}/#organization",
        "name": BRAND,
        "url": SITE,
        "logo": OG_IMG,
        "description": "AI-powered growth systems exclusively for law firms — AI SEO, websites, receptionists, and chatbots.",
        "foundingDate": "2013",
        "areaServed": [
            {"@type": "Country", "name": "United States"},
            {"@type": "Country", "name": "Canada"},
        ],
        "knowsAbout": [
            "Law Firm SEO", "AI Overviews Optimization",
            "ChatGPT Visibility for Attorneys", "Legal Website Design",
            "AI Receptionist", "Law Firm Lead Generation",
        ],
        "sameAs": [SITE],
    })


def website_schema() -> str:
    return _ld({
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": f"{SITE}/#website",
        "name": BRAND,
        "url": SITE,
        "publisher": {"@id": f"{SITE}/#organization"},
        "potentialAction": {
            "@type": "SearchAction",
            "target": {"@type": "EntryPoint", "urlTemplate": f"{SITE}/?s={{search_term_string}}"},
            "query-input": "required name=search_term_string",
        },
    })


def local_business_schema() -> str:
    return _ld({
        "@context": "https://schema.org",
        "@type": ["LocalBusiness", "ProfessionalService"],
        "@id": f"{SITE}/#localbusiness",
        "name": BRAND,
        "url": SITE,
        "logo": OG_IMG,
        "image": OG_IMG,
        "telephone": "+17059886026",
        "email": "info@lexscale.ai",
        "areaServed": [
            {"@type": "Country", "name": "United States"},
            {"@type": "Country", "name": "Canada"},
        ],
        "serviceType": [
            "AI SEO for Law Firms",
            "AI Website Design for Law Firms",
            "AI Receptionist for Law Firms",
            "AI Chatbot for Law Firms",
        ],
        "priceRange": "$$",
    })


def webpage_schema(name: str, desc: str, url: str, page_type: str = "WebPage") -> str:
    return _ld({
        "@context": "https://schema.org",
        "@type": page_type,
        "@id": f"{url}#webpage",
        "name": name,
        "description": desc,
        "url": url,
        "isPartOf": {"@id": f"{SITE}/#website"},
        "publisher": {"@id": f"{SITE}/#organization"},
    })


def breadcrumb_schema(items: list) -> str:
    """
    items = [("Home", "https://lexscale.ai"), ("Category", "..."), ("Page", "...")]
    """
    return _ld({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": url}
            for i, (name, url) in enumerate(items)
        ],
    })


def service_schema(name: str, desc: str, url: str) -> str:
    return _ld({
        "@context": "https://schema.org",
        "@type": "Service",
        "@id": f"{url}#service",
        "name": name,
        "description": desc,
        "provider": {"@id": f"{SITE}/#organization"},
        "url": url,
        "areaServed": [
            {"@type": "Country", "name": "United States"},
            {"@type": "Country", "name": "Canada"},
        ],
        "audience": {"@type": "Audience", "name": "Law Firms and Attorneys"},
    })


def article_schema(title: str, desc: str, url: str,
                   date_pub: str, date_mod: str = None) -> str:
    """
    date_pub / date_mod: ISO format strings e.g. "2025-03-01"
    """
    if date_mod is None:
        date_mod = datetime.date.today().isoformat()
    return _ld({
        "@context": "https://schema.org",
        "@type": "Article",
        "@id": f"{url}#article",
        "headline": title,
        "description": desc,
        "url": url,
        "datePublished": date_pub,
        "dateModified": date_mod,
        "author": {"@id": f"{SITE}/#organization"},
        "publisher": {"@id": f"{SITE}/#organization"},
        "isPartOf": {"@id": f"{SITE}/#website"},
        "image": OG_IMG,
    })


def faq_schema(pairs: list) -> str:
    """
    pairs = [("Question text", "Answer text"), ...]
    """
    return _ld({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in pairs
        ],
    })


def collection_schema(name: str, desc: str, url: str) -> str:
    return _ld({
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "@id": f"{url}#webpage",
        "name": name,
        "description": desc,
        "url": url,
        "isPartOf": {"@id": f"{SITE}/#website"},
        "publisher": {"@id": f"{SITE}/#organization"},
    })


def about_schema(desc: str) -> str:
    url = f"{SITE}/about"
    return _ld({
        "@context": "https://schema.org",
        "@type": "AboutPage",
        "@id": f"{url}#webpage",
        "name": f"About {BRAND}",
        "description": desc,
        "url": url,
        "isPartOf": {"@id": f"{SITE}/#website"},
        "publisher": {"@id": f"{SITE}/#organization"},
    })


# ─── head_block() ─────────────────────────────────────────────────────────────

def head_block(
    *,
    title: str,
    description: str,
    slug: str,            # e.g. "ai-seo-for-law-firms.html" or "" for homepage
    og_type: str = "website",
    keywords: str = "",
    schemas: list = None,  # list of pre-rendered <script> strings from helpers above
) -> str:
    """
    Returns a complete SEO <head> block (everything after <meta charset> and viewport).

    title       : 50–60 chars, keyword-first
    description : 140–155 chars
    slug        : path segment only. Empty string for homepage.
    schemas     : list of strings returned by schema helpers (org_schema(), etc.)

    The returned string is meant to replace/follow the viewport meta tag inside <head>.
    """
    assert len(title) <= 65,       f"Title too long ({len(title)}c): {title!r}"
    assert len(title) >= 20,       f"Title too short ({len(title)}c): {title!r}"
    assert len(description) <= 160, f"Description too long ({len(description)}c)"
    assert len(description) >= 100, f"Description too short ({len(description)}c)"

    slug = slug.removesuffix(".html")  # tolerate either form
    canonical = SITE if not slug else f"{SITE}/{slug}"
    kw_line   = f'\n<meta name="keywords" content="{keywords}"/>' if keywords else ""
    ld_blocks = "\n".join(schemas) if schemas else ""

    return f"""<title>{title}</title>
<meta name="description" content="{description}"/>{kw_line}
<link rel="canonical" href="{canonical}"/>
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"/>
<meta property="og:type" content="{og_type}"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{description}"/>
<meta property="og:url" content="{canonical}"/>
<meta property="og:image" content="{OG_IMG}"/>
<meta property="og:site_name" content="{BRAND}"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{title}"/>
<meta name="twitter:description" content="{description}"/>
<meta name="twitter:image" content="{OG_IMG}"/>
{ld_blocks}"""


# ─── validate_page() ──────────────────────────────────────────────────────────

def validate_page(html: str, filename: str = "?") -> list:
    """
    Audit a rendered HTML string and return a list of issue strings.
    An empty list means the page passes all checks.
    """
    issues = []

    def find(pat, flags=0): return re.search(pat, html, flags)
    def findall(pat, flags=0): return re.findall(pat, html, flags)

    # Title
    titles = findall(r'<title>([^<]*)</title>')
    if not titles:
        issues.append("MISSING <title>")
    elif len(titles) > 1:
        issues.append(f"DUPLICATE <title> ({len(titles)} found)")
    else:
        t = titles[0]
        if len(t) < 20: issues.append(f"Title too short ({len(t)}c): {t!r}")
        if len(t) > 65: issues.append(f"Title too long ({len(t)}c): {t!r}")

    # Description
    desc = find(r'<meta name="description" content="([^"]*)"')
    if not desc:
        issues.append("MISSING meta description")
    else:
        d = desc.group(1)
        if len(d) < 100: issues.append(f"Description too short ({len(d)}c)")
        if len(d) > 160: issues.append(f"Description too long ({len(d)}c)")

    # Canonical
    if not find(r'<link rel="canonical"'):
        issues.append("MISSING canonical URL")

    # Robots
    if not find(r'<meta name="robots"'):
        issues.append("MISSING robots meta")

    # OG tags
    for prop in ["og:title", "og:description", "og:url", "og:image", "og:site_name"]:
        if f'property="{prop}"' not in html:
            issues.append(f"MISSING {prop}")

    # Twitter tags
    for name in ["twitter:card", "twitter:title", "twitter:description", "twitter:image"]:
        if f'name="{name}"' not in html:
            issues.append(f"MISSING {name}")

    # H1
    h1s = findall(r'<h1(?:\s[^>]*)?>.*?</h1>', re.DOTALL)
    if not h1s:
        issues.append("NO <h1> found")
    elif len(h1s) > 1:
        issues.append(f"MULTIPLE <h1> ({len(h1s)} found)")

    # JSON-LD
    if 'application/ld+json' not in html:
        issues.append("NO JSON-LD schema")

    # BreadcrumbList (required on all non-homepage pages)
    # We skip this check for homepage (index.html or index)
    is_home = filename in ("index.html", "index", "")
    if '"BreadcrumbList"' not in html and not is_home:
        issues.append("MISSING BreadcrumbList schema")

    # Images without alt
    imgs_no_alt = [i for i in findall(r'<img([^>]*)>') if 'alt=' not in i]
    if imgs_no_alt:
        issues.append(f"{len(imgs_no_alt)} <img> tag(s) missing alt attribute")

    # Internal links — at least 2
    internal_links = findall(r'href="/[^"]*"') + findall(r'href="[a-z][^"]*"')
    if len(internal_links) < 5:
        issues.append(f"Too few internal links ({len(internal_links)}) — aim for ≥5")

    return issues


# ─── add_to_sitemap() ─────────────────────────────────────────────────────────

def add_to_sitemap(
    slug: str,
    priority: str = "0.7",
    changefreq: str = "monthly",
    lastmod: str = None,
) -> bool:
    """
    Append a new <url> entry to sitemap.xml if not already present.
    Returns True if added, False if it was already there.
    """
    if lastmod is None:
        lastmod = datetime.date.today().isoformat()

    url = SITE if not slug else f"{SITE}/{slug}"
    sitemap_path = os.path.join(BASE, "sitemap.xml")

    content = open(sitemap_path, encoding="utf-8").read()
    if f"<loc>{url}</loc>" in content:
        return False  # already present

    entry = f"""  <url>
    <loc>{url}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>"""

    new_content = content.replace("</urlset>", entry + "\n</urlset>")
    open(sitemap_path, "w", encoding="utf-8").write(new_content)
    return True


# ─── Shared layout blocks ─────────────────────────────────────────────────────
# These are the canonical versions — always import from here, never copy-paste.

NAV = """\
<nav>
  <a href="index" class="logo">Lex<span>Scale</span>.ai</a>
  <ul class="nav-links">
    <li><a href="index">Home</a></li>
    <li class="has-drop">
      <a href="#">Services
        <svg class="drop-arrow" viewBox="0 0 14 14" fill="none"><path d="M3 5l4 4 4-4" stroke="#4a5568" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
      <div class="dropdown">
        <a href="ai-website-design-for-law-firms" class="drop-item">
          <div class="drop-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg></div>
          <div><div class="drop-label">AI Website Design</div><div class="drop-sub">For law firms</div></div>
        </a>
        <a href="ai-seo-for-law-firms" class="drop-item">
          <div class="drop-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg></div>
          <div><div class="drop-label">AI SEO</div><div class="drop-sub">Rank higher, get cited by AI</div></div>
        </a>
        <a href="ai-receptionist-for-law-firms" class="drop-item">
          <div class="drop-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 8.81 19.79 19.79 0 01.1 2.18 2 2 0 012.08 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.91 7.91a16 16 0 006.16 6.16l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg></div>
          <div><div class="drop-label">AI Receptionist</div><div class="drop-sub">24/7 call answering</div></div>
        </a>
        <a href="ai-chatbot-for-law-firms" class="drop-item">
          <div class="drop-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg></div>
          <div><div class="drop-label">AI Chatbot</div><div class="drop-sub">Convert more website visitors</div></div>
        </a>
      </div>
    </li>
    <li class="has-drop">
      <a href="#">Insights
        <svg class="drop-arrow" viewBox="0 0 14 14" fill="none"><path d="M3 5l4 4 4-4" stroke="#4a5568" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
      <div class="dropdown">
        <a href="chatgpt" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div><div><div class="drop-label">ChatGPT for Law Firms</div><div class="drop-sub">12 articles</div></div></a>
        <a href="google-gemini" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#4285f4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg></div><div><div class="drop-label">Google Gemini</div><div class="drop-sub">For law firms</div></div></a>
        <a href="perplexity" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#20B8CD" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/></svg></div><div><div class="drop-label">Perplexity AI</div><div class="drop-sub">For law firms</div></div></a>
        <div class="drop-divider"></div>
        <a href="ai-seo" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg></div><div><div class="drop-label">AI SEO</div><div class="drop-sub">5 articles</div></div></a>
        <a href="ai-receptionists" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 8.81 19.79 19.79 0 01.1 2.18 2 2 0 012.08 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.91 7.91a16 16 0 006.16 6.16l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg></div><div><div class="drop-label">AI Receptionists</div><div class="drop-sub">5 articles</div></div></a>
        <a href="ai-chatbots" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div><div><div class="drop-label">AI Chatbots</div><div class="drop-sub">5 articles</div></div></a>
        <a href="entity-seo" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg></div><div><div class="drop-label">Entity SEO</div><div class="drop-sub">5 articles</div></div></a>
        <a href="ai-websites" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg></div><div><div class="drop-label">AI Websites</div><div class="drop-sub">5 articles</div></div></a>
      </div>
    </li>
    <li><a href="about">About</a></li>
    <li><a href="contact">Contact</a></li>
  </ul>
  <button class="nav-cta" onclick="document.getElementById('leadModal').style.display='flex'">Book A Demo</button>
  <button class="nav-mob" aria-label="Open menu" onclick="toggleMobNav(this)">
    <span></span><span></span><span></span>
  </button>
</nav>"""

FOOTER = f"""\
<footer>
  <div class="footer-inner">
    <div>
      <div class="footer-logo">Lex<span>Scale</span>.ai</div>
      <div class="footer-tagline">AI Growth Systems For Law Firms</div>
    </div>
    <div class="footer-links">
      <a href="ai-website-design-for-law-firms">AI Website Design</a>
      <a href="ai-seo-for-law-firms">AI SEO</a>
      <a href="ai-receptionist-for-law-firms">AI Receptionist</a>
      <a href="ai-chatbot-for-law-firms">AI Chatbot</a>
      <a href="about">About</a>
      <a href="contact">Contact</a>
      <a href="chatgpt-for-law-firms">Insights</a>
      <a href="resources">Resources</a>
      <a href="privacy">Privacy</a>
    </div>
    <div class="footer-copy">© {YEAR} LexScale.ai · All rights reserved</div>
  </div>
</footer>"""

STICKY = """\
<div class="sticky-cta">
  <p>Ready to grow your firm with AI?</p>
  <button onclick="document.getElementById('leadModal').style.display='flex'">Book a Free Strategy Call →</button>
</div>"""

MODAL = """\
<div id="leadModal" style="display:none;position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:1000;align-items:center;justify-content:center;padding:20px;">
  <div style="background:#fff;border-radius:24px;padding:40px;max-width:480px;width:100%;position:relative;">
    <button onclick="document.getElementById('leadModal').style.display='none'" style="position:absolute;top:16px;right:16px;background:none;border:none;font-size:22px;cursor:pointer;color:#94a3b8;">✕</button>
    <h3 style="font-size:22px;font-weight:800;color:#0B1536;margin-bottom:8px;">Book a Free Strategy Call</h3>
    <p style="font-size:14px;color:#64748b;margin-bottom:24px;">Tell us about your firm. We'll show you exactly how AI can help you grow.</p>
    <form name="lead" method="POST" action="/">
      <input type="text" name="name" placeholder="Your name" required style="width:100%;padding:12px 16px;border:1.5px solid rgba(11,21,54,.12);border-radius:10px;font-family:inherit;font-size:14px;margin-bottom:12px;outline:none;"/>
      <input type="email" name="email" placeholder="Work email" required style="width:100%;padding:12px 16px;border:1.5px solid rgba(11,21,54,.12);border-radius:10px;font-family:inherit;font-size:14px;margin-bottom:12px;outline:none;"/>
      <input type="text" name="firm" placeholder="Firm name" required style="width:100%;padding:12px 16px;border:1.5px solid rgba(11,21,54,.12);border-radius:10px;font-family:inherit;font-size:14px;margin-bottom:20px;outline:none;"/>
      <button type="submit" style="width:100%;background:linear-gradient(135deg,#6A5CFF,#8B7FFF);color:#fff;border:none;padding:14px;border-radius:100px;font-size:15px;font-weight:700;cursor:pointer;font-family:inherit;">Book My Strategy Call →</button>
    </form>
  </div>
</div>"""

# Canonical CSS (nav, footer, FAQ, article layout)
CSS = """\
*{margin:0;padding:0;box-sizing:border-box;}
:root{--navy:#0B1536;--pu:#6A5CFF;--pu2:#8B7FFF;--pu3:#a89fff;--gold:#D4AF37;--gold2:#F0C040;--gold3:#b8962e;}
body{font-family:'Inter',sans-serif;background:#fff;color:#0B1536;overflow-x:hidden;}
a{text-decoration:none;}
nav{position:sticky;top:0;z-index:100;display:flex;align-items:center;justify-content:space-between;padding:16px 40px;background:rgba(255,255,255,.93);backdrop-filter:blur(16px);border-bottom:1px solid rgba(106,92,255,.09);}
.logo{font-size:19px;font-weight:800;color:var(--navy);letter-spacing:-.4px;}
.logo span{color:var(--pu);}
.nav-links{display:flex;gap:26px;list-style:none;align-items:center;}
.nav-links a{font-size:13px;color:#4a5568;font-weight:500;transition:color .2s;}
.nav-links a:hover{color:var(--pu);}
.has-drop{position:relative;}
.has-drop>a{display:flex;align-items:center;gap:4px;cursor:pointer;}
.drop-arrow{width:14px;height:14px;opacity:.5;transition:transform .2s;}
.has-drop:hover .drop-arrow{transform:rotate(180deg);}
.dropdown{position:absolute;top:100%;left:50%;transform:translateX(-50%);background:#fff;border:1px solid rgba(106,92,255,.12);border-radius:16px;padding:12px 8px 8px;box-shadow:0 16px 48px rgba(11,21,54,.12);min-width:260px;opacity:0;pointer-events:none;visibility:hidden;transition:opacity .2s,visibility .2s;z-index:200;}
.has-drop:hover .dropdown{opacity:1;pointer-events:all;visibility:visible;}
.drop-item{display:flex;align-items:center;gap:10px;padding:10px 14px;border-radius:10px;transition:background .15s;}
.drop-item:hover{background:rgba(106,92,255,.07);}
.drop-ico{width:30px;height:30px;border-radius:8px;background:rgba(106,92,255,.1);display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.drop-label{font-size:12.5px;font-weight:600;color:var(--navy);}
.drop-sub{font-size:11px;color:#94a3b8;margin-top:1px;}
.drop-divider{height:1px;background:rgba(106,92,255,.07);margin:6px 8px;}
.nav-cta{background:var(--pu);color:#fff;border:none;padding:9px 20px;border-radius:100px;font-size:13px;font-weight:600;cursor:pointer;font-family:inherit;transition:all .2s;}
.nav-cta:hover{background:#5848e8;transform:translateY(-1px);}
footer{background:#0B1536;padding:48px 40px 32px;}
.footer-inner{max-width:1100px;margin:0 auto;display:flex;flex-direction:column;gap:28px;align-items:center;text-align:center;}
.footer-logo{font-size:18px;font-weight:800;color:#fff;letter-spacing:-.3px;}
.footer-logo span{color:var(--pu2);}
.footer-tagline{font-size:13px;color:rgba(255,255,255,.4);margin-top:4px;}
.footer-links{display:flex;flex-wrap:wrap;gap:20px;justify-content:center;}
.footer-links a{font-size:13px;color:rgba(255,255,255,.55);transition:color .2s;}
.footer-links a:hover{color:#fff;}
.footer-copy{font-size:12px;color:rgba(255,255,255,.3);}
.grid-bg{position:absolute;inset:0;background-image:linear-gradient(rgba(106,92,255,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(106,92,255,.04) 1px,transparent 1px);background-size:52px 52px;pointer-events:none;}
.tag{display:inline-flex;align-items:center;gap:7px;background:rgba(106,92,255,.08);border:1px solid rgba(106,92,255,.2);border-radius:100px;padding:6px 14px;margin-bottom:18px;}
.tag span{font-size:11px;font-weight:700;color:var(--pu);letter-spacing:.8px;text-transform:uppercase;}
.purple{color:var(--pu);}
.faq-list{display:flex;flex-direction:column;gap:0;margin:24px 0;}
.faq-item{border-bottom:1px solid rgba(106,92,255,.09);}
.faq-item:last-child{border-bottom:none;}
.faq-q{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:20px 0;cursor:pointer;font-size:15px;font-weight:700;color:var(--navy);line-height:1.4;}
.faq-q:hover{color:var(--pu);}
.faq-arrow{width:22px;height:22px;border-radius:50%;background:rgba(106,92,255,.08);display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:all .25s;}
.faq-item.open .faq-arrow{background:var(--pu);transform:rotate(180deg);}
.faq-a{font-size:14px;color:#4b5563;line-height:1.8;max-height:0;overflow:hidden;transition:max-height .35s ease,padding .35s;}
.faq-item.open .faq-a{max-height:400px;padding-bottom:20px;}
.sticky-cta{position:fixed;bottom:0;left:0;right:0;background:var(--navy);padding:14px 20px;display:flex;align-items:center;justify-content:center;gap:20px;z-index:90;border-top:1px solid rgba(106,92,255,.2);}
.sticky-cta p{font-size:14px;color:rgba(255,255,255,.7);margin:0;}
.sticky-cta button{background:var(--pu);color:#fff;border:none;padding:10px 22px;border-radius:100px;font-size:13px;font-weight:700;cursor:pointer;font-family:inherit;white-space:nowrap;}
.nav-mob{display:none;flex-direction:column;justify-content:center;gap:5px;background:none;border:none;cursor:pointer;padding:6px;z-index:101;flex-shrink:0;}
.nav-mob span{display:block;width:22px;height:2px;background:var(--navy);border-radius:2px;transition:transform .3s,opacity .3s;}
nav.mob-open .nav-mob span:nth-child(1){transform:translateY(7px) rotate(45deg);}
nav.mob-open .nav-mob span:nth-child(2){opacity:0;transform:scaleX(0);}
nav.mob-open .nav-mob span:nth-child(3){transform:translateY(-7px) rotate(-45deg);}
@media(max-width:768px){
  nav{padding:14px 20px;flex-wrap:wrap;gap:0;}
  .nav-links{display:none;flex-direction:column;gap:0;width:100%;order:3;background:#fff;border-top:1px solid rgba(106,92,255,.08);padding:8px 0 20px;margin-top:2px;}
  nav.mob-open .nav-links{display:flex;}
  .nav-links>li{width:100%;border-bottom:1px solid rgba(106,92,255,.06);}
  .nav-links>li:last-child{border-bottom:none;}
  .nav-links a{font-size:15px;font-weight:600;padding:13px 20px;display:block;width:100%;color:var(--navy);}
  .has-drop>a{display:flex;align-items:center;justify-content:space-between;padding:13px 20px;}
  .drop-arrow{margin-left:auto;transition:transform .25s;}
  .has-drop.mob-open .drop-arrow{transform:rotate(180deg);}
  .dropdown{position:static;transform:none;box-shadow:none;border:none;border-radius:0;background:rgba(106,92,255,.04);padding:4px 0 8px;min-width:unset;opacity:1;visibility:visible;pointer-events:all;display:none;transition:none;}
  .has-drop.mob-open .dropdown{display:block;}
  .drop-item{padding:10px 28px;}
  .drop-divider{margin:4px 20px;}
  .nav-cta{display:none;}
  .nav-mob{display:flex;}
  .sticky-cta{flex-direction:column;gap:10px;padding:16px;}
}"""

FAQ_JS = """\
<script>
function toggleFaq(el){
  const item=el.closest('.faq-item');
  const isOpen=item.classList.contains('open');
  document.querySelectorAll('.faq-item.open').forEach(i=>i.classList.remove('open'));
  if(!isOpen) item.classList.add('open');
}
function toggleMobNav(btn){
  const nav=btn.closest('nav');
  nav.classList.toggle('mob-open');
}
document.addEventListener('DOMContentLoaded',function(){
  /* Mobile sub-menu accordions */
  document.querySelectorAll('.has-drop>a').forEach(function(a){
    a.addEventListener('click',function(e){
      if(window.innerWidth>768)return;
      e.preventDefault();
      const li=a.closest('.has-drop');
      li.classList.toggle('mob-open');
    });
  });
  /* Close mobile menu on outside tap */
  document.addEventListener('click',function(e){
    const nav=document.querySelector('nav');
    if(nav&&nav.classList.contains('mob-open')&&!nav.contains(e.target)){
      nav.classList.remove('mob-open');
    }
  });
});
</script>"""


# ─── HTML page skeleton helpers ───────────────────────────────────────────────

def html_open(lang: str = "en") -> str:
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<style>
{CSS}
</style>"""


def html_close() -> str:
    return f"""{STICKY}
{MODAL}
{FAQ_JS}
</body>
</html>"""


def faq_html(pairs: list) -> str:
    """Render FAQ pairs as interactive HTML accordion."""
    items = ""
    for q, a in pairs:
        items += f"""
      <div class="faq-item">
        <div class="faq-q" onclick="toggleFaq(this)">{q}<div class="faq-arrow"><svg width="10" height="7" viewBox="0 0 10 7" fill="none"><path d="M1 1l4 4 4-4" stroke="#6A5CFF" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></div></div>
        <div class="faq-a">{a}</div>
      </div>"""
    return f'<div class="faq-list">{items}\n</div>'


# ─── Self-test ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("seo_helpers.py self-test")
    print("-" * 40)

    # Test head_block
    hb = head_block(
        title="AI SEO for Law Firms | Rank & Get Cited by AI",
        description="AI SEO built for law firms. Rank on Google, appear in AI Overviews, get cited by ChatGPT, Gemini, and Perplexity. Legal SEO across North America.",
        slug="ai-seo-for-law-firms",
        schemas=[
            webpage_schema("AI SEO for Law Firms", "...", f"{SITE}/ai-seo-for-law-firms"),
            service_schema("AI SEO for Law Firms", "...", f"{SITE}/ai-seo-for-law-firms"),
            breadcrumb_schema([("Home", SITE), ("AI SEO for Law Firms", f"{SITE}/ai-seo-for-law-firms")]),
        ]
    )
    print("head_block: OK")

    # Test validate_page with a minimal valid page
    sample = f"""<html><head>{hb}</head><body>
    {NAV}
    <h1>Test Page</h1>
    <h2>Section</h2>
    <p>Content <a href="about">about</a> <a href="contact">contact</a>
    <a href="ai-seo-for-law-firms">seo</a> <a href="/">home</a>
    <a href="ai-chatbot-for-law-firms">chatbot</a></p>
    {FOOTER}
    </body></html>"""

    issues = validate_page(sample, "test.html")
    if issues:
        print("Validation issues:", issues)
    else:
        print("validate_page: OK — no issues")

    print("\nAvailable exports:")
    exports = ["head_block","org_schema","website_schema","local_business_schema",
               "webpage_schema","breadcrumb_schema","service_schema","article_schema",
               "faq_schema","collection_schema","about_schema","validate_page",
               "add_to_sitemap","faq_html","html_open","html_close",
               "NAV","FOOTER","STICKY","MODAL","CSS","FAQ_JS",
               "SITE","OG_IMG","YEAR","BRAND"]
    for e in exports:
        print(f"  ✓ {e}")
