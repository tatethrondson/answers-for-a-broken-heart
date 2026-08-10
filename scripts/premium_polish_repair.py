from pathlib import Path
import re

CSS_START='<!-- PREMIUM-SHELL-CSS-START -->'
CSS_END='<!-- PREMIUM-SHELL-CSS-END -->'
HEADER_START='<!-- PREMIUM-SHELL-HEADER-START -->'
HEADER_END='<!-- PREMIUM-SHELL-HEADER-END -->'
FOOTER_START='<!-- PREMIUM-SHELL-FOOTER-START -->'
FOOTER_END='<!-- PREMIUM-SHELL-FOOTER-END -->'

CSS=f'''{CSS_START}<style>
.siteShellHeader{{position:sticky!important;top:0!important;z-index:90!important;background:rgba(255,254,251,.97)!important;border-bottom:1px solid rgba(33,49,40,.09)!important;backdrop-filter:blur(12px);color:#24312b!important}}
.siteShellWrap{{width:min(1160px,calc(100% - 44px));margin:auto}}.siteShellNav{{min-height:74px;display:flex;align-items:center;justify-content:space-between;gap:24px}}.siteShellBrand{{display:flex;align-items:center;gap:8px;text-decoration:none!important;color:#183024!important;line-height:.84}}.siteShellBrandWords{{font:1.62rem/.82 Georgia,"Times New Roman",serif;letter-spacing:-.04em}}.siteShellBrandWords small{{display:block;font-size:.74rem;letter-spacing:-.01em}}.siteShellHeart{{font:1.8rem Georgia,"Times New Roman",serif;color:#ad823d}}.siteShellLinks{{display:flex;align-items:center;gap:22px;font-size:.76rem;font-weight:700}}.siteShellLinks a{{text-decoration:none!important;color:#334139!important;white-space:nowrap}}.siteShellLinks a:hover{{color:#294533!important}}.siteShellMobile{{display:none;position:relative}}.siteShellMobile summary{{list-style:none;cursor:pointer;border:1px solid #ded8cd;background:#fff;padding:8px 12px;font-size:.73rem;font-weight:800;color:#294533}}.siteShellMobile summary::-webkit-details-marker{{display:none}}.siteShellMobileMenu{{position:absolute;right:0;top:44px;width:230px;background:#fff;border:1px solid #ded8cd;box-shadow:0 16px 36px rgba(30,44,35,.14);padding:8px}}.siteShellMobileMenu a{{display:block;text-decoration:none!important;color:#334139!important;padding:10px 11px;font-size:.78rem;font-weight:700;border-bottom:1px solid #eee9df}}.siteShellMobileMenu a:last-child{{border-bottom:0}}
.siteShellFooter{{background:#183024!important;color:rgba(255,255,255,.84)!important;padding:36px 0 30px!important;font-size:.76rem!important}}.siteShellFooterGrid{{display:grid;grid-template-columns:240px 1fr;gap:48px;align-items:start}}.siteShellFooterBrand{{font:1.45rem/.9 Georgia,"Times New Roman",serif;color:#fff}}.siteShellFooterBrand small{{display:block;font-size:.72rem;color:rgba(255,255,255,.7)}}.siteShellFooterTag{{margin-top:12px;color:rgba(255,255,255,.65);font-size:.71rem;line-height:1.5}}.siteShellFooterLinks{{display:flex;justify-content:flex-end;gap:18px 22px;flex-wrap:wrap}}.siteShellFooterLinks a{{text-decoration:none!important;color:rgba(255,255,255,.86)!important;font-size:.72rem}}.siteShellCopyright{{grid-column:1/-1;border-top:1px solid rgba(255,255,255,.13);padding-top:18px;color:rgba(255,255,255,.55);font-size:.67rem}}
@media(max-width:900px){{.siteShellLinks{{gap:14px;font-size:.7rem}}}}@media(max-width:760px){{.siteShellLinks{{display:none}}.siteShellMobile{{display:block}}.siteShellFooterGrid{{grid-template-columns:1fr;gap:22px}}.siteShellFooterLinks{{justify-content:flex-start}}.siteShellCopyright{{grid-column:1}}.siteShellWrap{{width:min(100% - 30px,1160px)}}}}
</style>{CSS_END}'''

HEADER=f'''{HEADER_START}<header class="siteShellHeader"><div class="siteShellWrap siteShellNav"><a class="siteShellBrand" href="/"><span class="siteShellBrandWords">Answers<small>for a Broken Heart</small></span><span class="siteShellHeart">♡</span></a><nav class="siteShellLinks" aria-label="Main navigation"><a href="/">Home</a><a href="/start-here">Start Here</a><a href="/all-answers">24 Answers</a><a href="/free-guides">Free Guides</a><a href="/?view=book">The Book</a><a href="/about">About Tate</a><a href="/contact">Contact</a></nav><details class="siteShellMobile"><summary>Menu</summary><nav class="siteShellMobileMenu" aria-label="Mobile navigation"><a href="/">Home</a><a href="/start-here">Start Here</a><a href="/all-answers">24 Answers</a><a href="/free-guides">Free Guides</a><a href="/?view=book">The Book</a><a href="/about">About Tate</a><a href="/contact">Contact</a></nav></details></div></header>{HEADER_END}'''

FOOTER=f'''{FOOTER_START}<footer class="siteShellFooter"><div class="siteShellWrap siteShellFooterGrid"><div><div class="siteShellFooterBrand">Answers<small>for a Broken Heart</small></div><div class="siteShellFooterTag">Biblical hope for grief, suffering, doubt, unanswered prayer, and the questions pain asks.</div></div><nav class="siteShellFooterLinks" aria-label="Footer navigation"><a href="/start-here">Start Here</a><a href="/all-answers">24 Answers</a><a href="/free-guides">Free Guides</a><a href="/church-resources">Church Resources</a><a href="/?view=book">The Book</a><a href="/about">About Tate</a><a href="/contact">Contact</a></nav><div class="siteShellCopyright">© 2026 Tate Throndson · Psalm 34:18 · Resources are pastoral and educational and are not a substitute for emergency, medical, or mental-health care.</div></div></footer>{FOOTER_END}'''

EXCLUDE={'unsafe.html','2am-guide-access.html','hope-thanks.html','book-updates-thanks.html','contact-thanks.html'}

def strip(text,start,end):
    return re.sub(re.escape(start)+r'.*?'+re.escape(end),'',text,flags=re.S)

for path in Path('.').glob('*.html'):
    if path.name in EXCLUDE:
        continue
    text=path.read_text(encoding='utf-8')
    original=text
    text=strip(text,CSS_START,CSS_END)
    text=strip(text,HEADER_START,HEADER_END)
    text=strip(text,FOOTER_START,FOOTER_END)
    # Normalize repeated cache-buster suffixes from prior polish passes.
    while '?v=7?v=7' in text:
        text=text.replace('?v=7?v=7','?v=7')
    # Replace a surviving legacy shell; otherwise insert the premium shell explicitly.
    if re.search(r'<header\b.*?</header>',text,flags=re.S|re.I):
        text=re.sub(r'<header\b.*?</header>',HEADER,text,count=1,flags=re.S|re.I)
    else:
        text=text.replace('<body>','<body>\n'+HEADER,1)
    footers=list(re.finditer(r'<footer\b.*?</footer>',text,flags=re.S|re.I))
    if footers:
        m=footers[-1]; text=text[:m.start()]+FOOTER+text[m.end():]
    elif '</main>' in text:
        text=text.replace('</main>','</main>\n'+FOOTER,1)
    else:
        text=text.replace('</body>',FOOTER+'\n</body>',1)
    text=text.replace('</head>',CSS+'\n</head>',1)
    if path.name=='contact.html':
        text=text.replace('Fill this out and we’ll prepare an email addressed directly to Tate.','Fill this out and your message will be sent directly to Tate.')
    if text!=original:
        path.write_text(text,encoding='utf-8')
        print('Repaired premium shell',path.name)
