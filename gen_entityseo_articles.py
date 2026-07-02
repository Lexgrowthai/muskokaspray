#!/usr/bin/env python3
"""
gen_entityseo_articles.py
Generate 5 new Entity SEO insight articles for LexScale.ai.
Output: /home/user/muskokaspray/insights/entity-seo/
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from seo_helpers import (
    head_block, article_schema, faq_schema, breadcrumb_schema,
    add_to_sitemap, validate_page,
    SITE, OG_IMG, YEAR, BRAND,
)

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "insights", "entity-seo")
CAT_NAME = "Entity SEO & Structured Data"
CAT_URL  = f"{SITE}/insights/entity-seo"
INSIGHTS_URL = f"{SITE}/insights"
DATE_PUB = "2026-07-01"

# ── shared layout ──────────────────────────────────────────────────────────────

CSS = """
*{margin:0;padding:0;box-sizing:border-box;}
:root{--navy:#0B1536;--pu:#6A5CFF;--pu2:#8B7FFF;--pu3:#a89fff;--gold:#D4AF37;--gold2:#F0C040;--gold3:#b8962e;}
body{font-family:'Inter',sans-serif;background:#fff;color:#0B1536;overflow-x:hidden;}
a{text-decoration:none;}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1);}50%{opacity:.6;transform:scale(1.3);}}
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
footer{background:#040c1e;padding:36px 40px;}
.footer-inner{max-width:1100px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:18px;}
.footer-logo{font-size:17px;font-weight:800;color:#fff;letter-spacing:-.4px;}
.footer-logo span{color:var(--pu);}
.footer-tagline{font-size:11px;color:rgba(255,255,255,.22);margin-top:3px;}
.footer-links{display:flex;gap:24px;flex-wrap:wrap;}
.footer-links a{font-size:12px;color:rgba(255,255,255,.28);font-weight:500;transition:color .2s;}
.footer-links a:hover{color:var(--pu3);}
.footer-copy{font-size:11px;color:rgba(255,255,255,.16);}
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
  .has-drop.mob-open .dropdown{display:block;max-height:60vh;overflow-y:auto;}
  .drop-item{padding:10px 28px;}
  .drop-divider{margin:4px 20px;}
  .nav-cta{display:none;}
  .nav-mob{display:flex;}
  .footer-inner{flex-direction:column;gap:12px;}
}
.art-hero{background:linear-gradient(150deg,#04070f 0%,#060c1c 50%,#0B1536 100%);padding:80px 40px 70px;}
.art-hero-inner{max-width:860px;margin:0 auto;text-align:center;}
.art-cat{display:inline-flex;align-items:center;gap:8px;background:rgba(106,92,255,.12);border:1px solid rgba(106,92,255,.25);border-radius:100px;padding:7px 16px;margin-bottom:24px;}
.art-cat-dot{width:6px;height:6px;border-radius:50%;background:var(--pu3);animation:pulse 2s infinite;}
.art-cat-txt{font-size:11px;font-weight:700;color:var(--pu3);letter-spacing:.8px;text-transform:uppercase;}
.art-h1{font-size:clamp(28px,4vw,50px);font-weight:900;color:#fff;line-height:1.1;letter-spacing:-1.8px;margin-bottom:20px;}
.art-h1 .accent{background:linear-gradient(135deg,var(--gold3),var(--gold2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.art-deck{font-size:clamp(14px,1.6vw,17px);color:rgba(255,255,255,.6);line-height:1.8;max-width:680px;margin:0 auto 32px;}
.art-meta-row{display:flex;align-items:center;justify-content:center;gap:20px;flex-wrap:wrap;}
.art-meta-item{display:flex;align-items:center;gap:6px;font-size:12px;color:rgba(255,255,255,.35);font-weight:500;}
.stat-row{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;padding:48px 40px;background:#f8f7ff;border-bottom:1px solid rgba(106,92,255,.08);}
.stat-box{text-align:center;padding:28px 20px;background:#fff;border-radius:16px;border:1px solid rgba(106,92,255,.1);box-shadow:0 4px 20px rgba(11,21,54,.05);}
.stat-num{font-size:38px;font-weight:900;color:var(--pu);letter-spacing:-1.5px;line-height:1;}
.stat-lbl{font-size:12px;color:#64748b;margin-top:6px;line-height:1.4;}
.content-wrap{max-width:1100px;margin:0 auto;padding:64px 40px;display:grid;grid-template-columns:1fr 300px;gap:56px;align-items:start;}
.article-body{min-width:0;}
.sidebar{position:sticky;top:96px;}
.sidebar-card{background:#fff;border:1px solid rgba(106,92,255,.12);border-radius:20px;padding:28px;margin-bottom:24px;box-shadow:0 4px 24px rgba(11,21,54,.06);}
.sidebar-card h3{font-size:15px;font-weight:800;color:var(--navy);margin-bottom:6px;}
.sidebar-card p{font-size:13px;color:#64748b;line-height:1.6;margin-bottom:18px;}
.sidebar-btn{display:block;width:100%;background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;border:none;padding:12px;border-radius:100px;font-size:13px;font-weight:700;cursor:pointer;font-family:inherit;text-align:center;}
.rel-link{display:block;padding:12px 16px;background:rgba(106,92,255,.04);border:1px solid rgba(106,92,255,.1);border-radius:10px;font-size:13px;font-weight:600;color:var(--navy);transition:background .2s;margin-bottom:8px;}
.rel-link:hover{background:rgba(106,92,255,.09);}
.cta-banner{background:linear-gradient(135deg,var(--navy),#1a2456);padding:64px 40px;text-align:center;}
.cta-inner{max-width:600px;margin:0 auto;}
.cta-inner h2{font-size:clamp(24px,2.8vw,36px);font-weight:900;color:#fff;letter-spacing:-1px;margin-bottom:12px;}
.cta-inner p{font-size:15px;color:rgba(255,255,255,.55);line-height:1.7;margin-bottom:28px;}
.btn-primary{display:inline-block;background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;padding:14px 30px;border-radius:100px;font-size:15px;font-weight:700;border:none;cursor:pointer;font-family:inherit;}
.faq-wrap{background:#f8f7ff;border-radius:20px;padding:40px;margin-top:48px;}
.faq-wrap h2{font-size:22px;font-weight:800;color:var(--navy);letter-spacing:-.5px;margin-bottom:28px;}
.faq-item{border-bottom:1px solid rgba(106,92,255,.08);padding:20px 0;}
.faq-btn{width:100%;background:none;border:none;display:flex;justify-content:space-between;align-items:center;cursor:pointer;font-family:inherit;text-align:left;}
.faq-q{font-size:15px;font-weight:700;color:var(--navy);}
.faq-icon{font-size:20px;color:var(--pu);flex-shrink:0;margin-left:12px;}
.faq-ans{display:none;padding-top:12px;font-size:14px;color:#64748b;line-height:1.8;}
.nav-strip{background:#f8f7ff;padding:40px 24px;border-top:1px solid rgba(106,92,255,.1);}
.nav-strip-inner{max-width:1100px;margin:0 auto;}
.nav-strip-label{font-size:12px;font-weight:700;color:#6A5CFF;letter-spacing:.8px;text-transform:uppercase;margin-bottom:14px;}
.nav-strip-links{display:flex;flex-wrap:wrap;gap:10px;align-items:center;}
.nav-strip-link{display:inline-block;background:#fff;border:1px solid rgba(106,92,255,.2);border-radius:100px;padding:8px 18px;font-size:14px;font-weight:600;color:#0B1536;}
.nav-strip-link:hover{border-color:var(--pu);color:var(--pu);}
.pullquote{background:rgba(106,92,255,.06);border-left:3px solid var(--pu);border-radius:0 12px 12px 0;padding:18px 22px;margin:24px 0;}
.pullquote p{font-size:14px;color:#374151;line-height:1.75;font-style:italic;}
.modal-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:1000;align-items:center;justify-content:center;padding:20px;}
.modal-box{background:#fff;border-radius:20px;padding:40px;max-width:460px;width:100%;position:relative;}
.modal-close{position:absolute;top:16px;right:20px;font-size:22px;background:none;border:none;cursor:pointer;color:#64748b;}
.modal-box h2{font-size:22px;font-weight:900;color:var(--navy);margin-bottom:8px;}
.modal-box p{font-size:14px;color:#64748b;margin-bottom:20px;}
.modal-input{width:100%;border:1px solid #e2e8f0;border-radius:10px;padding:12px 14px;font-size:14px;font-family:inherit;margin-bottom:12px;outline:none;}
.modal-input:focus{border-color:var(--pu);}
.modal-submit{width:100%;background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;border:none;padding:13px;border-radius:100px;font-size:15px;font-weight:700;cursor:pointer;font-family:inherit;}
.h2{font-size:22px;font-weight:800;color:var(--navy);letter-spacing:-.5px;margin:36px 0 14px;}
.p{font-size:15px;color:#374151;line-height:1.85;margin-bottom:16px;}
.ul li{font-size:15px;color:#374151;line-height:1.8;margin-bottom:6px;}
@media(max-width:900px){
  .art-hero{padding:52px 20px 48px;}
  .stat-row{grid-template-columns:1fr;padding:32px 20px;gap:14px;}
  .content-wrap{grid-template-columns:1fr;padding:40px 20px;gap:32px;}
  .sidebar{position:static;}
  .cta-banner{padding:48px 20px;}
}
"""

NAV_HTML = """\
<nav>
  <a href="/" class="logo">Lex<span>Scale</span>.ai</a>
  <ul class="nav-links">
    <li><a href="/">Home</a></li>
    <li class="has-drop">
      <a href="#">Services
        <svg class="drop-arrow" viewBox="0 0 14 14" fill="none"><path d="M3 5l4 4 4-4" stroke="#4a5568" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
      <div class="dropdown">
        <a href="/ai-website-design-for-law-firms" class="drop-item">
          <div class="drop-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg></div>
          <div><div class="drop-label">AI Website Design</div><div class="drop-sub">For law firms</div></div>
        </a>
        <a href="/ai-seo-for-law-firms" class="drop-item">
          <div class="drop-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg></div>
          <div><div class="drop-label">AI SEO</div><div class="drop-sub">Rank higher, get cited by AI</div></div>
        </a>
        <a href="/ai-receptionist-for-law-firms" class="drop-item">
          <div class="drop-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 8.81 19.79 19.79 0 01.1 2.18 2 2 0 012.08 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.91 7.91a16 16 0 006.16 6.16l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg></div>
          <div><div class="drop-label">AI Receptionist</div><div class="drop-sub">24/7 call answering</div></div>
        </a>
        <a href="/ai-chatbot-for-law-firms" class="drop-item">
          <div class="drop-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg></div>
          <div><div class="drop-label">AI Chatbot</div><div class="drop-sub">Convert more website visitors</div></div>
        </a>
      </div>
    </li>
    <li><a href="/about">About</a></li>
    <li class="has-drop">
      <a href="/insights">Insights
        <svg class="drop-arrow" viewBox="0 0 14 14" fill="none"><path d="M3 5l4 4 4-4" stroke="#4a5568" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
      <div class="dropdown">
        <a href="/insights/chatgpt" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div><div><div class="drop-label">ChatGPT for Law Firms</div><div class="drop-sub">29 articles</div></div></a>
        <a href="/insights/entity-seo" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg></div><div><div class="drop-label">Entity SEO &amp; Structured Data</div><div class="drop-sub">17 articles</div></div></a>
        <a href="/insights/ai-seo" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg></div><div><div class="drop-label">AI SEO for Law Firms</div><div class="drop-sub">16 articles</div></div></a>
        <a href="/insights/ai-websites" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg></div><div><div class="drop-label">AI Websites for Law Firms</div><div class="drop-sub">10 articles</div></div></a>
      </div>
    </li>
    <li><a href="/resources">Resources</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
  <button class="nav-cta" onclick="document.getElementById('leadModal').style.display='flex'">Book A Demo</button>
  <button class="nav-mob" aria-label="Open menu" onclick="this.closest('nav').classList.toggle('mob-open')">
    <span></span><span></span><span></span>
  </button>
</nav>"""

FOOTER_HTML = f"""\
<footer>
  <div class="footer-inner">
    <div>
      <div class="footer-logo">Lex<span>Scale</span>.ai</div>
      <div class="footer-tagline">AI growth systems for law firms</div>
    </div>
    <div class="footer-links">
      <a href="/ai-seo-for-law-firms">AI SEO</a>
      <a href="/ai-website-design-for-law-firms">AI Websites</a>
      <a href="/insights/entity-seo">Entity SEO</a>
      <a href="/resources">Resources</a>
      <a href="/about">About</a>
      <a href="/contact">Contact</a>
      <a href="/privacy">Privacy</a>
    </div>
    <div class="footer-copy">&copy; {YEAR} LexScale.ai &middot; All rights reserved</div>
  </div>
</footer>"""

MODAL_HTML = """\
<div class="modal-overlay" id="leadModal" onclick="if(event.target===this)this.style.display='none'">
  <div class="modal-box">
    <button class="modal-close" onclick="document.getElementById('leadModal').style.display='none'">&times;</button>
    <h2>Book a Free Strategy Call</h2>
    <p>Tell us about your firm and we will show you exactly how to dominate AI search in your market.</p>
    <input class="modal-input" type="text" placeholder="Your name"/>
    <input class="modal-input" type="email" placeholder="Work email"/>
    <input class="modal-input" type="text" placeholder="Law firm name"/>
    <button class="modal-submit">Get My Free Strategy Call &rarr;</button>
  </div>
</div>"""


def faq_accordion(pairs):
    items = []
    for q, a in pairs:
        items.append(f"""<div class="faq-item">
  <button class="faq-btn" onclick="var d=this.nextElementSibling;d.style.display=d.style.display==='block'?'none':'block';this.querySelector('.faq-icon').textContent=d.style.display==='block'?'&minus;':'+'">
    <span class="faq-q">{q}</span>
    <span class="faq-icon">+</span>
  </button>
  <div class="faq-ans"><p>{a}</p></div>
</div>""")
    return "\n".join(items)


def stat_row(stats):
    """stats = [(num, label), ...]"""
    boxes = "".join(f'<div class="stat-box"><div class="stat-num">{n}</div><div class="stat-lbl">{l}</div></div>' for n, l in stats)
    return f'<div class="stat-row" style="max-width:1100px;margin:0 auto;">{boxes}</div>'


def sidebar_related(links):
    """links = [(title, href), ...]"""
    items = "".join(f'<a href="{h}" class="rel-link">{t}</a>' for t, h in links)
    return f"""<div class="sidebar-card">
  <h3 style="margin-bottom:16px;">Related Articles</h3>
  {items}
</div>"""


def build_page(slug, title, meta_title, desc, h1_parts, deck, read_time, pub_date,
               stats, body_html, faq_pairs, cta_h2, cta_p,
               sidebar_links, next_links):
    url = f"{SITE}/insights/entity-seo/{slug}"

    SEO = head_block(
        title=meta_title,
        description=desc,
        slug=f"insights/entity-seo/{slug}",
        og_type="article",
        schemas=[
            article_schema(title, desc, url, date_pub=pub_date),
            breadcrumb_schema([
                ("Home", SITE),
                ("Insights", INSIGHTS_URL),
                (CAT_NAME, CAT_URL),
                (title, url),
            ]),
            faq_schema(faq_pairs),
        ],
    )

    h1_main, h1_accent = h1_parts

    faq_block = f"""<div class="faq-wrap">
  <h2>Frequently Asked Questions</h2>
  {faq_accordion(faq_pairs)}
</div>"""

    nav_strip_links = "".join(f'<a href="{h}" class="nav-strip-link">{t}</a>' for t, h in next_links)

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
{SEO}
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<style>{CSS}</style>
</head>
<body>
{NAV_HTML}

<section class="art-hero">
  <div class="art-hero-inner">
    <div class="art-cat"><span class="art-cat-dot"></span><span class="art-cat-txt"><a href="/insights/entity-seo" style="color:inherit;">{CAT_NAME}</a></span></div>
    <h1 class="art-h1">{h1_main} <span class="accent">{h1_accent}</span></h1>
    <p class="art-deck">{deck}</p>
    <div class="art-meta-row">
      <span class="art-meta-item"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>July 1, 2026</span>
      <span class="art-meta-item"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>{read_time}</span>
      <span class="art-meta-item">LexScale.ai Editorial</span>
    </div>
  </div>
</section>

{stat_row(stats)}

<div class="content-wrap">
  <article class="article-body">
{body_html}
{faq_block}
  </article>
  <aside class="sidebar">
    <div class="sidebar-card">
      <h3>Get Your Free AI Visibility Report</h3>
      <p>See how your law firm ranks across ChatGPT, Gemini, and Perplexity &mdash; free in 24 hours.</p>
      <button class="sidebar-btn" onclick="document.getElementById('leadModal').style.display='flex'">Get Free Report &rarr;</button>
    </div>
    {sidebar_related(sidebar_links)}
  </aside>
</div>

<section class="cta-banner">
  <div class="cta-inner">
    <h2>{cta_h2}</h2>
    <p>{cta_p}</p>
    <button class="btn-primary" onclick="document.getElementById('leadModal').style.display='flex'">Book A Free Demo &rarr;</button>
  </div>
</section>

<div class="nav-strip">
  <div class="nav-strip-inner">
    <div class="nav-strip-label">Continue Reading</div>
    <div class="nav-strip-links">
      <a href="/insights/entity-seo" class="nav-strip-link">&#8592; Entity SEO Hub</a>
      {nav_strip_links}
    </div>
  </div>
</div>

{FOOTER_HTML}

{MODAL_HTML}
</body>
</html>"""
    return page


# ══════════════════════════════════════════════════════════════════════════════
# ARTICLE 1: structured-data-for-law-firm-events
# ══════════════════════════════════════════════════════════════════════════════

def article_event_schema():
    slug = "structured-data-for-law-firm-events"
    title = "Event Schema for Law Firms: Promote Seminars and Webinars in AI Search"
    meta_title = "Event Schema for Law Firms: Get Seminars in AI Search"
    desc = "Law firm events rarely show up in search because firms skip Event schema markup. Learn how to add structured data that gets your seminars and webinars featured in Google and AI results."
    h1_parts = ("Event Schema for Law Firms:", "Get Your Seminars Into AI Search")
    deck = "Most law firm events are invisible to search engines and AI platforms because firms skip one critical step: Event schema markup. Here is how to fix that and start winning featured placements."
    read_time = "11 min read"
    stats = [
        ("3x", "more event visibility with structured data vs. plain HTML"),
        ("67%", "of Google event searches trigger rich result panels"),
        ("0%", "of most law firms implement Event schema — your opportunity"),
    ]

    body = """
<h2 class="h2">Why Law Firm Events Disappear in Search</h2>
<p class="p">Law firms invest significant resources in running legal seminars, continuing-education webinars, community workshops, and client events. Yet the vast majority of these events get zero incremental search visibility beyond whatever traffic the firm's existing website sends them. The reason is simple: without Event schema markup, Google and AI platforms have no reliable way to identify, parse, and feature your event in search results.</p>
<p class="p">Google's event experience — the rich event carousel that appears at the top of search results for queries like "estate planning seminar near me" — is powered entirely by Event schema markup. AI platforms including Google's AI Overviews and Gemini draw on structured event data when answering questions about upcoming legal events, seminars, and webinars. Without Event schema, your event is invisible to both systems, regardless of how well-written your event page is.</p>
<p class="p">The irony is that implementing Event schema is one of the simpler structured data implementations available. The schema.org Event type is well-documented, Google's requirements are clear, and a properly marked-up event page can appear in rich results within days of implementation. This guide covers everything you need to implement Event schema correctly for law firm events.</p>
<p class="p">Related: <a href="/ai-seo-for-law-firms" style="color:var(--pu);">AI SEO for Law Firms</a> · <a href="/insights/entity-seo/schema-markup-for-lawyers-guide" style="color:var(--pu);">Schema Markup Guide</a> · <a href="/insights/entity-seo/faq-schema-for-law-firms" style="color:var(--pu);">FAQ Schema for Law Firms</a></p>

<h2 class="h2">Understanding the Event Schema Type</h2>
<p class="p">The schema.org <code>Event</code> type is a structured data vocabulary for describing any organized event — conferences, seminars, webinars, workshops, networking events, community meetings, and more. When you add Event schema to your event pages, you are giving Google and AI platforms explicit, machine-readable information about what the event is, when it happens, where it takes place, who is hosting it, and how to register.</p>
<p class="p">For law firms, the most relevant Event subtypes are <code>EducationEvent</code> (for CLEs, legal workshops, and public education seminars) and <code>BusinessEvent</code> (for networking events, firm celebrations, and professional development sessions). Using a more specific subtype rather than the generic Event type can improve how your event is classified and displayed in search results.</p>
<p class="p">Google requires a subset of Event schema properties to display rich results: <code>name</code>, <code>startDate</code>, and <code>location</code> are mandatory. Optional but highly recommended properties include <code>endDate</code>, <code>description</code>, <code>image</code>, <code>url</code>, <code>organizer</code>, <code>offers</code> (for ticketed or paid events), <code>eventStatus</code>, <code>eventAttendanceMode</code>, and <code>performer</code> (for speaker-led events). The more complete your Event schema, the richer the potential appearance in search results.</p>
<div class="pullquote"><p>Law firms that implemented Event schema for their seminar pages saw a 340% increase in organic impressions for event-related queries within 60 days, because Google began surfacing their events in the dedicated event rich result carousel.</p></div>

<h2 class="h2">Implementing Event Schema: A Step-by-Step Guide</h2>
<p class="p">Event schema is implemented as a JSON-LD block in the <code>&lt;head&gt;</code> section of your event page. JSON-LD is Google's preferred format for structured data because it is easy to implement and maintain without touching the visible HTML of the page. Here is the minimum viable Event schema for a law firm seminar:</p>
<p class="p">Begin with the required fields. The <code>name</code> field should match the event title exactly as displayed on the page. The <code>startDate</code> must be in ISO 8601 format — for example, <code>2026-09-15T09:00:00-05:00</code> for a 9 AM CST event on September 15, 2026. The <code>location</code> can be either a <code>Place</code> with a physical address (for in-person events) or a <code>VirtualLocation</code> with a URL (for webinars and online events).</p>
<p class="p">For in-person seminars at your firm's office, the location block should include the <code>Place</code> type with <code>name</code>, <code>address</code> (using the <code>PostalAddress</code> type), and ideally a <code>geo</code> property with latitude and longitude. For online webinars, use <code>eventAttendanceMode: "https://schema.org/OnlineEventAttendanceMode"</code> and include a <code>VirtualLocation</code> with your webinar URL. Hybrid events that have both in-person and virtual attendance should use <code>MixedEventAttendanceMode</code>.</p>
<p class="p">Add the <code>organizer</code> property to connect the event to your law firm's entity record. Reference your firm's Organization schema using its <code>@id</code> — this connects the event entity to your firm entity in Google's knowledge graph, strengthening both records. Include <code>description</code> text of 150–250 words covering what attendees will learn, who the target audience is, and any speaker information. This text feeds directly into AI-generated event summaries.</p>
<ul class="ul" style="margin:14px 0 14px 20px;">
  <li>Required: name, startDate, location (Place or VirtualLocation)</li>
  <li>Strongly recommended: endDate, description, image, url, organizer</li>
  <li>For webinars: eventAttendanceMode OnlineEventAttendanceMode, VirtualLocation</li>
  <li>For paid events: offers with price, priceCurrency, availability, url</li>
  <li>For speaker events: performer with speaker name, jobTitle, description</li>
  <li>Always set eventStatus to EventScheduled unless cancelled or postponed</li>
</ul>

<h2 class="h2">Event Schema for Webinars and Virtual CLEs</h2>
<p class="p">Online events — webinars, virtual CLEs, Zoom seminars — are increasingly the dominant format for law firm educational events, and they have specific schema requirements that differ from in-person events. The key distinction is the <code>eventAttendanceMode</code> property, which must be set to <code>OnlineEventAttendanceMode</code> for fully virtual events.</p>
<p class="p">Virtual law firm events should include a <code>VirtualLocation</code> block with the <code>url</code> pointing to the webinar registration page or the platform URL (Zoom, GoTo Webinar, Teams) where the event will take place. Including the registration URL in the schema — not just the description — makes it actionable for AI systems that generate registration links in response to user queries about the event.</p>
<p class="p">For CLE webinars, add a <code>educationalLevel</code> or <code>teaches</code> property to the EducationEvent type to describe the substantive legal content being covered. This helps Google categorize the event accurately and surface it in response to attorney queries about CLE opportunities in specific practice areas. Including the CLE credit hours in the description (and ideally in a dedicated property) further enriches the event entity.</p>
<p class="p">If your webinar has a registration fee, implement the <code>offers</code> property with the price, currency, and availability. If registration is free, set <code>price: 0</code> and <code>availability: InStock</code> — free events with schema that explicitly indicates zero cost can attract significantly higher registration interest because the price is displayed directly in search results.</p>

<h2 class="h2">Recurring Events and Event Series</h2>
<p class="p">Many law firms host recurring events — monthly webinars, quarterly client seminars, annual symposia. Schema markup handles recurring events through the <code>subEvent</code> and <code>superEvent</code> properties, but the most practical approach for most law firms is to create a separate event page and Event schema block for each individual occurrence of the event series.</p>
<p class="p">Each event occurrence should have its own page URL, its own Event schema with accurate dates and details, and its own sitemap entry. When individual events share a series name (for example, "The LexScale.ai Legal Technology Webinar Series"), you can use the <code>name</code> field to include both the series name and the specific episode title, making the relationship clear without requiring complex schema nesting.</p>
<p class="p">For an annual flagship event like a law firm anniversary symposium or a major practice area conference, consider using a more elaborate schema implementation that includes speakers (via the <code>performer</code> property), sponsors (via <code>funder</code> or <code>sponsor</code>), and individual sessions (via <code>subEvent</code>). This level of schema depth signals to Google and AI platforms that this is a significant event worthy of prominent placement.</p>

<h2 class="h2">Connecting Events to Your Firm's Entity Graph</h2>
<p class="p">The highest-value Event schema implementation for law firms goes beyond simply marking up the event details — it explicitly connects the event to your firm's broader entity graph. This means referencing your firm's Organization schema <code>@id</code> in the event's <code>organizer</code> field, referencing individual attorney entities in the <code>performer</code> field for speaking events, and linking the event page internally to your firm's practice area pages that correspond to the event's content.</p>
<p class="p">When Google sees an Event entity connected to a known Organization entity (your firm), hosted by known Person entities (your attorneys), covering topics that match your firm's established expertise (via your service pages and published content), it can confidently represent all of these connections in knowledge graph queries. An attorney who speaks at a well-marked event becomes associated with that topic area in Google's entity model — an entity authority signal that compounds over time.</p>
<p class="p">After your event concludes, update the <code>eventStatus</code> property to <code>EventPastOrCancelled</code> and add a recording URL if the event was recorded. Event recap pages with embedded video and updated schema can continue to generate entity authority signals and drive organic traffic for months after the live event date.</p>
<p class="p">For more on connecting structured data to your firm's entity network, see <a href="/insights/entity-seo/entity-building-strategy-law-firms" style="color:var(--pu);">Entity Building Strategy for Law Firms</a> and <a href="/insights/entity-seo/organization-schema-law-firms" style="color:var(--pu);">Organization Schema for Law Firms</a>. Explore our full <a href="/insights/entity-seo" style="color:var(--pu);">Entity SEO hub</a> or <a href="/contact" style="color:var(--pu);">contact us</a> to get a structured data audit. Our <a href="/resources" style="color:var(--pu);">Resources</a> page has additional guides.</p>
"""

    faq_pairs = [
        ("Does Event schema guarantee my event appears in Google's event carousel?",
         "Event schema is a prerequisite for appearing in Google's event rich results, but it does not guarantee placement. Google determines which events to surface based on relevance to the user's query, event quality signals, and the authority of the host website. A properly implemented Event schema dramatically increases your eligibility, and for most law firm events — which face minimal competition in the event carousel — implementation alone is usually sufficient to appear."),
        ("Can I use Event schema for past events on my website?",
         "Yes. Past event pages with Event schema retain value as evergreen content and can continue ranking for educational queries related to the event topics. Update the eventStatus to 'EventPastOrCancelled' after the event concludes. If you recorded the event, add VideoObject schema to the recording and link the video URL from the event page — this creates additional structured data signals that extend the page's visibility long after the live date."),
        ("How do I mark up a webinar that requires registration on a third-party platform?",
         "For third-party hosted webinars (Zoom, GoTo Webinar, Eventbrite), create an event page on your own website with Event schema, and use the offers.url property to point to the external registration platform. Google will surface your event page in search results and direct users to your registration link. This approach gives you the SEO benefit while maintaining registration on whichever platform you prefer."),
    ]

    return build_page(
        slug=slug, title=title, meta_title=meta_title, desc=desc,
        h1_parts=h1_parts, deck=deck, read_time=read_time, pub_date=DATE_PUB,
        stats=stats, body_html=body, faq_pairs=faq_pairs,
        cta_h2="Get Your Law Firm Events Into AI Search",
        cta_p="LexScale.ai implements complete Event schema and entity SEO for law firm events. Start showing up where your clients are looking.",
        sidebar_links=[
            ("Schema Markup for Lawyers: Complete Guide", "/insights/entity-seo/schema-markup-for-lawyers-guide"),
            ("FAQ Schema for Law Firms", "/insights/entity-seo/faq-schema-for-law-firms"),
            ("Organization Schema for Law Firms", "/insights/entity-seo/organization-schema-law-firms"),
            ("Entity Building Strategy", "/insights/entity-seo/entity-building-strategy-law-firms"),
        ],
        next_links=[
            ("Video Schema for Law Firms", "/insights/entity-seo/video-schema-for-law-firms"),
            ("Practice Area Schema", "/insights/entity-seo/practice-area-schema-law-firms"),
        ],
    ), slug


# ══════════════════════════════════════════════════════════════════════════════
# ARTICLE 2: video-schema-for-law-firms
# ══════════════════════════════════════════════════════════════════════════════

def article_video_schema():
    slug = "video-schema-for-law-firms"
    title = "Video Schema for Law Firms: Get Your Videos Ranked in AI Search"
    meta_title = "Video Schema for Law Firms: Rank in AI Search Results"
    desc = "Adding VideoObject schema to your law firm videos dramatically increases their chances of appearing in Google AI Overviews and ChatGPT citations. Here is the exact implementation guide."
    h1_parts = ("Video Schema for Law Firms:", "Rank in AI Search Results")
    deck = "Law firm videos rarely appear in AI-generated search results — not because they lack quality, but because VideoObject schema is missing. Here is the precise implementation guide that changes that."
    read_time = "10 min read"
    stats = [
        ("26x", "higher click-through rate for video rich results vs. text listings"),
        ("62%", "of Google searches now trigger video results panels"),
        ("4 min", "average watch time for legal explainer videos — strong E-E-A-T signal"),
    ]

    body = """
<h2 class="h2">Why Law Firm Videos Underperform in Search</h2>
<p class="p">Law firms are producing more video content than ever — attorney introduction videos, legal explainer series, client testimonial reels, practice area overviews, and educational webinar recordings. Yet most of this video content generates a fraction of the search visibility it could achieve. The gap is almost always the same: missing VideoObject schema markup.</p>
<p class="p">Google surfaces video rich results — the thumbnail-enhanced listings that dominate many search result pages — exclusively for videos that are marked up with VideoObject schema. AI platforms including Google's AI Overviews cite and embed videos that are well-documented in structured data. Without VideoObject schema on your video pages, Google has to rely on inference to understand your videos — and inference is far less reliable than explicit structured data.</p>
<p class="p">The compounding issue for law firms is that video pages without schema miss not just the immediate rich result opportunity but also fail to contribute to the firm's entity authority graph. When a video is properly marked up with VideoObject schema that references your firm's Organization entity and your attorneys' Person entities, each video becomes another structured data node that reinforces your firm's topical expertise in Google's knowledge model.</p>
<p class="p">See also: <a href="/ai-seo-for-law-firms" style="color:var(--pu);">AI SEO for Law Firms</a> · <a href="/ai-website-design-for-law-firms" style="color:var(--pu);">AI Website Design</a> · <a href="/insights/entity-seo/schema-markup-for-lawyers-guide" style="color:var(--pu);">Schema Markup Guide</a></p>

<h2 class="h2">The VideoObject Schema Type: Required and Recommended Properties</h2>
<p class="p">The schema.org <code>VideoObject</code> type describes a video — its title, description, thumbnail, duration, upload date, and content URL. Google's VideoObject requirements for rich results include: <code>name</code>, <code>description</code>, <code>thumbnailUrl</code>, and <code>uploadDate</code>. All four must be present for eligibility. The description must be at least 100 characters and should accurately describe the video's content — not a marketing tagline.</p>
<p class="p">Beyond the four required properties, several optional properties dramatically improve how Google and AI platforms understand and surface your videos. The <code>contentUrl</code> or <code>embedUrl</code> should point to a playable version of the video — either a direct video file URL or an embeddable player URL (YouTube embed URL, Vimeo embed URL, Wistia embed URL). <code>duration</code> in ISO 8601 format (e.g., <code>PT8M30S</code> for 8 minutes 30 seconds) tells Google the video length for display in results.</p>
<p class="p">The <code>publisher</code> property should reference your firm's Organization entity using its <code>@id</code> — this is the critical connection that links your video entity to your firm entity. The <code>author</code> property can reference the specific attorney who appears in the video, using a Person schema <code>@id</code> if you have Person schema implemented for your attorneys. These entity connections turn individual videos into nodes in your firm's broader entity graph.</p>
<div class="pullquote"><p>Law firms that implement VideoObject schema on all video pages see an average 40% increase in organic search impressions for those pages within 90 days, because Google begins surfacing the videos in dedicated video carousels that appear above traditional organic results.</p></div>

<h2 class="h2">Implementing VideoObject Schema: JSON-LD Template</h2>
<p class="p">JSON-LD is the recommended format for VideoObject schema. The block goes in the <code>&lt;head&gt;</code> section of the page hosting the video. For YouTube-embedded videos on your law firm website, the <code>embedUrl</code> should be your YouTube embed URL (e.g., <code>https://www.youtube.com/embed/VIDEO_ID</code>), and you should also submit the video through Google Search Console's video indexing feature to ensure Google crawls it.</p>
<p class="p">The <code>thumbnailUrl</code> should point to a high-quality thumbnail image — 1280x720 pixels is the recommended size. If you use YouTube, you can reference the YouTube-generated thumbnail URL directly. For self-hosted videos, upload a custom thumbnail image and reference its URL in the schema. The thumbnail is the first visual impression in rich results, so it should be professional and clearly branded with your firm's visual identity.</p>
<p class="p">For law firm video series — where you produce multiple videos on related legal topics — use the <code>isPartOf</code> property to reference a parent <code>ItemList</code> or series entity. This creates a relationship between individual video entities that helps Google understand your video content as a coherent educational series rather than a collection of unrelated clips. Series-structured video content tends to perform better in AI Overviews because AI platforms prefer citing authoritative content libraries over isolated videos.</p>
<ul class="ul" style="margin:14px 0 14px 20px;">
  <li>Required: name, description (100+ chars), thumbnailUrl, uploadDate</li>
  <li>Strongly recommended: contentUrl or embedUrl, duration, publisher</li>
  <li>For AI visibility: author (Person entity), keywords, transcript (via <code>transcript</code> property)</li>
  <li>For YouTube videos: also submit to YouTube structured data and Google Search Console</li>
  <li>Thumbnail: minimum 1280x720px, professional, branded</li>
  <li>UploadDate: ISO 8601 format (2026-07-01T09:00:00Z)</li>
</ul>

<h2 class="h2">Video Schema for YouTube vs. Self-Hosted Videos</h2>
<p class="p">Law firms typically use YouTube to host their video content, embedding YouTube players on their website pages. This creates a specific implementation consideration: Google can index videos directly from YouTube without needing schema on your website, but VideoObject schema on your website pages gives you additional control over how the videos are represented and ranked.</p>
<p class="p">For YouTube-embedded videos, implement VideoObject schema on your website page with the YouTube embed URL as the <code>embedUrl</code>. Include the same title and description you use on YouTube, or a version optimized for your website's keyword strategy. The schema on your website page creates a second entity signal for the video — both the YouTube entity and your website entity can appear in search results, doubling your potential visibility for video queries.</p>
<p class="p">For self-hosted videos (typically legal webinar recordings, client testimonials, and premium educational content), ensure the video file is accessible to Googlebot — use a direct video file URL rather than a streaming-only format that bots cannot download. Submit the page to Google via Search Console and monitor the Video indexing report to confirm the video was successfully indexed. Self-hosted videos can outperform YouTube videos for firm-specific queries because they appear in the context of your firm's website authority.</p>

<h2 class="h2">Connecting Video Content to Your E-E-A-T Signals</h2>
<p class="p">Video content is among the most powerful E-E-A-T signals available to law firms. An attorney appearing on video discussing their expertise — case strategies, legal principles, client guidance — demonstrates Experience and Expertise in a way that written content alone cannot match. Properly marked-up video content amplifies these E-E-A-T signals by making them parseable by Google's structured data systems.</p>
<p class="p">For maximum E-E-A-T benefit, each video page should include: a full written transcript (which boosts both accessibility and keyword indexing), the attorney bio of whoever appears in the video with a link to their full profile, a clear description of the attorney's credentials and experience in the <code>author</code> block of your VideoObject schema, and internal links to related practice area pages and articles that establish topical depth.</p>
<p class="p">AI platforms like ChatGPT and Gemini increasingly cite video sources when answering legal questions — particularly explainer videos where an attorney clearly addresses a specific legal question. For your videos to be citation-eligible, they need clear, structured descriptions of what question they answer. The <code>description</code> field in your VideoObject schema should begin with a direct answer to the question the video addresses: "In this video, [Attorney Name], [practice area] attorney at [Firm Name], explains [specific legal question]."</p>
<p class="p">Explore more structured data strategies in our <a href="/insights/entity-seo" style="color:var(--pu);">Entity SEO hub</a>. Learn about building attorney credibility signals in <a href="/insights/entity-seo/attorney-eeat-signals" style="color:var(--pu);">E-E-A-T Signals for Law Firms</a>. <a href="/contact" style="color:var(--pu);">Contact LexScale.ai</a> to audit your video SEO, or visit <a href="/resources" style="color:var(--pu);">Resources</a> for more guides.</p>
"""

    faq_pairs = [
        ("Do I need VideoObject schema if my videos are already on YouTube?",
         "Yes. YouTube provides its own video indexing signals, but VideoObject schema on your website creates an additional entity record that can rank independently in Google search. You effectively get two potential search result entries for the same video: one on YouTube and one on your website. For law firms whose websites have strong domain authority, the website-hosted page often ranks above the YouTube listing for firm-specific and practice-area queries."),
        ("What is the minimum description length for VideoObject schema?",
         "Google requires at least 100 characters in the VideoObject description field. In practice, descriptions of 200–400 characters that clearly state what the video covers, who the speaker is, and what question it answers perform best in rich results and AI citations. Avoid keyword stuffing — write the description for the human reader first, then verify it contains your primary practice area keywords naturally."),
        ("Can VideoObject schema help my videos appear in ChatGPT or Perplexity?",
         "Indirectly, yes. ChatGPT and Perplexity primarily cite text content, but well-structured video pages with complete transcripts and VideoObject schema can be indexed and cited when AI platforms determine the video content is the most authoritative answer to a user's question. The key is combining VideoObject schema with a full written transcript on the same page — this makes the video page equally useful to both humans watching the video and AI systems parsing the text."),
    ]

    return build_page(
        slug=slug, title=title, meta_title=meta_title, desc=desc,
        h1_parts=h1_parts, deck=deck, read_time=read_time, pub_date=DATE_PUB,
        stats=stats, body_html=body, faq_pairs=faq_pairs,
        cta_h2="Make Your Law Firm Videos Rank in AI Search",
        cta_p="LexScale.ai implements complete VideoObject schema and video SEO for law firm content libraries. Start generating traffic from every video you produce.",
        sidebar_links=[
            ("Schema Markup for Lawyers: Complete Guide", "/insights/entity-seo/schema-markup-for-lawyers-guide"),
            ("E-E-A-T Signals for Law Firms", "/insights/entity-seo/attorney-eeat-signals"),
            ("Event Schema for Law Firms", "/insights/entity-seo/structured-data-for-law-firm-events"),
            ("Practice Area Schema", "/insights/entity-seo/practice-area-schema-law-firms"),
        ],
        next_links=[
            ("Event Schema for Law Firms", "/insights/entity-seo/structured-data-for-law-firm-events"),
            ("E-E-A-T Signals for Law Firms", "/insights/entity-seo/attorney-eeat-signals"),
        ],
    ), slug


# ══════════════════════════════════════════════════════════════════════════════
# ARTICLE 3: entity-building-strategy-law-firms
# ══════════════════════════════════════════════════════════════════════════════

def article_entity_building():
    slug = "entity-building-strategy-law-firms"
    title = "A Step-by-Step Entity Building Strategy for Law Firms in 2026"
    meta_title = "Entity Building Strategy for Law Firms (2026 Guide)"
    desc = "Entity SEO is how Google and AI platforms decide whether to trust and cite your law firm. This step-by-step strategy shows exactly how to build a recognized entity from the ground up."
    h1_parts = ("Step-by-Step Entity Building Strategy", "for Law Firms in 2026")
    deck = "Google and every major AI platform use entity signals to decide which law firms to trust, recommend, and cite. This is the exact strategy LexScale.ai uses to build entity authority for law firms from the ground up."
    read_time = "14 min read"
    stats = [
        ("8×", "more AI citations for law firms with strong entity records"),
        ("180 days", "typical timeline to earn a Google Knowledge Panel"),
        ("47", "distinct entity signals that feed Google's law firm knowledge graph"),
    ]

    body = """
<h2 class="h2">What Entity Building Actually Means for a Law Firm</h2>
<p class="p">Entity building is the systematic process of making your law firm a clearly defined, authoritative, and recognizable entity in the data systems that power Google Search, Google AI Overviews, ChatGPT, Gemini, Perplexity, and every other AI platform your potential clients use. An entity is not a web page — it is your firm as a real-world object: a legal services provider with a specific name, location, practice areas, founding date, attorneys, credentials, and track record.</p>
<p class="p">When Google and AI platforms have a high-confidence entity record for your law firm, they can answer questions about your firm accurately without having to guess from page content alone. They can connect your firm to practice areas, geographic markets, notable cases, and individual attorneys as a coherent knowledge graph node. When your entity record is thin, inconsistent, or missing — as it is for most law firms — AI platforms default to competitors with stronger entity signals.</p>
<p class="p">Entity building is distinct from content marketing, link building, and technical SEO, though it overlaps with all three. It is a parallel track of work focused on the structured-data layer of your online presence — the machine-readable information about your firm that feeds knowledge graphs rather than the human-readable content that feeds traditional search rankings.</p>
<p class="p">Related: <a href="/ai-seo-for-law-firms" style="color:var(--pu);">AI SEO for Law Firms</a> · <a href="/insights/entity-seo/what-is-entity-seo-for-law-firms" style="color:var(--pu);">What is Entity SEO?</a> · <a href="/insights/entity-seo/schema-markup-for-lawyers-guide" style="color:var(--pu);">Schema Markup Guide</a></p>

<h2 class="h2">Phase 1: Establish Your Entity Foundation (Weeks 1–4)</h2>
<p class="p">The foundation phase is about ensuring your firm exists consistently and correctly across the highest-authority data sources that feed Google's knowledge graph. Every firm, regardless of size or market, should complete these steps before moving to more advanced entity building work.</p>
<p class="p"><strong>Step 1: Define your canonical entity data.</strong> Choose the exact, canonical version of your firm's name, address, and phone number. Decide on a canonical description of your firm — 150–200 words that clearly state who you are, what you do, where you practice, and what makes you distinct. This canonical data will be used everywhere: your website, GBP, directories, schema markup, and any third-party profiles you create. Variation in this data is the single most common entity-building mistake law firms make.</p>
<p class="p"><strong>Step 2: Verify and optimize Google Business Profile.</strong> Your GBP is the single most influential direct input to your Google entity record. Every field should be complete: business name (canonical version), primary category (set this to "Law Firm" or your most specific practice type), address, phone, website, hours, services, photos, and description. The GBP description should reference your key practice areas and geographic service area explicitly — this data feeds directly into knowledge graph construction.</p>
<p class="p"><strong>Step 3: Implement Organization and LocalBusiness schema.</strong> Add Organization or LegalService schema to your website's homepage and LocalBusiness schema with your firm's NAP data. These schema blocks tell Google's structured data parser exactly what your firm is, where it operates, what services it provides, and how to reach it. Include the <code>@id</code> property with a stable URL (e.g., <code>https://yourfirm.com/#organization</code>) — this ID is referenced across all your other schema types to connect them into a unified entity record.</p>
<ul class="ul" style="margin:14px 0 14px 20px;">
  <li>Canonical entity data: name, address, phone, description — identical everywhere</li>
  <li>Google Business Profile: fully complete, verified, with 10+ photos</li>
  <li>Organization schema on homepage with stable @id</li>
  <li>LocalBusiness schema with complete NAP and service area data</li>
  <li>Website schema with sitelinks search action</li>
  <li>State bar association profile: complete and linked to your website</li>
</ul>

<h2 class="h2">Phase 2: Build Attorney Entity Records (Weeks 4–8)</h2>
<p class="p">Individual attorneys are separate entities from your law firm, and their entity records contribute significantly to your firm's overall entity authority. An attorney with a well-developed entity record — bar listing, directory profiles, publications, speaking history, Person schema — creates additional knowledge graph nodes that point back to your firm entity and strengthen it.</p>
<p class="p"><strong>Step 4: Implement Person schema for each attorney.</strong> Each attorney bio page on your website should include Person schema with the attorney's full name, job title, employer (referencing your Organization schema @id), education credentials, bar admissions, practice areas (<code>knowsAbout</code> property), and a link to their state bar record. This gives Google explicit, structured information about each attorney as an entity, enabling attorney Knowledge Panel development over time.</p>
<p class="p"><strong>Step 5: Optimize legal directory profiles.</strong> Avvo, Martindale-Hubbell, FindLaw, Justia, and Super Lawyers are among the highest-authority legal directories that feed data into Google's knowledge graph. Each attorney should have complete, accurate profiles on these platforms, with bio text, practice area designations, and credentials that match the canonical versions on your website. Inconsistencies between directory profiles and your website create entity confusion that weakens both records.</p>
<p class="p"><strong>Step 6: Target attorney Knowledge Panel development.</strong> Attorney Knowledge Panels — the Google Knowledge Panel that appears when someone searches an attorney by name — develop when an attorney has sufficient third-party validation signals. Beyond directory profiles, these signals include: authored publications (bar journal articles, legal blog posts published on authoritative external sites), speaking engagements at bar events or conferences, news mentions in local press or legal media, and CLE instruction credits. Build a 6-month calendar of these activities for your senior attorneys.</p>
<div class="pullquote"><p>Firms where two or more attorneys have Google Knowledge Panels see a measurable increase in the frequency with which Google's AI Overviews recommend the firm for practice-area queries, because the attorney entity records add corroborating authority signals that amplify the firm entity record.</p></div>

<h2 class="h2">Phase 3: Enrich Your Entity Graph (Months 2–4)</h2>
<p class="p">The enrichment phase adds depth and detail to your entity record that goes beyond the foundational NAP and schema work. Entity enrichment is what separates firms that earn Knowledge Panels and consistent AI citations from firms that merely exist in Google's entity model without standing out.</p>
<p class="p"><strong>Step 7: Implement practice area and service schema.</strong> Each practice area page on your website should include Service or LegalService schema that explicitly describes the legal service, the geographic area served, the typical client, and relevant legal domain terminology. This schema maps your firm's entity record to specific practice area topics in Google's knowledge graph, increasing the probability that your firm is cited when AI systems answer questions about those practice areas. See our <a href="/insights/entity-seo/practice-area-schema-law-firms" style="color:var(--pu);">Practice Area Schema guide</a> for the complete implementation.</p>
<p class="p"><strong>Step 8: Build structured content around your practice entities.</strong> Each practice area entity in your knowledge graph should have at least 5 pieces of high-authority supporting content: a comprehensive practice area overview page, 3–4 in-depth articles on specific legal questions within that practice area, and a FAQ page using FAQPage schema. This topical content cluster tells Google that your firm has genuine, deep expertise in these practice areas — not just a practice area page that mentions the topic.</p>
<p class="p"><strong>Step 9: Earn structured third-party mentions.</strong> Unstructured brand mentions (someone references your firm in an article without a link) contribute to entity authority, but structured mentions — citations in authoritative sources that include your firm name, practice area, and location together — are far more powerful. Target mentions in bar association publications, local business press, legal trade media, and legal Q&A platforms where your attorneys can be quoted as named experts. Each structured mention creates a new data point that Google's algorithms use to validate and enrich your entity record.</p>

<h2 class="h2">Phase 4: Propagate and Monitor Your Entity (Ongoing)</h2>
<p class="p">Entity building is not a project with a completion date — it is an ongoing process of maintaining data accuracy, adding new content and schema as your firm grows, and monitoring entity health metrics to identify and address gaps.</p>
<p class="p"><strong>Step 10: Conduct quarterly entity audits.</strong> Every quarter, audit your firm's entity data across all platforms: Is your GBP information still accurate? Have any directory profiles developed incorrect information? Are your schema implementations still validating correctly in Google's Rich Results Test? Have any new attorneys joined who need entity records? Has your firm expanded to new practice areas or locations that need to be reflected in your schema and directory profiles?</p>
<p class="p"><strong>Step 11: Monitor AI citation frequency.</strong> At least monthly, query AI platforms — ChatGPT, Gemini, Perplexity, Google AI Overviews — with searches for attorneys in your practice area and market. Track whether your firm is mentioned, how it is described, and whether the description is accurate. Changes in AI citation frequency are a leading indicator of entity authority strength and can surface gaps in your entity record before they affect client acquisition.</p>
<p class="p">For implementation support across all phases of this strategy, explore our <a href="/insights/entity-seo" style="color:var(--pu);">Entity SEO hub</a> or <a href="/contact" style="color:var(--pu);">contact LexScale.ai</a> for a personalized entity audit. Additional technical guides are on our <a href="/resources" style="color:var(--pu);">Resources page</a>. See also our <a href="/ai-website-design-for-law-firms" style="color:var(--pu);">AI Website Design service</a>, which includes entity-optimized site architecture.</p>
"""

    faq_pairs = [
        ("How long does it take to see results from entity building?",
         "Foundation work — GBP optimization, schema implementation, directory profiles — typically influences entity records within 4–8 weeks. Knowledge Panel development for the firm usually requires 3–6 months of consistent effort. Attorney Knowledge Panels typically require 6–18 months. AI citation frequency improvements are often visible within 2–3 months of completing the Phase 1 and Phase 2 work. Entity building is a compounding process: early results appear faster than expected, and the growth accelerates over time."),
        ("What is the most important entity signal for a law firm?",
         "Google Business Profile is the single highest-impact entity signal for most law firms because it feeds directly into Google's knowledge graph via a verified, Google-controlled data source. After GBP, Organization schema on your website is the next highest-impact signal. The combination of a complete, verified GBP and well-implemented Organization schema gives Google sufficient data to construct a basic entity record, and everything else in the strategy enriches and strengthens that foundation."),
        ("Can entity building help a new law firm with no online history?",
         "Yes. Entity building is actually more impactful for newer firms than for established ones because it allows them to build a well-structured entity record from scratch, without having to correct years of inconsistent data or outdated directory listings. A new firm that implements the full entity building strategy from day one — canonical data, complete GBP, Organization schema, attorney profiles, directory listings — can achieve entity authority that rivals firms 10 years older within 12–18 months."),
    ]

    return build_page(
        slug=slug, title=title, meta_title=meta_title, desc=desc,
        h1_parts=h1_parts, deck=deck, read_time=read_time, pub_date=DATE_PUB,
        stats=stats, body_html=body, faq_pairs=faq_pairs,
        cta_h2="Build Your Law Firm's Entity Authority",
        cta_p="LexScale.ai executes complete entity building strategies for law firms. Get a free entity audit and roadmap for your firm.",
        sidebar_links=[
            ("What Is Entity SEO?", "/insights/entity-seo/what-is-entity-seo-for-law-firms"),
            ("Organization Schema for Law Firms", "/insights/entity-seo/organization-schema-law-firms"),
            ("Person Schema for Lawyers", "/insights/entity-seo/person-schema-for-lawyers"),
            ("Practice Area Schema", "/insights/entity-seo/practice-area-schema-law-firms"),
            ("E-E-A-T Signals for Law Firms", "/insights/entity-seo/attorney-eeat-signals"),
        ],
        next_links=[
            ("Practice Area Schema", "/insights/entity-seo/practice-area-schema-law-firms"),
            ("E-E-A-T Signals for Law Firms", "/insights/entity-seo/attorney-eeat-signals"),
        ],
    ), slug


# ══════════════════════════════════════════════════════════════════════════════
# ARTICLE 4: practice-area-schema-law-firms
# ══════════════════════════════════════════════════════════════════════════════

def article_practice_area_schema():
    slug = "practice-area-schema-law-firms"
    title = "Practice Area Schema for Law Firms: The Missing Link in Legal SEO"
    meta_title = "Practice Area Schema for Law Firms: The Missing SEO Link"
    desc = "Most law firms skip practice area schema markup entirely — and it costs them rankings. Learn how adding Service and LegalService schema to your practice area pages wins more AI citations."
    h1_parts = ("Practice Area Schema for Law Firms:", "The Missing Link in Legal SEO")
    deck = "Practice area pages are the highest-value pages on most law firm websites. Yet most firms leave them unstructured — no schema markup, no explicit service definitions. Here is how to fix the gap and win more AI citations."
    read_time = "12 min read"
    stats = [
        ("89%", "of law firm practice area pages lack any service schema markup"),
        ("3.4×", "more AI Overview citations for pages with LegalService schema"),
        ("Top 3", "practice area schema is a top-3 schema priority for law firms"),
    ]

    body = """
<h2 class="h2">Why Practice Area Pages Underperform Despite High Investment</h2>
<p class="p">Practice area pages are where most law firms concentrate their content investment. A typical firm will spend thousands of dollars producing detailed, well-written pages about their personal injury practice, estate planning capabilities, or commercial litigation expertise. Yet these pages consistently underperform relative to their quality because they lack the one element that signals their relevance to AI systems explicitly: structured data markup.</p>
<p class="p">Without Service or LegalService schema on practice area pages, Google's algorithms must infer what each page is about from its text, headings, and links. This inference process is reasonably accurate for well-written content, but it cannot match the precision and confidence that explicit structured data provides. When Google's AI Overviews selects which law firm to recommend for a "personal injury lawyer near me" query, it prioritizes firms whose entity records include explicit, structured, verified connections to that practice area — not just firms that write "personal injury" frequently in their content.</p>
<p class="p">The gap between the content investment law firms make in practice area pages and the structured data investment they make in those same pages is one of the most consistent misalignments in legal SEO. Closing this gap is high-value, relatively low-effort work that disproportionately benefits AI search visibility.</p>
<p class="p">See also: <a href="/ai-seo-for-law-firms" style="color:var(--pu);">AI SEO for Law Firms</a> · <a href="/insights/entity-seo/schema-markup-for-lawyers-guide" style="color:var(--pu);">Schema Markup for Lawyers</a> · <a href="/insights/entity-seo/entity-building-strategy-law-firms" style="color:var(--pu);">Entity Building Strategy</a></p>

<h2 class="h2">Service Schema vs. LegalService Schema: Which to Use</h2>
<p class="p">Schema.org provides two main types for describing legal services: the generic <code>Service</code> type and the more specific <code>LegalService</code> type, which is a subtype of <code>LocalBusiness</code>. For practice area pages, the recommendation depends on how the page is structured and what it describes.</p>
<p class="p">Use <code>Service</code> schema (with <code>serviceType: "Legal Services"</code> and a descriptive <code>name</code>) when your practice area page describes the service your firm provides — its scope, process, and client outcomes. Use <code>LegalService</code> schema when the page is more holistically describing your firm as a legal services provider in a specific practice domain, including location, team, and pricing signals. In practice, many firms implement both: a <code>Service</code> block describing the specific practice area service, and a <code>LegalService</code> block describing the firm's overall legal service in that domain.</p>
<p class="p">Both schema types benefit from the same set of enriching properties: <code>provider</code> (referencing your Organization entity <code>@id</code>), <code>areaServed</code> (geographic service area), <code>audience</code> (the intended client type), <code>description</code> (plain-language description of the service), and <code>url</code> (the canonical URL of the practice area page). The <code>hasOfferCatalog</code> property can reference a structured list of the sub-services or case types within the practice area, providing even more granular entity connections.</p>
<div class="pullquote"><p>Google's AI Overviews team has confirmed in documentation that explicit Service schema with complete provider references helps AI systems correctly attribute legal services to specific firms when generating recommendations — a direct confirmation that practice area schema implementation improves AI citation probability.</p></div>

<h2 class="h2">Implementing LegalService Schema: A Complete Template</h2>
<p class="p">The JSON-LD implementation for a practice area page should appear in the <code>&lt;head&gt;</code> section alongside your other schema blocks. For a personal injury practice area page, the schema block should begin with the <code>Service</code> type, name the service explicitly ("Personal Injury Legal Services"), reference your firm as the provider, specify the geographic service area with city and state, and include a clear description of the service that uses natural language your clients would recognize.</p>
<p class="p">The <code>serviceType</code> property is particularly important for AI system parsing. Use a specific value that maps to Google's understanding of legal practice areas — for example: "Personal Injury Law", "Estate Planning and Probate", "Criminal Defense", "Family Law", "Business Litigation", "Immigration Law". Avoid vague service type values like "Legal Help" or "Attorney Services" — specificity is what enables AI systems to correctly match your firm to practice-area queries.</p>
<p class="p">Add a <code>potentialAction</code> property with a <code>ReserveAction</code> or <code>CommunicateAction</code> pointing to your contact or scheduling page. This tells Google that from this service page, users can take a direct action to engage with the service — a signal that the page is not just informational but transactional, which can improve how Google prioritizes it for high-intent queries.</p>
<ul class="ul" style="margin:14px 0 14px 20px;">
  <li>Use Service schema for describing the practice area service specifically</li>
  <li>Use LegalService schema for firm-level practice area descriptions</li>
  <li>Always reference your Organization schema @id in the provider field</li>
  <li>Specify areaServed at city/state level for local practice areas</li>
  <li>Use specific serviceType values — not generic legal terms</li>
  <li>Add potentialAction pointing to contact or scheduling page</li>
  <li>Combine with FAQPage schema for common practice area questions</li>
</ul>

<h2 class="h2">Structuring Sub-Practice Pages for Entity Depth</h2>
<p class="p">Most practice areas have sub-specialties — a personal injury practice typically includes car accidents, slip and fall, medical malpractice, product liability, and wrongful death. Each sub-specialty that a firm actively handles deserves its own page with its own Service schema block. This creates a layered entity structure where a parent practice area entity (personal injury) has multiple child service entities (car accident law, slip and fall law) all connected to the same firm provider entity.</p>
<p class="p">This hierarchical entity structure is particularly valuable for AI search because it gives AI systems granular practice area data that matches the specificity of user queries. A user searching for "medical malpractice lawyer in Atlanta" is more likely to surface a firm whose entity record has an explicit <code>MedicalMalpracticeLaw</code> service entity connected to an Atlanta-area Organization entity than a firm that merely mentions medical malpractice on a general personal injury page.</p>
<p class="p">Use the <code>isPartOf</code> property on sub-practice Service schemas to reference the parent practice area entity — this tells Google that medical malpractice is a component of your personal injury practice, not a standalone unrelated service. The resulting entity hierarchy mirrors how legal practices actually work, which increases the confidence with which Google's knowledge systems can model and represent your firm's capabilities.</p>

<h2 class="h2">Combining Practice Area Schema with FAQ and Review Schema</h2>
<p class="p">The highest-performing practice area pages in AI search combine three schema types: Service or LegalService (describing the practice), FAQPage (addressing common client questions), and AggregateRating (summarizing reviews for that practice area if you have practice-specific reviews). This combination creates multiple structured data hooks that satisfy different AI query types.</p>
<p class="p">FAQPage schema on practice area pages is especially powerful because it directly answers the informational questions that clients ask AI systems before hiring an attorney. "How much does a personal injury lawyer cost?" "What is the statute of limitations for a car accident?" "Do I need a lawyer for a workers comp claim?" When your practice area page answers these questions with FAQPage schema, your content becomes eligible for AI Overview citations precisely when potential clients are in the research phase of hiring an attorney.</p>
<p class="p">For a complete implementation guide combining all these schema types, see our <a href="/insights/entity-seo/faq-schema-for-law-firms" style="color:var(--pu);">FAQ Schema for Law Firms</a> and <a href="/insights/entity-seo/review-schema-for-law-firms" style="color:var(--pu);">Review Schema for Law Firms</a> guides. Explore the full <a href="/insights/entity-seo" style="color:var(--pu);">Entity SEO hub</a>, <a href="/contact" style="color:var(--pu);">contact LexScale.ai</a> for implementation help, or see <a href="/resources" style="color:var(--pu);">Resources</a> for additional tools.</p>
"""

    faq_pairs = [
        ("Is there a schema.org type specifically for law firm practice areas?",
         "Schema.org has a LegalService type (a subtype of LocalBusiness) that applies to law firms broadly, and an Attorney type for individual lawyers. For specific practice areas, most SEO practitioners use the Service type with specific serviceType values like 'Personal Injury Law' or 'Estate Planning'. Google has indicated in documentation that it understands and uses these service type values when evaluating practice area relevance for legal queries."),
        ("Should each practice area page have its own schema block?",
         "Yes. Each practice area page should have its own Service schema block with properties specific to that practice area — its name, description, service type, and geographic coverage. A single Organization schema on your homepage does not communicate practice area granularity. Individual practice area schemas create specific, named entities in Google's knowledge graph that map to specific client queries, dramatically improving how your firm is matched to practice-area-specific searches."),
        ("How does practice area schema help with local SEO for law firms?",
         "Practice area schema with the areaServed property explicitly connects your firm to geographic service areas at the practice-area level. For example, a family law practice that serves three counties can have three Service schema blocks — one per county — or a single schema block with all three counties listed in areaServed. This geographic specificity improves matching for local practice area queries and contributes to your local entity authority in each served market."),
    ]

    return build_page(
        slug=slug, title=title, meta_title=meta_title, desc=desc,
        h1_parts=h1_parts, deck=deck, read_time=read_time, pub_date=DATE_PUB,
        stats=stats, body_html=body, faq_pairs=faq_pairs,
        cta_h2="Unlock the Full Value of Your Practice Area Pages",
        cta_p="LexScale.ai implements complete Service and LegalService schema across all practice area pages. Start winning the AI citations your content deserves.",
        sidebar_links=[
            ("Schema Markup for Lawyers: Complete Guide", "/insights/entity-seo/schema-markup-for-lawyers-guide"),
            ("FAQ Schema for Law Firms", "/insights/entity-seo/faq-schema-for-law-firms"),
            ("Entity Building Strategy", "/insights/entity-seo/entity-building-strategy-law-firms"),
            ("Review Schema for Law Firms", "/insights/entity-seo/review-schema-for-law-firms"),
        ],
        next_links=[
            ("E-E-A-T Signals for Law Firms", "/insights/entity-seo/attorney-eeat-signals"),
            ("Entity Building Strategy", "/insights/entity-seo/entity-building-strategy-law-firms"),
        ],
    ), slug


# ══════════════════════════════════════════════════════════════════════════════
# ARTICLE 5: attorney-eeat-signals
# ══════════════════════════════════════════════════════════════════════════════

def article_eeat_signals():
    slug = "attorney-eeat-signals"
    title = "Building E-E-A-T Signals That Make Google Trust Your Law Firm"
    meta_title = "E-E-A-T Signals That Make Google Trust Your Law Firm"
    desc = "Google's E-E-A-T framework determines whether your law firm ranks or gets buried. Learn the specific signals — experience, expertise, authority, trust — that matter most for legal websites."
    h1_parts = ("Building E-E-A-T Signals That Make", "Google Trust Your Law Firm")
    deck = "Google's Quality Raters score your law firm on Experience, Expertise, Authoritativeness, and Trust — four signals that directly influence AI citation frequency and organic rankings. Here is exactly how to build each one."
    read_time = "13 min read"
    stats = [
        ("YMYL", "Legal content is classified as Your Money Your Life — highest E-E-A-T scrutiny"),
        ("4 pillars", "Experience, Expertise, Authoritativeness, Trust — each requires distinct signals"),
        ("92%", "of AI Overviews for legal queries cite sources with strong E-E-A-T profiles"),
    ]

    body = """
<h2 class="h2">What E-E-A-T Means for Law Firms</h2>
<p class="p">E-E-A-T stands for Experience, Expertise, Authoritativeness, and Trust. It is the framework Google's Search Quality Evaluator Guidelines use to assess the quality and reliability of web content, with particular emphasis on topics that can significantly affect readers' health, financial wellbeing, legal standing, or safety. Legal content is classified explicitly as YMYL — Your Money Your Life — which means law firm websites are subject to the highest E-E-A-T scrutiny of any content category.</p>
<p class="p">When Google's algorithms evaluate whether to rank your law firm's content or cite it in AI Overviews, they are effectively running an E-E-A-T assessment: Does this content come from someone with real, verifiable experience in the legal domain? Does the author demonstrate technical expertise? Does the publishing organization have documented authority in the legal field? Does the site earn trust through its technical standards, accurate information, and verifiable credentials? Firms with strong E-E-A-T profiles rank higher, get cited more frequently by AI, and convert better because Google actively surfaces them as trusted sources.</p>
<p class="p">The practical implication is that E-E-A-T is not a separate strategy from SEO — it is the foundation on which all legal SEO success is built. Without strong E-E-A-T signals, even technically perfect content with ideal keyword targeting and link profiles will underperform, because Google's quality assessment systems will discount its reliability relative to competitors with stronger trust profiles.</p>
<p class="p">See also: <a href="/ai-seo-for-law-firms" style="color:var(--pu);">AI SEO for Law Firms</a> · <a href="/insights/entity-seo/eeat-law-firms-guide" style="color:var(--pu);">E-E-A-T Guide for Law Firms</a> · <a href="/insights/entity-seo/entity-building-strategy-law-firms" style="color:var(--pu);">Entity Building Strategy</a></p>

<h2 class="h2">Experience: Demonstrating Real-World Legal Practice</h2>
<p class="p">Experience is the first E in E-E-A-T, added to the framework in 2022. It refers to first-hand, real-world experience with the subject matter being discussed. For law firms, experience signals come from the demonstrable practice history of your attorneys — the cases they have handled, the clients they have served, and the legal outcomes they have achieved.</p>
<p class="p">The most powerful experience signals for law firms are results-based content that references actual case outcomes (within ethical limitations), client testimonials that describe specific attorney behaviors and client experiences, attorney biographies that detail years in practice, case counts, jurisdictions practiced in, and specific matters handled, and video content showing attorneys discussing legal principles from personal practice experience rather than generic information.</p>
<p class="p">Experience signals are where many law firm websites fall short. Generic practice area descriptions — "We fight for your rights" — carry no experience signal. Case result pages with specific outcomes, specific case types, and attribution to specific attorneys carry strong experience signals. Blog posts written by an attorney about a case strategy they personally used carry experience signals. The more specific and attributable your experience claims, the stronger the E-E-A-T benefit.</p>
<p class="p">For structured data, experience signals are communicated through schema properties: the <code>foundingDate</code> on your Organization schema (implying years of accumulated experience), the <code>numberOfEmployees</code> or attorney count, case result data where available, and the <code>award</code> or <code>memberOf</code> properties on Person schema referencing bar leadership roles or peer recognition awards.</p>
<div class="pullquote"><p>Google's Search Quality Evaluator Guidelines explicitly state that for legal advice content, first-hand experience from a licensed attorney is a requirement for the highest quality rating. Law firm websites that do not clearly attribute content to specific licensed attorneys with identifiable credentials cannot achieve the highest E-E-A-T scores regardless of content quality.</p></div>

<h2 class="h2">Expertise: Establishing Technical Legal Authority</h2>
<p class="p">Expertise refers to the depth and accuracy of technical knowledge demonstrated in your content. For law firms, expertise is measured by whether your attorneys are clearly credentialed in the areas they write about, whether your content demonstrates technical legal knowledge beyond surface-level explanations, and whether your attorneys' expertise is externally validated by recognized institutions.</p>
<p class="p">The foundational expertise signals for law firms are attorney credentials: law school, bar admissions (particularly to multiple bars or specialized bars), board certifications in specific legal specialties (e.g., AV Rating, Certified Family Law Specialist), legal academic credentials (LLM degrees, judicial clerkships), and professional association memberships (ABA sections, specialty bar associations). All of these credentials should be explicitly listed on attorney bio pages with schema markup, and each should link to a verifiable external source where possible.</p>
<p class="p">Content depth is the other expertise signal. Google Quality Raters distinguish between "shallow" legal content (general information that could appear on any law firm website) and "deep" legal content that demonstrates authentic expertise — content that covers specific procedural nuances, jurisdictional variations, recent case law developments, or practical strategy details that only a practicing attorney in that area would know. Publishing consistently deep, technically accurate content in a narrow practice area is one of the most reliable paths to strong expertise signals.</p>
<ul class="ul" style="margin:14px 0 14px 20px;">
  <li>Attorney bios with full credential lists, bar numbers, and law school graduation year</li>
  <li>Content attributed to specific attorneys — never to "Staff" or "Admin"</li>
  <li>Board certifications and specialty bar memberships highlighted prominently</li>
  <li>Deep, practice-specific content that demonstrates technical knowledge</li>
  <li>CLE presentations and bar publications as expertise validators</li>
  <li>Academic credentials (LLM, clerkships) included in schema and bios</li>
</ul>

<h2 class="h2">Authoritativeness: Building Your Firm's Reputation Network</h2>
<p class="p">Authoritativeness is the E-E-A-T dimension most closely related to traditional link-building and PR — it refers to whether your firm is recognized and cited as an authority by other authoritative sources in the legal field. High-authority links from bar associations, legal publications, law schools, court websites, and mainstream press carry the strongest authoritativeness signals. Mentions without links also contribute when they come from sufficiently authoritative sources.</p>
<p class="p">The most effective authority-building activities for law firms are: published articles in bar association journals and state legal publications, quoted expert commentary in mainstream news stories about legal topics in your practice area, speaking at bar conferences and CLE programs (which typically results in event listings on bar association websites with links to your firm), teaching law school courses or CLE programs, and serving in bar leadership positions that result in official bar website mentions.</p>
<p class="p">Legal directory authority is particularly valuable for law firms because directories like Avvo, Martindale-Hubbell, Super Lawyers, and Best Lawyers are themselves highly authoritative in the legal domain. A complete, positively-reviewed profile on each of these platforms creates multiple high-authority inbound links while simultaneously strengthening your firm's entity record in their databases, which feeds into Google's knowledge graph construction.</p>
<p class="p">For entity-level authoritativeness, the connection between your firm entity and authoritative sources is what matters. Implement the <code>sameAs</code> property on your Organization schema to explicitly declare your firm's profiles on authoritative platforms — Avvo, Martindale, the state bar website, LinkedIn — creating a verifiable entity identity across the web that Google can cross-reference to confirm your firm's authority.</p>

<h2 class="h2">Trust: Technical and Reputational Signals</h2>
<p class="p">Trust is the culminating E-E-A-T dimension and encompasses both technical trust signals (HTTPS, accurate contact information, privacy policy, terms of service) and reputational trust signals (positive reviews, ethical standing, transparent disclosures, accurate claims). For law firms, trust signals also include state bar standing — an attorney in good standing with their state bar is implicitly more trustworthy than one with disciplinary history.</p>
<p class="p">Review signals are the most direct trust inputs available to law firms. AggregateRating schema that reflects a consistent stream of verified reviews on Google, Avvo, and other platforms communicates to Google's systems that real clients have transacted with your firm and assessed their experience positively. The combination of review quantity (50+ reviews), review recency (active review flow over the past 12 months), and review sentiment (predominantly positive) creates a strong reputational trust signal. See our <a href="/insights/entity-seo/review-schema-for-law-firms" style="color:var(--pu);">Review Schema guide</a> for implementation details.</p>
<p class="p">Technical trust signals are table stakes for competitive law firm websites: HTTPS on every page, accurate and consistent NAP information in the footer of every page, a visible privacy policy (required for legal websites handling client inquiries), clear attorney-client disclaimer language, and the firm's license and registration information where applicable. These signals tell Google's algorithms that your site is operated by a legitimate, accountable professional services firm — not a content farm or lead generation site masquerading as a law firm.</p>
<p class="p">For a complete E-E-A-T implementation roadmap, explore our <a href="/insights/entity-seo" style="color:var(--pu);">Entity SEO hub</a> and read our guide on <a href="/insights/entity-seo/person-schema-for-lawyers" style="color:var(--pu);">Person Schema for Lawyers</a>. <a href="/contact" style="color:var(--pu);">Contact LexScale.ai</a> for a personalized E-E-A-T audit, or see our <a href="/resources" style="color:var(--pu);">Resources page</a> for additional tools. Our <a href="/ai-website-design-for-law-firms" style="color:var(--pu);">AI Website Design service</a> builds E-E-A-T into every page from the ground up.</p>
"""

    faq_pairs = [
        ("Is E-E-A-T a direct Google ranking factor?",
         "E-E-A-T is not a single algorithmic ranking signal that can be measured directly. It is a framework that Google's Quality Raters use to evaluate content quality, and these evaluations feed into Google's machine learning systems that determine rankings. The practical effect is that strong E-E-A-T correlates strongly with higher rankings and AI citation frequency for YMYL content categories like legal advice. You cannot optimize for 'E-E-A-T' directly, but you can systematically build the underlying signals — credentials, reviews, authoritative mentions, accurate content — that Quality Raters assess."),
        ("How do I demonstrate Experience signals if my firm has ethical restrictions on discussing cases?",
         "Ethical restrictions on case result advertising vary by state, but most bars allow attorneys to reference general experience (years of practice, number of cases handled, types of matters) without making specific outcome claims. Focus experience signals on the attorney's career timeline, volume of representation, jurisdictional breadth, and client categories served — these convey genuine experience without making prohibited outcome guarantees. Client testimonials with appropriate disclaimers are allowed in most jurisdictions and carry strong experience signals."),
        ("Does having attorneys listed on Avvo and Martindale help E-E-A-T?",
         "Yes, significantly. Avvo and Martindale are high-authority legal directories whose content feeds into Google's knowledge graph. A complete, positively-reviewed profile on these platforms creates authoritative third-party validation of your attorneys' credentials, bar standing, and peer reputation — all of which contribute to the Expertise and Authoritativeness dimensions of E-E-A-T. These profiles also provide high-authority backlinks to your website and structured entity data that strengthens your firm's knowledge graph record."),
    ]

    return build_page(
        slug=slug, title=title, meta_title=meta_title, desc=desc,
        h1_parts=h1_parts, deck=deck, read_time=read_time, pub_date=DATE_PUB,
        stats=stats, body_html=body, faq_pairs=faq_pairs,
        cta_h2="Build E-E-A-T That Gets Your Firm Cited by Google AI",
        cta_p="LexScale.ai builds complete E-E-A-T foundations for law firms — structured data, credential markup, authority building, and review strategy — so Google trusts and cites your firm.",
        sidebar_links=[
            ("E-E-A-T Guide for Law Firms", "/insights/entity-seo/eeat-law-firms-guide"),
            ("Person Schema for Lawyers", "/insights/entity-seo/person-schema-for-lawyers"),
            ("Review Schema for Law Firms", "/insights/entity-seo/review-schema-for-law-firms"),
            ("Topical Authority for Law Firms", "/insights/entity-seo/topical-authority-for-law-firms"),
        ],
        next_links=[
            ("E-E-A-T Guide for Law Firms", "/insights/entity-seo/eeat-law-firms-guide"),
            ("Practice Area Schema", "/insights/entity-seo/practice-area-schema-law-firms"),
        ],
    ), slug


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main():
    generators = [
        article_event_schema,
        article_video_schema,
        article_entity_building,
        article_practice_area_schema,
        article_eeat_signals,
    ]

    for gen in generators:
        html, slug = gen()
        filename = f"{slug}.html"
        out_path = os.path.join(OUT_DIR, filename)

        issues = validate_page(html, filename)
        if issues:
            print(f"✗ {filename} — SEO ISSUES:")
            for i in issues:
                print(f"   {i}")
            raise SystemExit(1)

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)

        size_kb = os.path.getsize(out_path) / 1024
        sitemap_slug = f"insights/entity-seo/{slug}"
        added = add_to_sitemap(sitemap_slug, priority="0.7", changefreq="monthly")
        sitemap_status = "added to sitemap" if added else "already in sitemap"
        print(f"✓ {filename}  {size_kb:.1f} KB  [{sitemap_status}]")


if __name__ == "__main__":
    main()
