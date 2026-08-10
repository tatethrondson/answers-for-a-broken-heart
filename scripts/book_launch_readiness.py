from pathlib import Path
import json,re

cfg=json.loads(Path('data/book-launch.json').read_text(encoding='utf-8'))
p=Path('index.html')
s=p.read_text(encoding='utf-8')

status=cfg.get('status','coming_soon')
release=cfg.get('release_date','').strip()
amazon=cfg.get('amazon_url','').strip()

if cfg.get('purchase_enabled') and amazon:
    cta=f'<a class="btn primary" href="{amazon}" target="_blank" rel="noopener">Buy the Book</a>'
    kicker='Available Now'
elif cfg.get('preorder_enabled') and amazon:
    cta=f'<a class="btn primary" href="{amazon}" target="_blank" rel="noopener">Preorder the Book</a>'
    kicker='Preorder Available'
else:
    cta='<a class="btn primary" href="#launch-list">Join the Launch List</a>'
    kicker='Coming Soon'

if release:
    kicker += f' · {release}'

formats=[]
for key,label in [('paperback_enabled','Paperback'),('hardcover_enabled','Hardcover'),('ebook_enabled','eBook'),('audiobook_enabled','Audiobook'),('spanish_enabled','Spanish Edition')]:
    if cfg.get(key): formats.append(label)
format_text=' · '.join(formats) if formats else 'Formats will be announced as publication details are finalized.'

block=f'''<!-- BOOK-READY-START --><section class="bookReady"><div class="wrap bookReadyGrid"><div><p class="eyebrow">{kicker}</p><h2>{cfg['title']}</h2><p class="bookReadySub">{cfg['subtitle']}</p><p>The website will automatically switch from launch-list mode to preorder or purchase mode when verified publication links are added. Until then, nothing here implies that the book can already be ordered.</p>{cta}</div><div class="bookReadyMeta"><strong>Publication readiness</strong><span>{format_text}</span><span>Launch team: {'Ready to open' if cfg.get('launch_team_enabled') else 'Not open yet'}</span><span>Church bulk orders: {'Available' if cfg.get('bulk_orders_enabled') else 'Planned for launch'}</span></div></div></section><!-- BOOK-READY-END -->'''

css='''.bookReady{padding:48px 0;background:#f6f1e8;border-top:1px solid #ddd6c9;border-bottom:1px solid #ddd6c9}.bookReadyGrid{display:grid;grid-template-columns:1.2fr .8fr;gap:46px;align-items:center}.bookReady h2{font-size:2.45rem;line-height:1.05;color:#20372a;margin:0 0 6px}.bookReadySub{font:1.15rem/1.45 Georgia,serif;color:#48564d;margin:0 0 14px}.bookReady p{max-width:690px}.bookReadyMeta{background:#fffdf9;border:1px solid #ddd6c9;padding:24px}.bookReadyMeta strong{display:block;color:#20372a;margin-bottom:9px}.bookReadyMeta span{display:block;padding:7px 0;border-top:1px solid #ece6dd;font-size:.78rem;color:#657068}@media(max-width:760px){.bookReadyGrid{grid-template-columns:1fr}}'''
if '.bookReady{' not in s:
    s=s.replace('</style>',css+'</style>',1)
s=re.sub(r'<!-- BOOK-READY-START -->.*?<!-- BOOK-READY-END -->','',s,flags=re.S)
# Place near the existing book bridge rather than above the hurting-person journey.
marker='<!-- BOOK-BRIDGE-HOME-END -->'
if marker in s:
    s=s.replace(marker,marker+block,1)
elif '<!-- BOOK-LAUNCH-LIST-START -->' in s:
    s=s.replace('<!-- BOOK-LAUNCH-LIST-START -->',block+'<!-- BOOK-LAUNCH-LIST-START -->',1)
p.write_text(s,encoding='utf-8')
print('Book launch readiness rendered')