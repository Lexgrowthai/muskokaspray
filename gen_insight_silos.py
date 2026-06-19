#!/usr/bin/env python3
"""Generate insight silo hub + article pages for LexScale.ai and update nav dropdowns."""
import os, re, json, glob

DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Shared nav dropdown (8 categories)
# ---------------------------------------------------------------------------
NAV_DROPDOWN = '''<div class="dropdown">
  <a href="chatgpt.html" class="drop-item">
    <div class="drop-ico">🤖</div>
    <div><div class="drop-label">ChatGPT for Law Firms</div><div class="drop-sub">10 articles</div></div>
  </a>
  <a href="google-gemini.html" class="drop-item">
    <div class="drop-ico">✨</div>
    <div><div class="drop-label">Google Gemini for Law Firms</div><div class="drop-sub">5 articles</div></div>
  </a>
  <a href="perplexity.html" class="drop-item">
    <div class="drop-ico">🔍</div>
    <div><div class="drop-label">Perplexity for Law Firms</div><div class="drop-sub">5 articles</div></div>
  </a>
  <a href="ai-seo.html" class="drop-item">
    <div class="drop-ico">📈</div>
    <div><div class="drop-label">AI SEO for Law Firms</div><div class="drop-sub">5 articles</div></div>
  </a>
  <a href="ai-receptionists.html" class="drop-item">
    <div class="drop-ico">📞</div>
    <div><div class="drop-label">AI Receptionists for Law Firms</div><div class="drop-sub">5 articles</div></div>
  </a>
  <a href="ai-chatbots.html" class="drop-item">
    <div class="drop-ico">💬</div>
    <div><div class="drop-label">AI Chatbots for Law Firms</div><div class="drop-sub">5 articles</div></div>
  </a>
  <a href="entity-seo.html" class="drop-item">
    <div class="drop-ico">🗂️</div>
    <div><div class="drop-label">Entity SEO &amp; Structured Data</div><div class="drop-sub">5 articles</div></div>
  </a>
  <a href="ai-websites.html" class="drop-item">
    <div class="drop-ico">🌐</div>
    <div><div class="drop-label">AI Websites for Law Firms</div><div class="drop-sub">5 articles</div></div>
  </a>
</div>'''

# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------
HUB_CSS = '''*{margin:0;padding:0;box-sizing:border-box;}
:root{--navy:#0B1536;--pu:#6A5CFF;--pu2:#8B7FFF;--pu3:#a89fff;--gold:#D4AF37;--gold2:#F0C040;--gold3:#b8962e;}
body{font-family:'Inter',sans-serif;background:#fff;color:#0B1536;overflow-x:hidden;}
a{text-decoration:none;}
nav{position:sticky;top:0;z-index:100;display:flex;align-items:center;justify-content:space-between;padding:16px 40px;background:rgba(255,255,255,.9);backdrop-filter:blur(16px);border-bottom:1px solid rgba(106,92,255,.09);}
.logo{font-size:19px;font-weight:800;color:var(--navy);letter-spacing:-.4px;}
.logo span{color:var(--pu);}
.nav-links{display:flex;gap:26px;list-style:none;align-items:center;}
.nav-links a{font-size:13px;color:#4a5568;font-weight:500;transition:color .2s;}
.nav-links a:hover{color:var(--pu);}
.has-drop{position:relative;}
.has-drop>a{display:flex;align-items:center;gap:4px;cursor:pointer;}
.drop-arrow{width:14px;height:14px;opacity:.5;transition:transform .2s;}
.has-drop:hover .drop-arrow{transform:rotate(180deg);}
.dropdown{position:absolute;top:100%;left:50%;transform:translateX(-50%);background:#fff;border:1px solid rgba(106,92,255,.12);border-radius:16px;padding:12px 8px 8px;box-shadow:0 16px 48px rgba(11,21,54,.12);min-width:280px;opacity:0;pointer-events:none;visibility:hidden;transition:opacity .2s,visibility .2s;z-index:200;}
.has-drop:hover .dropdown{opacity:1;pointer-events:all;visibility:visible;}
.drop-item{display:flex;align-items:center;gap:10px;padding:10px 14px;border-radius:10px;transition:background .15s;cursor:pointer;}
.drop-item:hover{background:rgba(106,92,255,.07);}
.drop-ico{width:30px;height:30px;border-radius:8px;background:rgba(106,92,255,.1);display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:15px;}
.drop-label{font-size:12.5px;font-weight:600;color:var(--navy);}
.drop-sub{font-size:11px;color:#94a3b8;margin-top:1px;}
.drop-divider{height:1px;background:rgba(106,92,255,.07);margin:6px 8px;}
.nav-cta{background:var(--pu);color:#fff;border:none;padding:9px 20px;border-radius:100px;font-size:13px;font-weight:600;cursor:pointer;font-family:inherit;transition:all .2s;}
.nav-cta:hover{background:#5848e8;transform:translateY(-1px);}
.hub-hero{background:linear-gradient(160deg,#060d24 0%,#0B1536 55%,#111d45 100%);padding:72px 40px 64px;text-align:center;position:relative;overflow:hidden;}
.hub-hero .grid-bg{position:absolute;inset:0;background-image:linear-gradient(rgba(106,92,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(106,92,255,.05) 1px,transparent 1px);background-size:52px 52px;pointer-events:none;}
.hub-hero-inner{max-width:760px;margin:0 auto;position:relative;z-index:2;}
.hub-tag{display:inline-flex;align-items:center;gap:7px;background:rgba(106,92,255,.12);border:1px solid rgba(106,92,255,.3);border-radius:100px;padding:6px 16px;margin-bottom:20px;}
.hub-tag span{font-size:11px;font-weight:700;color:var(--pu3);letter-spacing:.8px;text-transform:uppercase;}
.hub-h1{font-size:clamp(30px,4vw,52px);font-weight:900;color:#fff;letter-spacing:-1.5px;line-height:1.08;margin-bottom:18px;}
.hub-h1 .accent{background:linear-gradient(135deg,var(--pu2),var(--pu3));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.hub-desc{font-size:17px;color:rgba(255,255,255,.55);line-height:1.7;margin-bottom:32px;max-width:560px;margin-left:auto;margin-right:auto;}
.hub-btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;}
.btn-primary{display:inline-block;background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;padding:14px 30px;border-radius:100px;font-size:15px;font-weight:700;box-shadow:0 4px 20px rgba(106,92,255,.4);transition:all .25s;}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 10px 32px rgba(106,92,255,.55);}
.btn-outline{display:inline-block;border:1.5px solid rgba(255,255,255,.2);color:rgba(255,255,255,.8);padding:14px 30px;border-radius:100px;font-size:15px;font-weight:600;transition:all .25s;}
.btn-outline:hover{border-color:rgba(106,92,255,.6);color:#fff;}
.stats-bar{background:#f8f7ff;border-bottom:1px solid rgba(106,92,255,.08);padding:20px 40px;}
.stats-inner{max-width:1100px;margin:0 auto;display:flex;justify-content:center;gap:60px;flex-wrap:wrap;}
.stat-item{text-align:center;}
.stat-num{font-size:24px;font-weight:900;color:var(--pu);letter-spacing:-.8px;}
.stat-lbl{font-size:11px;color:#94a3b8;font-weight:500;margin-top:2px;}
.articles-section{padding:72px 40px;background:#fff;}
.articles-inner{max-width:1160px;margin:0 auto;}
.section-header{margin-bottom:48px;}
.section-header h2{font-size:clamp(24px,2.8vw,36px);font-weight:900;color:var(--navy);letter-spacing:-1px;margin-bottom:10px;}
.section-header p{font-size:16px;color:#64748b;line-height:1.65;}
.articles-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;}
.art-card{background:#fff;border:1px solid rgba(106,92,255,.1);border-radius:20px;overflow:hidden;transition:all .3s cubic-bezier(.34,1.1,.64,1);display:flex;flex-direction:column;}
.art-card:hover{transform:translateY(-6px);border-color:rgba(106,92,255,.3);box-shadow:0 20px 56px rgba(106,92,255,.12);}
.art-card-top{padding:28px 28px 0;}
.art-cat-badge{display:inline-flex;align-items:center;gap:6px;background:rgba(106,92,255,.07);border:1px solid rgba(106,92,255,.15);border-radius:100px;padding:4px 12px;margin-bottom:16px;}
.art-cat-badge span{font-size:10px;font-weight:700;color:var(--pu);letter-spacing:.6px;text-transform:uppercase;}
.art-title{font-size:17px;font-weight:800;color:var(--navy);letter-spacing:-.4px;line-height:1.3;margin-bottom:10px;}
.art-desc{font-size:13px;color:#64748b;line-height:1.65;margin-bottom:20px;}
.art-meta{display:flex;align-items:center;gap:14px;font-size:11px;color:#94a3b8;font-weight:500;padding:0 28px 20px;}
.art-meta-dot{width:3px;height:3px;border-radius:50%;background:#cbd5e1;}
.art-card-footer{margin-top:auto;padding:0 28px 24px;}
.art-divider{height:1px;background:rgba(106,92,255,.07);margin-bottom:18px;}
.art-read-link{display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:700;color:var(--pu);transition:gap .2s;}
.art-read-link:hover{gap:12px;}
.art-card.featured{grid-column:1/-1;flex-direction:row;}
.art-card.featured .art-card-top{flex:1;padding:36px 0 36px 36px;}
.art-card.featured .art-card-footer{padding:0 36px 36px 36px;margin-top:0;display:flex;align-items:flex-end;}
.art-card.featured .art-divider{display:none;}
.art-card.featured .art-right{width:280px;flex-shrink:0;background:linear-gradient(135deg,rgba(106,92,255,.08),rgba(106,92,255,.03));display:flex;align-items:center;justify-content:center;border-left:1px solid rgba(106,92,255,.08);font-size:48px;}
.art-card.featured .art-title{font-size:22px;}
.art-card.featured .art-desc{font-size:14px;max-width:520px;}
.cta-banner{background:linear-gradient(135deg,var(--navy) 0%,#1a2456 100%);padding:72px 40px;text-align:center;position:relative;overflow:hidden;}
.cta-banner .grid-bg{position:absolute;inset:0;background-image:linear-gradient(rgba(106,92,255,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(106,92,255,.06) 1px,transparent 1px);background-size:52px 52px;pointer-events:none;}
.cta-inner{max-width:640px;margin:0 auto;position:relative;z-index:2;}
.cta-inner h2{font-size:clamp(26px,3vw,38px);font-weight:900;color:#fff;letter-spacing:-1px;margin-bottom:14px;}
.cta-inner p{font-size:16px;color:rgba(255,255,255,.55);line-height:1.7;margin-bottom:32px;}
footer{background:#040c1e;padding:36px 40px;}
.footer-inner{max-width:1100px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:18px;}
.footer-logo{font-size:17px;font-weight:800;color:#fff;letter-spacing:-.4px;}
.footer-logo span{color:var(--pu);}
.footer-tagline{font-size:11px;color:rgba(255,255,255,.22);margin-top:3px;}
.footer-links{display:flex;gap:24px;flex-wrap:wrap;}
.footer-links a{font-size:12px;color:rgba(255,255,255,.28);font-weight:500;transition:color .2s;}
.footer-links a:hover{color:var(--pu3);}
.footer-copy{font-size:11px;color:rgba(255,255,255,.16);}
@media(max-width:900px){
  nav{padding:14px 20px;}
  .hub-hero{padding:52px 20px 48px;}
  .stats-bar{padding:20px;}
  .stats-inner{gap:30px;}
  .articles-section{padding:48px 20px;}
  .articles-grid{grid-template-columns:1fr;}
  .art-card.featured{flex-direction:column;}
  .art-card.featured .art-card-top{padding:28px 24px 0;}
  .art-card.featured .art-card-footer{padding:0 24px 24px;margin-top:auto;}
  .art-card.featured .art-right{display:none;}
  .cta-banner{padding:52px 20px;}
  footer{padding:28px 20px;}
  .footer-inner{flex-direction:column;gap:14px;}
  .nav-links{display:none;}
}'''

ART_CSS = '''*{margin:0;padding:0;box-sizing:border-box;}
:root{--navy:#0B1536;--pu:#6A5CFF;--pu2:#8B7FFF;--pu3:#a89fff;--gold:#D4AF37;--gold2:#F0C040;--gold3:#b8962e;}
body{font-family:'Inter',sans-serif;background:#fff;color:#0B1536;overflow-x:hidden;}
a{text-decoration:none;}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1);}50%{opacity:.6;transform:scale(1.3);}}
@keyframes fadeUp{from{opacity:0;transform:translateY(24px);}to{opacity:1;transform:translateY(0);}}
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
.dropdown{position:absolute;top:100%;left:50%;transform:translateX(-50%);background:#fff;border:1px solid rgba(106,92,255,.12);border-radius:16px;padding:12px 8px 8px;box-shadow:0 16px 48px rgba(11,21,54,.12);min-width:280px;opacity:0;pointer-events:none;visibility:hidden;transition:opacity .2s,visibility .2s;z-index:200;}
.has-drop:hover .dropdown{opacity:1;pointer-events:all;visibility:visible;}
.drop-item{display:flex;align-items:center;gap:10px;padding:10px 14px;border-radius:10px;transition:background .15s;}
.drop-item:hover{background:rgba(106,92,255,.07);}
.drop-ico{width:30px;height:30px;border-radius:8px;background:rgba(106,92,255,.1);display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:15px;}
.drop-label{font-size:12.5px;font-weight:600;color:var(--navy);}
.drop-sub{font-size:11px;color:#94a3b8;margin-top:1px;}
.drop-divider{height:1px;background:rgba(106,92,255,.07);margin:6px 8px;}
.nav-cta{background:var(--pu);color:#fff;border:none;padding:9px 20px;border-radius:100px;font-size:13px;font-weight:600;cursor:pointer;font-family:inherit;transition:all .2s;}
.nav-cta:hover{background:#5848e8;transform:translateY(-1px);}
.art-hero{background:linear-gradient(150deg,#04070f 0%,#060c1c 50%,#0B1536 100%);padding:80px 40px 70px;}
.art-hero-inner{max-width:860px;margin:0 auto;text-align:center;}
.art-cat{display:inline-flex;align-items:center;gap:8px;background:rgba(106,92,255,.12);border:1px solid rgba(106,92,255,.25);border-radius:100px;padding:7px 16px;margin-bottom:24px;}
.art-cat-dot{width:6px;height:6px;border-radius:50%;background:var(--pu3);animation:pulse 2s infinite;}
.art-cat-txt{font-size:11px;font-weight:700;color:var(--pu3);letter-spacing:.8px;text-transform:uppercase;}
.art-h1{font-size:clamp(28px,4vw,52px);font-weight:900;color:#fff;line-height:1.1;letter-spacing:-1.8px;margin-bottom:20px;}
.art-h1 .gold-grad{background:linear-gradient(135deg,var(--gold3),var(--gold2),#ffe680);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.art-deck{font-size:clamp(14px,1.6vw,17px);color:rgba(255,255,255,.6);line-height:1.8;max-width:680px;margin:0 auto 32px;}
.art-meta{display:flex;align-items:center;justify-content:center;gap:20px;flex-wrap:wrap;}
.art-meta-item{display:flex;align-items:center;gap:6px;font-size:12px;color:rgba(255,255,255,.35);font-weight:500;}
.content-wrap{max-width:1100px;margin:0 auto;padding:64px 40px;display:grid;grid-template-columns:1fr 320px;gap:56px;align-items:start;}
.article-body{min-width:0;}
.sidebar{position:sticky;top:90px;}
.art-section{margin-bottom:56px;}
.art-h2{font-size:clamp(22px,2.5vw,30px);font-weight:800;color:var(--navy);letter-spacing:-.7px;line-height:1.2;margin-bottom:16px;}
.art-h2.with-bar{padding-left:18px;border-left:3px solid var(--pu);}
.art-h3{font-size:18px;font-weight:700;color:var(--navy);letter-spacing:-.3px;margin:28px 0 10px;}
.art-p{font-size:15.5px;color:#374151;line-height:1.85;margin-bottom:18px;}
.art-p:last-child{margin-bottom:0;}
.art-ul{margin:16px 0 20px 0;display:flex;flex-direction:column;gap:10px;}
.art-li{display:flex;align-items:flex-start;gap:12px;font-size:15px;color:#374151;line-height:1.65;}
.art-li::before{content:'';width:7px;height:7px;border-radius:50%;background:var(--pu);flex-shrink:0;margin-top:8px;}
.callout{border-radius:16px;padding:24px 28px;margin:28px 0;}
.callout.blue{background:rgba(106,92,255,.06);border:1px solid rgba(106,92,255,.18);}
.callout.gold{background:rgba(212,175,55,.06);border:1px solid rgba(212,175,55,.2);}
.callout.dark{background:linear-gradient(135deg,#060d1e,#0B1536);border:1px solid rgba(106,92,255,.2);}
.callout-label{font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;}
.callout.blue .callout-label{color:var(--pu);}
.callout.gold .callout-label{color:var(--gold3);}
.callout.dark .callout-label{color:var(--pu3);}
.callout-text{font-size:15px;line-height:1.75;}
.callout.blue .callout-text{color:#374151;}
.callout.gold .callout-text{color:#374151;}
.callout.dark .callout-text{color:rgba(255,255,255,.75);}
.faq-list{display:flex;flex-direction:column;gap:0;}
.faq-item{border-bottom:1px solid rgba(106,92,255,.08);}
.faq-q{display:flex;align-items:center;justify-content:space-between;padding:20px 0;cursor:pointer;gap:16px;}
.faq-q-text{font-size:15px;font-weight:700;color:var(--navy);line-height:1.4;}
.faq-icon{width:28px;height:28px;border-radius:50%;background:rgba(106,92,255,.08);display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:all .3s;}
.faq-item.open .faq-icon{background:var(--pu);transform:rotate(45deg);}
.faq-icon svg{transition:stroke .3s;}
.faq-item.open .faq-icon svg{stroke:#fff;}
.faq-a{max-height:0;overflow:hidden;transition:max-height .4s cubic-bezier(.4,0,.2,1);}
.faq-a-inner{padding:0 0 20px;}
.faq-a-text{font-size:14.5px;color:#64748b;line-height:1.8;}
.sidebar-card{background:#fff;border:1px solid rgba(106,92,255,.1);border-radius:20px;padding:24px;margin-bottom:20px;box-shadow:0 4px 20px rgba(11,21,54,.05);}
.sidebar-card.dark{background:linear-gradient(135deg,var(--navy),#162050);border-color:rgba(106,92,255,.2);}
.sidebar-card.gold-card{background:linear-gradient(135deg,rgba(212,175,55,.08),rgba(212,175,55,.04));border:1px solid rgba(212,175,55,.2);}
.sb-h{font-size:15px;font-weight:800;color:var(--navy);margin-bottom:14px;}
.sb-h.light{color:#fff;}
.sb-h.gold{color:var(--gold3);}
.toc-item{display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid rgba(106,92,255,.06);cursor:pointer;transition:color .2s;}
.toc-item:last-child{border-bottom:none;}
.toc-item:hover .toc-text{color:var(--pu);}
.toc-num{font-size:10px;font-weight:800;color:var(--pu);width:20px;flex-shrink:0;}
.toc-text{font-size:13px;color:#374151;font-weight:500;line-height:1.35;}
.sb-cta-btn{display:block;background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;text-align:center;padding:13px;border-radius:12px;font-size:14px;font-weight:700;transition:all .25s;margin-top:14px;}
.sb-cta-btn:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(106,92,255,.35);}
.sb-cta-btn.gold-btn{background:linear-gradient(135deg,var(--gold3),var(--gold2));color:var(--navy);}
.related-item{display:flex;align-items:flex-start;gap:10px;padding:10px 0;border-bottom:1px solid rgba(106,92,255,.07);}
.related-item:last-child{border-bottom:none;}
.related-ico{width:34px;height:34px;border-radius:10px;background:rgba(106,92,255,.08);display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:16px;}
.related-text{font-size:13px;font-weight:600;color:var(--navy);line-height:1.4;}
.related-text:hover{color:var(--pu);}
.cta-banner{background:linear-gradient(135deg,var(--navy) 0%,#162050 100%);border:1px solid rgba(106,92,255,.2);border-radius:24px;padding:44px;text-align:center;margin:56px 0 0;}
.cb-h{font-size:clamp(22px,2.5vw,30px);font-weight:900;color:#fff;letter-spacing:-.8px;margin-bottom:12px;}
.cb-p{font-size:15px;color:rgba(255,255,255,.55);line-height:1.7;margin-bottom:28px;}
.cb-btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;}
.btn-g{display:inline-flex;align-items:center;gap:7px;background:linear-gradient(135deg,var(--gold3),var(--gold2));color:var(--navy);border:none;padding:13px 26px;border-radius:100px;font-size:14px;font-weight:700;cursor:pointer;font-family:inherit;box-shadow:0 4px 16px rgba(212,175,55,.3);transition:all .25s;text-decoration:none;}
.btn-g:hover{transform:translateY(-2px);box-shadow:0 10px 28px rgba(212,175,55,.45);}
.btn-out{display:inline-flex;align-items:center;gap:7px;background:transparent;color:rgba(255,255,255,.7);border:1.5px solid rgba(255,255,255,.2);padding:13px 26px;border-radius:100px;font-size:14px;font-weight:600;cursor:pointer;font-family:inherit;transition:all .25s;text-decoration:none;}
.btn-out:hover{border-color:rgba(255,255,255,.5);color:#fff;}
footer{background:#04070f;border-top:1px solid rgba(255,255,255,.05);padding:36px 40px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;}
.foot-logo{font-size:17px;font-weight:800;color:#fff;letter-spacing:-.3px;}
.foot-logo span{color:var(--pu);}
.foot-links{display:flex;gap:24px;flex-wrap:wrap;}
.foot-links a{font-size:13px;color:rgba(255,255,255,.3);font-weight:500;transition:color .2s;}
.foot-links a:hover{color:rgba(255,255,255,.7);}
.foot-copy{font-size:12px;color:rgba(255,255,255,.18);}
#sticky-cta{position:fixed;bottom:0;left:0;right:0;z-index:999;background:linear-gradient(90deg,#040c1e,#0B1536);border-top:1px solid rgba(106,92,255,.2);padding:14px 32px;display:flex;align-items:center;justify-content:space-between;gap:16px;transform:translateY(100%);transition:transform .4s cubic-bezier(.34,1,.64,1);}
.sc-left{display:flex;align-items:center;gap:14px;}
.sc-text{font-size:14px;font-weight:600;color:rgba(255,255,255,.75);}
.sc-text strong{color:#fff;}
.sc-right{display:flex;align-items:center;gap:10px;}
.sc-dismiss{background:none;border:none;color:rgba(255,255,255,.3);font-size:20px;cursor:pointer;padding:4px 8px;line-height:1;}
.sc-dismiss:hover{color:rgba(255,255,255,.7);}
@media(max-width:960px){
  .content-wrap{grid-template-columns:1fr;gap:40px;}
  .sidebar{position:static;}
  nav{padding:14px 20px;}
  .nav-links{display:none;}
  .art-hero{padding:60px 24px 50px;}
  #sticky-cta{flex-direction:column;text-align:center;gap:10px;padding:16px 20px;}
}
@media(max-width:600px){
  .content-wrap{padding:40px 20px;}
  footer{padding:28px 20px;flex-direction:column;align-items:flex-start;}
}'''


def nav_html(active=False):
    insights_attr = ' style="color:#6A5CFF;font-weight:700;"' if active else ''
    return f'''<nav>
  <a href="index.html" class="logo">Lex<span>Scale</span>.ai</a>
  <ul class="nav-links">
    <li><a href="index.html">Home</a></li>
    <li class="has-drop">
      <a href="#">Services
        <svg class="drop-arrow" viewBox="0 0 14 14" fill="none"><path d="M3 5l4 4 4-4" stroke="#4a5568" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
      <div class="dropdown">
        <a href="ai-website-design-for-law-firms.html" class="drop-item"><div class="drop-ico">🌐</div><div><div class="drop-label">AI Website Design</div><div class="drop-sub">High-converting law firm sites</div></div></a>
        <a href="ai-seo-for-law-firms.html" class="drop-item"><div class="drop-ico">🔎</div><div><div class="drop-label">AI SEO</div><div class="drop-sub">Rank on Google &amp; AI platforms</div></div></a>
        <a href="ai-receptionist-for-law-firms.html" class="drop-item"><div class="drop-ico">📞</div><div><div class="drop-label">AI Receptionist</div><div class="drop-sub">Never miss a client call</div></div></a>
        <a href="ai-chatbot-for-law-firms.html" class="drop-item"><div class="drop-ico">💬</div><div><div class="drop-label">AI Chatbot</div><div class="drop-sub">Convert visitors into clients</div></div></a>
      </div>
    </li>
    <li><a href="about.html">About</a></li>
    <li class="has-drop">
      <a href="#"{insights_attr}>Insights
        <svg class="drop-arrow" viewBox="0 0 14 14" fill="none"><path d="M3 5l4 4 4-4" stroke="#4a5568" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
      {NAV_DROPDOWN}
    </li>
    <li><a href="index.html#contact">Contact</a></li>
  </ul>
  <button class="nav-cta" onclick="openForm()">Get a Free Strategy Call</button>
</nav>'''


FOOTER = '''<footer>
  <div class="foot-logo">Lex<span>Scale</span>.ai</div>
  <div class="foot-links">
    <a href="index.html">Home</a>
    <a href="about.html">About</a>
    <a href="ai-website-design-for-law-firms.html">AI Website Design</a>
    <a href="ai-seo-for-law-firms.html">AI SEO</a>
    <a href="ai-receptionist-for-law-firms.html">AI Receptionist</a>
    <a href="ai-chatbot-for-law-firms.html">AI Chatbot</a>
    <a href="chatgpt.html">Insights</a>
    <a href="index.html#contact">Contact</a>
  </div>
  <div class="foot-copy">© 2025 LexScale.ai · All rights reserved</div>
</footer>'''

STICKY_AND_MODAL = '''<div id="sticky-cta">
  <div class="sc-left">
    <div style="width:36px;height:36px;border-radius:50%;background:rgba(212,175,55,.15);border:1px solid rgba(212,175,55,.3);display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:16px;">🔎</div>
    <span class="sc-text"><strong>Is Your Firm Visible in AI Search?</strong> Find out where you stand — free AI visibility audit.</span>
  </div>
  <div class="sc-right">
    <button onclick="openForm()" style="background:linear-gradient(135deg,var(--gold3),var(--gold2));color:var(--navy);border:none;padding:10px 22px;border-radius:100px;font-size:13px;font-weight:700;cursor:pointer;font-family:inherit;white-space:nowrap;">Get Free AI Audit →</button>
    <button class="sc-dismiss" onclick="document.getElementById('sticky-cta').style.transform='translateY(100%)'">×</button>
  </div>
</div>
<div id="form-overlay" onclick="if(event.target===this)closeForm()" style="position:fixed;inset:0;background:rgba(6,9,15,.75);backdrop-filter:blur(8px);z-index:1000;display:none;align-items:center;justify-content:center;padding:20px;">
  <div style="background:#fff;border-radius:24px;padding:40px;max-width:500px;width:100%;position:relative;box-shadow:0 24px 80px rgba(0,0,0,.3);max-height:90vh;overflow-y:auto;">
    <button onclick="closeForm()" style="position:absolute;top:18px;right:18px;background:rgba(11,21,54,.06);border:none;width:34px;height:34px;border-radius:50%;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;color:#64748b;">×</button>
    <div style="display:inline-flex;align-items:center;gap:6px;background:rgba(212,175,55,.08);border:1px solid rgba(212,175,55,.2);border-radius:100px;padding:5px 12px;margin-bottom:16px;">
      <span style="font-size:10px;font-weight:700;color:var(--gold3);text-transform:uppercase;letter-spacing:.8px;">Free AI Visibility Audit</span>
    </div>
    <h3 style="font-size:22px;font-weight:800;color:var(--navy);letter-spacing:-.5px;margin-bottom:8px;">See How Your Firm Ranks in AI Search</h3>
    <p style="font-size:14px;color:#64748b;margin-bottom:24px;line-height:1.6;">We'll run a full AI visibility audit across ChatGPT, Perplexity, and Google AI — and show you exactly where your firm stands.</p>
    <form onsubmit="submitForm(event)" style="display:flex;flex-direction:column;gap:14px;">
      <input required type="text" placeholder="Your Name" style="width:100%;border:1.5px solid rgba(106,92,255,.15);border-radius:10px;padding:12px 14px;font-size:14px;font-family:inherit;color:var(--navy);outline:none;box-sizing:border-box;"/>
      <input required type="text" placeholder="Firm Name" style="width:100%;border:1.5px solid rgba(106,92,255,.15);border-radius:10px;padding:12px 14px;font-size:14px;font-family:inherit;color:var(--navy);outline:none;box-sizing:border-box;"/>
      <input required type="tel" placeholder="Phone Number" style="width:100%;border:1.5px solid rgba(106,92,255,.15);border-radius:10px;padding:12px 14px;font-size:14px;font-family:inherit;color:var(--navy);outline:none;box-sizing:border-box;"/>
      <input type="url" placeholder="https://yourfirm.com" style="width:100%;border:1.5px solid rgba(106,92,255,.15);border-radius:10px;padding:12px 14px;font-size:14px;font-family:inherit;color:var(--navy);outline:none;box-sizing:border-box;"/>
      <button type="submit" style="background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;border:none;padding:15px;border-radius:12px;font-size:15px;font-weight:700;cursor:pointer;font-family:inherit;margin-top:4px;box-shadow:0 4px 20px rgba(106,92,255,.3);">Run My Free AI Audit →</button>
    </form>
    <div id="form-success" style="display:none;text-align:center;padding:20px 0;">
      <div style="font-size:40px;margin-bottom:12px;">✅</div>
      <h4 style="font-size:20px;font-weight:800;color:var(--navy);margin-bottom:8px;">Audit Request Received!</h4>
      <p style="font-size:14px;color:#64748b;line-height:1.6;">We'll have your AI visibility audit ready within one business day.</p>
    </div>
  </div>
</div>
<script>
(function(){var s=false;window.addEventListener('scroll',function(){if(!s&&window.scrollY>400){s=true;document.getElementById('sticky-cta').style.transform='translateY(0)';}});})();
function toggleFaq(el){var item=el.parentElement;var ans=item.querySelector('.faq-a');var isOpen=item.classList.contains('open');document.querySelectorAll('.faq-item.open').forEach(function(i){i.classList.remove('open');i.querySelector('.faq-a').style.maxHeight='0';});if(!isOpen){item.classList.add('open');ans.style.maxHeight='600px';}}
function openForm(){document.getElementById('form-overlay').style.display='flex';document.body.style.overflow='hidden';}
function closeForm(){document.getElementById('form-overlay').style.display='none';document.body.style.overflow='';}
function submitForm(e){e.preventDefault();document.querySelector('#form-overlay form').style.display='none';document.getElementById('form-success').style.display='block';}
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeForm();});
</script>'''


def build_hub_page(category_slug, title, description, accent_label, icon, articles, stats):
    url = f"https://lexscale.ai/{category_slug}.html"
    schema = {
        "@context": "https://schema.org", "@type": "CollectionPage",
        "name": title, "description": description, "url": url,
        "publisher": {"@type": "Organization", "name": "LexScale.ai", "url": "https://lexscale.ai"},
    }
    cards = []
    for i, a in enumerate(articles):
        if i == 0:
            cards.append(f'''<a href="{a['slug']}.html" class="art-card featured">
  <div class="art-card-top">
    <div class="art-cat-badge"><span>{accent_label}</span></div>
    <div class="art-title">{a['title']}</div>
    <div class="art-desc">{a['desc']}</div>
  </div>
  <div class="art-meta"><span>{a['date']}</span><span class="art-meta-dot"></span><span>{a['read']}</span></div>
  <div class="art-card-footer">
    <div class="art-divider"></div>
    <span class="art-read-link">Read Article <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></span>
  </div>
  <div class="art-right">{icon}</div>
</a>''')
        else:
            cards.append(f'''<a href="{a['slug']}.html" class="art-card">
  <div class="art-card-top">
    <div class="art-cat-badge"><span>{accent_label}</span></div>
    <div class="art-title">{a['title']}</div>
    <div class="art-desc">{a['desc']}</div>
  </div>
  <div class="art-meta"><span>{a['date']}</span><span class="art-meta-dot"></span><span>{a['read']}</span></div>
  <div class="art-card-footer">
    <div class="art-divider"></div>
    <span class="art-read-link">Read Article <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></span>
  </div>
</a>''')
    stat_html = "".join(
        f'<div class="stat-item"><div class="stat-num">{s[0]}</div><div class="stat-lbl">{s[1]}</div></div>'
        for s in stats)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{title} | LexScale.ai</title>
<meta name="description" content="{description}"/>
<link rel="canonical" href="{url}"/>
<meta property="og:title" content="{title} | LexScale.ai"/>
<meta property="og:description" content="{description}"/>
<meta property="og:url" content="{url}"/>
<meta property="og:type" content="website"/>
<meta name="twitter:card" content="summary_large_image"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<script type="application/ld+json">{json.dumps(schema, indent=2)}</script>
<style>
{HUB_CSS}
</style>
</head>
<body>
{nav_html(active=True)}
<section class="hub-hero">
  <div class="grid-bg"></div>
  <div class="hub-hero-inner">
    <div class="hub-tag"><span>{accent_label}</span></div>
    <h1 class="hub-h1">{title.split(' for Law')[0]} <span class="accent">for Law Firms</span></h1>
    <p class="hub-desc">{description}</p>
    <div class="hub-btns">
      <a href="index.html#contact" class="btn-primary">Get AI Visible Now →</a>
      <a href="index.html" class="btn-outline">View All Services</a>
    </div>
  </div>
</section>
<div class="stats-bar"><div class="stats-inner">{stat_html}</div></div>
<section class="articles-section">
  <div class="articles-inner">
    <div class="section-header">
      <h2>All {accent_label} Articles</h2>
      <p>In-depth guides to help your law firm get found, get cited, and win more clients in the age of AI search.</p>
    </div>
    <div class="articles-grid">
      {''.join(cards)}
    </div>
  </div>
</section>
<section class="cta-banner">
  <div class="grid-bg"></div>
  <div class="cta-inner">
    <h2>Is Your Firm Visible in AI Search?</h2>
    <p>Get a free AI Visibility Report and see exactly where your law firm stands — and what it takes to get recommended.</p>
    <button class="btn-primary" onclick="document.getElementById('form-overlay').style.display='flex'" style="border:none;cursor:pointer;font-family:inherit;">Get My Free Report →</button>
  </div>
</section>
{FOOTER}
{STICKY_AND_MODAL}
</body>
</html>'''


def build_article_page(slug, title, description, deck, category_hub, category_name,
                       sections, faqs, related):
    url = f"https://lexscale.ai/{slug}.html"
    article_schema = {
        "@context": "https://schema.org", "@type": "Article", "headline": title,
        "description": description, "author": {"@type": "Organization", "name": "LexScale.ai"},
        "publisher": {"@type": "Organization", "name": "LexScale.ai", "url": "https://lexscale.ai"},
        "datePublished": "2025-06-18", "mainEntityOfPage": url,
    }
    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

    sec_html = []
    toc = []
    for i, (heading, blocks) in enumerate(sections, 1):
        body = "".join(blocks)
        sec_html.append(f'''<div class="art-section" id="s{i}">
      <h2 class="art-h2 with-bar">{heading}</h2>
      {body}
    </div>''')
        short = heading if len(heading) < 40 else heading[:37] + "…"
        toc.append(f'<a href="#s{i}" class="toc-item"><span class="toc-num">{i:02d}</span><span class="toc-text">{short}</span></a>')
    n = len(sections) + 1
    toc.append(f'<a href="#s{n}" class="toc-item"><span class="toc-num">{n:02d}</span><span class="toc-text">FAQs</span></a>')
    faq_items = []
    for q, a in faqs:
        faq_items.append(f'''<div class="faq-item">
          <div class="faq-q" onclick="toggleFaq(this)">
            <span class="faq-q-text">{q}</span>
            <div class="faq-icon"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg></div>
          </div>
          <div class="faq-a"><div class="faq-a-inner"><p class="faq-a-text">{a}</p></div></div>
        </div>''')
    faq_block = f'''<div class="art-section" id="s{n}">
      <h2 class="art-h2">Frequently Asked Questions</h2>
      <div class="faq-list">
        {''.join(faq_items)}
      </div>
    </div>'''
    related_html = "".join(
        f'<a href="{href}" class="related-item"><div class="related-ico">{ico}</div><div class="related-text">{label}</div></a>'
        for href, label, ico in related)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{title} | LexScale.ai</title>
<meta name="description" content="{description}"/>
<link rel="canonical" href="{url}"/>
<meta property="og:title" content="{title} | LexScale.ai"/>
<meta property="og:description" content="{description}"/>
<meta property="og:url" content="{url}"/>
<meta property="og:type" content="article"/>
<meta name="twitter:card" content="summary_large_image"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<script type="application/ld+json">{json.dumps(article_schema, indent=2)}</script>
<script type="application/ld+json">{json.dumps(faq_schema, indent=2)}</script>
<style>
{ART_CSS}
</style>
</head>
<body>
{nav_html(active=True)}
<section class="art-hero">
  <div class="art-hero-inner" style="animation:fadeUp .8s ease both;">
    <div class="art-cat"><div class="art-cat-dot"></div><span class="art-cat-txt">{category_name} · Legal Marketing</span></div>
    <h1 class="art-h1">{title}</h1>
    <p class="art-deck">{deck}</p>
    <div class="art-meta">
      <div class="art-meta-item">8 min read</div>
      <div class="art-meta-item">Updated June 2025</div>
      <div class="art-meta-item">LexScale.ai Editorial Team</div>
    </div>
  </div>
</section>
<div class="content-wrap">
  <article class="article-body">
    {''.join(sec_html)}
    {faq_block}
    <div class="cta-banner">
      <h2 class="cb-h">Is Your Firm Visible<br>Where Clients Are Searching?</h2>
      <p class="cb-p">LexScale.ai helps law firms build the authority, content, and AI visibility needed to compete in today's search landscape — and the one that's coming next.</p>
      <div class="cb-btns">
        <a href="index.html#contact" class="btn-g">Schedule a Free Strategy Call →</a>
        <a href="{category_hub}.html" class="btn-out">More {category_name} Guides</a>
      </div>
    </div>
  </article>
  <aside class="sidebar">
    <div class="sidebar-card">
      <div class="sb-h">Table of Contents</div>
      {''.join(toc)}
    </div>
    <div class="sidebar-card gold-card">
      <div class="sb-h gold">Is Your Firm Visible in AI Search?</div>
      <p style="font-size:13px;color:#64748b;line-height:1.65;margin-bottom:16px;">Get a free AI visibility audit and see exactly where your firm stands across ChatGPT, Perplexity, and Google AI.</p>
      <a href="index.html#contact" class="sb-cta-btn gold-btn">Get My Free AI Audit →</a>
    </div>
    <div class="sidebar-card">
      <div class="sb-h">Related Reading</div>
      {related_html}
    </div>
  </aside>
</div>
{FOOTER}
{STICKY_AND_MODAL}
</body>
</html>'''


def P(*texts):
    return "".join(f'<p class="art-p">{t}</p>' for t in texts)

def UL(*items):
    lis = "".join(f'<li class="art-li">{i}</li>' for i in items)
    return f'<ul class="art-ul">{lis}</ul>'

def CALLOUT(kind, label, text):
    return f'<div class="callout {kind}"><div class="callout-label">{label}</div><div class="callout-text">{text}</div></div>'


ARTICLES = []

def add(slug, title, deck, hub, cat, sections, faqs, related, card_desc, read="8 min read"):
    ARTICLES.append(dict(slug=slug, title=title, deck=deck, hub=hub, cat=cat,
                         sections=sections, faqs=faqs, related=related,
                         card_desc=card_desc, read=read))

REL_SEO = [("ai-seo.html","AI SEO for Law Firms (Hub)","📈"),("ai-seo-for-law-firms.html","Our AI SEO Service","🔎"),("chatgpt.html","ChatGPT for Law Firms","🤖")]
REL_RECEP = [("ai-receptionists.html","AI Receptionists Hub","📞"),("ai-receptionist-for-law-firms.html","Our AI Receptionist Service","☎️"),("ai-chatbots.html","AI Chatbots for Law Firms","💬")]
REL_CHAT = [("ai-chatbots.html","AI Chatbots Hub","💬"),("ai-chatbot-for-law-firms.html","Our AI Chatbot Service","🤖"),("ai-receptionists.html","AI Receptionists for Law Firms","📞")]
REL_ENTITY = [("entity-seo.html","Entity SEO Hub","🗂️"),("ai-seo.html","AI SEO for Law Firms","📈"),("ai-seo-for-law-firms.html","Our AI SEO Service","🔎")]
REL_WEB = [("ai-websites.html","AI Websites Hub","🌐"),("ai-website-design-for-law-firms.html","Our AI Website Service","🖥️"),("ai-seo.html","AI SEO for Law Firms","📈")]


# ---- AI SEO ----
add("ai-seo-for-law-firms-complete-guide",
    "AI SEO for Law Firms: The Complete Guide",
    "Search is no longer ten blue links. This guide explains how AI SEO works, why it matters for law firms, and the exact steps to get your firm cited by AI-powered search.",
    "ai-seo", "AI SEO",
    [
      ("What AI SEO Actually Means for Law Firms",
       [P("AI SEO is the practice of optimizing a law firm's online presence so that artificial intelligence systems — ChatGPT, Google AI Overviews, Gemini, Perplexity, and Bing Copilot — recognize, trust, and recommend the firm when potential clients ask legal questions.",
          "Traditional SEO was about ranking a web page in a list of results. AI SEO is about becoming the answer. When someone asks an AI assistant who the best personal injury lawyer near them is, the firms that have built the right authority, content depth, and structured data signals are the ones that get named.",
          "For law firms, this is a fundamental shift. Clients increasingly resolve their initial legal questions inside an AI conversation before they ever click a website. If your firm is invisible at that stage, you have already lost the lead to a competitor the AI chose to mention."),
        CALLOUT("gold","Why This Matters Now","The firms investing in AI SEO today are establishing authority signals that compound over months. Just as early Google SEO created lasting advantages, early AI visibility is becoming the new moat in legal marketing.")]),
      ("How AI Systems Choose Which Firms to Recommend",
       [P("AI models do not have a single ranking algorithm the way classic search engines did. Instead, they synthesize answers from the web content they were trained on and, increasingly, from live retrieval of authoritative pages. A handful of signals consistently determine which firms surface."),
        UL("Depth and accuracy of educational content across a practice area",
           "Consistent name, address, and entity information across the web",
           "Strong reviews and reputation signals on Google and legal directories",
           "Structured data (schema) that helps machines understand the firm",
           "Authoritative backlinks and citations from trusted legal sources"),
        P("None of these is a trick. They are durable trust signals. A firm that publishes thorough answers to the questions clients actually ask, and that maintains a clean, consistent web presence, is the firm AI systems learn to rely on.")]),
      ("Building Content That AI Engines Cite",
       [P("Content remains the engine of AI SEO. But the bar has risen. Thin, keyword-stuffed pages that once ranked on Google are ignored by AI systems, which are designed to extract genuinely useful, specific information."),
        P("The winning approach is topic clusters: a pillar page covering a practice area in depth, surrounded by supporting articles that answer narrower client questions. A family law firm might publish a pillar on divorce, then supporting pieces on child custody, support calculations, property division, and separation agreements."),
        P("Each piece should answer a real question directly, in plain language, near the top of the page. AI systems favor content that gets to the point and demonstrates genuine expertise.")]),
      ("Technical Foundations: Schema, Speed, and Structure",
       [P("Great content needs a technical foundation that machines can parse. Schema markup — particularly LegalService, Attorney, and FAQPage schema — tells AI systems exactly what your firm does, where it operates, and what questions it answers."),
        P("Site speed and mobile performance matter too. AI crawlers, like search crawlers, struggle with slow, bloated pages. A fast, well-structured, mobile-first website signals professionalism and makes your content easier to ingest and cite."),
        CALLOUT("blue","Quick Win","Add FAQPage schema to every practice-area page. It maps directly to how clients phrase questions to AI assistants and increases the odds your answers are reused.")]),
      ("Reputation and Entity Signals",
       [P("AI systems lean heavily on reputation. Reviews, mentions in news and legal publications, directory listings, and a consistent brand identity all feed the model's confidence in recommending your firm."),
        P("This is why entity SEO — making your firm a recognized, well-defined entity across the web — has become inseparable from AI SEO. The clearer and more consistent your digital footprint, the more reliably AI can identify and recommend you.")]),
      ("Measuring and Sustaining AI Visibility",
       [P("AI visibility is harder to measure than keyword rankings, but it is not invisible. Track how often AI assistants mention your firm for target queries, monitor referral traffic from AI platforms, and watch branded search growth as AI exposure drives awareness."),
        P("Most importantly, treat AI SEO as an ongoing program, not a one-time project. The firms that publish consistently, maintain their reputation, and keep their technical foundation clean are the ones that stay visible as the AI search landscape evolves.")]),
    ],
    [("What is AI SEO for law firms?","AI SEO is the practice of optimizing a law firm's content, reputation, and structured data so AI systems like ChatGPT, Gemini, and Google AI Overviews recognize and recommend the firm when potential clients ask legal questions."),
     ("How is AI SEO different from traditional SEO?","Traditional SEO aims to rank a page in a list of results. AI SEO aims to make your firm the answer an AI assistant gives — which depends more on content depth, entity consistency, reputation, and structured data than on keyword placement alone."),
     ("How long does AI SEO take to work?","Most firms see meaningful improvement within 3 to 6 months of consistent content publishing, schema implementation, and reputation building. Authority signals compound over time, so early movers gain a lasting advantage."),
     ("Do I still need Google SEO if I do AI SEO?","Yes. Google and AI search are complementary. A strong, authoritative, well-structured website performs well across both, and many AI systems draw on the same authority signals Google uses."),
     ("Can a small law firm compete in AI SEO?","Absolutely. AI systems reward depth and trust, not just budget. A focused firm that publishes genuinely helpful content on its practice areas and maintains a clean, consistent web presence can outperform larger competitors.")],
    REL_SEO,
    "Search is no longer ten blue links. Learn how AI SEO works, why it matters for law firms, and the exact steps to get cited by AI search.", "10 min read")

add("ai-seo-vs-traditional-seo-lawyers",
    "AI SEO vs Traditional SEO for Lawyers",
    "Traditional SEO and AI SEO share a foundation but optimize for different outcomes. Here's how they differ — and why law firms now need both.",
    "ai-seo", "AI SEO",
    [
      ("Two Different Goals",
       [P("Traditional SEO has one core goal: rank a web page as high as possible in a list of search results so a user clicks it. AI SEO has a different goal: become the source an AI assistant uses to answer a question, ideally by name."),
        P("For lawyers, this distinction is profound. In traditional search, you compete for a click. In AI search, you compete to be the recommendation — and often there is no click at all, just a spoken or written answer that names your firm."),
        CALLOUT("blue","The Shift in a Sentence","Traditional SEO wins the click. AI SEO wins the recommendation.")]),
      ("Where the Two Overlap",
       [P("The good news for law firms is that AI SEO and traditional SEO rest on the same foundation. High-quality content, fast websites, structured data, strong reviews, and authoritative backlinks help with both."),
        UL("Educational, in-depth content benefits Google and AI alike",
           "Schema markup helps both crawlers and AI models understand your firm",
           "Google reviews feed both local rankings and AI trust signals",
           "A clean, mobile-first site improves both classic and AI performance"),
        P("This overlap means firms do not have to choose. Investing in the fundamentals strengthens visibility everywhere.")]),
      ("Where They Diverge",
       [P("The differences emerge in emphasis. Traditional SEO rewards keyword targeting, internal linking structure, and competing for specific search phrases. AI SEO rewards topical completeness, entity clarity, and content that answers full questions conversationally."),
        P("Thin pages built only to capture a keyword may still scrape by on Google but are essentially invisible to AI. Meanwhile, deep, well-organized content that fully resolves a client's question is what AI systems extract and cite.")]),
      ("Why Lawyers Need Both",
       [P("Most legal clients still begin on Google for many searches, so abandoning traditional SEO would be a mistake. But a growing share of high-intent research now happens inside AI assistants, and that share is rising fast."),
        P("Firms that ignore AI SEO risk being absent at the exact moment a stressed client is forming an opinion about who to trust. Firms that ignore traditional SEO lose the still-large audience using Google directly. The answer is an integrated strategy.")]),
      ("Practical Steps to Cover Both",
       [P("Start by auditing your existing content for depth. Expand thin pages into comprehensive resources. Add FAQ sections that mirror how clients ask AI assistants questions. Implement legal-specific schema across the site."),
        UL("Build topic clusters around each practice area",
           "Keep firm name, address, and phone consistent everywhere",
           "Earn reviews and quality citations from legal sources",
           "Ensure fast load times and flawless mobile experience"),
        CALLOUT("gold","Bottom Line","You do not replace traditional SEO with AI SEO. You extend it. The same authoritative foundation, taken deeper, wins on both fronts.")]),
    ],
    [("Is traditional SEO dead for law firms?","No. Traditional SEO still drives substantial traffic from Google. However, AI SEO is now essential as more clients research legal questions inside AI assistants. The two work together."),
     ("Which matters more, AI SEO or traditional SEO?","Both matter. Most firms should maintain traditional SEO while adding AI SEO. The underlying investments — quality content, schema, reviews, fast sites — strengthen both at once."),
     ("Does AI SEO require different content than traditional SEO?","Largely the same content, but deeper and more conversational. AI systems favor comprehensive answers to full questions, so thin keyword pages need to be expanded into genuinely helpful resources."),
     ("Will AI search reduce my website traffic?","AI answers can reduce some clicks, but being the firm an AI recommends often produces higher-intent leads. The goal shifts from maximizing clicks to maximizing qualified recommendations."),
     ("How do I start combining both approaches?","Audit your content depth, expand thin pages, add FAQ and legal schema, build topic clusters per practice area, and maintain consistent reputation and entity signals across the web.")],
    REL_SEO,
    "AI SEO and traditional SEO share a foundation but optimize for different outcomes. Here's how they differ and why lawyers now need both.")

add("how-google-ai-overviews-affect-law-firms",
    "How Google AI Overviews Affect Law Firms",
    "Google AI Overviews now answer legal questions directly at the top of search results. Here's what that means for your firm's traffic, leads, and visibility.",
    "ai-seo", "AI SEO",
    [
      ("What Google AI Overviews Are",
       [P("Google AI Overviews are AI-generated summaries that appear at the very top of many search results. Instead of showing only links, Google composes a direct answer drawn from across the web, often citing a few sources."),
        P("For legal queries — what to do after a car accident, how child custody works — these overviews increasingly resolve the user's question on the results page itself, before they scroll to traditional listings."),
        CALLOUT("blue","Why Law Firms Should Care","An AI Overview that answers the client's question can reduce clicks to your site — unless your firm is the source being cited or recommended within that overview.")]),
      ("The Impact on Click-Through and Leads",
       [P("When Google answers a question directly, some informational clicks disappear. A user who just wanted to understand the basics may never click through. This is the much-discussed zero-click effect."),
        P("But there is an upside. The users who do click after reading an overview tend to be further along and more serious. And being cited in an overview puts your firm's name in front of every searcher, building authority and brand recall even without a click.")]),
      ("How to Get Cited in AI Overviews",
       [P("Google's overviews draw from content it deems authoritative and directly responsive. To increase the odds your firm is the cited source:"),
        UL("Answer common client questions clearly and near the top of each page",
           "Use descriptive headings that match how clients phrase questions",
           "Add FAQ and legal schema so Google understands your content",
           "Demonstrate genuine expertise, experience, and trust on every page",
           "Keep information current and accurate across your practice areas"),
        P("In short, the same depth-and-trust strategy that powers broader AI SEO is exactly what earns citations in Google's overviews.")]),
      ("Local Searches and Map-Driven Results",
       [P("For many legal queries, intent is local. Google often pairs AI Overviews with local pack results. A complete, well-reviewed Google Business Profile, consistent local citations, and location-specific content strengthen your presence in both."),
        P("Firms that combine authoritative practice-area content with strong local signals are best positioned to appear when Google blends AI answers with local recommendations.")]),
      ("Turning Overviews Into an Advantage",
       [P("Rather than fearing AI Overviews, treat them as a new front-page placement. Being the cited expert in an overview is the modern equivalent of ranking number one — it signals authority to every searcher."),
        P("Focus on becoming the most thorough, trustworthy resource for the questions your ideal clients ask. That is what gets cited, and citation is the new visibility.")]),
    ],
    [("What are Google AI Overviews?","Google AI Overviews are AI-generated summaries shown at the top of search results that answer a query directly and cite supporting sources, often before the traditional list of links."),
     ("Do AI Overviews hurt law firm website traffic?","They can reduce some informational clicks, but the remaining clicks tend to be higher-intent. Being cited in an overview also builds brand authority even without a click."),
     ("How can my firm appear in an AI Overview?","Publish clear, authoritative answers to common client questions, use FAQ and legal schema, structure content with descriptive headings, and demonstrate genuine expertise and trust."),
     ("Are AI Overviews shown for legal searches?","Yes. Google frequently shows AI Overviews for informational legal queries, and increasingly pairs them with local results for queries with local intent."),
     ("Should I change my SEO strategy because of AI Overviews?","You should deepen it. The same content depth, schema, local signals, and trust signals that earn overview citations also strengthen your overall AI and traditional SEO.")],
    REL_SEO,
    "Google AI Overviews now answer legal questions at the top of results. Here's what that means for your firm's traffic, leads, and visibility.")

add("topical-authority-for-law-firms",
    "Building Topical Authority for Law Firms",
    "Topical authority is the single biggest driver of AI and search visibility. Here's how law firms build deep, recognized expertise that AI systems trust.",
    "ai-seo", "AI SEO",
    [
      ("What Topical Authority Means",
       [P("Topical authority is the degree to which search engines and AI systems recognize your firm as a genuine expert on a subject. It is not built by a single page — it is built by covering a topic comprehensively, accurately, and consistently over time."),
        P("A firm with one shallow divorce page has little authority. A firm with a deep pillar on divorce surrounded by detailed articles on custody, support, property division, mediation, and separation agreements is recognized as a true authority — and AI systems reward that depth."),
        CALLOUT("gold","Core Principle","AI systems recommend firms that demonstrably understand a topic in full, not firms that mention it once.")]),
      ("Why It Drives AI Visibility",
       [P("AI models are trained to identify reliable, comprehensive sources. When a firm covers every facet of a practice area, the model develops confidence that the firm is a dependable expert, increasing the likelihood it is cited or recommended."),
        P("Topical authority also creates internal reinforcement: each related article strengthens the others through context and linking, signaling to machines that this body of content belongs together and is led by a clear expert entity.")]),
      ("Building Topic Clusters",
       [P("The proven structure for topical authority is the topic cluster: one comprehensive pillar page per practice area, supported by focused articles that each answer a specific client question."),
        UL("Pillar: a thorough overview of the practice area",
           "Supporting articles: one per common client question",
           "Internal links connecting supporting pieces to the pillar",
           "Consistent terminology and entity references throughout"),
        P("Each supporting article should fully resolve its narrow question. Together, the cluster signals end-to-end expertise.")]),
      ("Depth Beats Volume",
       [P("Publishing many shallow posts does not build authority — it dilutes it. One genuinely useful, complete article on how child support is calculated outperforms ten thin posts that skim the surface."),
        P("Aim for the most helpful resource on each topic in your market. Answer the question fully, anticipate follow-up questions, and write in plain language a stressed client can understand.")]),
      ("Sustaining Authority Over Time",
       [P("Topical authority is not static. Laws change, client questions evolve, and competitors publish. Firms that update their content, fill gaps, and keep adding depth maintain and grow their authority."),
        P("Combined with consistent entity signals and a strong reputation, sustained topical depth is the most reliable path to being the firm AI systems trust and recommend.")]),
    ],
    [("What is topical authority for a law firm?","Topical authority is the recognition by search engines and AI systems that your firm is a genuine, comprehensive expert on a subject, earned by covering a practice area thoroughly and consistently."),
     ("How do I build topical authority?","Create a topic cluster: a comprehensive pillar page for each practice area supported by focused articles answering specific client questions, all internally linked and consistently written."),
     ("Does topical authority help with AI search?","Yes. AI systems favor sources that demonstrate complete, reliable understanding of a topic, so deep topical coverage significantly increases the chance your firm is cited or recommended."),
     ("Is it better to publish many posts or fewer deep ones?","Fewer, deeper resources win. One complete, genuinely helpful article outperforms many thin posts, which can actually dilute your authority."),
     ("How long does it take to build topical authority?","It builds over months as you add depth and consistency. Firms that publish steadily and keep content current typically see compounding gains within a few months and lasting advantage over time.")],
    REL_SEO,
    "Topical authority is the biggest driver of AI and search visibility. Learn how law firms build deep expertise that AI systems trust.")

add("local-ai-seo-for-law-firms",
    "Local AI SEO for Law Firms",
    "Most legal clients hire locally. This guide shows how to make your firm the local recommendation across AI assistants, AI Overviews, and map results.",
    "ai-seo", "AI SEO",
    [
      ("Why Local Signals Matter More Than Ever",
       [P("Legal services are inherently local. Clients want a lawyer licensed in their jurisdiction who understands local courts and procedures. When someone asks an AI assistant for a family lawyer near them, the system must determine which firms genuinely serve that location."),
        P("Local AI SEO is the practice of making your firm's geographic relevance unmistakable to AI systems, so you are the firm recommended for your city and practice area."),
        CALLOUT("blue","Key Insight","AI systems can only recommend you locally if your location signals are complete, consistent, and unambiguous across the web.")]),
      ("Google Business Profile as a Foundation",
       [P("Your Google Business Profile remains one of the strongest local signals. A complete, accurate, well-reviewed profile feeds both Google's local results and the AI systems that draw on Google data."),
        UL("Choose precise, accurate practice-area categories",
           "Keep name, address, and phone identical everywhere",
           "Actively earn and respond to client reviews",
           "Add photos, hours, and detailed service descriptions"),
        P("A neglected profile undermines local visibility no matter how good your website is.")]),
      ("Location-Specific Content",
       [P("Generic content does not establish local relevance. Firms that publish content tied to their city — local court information, jurisdiction-specific legal guidance, community involvement — give AI systems clear geographic context."),
        P("For multi-location firms, dedicated, genuinely useful pages for each office reinforce relevance in each market. Avoid thin, duplicated location pages, which add no value and can dilute trust.")]),
      ("Local Citations and Consistency",
       [P("Citations — mentions of your firm's name, address, and phone across directories, legal listings, and local sites — reinforce your geographic entity. Consistency is everything: conflicting addresses or phone numbers confuse both search engines and AI models."),
        P("Audit your listings, fix inconsistencies, and ensure every reference to your firm matches exactly. This clean foundation strengthens local recommendation across every platform.")]),
      ("Reviews and Local Reputation",
       [P("Reviews are powerful local trust signals. A firm with many recent, positive, location-relevant reviews is far more likely to be recommended by AI systems for that area."),
        P("Build a steady review process, respond professionally, and let genuine client experiences accumulate. Combined with strong profiles, local content, and consistent citations, reviews complete the local AI SEO picture.")]),
    ],
    [("What is local AI SEO for law firms?","Local AI SEO makes your firm's geographic relevance clear to AI systems so you are recommended for your city and practice area across AI assistants, AI Overviews, and map results."),
     ("How important is Google Business Profile for AI visibility?","Very important. A complete, accurate, well-reviewed profile feeds Google's local results and the AI systems that draw on Google data, making it a foundational local signal."),
     ("Do I need location-specific content?","Yes. Content tied to your city and jurisdiction gives AI systems clear geographic context, which generic content cannot provide."),
     ("How do citations affect local AI SEO?","Consistent citations across directories reinforce your geographic entity. Inconsistent name, address, or phone information confuses AI systems and weakens local recommendation."),
     ("Do reviews help with local AI recommendations?","Strongly. Recent, positive, location-relevant reviews are powerful trust signals that increase the likelihood AI systems recommend your firm in your area.")],
    REL_SEO,
    "Most legal clients hire locally. Learn how to make your firm the local recommendation across AI assistants, AI Overviews, and map results.")

# ---- AI Receptionists ----
add("what-is-an-ai-receptionist-for-law-firms",
    "What Is an AI Receptionist for Law Firms?",
    "An AI receptionist answers every call, captures every lead, and books consultations 24/7. Here's how it works and why law firms are adopting it fast.",
    "ai-receptionists", "AI Receptionists",
    [
      ("Defining the AI Receptionist",
       [P("An AI receptionist is an intelligent voice system that answers your law firm's phone calls automatically, holds natural conversations with callers, answers common questions, captures caller information, and books consultations — all without a human picking up."),
        P("Unlike a basic voicemail or a rigid phone tree, a modern AI receptionist understands natural speech, responds conversationally, and adapts to what each caller needs. To most callers, it simply feels like a helpful, professional intake conversation."),
        CALLOUT("gold","Why Firms Are Adopting It","Every missed call is a potential client calling a competitor. An AI receptionist ensures no call goes unanswered, day or night.")]),
      ("How It Works",
       [P("When a call comes in, the AI receptionist greets the caller, listens to their reason for calling, and responds appropriately. It can answer FAQs about practice areas, hours, and process; collect the caller's name, contact details, and case type; and schedule a consultation directly into your calendar."),
        UL("Answers instantly, 24 hours a day, 7 days a week",
           "Handles multiple calls at once without holds",
           "Captures structured intake information for every caller",
           "Books consultations and sends confirmations automatically",
           "Routes urgent or complex matters to the right person")]),
      ("Why Phone Calls Still Matter in Law",
       [P("Despite the rise of digital channels, the phone remains the primary way legal clients reach out. Legal problems are urgent and emotional, and people want to talk to someone now. A call that goes unanswered is often a client lost in minutes."),
        P("Because demand is unpredictable — after-hours, weekends, lunch breaks, busy periods — human-only reception inevitably leaves gaps. An AI receptionist closes those gaps completely.")]),
      ("AI Receptionist vs Voicemail and Phone Trees",
       [P("Voicemail loses a large share of callers, who simply hang up and call the next firm. Phone trees frustrate people with rigid menus. An AI receptionist replaces both with a natural conversation that actually helps the caller and captures the lead."),
        CALLOUT("blue","The Difference","Voicemail records a missed opportunity. An AI receptionist converts it into a booked consultation.")]),
      ("Is It Right for Your Firm?",
       [P("AI receptionists benefit firms of every size. Solo practitioners gain coverage they could never staff. Growing firms handle overflow and after-hours demand without hiring. Larger firms ensure consistent, professional intake across high call volumes."),
        P("If your firm misses calls — and almost every firm does — an AI receptionist is one of the highest-return investments available, turning lost calls into captured, qualified leads.")]),
    ],
    [("What is an AI receptionist for a law firm?","An AI receptionist is an intelligent voice system that answers calls, holds natural conversations, answers common questions, captures caller details, and books consultations automatically, 24/7."),
     ("How is an AI receptionist different from voicemail?","Voicemail simply records a message and loses many callers who hang up. An AI receptionist holds a real conversation, helps the caller, and captures the lead by booking a consultation."),
     ("Can an AI receptionist book consultations?","Yes. It can collect caller information and schedule consultations directly into your calendar, sending confirmations automatically."),
     ("Does an AI receptionist sound robotic?","Modern AI receptionists use natural-sounding voice and conversational understanding, so most callers experience a smooth, professional intake conversation."),
     ("What size of law firm benefits from an AI receptionist?","Firms of every size benefit. Solos gain coverage they could not otherwise staff, while larger firms ensure consistent intake across high call volumes and after hours.")],
    REL_RECEP,
    "An AI receptionist answers every call, captures every lead, and books consultations 24/7. Here's how it works and why firms adopt it fast.")

add("ai-receptionist-vs-human-receptionist",
    "AI Receptionist vs Human Receptionist for Law Firms",
    "Should your firm rely on a human receptionist, an AI receptionist, or both? A clear comparison of coverage, cost, consistency, and client experience.",
    "ai-receptionists", "AI Receptionists",
    [
      ("The Core Comparison",
       [P("A human receptionist brings warmth, judgment, and relationship skills. An AI receptionist brings unlimited availability, perfect consistency, and the ability to handle many calls at once. The two are not really competitors — they solve different parts of the same problem."),
        CALLOUT("blue","Reframe","The real question is not human versus AI. It is how to ensure no call is ever missed while keeping the experience professional and human-feeling.")]),
      ("Coverage and Availability",
       [P("A human receptionist works set hours and can handle one call at a time. Lunch breaks, sick days, after-hours, and call surges all create gaps where calls go unanswered."),
        P("An AI receptionist answers every call instantly, around the clock, including weekends and holidays, and never puts callers on hold because another line is busy. For a business where missed calls mean lost clients, this coverage is decisive.")]),
      ("Cost Considerations",
       [P("A full-time receptionist carries salary, benefits, training, and turnover costs, and still only covers business hours. An AI receptionist provides 24/7 coverage at a predictable, typically far lower monthly cost."),
        UL("No salary, benefits, or payroll overhead",
           "No training or turnover disruption",
           "Consistent cost regardless of call volume",
           "Coverage that scales instantly with demand")]),
      ("Consistency and Accuracy",
       [P("Even excellent human receptionists have variable days. An AI receptionist asks the same intake questions every time, captures complete information consistently, and never forgets to log a lead — producing clean, reliable intake data."),
        P("This consistency is especially valuable for law firms, where capturing accurate case details and conflict-check information at first contact matters.")]),
      ("The Best of Both Worlds",
       [P("Many firms get the strongest results by combining the two: humans handle relationship-driven conversations during business hours, while the AI receptionist covers overflow, after-hours, and surges so no call is ever lost."),
        P("This hybrid model preserves the human touch where it matters most while guaranteeing complete coverage and consistent intake the rest of the time.")]),
    ],
    [("Is an AI receptionist better than a human receptionist?","Neither is strictly better — they solve different problems. AI offers unlimited 24/7 coverage and consistency, while humans offer warmth and judgment. Many firms combine both."),
     ("Can an AI receptionist replace my front desk staff?","It can cover overflow, after-hours, and surges so no call is missed, but many firms keep human staff for relationship-driven conversations and use AI to fill the gaps."),
     ("Is an AI receptionist cheaper than hiring staff?","Typically yes. It provides 24/7 coverage at a predictable monthly cost without salary, benefits, training, or turnover expenses."),
     ("Will clients know they are talking to AI?","Modern AI receptionists sound natural and professional. Many firms disclose it transparently, and callers generally value getting an immediate, helpful response over reaching voicemail."),
     ("What is the best setup for a law firm?","A hybrid model often works best: humans handle calls during business hours while the AI receptionist covers overflow, after-hours, and surges to ensure no call is ever missed.")],
    REL_RECEP,
    "Human receptionist, AI receptionist, or both? A clear comparison of coverage, cost, consistency, and client experience for law firms.")

add("how-ai-receptionists-increase-law-firm-revenue",
    "How AI Receptionists Increase Law Firm Revenue",
    "Missed calls are missed cases. This article breaks down exactly how an AI receptionist converts more callers into clients and grows firm revenue.",
    "ai-receptionists", "AI Receptionists",
    [
      ("The Hidden Cost of Missed Calls",
       [P("Most law firms miss far more calls than they realize — after hours, during meetings, at lunch, and whenever multiple callers ring at once. Each missed call is often a potential client who simply dials the next firm on their list."),
        P("Because a single legal matter can be worth thousands of dollars, even a few recovered calls per month can translate into substantial revenue. The cost of missed calls is real, ongoing, and usually invisible on the books."),
        CALLOUT("gold","The Math","If your firm misses just a handful of qualified callers each week and each retained case is worth thousands, the annual cost of unanswered calls is enormous.")]),
      ("Speed-to-Lead Drives Conversion",
       [P("Decades of sales research show that responding instantly dramatically increases conversion. Legal clients are anxious and often calling several firms. The firm that answers first and helps them feels trustworthy and capable."),
        P("An AI receptionist answers on the first ring, every time, so your firm is consistently the one that responds first — a powerful conversion advantage.")]),
      ("Capturing After-Hours Demand",
       [P("A large share of legal calls happen outside business hours — evenings, weekends, and holidays — often when a problem feels most urgent. Without coverage, those calls go to voicemail and many are never recovered."),
        P("An AI receptionist captures this demand, books consultations overnight, and ensures your firm wakes up to scheduled appointments instead of missed-call notifications.")]),
      ("Better Qualification and Intake",
       [P("Revenue is not just about answering more calls — it is about converting the right ones efficiently. An AI receptionist gathers consistent intake details, qualifies callers, and routes serious matters appropriately, so attorney time is spent on viable cases."),
        UL("Consistent capture of case type and contact details",
           "Pre-qualification before attorney time is spent",
           "Fewer leads lost to slow follow-up",
           "Cleaner data for conflict checks and intake")]),
      ("Compounding Growth Over Time",
       [P("Every captured lead is also a future referral source and review. By converting more first calls into clients, an AI receptionist compounds its value: more clients today means more referrals, reviews, and reputation tomorrow."),
        P("For most firms, recovering even a fraction of currently missed calls produces a return that far exceeds the cost of the system.")]),
    ],
    [("How does an AI receptionist increase revenue?","It captures calls that would otherwise be missed — after hours, during meetings, and in surges — and converts them into booked consultations, recovering revenue that was being lost."),
     ("Why does answering calls faster matter?","Legal clients often call multiple firms. The firm that responds instantly feels most trustworthy and capable, which dramatically improves conversion. An AI receptionist always answers first."),
     ("How much revenue do missed calls cost a firm?","It varies, but since a single case can be worth thousands, even a few missed qualified callers per week can add up to a large annual loss."),
     ("Does an AI receptionist help with after-hours leads?","Yes. It captures evening, weekend, and holiday calls — often the most urgent — and books consultations overnight instead of losing them to voicemail."),
     ("Does better intake affect revenue?","Yes. Consistent qualification and intake ensure attorney time goes to viable cases and fewer leads are lost to slow follow-up, improving overall conversion and efficiency.")],
    REL_RECEP,
    "Missed calls are missed cases. See exactly how an AI receptionist converts more callers into clients and grows firm revenue.")

add("never-miss-a-call-law-firm",
    "Why Law Firms Can't Afford to Miss Another Call",
    "In legal services, the first firm to answer often wins the client. Here's why missed calls quietly drain revenue and how to stop it for good.",
    "ai-receptionists", "AI Receptionists",
    [
      ("Every Call Is a Potential Case",
       [P("In most industries, a missed call is a minor inconvenience. In legal services, it is often a lost case worth thousands of dollars. Legal clients call when they have a pressing problem, and they rarely leave a voicemail and wait."),
        P("Instead, they move down their list to the next firm. The firm that answers — not necessarily the best firm — frequently wins the client."),
        CALLOUT("blue","Hard Truth","Your competitors are not winning clients by being better lawyers. Often, they are simply answering the phone when you cannot.")]),
      ("Why Firms Miss So Many Calls",
       [P("Missed calls are not a sign of negligence — they are structural. Attorneys are in court, in meetings, or with clients. Staff are on other lines or off the clock. Demand spikes unpredictably. No reasonable level of human staffing covers every call."),
        UL("After-hours, weekend, and holiday calls",
           "Calls during meetings, hearings, and consultations",
           "Simultaneous calls that overwhelm the front desk",
           "Lunch breaks and staffing gaps")]),
      ("The Real Cost Adds Up Quietly",
       [P("Because missed calls are invisible — there is no record of the client who hung up — the cost is easy to ignore. But it compounds week after week. A firm missing even a handful of qualified callers weekly can lose six figures of potential revenue a year."),
        P("Worse, those lost clients often become a competitor's clients, reviews, and referral sources, multiplying the long-term cost.")]),
      ("Solving It Permanently",
       [P("The only reliable solution is guaranteed coverage of every call. An AI receptionist answers instantly, around the clock, handling unlimited simultaneous calls, capturing intake, and booking consultations so no opportunity slips through."),
        P("This transforms the phone from a leaky funnel into a reliable client-acquisition channel.")]),
      ("From Missed Calls to Booked Clients",
       [P("Firms that close the missed-call gap routinely discover they were losing far more business than they assumed. Recovering those calls is often the fastest, highest-return improvement a firm can make."),
        P("In a competitive legal market, simply being the firm that always answers is a durable advantage.")]),
    ],
    [("Why are missed calls such a big problem for law firms?","Because legal clients usually call with urgent problems and move to the next firm if no one answers. A missed call is often a lost case worth thousands of dollars."),
     ("How many calls do law firms typically miss?","More than most realize. Between after-hours calls, simultaneous calls, and calls during meetings and court, many firms miss a significant share of inbound calls."),
     ("Why do firms miss calls even with staff?","Missed calls are structural: attorneys are in court or meetings, staff are on other lines or off the clock, and demand spikes unpredictably. Human staffing alone cannot cover every call."),
     ("How can a firm stop missing calls?","Guaranteed 24/7 coverage. An AI receptionist answers every call instantly, handles unlimited simultaneous calls, captures intake, and books consultations so no opportunity is lost."),
     ("Is recovering missed calls worth the investment?","Almost always. Since each case is worth thousands, recovering even a fraction of missed qualified calls typically produces a return far exceeding the cost.")],
    REL_RECEP,
    "In legal services, the first firm to answer often wins the client. Learn why missed calls drain revenue and how to stop it for good.")

add("ai-receptionist-intake-automation",
    "AI Receptionist + Intake Automation for Law Firms",
    "Pairing an AI receptionist with intake automation turns every call into clean, structured data and a booked consultation. Here's how the combined system works.",
    "ai-receptionists", "AI Receptionists",
    [
      ("Where Reception Meets Intake",
       [P("An AI receptionist answers the call; intake automation captures and organizes everything that happens next. Together they create a seamless pipeline from first ring to scheduled consultation, with no manual data entry and no dropped details."),
        P("This pairing addresses two chronic law-firm problems at once: missed calls and messy, inconsistent intake."),
        CALLOUT("gold","The Combined Value","Reception ensures you answer every call. Intake automation ensures every answered call becomes clean, actionable data and a booked appointment.")]),
      ("Capturing Structured Intake Data",
       [P("During the call, the AI receptionist asks the right questions and records answers in a consistent structure: name, contact details, matter type, jurisdiction, and key facts. That information flows automatically into your systems."),
        UL("Consistent intake questions on every call",
           "Structured capture of case type and details",
           "Automatic logging without manual transcription",
           "Clean data ready for conflict checks and review")]),
      ("Automated Scheduling and Follow-Up",
       [P("Once a caller is qualified, the system books a consultation directly into the calendar and sends confirmations and reminders automatically. This reduces no-shows and eliminates the back-and-forth that loses leads."),
        P("Follow-up sequences can nurture callers who are not yet ready to book, keeping your firm top of mind without manual effort.")]),
      ("Qualification and Routing",
       [P("Not every caller is a fit. Intake automation can apply your criteria to qualify callers, flag urgent matters, and route different case types to the appropriate attorney or team — so human time is reserved for genuine opportunities."),
        P("This protects attorney time while ensuring serious matters get prompt, appropriate attention.")]),
      ("A Connected Client-Acquisition System",
       [P("Individually, reception and intake automation each add value. Combined, they form a connected acquisition system: every call answered, every lead captured, every consultation booked, and every detail recorded — consistently and at scale."),
        P("For firms serious about growth, this integrated approach turns the intake process from a bottleneck into a competitive advantage.")]),
    ],
    [("What is intake automation for a law firm?","Intake automation captures, structures, and routes caller information automatically — recording case details, qualifying leads, booking consultations, and feeding clean data into your systems without manual entry."),
     ("How do an AI receptionist and intake automation work together?","The AI receptionist answers and converses with callers, while intake automation captures structured data, qualifies and routes leads, and books consultations — creating a seamless pipeline."),
     ("Does the system reduce no-shows?","Yes. Automated confirmations, reminders, and follow-up sequences reduce no-shows and keep leads engaged until they are ready to proceed."),
     ("Can it qualify and route different case types?","Yes. It can apply your criteria to qualify callers, flag urgent matters, and route different case types to the appropriate attorney or team."),
     ("Why combine reception and intake instead of using one?","Reception ensures every call is answered; intake automation ensures every answered call becomes clean data and a booked consultation. Together they form a complete acquisition system.")],
    REL_RECEP,
    "Pairing an AI receptionist with intake automation turns every call into clean data and a booked consultation. Here's how the system works.")

# ---- AI Chatbots ----
add("ai-chatbot-for-law-firm-website",
    "AI Chatbot for Your Law Firm Website: A Complete Guide",
    "An AI chatbot engages website visitors instantly, answers their questions, and turns anonymous traffic into booked consultations. Here's everything you need to know.",
    "ai-chatbots", "AI Chatbots",
    [
      ("What an AI Chatbot Does for a Law Firm",
       [P("An AI chatbot is an intelligent assistant on your website that engages visitors in real time. It answers common legal questions, explains your services, captures contact details, and books consultations — turning passive browsing into active engagement."),
        P("Most website visitors leave without contacting the firm. An AI chatbot reaches out at the moment of interest, when a visitor is most likely to act, and guides them toward becoming a client."),
        CALLOUT("blue","The Opportunity","The majority of your website traffic leaves without a word. An AI chatbot gives every visitor a reason — and a way — to start a conversation.")]),
      ("Engaging Visitors at the Right Moment",
       [P("Timing is everything. An AI chatbot can greet visitors, respond instantly to questions, and proactively offer help when someone lingers on a practice-area page or appears unsure where to go next."),
        UL("Instant responses, day or night",
           "Proactive engagement based on visitor behavior",
           "Plain-language answers to common legal questions",
           "A frictionless path to booking a consultation")]),
      ("Answering Questions and Building Trust",
       [P("Legal clients have questions before they commit: how the process works, what it costs, whether they have a case. An AI chatbot answers these immediately and accurately, building confidence and reducing the hesitation that causes visitors to leave."),
        P("Helpful, knowledgeable responses position your firm as approachable and competent — exactly the impression that turns a visitor into a lead.")]),
      ("Capturing and Qualifying Leads",
       [P("Beyond answering questions, a well-designed chatbot captures contact information and qualifies visitors, gathering the details your team needs while filtering out poor-fit inquiries."),
        P("Qualified conversations can be handed off to staff or booked directly into the calendar, ensuring no interested visitor slips away.")]),
      ("Implementing a Chatbot the Right Way",
       [P("An effective legal chatbot is trained on your firm's services, practice areas, and common questions, and is designed to escalate appropriately when a matter needs human attention. It should feel helpful, not pushy, and always make it easy to reach a person."),
        P("Done well, an AI chatbot becomes a tireless front-line team member that engages every visitor, answers their questions, and consistently converts traffic into consultations.")]),
    ],
    [("What does an AI chatbot do for a law firm website?","It engages visitors in real time, answers common legal questions, explains services, captures contact details, and books consultations — turning passive traffic into active leads."),
     ("Can an AI chatbot answer legal questions?","It can answer common, general questions about your services and process, building trust, while escalating matters that require an attorney to a human."),
     ("Does a chatbot replace human staff?","No. It handles initial engagement and qualification around the clock, then hands qualified conversations to your team or books consultations directly, complementing your staff."),
     ("Will a chatbot annoy visitors?","A well-designed chatbot is helpful rather than pushy, engages at appropriate moments, and always makes it easy to reach a person, improving rather than harming the experience."),
     ("How is a chatbot trained for a law firm?","It is configured with your firm's services, practice areas, and common client questions, and set to escalate appropriately when a matter requires human attention.")],
    REL_CHAT,
    "An AI chatbot engages visitors instantly, answers questions, and turns anonymous traffic into booked consultations. Everything you need to know.")

add("how-ai-chatbots-convert-legal-leads",
    "How AI Chatbots Convert More Legal Leads",
    "Traffic is worthless if it doesn't convert. Learn the specific ways an AI chatbot turns more website visitors into booked legal consultations.",
    "ai-chatbots", "AI Chatbots",
    [
      ("The Conversion Gap on Most Law Firm Sites",
       [P("Law firms invest heavily in driving traffic to their websites, yet the vast majority of visitors leave without ever contacting the firm. This conversion gap is where marketing budgets quietly evaporate."),
        P("An AI chatbot closes that gap by engaging visitors who would otherwise bounce, giving them an immediate, low-friction way to take the next step."),
        CALLOUT("gold","The Core Problem","You are already paying to attract visitors. The real opportunity is converting the ones who are about to leave.")]),
      ("Instant Engagement Beats Contact Forms",
       [P("Traditional contact forms ask visitors to do work and then wait. Many abandon the form or never hear back quickly enough. A chatbot replaces that friction with an immediate conversation that feels easy and responsive."),
        UL("No waiting for a callback or email reply",
           "Conversational instead of a static form",
           "Answers questions that remove hesitation",
           "Guides visitors smoothly toward booking")]),
      ("Reducing Hesitation in Real Time",
       [P("Most visitors hesitate because they have unanswered questions: cost, process, whether they have a case. A chatbot resolves these doubts instantly, removing the friction that causes people to leave and come back later — which usually means never."),
        P("By addressing concerns at the moment they arise, the chatbot keeps the visitor moving toward action.")]),
      ("Qualifying and Booking Automatically",
       [P("A chatbot does not just talk — it captures contact details, qualifies the visitor, and books consultations directly. This means more of your traffic converts into scheduled appointments without relying on slow manual follow-up."),
        P("Faster response and seamless booking are proven to lift conversion dramatically, especially for high-intent legal visitors.")]),
      ("Working Around the Clock",
       [P("Many visitors browse outside business hours, exactly when no one is available to respond. A chatbot engages and converts these visitors at any hour, capturing leads that would otherwise be lost overnight."),
        P("By engaging every visitor, answering questions, and booking consultations automatically, an AI chatbot turns existing traffic into measurably more clients.")]),
    ],
    [("How does an AI chatbot increase lead conversion?","It engages visitors who would otherwise leave, answers their questions instantly, removes hesitation, captures their details, and books consultations — converting more existing traffic into clients."),
     ("Why is a chatbot better than a contact form?","Contact forms require effort and a waiting period that many abandon. A chatbot offers an immediate, conversational experience that answers questions and guides visitors to book directly."),
     ("Does a chatbot help outside business hours?","Yes. It engages and converts visitors at any hour, capturing after-hours leads that would otherwise be lost to a quiet inbox."),
     ("Can a chatbot qualify leads?","Yes. It can gather the details your team needs, apply your criteria to qualify visitors, and filter out poor-fit inquiries before booking."),
     ("Will a chatbot actually improve ROI?","Because it converts traffic you already pay to attract, a chatbot typically improves marketing ROI by lifting conversion without increasing ad spend.")],
    REL_CHAT,
    "Traffic is worthless if it doesn't convert. Learn how an AI chatbot turns more website visitors into booked legal consultations.")

add("ai-chatbot-vs-live-chat-lawyers",
    "AI Chatbot vs Live Chat for Law Firms",
    "Live chat needs a human on standby. AI chat works 24/7 on its own. Here's how the two compare and which is right for your firm.",
    "ai-chatbots", "AI Chatbots",
    [
      ("Two Approaches to Website Conversations",
       [P("Live chat connects a visitor to a human agent in real time. An AI chatbot holds the conversation automatically using artificial intelligence. Both aim to engage visitors and capture leads, but they differ sharply in availability, cost, and scalability."),
        CALLOUT("blue","Key Distinction","Live chat is only as available as your staff. AI chat is always available, instantly, to everyone.")]),
      ("Availability and Response Time",
       [P("Live chat works only when a human is monitoring it. Outside business hours or during busy periods, visitors face the same problem as an unanswered phone. An AI chatbot responds instantly, every time, regardless of hour or volume."),
        P("For law firms whose visitors often arrive evenings and weekends, this around-the-clock availability is a decisive advantage.")]),
      ("Scalability and Cost",
       [P("Live chat does not scale well: each agent handles limited simultaneous conversations, and staffing it fully is expensive. An AI chatbot handles unlimited conversations at once at a predictable cost."),
        UL("AI: unlimited simultaneous conversations",
           "AI: consistent monthly cost, 24/7",
           "Live chat: limited by agent availability",
           "Live chat: higher cost to staff fully")]),
      ("Consistency and Quality",
       [P("Human agents vary in knowledge, tone, and availability. An AI chatbot delivers consistent, accurate answers every time, trained on your firm's specific services and common questions — while still escalating to a human when needed."),
        P("The best implementations blend both: AI handles the bulk of conversations instantly and consistently, and routes complex or sensitive matters to a person.")]),
      ("Choosing the Right Approach",
       [P("For most law firms, an AI chatbot is the stronger foundation because it guarantees coverage no human team can match. Live chat can layer on top for moments that benefit from a human touch."),
        P("The goal is simple: never leave a visitor's question unanswered. AI chat ensures that, with human escalation available when it truly matters.")]),
    ],
    [("What is the difference between an AI chatbot and live chat?","Live chat connects visitors to a human agent in real time, while an AI chatbot converses automatically using AI. AI chat is always available; live chat depends on staff."),
     ("Which is better for a law firm?","An AI chatbot is usually the stronger foundation because it guarantees 24/7 coverage and unlimited simultaneous conversations, with human escalation available when needed."),
     ("Is AI chat available outside business hours?","Yes. An AI chatbot responds instantly at any hour, capturing evening and weekend visitors that live chat would miss when staff are unavailable."),
     ("Can I use both AI chat and live chat?","Yes. Many firms let AI handle the bulk of conversations instantly and consistently, then route complex or sensitive matters to a human agent."),
     ("Is an AI chatbot cheaper than staffing live chat?","Generally yes. AI handles unlimited conversations at a predictable cost, while fully staffing live chat for 24/7 coverage is expensive and hard to scale.")],
    REL_CHAT,
    "Live chat needs a human on standby. AI chat works 24/7 on its own. Here's how the two compare and which is right for your firm.")

add("ai-chatbot-intake-qualification",
    "Using AI Chatbots to Qualify Legal Leads",
    "Not every website visitor is a good fit. Learn how AI chatbots qualify legal leads automatically so your team focuses on the cases worth pursuing.",
    "ai-chatbots", "AI Chatbots",
    [
      ("Why Lead Qualification Matters",
       [P("Attorney time is a law firm's most valuable and limited resource. Spending it on poor-fit inquiries — wrong practice area, wrong jurisdiction, no viable matter — is costly. Qualifying leads before they reach an attorney protects that time."),
        P("An AI chatbot can perform this qualification automatically, at the very first point of contact, around the clock."),
        CALLOUT("gold","The Principle","The goal is not just more leads — it is the right leads, routed efficiently to the right people.")]),
      ("How a Chatbot Qualifies Visitors",
       [P("Through natural conversation, a chatbot gathers the information needed to assess fit: the type of legal matter, location and jurisdiction, timeline, and key facts. It applies your firm's criteria to determine whether the inquiry is a genuine opportunity."),
        UL("Identifies practice area and matter type",
           "Confirms jurisdiction and location relevance",
           "Captures timeline and urgency",
           "Applies your criteria to assess fit")]),
      ("Routing and Prioritization",
       [P("Once qualified, leads can be routed intelligently — urgent matters flagged, high-value cases prioritized, and different practice areas directed to the appropriate attorney or team. This ensures the most promising opportunities get prompt attention."),
        P("Poor-fit inquiries can be handled gracefully with helpful information or referrals, preserving goodwill without consuming attorney time.")]),
      ("Improving Intake Quality",
       [P("Because the chatbot asks consistent questions every time, the intake data it produces is clean and complete. This improves conflict checking, reduces back-and-forth, and gives attorneys context before the first conversation."),
        P("Consistent, structured intake is far more valuable than the partial, variable notes that manual intake often produces.")]),
      ("Balancing Qualification and Experience",
       [P("Good qualification never feels like an interrogation. A well-designed chatbot gathers what it needs conversationally while remaining helpful and respectful, so genuine prospects feel supported rather than screened."),
        P("Done right, automated qualification improves both efficiency and client experience — serious prospects move quickly toward a consultation, and your team spends its time where it counts.")]),
    ],
    [("How does an AI chatbot qualify legal leads?","Through natural conversation it gathers matter type, jurisdiction, timeline, and key facts, then applies your firm's criteria to assess whether the inquiry is a genuine opportunity."),
     ("Why is lead qualification important for law firms?","Attorney time is limited and valuable. Qualifying leads first ensures that time is spent on viable, well-fitting cases rather than poor-fit inquiries."),
     ("Can a chatbot route leads to the right attorney?","Yes. It can flag urgent matters, prioritize high-value cases, and direct different practice areas to the appropriate attorney or team."),
     ("Does qualification hurt the client experience?","Not when done well. A good chatbot gathers what it needs conversationally and helpfully, so genuine prospects feel supported rather than screened."),
     ("Does chatbot qualification improve intake quality?","Yes. Consistent questions produce clean, complete intake data, improving conflict checks, reducing back-and-forth, and giving attorneys context before the first conversation.")],
    REL_CHAT,
    "Not every visitor is a good fit. Learn how AI chatbots qualify legal leads automatically so your team focuses on cases worth pursuing.")

add("ai-chatbot-roi-for-law-firms",
    "The ROI of AI Chatbots for Law Firms",
    "Is an AI chatbot worth the investment? This article breaks down the real return — in recovered leads, conversion lift, and reclaimed staff time.",
    "ai-chatbots", "AI Chatbots",
    [
      ("Framing Chatbot ROI Correctly",
       [P("To evaluate an AI chatbot's return, you have to look beyond its cost and measure the value it creates: leads recovered from visitors who would have left, higher conversion of existing traffic, and staff time reclaimed from repetitive inquiries."),
        CALLOUT("blue","The ROI Equation","Value created — recovered leads, higher conversion, reclaimed time — measured against a predictable monthly cost.")]),
      ("Recovered Leads From Existing Traffic",
       [P("Most website visitors leave without contacting the firm. A chatbot engages a portion of these would-be lost visitors and converts them into leads. Because this traffic is already paid for, every recovered lead is essentially incremental revenue."),
        P("Even a modest lift in conversion can represent significant value when each new case is worth thousands of dollars.")]),
      ("Higher Conversion and Faster Response",
       [P("Speed and ease of engagement drive conversion. By responding instantly and removing friction, a chatbot lifts the percentage of visitors who become leads — improving the return on all of your marketing spend simultaneously."),
        UL("Instant engagement lifts conversion",
           "24/7 coverage captures after-hours leads",
           "Qualification focuses effort on viable cases",
           "More clients from the same ad budget")]),
      ("Reclaimed Staff Time",
       [P("Chatbots handle repetitive questions — hours, location, process, cost ranges — that otherwise consume staff time. Freeing your team from routine inquiries lets them focus on higher-value work, an often-overlooked component of ROI."),
        P("This efficiency gain compounds across every inquiry the chatbot handles automatically.")]),
      ("Calculating Your Return",
       [P("To estimate ROI, consider your monthly website traffic, your current conversion rate, the average value of a case, and the chatbot's cost. Even a small improvement in conversion typically produces a return that dwarfs the investment."),
        P("For most firms, the question is not whether an AI chatbot pays for itself, but how much additional revenue it unlocks from traffic they already have.")]),
    ],
    [("Is an AI chatbot worth the cost for a law firm?","For most firms, yes. By recovering leads from existing traffic, lifting conversion, and reclaiming staff time, a chatbot typically produces a return far exceeding its predictable monthly cost."),
     ("How does a chatbot generate ROI?","It converts visitors who would otherwise leave into leads, improves conversion of all traffic, captures after-hours inquiries, and frees staff from repetitive questions."),
     ("How do I calculate chatbot ROI?","Compare the value created — recovered leads and higher conversion, valued by your average case worth — against the chatbot's monthly cost. Small conversion lifts usually yield large returns."),
     ("Does a chatbot save staff time?","Yes. It handles repetitive questions about hours, location, process, and cost ranges automatically, freeing your team for higher-value work."),
     ("Will a chatbot increase marketing ROI?","Because it converts traffic you already pay to attract, a chatbot improves the return on your entire marketing budget without increasing ad spend.")],
    REL_CHAT,
    "Is an AI chatbot worth it? A breakdown of the real return: recovered leads, conversion lift, and reclaimed staff time for law firms.")

# ---- Entity SEO ----
add("what-is-entity-seo-for-law-firms",
    "What Is Entity SEO for Law Firms?",
    "Search and AI no longer think in keywords — they think in entities. Learn what entity SEO is and how it makes your firm recognizable to AI systems.",
    "entity-seo", "Entity SEO",
    [
      ("From Keywords to Entities",
       [P("For years, SEO revolved around keywords — matching the words on your page to the words in a search. Modern search engines and AI systems work differently. They understand entities: distinct, real-world things like people, organizations, places, and concepts, along with the relationships between them."),
        P("Entity SEO is the practice of making your law firm a clearly defined, well-connected entity that search engines and AI systems can recognize, understand, and trust."),
        CALLOUT("gold","The Shift","Keywords describe what a page says. Entities describe what your firm is. AI systems recommend entities they understand and trust.")]),
      ("Why Entities Matter for AI Recommendations",
       [P("When someone asks an AI assistant to recommend a lawyer, the system is reasoning about entities — which firm, in which location, with which expertise, and how trustworthy. If your firm is not a well-defined entity in the model's understanding, it cannot be confidently recommended."),
        P("Establishing your firm as a recognized entity is therefore foundational to AI visibility.")]),
      ("Building Your Firm's Entity",
       [P("Your firm's entity is constructed from consistent signals across the web: your name, address, and phone number; your website and its structured data; your Google Business Profile; directory listings; reviews; and mentions in news and legal publications."),
        UL("Consistent name, address, and phone everywhere",
           "Structured data describing your firm and attorneys",
           "A complete, accurate Google Business Profile",
           "Citations and mentions across trusted sources"),
        P("The more consistent and connected these signals, the clearer and stronger your entity becomes.")]),
      ("The Role of Structured Data",
       [P("Schema markup is how you explicitly describe your entity to machines. LegalService, Attorney, and Organization schema tell search engines and AI systems exactly what your firm is, where it operates, and how its parts relate."),
        P("Structured data removes ambiguity, helping AI systems categorize and trust your firm rather than guessing.")]),
      ("Entity SEO as a Foundation for AI Visibility",
       [P("Entity SEO underpins everything else in AI visibility. Content depth and reputation matter, but they are far more powerful when attached to a clearly defined, consistent entity that AI systems can reliably identify."),
        P("Firms that invest in becoming a recognized entity give every other marketing effort a stronger foundation — and make themselves far easier for AI to recommend.")]),
    ],
    [("What is entity SEO for law firms?","Entity SEO is the practice of making your firm a clearly defined, well-connected entity — through consistent information, structured data, and reputation — that search engines and AI systems can recognize and trust."),
     ("How is entity SEO different from keyword SEO?","Keyword SEO matches page words to searches. Entity SEO defines what your firm is and how it relates to places, people, and concepts, which is how modern AI systems reason and recommend."),
     ("Why do entities matter for AI recommendations?","AI assistants reason about entities when recommending lawyers. If your firm is not a well-defined entity, the system cannot confidently identify or recommend it."),
     ("How do I build my firm's entity?","Maintain consistent name, address, and phone across the web, implement structured data, complete your Google Business Profile, and earn citations and mentions from trusted sources."),
     ("Does structured data help with entity SEO?","Yes. Schema markup explicitly describes your firm to machines, removing ambiguity and helping AI systems categorize and trust your firm.")],
    REL_ENTITY,
    "Search and AI no longer think in keywords — they think in entities. Learn what entity SEO is and how it makes your firm recognizable to AI.")

add("schema-markup-for-lawyers-guide",
    "Schema Markup for Lawyers: The Complete Guide",
    "Schema markup tells search engines and AI exactly what your firm is. This guide covers the schema types every law firm should implement and why.",
    "entity-seo", "Entity SEO",
    [
      ("What Schema Markup Is",
       [P("Schema markup is structured data added to your website's code that describes your content to machines in a standardized vocabulary. It does not change what visitors see — it gives search engines and AI systems explicit, unambiguous information about your firm."),
        P("For law firms, schema is the difference between hoping a machine infers what you do and telling it directly."),
        CALLOUT("blue","Why It Matters","AI systems and search engines trust explicit, structured information. Schema is how you give it to them.")]),
      ("Essential Schema Types for Law Firms",
       [P("Several schema types are particularly valuable for legal websites:"),
        UL("LegalService / Attorney — defines your firm and practitioners",
           "Organization — establishes your firm as an entity with consistent details",
           "LocalBusiness — communicates location, hours, and service area",
           "FAQPage — marks up question-and-answer content",
           "Review / AggregateRating — surfaces reputation signals"),
        P("Implemented together, these describe your firm comprehensively to machines.")]),
      ("FAQ Schema and AI Visibility",
       [P("FAQPage schema is especially powerful in the AI era. It maps your question-and-answer content directly to the way clients phrase questions to AI assistants, increasing the chance your answers are extracted and cited."),
        P("Adding FAQ schema to every practice-area page is one of the highest-value, lowest-effort improvements a firm can make.")]),
      ("Implementing Schema Correctly",
       [P("Schema should be accurate, complete, and consistent with the visible content and with your information elsewhere on the web. Inaccurate or mismatched markup can do more harm than good."),
        UL("Use JSON-LD, the format search engines prefer",
           "Keep markup consistent with on-page content",
           "Match firm details to your other listings",
           "Validate markup to catch errors")]),
      ("Maintaining and Expanding Schema",
       [P("Schema is not set-and-forget. As you add content, services, and locations, your structured data should expand to match. Regularly reviewing and updating markup keeps your entity description accurate and complete."),
        P("Well-maintained schema is a quiet but powerful driver of both traditional and AI visibility.")]),
    ],
    [("What is schema markup for a law firm?","Schema markup is structured data in your website's code that describes your firm to search engines and AI systems in a standardized vocabulary, providing explicit, unambiguous information."),
     ("Which schema types should law firms use?","Key types include LegalService or Attorney, Organization, LocalBusiness, FAQPage, and Review or AggregateRating, which together describe your firm comprehensively."),
     ("Does FAQ schema help with AI search?","Yes. FAQPage schema maps your Q&A content to how clients ask AI assistants questions, increasing the chance your answers are extracted and cited."),
     ("What format should schema be in?","JSON-LD is the format search engines prefer. It is added to your page code and kept consistent with visible content and your other listings."),
     ("Can incorrect schema hurt my site?","Yes. Inaccurate or mismatched markup can do more harm than good, so schema should always be accurate, complete, and consistent with your content and listings.")],
    REL_ENTITY,
    "Schema markup tells search engines and AI exactly what your firm is. The schema types every law firm should implement and why.")

add("attorney-knowledge-panel-optimization",
    "How to Get and Optimize Your Law Firm Knowledge Panel",
    "A knowledge panel is the box of information Google shows about your firm. Here's how to earn one and optimize it for both search and AI visibility.",
    "entity-seo", "Entity SEO",
    [
      ("What a Knowledge Panel Is",
       [P("A knowledge panel is the information box that appears on the right side of Google results when someone searches for your firm by name. It displays details like your name, location, hours, reviews, and links — drawn from Google's understanding of your firm as an entity."),
        P("Earning a knowledge panel is a strong signal that Google recognizes your firm as a distinct, established entity — which also supports AI recommendation."),
        CALLOUT("gold","Why It Matters","A knowledge panel is visible proof that your firm is a recognized entity. That same recognition underpins AI visibility.")]),
      ("How Knowledge Panels Are Generated",
       [P("Google generates knowledge panels automatically from information it trusts across the web: your website, Google Business Profile, directory listings, news mentions, and structured data. You do not create a panel directly — you earn it by building a clear, consistent entity."),
        P("The more confident Google is about who your firm is, the more likely it is to display a panel.")]),
      ("Building the Signals That Earn a Panel",
       [P("To earn and strengthen a knowledge panel, focus on the signals that define your entity:"),
        UL("A complete, accurate Google Business Profile",
           "Consistent name, address, and phone across the web",
           "Organization and LegalService schema on your site",
           "Mentions and citations from trusted sources",
           "Strong, consistent reviews and reputation"),
        P("These are the same signals that drive entity SEO and AI visibility more broadly.")]),
      ("Optimizing an Existing Panel",
       [P("If you already have a knowledge panel, keep its information accurate and complete. Verify the panel through Google where possible, correct errors, and ensure the linked profiles and details match your firm's current information."),
        P("An accurate, well-maintained panel reinforces trust with both searchers and AI systems.")]),
      ("Knowledge Panels and AI Recommendations",
       [P("The entity recognition that produces a knowledge panel is the same recognition AI systems rely on when deciding which firms to recommend. Earning a panel is both a visible win and a sign that your underlying entity is strong."),
        P("Invest in the consistent, well-structured digital footprint that earns a panel, and you simultaneously strengthen your AI visibility.")]),
    ],
    [("What is a law firm knowledge panel?","It is the information box Google shows about your firm when searched by name, displaying details like location, hours, reviews, and links drawn from Google's understanding of your firm as an entity."),
     ("How do I get a knowledge panel for my firm?","You earn one by building a clear, consistent entity: a complete Google Business Profile, consistent information across the web, structured data, trusted mentions, and strong reviews."),
     ("Can I create a knowledge panel directly?","No. Google generates panels automatically from trusted information. You influence it by strengthening the signals that define your firm's entity."),
     ("How do I fix errors in my knowledge panel?","Verify the panel through Google where possible, correct inaccurate details, and ensure linked profiles and information match your firm's current details."),
     ("Does a knowledge panel help with AI recommendations?","Yes. The entity recognition that produces a knowledge panel is the same recognition AI systems use when deciding which firms to recommend.")],
    REL_ENTITY,
    "A knowledge panel is the info box Google shows about your firm. How to earn one and optimize it for both search and AI visibility.")

add("local-business-schema-law-firms",
    "Local Business Schema for Law Firms",
    "Local business schema tells AI and search engines exactly where your firm operates. Here's how to implement it for maximum local visibility.",
    "entity-seo", "Entity SEO",
    [
      ("Why Local Schema Matters for Lawyers",
       [P("Legal services are local. Clients need a lawyer in their jurisdiction, and AI systems must determine which firms genuinely serve a given area. Local business schema gives machines explicit information about your firm's location, service area, and contact details."),
        P("Without it, you leave AI systems to infer your location from scattered, sometimes inconsistent signals."),
        CALLOUT("blue","Core Idea","Local schema removes guesswork. It tells AI and search engines precisely where you operate.")]),
      ("What Local Business Schema Includes",
       [P("LocalBusiness schema (and its legal-specific variants) communicates the essential facts about your firm's physical presence:"),
        UL("Business name, address, and phone number",
           "Geographic coordinates and service area",
           "Opening hours and days of operation",
           "Practice areas and services offered",
           "Links to profiles and reviews"),
        P("Together these define your firm's local identity for machines.")]),
      ("Consistency Is Everything",
       [P("Local schema only helps if it matches your information everywhere else — your Google Business Profile, directory listings, and website. Conflicting addresses or phone numbers confuse AI systems and undermine local trust."),
        P("Audit your listings, resolve inconsistencies, and ensure your schema reflects the exact same details everywhere.")]),
      ("Multi-Location Firms",
       [P("Firms with multiple offices should implement distinct local schema for each genuine location, paired with dedicated, useful location pages. Avoid thin or duplicated pages, which add no value and can weaken trust."),
        P("Done correctly, per-location schema reinforces relevance in each market the firm serves.")]),
      ("Combining Schema With Local Signals",
       [P("Local schema is most powerful alongside the other local signals: a complete Google Business Profile, consistent citations, location-specific content, and strong local reviews. Together they make your firm unmistakably relevant to its area."),
        P("This combination is what positions a firm to be the local recommendation across AI assistants, AI Overviews, and map results.")]),
    ],
    [("What is local business schema for a law firm?","It is structured data that tells search engines and AI systems your firm's location, service area, hours, and contact details, defining your local identity for machines."),
     ("Why do law firms need local schema?","Because legal services are local. Local schema removes guesswork and tells AI and search engines precisely where your firm operates, supporting local recommendations."),
     ("What does local business schema include?","Business name, address, and phone; geographic coordinates and service area; hours; practice areas; and links to profiles and reviews."),
     ("How should multi-location firms handle schema?","Implement distinct local schema for each genuine location paired with dedicated, useful location pages, avoiding thin or duplicated pages that can weaken trust."),
     ("Does schema need to match my other listings?","Yes. Local schema must match your Google Business Profile, directories, and website exactly; conflicting details confuse AI systems and undermine local trust.")],
    REL_ENTITY,
    "Local business schema tells AI and search engines exactly where your firm operates. How to implement it for maximum local visibility.")

add("entity-seo-vs-keyword-seo",
    "Entity SEO vs Keyword SEO for Law Firms",
    "Keyword SEO targets phrases; entity SEO defines what your firm is. Here's how they differ and why entity SEO now drives AI visibility.",
    "entity-seo", "Entity SEO",
    [
      ("Two Models of Search",
       [P("Keyword SEO is built on matching: align the words on your page with the words people search. Entity SEO is built on understanding: establish your firm as a recognized, well-defined entity that machines comprehend and trust."),
        P("Both still matter, but the balance has shifted decisively toward entities as AI systems take over more of search."),
        CALLOUT("gold","The Distinction","Keywords are about what a page says. Entities are about what your firm is.")]),
      ("How Keyword SEO Works",
       [P("Keyword SEO involves researching the terms clients search, then creating and optimizing pages around those terms. It remains useful for capturing specific searches and structuring content."),
        P("But on its own, keyword targeting no longer guarantees visibility. AI systems look past keywords to assess genuine expertise, trust, and entity clarity.")]),
      ("How Entity SEO Works",
       [P("Entity SEO focuses on defining and reinforcing your firm as an entity: consistent information across the web, structured data, a complete Google Business Profile, citations, and reputation signals that together tell machines who you are and why you can be trusted."),
        UL("Consistent name, address, and phone everywhere",
           "Structured data describing the firm and attorneys",
           "Citations and mentions from trusted sources",
           "Strong, consistent reviews and reputation")]),
      ("Why Entity SEO Wins in the AI Era",
       [P("When an AI assistant recommends a lawyer, it reasons about entities — which firm, where, with what expertise and trust. Keyword matching alone cannot produce a confident recommendation; entity clarity can."),
        P("This is why entity SEO has become the foundation of AI visibility, with keyword work playing a supporting role.")]),
      ("Using Both Together",
       [P("The strongest strategy combines the two: use keyword research to inform helpful, well-structured content, and build that content on a foundation of clear entity signals and structured data."),
        P("Content tells AI what you know; your entity tells AI who you are. Firms that invest in both are the ones AI systems most reliably recommend.")]),
    ],
    [("What is the difference between entity SEO and keyword SEO?","Keyword SEO matches page words to searches, while entity SEO defines your firm as a recognized entity that machines understand and trust. Entity SEO now drives AI visibility."),
     ("Is keyword SEO still useful?","Yes, for capturing specific searches and structuring content. But on its own it no longer guarantees visibility, because AI systems look past keywords to expertise and entity clarity."),
     ("Why does entity SEO matter for AI?","AI assistants reason about entities when recommending lawyers. Entity clarity allows a confident recommendation that keyword matching alone cannot produce."),
     ("How do I build entity signals?","Maintain consistent information across the web, implement structured data, complete your Google Business Profile, and earn citations, mentions, and reviews from trusted sources."),
     ("Should I use both entity and keyword SEO?","Yes. Use keyword research to inform helpful content, built on a foundation of clear entity signals and structured data. Content shows what you know; your entity shows who you are.")],
    REL_ENTITY,
    "Keyword SEO targets phrases; entity SEO defines what your firm is. How they differ and why entity SEO now drives AI visibility.")

# ---- AI Websites ----
add("ai-website-design-for-law-firms-guide",
    "AI Website Design for Law Firms: The Complete Guide",
    "A modern law firm website must convert visitors and be readable by AI. This guide covers design, structure, and content that wins on both fronts.",
    "ai-websites", "AI Websites",
    [
      ("What AI Website Design Means",
       [P("AI website design is the practice of building law firm websites that perform on two fronts at once: converting human visitors into clients, and being clearly understood and trusted by AI systems that increasingly mediate search."),
        P("It blends conversion-focused design with the structure, speed, and clarity that AI crawlers and models reward."),
        CALLOUT("blue","Dual Goal","A modern law firm site must persuade people and be readable by machines. AI website design does both.")]),
      ("Designing for Conversion",
       [P("A law firm website exists to turn visitors into consultations. That requires clear value propositions, obvious calls to action, trust signals like reviews and credentials, and a frictionless path to contact the firm."),
        UL("Clear, benefit-focused messaging above the fold",
           "Prominent, repeated calls to action",
           "Trust signals: reviews, results, credentials",
           "Easy contact options, including chat and click-to-call")]),
      ("Structuring for AI Readability",
       [P("AI systems favor well-structured content: logical headings, direct answers near the top, FAQ sections, and clean markup. Designing your site so machines can easily parse and extract your expertise increases the chance you are cited and recommended."),
        P("Structured data (schema) is essential here, explicitly describing your firm, services, and answers to machines.")]),
      ("Speed, Mobile, and Technical Quality",
       [P("Most legal visitors arrive on mobile, and slow, clunky sites lose them — and hinder AI crawlers. A fast, mobile-first, technically clean website improves conversion and machine readability simultaneously."),
        P("Performance is not a luxury; it is a baseline requirement for both human and AI visibility.")]),
      ("Content as the Connective Tissue",
       [P("Great design needs great content. Deep practice-area pages, helpful FAQs, and educational resources give visitors confidence and give AI systems the substance they need to recognize your expertise."),
        P("AI website design ties these together: a fast, conversion-focused, well-structured site full of genuinely helpful content is the foundation of modern legal marketing.")]),
    ],
    [("What is AI website design for law firms?","It is building websites that both convert human visitors into clients and are clearly understood and trusted by AI systems, blending conversion-focused design with AI-readable structure and speed."),
     ("How is it different from regular web design?","It adds an AI-readability layer — structured content, schema, fast performance, and depth — on top of conversion-focused design, so the site performs for both people and machines."),
     ("Why does AI readability matter for a law firm site?","AI systems increasingly mediate search. A site that machines can easily parse and trust is more likely to be cited and recommended when clients ask AI for legal help."),
     ("Does site speed affect AI visibility?","Yes. Slow sites lose mobile visitors and hinder AI crawlers. A fast, mobile-first, technically clean site improves both conversion and machine readability."),
     ("What content should a law firm website include?","Deep practice-area pages, helpful FAQs, and educational resources that build visitor confidence and give AI systems the substance to recognize your firm's expertise.")],
    REL_WEB,
    "A modern law firm website must convert visitors and be readable by AI. Design, structure, and content that win on both fronts.")

add("law-firm-website-conversion-optimization",
    "Law Firm Website Conversion Optimization",
    "Traffic without conversion is wasted budget. Learn the proven changes that turn more law firm website visitors into booked consultations.",
    "ai-websites", "AI Websites",
    [
      ("Why Conversion Is the Real Metric",
       [P("Many law firms obsess over traffic while ignoring conversion — the percentage of visitors who actually contact the firm. Yet conversion is where revenue is won or lost. Doubling conversion has the same effect as doubling traffic, usually at a fraction of the cost."),
        CALLOUT("gold","Reframe","More traffic is expensive. Better conversion is efficient. Optimize conversion first.")]),
      ("Clarity and Messaging",
       [P("Visitors decide within seconds whether your site is relevant. Clear, benefit-focused messaging that immediately communicates who you help and how is essential. Confusing or generic messaging causes visitors to leave."),
        UL("State who you help and how, immediately",
           "Lead with client benefits, not jargon",
           "Make practice areas obvious and easy to find",
           "Remove clutter that distracts from the next step")]),
      ("Calls to Action and Contact Paths",
       [P("Every page should make the next step obvious. Prominent, repeated calls to action — call now, book a consultation, chat with us — guide visitors toward contact. Multiple low-friction contact options accommodate different preferences."),
        P("Adding click-to-call and chat options captures visitors who would never fill out a long form.")]),
      ("Trust Signals That Convert",
       [P("Legal clients are choosing who to trust with a serious problem. Reviews, case results, credentials, associations, and professional design all reduce anxiety and increase the likelihood a visitor reaches out."),
        P("Prominently displaying genuine trust signals is one of the most reliable ways to lift conversion.")]),
      ("Testing and Continuous Improvement",
       [P("Conversion optimization is iterative. Test headlines, calls to action, page layouts, and forms; measure what improves contact rates; and keep refining. Small, evidence-based improvements compound into meaningful gains over time."),
        P("Firms that treat their website as a living asset — continually improved — consistently outperform those that build once and forget.")]),
    ],
    [("What is conversion optimization for a law firm website?","It is the practice of increasing the percentage of visitors who contact the firm, through clearer messaging, stronger calls to action, trust signals, and reduced friction."),
     ("Why focus on conversion instead of traffic?","Improving conversion is usually far cheaper than buying more traffic and has the same revenue effect as increasing visitors, making it the more efficient priority."),
     ("What are the most important conversion factors?","Clear benefit-focused messaging, prominent calls to action, easy contact options like chat and click-to-call, and strong trust signals such as reviews and results."),
     ("How do trust signals affect conversion?","Legal clients are choosing who to trust with a serious problem. Reviews, results, and credentials reduce anxiety and make visitors far more likely to reach out."),
     ("Is conversion optimization a one-time task?","No. It is iterative. Continually testing headlines, calls to action, and layouts and refining based on results produces compounding gains over time.")],
    REL_WEB,
    "Traffic without conversion is wasted budget. The proven changes that turn more law firm website visitors into booked consultations.")

add("law-firm-website-speed-performance",
    "Law Firm Website Speed & Performance Guide",
    "A slow website loses clients and hurts visibility. Learn why speed matters for law firms and the practical steps to make your site fast.",
    "ai-websites", "AI Websites",
    [
      ("Why Speed Directly Affects Revenue",
       [P("Website speed is not a technical nicety — it directly affects how many visitors become clients. Studies consistently show that slow-loading pages cause visitors to abandon a site before they ever see your content or contact options."),
        P("For law firms paying to attract each visitor, a slow site quietly wastes that investment by losing people before they engage."),
        CALLOUT("blue","Hard Number","Every additional second of load time increases the share of visitors who leave. Speed is conversion.")]),
      ("Speed and AI Visibility",
       [P("Performance also affects machine visibility. Search and AI crawlers favor fast, responsive sites and can struggle with slow, bloated ones. A fast site is easier to crawl, parse, and ultimately cite."),
        P("Optimizing speed therefore improves both human conversion and AI readability at once.")]),
      ("Common Causes of Slow Law Firm Sites",
       [P("Most slow law firm websites share a few culprits:"),
        UL("Large, unoptimized images",
           "Bloated themes and excessive plugins",
           "Lack of caching and compression",
           "Slow or low-quality hosting",
           "Unnecessary scripts and trackers")]),
      ("Practical Steps to Improve Speed",
       [P("Improving speed is usually straightforward. Compress and properly size images, minimize and combine scripts, enable caching and compression, and choose quality hosting. A clean, modern build avoids the bloat that slows older sites."),
        P("Mobile performance deserves special attention, since most legal visitors arrive on phones and are the quickest to abandon a slow page.")]),
      ("Making Performance a Standard",
       [P("Speed should be treated as a permanent standard, not a one-time fix. As you add content and features, monitor performance to ensure the site stays fast. Regular checks prevent gradual slowdown."),
        P("A consistently fast website converts better, ranks better, and is more easily understood by the AI systems shaping the future of search.")]),
    ],
    [("Why does website speed matter for law firms?","Slow pages cause visitors to leave before engaging, wasting the budget spent attracting them. Speed directly affects how many visitors become clients."),
     ("Does site speed affect AI and search visibility?","Yes. Search and AI crawlers favor fast, responsive sites and struggle with slow ones, so speed improves both human conversion and machine readability."),
     ("What slows down a law firm website?","Common causes include large unoptimized images, bloated themes and plugins, missing caching and compression, slow hosting, and unnecessary scripts."),
     ("How can I make my law firm website faster?","Compress and size images properly, minimize scripts, enable caching and compression, choose quality hosting, and prioritize mobile performance."),
     ("Is website speed a one-time fix?","No. Speed should be maintained as a standard. As you add content and features, monitor performance regularly to prevent gradual slowdown.")],
    REL_WEB,
    "A slow website loses clients and hurts visibility. Why speed matters for law firms and the practical steps to make your site fast.")

add("mobile-first-law-firm-website",
    "Mobile-First Design for Law Firm Websites",
    "Most legal clients find you on their phone. Learn why mobile-first design is essential and how to build a law firm site that converts on mobile.",
    "ai-websites", "AI Websites",
    [
      ("Why Mobile Comes First",
       [P("The majority of people searching for legal help do so on their phones, often in stressful, urgent moments. If your website is hard to use on mobile, you lose these visitors regardless of how good your firm is."),
        P("Mobile-first design means building the mobile experience as the primary experience, not an afterthought scaled down from desktop."),
        CALLOUT("gold","Reality","Your next client is probably reading this on a phone. Design for them first.")]),
      ("The Cost of a Poor Mobile Experience",
       [P("Tiny text, cramped layouts, slow loading, and hard-to-tap buttons all drive mobile visitors away. Because legal decisions are often urgent, a frustrated visitor simply moves to a competitor whose site works smoothly on their phone."),
        P("A poor mobile experience is one of the most common and costly weaknesses in law firm websites.")]),
      ("Principles of Mobile-First Design",
       [P("Effective mobile-first design follows a few clear principles:"),
        UL("Readable text without zooming (minimum comfortable size)",
           "Large, easy-to-tap buttons and touch targets",
           "Fast loading on mobile connections",
           "Click-to-call and chat prominently available",
           "Simple, focused layouts that guide the next step")]),
      ("Mobile Conversion Essentials",
       [P("On mobile, friction is fatal. Click-to-call buttons, simple contact options, and chat let visitors reach you in a single tap. Long forms and complex navigation kill mobile conversion and should be minimized."),
        P("The easier you make it to contact the firm from a phone, the more leads you capture.")]),
      ("Mobile and AI Visibility",
       [P("Search and AI systems prioritize mobile-friendly sites, so mobile-first design supports machine visibility as well as human conversion. A fast, well-structured mobile site is easier for AI to crawl and trust."),
        P("Building mobile-first is therefore not just good for users — it strengthens your position across the entire search and AI landscape.")]),
    ],
    [("Why is mobile-first design important for law firms?","Most legal clients search on their phones, often urgently. A poor mobile experience loses these visitors regardless of your firm's quality, so mobile must be the primary design focus."),
     ("What makes a good mobile law firm website?","Readable text without zooming, large tappable buttons, fast loading, prominent click-to-call and chat, and simple layouts that guide visitors toward contact."),
     ("How does a poor mobile experience hurt my firm?","Tiny text, slow loading, and hard-to-tap buttons frustrate visitors, who quickly move to a competitor whose site works smoothly on their phone."),
     ("What helps mobile conversion most?","Reducing friction: click-to-call buttons, simple contact options, and chat that let visitors reach you in a single tap, while minimizing long forms and complex navigation."),
     ("Does mobile-first design help with AI visibility?","Yes. Search and AI systems prioritize mobile-friendly sites, so mobile-first design supports machine crawling and trust as well as human conversion.")],
    REL_WEB,
    "Most legal clients find you on their phone. Why mobile-first design is essential and how to build a law firm site that converts on mobile.")

add("law-firm-website-seo-structure",
    "How to Structure Your Law Firm Website for SEO",
    "The right site structure helps both search engines and AI understand your firm. Learn how to organize a law firm website for maximum visibility.",
    "ai-websites", "AI Websites",
    [
      ("Why Structure Matters",
       [P("Website structure is the organization of your pages and how they connect. A clear, logical structure helps visitors find what they need and helps search engines and AI systems understand your firm, your services, and your expertise."),
        P("A disorganized site confuses both people and machines, undermining even excellent content."),
        CALLOUT("blue","Core Idea","Good structure makes your expertise legible — to clients and to the AI systems that recommend firms.")]),
      ("Organizing Around Practice Areas",
       [P("The backbone of an effective law firm site is a clear practice-area structure. Each practice area should have a dedicated, comprehensive page, supported by deeper content addressing specific client questions within that area."),
        UL("A clear page for each practice area",
           "Supporting articles answering specific questions",
           "Logical grouping that reflects how clients think",
           "Easy navigation between related topics")]),
      ("Internal Linking and Topic Clusters",
       [P("Internal links connect related pages, signaling to search engines and AI systems which content belongs together and reinforcing your topical authority. Organizing content into clusters — a pillar page linked to supporting articles — is a proven structure."),
        P("Thoughtful internal linking helps machines map your expertise and helps visitors move smoothly through your content.")]),
      ("Clear Navigation and URLs",
       [P("Navigation should be simple and predictable, letting visitors and crawlers reach any important page in a few clicks. Clean, descriptive URLs that reflect your structure further help both users and machines understand each page's purpose."),
        P("Avoid deep, tangled hierarchies that bury important content where it is hard to find.")]),
      ("Structuring for AI Visibility",
       [P("AI systems reward sites that are well-organized, clearly structured, and rich with directly answered questions. A logical architecture, combined with schema and FAQ content, makes your expertise easy for AI to parse, trust, and cite."),
        P("Structure your site well, and every other investment — content, design, reputation — works harder across both search and AI.")]),
    ],
    [("Why is website structure important for SEO?","A clear, logical structure helps visitors find content and helps search engines and AI systems understand your firm, services, and expertise, while a disorganized site confuses both."),
     ("How should a law firm website be organized?","Around clear practice areas, each with a dedicated comprehensive page supported by deeper content answering specific client questions, grouped the way clients think."),
     ("What is internal linking and why does it matter?","Internal linking connects related pages, signaling which content belongs together, reinforcing topical authority, and helping both visitors and machines navigate your expertise."),
     ("Do clean URLs help SEO?","Yes. Clean, descriptive URLs that reflect your structure help users and machines understand each page's purpose and support clearer navigation."),
     ("How does site structure affect AI visibility?","AI systems reward well-organized sites with clearly answered questions. A logical architecture combined with schema and FAQ content makes your expertise easy to parse, trust, and cite.")],
    REL_WEB,
    "The right site structure helps both search engines and AI understand your firm. How to organize a law firm website for maximum visibility.")


HUBS = {
    "ai-seo": dict(
        title="AI SEO for Law Firms",
        description="The complete resource hub on AI SEO for law firms. Learn how to rank in AI search, earn citations from ChatGPT and Google AI, and win more clients — 5 expert guides.",
        label="AI SEO", icon="📈",
        stats=[("5","in-depth guides"),("3-6mo","to see results"),("2025","fully up to date"),("AI-first","strategy")]),
    "ai-receptionists": dict(
        title="AI Receptionists for Law Firms",
        description="Everything law firms need to know about AI receptionists — how they answer every call, capture leads 24/7, and turn missed calls into booked consultations.",
        label="AI Receptionists", icon="📞",
        stats=[("24/7","call coverage"),("5","in-depth guides"),("0","missed calls"),("2025","up to date")]),
    "ai-chatbots": dict(
        title="AI Chatbots for Law Firms",
        description="The complete guide to AI chatbots for law firms — engaging website visitors, qualifying leads, and converting traffic into consultations around the clock.",
        label="AI Chatbots", icon="💬",
        stats=[("5","in-depth guides"),("24/7","visitor engagement"),("Higher","conversion"),("2025","up to date")]),
    "entity-seo": dict(
        title="Entity SEO for Law Firms",
        description="Learn how entity SEO and structured data make your law firm recognizable to AI systems — earning knowledge panels, citations, and AI recommendations.",
        label="Entity SEO", icon="🗂️",
        stats=[("5","in-depth guides"),("Entity","recognition"),("Schema","powered"),("2025","up to date")]),
    "ai-websites": dict(
        title="AI Websites for Law Firms",
        description="The complete hub on AI website design for law firms — building fast, conversion-focused, AI-readable websites that win clients and get cited by AI search.",
        label="AI Websites", icon="🌐",
        stats=[("5","in-depth guides"),("Mobile","first"),("Fast","by design"),("2025","up to date")]),
}


def main():
    written = []
    by_hub = {}
    for a in ARTICLES:
        by_hub.setdefault(a["hub"], []).append(a)

    for slug, h in HUBS.items():
        arts = by_hub[slug]
        cards = [dict(slug=a["slug"], title=a["title"], desc=a["card_desc"],
                      date="June 2025", read=a["read"]) for a in arts]
        page = build_hub_page(slug, h["title"], h["description"], h["label"], h["icon"], cards, h["stats"])
        with open(os.path.join(DIR, f"{slug}.html"), "w", encoding="utf-8") as f:
            f.write(page)
        written.append(f"{slug}.html")

    for a in ARTICLES:
        page = build_article_page(a["slug"], a["title"], a["card_desc"], a["deck"],
                                  a["hub"], a["cat"], a["sections"], a["faqs"], a["related"])
        with open(os.path.join(DIR, f"{a['slug']}.html"), "w", encoding="utf-8") as f:
            f.write(page)
        written.append(f"{a['slug']}.html")

    print(f"Generated {len(written)} files.")

    generated = set(written)
    pattern = re.compile(
        r'<div class="dropdown">.*?href="perplexity\.html".*?</div>\s*(?=</li>)',
        re.DOTALL)

    updated = 0
    for fp in glob.glob(os.path.join(DIR, "*.html")):
        name = os.path.basename(fp)
        if name in generated:
            continue
        with open(fp, "r", encoding="utf-8") as f:
            content = f.read()
        if 'href="perplexity.html"' not in content:
            continue
        new_content, count = pattern.subn(NAV_DROPDOWN, content)
        if count:
            with open(fp, "w", encoding="utf-8") as f:
                f.write(new_content)
            updated += 1
    print(f"Updated dropdown in {updated} existing files.")


if __name__ == "__main__":
    main()
