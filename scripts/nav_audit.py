from pathlib import Path
from html.parser import HTMLParser
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib.parse import urljoin

ROOT = Path('.')
LIVE_BASE = 'https://answersforabrokenheart.com'
REPORT = ROOT / 'NAV-AUDIT.md'
CANONICAL = [
    ('Start Here', '/start-here'),
    ('24 Answers', '/all-answers'),
    ('Free Resources', '/free-guides'),
    ('The Book', '/book'),
    ('About', '/about'),
]

class NavParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_header = 0
        self.nav_stack = []
        self.navs = []
        self.current_link = None
        self.capture_text = False
        self.text_buf = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'header':
            self.in_header += 1
        if tag == 'nav' and self.in_header:
            cls = a.get('class','')
            aria = a.get('aria-label','')
            self.nav_stack.append({'class':cls,'aria':aria,'links':[]})
        if tag == 'a' and self.nav_stack:
            self.current_link = {'href':a.get('href',''),'text':''}
            self.capture_text = True
            self.text_buf = []

    def handle_data(self, data):
        if self.capture_text:
            self.text_buf.append(data)

    def handle_endtag(self, tag):
        if tag == 'a' and self.current_link is not None and self.nav_stack:
            self.current_link['text'] = ' '.join(''.join(self.text_buf).split())
            self.nav_stack[-1]['links'].append(self.current_link)
            self.current_link = None
            self.capture_text = False
            self.text_buf = []
        elif tag == 'nav' and self.nav_stack:
            self.navs.append(self.nav_stack.pop())
        elif tag == 'header' and self.in_header:
            self.in_header -= 1


def parse(html):
    p = NavParser(); p.feed(html); return p

def primary_nav(p):
    # Prefer the explicit desktop main navigation.
    for nav in p.navs:
        if nav['aria'].lower() == 'main navigation' and 'Mobile' not in nav['class']:
            return nav['links']
    for nav in p.navs:
        if 'siteShellLinks' in nav['class'] or 'navlinks' in nav['class']:
            return nav['links']
    return p.navs[0]['links'] if p.navs else []

def signature(links):
    return tuple((x['text'], x['href']) for x in links)

def route_for(path):
    if path.name == 'index.html': return '/'
    if path.name == 'photo-test.html': return None
    return '/' + path.stem

def fetch(url):
    req = Request(url, headers={'User-Agent':'Mozilla/5.0 NavAudit/1.0'})
    try:
        with urlopen(req, timeout=15) as r:
            return r.read().decode('utf-8','ignore'), getattr(r,'status',200), r.geturl()
    except HTTPError as e:
        return '', e.code, url
    except Exception as e:
        return '', None, f'{url} ({type(e).__name__}: {e})'

pages = [p for p in sorted(ROOT.glob('*.html')) if p.name != 'photo-test.html']
repo_groups = {}
repo_bad = []
for path in pages:
    html = path.read_text(encoding='utf-8', errors='ignore')
    links = primary_nav(parse(html))
    sig = signature(links)
    repo_groups.setdefault(sig, []).append(path.name)
    if sig != tuple(CANONICAL):
        repo_bad.append((path.name, sig))

live_groups = {}
live_bad = []
live_fail = []
for path in pages:
    route = route_for(path)
    if not route: continue
    html, status, final = fetch(LIVE_BASE + route)
    if status is None or status >= 400:
        live_fail.append((route,status,final)); continue
    sig = signature(primary_nav(parse(html)))
    live_groups.setdefault(sig, []).append(route)
    if sig != tuple(CANONICAL):
        live_bad.append((route,sig,final))

lines = ['# Navigation Consistency Audit','',
         'Canonical primary navigation: `Start Here | 24 Answers | Free Resources | The Book | About`','',
         f'Repository pages checked: {len(pages)}',
         f'Repository pages with noncanonical navigation: {len(repo_bad)}',
         f'Live pages checked: {len(pages)-len(live_fail)}',
         f'Live pages with noncanonical navigation: {len(live_bad)}',
         f'Live pages that failed to load: {len(live_fail)}','']

lines += ['## Repository navigation variants','']
for sig, names in sorted(repo_groups.items(), key=lambda x:(-len(x[1]), str(x[0]))):
    label = ' | '.join(t or '(blank)' for t,h in sig) if sig else '(no primary nav found)'
    lines.append(f'- **{len(names)} pages** — `{label}`')
    lines.append('  - ' + ', '.join(f'`{n}`' for n in names))
lines.append('')

lines += ['## Live navigation variants','']
for sig, routes in sorted(live_groups.items(), key=lambda x:(-len(x[1]), str(x[0]))):
    label = ' | '.join(t or '(blank)' for t,h in sig) if sig else '(no primary nav found)'
    lines.append(f'- **{len(routes)} pages** — `{label}`')
    lines.append('  - ' + ', '.join(f'`{r}`' for r in routes))
lines.append('')

lines += ['## Noncanonical repository pages','']
if repo_bad:
    for name,sig in repo_bad:
        lines.append(f'- `{name}` — ' + ' | '.join(f'{t} ({h})' for t,h in sig))
else: lines.append('None.')
lines.append('')

lines += ['## Noncanonical live pages','']
if live_bad:
    for route,sig,final in live_bad:
        lines.append(f'- `{route}` — ' + ' | '.join(f'{t} ({h})' for t,h in sig) + f' — final `{final}`')
else: lines.append('None.')
lines.append('')

lines += ['## Live fetch failures','']
if live_fail:
    for route,status,note in live_fail: lines.append(f'- `{route}` — status `{status}` — {note}')
else: lines.append('None.')
lines.append('')

REPORT.write_text('\n'.join(lines), encoding='utf-8')
print('\n'.join(lines[:9]))
