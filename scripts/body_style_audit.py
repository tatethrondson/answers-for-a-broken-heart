from pathlib import Path
import re
LOCK='\n'.join(Path(p).read_text(encoding='utf-8') for p in ['site-homepage-lock.css','site-body-lock-v2.css','site-body-lock-v3.css','site-body-lock-v4.css','site-body-lock-v5.css']); LOCK_CLASSES=set(re.findall(r'\.([A-Za-z_][\w-]*)',LOCK))
STRUCTURAL={'wrap','grid','row','heroGrid','introGrid','storyGrid','ctaGrid','bookHeroGrid','bookIntroGrid','bookAudienceGrid','bookInsideGrid','bookReleaseGrid','resourceGrid','resourcesGrid','journalGrid','journalsGrid','choiceGrid','answerGrid','relatedGrid','questionGrid','cards','useGrid','kitGrid','minuteGrid','launchGrid','newsGrid','footerGrid','homeNoteForm','bookBridgeInner','bookBridgeActions','articleWrap','layout','heroCopy','bookHeroCopy','bookIntroCopy','bookVisual','bookStage','bookPhoto','authorInner','sampleInner','footer','nav','links','navlinks','actions','buttons','bottom','filters','signup','form','field','formRow','reason','step','entry','pair','pairs','features','feature','page','article','story','main','section','inside','resources','journals','library','tools','related','relatedAnswers','truthGrid','tonightGrid','quickGrid','searchIntent','allHelp','breadcrumb','meta','byline','answerByline'}
VISUAL_PROP=re.compile(r'(^|;)\s*(background(?:-image|-color)?|color|border(?:-[\w-]+)?|border-radius|box-shadow|font(?:-family|-size|-weight|-style)?|outline)\s*:',re.I); STYLE_BLOCK=re.compile(r'<style\b[^>]*>(.*?)</style>',re.I|re.S); SCRIPT_BLOCK=re.compile(r'<script\b[^>]*>.*?</script>',re.I|re.S); RULE=re.compile(r'([^{}]+)\{([^{}]*)\}',re.S); CLASS=re.compile(r'\.([A-Za-z_][\w-]*)'); CLASS_ATTR=re.compile(r'class=["\']([^"\']+)["\']',re.I); HEX=re.compile(r'#[0-9a-fA-F]{3,8}\b'); RADIUS=re.compile(r'border-radius\s*:\s*([^;]+)',re.I); SHADOW=re.compile(r'box-shadow\s*:\s*([^;]+)',re.I); FONT=re.compile(r'font-family\s*:\s*([^;]+)',re.I)
ALLOWED_HEX={x.lower() for x in {'#294533','#183024','#738371','#f5f0e7','#fbf8f2','#fffefb','#242a26','#656d67','#ad823d','#ded8cd','#244833','#244432','#334139','#25382d','#2b5540','#264b39','#29332d','#2d3b33','#283b30','#343a36','#3d4540','#3e4741','#3f4642','#252b27','#333333','#333','#393b39','#6a655e','#6b736f','#8b6939','#88683b','#5f6862','#657068','#59645d','#5d665f','#525c56','#4b5850','#48564d','#eef2ed','#eaf0e8','#f7f2e9','#f8f5ef','#faf8f3','#f1eadf','#f0ece4','#eee7da','#eee8de','#f5f1e9','#fff8fa','#f3dce4','#5d464b','#fbf7f0','#c6a982','#d8bd87','#ebe5da','#e3ddd2','#cfc6b7','#dad4c8','#d7d0c5','#ece6dd','#dde5dc','#d7dfd6','#d9d4ca','#17291f','#2c503a','#274a36','#2b503b','#f6f4ed','#cbc6bc','#ccc5b9','#d9d4cb','#f8f5ee','#eee8df','#e6e0d7','#ddd7cd','#6a716d','#777f79','#4d5751','#555e58','#676f6a','#d8d2c8','#2d332f','#5b655f','#f8f4ec','#fffaf2','#e8efe8','#e4ded3','#fff'}}
def uniq(seq,limit=30):
    out=[];seen=set()
    for x in seq:
        k=str(x)
        if k not in seen:seen.add(k);out.append(x)
        if len(out)>=limit:break
    return out
rows=[];details={}
for path in sorted(Path('.').glob('*.html')):
    if path.name=='index.html':continue
    text=path.read_text(encoding='utf-8');markup=SCRIPT_BLOCK.sub('',STYLE_BLOCK.sub('',text));dom=set()
    for a in CLASS_ATTR.findall(markup):dom.update(a.split())
    rules=0;un=[];colors=set();radii=[];shadows=[];fonts=[]
    for block in STYLE_BLOCK.findall(text):
        for sel,decl in RULE.findall(block):
            sel=' '.join(sel.split())
            if sel.startswith('@') or not VISUAL_PROP.search(';'+decl):continue
            classes=set(CLASS.findall(sel))
            if classes and not(classes&dom):continue
            rules+=1;meaning=(classes&dom)-STRUCTURAL
            if meaning and not(meaning&LOCK_CLASSES):
                un.append(sel[:180])
                for h in HEX.findall(decl):
                    if h.lower() not in ALLOWED_HEX:colors.add(h.lower())
                for v in RADIUS.findall(decl):
                    x=v.strip().lower()
                    if x not in {'0','0px','2px','2px!important','50%','0!important'} and 'var(' not in x:radii.append((sel[:100],v.strip()[:60]))
                for v in SHADOW.findall(decl):
                    if v.strip().lower() not in {'none','none!important'}:shadows.append((sel[:100],v.strip()[:80]))
                for v in FONT.findall(decl):
                    if not any(x in v.lower() for x in ['arial','helvetica','georgia','times new roman','serif','sans-serif']):fonts.append((sel[:100],v.strip()[:80]))
    un=uniq(un);radii=uniq(radii,15);shadows=uniq(shadows,15);fonts=uniq(fonts,10);score=len(un)+2*len(colors)+len(radii)+len(shadows)+2*len(fonts);rows.append((score,path.name,rules,len(un),sorted(colors),radii,shadows,fonts));details[path.name]=un
rows.sort(reverse=True);report=['# Body Visual Consistency Audit','','This audit checks only page-specific visual CSS selectors that are **actually used by elements in the current page markup** and are not explicitly governed by the final homepage/body design locks. Dead/unused legacy CSS is ignored.','',f'- Interior pages inspected: **{len(rows)}**','', '| Page | Risk score | Used visual rules | Used uncovered selectors | Noncanonical colors | Unusual radii | Shadows | Fonts |','|---|---:|---:|---:|---:|---:|---:|---:|']
for r in rows:report.append(f'| `{r[1]}` | {r[0]} | {r[2]} | {r[3]} | {len(r[4])} | {len(r[5])} | {len(r[6])} | {len(r[7])} |')
report+=['','## Remaining pages and used selectors']
for score,name,rules,nun,colors,radii,shadows,fonts in rows:
    if not score:continue
    report+=['',f'### `{name}` — score {score}']
    if colors:report.append('- Noncanonical colors: '+', '.join(colors))
    if radii:report.append('- Unusual radii: '+'; '.join(f'`{s}` → `{v}`' for s,v in radii[:6]))
    if shadows:report.append('- Shadows: '+'; '.join(f'`{s}`' for s,_ in shadows[:6]))
    if fonts:report.append('- Fonts: '+'; '.join(f'`{s}` → `{v}`' for s,v in fonts[:4]))
    if details[name]:
        report.append('- Used visual selectors not governed by the final locks:')
        for s in details[name][:20]:report.append(f'  - `{s}`')
zero=sum(1 for r in rows if not r[0]);report+=['',f'- Pages with no used visual escape selectors: **{zero}/{len(rows)}**'];Path('BODY-STYLE-AUDIT.md').write_text('\n'.join(report)+'\n',encoding='utf-8');print('Used-body visual audit complete; zero-risk pages:',zero,'/',len(rows))
