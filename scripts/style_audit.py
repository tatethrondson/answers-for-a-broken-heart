from pathlib import Path
import re
import sys

EXPECTED_STYLES = [
    '/site-interior-v3.css',
    '/site-polish-v4.css',
    '/site-homepage-lock.css',
]
LEGACY_LINK_RE = re.compile(
    r'href=["\']/((?:site-cohesive|site-theme|site-unified|site-finish|site-phase[1-5])\.css)(?:\?[^"\']*)?["\']',
    re.I,
)
STYLE_LINK_RE = re.compile(r'<link\b[^>]*rel=["\']stylesheet["\'][^>]*href=["\']([^"\']+)["\'][^>]*>', re.I)
BODY_RE = re.compile(r'<body\b([^>]*)>', re.I)
CLASS_RE = re.compile(r'class=["\']([^"\']*)["\']', re.I)

TOPIC_HUBS = {
    'grief-and-loss.html',
    'why-god-allows-suffering.html',
    'god-feels-far-away.html',
    'anger-and-unanswered-prayer.html',
    'forgiveness-and-relational-hurt.html',
    'doubt-and-church-hurt.html',
}
DISCOVERY = {'start-here.html', 'begin-here.html', 'what-hurts-today.html', 'all-answers.html'}
CARE = {'2am-guide.html', '2am-guide-access.html', 'can-christians-be-depressed.html', 'help-someone.html', 'unsafe.html'}
CORE = {'book.html', 'about.html', 'free-guides.html', 'church-resources.html', 'contact.html'}
UTILITY = {'contact-thanks.html', 'hope-thanks.html', 'book-updates-thanks.html', '404.html'}

def family(name):
    if re.fullmatch(r'answer-\d\d\.html', name):
        return 'Answer article'
    if name in TOPIC_HUBS:
        return 'Topic hub'
    if name in DISCOVERY:
        return 'Discovery'
    if name in CARE:
        return 'Care / guide'
    if name in CORE:
        return 'Core page'
    if name in UTILITY:
        return 'Utility'
    return 'Other'

rows = []
errors = []
pages = sorted(p for p in Path('.').glob('*.html') if p.name != 'index.html')

for path in pages:
    text = path.read_text(encoding='utf-8')
    issues = []

    links = STYLE_LINK_RE.findall(text)
    normalized = [re.sub(r'\?.*$', '', h) for h in links]
    expected_positions = []
    for css in EXPECTED_STYLES:
        count = normalized.count(css)
        if count != 1:
            issues.append(f'{css} count={count}')
        else:
            expected_positions.append(normalized.index(css))
    if len(expected_positions) == len(EXPECTED_STYLES) and expected_positions != sorted(expected_positions):
        issues.append('shared styles are out of order')
    if normalized and '/site-homepage-lock.css' in normalized:
        if normalized.index('/site-homepage-lock.css') != len(normalized) - 1:
            issues.append('homepage lock is not the final linked stylesheet')

    legacy = sorted(set(LEGACY_LINK_RE.findall(text)))
    if legacy:
        issues.append('legacy linked CSS: ' + ', '.join(legacy))

    if text.count('PREMIUM-SHELL-HEADER-START') != 1:
        issues.append('canonical header marker count != 1')
    if text.count('PREMIUM-SHELL-FOOTER-START') != 1:
        issues.append('canonical footer marker count != 1')

    headers = len(re.findall(r'<header\b', text, re.I))
    footers = len(re.findall(r'<footer\b', text, re.I))
    if headers != 1:
        issues.append(f'header count={headers}')
    if footers != 1:
        issues.append(f'footer count={footers}')

    body = BODY_RE.search(text)
    page_class = 'page-' + re.sub(r'[^a-z0-9-]+', '-', path.stem.lower()).strip('-')
    if not body:
        issues.append('missing body tag')
    else:
        cm = CLASS_RE.search(body.group(1))
        classes = cm.group(1).split() if cm else []
        if page_class not in classes:
            issues.append(f'missing body class {page_class}')

    inline_styles = len(re.findall(r'<style\b', text, re.I))
    status = 'PASS' if not issues else 'FAIL'
    rows.append((path.name, family(path.name), inline_styles, status, '; '.join(issues) if issues else ''))
    if issues:
        errors.append((path.name, issues))

report = [
    '# Homepage Design Consistency Audit',
    '',
    'The homepage is the visual source of truth. Every root interior HTML page must load the canonical interior base, polish layer, and final homepage design lock in that order; use one canonical header/footer; and avoid older linked shared design systems.',
    '',
    'Page-specific inline CSS is allowed because some pages have unique content layouts. The final homepage lock loads last and is authoritative for the visible brand language.',
    '',
    f'- Interior pages audited: **{len(pages)}**',
    f'- Pages passing structural design checks: **{len(pages) - len(errors)}**',
    f'- Pages with hard design-system issues: **{len(errors)}**',
    '',
    '| Page | Family | Inline style blocks | Status | Issue |',
    '|---|---|---:|---|---|',
]
for name, fam, inline_styles, status, issue in rows:
    safe_issue = issue.replace('|', '\\|')
    report.append(f'| `{name}` | {fam} | {inline_styles} | **{status}** | {safe_issue or "—"} |')

if errors:
    report += ['', '## Hard failures']
    for name, issues in errors:
        report.append(f'- `{name}`: ' + '; '.join(issues))
else:
    report += ['', '**Result: all interior pages are structurally locked to the homepage design system.**']

Path('STYLE-AUDIT.md').write_text('\n'.join(report) + '\n', encoding='utf-8')
print(f'Audited {len(pages)} interior pages; hard failures: {len(errors)}')
sys.exit(1 if errors else 0)
