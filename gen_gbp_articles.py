#!/usr/bin/env python3
"""
gen_gbp_articles.py — Generate 5 new GBP insight articles for LexScale.ai.

Articles written to /home/user/muskokaspray/insights/google-business-profile/
"""

import os, sys
sys.path.insert(0, "/home/user/muskokaspray")

from seo_helpers import (
    head_block, article_schema, breadcrumb_schema, faq_schema,
    validate_page, add_to_sitemap,
    SITE, OG_IMG, YEAR,
)

OUT_DIR = "/home/user/muskokaspray/insights/google-business-profile"
HUB_URL = f"{SITE}/insights/google-business-profile"
DATE    = "2026-07-01"

# ─── Shared page chrome ───────────────────────────────────────────────────────

CSS = """\
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
.stat-row{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin:40px 0;}
.stat-box{background:linear-gradient(135deg,rgba(106,92,255,.09),rgba(139,127,255,.05));border:1px solid rgba(106,92,255,.15);border-radius:16px;padding:24px;text-align:center;}
.stat-box .s-num{font-size:42px;font-weight:900;color:var(--pu);letter-spacing:-1.5px;line-height:1;}
.stat-box .s-lbl{font-size:13px;color:#64748b;margin-top:8px;line-height:1.5;}
.content-wrap{max-width:1100px;margin:0 auto;padding:64px 40px;display:grid;grid-template-columns:1fr 300px;gap:56px;align-items:start;}
.article-body{min-width:0;}
.sidebar{position:sticky;top:96px;}
.sidebar-card{background:#fff;border:1px solid rgba(106,92,255,.12);border-radius:20px;padding:28px;margin-bottom:24px;box-shadow:0 4px 24px rgba(11,21,54,.06);}
.sidebar-card h3{font-size:15px;font-weight:800;color:var(--navy);margin-bottom:6px;}
.sidebar-card p{font-size:13px;color:#64748b;line-height:1.6;margin-bottom:18px;}
.sidebar-btn{display:block;width:100%;background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;border:none;padding:12px;border-radius:100px;font-size:13px;font-weight:700;cursor:pointer;font-family:inherit;text-align:center;}
.sidebar-stat{background:linear-gradient(135deg,rgba(106,92,255,.1),rgba(139,127,255,.06));border:1px solid rgba(106,92,255,.18);border-radius:16px;padding:24px;margin-bottom:24px;text-align:center;}
.sidebar-stat .s-num{font-size:42px;font-weight:900;color:var(--pu);letter-spacing:-1.5px;line-height:1;}
.sidebar-stat .s-label{font-size:12px;color:#64748b;margin-top:8px;line-height:1.6;}
.cta-banner{background:linear-gradient(135deg,var(--navy),#1a2456);padding:64px 40px;text-align:center;}
.cta-inner{max-width:600px;margin:0 auto;}
.cta-inner h2{font-size:clamp(24px,2.8vw,36px);font-weight:900;color:#fff;letter-spacing:-1px;margin-bottom:12px;}
.cta-inner p{font-size:15px;color:rgba(255,255,255,.55);line-height:1.7;margin-bottom:28px;}
.btn-primary{display:inline-block;background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;padding:14px 30px;border-radius:100px;font-size:15px;font-weight:700;border:none;cursor:pointer;font-family:inherit;}
@media(max-width:900px){.art-hero{padding:52px 20px 48px;}.content-wrap{grid-template-columns:1fr;padding:40px 20px;gap:32px;}.sidebar{position:static;}.cta-banner{padding:48px 20px;}.stat-row{grid-template-columns:1fr;}}
.article-body h2{font-size:clamp(20px,2.4vw,28px);font-weight:800;color:var(--navy);letter-spacing:-.6px;margin:48px 0 16px;}
.article-body h3{font-size:18px;font-weight:700;color:var(--navy);margin:32px 0 12px;}
.article-body p{font-size:15px;color:#374151;line-height:1.85;margin-bottom:18px;}
.article-body ul,.article-body ol{margin:0 0 18px 24px;}
.article-body li{font-size:15px;color:#374151;line-height:1.8;margin-bottom:6px;}
.article-body a{color:var(--pu);font-weight:600;}
.article-body a:hover{text-decoration:underline;}
.callout-box{background:#f0f4ff;border-left:4px solid var(--pu);border-radius:0 12px 12px 0;padding:20px 24px;margin:28px 0;}
.callout-box p{font-size:14px;color:#374151;line-height:1.8;margin:0;}
.callout-box strong{color:var(--navy);}
"""

NAV_HTML = """\
<nav id="mainNav">
  <a href="/index" class="logo">Lex<span>Scale</span>.ai</a>
  <button class="nav-mob" onclick="toggleMobNav(this)" aria-label="Toggle navigation">
    <span></span><span></span><span></span>
  </button>
  <ul class="nav-links">
    <li class="has-drop">
      <a href="#">Services <svg class="drop-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></a>
      <div class="dropdown">
        <a href="/ai-website-design-for-law-firms" class="drop-item"><div class="drop-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg></div><div><div class="drop-label">AI Website Design</div><div class="drop-sub">For law firms</div></div></a>
        <a href="/ai-seo-for-law-firms" class="drop-item"><div class="drop-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg></div><div><div class="drop-label">AI SEO</div><div class="drop-sub">Rank higher, get cited by AI</div></div></a>
        <a href="/ai-receptionist-for-law-firms" class="drop-item"><div class="drop-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 8.81 19.79 19.79 0 01.1 2.18 2 2 0 012.08 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.91 7.91a16 16 0 006.16 6.16l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg></div><div><div class="drop-label">AI Receptionist</div><div class="drop-sub">24/7 call answering</div></div></a>
        <a href="/ai-chatbot-for-law-firms" class="drop-item"><div class="drop-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg></div><div><div class="drop-label">AI Chatbot</div><div class="drop-sub">Convert more website visitors</div></div></a>
      </div>
    </li>
    <li class="has-drop">
      <a href="/insights">Insights <svg class="drop-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></a>
      <div class="dropdown" style="left:0;transform:none;min-width:280px;">
        <a href="/insights/google-business-profile" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></div><div><div class="drop-label">Google Business Profile</div><div class="drop-sub">13 articles</div></div></a>
        <a href="/insights/ai-seo" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg></div><div><div class="drop-label">AI SEO for Law Firms</div><div class="drop-sub">16 articles</div></div></a>
        <a href="/insights/chatgpt" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div><div><div class="drop-label">ChatGPT for Law Firms</div><div class="drop-sub">29 articles</div></div></a>
        <div class="drop-divider"></div>
        <a href="/resources" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg></div><div><div class="drop-label">Resources</div><div class="drop-sub">Guides &amp; checklists</div></div></a>
      </div>
    </li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
    <li><button class="nav-cta" onclick="document.getElementById('leadModal').style.display='flex'">Get Free Audit</button></li>
  </ul>
</nav>"""

FOOTER_HTML = f"""\
<footer>
  <div class="footer-inner">
    <div><div class="footer-logo">Lex<span>Scale</span>.ai</div><div class="footer-tagline">AI Growth Systems For Law Firms</div></div>
    <div class="footer-links">
      <a href="/ai-website-design-for-law-firms">AI Website Design</a>
      <a href="/ai-seo-for-law-firms">AI SEO</a>
      <a href="/ai-receptionist-for-law-firms">AI Receptionist</a>
      <a href="/ai-chatbot-for-law-firms">AI Chatbot</a>
      <a href="/about">About</a>
      <a href="/insights/google-business-profile">GBP Insights</a>
      <a href="/resources">Resources</a>
      <a href="/contact">Contact</a>
      <a href="/privacy">Privacy</a>
    </div>
    <div class="footer-copy">&copy; {YEAR} LexScale.ai &middot; All rights reserved</div>
  </div>
</footer>"""

STICKY_MODAL_JS = """\
<div id="stickyCTA" style="position:fixed;bottom:0;left:0;right:0;z-index:500;background:linear-gradient(135deg,var(--navy),#1a2456);padding:14px 24px;display:flex;align-items:center;justify-content:space-between;box-shadow:0 -4px 24px rgba(11,21,54,.2);transform:translateY(100%);transition:transform .4s;">
  <div style="color:#fff;font-size:14px;font-weight:600;">Is your law firm dominating Google Maps?</div>
  <button onclick="document.getElementById('leadModal').style.display='flex'" style="background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;border:none;padding:10px 22px;border-radius:100px;font-size:13px;font-weight:700;cursor:pointer;font-family:inherit;white-space:nowrap;">Get Free GBP Audit &rarr;</button>
</div>
<script>setTimeout(function(){document.getElementById('stickyCTA').style.transform='translateY(0)';},3000);</script>

<div id="leadModal" style="display:none;position:fixed;inset:0;z-index:1000;background:rgba(11,21,54,.7);backdrop-filter:blur(6px);align-items:center;justify-content:center;padding:20px;">
  <div style="background:#fff;border-radius:24px;padding:40px;max-width:480px;width:100%;position:relative;box-shadow:0 32px 80px rgba(11,21,54,.25);">
    <button onclick="document.getElementById('leadModal').style.display='none'" style="position:absolute;top:16px;right:16px;background:none;border:none;cursor:pointer;color:#94a3b8;font-size:22px;">&times;</button>
    <div style="font-size:11px;font-weight:700;color:var(--pu);letter-spacing:.8px;text-transform:uppercase;margin-bottom:8px;">Free GBP Audit</div>
    <h3 style="font-size:22px;font-weight:800;color:var(--navy);letter-spacing:-.5px;margin-bottom:6px;">See How Your GBP Stacks Up</h3>
    <p style="font-size:13px;color:#64748b;line-height:1.6;margin-bottom:22px;">Get a free audit of your Google Business Profile and local search visibility.</p>
    <input type="text" placeholder="Your Name" style="width:100%;padding:12px 16px;border:1.5px solid rgba(11,21,54,.12);border-radius:10px;font-size:14px;font-family:inherit;margin-bottom:10px;outline:none;">
    <input type="email" placeholder="Work Email" style="width:100%;padding:12px 16px;border:1.5px solid rgba(11,21,54,.12);border-radius:10px;font-size:14px;font-family:inherit;margin-bottom:10px;outline:none;">
    <input type="text" placeholder="Law Firm Name" style="width:100%;padding:12px 16px;border:1.5px solid rgba(11,21,54,.12);border-radius:10px;font-size:14px;font-family:inherit;margin-bottom:16px;outline:none;">
    <button style="width:100%;background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;border:none;padding:14px;border-radius:100px;font-size:15px;font-weight:700;cursor:pointer;font-family:inherit;">Get My Free Audit &rarr;</button>
  </div>
</div>

<script>
function toggleMobNav(btn){const nav=btn.closest('nav');nav.classList.toggle('mob-open');}
document.addEventListener('DOMContentLoaded',function(){
  document.querySelectorAll('.has-drop>a').forEach(function(a){
    a.addEventListener('click',function(e){
      if(window.innerWidth>768)return;
      e.preventDefault();
      var li=a.closest('.has-drop');
      li.classList.toggle('mob-open');
    });
  });
});
</script>"""


def faq_accordion(pairs):
    items = []
    for i, (q, a) in enumerate(pairs):
        border = "border-bottom:1px solid rgba(106,92,255,.08);" if i < len(pairs) - 1 else ""
        items.append(f"""\
      <div style="{border}padding:20px 0;">
        <button onclick="var d=this.nextElementSibling;d.style.display=d.style.display==='block'?'none':'block';this.querySelector('span').textContent=d.style.display==='block'?'−':'+'" style="width:100%;background:none;border:none;display:flex;justify-content:space-between;align-items:center;cursor:pointer;font-family:inherit;text-align:left;">
          <span style="font-size:15px;font-weight:700;color:var(--navy);">{q}</span>
          <span style="font-size:20px;color:var(--pu);flex-shrink:0;margin-left:12px;">+</span>
        </button>
        <div style="display:none;padding-top:12px;"><p style="font-size:14px;color:#64748b;line-height:1.8;">{a}</p></div>
      </div>""")
    return "\n".join(items)


def stat_row(stats):
    """stats = [(num, label), (num, label), (num, label)]"""
    boxes = "".join(
        f'<div class="stat-box"><div class="s-num">{n}</div><div class="s-lbl">{l}</div></div>'
        for n, l in stats
    )
    return f'<div class="stat-row">{boxes}</div>'


def sidebar_block(stat_num, stat_label, cta_heading, cta_body, related_links):
    links_html = "".join(
        f'<a href="{url}" style="font-size:13px;font-weight:600;color:var(--pu);display:block;line-height:1.4;">{label} &rarr;</a>'
        for label, url in related_links
    )
    return f"""\
  <aside class="sidebar">
    <div class="sidebar-stat">
      <div class="s-num">{stat_num}</div>
      <div class="s-label">{stat_label}</div>
    </div>
    <div class="sidebar-card">
      <h3>{cta_heading}</h3>
      <p>{cta_body}</p>
      <button class="sidebar-btn" onclick="document.getElementById('leadModal').style.display='flex'">Get My Free GBP Audit &rarr;</button>
    </div>
    <div class="sidebar-card">
      <h3 style="margin-bottom:14px;">Related Articles</h3>
      <div style="display:flex;flex-direction:column;gap:12px;">
        {links_html}
      </div>
    </div>
    <div class="sidebar-card">
      <h3 style="margin-bottom:14px;">Our Services</h3>
      <div style="display:flex;flex-direction:column;gap:10px;">
        <a href="/ai-seo-for-law-firms" style="font-size:13px;font-weight:600;color:var(--pu);display:block;">AI SEO for Law Firms &rarr;</a>
        <a href="/ai-website-design-for-law-firms" style="font-size:13px;font-weight:600;color:var(--pu);display:block;">AI Website Design &rarr;</a>
        <a href="/contact" style="font-size:13px;font-weight:600;color:var(--pu);display:block;">Book a Strategy Call &rarr;</a>
      </div>
    </div>
  </aside>"""


def build_page(slug, title, seo_title, description, h1_main, h1_accent, deck,
               meta_date, read_time, stats_3, body_html, faq_pairs,
               cta_h2, cta_p, sidebar_stat_num, sidebar_stat_lbl,
               sidebar_cta_h, sidebar_cta_p, related_links):
    url = f"{SITE}/insights/google-business-profile/{slug}"

    SEO = head_block(
        title=seo_title,
        description=description,
        slug=f"insights/google-business-profile/{slug}",
        og_type="article",
        schemas=[
            article_schema(title, description, url, date_pub=DATE),
            breadcrumb_schema([
                ("Home", SITE),
                ("Insights", f"{SITE}/insights"),
                ("Google Business Profile", HUB_URL),
                (title, url),
            ]),
            faq_schema(faq_pairs),
        ],
    )

    sb = sidebar_block(sidebar_stat_num, sidebar_stat_lbl, sidebar_cta_h,
                       sidebar_cta_p, related_links)

    faq_sec = f"""\
    <div style="background:#f8f7ff;border-radius:20px;padding:40px;margin-top:48px;">
      <h2 style="font-size:22px;font-weight:800;color:var(--navy);letter-spacing:-.5px;margin-bottom:28px;">Frequently Asked Questions</h2>
{faq_accordion(faq_pairs)}
    </div>"""

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
{SEO}
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<style>
{CSS}
</style>
</head>
<body>

{NAV_HTML}

<div class="art-hero">
  <div class="art-hero-inner">
    <a href="/insights/google-business-profile" class="art-cat">
      <div class="art-cat-dot"></div>
      <span class="art-cat-txt">Google Business Profile</span>
    </a>
    <h1 class="art-h1">{h1_main} <span class="accent">{h1_accent}</span></h1>
    <p class="art-deck">{deck}</p>
    <div class="art-meta-row">
      <div class="art-meta-item">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>
        {meta_date}
      </div>
      <div class="art-meta-item">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
        {read_time} min read
      </div>
      <div class="art-meta-item">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
        LexScale.ai Editorial
      </div>
    </div>
  </div>
</div>

<div class="content-wrap">
  <article class="article-body">
{stat_row(stats_3)}
{body_html}
{faq_sec}
  </article>
{sb}
</div>

<div class="cta-banner">
  <div class="cta-inner">
    <h2>{cta_h2}</h2>
    <p>{cta_p}</p>
    <button class="btn-primary" onclick="document.getElementById('leadModal').style.display='flex'">Get My Free GBP Audit &rarr;</button>
  </div>
</div>

{FOOTER_HTML}

{STICKY_MODAL_JS}
</body>
</html>"""
    return page


# ══════════════════════════════════════════════════════════════════════════════
# Article 1 — GBP Photos for Law Firms
# ══════════════════════════════════════════════════════════════════════════════

A1_SLUG  = "gbp-photos-for-law-firms"
A1_TITLE = "Google Business Profile Photos for Law Firms: What to Post and Why It Matters"
A1_SEO_T = "GBP Photos for Law Firms: What to Post | LexScale.ai"
A1_DESC  = "GBP photos affect how often your law firm appears in Google Maps and AI results. Learn which photos to post, how often to update them, and what the algorithm rewards."
A1_FAQ = [
    ("How many photos should a law firm have on Google Business Profile?",
     "Aim for a minimum of 20 high-quality photos. Google's own data shows that businesses with 100+ photos receive 520% more phone calls than the average. For law firms, a practical starting target is 30–50 photos covering your office, team, and firm identity — then build from there with fresh monthly additions."),
    ("Do Google Business Profile photos affect local search ranking?",
     "Yes, directly. Google's local ranking algorithm weights photo quantity, photo quality signals (engagement — views and clicks), and photo recency. A profile with regularly updated photos signals an active, managed business. Google uses image recognition to verify that photos are genuine and relevant, penalising stock images and low-quality uploads."),
    ("Can law firms use stock photos on Google Business Profile?",
     "Technically you can upload them, but you should not. Google's image recognition flags generic stock photos and discounts their ranking value. More importantly, potential clients who see stock imagery on a law firm's GBP profile immediately sense inauthenticity — trust erodes before the first call. All GBP photos should be genuine images of your firm, team, and office."),
]
A1_BODY = """\
    <h2>Why Photos Are a Direct Local Ranking Signal</h2>
    <p>Most law firms think of Google Business Profile photos as a cosmetic nicety — something to fill the profile with a few office shots and forget about. This is wrong. Photos are one of the most directly measurable ranking signals in Google's local search algorithm, and law firms that treat them strategically outperform competitors who don't.</p>
    <p>Google uses photo engagement data — how often your photos are viewed, how many photos you have, how recently photos were added — as signals of business activity and relevance. A GBP profile with 12 photos added three years ago and never updated signals to Google's algorithm that the business may be inactive, stale, or neglected. A profile with 60 photos, updated monthly, signals an active practice that is invested in its online presence.</p>
    <p>Google's published data is unambiguous: businesses with more than 100 photos receive 520% more phone calls, 1,065% more website clicks, and 2,717% more direction requests than the median business. For law firms, where each new client engagement can be worth thousands of dollars, the ROI of a disciplined photo strategy is extraordinary relative to its cost.</p>
    <p>In 2026, Google's AI-powered local recommendations — in Google Maps, in AI Overviews, and in Gemini responses — incorporate visual signals from GBP profiles. A firm whose profile includes professional, authentic, regularly updated photos is more likely to appear in these AI-generated recommendations than a firm with a sparse or stale photo set. The photo strategy you implement today compounds over months and years.</p>

    <h2>The Photo Categories Every Law Firm Needs</h2>
    <p>Google organises GBP photos into specific categories: Exterior, Interior, Team/Staff, At Work, and Additional. Each category serves a different function, and law firms that populate all categories consistently outperform those that post photos randomly without a category strategy.</p>
    <h3>Exterior Photos</h3>
    <p>Upload at least 4–6 exterior shots showing your building from different angles, at different times of day (daytime, evening if your building is illuminated), and in different seasons. Include a photo showing your building from the street with visible signage. This helps clients who have never visited identify your office. It also confirms to Google that your business operates at a real physical location — a legitimacy signal that contributes to local ranking.</p>
    <h3>Interior Photos</h3>
    <p>Show your reception area, boardroom or client meeting rooms, and working spaces. Aim for 6–10 interior shots. The interior photos communicate professionalism, firm culture, and the quality of the environment clients can expect when they visit. Firms in larger cities where clients have many options will be compared partly on the basis of perceived professionalism communicated through interior photography. A modern, well-lit, professionally photographed office signals a premium practice.</p>
    <h3>Team Photos</h3>
    <p>Individual and group team photos are among the highest-performing photo types for law firms in terms of engagement and conversion impact. Clients are hiring a person, not just a brand. Seeing the faces of the lawyers and staff they will be working with reduces anxiety and accelerates trust. Upload professional headshots of all attorneys and a group photo of the full team. Update these when attorneys join or leave the firm.</p>
    <h3>At Work Photos</h3>
    <p>Photos of lawyers in client consultations (with consent), at their desks reviewing documents, in meetings, or in court settings (where permitted) add authenticity and context. These are the hardest photos to produce but have among the highest engagement rates — they depict the actual work, not just the surroundings. Even a posed version of common work scenarios adds significant value compared to office-only imagery.</p>
    <h3>Additional and Product Photos</h3>
    <p>Use this category for community involvement photos (charity events, bar association activities, speaking engagements), awards and recognition photos, and any visuals that reinforce your firm's identity and community presence. These are excellent for differentiating your firm from competitors whose GBP consists entirely of office and team shots.</p>

    <h2>Photo Quality Standards That Move the Needle</h2>
    <p>Quality matters as much as quantity. Google's image recognition algorithms assess photo quality, and low-resolution, poorly lit, or blurry images are discounted in the ranking calculation. More practically, poor photo quality repels potential clients before they've read a single word about your practice.</p>
    <p>The minimum technical standards for GBP photos: minimum 720 x 720 pixels (ideally 1200 x 900 or higher), JPG or PNG format, file size between 10KB and 5MB. Photos should be well-lit, in focus, and uncropped. Avoid adding text overlays, filters, or promotional messaging to GBP photos — Google may reject or deprioritize edited photos that look promotional.</p>
    <p>Hire a professional photographer for your initial batch of photos. A half-day commercial photography session will produce 80–120 usable images across all categories. The cost — typically between $500 and $1,500 depending on your market — is one of the highest-ROI marketing investments a law firm can make, producing assets that will be used across your GBP, website, social media, and print materials for years.</p>

    <div class="callout-box">
      <p><strong>Professional tip:</strong> Ask your photographer to shoot vertical (9:16) versions of key shots alongside horizontal ones. Vertical images display better on mobile Google Maps searches, where most local legal searches now originate. Nearly 70% of "lawyer near me" searches happen on mobile — your photos need to look exceptional on a phone screen.</p>
    </div>

    <p>After your professional session, continue adding photos regularly using a smartphone. Modern smartphones produce GBP-quality images without professional equipment. The goal is recency — a new photo every week or two keeps your profile looking active. Rotate through categories: this week an exterior shot, next week a team event, the week after a community involvement photo.</p>

    <h2>How to Build a Sustainable Photo Cadence</h2>
    <p>The biggest mistake law firms make with GBP photos is treating it as a one-time setup task rather than an ongoing content strategy. Photos posted three years ago and never supplemented signal neglect to Google's algorithm regardless of how many there are. Recency is a scoring factor. The algorithm rewards active management.</p>
    <p>Build photo addition into your monthly marketing workflow. Assign responsibility to a specific person — a marketing coordinator, office manager, or receptionist. Set a minimum of two new photos per month as a baseline. Tie photo opportunities to regular firm activities: team lunches, charity events, speaking engagements, award receptions, new hires. Every firm event is a photo opportunity for your GBP.</p>
    <p>Track your photo views in GBP Insights (Google Business Profile Manager). You will see total photo views, photo view breakdown by category, and how your views compare to similar businesses. Use this data to identify which categories drive the most engagement and invest more heavily in those. In our experience working with law firms, team photos and at-work photos consistently outperform exterior and interior shots for engagement — but exterior shots are critical for the location legitimacy signal they send to Google's algorithm.</p>
    <p>For more on how your full GBP profile — including photos, reviews, posts, and categories — drives local search performance, read our <a href="/insights/google-business-profile/google-business-profile-complete-guide-law-firms">complete Google Business Profile guide for law firms</a> and the <a href="/insights/google-business-profile/gbp-optimization-checklist-law-firms">GBP optimisation checklist</a>. To understand how AI search tools like Gemini and ChatGPT use GBP data, see our article on <a href="/insights/google-business-profile/gbp-for-law-firms-and-ai-search">GBP and AI search for law firms</a>. For the complete local SEO picture, explore our <a href="/ai-seo-for-law-firms">AI SEO services for law firms</a> and our <a href="/ai-website-design-for-law-firms">AI website design services</a>.</p>"""

# ══════════════════════════════════════════════════════════════════════════════
# Article 2 — GBP Q&A for Law Firms
# ══════════════════════════════════════════════════════════════════════════════

A2_SLUG  = "gbp-questions-answers-law-firms"
A2_TITLE = "Using GBP Questions and Answers to Generate More Leads From Google Maps"
A2_SEO_T = "GBP Q&A for Law Firms: More Leads From Maps | LexScale.ai"
A2_DESC  = "The Q&A section on your Google Business Profile is a powerful but overlooked lead tool in legal marketing. Learn how to use it to attract and convert more clients."
A2_FAQ = [
    ("Can law firms add their own questions and answers to Google Business Profile?",
     "Yes. Anyone can submit a question on a GBP listing, including the business owner. Law firms should proactively seed their Q&A section with the questions prospective clients most commonly ask — and provide authoritative, keyword-rich answers. This prevents the section from remaining blank or being filled with questions from third parties before you have the chance to respond."),
    ("How quickly should law firms respond to new Q&A questions?",
     "Within 24 hours. Q&A questions on GBP are publicly visible and can influence whether a prospective client chooses your firm or a competitor. Unanswered questions create doubt — potential clients wonder if the firm is attentive, if the information is current, or if the firm is even still operating. Monitor your GBP Q&A section daily, or set up Google Business Profile notifications so you are alerted when new questions are submitted."),
    ("Do answers in GBP Q&A affect Google search rankings?",
     "Google indexes the content of GBP Q&A sections and uses it as a relevance signal for local search. Thorough, keyword-rich answers that address the specific legal services you offer in your geographic market can improve your profile's relevance for related search queries. The Q&A section is, in effect, a secondary content block within your GBP — treat it with the same keyword intentionality you apply to your website's service pages."),
]
A2_BODY = """\
    <h2>The Most Overlooked Section of Every Law Firm's GBP</h2>
    <p>If you search for your law firm on Google Maps right now and look at your Google Business Profile, there is a high probability that the Q&A section is either empty, answered inconsistently, or populated with random questions that no one from your firm has addressed. This is true of the majority of law firm GBP profiles — and it represents a significant missed opportunity.</p>
    <p>The Q&A section appears prominently in Google Maps and in the knowledge panel that surfaces when someone searches directly for your firm. It is one of the first things a prospective client encounters when evaluating whether to contact your firm. A blank Q&A section signals neglect. A poorly answered Q&A section can actively damage conversion. A well-managed Q&A section, by contrast, is a 24/7 lead generation asset that addresses objections, establishes expertise, and moves prospects toward making contact.</p>
    <p>Unlike reviews, which you depend on clients to provide, Q&A is a section you can proactively control. You can submit your own questions and provide your own answers. You can upvote answers to ensure the best ones appear most prominently. You can respond to questions submitted by third parties before anyone else does. This level of control makes Q&A one of the most actionable GBP optimisation levers available to law firms.</p>

    <h2>How to Seed Your Q&A Section Strategically</h2>
    <p>Do not wait for prospective clients to submit questions. Proactively populate your Q&A section with the questions your intake team hears most frequently. These are the questions that determine whether a prospect converts to a consultation — which means they are the questions that have the highest commercial value when answered well.</p>
    <p>To submit a question on your own GBP, search for your firm on Google Maps while logged into a personal Google account (not your business account), navigate to the Q&A section, click "Ask a question," and submit your question. Then log into your GBP dashboard and respond with your authoritative answer. Repeat for each question you want to seed.</p>
    <p>The best questions to seed are those that prospective clients have at the moment of decision — the questions that, if answered well, move them from consideration to contact. Examples that consistently perform well for law firms include: "How much does a [practice area] lawyer cost?", "What should I do immediately after [triggering event]?", "How long does a [matter type] case typically take?", "What do I need to bring to my first consultation?", "Do you offer free initial consultations?", and "Are you available to take cases outside [city]?"</p>
    <h3>Answer Formula for Maximum Conversion Impact</h3>
    <p>Each Q&A answer should follow a simple formula: lead with a direct, specific answer (not "it depends"), provide one to two sentences of context, and close with a call to action directing the reader to contact your firm. Keep answers between 50 and 150 words — long enough to be substantive, short enough to be read in the context of a mobile Google Maps search.</p>
    <p>Include your primary practice area keyword and city name in answers where it flows naturally. "Our Toronto family law firm offers free 30-minute initial consultations" is better than "Yes, we offer free consultations" — both from a conversion standpoint and as a local search relevance signal. Google indexes these answers, and keyword-relevant answers strengthen your profile's relevance for local legal searches.</p>

    <div class="callout-box">
      <p><strong>Important:</strong> Do not include specific legal advice in Q&A answers. Q&A answers are public and speak to an unknown audience. Answers should be general, practical, and procedural — addressing process, cost, and logistics rather than providing legal counsel on specific fact patterns. This protects your firm professionally and sets appropriate expectations with prospective clients.</p>
    </div>

    <h2>Monitoring and Responding to Third-Party Questions</h2>
    <p>Anyone with a Google account can submit a question on your GBP listing. They do not have to be a client or even someone who has interacted with your firm. This means your Q&A section can receive questions from genuine prospective clients, current clients with questions better handled through direct contact, competitors conducting research, and occasionally spam or off-topic submissions.</p>
    <p>The critical discipline is speed. Questions submitted by third parties sit unanswered until you respond — and that silence is visible to every prospective client who views your profile during that window. Set up push notifications for your GBP so you are alerted immediately when a new question is submitted. Aim to respond within 24 hours, ideally within a few hours. In the legal services context, response speed communicates responsiveness — a quality that prospective clients are explicitly evaluating when they are choosing a law firm.</p>
    <p>Note also that other Google users can answer questions on your listing — and their answers appear alongside yours. Monitor third-party answers carefully. If another user provides an answer that is inaccurate, misleading, or professionally problematic, you can flag it for removal and submit a correct answer. Your answers as the business owner appear with a "Business owner" badge, which signals authority — but only if you are present and responsive enough to have answered first.</p>

    <h2>Using Q&A to Address Common Objections</h2>
    <p>Every legal service has predictable conversion objections — reasons why a prospect might hesitate to make contact. The Q&A section gives you a public, indexed platform to address these objections before the prospect even reaches out. This is one of the most powerful conversion levers in GBP management.</p>
    <p>Common law firm objections that Q&A can neutralise: cost uncertainty ("I don't know if I can afford a lawyer"), jurisdictional confusion ("I'm not sure if this firm handles my type of case"), process anxiety ("I don't know what happens after the first call"), timing uncertainty ("I don't know if I need a lawyer yet or if this can wait"), and privacy concerns ("I'm worried about who will see my information").</p>
    <p>For each objection, craft a Q&A entry that directly addresses it. "How much does it cost to hire a family lawyer?" → "Our family law retainers typically range from $X to $X depending on the complexity of your matter. We offer a free 30-minute consultation with no obligation. Call us at [phone] or book online to discuss your situation and get an accurate estimate." This answer addresses cost anxiety, provides social proof of accessibility through the free consultation, and ends with a direct CTA.</p>
    <p>For the full picture of how your GBP generates leads, see our article on <a href="/insights/google-business-profile/gbp-posts-for-law-firms">GBP Posts for law firms</a> and the <a href="/insights/google-business-profile/gbp-reviews-for-law-firms">Google Reviews guide</a>. Our <a href="/insights/google-business-profile/google-business-profile-complete-guide-law-firms">complete GBP guide</a> covers every section of the profile in depth. For the broader local SEO strategy, explore our <a href="/ai-seo-for-law-firms">AI SEO for law firms</a> service and our <a href="/resources">resources library</a>. Ready to turn your GBP into a lead generation machine? <a href="/contact">Contact our team</a> for a free GBP audit.</p>"""

# ══════════════════════════════════════════════════════════════════════════════
# Article 3 — GBP Categories for Law Firms
# ══════════════════════════════════════════════════════════════════════════════

A3_SLUG  = "gbp-categories-for-law-firms"
A3_TITLE = "Choosing the Right Google Business Profile Categories for Your Law Firm"
A3_SEO_T = "GBP Categories for Law Firms: Rank Higher Locally | LexScale.ai"
A3_DESC  = "Wrong GBP categories tank your local rankings overnight. Learn which primary and secondary categories help law firms rank higher in Google Maps and AI local results."
A3_FAQ = [
    ("What is the best primary category for a law firm on Google Business Profile?",
     "The best primary GBP category is the most specific category that accurately describes your firm's core practice. 'Personal Injury Attorney' outperforms 'Law Firm' for personal injury searches. 'Family Law Attorney' outperforms 'Lawyer' for family law searches. Always choose the most specific accurate primary category that matches your dominant practice area. Reserve the broader 'Law Firm' or 'Lawyer' category as a secondary category only if relevant."),
    ("How many categories can a law firm add to Google Business Profile?",
     "Google allows up to 10 categories per GBP listing — one primary and up to 9 secondary. Most law firms should use 4–7 secondary categories that accurately reflect their practice areas. Do not add categories that do not genuinely reflect services you offer — irrelevant categories dilute your profile's relevance signals and can result in appearing for searches where you cannot convert the lead."),
    ("Can changing GBP categories hurt my law firm's rankings?",
     "Yes. Changing your primary category resets some of the relevance signals Google has built around your profile for that category. Avoid changing your primary category unless your firm genuinely pivots its main practice area. Adding or adjusting secondary categories is lower-risk and can be done as your practice areas evolve. Monitor your GBP Insights for 30–60 days after any category change to assess the impact on search visibility and profile actions."),
]
A3_BODY = """\
    <h2>Why Category Selection Is the Foundation of Local Pack Rankings</h2>
    <p>Your Google Business Profile primary category is the single most powerful relevance signal you control in local search. Google uses your primary category to determine which searches your profile is eligible to appear for in the local pack and Google Maps results. Get it wrong and you are invisible for searches that should be converting to consultations. Get it right and you immediately gain visibility for the searches your most valuable prospects are running.</p>
    <p>The mistake most law firms make is choosing a category that is too broad. "Lawyer" and "Law Firm" are valid GBP categories, but they compete for relevance across every practice area simultaneously — which means they achieve dominance in none. A personal injury firm that uses "Personal Injury Attorney" as its primary category will consistently outrank a firm using "Lawyer" for personal injury searches, everything else being equal. Specificity is rewarded.</p>
    <p>This matters more than most law firm marketers realise because Google's local ranking algorithm uses the primary category as the dominant filter for determining which searches trigger your profile. Your category effectively tells Google: "These are the searches I want to appear for." Choosing too broadly or too narrowly costs you either relevance or reach — and in a competitive legal market, you cannot afford either.</p>

    <h2>Primary Category Strategy: The Right Level of Specificity</h2>
    <p>The ideal primary category is the most specific category that accurately describes the practice area that generates the majority of your firm's revenue. Here is how this plays out across common law firm types:</p>
    <ul>
      <li><strong>Personal injury firm:</strong> "Personal Injury Attorney" — not "Lawyer" or "Law Firm"</li>
      <li><strong>Family law practice:</strong> "Family Law Attorney" — not "Divorce Lawyer" (which is not a current GBP category option) or "Law Firm"</li>
      <li><strong>Criminal defence:</strong> "Criminal Justice Attorney" — the closest current match in GBP's category taxonomy</li>
      <li><strong>Immigration practice:</strong> "Immigration Attorney" — highly specific and directly maps to the primary search intent</li>
      <li><strong>Estate planning:</strong> "Estate Planning Attorney" — preferred over "Wills and Estates Lawyer"</li>
      <li><strong>Real estate law:</strong> "Real Estate Attorney" — specific to the transactional and litigation work</li>
      <li><strong>Multi-practice general firm:</strong> "Law Firm" as primary, with specific practice area categories as secondaries</li>
    </ul>
    <p>GBP category options are set by Google and are not infinitely customisable. The available legal categories in Google's taxonomy change periodically. Always search within the GBP category field (not on a third-party list) to see current options — third-party category lists can be outdated by months or years.</p>

    <h2>Secondary Categories: Extending Your Reach Without Diluting Relevance</h2>
    <p>Secondary categories expand the set of searches for which your profile is eligible without displacing the primary relevance signal your main category provides. Used correctly, secondary categories multiply your visibility across related practice areas. Used incorrectly, they dilute your profile's focus and create confusion about what your firm actually does.</p>
    <p>The rule for secondary categories: only add categories that accurately reflect services your firm genuinely provides and that you want to receive and convert leads for. Adding "Personal Injury Attorney" as a secondary category when your firm does not handle personal injury matters creates a mismatch — prospects who find you through that category and then discover you don't handle their case type have wasted time, and Google's algorithm eventually penalises profiles for irrelevant category matches signalled by high bounce rates and no engagement.</p>
    <h3>Effective Secondary Category Combinations</h3>
    <p>For a family law firm with estate planning services: "Family Law Attorney" (primary), "Estate Planning Attorney," "Divorce Lawyer" (if listed), "Mediation Service," "Law Firm." For a personal injury firm with criminal defence services: "Personal Injury Attorney" (primary), "Criminal Justice Attorney," "Law Firm." For a general practice firm: "Law Firm" (primary), "Family Law Attorney," "Real Estate Attorney," "Estate Planning Attorney," "Business Administration Service" (if you do corporate work).</p>
    <p>Audit your secondary categories annually. As your firm's practice mix evolves — if you enter or exit a practice area — update your secondary categories to match. Outdated secondary categories that no longer reflect your services cost you relevance points with Google's algorithm when the signals from your website, reviews, and posts don't align with those category claims.</p>

    <h2>How Categories Interact with Other GBP Signals</h2>
    <p>Your GBP category does not operate in isolation. Google cross-references your category against the content of your website, the keywords in your reviews, the topics of your GBP posts, and the keywords in your Q&A section. Profiles where all of these signals align with the primary category rank higher than profiles where signals conflict.</p>
    <p>If your primary GBP category is "Family Law Attorney" but your website's homepage is dominated by content about estate planning and your GBP posts are about business law, Google perceives a signals mismatch and your family law rankings suffer. The strongest local pack positions are built by firms where every signal — website, reviews, posts, Q&A, photos, and category — consistently reinforces the same practice area identity.</p>
    <p>This is why GBP optimisation cannot be treated as a standalone exercise. Your GBP category strategy needs to be aligned with your website's SEO strategy, your content strategy, and your review acquisition approach. For a law firm building serious local search dominance, all of these pieces work together — or they underperform separately. Our <a href="/insights/google-business-profile/gbp-optimization-checklist-law-firms">GBP optimisation checklist</a> walks through every element of this alignment. For the AI search dimension, see <a href="/insights/google-business-profile/gbp-for-law-firms-and-ai-search">GBP and AI search for law firms</a>. To get your full GBP strategy right, explore our <a href="/ai-seo-for-law-firms">AI SEO service</a>, our <a href="/ai-website-design-for-law-firms">law firm website design</a>, and our <a href="/resources">resources library</a> — or <a href="/contact">speak with our team</a> directly.</p>"""

# ══════════════════════════════════════════════════════════════════════════════
# Article 4 — GBP for Family Law Firms
# ══════════════════════════════════════════════════════════════════════════════

A4_SLUG  = "gbp-family-law-firms"
A4_TITLE = "Google Business Profile Optimisation for Family Law Firms"
A4_SEO_T = "GBP Optimisation for Family Law Firms | LexScale.ai"
A4_DESC  = "Family law clients search Google Maps before making an emotional phone call. A fully optimised GBP puts your family law firm in front of these clients at the right moment."
A4_FAQ = [
    ("What GBP primary category should a family law firm use?",
     "Use 'Family Law Attorney' as your primary GBP category. This is the most specific accurate category for family law practices and directly matches the search queries your ideal clients are using. Secondary categories might include 'Divorce Lawyer' (if available in your region's GBP taxonomy), 'Mediation Service,' 'Estate Planning Attorney' (if you offer that), and 'Law Firm.' Avoid using the generic 'Lawyer' or 'Law Firm' as your primary category — you lose specificity and compete across all practice areas without dominating any."),
    ("How should family law firms handle sensitive topics in their GBP description?",
     "Acknowledge the emotional weight of the client's situation without sensationalising it. Phrases like 'We understand that family law matters are among the most stressful experiences of your life' establish empathy without being exploitative. Your GBP description should be factual, warm, and professional — describing your services, geographic coverage, and approach in 750 characters or fewer. Avoid making claims about outcomes or implying results that may not be achievable."),
    ("Should family law firms use GBP posts to address specific topics like divorce or child custody?",
     "Yes — with professional care. GBP posts on family law topics (divorce process, custody arrangements, property division, spousal support) serve as both trust signals and keyword-relevance content. Each post should be informative and educational rather than alarmist or emotionally manipulative. Clients searching for family law help are already in a difficult situation — your posts should reassure them that your firm understands their situation and is equipped to help, not amplify their anxiety."),
]
A4_BODY = """\
    <h2>The Unique Psychology of the Family Law Client Search</h2>
    <p>Family law searches are unlike any other legal search category. A person searching for a personal injury attorney is often in pain but has time to research. A person searching for a criminal defence lawyer may be panicked but has a clear immediate need. A person searching for a family law firm is often in emotional turmoil — navigating the breakdown of a marriage, a custody dispute, or an estate conflict — and they are making decisions while emotionally compromised.</p>
    <p>This emotional context shapes everything about how family law firms should present themselves on Google Business Profile. The prospective client is not comparison shopping on price. They are looking for signals of trust, competence, empathy, and local accessibility. Your GBP is often the first impression your firm makes on this person in one of the most difficult moments of their life. The profile that communicates "we understand what you are going through and we know how to help" wins the call.</p>
    <p>Google Maps research precedes the phone call in the vast majority of family law client acquisition journeys. Prospective clients search, compare two or three profiles, read reviews looking for stories that match their situation, and then call the firm whose profile communicated the right combination of competence and humanity. A technically complete but emotionally cold GBP — all facts, no warmth — underperforms against a profile that signals genuine understanding of the client's situation.</p>

    <h2>Writing a GBP Description That Converts Family Law Prospects</h2>
    <p>Your GBP business description is 750 characters — roughly 100 to 120 words. Every word should do work. For family law firms, the description needs to accomplish four things: establish what you do (practice area), where you do it (geographic market), how you are different (distinctive quality or approach), and prompt a next action (contact or consultation).</p>
    <p>A high-converting family law GBP description structure: Open with a statement that acknowledges the client's emotional situation. Follow with a description of your specific practice areas within family law. Name your primary geographic markets. Mention the consultation format. Close with your direct contact information or an explicit prompt to call or book online.</p>
    <p>Example structure: "Navigating divorce, custody, and family law disputes requires a firm that is as strategic as it is compassionate. [Firm Name] has represented [City] families through separation, child custody, property division, and spousal support matters since [year]. We provide clear guidance, transparent fees, and direct lawyer access — because you deserve to know where your case stands. Call [phone] for a free 30-minute consultation."</p>
    <p>The key phrases that perform in family law GBP descriptions: references to the specific practice areas you handle (divorce, custody, separation, property division), your city or region, the consultation offer, and a tone that is professional but warm rather than clinical. Avoid legal jargon — prospective family law clients are not lawyers and the description should be entirely accessible without any legal background.</p>

    <h2>Reviews: The Most Powerful Signal for Family Law Firms</h2>
    <p>In family law, reviews are more important than in any other legal category. Prospective clients are making an intimate, high-stakes decision in an emotionally compromised state. Reviews from people who have been through similar experiences — divorce, custody disputes, family business conflicts — are the single most persuasive content on your entire GBP profile.</p>
    <p>When family law clients read reviews, they are looking for specific things: reviewers who describe situations that mirror their own, language that confirms the firm was empathetic and accessible, references to outcomes that were as good as possible given the circumstances, and confirmation that the process — however difficult — was handled with professionalism. Generic five-star reviews ("great service, highly recommend") have almost no impact. Specific, narrative reviews ("went through a difficult custody case, [lawyer] kept me informed every step of the way, the outcome was better than I hoped") are enormously persuasive.</p>
    <p>Build your review acquisition strategy around requesting reviews from clients immediately after successful matter resolutions. Family law matters often have emotionally loaded resolution points — the final divorce order, the signed parenting agreement, the property settlement — where clients feel relief and gratitude. That is the moment to ask. For detailed guidance on how to build a compliant review pipeline, see our full <a href="/insights/google-business-profile/gbp-reviews-for-law-firms">guide to Google reviews for law firms</a>.</p>

    <div class="callout-box">
      <p><strong>Family law review tip:</strong> Respond to every review — positive and negative — with specific, empathetic language. Review responses on a family law GBP are read by prospective clients assessing how the firm treats people. A professional, warm response to even a critical review can actually convert prospects who would have been deterred by the review alone.</p>
    </div>

    <h2>GBP Posts for Family Law: Content That Builds Trust</h2>
    <p>Family law firms that publish regular GBP posts outperform those that don't — both in local search ranking (post frequency is an activity signal) and in conversion (posts provide additional content for undecided prospects to engage with before making contact). The content strategy for family law GBP posts should be educational, empathetic, and practical.</p>
    <p>High-performing post topics for family law GBP profiles: "What to expect in your first family law consultation," "How property is divided in a divorce in [province/state]," "Your rights as a non-custodial parent," "Understanding the difference between legal separation and divorce," "How to prepare financially for a divorce," and "What factors do courts consider in child custody decisions." Each of these topics directly addresses questions that prospective clients are searching before they find a lawyer.</p>
    <p>Post monthly at minimum. Each post should be 150–300 words with a clear headline, a substantive body that delivers real information, and a call to action directing readers to book a consultation or call the firm directly. Include a relevant photo — the team, the office, or a professional stock image of families (parents with children, not distressed imagery) — to increase post engagement. For a complete framework on GBP posting for law firms, see our dedicated article on <a href="/insights/google-business-profile/gbp-posts-for-law-firms">GBP Posts for law firms</a>.</p>
    <p>The complete family law GBP strategy connects every element: the right category, a converting description, a review pipeline, regular posts, and active Q&A management. For the broader SEO picture that supports your GBP, explore our <a href="/ai-seo-for-law-firms">AI SEO services</a>, our <a href="/ai-website-design-for-law-firms">family law website design</a>, our <a href="/resources">resources</a>, and our <a href="/contact">free strategy consultation</a>.</p>"""

# ══════════════════════════════════════════════════════════════════════════════
# Article 5 — GBP for Criminal Defense Law Firms
# ══════════════════════════════════════════════════════════════════════════════

A5_SLUG  = "gbp-criminal-defense-law-firms"
A5_TITLE = "Google Business Profile for Criminal Defense Lawyers: Win the Local Pack"
A5_SEO_T = "GBP for Criminal Defense Lawyers: Win Local Pack | LexScale.ai"
A5_DESC  = "Criminal defense clients search for an attorney in a moment of panic. Dominating the Google Maps local pack for criminal defense puts your firm first when urgency is highest."
A5_FAQ = [
    ("What GBP primary category should a criminal defense lawyer use?",
     "Use 'Criminal Justice Attorney' as your primary GBP category — this is the most specific and widely recognised category for criminal defence practices in Google's taxonomy. Secondary categories can include 'DUI & DWI Attorney,' 'Lawyer,' and 'Law Firm.' If you also handle civil matters, those can be added as secondary categories without displacing your criminal defence primary relevance. Avoid 'Lawyer' as primary — it is too broad to compete effectively for criminal defence searches."),
    ("How fast do criminal defense clients convert from Google Maps search to phone call?",
     "Extremely fast. Research indicates that criminal defence Google Maps searches have among the highest same-session conversion rates of any legal category — typically 60–80% of searchers who view a criminal defence GBP call within minutes. This is because criminal defence searches are driven by immediate, urgent need. Someone whose family member has been arrested is not comparison shopping over days; they are making a phone call within minutes of finding a credible option. Your GBP needs to be optimised to convert at this speed."),
    ("Should criminal defense law firms respond to negative GBP reviews?",
     "Yes — always, and promptly. Criminal defence clients' situations are highly charged, and negative reviews often reflect outcome disappointment rather than genuine service failure. Respond professionally: acknowledge the feedback, avoid revealing case details or arguing the facts publicly, and invite the reviewer to contact you directly. A calm, professional response to a negative review in the criminal defence context actually builds trust with prospective clients who understand that criminal cases do not always end with acquittals."),
]
A5_BODY = """\
    <h2>The Urgency-Driven Search: Criminal Defence Is Different</h2>
    <p>No legal search category has higher urgency than criminal defence. Someone whose family member was arrested at midnight is not reading blog posts, comparing law firm websites, or requesting multiple consultations. They are on Google Maps at 1am, scanning profiles, and calling the first firm that looks credible and available. The time between search and first phone call in criminal defence is measured in minutes, not hours or days.</p>
    <p>This urgency fundamentally changes how your Google Business Profile needs to be optimised. In family law or estate planning, you are building trust over a longer evaluation window. In criminal defence, your GBP has seconds to communicate credibility, availability, and competence before the searcher calls you or moves to the next listing. Every element of your profile — your photos, your description, your review score, your response time signals — must be optimised for instant trust transfer.</p>
    <p>The stakes are also higher per client than in most practice areas. Criminal defence retainers are substantial, and a serious criminal matter — felony charges, DUI with injury, white-collar crime — can represent tens of thousands of dollars in fees over the life of the matter. The ROI of dominating the local pack for criminal defence searches in your market is among the highest available in legal marketing.</p>

    <h2>Profile Setup: The Criminal Defence GBP Must-Haves</h2>
    <p>Your GBP primary category should be "Criminal Justice Attorney" — the most specific available category for criminal defence practices. Supplement with secondary categories that reflect your specific criminal sub-specialties: "DUI & DWI Attorney" if you handle drink-driving cases, "Bankruptcy Attorney" if you handle white-collar financial crimes, "Lawyer" as a broad catch-all secondary. The primary category signals to Google exactly which searches your profile is most relevant for.</p>
    <p>The business description is especially critical for criminal defence GBPs. Prospective clients — often family members of the accused — are scanning for specific signals: 24/7 availability, experience with the specific charge type, local court knowledge, and an accessible first step (free consultation or immediate call-back). Your 750-character description must communicate all of these signals clearly and quickly.</p>
    <p>A high-converting criminal defence description template: "[Firm Name] defends clients facing serious criminal charges in [City/County] courts. Our criminal defence team handles [charge types: DUI, drug offences, assault, fraud, etc.] with over [X] years of combined courtroom experience. We are available 24/7 — including for arrest calls and bail hearings. Call [phone] immediately for a confidential consultation. We answer at any hour."</p>
    <p>The phrase "available 24/7" is arguably the most conversion-critical statement on a criminal defence GBP. Many arrests happen evenings and weekends. A firm that explicitly signals availability outside business hours will consistently outperform competitors whose profiles imply 9-to-5 accessibility only. If you genuinely do answer calls around the clock — even via a legal intake service — say so explicitly on your profile.</p>

    <div class="callout-box">
      <p><strong>24/7 intake is not optional for top criminal defence firms.</strong> The window between arrest and the first court appearance is critical, and the family member making that call needs to reach someone immediately. An <a href="/ai-receptionist-for-law-firms">AI receptionist</a> can capture those midnight leads and route genuine emergencies to your on-call lawyer — ensuring you never lose a high-value criminal matter to a competitor who picked up the phone.</p>
    </div>

    <h2>Reviews for Criminal Defence: Volume, Recency, and Emotional Resonance</h2>
    <p>Criminal defence reviews have a specific character that separates them from reviews in other legal categories. The best criminal defence reviews describe specific charge types, specific courts or jurisdictions, and — critically — favourable outcomes or exceptional professional conduct even in difficult cases. "My son was facing felony drug charges. [Lawyer] got the charges reduced to a misdemeanour. We couldn't believe it." This is the type of review that converts criminal defence leads at the moment of highest urgency.</p>
    <p>Build your review acquisition process specifically around the resolution point of criminal matters: acquittals, charge reductions, diversions, successful bail hearings, and suspended sentences. These are the moments when clients feel genuine relief and gratitude — and when asking for a review is appropriate and natural. A simple text message with your Google review link immediately following a favourable verdict or resolution converts at a high rate in the criminal defence context.</p>
    <p>Volume matters more in criminal defence than in almost any other legal category because the decision timeline is so compressed. A prospect scanning Google Maps at 1am does not have time to read detailed reviews — they are doing a rapid credibility scan: review count (more = established), average rating (4.5+ = safe to call), recency (recent reviews = currently active). Aim for 50+ reviews as your medium-term target, 100+ as your long-term goal. In competitive urban criminal defence markets (major metropolitan areas), 200+ reviews may be needed to consistently hold top-3 local pack positions.</p>

    <h2>Posts, Photos, and Q&A for Criminal Defence GBPs</h2>
    <p>GBP posts for criminal defence firms should address the questions urgent searchers are asking at the moment of crisis: "What to do if you've been arrested," "Your rights during a police stop," "What happens at a bail hearing," "How to choose a criminal defence lawyer," "What are the penalties for [charge type] in [jurisdiction]." These posts position your firm as the authoritative resource at the exact moment when potential clients are searching in panic.</p>
    <p>Photos for criminal defence GBPs should emphasise professionalism, experience, and presence. Images of your lawyers in court attire, your office, and the courthouses you regularly appear in (where permitted) build the visual credibility that converts urgent searches. Team photos showing confident, professional lawyers are especially important — the prospective client is choosing someone to defend them in the most stressful situation of their life, and visual signals of competence matter enormously at this decision point.</p>
    <p>Seed your Q&A section with the questions that criminal defence clients are most likely to ask: "Are you available for immediate consultations?", "What are your fees for criminal defence?", "Do you handle [specific charge type]?", "Which courts do you appear in?", "What should I do if I've been charged?" Answer each with directness and specificity — the urgency of the criminal defence search context rewards answers that provide clear, actionable information without equivocation.</p>
    <p>The criminal defence GBP strategy works best when it supports a broader local SEO infrastructure. Your website needs to rank for criminal defence terms alongside your GBP. Your content should mirror your GBP signals. For the full picture, explore our <a href="/ai-seo-for-law-firms">AI SEO for law firms</a>, our <a href="/ai-website-design-for-law-firms">criminal defence website design</a>, our <a href="/insights/google-business-profile/google-business-profile-complete-guide-law-firms">complete GBP guide</a>, and our <a href="/resources">resources library</a>. To get your criminal defence GBP optimised today, <a href="/contact">speak with our team</a>.</p>"""

# ══════════════════════════════════════════════════════════════════════════════
# Article definitions
# ══════════════════════════════════════════════════════════════════════════════

ARTICLES = [
    dict(
        slug=A1_SLUG,
        title=A1_TITLE,
        seo_title=A1_SEO_T,
        description=A1_DESC,
        h1_main="GBP Photos for Law Firms:",
        h1_accent="What to Post and Why It Matters",
        deck="Most law firms treat Google Business Profile photos as an afterthought. They are a direct ranking signal — and the firms that post strategically and consistently dominate Google Maps.",
        meta_date="July 1, 2026",
        read_time=10,
        stats_3=[("520%", "More phone calls for businesses with 100+ GBP photos vs. the median"),
                 ("70%", "Of 'lawyer near me' searches now originate on mobile"),
                 ("2,717%", "More direction requests for photo-rich GBP profiles")],
        body_html=A1_BODY,
        faq_pairs=A1_FAQ,
        cta_h2="Make Your GBP Photos Work Harder",
        cta_p="LexScale.ai builds complete GBP photo strategies for law firms — from professional photography briefs to monthly update cadences that keep your profile ranked.",
        sidebar_stat_num="520%",
        sidebar_stat_lbl="More phone calls for businesses with 100+ GBP photos vs. the average business",
        sidebar_cta_h="Get Your GBP Audit",
        sidebar_cta_p="Find out exactly what your GBP photos are (and aren't) doing for your local rankings.",
        related_links=[
            ("Complete GBP Guide for Law Firms", "/insights/google-business-profile/google-business-profile-complete-guide-law-firms"),
            ("GBP Optimisation Checklist", "/insights/google-business-profile/gbp-optimization-checklist-law-firms"),
            ("GBP Posts for Law Firms", "/insights/google-business-profile/gbp-posts-for-law-firms"),
        ],
    ),
    dict(
        slug=A2_SLUG,
        title=A2_TITLE,
        seo_title=A2_SEO_T,
        description=A2_DESC,
        h1_main="GBP Questions & Answers:",
        h1_accent="Generate More Leads From Google Maps",
        deck="The Q&A section on your Google Business Profile appears before reviews and descriptions for many mobile searchers. Most law firms leave it blank. The ones who don't are converting more leads.",
        meta_date="July 1, 2026",
        read_time=9,
        stats_3=[("Q&A", "Indexed by Google as a local search relevance signal"),
                 ("24hr", "Maximum response time before prospects move to a competitor"),
                 ("750", "Maximum characters for GBP description — every word must work")],
        body_html=A2_BODY,
        faq_pairs=A2_FAQ,
        cta_h2="Turn Your GBP Q&A Into a Lead Machine",
        cta_p="LexScale.ai builds complete GBP lead generation systems for law firms — including Q&A strategy, review pipelines, and post cadences.",
        sidebar_stat_num="24hrs",
        sidebar_stat_lbl="Maximum acceptable response time for new GBP Q&A questions before prospects move on",
        sidebar_cta_h="Get a Free GBP Audit",
        sidebar_cta_p="Find out how your Q&A section stacks up — and what it's costing you in unconverted leads.",
        related_links=[
            ("GBP Reviews for Law Firms", "/insights/google-business-profile/gbp-reviews-for-law-firms"),
            ("GBP Posts for Law Firms", "/insights/google-business-profile/gbp-posts-for-law-firms"),
            ("Complete GBP Guide", "/insights/google-business-profile/google-business-profile-complete-guide-law-firms"),
        ],
    ),
    dict(
        slug=A3_SLUG,
        title=A3_TITLE,
        seo_title=A3_SEO_T,
        description=A3_DESC,
        h1_main="GBP Categories for Law Firms:",
        h1_accent="Choose Right to Rank Higher",
        deck="Your Google Business Profile primary category is the single most powerful relevance signal you control in local search. Most law firms choose too broadly and pay the price in rankings.",
        meta_date="July 1, 2026",
        read_time=9,
        stats_3=[("10", "Maximum GBP categories per listing — use 4–7 for best results"),
                 ("#1", "Factor Google uses to filter local pack eligibility by search query"),
                 ("30–60", "Days to monitor rankings after any GBP category change")],
        body_html=A3_BODY,
        faq_pairs=A3_FAQ,
        cta_h2="Get Your GBP Category Strategy Right",
        cta_p="LexScale.ai audits and optimises GBP categories for law firms as part of a complete local search strategy. Start with a free GBP audit.",
        sidebar_stat_num="10",
        sidebar_stat_lbl="Maximum GBP categories allowed — most law firms should use 4–7 precise ones",
        sidebar_cta_h="Free GBP Category Audit",
        sidebar_cta_p="Find out if your current categories are costing you local pack positions — and what to change.",
        related_links=[
            ("GBP Optimisation Checklist", "/insights/google-business-profile/gbp-optimization-checklist-law-firms"),
            ("Complete GBP Guide", "/insights/google-business-profile/google-business-profile-complete-guide-law-firms"),
            ("GBP and AI Search", "/insights/google-business-profile/gbp-for-law-firms-and-ai-search"),
        ],
    ),
    dict(
        slug=A4_SLUG,
        title=A4_TITLE,
        seo_title=A4_SEO_T,
        description=A4_DESC,
        h1_main="Google Business Profile for Family Law Firms:",
        h1_accent="Convert Clients at Their Most Vulnerable Moment",
        deck="Family law clients don't choose a firm on price — they choose on trust. Your GBP is the first trust signal they encounter. Here is how to make it count.",
        meta_date="July 1, 2026",
        read_time=11,
        stats_3=[("86%", "Of family law clients consult online reviews before making first contact"),
                 ("3", "Reviews mentioning specific outcomes needed to influence undecided prospects"),
                 ("750", "Characters in GBP description — empathy and specificity must both fit")],
        body_html=A4_BODY,
        faq_pairs=A4_FAQ,
        cta_h2="Build a GBP That Converts Family Law Clients",
        cta_p="LexScale.ai builds complete GBP and local SEO strategies for family law firms — combining profile optimisation, review pipelines, and content that converts.",
        sidebar_stat_num="86%",
        sidebar_stat_lbl="Of family law clients read online reviews before making their first call to a firm",
        sidebar_cta_h="Get a Family Law GBP Audit",
        sidebar_cta_p="Find out what your GBP is communicating to prospective family law clients — and what to improve.",
        related_links=[
            ("GBP Reviews for Law Firms", "/insights/google-business-profile/gbp-reviews-for-law-firms"),
            ("GBP Posts for Law Firms", "/insights/google-business-profile/gbp-posts-for-law-firms"),
            ("GBP for Personal Injury Firms", "/insights/google-business-profile/gbp-personal-injury-law-firms"),
        ],
    ),
    dict(
        slug=A5_SLUG,
        title=A5_TITLE,
        seo_title=A5_SEO_T,
        description=A5_DESC,
        h1_main="GBP for Criminal Defense Lawyers:",
        h1_accent="Win the Local Pack When It Matters Most",
        deck="Criminal defense searches have the highest same-session conversion rate of any legal category. Your GBP profile has seconds to communicate credibility. Here is how to dominate.",
        meta_date="July 1, 2026",
        read_time=10,
        stats_3=[("60–80%", "Same-session conversion rate for criminal defence Google Maps searches"),
                 ("1am", "When most criminal defence searches happen — 24/7 availability is non-negotiable"),
                 ("200+", "Reviews needed to hold top-3 local pack in major metropolitan criminal defence markets")],
        body_html=A5_BODY,
        faq_pairs=A5_FAQ,
        cta_h2="Dominate the Local Pack for Criminal Defence",
        cta_p="LexScale.ai builds GBP and local SEO systems for criminal defence firms — designed to capture high-urgency searches and convert them to consultations around the clock.",
        sidebar_stat_num="60–80%",
        sidebar_stat_lbl="Of criminal defence Google Maps searchers call a firm within minutes of viewing the local pack",
        sidebar_cta_h="Get a Criminal Defence GBP Audit",
        sidebar_cta_p="Find out if your GBP is capturing the high-urgency criminal defence searches in your market.",
        related_links=[
            ("GBP for Personal Injury Law Firms", "/insights/google-business-profile/gbp-personal-injury-law-firms"),
            ("Complete GBP Guide", "/insights/google-business-profile/google-business-profile-complete-guide-law-firms"),
            ("GBP Reviews for Law Firms", "/insights/google-business-profile/gbp-reviews-for-law-firms"),
        ],
    ),
]

# ══════════════════════════════════════════════════════════════════════════════
# Generate all articles
# ══════════════════════════════════════════════════════════════════════════════

for art in ARTICLES:
    page = build_page(**art)
    slug = art["slug"]
    fname = f"{slug}.html"
    fpath = os.path.join(OUT_DIR, fname)

    issues = validate_page(page, fname)
    assert not issues, f"SEO issues in {fname}:\n" + "\n".join(issues)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(page)

    size_kb = os.path.getsize(fpath) / 1024
    add_to_sitemap(f"insights/google-business-profile/{slug}", priority="0.7", changefreq="monthly")
    print(f"✓ {fname}  {size_kb:.1f} KB")

print("\nAll 5 articles written successfully.")
