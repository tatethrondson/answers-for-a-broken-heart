from pathlib import Path
import re

STYLE_LINKS = (
    '<link rel="stylesheet" href="/site-interior-v3.css?v=3">\n'
    '<link rel="stylesheet" href="/site-polish-v4.css?v=3">\n'
    '<link rel="stylesheet" href="/site-homepage-lock.css?v=1">'
)

HEADER = '''<!-- PREMIUM-SHELL-HEADER-START --><header class="siteShellHeader"><div class="siteShellWrap siteShellNav"><a class="siteShellBrand" href="/" aria-label="Answers for a Broken Heart home"><span class="siteShellBrandWords">Answers<small>for a Broken Heart</small></span><span class="siteShellHeart">♡</span></a><nav class="siteShellLinks" aria-label="Main navigation"><a href="/start-here">Start Here</a><a href="/all-answers">24 Answers</a><a href="/free-guides">Free Resources</a><a href="/book">The Book</a><a href="/about">About</a></nav><details class="siteShellMobile"><summary>Menu</summary><nav class="siteShellMobileMenu" aria-label="Mobile navigation"><a href="/start-here">Start Here</a><a href="/all-answers">24 Answers</a><a href="/free-guides">Free Resources</a><a href="/book">The Book</a><a href="/about">About</a></nav></details></div></header><!-- PREMIUM-SHELL-HEADER-END -->'''

FOOTER = '''<!-- PREMIUM-SHELL-FOOTER-START --><footer class="siteShellFooter"><div class="siteShellWrap siteShellFooterGrid"><div><div class="siteShellFooterBrand">Answers<small>for a Broken Heart</small></div><div class="siteShellFooterTag">Biblical hope for grief, suffering, doubt, unanswered prayer, and the questions pain asks.</div></div><nav class="siteShellFooterLinks" aria-label="Footer navigation"><a href="/start-here">Start Here</a><a href="/all-answers">24 Answers</a><a href="/free-guides">Free Resources</a><a href="/church-resources">Church Resources</a><a href="/book">The Book</a><a href="/about">About</a><a href="/contact">Contact</a></nav><div class="siteShellCopyright">© 2026 Tate Throndson · Psalm 34:18 · Resources are pastoral and educational and are not a substitute for emergency, medical, or mental-health care.</div></div></footer><!-- PREMIUM-SHELL-FOOTER-END -->'''

SKIP = {'index.html'}

LEGACY_SHARED_CSS = re.compile(
    r'<link\s+rel=["\']stylesheet["\']\s+href=["\']/'
    r'(?:site-cohesive|site-theme|site-unified|site-finish|site-phase[1-5])'
    r'\.css(?:\?v=[^"\']+)?["\']\s*/?>',
    flags=re.I,
)

for path in Path('.').glob('*.html'):
    if path.name in SKIP:
        continue

    text = path.read_text(encoding='utf-8')
    original = text

    text = re.sub(
        r'<!-- HOMEPAGE-DESIGN-SYSTEM-START -->.*?<!-- HOMEPAGE-DESIGN-SYSTEM-END -->',
        '', text, flags=re.S,
    )
    text = LEGACY_SHARED_CSS.sub('', text)

    for stylesheet in ('site-interior-v3.css', 'site-polish-v4.css', 'site-homepage-lock.css'):
        text = re.sub(
            rf'<link\s+rel=["\']stylesheet["\']\s+href=["\']/{re.escape(stylesheet)}'
            rf'(?:\?v=[^"\']+)?["\']\s*/?>',
            '', text, flags=re.I,
        )

    text = re.sub(
        r'<!-- PREMIUM-SHELL-CSS-START -->.*?<!-- PREMIUM-SHELL-CSS-END -->',
        '', text, flags=re.S,
    )
    text = re.sub(
        r'<!-- PREMIUM-SHELL-HEADER-START -->.*?<!-- PREMIUM-SHELL-HEADER-END -->',
        '', text, flags=re.S,
    )
    text = re.sub(
        r'<!-- PREMIUM-SHELL-FOOTER-START -->.*?<!-- PREMIUM-SHELL-FOOTER-END -->',
        '', text, flags=re.S,
    )
    text = re.sub(r'<header\b[^>]*>.*?</header>', '', text, count=1, flags=re.S | re.I)
    text = re.sub(r'<footer\b[^>]*>.*?</footer>', '', text, count=1, flags=re.S | re.I)

    if '</head>' in text:
        text = text.replace('</head>', STYLE_LINKS + '\n</head>', 1)

    page_class = 'page-' + re.sub(r'[^a-z0-9-]+', '-', path.stem.lower()).strip('-')

    def add_page_class(match):
        tag = match.group(0)
        cm = re.search(r'class=(["\'])(.*?)\1', tag, flags=re.I | re.S)
        if cm:
            classes = cm.group(2).split()
            if page_class not in classes:
                classes.append(page_class)
            replacement = 'class=' + cm.group(1) + ' '.join(classes) + cm.group(1)
            return tag[:cm.start()] + replacement + tag[cm.end():]
        return tag[:-1] + f' class="{page_class}">'

    text, _ = re.subn(r'<body\b[^>]*>', add_page_class, text, count=1, flags=re.I)
    text, body_count = re.subn(r'(<body\b[^>]*>)', r'\1\n' + HEADER + '\n', text, count=1, flags=re.I)
    if body_count == 0:
        print('WARNING: no <body> found:', path.name)

    analytics_marker = '<!-- CONVERSION-ANALYTICS-START -->'
    if analytics_marker in text:
        text = text.replace(analytics_marker, FOOTER + '\n\n' + analytics_marker, 1)
    elif '</body>' in text:
        text = text.replace('</body>', FOOTER + '\n</body>', 1)

    if text != original:
        path.write_text(text, encoding='utf-8')
        print('Normalized design and shell:', path.name)
