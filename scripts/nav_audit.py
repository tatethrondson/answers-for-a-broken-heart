from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen
import re

BASE='https://answersforabrokenheart.com/'
EXPECTED=[('Start Here','/start-here'),('24 Answers','/all-answers'),('Free Resources','/free-guides'),('The Book','/book'),('About','/about')]


def norm(href):
    if not href: return ''
    if href.startswith('http'):
        p=urlparse(href).path
    else: p=href.split('#')[0].split('?')[0]
    p=re.sub(r'\.html$','',p)
    return p.rstrip('/') or '/'

class Parser(HTMLParser):
    def __init__(self):
        super().__init__(); self.headers=0; self.in_shell=False; self.in_desktop=False; self.in_mobile=False; self.link=None; self.text=[]; self.desktop=[]; self.mobile=[]; self.before_main=True; self.site_nav_before_main=0; self.nav_depth=[]; self.current_nav=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs); classes=set(d.get('class','').split())
        if tag=='main': self.before_main=False
        if tag=='header':
            self.headers+=1
            if 'siteShellHeader' in classes: self.in_shell=True
        if tag=='nav':
            self.nav_depth.append((self.before_main,[]))
            if self.in_shell and 'siteShellLinks' in classes: self.in_desktop=True
            if self.in_shell and 'siteShellMobileMenu' in classes: self.in_mobile=True
        if tag=='a': self.link=d.get('href'); self.text=[]
    def handle_data(self,data):
        if self.link is not None: self.text.append(data)
    def handle_endtag(self,tag):
        if tag=='a' and self.link is not None:
            item=(' '.join(''.join(self.text).split()),norm(self.link))
            if self.in_desktop: self.desktop.append(item)
            if self.in_mobile: self.mobile.append(item)
            if self.nav_depth: self.nav_depth[-1][1].append(item)
            self.link=None; self.text=[]
        elif tag=='nav' and self.nav_depth:
            before,items=self.nav_depth.pop()
            site_names={'Home','Start Here','24 Answers','Free Guides','Free Resources','The Book','About','Contact'}
            if before and any(label in site_names for label,_ in items) and items not in (EXPECTED,): self.site_nav_before_main+=1
            self.in_desktop=False; self.in_mobile=False
        elif tag=='header': self.in_shell=False


def inspect(text):
    p=Parser(); p.feed(text)
    issues=[]
    if p.headers!=1: issues.append(f'header count={p.headers}')
    if p.desktop!=EXPECTED: issues.append('desktop nav mismatch')
    if p.mobile!=EXPECTED: issues.append('mobile nav mismatch')
    if p.site_nav_before_main: issues.append(f'extra legacy site navs before main={p.site_nav_before_main}')
    return issues,p.desktop,p.mobile

pages=sorted(Path('.').glob('*.html'))
repo=[]
for path in pages:
    text=path.read_text(encoding='utf-8')
    issues,d,m=inspect(text)
    repo.append((path.name,issues,d,m))

# Live audit is diagnostic rather than build-blocking because production can briefly lag a source commit.
live=[]
for path in pages:
    route='/' if path.name=='index.html' else '/'+path.stem
    url=urljoin(BASE,route)
    try:
        req=Request(url,headers={'User-Agent':'Mozilla/5.0 AnswersForABrokenHeartNavAudit/2.0'})
        with urlopen(req,timeout=12) as r: text=r.read().decode('utf-8','replace')
        issues,d,m=inspect(text)
        live.append((route,issues,d,m,''))
    except Exception as e:
        live.append((route,['fetch failed'],[],[],str(e)))

repo_bad=[x for x in repo if x[1]]
live_bad=[x for x in live if x[1]]
lines=['# Navigation Consistency Audit','',
       'Canonical top navigation: **Start Here | 24 Answers | Free Resources | The Book | About**. The logo is Home; Contact and Church Resources remain in the footer.','',
       f'- Repository pages checked: **{len(repo)}**',f'- Repository pages with mismatches: **{len(repo_bad)}**',
       f'- Live routes checked: **{len(live)}**',f'- Live routes with mismatches/fetch failures: **{len(live_bad)}**','']
if repo_bad:
    lines+=['## Repository failures']
    for name,issues,_,_ in repo_bad: lines.append(f'- `{name}`: '+', '.join(issues))
else: lines+=['**Repository result: every root page has one header and the exact same five desktop/mobile options.**']
if live_bad:
    lines+=['','## Live differences (diagnostic)']
    for route,issues,_,_,err in live_bad: lines.append(f'- `{route}`: '+', '.join(issues)+(f' — {err}' if err else ''))
else: lines+=['','**Live result: every checked route currently exposes the same five-option header.**']
Path('NAV-AUDIT.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(f'Repository mismatches: {len(repo_bad)}; live differences: {len(live_bad)}')
raise SystemExit(1 if repo_bad else 0)
