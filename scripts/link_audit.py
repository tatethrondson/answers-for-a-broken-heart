from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

ROOT = Path('.')
REPORT = ROOT / 'LINK-AUDIT.md'
LIVE_BASE = 'https://answersforabrokenheart.com'
SITE_HOSTS = {'answersforabrokenheart.com','www.answersforabrokenheart.com'}
SKIP_SCHEMES = ('mailto:','tel:','sms:','javascript:','data:')

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=set()
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if a.get('id'): self.ids.add(a['id'])
        if a.get('name'): self.ids.add(a['name'])
        if tag == 'a' and a.get('href'): self.links.append(('anchor',a['href']))
        elif tag == 'link' and a.get('href'): self.links.append(('resource',a['href']))
        elif tag == 'form' and a.get('action'): self.links.append(('form',a['action']))

def parse_page(path):
    p=PageParser(); p.feed(path.read_text(encoding='utf-8',errors='ignore')); return p

def check_http(url):
    status=None; note=''; final=url
    try:
        req=Request(url,method='HEAD',headers={'User-Agent':'Mozilla/5.0 LinkAudit/2.0'})
        with urlopen(req,timeout=12) as r:
            status=getattr(r,'status',200); final=r.geturl()
    except HTTPError as e:
        status=e.code; note=str(e)
        if status in (403,405,429):
            try:
                req=Request(url,headers={'User-Agent':'Mozilla/5.0 LinkAudit/2.0','Range':'bytes=0-0'})
                with urlopen(req,timeout=12) as r:
                    status=getattr(r,'status',200); final=r.geturl(); note=''
            except Exception as e2:
                note=f'blocked/limited: {type(e2).__name__}'
    except Exception as e:
        note=f'{type(e).__name__}: {e}'
    return status,final,note

pages={p.name:p for p in ROOT.glob('*.html')}
parsed={name:parse_page(path) for name,path in pages.items()}

def resolve_internal(raw,source):
    u=urlparse(raw); path=unquote(u.path or ''); frag=unquote(u.fragment or '')
    if not path: target=source
    elif path=='/': target='index.html'
    else:
        clean=path.lstrip('/')
        if clean.endswith('/'): clean+='index.html'
        target=clean if Path(clean).suffix else clean+'.html'
    return target,frag

internal_broken=[]; fragment_broken=[]; resource_broken=[]
external_sources={}; live_internal_sources={}; checked_occurrences=0

for source,parser in parsed.items():
    for kind,raw in parser.links:
        raw=raw.strip()
        if not raw or raw.startswith(SKIP_SCHEMES): continue
        checked_occurrences+=1; u=urlparse(raw)
        if u.scheme in ('http','https') and (u.hostname or '').lower() not in SITE_HOSTS:
            external_sources.setdefault(raw,[]).append((source,kind)); continue
        if u.scheme in ('http','https') and (u.hostname or '').lower() in SITE_HOSTS:
            raw=(u.path or '/') + (('?'+u.query) if u.query else '') + (('#'+u.fragment) if u.fragment else '')
        target,frag=resolve_internal(raw,source)
        if target.endswith('.html'):
            if target not in pages:
                internal_broken.append((source,kind,raw,target)); continue
            if frag and frag not in parsed[target].ids:
                fragment_broken.append((source,raw,target,frag))
        else:
            if not (ROOT/target).exists(): resource_broken.append((source,kind,raw,target))
        if kind!='form':
            pu=urlparse(raw)
            if pu.path:
                live_path=pu.path
            elif target=='index.html':
                live_path='/'
            elif target.endswith('.html'):
                live_path='/' + target[:-5]
            else:
                live_path='/' + target
            live_url=LIVE_BASE + live_path + (('?'+pu.query) if pu.query else '')
            live_internal_sources.setdefault(live_url,[]).append((source,kind,raw))

external_results=[]
for url,refs in sorted(external_sources.items()):
    status,final,note=check_http(url); external_results.append((url,status,final,note,refs))
external_broken=[r for r in external_results if r[1] is None or (r[1]>=400 and r[1] not in (401,403,405,429))]
external_warnings=[r for r in external_results if r[1] in (401,403,405,429)]

live_results=[]
for url,refs in sorted(live_internal_sources.items()):
    status,final,note=check_http(url); live_results.append((url,status,final,note,refs))
live_broken=[r for r in live_results if r[1] is None or r[1]>=400]

lines=['# Full Site Link Audit','',f'HTML pages scanned: {len(pages)}',f'Link/resource/form occurrences checked: {checked_occurrences}',f'Unique live internal destinations checked: {len(live_results)}',f'Unique external URLs checked: {len(external_results)}','',f'Broken internal page links in repository: {len(internal_broken)}',f'Broken page fragments: {len(fragment_broken)}',f'Missing linked resources in repository: {len(resource_broken)}',f'Broken live production destinations: {len(live_broken)}',f'Broken/unreachable external URLs: {len(external_broken)}',f'Externally blocked/rate-limited checks: {len(external_warnings)}','']

def section(title,rows,formatter):
    lines.extend([f'## {title}',''])
    if not rows: lines.extend(['None.',''])
    else:
        for r in rows: lines.append('- '+formatter(r))
        lines.append('')

section('Broken internal page links in repository',internal_broken,lambda r:f'`{r[0]}` → `{r[2]}` (expected `{r[3]}`)')
section('Broken fragments / anchors',fragment_broken,lambda r:f'`{r[0]}` → `{r[1]}` (missing `#{r[3]}` in `{r[2]}`)')
section('Missing linked resources in repository',resource_broken,lambda r:f'`{r[0]}` → `{r[2]}` (missing `{r[3]}`)')
section('Broken live production destinations',live_broken,lambda r:f'`{r[0]}` — status `{r[1]}` {r[3]} — referenced by '+', '.join(sorted({x[0] for x in r[4]})))
section('Broken or unreachable external links',external_broken,lambda r:f'`{r[0]}` — status `{r[1]}` {r[3]} — used on '+', '.join(sorted({x[0] for x in r[4]})))
section('External checks blocked or rate-limited',external_warnings,lambda r:f'`{r[0]}` — status `{r[1]}` {r[3]} — used on '+', '.join(sorted({x[0] for x in r[4]})))
REPORT.write_text('\n'.join(lines),encoding='utf-8')
print('\n'.join(lines[:13]))
if internal_broken or fragment_broken or resource_broken or live_broken:
    raise SystemExit(2)
