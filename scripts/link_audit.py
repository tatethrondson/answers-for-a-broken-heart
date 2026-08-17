from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote, urljoin
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import json

ROOT=Path('.')
REPORT=ROOT/'LINK-AUDIT.md'
LIVE_BASE='https://answersforabrokenheart.com'
SITE_HOSTS={'answersforabrokenheart.com','www.answersforabrokenheart.com'}
SKIP_SCHEMES=('mailto:','tel:','sms:','data:')
RUNTIME_PREFIXES=('_vercel/','api/')

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=set()
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get('id'): self.ids.add(a['id'])
        if a.get('name'): self.ids.add(a['name'])
        if tag=='a' and a.get('href') is not None: self.links.append(('anchor',a.get('href','')))
        elif tag=='link' and a.get('href'): self.links.append(('resource',a['href']))
        elif tag in ('script','img','iframe','source') and a.get('src'): self.links.append(('resource',a['src']))
        elif tag=='form' and a.get('action'): self.links.append(('form',a['action']))

def parse_text(text):
    p=PageParser(); p.feed(text); return p

def parse_page(path): return parse_text(path.read_text(encoding='utf-8',errors='ignore'))

def check_http(url,want_body=False):
    status=None; note=''; final=url; body=''
    try:
        req=Request(url,method='GET' if want_body else 'HEAD',headers={'User-Agent':'Mozilla/5.0 LinkAudit/5.0'})
        with urlopen(req,timeout=12) as r:
            status=getattr(r,'status',200); final=r.geturl()
            if want_body: body=r.read(2_000_000).decode('utf-8','ignore')
    except HTTPError as e:
        status=e.code; note=str(e)
        if not want_body and status in (403,405,429):
            try:
                req=Request(url,headers={'User-Agent':'Mozilla/5.0 LinkAudit/5.0','Range':'bytes=0-0'})
                with urlopen(req,timeout=12) as r:
                    status=getattr(r,'status',200); final=r.geturl(); note=''
            except Exception as e2: note=f'blocked/limited: {type(e2).__name__}'
    except Exception as e: note=f'{type(e).__name__}: {e}'
    return status,final,note,body

pages={p.name:p for p in ROOT.glob('*.html')}
parsed={name:parse_page(path) for name,path in pages.items()}
config=json.loads((ROOT/'vercel.json').read_text()) if (ROOT/'vercel.json').exists() else {}
redirects={r.get('source'):r.get('destination') for r in config.get('redirects',[]) if r.get('source') and r.get('destination')}
rewrites={r.get('source'):r.get('destination') for r in config.get('rewrites',[]) if r.get('source') and r.get('destination')}

def resolve_internal(raw,source):
    u=urlparse(raw); path=unquote(u.path or ''); frag=unquote(u.fragment or '')
    if not path:
        target=source
    elif path=='/':
        target='index.html'
    elif path in rewrites:
        target=unquote(urlparse(rewrites[path]).path).lstrip('/')
        if target and not Path(target).suffix:
            target += '.html'
    else:
        clean=path.lstrip('/')
        if clean.endswith('/'): clean+='index.html'
        target=clean if Path(clean).suffix else clean+'.html'
    return target,frag

internal_broken=[]; fragment_broken=[]; resource_broken=[]; placeholder_links=[]; redirect_alias_links=[]
external_sources={}; repo_live_sources={}; checked_occurrences=0

for source,parser in parsed.items():
    for kind,raw in parser.links:
        raw=(raw or '').strip(); checked_occurrences+=1
        if kind=='anchor' and (not raw or raw=='#' or raw.lower().startswith('javascript:')):
            placeholder_links.append((source,raw or '(empty href)')); continue
        if not raw or raw.startswith(SKIP_SCHEMES): continue
        u=urlparse(raw)
        if u.scheme in ('http','https') and (u.hostname or '').lower() not in SITE_HOSTS:
            external_sources.setdefault(raw,[]).append((source,kind)); continue
        if u.scheme in ('http','https') and (u.hostname or '').lower() in SITE_HOSTS:
            raw=(u.path or '/')+(('?'+u.query) if u.query else '')+(('#'+u.fragment) if u.fragment else '')
            u=urlparse(raw)
        if kind=='anchor' and u.path in redirects:
            redirect_alias_links.append((source,raw,redirects[u.path]))
        target,frag=resolve_internal(raw,source)
        if target.endswith('.html'):
            if target not in pages:
                internal_broken.append((source,kind,raw,target)); continue
            if frag and frag not in parsed[target].ids: fragment_broken.append((source,raw,target,frag))
        else:
            if not target.startswith(RUNTIME_PREFIXES) and not (ROOT/target).exists(): resource_broken.append((source,kind,raw,target))
        if kind!='form':
            pu=urlparse(raw)
            if pu.path: live_path=pu.path
            elif target=='index.html': live_path='/'
            elif target.endswith('.html'): live_path='/'+target[:-5]
            else: live_path='/'+target
            repo_live_sources.setdefault(LIVE_BASE+live_path+(('?'+pu.query) if pu.query else ''),[]).append((source,kind,raw))

external_results=[]
for url,refs in sorted(external_sources.items()):
    status,final,note,_=check_http(url); external_results.append((url,status,final,note,refs))
external_broken=[r for r in external_results if r[1] is None or (r[1]>=400 and r[1] not in (401,403,405,429))]
external_warnings=[r for r in external_results if r[1] in (401,403,405,429)]

repo_live_results=[]
for url,refs in sorted(repo_live_sources.items()):
    status,final,note,_=check_http(url); repo_live_results.append((url,status,final,note,refs))
repo_live_broken=[r for r in repo_live_results if r[1] is None or r[1]>=400]

live_page_failures=[]; live_markup_sources={}; live_pages_fetched=0
for filename in sorted(pages):
    route='/' if filename=='index.html' else '/'+filename[:-5]
    status,final,note,body=check_http(LIVE_BASE+route,want_body=True)
    if status is None or status>=400:
        live_page_failures.append((LIVE_BASE+route,status,note)); continue
    live_pages_fetched+=1
    for kind,raw in parse_text(body).links:
        raw=(raw or '').strip()
        if not raw or raw.startswith(SKIP_SCHEMES) or raw.lower().startswith('javascript:') or kind=='form': continue
        absolute=urljoin(final,raw); u=urlparse(absolute)
        if u.scheme in ('http','https') and (u.hostname or '').lower() in SITE_HOSTS:
            live_markup_sources.setdefault(u._replace(fragment='').geturl(),[]).append((route,kind,raw))

live_markup_results=[]
for url,refs in sorted(live_markup_sources.items()):
    status,final,note,_=check_http(url); live_markup_results.append((url,status,final,note,refs))
live_markup_broken=[r for r in live_markup_results if r[1] is None or r[1]>=400]

lines=['# Full Site Link Audit','',f'HTML pages scanned in repository: {len(pages)}',f'Clickable/resource/form occurrences checked: {checked_occurrences}',f'Unique repo-derived live destinations checked: {len(repo_live_results)}',f'Live HTML pages fetched: {live_pages_fetched}',f'Unique destinations found in live page markup: {len(live_markup_results)}',f'Unique external URLs checked: {len(external_results)}','',f'Broken internal page links: {len(internal_broken)}',f'Broken page fragments: {len(fragment_broken)}',f'Missing linked repository resources: {len(resource_broken)}',f'Placeholder/dead anchor links: {len(placeholder_links)}',f'Links still using redirect aliases: {len(redirect_alias_links)}',f'Broken production destinations: {len(repo_live_broken)}',f'Live pages that failed to load: {len(live_page_failures)}',f'Broken destinations found in live markup: {len(live_markup_broken)}',f'Broken/unreachable external URLs: {len(external_broken)}',f'Externally blocked/rate-limited checks: {len(external_warnings)}','']

def section(title,rows,formatter):
    lines.extend([f'## {title}',''])
    if not rows: lines.extend(['None.',''])
    else:
        for r in rows: lines.append('- '+formatter(r))
        lines.append('')
section('Broken internal page links',internal_broken,lambda r:f'`{r[0]}` → `{r[2]}` (expected `{r[3]}`)')
section('Broken fragments / anchors',fragment_broken,lambda r:f'`{r[0]}` → `{r[1]}` (missing `#{r[3]}` in `{r[2]}`)')
section('Missing linked repository resources',resource_broken,lambda r:f'`{r[0]}` → `{r[2]}` (missing `{r[3]}`)')
section('Placeholder / dead anchor links',placeholder_links,lambda r:f'`{r[0]}` → `{r[1]}`')
section('Links still using redirect aliases',redirect_alias_links,lambda r:f'`{r[0]}` → `{r[1]}`; should link directly to `{r[2]}`')
section('Broken production destinations',repo_live_broken,lambda r:f'`{r[0]}` — status `{r[1]}` {r[3]} — referenced by '+', '.join(sorted({x[0] for x in r[4]})))
section('Live pages that failed to load',live_page_failures,lambda r:f'`{r[0]}` — status `{r[1]}` {r[2]}')
section('Broken destinations found in live page markup',live_markup_broken,lambda r:f'`{r[0]}` — status `{r[1]}` {r[3]} — found on '+', '.join(sorted({x[0] for x in r[4]})))
section('Broken or unreachable external links',external_broken,lambda r:f'`{r[0]}` — status `{r[1]}` {r[3]} — used on '+', '.join(sorted({x[0] for x in r[4]})))
section('External checks blocked or rate-limited',external_warnings,lambda r:f'`{r[0]}` — status `{r[1]}` {r[3]} — used on '+', '.join(sorted({x[0] for x in r[4]})))
REPORT.write_text('\n'.join(lines),encoding='utf-8')
print('\n'.join(lines[:19]))
if internal_broken or fragment_broken or resource_broken or placeholder_links or repo_live_broken or live_page_failures or live_markup_broken:
    raise SystemExit(2)
