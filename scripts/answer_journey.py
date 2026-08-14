from pathlib import Path
import re
import html

START = "<!-- ANSWER-JOURNEY-START -->"
END = "<!-- ANSWER-JOURNEY-END -->"
GUIDE_ACCESS = "/2am-guide-access"

STYLE = '''<style>
.answerJourney{margin:52px 0 18px;padding:32px;background:#183024;color:#fff;border:1px solid #183024}
.answerJourney .journeyEyebrow{margin:0 0 8px;text-transform:uppercase;letter-spacing:.14em;font-size:.66rem;font-weight:800;color:#d8bd87}
.answerJourney h2{font:2.15rem/1.08 Georgia,"Times New Roman",serif;font-weight:400;color:#fff;margin:0 0 10px}
.answerJourney .journeyLead{margin:0 0 23px!important;color:rgba(255,255,255,.8);font-size:.92rem;line-height:1.62}
.journeyGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.journeyCard{display:flex;flex-direction:column;text-decoration:none!important;background:#fff;color:#24312b!important;border:1px solid rgba(255,255,255,.2);padding:20px;min-height:150px;transition:.2s ease}
.journeyCard:hover{transform:translateY(-2px);box-shadow:0 12px 26px rgba(0,0,0,.14)}
.journeyCard small{display:block;text-transform:uppercase;letter-spacing:.11em;font-size:.62rem;font-weight:800;color:#88683b;margin-bottom:7px}
.journeyCard strong{display:block;font:1.24rem/1.18 Georgia,"Times New Roman",serif;font-weight:400;color:#20372a;margin-bottom:7px}
.journeyCard span{display:block;margin-top:auto;font-size:.75rem;font-weight:800;color:#294533}
.journeyCard.listen{background:#f6f1e8}.journeyCard.nightPath{background:#eef2ed}
.journeyCard.listen.hasThumb{padding:0;background:#fffdf9;overflow:hidden}
.journeyThumb{position:relative;aspect-ratio:16/9;overflow:hidden;background:#d8d2c8}
.journeyThumb img{display:block;width:100%;height:100%;object-fit:cover}
.journeyPlay{position:absolute;left:14px;bottom:12px;width:42px;height:42px;border-radius:50%;display:flex!important;align-items:center;justify-content:center;background:rgba(24,48,36,.94);color:#fff!important;font-size:1rem!important;line-height:1;margin:0!important;box-shadow:0 6px 16px rgba(0,0,0,.2)}
.journeyListenCopy{padding:17px 18px 18px;display:flex;flex-direction:column;flex:1}
.journeyBookLink{margin-top:15px;font-size:.76rem;color:rgba(255,255,255,.72)}
.journeyBookLink a{color:#fff;font-weight:800}
.shareHelp{margin-top:18px;padding:22px 0 0;border-top:1px solid rgba(255,255,255,.18)}
.shareHelp strong{display:block;font:1.28rem/1.2 Georgia,"Times New Roman",serif;font-weight:400;color:#fff;margin-bottom:5px}
.shareHelp p{margin:0 0 13px!important;color:rgba(255,255,255,.76);font-size:.8rem}
.shareRow{display:flex;gap:8px;flex-wrap:wrap}.shareBtn{border:1px solid rgba(255,255,255,.35);background:transparent;color:#fff;text-decoration:none;padding:9px 12px;font-size:.68rem;font-weight:800;cursor:pointer}.shareBtn:hover{background:#fff;color:#183024}.copyStatus{font-size:.66rem;color:#d8bd87;align-self:center}
.guideCapture{margin-top:18px;padding:22px;background:#f6f1e8;color:#24312b;display:grid;grid-template-columns:1.05fr .95fr;gap:24px;align-items:center}
.guideCapture small{display:block;text-transform:uppercase;letter-spacing:.12em;font-size:.62rem;font-weight:800;color:#88683b;margin-bottom:6px}.guideCapture strong{display:block;font:1.35rem/1.18 Georgia,"Times New Roman",serif;font-weight:400;color:#20372a;margin-bottom:6px}.guideCapture p{margin:0!important;font-size:.82rem;line-height:1.5;color:#5e6861}.guideForm{display:grid;grid-template-columns:1fr 138px;gap:8px}.guideForm input[type="email"]{width:100%;border:1px solid #d7d0c5;background:#fff;padding:12px 13px;font-size:.82rem;min-height:44px}.guideForm button{border:0;background:#294533;color:#fff;padding:11px 12px;min-height:44px;font-size:.68rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em;cursor:pointer}.guideForm .privacy{grid-column:1/-1;font-size:.62rem;color:#6c746f;line-height:1.4}.guideHoney{position:absolute!important;left:-5000px!important;width:1px!important;height:1px!important;overflow:hidden!important}
.journeyAfter{margin-top:15px;font-size:.78rem;color:rgba(255,255,255,.72)}.journeyAfter a{color:#fff;font-weight:800}
@media(max-width:760px){.answerJourney{padding:27px 22px}.answerJourney h2{font-size:1.9rem}.journeyGrid,.guideCapture{grid-template-columns:1fr}.journeyCard{min-height:0}.guideForm{grid-template-columns:1fr}.guideForm button{width:100%}}
</style>'''

PODCASTS = {4:("Ava's Story: How God Is Still Good in the Hardest Trials","https://www.youtube.com/watch?v=JpQrjWxY4Ys"),6:("When Life Doesn't Let Up... Listen to This","https://www.youtube.com/watch?v=UP_nNGjbvNY"),7:("When Everything Falls Apart: How Ron & Nancy Are Still Trusting God","https://www.youtube.com/watch?v=mOayIZ01R5w"),11:("When Everything Falls Apart: How Ron & Nancy Are Still Trusting God","https://www.youtube.com/watch?v=mOayIZ01R5w"),13:("John & Carol Johnson: Faith Through a Cancer Journey","https://youtu.be/fkPXcbH79-c"),17:("Bitter No More: 4 Signs God's Wisdom Is Winning in You","https://www.youtube.com/watch?v=C-gKb_skcUg"),21:("Overcoming Bitterness with Pastor Tate Throndson","https://youtu.be/opc26tntVRc"),22:("Turn the Other Cheek... or Protect Your Family?","https://www.youtube.com/watch?v=-Tj-7LsEAUY")}
TOPICS = {1:("When God Feels Far Away","/god-feels-far-away"),2:("When God Feels Far Away","/god-feels-far-away"),3:("When God Feels Far Away","/god-feels-far-away"),9:("When God Feels Far Away","/god-feels-far-away"),10:("When God Feels Far Away","/god-feels-far-away"),4:("Why God Allows Suffering","/why-god-allows-suffering"),5:("Why God Allows Suffering","/why-god-allows-suffering"),6:("Why God Allows Suffering","/why-god-allows-suffering"),7:("Why God Allows Suffering","/why-god-allows-suffering"),8:("Why God Allows Suffering","/why-god-allows-suffering"),11:("Anger & Unanswered Prayer","/anger-and-unanswered-prayer"),13:("Anger & Unanswered Prayer","/anger-and-unanswered-prayer"),18:("Anger & Unanswered Prayer","/anger-and-unanswered-prayer"),19:("Anger & Unanswered Prayer","/anger-and-unanswered-prayer"),12:("Forgiveness & Relational Hurt","/forgiveness-and-relational-hurt"),20:("Forgiveness & Relational Hurt","/forgiveness-and-relational-hurt"),21:("Forgiveness & Relational Hurt","/forgiveness-and-relational-hurt"),22:("Forgiveness & Relational Hurt","/forgiveness-and-relational-hurt"),14:("Grief & Loss","/grief-and-loss"),15:("Grief & Loss","/grief-and-loss"),16:("Grief & Loss","/grief-and-loss"),17:("Grief & Loss","/grief-and-loss"),23:("Doubt, Church Hurt & Faith","/doubt-and-church-hurt"),24:("Doubt, Church Hurt & Faith","/doubt-and-church-hurt")}
FOLLOW_UP = {
    1:3, 2:1, 3:1, 9:10, 10:9,
    4:5, 5:6, 6:7, 7:8, 8:4,
    11:18, 13:19, 18:19, 19:18,
    12:20, 20:21, 21:22, 22:12,
    14:15, 15:17, 16:15, 17:15,
    23:24, 24:23,
}


def youtube_id(url):
    if 'youtu.be/' in url:
        return url.split('youtu.be/',1)[1].split('?',1)[0].split('&',1)[0]
    match = re.search(r'[?&]v=([^&]+)', url)
    return match.group(1) if match else ''


def answer_title(n):
    path = Path(f"answer-{n:02d}.html")
    if not path.exists():
        return f"Read Answer {n:02d}"
    text = path.read_text(encoding='utf-8')
    match = re.search(r'<h1>(.*?)</h1>', text, re.S)
    if not match:
        return f"Read Answer {n:02d}"
    value = re.sub(r'<[^>]+>', '', match.group(1))
    return html.unescape(value).strip()


def youtube_card(title, url):
    vid = youtube_id(url)
    thumb = f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg" if vid else ''
    image = f'''<div class="journeyThumb"><img src="{thumb}" alt="" loading="lazy" decoding="async"><span class="journeyPlay" aria-hidden="true">▶</span></div>''' if thumb else ''
    return f'''<a class="journeyCard listen hasThumb" href="{url}" target="_blank" rel="noopener noreferrer">{image}<div class="journeyListenCopy"><small>Listen</small><strong>{title}</strong><span>Listen on YouTube →</span></div></a>'''


def related_card(target):
    return f'''<a class="journeyCard listen" href="/answer-{target:02d}"><small>Another question nearby</small><strong>{answer_title(target)}</strong><span>Read this answer →</span></a>'''


def block(n):
    topic, topic_url = TOPICS[n]
    follow = FOLLOW_UP[n]
    page_url = f"https://answersforabrokenheart.com/answer-{n:02d}"

    if n in PODCASTS:
        title, url = PODCASTS[n]
        first = youtube_card(title, url)
    else:
        first = related_card(follow)

    topic_card = f'''<a class="journeyCard" href="{topic_url}"><small>See the whole subject</small><strong>{topic}</strong><span>Explore the topic guide →</span></a>'''
    tonight_card = f'''<a class="journeyCard nightPath" href="{GUIDE_ACCESS}"><small>For a hard night</small><strong>I just need something true to hold onto.</strong><span>Open the 2:00 A.M. Guide →</span></a>'''

    share = f'''<div class="shareHelp"><strong>Know someone who may need this?</strong><p>You do not have to explain their pain for them. Sometimes the kindest thing is simply to send something that may help them feel less alone.</p><div class="shareRow"><button class="shareBtn" type="button" onclick="navigator.clipboard.writeText('{page_url}').then(()=>{{this.parentElement.querySelector('.copyStatus').textContent='Link copied'}})">Copy Link</button><a class="shareBtn" href="sms:?&body=I thought this might help you: {page_url}">Text This</a><a class="shareBtn" href="mailto:?subject=Thought this might help&body=I came across this and thought of you: {page_url}">Email This</a><span class="copyStatus" aria-live="polite"></span></div></div>'''

    capture = f'''<div class="guideCapture"><div><small>Optional · Pastoral notes</small><strong>Want occasional encouragement like this?</strong><p>The answers and guides are free to read. If you would like occasional pastoral notes, new resources, and book-release updates, leave your email here.</p></div><form data-email-segment="pastoral_notes" class="guideForm" action="https://formsubmit.co/tatethrondson@gmail.com" method="POST"><input type="email" name="email" placeholder="Your email address" aria-label="Your email address" autocomplete="email" required><input type="text" name="_honey" class="guideHoney" tabindex="-1" autocomplete="off"><input type="hidden" name="_subject" value="New pastoral notes signup from Answer {n:02d}"><input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="_next" value="{page_url}"><input type="hidden" name="interest" value="Pastoral encouragement + new resources + book release updates"><input type="hidden" name="source" value="Answer {n:02d}"><input type="hidden" name="segment" value="pastoral_notes"><button type="submit">Keep Me Encouraged</button><div class="privacy">Optional. No daily emails—just occasional pastoral encouragement, new resources, and book updates.</div></form></div>'''

    related_line = ''
    if n in PODCASTS:
        related_line = f'''You may also want to read <a href="/answer-{follow:02d}">{answer_title(follow)} →</a> &nbsp;·&nbsp; '''

    return f'''{START}\n{STYLE}\n<section class="answerJourney" aria-label="Where to go next"><p class="journeyEyebrow">If you need another step</p><h2>Choose what would help next.</h2><p class="journeyLead">You do not have to keep reading just because there is more on the page. Stop here if this was enough. If you need another step, choose only one.</p><div class="journeyGrid">{first}{topic_card}{tonight_card}</div><div class="journeyBookLink">When you want a longer, deeper journey, <a href="/book">explore <em>Answers for a Broken Heart</em> →</a></div>{share}{capture}<div class="journeyAfter">{related_line}<a href="/start-here">start again with what hurts →</a> &nbsp;·&nbsp; <a href="/all-answers">browse all 24 questions →</a></div></section>\n{END}'''


for n in range(1,25):
    p = Path(f"answer-{n:02d}.html")
    if not p.exists():
        continue
    text = p.read_text(encoding="utf-8")
    text = re.sub(re.escape(START) + r".*?" + re.escape(END), "", text, flags=re.S)
    # The unified journey is now the single home for contextual podcast recommendations.
    text = re.sub(r"<!-- PODCAST-RESOURCE-START -->.*?<!-- PODCAST-RESOURCE-END -->", "", text, flags=re.S)
    # Normalize legacy SPA-style answer links to clean, shareable URLs.
    text = re.sub(r'href="/\?answer=(\d{2})"', r'href="/answer-\1"', text)
    text = re.sub(r'href="\?answer=(\d{2})"', r'href="/answer-\1"', text)
    if "</article>" in text:
        text = text.replace("</article>", block(n) + "\n</article>", 1)
    p.write_text(text, encoding="utf-8")
