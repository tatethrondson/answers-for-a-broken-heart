from pathlib import Path
import re
from html import unescape

BATCH=[1,5,9,13,14,15,18,19,21,22]

def clean(s):
    s=re.sub(r'<[^>]+>',' ',s,flags=re.S)
    return re.sub(r'\s+',' ',unescape(s)).strip()

def grab(pattern,text,default=''):
    m=re.search(pattern,text,re.S|re.I)
    return clean(m.group(1)) if m else default

lines=['# Audio Batch 1 Source Extract','', 'Pulled directly from the current Answer pages so recording scripts stay aligned with the published site.','']
for n in BATCH:
    p=Path(f'answer-{n:02d}.html')
    text=p.read_text(encoding='utf-8',errors='ignore')
    question=grab(r'<section class="hero".*?<h1>(.*?)</h1>',text)
    short_block=re.search(r'<section class="short".*?</section>',text,re.S|re.I)
    sb=short_block.group(0) if short_block else ''
    short_heading=grab(r'<h2>(.*?)</h2>',sb)
    short_paras=re.findall(r'<p(?:\s[^>]*)?>(.*?)</p>',sb,re.S|re.I)
    short_text=clean(short_paras[-1]) if short_paras else ''
    minute=re.search(r'<section class="minuteHelp".*?</section>',text,re.S|re.I)
    mb=minute.group(0) if minute else ''
    items=re.findall(r'<div class="minuteItem">(.*?)</div>',mb,re.S|re.I)
    scripture_label=scripture=''; prayer=''; next_step=''
    if len(items)>0:
        scripture_label=grab(r'<strong>(.*?)</strong>',items[0])
        scripture=grab(r'<p[^>]*>(.*?)</p>',items[0])
    if len(items)>1:
        prayer=grab(r'<p[^>]*>(.*?)</p>',items[1])
    if len(items)>2:
        next_step=grab(r'<p[^>]*>(.*?)</p>',items[2])
    lines += [
        f'## Answer {n:02d}', '',
        f'**Question:** {question}', '',
        f'**Short answer:** {short_heading}', '',
        short_text, '',
        f'**Featured Scripture:** {scripture_label}', '',
        scripture, '',
        f'**Existing prayer:** {prayer}', '',
        f'**Existing next step:** {next_step}', '',
        '---',''
    ]

Path('AUDIO-BATCH1-SOURCE.md').write_text('\n'.join(lines),encoding='utf-8')
print('Extracted',len(BATCH),'Answer sources')
