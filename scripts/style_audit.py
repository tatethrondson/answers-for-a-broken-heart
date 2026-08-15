from pathlib import Path
import re
import sys

CANONICAL = [
    ('Start Here', '/start-here'),
    ('24 Answers', '/all-answers'),
    ('Free Resources', '/free-guides'),
    ('The Book', '/book'),
    ('About', '/about'),
]
INTERIOR_STYLES = [
    '/site-interior-v3.css',
    '/site-polish-v4.css',
    '/site-homepage-lock.css',
]
SHELL_STYLE = '/site-shell.css'
SHELL_SCRIPT = '/site-shell.js'

LEGACY_LINK_RE = re.compile(
    r'href=["\']/((?:site-cohesive|site-theme|site-unified|site-finish|site-phase[1-5])\.css)(?:\?[^"\']*)?["\']',
    re.I,
)
STYLE_LINK_RE = re.compile(r'<link\b[^>]*rel=["\']stylesheet["\'][^>]*href=["\']([^"\']+)["\'][^>]*>', re.I)
SCRIPT_SRC_RE = re.compile(r'<script\b[^>]*src=["\']([^"\']+)["\'][^>]*></script>', re.I)
HEADER_RE = re.compile(r'<header\b[^>]*class=["\'][^"\']*siteShellHeader[^"\']*["\'][^>]*>(.*?)</header>', re.I | re.S)
DESKTOP_RE = re.compile(r'<nav\b[^>]*class=["\'][^"\']*siteShellLinks[^"\']*["\'][^>]*>(.*?)</nav>', re.I | re.S)
MOBILE_RE = re.compile(r'<nav\b[^>]*class=["\'][^"\']*siteShellMobileMenu[^"\']*["\'][^>]*>(.*?)</nav>', re.I | re.S)
A_RE = re.compile(r'<a\b[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', re.I | re.S)
TAG_RE = re.compile(r'<[^>]+>')

TOPIC_HUBS = {
    'grief-and-loss.html','why-god-allows-suffering.html','god-feels-far-away.html',
    'anger-and-unanswered-prayer.html','forgiveness-and-relational-hurt.html','doubt-and-church-hurt.html',
}
DISCOVERY = {'start-here.html','begin-here.html','what-hurts-today.html','all-answers.html'}
CARE = {'2am-guide.html','2am-guide-access.html','can-christians-be-depressed.html','help-someone.html','unsafe.html'}
CORE = {'index.html','book.html','about.html','free-guides.html','church-resources.html','contact.html'}
UTILITY = {'contact-thanks.html','hope-thanks.html','book-updates-thanks.html','404.html'}


def family(name):
    if name == 'index.html': return 'Homepage'
    if re.fullmatch(r'answer-\d\d\.html', name): return 'Answer article'
    if name in TOPIC_HUBS: return 'Topic hub'
    if name in DISCOVERY: return 'Discovery'
    if name in CARE: return 'Care / guide'
    if name in CORE: return 'Core page'
    if name in UTILITY: return 'Utility'
    return 'Other'


def clean_href(href):
    return re.sub(r'\?.*$', '', href).rstrip('/') or '/'


def nav_signature(fragment):
    result=[]
    for href, inner in A_RE.findall(fragment):
        label=' '.join(TAG_RE.sub('', inner).split())
        result.append((label, clean_href(href)))
    return result

pages=sorted(Path('.').glob('*.html'))
rows=[]
errors=[]

for path in pages:
    text=path.read_text(encoding='utf-8')
    issues=[]

    styles=[clean_href(x) for x in STYLE_LINK_RE.findall(text)]
    scripts=[clean_href(x) for x in SCRIPT_SRC_RE.findall(text)]

    if styles.count(SHELL_STYLE) != 1:
        issues.append(f'{SHELL_STYLE} count={styles.count(SHELL_STYLE)}')
    elif styles[-1] != SHELL_STYLE:
        issues.append('shared shell CSS is not the final linked stylesheet')
    if scripts.count(SHELL_SCRIPT) != 1:
        issues.append(f'{SHELL_SCRIPT} count={scripts.count(SHELL_SCRIPT)}')

    if path.name != 'index.html':
        positions=[]
        for css in INTERIOR_STYLES:
            count=styles.count(css)
            if count != 1:
                issues.append(f'{css} count={count}')
            else:
                positions.append(styles.index(css))
        if len(positions)==len(INTERIOR_STYLES) and positions != sorted(positions):
            issues.append('interior styles are out of order')
        if positions and SHELL_STYLE in styles and styles.index(SHELL_STYLE) < positions[-1]:
            issues.append('shared shell CSS loads before interior design layers')

    legacy=sorted(set(LEGACY_LINK_RE.findall(text)))
    if legacy:
        issues.append('legacy linked CSS: '+', '.join(legacy))
    if 'PREMIUM-SHELL-CSS-START' in text or 'PREMIUM-SHELL-CSS-END' in text:
        issues.append('legacy inline premium shell CSS remains')

    if text.count('PREMIUM-SHELL-HEADER-START') != 1:
        issues.append(f'canonical header marker count={text.count("PREMIUM-SHELL-HEADER-START")}')
    if text.count('PREMIUM-SHELL-FOOTER-START') != 1:
        issues.append(f'canonical footer marker count={text.count("PREMIUM-SHELL-FOOTER-START")}')
    header_count=len(re.findall(r'<header\b', text, re.I))
    footer_count=len(re.findall(r'<footer\b', text, re.I))
    if header_count != 1: issues.append(f'header count={header_count}')
    if footer_count != 1: issues.append(f'footer count={footer_count}')

    hm=HEADER_RE.search(text)
    if not hm:
        issues.append('canonical siteShellHeader missing')
        desktop=[]; mobile=[]
    else:
        dm=DESKTOP_RE.search(hm.group(1)); mm=MOBILE_RE.search(hm.group(1))
        desktop=nav_signature(dm.group(1)) if dm else []
        mobile=nav_signature(mm.group(1)) if mm else []
        if desktop != CANONICAL:
            issues.append('desktop top nav is not the exact five canonical links')
        if mobile != CANONICAL:
            issues.append('mobile top nav is not the exact five canonical links')

    # Strip the approved header and footer, then make sure no other site navigation survives anywhere.
    outside=text
    outside=re.sub(r'<header\b[^>]*class=["\'][^"\']*siteShellHeader[^"\']*["\'][^>]*>.*?</header>','',outside,flags=re.I|re.S)
    outside=re.sub(r'<footer\b[^>]*class=["\'][^"\']*siteShellFooter[^"\']*["\'][^>]*>.*?</footer>','',outside,flags=re.I|re.S)
    site_labels={'Home','Start Here','24 Answers','Free Guides','Free Resources','The Book','About','Contact'}
    extra_site_navs=0
    for frag in re.findall(r'<nav\b[^>]*>(.*?)</nav>', outside, re.I|re.S):
        sig=nav_signature(frag)
        if any(label in site_labels for label,_ in sig):
            extra_site_navs += 1
    if extra_site_navs:
        issues.append(f'extra/legacy site navigation outside shared shell={extra_site_navs}')

    status='PASS' if not issues else 'FAIL'
    rows.append((path.name,family(path.name),len(re.findall(r'<style\b',text,re.I)),status,'; '.join(issues)))
    if issues: errors.append((path.name,issues))

report=[
    '# Homepage Design & Header Audit','',
    'The homepage and every public root HTML page are tested against one shared site shell. The top navigation must contain exactly five options: **Start Here | 24 Answers | Free Resources | The Book | About**. Home is reached through the logo; Contact and Church Resources belong in the footer.','',
    f'- Pages audited: **{len(pages)}**',
    f'- Pages passing: **{len(pages)-len(errors)}**',
    f'- Pages failing: **{len(errors)}**','',
    '| Page | Family | Inline style blocks | Status | Issue |','|---|---|---:|---|---|'
]
for name,fam,n,status,issue in rows:
    report.append(f'| `{name}` | {fam} | {n} | **{status}** | {(issue or "—").replace("|","\\|")} |')
if errors:
    report += ['', '## Failures']
    for name,issues in errors: report.append(f'- `{name}`: '+'; '.join(issues))
else:
    report += ['', '**Result: all 50 root pages use the same canonical shared shell and exact five-option top navigation.**']
Path('STYLE-AUDIT.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
print(f'Audited {len(pages)} pages; failures: {len(errors)}')
for name,issues in errors:
    print('FAIL',name,':','; '.join(issues))
sys.exit(1 if errors else 0)
