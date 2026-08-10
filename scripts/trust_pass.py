from pathlib import Path
import re

# Strengthen authorship across all Answer pages without clutter.
for n in range(1,25):
    p=Path(f'answer-{n:02d}.html')
    if not p.exists(): continue
    s=p.read_text(encoding='utf-8')
    s=s.replace('Written by <a href="/about" rel="author">Tate Throndson</a> · Pastor and author of <em>Answers for a Broken Heart</em>', 'Written by <a href="/about" rel="author">Tate Throndson</a> · Senior pastor of Castleview Baptist Church in Castle Rock, Colorado · Pastor and author of <em>Answers for a Broken Heart</em>')
    # Make 24 Answers link use the clean all-answers route.
    s=s.replace('<a href="/what-hurts-today">24 Answers</a>','<a href="/all-answers">24 Answers</a>')
    p.write_text(s,encoding='utf-8')

# About page: clarify why this voice can be trusted, while avoiding inflated claims.
p=Path('about.html')
if p.exists():
    s=p.read_text(encoding='utf-8')
    s=s.replace('<a class="mobileStart" href="/what-hurts-today">Start Here</a>','<a class="mobileStart" href="/start-here">Start Here</a>')
    marker='<section class="section approach">'
    trust='''<!-- TRUST-CREDIBILITY-START -->
<section class="section" aria-label="Why readers can trust this resource"><div class="wrap"><div class="approachHead"><p class="eyebrow">Why this voice?</p><h2>Pastoral experience. Biblical conviction. No promise of easy answers.</h2><p>This site is not written from a distance. Tate has spent more than twenty-five years in full-time ministry and has pastored Castleview Baptist Church since planting it in 2008. The perspective here has been shaped not only in sermon preparation, but in hospital rooms, funerals, counseling conversations, family crises, and years of walking with people through questions that do not disappear when the service ends.</p></div><div class="cards"><div class="card"><small>Pastoral</small><h3>Written by a working pastor.</h3><p>The aim is the same as a good pastoral conversation: listen carefully, tell the truth, open Scripture, and resist the temptation to rush someone through pain.</p></div><div class="card"><small>Biblical</small><h3>Scripture sets the boundaries.</h3><p>The answers are written from a Baptist, evangelical Christian perspective and are intended to be clear about what Scripture says—and careful where Scripture does not give us a private explanation.</p></div><div class="card"><small>Personal</small><h3>Help before promotion.</h3><p>You can read the Answers, use the guides, and listen to the resources without buying the book. The site is designed to serve hurting people first.</p></div></div></div></section>
<!-- TRUST-CREDIBILITY-END -->'''
    s=re.sub(r'<!-- TRUST-CREDIBILITY-START -->.*?<!-- TRUST-CREDIBILITY-END -->','',s,flags=re.S)
    if marker in s: s=s.replace(marker,trust+marker,1)
    p.write_text(s,encoding='utf-8')

# Homepage: add a compact credibility bridge near the author/book area, not in the hero.
p=Path('index.html')
if p.exists():
    s=p.read_text(encoding='utf-8')
    css='''.trustStrip{padding:24px 0;background:#fffdf9;border-top:1px solid #ddd6c9;border-bottom:1px solid #ddd6c9}.trustStripInner{display:grid;grid-template-columns:auto 1fr auto;gap:20px;align-items:center}.trustStrip img{width:62px;height:62px;border-radius:50%;object-fit:cover;object-position:center 23%}.trustStrip strong{display:block;font:1.05rem/1.2 Georgia,serif;color:#20372a;margin-bottom:4px}.trustStrip p{margin:0;font-size:.75rem;line-height:1.5;color:#657068}.trustStrip a{font-size:.7rem;font-weight:800;color:#294533;text-decoration:none;white-space:nowrap}@media(max-width:700px){.trustStripInner{grid-template-columns:auto 1fr}.trustStrip a{grid-column:2}}'''
    if '.trustStrip{' not in s: s=s.replace('</style>',css+'</style>',1)
    block='''<!-- HOME-TRUST-START --><section class="trustStrip"><div class="wrap trustStripInner"><img src="/author-tate.jpg?v=7" alt="Tate Throndson"><div><strong>Written from a pastor’s chair, not an ivory tower.</strong><p>Tate Throndson is senior pastor of Castleview Baptist Church in Castle Rock, Colorado, where he has served since planting the church in 2008. These resources grow out of years of preaching, counseling, hospital rooms, funerals, and walking with hurting people.</p></div><a href="/about">Meet Tate →</a></div></section><!-- HOME-TRUST-END -->'''
    s=re.sub(r'<!-- HOME-TRUST-START -->.*?<!-- HOME-TRUST-END -->','',s,flags=re.S)
    # Place before book bridge if possible, otherwise before newsletter.
    target='<!-- BOOK-BRIDGE-HOME-START -->'
    if target in s: s=s.replace(target,block+target,1)
    elif '<section class="newsletter"' in s: s=s.replace('<section class="newsletter"',block+'<section class="newsletter"',1)
    p.write_text(s,encoding='utf-8')

print('Trust and credibility pass applied')