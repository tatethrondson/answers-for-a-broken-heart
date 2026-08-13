from pathlib import Path
import re

for filename in ('index.html', 'free-guides.html'):
    path = Path(filename)
    if not path.exists():
        continue
    text = path.read_text(encoding='utf-8')
    original = text

    # Only the 2:00 A.M. Guide is email-gated. Keep the depression guide clearly open.
    text = re.sub(
        r'(<strong>Can Christians Be Depressed\?</strong>.*?<b>)Get the free guide →(</b>)',
        r'\1Read the free guide →\2',
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(
        r'(<h3>Can Christians Be Depressed\?</h3>.*?<span class="cardLink">)Get the free guide →(</span>)',
        r'\1Read the free guide →\2',
        text,
        count=1,
        flags=re.S,
    )

    if text != original:
        path.write_text(text, encoding='utf-8')
        print('Corrected open-guide CTA in', filename)

# Keep the help-first homepage and Book-page presentation aligned with the site polish pass.
redesign = Path('scripts/help_first_redesign.py')
if redesign.exists():
    exec(compile(redesign.read_text(encoding='utf-8'), str(redesign), 'exec'))

# Keep the primary navigation intentionally small for a hurting visitor. The logo is Home;
# Contact remains available in the footer.
def simplify_nav(html: str) -> str:
    def trim(match):
        inside = match.group(2)
        inside = inside.replace('<a href="/">Home</a>', '')
        inside = inside.replace('<a href="/contact">Contact</a>', '')
        return match.group(1) + inside + match.group(3)
    html = re.sub(r'(<nav class="siteShellLinks"[^>]*>)(.*?)(</nav>)', trim, html, flags=re.S)
    html = re.sub(r'(<nav class="siteShellMobileMenu"[^>]*>)(.*?)(</nav>)', trim, html, flags=re.S)
    return html

for path in Path('.').glob('*.html'):
    text = path.read_text(encoding='utf-8')
    updated = simplify_nav(text)
    if updated != text:
        path.write_text(updated, encoding='utf-8')
        print('Simplified navigation in', path.name)

# Bring the 24 Answers library into the same pine / cream / gold system as Start Here.
answers = Path('all-answers.html')
if answers.exists():
    text = answers.read_text(encoding='utf-8')
    start = '<!-- HELP-FIRST-ANSWERS-START -->'
    end = '<!-- HELP-FIRST-ANSWERS-END -->'
    text = re.sub(re.escape(start) + r'.*?' + re.escape(end), '', text, flags=re.S)
    css = '''<!-- HELP-FIRST-ANSWERS-START --><style>
body{background:#fffefb!important;color:#242a26!important}.hero{background:linear-gradient(120deg,#f7f2e9,#e8efe8)!important}.hero h1,.intro h2,.groupHead h2{color:#183024!important}.hero .lead,.intro p,.groupHead p,.card p{color:#656d67!important}.eyebrow,.num,.count{color:#8b6939!important}.intro{background:#fffefb!important}.anchor{background:#183024!important;color:#fff!important}.tools{background:#f8f5ef!important;border-top:1px solid #ebe5da!important;border-bottom:1px solid #ded8cd!important;padding:18px 0!important}.search,.filter,.card{border-color:#ded8cd!important;background:#fff!important}.filter.active{background:#294533!important;color:#fff!important;border-color:#294533!important}.library{background:#faf8f3!important}.card{border-radius:0!important;box-shadow:none!important}.card h3{color:#25382d!important}.read{color:#294533!important}.bookCta{background:#183024!important;color:#fff!important}.bookCta h2{color:#fff!important}.bookCta p{color:rgba(255,255,255,.8)!important}.bookCta .btn{background:#fff!important;color:#183024!important;border-radius:0!important}
</style><!-- HELP-FIRST-ANSWERS-END -->'''
    text = text.replace('</head>', css + '\n</head>', 1)
    answers.write_text(text, encoding='utf-8')
    print('Unified all-answers.html')

# Make Start Here the guided front door, while /all-answers remains the full library.
start_here = Path('start-here.html')
if start_here.exists():
    text = start_here.read_text(encoding='utf-8')
    text = text.replace('<title>What Hurts Today? | Find a Biblical Place to Begin</title>', '<title>Start Here | Find Biblical Help for What Hurts</title>')
    text = text.replace('<link rel="canonical" href="https://answersforabrokenheart.com/what-hurts-today">', '<link rel="canonical" href="https://answersforabrokenheart.com/start-here">')
    text = text.replace('content="What Hurts Today? | Find a Biblical Place to Begin"', 'content="Start Here | Find Biblical Help for What Hurts"')
    text = text.replace('content="https://answersforabrokenheart.com/what-hurts-today"', 'content="https://answersforabrokenheart.com/start-here"')
    start_here.write_text(text, encoding='utf-8')
    print('Clarified start-here.html metadata')
