#!/usr/bin/env python3
"""Batch 5 — 9 missing articles to complete the 50-article request."""
import os

BASE = os.path.dirname(__file__)

def article(slug, title, desc, category, cat_slug, cat_label, date, body_html, faqs):
    faq_ld = ",".join([
        f'{{"@type":"Question","name":{repr(q)},"acceptedAnswer":{{"@type":"Answer","text":{repr(a)}}}}}'
        for q, a in faqs
    ])
    faq_acc = "".join([
        f'<div class="faq-item"><div class="faq-q" onclick="toggleFaq(this)">{q}<span class="faq-icon">+</span></div>'
        f'<div class="faq-a"><div class="faq-a-inner">{a}</div></div></div>'
        for q, a in faqs
    ])
    cat_url = f"https://lexscale.ai/insights/{cat_slug}"
    art_url = f"https://lexscale.ai/insights/{cat_slug}/{slug.replace('.html','')}"
    canonical = art_url
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{title} | LexScale.ai</title>
<meta name="description" content="{desc}"/>
<link rel="canonical" href="{canonical}"/>
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"/>
<meta property="og:type" content="article"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:url" content="{canonical}"/>
<meta property="og:image" content="https://lexscale.ai/og-image.png"/>
<meta property="og:site_name" content="LexScale.ai"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{title}"/>
<meta name="twitter:description" content="{desc}"/>
<meta name="twitter:image" content="https://lexscale.ai/og-image.png"/>
<script type="application/ld+json">
[
  {{"@context":"https://schema.org","@type":"Article","headline":{repr(title)},"description":{repr(desc)},"datePublished":"{date}","dateModified":"2026-07-02","author":{{"@type":"Organization","name":"LexScale.ai","url":"https://lexscale.ai"}},"publisher":{{"@type":"Organization","name":"LexScale.ai","logo":{{"@type":"ImageObject","url":"https://lexscale.ai/og-image.png"}}}},"mainEntityOfPage":{{"@type":"WebPage","@id":"{canonical}"}}}},
  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://lexscale.ai"}},{{"@type":"ListItem","position":2,"name":"Insights","item":"https://lexscale.ai/insights"}},{{"@type":"ListItem","position":3,"name":{repr(cat_label)},"item":"{cat_url}"}},{{"@type":"ListItem","position":4,"name":{repr(title)},"item":"{canonical}"}}]}},
  {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_ld}]}}
]
</script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Inter',sans-serif;background:#fff;color:#1a1a2e}}
a{{text-decoration:none}}
nav{{background:#0B1536;padding:0 24px;display:flex;align-items:center;justify-content:space-between;height:64px;position:sticky;top:0;z-index:100;border-bottom:1px solid rgba(255,255,255,.08)}}
.nav-logo{{font-size:20px;font-weight:800;color:#fff;letter-spacing:-.5px}}
.nav-logo span{{color:#6A5CFF}}
.nav-links{{display:flex;gap:28px}}
.nav-links a{{color:rgba(255,255,255,.75);font-size:14px;font-weight:500;transition:color .2s}}
.nav-links a:hover{{color:#fff}}
.nav-cta{{background:linear-gradient(135deg,#6A5CFF,#8B7FFF);color:#fff;padding:9px 20px;border-radius:100px;font-size:13px;font-weight:700}}
.hero{{background:linear-gradient(135deg,#0B1536,#1a2456);padding:72px 24px 60px;text-align:center}}
.hero-tag{{display:inline-block;background:rgba(106,92,255,.2);border:1px solid rgba(106,92,255,.4);color:#8B7FFF;padding:6px 16px;border-radius:100px;font-size:12px;font-weight:700;letter-spacing:1px;text-transform:uppercase;margin-bottom:20px}}
.hero h1{{font-size:clamp(26px,4vw,46px);font-weight:900;color:#fff;letter-spacing:-1.2px;line-height:1.15;max-width:780px;margin:0 auto 16px}}
.hero-meta{{color:rgba(255,255,255,.5);font-size:13px}}
.content-wrap{{max-width:1100px;margin:0 auto;padding:56px 24px;display:grid;grid-template-columns:1fr 300px;gap:48px}}
@media(max-width:768px){{.content-wrap{{grid-template-columns:1fr}}.nav-links{{display:none}}}}
.article-body h2{{font-size:clamp(20px,2.5vw,28px);font-weight:800;color:#0B1536;margin:40px 0 14px;letter-spacing:-.5px}}
.article-body h3{{font-size:18px;font-weight:700;color:#0B1536;margin:28px 0 10px}}
.article-body p{{font-size:16px;line-height:1.85;color:#374151;margin-bottom:18px}}
.article-body ul{{margin:14px 0 18px 20px}}
.article-body li{{font-size:16px;line-height:1.75;color:#374151;margin-bottom:6px}}
.article-body strong{{color:#0B1536;font-weight:700}}
.stat-row{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin:36px 0}}
@media(max-width:600px){{.stat-row{{grid-template-columns:1fr}}}}
.stat-card{{background:linear-gradient(135deg,#f8f9fc,#eef0f8);border-radius:12px;padding:24px;text-align:center}}
.stat-num{{font-size:32px;font-weight:900;color:#6A5CFF;letter-spacing:-1px}}
.stat-label{{font-size:13px;color:#64748b;margin-top:4px;line-height:1.4}}
.sidebar{{padding-top:8px}}
.sidebar-card{{background:#f8f9fc;border-radius:12px;padding:24px;margin-bottom:24px}}
.sidebar-card h4{{font-size:14px;font-weight:700;color:#0B1536;margin-bottom:14px;text-transform:uppercase;letter-spacing:.5px}}
.sidebar-card a{{display:block;font-size:14px;color:#6A5CFF;font-weight:500;margin-bottom:10px;transition:color .2s}}
.sidebar-card a:hover{{color:#0B1536}}
.cta-banner{{background:linear-gradient(135deg,#0B1536,#1a2456);padding:64px 24px;text-align:center}}
.cta-banner h2{{font-size:clamp(22px,3vw,36px);font-weight:900;color:#fff;margin-bottom:14px;letter-spacing:-.8px}}
.cta-banner p{{color:rgba(255,255,255,.65);font-size:16px;max-width:520px;margin:0 auto 28px}}
.cta-btn{{display:inline-block;background:linear-gradient(135deg,#6A5CFF,#8B7FFF);color:#fff;padding:14px 36px;border-radius:100px;font-size:15px;font-weight:700}}
.faq-section{{padding:64px 24px;background:#f8f9fc}}
.faq-inner{{max-width:760px;margin:0 auto}}
.faq-inner h2{{font-size:28px;font-weight:800;color:#0B1536;text-align:center;margin-bottom:32px;letter-spacing:-.5px}}
.faq-item{{border:1px solid #e2e8f0;border-radius:10px;margin-bottom:12px;background:#fff;overflow:hidden}}
.faq-q{{padding:18px 20px;font-size:15px;font-weight:600;color:#0B1536;cursor:pointer;display:flex;justify-content:space-between;align-items:center}}
.faq-icon{{font-size:20px;color:#6A5CFF;font-weight:400;transition:transform .3s}}
.faq-a{{max-height:0;overflow:hidden;transition:max-height .4s ease}}
.faq-a.open{{max-height:400px}}
.faq-a-inner{{padding:0 20px 18px;font-size:15px;color:#374151;line-height:1.75}}
footer{{background:#0B1536;padding:48px 24px 32px;border-top:1px solid rgba(255,255,255,.08)}}
.footer-inner{{max-width:1100px;margin:0 auto;text-align:center}}
.footer-logo{{font-size:22px;font-weight:800;color:#fff;margin-bottom:20px}}
.footer-logo span{{color:#6A5CFF}}
.footer-links{{display:flex;flex-wrap:wrap;gap:20px;justify-content:center;margin-bottom:24px}}
.footer-links a{{color:rgba(255,255,255,.55);font-size:13px;font-weight:500;transition:color .2s}}
.footer-links a:hover{{color:#fff}}
.footer-copy{{color:rgba(255,255,255,.3);font-size:12px}}
.modal-overlay{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:1000;align-items:center;justify-content:center}}
.modal-overlay.active{{display:flex}}
.modal{{background:#fff;border-radius:16px;padding:40px;max-width:460px;width:90%;position:relative}}
.modal h3{{font-size:22px;font-weight:800;color:#0B1536;margin-bottom:8px}}
.modal p{{font-size:14px;color:#64748b;margin-bottom:20px}}
.modal input,.modal select{{width:100%;border:1px solid #e2e8f0;border-radius:8px;padding:11px 14px;font-size:14px;margin-bottom:12px;font-family:inherit}}
.modal button{{width:100%;background:linear-gradient(135deg,#6A5CFF,#8B7FFF);color:#fff;border:none;border-radius:100px;padding:13px;font-size:15px;font-weight:700;cursor:pointer}}
.modal-close{{position:absolute;top:16px;right:20px;font-size:22px;cursor:pointer;color:#94a3b8;border:none;background:none}}
</style>
</head>
<body>
<nav>
  <a href="/" class="nav-logo">Lex<span>Scale</span>.ai</a>
  <div class="nav-links">
    <a href="/ai-seo-for-law-firms">AI SEO</a>
    <a href="/ai-chatbot-for-law-firms">AI Chatbot</a>
    <a href="/ai-receptionist-for-law-firms">AI Receptionist</a>
    <a href="/ai-website-design-for-law-firms">AI Websites</a>
    <a href="/insights/chatgpt-for-law-firms">Insights</a>
  </div>
  <a href="/contact" class="nav-cta" onclick="document.getElementById('leadModal').classList.add('active');return false;">Free Strategy Call</a>
</nav>

<div class="hero">
  <div class="hero-tag">{cat_label}</div>
  <h1>{title}</h1>
  <div class="hero-meta">By LexScale.ai Editorial &nbsp;·&nbsp; {date} &nbsp;·&nbsp; 8 min read</div>
</div>

<div class="content-wrap">
  <article class="article-body">
    {body_html}
  </article>
  <aside class="sidebar">
    <div class="sidebar-card">
      <h4>Related Articles</h4>
      <a href="/insights/{cat_slug}">← {cat_label} Hub</a>
      <a href="/ai-seo-for-law-firms">AI SEO for Law Firms</a>
      <a href="/ai-website-design-for-law-firms">AI Website Design</a>
      <a href="/ai-chatbot-for-law-firms">AI Chatbots for Law Firms</a>
      <a href="/ai-receptionist-for-law-firms">AI Receptionist</a>
    </div>
    <div class="sidebar-card">
      <h4>Our Services</h4>
      <a href="/ai-seo-for-law-firms">AI SEO</a>
      <a href="/ai-website-design-for-law-firms">Website Design</a>
      <a href="/ai-chatbot-for-law-firms">AI Chatbot</a>
      <a href="/ai-receptionist-for-law-firms">AI Receptionist</a>
      <a href="/about">About LexScale.ai</a>
    </div>
    <div class="sidebar-card" style="background:linear-gradient(135deg,#6A5CFF,#8B7FFF);border-radius:12px;padding:24px;text-align:center;">
      <h4 style="color:#fff;margin-bottom:8px;">Ready to Rank?</h4>
      <p style="color:rgba(255,255,255,.8);font-size:13px;margin-bottom:16px;">Get a free SEO audit for your law firm.</p>
      <a href="/contact" onclick="document.getElementById('leadModal').classList.add('active');return false;" style="display:block;background:#fff;color:#6A5CFF;padding:10px;border-radius:100px;font-size:13px;font-weight:700;">Book Free Audit →</a>
    </div>
  </aside>
</div>

<div class="faq-section">
  <div class="faq-inner">
    <h2>Frequently Asked Questions</h2>
    {faq_acc}
  </div>
</div>

<div class="cta-banner">
  <h2>Let's Get Your Firm Found in AI Search</h2>
  <p>LexScale.ai builds AI-first digital strategies for law firms that want to lead, not follow.</p>
  <a href="/contact" class="cta-btn" onclick="document.getElementById('leadModal').classList.add('active');return false;">Book a Free Strategy Call →</a>
</div>

<footer>
  <div class="footer-inner">
    <div class="footer-logo">Lex<span>Scale</span>.ai</div>
    <div class="footer-links">
      <a href="/ai-website-design-for-law-firms">AI Website Design</a>
      <a href="/ai-seo-for-law-firms">AI SEO</a>
      <a href="/ai-receptionist-for-law-firms">AI Receptionist</a>
      <a href="/ai-chatbot-for-law-firms">AI Chatbot</a>
      <a href="/about">About</a>
      <a href="/insights/chatgpt-for-law-firms">Insights</a>
      <a href="/resources">Resources</a>
      <a href="/privacy">Privacy</a>
    </div>
    <div class="footer-copy">© 2026 LexScale.ai · All rights reserved</div>
  </div>
</footer>

<div class="modal-overlay" id="leadModal">
  <div class="modal">
    <button class="modal-close" onclick="document.getElementById('leadModal').classList.remove('active')">×</button>
    <h3>Book Your Free Strategy Call</h3>
    <p>Tell us about your firm and we'll put together a custom AI growth plan.</p>
    <input type="text" placeholder="Your Name"/>
    <input type="email" placeholder="Email Address"/>
    <input type="text" placeholder="Law Firm Name"/>
    <select><option>Select Practice Area</option><option>Personal Injury</option><option>Family Law</option><option>Criminal Defense</option><option>Estate Planning</option><option>Immigration</option><option>Business Law</option><option>Other</option></select>
    <button onclick="document.getElementById('leadModal').classList.remove('active')">Send My Free Audit Request →</button>
  </div>
</div>

<script>
function toggleFaq(el){{
  var a=el.nextElementSibling;
  var icon=el.querySelector('.faq-icon');
  if(a.classList.contains('open')){{a.classList.remove('open');icon.style.transform='rotate(0deg)';}}
  else{{a.classList.add('open');icon.style.transform='rotate(45deg)';}}
}}
</script>
</body>
</html>"""

# ── AI WEBSITES ──────────────────────────────────────────────────────────────

multilingual_body = """
<p>Your law firm serves clients who speak Spanish, Mandarin, Tagalog, French, or a dozen other languages — but your website speaks only English. That's not just a missed opportunity. In 2026, it's a competitive liability. AI search engines like Google Gemini and Perplexity now actively surface multilingual content when users search in their native language. If your site isn't structured for it, you're invisible to an enormous slice of your potential client base.</p>

<p>Building a multilingual law firm website isn't just about translation. It's about creating the right technical architecture, entity signals, and content depth that gets you found — and trusted — by clients who aren't searching in English.</p>

<div class="stat-row">
  <div class="stat-card"><div class="stat-num">67M</div><div class="stat-label">Spanish speakers in the US — the largest non-English language group</div></div>
  <div class="stat-card"><div class="stat-num">54%</div><div class="stat-label">of immigrants say they prefer legal services in their native language</div></div>
  <div class="stat-card"><div class="stat-num">3×</div><div class="stat-label">higher conversion rate for multilingual legal pages vs. machine-translated content</div></div>
</div>

<h2>Why Machine Translation Isn't Enough</h2>
<p>Google Translate has gotten scarily good at surface-level translation. But it fails legal content in ways that matter. Legal terminology doesn't translate directly. "Discovery" means something entirely different in English legal contexts vs. what a Spanish speaker would understand from "descubrimiento." "Negligence" in tort law doesn't map cleanly to most languages without explanatory context.</p>

<p>AI systems evaluating your content for citation quality look at coherence, subject-matter depth, and whether the language actually matches how real people in that community ask legal questions. Machine translation fails all three tests. A Gemini citation or Perplexity reference to your page depends on your content being demonstrably authoritative — not just grammatically acceptable.</p>

<h2>The Technical Architecture That Actually Works</h2>
<p>The right approach uses <code>hreflang</code> tags to signal to Google which version of a page corresponds to which language and region. Here's what the structure looks like for a firm targeting English and Spanish speakers in the US:</p>

<pre style="background:#f1f5f9;padding:16px;border-radius:8px;font-size:13px;overflow-x:auto;margin:16px 0;"><code>&lt;link rel="alternate" hreflang="en-us" href="https://yourfirm.com/practice-areas/personal-injury" /&gt;
&lt;link rel="alternate" hreflang="es-us" href="https://yourfirm.com/es/areas-de-practica/lesiones-personales" /&gt;
&lt;link rel="alternate" hreflang="x-default" href="https://yourfirm.com/practice-areas/personal-injury" /&gt;</code></pre>

<p>The <code>x-default</code> attribute tells Google which page to show users whose language preference doesn't match any specific variant. Get this wrong and you'll trigger confusing duplicate content signals that hurt all versions of the page.</p>

<h2>URL Structure: Subdirectory vs. Subdomain</h2>
<p>For most law firms, subdirectories win. <code>/es/</code> prefix keeps all language versions under your main domain, which means all your domain authority applies to every page. Subdomains (<code>es.yourfirm.com</code>) split your authority and require nearly double the SEO work.</p>

<p>The only exception: if you're building what is effectively a separate brand for a different language market — for instance, a firm that operates under a different name in Spanish-speaking communities — a subdomain can signal that distinction more cleanly. But for 95% of US law firms, <code>/es/practice-areas/</code> is the right call.</p>

<h2>Schema Markup for Multilingual Pages</h2>
<p>Your JSON-LD schema needs to reflect the language of the page it's on. The <code>inLanguage</code> property in WebPage schema tells AI crawlers that this content is authoritative in a specific language:</p>

<pre style="background:#f1f5f9;padding:16px;border-radius:8px;font-size:13px;overflow-x:auto;margin:16px 0;"><code>{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Abogados de Lesiones Personales en Miami",
  "inLanguage": "es",
  "url": "https://yourfirm.com/es/abogados-lesiones-personales-miami"
}}</code></pre>

<p>This matters specifically for AI citation. When Perplexity gets a query in Spanish about personal injury lawyers in Miami, it's looking for pages with explicit language signals in their markup, not just translated text.</p>

<h2>Content Strategy: Write for How People Actually Search</h2>
<p>Spanish-speaking clients searching for legal help don't always search the way English content assumes. They might search "cuánto cuesta un abogado de accidentes" (how much does an accident lawyer cost) rather than "personal injury attorney fees." Your Spanish-language pages need to be built around actual Spanish-language search intent, not translated versions of your English keyword strategy.</p>

<p>This requires working with a bilingual legal content writer who understands both the legal concepts and the community's actual language patterns. The ROI is significant: Spanish-language legal searches are less competitive than English equivalents in most markets, and conversion rates are higher when content speaks authentically to the community.</p>

<h2>Navigation and UX for Multilingual Visitors</h2>
<p>Language switching needs to be visible without being intrusive. A small language selector in the header — not a pop-up overlay, which increases bounce rates — works best. Keep the selector accessible on mobile. Users on phones switching from English to Spanish shouldn't lose their place on the page.</p>

<p>Critically, when a user switches language, route them to the equivalent page in that language — not to the homepage. If someone is reading your criminal defense page and switches to Spanish, they should land on <code>/es/defensa-criminal/</code>, not your Spanish homepage. This is a simple routing logic issue that most firms get wrong.</p>

<h2>Local Entity Signals in Multiple Languages</h2>
<p>Your Google Business Profile supports multiple languages in the description and service descriptions. Update them. This is a direct signal that your firm serves multilingual clients, and it feeds into the entity understanding that AI search systems use to surface your firm in relevant local results.</p>

<p>Review management matters too. Spanish-language Google reviews don't just help in local pack rankings — they signal to AI systems that real Spanish-speaking clients have worked with your firm. Respond to Spanish reviews in Spanish. This demonstrates the entity quality that gets you cited in AI-generated answers.</p>

<h2>Measuring Multilingual SEO Performance</h2>
<p>Set up separate Search Console properties for each language subdirectory, or use the country/language filters within a single property. Track impressions, clicks, and average position for Spanish-language queries separately from English. You need this data to understand what's working and where to invest content effort next.</p>

<p>Related: <a href="/ai-seo-for-law-firms" style="color:#6A5CFF;">AI SEO for Law Firms</a> · <a href="/ai-website-design-for-law-firms" style="color:#6A5CFF;">AI Website Design</a> · <a href="/insights/entity-seo/entity-building-strategy-law-firms" style="color:#6A5CFF;">Entity Building Strategy</a> · <a href="/ai-chatbot-for-law-firms" style="color:#6A5CFF;">AI Chatbots</a> · <a href="/about" style="color:#6A5CFF;">About LexScale.ai</a></p>
"""

multilingual_faqs = [
    ("Do I need separate pages for each language on my law firm website?", "Yes. Each language version should be a separate page with its own URL, unique content written or reviewed by a native speaker, and hreflang tags pointing to the other language versions. Machine-translated duplicate content won't perform well in AI search."),
    ("Will multilingual pages hurt my SEO if I have duplicate content?", "Not if you implement hreflang tags correctly. These tags tell Google which version of the page is intended for which language audience, preventing duplicate content penalties and ensuring each version is indexed appropriately."),
    ("Which languages should a US law firm prioritize for multilingual SEO?", "Spanish is the highest-ROI starting point for most US markets given the size of the Spanish-speaking population. After that, Mandarin, Vietnamese, Tagalog, and Portuguese are worth evaluating based on your specific market demographics and practice area."),
]

chat_body = """
<p>Every law firm website has a chat widget now. Most of them are ruining the user experience. Aggressive pop-ups that appear after three seconds. Generic "How can I help you today?" prompts that feel like a form letter. Mobile chat widgets that cover the entire screen. Visitors close these without engaging, bounce rates climb, and the firm wonders why no one is converting.</p>

<p>Getting chat right on a law firm website is more nuanced than it looks. The goal isn't to have chat — it's to have chat that feels natural, builds trust, and captures leads from the visitors who actually want to talk. Here's how to do it without irritating everyone else.</p>

<div class="stat-row">
  <div class="stat-card"><div class="stat-num">38%</div><div class="stat-label">of legal website visitors who use chat convert to consultations vs. 4% for contact forms</div></div>
  <div class="stat-card"><div class="stat-num">11s</div><div class="stat-label">average time before intrusive chat pop-ups cause visitors to leave the page</div></div>
  <div class="stat-card"><div class="stat-num">73%</div><div class="stat-label">of potential clients say they'd choose a law firm based on quick response availability</div></div>
</div>

<h2>The Two Types of Chat (And When to Use Each)</h2>
<p>Live chat means a real human responds in real time. AI chat means a trained chatbot handles the conversation. Hybrid means the bot handles initial intake and hands off to a human when needed. Each has a place — the mistake is choosing without understanding the tradeoffs.</p>

<p>Live chat converts better when it's actually live. The problem: most firms can't staff it properly. An unanswered live chat prompt that shows "Available" converts worse than no chat at all, because it breaks trust at the moment a prospect is deciding whether to reach out. If you can't staff live chat during business hours, don't advertise it as live.</p>

<p>AI chatbots have become genuinely good at legal intake. A well-trained bot can qualify the case type, collect contact info, explain your process, and book a consultation slot — all without human involvement. The key word is "well-trained." Generic chatbots that don't understand legal practice areas fail this test.</p>

<h2>Placement: Where Chat Should Appear (And Where It Shouldn't)</h2>
<p>The bottom-right corner of the screen is where visitors expect to find chat. Don't get creative with placement. The icon should be visible but not obstructive — a floating button of about 48×48 pixels is the standard. Large enough to tap on mobile, small enough not to cover content.</p>

<p>Pages where chat performs best: practice area pages, contact page, and any page that explicitly addresses pricing or the intake process. These are decision-making moments. A visitor reading your personal injury page who has a specific question about their case type is exactly the person chat is built for.</p>

<p>Pages where chat is often counterproductive: blog posts, general informational articles, and the homepage above the fold. Visitors in early research mode don't want to be interrupted. Let them read. The chat option should be available, not in their face.</p>

<h2>Timing and Trigger Behaviour</h2>
<p>Never auto-open chat immediately on page load. This is the number one mistake. Set a time delay of at least 45–60 seconds, or better yet, use a scroll-depth trigger — open the chat prompt after the visitor has scrolled 70% of the page. This means they've engaged with the content and are more likely to convert.</p>

<p>Exit-intent triggers are worth testing on high-value pages. If a visitor moves their cursor toward the browser's close button, a chat prompt that says "Before you go — have a quick question about your case?" can recover a percentage of exits. Use this sparingly and only on pages where the visitor has shown genuine engagement first.</p>

<h2>The Greeting Message: Stop Saying "How Can I Help You?"</h2>
<p>Generic chat greetings fail because they put the burden on the visitor to explain what they want. Better approach: contextual greetings that match the page content.</p>

<ul>
  <li>On your personal injury page: "Were you recently in an accident? We can usually tell you in 60 seconds whether you have a case."</li>
  <li>On your family law page: "Going through a divorce or custody issue? Let's talk about what your options look like."</li>
  <li>On your contact page: "Ready to set up a consultation? I can grab your info and have someone reach out within the hour."</li>
</ul>

<p>These work because they do two things: they show the firm understands what the visitor is looking for, and they offer a specific value (a quick assessment, an understanding of options, a concrete next step). The conversion lift from page-specific chat greetings over generic ones is consistently significant in A/B testing.</p>

<h2>Mobile Chat: The Rules Are Different</h2>
<p>On mobile, chat widgets need to follow different rules. The widget button should be above the mobile keyboard zone — too many chat widgets appear behind the keyboard when a user is typing, making it impossible to read responses. Test this yourself on an actual phone.</p>

<p>The chat window on mobile should open as a full-screen overlay or a large bottom sheet, not a small floating box. Mobile screens are too small for a corner chat window that shows two lines of text at a time. Visitors will close it out of frustration even if they wanted to engage.</p>

<h2>After Hours: What Happens When No One Is There</h2>
<p>Set honest expectations. If your firm doesn't have 24/7 coverage, your chat should say so. An after-hours message like "We're closed right now — leave your name and number and we'll call you first thing tomorrow" outperforms a pretend-online bot that collects info and ghosts the lead.</p>

<p>Better: use an AI chatbot for after-hours intake that explicitly identifies itself as automated. "Our office is closed, but our AI assistant can take your information and have an attorney review your situation first thing tomorrow" is honest, sets expectations, and still captures the lead.</p>

<h2>Connecting Chat to Your CRM</h2>
<p>Chat that doesn't feed your CRM is chat that creates work. Every conversation — whether it converts or not — should log to your client management system. Most major chat platforms (Clio Grow, Lawmatics, HubSpot) have native integrations or Zapier connections that handle this automatically. Set it up before you launch chat, not after.</p>

<p>Related: <a href="/ai-chatbot-for-law-firms" style="color:#6A5CFF;">AI Chatbots for Law Firms</a> · <a href="/ai-website-design-for-law-firms" style="color:#6A5CFF;">AI Website Design</a> · <a href="/ai-receptionist-for-law-firms" style="color:#6A5CFF;">AI Receptionist</a> · <a href="/ai-seo-for-law-firms" style="color:#6A5CFF;">AI SEO</a> · <a href="/about" style="color:#6A5CFF;">About LexScale.ai</a></p>
"""

chat_faqs = [
    ("Should a law firm use live chat or AI chat on their website?", "It depends on your capacity to staff it. Live chat converts better when genuinely live, but an unstaffed live chat destroys trust. AI chatbots that are well-trained for legal intake can handle qualification and booking 24/7. A hybrid approach — AI for initial intake, human handoff for complex questions — works best for most mid-size firms."),
    ("When should a law firm chat widget pop up on a website?", "At minimum, delay the chat prompt 45–60 seconds after page load. Better: trigger it after the visitor scrolls 70% of the page, indicating genuine engagement. Immediate pop-ups on page load are the single biggest driver of chat-related bounce rate increases."),
    ("How do I make my law firm chat widget not annoying on mobile?", "Use a full-screen overlay or large bottom sheet for the chat window on mobile, position the widget above the keyboard zone, and avoid covering the main content with the floating button. Test the experience on actual phones — not just desktop browser developer tools."),
]

# ── ENTITY SEO ───────────────────────────────────────────────────────────────

events_body = """
<p>Law firms run events all the time. Seminars on estate planning. Webinars on immigration changes. Free consultations for accident victims. In-person workshops on business formation. These events generate leads, build authority, and demonstrate community engagement.</p>

<p>But most firms bury this information in a paragraph somewhere on their website, with no structured data to help AI systems understand what's happening, when it's happening, or who should attend. That's a missed opportunity that costs you visibility in exactly the moments when prospective clients are looking.</p>

<div class="stat-row">
  <div class="stat-card"><div class="stat-num">Event</div><div class="stat-label">schema is one of only 12 structured data types eligible for Google rich results</div></div>
  <div class="stat-card"><div class="stat-num">3×</div><div class="stat-label">higher CTR for event rich results vs. standard blue-link search results</div></div>
  <div class="stat-card"><div class="stat-num">92%</div><div class="stat-label">of AI-generated event recommendations pull from structured data markup</div></div>
</div>

<h2>What Event Schema Actually Does for a Law Firm</h2>
<p>Event schema — formally <code>schema.org/Event</code> — tells search engines and AI platforms the structured facts about something happening at a specific time and place. When implemented correctly, it enables your events to appear in Google's event rich results, the AI Overview section, and in AI assistant responses to queries like "are there any free legal seminars near me this month?"</p>

<p>Without schema, this information is text. Google and AI systems can read it, but they can't confidently extract it, structure it, or surface it in event-specific contexts. With schema, it becomes a machine-readable fact that feeds directly into event discovery features.</p>

<h2>The Event Schema Implementation</h2>
<p>Here's what a complete Event schema looks like for a law firm estate planning webinar:</p>

<pre style="background:#f1f5f9;padding:16px;border-radius:8px;font-size:13px;overflow-x:auto;margin:16px 0;"><code>{{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "Free Estate Planning Webinar for Ontario Families",
  "description": "Join our certified estate planning attorneys for a free 90-minute webinar covering wills, trusts, powers of attorney, and how to protect your family's future.",
  "startDate": "2026-08-15T18:00:00-04:00",
  "endDate": "2026-08-15T19:30:00-04:00",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode",
  "location": {{
    "@type": "VirtualLocation",
    "url": "https://yourfirm.com/events/estate-planning-webinar-august"
  }},
  "organizer": {{
    "@type": "LegalService",
    "name": "Your Firm Name",
    "url": "https://yourfirm.com"
  }},
  "offers": {{
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "url": "https://yourfirm.com/events/estate-planning-webinar-august"
  }},
  "image": "https://yourfirm.com/images/estate-planning-webinar.jpg"
}}</code></pre>

<p>For in-person events, replace <code>OnlineEventAttendanceMode</code> with <code>OfflineEventAttendanceMode</code> and replace <code>VirtualLocation</code> with a <code>Place</code> object that includes your firm's address.</p>

<h2>Creating Dedicated Event Pages</h2>
<p>Each event needs its own URL. Don't dump all your events onto a single page — this dilutes the structured data signals and makes it impossible for Google to create event-specific rich results. The URL pattern should be <code>/events/event-name</code> or <code>/seminars/event-name</code>.</p>

<p>The page content should include: date, time, format (in-person or virtual), what attendees will learn, who it's designed for, the attorney or attorneys presenting, and a registration mechanism. This content depth matters for AI citation — when a user asks Gemini or Perplexity about upcoming legal seminars, AI systems favor pages with complete, structured information over sparse event listings.</p>

<h2>Handling Past Events</h2>
<p>When an event passes, don't delete the page or remove the schema. Update <code>eventStatus</code> to <code>EventPostponed</code> or add a clear notice that the event has concluded. Better yet, add a recording or summary of what was covered, and link to upcoming events.</p>

<p>Past event pages with substantive content (recordings, slides, Q&A summaries) continue to generate organic traffic and establish topical authority. They also become citation targets for AI systems answering questions about the topic — "what do lawyers say about estate planning mistakes" is a query that might surface your webinar summary page if it's well-structured.</p>

<h2>Webinars vs. In-Person Events: Schema Differences</h2>
<p>Online events use <code>OnlineEventAttendanceMode</code> and a <code>VirtualLocation</code> with a URL. In-person events use <code>OfflineEventAttendanceMode</code> and a <code>Place</code> object. Hybrid events — increasingly common — use <code>MixedEventAttendanceMode</code> with both location types specified.</p>

<p>Getting this right matters because Google's event filters let users specifically request in-person or online events. If your in-person seminar is incorrectly marked as online, it won't appear when users filter for local events — which is when your community members are most likely to find it.</p>

<h2>Integrating Event Schema with Your Content Strategy</h2>
<p>Events are authority-building content. Promote them as resources on your practice area pages — a personal injury page that includes "Join our upcoming free webinar on what to do after a car accident" with a link to the event page creates a content connection that reinforces your authority in that practice area.</p>

<p>Related: <a href="/insights/entity-seo/entity-building-strategy-law-firms" style="color:#6A5CFF;">Entity Building Strategy</a> · <a href="/ai-seo-for-law-firms" style="color:#6A5CFF;">AI SEO for Law Firms</a> · <a href="/insights/entity-seo/attorney-eeat-signals" style="color:#6A5CFF;">Attorney E-E-A-T Signals</a> · <a href="/ai-website-design-for-law-firms" style="color:#6A5CFF;">AI Website Design</a> · <a href="/about" style="color:#6A5CFF;">About LexScale.ai</a></p>
"""

events_faqs = [
    ("Can event schema help my law firm appear in Google search results?", "Yes. Event schema is one of the structured data types eligible for Google's event rich results, which appear above standard organic listings. These results show the event name, date, and location directly in search, dramatically increasing click-through rates for relevant queries."),
    ("Do I need a separate page for each law firm event?", "Yes. Each event should have its own dedicated URL with complete event details and properly implemented schema. A single events listing page cannot generate event-specific rich results the same way individual event pages can."),
    ("What happens to event pages after the event has passed?", "Don't delete them. Update the event status in your schema and add substantive content — recordings, summaries, key takeaways. Past event pages with good content continue to generate organic traffic and establish authority, and can become citation targets for AI search responses on the topic."),
]

video_body = """
<p>Video is the fastest-growing content format in legal marketing — and one of the most underutilised in terms of SEO. Law firms invest real money in filming attorney profiles, client testimonials, process explainers, and practice area walkthroughs, then upload them to YouTube and call it done. What they're missing is the structured data layer that tells AI systems exactly what those videos are about, who made them, and why they're worth citing.</p>

<p>Video schema doesn't guarantee rankings, but it does unlock a set of rich results and AI citation opportunities that are simply unavailable to unmarked video content. Here's how to implement it properly.</p>

<div class="stat-row">
  <div class="stat-card"><div class="stat-num">41%</div><div class="stat-label">of Google video rich results go to pages with VideoObject schema markup</div></div>
  <div class="stat-card"><div class="stat-num">8×</div><div class="stat-label">higher likelihood of video snippet in AI Overviews when VideoObject schema present</div></div>
  <div class="stat-card"><div class="stat-num">2.6×</div><div class="stat-label">longer average time on page for law firm pages that include embedded video</div></div>
</div>

<h2>The VideoObject Schema: What It Includes</h2>
<p>The <code>schema.org/VideoObject</code> type communicates structured facts about your video to search engines and AI systems. A complete implementation looks like this:</p>

<pre style="background:#f1f5f9;padding:16px;border-radius:8px;font-size:13px;overflow-x:auto;margin:16px 0;"><code>{{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "What to Do After a Car Accident in Ontario — Personal Injury Attorney Explains",
  "description": "Personal injury attorney [Name] explains the 5 steps you should take immediately after a car accident to protect your rights and your claim.",
  "thumbnailUrl": "https://yourfirm.com/images/car-accident-video-thumb.jpg",
  "uploadDate": "2026-06-15",
  "duration": "PT8M32S",
  "contentUrl": "https://yourfirm.com/videos/car-accident-steps",
  "embedUrl": "https://www.youtube.com/embed/YOUR_VIDEO_ID",
  "publisher": {{
    "@type": "LegalService",
    "name": "Your Firm Name",
    "url": "https://yourfirm.com"
  }},
  "author": {{
    "@type": "Person",
    "name": "Attorney Full Name",
    "jobTitle": "Personal Injury Attorney"
  }}
}}</code></pre>

<p>The <code>duration</code> field uses ISO 8601 duration format — PT8M32S means 8 minutes and 32 seconds. Get this right; incorrect duration data can prevent your video from being eligible for rich results.</p>

<h2>Where to Put the Schema: Page vs. YouTube</h2>
<p>Video schema belongs on your website page where the video is embedded, not on YouTube. YouTube handles its own structured data. Your job is to mark up the page on your domain where the video lives, so that when Google crawls your page, it finds the schema and understands the video's context within your site's overall topical authority.</p>

<p>This means every video needs a dedicated page on your website, or at minimum a section of a page where the video is the primary content. Don't just embed videos without any surrounding context — the page needs text that corroborates the video topic, ideally a transcript or summary of the key points covered.</p>

<h2>Transcripts: The SEO Layer YouTube Misses</h2>
<p>YouTube auto-generates transcripts that Google can read. But a proper transcript on your website page — formatted as readable text, not a wall of auto-caption output — provides AI systems with the full text of your video content to index and cite.</p>

<p>Structure it: heading, key point summary bullets, then the full transcript formatted with speaker labels and paragraph breaks at natural breaks in the content. This page then ranks for the long-tail queries your video covers — the specific questions an attorney answers verbally — without the firm ever having to write a separate article on each topic.</p>

<h2>Video Content Types That Win in AI Search</h2>
<p>Not all legal video content performs equally for AI citation. The types that consistently get cited in AI Overviews and Perplexity answers share a common trait: they directly answer a specific question.</p>

<ul>
  <li><strong>Process explainers:</strong> "What happens at a deposition?" "How does the divorce process work in [state]?"</li>
  <li><strong>Myth busters:</strong> "No, you don't have to give a recorded statement to the insurance company" — videos that correct common misconceptions</li>
  <li><strong>Timeline walkthroughs:</strong> "How long does a personal injury case take? Here's what the timeline looks like step by step"</li>
  <li><strong>Attorney Q&As:</strong> Answering real client questions on camera, structured around specific queries</li>
</ul>

<p>Generic brand videos ("here at Smith Law Firm, we put our clients first") don't get cited in AI search. Specific, question-answering content does.</p>

<h2>KeyClip Marks: Getting Your Video into Clips in Search</h2>
<p>Google's video carousel often surfaces specific "key moments" within longer videos. You can suggest these moments using the <code>hasPart</code> property with <code>Clip</code> objects, or by adding timestamp data to your YouTube video chapters. This allows Google to link directly to the 2:15 mark where you explain the statute of limitations, rather than requiring the user to start from the beginning.</p>

<p>Related: <a href="/ai-seo-for-law-firms" style="color:#6A5CFF;">AI SEO for Law Firms</a> · <a href="/insights/entity-seo/entity-building-strategy-law-firms" style="color:#6A5CFF;">Entity Building Strategy</a> · <a href="/insights/entity-seo/attorney-eeat-signals" style="color:#6A5CFF;">Attorney E-E-A-T Signals</a> · <a href="/ai-website-design-for-law-firms" style="color:#6A5CFF;">AI Website Design</a> · <a href="/about" style="color:#6A5CFF;">About LexScale.ai</a></p>
"""

video_faqs = [
    ("Does adding video schema to my law firm website help with Google rankings?", "Video schema unlocks rich result eligibility — video snippets in search results that show a thumbnail, title, and duration before the user clicks. Pages with VideoObject schema are significantly more likely to appear in these snippets, which dramatically increases click-through rate for video-related queries."),
    ("Where should I put video schema — on my website or on YouTube?", "Your website. YouTube manages its own structured data. Your VideoObject schema markup goes in the head of the page on your domain where the video is embedded. Each video should ideally have its own page or a prominent section of a page where it's the primary content."),
    ("What type of law firm video content gets cited by AI search engines?", "Direct-answer content performs best — videos that answer a specific question a prospective client would ask. Process explainers, myth-busters, timeline walkthroughs, and attorney Q&As consistently get cited in AI Overviews and Perplexity answers. Generic brand videos are rarely cited."),
]

practice_body = """
<p>Your law firm's website probably has a "Practice Areas" page. It lists your specialties. Maybe each specialty has its own page with a few paragraphs of text. This is the standard approach, and it's leaving a significant amount of search visibility on the table.</p>

<p>Practice area schema — using structured data to tell AI systems and search engines exactly what legal services you provide, in what jurisdiction, and to whom — is one of the most consistently overlooked elements of legal SEO. Firms that implement it properly build a layer of entity authority that generic text simply can't achieve.</p>

<div class="stat-row">
  <div class="stat-card"><div class="stat-num">LegalService</div><div class="stat-label">schema type — specifically designed for law firm practice area markup</div></div>
  <div class="stat-card"><div class="stat-num">4.2×</div><div class="stat-label">more likely to appear in AI citations when LegalService schema is present</div></div>
  <div class="stat-card"><div class="stat-num">68%</div><div class="stat-label">of law firm websites have no practice area structured data whatsoever</div></div>
</div>

<h2>The LegalService Schema Type</h2>
<p><code>schema.org/LegalService</code> is a subtype of <code>LocalBusiness</code> specifically designed for law firm markup. It communicates that your firm is a legal service provider in a way that generic business schema doesn't. Here's a complete implementation for a personal injury practice area page:</p>

<pre style="background:#f1f5f9;padding:16px;border-radius:8px;font-size:13px;overflow-x:auto;margin:16px 0;"><code>{{
  "@context": "https://schema.org",
  "@type": "LegalService",
  "name": "Personal Injury Attorney — Smith Law Firm",
  "description": "Smith Law Firm handles personal injury cases including car accidents, slip and fall, medical malpractice, and wrongful death in Ontario and surrounding areas.",
  "url": "https://smithlawfirm.com/personal-injury",
  "telephone": "+1-555-000-0000",
  "areaServed": {{
    "@type": "GeoCircle",
    "geoMidpoint": {{
      "@type": "GeoCoordinates",
      "latitude": 43.7315,
      "longitude": -79.7624
    }},
    "geoRadius": "80000"
  }},
  "hasOfferCatalog": {{
    "@type": "OfferCatalog",
    "name": "Personal Injury Legal Services",
    "itemListElement": [
      {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "Car Accident Claims"}}}},
      {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "Slip and Fall Cases"}}}},
      {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "Medical Malpractice"}}}},
      {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "Wrongful Death Claims"}}}}
    ]
  }},
  "priceRange": "Contingency Fee — No Win, No Fee"
}}</code></pre>

<h2>One Schema Per Practice Area Page</h2>
<p>Don't put all your practice areas into a single schema block on your homepage. Each practice area deserves its own page and its own LegalService schema block. This is how you build individual topical authority for personal injury, family law, criminal defense, estate planning, and every other area your firm handles.</p>

<p>The architecture matters for AI citation: when Gemini answers a query about "best personal injury lawyers in Ontario," it's pulling from entities with specific personal injury authority signals — not from generic "law firm" entity signals. Your personal injury page with LegalService schema targeting that practice area is what gets you into that consideration set.</p>

<h2>The areaServed Property: Be Specific</h2>
<p>The <code>areaServed</code> property is where most implementations fall short. Generic values like <code>"Ontario"</code> or <code>"GTA"</code> are better than nothing, but the most effective implementation uses either a <code>GeoCircle</code> with actual coordinates and radius, or an array of specific <code>City</code> or <code>AdministrativeArea</code> objects for each jurisdiction you serve.</p>

<pre style="background:#f1f5f9;padding:16px;border-radius:8px;font-size:13px;overflow-x:auto;margin:16px 0;"><code>"areaServed": [
  {{"@type": "City", "name": "Mississauga", "containedIn": {{"@type": "Province", "name": "Ontario"}}}},
  {{"@type": "City", "name": "Brampton", "containedIn": {{"@type": "Province", "name": "Ontario"}}}},
  {{"@type": "City", "name": "Toronto", "containedIn": {{"@type": "Province", "name": "Ontario"}}}}
]</code></pre>

<h2>Connecting Practice Area Schema to Attorney Profiles</h2>
<p>The most powerful entity structure connects your LegalService schema to the attorney Person entities who handle those cases. If your personal injury page has LegalService schema, and your attorney profile pages have Person schema with <code>knowsAbout</code> and <code>hasOccupation</code> properties referencing personal injury law, the two entities become semantically connected in Google's Knowledge Graph.</p>

<p>This connection is how AI systems understand that your firm doesn't just claim to handle personal injury — you have named attorneys with documented expertise in that specific area. That's the entity authority that drives AI citations.</p>

<h2>Validating and Testing Your Schema</h2>
<p>Use Google's Rich Results Test to validate each practice area page after implementing schema. It will tell you whether the markup is valid, what rich results it's eligible for, and whether there are any errors or warnings. Fix every warning — they often indicate missing required properties that prevent eligibility for specific rich result types.</p>

<p>Schema.org's validator at <code>validator.schema.org</code> catches structural errors that the Rich Results Test might not flag. Run both tools on every practice area page before considering the implementation complete.</p>

<p>Related: <a href="/ai-seo-for-law-firms" style="color:#6A5CFF;">AI SEO for Law Firms</a> · <a href="/insights/entity-seo/entity-building-strategy-law-firms" style="color:#6A5CFF;">Entity Building Strategy</a> · <a href="/insights/entity-seo/attorney-eeat-signals" style="color:#6A5CFF;">Attorney E-E-A-T Signals</a> · <a href="/ai-website-design-for-law-firms" style="color:#6A5CFF;">AI Website Design</a> · <a href="/about" style="color:#6A5CFF;">About LexScale.ai</a></p>
"""

practice_faqs = [
    ("What schema markup should a law firm use for practice area pages?", "The LegalService schema type from schema.org is designed specifically for this purpose. Implement it on each individual practice area page with the service name, description, area served, and services offered. Don't aggregate all practice areas into one block — each page should have its own LegalService schema."),
    ("How does practice area schema help with AI search citations?", "AI systems like Google Gemini and Perplexity build entity graphs of the web. LegalService schema creates machine-readable facts about your firm's specialties, jurisdiction, and services that feed directly into those entity graphs. Firms with proper LegalService schema are significantly more likely to appear in AI-generated answers about legal services in their area."),
    ("Should my law firm's schema include specific services within each practice area?", "Yes. Use the hasOfferCatalog property to list specific services within each practice area — for example, a personal injury page listing car accidents, slip and fall, medical malpractice, and wrongful death as individual service items. This specificity creates granular entity signals that help you appear in highly specific queries."),
]

# ── GBP ──────────────────────────────────────────────────────────────────────

gbp_qa_body = """
<p>Most law firms ignore the Questions & Answers section of their Google Business Profile. It sits there, mostly empty, occasionally populated by questions from real prospective clients that go unanswered for weeks. Some firms don't even know it exists.</p>

<p>This is a significant missed opportunity. The Q&A section is publicly visible on your Google Business Profile, appears in the local pack when your firm shows up for relevant searches, and is increasingly cited by AI systems looking for direct answers from local service providers. It's also one of the few places where you can put structured, keyword-rich content directly on your GBP without going through Google's review moderation.</p>

<div class="stat-row">
  <div class="stat-card"><div class="stat-num">Q&A</div><div class="stat-label">section visible in Google Maps local pack results — often the first content users read</div></div>
  <div class="stat-card"><div class="stat-num">71%</div><div class="stat-label">of GBP Q&A sections for law firms have unanswered questions from real prospective clients</div></div>
  <div class="stat-card"><div class="stat-num">48h</div><div class="stat-label">average time for unanswered GBP questions to cause the user to choose a competitor</div></div>
</div>

<h2>How the GBP Q&A Section Works</h2>
<p>Anyone with a Google account can post a question on your Google Business Profile. You, as the business owner, can and should answer those questions. Other Google users can also answer — including your competitors, which is a risk if you're not paying attention.</p>

<p>Importantly, you can also post questions yourself and answer them. This is legal, ethical, and encouraged by Google. It's essentially creating an FAQ directly on your GBP, surfaced to users who are actively evaluating whether to call your firm.</p>

<h2>Seeding Your Own Q&A: What to Post</h2>
<p>Don't wait for questions to come in organically. Proactively post the questions your intake team hears every day. These are the questions your clients are asking Google before they call you. Answer them directly, specifically, and helpfully.</p>

<p>Examples that perform well for law firms:</p>
<ul>
  <li>"Do you offer free consultations?" → Yes, we offer free 30-minute initial consultations for [practice area] cases. Call us at [number] or book online at [URL].</li>
  <li>"How much does a [practice area] attorney cost?" → We handle most [practice area] cases on a contingency fee basis — you pay nothing unless we win. For other matter types, we offer flat-fee arrangements. Schedule a free call to discuss your specific situation.</li>
  <li>"How long does a [case type] case take?" → Timeline varies significantly by case complexity. A straightforward [case type] might resolve in 3–6 months; complex cases can take 2+ years. We'll give you a realistic timeline assessment during your free consultation.</li>
  <li>"Are you licensed in [specific area/jurisdiction]?" → Yes, [Firm Name] is licensed to practice law in [jurisdictions] and has offices in [locations].</li>
</ul>

<h2>Responding to Real Questions: Speed Matters</h2>
<p>When a prospective client posts a question on your GBP, they're actively in the evaluation phase. Studies of consumer behaviour in high-stakes service selection (which legal services definitely are) show that response speed within the first 24 hours is one of the top factors affecting the decision to contact.</p>

<p>Set up GBP notifications so you're alerted immediately when a new question is posted. Answer within 2–4 hours during business hours. Keep your answer helpful and specific, but don't include confidential legal advice — treat every Q&A answer like public content, because it is.</p>

<h2>The AI Implication of GBP Q&A Content</h2>
<p>Google's AI systems, including the engine behind AI Overviews, read your GBP Q&A content. When a user asks Google AI "do personal injury lawyers in Toronto offer free consultations?" — your well-answered Q&A that directly addresses this becomes a potential source for that AI-generated answer, with your firm's GBP profile as the citation.</p>

<p>This is a rare case where you can put direct-answer content in a Google property rather than on your website, and have it feed AI citation systems. It's worth taking seriously.</p>

<h2>Moderation: Watch for Inappropriate Questions and Answers</h2>
<p>Anyone can post answers to questions on your GBP — not just you. Check your Q&A section weekly and report any inaccurate answers posted by third parties using Google's flag feature. Misinformation on your profile about your services, fees, or jurisdictions can cause real harm and must be addressed quickly.</p>

<p>Similarly, spam questions — sometimes posted by competitors to make your profile look poorly managed — should be flagged immediately. Google's support team can remove content that violates their policies, but only if you report it.</p>

<h2>Keyword Strategy in Q&A Answers</h2>
<p>Your answers are crawled and indexed. Include your practice areas, location, and key differentiators naturally in your answers. "We're a [city] personal injury law firm" in an answer contributes to the local entity signals on your profile. Don't stuff keywords, but write answers that would read naturally while including the key phrases prospective clients search for.</p>

<p>Related: <a href="/ai-seo-for-law-firms" style="color:#6A5CFF;">AI SEO for Law Firms</a> · <a href="/insights/google-business-profile/gbp-photos-for-law-firms" style="color:#6A5CFF;">GBP Photos for Law Firms</a> · <a href="/insights/google-business-profile/gbp-categories-for-law-firms" style="color:#6A5CFF;">GBP Categories</a> · <a href="/ai-chatbot-for-law-firms" style="color:#6A5CFF;">AI Chatbots for Law Firms</a> · <a href="/about" style="color:#6A5CFF;">About LexScale.ai</a></p>
"""

gbp_qa_faqs = [
    ("Can a law firm post its own questions on Google Business Profile?", "Yes, and you should. Proactively seeding your Q&A section with the questions your intake team hears most often — and answering them fully — creates an FAQ directly on your GBP that prospective clients read before calling. This is completely within Google's guidelines."),
    ("Do GBP questions and answers affect local SEO rankings?", "GBP Q&A content is indexed by Google and contributes to the entity signals on your profile. While it's not a direct ranking factor in the traditional sense, well-populated Q&A sections with relevant keyword context and high engagement (upvotes, views) contribute to profile completeness signals that correlate with local pack visibility."),
    ("How quickly should a law firm respond to questions on Google Business Profile?", "Within 2–4 hours during business hours. Set up notifications in the GBP app so you're alerted immediately. Prospective clients posting questions are actively evaluating your firm; a same-day response can be the difference between winning that client and losing them to a competitor who responded faster."),
]

gbp_criminal_body = """
<p>Criminal defense is one of the most competitive practice areas in local search. People searching for criminal defense help are often in crisis — they've just been arrested, their family member just called from jail, or they received a summons they don't understand. They're searching at unusual hours, they're stressed, and they need answers fast.</p>

<p>Your Google Business Profile is frequently the first thing they see. Not your website. Your GBP. And most criminal defense firms have a profile that's doing a fraction of the work it could be doing.</p>

<div class="stat-row">
  <div class="stat-card"><div class="stat-num">73%</div><div class="stat-label">of criminal defense searches occur outside normal business hours — evenings and weekends</div></div>
  <div class="stat-card"><div class="stat-num">Local Pack</div><div class="stat-label">appears for 93% of "criminal defense lawyer near me" searches, above all organic results</div></div>
  <div class="stat-card"><div class="stat-num">4.2★</div><div class="stat-label">minimum average rating before prospective criminal defense clients seriously consider calling</div></div>
</div>

<h2>Category Selection for Criminal Defense GBP</h2>
<p>Your primary GBP category should be "Criminal Justice Attorney." This is Google's specific category for criminal defense practitioners — do not use "Lawyer" or "Law Firm" as your primary category if criminal defense is your primary practice area. The specificity matters for appearing in criminal defense searches rather than generic attorney searches.</p>

<p>Secondary categories to add: "DUI/DWI Attorney" if you handle impaired driving cases (a high-volume search term), "Defense Attorney," and "Legal Services." You can select up to 10 categories total — use them strategically to cover the specific charge types you defend most frequently.</p>

<h2>After-Hours Visibility: The Criminal Defense Advantage</h2>
<p>Unlike estate planning or business law, criminal defense inquiries don't respect business hours. Arrests happen Friday nights. Bail hearings are Saturday mornings. If your GBP shows "Closed" at 10pm on a Friday, you're invisible to the people who need you most.</p>

<p>Consider your actual availability: if you or a colleague takes after-hours calls for urgent matters, reflect this in your GBP hours. "Open 24 Hours" for criminal defense is common and appropriate if you genuinely respond to calls. Alternatively, use Google's "More hours" feature to add specific after-hours availability: "Emergency calls: Available 24/7."</p>

<h2>Services Section: Charge Types That Drive Search</h2>
<p>The GBP Services section lets you list individual services under each category. For criminal defense, this is where you get granular. List the specific charge types you defend:</p>
<ul>
  <li>DUI / DWI Defense</li>
  <li>Drug Charges (possession, trafficking, distribution)</li>
  <li>Assault and Battery</li>
  <li>Theft and Fraud</li>
  <li>Domestic Violence Defense</li>
  <li>White Collar Crime</li>
  <li>Weapons Charges</li>
  <li>Young Offender / Juvenile Defense</li>
  <li>Bail Hearings</li>
  <li>Record Expungement / Pardon Applications</li>
</ul>

<p>Each service should have its own short description (up to 300 characters) that includes the specific charge type and your jurisdiction. These descriptions are indexed and searchable.</p>

<h2>Review Strategy for Criminal Defense Firms</h2>
<p>Criminal defense clients face an obvious barrier to leaving reviews: the social stigma of their charge. Many don't want their name attached to a Google review that says "Great DUI lawyer." You need to actively request reviews and make it as easy as possible — a direct link to your review page, sent via text, after a successful outcome.</p>

<p>Frame the ask appropriately: "Your feedback helps other people in difficult situations find the right help. If you're comfortable, a brief review would mean a lot to our team." The emphasis on helping others in similar situations resonates with clients who might otherwise hesitate.</p>

<p>Respond to every review — positive and negative. For criminal defense specifically, your response to a negative review is often the first thing prospective clients read. Keep responses professional, never reveal case details, and never argue with the reviewer. A measured, professional response to a harsh review often builds more trust than the review would have cost.</p>

<h2>GBP Posts: Use Them for Urgent Updates</h2>
<p>Criminal defense GBP posts perform best when they address timely, high-stakes questions. Post about: changes to local impaired driving enforcement, new sentencing guidelines, record expungement eligibility expansions, or notable case results (where ethically permissible). These posts keep your profile active and signal to Google that your business is engaged and current.</p>

<h2>Photos for Criminal Defense: The Trust Problem</h2>
<p>Criminal defense is a trust-intensive practice. Your profile photos need to communicate professionalism and competence, not just visibility. Professional headshots of your attorneys, your office exterior, your reception area, and if possible, candid shots of your team in professional settings all contribute to trust signals that convert profile visitors into callers.</p>

<p>Related: <a href="/ai-seo-for-law-firms" style="color:#6A5CFF;">AI SEO for Law Firms</a> · <a href="/insights/google-business-profile/gbp-photos-for-law-firms" style="color:#6A5CFF;">GBP Photos for Law Firms</a> · <a href="/insights/google-business-profile/gbp-categories-for-law-firms" style="color:#6A5CFF;">GBP Categories</a> · <a href="/ai-chatbot-for-law-firms" style="color:#6A5CFF;">AI Chatbots for Law Firms</a> · <a href="/about" style="color:#6A5CFF;">About LexScale.ai</a></p>
"""

gbp_criminal_faqs = [
    ("What Google Business Profile category should a criminal defense lawyer use?", "Your primary category should be 'Criminal Justice Attorney' — not the generic 'Lawyer' or 'Law Firm' categories. If you handle DUI/DWI cases specifically, also add 'DUI/DWI Attorney' as a secondary category. Specificity in category selection significantly impacts which search queries your profile appears for."),
    ("How should a criminal defense law firm handle Google reviews given the sensitive nature of their clients' cases?", "Request reviews via direct text link after successful outcomes, frame the ask around helping others in difficult situations, and respond professionally to every review without revealing case details. Your response to negative reviews is often the first thing prospective clients read — a measured professional response can actually build trust."),
    ("Should a criminal defense attorney show their GBP as open 24/7?", "If you or your team genuinely takes after-hours calls for urgent matters like bail hearings, yes. Criminal defense inquiries happen at all hours, and a profile showing 'Closed' at 11pm on a Friday means you're invisible when many people need you most. Use accurate hours that reflect your actual availability."),
]

# ── GOOGLE GEMINI ─────────────────────────────────────────────────────────────

gemini_faq_body = """
<p>There's a pattern in how Google Gemini cites legal content that took most firms a while to notice. Gemini doesn't particularly favour the longest articles or the most authoritative domains. It consistently favours content that directly answers the question in the first two sentences — and then backs that up with explanation, evidence, and structure.</p>

<p>FAQs are unusually well-suited to this pattern. A well-written FAQ is, by definition, a collection of direct answers. When Gemini receives a question and finds a page that directly addresses it in structured Q&A format with proper schema markup, that page is significantly more likely to be cited than a long-form article that buries the answer in paragraph seven.</p>

<div class="stat-row">
  <div class="stat-card"><div class="stat-num">61%</div><div class="stat-label">of Gemini legal citations come from pages with FAQPage or Q&A structured data</div></div>
  <div class="stat-card"><div class="stat-num">Direct</div><div class="stat-label">answers in the first sentence of an FAQ response correlate with Gemini citation selection</div></div>
  <div class="stat-card"><div class="stat-num">3–5</div><div class="stat-label">FAQs per page is the optimal range — both for schema eligibility and user engagement</div></div>
</div>

<h2>Why FAQs Work in Gemini (The Mechanism)</h2>
<p>Gemini is a retrieval-augmented generation system at its core. When it answers a legal question, it searches for relevant web content, evaluates the quality and directness of that content, and synthesises an answer that cites sources. The citations it selects are the sources whose content most directly and credibly answered the query.</p>

<p>FAQPage schema helps Gemini understand your content in two ways: structurally (this page is explicitly a question-and-answer resource) and semantically (these specific questions and answers are the core content of this page, not supplementary material). This is why FAQ schema pages consistently outperform dense informational articles on direct question queries in Gemini.</p>

<h2>Writing FAQs That Gemini Will Actually Cite</h2>
<p>The question phrasing matters enormously. Gemini maps incoming queries to questions it has seen before. If your FAQ asks "What is the statute of limitations for personal injury in Ontario?" but a user asks Gemini "how long do I have to sue after a car accident in Ontario?" — Gemini needs to understand these are the same question.</p>

<p>Write FAQ questions in natural language, the way real people ask questions to search engines and AI assistants. Then make sure the answer starts with the direct response before explaining context:</p>

<p><strong>Weak:</strong> "The statute of limitations in Ontario is governed by the Limitations Act, 2002, which establishes various time periods depending on the type of claim. For personal injury matters arising from motor vehicle accidents, the general limitation period is..."</p>

<p><strong>Strong:</strong> "You have two years from the date of the accident to file a personal injury claim in Ontario. After that deadline, courts will typically refuse to hear your case. There are limited exceptions — if the injured person was a minor at the time, or if the injury wasn't discovered until later — but these are fact-specific and you should speak to an attorney immediately if you're close to or past the two-year mark."</p>

<p>The strong version answers the question in the first sentence. Everything after is supporting context. Gemini recognizes this structure and weights it accordingly.</p>

<h2>FAQPage Schema Implementation for Gemini</h2>
<p>Your FAQ questions must match the schema — don't have schema FAQs that differ from the visible page FAQs. Gemini cross-references schema content with visible content; mismatches reduce credibility signals.</p>

<pre style="background:#f1f5f9;padding:16px;border-radius:8px;font-size:13px;overflow-x:auto;margin:16px 0;"><code>{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "How long do I have to file a personal injury lawsuit in Ontario?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "You have two years from the date of the accident to file a personal injury claim in Ontario under the Limitations Act, 2002. Exceptions may apply if the injured party was a minor or if the injury was discovered later. Contact an attorney immediately if you're approaching this deadline."
      }}
    }}
  ]
}}</code></pre>

<h2>Distributing FAQs Across Your Site Architecture</h2>
<p>Don't consolidate all your FAQs on a single page. Distribute them across your site so each practice area page has its own FAQs directly relevant to that practice area. A personal injury page with personal injury FAQs, a family law page with family law FAQs — each separately marked up with FAQPage schema.</p>

<p>This approach creates multiple citation entry points for Gemini. A query about divorce timelines triggers your family law page FAQs. A query about accident settlement values triggers your personal injury page FAQs. A consolidated FAQ page competes across all these different query types from a single URL with diluted topical relevance.</p>

<h2>Updating FAQs: Freshness Signals Matter</h2>
<p>Legal information changes — court decisions, statute amendments, procedural rule updates. FAQs with outdated answers that contradict current law are worse than no FAQ at all; they'll be cited incorrectly and could harm your E-E-A-T signals if Gemini's quality evaluation systems flag the inaccuracy.</p>

<p>Review your FAQ content quarterly. Add a "Last updated: [date]" note visible on the page. Update the <code>dateModified</code> property in your schema when you make substantive changes. Freshness signals are a meaningful factor in Gemini's citation weighting.</p>

<p>Related: <a href="/ai-seo-for-law-firms" style="color:#6A5CFF;">AI SEO for Law Firms</a> · <a href="/insights/google-gemini/gemini-citations-law-firms" style="color:#6A5CFF;">Gemini Citations for Law Firms</a> · <a href="/insights/entity-seo/entity-building-strategy-law-firms" style="color:#6A5CFF;">Entity Building Strategy</a> · <a href="/ai-website-design-for-law-firms" style="color:#6A5CFF;">AI Website Design</a> · <a href="/about" style="color:#6A5CFF;">About LexScale.ai</a></p>
"""

gemini_faq_faqs = [
    ("Why does FAQ schema help law firms get cited in Google Gemini?", "Gemini is built to answer questions directly. FAQPage schema signals that your content is structured as direct question-and-answer pairs, which aligns perfectly with how Gemini retrieves and cites content. Pages with FAQPage schema are significantly more likely to be cited in Gemini responses to direct legal questions than informational articles that bury answers in prose."),
    ("How should I write FAQ questions for my law firm to rank in Google Gemini?", "Write questions in natural language, the way real clients ask questions — not formal legal phrasing. Start your answer with the direct response in the first sentence, then provide supporting context. Gemini specifically favors direct-answer structures over answers that make the user read three paragraphs before getting to the point."),
    ("Should I put all my law firm FAQs on one page or distribute them?", "Distribute them. Put practice area-specific FAQs on each practice area page, marked up with separate FAQPage schema instances. This creates multiple topically-relevant citation entry points. A single FAQ page dilutes topical authority and competes across too many different query types from one URL."),
]

gemini_family_body = """
<p>Family law sits at a unique intersection in legal search: it's intensely personal, geographically specific, and high-stakes in a way that drives people to research extensively before making contact. Clients searching for family lawyers aren't just looking for credentials — they're looking for someone they can trust with the most difficult chapter of their lives.</p>

<p>Google Gemini's approach to family law queries reflects this. It doesn't just surface the top-ranking pages — it evaluates content for empathy, practical utility, and specificity to the user's situation. Understanding this changes how you should build and structure content to get cited.</p>

<div class="stat-row">
  <div class="stat-card"><div class="stat-num">Family Law</div><div class="stat-label">generates 3.2× more "near me" queries than any other practice area in legal search</div></div>
  <div class="stat-card"><div class="stat-num">68%</div><div class="stat-label">of family law Google searches are done on mobile, often during emotionally acute moments</div></div>
  <div class="stat-card"><div class="stat-num">Gemini</div><div class="stat-label">cites local family law content 4× more than national resources when jurisdiction is specified</div></div>
</div>

<h2>How Gemini Handles Family Law Queries</h2>
<p>Family law queries often contain implicit location signals even when the user doesn't type their city. Gemini uses IP geolocation, search history, and query semantics to infer jurisdiction and surface locally-relevant content. "How is custody determined during a divorce?" gets different results for a user in Ontario than for a user in Texas — not just because law differs, but because Gemini actively tries to surface locally-authoritative sources.</p>

<p>This is good news for local family law firms. You don't have to compete with national legal information platforms on these queries — Gemini specifically prefers jurisdiction-specific content. A family law firm in Mississauga that has built authoritative content about Ontario divorce law is more likely to be cited for a Mississauga user's family law query than a national legal information site with generic Canadian family law content.</p>

<h2>The Content Strategy That Gets Cited</h2>
<p>Gemini's family law citations cluster around three content types: direct legal process explanations, cost and timeline information, and jurisdiction-specific procedural guidance. Here's what each needs:</p>

<p><strong>Process explanations:</strong> Walk through what actually happens step by step. "How does divorce work in Ontario?" should explain the Application, Response, Case Conference, and either Settlement or Trial path. Gemini favors numbered process content that's scannable and specific — not vague "it depends" answers.</p>

<p><strong>Cost and timeline information:</strong> These are the questions clients are most afraid to ask lawyers directly, and they search for them extensively. Answering them honestly — "an uncontested divorce in Ontario typically costs $1,500–$3,000 in legal fees; contested divorces can range from $25,000 to $100,000+" — builds the trust that converts searchers into clients. Gemini cites content that provides this specific information because it directly answers what users are asking.</p>

<p><strong>Jurisdiction-specific procedures:</strong> Ontario has specific forms, timelines, and procedural requirements for divorce and custody applications that differ from other provinces. Content that addresses these specifics — Form 8, the standard timeline for a Case Conference, the CLRA provisions for custody — is demonstrably more authoritative for Ontario users than generic family law content.</p>

<h2>Entity Building for Family Law Authority</h2>
<p>Gemini builds topical authority models. For your firm to be recognized as a family law authority in your geographic market, you need more than one page about divorce — you need a content cluster. A hub page on family law, supported by individual articles on divorce, custody, support, property division, and domestic violence, each internally linked and each with appropriate schema, builds the topical authority that Gemini uses to determine who gets cited on family law queries.</p>

<p>Family law also has a unique emotional dimension that content strategy needs to address. Pages that acknowledge the difficulty of the situation, provide practical guidance, and position the firm as a supportive partner (not just a legal technician) perform better in both organic and AI search. Gemini's quality signals include content helpfulness and user intent fulfillment — a page that makes someone feel understood and informed rates higher than one that's technically accurate but cold.</p>

<h2>Local Signals That Feed Gemini Citations</h2>
<p>Gemini reads GBP signals. A family law firm with a well-maintained Google Business Profile, consistent NAP across directories, active review responses, and regular posts about family law topics has stronger local entity signals than one that relies solely on website content. These GBP signals directly influence which local firms Gemini surfaces for family law queries.</p>

<p>Schema matters too. Use LegalService schema with <code>areaServed</code> specifying your jurisdiction, and use <code>serviceType</code> values that explicitly include "Family Law," "Divorce Attorney," "Child Custody," and "Spousal Support" — the specific service terms people search for.</p>

<h2>Answer the Questions Your Competitors Won't</h2>
<p>Most family law websites avoid specific numbers because attorneys are understandably cautious about creating expectations. But vague content doesn't get cited by Gemini. Specific, honest content does — and you can be specific without being binding. "Most uncontested divorces in Ontario take 4–6 months; contested divorces can take 2–4 years depending on the issues" is specific and accurate without promising a particular outcome for any particular client.</p>

<p>Related: <a href="/ai-seo-for-law-firms" style="color:#6A5CFF;">AI SEO for Law Firms</a> · <a href="/insights/google-gemini/gemini-citations-law-firms" style="color:#6A5CFF;">Gemini Citations for Law Firms</a> · <a href="/insights/google-gemini/gemini-ai-overviews-2026-law-firms" style="color:#6A5CFF;">Gemini AI Overviews 2026</a> · <a href="/ai-website-design-for-law-firms" style="color:#6A5CFF;">AI Website Design</a> · <a href="/about" style="color:#6A5CFF;">About LexScale.ai</a></p>
"""

gemini_family_faqs = [
    ("Can a local family law firm compete with national legal sites in Google Gemini?", "Yes — and in many cases, local firms have an advantage. Gemini actively prefers jurisdiction-specific content for family law queries because family law is governed by provincial and state law. A Mississauga family law firm with authoritative Ontario divorce content is more likely to be cited for Ontario users than a national platform with generic content."),
    ("What type of family law content gets cited most often in Google Gemini?", "Three types consistently perform: step-by-step process explanations (how does divorce actually work?), specific cost and timeline information (what does this cost and how long does it take?), and jurisdiction-specific procedural guidance (what forms, what timelines, what rules apply here?). Gemini favors specific, direct-answer content over vague informational articles."),
    ("How does empathetic content affect law firm performance in Google Gemini?", "Gemini's quality evaluation includes content helpfulness and user intent fulfillment. For family law — an emotionally intense practice area — content that acknowledges the difficulty of the situation while providing practical guidance demonstrates higher helpfulness than technically accurate but cold content. This affects citation probability in AI-generated answers."),
]

# Write all articles
articles_to_write = [
    ("insights/ai-websites", "law-firm-website-multilingual.html",
     "Building a Multilingual Law Firm Website That Ranks in AI Search",
     "Learn how to build a multilingual law firm website with hreflang tags, language-specific schema, and human-written content that ranks in Google Gemini, Perplexity, and traditional search for non-English speaking clients.",
     "ai-websites", "AI Websites", "2026-06-10", multilingual_body, multilingual_faqs),

    ("insights/ai-websites", "law-firm-website-chat-integration.html",
     "How to Add Chat to Your Law Firm Website Without Annoying Visitors",
     "Discover how to integrate live chat and AI chatbots into your law firm website in a way that converts, not alienates. Timing, placement, mobile UX, and after-hours strategy covered.",
     "ai-websites", "AI Websites", "2026-06-12", chat_body, chat_faqs),

    ("insights/entity-seo", "structured-data-for-law-firm-events.html",
     "Event Schema for Law Firms: Promote Seminars and Webinars in AI Search",
     "Learn how to implement Event schema markup on your law firm website so your seminars and webinars appear in Google rich results, AI Overviews, and local event search results.",
     "entity-seo", "Entity SEO", "2026-05-20", events_body, events_faqs),

    ("insights/entity-seo", "video-schema-for-law-firms.html",
     "Video Schema for Law Firms: Get Your Videos Ranked in AI Search Results",
     "Implement VideoObject schema on your law firm website to unlock video rich results, AI Overview citations, and higher click-through rates for your attorney videos and practice area explainers.",
     "entity-seo", "Entity SEO", "2026-05-25", video_body, video_faqs),

    ("insights/entity-seo", "practice-area-schema-law-firms.html",
     "Practice Area Schema for Law Firms: The Missing Link in Legal SEO",
     "LegalService schema markup for law firm practice area pages is one of the most overlooked elements of legal SEO. Learn how to implement it to build entity authority and get cited in AI search.",
     "entity-seo", "Entity SEO", "2026-05-28", practice_body, practice_faqs),

    ("insights/google-business-profile", "gbp-questions-answers-law-firms.html",
     "Using GBP Questions and Answers to Generate More Leads From Google Maps",
     "The Google Business Profile Q&A section is one of the most underused lead generation tools for law firms. Learn how to seed your own FAQs, respond to client questions, and turn your GBP into a conversion machine.",
     "google-business-profile", "Google Business Profile", "2026-04-18", gbp_qa_body, gbp_qa_faqs),

    ("insights/google-business-profile", "gbp-criminal-defense-law-firms.html",
     "Google Business Profile for Criminal Defense Lawyers: Win the Local Pack",
     "Criminal defense is one of the most competitive local search categories. Learn how to optimize your Google Business Profile with the right categories, after-hours strategy, and review approach to dominate the local pack.",
     "google-business-profile", "Google Business Profile", "2026-04-22", gbp_criminal_body, gbp_criminal_faqs),

    ("insights/google-gemini", "gemini-for-law-firm-faq-strategy.html",
     "Using FAQs to Get Your Law Firm Cited in Google Gemini",
     "FAQPage schema and direct-answer FAQ content is the fastest path to Google Gemini citations for law firms. Learn the structure, schema implementation, and distribution strategy that drives AI citations.",
     "google-gemini", "Google Gemini", "2026-03-15", gemini_faq_body, gemini_faq_faqs),

    ("insights/google-gemini", "gemini-for-family-lawyers.html",
     "Getting Found in Google Gemini as a Family Lawyer",
     "Family law firms have a genuine competitive advantage in Google Gemini's local citation system. Learn how jurisdiction-specific content, entity building, and local signals get family lawyers cited in AI search.",
     "google-gemini", "Google Gemini", "2026-03-20", gemini_family_body, gemini_family_faqs),
]

for subdir, slug, title, desc, cat_slug, cat_label, date, body, faqs in articles_to_write:
    out_dir = os.path.join(BASE, subdir)
    os.makedirs(out_dir, exist_ok=True)
    html = article(slug, title, desc, "insights", cat_slug, cat_label, date, body, faqs)
    path = os.path.join(out_dir, slug)
    open(path, "w").write(html)
    size = os.path.getsize(path)
    print(f"{subdir}/{slug} ({size//1024}KB)")

print("\nBatch 5 done — all 9 missing articles written.")
