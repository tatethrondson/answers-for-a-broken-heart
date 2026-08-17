from pathlib import Path
import json
import re

ROOT=Path('.')
html_files=list(ROOT.glob('*.html'))
existing={'/'+p.stem for p in html_files}
existing.add('/')
aliases={
'/start-here','/what-hurts-today','/all-answers','/church-resources','/free-guides','/contact','/about','/book','/2am-guide','/help-someone','/unsafe','/can-christians-be-depressed','/grief-and-loss','/why-god-allows-suffering','/god-feels-far-away','/anger-and-unanswered-prayer','/forgiveness-and-relational-hurt','/doubt-and-church-hurt'
}
existing |= aliases
existing |= {f'/answer-{i:02d}' for i in range(1,25)}

# A clean URL can be backed by a different physical HTML filename in Vercel.
# Treat rewrite sources as real internal routes so QA validates the deployed
# routing model rather than assuming URL path == repository filename.
vercel=Path('vercel.json')
if vercel.exists():
    try:
        config=json.loads(vercel.read_text(encoding='utf-8'))
        existing |= {r.get('source') for r in config.get('rewrites',[]) if r.get('source')}
        existing |= {r.get('source') for r in config.get('redirects',[]) if r.get('source')}
    except Exception as exc:
        print(f'WARN: could not parse vercel.json for route-aware QA: {exc}')

issues=[]

def add(level,file,msg): issues.append((level,file,msg))
def hrefs(text): return re.findall(r'href=["\']([^"\']+)',text,re.I)
def internal_ok(h):
    if h.startswith(('#','mailto:','tel:','javascript:','http://','https://','sms:')): return True
    base=h.split('#')[0].split('?')[0]
    if base in ('','./','.'): return True
    if not base.startswith('/'): return True
    return base in existing or Path(base.lstrip('/')+'.html').exists() or Path(base.lstrip('/')).exists()

def has_stylesheet(text, filename):
    # Cache-busting versions are intentionally allowed to change.
    return bool(re.search(r'href=["\']/'+re.escape(filename)+r'(?:\?[^"\']*)?["\']', text, re.I))

if not Path('site-interior-v3.css').exists():
    add('ERROR','site-interior-v3.css','Unified homepage-derived interior design system is missing')
if not Path('site-polish-v4.css').exists():
    add('ERROR','site-polish-v4.css','Second-pass visual polish layer is missing')

for p in html_files:
    t=p.read_text(encoding='utf-8',errors='ignore')
    for h in hrefs(t):
        if not internal_ok(h): add('ERROR',p.name,f'Broken-looking internal href: {h}')
    if p.name not in {'index.html','photo-test.html'}:
        if not has_stylesheet(t,'site-interior-v3.css'):
            add('ERROR',p.name,'Missing unified homepage-derived interior design system')
        if not has_stylesheet(t,'site-polish-v4.css'):
            add('ERROR',p.name,'Missing second-pass visual polish layer')
        if 'PREMIUM-SHELL-HEADER-START' not in t or 'class="siteShellHeader"' not in t:
            add('ERROR',p.name,'Missing canonical homepage-derived header shell')
        if 'PREMIUM-SHELL-FOOTER-START' not in t or 'class="siteShellFooter"' not in t:
            add('ERROR',p.name,'Missing canonical homepage-derived footer shell')
    if 'formsubmit.co' in t:
        if 'name="_next"' not in t: add('WARN',p.name,'FormSubmit form missing _next redirect')
        if 'name="_honey"' not in t: add('WARN',p.name,'FormSubmit form missing honeypot')
        if 'name="_captcha"' not in t: add('WARN',p.name,'FormSubmit form missing explicit captcha setting')

for i in range(1,25):
    p=Path(f'answer-{i:02d}.html')
    if not p.exists():
        add('ERROR',p.name,'Answer page missing'); continue
    t=p.read_text(encoding='utf-8',errors='ignore')
    required={
      'canonical':'rel="canonical"',
      'author byline':'AUTHOR-BYLINE',
      '60-second help':'HURTING-HELP',
      'answer journey':'ANSWER-JOURNEY',
      'sharing tools':'class="shareHelp"',
      'conversion analytics':'CONVERSION-ANALYTICS',
      'mobile resilience':'MOBILE-RESILIENCE',
    }
    for label,needle in required.items():
        if needle not in t: add('ERROR',p.name,f'Missing {label}')
    if 'SAFETY-LINK' not in t and 'class="answerSafety"' not in t:
        add('ERROR',p.name,'Missing safety pathway')
    if '/all-answers' not in t: add('WARN',p.name,'No all-answers link')
    if 'href="/book"' not in t: add('WARN',p.name,'No canonical book path')
    if 'PODCAST-RESOURCE-START' in t: add('WARN',p.name,'Legacy standalone podcast block still present')
    if re.search(r'href="/?\?answer=\d{2}"',t): add('WARN',p.name,'Legacy query-style answer link still present')

for route,file in [('/start-here','begin-here.html'),('/all-answers','all-answers.html'),('/book','book.html'),('/church-resources','church-resources.html'),('/free-guides','free-guides.html')]:
    if not Path(file).exists(): add('ERROR',file,f'Backing file missing for {route}')

start=Path('begin-here.html')
if start.exists():
    t=start.read_text(encoding='utf-8',errors='ignore')
    if 'https://answersforabrokenheart.com/start-here' not in t: add('ERROR',start.name,'Start Here canonical missing or incorrect')
    if '/can-christians-be-depressed' not in t: add('WARN',start.name,'No direct depression pathway')

idx=Path('index.html')
if idx.exists():
    t=idx.read_text(encoding='utf-8',errors='ignore')
    for route in ['/start-here','/all-answers','/free-guides','/church-resources']:
        if route not in t: add('ERROR','index.html',f'Homepage missing key route {route}')
    if 'CONVERSION-ANALYTICS' not in t: add('WARN','index.html','Homepage missing conversion analytics marker')
    if 'View All 24 Answers' not in t: add('WARN','index.html','Homepage missing explicit 24 Answers library CTA')
else: add('ERROR','index.html','Homepage missing')

errors=sum(1 for x in issues if x[0]=='ERROR')
warns=sum(1 for x in issues if x[0]=='WARN')
lines=['# Site QA Report','',f'HTML files scanned: {len(html_files)}',f'Errors: {errors}',f'Warnings: {warns}','']
if issues:
    lines.append('## Findings')
    for level,file,msg in issues: lines.append(f'- **{level}** `{file}` — {msg}')
else:
    lines.append('No issues found by the automated checks.')
Path('SITE-QA.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(f'QA complete: {errors} errors, {warns} warnings')
for level,file,msg in issues:
    print(f'{level}: {file} — {msg}')
if errors: raise SystemExit(1)
