from pathlib import Path
import re
from collections import defaultdict

LOCK = Path('site-homepage-lock.css').read_text(encoding='utf-8')

# Classes explicitly governed by the final homepage design lock.
LOCK_CLASSES = set(re.findall(r'\.([A-Za-z_][\w-]*)', LOCK))

# These are layout/behavior classes whose unique geometry is allowed to vary by page.
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

# Visual properties that can make a page look like a different design system.
VISUAL_PROP = re.compile(
    r'(^|;)\s*(background(?:-image|-color)?|color|border(?:-[\w-]+)?|border-radius|box-shadow|font(?:-family|-size|-weight|-style)?|outline)\s*:',
    re.I,
)

STYLE_BLOCK = re.compile(r'<style\b[^>]*>(.*?)</style>', re.I | re.S)
RULE = re.compile(r'([^{}]+)\{([^{}]*)\}', re.S)
CLASS = re.compile(r'\.([A-Za-z_][\w-]*)')
HEX = re.compile(r'#[0-9a-fA-F]{3,8}\b')
RADIUS = re.compile(r'border-radius\s*:\s*([^;]+)', re.I)
SHADOW = re.compile(r'box-shadow\s*:\s*([^;]+)', re.I)
FONT = re.compile(r'font-family\s*:\s*([^;]+)', re.I)

# Canonical palette plus intentional neutral/support colors already present on homepage.
ALLOWED_HEX = {
    '#294533','#183024','#738371','#f5f0e7','#fbf8f2','#fffefb','#242a26','#656d67','#ad823d','#ded8cd',
    '#244833','#244432','#334139','#25382d','#2b5540','#264b39','#29332d','#2d3b33','#283b30','#343a36',
    '#3d4540','#3e4741','#3f4642','#252b27','#333333','#333','#393b39','#6a655e','#6b736f','#8b6939',
    '#88683b','#5f6862','#657068','#59645d','#5d665f','#525c56','#4b5850','#48564d','#eef2ed','#eaf0e8',
    '#f7f2e9','#f8f5ef','#faf8f3','#f1eadf','#f0ece4','#eee7da','#eee8de','#f5f1e9','#fff8fa','#f3dce4',
    '#5d464b','#fbf7f0','#c6a982','#d8bd87','#ebe5da','#e3ddd2','#cfc6b7','#dad4c8','#d7d0c5','#ece6dd',
    '#dde5dc','#d7dfd6','#d9d4ca','#17291f','#2c503a','#274a36','#2b503b','#f6f4ed','#cbc6bc','#ccc5b9',
    '#d9d4cb','#f8f5ee','#eee8df','#e6e0d7','#ddd7cd','#6a716d','#777f79','#4d5751','#555e58','#676f6a',
    '#d8d2c8','#2d332f','#5b655f','#f8f4ec','#fffaf2','#e8efe8','#e4ded3'
}

pages = sorted(Path('.').glob('*.html'))
rows=[]
page_findings=defaultdict(list)

for path in pages:
    if path.name == 'index.html':
        # Homepage is the source of truth; audit other pages against it.
        continue
    text=path.read_text(encoding='utf-8')
    rules_seen=0
    uncovered=[]
    old_colors=set()
    rounded=[]
    shadows=[]
    fonts=[]

    for block in STYLE_BLOCK.findall(text):
        # Ignore generated shared-content blocks whose selectors are already covered by the final lock.
        for selectors, decl in RULE.findall(block):
            selectors=' '.join(selectors.split())
            if selectors.startswith('@') or not VISUAL_PROP.search(';'+decl):
                continue
            rules_seen += 1
            classes=set(CLASS.findall(selectors))
            meaningful=classes-STRUCTURAL
            if meaningful and not (meaningful & LOCK_CLASSES):
                uncovered.append(selectors[:150])

            for h in HEX.findall(decl):
                if h.lower() not in {x.lower() for x in ALLOWED_HEX}:
                    old_colors.add(h.lower())
            for value in RADIUS.findall(decl):
                v=value.strip()
                if v not in {'0','0px','2px','50%'} and 'var(' not in v:
                    rounded.append((selectors[:90],v[:60]))
            for value in SHADOW.findall(decl):
                v=value.strip().lower()
                if v not in {'none','none!important'}:
                    shadows.append((selectors[:90],v[:80]))
            for value in FONT.findall(decl):
                v=value.strip()
                if not any(x in v.lower() for x in ['arial','helvetica','georgia','times new roman','serif','sans-serif']):
                    fonts.append((selectors[:90],v[:80]))

    # Deduplicate while preserving useful examples.
    def uniq(seq,limit=18):
        out=[]; seen=set()
        for x in seq:
            key=str(x)
            if key in seen: continue
            seen.add(key); out.append(x)
            if len(out)>=limit: break
        return out

    uncovered=uniq(uncovered,25)
    rounded=uniq(rounded,12)
    shadows=uniq(shadows,12)
    fonts=uniq(fonts,8)
    score=len(uncovered)+2*len(old_colors)+len(rounded)+len(shadows)+2*len(fonts)
    rows.append((score,path.name,rules_seen,len(uncovered),sorted(old_colors),rounded,shadows,fonts))

rows.sort(reverse=True)

report=[
    '# Body Visual Consistency Audit','',
    'This audit looks beyond the shared header and asks which interior pages still contain page-specific visual rules that are not explicitly governed by the final homepage design lock. It flags uncovered appearance selectors, non-canonical colors, unusual corner radii, shadows, and non-brand fonts.','',
    f'- Interior pages inspected: **{len(rows)}**','',
    '| Page | Risk score | Visual rules | Uncovered selectors | Noncanonical colors | Unusual radii | Shadows | Fonts |',
    '|---|---:|---:|---:|---:|---:|---:|---:|'
]
for score,name,rules,nuncovered,colors,radii,shadows,fonts in rows:
    report.append(f'| `{name}` | {score} | {rules} | {nuncovered} | {len(colors)} | {len(radii)} | {len(shadows)} | {len(fonts)} |')

report += ['', '## Highest-risk pages and examples']
for score,name,rules,nuncovered,colors,radii,shadows,fonts in rows[:18]:
    if score == 0: continue
    report += ['', f'### `{name}` — score {score}']
    if colors: report.append('- Noncanonical colors: '+', '.join(colors))
    if radii: report.append('- Unusual radii: '+'; '.join(f'`{s}` → `{v}`' for s,v in radii[:6]))
    if shadows: report.append('- Shadows: '+'; '.join(f'`{s}`' for s,_ in shadows[:6]))
    if fonts: report.append('- Fonts: '+'; '.join(f'`{s}` → `{v}`' for s,v in fonts[:4]))
    if nuncovered:
        report.append('- Uncovered visual selectors:')
        for sel in rows[[r[1] for r in rows].index(name)][3] and []: pass
        # Regenerate selectors for this page for readable examples.
        t=Path(name).read_text(encoding='utf-8'); examples=[]
        for block in STYLE_BLOCK.findall(t):
            for selectors,decl in RULE.findall(block):
                selectors=' '.join(selectors.split())
                if selectors.startswith('@') or not VISUAL_PROP.search(';'+decl): continue
                classes=set(CLASS.findall(selectors)); meaningful=classes-STRUCTURAL
                if meaningful and not (meaningful & LOCK_CLASSES) and selectors not in examples:
                    examples.append(selectors)
                if len(examples)>=10: break
            if len(examples)>=10: break
        for sel in examples: report.append(f'  - `{sel}`')

Path('BODY-STYLE-AUDIT.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
print('Body visual audit complete. Highest risk:')
for row in rows[:15]: print(row[1], row[0])
