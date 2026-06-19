#!/usr/bin/env python3
"""
patch_mobile_nav.py — Add working mobile hamburger menu to all 53 existing HTML pages.

Three changes per file:
  1. Inject hamburger <button> inside <nav> (before </nav>)
  2. Replace old single-line @media mobile block with full mobile menu CSS
  3. Replace old <script> block (or inject before </body>) with updated JS
     that includes toggleMobNav() and mobile accordion sub-menu logic
"""

import re, os, glob

BASE = os.path.dirname(os.path.abspath(__file__))

def read(f):  return open(os.path.join(BASE, f), encoding="utf-8").read()
def write(f, c): open(os.path.join(BASE, f), "w", encoding="utf-8").write(c)

# ─── Snippets ─────────────────────────────────────────────────────────────────

HAMBURGER_BTN = '''\
  <button class="nav-mob" aria-label="Open menu" onclick="toggleMobNav(this)">
    <span></span><span></span><span></span>
  </button>'''

MOBILE_CSS = '''\
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
}'''

MOB_JS = '''\
<script>
function toggleFaq(el){
  const item=el.closest('.faq-item');
  const isOpen=item.classList.contains('open');
  document.querySelectorAll('.faq-item.open').forEach(i=>i.classList.remove('open'));
  if(!isOpen) item.classList.add('open');
}
function toggleMobNav(btn){
  const nav=btn.closest('nav');
  nav.classList.toggle('mob-open');
}
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
    if(nav&&nav.classList.contains('mob-open')&&!nav.contains(e.target)){
      nav.classList.remove('mob-open');
    }
  });
});
</script>'''

# ─── Patch each HTML file ─────────────────────────────────────────────────────

files = sorted(glob.glob(os.path.join(BASE, "*.html")))
patched = 0
skipped = 0

for fpath in files:
    fname = os.path.basename(fpath)
    html = read(fname)
    original = html
    changed = False

    # ── 1. Add hamburger button ─────────────────────────────────────────────
    if 'class="nav-mob"' not in html:
        # Insert before </nav>
        html = html.replace('</nav>', HAMBURGER_BTN + '\n</nav>', 1)
        changed = True

    # ── 2. Replace mobile CSS ────────────────────────────────────────────────
    # Match any existing @media(max-width:768px){...} block (single or multi-line)
    # Two patterns: old single-line compact form and older multi-line form
    old_media_patterns = [
        # single-line from seo_upgrade.py
        r'@media\(max-width:768px\)\{[^}]*\.nav-links\{display:none[^}]*\}[^}]*\}',
        # multi-line variant
        r'@media\s*\(max-width:\s*768px\)\s*\{[\s\S]*?\.nav-links[\s\S]*?\}[\s\S]*?\}',
    ]

    if '.nav-mob{display:none' not in html:
        replaced = False
        for pat in old_media_patterns:
            m = re.search(pat, html)
            if m:
                html = html[:m.start()] + MOBILE_CSS + html[m.end():]
                replaced = True
                changed = True
                break

        if not replaced:
            # No @media block found — append CSS before </style>
            if '</style>' in html:
                html = html.replace('</style>', MOBILE_CSS + '\n</style>', 1)
                changed = True

    # ── 3. Replace or inject JS ──────────────────────────────────────────────
    if 'toggleMobNav' not in html:
        # Replace existing toggleFaq script block if present
        old_js = re.search(
            r'<script>\s*function toggleFaq[\s\S]*?</script>',
            html
        )
        if old_js:
            html = html[:old_js.start()] + MOB_JS + html[old_js.end():]
            changed = True
        else:
            # No existing script — inject before </body>
            html = html.replace('</body>', MOB_JS + '\n</body>', 1)
            changed = True

    if changed:
        write(fname, html)
        patched += 1
        print(f"  ✓ {fname}")
    else:
        skipped += 1

print(f"\n✅ {patched} pages patched, {skipped} already up to date")

# ─── Quick verification ────────────────────────────────────────────────────────
print("\n=== Verification ===")
missing_btn = [os.path.basename(f) for f in files if 'class="nav-mob"' not in read(os.path.basename(f))]
missing_js  = [os.path.basename(f) for f in files if 'toggleMobNav' not in read(os.path.basename(f))]
missing_css = [os.path.basename(f) for f in files if 'nav-mob{display:none' not in read(os.path.basename(f))]

print(f"  Pages missing hamburger button : {len(missing_btn)}")
print(f"  Pages missing mobile JS        : {len(missing_js)}")
print(f"  Pages missing mobile CSS       : {len(missing_css)}")
if missing_btn: print("  MISSING BTN:", missing_btn[:5])
if missing_js:  print("  MISSING JS:",  missing_js[:5])
if missing_css: print("  MISSING CSS:", missing_css[:5])
