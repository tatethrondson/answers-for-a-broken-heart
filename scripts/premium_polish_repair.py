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

HEADER=f'''{HEADER_START}<header class="siteShellHeader"><div class="siteShellWrap siteShellNav"><a class="siteShellBrand" href="/"><span class="siteShellBrandWords">Answers<small>for a Broken Heart</small></span><span class="siteShellHeart">♡</span></a><nav class="siteShellLinks" aria-label="Main navigation"><a href="/">Home</a><a href="/start-here">Start Here</a><a href="/all-answers">24 Answers</a><a href="/free-guides">Free Guides</a><a href="/book">The Book</a><a href="/about">About</a><a href="/contact">Contact</a></nav><details class="siteShellMobile"><summary>Menu</summary><nav class="siteShellMobileMenu" aria-label="Mobile navigation"><a href="/">Home</a><a href="/start-here">Start Here</a><a href="/all-answers">24 Answers</a><a href="/free-guides">Free Guides</a><a href="/book">The Book</a><a href="/about">About</a><a href="/contact">Contact</a></nav></details></div></header>{HEADER_END}'''

FOOTER=f'''{FOOTER_START}<footer class="siteShellFooter"><div class="siteShellWrap siteShellFooterGrid"><div><div class="siteShellFooterBrand">Answers<small>for a Broken Heart</small></div><div class="siteShellFooterTag">Biblical hope for grief, suffering, doubt, unanswered prayer, and the questions pain asks.</div></div><nav class="siteShellFooterLinks" aria-label="Footer navigation"><a href="/start-here">Start Here</a><a href="/all-answers">24 Answers</a><a href="/free-guides">Free Guides</a><a href="/church-resources">Church Resources</a><a href="/book">The Book</a><a href="/about">About</a><a href="/contact">Contact</a></nav><div class="siteShellCopyright">© 2026 Tate Throndson · Psalm 34:18 · Resources are pastoral and educational and are not a substitute for emergency, medical, or mental-health care.</div></div></footer>{FOOTER_END}'''

EXCLUDE={'unsafe.html','2am-guide-access.html','hope-thanks.html','book-updates-thanks.html','contact-thanks.html'}

CARD_COPY_REPLACEMENTS={
    'He’s Always Been There →':'He’s always been there. →',
    'He Showed You His Face →':'He showed you His face. →',
    'You’ll See It Looking Back →':'Some things become clearer looking back. →',
    'This Is Not the World He Made →':'This is not the world God called very good. →',
    'Honest Questions Are Not Unbelief →':'Honest questions are not unbelief. →',
    'He Knows More Than You Do →':'Your view is not the whole story. →',
    'All Things — Even This →':'God can redeem even this. →',
    'Sometimes He Gives You Himself Instead of an Explanation →':'Sometimes He gives you Himself instead of an explanation. →',
    'He Wept With You →':'He wept with you. →',
    'He Didn’t Just Enter It — He Ended It →':'He entered it—and He will end it. →',
    'His Silence Isn’t His Approval →':'His silence isn’t His approval. →',
    'A No Is Not the End of the Story →':'A no is not the end of the story. →',
    'Death Does Not Get the Final Word →':'Death does not get the final word. →',
    'You’re Allowed to Grieve as Long as It Takes →':'You’re allowed to grieve as long as it takes. →',
    'Ask a Different Question →':'When you’re ready, ask a different question. →',
    'Grief That Stops Moving Becomes Bitterness →':'Healing is not a straight line. →',
    'Anger at God Is Not the Opposite of Faith →':'Anger at God is not the opposite of faith. →',
    'Bring Him the Real Prayer, Not the Polished One →':'Bring Him the real prayer, not the polished one. →',
    'Your Pain and Their Guilt Are Not the Same Conversation →':'Your pain and their guilt are not the same conversation. →',
    'To Be Loved Is to Be Woundable →':'To be loved is to be woundable. →',
    'Forgiving Them Lets You Look Like Your Father →':'Forgiveness releases vengeance without calling the wrong right. →',
    'Forgiveness Is Not Reconciliation →':'Forgiveness is not reconciliation. →',
    'Make Sure You’re Rejecting the Real Thing →':'Separate Jesus from what was done in His name. →',
    'Your Doubt Is Not Disqualifying →':'Your doubt is not disqualifying. →',
}

TEXT_REPLACEMENTS={
    'Isn’t His sympathy enough?':'Is sympathy all God offers?',
    'Forgiveness & Relational Hurt':'Relational Hurt & Forgiveness',
    'Doubt, Church Hurt & Faith':'Doubt & Church Hurt',
}

def strip(text,start,end):
    return re.sub(re.escape(start)+r'.*?'+re.escape(end),'',text,flags=re.S)

def normalize_legacy_content(text):
    # Keep raw HTML aligned with the site's canonical routes instead of relying on
    # client-side correction after the page loads.
    text=text.replace('href="/?view=book"','href="/book"')
    text=text.replace('href="/what-hurts-today">Browse All 24 Answers','href="/all-answers">Browse All 24 Answers')
    text=text.replace('href="/what-hurts-today">See all 24 questions','href="/all-answers">See all 24 questions')
    text=re.sub(
        r'"name"\s*:\s*"What Hurts Today\?"\s*,\s*"item"\s*:\s*"https://answersforabrokenheart\.com/what-hurts-today"',
        '"name": "24 Biblical Answers", "item": "https://answersforabrokenheart.com/all-answers"',
        text
    )
    for old,new in TEXT_REPLACEMENTS.items():
        text=text.replace(old,new)
    for old,new in CARD_COPY_REPLACEMENTS.items():
        text=text.replace(old,new)
    return text

for path in Path('.').glob('*.html'):
    if path.name in EXCLUDE:
        continue
    text=path.read_text(encoding='utf-8')
    original=text
    text=strip(text,CSS_START,CSS_END)
    text=strip(text,HEADER_START,HEADER_END)
    text=strip(text,FOOTER_START,FOOTER_END)
    while '?v=7?v=7' in text:
        text=text.replace('?v=7?v=7','?v=7')
    text=normalize_legacy_content(text)

    # Header always belongs immediately after <body> once any legacy header is removed.
    text=re.sub(r'<header\b.*?</header>','',text,count=1,flags=re.S|re.I)
    text=text.replace('<body>','<body>\n'+HEADER,1)

    # Remove any legacy footer wherever an older template placed it. Then put the one
    # universal footer after all visible content, immediately before analytics/scripts.
    text=re.sub(r'<footer\b.*?</footer>','',text,flags=re.S|re.I)
    analytics='<!-- CONVERSION-ANALYTICS-START -->'
    if analytics in text:
        text=text.replace(analytics,FOOTER+'\n'+analytics,1)
    elif '</body>' in text:
        text=text.replace('</body>',FOOTER+'\n</body>',1)
    else:
        text += '\n'+FOOTER

    text=text.replace('</head>',CSS+'\n</head>',1)
    if path.name=='contact.html':
        text=text.replace('Fill this out and we’ll prepare an email addressed directly to Tate.','Fill this out and your message will be sent directly to Tate.')
    if text!=original:
        path.write_text(text,encoding='utf-8')
        print('Repaired premium shell',path.name)
