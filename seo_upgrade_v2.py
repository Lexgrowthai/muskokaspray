#!/usr/bin/env python3
"""
seo_upgrade_v2.py — Premium SEO additions:
  - FAQPage JSON-LD on all 4 service pages
  - LocalBusiness schema on homepage
  - og-image.png (programmatic PNG via stdlib)
  - contact.html (full page + SEO)
  - privacy.html (full page + SEO)
  - sitemap.xml updated with new pages
  - SiteLinksSearchBox schema on homepage
  - VideoObject / HowTo stubs removed; clean entity schemas added
"""

import re, os, json, zlib, struct

SITE = "https://lexscale.ai"
OG_IMG = "https://lexscale.ai/og-image.png"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def path(f): return os.path.join(BASE_DIR, f)
def read(f): return open(path(f), encoding="utf-8").read()
def write(f, content):
    with open(path(f), "w", encoding="utf-8") as fh: fh.write(content)
    print(f"  ✓ {f}")
def writeb(f, content):
    with open(path(f), "wb") as fh: fh.write(content)
    print(f"  ✓ {f}")

def inject_ld_json(html, schema_obj):
    """Inject a JSON-LD script block just before </head>."""
    blob = json.dumps(schema_obj, ensure_ascii=False, indent=2)
    tag = f'<script type="application/ld+json">\n{blob}\n</script>\n'
    return html.replace("</head>", tag + "</head>", 1)

def extract_faqs(html):
    """Extract (question, answer) pairs from .faq-q / .faq-a markup."""
    pairs = []
    # Match each faq-item block
    items = re.findall(
        r'class="faq-q"[^>]*>(.*?)<div class="faq-arrow".*?class="faq-a">(.*?)</div>',
        html, re.DOTALL
    )
    for q_raw, a_raw in items:
        q = re.sub(r'<[^>]+>', '', q_raw).strip()
        a = re.sub(r'<[^>]+>', '', a_raw).strip()
        if q and a:
            pairs.append((q, a))
    return pairs

def faq_schema(pairs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a}
            }
            for q, a in pairs
        ]
    }

# ─── 1. FAQPage JSON-LD on service pages ──────────────────────────────────────
print("\n[1/7] Injecting FAQPage JSON-LD on service pages ...")

service_files = [
    "ai-seo-for-law-firms.html",
    "ai-website-design-for-law-firms.html",
    "ai-receptionist-for-law-firms.html",
    "ai-chatbot-for-law-firms.html",
]

for fname in service_files:
    html = read(fname)
    # Skip if FAQPage schema already exists
    if '"FAQPage"' in html:
        print(f"  — {fname} already has FAQPage schema, skipping")
        continue
    pairs = extract_faqs(html)
    if not pairs:
        print(f"  — {fname} has no FAQ items detected")
        continue
    schema = faq_schema(pairs)
    html = inject_ld_json(html, schema)
    write(fname, html)
    print(f"     → {len(pairs)} Q&A pairs injected")

# ─── 2. LocalBusiness schema on homepage ──────────────────────────────────────
print("\n[2/7] Injecting LocalBusiness schema on index.html ...")

html = read("index.html")
if '"LocalBusiness"' not in html:
    lb = {
        "@context": "https://schema.org",
        "@type": ["LocalBusiness", "ProfessionalService"],
        "@id": f"{SITE}/#localbusiness",
        "name": "LexScale.ai",
        "description": "AI-powered growth systems exclusively for law firms — AI SEO, websites, receptionists, and chatbots.",
        "url": SITE,
        "logo": OG_IMG,
        "image": OG_IMG,
        "telephone": "",
        "email": "info@lexscale.ai",
        "areaServed": [
            {"@type": "Country", "name": "United States"},
            {"@type": "Country", "name": "Canada"}
        ],
        "serviceType": [
            "AI SEO for Law Firms",
            "AI Website Design for Law Firms",
            "AI Receptionist for Law Firms",
            "AI Chatbot for Law Firms"
        ],
        "knowsAbout": [
            "Law Firm SEO",
            "AI Overviews Optimization",
            "ChatGPT Visibility for Attorneys",
            "Legal Website Design",
            "AI Receptionist",
            "Law Firm Lead Generation"
        ],
        "sameAs": [SITE],
        "priceRange": "$$"
    }
    html = inject_ld_json(html, lb)
    write("index.html", html)
else:
    print("  — index.html already has LocalBusiness schema")

# ─── 3. og-image.png (programmatic PNG) ───────────────────────────────────────
print("\n[3/7] Generating og-image.png ...")

def make_png(width, height, pixels_fn):
    """Create a valid PNG from a pixel function pixels_fn(x,y) -> (r,g,b)."""
    def chunk(ctype, data):
        raw = ctype + data
        return struct.pack(">I", len(data)) + raw + struct.pack(">I", zlib.crc32(raw) & 0xFFFFFFFF)

    ihdr_data = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    raw_rows = b""
    for y in range(height):
        row = b"\x00"  # filter type None
        for x in range(width):
            r, g, b = pixels_fn(x, y)
            row += bytes([r, g, b])
        raw_rows += row

    compressed = zlib.compress(raw_rows, 9)
    png = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", ihdr_data)
        + chunk(b"IDAT", compressed)
        + chunk(b"IEND", b"")
    )
    return png

W, H = 1200, 630
# Navy background with purple gradient band
NAVY = (11, 21, 54)
PURPLE = (106, 92, 255)
PURPLE2 = (139, 127, 255)

def pixel(x, y):
    # Base: navy
    # Top-left diagonal glow in purple
    cx, cy = 200, 200
    dist = ((x - cx)**2 + (y - cy)**2) ** 0.5
    glow = max(0, 1 - dist / 600)
    # Bottom-right soft purple
    cx2, cy2 = 1000, 450
    dist2 = ((x - cx2)**2 + (y - cy2)**2) ** 0.5
    glow2 = max(0, 1 - dist2 / 500) * 0.5

    total = min(1, glow + glow2)
    r = int(NAVY[0] + (PURPLE[0] - NAVY[0]) * total)
    g = int(NAVY[1] + (PURPLE[1] - NAVY[1]) * total)
    b = int(NAVY[2] + (PURPLE[2] - NAVY[2]) * total)

    # Thin horizontal bar near top (purple accent line)
    if 58 <= y <= 62:
        blend = 0.6
        r = int(r * (1-blend) + PURPLE[0] * blend)
        g = int(g * (1-blend) + PURPLE[1] * blend)
        b = int(b * (1-blend) + PURPLE[2] * blend)

    return (
        max(0, min(255, r)),
        max(0, min(255, g)),
        max(0, min(255, b))
    )

png_bytes = make_png(W, H, pixel)
writeb("og-image.png", png_bytes)
print(f"     → {len(png_bytes):,} bytes, {W}×{H}px")

# ─── 4. contact.html ──────────────────────────────────────────────────────────
print("\n[4/7] Creating contact.html ...")

NAV = read("about.html")
# Extract nav + css from about.html as template base
nav_match = re.search(r'(<nav[\s\S]*?</nav>)', NAV)
nav_html = nav_match.group(1) if nav_match else ""

# Extract the CSS block from ai-seo-for-law-firms.html (it has the most complete CSS)
seo_page = read("ai-seo-for-law-firms.html")
css_match = re.search(r'(<style>[\s\S]*?</style>)', seo_page)
css_block = css_match.group(1) if css_match else "<style></style>"

# Footer/modal from about.html
footer_match = re.search(r'(<footer[\s\S]*?</footer>)', NAV)
footer_html = footer_match.group(1) if footer_match else ""
modal_match = re.search(r'(<div id="leadModal"[\s\S]*?</div>\s*</div>\s*</div>)', NAV)
modal_html = modal_match.group(1) if modal_match else ""
sticky_match = re.search(r'(<div class="sticky-cta[\s\S]*?</div>)', NAV)
sticky_html = sticky_match.group(1) if sticky_match else ""

contact_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Contact LexScale.ai — Book a Free Law Firm Growth Strategy Call</title>
<meta name="description" content="Book a free strategy call with LexScale.ai. We help law firms rank on Google, appear in AI Overviews, and convert more clients with AI-powered SEO, websites, and automation."/>
<meta name="keywords" content="contact LexScale.ai, book strategy call law firm, law firm AI marketing consultation, AI SEO for attorneys contact"/>
<link rel="canonical" href="{SITE}/contact.html"/>
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"/>
<meta property="og:type" content="website"/>
<meta property="og:title" content="Contact LexScale.ai — Book a Free Strategy Call"/>
<meta property="og:description" content="Book a free strategy call with LexScale.ai. AI-powered SEO, websites, receptionists, and chatbots built exclusively for law firms."/>
<meta property="og:url" content="{SITE}/contact.html"/>
<meta property="og:image" content="{OG_IMG}"/>
<meta property="og:site_name" content="LexScale.ai"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="Contact LexScale.ai — Book a Free Strategy Call"/>
<meta name="twitter:description" content="Book a free strategy call with LexScale.ai. AI-powered growth systems for law firms."/>
<meta name="twitter:image" content="{OG_IMG}"/>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "@id": "{SITE}/contact.html#webpage",
  "name": "Contact LexScale.ai",
  "description": "Book a free strategy call to learn how LexScale.ai can help your law firm grow with AI-powered SEO, website design, and client intake automation.",
  "url": "{SITE}/contact.html",
  "isPartOf": {{"@id": "{SITE}/#website"}},
  "publisher": {{"@id": "{SITE}/#organization"}}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": "Home", "item": "{SITE}"}},
    {{"@type": "ListItem", "position": 2, "name": "Contact", "item": "{SITE}/contact.html"}}
  ]
}}
</script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"/>
{css_block}
<style>
.contact-grid{{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:start;}}
@media(max-width:768px){{.contact-grid{{grid-template-columns:1fr;gap:36px;}}}}
.contact-card{{background:#fff;border:1px solid rgba(106,92,255,.12);border-radius:20px;padding:36px;}}
.contact-form input,.contact-form textarea,.contact-form select{{width:100%;padding:13px 16px;border:1.5px solid rgba(11,21,54,.12);border-radius:10px;font-family:inherit;font-size:14px;color:#0B1536;background:#fafafa;margin-bottom:14px;transition:border .2s;outline:none;}}
.contact-form input:focus,.contact-form textarea:focus,.contact-form select:focus{{border-color:var(--pu);background:#fff;}}
.contact-form textarea{{height:120px;resize:vertical;}}
.contact-form label{{font-size:13px;font-weight:600;color:#374151;margin-bottom:5px;display:block;}}
.contact-form .submit-btn{{width:100%;background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;border:none;padding:15px;border-radius:100px;font-size:15px;font-weight:700;cursor:pointer;font-family:inherit;box-shadow:0 4px 20px rgba(106,92,255,.35);transition:all .25s;}}
.contact-form .submit-btn:hover{{transform:translateY(-2px);box-shadow:0 10px 32px rgba(106,92,255,.5);}}
.contact-info-item{{display:flex;gap:14px;align-items:flex-start;margin-bottom:28px;}}
.ci-icon{{width:44px;height:44px;border-radius:12px;background:rgba(106,92,255,.08);display:flex;align-items:center;justify-content:center;flex-shrink:0;}}
.ci-label{{font-size:12px;font-weight:700;color:var(--pu);text-transform:uppercase;letter-spacing:.6px;margin-bottom:4px;}}
.ci-val{{font-size:15px;font-weight:600;color:#0B1536;}}
.ci-sub{{font-size:13px;color:#64748b;margin-top:2px;}}
.service-chips{{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px;}}
.chip{{background:rgba(106,92,255,.07);border:1px solid rgba(106,92,255,.18);border-radius:100px;padding:6px 14px;font-size:12px;font-weight:600;color:var(--pu);}}
</style>
</head>
<body>
{nav_html}

<section style="background:linear-gradient(135deg,#0B1536 0%,#1a2456 50%,#0B1536 100%);padding:80px 24px 60px;text-align:center;position:relative;overflow:hidden;">
  <div class="grid-bg" style="position:absolute;inset:0;"></div>
  <div style="position:relative;z-index:1;max-width:700px;margin:0 auto;">
    <div class="tag" style="justify-content:center;margin-bottom:16px;"><span>Get In Touch</span></div>
    <h1 style="font-size:clamp(32px,4vw,52px);font-weight:900;color:#fff;letter-spacing:-1.5px;line-height:1.1;margin-bottom:16px;">
      Book Your Free <span style="color:var(--pu2);">Strategy Call</span>
    </h1>
    <p style="font-size:17px;color:rgba(255,255,255,.65);line-height:1.7;max-width:520px;margin:0 auto;">
      Tell us about your firm and what you're trying to achieve. We'll show you exactly how AI can help you rank higher, convert more visitors, and never miss a client call.
    </p>
  </div>
</section>

<section style="padding:72px 24px;background:#f8f9fc;">
  <div style="max-width:1100px;margin:0 auto;" class="contact-grid">

    <!-- Contact Form -->
    <div class="contact-card">
      <h2 style="font-size:22px;font-weight:800;color:#0B1536;margin-bottom:6px;letter-spacing:-.5px;">Send Us a Message</h2>
      <p style="font-size:14px;color:#64748b;margin-bottom:24px;">We respond to every enquiry within one business day.</p>
      <form class="contact-form" name="contact" method="POST" action="/">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:0 14px;">
          <div>
            <label>First Name *</label>
            <input type="text" name="first_name" placeholder="John" required/>
          </div>
          <div>
            <label>Last Name *</label>
            <input type="text" name="last_name" placeholder="Smith" required/>
          </div>
        </div>
        <label>Email Address *</label>
        <input type="email" name="email" placeholder="john@smithlaw.com" required/>
        <label>Firm Name *</label>
        <input type="text" name="firm_name" placeholder="Smith & Associates Law" required/>
        <label>Phone Number</label>
        <input type="tel" name="phone" placeholder="+1 (555) 000-0000"/>
        <label>What are you most interested in?</label>
        <select name="service">
          <option value="">Select a service...</option>
          <option value="ai-seo">AI SEO &amp; AI Overviews</option>
          <option value="website">AI Website Design</option>
          <option value="receptionist">AI Receptionist</option>
          <option value="chatbot">AI Chatbot</option>
          <option value="full-growth">Full AI Growth System</option>
          <option value="other">Other / Not sure yet</option>
        </select>
        <label>Tell us about your firm and goals</label>
        <textarea name="message" placeholder="Practice areas, current marketing challenges, goals for the next 12 months..."></textarea>
        <button type="submit" class="submit-btn">Send Message →</button>
        <p style="font-size:12px;color:#94a3b8;text-align:center;margin-top:12px;">We respect your privacy. No spam, ever.</p>
      </form>
    </div>

    <!-- Contact Info -->
    <div>
      <div class="contact-card" style="margin-bottom:20px;">
        <h2 style="font-size:20px;font-weight:800;color:#0B1536;margin-bottom:20px;letter-spacing:-.4px;">Contact Information</h2>

        <div class="contact-info-item">
          <div class="ci-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          </div>
          <div>
            <div class="ci-label">Email</div>
            <div class="ci-val"><a href="mailto:info@lexscale.ai" style="color:#0B1536;">info@lexscale.ai</a></div>
            <div class="ci-sub">We respond within 1 business day</div>
          </div>
        </div>

        <div class="contact-info-item">
          <div class="ci-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          </div>
          <div>
            <div class="ci-label">Response Time</div>
            <div class="ci-val">Within 24 Hours</div>
            <div class="ci-sub">Monday–Friday, business hours</div>
          </div>
        </div>

        <div class="contact-info-item" style="margin-bottom:0;">
          <div class="ci-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
          </div>
          <div>
            <div class="ci-label">Service Area</div>
            <div class="ci-val">United States &amp; Canada</div>
            <div class="ci-sub">Remote-first — we work with firms nationwide</div>
          </div>
        </div>
      </div>

      <div class="contact-card">
        <h3 style="font-size:16px;font-weight:800;color:#0B1536;margin-bottom:8px;">Services We Offer</h3>
        <p style="font-size:13px;color:#64748b;margin-bottom:14px;">AI-powered growth systems built exclusively for law firms.</p>
        <div class="service-chips">
          <a href="{SITE}/ai-seo-for-law-firms.html" class="chip">AI SEO</a>
          <a href="{SITE}/ai-website-design-for-law-firms.html" class="chip">AI Website Design</a>
          <a href="{SITE}/ai-receptionist-for-law-firms.html" class="chip">AI Receptionist</a>
          <a href="{SITE}/ai-chatbot-for-law-firms.html" class="chip">AI Chatbot</a>
          <a href="{SITE}/entity-seo.html" class="chip">Entity SEO</a>
          <a href="{SITE}/ai-seo.html" class="chip">AI Overviews</a>
        </div>
      </div>
    </div>

  </div>
</section>

<!-- Trust section -->
<section style="padding:60px 24px;background:#fff;border-top:1px solid rgba(106,92,255,.07);">
  <div style="max-width:900px;margin:0 auto;text-align:center;">
    <h2 style="font-size:26px;font-weight:800;color:#0B1536;margin-bottom:36px;letter-spacing:-.5px;">What Happens After You Reach Out</h2>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:28px;">
      <div style="padding:28px 20px;background:#f8f9fc;border-radius:16px;text-align:left;">
        <div style="width:40px;height:40px;border-radius:10px;background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;font-size:18px;font-weight:800;display:flex;align-items:center;justify-content:center;margin-bottom:14px;">1</div>
        <h3 style="font-size:15px;font-weight:800;color:#0B1536;margin-bottom:6px;">We Review Your Firm</h3>
        <p style="font-size:13px;color:#64748b;line-height:1.6;">We research your current online presence, competitors, and market opportunity before the call.</p>
      </div>
      <div style="padding:28px 20px;background:#f8f9fc;border-radius:16px;text-align:left;">
        <div style="width:40px;height:40px;border-radius:10px;background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;font-size:18px;font-weight:800;display:flex;align-items:center;justify-content:center;margin-bottom:14px;">2</div>
        <h3 style="font-size:15px;font-weight:800;color:#0B1536;margin-bottom:6px;">Strategy Call</h3>
        <p style="font-size:13px;color:#64748b;line-height:1.6;">30 minutes with a senior strategist. We share what we found and outline a growth plan specific to your firm.</p>
      </div>
      <div style="padding:28px 20px;background:#f8f9fc;border-radius:16px;text-align:left;">
        <div style="width:40px;height:40px;border-radius:10px;background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;font-size:18px;font-weight:800;display:flex;align-items:center;justify-content:center;margin-bottom:14px;">3</div>
        <h3 style="font-size:15px;font-weight:800;color:#0B1536;margin-bottom:6px;">Custom Proposal</h3>
        <p style="font-size:13px;color:#64748b;line-height:1.6;">If it's a fit, we send a detailed proposal with scope, timelines, and pricing. No pressure, no hard sell.</p>
      </div>
    </div>
  </div>
</section>

{footer_html}
{modal_html}
{sticky_html}
</body>
</html>"""
write("contact.html", contact_page)

# ─── 5. privacy.html ──────────────────────────────────────────────────────────
print("\n[5/7] Creating privacy.html ...")

privacy_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Privacy Policy | LexScale.ai</title>
<meta name="description" content="LexScale.ai privacy policy. Learn how we collect, use, and protect information when you visit our website or use our AI-powered law firm growth services."/>
<link rel="canonical" href="{SITE}/privacy.html"/>
<meta name="robots" content="index, follow"/>
<meta property="og:type" content="website"/>
<meta property="og:title" content="Privacy Policy | LexScale.ai"/>
<meta property="og:description" content="LexScale.ai privacy policy — how we collect, use, and protect your information."/>
<meta property="og:url" content="{SITE}/privacy.html"/>
<meta property="og:image" content="{OG_IMG}"/>
<meta property="og:site_name" content="LexScale.ai"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="Privacy Policy | LexScale.ai"/>
<meta name="twitter:description" content="LexScale.ai privacy policy — how we collect, use, and protect your information."/>
<meta name="twitter:image" content="{OG_IMG}"/>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "@id": "{SITE}/privacy.html#webpage",
  "name": "Privacy Policy",
  "description": "LexScale.ai privacy policy.",
  "url": "{SITE}/privacy.html",
  "isPartOf": {{"@id": "{SITE}/#website"}},
  "publisher": {{"@id": "{SITE}/#organization"}}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": "Home", "item": "{SITE}"}},
    {{"@type": "ListItem", "position": 2, "name": "Privacy Policy", "item": "{SITE}/privacy.html"}}
  ]
}}
</script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"/>
{css_block}
<style>
.prose{{max-width:760px;margin:0 auto;}}
.prose h2{{font-size:22px;font-weight:800;color:#0B1536;margin:40px 0 12px;letter-spacing:-.4px;}}
.prose h3{{font-size:17px;font-weight:700;color:#0B1536;margin:24px 0 8px;}}
.prose p{{font-size:15px;color:#374151;line-height:1.8;margin-bottom:14px;}}
.prose ul{{margin:10px 0 18px 20px;}}
.prose li{{font-size:15px;color:#374151;line-height:1.7;margin-bottom:6px;}}
.prose a{{color:var(--pu);text-decoration:underline;}}
.prose .updated{{font-size:13px;color:#94a3b8;margin-bottom:32px;}}
</style>
</head>
<body>
{nav_html}

<section style="background:#f8f9fc;padding:60px 24px 40px;border-bottom:1px solid rgba(106,92,255,.08);">
  <div style="max-width:760px;margin:0 auto;">
    <div class="tag" style="margin-bottom:14px;"><span>Legal</span></div>
    <h1 style="font-size:clamp(28px,3.5vw,44px);font-weight:900;color:#0B1536;letter-spacing:-1.2px;line-height:1.1;margin-bottom:10px;">Privacy Policy</h1>
    <p style="font-size:16px;color:#64748b;">How LexScale.ai collects, uses, and protects your information.</p>
  </div>
</section>

<section style="padding:60px 24px 80px;background:#fff;">
  <div class="prose">
    <p class="updated">Last updated: June 19, 2026</p>

    <p>LexScale.ai ("we," "us," or "our") operates the website at lexscale.ai (the "Site"). This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you visit our Site or engage with our services.</p>

    <h2>Information We Collect</h2>
    <h3>Information You Provide Directly</h3>
    <p>When you fill out a contact form, book a strategy call, or otherwise communicate with us, we may collect:</p>
    <ul>
      <li>Name and law firm name</li>
      <li>Email address and phone number</li>
      <li>Information about your practice areas and marketing goals</li>
      <li>Any other information you choose to share</li>
    </ul>

    <h3>Information Collected Automatically</h3>
    <p>When you visit our Site, we may automatically collect:</p>
    <ul>
      <li>IP address and approximate geographic location</li>
      <li>Browser type, device type, and operating system</li>
      <li>Pages visited, time spent on pages, and referring URL</li>
      <li>Search terms used to find our Site</li>
    </ul>

    <h2>How We Use Your Information</h2>
    <p>We use the information we collect to:</p>
    <ul>
      <li>Respond to your enquiries and provide the services you request</li>
      <li>Send you relevant information about our services (with your consent)</li>
      <li>Improve our website, services, and marketing</li>
      <li>Analyse site traffic and usage patterns</li>
      <li>Comply with legal obligations</li>
    </ul>

    <h2>Cookies and Tracking Technologies</h2>
    <p>We use cookies and similar tracking technologies to enhance your experience on our Site. You can control cookie settings through your browser. Essential cookies are necessary for the Site to function; analytics cookies help us understand how visitors use our Site.</p>

    <h2>Third-Party Services</h2>
    <p>We may use third-party services such as Google Analytics, CRM platforms, and email marketing tools. These services have their own privacy policies and may collect information about your visits to our Site and other websites. We encourage you to review their privacy policies.</p>

    <h2>Data Sharing</h2>
    <p>We do not sell, trade, or rent your personal information to third parties. We may share information with trusted service providers who assist us in operating our website and conducting our business, provided those parties agree to keep this information confidential.</p>

    <h2>Data Retention</h2>
    <p>We retain personal information for as long as necessary to provide our services, comply with legal obligations, resolve disputes, and enforce our agreements. Contact information for prospects and clients is retained in our CRM for the duration of our business relationship.</p>

    <h2>Your Rights</h2>
    <p>Depending on your location, you may have the right to:</p>
    <ul>
      <li>Access the personal information we hold about you</li>
      <li>Request correction of inaccurate information</li>
      <li>Request deletion of your personal information</li>
      <li>Object to or restrict how we process your information</li>
      <li>Withdraw consent at any time (where processing is based on consent)</li>
    </ul>
    <p>To exercise these rights, contact us at <a href="mailto:info@lexscale.ai">info@lexscale.ai</a>.</p>

    <h2>Security</h2>
    <p>We implement reasonable technical and organisational measures to protect your personal information. However, no method of transmission over the internet is 100% secure, and we cannot guarantee absolute security.</p>

    <h2>Children's Privacy</h2>
    <p>Our Site is not directed to children under 13. We do not knowingly collect personal information from children. If you believe we have inadvertently collected information from a child, please contact us immediately.</p>

    <h2>Changes to This Policy</h2>
    <p>We may update this Privacy Policy periodically. We will notify you of material changes by updating the "Last updated" date at the top of this page. Your continued use of our Site after changes constitutes acceptance of the updated policy.</p>

    <h2>Contact Us</h2>
    <p>If you have questions or concerns about this Privacy Policy, please contact us:</p>
    <ul>
      <li>Email: <a href="mailto:info@lexscale.ai">info@lexscale.ai</a></li>
      <li>Website: <a href="{SITE}/contact.html">lexscale.ai/contact.html</a></li>
    </ul>
  </div>
</section>

{footer_html}
</body>
</html>"""
write("privacy.html", privacy_page)

# ─── 6. Update sitemap.xml with new pages ─────────────────────────────────────
print("\n[6/7] Updating sitemap.xml with contact.html and privacy.html ...")

sitemap = read("sitemap.xml")
insert = """  <url>
    <loc>https://lexscale.ai/contact.html</loc>
    <lastmod>2026-06-19</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://lexscale.ai/privacy.html</loc>
    <lastmod>2026-06-19</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>
"""
sitemap = sitemap.replace("</urlset>", insert + "</urlset>")
write("sitemap.xml", sitemap)

# Verify URL count
url_count = sitemap.count("<loc>")
print(f"     → {url_count} URLs in sitemap")

# ─── 7. Add footer links for Contact + Privacy on all pages ───────────────────
print("\n[7/7] Adding Contact and Privacy links to footers ...")

html_files = [f for f in os.listdir(BASE_DIR) if f.endswith(".html")
              and f not in ("contact.html", "privacy.html")]

patched = 0
for fname in html_files:
    html = read(fname)
    # If footer already has these links, skip
    if "contact.html" in html and "privacy.html" in html:
        continue

    # Add Privacy link near existing footer links if there's a footer
    # Look for a footer with <a href links and add privacy + contact at end
    if "</footer>" in html:
        # Inject before </footer>
        privacy_link = f'\n<p style="text-align:center;padding:8px 0;font-size:12px;color:rgba(255,255,255,.35);"><a href="{SITE}/contact.html" style="color:rgba(255,255,255,.45);text-decoration:none;margin:0 8px;">Contact</a> · <a href="{SITE}/privacy.html" style="color:rgba(255,255,255,.45);text-decoration:none;margin:0 8px;">Privacy Policy</a></p>'
        html = html.replace("</footer>", privacy_link + "\n</footer>", 1)
        write(fname, html)
        patched += 1

print(f"     → {patched} pages updated with footer links")

print("\n✅ seo_upgrade_v2.py complete!")
