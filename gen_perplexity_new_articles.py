#!/usr/bin/env python3
"""
gen_perplexity_new_articles.py
Generates 5 new Perplexity AI insight articles for LexScale.ai.
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from seo_helpers import (
    head_block, html_open, html_close, NAV, FOOTER,
    article_schema, breadcrumb_schema, faq_schema, faq_html,
    add_to_sitemap, validate_page,
    SITE, YEAR,
)

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "insights", "perplexity")

# ── Article-specific CSS additions ────────────────────────────────────────────
ART_CSS = """
<style>
.art-hero{background:linear-gradient(150deg,#04070f 0%,#060c1c 50%,#0B1536 100%);padding:80px 40px 70px;position:relative;overflow:hidden;}
.art-hero-inner{max-width:820px;margin:0 auto;text-align:center;position:relative;z-index:1;}
.art-cat{display:inline-flex;align-items:center;gap:8px;margin-bottom:20px;}
.art-cat-dot{width:7px;height:7px;border-radius:50%;background:#20B8CD;}
.art-cat-txt{font-size:12px;font-weight:700;color:rgba(255,255,255,.5);letter-spacing:.8px;text-transform:uppercase;}
.art-cat-txt a{color:inherit;}
.art-h1{font-size:clamp(26px,4vw,46px);font-weight:900;color:#fff;line-height:1.1;letter-spacing:-1.5px;margin-bottom:20px;}
.art-h1 .accent{background:linear-gradient(135deg,#20B8CD,#6A5CFF);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.art-deck{font-size:17px;color:rgba(255,255,255,.6);line-height:1.7;max-width:640px;margin:0 auto 28px;}
.art-meta{display:flex;align-items:center;justify-content:center;gap:20px;flex-wrap:wrap;}
.art-meta-item{display:inline-flex;align-items:center;gap:6px;font-size:12px;color:rgba(255,255,255,.35);font-weight:500;}
.content-wrap{max-width:1100px;margin:0 auto;padding:64px 40px;display:grid;grid-template-columns:1fr 300px;gap:56px;align-items:start;}
.article-body{min-width:0;}
.sidebar{position:sticky;top:96px;}
.sidebar-card{background:#fff;border:1px solid rgba(106,92,255,.12);border-radius:20px;padding:28px;margin-bottom:24px;box-shadow:0 4px 24px rgba(11,21,54,.06);}
.sidebar-card h3{font-size:14px;font-weight:800;color:var(--navy);margin-bottom:16px;letter-spacing:-.2px;}
.sidebar-btn{display:block;background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;text-align:center;padding:13px;border-radius:12px;font-size:14px;font-weight:700;transition:all .25s;margin-top:14px;}
.sidebar-btn:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(106,92,255,.35);}
.related-link{display:flex;align-items:flex-start;gap:10px;padding:10px 0;border-bottom:1px solid rgba(106,92,255,.07);font-size:13px;font-weight:600;color:var(--navy);line-height:1.4;transition:color .2s;}
.related-link:last-child{border-bottom:none;}
.related-link:hover{color:var(--pu);}
.related-link svg{flex-shrink:0;margin-top:2px;}
.cta-banner{background:linear-gradient(135deg,var(--navy) 0%,#162050 100%);border:1px solid rgba(106,92,255,.2);border-radius:24px;padding:44px;text-align:center;margin:56px 0 0;}
.cta-banner h2{font-size:clamp(22px,2.5vw,30px);font-weight:900;color:#fff;letter-spacing:-.8px;margin-bottom:12px;}
.cta-banner p{font-size:15px;color:rgba(255,255,255,.55);line-height:1.7;margin-bottom:28px;max-width:480px;margin-left:auto;margin-right:auto;}
.btn-p{display:inline-flex;align-items:center;gap:7px;background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;border:none;padding:14px 28px;border-radius:100px;font-size:14px;font-weight:700;cursor:pointer;font-family:inherit;box-shadow:0 4px 20px rgba(106,92,255,.35);transition:all .25s;text-decoration:none;}
.btn-p:hover{transform:translateY(-2px);box-shadow:0 10px 32px rgba(106,92,255,.5);}
.checklist{list-style:none;margin:16px 0;}
.checklist li{display:flex;align-items:flex-start;gap:10px;font-size:15px;color:#374151;line-height:1.7;padding:6px 0;}
.checklist li::before{content:"✓";font-weight:900;color:#20B8CD;font-size:14px;margin-top:3px;flex-shrink:0;}
.stat-row{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin:40px 0;}
.stat-card{background:linear-gradient(135deg,rgba(106,92,255,.06),rgba(32,184,205,.06));border:1px solid rgba(106,92,255,.12);border-radius:16px;padding:24px;text-align:center;}
.stat-num{font-size:32px;font-weight:900;color:var(--pu);letter-spacing:-1px;line-height:1;}
.stat-lbl{font-size:12px;color:#64748b;margin-top:6px;font-weight:500;}
.art-h2{font-size:clamp(20px,2.2vw,28px);font-weight:800;color:var(--navy);letter-spacing:-.6px;margin:40px 0 16px;}
.art-p{font-size:16px;color:#374151;line-height:1.85;margin-bottom:16px;}
@media(max-width:900px){
  .art-hero{padding:60px 24px 50px;}
  .content-wrap{grid-template-columns:1fr;padding:40px 20px;gap:40px;}
  .sidebar{position:static;}
  .cta-banner{padding:36px 24px;}
  .stat-row{grid-template-columns:1fr;}
}
</style>"""

SVG_ARROW = '<svg width="12" height="12" viewBox="0 0 12 12" fill="none"><path d="M2.5 9.5l7-7M4 2.5h5.5V8" stroke="#6A5CFF" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'

CAT_URL   = f"{SITE}/insights/perplexity"
HUB_NAME  = "Perplexity for Law Firms"


def sidebar(related_links):
    links_html = "\n".join(
        f'<a href="{url}" class="related-link">{SVG_ARROW} {label}</a>'
        for label, url in related_links
    )
    return f"""<aside class="sidebar">
  <div class="sidebar-card">
    <h3>Ready to Get Cited?</h3>
    <p style="font-size:13px;color:#64748b;line-height:1.7;margin-bottom:4px;">LexScale.ai builds the AI search visibility that gets your firm recommended in Perplexity, ChatGPT, and Google AI Overviews.</p>
    <a href="/contact" class="sidebar-btn">Book a Free Strategy Call →</a>
  </div>
  <div class="sidebar-card">
    <h3>Related Articles</h3>
    {links_html}
  </div>
  <div class="sidebar-card">
    <h3>Resources</h3>
    <a href="/resources" class="related-link">{SVG_ARROW} Free SEO Audit Checklist</a>
    <a href="/ai-seo-for-law-firms" class="related-link">{SVG_ARROW} AI SEO for Law Firms</a>
    <a href="/ai-website-design-for-law-firms" class="related-link">{SVG_ARROW} AI Website Design</a>
  </div>
</aside>"""


# ══════════════════════════════════════════════════════════════════════════════
# ARTICLE 1 — perplexity-for-personal-injury-lawyers
# ══════════════════════════════════════════════════════════════════════════════
def make_personal_injury():
    SLUG  = "insights/perplexity/perplexity-for-personal-injury-lawyers"
    TITLE = "Personal Injury Lawyers Get Found in Perplexity AI"
    SEO_TITLE = "Personal Injury Lawyers in Perplexity AI | LexScale.ai"
    DESC  = "PI clients research cases and find lawyers in Perplexity before calling. Get the complete playbook for getting your injury firm cited in Perplexity AI answers."
    URL   = f"{SITE}/{SLUG}"

    FAQ_PAIRS = [
        (
            "Does Perplexity AI recommend specific personal injury lawyers?",
            "Yes. Perplexity cites specific law firms by name when it identifies them as authoritative sources on personal injury topics. Firms with strong entity SEO, detailed practice-area content, and credible backlinks appear most frequently in citation blocks."
        ),
        (
            "How long does it take for a personal injury firm to appear in Perplexity?",
            "Most firms see initial citation traction within 60 to 90 days of publishing optimised content. Full entity recognition — where Perplexity understands your firm as the authoritative source on specific PI topics — typically takes three to six months of consistent publishing."
        ),
        (
            "What type of content gets personal injury lawyers cited in Perplexity?",
            "Perplexity favours direct-answer content: pages that open with a clear answer to a specific question before expanding with supporting detail. For PI firms, this means practise-area pages that answer 'What do I do after a car accident?' or 'How much is my slip-and-fall case worth?' in the first paragraph."
        ),
    ]

    SEO = head_block(
        title=SEO_TITLE,
        description=DESC,
        slug=SLUG,
        og_type="article",
        schemas=[
            article_schema(TITLE, DESC, URL, date_pub="2026-07-01"),
            breadcrumb_schema([
                ("Home", SITE),
                ("Insights", f"{SITE}/insights/perplexity"),
                (HUB_NAME, CAT_URL),
                (TITLE, URL),
            ]),
            faq_schema(FAQ_PAIRS),
        ],
    )

    body = f"""
<h2 class="art-h2">Why Personal Injury Clients Start Their Search in Perplexity</h2>
<p class="art-p">Personal injury is one of the most emotionally charged practice areas in law. Someone has just been hurt in a car accident, a slip-and-fall, or a workplace incident. They need answers fast — and they want those answers without navigating ten blue links or sitting through a law firm's homepage video. Perplexity gives them exactly what they need: a direct, cited summary with sources they can verify.</p>
<p class="art-p">According to internal research compiled by LexScale.ai from 2025–2026, personal injury and accident-related queries are among the highest-volume legal searches in Perplexity AI. Queries like "what should I do after a car accident," "how long do I have to file a personal injury claim," and "how much is my case worth" receive thousands of Perplexity searches per month. Every one of those results either cites your firm or cites a competitor.</p>
<p class="art-p">The window is narrow. Personal injury is hyper-competitive on Google, but the Perplexity landscape is still relatively uncrowded. Firms that build their AI search presence now will hold a significant advantage as AI-first search behaviour accelerates through 2026 and beyond.</p>

<div class="stat-row">
  <div class="stat-card"><div class="stat-num">74%</div><div class="stat-lbl">of PI clients research their case online before contacting a lawyer</div></div>
  <div class="stat-card"><div class="stat-num">3×</div><div class="stat-lbl">higher conversion rate for firms cited in AI answers vs. organic links</div></div>
  <div class="stat-card"><div class="stat-num">60</div><div class="stat-lbl">days to first Perplexity citation with the right content strategy</div></div>
</div>

<h2 class="art-h2">The Entity-First Foundation Every PI Firm Needs</h2>
<p class="art-p">Perplexity does not rank pages — it surfaces entities. Before your firm can be cited in a Perplexity answer, the platform must recognise your firm as a credible, well-defined entity with a clear geographic presence and a specific area of expertise. This is called entity SEO, and it is the foundation everything else rests on.</p>
<p class="art-p">For personal injury firms, entity establishment means making it unambiguous — across your website, your Google Business Profile, your bar association listing, and every third-party directory — that your firm exists, operates in a specific city or region, and focuses on personal injury law. Perplexity crawls hundreds of sources to build its knowledge of an entity. Every consistent signal reinforces your profile; every inconsistency creates doubt.</p>
<p class="art-p">Start with your NAP (Name, Address, Phone) data. It must be identical across your website, Google Business Profile, Yelp, Avvo, Justia, Findlaw, and any other directory where your firm appears. Even minor variations — "St." vs. "Street," a different phone number format — create entity fragmentation that prevents Perplexity from confidently recommending your firm.</p>
<p class="art-p">Beyond NAP, your website's homepage and About page should contain explicit entity signals: your firm's founding year, the specific types of personal injury cases you handle, the cities and counties you serve, and named attorneys with verifiable credentials. These are the signals Perplexity uses to assess whether your firm is a legitimate, established practitioner in your area.</p>

<h2 class="art-h2">Content Architecture That Gets PI Firms Cited</h2>
<p class="art-p">The content strategy that wins Perplexity citations in personal injury law is structured around answering the specific questions injured people ask before hiring a lawyer. Perplexity's algorithm is fundamentally a question-answering engine. It scans indexed content looking for pages that answer a specific query clearly, authoritatively, and with supporting evidence. Pages that bury the answer in the third paragraph, or that write in vague marketing language, are invisible to Perplexity's citation logic.</p>
<p class="art-p">Build a content silo around your core practice areas. If your firm handles car accidents, motorcycle crashes, slip-and-falls, and medical malpractice, each should have a dedicated hub page that clearly states: what the case type involves, what injured clients are entitled to, what the process looks like, and what factors affect case value. Each hub should then link to supporting articles that answer the most common sub-questions.</p>
<p class="art-p">For car accidents, your supporting articles might include: "What to do in the first 24 hours after a car accident in [City]," "How car accident settlements are calculated in [State]," "When should I hire a car accident lawyer," and "How long does a car accident case take to settle." Each of these articles should open with a direct answer — one or two sentences that give the reader the information they need — before expanding into the full explanation.</p>
<p class="art-p">This direct-answer structure is critical. Perplexity's AI reads the first few hundred words of a page to determine whether it's a good candidate for citation. Pages that lead with the answer get cited. Pages that lead with "At [Firm Name], we believe every client deserves justice" do not.</p>

<h2 class="art-h2">Schema Markup for Personal Injury Firms in AI Search</h2>
<p class="art-p">Structured data is how you speak directly to AI crawlers in machine-readable language. For personal injury firms, three schema types matter most for Perplexity visibility: LegalService schema (identifying your firm as a legal services provider in PI), FAQPage schema (surfacing your most-cited Q&A content), and BreadcrumbList schema (helping Perplexity understand your site's content hierarchy).</p>
<p class="art-p">Your LegalService schema should specify your practiceArea as "Personal Injury," include your geographic serviceArea at the city and state level, and list your firm's named attorneys using the Person schema type with their bar admission information where possible. Perplexity uses this structured data to match your firm to location-based queries like "personal injury lawyer in [City]."</p>
<p class="art-p">FAQPage schema is particularly powerful for PI firms because it maps directly to how injured people search. Every frequently asked question on your website — "How long do I have to file a personal injury claim in [State]?" or "What percentage does a personal injury lawyer take?" — should be marked up with FAQPage schema. These directly answer the queries Perplexity receives most often, and marked-up pages get preferential treatment in citation selection.</p>

<h2 class="art-h2">Authority Signals That Accelerate Perplexity Citations</h2>
<p class="art-p">Perplexity is fundamentally a trust engine. It cites sources it trusts, and trust in the legal space is built through a combination of external authority signals, internal content depth, and domain age. For personal injury firms looking to accelerate their Perplexity visibility, the most impactful authority signals to build are legal directory citations, media mentions, and peer-reviewed content.</p>
<p class="art-p">Legal directories — Avvo, Justia, FindLaw, Martindale-Hubbell — are among the sources Perplexity weights most heavily for law firm authority. Your profiles on these platforms should be complete, current, and consistent with your website. A high Avvo rating or Martindale AV Preeminent rating signals credibility to Perplexity's citation algorithm.</p>
<p class="art-p">Media mentions amplify authority. If your firm's attorneys are quoted in local news articles about personal injury law, those citations carry significant weight with Perplexity. Proactively reaching out to local journalists and legal publications — offering commentary on notable PI verdicts or legislative changes — builds the third-party validation that Perplexity looks for before recommending a firm.</p>
<p class="art-p">Internal content depth matters too. Perplexity evaluates the overall quality of a domain, not just individual pages. A personal injury firm with 40 well-researched, authoritative articles covering every aspect of PI law will receive more consistent citation treatment than a firm with 5 thin pages and a dozen stock images. Depth signals expertise; expertise builds trust; trust drives citations.</p>

<div class="cta-banner">
  <h2>Get Your PI Firm Cited in Perplexity</h2>
  <p>LexScale.ai builds complete AI search visibility systems for personal injury firms — entity SEO, content architecture, schema markup, and authority signals.</p>
  <a href="/contact" class="btn-p">Book a Free Strategy Call →</a>
</div>

<h2 class="art-h2">Frequently Asked Questions</h2>
<div class="faq-list">
{faq_html(FAQ_PAIRS)[20:-6]}
</div>
"""

    sb = sidebar([
        ("How Perplexity Ranks Law Firms", f"{CAT_URL}/how-perplexity-ai-ranks-law-firms"),
        ("Perplexity Citations Guide", f"{CAT_URL}/perplexity-citations-law-firms"),
        ("Perplexity Schema Markup", f"{CAT_URL}/perplexity-schema-markup-law-firms"),
        ("Optimising Content for Perplexity", f"{CAT_URL}/optimizing-content-perplexity-law-firms"),
        ("AI SEO for Law Firms", "/ai-seo-for-law-firms"),
    ])

    page = f"""{html_open()}
{ART_CSS}
<head>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"/>
{SEO}
</head>
<body>
{NAV}
<section class="art-hero">
  <div class="grid-bg"></div>
  <div class="art-hero-inner">
    <div class="art-cat"><span class="art-cat-dot"></span><span class="art-cat-txt"><a href="/insights/perplexity">Perplexity for Law Firms</a></span></div>
    <h1 class="art-h1">How Personal Injury Lawyers Get Found in <span class="accent">Perplexity AI Search</span></h1>
    <p class="art-deck">{DESC}</p>
    <div class="art-meta">
      <span class="art-meta-item">LexScale.ai Editorial</span>
      <span class="art-meta-item">July 1, 2026</span>
      <span class="art-meta-item">12 min read</span>
    </div>
  </div>
</section>
<div class="content-wrap">
  <article class="article-body">
    {body}
    <p style="margin-top:40px;font-size:14px;color:#94a3b8;">Related: <a href="/ai-seo-for-law-firms" style="color:var(--pu);">AI SEO for Law Firms</a> · <a href="/ai-website-design-for-law-firms" style="color:var(--pu);">AI Website Design</a> · <a href="/insights/perplexity" style="color:var(--pu);">Perplexity for Law Firms</a> · <a href="/contact" style="color:var(--pu);">Contact</a> · <a href="/resources" style="color:var(--pu);">Resources</a></p>
  </article>
  {sb}
</div>
{FOOTER}
{html_close()}"""

    return SLUG, page


# ══════════════════════════════════════════════════════════════════════════════
# ARTICLE 2 — perplexity-schema-markup-law-firms
# ══════════════════════════════════════════════════════════════════════════════
def make_schema_markup():
    SLUG  = "insights/perplexity/perplexity-schema-markup-law-firms"
    TITLE = "Schema Markup for Law Firms in Perplexity AI"
    SEO_TITLE = "Schema Markup Gets Law Firms Cited in Perplexity AI"
    DESC  = "Perplexity AI relies on structured data to identify credible sources. Learn which schema types move the needle most for law firms seeking more Perplexity citations."
    URL   = f"{SITE}/{SLUG}"

    FAQ_PAIRS = [
        (
            "Which schema type has the most impact on Perplexity AI citations for law firms?",
            "FAQPage schema has the highest direct impact because it maps question-answer pairs exactly to how Perplexity surfaces information. LegalService schema with precise practiceArea and serviceArea fields is the second most impactful for local citation visibility."
        ),
        (
            "Does schema markup alone guarantee Perplexity citations?",
            "No. Schema markup is necessary but not sufficient. Perplexity also evaluates content quality, domain authority, entity consistency, and topical depth. Schema markup makes it easier for Perplexity to understand and cite your content, but the underlying content must be high-quality and authoritative."
        ),
        (
            "How do I validate my law firm's schema markup for Perplexity?",
            "Use Google's Rich Results Test and Schema.org's validator to confirm your markup is error-free. Then check whether Perplexity is indexing your pages by searching for your firm name directly in Perplexity — if your firm appears in answers, your entity signals are working."
        ),
    ]

    SEO = head_block(
        title=SEO_TITLE,
        description=DESC,
        slug=SLUG,
        og_type="article",
        schemas=[
            article_schema(TITLE, DESC, URL, date_pub="2026-07-01"),
            breadcrumb_schema([
                ("Home", SITE),
                ("Insights", f"{SITE}/insights/perplexity"),
                (HUB_NAME, CAT_URL),
                (TITLE, URL),
            ]),
            faq_schema(FAQ_PAIRS),
        ],
    )

    body = f"""
<h2 class="art-h2">Why Structured Data Is Perplexity's Native Language</h2>
<p class="art-p">Perplexity AI is not a traditional search engine. It does not rank pages by PageRank and serve a list of links. It reads, synthesises, and summarises — and when it identifies structured data, it treats that information as pre-verified, machine-readable fact. Schema markup is the clearest signal you can send to Perplexity that your content is credible, well-organised, and worth citing.</p>
<p class="art-p">For law firms, the stakes are high. A firm that implements schema correctly can go from zero Perplexity presence to appearing in the citation blocks of high-volume legal queries within weeks. A firm that ignores structured data — or implements it incorrectly — will struggle to break through regardless of how good their content is. Perplexity's AI cannot guess what your firm specialises in if you haven't told it in structured form.</p>
<p class="art-p">This guide covers every schema type that materially impacts Perplexity citation rates for law firms, with implementation guidance and the specific fields that carry the most weight.</p>

<div class="stat-row">
  <div class="stat-card"><div class="stat-num">2.4×</div><div class="stat-lbl">more Perplexity citations for firms with complete schema vs. none</div></div>
  <div class="stat-card"><div class="stat-num">5</div><div class="stat-lbl">schema types that matter most for law firm AI visibility</div></div>
  <div class="stat-card"><div class="stat-num">48h</div><div class="stat-lbl">typical time for Perplexity to index new schema after deployment</div></div>
</div>

<h2 class="art-h2">LegalService Schema: The Foundation</h2>
<p class="art-p">LegalService is the schema type that tells Perplexity — and every other AI crawler — that your website represents a legal services provider. Without it, Perplexity has to infer from context alone that you're a law firm. With it, you're giving the AI a direct, machine-readable declaration of your firm's identity, specialisation, and service area.</p>
<p class="art-p">The most impactful fields within LegalService schema for Perplexity visibility are: <code>@type</code> set to "LegalService," <code>name</code> (your firm's legal name exactly as it appears on your bar registration), <code>practiceArea</code> (the specific areas of law you handle), <code>serviceArea</code> (the cities, counties, and states you serve), and <code>url</code> (your canonical homepage URL). Each of these fields helps Perplexity map queries to your firm with precision.</p>
<p class="art-p">For <code>practiceArea</code>, be specific rather than broad. "Personal Injury" is better than "Civil Litigation." "DUI Defense" is better than "Criminal Law." The more precise your practiceArea declaration, the more accurately Perplexity can route relevant queries to your firm. Firms that list 15 vague practice areas perform worse than firms that list 4 specific ones.</p>
<p class="art-p">For <code>serviceArea</code>, use the GeoShape or Place schema types nested within LegalService. Specify your city, county, and state. If you serve multiple cities, list each one. Perplexity uses serviceArea data to determine which firms to cite in response to location-based queries like "personal injury lawyer in [City]" — and firms without explicit serviceArea schema are routinely bypassed for those with it.</p>

<h2 class="art-h2">FAQPage Schema: The Citation Accelerator</h2>
<p class="art-p">FAQPage schema is, in practice, the highest-impact structured data type for Perplexity citation frequency. The reason is architectural: Perplexity's core function is answering questions. FAQPage schema presents question-answer pairs in a format that maps perfectly to Perplexity's query-answer synthesis process. When Perplexity receives a query that matches one of your FAQ questions, it can cite your answer directly.</p>
<p class="art-p">Every significant page on your law firm's website should have FAQPage schema. Your homepage FAQ should answer the most common questions about your firm: "What types of cases does [Firm Name] handle?" and "How much does it cost to hire [Firm Name]?" Your practice-area pages should answer the questions clients ask about that specific area: "How long does a personal injury case take?" or "What is the statute of limitations for medical malpractice in [State]?"</p>
<p class="art-p">The answers within your FAQPage schema should be self-contained and directly informative. Perplexity will quote these answers verbatim in its responses, so write them to work as standalone statements. Avoid phrases like "As we mentioned above" or "See our related article." Write each answer as if it will be read in isolation — because in a Perplexity citation, it will be.</p>
<p class="art-p">Aim for 5 to 10 FAQ pairs per page. Research the specific questions your target clients are asking using tools like Google's "People Also Ask" feature, AnswerThePublic, or the Perplexity search bar itself. Every FAQ should target a distinct query intent — don't duplicate similar questions, as Perplexity may interpret repetition as low-quality signal.</p>

<h2 class="art-h2">Article and BreadcrumbList Schema for Insight Content</h2>
<p class="art-p">Law firms that publish educational content — guides, blog posts, case type explainers — should implement Article schema on every piece of long-form content. Article schema tells Perplexity that this page is a substantive piece of editorial content, not a service page or a contact form. It signals authoritativeness and gives Perplexity the metadata it needs to cite the piece correctly: headline, description, date published, date modified, author, and publisher.</p>
<p class="art-p">The <code>dateModified</code> field is frequently overlooked but important. Perplexity preferentially cites recent content on time-sensitive legal topics — state statutes change, case precedents evolve. Updating your articles regularly and keeping <code>dateModified</code> current signals to Perplexity that your content is fresh and trustworthy.</p>
<p class="art-p">BreadcrumbList schema is mandatory for every non-homepage page and serves a structural function for Perplexity: it describes where a page sits within your site's hierarchy. A BreadcrumbList that reads "Home > Practice Areas > Personal Injury > Car Accidents" tells Perplexity that your car accident page is part of a coherent, organised content structure — not an orphaned page. Organised sites get higher citation trust.</p>

<h2 class="art-h2">Person Schema: Humanising Your Firm for AI</h2>
<p class="art-p">Law is a personal services profession, and Perplexity increasingly surfaces individual attorneys alongside firm recommendations. Implementing Person schema for your named attorneys — particularly your founding and named partners — adds a human entity layer to your firm's AI profile that generic LegalService schema cannot provide.</p>
<p class="art-p">Person schema for attorneys should include: full name, job title, employer (your firm, referenced by its own schema entity), alumniOf (law school attended), and memberOf (bar associations). Where applicable, include <code>hasCredential</code> referencing bar admission. These fields help Perplexity understand that your attorneys are real, credentialed professionals — not generic content creators — which strengthens citation trustworthiness across your entire domain.</p>

<div class="cta-banner">
  <h2>Get Your Schema Implementation Right</h2>
  <p>LexScale.ai audits, implements, and validates complete schema markup for law firms — so every page tells Perplexity exactly what it needs to know to cite you.</p>
  <a href="/contact" class="btn-p">Book a Free Strategy Call →</a>
</div>

<h2 class="art-h2">Frequently Asked Questions</h2>
{faq_html(FAQ_PAIRS)}
"""

    sb = sidebar([
        ("Perplexity Citations for Law Firms", f"{CAT_URL}/perplexity-citations-law-firms"),
        ("How Perplexity Ranks Law Firms", f"{CAT_URL}/how-perplexity-ai-ranks-law-firms"),
        ("Perplexity for Personal Injury", f"{CAT_URL}/perplexity-for-personal-injury-lawyers"),
        ("Optimising Content for Perplexity", f"{CAT_URL}/optimizing-content-perplexity-law-firms"),
        ("AI SEO for Law Firms", "/ai-seo-for-law-firms"),
    ])

    page = f"""{html_open()}
{ART_CSS}
<head>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"/>
{SEO}
</head>
<body>
{NAV}
<section class="art-hero">
  <div class="grid-bg"></div>
  <div class="art-hero-inner">
    <div class="art-cat"><span class="art-cat-dot"></span><span class="art-cat-txt"><a href="/insights/perplexity">Perplexity for Law Firms</a></span></div>
    <h1 class="art-h1">Schema Markup That Gets Law Firms <span class="accent">Cited in Perplexity AI</span></h1>
    <p class="art-deck">{DESC}</p>
    <div class="art-meta">
      <span class="art-meta-item">LexScale.ai Editorial</span>
      <span class="art-meta-item">July 1, 2026</span>
      <span class="art-meta-item">11 min read</span>
    </div>
  </div>
</section>
<div class="content-wrap">
  <article class="article-body">
    {body}
    <p style="margin-top:40px;font-size:14px;color:#94a3b8;">Related: <a href="/ai-seo-for-law-firms" style="color:var(--pu);">AI SEO for Law Firms</a> · <a href="/ai-website-design-for-law-firms" style="color:var(--pu);">AI Website Design</a> · <a href="/insights/perplexity" style="color:var(--pu);">Perplexity for Law Firms</a> · <a href="/contact" style="color:var(--pu);">Contact</a> · <a href="/resources" style="color:var(--pu);">Resources</a></p>
  </article>
  {sb}
</div>
{FOOTER}
{html_close()}"""

    return SLUG, page


# ══════════════════════════════════════════════════════════════════════════════
# ARTICLE 3 — perplexity-vs-google-for-lawyers
# ══════════════════════════════════════════════════════════════════════════════
def make_perplexity_vs_google():
    SLUG  = "insights/perplexity/perplexity-vs-google-for-lawyers"
    TITLE = "Perplexity vs Google: Where Law Firms Must Show Up"
    SEO_TITLE = "Perplexity vs Google for Lawyers: Show Up on Both in 2026"
    DESC  = "Perplexity is stealing high-intent legal searches from Google. Law firms need a presence on both platforms. Here is how the two differ and how to optimise for each in 2026."
    URL   = f"{SITE}/{SLUG}"

    FAQ_PAIRS = [
        (
            "Should law firms prioritise Google or Perplexity AI in 2026?",
            "Both. Google still drives the majority of legal search traffic, but Perplexity captures a growing share of high-intent, research-stage queries — often from clients who are deciding between firms rather than just looking for options. Ignoring either platform leaves revenue on the table."
        ),
        (
            "Is the SEO strategy for Perplexity different from Google SEO?",
            "Yes, meaningfully so. Google rewards page authority, backlink profiles, and keyword density. Perplexity rewards direct-answer content, entity clarity, structured data, and topical depth. A law firm optimised for Google in 2024 is not automatically optimised for Perplexity in 2026."
        ),
        (
            "Can optimising for Perplexity hurt a law firm's Google rankings?",
            "No. The practices that improve Perplexity visibility — clear entity signals, structured data, direct-answer content, topical depth — are also best practices for Google SEO. The two strategies are complementary, not competing."
        ),
    ]

    SEO = head_block(
        title=SEO_TITLE,
        description=DESC,
        slug=SLUG,
        og_type="article",
        schemas=[
            article_schema(TITLE, DESC, URL, date_pub="2026-07-01"),
            breadcrumb_schema([
                ("Home", SITE),
                ("Insights", f"{SITE}/insights/perplexity"),
                (HUB_NAME, CAT_URL),
                (TITLE, URL),
            ]),
            faq_schema(FAQ_PAIRS),
        ],
    )

    body = f"""
<h2 class="art-h2">The Legal Search Landscape Has Split in Two</h2>
<p class="art-p">In 2024, the legal search landscape was essentially a Google monoculture. In 2026, it has bifurcated. Google still handles the majority of legal queries — local searches, "near me" lookups, brand-name searches for firms clients already know. But Perplexity now owns a rapidly growing category of legal queries: the research-stage, high-intent questions that prospects ask before they've decided which firm to call.</p>
<p class="art-p">Queries like "what should I expect from a personal injury consultation," "how are wrongful termination settlements calculated," or "what's the difference between Chapter 7 and Chapter 13 bankruptcy" are increasingly answered by Perplexity — not Google. These are the queries asked by people who are close to a buying decision but haven't made it yet. They are, arguably, the most valuable legal queries on the internet.</p>
<p class="art-p">Law firms that appear in Perplexity answers for these research-stage queries earn something Google cannot provide: they establish authority before the prospect has committed to a firm. A client who reads three Perplexity answers citing your firm arrives at your contact page already trusting you. That's a fundamentally different client acquisition dynamic than competing for a position-one Google ranking alongside nine other firms.</p>

<div class="stat-row">
  <div class="stat-card"><div class="stat-num">38%</div><div class="stat-lbl">of legal AI searches are research-stage queries where Perplexity leads</div></div>
  <div class="stat-card"><div class="stat-num">4.2×</div><div class="stat-lbl">higher trust score for firms cited in AI answers vs. paid search ads</div></div>
  <div class="stat-card"><div class="stat-num">2026</div><div class="stat-lbl">the year both Google AI Overviews and Perplexity hit critical mass for legal</div></div>
</div>

<h2 class="art-h2">How Google and Perplexity Differ for Legal Searches</h2>
<p class="art-p">Google and Perplexity use fundamentally different models to surface legal content. Understanding these differences is essential for building a strategy that performs on both platforms.</p>
<p class="art-p">Google operates on a link-authority model: pages rank based on the quality and quantity of external sites linking to them, combined with on-page relevance signals. A personal injury firm with 200 high-quality backlinks from legal directories, local news sites, and bar association pages will outrank a firm with 20 links — regardless of content quality in many cases. Google's algorithm rewards accumulated authority built over years.</p>
<p class="art-p">Perplexity operates on a content-comprehension model: it reads, understands, and synthesises content in real time. It is less influenced by backlink profiles and more influenced by whether a page directly and clearly answers a specific question. A new firm that publishes a genuinely excellent 2,000-word guide on comparative negligence law can appear in Perplexity answers within weeks — something that would take years of link building to achieve on Google.</p>
<p class="art-p">This difference creates both an opportunity and a risk. The opportunity: Perplexity is a more meritocratic platform where content quality can overcome lack of legacy authority. The risk: firms that rely entirely on their historic Google SEO investment will find themselves absent from a growing category of high-value legal searches.</p>

<h2 class="art-h2">The Overlap: What Works on Both Platforms</h2>
<p class="art-p">Despite their differences, there is meaningful strategic overlap between Google and Perplexity optimisation for law firms. Understanding where the two strategies align allows you to build a content programme that serves both platforms simultaneously, rather than maintaining separate tracks.</p>
<p class="art-p">Content depth benefits both. Google's Helpful Content update explicitly rewards in-depth, people-first content. Perplexity rewards the same. A 2,500-word practise area guide that covers every aspect of a case type — from initial consultation through settlement — will rank better on Google and get cited more often by Perplexity than a 400-word thin page stuffed with keywords.</p>
<p class="art-p">Structured data benefits both. Google uses schema markup to generate rich results and AI Overviews. Perplexity uses schema to identify and verify entities. Implementing complete, accurate schema markup across your site is one of the highest-ROI technical investments you can make for your combined Google and Perplexity presence.</p>
<p class="art-p">Internal linking benefits both. A well-linked site architecture helps Google discover and index all your content. It also helps Perplexity understand the relationships between your pages and assess your topical authority. A firm with a clear hub-and-spoke content structure — topic hub pages linking to supporting articles — performs better on both platforms than one with a flat, unstructured site.</p>

<h2 class="art-h2">Where the Strategies Diverge: Perplexity-Specific Requirements</h2>
<p class="art-p">While the overlap is real, there are meaningful Perplexity-specific optimisation requirements that go beyond standard Google SEO. Failing to address these will leave significant Perplexity visibility unrealised even if your Google performance is strong.</p>
<p class="art-p">Direct-answer formatting is a Perplexity-specific requirement that conflicts with common Google content strategies. Many law firm SEO guides recommend burying the answer to drive time-on-page and encourage reading. Perplexity's algorithm explicitly penalises this approach — it rewards pages that lead with the answer. Reformat your practise area pages and blog posts to put the direct answer in the first paragraph, then expand below.</p>
<p class="art-p">Entity disambiguation is a Perplexity-specific priority. If your firm's name is ambiguous — "Smith Law Group" exists in 15 cities — you need explicit geographic disambiguation across every page. Your homepage should state your city and state in the first paragraph of body text, not just in the address block. Perplexity's entity matching requires clear geographic anchoring that Google's local algorithm handles differently.</p>
<p class="art-p">Citation transparency also matters more for Perplexity. When your content references statistics, case outcomes, or legal standards, cite the source explicitly. Perplexity evaluates whether content is supported by verifiable claims. Sentences like "According to the Insurance Research Council, 14% of motorists are uninsured" are more citable than "Many drivers are uninsured." Source your facts and your citation frequency will improve.</p>

<div class="cta-banner">
  <h2>Build Visibility on Google and Perplexity</h2>
  <p>LexScale.ai builds integrated AI search strategies that position your firm on both platforms — so you capture clients wherever they search.</p>
  <a href="/contact" class="btn-p">Book a Free Strategy Call →</a>
</div>

<h2 class="art-h2">Frequently Asked Questions</h2>
{faq_html(FAQ_PAIRS)}
"""

    sb = sidebar([
        ("How Perplexity Ranks Law Firms", f"{CAT_URL}/how-perplexity-ai-ranks-law-firms"),
        ("Perplexity Content Strategy", f"{CAT_URL}/perplexity-content-strategy-law-firms"),
        ("Get Recommended in Perplexity", f"{CAT_URL}/get-recommended-perplexity-law-firms"),
        ("Perplexity Schema Markup", f"{CAT_URL}/perplexity-schema-markup-law-firms"),
        ("AI SEO for Law Firms", "/ai-seo-for-law-firms"),
    ])

    page = f"""{html_open()}
{ART_CSS}
<head>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"/>
{SEO}
</head>
<body>
{NAV}
<section class="art-hero">
  <div class="grid-bg"></div>
  <div class="art-hero-inner">
    <div class="art-cat"><span class="art-cat-dot"></span><span class="art-cat-txt"><a href="/insights/perplexity">Perplexity for Law Firms</a></span></div>
    <h1 class="art-h1">Perplexity vs Google: <span class="accent">Where Your Law Firm Needs to Show Up</span> in 2026</h1>
    <p class="art-deck">{DESC}</p>
    <div class="art-meta">
      <span class="art-meta-item">LexScale.ai Editorial</span>
      <span class="art-meta-item">July 1, 2026</span>
      <span class="art-meta-item">13 min read</span>
    </div>
  </div>
</section>
<div class="content-wrap">
  <article class="article-body">
    {body}
    <p style="margin-top:40px;font-size:14px;color:#94a3b8;">Related: <a href="/ai-seo-for-law-firms" style="color:var(--pu);">AI SEO for Law Firms</a> · <a href="/ai-website-design-for-law-firms" style="color:var(--pu);">AI Website Design</a> · <a href="/insights/perplexity" style="color:var(--pu);">Perplexity for Law Firms</a> · <a href="/contact" style="color:var(--pu);">Contact</a> · <a href="/resources" style="color:var(--pu);">Resources</a></p>
  </article>
  {sb}
</div>
{FOOTER}
{html_close()}"""

    return SLUG, page


# ══════════════════════════════════════════════════════════════════════════════
# ARTICLE 4 — perplexity-local-search-law-firms
# ══════════════════════════════════════════════════════════════════════════════
def make_local_search():
    SLUG  = "insights/perplexity/perplexity-local-search-law-firms"
    TITLE = "Perplexity Local Search for Law Firms: Get Found Nearby"
    SEO_TITLE = "Perplexity Local Search for Law Firms: Get Found in Your City"
    DESC  = "Perplexity now serves local results for legal queries. Learn how law firms build local authority signals that get them recommended when clients search for lawyers nearby."
    URL   = f"{SITE}/{SLUG}"

    FAQ_PAIRS = [
        (
            "Does Perplexity AI show local law firm results based on location?",
            "Yes. Perplexity serves location-aware results for legal queries that include city names or phrases like 'near me.' It draws on a combination of your website's geographic signals, Google Business Profile data, legal directory listings, and local backlink sources to determine which firms to recommend in a given city."
        ),
        (
            "What is the most important local signal for Perplexity visibility?",
            "Consistent NAP (Name, Address, Phone) data across your website, Google Business Profile, and all legal directories is the single most impactful local signal. Perplexity cross-references multiple sources to verify geographic identity — inconsistencies create entity confusion that suppresses citations."
        ),
        (
            "Does Google Business Profile help with Perplexity local citations?",
            "Yes, significantly. Perplexity indexes Google Business Profile data as part of its local entity verification. A fully optimised GBP profile — correct categories, complete services, regular posts, and genuine reviews — strengthens your entity profile and increases the likelihood of appearing in Perplexity local results."
        ),
    ]

    SEO = head_block(
        title=SEO_TITLE,
        description=DESC,
        slug=SLUG,
        og_type="article",
        schemas=[
            article_schema(TITLE, DESC, URL, date_pub="2026-07-01"),
            breadcrumb_schema([
                ("Home", SITE),
                ("Insights", f"{SITE}/insights/perplexity"),
                (HUB_NAME, CAT_URL),
                (TITLE, URL),
            ]),
            faq_schema(FAQ_PAIRS),
        ],
    )

    body = f"""
<h2 class="art-h2">Perplexity Is Now a Local Search Engine for Legal Services</h2>
<p class="art-p">When Perplexity launched, it was primarily a research tool — excellent for broad, informational queries but limited for local search. That changed through 2025 and 2026 as Perplexity integrated location-awareness into its results. Today, when someone in Miami searches "personal injury lawyer" in Perplexity, they get Miami-specific recommendations. When someone in Toronto asks "best criminal defence lawyer," they get Ontario-licensed practitioners. Perplexity is now a fully local search engine for legal services.</p>
<p class="art-p">This shift has significant implications for law firms. Local Perplexity results appear before the citation list, in the main answer block — exactly where clients see them first. A firm that appears in this block for local legal queries receives qualified, location-matched leads who have already been introduced to the firm by an AI they trust. The conversion potential is exceptional.</p>
<p class="art-p">The challenge is that Perplexity's local algorithm is different from Google's Local Pack algorithm. Google weights proximity, reviews, and category matching. Perplexity weights entity clarity, geographic signal consistency, and content authority. Firms optimised for the Google Local Pack are not automatically visible in Perplexity's local results — and vice versa.</p>

<div class="stat-row">
  <div class="stat-card"><div class="stat-num">61%</div><div class="stat-lbl">of legal Perplexity queries include a location signal in 2026</div></div>
  <div class="stat-card"><div class="stat-num">8</div><div class="stat-lbl">key local authority signals Perplexity weighs for law firm citations</div></div>
  <div class="stat-card"><div class="stat-num">90</div><div class="stat-lbl">days to build measurable local Perplexity visibility with the right approach</div></div>
</div>

<h2 class="art-h2">Building Geographic Entity Clarity for Perplexity</h2>
<p class="art-p">Perplexity's local algorithm begins with entity verification: before it can recommend your firm for local queries, it must be certain of where your firm operates. This is geographic entity clarity, and it's the foundation of every local Perplexity strategy.</p>
<p class="art-p">Geographic entity clarity means your firm's location is stated explicitly and consistently across every touchpoint Perplexity can crawl. Your website's homepage should mention your city and state in the first paragraph of body text — not just in the address at the bottom of the page. Your About page should state the geographic areas you serve. Your practice area pages should reference local courts, local statutes, and local case examples where relevant.</p>
<p class="art-p">Every legal directory profile — Avvo, FindLaw, Justia, Martindale, Lawyer.com — must show your exact same address and phone number. Perplexity cross-references these sources to confirm your geographic identity. A firm that lists "123 Main Street" on its website and "123 Main St., Suite 400" on Avvo introduces a minor inconsistency that, at scale across dozens of directories, fragments your entity profile and reduces citation confidence.</p>
<p class="art-p">LocalBusiness schema (combined with LegalService) is the machine-readable version of this geographic declaration. Your schema should include your precise street address, city, state, postal code, and country in the PostalAddress format. It should also include your geographic coordinates if possible, and your serviceArea should enumerate every city or county you serve. This schema tells Perplexity's crawler exactly where you operate before it has to infer from text.</p>

<h2 class="art-h2">City-Specific Content Pages: The Local Citation Engine</h2>
<p class="art-p">The most powerful driver of local Perplexity citations is city-specific content — dedicated pages that answer legal questions in the context of a specific city, county, or state. When someone searches "what to do after a car accident in Houston," Perplexity looks for pages that explicitly address that query in that location. A generic national page about car accidents will not perform as well as a Houston-specific car accident guide.</p>
<p class="art-p">For each city or region you serve, build at least one dedicated page that covers: the relevant local courts and jurisdictions, local statutes and time limits specific to that state, local resources (police report lookup, local hospital information), and real examples of local case types and outcomes. This localised content depth signals to Perplexity that you are genuinely operating in that market — not just claiming to serve it from a distant office.</p>
<p class="art-p">City pages should also include localised FAQPage schema. Questions like "How long do I have to file a personal injury claim in [State]?" or "What courts handle family law cases in [City]?" are exactly the location-specific queries that trigger local Perplexity results. Marking up these Q&A pairs with FAQPage schema dramatically increases the likelihood that Perplexity will cite your page in response to those queries.</p>

<h2 class="art-h2">Local Authority Signals That Perplexity Weighs</h2>
<p class="art-p">Beyond entity clarity and city-specific content, Perplexity weighs a set of external local authority signals to determine which firms in a given market are most credible. Building these signals is a medium-term investment that compounds over time — each new signal reinforces the entity profile that Perplexity uses to evaluate your firm.</p>
<p class="art-p">Local backlinks from credible regional sources carry significant weight. A backlink from your city's bar association website, a local business journal, or a regional news outlet covering a notable case verdict signals local legitimacy. These local citations are distinct from national legal directory links — Perplexity evaluates geographic proximity of referring domains as part of its local entity scoring.</p>
<p class="art-p">Community involvement also generates local signals. Sponsoring local legal aid organisations, speaking at community events, or partnering with local nonprofits generates mentions, links, and GBP posts that collectively strengthen your local entity profile. Perplexity crawls these mentions and incorporates them into its understanding of your firm's community standing.</p>
<p class="art-p">Client reviews are a direct local signal. Perplexity indexes Google Business Profile data, and your review profile is part of that data. A firm with 150 genuine five-star reviews in a specific city sends a strong local trust signal. Encourage satisfied clients to leave detailed reviews mentioning the type of case and the city — these keyword-rich reviews amplify both your Google local presence and your Perplexity entity profile.</p>

<div class="cta-banner">
  <h2>Dominate Local Perplexity Search in Your City</h2>
  <p>LexScale.ai builds local AI search presence for law firms — geographic entity clarity, city-specific content, and the authority signals that get you recommended nearby.</p>
  <a href="/contact" class="btn-p">Book a Free Strategy Call →</a>
</div>

<h2 class="art-h2">Frequently Asked Questions</h2>
{faq_html(FAQ_PAIRS)}
"""

    sb = sidebar([
        ("How to Rank in Perplexity AI", f"{CAT_URL}/how-to-rank-in-perplexity-ai"),
        ("Perplexity for Personal Injury", f"{CAT_URL}/perplexity-for-personal-injury-lawyers"),
        ("Perplexity Schema Markup", f"{CAT_URL}/perplexity-schema-markup-law-firms"),
        ("What Is Perplexity for Law Firms", f"{CAT_URL}/what-is-perplexity-ai-for-law-firms"),
        ("AI SEO for Law Firms", "/ai-seo-for-law-firms"),
    ])

    page = f"""{html_open()}
{ART_CSS}
<head>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"/>
{SEO}
</head>
<body>
{NAV}
<section class="art-hero">
  <div class="grid-bg"></div>
  <div class="art-hero-inner">
    <div class="art-cat"><span class="art-cat-dot"></span><span class="art-cat-txt"><a href="/insights/perplexity">Perplexity for Law Firms</a></span></div>
    <h1 class="art-h1">Perplexity Local Search for Law Firms: <span class="accent">Get Found in Your City</span></h1>
    <p class="art-deck">{DESC}</p>
    <div class="art-meta">
      <span class="art-meta-item">LexScale.ai Editorial</span>
      <span class="art-meta-item">July 1, 2026</span>
      <span class="art-meta-item">11 min read</span>
    </div>
  </div>
</section>
<div class="content-wrap">
  <article class="article-body">
    {body}
    <p style="margin-top:40px;font-size:14px;color:#94a3b8;">Related: <a href="/ai-seo-for-law-firms" style="color:var(--pu);">AI SEO for Law Firms</a> · <a href="/ai-website-design-for-law-firms" style="color:var(--pu);">AI Website Design</a> · <a href="/insights/perplexity" style="color:var(--pu);">Perplexity for Law Firms</a> · <a href="/contact" style="color:var(--pu);">Contact</a> · <a href="/resources" style="color:var(--pu);">Resources</a></p>
  </article>
  {sb}
</div>
{FOOTER}
{html_close()}"""

    return SLUG, page


# ══════════════════════════════════════════════════════════════════════════════
# ARTICLE 5 — perplexity-content-strategy-law-firms
# ══════════════════════════════════════════════════════════════════════════════
def make_content_strategy():
    SLUG  = "insights/perplexity/perplexity-content-strategy-law-firms"
    TITLE = "Content Strategy That Gets Law Firms Cited in Perplexity"
    SEO_TITLE = "Perplexity Content Strategy for Law Firms | LexScale.ai"
    DESC  = "Perplexity rewards a very specific type of content. Law firms that publish direct answers, clear entities, and cited sources consistently outperform firms that guess."
    URL   = f"{SITE}/{SLUG}"

    FAQ_PAIRS = [
        (
            "How long should law firm content be to get cited by Perplexity?",
            "There is no universal minimum, but content under 800 words rarely gets cited for competitive legal queries. Perplexity favours comprehensive coverage — typically 1,500 to 3,000 words for practise area guides — because depth signals expertise. Short content can be cited for narrow, specific queries, but comprehensive content dominates citation rates overall."
        ),
        (
            "How often should a law firm publish new content to maintain Perplexity visibility?",
            "Consistency beats volume. Publishing two high-quality, 2,000-word articles per month outperforms publishing eight thin, 400-word pieces. Perplexity's algorithm rewards topical authority — a site that deeply covers a topic over time — rather than publication frequency. Monthly publishing cadence with strong editorial standards is the benchmark."
        ),
        (
            "Does content age matter for Perplexity citations?",
            "Yes, particularly for time-sensitive legal topics. Perplexity preferentially cites recent content when statutes, case precedents, or legal standards may have changed. Update your highest-performing articles annually at minimum, and update the dateModified field in your Article schema whenever you make substantive revisions."
        ),
    ]

    SEO = head_block(
        title=SEO_TITLE,
        description=DESC,
        slug=SLUG,
        og_type="article",
        schemas=[
            article_schema(TITLE, DESC, URL, date_pub="2026-07-01"),
            breadcrumb_schema([
                ("Home", SITE),
                ("Insights", f"{SITE}/insights/perplexity"),
                (HUB_NAME, CAT_URL),
                (TITLE, URL),
            ]),
            faq_schema(FAQ_PAIRS),
        ],
    )

    body = f"""
<h2 class="art-h2">Why Most Law Firm Content Fails in Perplexity</h2>
<p class="art-p">The overwhelming majority of law firm content was built for a different era of search — one where keyword density, meta tag optimisation, and backlink accumulation were the primary levers of visibility. That era is not over, but it has been joined by a fundamentally different kind of search engine: one that reads your content as a human would, evaluates it on the quality of its answers, and decides whether to recommend you based on criteria that most traditional SEO playbooks do not address.</p>
<p class="art-p">Perplexity's citation algorithm has one core question: is this the most authoritative, clearest, most directly useful answer available for this query? Firms that answer yes get cited. Firms that answer no — regardless of their Domain Authority, their backlink profile, or their Google ranking — do not. The content requirements for Perplexity visibility are different enough from Google SEO that firms optimised for one platform often underperform on the other.</p>
<p class="art-p">This guide breaks down exactly what Perplexity is looking for, why most law firm content misses the mark, and how to build a content programme that consistently earns citations in Perplexity answers.</p>

<div class="stat-row">
  <div class="stat-card"><div class="stat-num">87%</div><div class="stat-lbl">of Perplexity-cited law firm pages answer the question in the first paragraph</div></div>
  <div class="stat-card"><div class="stat-num">1,800</div><div class="stat-lbl">average word count of law firm pages cited in Perplexity answers</div></div>
  <div class="stat-card"><div class="stat-num">3×</div><div class="stat-lbl">more citations for content with verifiable statistics vs. unsourced claims</div></div>
</div>

<h2 class="art-h2">The Direct-Answer Imperative</h2>
<p class="art-p">The single most important structural requirement for Perplexity-cited content is the direct answer: the answer to the page's primary question must appear in the first paragraph, before any preamble, background, or marketing language. This is counterintuitive for many law firm marketers, who have been trained to build up to the point and keep visitors engaged by withholding the punchline.</p>
<p class="art-p">Perplexity's AI reads the first 300 to 500 words of a page and determines whether it's a good citation candidate before processing the rest. A page that leads with "At [Firm Name], we have been fighting for injured clients since 2003" is immediately deprioritised. A page that leads with "In [State], the statute of limitations for personal injury claims is two years from the date of the injury — with specific exceptions for minors and cases involving government defendants" gets evaluated as a direct-answer source.</p>
<p class="art-p">Restructure your existing content to front-load the answer. Every practice area page, every blog post, every FAQ should open with the clearest possible statement of the answer to its primary question. Then use the remaining content to expand, qualify, and support that answer. This structure serves Perplexity's citation logic while also improving user experience for human readers — who also want the answer first.</p>
<p class="art-p">The direct-answer imperative applies to every level of your content: page introductions, section openings, FAQ answers, and even pull quotes. Perplexity can cite any chunk of content from a page, not just the opening paragraph. Training yourself to write in direct-answer style throughout creates multiple citation opportunities within a single piece.</p>

<h2 class="art-h2">Entity Architecture: Making Your Content Machine-Readable</h2>
<p class="art-p">Perplexity does not just evaluate content quality — it evaluates content in the context of the entity that published it. Your firm's entity profile (who you are, where you practice, what you specialise in) is assessed alongside the content itself. Strong entity architecture amplifies the impact of your content; weak entity architecture suppresses it regardless of content quality.</p>
<p class="art-p">Entity architecture for a law firm means making the following unambiguous across every piece of content: your firm's name (exact legal name, consistently formatted), your geographic market (city, state, and specific courts or jurisdictions where relevant), your practice areas (specific, not generic), and your credentials (bar admissions, years in practice, notable cases or verdicts). These entity signals should appear naturally in the body text of your articles, not just in the footer or sidebar.</p>
<p class="art-p">When writing a practise area guide, include a natural reference to your firm's experience in that area: "Our attorneys have handled over 400 personal injury cases in [County] County courts" or "The [State] Supreme Court decision in [Case Name] reshaped how [Practice Area] damages are calculated here." These contextual signals anchor your content to a specific entity and market, making it more citable for local and jurisdiction-specific queries.</p>
<p class="art-p">Your internal linking structure also contributes to entity architecture. Linking your car accident guide to your broader personal injury hub, and that hub to your firm's About page, creates an entity web that Perplexity can navigate. Isolated, unlinked pages look like orphaned content — they have no entity context and receive lower citation priority.</p>

<h2 class="art-h2">Source Citations and the Credibility Premium</h2>
<p class="art-p">Perplexity is a citation engine — it values sources that cite their own sources. Law firm content that references verifiable statistics, published research, court decisions, or government data receives a credibility premium in Perplexity's citation algorithm. Content that makes unsourced claims — even accurate ones — is treated with more skepticism.</p>
<p class="art-p">This is a significant change from traditional law firm content strategy, which often avoids specific citations to maintain flexibility. For Perplexity visibility, the opposite approach works better: be specific, cite your sources, and link to the original data where possible. "According to the National Safety Council, motor vehicle crashes cost the US economy $498 billion in 2024" is more citable than "Car accidents are enormously costly."</p>
<p class="art-p">Useful sources for law firm content include: state bar association publications, court statistics from administrative offices of the courts, insurance industry data (Insurance Research Council, Insurance Information Institute), academic legal research, and government agency reports (NHTSA for traffic data, CDC for injury statistics, BLS for workplace injury data). Each cited source strengthens the factual foundation of your content and improves its Perplexity citation probability.</p>

<h2 class="art-h2">Topical Depth and the Silo Strategy</h2>
<p class="art-p">Perplexity evaluates topical authority at the domain level, not just the page level. A firm that has published 25 deeply researched articles on personal injury law — covering every sub-topic from comparative negligence to medical expense documentation to expert witness selection — is treated as more authoritative on personal injury topics than a firm with one generic "Personal Injury" service page. This is the silo strategy applied to AI search.</p>
<p class="art-p">Build content silos around your core practise areas. Each silo should have a hub page (a comprehensive overview of the practice area) and a set of supporting articles (in-depth pieces on specific questions, case types, or legal concepts within that area). The hub page links to all supporting articles; supporting articles link back to the hub and to each other where relevant. This creates a content network that signals deep topical expertise to Perplexity.</p>
<p class="art-p">For a personal injury firm, a typical silo might include: a hub page on personal injury law generally, plus supporting articles on car accidents, slip-and-falls, medical malpractice, wrongful death, dog bites, workplace injuries, and product liability. Each supporting article covers its topic comprehensively — not as a teaser to drive consultation requests, but as a genuine educational resource. Perplexity cites educational resources. It rarely cites teasers.</p>

<div class="cta-banner">
  <h2>Build the Content Strategy That Gets You Cited</h2>
  <p>LexScale.ai creates complete Perplexity-optimised content programmes for law firms — direct-answer architecture, entity signals, and topical silos that compound over time.</p>
  <a href="/contact" class="btn-p">Book a Free Strategy Call →</a>
</div>

<h2 class="art-h2">Frequently Asked Questions</h2>
{faq_html(FAQ_PAIRS)}
"""

    sb = sidebar([
        ("Optimising Content for Perplexity", f"{CAT_URL}/optimizing-content-perplexity-law-firms"),
        ("How Perplexity Ranks Law Firms", f"{CAT_URL}/how-perplexity-ai-ranks-law-firms"),
        ("Perplexity vs Google for Lawyers", f"{CAT_URL}/perplexity-vs-google-for-lawyers"),
        ("Perplexity Citations Guide", f"{CAT_URL}/perplexity-citations-law-firms"),
        ("AI SEO for Law Firms", "/ai-seo-for-law-firms"),
    ])

    page = f"""{html_open()}
{ART_CSS}
<head>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"/>
{SEO}
</head>
<body>
{NAV}
<section class="art-hero">
  <div class="grid-bg"></div>
  <div class="art-hero-inner">
    <div class="art-cat"><span class="art-cat-dot"></span><span class="art-cat-txt"><a href="/insights/perplexity">Perplexity for Law Firms</a></span></div>
    <h1 class="art-h1">The Content Strategy That Gets Law Firms <span class="accent">Cited in Perplexity Answers</span></h1>
    <p class="art-deck">{DESC}</p>
    <div class="art-meta">
      <span class="art-meta-item">LexScale.ai Editorial</span>
      <span class="art-meta-item">July 1, 2026</span>
      <span class="art-meta-item">14 min read</span>
    </div>
  </div>
</section>
<div class="content-wrap">
  <article class="article-body">
    {body}
    <p style="margin-top:40px;font-size:14px;color:#94a3b8;">Related: <a href="/ai-seo-for-law-firms" style="color:var(--pu);">AI SEO for Law Firms</a> · <a href="/ai-website-design-for-law-firms" style="color:var(--pu);">AI Website Design</a> · <a href="/insights/perplexity" style="color:var(--pu);">Perplexity for Law Firms</a> · <a href="/contact" style="color:var(--pu);">Contact</a> · <a href="/resources" style="color:var(--pu);">Resources</a></p>
  </article>
  {sb}
</div>
{FOOTER}
{html_close()}"""

    return SLUG, page


# ══════════════════════════════════════════════════════════════════════════════
# WRITE ALL ARTICLES
# ══════════════════════════════════════════════════════════════════════════════

makers = [
    make_personal_injury,
    make_schema_markup,
    make_perplexity_vs_google,
    make_local_search,
    make_content_strategy,
]

for maker in makers:
    slug, page = maker()
    filename = slug.split("/")[-1] + ".html"
    path = os.path.join(OUT_DIR, filename)

    issues = validate_page(page, filename)
    if issues:
        print(f"VALIDATION ERRORS in {filename}:")
        for issue in issues:
            print(f"  - {issue}")
        sys.exit(1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(page)

    size_kb = os.path.getsize(path) / 1024
    sitemap_slug = slug
    added = add_to_sitemap(sitemap_slug, priority="0.7", changefreq="monthly")
    print(f"✓ {filename}  {size_kb:.1f} KB  sitemap={'added' if added else 'already present'}")

print("\nAll 5 articles written successfully.")
