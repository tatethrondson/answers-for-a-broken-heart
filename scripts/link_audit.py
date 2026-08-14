from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import re

ROOT = Path('.')
REPORT = ROOT / 'LINK-AUDIT.md'
SITE_HOSTS = {'answersforabrokenheart.com','www.answersforabrokenheart.com'}
SKIP_SCHEMES = ('mailto:','tel:','sms:','javascript:','data:')

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]
        self.ids=set()
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if a.get('id'): self.ids.add(a['id'])
        if a.get('name'): self.ids.add(a['name'])
        if tag == 'a' and a.get('href'):
            self.links.append(('anchor', a['href']))
        elif tag == 'link' and a.get('href'):
            self.links.append(('resource', a['href']))
        elif tag == 'form' and a.get('action'):
            self.links.append(('form', a['action']))

def parse_page(path):
    p=PageParser()
    p.feed(path.read_text(encoding='utf-8', errors='ignore'))
    return p

pages={p.name:p for p in ROOT.glob('*.html')}
parsed={name:parse_page(path) for name,path in pages.items()}

def resolve_internal(raw, source):
    u=urlparse(raw)
    path=unquote(u.path or '')
    frag=unquote(u.fragment or '')
    if not path:
        target=source
    elif path == '/':
        target='index.html'
    else:
        clean=path.lstrip('/')
        if clean.endswith('/'):
            clean += 'index.html'
        if Path(clean).suffix:
            target=clean
        else:
            target=clean + '.html'
    return target, frag

internal_broken=[]
fragment_broken=[]
resource_broken=[]
external_sources={}
checked_occurrences=0

for source, parser in parsed.items():
    for kind, raw in parser.links:
        raw=raw.strip()
        if not raw or raw.startswith(SKIP_SCHEMES):
            continue
        checked_occurrences += 1
        u=urlparse(raw)
        if u.scheme in ('http','https') and (u.hostname or '').lower() not in SITE_HOSTS:
            external_sources.setdefault(raw, []).append((source,kind))
            continue
        if u.scheme in ('http','https') and (u.hostname or '').lower() in SITE_HOSTS:
            raw=(u.path or '/') + (('#'+u.fragment) if u.fragment else '')
        target,frag=resolve_internal(raw, source)
        # Clean-route HTML target
        if target.endswith('.html'):
            if target not in pages:
                internal_broken.append((source,kind,raw,target))
                continue
            if frag and frag not in parsed[target].ids:
                fragment_broken.append((source,raw,target,frag))
        else:
            # linked asset / stylesheet / download
            if not (ROOT/target).exists():
                resource_broken.append((source,kind,raw,target))

external_results=[]
for url, refs in sorted(external_sources.items()):
    status=None; note=''
    try:
        req=Request(url, method='HEAD', headers={'User-Agent':'Mozilla/5.0 LinkAudit/1.0'})
        with urlopen(req, timeout=12) as r:
            status=getattr(r,'status',200)
    except HTTPError as e:
        status=e.code
        if status in (403,405,429):
            try:
                req=Request(url, headers={'User-Agent':'Mozilla/5.0 LinkAudit/1.0','Range':'bytes=0-0'})
                with urlopen(req, timeout=12) as r:
                    status=getattr(r,'status',200)
            except Exception as e2:
                note=f'blocked/limited: {type(e2).__name__}'
        else:
            note=str(e)
    except (URLError, TimeoutError, Exception) as e:
        note=f'{type(e).__name__}: {e}'
    external_results.append((url,status,note,refs))

external_broken=[r for r in external_results if r[1] is None or (r[1] >= 400 and r[1] not in (401,403,405,429))]
external_warnings=[r for r in external_results if r[1] in (401,403,405,429)]

lines=['# Full Site Link Audit','',f'HTML pages scanned: {len(pages)}',f'Link/resource/form occurrences checked: {checked_occurrences}',f'Unique external URLs checked: {len(external_results)}','',
       f'Broken internal page links: {len(internal_broken)}',f'Broken page fragments: {len(fragment_broken)}',f'Missing linked resources: {len(resource_broken)}',f'Broken/unreachable external URLs: {len(external_broken)}',f'Externally blocked/rate-limited checks: {len(external_warnings)}','']

def section(title, rows, formatter):
    lines.extend([f'## {title}',''])
    if not rows:
        lines.extend(['None.',''])
    else:
        for r in rows: lines.append('- '+formatter(r))
        lines.append('')

section('Broken internal page links', internal_broken, lambda r:f'`{r[0]}` → `{r[2]}` (expected `{r[3]}`)')
section('Broken fragments / anchors', fragment_broken, lambda r:f'`{r[0]}` → `{r[1]}` (missing `#{r[3]}` in `{r[2]}`)')
section('Missing linked resources', resource_broken, lambda r:f'`{r[0]}` → `{r[2]}` (missing `{r[3]}`)')
section('Broken or unreachable external links', external_broken, lambda r:f'`{r[0]}` — status `{r[1]}` {r[2]} — used on '+', '.join(sorted({x[0] for x in r[3]})))
section('External checks blocked or rate-limited', external_warnings, lambda r:f'`{r[0]}` — status `{r[1]}` {r[2]} — used on '+', '.join(sorted({x[0] for x in r[3]})))
REPORT.write_text('\n'.join(lines),encoding='utf-8')
print('\n'.join(lines[:11]))
# Internal failures are authoritative and should fail CI. External failures are reported but do not fail CI because some sites block bots.
if internal_broken or fragment_broken or resource_broken:
    raise SystemExit(2)
