import os, json

BASE = "/home/user/muskokaspray"

NAV_INSIGHTS_DROPDOWN = '''      <div class="dropdown">
        <a href="chatgpt.html" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div><div><div class="drop-label">ChatGPT for Law Firms</div><div class="drop-sub">10 articles</div></div></a>
        <a href="google-gemini.html" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#4285f4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg></div><div><div class="drop-label">Google Gemini for Law Firms</div><div class="drop-sub">1 article</div></div></a>
        <a href="perplexity.html" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#20B8CD" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/></svg></div><div><div class="drop-label">Perplexity for Law Firms</div><div class="drop-sub">Coming soon</div></div></a>
        <div class="drop-divider"></div>
        <a href="ai-seo.html" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg></div><div><div class="drop-label">AI SEO for Law Firms</div><div class="drop-sub">5 articles</div></div></a>
        <a href="ai-receptionists.html" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 8.81 19.79 19.79 0 01.1 2.18 2 2 0 012.08 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.91 7.91a16 16 0 006.16 6.16l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg></div><div><div class="drop-label">AI Receptionists for Law Firms</div><div class="drop-sub">5 articles</div></div></a>
        <a href="ai-chatbots.html" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div><div><div class="drop-label">AI Chatbots for Law Firms</div><div class="drop-sub">5 articles</div></div></a>
        <a href="entity-seo.html" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg></div><div><div class="drop-label">Entity SEO &amp; Structured Data</div><div class="drop-sub">5 articles</div></div></a>
        <a href="ai-websites.html" class="drop-item"><div class="drop-ico"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg></div><div><div class="drop-label">AI Websites for Law Firms</div><div class="drop-sub">5 articles</div></div></a>
      </div>'''

def css_common():
    return """*{margin:0;padding:0;box-sizing:border-box;}
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
@media(max-width:768px){nav{padding:14px 20px;}.nav-links{display:none;}footer{padding:28px 20px;}.footer-inner{flex-direction:column;gap:12px;}}"""

def nav_html():
    return f"""<nav>
  <a href="index.html" class="logo">Lex<span>Scale</span>.ai</a>
  <ul class="nav-links">
    <li><a href="index.html">Home</a></li>
    <li class="has-drop"><a href="#">Services<svg class="drop-arrow" viewBox="0 0 14 14" fill="none"><path d="M3 5l4 4 4-4" stroke="#4a5568" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
      <div class="dropdown">
        <a href="ai-website-design-for-law-firms.html" class="drop-item"><div class="drop-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg></div><div><div class="drop-label">AI Website Design</div><div class="drop-sub">For law firms</div></div></a>
        <a href="ai-seo-for-law-firms.html" class="drop-item"><div class="drop-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg></div><div><div class="drop-label">AI SEO</div><div class="drop-sub">Rank higher, get cited by AI</div></div></a>
        <a href="ai-receptionist-for-law-firms.html" class="drop-item"><div class="drop-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 8.81 19.79 19.79 0 01.1 2.18 2 2 0 012.08 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.91 7.91a16 16 0 006.16 6.16l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg></div><div><div class="drop-label">AI Receptionist</div><div class="drop-sub">24/7 call answering</div></div></a>
        <a href="ai-chatbot-for-law-firms.html" class="drop-item"><div class="drop-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#6A5CFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg></div><div><div class="drop-label">AI Chatbot</div><div class="drop-sub">Convert more website visitors</div></div></a>
      </div>
    </li>
    <li><a href="about.html">About</a></li>
    <li class="has-drop"><a href="#">Insights<svg class="drop-arrow" viewBox="0 0 14 14" fill="none"><path d="M3 5l4 4 4-4" stroke="#4a5568" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
{NAV_INSIGHTS_DROPDOWN}
    </li>
  </ul>
  <button class="nav-cta" onclick="document.getElementById('leadModal').style.display='flex'">Book A Demo</button>
</nav>"""

def footer_html():
    return """<footer>
  <div class="footer-inner">
    <div><div class="footer-logo">Lex<span>Scale</span>.ai</div><div class="footer-tagline">AI Growth Systems For Law Firms</div></div>
    <div class="footer-links">
      <a href="ai-website-design-for-law-firms.html">AI Website Design</a>
      <a href="ai-seo-for-law-firms.html">AI SEO</a>
      <a href="ai-receptionist-for-law-firms.html">AI Receptionist</a>
      <a href="ai-chatbot-for-law-firms.html">AI Chatbot</a>
      <a href="about.html">About</a>
      <a href="chatgpt.html">Insights</a>
      <a href="#">Privacy</a><a href="#">Terms</a>
    </div>
    <div class="footer-copy">© 2025 LexScale.ai · All rights reserved</div>
  </div>
</footer>"""

def modal_html():
    return """<div id="leadModal" style="display:none;position:fixed;inset:0;z-index:1000;background:rgba(11,21,54,.7);backdrop-filter:blur(6px);align-items:center;justify-content:center;padding:20px;">
  <div style="background:#fff;border-radius:24px;padding:40px;max-width:480px;width:100%;position:relative;box-shadow:0 32px 80px rgba(11,21,54,.25);">
    <button onclick="document.getElementById('leadModal').style.display='none'" style="position:absolute;top:16px;right:16px;background:none;border:none;cursor:pointer;color:#94a3b8;font-size:22px;">✕</button>
    <div style="font-size:11px;font-weight:700;color:var(--pu);letter-spacing:.8px;text-transform:uppercase;margin-bottom:8px;">Free AI Visibility Report</div>
    <h3 style="font-size:22px;font-weight:800;color:var(--navy);letter-spacing:-.5px;margin-bottom:6px;">See How Your Firm Ranks in AI Search</h3>
    <p style="font-size:13px;color:#64748b;line-height:1.6;margin-bottom:22px;">Get a free report showing your firm's visibility across ChatGPT, Gemini, and Perplexity.</p>
    <input type="text" placeholder="Your Name" style="width:100%;padding:12px 16px;border:1.5px solid rgba(11,21,54,.12);border-radius:10px;font-size:14px;font-family:inherit;margin-bottom:10px;outline:none;">
    <input type="email" placeholder="Work Email" style="width:100%;padding:12px 16px;border:1.5px solid rgba(11,21,54,.12);border-radius:10px;font-size:14px;font-family:inherit;margin-bottom:10px;outline:none;">
    <input type="text" placeholder="Law Firm Name" style="width:100%;padding:12px 16px;border:1.5px solid rgba(11,21,54,.12);border-radius:10px;font-size:14px;font-family:inherit;margin-bottom:16px;outline:none;">
    <button style="width:100%;background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;border:none;padding:14px;border-radius:100px;font-size:15px;font-weight:700;cursor:pointer;font-family:inherit;">Get My Free Report →</button>
  </div>
</div>"""

def sticky_html():
    return """<div id="stickyCTA" style="position:fixed;bottom:0;left:0;right:0;z-index:500;background:linear-gradient(135deg,var(--navy),#1a2456);padding:14px 24px;display:flex;align-items:center;justify-content:space-between;box-shadow:0 -4px 24px rgba(11,21,54,.2);transform:translateY(100%);transition:transform .4s;">
  <div style="color:#fff;font-size:14px;font-weight:600;">Is your firm visible in AI search?</div>
  <button onclick="document.getElementById('leadModal').style.display='flex'" style="background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;border:none;padding:10px 22px;border-radius:100px;font-size:13px;font-weight:700;cursor:pointer;font-family:inherit;white-space:nowrap;">Get Free Report →</button>
</div>
<script>setTimeout(function(){document.getElementById('stickyCTA').style.transform='translateY(0)';},3000);</script>"""

def hub_page(filename, title, meta_desc, h1, accent, hero_desc, tag, tag_color, articles, stats):
    cards = ""
    for i, a in enumerate(articles):
        featured = i == 0
        cls = "art-card featured" if featured else "art-card"
        right = '<div class="art-right"></div>' if featured else ""
        cards += f"""<a href="{a['href']}" class="{cls}">
  <div class="art-card-top">
    <div class="art-cat-badge"><span>{tag}</span></div>
    <div class="art-title">{a['title']}</div>
    <div class="art-desc">{a['desc']}</div>
  </div>
  <div class="art-meta"><span>{a.get('date','June 2025')}</span><span class="art-meta-dot"></span><span>{a.get('rt','6 min read')}</span></div>
  <div class="art-card-footer"><div class="art-divider"></div><span class="art-read-link">Read Article <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></span></div>
  {right}
</a>\n"""

    stats_html = "".join([f'<div class="stat-item"><div class="stat-num">{s["num"]}</div><div class="stat-lbl">{s["lbl"]}</div></div>' for s in stats])
    schema = json.dumps({"@context":"https://schema.org","@type":"CollectionPage","name":title,"description":meta_desc,"url":f"https://lexscale.ai/{filename}","publisher":{"@type":"Organization","name":"LexScale.ai","url":"https://lexscale.ai"}})

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{title} | LexScale.ai</title>
<meta name="description" content="{meta_desc}"/>
<link rel="canonical" href="https://lexscale.ai/{filename}"/>
<meta property="og:title" content="{title} | LexScale.ai"/>
<meta property="og:description" content="{meta_desc}"/>
<meta property="og:type" content="website"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<script type="application/ld+json">{schema}</script>
<style>
{css_common()}
.hub-hero{{background:linear-gradient(160deg,#060d24 0%,#0B1536 55%,#111d45 100%);padding:72px 40px 64px;text-align:center;position:relative;overflow:hidden;}}
.grid-bg{{position:absolute;inset:0;background-image:linear-gradient(rgba(106,92,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(106,92,255,.05) 1px,transparent 1px);background-size:52px 52px;pointer-events:none;}}
.hub-inner{{max-width:760px;margin:0 auto;position:relative;z-index:2;}}
.hub-tag{{display:inline-flex;align-items:center;gap:7px;background:rgba(106,92,255,.12);border:1px solid rgba(106,92,255,.3);border-radius:100px;padding:6px 16px;margin-bottom:20px;}}
.hub-tag span{{font-size:11px;font-weight:700;color:{tag_color};letter-spacing:.8px;text-transform:uppercase;}}
.hub-h1{{font-size:clamp(30px,4vw,52px);font-weight:900;color:#fff;letter-spacing:-1.5px;line-height:1.08;margin-bottom:18px;}}
.hub-h1 .accent{{background:linear-gradient(135deg,{tag_color},{tag_color}aa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}}
.hub-desc{{font-size:17px;color:rgba(255,255,255,.55);line-height:1.7;margin-bottom:32px;max-width:560px;margin-left:auto;margin-right:auto;}}
.hub-btns{{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;}}
.btn-primary{{display:inline-block;background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;padding:14px 30px;border-radius:100px;font-size:15px;font-weight:700;box-shadow:0 4px 20px rgba(106,92,255,.4);transition:all .25s;}}
.btn-primary:hover{{transform:translateY(-2px);}}
.btn-outline{{display:inline-block;border:1.5px solid rgba(255,255,255,.2);color:rgba(255,255,255,.8);padding:14px 30px;border-radius:100px;font-size:15px;font-weight:600;transition:all .25s;}}
.stats-bar{{background:#f8f7ff;border-bottom:1px solid rgba(106,92,255,.08);padding:20px 40px;}}
.stats-inner{{max-width:1100px;margin:0 auto;display:flex;justify-content:center;gap:60px;flex-wrap:wrap;}}
.stat-item{{text-align:center;}}
.stat-num{{font-size:24px;font-weight:900;color:var(--pu);letter-spacing:-.8px;}}
.stat-lbl{{font-size:11px;color:#94a3b8;font-weight:500;margin-top:2px;}}
.articles-section{{padding:72px 40px;background:#fff;}}
.articles-inner{{max-width:1160px;margin:0 auto;}}
.section-header{{margin-bottom:48px;}}
.section-header h2{{font-size:clamp(24px,2.8vw,36px);font-weight:900;color:var(--navy);letter-spacing:-1px;margin-bottom:10px;}}
.section-header p{{font-size:16px;color:#64748b;line-height:1.65;}}
.articles-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;}}
.art-card{{background:#fff;border:1px solid rgba(106,92,255,.1);border-radius:20px;overflow:hidden;transition:all .3s cubic-bezier(.34,1.1,.64,1);display:flex;flex-direction:column;}}
.art-card:hover{{transform:translateY(-6px);border-color:rgba(106,92,255,.3);box-shadow:0 20px 56px rgba(106,92,255,.12);}}
.art-card-top{{padding:28px 28px 0;}}
.art-cat-badge{{display:inline-flex;align-items:center;background:rgba(106,92,255,.07);border:1px solid rgba(106,92,255,.15);border-radius:100px;padding:4px 12px;margin-bottom:16px;}}
.art-cat-badge span{{font-size:10px;font-weight:700;color:var(--pu);letter-spacing:.6px;text-transform:uppercase;}}
.art-title{{font-size:17px;font-weight:800;color:var(--navy);letter-spacing:-.4px;line-height:1.3;margin-bottom:10px;}}
.art-desc{{font-size:13px;color:#64748b;line-height:1.65;margin-bottom:20px;}}
.art-meta{{display:flex;align-items:center;gap:14px;font-size:11px;color:#94a3b8;font-weight:500;padding:0 28px 20px;}}
.art-meta-dot{{width:3px;height:3px;border-radius:50%;background:#cbd5e1;}}
.art-card-footer{{margin-top:auto;padding:0 28px 24px;}}
.art-divider{{height:1px;background:rgba(106,92,255,.07);margin-bottom:18px;}}
.art-read-link{{display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:700;color:var(--pu);transition:gap .2s;}}
.art-read-link:hover{{gap:12px;}}
.art-card.featured{{grid-column:1/-1;flex-direction:row;}}
.art-card.featured .art-card-top{{flex:1;padding:36px 0 36px 36px;}}
.art-card.featured .art-card-footer{{padding:0 36px 36px 36px;margin-top:0;display:flex;align-items:flex-end;}}
.art-card.featured .art-divider{{display:none;}}
.art-card.featured .art-right{{width:260px;flex-shrink:0;background:linear-gradient(135deg,rgba(106,92,255,.06),rgba(106,92,255,.02));border-left:1px solid rgba(106,92,255,.08);}}
.art-card.featured .art-title{{font-size:22px;}}
.cta-banner{{background:linear-gradient(135deg,var(--navy) 0%,#1a2456 100%);padding:72px 40px;text-align:center;position:relative;overflow:hidden;}}
.cta-inner{{max-width:640px;margin:0 auto;position:relative;z-index:2;}}
.cta-inner h2{{font-size:clamp(26px,3vw,38px);font-weight:900;color:#fff;letter-spacing:-1px;margin-bottom:14px;}}
.cta-inner p{{font-size:16px;color:rgba(255,255,255,.55);line-height:1.7;margin-bottom:32px;}}
@media(max-width:900px){{.hub-hero{{padding:52px 20px 48px;}}.articles-section{{padding:48px 20px;}}.articles-grid{{grid-template-columns:1fr;}}.art-card.featured{{flex-direction:column;}}.art-card.featured .art-card-top{{padding:28px 24px 0;}}.art-card.featured .art-card-footer{{padding:0 24px 24px;margin-top:auto;}}.art-card.featured .art-right{{display:none;}}.cta-banner{{padding:52px 20px;}}.stats-bar{{padding:20px;}}.stats-inner{{gap:30px;}}}}
</style>
</head>
<body>
{nav_html()}
<section class="hub-hero">
  <div class="grid-bg"></div>
  <div class="hub-inner">
    <div class="hub-tag"><span>{tag}</span></div>
    <h1 class="hub-h1">{h1} <span class="accent">{accent}</span></h1>
    <p class="hub-desc">{hero_desc}</p>
    <div class="hub-btns">
      <a href="ai-seo-for-law-firms.html" class="btn-primary">Get AI Visible Now →</a>
      <a href="index.html" class="btn-outline">View All Services</a>
    </div>
  </div>
</section>
<div class="stats-bar"><div class="stats-inner">{stats_html}</div></div>
<section class="articles-section">
  <div class="articles-inner">
    <div class="section-header"><h2>All {tag} Articles</h2><p>Expert guides to help your law firm grow with AI-powered marketing and search visibility.</p></div>
    <div class="articles-grid">{cards}</div>
  </div>
</section>
<section class="cta-banner">
  <div class="grid-bg"></div>
  <div class="cta-inner">
    <h2>Ready to Grow Your Law Firm with AI?</h2>
    <p>Get a free AI Visibility Report and see exactly where your firm stands across ChatGPT, Gemini, and Perplexity.</p>
    <button class="btn-primary" onclick="document.getElementById('leadModal').style.display='flex'" style="border:none;cursor:pointer;font-family:inherit;">Get My Free Report →</button>
  </div>
</section>
{footer_html()}
{sticky_html()}
{modal_html()}
</body>
</html>"""

def article_page(filename, title, meta_desc, category, category_href, h1, h1_accent, deck, sections, faqs, related):
    faq_schema_items = [{"@type":"Question","name":f["q"],"acceptedAnswer":{"@type":"Answer","text":f["a"]}} for f in faqs]
    article_schema = json.dumps({"@context":"https://schema.org","@type":"Article","headline":title,"description":meta_desc,"author":{"@type":"Organization","name":"LexScale.ai"},"publisher":{"@type":"Organization","name":"LexScale.ai","url":"https://lexscale.ai"},"datePublished":"2025-06-19","mainEntityOfPage":f"https://lexscale.ai/{filename}"})
    faq_schema = json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":faq_schema_items})

    sections_html = ""
    for s in sections:
        sections_html += f'<h2 style="font-size:22px;font-weight:800;color:var(--navy);letter-spacing:-.5px;margin:36px 0 14px;">{s["h2"]}</h2>\n'
        for p in s.get("paras",[]):
            if p.startswith("UL:"):
                items = p[3:].split("|")
                sections_html += '<ul style="margin:14px 0 14px 20px;">' + "".join(f'<li style="font-size:15px;color:#374151;line-height:1.8;margin-bottom:6px;">{item}</li>' for item in items) + '</ul>\n'
            elif p.startswith("CALLOUT:"):
                sections_html += f'<div style="background:rgba(106,92,255,.06);border-left:3px solid var(--pu);border-radius:0 12px 12px 0;padding:18px 22px;margin:24px 0;"><p style="font-size:14px;color:#374151;line-height:1.75;font-style:italic;">{p[8:]}</p></div>\n'
            else:
                sections_html += f'<p style="font-size:15px;color:#374151;line-height:1.85;margin-bottom:16px;">{p}</p>\n'

    faq_html = ""
    for f in faqs:
        faq_html += f"""<div style="border-bottom:1px solid rgba(106,92,255,.08);padding:20px 0;">
  <button onclick="var a=this.nextElementSibling;a.style.display=a.style.display==='block'?'none':'block';this.querySelector('span').textContent=a.style.display==='block'?'−':'+'" style="width:100%;background:none;border:none;display:flex;justify-content:space-between;align-items:center;cursor:pointer;font-family:inherit;text-align:left;">
    <span style="font-size:15px;font-weight:700;color:var(--navy);">{f['q']}</span>
    <span style="font-size:20px;color:var(--pu);flex-shrink:0;margin-left:12px;">+</span>
  </button>
  <div style="display:none;padding-top:12px;"><p style="font-size:14px;color:#64748b;line-height:1.8;">{f['a']}</p></div>
</div>\n"""

    related_html = "".join([f'<a href="{r["href"]}" style="display:block;padding:12px 16px;background:rgba(106,92,255,.04);border:1px solid rgba(106,92,255,.1);border-radius:10px;font-size:13px;font-weight:600;color:var(--navy);transition:background .2s;margin-bottom:8px;" onmouseover="this.style.background=\'rgba(106,92,255,.09)\'" onmouseout="this.style.background=\'rgba(106,92,255,.04)\'">{r["title"]}</a>' for r in related])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{title} | LexScale.ai</title>
<meta name="description" content="{meta_desc}"/>
<link rel="canonical" href="https://lexscale.ai/{filename}"/>
<meta property="og:title" content="{title} | LexScale.ai"/>
<meta property="og:description" content="{meta_desc}"/>
<meta property="og:type" content="article"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<script type="application/ld+json">{article_schema}</script>
<script type="application/ld+json">{faq_schema}</script>
<style>
{css_common()}
@keyframes pulse{{0%,100%{{opacity:1;transform:scale(1);}}50%{{opacity:.6;transform:scale(1.3);}}}}
.art-hero{{background:linear-gradient(150deg,#04070f 0%,#060c1c 50%,#0B1536 100%);padding:80px 40px 70px;}}
.art-hero-inner{{max-width:860px;margin:0 auto;text-align:center;}}
.art-cat{{display:inline-flex;align-items:center;gap:8px;background:rgba(106,92,255,.12);border:1px solid rgba(106,92,255,.25);border-radius:100px;padding:7px 16px;margin-bottom:24px;}}
.art-cat-dot{{width:6px;height:6px;border-radius:50%;background:var(--pu3);animation:pulse 2s infinite;}}
.art-cat-txt{{font-size:11px;font-weight:700;color:var(--pu3);letter-spacing:.8px;text-transform:uppercase;}}
.art-h1{{font-size:clamp(28px,4vw,50px);font-weight:900;color:#fff;line-height:1.1;letter-spacing:-1.8px;margin-bottom:20px;}}
.art-h1 .accent{{background:linear-gradient(135deg,var(--gold3),var(--gold2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}}
.art-deck{{font-size:clamp(14px,1.6vw,17px);color:rgba(255,255,255,.6);line-height:1.8;max-width:680px;margin:0 auto 32px;}}
.art-meta-row{{display:flex;align-items:center;justify-content:center;gap:20px;flex-wrap:wrap;}}
.art-meta-item{{display:flex;align-items:center;gap:6px;font-size:12px;color:rgba(255,255,255,.35);font-weight:500;}}
.content-wrap{{max-width:1100px;margin:0 auto;padding:64px 40px;display:grid;grid-template-columns:1fr 300px;gap:56px;align-items:start;}}
.article-body{{min-width:0;}}
.sidebar{{position:sticky;top:96px;}}
.sidebar-card{{background:#fff;border:1px solid rgba(106,92,255,.12);border-radius:20px;padding:28px;margin-bottom:24px;box-shadow:0 4px 24px rgba(11,21,54,.06);}}
.sidebar-card h3{{font-size:15px;font-weight:800;color:var(--navy);margin-bottom:6px;}}
.sidebar-card p{{font-size:13px;color:#64748b;line-height:1.6;margin-bottom:18px;}}
.sidebar-btn{{display:block;width:100%;background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;border:none;padding:12px;border-radius:100px;font-size:13px;font-weight:700;cursor:pointer;font-family:inherit;text-align:center;}}
.cta-banner{{background:linear-gradient(135deg,var(--navy),#1a2456);padding:64px 40px;text-align:center;}}
.cta-inner{{max-width:600px;margin:0 auto;}}
.cta-inner h2{{font-size:clamp(24px,2.8vw,36px);font-weight:900;color:#fff;letter-spacing:-1px;margin-bottom:12px;}}
.cta-inner p{{font-size:15px;color:rgba(255,255,255,.55);line-height:1.7;margin-bottom:28px;}}
.btn-primary{{display:inline-block;background:linear-gradient(135deg,var(--pu),var(--pu2));color:#fff;padding:14px 30px;border-radius:100px;font-size:15px;font-weight:700;border:none;cursor:pointer;font-family:inherit;}}
@media(max-width:900px){{.art-hero{{padding:52px 20px 48px;}}.content-wrap{{grid-template-columns:1fr;padding:40px 20px;gap:32px;}}.sidebar{{position:static;}}.cta-banner{{padding:48px 20px;}}}}
</style>
</head>
<body>
{nav_html()}
<section class="art-hero">
  <div class="art-hero-inner">
    <div class="art-cat"><span class="art-cat-dot"></span><span class="art-cat-txt"><a href="{category_href}" style="color:inherit;">{category}</a></span></div>
    <h1 class="art-h1">{h1} <span class="accent">{h1_accent}</span></h1>
    <p class="art-deck">{deck}</p>
    <div class="art-meta-row">
      <span class="art-meta-item"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>June 19, 2025</span>
      <span class="art-meta-item"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>6 min read</span>
      <span class="art-meta-item">LexScale Editorial</span>
    </div>
  </div>
</section>
<div class="content-wrap">
  <article class="article-body">
    {sections_html}
    <div style="background:#f8f7ff;border-radius:20px;padding:40px;margin-top:48px;">
      <h2 style="font-size:22px;font-weight:800;color:var(--navy);letter-spacing:-.5px;margin-bottom:28px;">Frequently Asked Questions</h2>
      {faq_html}
    </div>
  </article>
  <aside class="sidebar">
    <div class="sidebar-card">
      <h3>Get Your Free AI Visibility Report</h3>
      <p>See how your law firm ranks across ChatGPT, Gemini, and Perplexity — free in 24 hours.</p>
      <button class="sidebar-btn" onclick="document.getElementById('leadModal').style.display='flex'">Get Free Report →</button>
    </div>
    <div class="sidebar-card">
      <h3 style="margin-bottom:16px;">Related Articles</h3>
      {related_html}
    </div>
  </aside>
</div>
<section class="cta-banner">
  <div class="cta-inner">
    <h2>Ready to Dominate AI Search?</h2>
    <p>LexScale.ai builds AI-first growth systems for law firms. Get your free visibility report today.</p>
    <button class="btn-primary" onclick="document.getElementById('leadModal').style.display='flex'">Book A Free Demo →</button>
  </div>
</section>
{footer_html()}
{sticky_html()}
{modal_html()}
</body>
</html>"""

# ============================================================
# DATA
# ============================================================

CATEGORIES = {
  "ai-seo": {
    "hub_file": "ai-seo.html",
    "title": "AI SEO for Law Firms",
    "meta_desc": "Expert guides on AI SEO for law firms. Learn how to rank in AI-powered search, build topical authority, and get your firm cited by ChatGPT, Gemini, and Perplexity.",
    "h1": "AI SEO Insights for",
    "accent": "Law Firms",
    "hero_desc": "Everything your law firm needs to know about AI SEO — from Google AI Overviews to topical authority to getting cited by AI search engines.",
    "tag": "AI SEO",
    "tag_color": "#6A5CFF",
    "stats": [{"num":"73%","lbl":"of searches now use AI"},{"num":"5","lbl":"in-depth articles"},{"num":"6 min","lbl":"avg read time"},{"num":"2025","lbl":"fully up to date"}],
    "articles": [
      {"file":"ai-seo-for-law-firms-complete-guide.html","title":"AI SEO for Law Firms: The Complete Guide","desc":"How AI is transforming search for attorneys and what your firm must do now to stay visible and competitive.","rt":"8 min read","date":"June 2025"},
      {"file":"ai-seo-vs-traditional-seo-lawyers.html","title":"AI SEO vs Traditional SEO for Lawyers","desc":"The key differences between AI SEO and traditional SEO — and why law firms need both strategies working together.","rt":"6 min read","date":"June 2025"},
      {"file":"how-google-ai-overviews-affect-law-firms.html","title":"How Google AI Overviews Affect Law Firms","desc":"What AI Overviews mean for legal search traffic, how they work, and how to get your firm featured in them.","rt":"7 min read","date":"June 2025"},
      {"file":"topical-authority-for-law-firms.html","title":"Building Topical Authority for Law Firms","desc":"How to become the definitive online resource in your practice area so Google and AI engines trust and recommend you.","rt":"7 min read","date":"June 2025"},
      {"file":"local-ai-seo-for-law-firms.html","title":"Local AI SEO for Law Firms","desc":"How to dominate local AI search results and get recommended to potential clients searching in your city.","rt":"5 min read","date":"June 2025"},
    ]
  },
  "ai-receptionists": {
    "hub_file": "ai-receptionists.html",
    "title": "AI Receptionists for Law Firms",
    "meta_desc": "Complete guides on AI receptionists for law firms. Learn how AI answering services capture leads 24/7, reduce missed calls, and increase revenue for attorneys.",
    "h1": "AI Receptionist Insights for",
    "accent": "Law Firms",
    "hero_desc": "How AI receptionists are helping law firms answer every call, qualify every lead, and book more consultations — around the clock, without extra staff.",
    "tag": "AI Receptionists",
    "tag_color": "#6A5CFF",
    "stats": [{"num":"62%","lbl":"of callers won't leave voicemail"},{"num":"5","lbl":"in-depth articles"},{"num":"6 min","lbl":"avg read time"},{"num":"24/7","lbl":"AI availability"}],
    "articles": [
      {"file":"what-is-an-ai-receptionist-for-law-firms.html","title":"What Is an AI Receptionist for Law Firms?","desc":"How AI receptionists work, what they do, and why law firms across the country are adopting them fast.","rt":"7 min read","date":"June 2025"},
      {"file":"ai-receptionist-vs-human-receptionist.html","title":"AI Receptionist vs Human Receptionist for Law Firms","desc":"A head-to-head comparison of cost, availability, performance, and client experience for law firm reception.","rt":"6 min read","date":"June 2025"},
      {"file":"how-ai-receptionists-increase-law-firm-revenue.html","title":"How AI Receptionists Increase Law Firm Revenue","desc":"The direct connection between answering every call and growing your caseload — with real numbers.","rt":"6 min read","date":"June 2025"},
      {"file":"never-miss-a-call-law-firm.html","title":"Why Law Firms Can't Afford to Miss Another Call","desc":"The hidden cost of missed calls and unanswered after-hours inquiries — and how AI solves it permanently.","rt":"5 min read","date":"June 2025"},
      {"file":"ai-receptionist-intake-automation.html","title":"AI Receptionist + Intake Automation for Law Firms","desc":"How to automate the entire new client journey from first call to signed retainer with AI-powered systems.","rt":"7 min read","date":"June 2025"},
    ]
  },
  "ai-chatbots": {
    "hub_file": "ai-chatbots.html",
    "title": "AI Chatbots for Law Firms",
    "meta_desc": "Expert guides on AI chatbots for law firms. Learn how chatbots convert website visitors into clients, qualify leads, and work 24/7 to grow your practice.",
    "h1": "AI Chatbot Insights for",
    "accent": "Law Firms",
    "hero_desc": "How AI chatbots are turning law firm websites into lead generation machines — qualifying visitors, booking consultations, and capturing clients around the clock.",
    "tag": "AI Chatbots",
    "tag_color": "#6A5CFF",
    "stats": [{"num":"3x","lbl":"more leads with chatbots"},{"num":"5","lbl":"in-depth articles"},{"num":"6 min","lbl":"avg read time"},{"num":"24/7","lbl":"lead capture"}],
    "articles": [
      {"file":"ai-chatbot-for-law-firm-website.html","title":"AI Chatbot for Your Law Firm Website: A Complete Guide","desc":"Everything you need to know about adding an AI chatbot to your law firm site — how it works and what results to expect.","rt":"8 min read","date":"June 2025"},
      {"file":"how-ai-chatbots-convert-legal-leads.html","title":"How AI Chatbots Convert More Legal Leads","desc":"The psychology and mechanics of chatbot lead conversion for attorneys — why visitors engage and how to maximize results.","rt":"6 min read","date":"June 2025"},
      {"file":"ai-chatbot-vs-live-chat-lawyers.html","title":"AI Chatbot vs Live Chat for Law Firms","desc":"Which option is right for your firm's size, budget, and client base? A detailed comparison of both approaches.","rt":"6 min read","date":"June 2025"},
      {"file":"ai-chatbot-intake-qualification.html","title":"Using AI Chatbots to Qualify Legal Leads","desc":"How to filter out low-value inquiries and focus your team on high-value prospects using intelligent chatbot flows.","rt":"5 min read","date":"June 2025"},
      {"file":"ai-chatbot-roi-for-law-firms.html","title":"The ROI of AI Chatbots for Law Firms","desc":"Real numbers on what chatbots return for law firm marketing investment — and how to calculate your firm's potential.","rt":"6 min read","date":"June 2025"},
    ]
  },
  "entity-seo": {
    "hub_file": "entity-seo.html",
    "title": "Entity SEO & Structured Data for Law Firms",
    "meta_desc": "Expert guides on entity SEO and structured data for law firms. Learn schema markup, Knowledge Graph optimization, and how to build entity authority for AI search.",
    "h1": "Entity SEO & Structured Data for",
    "accent": "Law Firms",
    "hero_desc": "How entity SEO and structured data help law firms get understood by Google, earn Knowledge Panels, and get recommended by AI search engines.",
    "tag": "Entity SEO",
    "tag_color": "#6A5CFF",
    "stats": [{"num":"40%","lbl":"higher CTR with schema"},{"num":"5","lbl":"in-depth articles"},{"num":"6 min","lbl":"avg read time"},{"num":"2025","lbl":"fully up to date"}],
    "articles": [
      {"file":"what-is-entity-seo-for-law-firms.html","title":"What Is Entity SEO for Law Firms?","desc":"How Google's Knowledge Graph works and why entity optimization is becoming the most important SEO strategy for attorneys.","rt":"7 min read","date":"June 2025"},
      {"file":"schema-markup-for-lawyers-guide.html","title":"Schema Markup for Lawyers: The Complete Guide","desc":"How to implement structured data that helps Google and AI platforms understand your law firm and recommend you.","rt":"8 min read","date":"June 2025"},
      {"file":"attorney-knowledge-panel-optimization.html","title":"How to Get and Optimize Your Law Firm Knowledge Panel","desc":"Step-by-step guide to earning and controlling your Google Knowledge Panel — a key signal for AI visibility.","rt":"6 min read","date":"June 2025"},
      {"file":"local-business-schema-law-firms.html","title":"Local Business Schema for Law Firms","desc":"The specific schema types every law firm website needs — and how to implement them correctly for maximum impact.","rt":"6 min read","date":"June 2025"},
      {"file":"entity-seo-vs-keyword-seo.html","title":"Entity SEO vs Keyword SEO for Law Firms","desc":"Why the future of legal search is about entities, not just keywords — and how to build an entity-first strategy.","rt":"5 min read","date":"June 2025"},
    ]
  },
  "ai-websites": {
    "hub_file": "ai-websites.html",
    "title": "AI Websites for Law Firms",
    "meta_desc": "Expert guides on AI website design for law firms. Learn what makes a law firm website AI-ready, how to optimize for conversions, and why site speed matters for rankings.",
    "h1": "AI Website Insights for",
    "accent": "Law Firms",
    "hero_desc": "What separates an ordinary law firm website from one that ranks on Google, gets cited by AI, and converts visitors into signed clients.",
    "tag": "AI Websites",
    "tag_color": "#6A5CFF",
    "stats": [{"num":"95+","lbl":"PageSpeed scores we deliver"},{"num":"5","lbl":"in-depth articles"},{"num":"6 min","lbl":"avg read time"},{"num":"<1.5s","lbl":"load time target"}],
    "articles": [
      {"file":"ai-website-design-for-law-firms-guide.html","title":"AI Website Design for Law Firms: The Complete Guide","desc":"What makes an AI-optimized law firm website and why the right design directly impacts your Google rankings and lead flow.","rt":"8 min read","date":"June 2025"},
      {"file":"law-firm-website-conversion-optimization.html","title":"Law Firm Website Conversion Optimization","desc":"How to turn more website visitors into booked consultations — the design and content principles that move people to act.","rt":"7 min read","date":"June 2025"},
      {"file":"law-firm-website-speed-performance.html","title":"Law Firm Website Speed & Performance Guide","desc":"Why page speed matters for rankings, AI visibility, and client trust — and how to achieve a 95+ PageSpeed score.","rt":"6 min read","date":"June 2025"},
      {"file":"mobile-first-law-firm-website.html","title":"Mobile-First Design for Law Firm Websites","desc":"Why most law firm websites fail on mobile — and the specific design principles that fix it and win more mobile clients.","rt":"5 min read","date":"June 2025"},
      {"file":"law-firm-website-seo-structure.html","title":"How to Structure Your Law Firm Website for SEO","desc":"The ideal site architecture that helps Google and AI understand your firm — and funnels visitors to convert.","rt":"6 min read","date":"June 2025"},
    ]
  }
}

ARTICLE_CONTENT = {
  "ai-seo-for-law-firms-complete-guide.html": {
    "h1":"AI SEO for Law Firms:", "h1_accent":"The Complete Guide",
    "deck":"Search has fundamentally changed. AI now answers questions directly — and your law firm either shows up or it doesn't. Here's everything you need to know.",
    "sections":[
      {"h2":"What Is AI SEO and Why Does It Matter for Law Firms?","paras":["AI SEO is the practice of optimizing your law firm's online presence to be recommended by AI-powered search engines like ChatGPT, Google Gemini, Perplexity, and Bing Copilot. Unlike traditional SEO, which focuses on ranking in blue-link search results, AI SEO focuses on becoming a trusted source that AI engines cite when answering questions.","The shift matters because behavior is changing fast. A growing percentage of people — especially younger demographics — now type their legal questions into AI tools instead of traditional search engines. If your firm isn't visible in those AI responses, you're invisible to an increasingly large segment of potential clients.","CALLOUT:Law firms that invest in AI SEO now are positioning themselves 12–18 months ahead of competitors who haven't started. Early movers in new search paradigms consistently capture disproportionate market share."]},
      {"h2":"How AI Search Engines Evaluate Law Firms","paras":["AI search engines don't rank websites the way Google does. Instead, they synthesize information from multiple sources and generate answers. When someone asks 'Who is the best personal injury lawyer in Chicago?', the AI pulls from websites it deems authoritative, review platforms, directories, and news sources.","Factors that influence whether your firm is cited include: the quality and depth of your published content, the consistency of your name, address, and phone number across the web, the volume and sentiment of your Google reviews, your presence in legal directories like Avvo and Martindale, and the overall authority of your website as judged by backlinks.","UL:Content depth and comprehensiveness|Google Business Profile completeness|Third-party mentions and citations|Schema markup and structured data|Domain authority and backlink profile"]},
      {"h2":"The Four Pillars of AI SEO for Law Firms","paras":["Successful AI SEO rests on four pillars: authority, relevance, trust, and accessibility. Authority means your firm is recognized as a credible source — built through backlinks, reviews, and mentions. Relevance means your content directly addresses the questions potential clients ask. Trust means your information is accurate, current, and consistent everywhere it appears. Accessibility means AI systems can easily read, parse, and understand your content.","Each pillar requires a specific strategy. Authority is built over time through content marketing and digital PR. Relevance is achieved by mapping your content to real client questions. Trust is maintained through regular audits of your online presence. Accessibility is achieved through technical SEO and proper schema implementation."]},
      {"h2":"Getting Started: Your AI SEO Action Plan","paras":["Start by auditing your current visibility. Ask ChatGPT, Gemini, and Perplexity: 'Who are the best [practice area] lawyers in [your city]?' If your firm isn't mentioned, you have work to do. Next, audit your Google Business Profile, ensure it's complete and up to date, and prioritize getting more Google reviews.","Then focus on content. Create comprehensive, expert-level articles on the legal questions your clients ask most. Each piece of content should be at least 1,000 words, include FAQs, and be structured with clear H2 headings. This format is exactly what AI systems prefer when synthesizing answers."]}
    ],
    "faqs":[
      {"q":"How long does AI SEO take to show results?","a":"AI SEO is a medium-to-long-term investment. Most law firms begin seeing improvements in AI visibility within 3 to 6 months of consistent effort. Firms that publish high-quality content regularly and earn quality backlinks tend to see the fastest results."},
      {"q":"Is AI SEO different from traditional SEO?","a":"AI SEO and traditional SEO share a foundation — quality content, technical optimization, and authority signals. However, AI SEO places more emphasis on conversational content, comprehensive topic coverage, and structured data that helps AI systems parse and cite your information accurately."},
      {"q":"Do I need to optimize for every AI platform separately?","a":"Not entirely. A strong content and authority foundation benefits your visibility across all AI platforms simultaneously. However, each platform has nuances — for example, Perplexity prioritizes real-time web sources, while ChatGPT relies heavily on its training data supplemented by web browsing. A good AI SEO strategy addresses the common foundation first."},
      {"q":"What type of content works best for AI SEO?","a":"Comprehensive, question-and-answer formatted content works exceptionally well. FAQ pages, detailed practice area guides, and articles that directly address common client questions are all highly effective. Content should be structured with clear headings, written in plain language, and backed by real expertise."},
      {"q":"How does AI SEO affect my Google rankings?","a":"AI SEO and Google SEO are largely complementary. The content strategies, technical improvements, and authority-building activities that improve AI visibility also tend to improve Google rankings. Think of them as two tracks that run in parallel and reinforce each other."}
    ],
    "related":[
      {"title":"AI SEO vs Traditional SEO for Lawyers","href":"ai-seo-vs-traditional-seo-lawyers.html"},
      {"title":"How Google AI Overviews Affect Law Firms","href":"how-google-ai-overviews-affect-law-firms.html"},
      {"title":"Building Topical Authority for Law Firms","href":"topical-authority-for-law-firms.html"},
    ]
  },
  "what-is-an-ai-receptionist-for-law-firms.html": {
    "h1":"What Is an AI Receptionist", "h1_accent":"for Law Firms?",
    "deck":"AI receptionists answer every call, qualify every lead, and book consultations automatically — 24 hours a day, without hiring additional staff.",
    "sections":[
      {"h2":"The Problem: Law Firms Miss Too Many Calls","paras":["Every missed call is a missed client. For law firms, where a single retained case can be worth thousands of dollars, the cost of unanswered calls is staggering. Studies show that 62% of callers who reach voicemail don't leave a message — they simply call the next firm on the list. And with after-hours inquiries representing a significant portion of new business, firms that only answer during business hours are leaving revenue on the table every day.","CALLOUT:The average law firm misses 35–40% of inbound calls. For a firm billing $300 average per hour and converting even 10% of those missed calls into clients, that represents tens of thousands of dollars in lost annual revenue."]},
      {"h2":"How AI Receptionists Work","paras":["An AI receptionist is a software system that answers phone calls using natural language processing — the same underlying technology that powers ChatGPT and Siri. When a potential client calls your firm, the AI answers immediately, greets them professionally using your firm's name, and engages them in a natural conversation to understand their needs.","The AI can ask qualifying questions (what type of legal matter do you have? When do you need help?), collect contact information, provide basic information about your services, and book a consultation directly into your calendar. All of this happens instantly, whether it's 2pm on a Tuesday or 11pm on a Sunday.","UL:Answers 100% of calls immediately, no hold time|Qualifies leads using your specific intake criteria|Books appointments directly into your calendar|Sends follow-up texts and emails automatically|Transcribes every call for your review"]},
      {"h2":"What AI Receptionists Can and Cannot Do","paras":["AI receptionists excel at intake, qualification, scheduling, and information gathering. They maintain a consistently professional tone, never have a bad day, and can handle multiple calls simultaneously — eliminating hold queues entirely.","What they cannot do is provide legal advice or handle complex emotional conversations that require human empathy. For those situations, the AI seamlessly transfers the call to a human team member or schedules a callback. The best implementations use AI to handle the volume work while freeing your human team to focus on high-value interactions."]},
      {"h2":"The ROI of an AI Receptionist for Law Firms","paras":["The financial case for AI receptionists is straightforward. Compare the cost of the service (typically $200–$600/month) against the value of even one additional retained client per month. For most practice areas, the ROI is 10:1 or better. Add in the value of recaptured after-hours leads, reduced receptionist overtime, and improved client experience, and the numbers become even more compelling."]}
    ],
    "faqs":[
      {"q":"Will clients know they're talking to an AI?","a":"Modern AI receptionists are transparent and typically identify themselves as automated assistants. Most law firms find that clients respond positively when the AI is fast, helpful, and professional — which is exactly the experience a well-configured AI receptionist delivers."},
      {"q":"Can the AI handle complex legal inquiries?","a":"AI receptionists are designed for intake and qualification, not legal advice. They gather information, qualify the lead, and either book a consultation or transfer to a human attorney. They are not designed to answer substantive legal questions."},
      {"q":"How long does setup take?","a":"Most AI receptionist setups for law firms take 1–3 business days. The process involves configuring your intake questions, setting your availability for bookings, and forwarding your phone number. LexScale handles the entire setup process."},
      {"q":"What happens to calls the AI can't handle?","a":"Any call that exceeds the AI's configured parameters is either transferred to a live team member in real time or scheduled for a callback. No call falls through the cracks."},
      {"q":"Can I review the calls?","a":"Yes. Every call is recorded, transcribed, and available in your dashboard. You can review any conversation, listen to recordings, and see the full intake data the AI collected."}
    ],
    "related":[
      {"title":"AI Receptionist vs Human Receptionist","href":"ai-receptionist-vs-human-receptionist.html"},
      {"title":"Never Miss a Call: The Hidden Cost for Law Firms","href":"never-miss-a-call-law-firm.html"},
      {"title":"AI Receptionist + Intake Automation","href":"ai-receptionist-intake-automation.html"},
    ]
  },
  "ai-chatbot-for-law-firm-website.html": {
    "h1":"AI Chatbot for Your Law Firm Website:", "h1_accent":"A Complete Guide",
    "deck":"An AI chatbot on your law firm website works 24/7 to engage visitors, answer questions, qualify leads, and book consultations — even while you sleep.",
    "sections":[
      {"h2":"Why Law Firm Websites Need AI Chatbots","paras":["Most law firm websites have a fundamental problem: they're passive. Visitors land, browse, and leave — often without taking any action. Studies show that 96% of website visitors leave without contacting the firm. An AI chatbot changes that dynamic by proactively engaging visitors, answering their questions in real time, and guiding them toward booking a consultation.","CALLOUT:Law firms that add AI chatbots to their websites report an average 40–60% increase in lead capture rate within the first 90 days of deployment.","The timing of engagement matters enormously in legal marketing. When someone is searching for a lawyer, they're often in a state of urgency or stress. A chatbot that responds within seconds — day or night — meets them at the exact moment of need, which is when conversion rates are highest."]},
      {"h2":"How AI Chatbots Work on Law Firm Websites","paras":["Modern AI chatbots for law firms use large language model technology to understand natural language questions and respond intelligently. Unlike older rule-based chatbots that followed rigid scripts, AI chatbots can handle a wide range of questions, maintain context throughout a conversation, and adapt their responses based on what the visitor says.","A typical chatbot interaction on a law firm site goes like this: the visitor lands on the page, the chatbot greets them after a few seconds, asks what brings them to the site, gathers basic information about their legal matter, asks qualifying questions, and then either books a consultation or collects contact info for follow-up.","UL:Engages visitors within seconds of arriving|Answers common questions about your practice areas|Qualifies leads using your intake criteria|Books consultations directly into your calendar|Works 24/7 with no breaks or sick days"]},
      {"h2":"Choosing the Right Chatbot for Your Law Firm","paras":["Not all chatbots are equal. For law firms, you need a solution that understands legal contexts, can be customized to your specific practice areas, and integrates with your existing calendar and CRM systems. Rule-based chatbots are cheaper but limited — they can only handle questions they're explicitly programmed for. AI-powered chatbots are more expensive but dramatically more capable and effective.","Look for solutions that offer: conversation transcripts and lead data, calendar integration for instant booking, customizable intake flows, mobile optimization, and HIPAA/privacy compliance if you handle sensitive matters."]},
      {"h2":"Setting Up Your Law Firm Chatbot for Maximum Results","paras":["The most important step in chatbot implementation is defining your intake flow. What information do you need to qualify a lead? What questions should the chatbot ask? What response should it give if someone describes a matter outside your practice areas? Taking time to map this out before implementation ensures the chatbot works as an extension of your firm, not a generic tool."]}
    ],
    "faqs":[
      {"q":"Will a chatbot make my firm look unprofessional?","a":"A well-designed AI chatbot enhances professionalism by ensuring every visitor gets an immediate, helpful response. Law firms that deploy chatbots consistently report that clients appreciate the instant responsiveness. The key is using a high-quality solution configured to match your firm's voice and standards."},
      {"q":"Can the chatbot provide legal advice?","a":"No, and it shouldn't. Law firm chatbots are configured to gather information, answer general questions about your services, and connect people with your team — not to provide legal counsel. Any substantive legal question is directed to schedule a consultation with an attorney."},
      {"q":"How much does a law firm chatbot cost?","a":"Quality AI chatbots for law firms typically range from $200–$800/month depending on features and usage volume. When measured against the value of even one or two additional clients per month, most firms see a strongly positive ROI within 60–90 days."},
      {"q":"Does the chatbot work on mobile?","a":"Yes. Modern law firm chatbots are built mobile-first and work seamlessly on all devices. Given that over 60% of legal searches happen on mobile, this is a non-negotiable requirement."},
      {"q":"How long does it take to set up?","a":"With LexScale, law firm chatbot setup typically takes 3–5 business days. We handle the configuration, intake flow design, calendar integration, and testing before going live."}
    ],
    "related":[
      {"title":"How AI Chatbots Convert More Legal Leads","href":"how-ai-chatbots-convert-legal-leads.html"},
      {"title":"AI Chatbot vs Live Chat for Law Firms","href":"ai-chatbot-vs-live-chat-lawyers.html"},
      {"title":"The ROI of AI Chatbots for Law Firms","href":"ai-chatbot-roi-for-law-firms.html"},
    ]
  },
  "what-is-entity-seo-for-law-firms.html": {
    "h1":"What Is Entity SEO", "h1_accent":"for Law Firms?",
    "deck":"Entity SEO is how Google and AI engines understand who your firm is, not just what keywords you use. It's the foundation of modern legal search visibility.",
    "sections":[
      {"h2":"From Keywords to Entities: How Google Thinks","paras":["Traditional SEO was built around keywords. You picked a phrase like 'personal injury lawyer Chicago', optimized your page for it, and hoped to rank. That approach still matters — but it's no longer sufficient. Google has evolved to understand entities: real-world people, places, organizations, and concepts that exist independently of any single keyword.","Your law firm is an entity. Your attorneys are entities. Your practice areas connect to legal concepts that are entities. When Google fully understands your firm as an entity — its name, location, specialties, attorneys, history, and reputation — it can recommend you confidently across a much wider range of searches and AI-generated answers.","CALLOUT:Law firms with strong entity profiles are significantly more likely to appear in Google's AI Overviews, Knowledge Panels, and AI-generated search responses — representing the next frontier of client acquisition."]},
      {"h2":"The Google Knowledge Graph and Your Law Firm","paras":["The Google Knowledge Graph is a massive database of entities and the relationships between them. When Google has sufficient confidence about your firm's entity, it creates a Knowledge Panel — that information box that appears on the right side of search results showing your firm's name, address, phone, hours, and reviews.","Earning a Knowledge Panel is a signal that Google trusts your firm's entity. It also improves your visibility in local search, voice search, and AI-generated answers. The path to a Knowledge Panel runs through consistent information across the web, schema markup, Wikipedia or Wikidata presence for larger firms, and strong Google Business Profile optimization.","UL:Consistent NAP (Name, Address, Phone) across all directories|Complete and verified Google Business Profile|Schema markup on your website|Mentions in reputable publications|Attorney profiles on LinkedIn and legal directories"]},
      {"h2":"Why Entity SEO Matters for AI Search","paras":["When ChatGPT, Gemini, or Perplexity answers a question about legal services, they're drawing on entity relationships. They know that personal injury law firms handle car accidents. They know that a firm with 500 Google reviews in Chicago is likely reputable. They know that attorneys with bar association memberships are licensed professionals.","Building your entity profile means feeding these systems the signals they need to understand and recommend your firm. It's not about tricks or hacks — it's about genuinely establishing your firm's identity and reputation across the digital ecosystem."]},
      {"h2":"How to Build Your Law Firm's Entity Profile","paras":["Start with the basics: ensure your firm name, address, and phone number are identical across your website, Google Business Profile, legal directories, and social media. Even minor variations (Street vs St, Suite vs Ste) can confuse entity disambiguation algorithms.","Next, implement schema markup on your website. At minimum, law firms should have LegalService schema, LocalBusiness schema, and Person schema for each attorney. This structured data speaks directly to search engine entity recognition systems."]}
    ],
    "faqs":[
      {"q":"What is the difference between entity SEO and traditional SEO?","a":"Traditional SEO optimizes pages for specific keyword phrases. Entity SEO optimizes your firm's overall identity and reputation so that search engines and AI tools understand who you are, what you do, and why you're trustworthy — regardless of the specific words used in a query."},
      {"q":"Does entity SEO help with local search?","a":"Yes, significantly. Entity SEO is closely tied to local search because Google uses entity signals to determine which businesses to show for location-based queries. A strong entity profile with consistent NAP data, Google Business Profile optimization, and local schema markup directly improves local rankings."},
      {"q":"What is schema markup and do I need it?","a":"Schema markup is code you add to your website that explicitly tells search engines what type of entity you are, what services you provide, where you're located, and more. For law firms, schema markup is highly recommended and directly supports entity recognition, Knowledge Panel eligibility, and AI citation potential."},
      {"q":"How long does it take to build a strong entity profile?","a":"Building a comprehensive entity profile is a 3–6 month project for most law firms. The first priority is consistency across existing profiles, followed by schema implementation, then earned mentions and citations. Progress is incremental but compounds over time."},
      {"q":"Can a small law firm benefit from entity SEO?","a":"Absolutely. Entity SEO actually levels the playing field somewhat — a small firm with a perfectly consistent, well-documented entity profile can outperform a larger firm with inconsistent online presence. The signals Google and AI use for entity recognition don't inherently favor size."}
    ],
    "related":[
      {"title":"Schema Markup for Lawyers: The Complete Guide","href":"schema-markup-for-lawyers-guide.html"},
      {"title":"How to Get Your Law Firm Knowledge Panel","href":"attorney-knowledge-panel-optimization.html"},
      {"title":"Entity SEO vs Keyword SEO for Law Firms","href":"entity-seo-vs-keyword-seo.html"},
    ]
  },
  "ai-website-design-for-law-firms-guide.html": {
    "h1":"AI Website Design for Law Firms:", "h1_accent":"The Complete Guide",
    "deck":"Your website is your most powerful marketing asset. An AI-optimized law firm website ranks higher, gets cited by AI engines, and converts more visitors into clients.",
    "sections":[
      {"h2":"Why Most Law Firm Websites Underperform","paras":["The average law firm website was built to look professional — not to perform. It has a nice logo, stock photos of courthouses, and a contact page. But it loads slowly, ranks poorly on Google, fails on mobile, and converts less than 2% of visitors into leads. In an era where your website is your firm's primary marketing vehicle, that's an unacceptable performance.","CALLOUT:A law firm website that scores 95+ on Google PageSpeed, ranks on page one for local searches, and has clear conversion pathways can generate 3–5x more client inquiries than an average firm website — without spending more on advertising.","AI-optimized law firm websites are built differently from the ground up. They're engineered for speed, designed with conversion psychology, structured for search engine comprehension, and built to be cited by AI platforms like ChatGPT and Gemini."]},
      {"h2":"The Five Elements of an AI-Optimized Law Firm Website","paras":["First: Speed. Your site must load in under 2 seconds on mobile. Google's Core Web Vitals are now a ranking factor, and AI search engines favor sources that provide good user experiences. Slow sites get penalized and deprioritized.","Second: Structure. AI engines and search bots need to understand your content hierarchy. This means proper H1/H2/H3 heading structure, clear practice area pages, attorney bio pages, and schema markup that explicitly identifies your firm's services and location.","Third: Content depth. Thin pages don't rank and don't get cited by AI. Each practice area page should be at least 1,500 words, covering what the law says, how your firm approaches cases, what clients can expect, and FAQs. This depth signals expertise.","Fourth: Conversion pathways. Every page should have a clear call to action — a phone number in the header, a contact form above the fold, a chatbot, and a sticky CTA bar. Don't make visitors hunt for how to contact you.","UL:Sub-2 second load time on mobile|Clear heading structure (H1 > H2 > H3)|1,500+ word practice area pages|Schema markup for LegalService and LocalBusiness|Multiple conversion pathways on every page"]},
      {"h2":"Technical Requirements for AI Visibility","paras":["To be cited by AI search engines, your website needs to be technically impeccable. This means valid HTML, no broken links, a proper sitemap, robots.txt configuration, and HTTPS. It also means implementing structured data in JSON-LD format — the schema markup that tells AI systems exactly what your firm is and does.","Core Web Vitals are increasingly important. Largest Contentful Paint (LCP) should be under 2.5 seconds. Cumulative Layout Shift (CLS) should be below 0.1. First Input Delay (FID) or Interaction to Next Paint (INP) should be under 200ms. Achieving these scores requires careful engineering of your site's code, images, and hosting infrastructure."]},
      {"h2":"What Makes a Law Firm Website Convert","paras":["Conversion optimization for law firms follows clear principles. Trust signals — reviews, case results, bar memberships, photos of real attorneys — increase the likelihood of contact. Urgency framing — emphasizing free consultations, same-day response, 24/7 availability — reduces friction. Clear hierarchy — leading with your strongest differentiator — ensures visitors understand your value proposition within 5 seconds of landing."]}
    ],
    "faqs":[
      {"q":"How much does an AI-optimized law firm website cost?","a":"Quality AI-optimized law firm websites typically range from $5,000–$20,000 for custom builds, or $300–$800/month for managed platforms. The investment pays back quickly when the site generates consistent leads — most firms recoup the cost within 2–4 months of launch."},
      {"q":"How long does it take to build a law firm website?","a":"A properly built law firm website takes 4–8 weeks from kickoff to launch. This includes discovery, design, content creation, development, schema implementation, and testing. Rushing the process typically results in performance issues that hurt long-term results."},
      {"q":"Do I need a custom website or is a template okay?","a":"Templates can work if they're built on a performance-first platform and properly optimized. However, custom websites offer significantly more control over technical performance, schema implementation, and conversion optimization. For competitive markets, custom is almost always worth the investment."},
      {"q":"How often should a law firm update its website?","a":"Content should be updated regularly — new blog posts monthly, practice area pages reviewed annually, attorney bios updated as needed. The technical foundation (hosting, plugins, code) should be reviewed quarterly. A stale, outdated website sends negative signals to both users and search engines."},
      {"q":"What platform should a law firm website be built on?","a":"The best platforms for law firm websites in 2025 are Next.js (for maximum performance), WordPress with a performance theme, or Webflow. The platform matters less than how it's implemented — a well-built WordPress site will outperform a poorly built Next.js site every time."}
    ],
    "related":[
      {"title":"Law Firm Website Conversion Optimization","href":"law-firm-website-conversion-optimization.html"},
      {"title":"Law Firm Website Speed & Performance Guide","href":"law-firm-website-speed-performance.html"},
      {"title":"How to Structure Your Law Firm Website for SEO","href":"law-firm-website-seo-structure.html"},
    ]
  }
}

def get_article_content(filename, category, category_href, fallback_title, fallback_desc, related_articles):
    if filename in ARTICLE_CONTENT:
        d = ARTICLE_CONTENT[filename]
        return d["h1"], d["h1_accent"], d["deck"], d["sections"], d["faqs"], d["related"]
    # Fallback generic content
    h1_parts = fallback_title.rsplit(":",1)
    h1 = h1_parts[0] if len(h1_parts)>1 else fallback_title
    h1_accent = h1_parts[1].strip() if len(h1_parts)>1 else ""
    sections = [
      {"h2":f"Understanding {fallback_title}","paras":[f"Law firms that invest in {category.lower()} are positioning themselves ahead of competitors who haven't started. The landscape is shifting rapidly, and early movers consistently capture disproportionate market share.",fallback_desc,"CALLOUT:The firms that win in the next 5 years will be those that adopted AI-powered marketing strategies before their competitors. Now is the time to act."]},
      {"h2":"Key Strategies and Best Practices","paras":["A comprehensive approach requires focusing on multiple areas simultaneously. Start with the fundamentals — ensure your online presence is consistent, professional, and technically sound — then layer in more advanced strategies as your foundation strengthens.","UL:Audit your current online presence and identify gaps|Prioritize the highest-impact improvements first|Implement changes systematically and track results|Continuously optimize based on performance data"]},
      {"h2":"Implementation and Next Steps","paras":["Getting started doesn't have to be overwhelming. The most important step is taking action. Even small improvements compound over time, and the firms that begin their AI SEO and marketing journey today will be the dominant players in their markets within 12–18 months."]}
    ]
    faqs = [
      {"q":f"How does {category} help law firms grow?","a":f"{category} helps law firms attract more qualified clients by improving visibility across search engines and AI platforms, automating lead capture, and creating more professional client experiences."},
      {"q":"How long does it take to see results?","a":"Most law firms begin seeing meaningful results within 60–90 days of implementing a comprehensive strategy. Full impact is typically realized within 6–12 months."},
      {"q":"Is this right for a small law firm?","a":"Absolutely. In fact, smaller firms often see the highest percentage ROI from these strategies because they're starting from a lower baseline and have more room to grow."},
      {"q":"What does LexScale do differently?","a":"LexScale builds comprehensive AI-first growth systems designed specifically for law firms — combining website performance, SEO, AI search optimization, and lead capture into a single integrated strategy."},
    ]
    related = related_articles[:3]
    return h1, h1_accent, fallback_desc, sections, faqs, related

# ============================================================
# GENERATE FILES
# ============================================================
created = []

for cat_key, cat in CATEGORIES.items():
    articles = cat["articles"]
    hub_articles = [{"title":a["title"],"desc":a["desc"],"href":a["file"],"rt":a["rt"],"date":a["date"]} for a in articles]
    
    # Hub page
    content = hub_page(
        cat["hub_file"], cat["title"], cat["meta_desc"],
        cat["h1"], cat["accent"], cat["hero_desc"],
        cat["tag"], cat["tag_color"], hub_articles, cat["stats"]
    )
    with open(os.path.join(BASE, cat["hub_file"]), "w") as f:
        f.write(content)
    print(f"  ✓ hub: {cat['hub_file']}")
    created.append(cat["hub_file"])
    
    # Article pages
    for a in articles:
        related_others = [{"title":o["title"],"href":o["file"]} for o in articles if o["file"] != a["file"]]
        h1, h1a, deck, sections, faqs, related = get_article_content(
            a["file"], cat["tag"], cat["hub_file"], a["title"], a["desc"], related_others
        )
        content = article_page(
            a["file"], a["title"], a["desc"],
            cat["tag"], cat["hub_file"],
            h1, h1a, deck, sections, faqs, related
        )
        with open(os.path.join(BASE, a["file"]), "w") as f:
            f.write(content)
        print(f"  ✓ article: {a['file']}")
        created.append(a["file"])

print(f"\nTotal: {len(created)} files created")
