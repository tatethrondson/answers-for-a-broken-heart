from pathlib import Path
import re

DESIGN_START = '<!-- HOMEPAGE-DESIGN-SYSTEM-START -->'
DESIGN_END = '<!-- HOMEPAGE-DESIGN-SYSTEM-END -->'
HEADER_START = '<!-- PREMIUM-SHELL-HEADER-START -->'
HEADER_END = '<!-- PREMIUM-SHELL-HEADER-END -->'
FOOTER_START = '<!-- PREMIUM-SHELL-FOOTER-START -->'
FOOTER_END = '<!-- PREMIUM-SHELL-FOOTER-END -->'

DESIGN_LINK = DESIGN_START + '<link rel="stylesheet" href="/site-cohesive.css?v=2">' + DESIGN_END

HEADER = f'''{HEADER_START}<header class="siteShellHeader"><div class="siteShellWrap siteShellNav"><a class="siteShellBrand" href="/" aria-label="Answers for a Broken Heart home"><span class="siteShellBrandWords">Answers<small>for a Broken Heart</small></span><span class="siteShellHeart">♡</span></a><nav class="siteShellLinks" aria-label="Main navigation"><a href="/start-here">Start Here</a><a href="/all-answers">24 Answers</a><a href="/free-guides">Free Resources</a><a href="/book">The Book</a><a href="/about">About</a></nav><details class="siteShellMobile"><summary>Menu</summary><nav class="siteShellMobileMenu" aria-label="Mobile navigation"><a href="/start-here">Start Here</a><a href="/all-answers">24 Answers</a><a href="/free-guides">Free Resources</a><a href="/book">The Book</a><a href="/about">About</a></nav></details></div></header>{HEADER_END}'''

FOOTER = f'''{FOOTER_START}<footer class="siteShellFooter"><div class="siteShellWrap siteShellFooterGrid"><div><div class="siteShellFooterBrand">Answers<small>for a Broken Heart</small></div><div class="siteShellFooterTag">Biblical hope for grief, suffering, doubt, unanswered prayer, and the questions pain asks.</div></div><nav class="siteShellFooterLinks" aria-label="Footer navigation"><a href="/start-here">Start Here</a><a href="/all-answers">24 Answers</a><a href="/free-guides">Free Resources</a><a href="/church-resources">Church Resources</a><a href="/book">The Book</a><a href="/about">About</a><a href="/contact">Contact</a></nav><div class="siteShellCopyright">© 2026 Tate Throndson · Psalm 34:18 · Resources are pastoral and educational and are not a substitute for emergency, medical, or mental-health care.</div></div></footer>{FOOTER_END}'''


def strip_marked(text: str, start: str, end: str) -> str:
    return re.sub(re.escape(start) + r'.*?' + re.escape(end), '', text, flags=re.S)


def ensure_design_link(text: str, filename: str) -> str:
    text = strip_marked(text, DESIGN_START, DESIGN_END)
    if filename != 'index.html' and '</head>' in text:
        text = text.replace('</head>', DESIGN_LINK + '\n</head>', 1)
    return text


def ensure_shell(text: str) -> str:
    text = strip_marked(text, HEADER_START, HEADER_END)
    text = strip_marked(text, FOOTER_START, FOOTER_END)
    text = re.sub(r'<header\b.*?</header>', '', text, count=1, flags=re.S | re.I)
    body = re.search(r'<body\b[^>]*>', text, flags=re.I)
    if body:
        text = text[:body.end()] + '\n' + HEADER + text[body.end():]
    text = re.sub(r'<footer\b.*?</footer>', '', text, flags=re.S | re.I)
    analytics = '<!-- CONVERSION-ANALYTICS-START -->'
    if analytics in text:
        text = text.replace(analytics, FOOTER + '\n' + analytics, 1)
    elif '</body>' in text:
        text = text.replace('</body>', FOOTER + '\n</body>', 1)
    else:
        text += '\n' + FOOTER
    return text


def simplify_home(text: str) -> str:
    text = text.replace(
        '<h1>When your heart is broken, you need more than a cliché.</h1><p class="heroLead">No pretending. No shallow answers. Just Scripture, honesty, and a path toward hope.</p><div class="heroButtons"><a class="btn primary" href="/start-here">I’m Hurting — Start Here</a> <a class="btn outline" href="/all-answers">Browse the 24 Answers</a></div>',
        '<h1>Something hurts. You don’t have to know where to begin.</h1><p class="heroLead">Tell me where it hurts, and I’ll help you find a biblical place to begin.</p><div class="heroButtons"><a class="btn primary" href="/start-here">Tell Me Where It Hurts</a> <a class="btn outline" href="/all-answers">Browse the 24 Answers</a></div>'
    )
    text = text.replace(
        '<a class="careChoiceCard" href="/all-answers"><small>I’m hurting</small><strong>Help me find the question underneath the pain.</strong><span>Search grief, depression, anger, doubt, betrayal, unanswered prayer, loneliness, and more in your own words.</span></a>',
        '<a class="careChoiceCard" href="/start-here"><small>I’m hurting</small><strong>Help me find a place to begin.</strong><span>Choose the hurt that feels closest—grief, suffering, unanswered prayer, relational pain, doubt, or emotional heaviness.</span></a>'
    )
    return text


def clean_answers_library(text: str) -> str:
    text = re.sub(r'<div class="num">Answer \d{2} · .*?</div>', '', text, flags=re.S)
    return text


def tighten_about_page(text: str) -> str:
    text = re.sub(r'<section class="section approach">.*?</section>', '', text, count=1, flags=re.S)
    return text


def refine_free_resources(text: str) -> str:
    text = text.replace('<h2>Free guides for hard days.</h2>', '<h2>Free resources for hard days.</h2>', 1)
    return text


for path in Path('.').glob('*.html'):
    if path.name == 'photo-test.html':
        continue
    text = path.read_text(encoding='utf-8')
    original = text
    if path.name == 'index.html':
        text = simplify_home(text)
    elif path.name == 'all-answers.html':
        text = clean_answers_library(text)
    elif path.name == 'book.html':
        # The Book page now has its own current-design structure. Do not inject
        # legacy bookBand/bookUpdates/bookForYou components into it.
        pass
    elif path.name == 'about.html':
        text = tighten_about_page(text)
    elif path.name == 'free-guides.html':
        text = refine_free_resources(text)
    text = ensure_design_link(text, path.name)
    text = ensure_shell(text)
    if text != original:
        path.write_text(text, encoding='utf-8')
        print('Unified homepage design and reader flow:', path.name)
