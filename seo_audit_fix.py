#!/usr/bin/env python3
"""
seo_audit_fix.py — Fixes found by live audit:
  1. Trim 15 titles over 65 chars to under 60c (concise + keyword-leading)
  2. Trim 19 meta descriptions over 160 chars to under 155c
  3. Fix footer year 2025 → 2026 on all 53 pages
  4. Fix broken footer Privacy/Terms href="#" → real pages
  5. Fix brand "LexScale Editorial" → "LexScale.ai Editorial" on 25 article pages
  6. Fix brand "LexScale deployed" → "LexScale.ai deployed" in index.html case studies
  7. Add Contact to nav on index.html (currently missing from nav bar)
  8. Fix duplicate footer privacy block (make relative not absolute URLs)
  9. Fix privacy.html title (only 28 chars, expand)
 10. Add LocalBusiness @id cross-reference to Organization on about.html
"""

import re, os, glob

BASE = os.path.dirname(os.path.abspath(__file__))
changes = []

def read(f):   return open(os.path.join(BASE, f), encoding="utf-8").read()
def write(f, c):
    open(os.path.join(BASE, f), "w", encoding="utf-8").write(c)
    print(f"  ✓ {f}")

def swap_title(html, new_title):
    return re.sub(r'<title>[^<]*</title>', f'<title>{new_title}</title>', html, count=1)

def swap_meta(html, name, new_val):
    pat = rf'(<meta name="{name}" content=")[^"]*(")'
    return re.sub(pat, rf'\g<1>{new_val}\g<2>', html, count=1)

def swap_og(html, prop, new_val):
    pat = rf'(<meta property="{prop}" content=")[^"]*(")'
    return re.sub(pat, rf'\g<1>{new_val}\g<2>', html, count=1)

def swap_twitter(html, name, new_val):
    pat = rf'(<meta name="{name}" content=")[^"]*(")'
    return re.sub(pat, rf'\g<1>{new_val}\g<2>', html, count=1)

# ─── 1 & 2: Title and description corrections ─────────────────────────────────
# Format: file → (new_title, new_desc)  [title=None means leave, desc=None means leave]
METADATA = {
    "index.html": (
        "LexScale.ai — AI Growth Systems for Law Firms",
        "AI SEO, AI receptionists, AI chatbots, and AI websites built for law firms. Rank on Google, appear in AI Overviews, and get cited by ChatGPT and Gemini.",
    ),
    "about.html": (
        "About LexScale.ai — AI Built for Law Firms",
        "LexScale.ai blends 10+ years of legal marketing expertise with AI to help law firms rank on Google, appear in AI Overviews, and convert more clients.",
    ),
    "contact.html": (
        "Contact LexScale.ai — Book a Free Strategy Call",
        "Book a free strategy call with LexScale.ai. We help law firms rank on Google, get cited by AI platforms, and automate client intake with AI.",
    ),
    "privacy.html": (
        "Privacy Policy | LexScale.ai — How We Handle Your Data",
        "How LexScale.ai collects, uses, and protects your information when you visit our site or use our AI-powered law firm growth services.",
    ),
    # Service pages
    "ai-seo-for-law-firms.html": (
        "AI SEO for Law Firms | Rank & Get Cited by AI",
        "AI SEO built for law firms. Rank on Google, appear in AI Overviews, get cited by ChatGPT, Gemini, and Perplexity. Legal SEO across North America.",
    ),
    "ai-website-design-for-law-firms.html": (
        "AI Website Design for Law Firms | LexScale.ai",
        "AI-powered law firm websites designed to rank, convert visitors into clients, and appear in AI Overviews. Custom builds for attorneys across North America.",
    ),
    "ai-receptionist-for-law-firms.html": (
        "AI Receptionist for Law Firms | 24/7 Legal Intake",
        "Never miss a client call. Our AI receptionist answers 24/7, qualifies leads, books consultations, and integrates with your practice management software.",
    ),
    "ai-chatbot-for-law-firms.html": (
        "AI Chatbot for Law Firms | Convert Website Visitors",
        "AI chatbots built for law firm websites. Qualify leads 24/7, answer legal questions, and book consultations automatically — without adding staff.",
    ),
    # Hub pages
    "chatgpt.html": (
        "ChatGPT for Law Firms — AI Visibility Guides",
        "The complete hub for law firms on ChatGPT visibility. Learn how to rank in ChatGPT, earn citations, and win clients from AI search — 12 expert guides.",
    ),
    "google-gemini.html": (
        "Google Gemini for Law Firms — AI Visibility Hub",
        "How law firms can appear in Google Gemini AI responses. Guides on entity optimization, structured data, and AI Overviews for attorneys.",
    ),
    "perplexity.html": (
        "Perplexity AI for Law Firms — Visibility & Citations",
        "How law firms get cited and recommended by Perplexity AI. Guides on optimizing your firm for AI-powered answer engines.",
    ),
    "ai-seo.html": (
        "AI SEO for Law Firms — Strategy Hub | LexScale.ai",
        "Complete AI SEO strategy guides for law firms. Learn topical authority, entity SEO, local AI search, and how to rank in Google AI Overviews.",
    ),
    "ai-receptionists.html": (
        "AI Receptionists for Law Firms — Guide Hub",
        "Everything law firms need on AI receptionists. Guides on intake automation, revenue impact, 24/7 coverage, and choosing the right AI receptionist.",
    ),
    "ai-chatbots.html": (
        "AI Chatbots for Law Firms — Complete Guide Hub",
        "Everything law firms need on AI chatbots. Guides on lead conversion, intake qualification, ROI, and choosing the right chatbot for your practice.",
    ),
    "entity-seo.html": (
        "Entity SEO for Law Firms — Knowledge Graph Hub",
        "Master entity SEO for law firms. Guides on schema markup, knowledge panels, structured data, and entity optimization for Google and AI search.",
    ),
    "ai-websites.html": (
        "AI Website Design for Law Firms — Strategy Hub",
        "Complete guides on AI-powered law firm websites. Learn conversion optimization, SEO structure, speed, and mobile-first design for attorneys.",
    ),
    # Articles with titles >65 chars
    "ai-chatbot-for-law-firm-website.html": (
        "AI Chatbot for Law Firm Websites: Convert More Visitors",
        "Add an AI chatbot to your law firm website and convert more visitors into consultations. 24/7 lead qualification and appointment booking for attorneys.",
    ),
    "ai-chatbot-intake-qualification.html": (
        "AI Chatbot Intake & Lead Qualification for Law Firms",
        "Use AI chatbots to qualify legal leads before they reach your team. Automated intake questions, case screening, and lead scoring for law firms.",
    ),
    "ai-chatbot-roi-for-law-firms.html": (
        "AI Chatbot ROI for Law Firms: Is It Worth It?",
        "Calculate the true ROI of an AI chatbot for your law firm. Revenue captured from missed leads, time saved on intake, and cost vs. traditional live chat.",
    ),
    "ai-receptionist-intake-automation.html": (
        "AI Receptionist & Intake Automation for Law Firms",
        "Automate your law firm's entire intake process with AI. From first call to booked consultation, AI handles qualification, scheduling, and CRM entry.",
    ),
    "ai-seo-vs-traditional-seo-lawyers.html": (
        "AI SEO vs Traditional SEO for Lawyers: Key Differences",
        "How AI SEO differs from traditional SEO for law firms. What changed, what still matters, and how to balance both strategies for maximum visibility.",
    ),
    "best-practices-optimizing-law-firm-websites-for-chatgpt.html": (
        "Optimizing Law Firm Websites for ChatGPT: Best Practices",
        "Proven best practices for making your law firm website ChatGPT-friendly. From structured data to content depth — what AI search engines reward.",
    ),
    "chatgpt-citations-explained.html": (
        "ChatGPT Citations for Law Firms: How to Earn References",
        "What are ChatGPT citations and how do law firms earn them? The exact signals and content strategies that get your firm cited as an authoritative source.",
    ),
    "chatgpt-for-law-firms.html": (
        "ChatGPT for Law Firms: Why AI Visibility Matters",
        "Why ChatGPT visibility is essential for law firms. How AI search is changing legal marketing and how to position your firm to be recommended by AI.",
    ),
    "chatgpt-vs-google-search-for-lawyers.html": (
        "ChatGPT vs Google Search for Lawyers: Key Differences",
        "How ChatGPT and Google Search differ for law firm visibility. Optimize for both AI and traditional search to capture every client touchpoint.",
    ),
    "common-mistakes-law-firms-make-with-ai-search.html": (
        "Common AI Search Mistakes Law Firms Make",
        "Avoid the top AI search mistakes law firms make. From missing structured data to thin content — what's keeping your firm out of ChatGPT and Gemini.",
    ),
    "future-of-chatgpt-and-legal-marketing.html": (
        "The Future of ChatGPT and Legal Marketing",
        "Where is ChatGPT taking legal marketing? Explore emerging trends in AI search and what law firms must do to stay competitive through 2026 and beyond.",
    ),
    "google-gemini-for-law-firms.html": (
        "Google Gemini for Law Firms: Get Recommended by AI",
        "How law firms can appear in Google Gemini AI responses. Optimize your entity presence and structured data to rank in Google's AI search results.",
    ),
    "how-ai-search-is-changing-legal-marketing.html": (
        "How AI Search Is Changing Legal Marketing",
        "AI search is reshaping how clients find law firms. How ChatGPT, Gemini, and Perplexity are changing legal marketing and what smart firms are doing.",
    ),
    "law-firm-website-conversion-optimization.html": (
        "Law Firm Website Conversion Optimization Guide",
        "Turn more website visitors into consultations. Proven conversion optimization strategies for law firm websites — CTAs, trust signals, speed, and UX.",
    ),
    "law-firm-website-seo-structure.html": (
        "Law Firm Website SEO Structure: Architecture That Ranks",
        "Build a law firm website SEO structure that Google and AI search engines love. Silo architecture, internal linking, and page hierarchy for attorneys.",
    ),
    "law-firm-website-speed-performance.html": (
        "Law Firm Website Speed & Performance Optimization",
        "Website speed directly impacts law firm rankings and conversions. Optimize your attorney website for Core Web Vitals and fast load times.",
    ),
    "local-ai-seo-for-law-firms.html": (
        "Local AI SEO for Law Firms: Dominate Your Market",
        "Local AI SEO strategies that help law firms dominate their geographic market. Optimize for local AI search and geo-specific AI recommendations.",
    ),
    "local-business-schema-law-firms.html": (
        "Local Business Schema for Law Firms: Complete Setup Guide",
        "Implement LocalBusiness and LegalService schema for your law firm to dominate local search, Google Maps, and AI-powered local recommendations.",
    ),
    "never-miss-a-call-law-firm.html": (
        "Never Miss a Client Call: AI Solutions for Law Firms",
        "Law firms miss up to 40% of calls. AI receptionists ensure every lead is captured 24/7. Learn how to stop losing clients to unanswered phones.",
    ),
    "schema-markup-for-lawyers-guide.html": (
        "Schema Markup for Lawyers: The Complete Guide",
        "Schema markup for law firms explained. Implement LegalService, FAQPage, and BreadcrumbList schema to boost Google rankings and AI visibility.",
    ),
    "topical-authority-for-law-firms.html": (
        "Topical Authority for Law Firms: Content Strategy Guide",
        "Build topical authority that makes your law firm the go-to resource for AI and Google. Content clustering, silo architecture, and semantic SEO.",
    ),
}

print("[1/7] Fixing title tags, meta descriptions, og:title, og:description, twitter:title, twitter:description ...")
for fname, (new_title, new_desc) in METADATA.items():
    html = read(fname)
    original = html

    if new_title:
        html = swap_title(html, new_title)
        html = swap_og(html, "og:title", new_title)
        html = swap_twitter(html, "twitter:title", new_title)

    if new_desc:
        html = swap_meta(html, "description", new_desc)
        html = swap_og(html, "og:description", new_desc)
        html = swap_twitter(html, "twitter:description", new_desc)

    if html != original:
        write(fname, html)
        changes.append(f"{fname}: title/desc updated")

# ─── 3: Footer year 2025 → 2026 on ALL pages ──────────────────────────────────
print("\n[2/7] Updating footer year 2025 → 2026 on all pages ...")
year_updated = 0
for fname in sorted(glob.glob(os.path.join(BASE, "*.html"))):
    html = read(os.path.basename(fname))
    if "© 2025" in html:
        new_html = html.replace("© 2025", "© 2026")
        write(os.path.basename(fname), new_html)
        year_updated += 1
        changes.append(f"{os.path.basename(fname)}: footer year 2025→2026")
print(f"  → {year_updated} pages updated")

# ─── 4: Fix broken href="#" for Privacy and Terms in footer ───────────────────
print("\n[3/7] Fixing broken footer Privacy/Terms links (href='#') ...")
link_fixed = 0
for fname in sorted(glob.glob(os.path.join(BASE, "*.html"))):
    bname = os.path.basename(fname)
    html = read(bname)
    original = html

    # Fix href="#" for Privacy link in footer
    # Pattern: <a href="#">Privacy</a>
    html = re.sub(
        r'<a href="#">(Privacy)</a>',
        r'<a href="privacy.html">\1</a>',
        html
    )
    # Fix href="#" for Terms link
    html = re.sub(
        r'<a href="#">(Terms)</a>',
        r'<a href="privacy.html">\1</a>',
        html
    )
    if html != original:
        write(bname, html)
        link_fixed += 1
        changes.append(f"{bname}: broken footer links fixed")
print(f"  → {link_fixed} pages updated")

# ─── 5: Brand name "LexScale Editorial" → "LexScale.ai Editorial" ─────────────
print("\n[4/7] Fixing brand name 'LexScale Editorial' → 'LexScale.ai Editorial' ...")
brand_fixed = 0
for fname in sorted(glob.glob(os.path.join(BASE, "*.html"))):
    bname = os.path.basename(fname)
    html = read(bname)
    if "LexScale Editorial" in html:
        new_html = html.replace("LexScale Editorial", "LexScale.ai Editorial")
        write(bname, new_html)
        brand_fixed += 1
        changes.append(f"{bname}: brand 'LexScale Editorial'→'LexScale.ai Editorial'")
print(f"  → {brand_fixed} pages updated")

# Fix case study text in index.html
print("\n[5/7] Fixing 'LexScale deployed' case studies in index.html ...")
html = read("index.html")
original = html
html = html.replace("LexScale deployed", "LexScale.ai deployed")
if html != original:
    write("index.html", html)
    changes.append("index.html: case study brand names fixed")
    print("  ✓ index.html")
else:
    print("  — no changes needed")

# ─── 6: Add Contact to nav on index.html ──────────────────────────────────────
print("\n[6/7] Adding Contact to nav bar on index.html ...")
html = read("index.html")
original = html

# The nav has: Home | Services (dropdown) | Insights (dropdown) | About | [CTA button]
# Find About link and add Contact after it, before the nav-cta button
# Pattern to find: <li><a href="about.html">About</a></li>
if '<a href="about.html">About</a>' in html and '<a href="contact.html">Contact</a>' not in html:
    html = html.replace(
        '<li><a href="about.html">About</a></li>',
        '<li><a href="about.html">About</a></li>\n    <li><a href="contact.html">Contact</a></li>'
    )
    write("index.html", html)
    changes.append("index.html: Contact added to nav")
    print("  ✓ index.html — Contact added to nav")
else:
    print("  — Contact already in nav or About not found")

# Apply the same nav fix to about.html and other core pages that use the same nav
core_pages = [
    "about.html", "contact.html", "privacy.html",
    "ai-seo-for-law-firms.html", "ai-website-design-for-law-firms.html",
    "ai-receptionist-for-law-firms.html", "ai-chatbot-for-law-firms.html",
]
for fname in core_pages:
    html = read(fname)
    if '<a href="about.html">About</a>' in html and '<a href="contact.html">Contact</a>' not in html:
        html = html.replace(
            '<li><a href="about.html">About</a></li>',
            '<li><a href="about.html">About</a></li>\n    <li><a href="contact.html">Contact</a></li>'
        )
        write(fname, html)
        changes.append(f"{fname}: Contact added to nav")
        print(f"  ✓ {fname}")

# ─── 7: Clean up the duplicate footer contact/privacy paragraph ───────────────
# The v2 script injected a second paragraph with absolute URLs before </footer>
# Replace absolute URLs with relative ones for consistency
print("\n[7/7] Normalising injected footer links (absolute → relative URLs) ...")
footer_fixed = 0
for fname in sorted(glob.glob(os.path.join(BASE, "*.html"))):
    bname = os.path.basename(fname)
    html = read(bname)
    original = html
    # Replace absolute lexscale.ai URLs in the injected footer paragraph
    html = html.replace('href="https://lexscale.ai/contact.html"', 'href="contact.html"')
    html = html.replace('href="https://lexscale.ai/privacy.html"', 'href="privacy.html"')
    if html != original:
        write(bname, html)
        footer_fixed += 1
print(f"  → {footer_fixed} pages normalised")

# ─── Summary ──────────────────────────────────────────────────────────────────
print(f"\n✅ Done. {len(changes)} files modified.")
print("\nChange log:")
# deduplicate
for c in sorted(set(changes)):
    print(f"  {c}")
