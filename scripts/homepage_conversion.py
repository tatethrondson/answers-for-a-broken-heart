from pathlib import Path
import re
p=Path('index.html')
s=p.read_text(encoding='utf-8')

# Make the hero's first decision unmistakable.
s=re.sub(r'<div class="heroButtons">.*?</div>', '<div class="heroButtons"><a class="btn primary" href="/start-here">I\'m Hurting — Start Here</a> <a class="btn outline" href="/all-answers">Browse the 24 Answers</a></div>', s, count=1, flags=re.S)

# Add a short first-visit bridge immediately after the hero, only once.
start='<!-- HOME-FIRST-VISIT-START -->'; end='<!-- HOME-FIRST-VISIT-END -->'
block='''<!-- HOME-FIRST-VISIT-START -->
<section class="firstVisit"><div class="wrap firstVisitGrid"><div><p class="eyebrow">First time here?</p><h2>You do not have to figure out the whole site.</h2><p>If you are hurting, begin with one simple question: <strong>What hurts today?</strong> Start Here will help you find the most useful Answer, Scripture, guide, or conversation for what you are carrying right now.</p></div><div class="firstVisitActions"><a class="btn primary" href="/start-here">Start Here</a><a class="quietLink" href="/what-hurts-today">Or tell me where it hurts →</a></div></div></section>
<!-- HOME-FIRST-VISIT-END -->'''
if start in s:
    a=s.index(start); b=s.index(end,a)+len(end); s=s[:a]+block+s[b:]
else:
    hero_end=s.find('</section>',s.find('<section class="hero"'))
    if hero_end!=-1:
        hero_end+=len('</section>'); s=s[:hero_end]+'\n'+block+s[hero_end:]

css='''.firstVisit{padding:30px 0;background:#183024;color:white;border-bottom:1px solid rgba(255,255,255,.08)}.firstVisitGrid{display:grid;grid-template-columns:1fr auto;gap:42px;align-items:center}.firstVisit .eyebrow{color:#d8bd87}.firstVisit h2{font-size:1.9rem;line-height:1.08;margin:0 0 8px;color:white}.firstVisit p{margin:0;max-width:720px;font-size:.84rem;color:rgba(255,255,255,.8)}.firstVisitActions{display:flex;align-items:center;gap:18px;white-space:nowrap}.firstVisit .btn.primary{background:#f6f1e8;color:#20372a;border-color:#f6f1e8}.quietLink{font-size:.72rem;font-weight:800;color:white;text-decoration:none}@media(max-width:760px){.firstVisitGrid{grid-template-columns:1fr;gap:18px}.firstVisitActions{align-items:flex-start;flex-direction:column;gap:10px}}'''
if '.firstVisit{' not in s:
    s=s.replace('</style>',css+'</style>',1)

# Reduce top-navigation competition: preserve destinations, but prioritize Start Here.
nav=re.search(r'<nav class="navlinks">.*?</nav>',s,re.S)
if nav:
    new='<nav class="navlinks"><a class="active" href="/start-here">Start Here</a><a href="/what-hurts-today">What Hurts Today?</a><a href="/free-guides">Free Guides</a><a href="/?view=book">The Book</a><a href="/church-resources">For Churches</a></nav>'
    s=s[:nav.start()]+new+s[nav.end():]

p.write_text(s,encoding='utf-8')
print('Homepage conversion hierarchy updated')