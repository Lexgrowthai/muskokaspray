# LexScale.ai — Developer Rules

## SEO IS NOT OPTIONAL

Every page created for this project must ship with complete backend SEO.
A page is not finished until both content AND technical SEO are done. No exceptions.

This is a **static HTML site** deployed on Vercel. There is no framework.
All pages are plain `.html` files in the root directory.

---

## Stack

| Thing | What it is |
|---|---|
| Pages | Plain `.html` files in `/` |
| Styles | Inline `<style>` blocks using CSS custom properties |
| Scripts | Inline `<script>` blocks |
| SEO helpers | `seo_helpers.py` — **always import from here** |
| Page generators | `expand_articles.py`, `gen_insight_silos.py` |
| Deployment | Vercel (`vercel.json`: `cleanUrls: true`, `trailingSlash: false`) |
| URLs | **No `.html` extension** in hrefs, canonicals, or sitemap (e.g. `/about`, not `about.html`) |

### CSS Custom Properties
```
--navy:  #0B1536
--pu:    #6A5CFF
--pu2:   #8B7FFF
--pu3:   #a89fff
--gold:  #D4AF37
--gold2: #F0C040
--gold3: #b8962e
```

---

## The SEO Helper Module

**`seo_helpers.py`** is the single source of truth for all SEO architecture.
Import from it. Never duplicate its code inline.

```python
from seo_helpers import (
    head_block,            # complete <head> SEO block
    article_schema,        # Article JSON-LD
    service_schema,        # Service JSON-LD
    faq_schema,            # FAQPage JSON-LD
    breadcrumb_schema,     # BreadcrumbList JSON-LD
    collection_schema,     # CollectionPage JSON-LD (hub pages)
    org_schema,            # Organization JSON-LD (homepage only)
    website_schema,        # WebSite JSON-LD (homepage only)
    local_business_schema, # LocalBusiness JSON-LD (homepage only)
    webpage_schema,        # WebPage JSON-LD
    validate_page,         # audit HTML string — returns list of issues
    add_to_sitemap,        # append URL to sitemap.xml
    faq_html,              # render FAQ pairs as accordion HTML
    html_open, html_close, # DOCTYPE+<style> open / sticky+modal+js close
    NAV, FOOTER,           # shared nav and footer blocks
    SITE, OG_IMG, YEAR, BRAND,  # constants
)
```

---

## Required on Every Page

### 1. `head_block()` — all metadata in one call

```python
from seo_helpers import head_block, webpage_schema, breadcrumb_schema, SITE

SEO = head_block(
    title="Keyword-First Title Here (50–60 chars)",
    description="Unique 140–155 character description with primary keyword.",
    slug="filename.html",      # "" for homepage
    og_type="website",         # "article" for insight posts
    keywords="kw1, kw2, kw3", # optional
    schemas=[
        webpage_schema(NAME, DESC, URL),
        breadcrumb_schema([("Home", SITE), ("Parent", PARENT_URL), (NAME, URL)]),
        # + page-type schema
    ],
)
```

This generates automatically:
- `<title>` (unique, 50–60 chars, keyword-first)
- `<meta name="description">` (unique, 140–155 chars)
- `<link rel="canonical">`
- `<meta name="robots" content="index, follow, max-snippet:-1, ...">`
- `og:type`, `og:title`, `og:description`, `og:url`, `og:image`, `og:site_name`
- `twitter:card`, `twitter:title`, `twitter:description`, `twitter:image`
- All JSON-LD `<script>` blocks passed in `schemas=[]`

### 2. Page Structure

```python
from seo_helpers import html_open, html_close, NAV, FOOTER

page = f"""{html_open()}
<head>
<link href="https://fonts.googleapis.com/...Inter..." rel="stylesheet"/>
{SEO}
</head>
<body>
{NAV}

<section>
  <h1>Primary Keyword Phrase</h1>   <!-- Exactly one H1 -->
</section>

<section>
  <h2>Section Heading</h2>           <!-- H2 for major sections -->
  <h3>Card or Subsection Title</h3>  <!-- H3 for items within sections -->
</section>

{FOOTER}
{html_close()}"""
```

### 3. Heading Hierarchy

- **Exactly one `<h1>`** — the primary keyword phrase
- **`<h2>`** for all major content sections
- **`<h3>`** for subsection headings or card titles
- Never skip levels (H1 → H3 without H2)

### 4. Internal Links

Every page must link to at least **5 related pages**:

| Page type | Required links |
|---|---|
| Service page | Home, About, Contact, 2+ other services, 2+ related articles |
| Insight article | Its category hub, 2+ related articles, 1+ service page |
| Hub/category page | All articles in the category, related services |

### 5. Image Alt Text

Every `<img>` must have descriptive `alt` text. Decorative images use `alt=""`.

### 6. sitemap.xml

Every new page must be added to `sitemap.xml` using `add_to_sitemap()`:

```python
from seo_helpers import add_to_sitemap
add_to_sitemap("new-page.html", priority="0.7", changefreq="monthly")
```

---

## Schema by Page Type

### Homepage (`index.html`)
```python
schemas=[
    org_schema(),
    website_schema(),
    local_business_schema(),
    webpage_schema(NAME, DESC, SITE),
]
```

### About Page
```python
schemas=[
    about_schema(DESC),
    org_schema(),
    breadcrumb_schema([("Home", SITE), ("About", f"{SITE}/about.html")]),
]
```

### Service Pages
```python
schemas=[
    webpage_schema(NAME, DESC, URL),
    service_schema(NAME, DESC, URL),
    breadcrumb_schema([("Home", SITE), (NAME, URL)]),
    faq_schema(FAQ_PAIRS),   # if page has FAQ section
]
```

### Insight Articles
```python
schemas=[
    article_schema(TITLE, DESC, URL, date_pub="2025-03-01"),
    breadcrumb_schema([("Home", SITE), (CATEGORY, CAT_URL), (TITLE, URL)]),
]
```

### Hub / Category Pages
```python
schemas=[
    collection_schema(NAME, DESC, URL),
    breadcrumb_schema([("Home", SITE), (NAME, URL)]),
]
```

---

## Page Template (copy-paste starting point)

```python
from seo_helpers import (
    head_block, html_open, html_close, NAV, FOOTER,
    webpage_schema, service_schema, breadcrumb_schema, faq_schema, faq_html,
    add_to_sitemap, validate_page,
    SITE,
)
import os

SLUG     = "new-page.html"
NAME     = "Page Title Here"
DESC     = "140–155 character meta description with primary keyword for law firms."
URL      = f"{SITE}/{SLUG}"
CAT      = "Services"
CAT_URL  = f"{SITE}/ai-seo-for-law-firms.html"

FAQ_PAIRS = [
    ("Question one?", "Answer one."),
    ("Question two?", "Answer two."),
]

SEO = head_block(
    title=f"{NAME} | LexScale.ai",
    description=DESC,
    slug=SLUG,
    og_type="website",
    schemas=[
        webpage_schema(NAME, DESC, URL),
        service_schema(NAME, DESC, URL),
        breadcrumb_schema([("Home", SITE), (CAT, CAT_URL), (NAME, URL)]),
        faq_schema(FAQ_PAIRS),
    ],
)

page = f"""{html_open()}
<head>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"/>
{SEO}
</head>
<body>
{NAV}

<section style="background:linear-gradient(135deg,#0B1536,#1a2456);padding:80px 24px;text-align:center;position:relative;overflow:hidden;">
  <div class="grid-bg"></div>
  <div style="position:relative;z-index:1;max-width:720px;margin:0 auto;">
    <div class="tag"><span>{CAT.upper()}</span></div>
    <h1 style="font-size:clamp(32px,4vw,52px);font-weight:900;color:#fff;letter-spacing:-1.5px;margin-bottom:16px;">
      {NAME}
    </h1>
    <p style="font-size:17px;color:rgba(255,255,255,.65);line-height:1.7;max-width:540px;margin:0 auto 32px;">
      {DESC}
    </p>
    <a href="contact.html" style="display:inline-block;background:linear-gradient(135deg,#6A5CFF,#8B7FFF);color:#fff;padding:14px 32px;border-radius:100px;font-size:15px;font-weight:700;">
      Book a Free Strategy Call →
    </a>
  </div>
</section>

<section style="padding:72px 24px;background:#fff;">
  <div style="max-width:1100px;margin:0 auto;">
    <h2 style="font-size:clamp(24px,2.8vw,36px);font-weight:800;color:#0B1536;letter-spacing:-.8px;margin-bottom:16px;">
      Section Heading
    </h2>
    <p style="font-size:16px;color:#374151;line-height:1.8;">Content here.</p>
    <p style="margin-top:24px;font-size:14px;color:#64748b;">
      Related: <a href="ai-seo-for-law-firms.html" style="color:#6A5CFF;">AI SEO for Law Firms</a> ·
      <a href="ai-chatbot-for-law-firms.html" style="color:#6A5CFF;">AI Chatbots</a> ·
      <a href="about.html" style="color:#6A5CFF;">About LexScale.ai</a>
    </p>
  </div>
</section>

<section style="padding:72px 24px;background:#f8f9fc;">
  <div style="max-width:760px;margin:0 auto;">
    <h2 style="font-size:28px;font-weight:800;color:#0B1536;text-align:center;margin-bottom:32px;">
      Frequently Asked Questions
    </h2>
    {faq_html(FAQ_PAIRS)}
  </div>
</section>

{FOOTER}
{html_close()}"""

issues = validate_page(page, SLUG)
assert not issues, f"SEO issues:\\n" + "\\n".join(issues)

open(os.path.join(os.path.dirname(__file__), SLUG), "w").write(page)
add_to_sitemap(SLUG, priority="0.7", changefreq="monthly")
print(f"✓ {SLUG} written and added to sitemap")
```

---

## Validation Checklist

Run `validate_page(html, filename)` before writing every file. It checks:

| Check | Requirement |
|---|---|
| `<title>` | Exactly one, 20–65 chars |
| Meta description | Present, 100–160 chars |
| Canonical URL | Present |
| Robots meta | Present |
| OG tags | `og:title`, `og:description`, `og:url`, `og:image`, `og:site_name` |
| Twitter tags | `twitter:card`, `twitter:title`, `twitter:description`, `twitter:image` |
| H1 | Exactly one |
| JSON-LD | At least one block present |
| BreadcrumbList | Present on every non-homepage page |
| Images | All `<img>` have `alt` attribute |
| Internal links | At least 5 `href="*.html"` links |

A page with any validation issue must not be committed.

---

## Brand Standards

- Always write **LexScale.ai** (with `.ai`) — never "LexScale" alone in visible text
- Article bylines: **LexScale.ai Editorial**
- Footer copyright: `© {YEAR} LexScale.ai · All rights reserved`
- Nav logo markup: `Lex<span>Scale</span>.ai` (the `<span>` gets purple colour via CSS)

---

## URL Rules

- All pages are `.html` files on disk but are served and linked **without** `.html` — `/about`, not `about.html`
- Canonical URLs never include `.html` — `https://lexscale.ai/about`, not `.../about.html`
- Vercel `cleanUrls: true` — pages served without `.html`; `.html` URLs 301 redirect to clean URL
- No trailing slashes on any page

---

## File Locations

```
/                          → all HTML pages (53 total)
/seo_helpers.py            → SEO helper module — single source of truth
/sitemap.xml               → 53 URLs; update with add_to_sitemap()
/robots.txt                → allows *, GPTBot, Google-Extended, PerplexityBot, anthropic-ai
/og-image.png              → 1200×630px OG image
/expand_articles.py        → generates the 25 insight articles
/gen_insight_silos.py      → generates hub/category pages
/seo_upgrade.py            → initial SEO patch script (reference only)
/seo_upgrade_v2.py         → FAQPage + LocalBusiness + contact/privacy pages (reference)
/seo_audit_fix.py          → audit fix pass (reference only)
```

---

## AI Search Optimisation Notes

To rank in Google AI Overviews, ChatGPT, Gemini, and Perplexity:

1. **Entities over keywords** — establish clear entities (who, what, where) in the first 150 words
2. **Direct answers** — open paragraphs with the answer before the explanation
3. **FAQPage schema** — on all service pages; eligible for Google FAQ rich results
4. **BreadcrumbList schema** — on every non-homepage page
5. **Topical depth** — articles should be 3,000+ words covering a topic thoroughly
6. **Internal silo structure** — hub → articles → service pages with consistent anchor text
7. **robots.txt** explicitly allows GPTBot, anthropic-ai, PerplexityBot, Google-Extended
