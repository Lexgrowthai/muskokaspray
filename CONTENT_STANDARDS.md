# LexScale.ai Content Standards
**Permanent publishing rules. Every new page must meet these before commit.**

---

## Hub Pages

### Required Structure (in order)
1. `<head>` with `head_block()` — CollectionPage + BreadcrumbList + FAQPage schemas
2. Nav (`NAV`)
3. **Hub hero** — eyebrow tag, `<h1>`, stat bar
4. **Stat bar** — count must match actual published article count (disk files, not planned)
5. **Table of Contents** — `.toc-section` with jump links to every `art-group`
6. **Article groups** — 2–4 themed `<div class="art-group">` sections, each with `<h2 id="group-id" class="group-h2">`
7. **FAQ section** — `.hub-faq-section` with ≥8 law-firm-specific Q&A pairs
8. CTA banner
9. Footer (`FOOTER`)

### Article Cards in Hub Grids
- Every `.html` file in the hub's `/insights/<category>/` directory must appear as an `art-card` in the hub
- Card `href` must match the actual file path exactly (including `.html` extension)
- Card title = article `<title>` tag (strip ` | LexScale.ai` suffix)
- Card description = article `<meta name="description">` content (truncated to ~120 chars)
- New articles must be added to the hub **in the same commit** they are created

### Stat Bar Accuracy
- `<div class="stat-num">N</div>` where N = count of `.html` files in `/insights/<category>/`
- Do not hardcode counts — derive from disk at generation time
- Run `validate_content.py --hub insights/<category>.html` before committing

### Schema Requirements
| Schema | Required |
|---|---|
| CollectionPage | Yes |
| BreadcrumbList (Home → Hub) | Yes |
| FAQPage | Yes (≥8 questions) |

### Internal Links
- Hub hero CTA → `contact.html`
- Each article card → correct article file
- FAQ section links → at least 2 related service pages
- Footer (auto via `FOOTER`)

---

## Article Pages

### Required Structure (in order)
1. `<head>` with `head_block()` — Article + BreadcrumbList (4 levels) schemas
2. Nav (`NAV`)
3. **Article hero** — category badge, `<h1>`, byline (`LexScale.ai Editorial`), publish date
4. **Article body** — ≥1,500 words, structured with `<h2>` sections and `<h3>` subsections
5. **Internal links block** — Related Articles + Related Services
6. **Author / CTA block**
7. Footer (`FOOTER`)

### Heading Hierarchy
- Exactly **one `<h1>`** — the primary keyword phrase
- `<h2>` for major sections (minimum 3)
- `<h3>` for subsections or list items within sections
- Never skip levels (H1 → H3 without H2)

### Schema Requirements
| Schema | Required |
|---|---|
| Article | Yes |
| BreadcrumbList (Home → Hub → Article) | Yes |
| FAQPage | Optional but recommended for 800+ word articles |

### Breadcrumb Levels
```
Home (https://lexscale.ai) →
Hub Name (https://lexscale.ai/insights/<category>.html) →
Article Title (https://lexscale.ai/insights/<category>/slug.html)
```

### Internal Links (minimum)
| Link type | Count |
|---|---|
| Back to parent hub | 1 |
| Related articles (same or other category) | 2 |
| Service page (e.g. ai-seo-for-law-firms.html) | 1 |
| Contact or homepage | 1 |
| **Total minimum** | **5** |

### Dates
- `datePublished` = actual publish date (ISO 8601, e.g. `"2026-06-24"`)
- `dateModified` = same as publish date on first publish; update on edits
- Visible byline date format: `June 24, 2026`

### Meta Requirements
| Tag | Requirement |
|---|---|
| `<title>` | 50–65 chars, keyword-first, ends with ` \| LexScale.ai` |
| `<meta name="description">` | 140–155 chars, unique, includes primary keyword |
| Canonical | Matches slug exactly, includes `.html` |
| Robots | `index, follow` |
| OG tags | All 5 required (title, description, url, image, site_name) |
| Twitter tags | All 4 required (card, title, description, image) |

---

## File Naming

- All files: lowercase, hyphen-separated, `.html` extension
- Articles: `/insights/<category>/<descriptive-slug>.html`
- Hub pages: `/insights/<category>.html`
- Service pages: `/<service-slug>.html` in root
- No trailing slashes, no `/index.html` style paths

---

## Sitemap

Every new page must be added to `sitemap.xml`:
```python
from seo_helpers import add_to_sitemap
add_to_sitemap("insights/category/slug.html", priority="0.7", changefreq="monthly")
```

Hub pages: `priority="0.8"`, `changefreq="weekly"`
Service pages: `priority="0.9"`, `changefreq="monthly"`
Homepage: `priority="1.0"`, `changefreq="weekly"`

---

## Publishing Checklist

Run before every commit:
```bash
python validate_content.py insights/category/new-article.html
```

The validator checks:
- [ ] `<title>` length 50–65 chars
- [ ] Meta description length 140–155 chars
- [ ] Canonical URL present and correct
- [ ] Robots meta present
- [ ] All 5 OG tags present
- [ ] All 4 Twitter tags present
- [ ] Exactly one `<h1>`
- [ ] No heading level skips
- [ ] At least one JSON-LD block
- [ ] BreadcrumbList schema present
- [ ] All `<img>` have `alt` attributes
- [ ] At least 5 internal `.html` links
- [ ] Page appears in hub grid (for articles)
- [ ] Page appears in `sitemap.xml`
- [ ] Stat bar count matches disk file count (for hubs)

**A page with any validator failure must not be committed.**

---

## Content Quality

- Articles must be **≥1,500 words** (aim for 2,500–4,000 for pillar content)
- Open with the direct answer in the first paragraph (AI Overview eligibility)
- Include at least one data point or statistic per major section
- Use second-person ("your law firm") not third-person ("law firms")
- Canadian context where relevant (Ontario bar, Law Society compliance)
- No orphan pages — every article must be reachable from its hub

---

## Brand Voice

- Company name: **LexScale.ai** (never "LexScale" alone in body copy)
- Article byline: **LexScale.ai Editorial**
- Footer copyright: `© 2026 LexScale.ai · All rights reserved`
- Audience: Canadian and US law firm owners, managing partners, operations managers
- Tone: authoritative, direct, no fluff — practitioners, not beginners
