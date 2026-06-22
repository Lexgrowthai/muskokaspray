#!/usr/bin/env python3
"""Regenerate all category hub pages to match the Google Gemini hub layout."""
import os

BASE = os.path.dirname(__file__)
SITE = "https://lexscale.ai"

NAV_FULL = '''<nav>
  <a href="/" class="logo">Lex<span>Scale</span>.ai</a>
  <ul class="nav-links">
    <li><a href="/">Home</a></li>
    <li class="has-drop">
      <a href="#">Services
        <svg class="drop-arrow" viewBox="0 0 14 14" fill="none"><path d="M3 5l4 4 4-4" stroke="#4a5568" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
      <div class="dropdown">
        <a href="/ai-website-design-for-law-firms.html" class="drop-item">
          <div class="drop-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg></div>
          <div><div class="drop-label">AI Website Design</div><div class="drop-sub">For law firms</div></div>
        </a>
        <a href="/ai-seo-for-law-firms.html" class="drop-item">
          <div class="drop-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg></div>
          <div><div class="drop-label">AI SEO</div><div class="drop-sub">Rank higher, get cited by AI</div></div>
        </a>
        <a href="/ai-receptionist-for-law-firms.html" class="drop-item">
          <div class="drop-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 8.81 19.79 19.79 0 01.1 2.18 2 2 0 012.08 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.91 7.91a16 16 0 006.16 6.16l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg></div>
          <div><div class="drop-label">AI Receptionist</div><div class="drop-sub">24/7 call answering</div></div>
        </a>
        <a href="/ai-chatbot-for-law-firms.html" class="drop-item">
          <div class="drop-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg></div>
          <div><div class="drop-label">AI Chatbot</div><div class="drop-sub">Convert more website visitors</div></div>
        </a>
      </div>
    </li>
    <li><a href="/about.html">About</a></li>
    <li class="has-drop">
      <a href="#">Insights
        <svg class="drop-arrow" viewBox="0 0 14 14" fill="none"><path d="M3 5l4 4 4-4" stroke="#4a5568" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
      <div class="dropdown">
        <a href="/insights/chatgpt.html" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div><div><div class="drop-label">ChatGPT for Law Firms</div><div class="drop-sub">29 articles</div></div></a>
        <a href="/insights/google-gemini.html" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#4285f4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg></div><div><div class="drop-label">Google Gemini for Law Firms</div><div class="drop-sub">6 articles</div></div></a>
        <a href="/insights/perplexity.html" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#20B8CD" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/></svg></div><div><div class="drop-label">Perplexity for Law Firms</div><div class="drop-sub">3 articles</div></div></a>
        <div class="drop-divider"></div>
        <a href="/insights/ai-seo.html" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg></div><div><div class="drop-label">AI SEO for Law Firms</div><div class="drop-sub">16 articles</div></div></a>
        <a href="/insights/ai-receptionists.html" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 8.81 19.79 19.79 0 01.1 2.18 2 2 0 012.08 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.91 7.91a16 16 0 006.16 6.16l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg></div><div><div class="drop-label">AI Receptionists for Law Firms</div><div class="drop-sub">5 articles</div></div></a>
        <a href="/insights/ai-chatbots.html" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div><div><div class="drop-label">AI Chatbots for Law Firms</div><div class="drop-sub">5 articles</div></div></a>
        <a href="/insights/entity-seo.html" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg></div><div><div class="drop-label">Entity SEO &amp; Structured Data</div><div class="drop-sub">6 articles</div></div></a>
        <a href="/insights/ai-websites.html" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg></div><div><div class="drop-label">AI Websites for Law Firms</div><div class="drop-sub">15 articles</div></div></a>
      </div>
    </li>
  </ul>
  <button class="nav-cta" onclick="document.getElementById('leadModal').style.display='flex'">Book A Demo</button>
  <button class="nav-mob" aria-label="Open menu" onclick="toggleMobNav(this)">
    <span></span><span></span><span></span>
  </button>
</nav>'''

CSS = '''<style>
*{margin:0;padding:0;box-sizing:border-box;}
:root{--navy:#0B1536;--pu:#6A5CFF;--pu2:#8B7FFF;--pu3:#a89fff;--gold:#D4AF37;}
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
.dropdown{position:absolute;top:100%;left:50%;transform:translateX(-50%);background:#fff;border:1px solid rgba(106,92,255,.12);border-radius:16px;padding:12px 8px 8px;box-shadow:0 16px 48px rgba(11,21,54,.12);min-width:240px;opacity:0;pointer-events:none;visibility:hidden;transition:opacity .2s,visibility .2s;z-index:200;}
.has-drop:hover .dropdown{opacity:1;pointer-events:all;visibility:visible;}
.drop-item{display:flex;align-items:center;gap:10px;padding:10px 14px;border-radius:10px;transition:background .15s;cursor:pointer;}
.drop-item:hover{background:rgba(106,92,255,.07);}
.drop-ico{width:30px;height:30px;border-radius:8px;background:rgba(106,92,255,.1);display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.drop-label{font-size:12.5px;font-weight:600;color:var(--navy);}
.drop-sub{font-size:11px;color:#94a3b8;margin-top:1px;}
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
.art-card.featured .art-right{width:280px;flex-shrink:0;background:linear-gradient(135deg,rgba(106,92,255,.08),rgba(106,92,255,.03));display:flex;align-items:center;justify-content:center;border-left:1px solid rgba(106,92,255,.08);}
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
}
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
}
</style>'''

FOOTER_HTML = '''<footer>
  <div class="footer-inner">
    <div><div class="footer-logo">Lex<span>Scale</span>.ai</div><div class="footer-tagline">AI Growth Systems For Law Firms</div></div>
    <div class="footer-links">
      <a href="/ai-website-design-for-law-firms.html">AI Website Design</a>
      <a href="/ai-seo-for-law-firms.html">AI SEO</a>
      <a href="/ai-receptionist-for-law-firms.html">AI Receptionist</a>
      <a href="/ai-chatbot-for-law-firms.html">AI Chatbot</a>
      <a href="/about.html">About</a>
      <a href="/insights/chatgpt.html">Insights</a>
      <a href="/privacy.html">Privacy</a>
      <a href="/privacy.html">Terms</a>
    </div>
    <div class="footer-copy">&copy; 2026 LexScale.ai &middot; All rights reserved</div>
  </div>
  <p style="text-align:center;padding:8px 0;font-size:12px;color:rgba(255,255,255,.35);"><a href="/contact.html" style="color:rgba(255,255,255,.45);text-decoration:none;margin:0 8px;">Contact</a> &middot; <a href="/privacy.html" style="color:rgba(255,255,255,.45);text-decoration:none;margin:0 8px;">Privacy Policy</a></p>
</footer>'''

STICKY_AND_MODAL = '''<div id="stickyCTA" style="position:fixed;bottom:0;left:0;right:0;z-index:500;background:linear-gradient(135deg,var(--navy),#1a2456);padding:14px 24px;display:flex;align-items:center;justify-content:space-between;box-shadow:0 -4px 24px rgba(11,21,54,.2);transform:translateY(100%);transition:transform .4s;">
  <div style="color:#fff;font-size:14px;font-weight:600;">Is your firm visible in AI search?</div>
  <button onclick="document.getElementById('leadModal').style.display='flex'" style="background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;border:none;padding:10px 22px;border-radius:100px;font-size:13px;font-weight:700;cursor:pointer;font-family:inherit;white-space:nowrap;">Get Free Report &rarr;</button>
</div>
<script>setTimeout(function(){document.getElementById('stickyCTA').style.transform='translateY(0)';},3000);</script>
<div id="leadModal" style="display:none;position:fixed;inset:0;z-index:1000;background:rgba(11,21,54,.7);backdrop-filter:blur(6px);align-items:center;justify-content:center;padding:20px;">
  <div style="background:#fff;border-radius:24px;padding:40px;max-width:480px;width:100%;position:relative;box-shadow:0 32px 80px rgba(11,21,54,.25);">
    <button onclick="document.getElementById('leadModal').style.display='none'" style="position:absolute;top:16px;right:16px;background:none;border:none;cursor:pointer;color:#94a3b8;font-size:22px;">&times;</button>
    <div style="font-size:11px;font-weight:700;color:var(--pu);letter-spacing:.8px;text-transform:uppercase;margin-bottom:8px;">Free AI Visibility Report</div>
    <h3 style="font-size:22px;font-weight:800;color:var(--navy);letter-spacing:-.5px;margin-bottom:6px;">See How Your Firm Ranks in AI Search</h3>
    <p style="font-size:13px;color:#64748b;line-height:1.6;margin-bottom:22px;">Get a free report showing your firm\'s visibility across ChatGPT, Gemini, and Perplexity.</p>
    <input type="text" placeholder="Your Name" style="width:100%;padding:12px 16px;border:1.5px solid rgba(11,21,54,.12);border-radius:10px;font-size:14px;font-family:inherit;margin-bottom:10px;outline:none;">
    <input type="email" placeholder="Work Email" style="width:100%;padding:12px 16px;border:1.5px solid rgba(11,21,54,.12);border-radius:10px;font-size:14px;font-family:inherit;margin-bottom:10px;outline:none;">
    <input type="text" placeholder="Law Firm Name" style="width:100%;padding:12px 16px;border:1.5px solid rgba(11,21,54,.12);border-radius:10px;font-size:14px;font-family:inherit;margin-bottom:16px;outline:none;">
    <button style="width:100%;background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;border:none;padding:14px;border-radius:100px;font-size:15px;font-weight:700;cursor:pointer;font-family:inherit;box-shadow:0 4px 20px rgba(106,92,255,.35);">Get My Free Report &rarr;</button>
  </div>
</div>
<script>
function toggleFaq(el){const item=el.closest('.faq-item');const isOpen=item.classList.contains('open');document.querySelectorAll('.faq-item.open').forEach(i=>i.classList.remove('open'));if(!isOpen)item.classList.add('open');}
function toggleMobNav(btn){const nav=btn.closest('nav');nav.classList.toggle('mob-open');}
document.addEventListener('DOMContentLoaded',function(){
  document.querySelectorAll('.has-drop>a').forEach(function(a){
    a.addEventListener('click',function(e){
      if(window.innerWidth>768)return;
      e.preventDefault();
      const li=a.closest('.has-drop');
      li.classList.toggle('mob-open');
    });
  });
  document.addEventListener('click',function(e){
    const nav=document.querySelector('nav');
    if(nav&&nav.classList.contains('mob-open')&&!nav.contains(e.target)){nav.classList.remove('mob-open');}
  });
});
</script>'''

ARROW_SVG = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>'

def card_featured(href, badge, title, desc, date, read_time):
    return f'''<a href="{href}" class="art-card featured">
  <div class="art-card-top">
    <div class="art-cat-badge"><span>{badge}</span></div>
    <div class="art-title">{title}</div>
    <div class="art-desc">{desc}</div>
  </div>
  <div class="art-meta"><span>{date}</span><span class="art-meta-dot"></span><span>{read_time}</span></div>
  <div class="art-card-footer">
    <div class="art-divider"></div>
    <span class="art-read-link">Read Article {ARROW_SVG}</span>
  </div>
  <div class="art-right"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div>
</a>'''

def card_regular(href, badge, title, desc, date, read_time):
    return f'''<a href="{href}" class="art-card">
  <div class="art-card-top">
    <div class="art-cat-badge"><span>{badge}</span></div>
    <div class="art-title">{title}</div>
    <div class="art-desc">{desc}</div>
  </div>
  <div class="art-meta"><span>{date}</span><span class="art-meta-dot"></span><span>{read_time}</span></div>
  <div class="art-card-footer">
    <div class="art-divider"></div>
    <span class="art-read-link">Read Article {ARROW_SVG}</span>
  </div>
</a>'''

def build_hub(slug, title, meta_desc, keywords, canonical, og_title, collection_name,
              tag_html, h1_html, hero_desc, hero_btn1_href, hero_btn1_text,
              stats_items, section_h2, section_p, articles, cta_h2, cta_p):
    """Build a complete hub page HTML string."""
    # schemas
    collection_schema = f'''<script type="application/ld+json">{{
  "@context":"https://schema.org",
  "@type":"CollectionPage",
  "@id":"{SITE}/{canonical}#webpage",
  "name":"{collection_name}",
  "description":"{meta_desc}",
  "url":"{SITE}/{canonical}",
  "isPartOf":{{"@id":"{SITE}/#website"}},
  "publisher":{{"@id":"{SITE}/#organization"}}
}}</script>'''

    breadcrumb_schema = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type":"ListItem","position":1,"name":"Home","item":"{SITE}"}},
    {{"@type":"ListItem","position":2,"name":"Insights","item":"{SITE}/insights"}},
    {{"@type":"ListItem","position":3,"name":"{collection_name}","item":"{SITE}/{canonical}"}}
  ]
}}
</script>'''

    # stats bar
    stat_html_parts = []
    for num, lbl in stats_items:
        stat_html_parts.append(f'<div class="stat-item"><div class="stat-num">{num}</div><div class="stat-lbl">{lbl}</div></div>')
    stats_html = ''.join(stat_html_parts)

    # articles grid
    cards_html = []
    for i, art in enumerate(articles):
        href, badge, atitle, adesc, date, read_time = art
        if i == 0:
            cards_html.append(card_featured(href, badge, atitle, adesc, date, read_time))
        else:
            cards_html.append(card_regular(href, badge, atitle, adesc, date, read_time))
    grid_html = '\n      '.join(cards_html)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{title}</title>
<meta name="description" content="{meta_desc}"/>
<meta name="keywords" content="{keywords}"/>
<link rel="canonical" href="{SITE}/{canonical}"/>
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"/>
<meta property="og:type" content="website"/>
<meta property="og:title" content="{og_title}"/>
<meta property="og:description" content="{meta_desc}"/>
<meta property="og:url" content="{SITE}/{canonical}"/>
<meta property="og:image" content="{SITE}/og-image.png"/>
<meta property="og:site_name" content="LexScale.ai"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{og_title}"/>
<meta name="twitter:description" content="{meta_desc}"/>
<meta name="twitter:image" content="{SITE}/og-image.png"/>
{collection_schema}
{breadcrumb_schema}
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"/>
{CSS}
</head>
<body>

{NAV_FULL}

<section class="hub-hero">
  <div class="grid-bg"></div>
  <div class="hub-hero-inner">
    {tag_html}
    <h1 class="hub-h1">{h1_html}</h1>
    <p class="hub-desc">{hero_desc}</p>
    <div class="hub-btns">
      <a href="{hero_btn1_href}" class="btn-primary">{hero_btn1_text}</a>
      <a href="/" class="btn-outline">View All Services</a>
    </div>
  </div>
</section>

<div class="stats-bar">
  <div class="stats-inner">
    {stats_html}
  </div>
</div>

<section class="articles-section">
  <div class="articles-inner">
    <div class="section-header">
      <h2>{section_h2}</h2>
      <p>{section_p}</p>
    </div>
    <div class="articles-grid">
      {grid_html}
    </div>
  </div>
</section>

<section class="cta-banner">
  <div class="grid-bg"></div>
  <div class="cta-inner">
    <h2>{cta_h2}</h2>
    <p>{cta_p}</p>
    <button class="btn-primary" onclick="document.getElementById('leadModal').style.display='flex'" style="border:none;cursor:pointer;font-family:inherit;">Get My Free Report &rarr;</button>
  </div>
</section>

{FOOTER_HTML}
{STICKY_AND_MODAL}
</body>
</html>'''


# ============================================================
# CHATGPT HUB (29 articles)
# ============================================================
chatgpt_articles = [
    ("/insights/chatgpt/chatgpt-for-law-firms.html","ChatGPT","ChatGPT for Law Firms: The Complete 2026 Guide","Everything your law firm needs to know about ChatGPT — how it works, how it recommends lawyers, and how to get your firm cited in AI responses.","June 2025","10 min read"),
    ("/insights/chatgpt/why-chatgpt-matters-for-law-firms.html","ChatGPT","Why ChatGPT Matters for Law Firms in 2026","Millions of potential clients now use ChatGPT to find legal help. Discover why AI search visibility is the most important marketing channel for law firms right now.","March 2025","8 min read"),
    ("/insights/chatgpt/how-chatgpt-finds-and-recommends-law-firms.html","ChatGPT","How ChatGPT Finds and Recommends Law Firms","Learn exactly how ChatGPT sources law firm recommendations — and the key factors that determine whether your firm gets cited or ignored.","March 2025","9 min read"),
    ("/insights/chatgpt/how-law-firms-can-rank-in-chatgpt.html","ChatGPT","How Law Firms Can Rank in ChatGPT","A practical, actionable guide to getting your law firm recommended in ChatGPT responses — from content strategy to authority signals.","March 2025","12 min read"),
    ("/insights/chatgpt/chatgpt-vs-google-search-for-lawyers.html","ChatGPT","ChatGPT vs Google Search for Lawyers: Key Differences","ChatGPT and Google rank law firms differently. Understand both systems and learn how to optimize your firm's presence on each platform.","March 2025","11 min read"),
    ("/insights/chatgpt/chatgpt-seo-for-lawyers.html","ChatGPT","ChatGPT SEO for Lawyers: What Actually Works in 2026","The complete guide to ChatGPT SEO for law firms — covering entity optimization, authority signals, and the content strategy that gets results.","March 2025","13 min read"),
    ("/insights/chatgpt/best-practices-optimizing-law-firm-websites-for-chatgpt.html","ChatGPT","Best Practices for Optimizing Your Law Firm Website for ChatGPT","Technical and content best practices to make your law firm website more visible to ChatGPT and other AI search platforms.","March 2025","10 min read"),
    ("/insights/chatgpt/chatgpt-citations-explained.html","ChatGPT","ChatGPT Citations Explained: How Law Firms Get Referenced","Understand exactly how ChatGPT citation and sourcing works — and what your firm needs to do to earn consistent references in AI responses.","March 2025","9 min read"),
    ("/insights/chatgpt/future-of-chatgpt-and-legal-marketing.html","ChatGPT","The Future of ChatGPT and Legal Marketing","Where is AI-powered legal marketing heading? A forward-looking analysis of ChatGPT, AI search, and what law firms must do to stay ahead.","March 2025","11 min read"),
    ("/insights/chatgpt/chatgpt-search-for-lawyers.html","ChatGPT","ChatGPT Search for Lawyers: How to Get Found","ChatGPT Search is now a primary discovery channel for legal services. Learn what it is, how it ranks law firms, and how to dominate it.","June 2026","11 min read"),
    ("/insights/chatgpt/law-firm-chatgpt-visibility-audit.html","ChatGPT","Law Firm ChatGPT Visibility Audit: A Step-by-Step Guide","A complete step-by-step audit process to measure and improve your law firm's visibility across ChatGPT and other AI search engines.","June 2026","13 min read"),
    ("/insights/chatgpt/chatgpt-local-search-law-firms.html","ChatGPT","ChatGPT Local Search for Law Firms: A Complete Guide","How ChatGPT handles local legal searches — and how to ensure your law firm dominates 'lawyers near me' queries in AI search responses.","June 2026","12 min read"),
    ("/insights/chatgpt/chatgpt-content-for-law-firms.html","ChatGPT","ChatGPT Content Strategy for Law Firms","The content strategy that gets law firms recommended in ChatGPT — covering topic clusters, FAQ pages, and AI-optimized writing.","June 2026","14 min read"),
    ("/insights/chatgpt/chatgpt-personal-injury-lawyers.html","ChatGPT","ChatGPT for Personal Injury Lawyers: Get More Clients","How personal injury law firms can leverage ChatGPT visibility to attract more clients and dominate AI-powered legal searches.","June 2026","12 min read"),
    ("/insights/chatgpt/chatgpt-family-law-firms.html","ChatGPT","ChatGPT for Family Law Firms: Attract More Clients","Family law clients increasingly use ChatGPT to find attorneys. Learn how to position your firm as the top recommendation for family law.","June 2026","11 min read"),
    ("/insights/chatgpt/chatgpt-criminal-defense-lawyers.html","ChatGPT","ChatGPT for Criminal Defense Lawyers: Visibility Guide","Criminal defense clients need help fast — and they're asking ChatGPT. Learn how criminal defense firms can dominate AI search results.","June 2026","12 min read"),
    ("/insights/chatgpt/chatgpt-immigration-lawyers.html","ChatGPT","ChatGPT for Immigration Lawyers: AI Visibility Tactics","Immigration clients search ChatGPT across languages and jurisdictions. Here's how immigration law firms can maximize their AI visibility.","June 2026","11 min read"),
    ("/insights/chatgpt/chatgpt-estate-planning-lawyers.html","ChatGPT","ChatGPT for Estate Planning Lawyers: Get Recommended","Estate planning clients ask thoughtful questions — and ChatGPT answers them. Learn how estate planning firms get cited in AI responses.","June 2026","10 min read"),
    ("/insights/chatgpt/chatgpt-business-lawyers.html","ChatGPT","ChatGPT for Business Lawyers: Corporate AI Visibility","Business owners use ChatGPT to find corporate counsel. Learn how business and corporate law firms build AI search authority.","June 2026","11 min read"),
    ("/insights/chatgpt/chatgpt-real-estate-lawyers.html","ChatGPT","ChatGPT for Real Estate Lawyers: AI Search Guide","Real estate clients ask ChatGPT for legal guidance every day. Discover how real estate law firms can dominate these AI-powered queries.","June 2026","10 min read"),
    ("/insights/chatgpt/how-chatgpt-ranks-law-firm-websites.html","ChatGPT","How ChatGPT Ranks Law Firm Websites: The Algorithm Explained","A deep dive into the signals and factors ChatGPT uses to evaluate and rank law firm websites when answering legal questions.","June 2026","13 min read"),
    ("/insights/chatgpt/chatgpt-google-business-profile-law-firms.html","ChatGPT","ChatGPT and Google Business Profile for Law Firms","Your Google Business Profile is a key signal for ChatGPT local recommendations. Learn how to optimize your GBP for AI search citations.","June 2026","10 min read"),
    ("/insights/chatgpt/chatgpt-reviews-law-firms.html","ChatGPT","ChatGPT Reviews Strategy for Law Firms","Online reviews influence ChatGPT recommendations more than most firms realize. Learn the review strategy that maximizes your AI visibility.","June 2026","9 min read"),
    ("/insights/chatgpt/chatgpt-schema-markup-law-firms.html","ChatGPT","ChatGPT and Schema Markup for Law Firms","Structured data and schema markup help ChatGPT understand and recommend your firm. Here's the complete implementation guide for law firms.","June 2026","11 min read"),
    ("/insights/chatgpt/chatgpt-legal-content-writing.html","ChatGPT","ChatGPT-Ready Legal Content Writing for Law Firms","How to write legal content that ChatGPT will cite — covering format, structure, authority signals, and topical depth for law firms.","June 2026","12 min read"),
    ("/insights/chatgpt/chatgpt-law-firm-faq-strategy.html","ChatGPT","ChatGPT FAQ Strategy for Law Firms","FAQ pages are one of the highest-value assets for ChatGPT visibility. Learn how to build an FAQ strategy that gets your firm recommended.","June 2026","10 min read"),
    ("/insights/chatgpt/chatgpt-backlinks-law-firms.html","ChatGPT","Backlinks and ChatGPT Visibility for Law Firms","Authority links still matter for ChatGPT. Learn which types of backlinks improve your firm's AI search visibility and how to earn them.","June 2026","11 min read"),
    ("/insights/chatgpt/measuring-chatgpt-visibility-law-firms.html","ChatGPT","Measuring ChatGPT Visibility for Law Firms","How to track, measure, and report on your law firm's ChatGPT visibility — including tools, prompts, and KPIs to monitor progress.","June 2026","10 min read"),
    ("/insights/chatgpt/chatgpt-law-firm-roi.html","ChatGPT","ChatGPT ROI for Law Firms: Measuring What Matters","How to calculate the real ROI of ChatGPT visibility investment — and the metrics that prove AI search is driving clients to your firm.","June 2026","11 min read"),
]

chatgpt_hub = build_hub(
    slug="insights/chatgpt.html",
    title="ChatGPT for Law Firms — AI Visibility Hub | LexScale.ai",
    meta_desc="Expert guides on how law firms can appear in ChatGPT responses. 29 in-depth articles on AI search optimization, content strategy, and local AI visibility for attorneys.",
    keywords="ChatGPT for law firms, ChatGPT SEO for lawyers, law firm AI visibility, ChatGPT legal marketing",
    canonical="insights/chatgpt.html",
    og_title="ChatGPT for Law Firms — AI Visibility Hub",
    collection_name="ChatGPT for Law Firms",
    tag_html='<div class="hub-tag"><span>ChatGPT</span></div>',
    h1_html='ChatGPT Insights for <span class="accent">Law Firms</span>',
    hero_desc="Expert guides on how law firms can get recommended by ChatGPT — the AI search engine now used by millions of people looking for legal help every day.",
    hero_btn1_href="/ai-seo-for-law-firms.html",
    hero_btn1_text="Get AI Visible Now &rarr;",
    stats_items=[("180M+","ChatGPT users globally"),("29","in-depth articles"),("10 min","average read time"),("2026","fully up to date")],
    section_h2="All ChatGPT Articles",
    section_p="In-depth guides to help your law firm get recommended by ChatGPT and win more clients from AI search.",
    articles=chatgpt_articles,
    cta_h2="Is Your Firm Visible in ChatGPT?",
    cta_p="Get a free AI Visibility Report and see exactly where your law firm stands — and what it takes to get recommended.",
)

# ============================================================
# AI SEO HUB (16 articles)
# ============================================================
ai_seo_articles = [
    ("/insights/ai-seo/ai-seo-for-law-firms-complete-guide.html","AI SEO","AI SEO for Law Firms: The Complete 2026 Guide","The definitive guide to AI SEO for law firms — covering how ChatGPT, Gemini, and Perplexity rank attorneys and how to dominate every platform.","March 2025","12 min read"),
    ("/insights/ai-seo/how-ai-search-is-changing-legal-marketing.html","AI SEO","How AI Search Is Changing Legal Marketing Forever","AI is fundamentally reshaping how clients find lawyers. Understand the shift and what law firms must do to compete in the AI search era.","March 2025","10 min read"),
    ("/insights/ai-seo/ai-seo-vs-traditional-seo-lawyers.html","AI SEO","AI SEO vs Traditional SEO for Lawyers: Key Differences","Traditional SEO and AI SEO are fundamentally different. Learn which tactics still work, which are obsolete, and what to prioritize for 2026.","March 2025","11 min read"),
    ("/insights/ai-seo/how-google-ai-overviews-affect-law-firms.html","AI SEO","How Google AI Overviews Affect Law Firms","Google AI Overviews are changing search traffic patterns for law firms. Learn how they work and how to earn citations in AI-generated results.","March 2025","9 min read"),
    ("/insights/ai-seo/local-ai-seo-for-law-firms.html","AI SEO","Local AI SEO for Law Firms: Get Found in Your City","How to dominate local AI search results — getting your law firm recommended in ChatGPT, Gemini, and Perplexity for local legal queries.","March 2025","11 min read"),
    ("/insights/ai-seo/common-mistakes-law-firms-make-with-ai-search.html","AI SEO","Common AI Search Mistakes Law Firms Make","Avoid the costly AI search mistakes that are keeping law firms invisible in ChatGPT and Gemini — and how to fix them fast.","March 2025","8 min read"),
    ("/insights/ai-seo/ai-seo-keyword-strategy-law-firms.html","AI SEO","AI SEO Keyword Strategy for Law Firms","How to build a keyword strategy optimized for AI search — including entity-based keywords, conversational queries, and intent mapping.","June 2026","12 min read"),
    ("/insights/ai-seo/ai-seo-link-building-law-firms.html","AI SEO","AI SEO Link Building for Law Firms","Which backlinks still drive AI search visibility in 2026 — and the link-building tactics that help law firms earn AI citations consistently.","June 2026","11 min read"),
    ("/insights/ai-seo/ai-seo-for-personal-injury-lawyers.html","AI SEO","AI SEO for Personal Injury Lawyers","A complete AI SEO playbook for personal injury law firms — how to dominate ChatGPT and Gemini for high-value injury law queries.","June 2026","12 min read"),
    ("/insights/ai-seo/ai-seo-for-family-lawyers.html","AI SEO","AI SEO for Family Lawyers","How family law firms can build AI search visibility across ChatGPT, Gemini, and Perplexity — and attract more clients in 2026.","June 2026","11 min read"),
    ("/insights/ai-seo/technical-ai-seo-for-law-firms.html","AI SEO","Technical AI SEO for Law Firms: A Complete Guide","The technical foundation of AI search visibility — schema markup, site structure, Core Web Vitals, and entity signals for law firms.","June 2026","13 min read"),
    ("/insights/ai-seo/ai-seo-content-calendar-law-firms.html","AI SEO","AI SEO Content Calendar for Law Firms","How to plan, produce, and publish AI-optimized content at scale — a complete content calendar framework for law firm AI SEO.","June 2026","10 min read"),
    ("/insights/ai-seo/ai-seo-for-criminal-defense-lawyers.html","AI SEO","AI SEO for Criminal Defense Lawyers","Criminal defense clients need immediate help — and they're asking AI. Learn how criminal defense firms dominate AI search results.","June 2026","11 min read"),
    ("/insights/ai-seo/ai-seo-google-business-profile-law-firms.html","AI SEO","Google Business Profile AI SEO for Law Firms","Your GBP is a critical signal for AI search. Learn how to optimize your Google Business Profile for maximum AI visibility in 2026.","June 2026","10 min read"),
    ("/insights/ai-seo/ai-seo-reporting-law-firms.html","AI SEO","AI SEO Reporting for Law Firms: Metrics That Matter","How to measure and report on AI search performance — the KPIs, tools, and reporting frameworks law firms need to track progress.","June 2026","10 min read"),
    ("/insights/ai-seo/ai-seo-for-immigration-lawyers.html","AI SEO","AI SEO for Immigration Lawyers","Immigration law clients search across languages and borders. Learn how immigration firms build AI visibility that attracts more consultations.","June 2026","11 min read"),
]

ai_seo_hub = build_hub(
    slug="insights/ai-seo.html",
    title="AI SEO for Law Firms — Complete Guide Hub | LexScale.ai",
    meta_desc="16 in-depth AI SEO guides for law firms. Learn how to rank in ChatGPT, Google Gemini, and Perplexity — and turn AI search visibility into more clients.",
    keywords="AI SEO for law firms, law firm AI search, AI SEO lawyers, legal AI marketing 2026",
    canonical="insights/ai-seo.html",
    og_title="AI SEO for Law Firms — Complete Guide Hub",
    collection_name="AI SEO for Law Firms",
    tag_html='<div class="hub-tag"><span>AI SEO</span></div>',
    h1_html='AI SEO Insights for <span class="accent">Law Firms</span>',
    hero_desc="Expert guides on AI SEO for law firms — how to rank in ChatGPT, Google Gemini, and Perplexity, and turn AI search visibility into a steady stream of new clients.",
    hero_btn1_href="/ai-seo-for-law-firms.html",
    hero_btn1_text="Get AI Visible Now &rarr;",
    stats_items=[("3","major AI search engines"),("16","in-depth articles"),("11 min","average read time"),("2026","fully up to date")],
    section_h2="All AI SEO Articles",
    section_p="Everything your law firm needs to dominate AI search across ChatGPT, Google Gemini, and Perplexity.",
    articles=ai_seo_articles,
    cta_h2="Ready to Dominate AI Search?",
    cta_p="Get a free AI Visibility Report and see exactly where your law firm ranks in ChatGPT, Gemini, and Perplexity — and what it takes to reach the top.",
)

# ============================================================
# AI WEBSITES HUB (10 articles)
# ============================================================
ai_websites_articles = [
    ("/insights/ai-websites/ai-website-design-for-law-firms-guide.html","AI Websites","AI Website Design for Law Firms: The Complete Guide","Everything your law firm needs to know about AI-powered website design — from conversion optimization to AI search compatibility.","March 2025","10 min read"),
    ("/insights/ai-websites/why-law-firms-need-ai-websites.html","AI Websites","Why Law Firms Need AI-Powered Websites in 2026","Traditional websites no longer cut it. Discover why AI-powered websites are the new standard for law firms that want to attract and convert clients.","June 2026","9 min read"),
    ("/insights/ai-websites/law-firm-website-trust-signals.html","AI Websites","Law Firm Website Trust Signals That Convert Visitors","The trust signals that turn law firm website visitors into consultations — credibility indicators, social proof, and authority elements.","June 2026","10 min read"),
    ("/insights/ai-websites/law-firm-website-content-strategy.html","AI Websites","Law Firm Website Content Strategy for AI Search","How to structure and write your law firm website content to rank in both traditional Google search and AI-powered search engines.","June 2026","12 min read"),
    ("/insights/ai-websites/law-firm-website-lead-generation.html","AI Websites","Law Firm Website Lead Generation: Convert More Visitors","The lead generation tactics, CTAs, and conversion strategies that turn law firm website visitors into qualified consultation requests.","June 2026","11 min read"),
    ("/insights/ai-websites/law-firm-homepage-design.html","AI Websites","Law Firm Homepage Design: What Works in 2026","A complete guide to designing a law firm homepage that builds trust, converts visitors, and signals authority to both humans and AI.","June 2026","10 min read"),
    ("/insights/ai-websites/law-firm-website-seo-structure.html","AI Websites","Law Firm Website SEO Structure: Architecture That Ranks","How to structure your law firm website for maximum SEO impact — URL architecture, silo structure, and internal linking for AI search.","March 2025","11 min read"),
    ("/insights/ai-websites/law-firm-website-speed-performance.html","AI Websites","Law Firm Website Speed and Performance Optimization","Page speed is a ranking factor for AI and traditional search. Learn how to optimize your law firm website for maximum speed.","March 2025","9 min read"),
    ("/insights/ai-websites/law-firm-website-conversion-optimization.html","AI Websites","Law Firm Website Conversion Optimization Guide","How to systematically improve your law firm website's conversion rate — from layout and copy to forms and follow-up sequences.","March 2025","11 min read"),
    ("/insights/ai-websites/mobile-first-law-firm-website.html","AI Websites","Mobile-First Law Firm Website Design Guide","Most legal searches happen on mobile. Learn how to design and optimize a mobile-first law firm website that ranks and converts.","March 2025","10 min read"),
]

ai_websites_hub = build_hub(
    slug="insights/ai-websites.html",
    title="AI Websites for Law Firms — Design & Strategy Hub | LexScale.ai",
    meta_desc="10 expert guides on AI-powered website design for law firms. Learn how to build a law firm website that ranks in AI search and converts more visitors into clients.",
    keywords="AI website design for law firms, law firm website, legal website design, AI law firm website 2026",
    canonical="insights/ai-websites.html",
    og_title="AI Websites for Law Firms — Design & Strategy Hub",
    collection_name="AI Websites for Law Firms",
    tag_html='<div class="hub-tag"><span>AI Websites</span></div>',
    h1_html='AI Website Insights for <span class="accent">Law Firms</span>',
    hero_desc="Expert guides on building AI-powered law firm websites that rank in ChatGPT and Google, convert visitors into clients, and establish your firm's authority online.",
    hero_btn1_href="/ai-website-design-for-law-firms.html",
    hero_btn1_text="See AI Website Design &rarr;",
    stats_items=[("10","in-depth articles"),("3x","more leads than traditional sites"),("10 min","average read time"),("2026","fully up to date")],
    section_h2="All AI Website Articles",
    section_p="Everything your law firm needs to build a website that ranks in AI search and converts more visitors into consultations.",
    articles=ai_websites_articles,
    cta_h2="Ready for an AI-Powered Law Firm Website?",
    cta_p="Get a free website audit and see how your law firm's website compares to the best in your market — and what it takes to outrank them.",
)

# ============================================================
# PERPLEXITY HUB (3 articles)
# ============================================================
perplexity_articles = [
    ("/insights/perplexity/what-is-perplexity-ai-for-law-firms.html","Perplexity","What Is Perplexity AI and Why Should Law Firms Care?","Perplexity AI is the fastest-growing AI search engine — and it's recommending law firms right now. Learn what it is and how it works.","March 2025","8 min read"),
    ("/insights/perplexity/how-perplexity-ai-ranks-law-firms.html","Perplexity","How Perplexity AI Ranks and Recommends Law Firms","Discover the signals Perplexity uses to recommend law firms — and the optimization tactics that get your firm cited consistently.","March 2025","10 min read"),
    ("/insights/perplexity/how-to-rank-in-perplexity-ai.html","Perplexity","How to Rank in Perplexity AI: A Guide for Law Firms","A step-by-step guide to getting your law firm recommended in Perplexity AI responses — covering content, authority, and technical signals.","March 2025","11 min read"),
]

perplexity_hub = build_hub(
    slug="insights/perplexity.html",
    title="Perplexity AI for Law Firms — AI Visibility Hub | LexScale.ai",
    meta_desc="How law firms can appear in Perplexity AI responses. Expert guides on Perplexity optimization, citation signals, and AI search visibility for attorneys.",
    keywords="Perplexity AI for law firms, Perplexity for lawyers, law firm AI visibility, Perplexity legal marketing",
    canonical="insights/perplexity.html",
    og_title="Perplexity AI for Law Firms — AI Visibility Hub",
    collection_name="Perplexity AI for Law Firms",
    tag_html='<div class="hub-tag" style="background:rgba(32,184,205,.1);border-color:rgba(32,184,205,.3);"><span style="color:#20B8CD;">Perplexity AI</span></div>',
    h1_html='Perplexity AI Insights for <span class="accent" style="background:linear-gradient(135deg,#20B8CD,#20b8cdcc);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">Law Firms</span>',
    hero_desc="Expert guides on how law firms can get recommended by Perplexity AI — the AI-native search engine that's reshaping how clients find legal help.",
    hero_btn1_href="/ai-seo-for-law-firms.html",
    hero_btn1_text="Get AI Visible Now &rarr;",
    stats_items=[("100M+","Perplexity monthly queries"),("3","in-depth articles"),("10 min","average read time"),("2026","fully up to date")],
    section_h2="All Perplexity AI Articles",
    section_p="In-depth guides to help your law firm get recommended by Perplexity AI and win more clients from AI-native search.",
    articles=perplexity_articles,
    cta_h2="Is Your Firm Visible in Perplexity AI?",
    cta_p="Get a free AI Visibility Report and see how your law firm ranks across Perplexity, ChatGPT, and Gemini — and what to do next.",
)

# ============================================================
# AI RECEPTIONISTS HUB (5 articles)
# ============================================================
ai_rec_articles = [
    ("/insights/ai-receptionists/what-is-an-ai-receptionist-for-law-firms.html","AI Receptionists","What Is an AI Receptionist for Law Firms?","A complete introduction to AI receptionists for law firms — how they work, what they do, and why they're becoming essential for modern practices.","March 2025","8 min read"),
    ("/insights/ai-receptionists/never-miss-a-call-law-firm.html","AI Receptionists","Never Miss a Call: AI Receptionists for Law Firms","Every missed call is a missed client. Learn how AI receptionists ensure your law firm answers every inquiry — 24/7, instantly.","March 2025","9 min read"),
    ("/insights/ai-receptionists/how-ai-receptionists-increase-law-firm-revenue.html","AI Receptionists","How AI Receptionists Increase Law Firm Revenue","The ROI of AI receptionists for law firms — from reduced overhead to higher intake conversion rates and more retained clients.","March 2025","10 min read"),
    ("/insights/ai-receptionists/ai-receptionist-vs-human-receptionist.html","AI Receptionists","AI Receptionist vs Human Receptionist for Law Firms","A detailed comparison of AI receptionists vs human staff for law firms — cost, quality, availability, and when to use each.","March 2025","9 min read"),
    ("/insights/ai-receptionists/ai-receptionist-intake-automation.html","AI Receptionists","AI Receptionist Intake Automation for Law Firms","How AI receptionists automate the entire client intake process — from first call to qualified lead, without human intervention.","March 2025","11 min read"),
]

ai_rec_hub = build_hub(
    slug="insights/ai-receptionists.html",
    title="AI Receptionists for Law Firms — Complete Guide Hub | LexScale.ai",
    meta_desc="5 expert guides on AI receptionists for law firms. Learn how AI answering services can handle intake, book consultations, and convert more callers into clients 24/7.",
    keywords="AI receptionist for law firms, law firm answering service, AI intake for lawyers, 24/7 law firm receptionist",
    canonical="insights/ai-receptionists.html",
    og_title="AI Receptionists for Law Firms — Complete Guide Hub",
    collection_name="AI Receptionists for Law Firms",
    tag_html='<div class="hub-tag"><span>AI Receptionists</span></div>',
    h1_html='AI Receptionist Insights for <span class="accent">Law Firms</span>',
    hero_desc="Expert guides on AI receptionists for law firms — how they work, how they increase revenue, and how to implement 24/7 AI answering to convert more callers into clients.",
    hero_btn1_href="/ai-receptionist-for-law-firms.html",
    hero_btn1_text="See AI Receptionist &rarr;",
    stats_items=[("24/7","availability — never miss a call"),("5","in-depth articles"),("9 min","average read time"),("2026","fully up to date")],
    section_h2="All AI Receptionist Articles",
    section_p="Everything your law firm needs to know about AI receptionists — from how they work to how they drive more clients and revenue.",
    articles=ai_rec_articles,
    cta_h2="Ready to Never Miss Another Call?",
    cta_p="Get a free consultation and see how an AI receptionist can transform your law firm's intake process and increase revenue.",
)

# ============================================================
# AI CHATBOTS HUB (5 articles)
# ============================================================
ai_chatbot_articles = [
    ("/insights/ai-chatbots/ai-chatbot-for-law-firm-website.html","AI Chatbots","AI Chatbot for Your Law Firm Website: Complete Guide","Everything you need to know about adding an AI chatbot to your law firm website — how they work, what they cost, and how they convert.","March 2025","9 min read"),
    ("/insights/ai-chatbots/how-ai-chatbots-convert-legal-leads.html","AI Chatbots","How AI Chatbots Convert Legal Website Visitors Into Leads","AI chatbots engage visitors the moment they land on your website. Learn how they qualify leads and book consultations automatically.","March 2025","10 min read"),
    ("/insights/ai-chatbots/ai-chatbot-intake-qualification.html","AI Chatbots","AI Chatbot Intake and Lead Qualification for Law Firms","How AI chatbots pre-qualify leads before they ever speak to an attorney — saving time and ensuring only the right clients get through.","March 2025","10 min read"),
    ("/insights/ai-chatbots/ai-chatbot-vs-live-chat-lawyers.html","AI Chatbots","AI Chatbot vs Live Chat for Law Firms: Honest Comparison","AI chatbot or live chat — which is right for your law firm? A detailed comparison of cost, conversion rates, and client experience.","March 2025","8 min read"),
    ("/insights/ai-chatbots/ai-chatbot-roi-for-law-firms.html","AI Chatbots","AI Chatbot ROI for Law Firms: Calculating the Returns","How to calculate the real ROI of an AI chatbot for your law firm — and the metrics that prove it's generating more revenue than it costs.","March 2025","9 min read"),
]

ai_chatbot_hub = build_hub(
    slug="insights/ai-chatbots.html",
    title="AI Chatbots for Law Firms — Complete Guide Hub | LexScale.ai",
    meta_desc="5 expert guides on AI chatbots for law firms. Learn how AI chat converts website visitors into clients, automates intake, and delivers ROI 24/7.",
    keywords="AI chatbot for law firms, law firm chatbot, legal chatbot, AI chat for lawyers",
    canonical="insights/ai-chatbots.html",
    og_title="AI Chatbots for Law Firms — Complete Guide Hub",
    collection_name="AI Chatbots for Law Firms",
    tag_html='<div class="hub-tag"><span>AI Chatbots</span></div>',
    h1_html='AI Chatbot Insights for <span class="accent">Law Firms</span>',
    hero_desc="Expert guides on AI chatbots for law firms — how they work, how they qualify leads, and how to add one to your website to convert more visitors into clients 24/7.",
    hero_btn1_href="/ai-chatbot-for-law-firms.html",
    hero_btn1_text="See AI Chatbot &rarr;",
    stats_items=[("24/7","client engagement — never offline"),("5","in-depth articles"),("9 min","average read time"),("2026","fully up to date")],
    section_h2="All AI Chatbot Articles",
    section_p="Everything your law firm needs to know about AI chatbots — from how they work to how they convert visitors and pay for themselves.",
    articles=ai_chatbot_articles,
    cta_h2="Ready to Convert More Website Visitors?",
    cta_p="Get a free consultation and see how an AI chatbot can turn your law firm website into a 24/7 client acquisition machine.",
)

# ============================================================
# ENTITY SEO HUB (6 articles)
# ============================================================
entity_seo_articles = [
    ("/insights/entity-seo/what-is-entity-seo-for-law-firms.html","Entity SEO","What Is Entity SEO for Law Firms?","Entity SEO is the foundation of AI search visibility. Learn how search engines understand entities and why it matters for law firms in 2026.","March 2025","9 min read"),
    ("/insights/entity-seo/entity-seo-vs-keyword-seo.html","Entity SEO","Entity SEO vs Keyword SEO for Lawyers: The Key Differences","How entity-based SEO differs from traditional keyword SEO — and why law firms that ignore entity optimization are falling behind in AI search.","March 2025","10 min read"),
    ("/insights/entity-seo/schema-markup-for-lawyers-guide.html","Entity SEO","Schema Markup for Lawyers: The Complete Implementation Guide","A complete guide to implementing schema markup on your law firm website — the structured data that helps AI understand and recommend your firm.","March 2025","12 min read"),
    ("/insights/entity-seo/local-business-schema-law-firms.html","Entity SEO","Local Business Schema for Law Firms: Setup and Optimization","How to implement LocalBusiness schema for your law firm — the structured data that boosts local AI visibility and helps you appear in map results.","March 2025","10 min read"),
    ("/insights/entity-seo/attorney-knowledge-panel-optimization.html","Entity SEO","Attorney Knowledge Panel Optimization Guide","How to claim, build, and optimize a Google Knowledge Panel for your law firm and attorneys — the entity signal that AI relies on most.","March 2025","11 min read"),
    ("/insights/entity-seo/topical-authority-for-law-firms.html","Entity SEO","Topical Authority for Law Firms: How to Build It","How to establish your law firm as the topical authority in your practice areas — the content and link strategy that makes AI search engines trust you.","March 2025","12 min read"),
]

entity_seo_hub = build_hub(
    slug="insights/entity-seo.html",
    title="Entity SEO & Structured Data for Law Firms | LexScale.ai",
    meta_desc="6 expert guides on entity SEO and structured data for law firms. Learn schema markup, knowledge panels, and topical authority to dominate AI search in 2026.",
    keywords="entity SEO for law firms, schema markup for lawyers, structured data legal, knowledge panel attorney",
    canonical="insights/entity-seo.html",
    og_title="Entity SEO & Structured Data for Law Firms",
    collection_name="Entity SEO & Structured Data for Law Firms",
    tag_html='<div class="hub-tag"><span>Entity SEO</span></div>',
    h1_html='Entity SEO & Structured Data for <span class="accent">Law Firms</span>',
    hero_desc="Expert guides on entity SEO and structured data for law firms — the technical foundation that helps ChatGPT, Gemini, and Perplexity understand and recommend your firm.",
    hero_btn1_href="/ai-seo-for-law-firms.html",
    hero_btn1_text="Get AI Visible Now &rarr;",
    stats_items=[("6","in-depth articles"),("3","AI engines benefit"),("11 min","average read time"),("2026","fully up to date")],
    section_h2="All Entity SEO Articles",
    section_p="Everything your law firm needs to know about entity SEO, schema markup, and structured data — the signals AI search engines rely on most.",
    articles=entity_seo_articles,
    cta_h2="Is Your Firm's Entity Optimized for AI Search?",
    cta_p="Get a free AI Visibility Report and see how AI search engines understand your law firm — and what it takes to earn more recommendations.",
)

# ============================================================
# WRITE ALL FILES
# ============================================================
pages = [
    ("insights/chatgpt.html", chatgpt_hub),
    ("insights/ai-seo.html", ai_seo_hub),
    ("insights/ai-websites.html", ai_websites_hub),
    ("insights/perplexity.html", perplexity_hub),
    ("insights/ai-receptionists.html", ai_rec_hub),
    ("insights/ai-chatbots.html", ai_chatbot_hub),
    ("insights/entity-seo.html", entity_seo_hub),
]

for fname, html in pages:
    path = os.path.join(BASE, fname)
    with open(path, "w") as f:
        f.write(html)
    print(f"✓ {fname} written")

print("\nAll hub pages rebuilt successfully.")
