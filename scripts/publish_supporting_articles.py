from pathlib import Path
import re

START='<!-- SUPPORTING-ARTICLES-START -->'
END='<!-- SUPPORTING-ARTICLES-END -->'

STYLE='''<style>
.supportingLinks{padding:46px 0;background:#fff;border-top:1px solid #e8e1d7}
.supportingLinks .supportingInner{width:min(1120px,calc(100% - 42px));margin:auto}
.supportingLinks .supportingEyebrow{text-transform:uppercase;letter-spacing:.15em;color:#ad823d;font-size:.67rem;font-weight:800;margin:0 0 9px}
.supportingLinks h2{font:400 2rem/1.1 Georgia,"Times New Roman",serif;color:#183024;margin:0 0 10px}
.supportingLinks .supportingIntro{color:#626b65;margin:0 0 20px;max-width:760px;font-size:.91rem;line-height:1.6}
.supportingLinks .supportingGrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.supportingLinks .supportingCard{display:block;text-decoration:none;border:1px solid #ded8cd;background:#faf8f3;padding:20px;transition:.2s ease}
.supportingLinks .supportingCard:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(30,44,35,.08)}
.supportingLinks .supportingCard small{display:block;text-transform:uppercase;letter-spacing:.11em;color:#87683a;font-size:.64rem;font-weight:800;margin-bottom:7px}
.supportingLinks .supportingCard strong{display:block;font:400 1.32rem/1.22 Georgia,"Times New Roman",serif;color:#183024;margin-bottom:6px}
.supportingLinks .supportingCard span{display:block;color:#626b65;font-size:.82rem;line-height:1.5}
@media(max-width:700px){.supportingLinks .supportingGrid{grid-template-columns:1fr}}
</style>'''

def block(cards, eyebrow='Practical help', heading='One more step for the situation you are carrying.', intro='These web-only resources go beyond the 24 core Answers with practical help for common questions.'):
    html=[]
    for href,title,desc in cards:
        html.append(f'<a class="supportingCard" href="{href}"><small>Practical guide</small><strong>{title}</strong><span>{desc} →</span></a>')
    return START+'\n'+STYLE+f'''\n<section class="supportingLinks"><div class="supportingInner"><p class="supportingEyebrow">{eyebrow}</p><h2>{heading}</h2><p class="supportingIntro">{intro}</p><div class="supportingGrid">{''.join(html)}</div></div></section>\n'''+END

def inject(path, cards, *, before=None, eyebrow='Practical help', heading='One more step for the situation you are carrying.', intro='These web-only resources go beyond the 24 core Answers with practical help for common questions.'):
    p=Path(path)
    text=p.read_text(encoding='utf-8')
    text=re.sub(re.escape(START)+r'.*?'+re.escape(END)+r'\s*','',text,flags=re.S)
    addition=block(cards,eyebrow,heading,intro)+'\n'
    if before and before in text:
        text=text.replace(before,addition+before,1)
    elif '</main>' in text:
        text=text.replace('</main>',addition+'</main>',1)
    else:
        raise RuntimeError(f'No insertion point in {path}')
    p.write_text(text,encoding='utf-8')

inject('grief-and-loss.html',[
    ('/what-not-to-say-to-someone-grieving','What not to say to someone who is grieving','Simple guidance for loving someone without minimizing or explaining away the loss.'),
    ('/help-someone','When someone you love is hurting','A practical pastoral guide for showing up when you do not know what to do.')
],before='<!-- PODCAST-RESOURCE-START -->',eyebrow='Helping someone else',heading='Walking beside grief without trying to fix it.',intro='Sometimes the question is not only, “How do I survive this?” It is, “How do I love someone else who is hurting?”')

inject('forgiveness-and-relational-hurt.html',[
    ('/what-forgiveness-does-not-mean','What forgiveness does not mean','Forgiveness is not the same as forgetting, removing consequences, restoring trust, or immediate reconciliation.'),
    ('/does-forgiveness-mean-reconciliation','Does forgiveness mean reconciliation?','A core Answer about forgiveness, access, trust, boundaries, and restoration.')
],before='<!-- PODCAST-RESOURCE-START -->',eyebrow='Practical boundaries',heading='Forgiveness needs clarity, not clichés.',intro='Biblical forgiveness is powerful enough to coexist with truth, consequences, wisdom, and appropriate boundaries.')

inject('doubt-and-church-hurt.html',[
    ('/can-christians-go-to-counseling','Can Christians go to counseling?','A biblical way to think about pastoral care, therapy, mental-health treatment, and asking for wise help.'),
    ('/can-christians-be-depressed','Can Christians be depressed?','Pastoral help for the shame many believers feel when emotional pain does not disappear with prayer.')
],before='<!-- PODCAST-RESOURCE-START -->',eyebrow='Faith and mental health',heading='Getting help does not mean faith has failed.',intro='Spiritual questions and mental-health concerns can overlap. You do not have to hide one in order to address the other.')

inject('can-christians-be-depressed.html',[
    ('/can-christians-go-to-counseling','Can Christians go to counseling?','When prayer, Scripture, church care, counseling, and medical care may need to work together.'),
    ('/start-here','Tell me where it hurts','If depression is only one piece of what you are carrying, start with the sentence that sounds most like your pain.')
],eyebrow='A wise next step',heading='You do not have to carry this alone.',intro='Sometimes the next faithful step is not trying harder by yourself. It is telling someone trustworthy what is really happening.')

sitemap=Path('sitemap.xml')
text=sitemap.read_text(encoding='utf-8')
for route in [
    '/what-not-to-say-to-someone-grieving',
    '/can-christians-go-to-counseling',
    '/what-forgiveness-does-not-mean',
]:
    url='https://www.answersforabrokenheart.com'+route
    if f'<loc>{url}</loc>' not in text:
        entry=f'  <url><loc>{url}</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>\n'
        text=text.replace('</urlset>',entry+'</urlset>')
sitemap.write_text(text,encoding='utf-8')

print('Supporting articles integrated into topic paths and sitemap.')
