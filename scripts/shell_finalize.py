from pathlib import Path
import re

CSS_START='<!-- PREMIUM-SHELL-CSS-START -->'
CSS_END='<!-- PREMIUM-SHELL-CSS-END -->'
HEADER_START='<!-- PREMIUM-SHELL-HEADER-START -->'
HEADER_END='<!-- PREMIUM-SHELL-HEADER-END -->'
FOOTER_START='<!-- PREMIUM-SHELL-FOOTER-START -->'
FOOTER_END='<!-- PREMIUM-SHELL-FOOTER-END -->'
RUNTIME_START='<!-- SITE-SHELL-RUNTIME-START -->'
RUNTIME_END='<!-- SITE-SHELL-RUNTIME-END -->'

HEADER=f'''{HEADER_START}<header class="siteShellHeader"><div class="siteShellWrap siteShellNav"><a class="siteShellBrand" href="/" aria-label="Answers for a Broken Heart home"><span class="siteShellBrandWords">Answers<small>for a Broken Heart</small></span><span class="siteShellHeart">♡</span></a><nav class="siteShellLinks" aria-label="Main navigation"><a href="/start-here">Start Here</a><a href="/all-answers">24 Answers</a><a href="/free-guides">Free Resources</a><a href="/book">The Book</a><a href="/about">About</a></nav><details class="siteShellMobile"><summary>Menu</summary><nav class="siteShellMobileMenu" aria-label="Mobile navigation"><a href="/start-here">Start Here</a><a href="/all-answers">24 Answers</a><a href="/free-guides">Free Resources</a><a href="/book">The Book</a><a href="/about">About</a></nav></details></div></header>{HEADER_END}'''

FOOTER=f'''{FOOTER_START}<footer class="siteShellFooter"><div class="siteShellWrap siteShellFooterGrid"><div><div class="siteShellFooterBrand">Answers<small>for a Broken Heart</small></div><div class="siteShellFooterTag">Biblical hope for grief, suffering, doubt, unanswered prayer, and the questions pain asks.</div></div><nav class="siteShellFooterLinks" aria-label="Footer navigation"><a href="/start-here">Start Here</a><a href="/all-answers">24 Answers</a><a href="/free-guides">Free Resources</a><a href="/church-resources">Church Resources</a><a href="/book">The Book</a><a href="/about">About</a><a href="/contact">Contact</a></nav><div class="siteShellCopyright">© 2026 Tate Throndson · Psalm 34:18 · Resources are pastoral and educational and are not a substitute for emergency, medical, or mental-health care.</div></div></footer>{FOOTER_END}'''

ASSETS='''<link rel="stylesheet" href="/site-body-lock-v2.css?v=2">\n<link rel="stylesheet" href="/site-shell.css?v=2">\n<!-- SITE-SHELL-RUNTIME-START --><script defer src="/site-shell.js?v=2"></script><!-- SITE-SHELL-RUNTIME-END -->'''


def strip_marked(text,start,end):
    return re.sub(re.escape(start)+r'.*?'+re.escape(end),'',text,flags=re.S)


def remove_premain_headers(text):
    body=re.search(r'<body\b[^>]*>',text,flags=re.I)
    if not body:
        return text
    main=re.search(r'<main\b',text[body.end():],flags=re.I)
    end=body.end()+(main.start() if main else min(8000,len(text)-body.end()))
    prefix=text[:end]
    suffix=text[end:]
    prefix=re.sub(r'<header\b[^>]*>.*?</header>','',prefix,flags=re.S|re.I)
    prefix=re.sub(r'<nav\b[^>]*aria-label=["\'](?:Main navigation|Mobile navigation)["\'][^>]*>.*?</nav>','',prefix,flags=re.S|re.I)
    return prefix+suffix


for path in sorted(Path('.').glob('*.html')):
    text=path.read_text(encoding='utf-8')
    original=text

    text=strip_marked(text,CSS_START,CSS_END)
    text=strip_marked(text,HEADER_START,HEADER_END)
    text=strip_marked(text,FOOTER_START,FOOTER_END)
    text=strip_marked(text,RUNTIME_START,RUNTIME_END)

    text=re.sub(r'<link\s+rel=["\']stylesheet["\']\s+href=["\']/site-shell\.css(?:\?[^"\']*)?["\']\s*/?>','',text,flags=re.I)
    text=re.sub(r'<link\s+rel=["\']stylesheet["\']\s+href=["\']/site-body-lock-v2\.css(?:\?[^"\']*)?["\']\s*/?>','',text,flags=re.I)
    text=re.sub(r'<script\b[^>]*src=["\']/site-shell\.js(?:\?[^"\']*)?["\'][^>]*></script>','',text,flags=re.I)

    text=remove_premain_headers(text)
    text=re.sub(r'<footer\b[^>]*>.*?</footer>','',text,flags=re.S|re.I)

    body=re.search(r'<body\b[^>]*>',text,flags=re.I)
    if body:
        text=text[:body.end()]+'\n'+HEADER+'\n'+text[body.end():]
    else:
        print('WARNING: no body tag in',path.name)

    if '</head>' in text:
        text=text.replace('</head>',ASSETS+'\n</head>',1)
    else:
        print('WARNING: no head close in',path.name)

    analytics='<!-- CONVERSION-ANALYTICS-START -->'
    if analytics in text:
        text=text.replace(analytics,FOOTER+'\n\n'+analytics,1)
    elif '</body>' in text:
        text=text.replace('</body>',FOOTER+'\n</body>',1)
    else:
        text+='\n'+FOOTER

    if text!=original:
        path.write_text(text,encoding='utf-8')
        print('Finalized shared shell:',path.name)
