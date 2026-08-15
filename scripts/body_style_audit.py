from pathlib import Path
import re

LOCK = Path('site-homepage-lock.css').read_text(encoding='utf-8')
LOCK_CLASSES = set(re.findall(r'\.([A-Za-z_][\w-]*)', LOCK))

STRUCTURAL = {
    'wrap','grid','row','heroGrid','introGrid','storyGrid','ctaGrid','bookHeroGrid','bookIntroGrid',
    'bookAudienceGrid','bookInsideGrid','bookReleaseGrid','resourceGrid','resourcesGrid','journalGrid',
    'journalsGrid','choiceGrid','answerGrid','relatedGrid','questionGrid','cards','useGrid','kitGrid',
    'minuteGrid','launchGrid','newsGrid','footerGrid','homeNoteForm','bookBridgeInner','bookBridgeActions',
    'articleWrap','layout','heroCopy','bookHeroCopy','bookIntroCopy','bookVisual','bookStage','bookPhoto',
    'authorInner','sampleInner','footer','nav','links','navlinks','actions','buttons','bottom','filters',
    'signup','form','field','formRow','reason','step','entry','pair','pairs','features','feature','page',
    'article','story','main','section','inside','resources','journals','library','tools','related','relatedAnswers',
    'truthGrid','tonightGrid','quickGrid','searchIntent','allHelp','breadcrumb','meta','byline','answerByline',
}

VISUAL_PROP = re.compile(
    r'(^|;)\s*(background(?:-image|-color)?|color|border(?:-[\w-]+)?|border-radius|box-shadow|font(?:-family|-size|-weight|-style)?|outline)\s*:',
    re.I,
)
STYLE_BLOCK = re.compile(r'<style\b[^>]*>(.*?)</style>', re.I | re.S)
SCRIPT_BLOCK = re.compile(r'<script\b[^>]*>.*?</script>', re.I | re.S)
RULE = re.compile(r'([^{}]+)\{([^{}]*)\}', re.S)
CLASS = re.compile(r'\.([A-Za-z_][\w-]*)')
CLASS_ATTR = re.compile(r'class=["\']([^"\']+)["\']', re.I)
HEX = re.compile(r'#[0-9a-fA-F]{3,8}\b')
RADIUS = re.compile(r'border-radius\s*:\s*([^;]+)', re.I)
SHADOW = re.compile(r'box-shadow\s*:\s*([^;]+)', re.I)
FONT = re.compile(r'font-family\s*:\s*([^;]+)', re.I)

ALLOWED_HEX = {x.lower() for x in {
    '#294533','#183024','#738371','#f5f0e7','#fbf8f2','#fffefb','#242a26','#656d67','#ad823d','#ded8cd',
    '#244833','#244432','#334139','#25382d','#2b5540','#264b39','#29332d','#2d3b33','#283b30','#343a36',
    '#3d4540','#3e4741','#3f4642','#252b27','#333333','#333','#393b39','#6a655e','#6b736f','#8b6939',
    '#88683b','#5f6862','#657068','#59645d','#5d665f','#525c56','#4b5850','#48564d','#eef2ed','#eaf0e8',
    '#f7f2e9','#f8f5ef','#faf8f3','#f1eadf','#f0ece4','#eee7da','#eee8de','#f5f1e9','#fff8fa','#f3dce4',
    '#5d464b','#fbf7f0','#c6a982','#d8bd87','#ebe5da','#e3ddd2','#cfc6b7','#dad4c8','#d7d0c5','#ece6dd',
    '#dde5dc','#d7dfd6','#d9d4ca','#17291f','#2c503a','#274a36','#2b503b','#f6f4ed','#cbc6bc','#ccc5b9',
    '#d9d4cb','#f8f5ee','#eee8df','#e6e0d7','#ddd7cd','#6a716d','#777f79','#4d5751','#555e58','#676f6a',
    '#d8d2c8','#2d332f','#5b655f','#f8f4ec','#fffaf2','#e8efe8','#e4ded3','#fff'
}}


def uniq(seq,limit=30):
    out=[]; seen=set()
    for x in seq:
        key=str(x)
        if key in seen: continue
        seen.add(key); out.append(x)
        if len(out)>=limit: break
    return out

rows=[]
page_details={}
for path in sorted(Path('.').glob('*.html')):
    if path.name == 'index.html': continue
    text=path.read_text(encoding='utf-8')

    # Only count selectors whose classes are actually present in the HTML markup.
    markup=STYLE_BLOCK.sub('', text)
    markup=SCRIPT_BLOCK.sub('', markup)
    dom_classes=set()
    for attr in CLASS_ATTR.findall(markup): dom_classes.update(attr.split())

    rules_seen=0; uncovered=[]; old_colors=set(); rounded=[]; shadows=[]; fonts=[]
    for block in STYLE_BLOCK.findall(text):
        for selectors,decl in RULE.findall(block):
            selectors=' '.join(selectors.split())
            if selectors.startswith('@') or not VISUAL_PROP.search(';'+decl): continue
            classes=set(CLASS.findall(selectors))
            if classes and not (classes & dom_classes):
                continue  # dead CSS; it cannot affect this page
            rules_seen += 1
            meaningful=(classes & dom_classes)-STRUCTURAL
            governed=meaningful & LOCK_CLASSES
            if meaningful and not governed:
                uncovered.append(selectors[:180])
                for h in HEX.findall(decl):
                    if h.lower() not in ALLOWED_HEX: old_colors.add(h.lower())
                for value in RADIUS.findall(decl):
                    v=value.strip().lower()
                    if v not in {'0','0px','2px','2px!important','50%','0!important'} and 'var(' not in v:
                        rounded.append((selectors[:100],value.strip()[:60]))
                for value in SHADOW.findall(decl):
                    v=value.strip().lower()
                    if v not in {'none','none!important'}:
                        shadows.append((selectors[:100],value.strip()[:80]))
                for value in FONT.findall(decl):
                    v=value.strip()
                    if not any(x in v.lower() for x in ['arial','helvetica','georgia','times new roman','serif','sans-serif']):
                        fonts.append((selectors[:100],v[:80]))

    uncovered=uniq(uncovered,30); rounded=uniq(rounded,15); shadows=uniq(shadows,15); fonts=uniq(fonts,10)
    score=len(uncovered)+2*len(old_colors)+len(rounded)+len(shadows)+2*len(fonts)
    rows.append((score,path.name,rules_seen,len(uncovered),sorted(old_colors),rounded,shadows,fonts))
    page_details[path.name]=uncovered

rows.sort(reverse=True)
report=[
    '# Body Visual Consistency Audit','',
    'This audit checks only page-specific visual CSS selectors that are **actually used by elements in the current page markup** and are not explicitly governed by the final homepage design lock. Dead/unused legacy CSS is ignored.','',
    f'- Interior pages inspected: **{len(rows)}**','',
    '| Page | Risk score | Used visual rules | Used uncovered selectors | Noncanonical colors | Unusual radii | Shadows | Fonts |',
    '|---|---:|---:|---:|---:|---:|---:|---:|'
]
for score,name,rules,nuncovered,colors,radii,shadows,fonts in rows:
    report.append(f'| `{name}` | {score} | {rules} | {nuncovered} | {len(colors)} | {len(radii)} | {len(shadows)} | {len(fonts)} |')

report += ['', '## Highest-risk pages and used selectors']
for score,name,rules,nuncovered,colors,radii,shadows,fonts in rows[:20]:
    if score==0: continue
    report += ['', f'### `{name}` — score {score}']
    if colors: report.append('- Noncanonical colors: '+', '.join(colors))
    if radii: report.append('- Unusual radii: '+'; '.join(f'`{s}` → `{v}`' for s,v in radii[:6]))
    if shadows: report.append('- Shadows: '+'; '.join(f'`{s}`' for s,_ in shadows[:6]))
    if fonts: report.append('- Fonts: '+'; '.join(f'`{s}` → `{v}`' for s,v in fonts[:4]))
    if page_details[name]:
        report.append('- Used visual selectors not governed by homepage lock:')
        for sel in page_details[name][:12]: report.append(f'  - `{sel}`')

zero=sum(1 for r in rows if r[0]==0)
report += ['', f'- Pages with no used visual escape selectors: **{zero}/{len(rows)}**']
Path('BODY-STYLE-AUDIT.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
print('Used-body visual audit complete. Highest risk:')
for row in rows[:18]: print(row[1],row[0], 'uncovered',row[3])
