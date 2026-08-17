from pathlib import Path

ROOT = Path('.')
MARKER = '<!-- SUPPORTING-ARTICLES-WAVE2-START -->'

STYLE = '''<style>
.supportingLinksWave2{padding:54px 0;background:#f8f5ef;border-top:1px solid #e7e0d6}
.supportingLinksWave2 .waveWrap{width:min(1120px,calc(100% - 42px));margin:auto}
.supportingLinksWave2 .waveEyebrow{text-transform:uppercase;letter-spacing:.15em;font-size:.67rem;font-weight:800;color:#88683b;margin:0 0 8px}
.supportingLinksWave2 h2{font:400 2.25rem/1.08 Georgia,"Times New Roman",serif;color:#183024;margin:0 0 10px}
.supportingLinksWave2 .waveLead{max-width:760px;margin:0 0 23px;color:#5f6862}
.supportingLinksWave2 .waveGrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.supportingLinksWave2 .waveCard{display:block;text-decoration:none;background:#fff;border:1px solid #ded8cd;padding:22px;transition:.2s ease}
.supportingLinksWave2 .waveCard:hover{transform:translateY(-2px);box-shadow:0 12px 28px rgba(30,44,35,.08)}
.supportingLinksWave2 .waveCard small{display:block;text-transform:uppercase;letter-spacing:.11em;font-size:.64rem;font-weight:800;color:#88683b;margin-bottom:7px}
.supportingLinksWave2 .waveCard strong{display:block;font:400 1.35rem/1.22 Georgia,"Times New Roman",serif;color:#183024;margin-bottom:8px}
.supportingLinksWave2 .waveCard span{display:block;font-size:.84rem;line-height:1.55;color:#657068}
@media(max-width:700px){.supportingLinksWave2 .waveGrid{grid-template-columns:1fr}.supportingLinksWave2 h2{font-size:2rem}}
</style>'''

def block(cards, heading='Practical help for the next step', lead='Sometimes the question is not only what is true, but what to do with it today.'):
    card_html=''.join(
        f'<a class="waveCard" href="{href}"><small>Practical guide</small><strong>{title}</strong><span>{desc}</span></a>'
        for href,title,desc in cards
    )
    return f'''\n{MARKER}\n{STYLE}\n<section class="supportingLinksWave2"><div class="waveWrap"><p class="waveEyebrow">Practical help</p><h2>{heading}</h2><p class="waveLead">{lead}</p><div class="waveGrid">{card_html}</div></div></section>\n<!-- SUPPORTING-ARTICLES-WAVE2-END -->\n'''

def inject(path, html):
    p=ROOT/path
    text=p.read_text(encoding='utf-8')
    if MARKER in text:
        return False
    if '</main>' not in text:
        raise RuntimeError(f'{path}: </main> not found')
    p.write_text(text.replace('</main>', html+'\n</main>',1),encoding='utf-8')
    return True

changes=[]
if inject('anger-and-unanswered-prayer.html', block([
    ('/how-to-pray-when-angry-with-god','How do I pray when I’m angry with God?','A simple KJV framework for bringing disappointment and anger into God’s presence without pretending the hurt is small.'),
    ('/what-do-i-say-to-god-right-now','What do I say to God right now?','Continue into the full Answer when you do not have polished words left.')
], heading='When prayer itself feels hard', lead='Anger and disappointment can make prayer feel dangerous. These resources give you a place to begin without forcing a tidy emotion.')):
    changes.append('anger-and-unanswered-prayer.html')

if inject('grief-and-loss.html', block([
    ('/what-to-say-to-someone-grieving','What should I say to someone who is grieving?','Simple words, specific help, and a way to stay present without trying to fix the loss.'),
    ('/what-not-to-say-to-someone-grieving','What should I avoid saying?','Well-meant phrases can make grief feel smaller. Learn what to avoid—and what to say instead.')
], heading='Helping someone walk through grief', lead='Grief is hard to carry and sometimes just as hard to stand beside. These guides are for the friend, family member, pastor, or church member who wants to love someone well.')):
    changes.append('grief-and-loss.html')

if inject('help-someone.html', block([
    ('/what-to-say-to-someone-grieving','What to say to someone who is grieving','A practical script for the room where words suddenly feel inadequate.'),
    ('/what-not-to-say-to-someone-grieving','What not to say to someone who is grieving','Avoid explanations, comparisons, and spiritual shortcuts that accidentally minimize pain.')
], heading='When you are trying to find the words', lead='You do not need a perfect sentence. These guides help you speak with compassion and stay present.')):
    changes.append('help-someone.html')

if inject('god-feels-far-away.html', block([
    ('/scriptures-when-god-feels-far-away','7 KJV Scriptures for when God feels far away','Read one promise slowly when prayer feels flat or God’s presence is hard to recognize.'),
    ('/why-does-god-feel-far-away','Why does God feel far away when I’m hurting?','Go deeper into the first Answer and the biblical pattern of God moving toward broken people.')
], heading='Something true to hold onto tonight', lead='When feelings are loud and God seems quiet, start with one promise rather than trying to solve everything at once.')):
    changes.append('god-feels-far-away.html')

sitemap=ROOT/'sitemap.xml'
text=sitemap.read_text(encoding='utf-8')
urls=[
    'https://www.answersforabrokenheart.com/how-to-pray-when-angry-with-god',
    'https://www.answersforabrokenheart.com/what-to-say-to-someone-grieving',
    'https://www.answersforabrokenheart.com/scriptures-when-god-feels-far-away',
]
new=[]
for url in urls:
    if f'<loc>{url}</loc>' not in text:
        new.append(f'  <url><loc>{url}</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>')
if new:
    text=text.replace('</urlset>','\n'.join(new)+'\n</urlset>')
    sitemap.write_text(text,encoding='utf-8')
    changes.append('sitemap.xml')

print('Updated:', ', '.join(changes) if changes else 'already current')
