from pathlib import Path
import re

START = "<!-- ANSWER-JOURNEY-START -->"
END = "<!-- ANSWER-JOURNEY-END -->"

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
.journeyCard.listen{background:#f6f1e8}
.journeyCard.bookPath{background:#eef2ed}
.guideCapture{margin-top:18px;padding:22px;background:#f6f1e8;color:#24312b;display:grid;grid-template-columns:1.05fr .95fr;gap:24px;align-items:center}
.guideCapture small{display:block;text-transform:uppercase;letter-spacing:.12em;font-size:.62rem;font-weight:800;color:#88683b;margin-bottom:6px}
.guideCapture strong{display:block;font:1.35rem/1.18 Georgia,"Times New Roman",serif;font-weight:400;color:#20372a;margin-bottom:6px}
.guideCapture p{margin:0!important;font-size:.82rem;line-height:1.5;color:#5e6861}
.guideForm{display:grid;grid-template-columns:1fr 138px;gap:8px}
.guideForm input[type="email"]{width:100%;border:1px solid #d7d0c5;background:#fff;padding:12px 13px;font-size:.82rem;min-height:44px}
.guideForm button{border:0;background:#294533;color:#fff;padding:11px 12px;min-height:44px;font-size:.68rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em;cursor:pointer}
.guideForm .privacy{grid-column:1/-1;font-size:.62rem;color:#6c746f;line-height:1.4}
.guideHoney{position:absolute!important;left:-5000px!important;width:1px!important;height:1px!important;overflow:hidden!important}
@media(max-width:760px){.answerJourney{padding:27px 22px}.answerJourney h2{font-size:1.9rem}.journeyGrid,.guideCapture{grid-template-columns:1fr}.journeyCard{min-height:0}.guideForm{grid-template-columns:1fr}.guideForm button{width:100%}}
</style>'''

PODCASTS = {
4:("Ava's Story: How God Is Still Good in the Hardest Trials","https://www.youtube.com/watch?v=JpQrjWxY4Ys"),
6:("When Life Doesn't Let Up... Listen to This","https://www.youtube.com/watch?v=UP_nNGjbvNY"),
7:("When Everything Falls Apart: How Ron & Nancy Are Still Trusting God","https://www.youtube.com/watch?v=mOayIZ01R5w"),
11:("When Everything Falls Apart: How Ron & Nancy Are Still Trusting God","https://www.youtube.com/watch?v=mOayIZ01R5w"),
13:("John & Carol Johnson: Faith Through a Cancer Journey","https://youtu.be/fkPXcbH79-c"),
17:("Bitter No More: 4 Signs God's Wisdom Is Winning in You","https://www.youtube.com/watch?v=C-gKb_skcUg"),
21:("Overcoming Bitterness with Pastor Tate Throndson","https://youtu.be/opc26tntVRc"),
22:("Turn the Other Cheek... or Protect Your Family?","https://www.youtube.com/watch?v=-Tj-7LsEAUY"),
}

TOPICS = {
1:("When God Feels Far Away","/god-feels-far-away"),2:("When God Feels Far Away","/god-feels-far-away"),3:("When God Feels Far Away","/god-feels-far-away"),9:("When God Feels Far Away","/god-feels-far-away"),10:("When God Feels Far Away","/god-feels-far-away"),
4:("Why God Allows Suffering","/why-god-allows-suffering"),5:("Why God Allows Suffering","/why-god-allows-suffering"),6:("Why God Allows Suffering","/why-god-allows-suffering"),7:("Why God Allows Suffering","/why-god-allows-suffering"),8:("Why God Allows Suffering","/why-god-allows-suffering"),
11:("Anger & Unanswered Prayer","/anger-and-unanswered-prayer"),13:("Anger & Unanswered Prayer","/anger-and-unanswered-prayer"),18:("Anger & Unanswered Prayer","/anger-and-unanswered-prayer"),19:("Anger & Unanswered Prayer","/anger-and-unanswered-prayer"),
12:("Forgiveness & Relational Hurt","/forgiveness-and-relational-hurt"),20:("Forgiveness & Relational Hurt","/forgiveness-and-relational-hurt"),21:("Forgiveness & Relational Hurt","/forgiveness-and-relational-hurt"),22:("Forgiveness & Relational Hurt","/forgiveness-and-relational-hurt"),
14:("Grief & Loss","/grief-and-loss"),15:("Grief & Loss","/grief-and-loss"),16:("Grief & Loss","/grief-and-loss"),17:("Grief & Loss","/grief-and-loss"),
23:("Doubt, Church Hurt & Faith","/doubt-and-church-hurt"),24:("Doubt, Church Hurt & Faith","/doubt-and-church-hurt"),
}

NEXT = {i:(i+1 if i<24 else 1) for i in range(1,25)}

def block(n):
    topic, topic_url = TOPICS[n]
    nxt = NEXT[n]
    if n in PODCASTS:
        title,url=PODCASTS[n]
        listen=f'''<a class="journeyCard listen" href="{url}" target="_blank" rel="noopener noreferrer"><small>Listen</small><strong>{title}</strong><span>Listen on YouTube →</span></a>'''
    else:
        listen=f'''<a class="journeyCard listen" href="{topic_url}"><small>Stay with this subject</small><strong>Explore {topic}</strong><span>See the topic guide →</span></a>'''
    capture=f'''<div class="guideCapture"><div><small>Free resource · 7 Scriptures</small><strong>Want something to hold onto tonight?</strong><p>I’ll send you the free 2:00 A.M. Guide: seven Scriptures, short pastoral reminders, and simple prayers for the nights when your thoughts are loud.</p></div><form class="guideForm" action="https://formsubmit.co/tatethrondson@gmail.com" method="POST"><input type="email" name="email" placeholder="Your email address" aria-label="Your email address" autocomplete="email" required><input type="text" name="_honey" class="guideHoney" tabindex="-1" autocomplete="off"><input type="hidden" name="_subject" value="New 2:00 A.M. Guide signup from Answer {n:02d}"><input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="_next" value="https://answersforabrokenheart.com/2am-guide"><input type="hidden" name="interest" value="2:00 A.M. Guide + occasional pastoral notes + book release updates"><input type="hidden" name="source" value="Answer {n:02d}"><button type="submit">Send Me the Guide</button><div class="privacy">You’ll go straight to the guide after signing up. Occasional pastoral notes and book updates only.</div></form></div>'''
    return f'''{START}\n{STYLE}\n<section class="answerJourney" aria-label="Where to go next"><p class="journeyEyebrow">You do not have to stop here</p><h2>Choose your next step.</h2><p class="journeyLead">You may need to keep reading, hear a real conversation, or simply stay with this subject a little longer. Choose what would help most right now.</p><div class="journeyGrid">{listen}<a class="journeyCard" href="{topic_url}"><small>Go deeper</small><strong>{topic}</strong><span>Explore the full topic →</span></a><a class="journeyCard bookPath" href="/?view=book"><small>The deeper journey</small><strong>Answers for a Broken Heart</strong><span>Explore the book →</span></a></div>{capture}<div style="margin-top:15px;font-size:.78rem;color:rgba(255,255,255,.72)">Or <a href="/answer-{nxt:02d}" style="color:#fff;font-weight:800">continue to Answer {nxt:02d} →</a> &nbsp;·&nbsp; <a href="/all-answers" style="color:#fff;font-weight:800">browse all 24 answers →</a></div></section>\n{END}'''

for n in range(1,25):
    p=Path(f"answer-{n:02d}.html")
    if not p.exists():
        print("Missing",p); continue
    text=p.read_text(encoding="utf-8")
    text=re.sub(re.escape(START)+r".*?"+re.escape(END),"",text,flags=re.S)
    text=re.sub(r"<!-- PODCAST-RESOURCE-START -->.*?<!-- PODCAST-RESOURCE-END -->","",text,flags=re.S)
    anchor="</article>"
    if anchor not in text:
        print("No article anchor",p); continue
    text=text.replace(anchor,block(n)+"\n"+anchor,1)
    p.write_text(text,encoding="utf-8")
    print("Journey added",p)
