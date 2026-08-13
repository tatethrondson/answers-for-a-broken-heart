from pathlib import Path
import re

CSS_MARKER_START = '<!-- PREMIUM-SHELL-CSS-START -->'
CSS_MARKER_END = '<!-- PREMIUM-SHELL-CSS-END -->'
HEADER_MARKER_START = '<!-- PREMIUM-SHELL-HEADER-START -->'
HEADER_MARKER_END = '<!-- PREMIUM-SHELL-HEADER-END -->'
FOOTER_MARKER_START = '<!-- PREMIUM-SHELL-FOOTER-START -->'
FOOTER_MARKER_END = '<!-- PREMIUM-SHELL-FOOTER-END -->'

SHELL_CSS = f'''{CSS_MARKER_START}
<style>
.siteShellHeader{{position:sticky!important;top:0!important;z-index:90!important;background:rgba(255,254,251,.97)!important;border-bottom:1px solid rgba(33,49,40,.09)!important;backdrop-filter:blur(12px);color:#24312b!important}}
.siteShellWrap{{width:min(1160px,calc(100% - 44px));margin:auto}}
.siteShellNav{{min-height:74px;display:flex;align-items:center;justify-content:space-between;gap:24px}}
.siteShellBrand{{display:flex;align-items:center;gap:8px;text-decoration:none!important;color:#183024!important;line-height:.84}}
.siteShellBrandWords{{font:1.62rem/.82 Georgia,"Times New Roman",serif;letter-spacing:-.04em}}
.siteShellBrandWords small{{display:block;font-size:.74rem;letter-spacing:-.01em}}
.siteShellHeart{{font:1.8rem Georgia,"Times New Roman",serif;color:#ad823d}}
.siteShellLinks{{display:flex;align-items:center;gap:22px;font-size:.76rem;font-weight:700}}
.siteShellLinks a{{text-decoration:none!important;color:#334139!important;white-space:nowrap}}
.siteShellLinks a:hover{{color:#294533!important}}
.siteShellMobile{{display:none;position:relative}}
.siteShellMobile summary{{list-style:none;cursor:pointer;border:1px solid #ded8cd;background:#fff;padding:8px 12px;font-size:.73rem;font-weight:800;color:#294533}}
.siteShellMobile summary::-webkit-details-marker{{display:none}}
.siteShellMobileMenu{{position:absolute;right:0;top:44px;width:230px;background:#fff;border:1px solid #ded8cd;box-shadow:0 16px 36px rgba(30,44,35,.14);padding:8px}}
.siteShellMobileMenu a{{display:block;text-decoration:none!important;color:#334139!important;padding:10px 11px;font-size:.78rem;font-weight:700;border-bottom:1px solid #eee9df}}
.siteShellMobileMenu a:last-child{{border-bottom:0}}
.siteShellFooter{{background:#183024!important;color:rgba(255,255,255,.84)!important;padding:36px 0 30px!important;font-size:.76rem!important}}
.siteShellFooterGrid{{display:grid;grid-template-columns:240px 1fr;gap:48px;align-items:start}}
.siteShellFooterBrand{{font:1.45rem/.9 Georgia,"Times New Roman",serif;color:#fff}}
.siteShellFooterBrand small{{display:block;font-size:.72rem;color:rgba(255,255,255,.7)}}
.siteShellFooterTag{{margin-top:12px;color:rgba(255,255,255,.65);font-size:.71rem;line-height:1.5}}
.siteShellFooterLinks{{display:flex;justify-content:flex-end;gap:18px 22px;flex-wrap:wrap}}
.siteShellFooterLinks a{{text-decoration:none!important;color:rgba(255,255,255,.86)!important;font-size:.72rem}}
.siteShellCopyright{{grid-column:1/-1;border-top:1px solid rgba(255,255,255,.13);padding-top:18px;color:rgba(255,255,255,.55);font-size:.67rem}}
@media(max-width:900px){{.siteShellLinks{{gap:14px;font-size:.7rem}}}}
@media(max-width:760px){{.siteShellLinks{{display:none}}.siteShellMobile{{display:block}}.siteShellFooterGrid{{grid-template-columns:1fr;gap:22px}}.siteShellFooterLinks{{justify-content:flex-start}}.siteShellCopyright{{grid-column:1}}.siteShellWrap{{width:min(100% - 30px,1160px)}}}}
</style>
{CSS_MARKER_END}'''

HEADER = f'''{HEADER_MARKER_START}
<header class="siteShellHeader"><div class="siteShellWrap siteShellNav"><a class="siteShellBrand" href="/"><span class="siteShellBrandWords">Answers<small>for a Broken Heart</small></span><span class="siteShellHeart">♡</span></a><nav class="siteShellLinks" aria-label="Main navigation"><a href="/">Home</a><a href="/start-here">Start Here</a><a href="/all-answers">24 Answers</a><a href="/free-guides">Free Guides</a><a href="/book">The Book</a><a href="/about">About</a><a href="/contact">Contact</a></nav><details class="siteShellMobile"><summary>Menu</summary><nav class="siteShellMobileMenu" aria-label="Mobile navigation"><a href="/">Home</a><a href="/start-here">Start Here</a><a href="/all-answers">24 Answers</a><a href="/free-guides">Free Guides</a><a href="/book">The Book</a><a href="/about">About</a><a href="/contact">Contact</a></nav></details></div></header>
{HEADER_MARKER_END}'''

FOOTER = f'''{FOOTER_MARKER_START}
<footer class="siteShellFooter"><div class="siteShellWrap siteShellFooterGrid"><div><div class="siteShellFooterBrand">Answers<small>for a Broken Heart</small></div><div class="siteShellFooterTag">Biblical hope for grief, suffering, doubt, unanswered prayer, and the questions pain asks.</div></div><nav class="siteShellFooterLinks" aria-label="Footer navigation"><a href="/start-here">Start Here</a><a href="/all-answers">24 Answers</a><a href="/free-guides">Free Guides</a><a href="/church-resources">Church Resources</a><a href="/book">The Book</a><a href="/about">About</a><a href="/contact">Contact</a></nav><div class="siteShellCopyright">© 2026 Tate Throndson · Psalm 34:18 · Resources are pastoral and educational and are not a substitute for emergency, medical, or mental-health care.</div></div></footer>
{FOOTER_MARKER_END}'''

EXCLUDE = {
    'unsafe.html', '2am-guide-access.html', 'hope-thanks.html',
    'book-updates-thanks.html', 'contact-thanks.html'
}

def strip_marked(text, start, end):
    return re.sub(re.escape(start) + r'.*?' + re.escape(end), '', text, flags=re.S)

def replace_shell(path: Path, text: str) -> str:
    if path.name in EXCLUDE:
        return text
    text = strip_marked(text, CSS_MARKER_START, CSS_MARKER_END)
    text = strip_marked(text, HEADER_MARKER_START, HEADER_MARKER_END)
    text = strip_marked(text, FOOTER_MARKER_START, FOOTER_MARKER_END)
    # Replace the first page header and last page footer. The premium classes are unique
    # so page-specific legacy header/footer CSS no longer controls the visible shell.
    text = re.sub(r'<header\b.*?</header>', HEADER, text, count=1, flags=re.S | re.I)
    matches = list(re.finditer(r'<footer\b.*?</footer>', text, flags=re.S | re.I))
    if matches:
        m = matches[-1]
        text = text[:m.start()] + FOOTER + text[m.end():]
    if CSS_MARKER_START not in text:
        text = text.replace('</head>', SHELL_CSS + '\n</head>', 1)
    return text


def simplify_home(text: str) -> str:
    # The hero already carries the book identity. Remove the older mid-page sales band
    # and the redundant publication-readiness band; keep one gentle book bridge and one
    # launch-list invitation lower on the page.
    text = re.sub(
        r'(<!-- FREE-GUIDES-HOME-END -->)\s*<section class="bookBand">.*?</section>\s*(<section class="section"><div class="wrap authorSample">)',
        r'\1\2', text, count=1, flags=re.S
    )
    text = re.sub(r'<!-- BOOK-READY-START -->.*?<!-- BOOK-READY-END -->', '', text, flags=re.S)
    # Stop embedding the tiny portrait as a data URI. Use the shared real image asset.
    text = re.sub(r'const AUTHOR="data:image/jpeg;base64,[^"]+";', 'const AUTHOR="/author-tate.jpg?v=7";', text, count=1)
    # Make the distinction between the gated 2AM guide and open resources explicit.
    text = text.replace('<b>Get the free guide →</b></a><a class="guideCard" href="/can-christians-be-depressed">', '<b>Get the free guide →</b></a><a class="guideCard" href="/can-christians-be-depressed">')
    text = text.replace('Includes three practical steps for this week.</span><b>Get the free guide →</b>', 'Includes three practical steps for this week.</span><b>Read the free guide →</b>')
    return text


def polish_about(text: str) -> str:
    text = text.replace('https://answersforabrokenheart.com/author-tate.jpg', 'https://answersforabrokenheart.com/author-tate.jpg?v=7')
    text = text.replace('src="/author-tate.jpg?v=7"', 'src="/author-tate.jpg?v=7"')
    # The original photo is roughly portrait-oriented. Keeping it near native display size
    # produces a sharper, more premium result than blowing it into a large circular crop.
    text = re.sub(r'\.heroGrid\{display:grid;grid-template-columns:1fr 340px;', '.heroGrid{display:grid;grid-template-columns:1fr 230px;', text, count=1)
    text = re.sub(r'\.portrait\{width:310px;height:310px;border-radius:50%;object-fit:cover;object-position:center 23%;', '.portrait{width:220px;height:308px;border-radius:6px;object-fit:cover;object-position:center center;', text, count=1)
    text = text.replace('.portrait{justify-self:start;width:220px;height:220px}', '.portrait{justify-self:start;width:180px;height:252px}')
    return text


def polish_contact(text: str) -> str:
    # Move from a mailto composer to a direct web form submission. This still uses the
    # existing FormSubmit transport until the dedicated email-marketing platform is connected.
    text = text.replace('<form id="contactForm">', '<form id="contactForm" action="https://formsubmit.co/tatethrondson@gmail.com" method="POST"><input type="hidden" name="_subject" value="New Answers for a Broken Heart contact message"><input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="_next" value="https://answersforabrokenheart.com/contact-thanks"><input type="text" name="_honey" style="position:absolute;left:-5000px;width:1px;height:1px;overflow:hidden" tabindex="-1" autocomplete="off">')
    text = text.replace('<input id="subject" name="subject" required>', '<input id="subject" name="reader_subject" required>')
    text = text.replace('<button class="btn" type="submit">Compose Email</button>', '<button class="btn" type="submit">Send Message</button>')
    text = re.sub(r'<p class="note">For now, this opens your email app.*?</p>', '<p class="note">Your message will be sent directly. Please allow time for a personal response.</p>', text, flags=re.S)
    text = re.sub(r'<div id="status" class="success">.*?</div>', '', text, flags=re.S)
    text = re.sub(r'<script>\s*document\.getElementById\(\'contactForm\'\).*?</script>', '', text, flags=re.S)
    return text


def contact_thanks():
    return '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,follow"><title>Message Sent | Answers for a Broken Heart</title><style>body{margin:0;background:#f7f2e9;color:#24312b;font-family:Arial,Helvetica,sans-serif}.wrap{width:min(760px,calc(100% - 40px));margin:auto;padding:90px 0}h1{font:3.2rem/1.03 Georgia,serif;color:#183024;margin:0 0 16px}p{line-height:1.7;color:#58635c}.btn{display:inline-block;margin-top:16px;background:#294533;color:white;text-decoration:none;padding:12px 17px;font-weight:800;font-size:.76rem;text-transform:uppercase;letter-spacing:.05em}</style></head><body><main><div class="wrap"><p style="text-transform:uppercase;letter-spacing:.14em;color:#9a743a;font-size:.7rem;font-weight:800">Message sent</p><h1>Thank you for reaching out.</h1><p>Your message has been sent to Tate. If you came here because you are carrying something difficult, you do not have to wait for a reply to find help on the site.</p><a class="btn" href="/start-here">Find a Place to Begin</a></div></main></body></html>'''

for path in Path('.').glob('*.html'):
    text = path.read_text(encoding='utf-8')
    original = text
    if path.name == 'index.html':
        text = simplify_home(text)
    if path.name == 'about.html':
        text = polish_about(text)
    if path.name == 'contact.html':
        text = polish_contact(text)
    text = replace_shell(path, text)
    if text != original:
        path.write_text(text, encoding='utf-8')
        print('Premium polished', path.name)

thanks = Path('contact-thanks.html')
if not thanks.exists():
    thanks.write_text(contact_thanks(), encoding='utf-8')
    print('Created contact-thanks.html')
