from pathlib import Path
import re

SITE = "https://answersforabrokenheart.com"
EMAIL = "tatethrondson@gmail.com"

CSS_START = "/* HOPE-CONVERSION-START */"
CSS_END = "/* HOPE-CONVERSION-END */"
CSS = f'''{CSS_START}
.hopeBand{{background:#183024;color:#fff;padding:42px 0;border-top:1px solid rgba(255,255,255,.08);border-bottom:1px solid rgba(255,255,255,.08)}}
.hopeGrid{{display:grid;grid-template-columns:1.05fr .95fr;gap:52px;align-items:center}}
.hopeBand .eyebrow{{color:#d8bd87;margin-bottom:9px}}
.hopeBand h2{{font:2.45rem/1.04 Georgia,"Times New Roman",serif;font-weight:400;letter-spacing:-.025em;color:#fff;margin:0 0 11px}}
.hopeBand p{{margin:0;color:rgba(255,255,255,.82);font-size:.88rem;line-height:1.62;max-width:620px}}
.bookUpdates.hopeBand{{display:block;padding:42px 46px}}
.hopeForm{{display:grid;grid-template-columns:1fr 150px;gap:9px;align-items:start}}
.hopeForm input[type="email"]{{width:100%;border:1px solid rgba(255,255,255,.28);background:#fff;color:#28332d;padding:14px 15px;min-height:49px;font-size:.9rem;border-radius:0}}
.hopeForm button{{border:1px solid #d8bd87;background:#d8bd87;color:#183024;padding:13px 16px;min-height:49px;font-size:.72rem;letter-spacing:.06em;text-transform:uppercase;font-weight:800;cursor:pointer}}
.hopeForm button:hover{{background:#ead9b7}}
.hopePrivacy{{grid-column:1/-1;font-size:.66rem!important;line-height:1.45!important;color:rgba(255,255,255,.67)!important;margin-top:1px!important}}
.hopeHoney{{position:absolute!important;left:-5000px!important;width:1px!important;height:1px!important;overflow:hidden!important}}
.answerHope{{background:#20372a;color:#fff;padding:42px 0;border-top:1px solid rgba(255,255,255,.06)}}
.answerHope .hopeGrid{{grid-template-columns:1.02fr .98fr}}
.answerHope .eyebrow{{color:#d8bd87}}
.answerHope h2{{font:2.3rem/1.06 Georgia,"Times New Roman",serif;font-weight:400;margin:0 0 11px;color:#fff}}
.answerHope p{{color:rgba(255,255,255,.82);margin:0;max-width:610px}}
@media(max-width:780px){{.hopeGrid,.answerHope .hopeGrid{{grid-template-columns:1fr;gap:24px}}.hopeForm{{grid-template-columns:1fr}}.hopeForm button{{width:100%}}.hopeBand h2,.answerHope h2{{font-size:2rem}}}}
{CSS_END}'''


def form_html(source, button="Get the Free Guide"):
    return f'''<form class="hopeForm" action="https://formsubmit.co/{EMAIL}" method="POST">
<input type="email" name="email" placeholder="Your email address" aria-label="Your email address" autocomplete="email" required>
<input type="text" name="_honey" class="hopeHoney" tabindex="-1" autocomplete="off">
<input type="hidden" name="_subject" value="New 2:00 A.M. Guide signup - {source}">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_captcha" value="false">
<input type="hidden" name="_url" value="{SITE}/">
<input type="hidden" name="_next" value="{SITE}/hope-thanks">
<input type="hidden" name="interest" value="The 2:00 A.M. Guide + Answers for a Broken Heart updates">
<input type="hidden" name="source" value="{source}">
<button type="submit">{button}</button>
<div class="hopePrivacy">Immediate access to the guide, plus occasional biblical encouragement and book-release updates. No spam.</div>
</form>'''

HOME_SECTION = f'''<section class="hopeBand" id="newsletter"><div class="wrap hopeGrid"><div><p class="eyebrow">Free 2:00 A.M. Guide</p><h2>Hope for the hour when your mind won’t shut off.</h2><p>Get <em>The 2:00 A.M. Guide: 7 Scriptures to Read When You Don’t Know What Else to Do</em>. It is short, pastoral, printable, and built for the moment when you need something true to hold onto.</p></div>{form_html("Homepage", "Get the Free Guide")}</div></section>'''

BOOK_SECTION = f'''<!-- BOOK-UPDATES-START --><div id="book-updates" class="bookUpdates hopeBand" style="margin-top:30px"><div class="hopeGrid"><div><p class="eyebrow">Free Guide + Book Updates</p><h2>Be the first to know — and take something helpful with you now.</h2><p>Get <em>The 2:00 A.M. Guide</em> today, then receive occasional updates when Kindle preorder, signed copies, and release details for <em>Answers for a Broken Heart</em> become available.</p></div>{form_html("About the Book / preorder page", "Get the Guide + Updates")}</div></div><!-- BOOK-UPDATES-END -->'''

def answer_section(source):
    return f'''<!-- ANSWER-HOPE-START --><section class="answerHope"><div class="wrap hopeGrid"><div><p class="eyebrow">Before you go</p><h2>Take something with you for tonight.</h2><p>Get the free <em>2:00 A.M. Guide</em> — seven Scriptures with brief pastoral thoughts and simple prayers for the moments when your heart is heavy and you do not know what else to do.</p></div>{form_html(source, "Get the Free Guide")}</div></section><!-- ANSWER-HOPE-END -->'''


def inject_css(text):
    text = re.sub(re.escape(CSS_START) + r".*?" + re.escape(CSS_END) + r"\s*", "", text, flags=re.S)
    return text.replace("</style>", CSS + "\n</style>", 1)


def patch_index(path):
    text = path.read_text()
    text = inject_css(text)
    text = re.sub(r'<section class="newsletter" id="newsletter">.*?</section>', HOME_SECTION, text, count=1, flags=re.S)
    text = re.sub(r'<!-- BOOK-UPDATES-START -->.*?<!-- BOOK-UPDATES-END -->', BOOK_SECTION, text, count=1, flags=re.S)
    path.write_text(text)


def patch_answer(path):
    text = path.read_text()
    text = inject_css(text)
    text = re.sub(r'<!-- ANSWER-HOPE-START -->.*?<!-- ANSWER-HOPE-END -->\s*', "", text, flags=re.S)
    anchor = '<!-- RELATED-ANSWERS-START -->'
    if anchor in text:
        text = text.replace(anchor, answer_section(path.stem.replace("answer-", "Answer ")) + "\n" + anchor, 1)
    elif '<section class="cta">' in text:
        text = text.replace('<section class="cta">', answer_section(path.stem.replace("answer-", "Answer ")) + '\n<section class="cta">', 1)
    path.write_text(text)


GUIDE = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>The 2:00 A.M. Guide | Answers for a Broken Heart</title>
<meta name="robots" content="noindex,follow"><meta name="theme-color" content="#294533">
<style>
:root{--deep:#183024;--green:#294533;--cream:#f6f1e8;--paper:#fffdf9;--ink:#24312b;--gold:#b69258;--line:#ddd6c9}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:Arial,Helvetica,sans-serif;line-height:1.72}.wrap{width:min(820px,calc(100% - 38px));margin:auto}header{background:var(--deep);color:white;padding:22px 0}.brand{color:white;text-decoration:none;font:1.35rem/.9 Georgia,serif}.brand small{display:block;font-size:.72rem}.hero{padding:68px 0 56px;background:linear-gradient(120deg,#f8f4eb,#edf1eb)}.eyebrow{text-transform:uppercase;letter-spacing:.16em;font-size:.7rem;color:#88683b;font-weight:800;margin:0 0 12px}h1,h2{font-family:Georgia,"Times New Roman",serif;font-weight:400;letter-spacing:-.025em}h1{font-size:clamp(3rem,7vw,5.2rem);line-height:1;margin:0 0 18px;color:var(--deep)}.lead{font:1.2rem/1.6 Georgia,serif;color:#4e5b53;max-width:720px}.tools{margin-top:24px;display:flex;gap:10px;flex-wrap:wrap}.btn{display:inline-block;padding:11px 15px;background:var(--green);color:#fff;text-decoration:none;border:0;font-weight:800;font-size:.77rem;letter-spacing:.05em;text-transform:uppercase;cursor:pointer}.guide{padding:52px 0 72px}.intro{font-size:1.04rem;margin-bottom:38px}.entry{padding:32px 0;border-top:1px solid var(--line)}.num{font-size:.7rem;letter-spacing:.15em;text-transform:uppercase;color:#88683b;font-weight:800}.entry h2{font-size:2rem;line-height:1.08;color:var(--deep);margin:7px 0 14px}.scripture{background:var(--cream);padding:22px 24px;border-left:3px solid var(--gold);font:1.13rem/1.65 Georgia,serif;margin:0 0 18px}.remember{font-weight:800;color:var(--green)}.prayer{font:italic 1rem/1.6 Georgia,serif;color:#4a554e;margin-top:13px}.closing{background:var(--deep);color:white;padding:42px 0}.closing h2{color:white;font-size:2.25rem;margin:0 0 12px}.closing p{color:rgba(255,255,255,.82)}.closing .btn{background:#d8bd87;color:#183024;margin-right:8px;margin-top:8px}footer{background:#10251b;color:rgba(255,255,255,.7);padding:24px 0;font-size:.76rem}@media print{header,.tools,.closing,footer{display:none}.hero{padding:20px 0;background:white}.guide{padding:0}.entry{break-inside:avoid}.wrap{width:100%}}
</style>
<script>window.va=window.va||function(){(window.vaq=window.vaq||[]).push(arguments)};</script><script defer src="/_vercel/insights/script.js"></script>
</head><body><header><div class="wrap"><a class="brand" href="/">Answers<small>for a Broken Heart</small></a></div></header>
<section class="hero"><div class="wrap"><p class="eyebrow">A free resource from Tate Throndson</p><h1>The 2:00 A.M. Guide</h1><p class="lead">7 Scriptures to Read When You Don’t Know What Else to Do</p><div class="tools"><button class="btn" onclick="window.print()">Print / Save as PDF</button><a class="btn" href="/what-hurts-today">Find an Answer</a></div></div></section>
<main class="guide"><div class="wrap"><p class="intro">If you are reading this in the middle of the night, you probably do not need a lecture. You need something solid enough to hold onto while your emotions are loud and the room is quiet. You do not have to solve everything tonight. Read one passage slowly. Tell God the truth. Stay with the words long enough for them to become more than words.</p>
<section class="entry"><div class="num">01 · When God feels far away</div><h2>Psalm 34:18</h2><div class="scripture">“The LORD is nigh unto them that are of a broken heart; and saveth such as be of a contrite spirit.”</div><p><span class="remember">What to remember:</span> A broken heart can make God feel distant, but Scripture says the opposite. He is not standing at the edge of your pain waiting for you to get yourself together. He is near to the person whose heart has been crushed.</p><p class="prayer">“Lord, I do not feel strong right now. Help me believe that You are nearer than I can feel.”</p></section>
<section class="entry"><div class="num">02 · When everything feels unstable</div><h2>Psalm 46:1</h2><div class="scripture">“God is our refuge and strength, a very present help in trouble.”</div><p><span class="remember">What to remember:</span> God does not promise that trouble will never arrive. He promises that when it does, you will not face it without a refuge. You may not know what tomorrow holds, but you know where to run tonight.</p><p class="prayer">“God, be my refuge for the next hour. Give me enough strength for the next faithful step.”</p></section>
<section class="entry"><div class="num">03 · When fear keeps talking</div><h2>Isaiah 41:10</h2><div class="scripture">“Fear thou not; for I am with thee: be not dismayed; for I am thy God: I will strengthen thee; yea, I will help thee; yea, I will uphold thee with the right hand of my righteousness.”</div><p><span class="remember">What to remember:</span> The answer to fear is not pretending there is nothing frightening. It is remembering who is with you in it. God does not merely tell you to be stronger. He says, “I will strengthen thee.”</p><p class="prayer">“Father, my mind keeps running toward what might happen. Hold me steady while I cannot see ahead.”</p></section>
<section class="entry"><div class="num">04 · When you are afraid to admit you are afraid</div><h2>Psalm 56:3</h2><div class="scripture">“What time I am afraid, I will trust in thee.”</div><p><span class="remember">What to remember:</span> David did not say, “I am never afraid.” He said there is something he can do when fear arrives. Faith is not the absence of fear. Sometimes faith is deciding where you will turn while you are still afraid.</p><p class="prayer">“Lord, I am afraid. I am bringing that fear to You instead of hiding it from You.”</p></section>
<section class="entry"><div class="num">05 · When you are exhausted</div><h2>Matthew 11:28</h2><div class="scripture">“Come unto me, all ye that labour and are heavy laden, and I will give you rest.”</div><p><span class="remember">What to remember:</span> Jesus does not ask weary people to impress Him. He invites them to come. You can come tired. You can come confused. You can come with unanswered questions. Rest begins with bringing the weight to Christ instead of carrying it alone.</p><p class="prayer">“Jesus, I am tired of carrying this. Teach me what it means to come to You with it tonight.”</p></section>
<section class="entry"><div class="num">06 · When you feel too weak for this</div><h2>2 Corinthians 12:9</h2><div class="scripture">“My grace is sufficient for thee: for my strength is made perfect in weakness.”</div><p><span class="remember">What to remember:</span> Weakness is not a disqualification from grace. It is often the place where grace becomes most visible. You may not have enough strength for everything ahead of you, but God has not asked you to manufacture tomorrow’s strength tonight.</p><p class="prayer">“God, I do not have enough for all of this. Let Your grace be enough for me right now.”</p></section>
<section class="entry"><div class="num">07 · When morning feels a long way off</div><h2>Lamentations 3:22-23</h2><div class="scripture">“It is of the LORD'S mercies that we are not consumed, because his compassions fail not. They are new every morning: great is thy faithfulness.”</div><p><span class="remember">What to remember:</span> Jeremiah wrote about new mercies while standing in the wreckage of deep grief. Morning did not erase what had happened. It reminded him that pain had not exhausted the compassion of God. There will be mercy for the morning when it comes.</p><p class="prayer">“Father, carry me through this night. Help me trust that Your mercy will meet me again in the morning.”</p></section>
</div></main>
<section class="closing"><div class="wrap"><p class="eyebrow" style="color:#d8bd87">You do not have to solve everything tonight</p><h2>Start with the question that hurts most.</h2><p><em>Answers for a Broken Heart</em> exists to help you bring the real question into the light of Scripture without pretending the pain is simple.</p><a class="btn" href="/what-hurts-today">Browse All 24 Answers</a><a class="btn" href="/?view=book">About the Book</a></div></section>
<footer><div class="wrap">Answers for a Broken Heart · Tate Throndson · Psalm 34:18</div></footer></body></html>'''

THANKS = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,follow"><meta name="theme-color" content="#294533"><title>Your 2:00 A.M. Guide Is Ready | Answers for a Broken Heart</title><style>:root{--deep:#183024;--green:#294533;--cream:#f6f1e8;--paper:#fffdf9;--ink:#24312b;--gold:#b69258;--line:#ddd6c9}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:Arial,Helvetica,sans-serif;line-height:1.65}.wrap{width:min(980px,calc(100% - 40px));margin:auto}header{background:var(--deep);padding:22px 0}.brand{color:white;text-decoration:none;font:1.35rem/.9 Georgia,serif}.brand small{display:block;font-size:.72rem}.hero{padding:78px 0 68px;background:linear-gradient(120deg,#f8f4eb,#edf1eb)}.eyebrow{text-transform:uppercase;letter-spacing:.16em;font-size:.7rem;color:#88683b;font-weight:800;margin:0 0 12px}h1,h2,h3{font-family:Georgia,"Times New Roman",serif;font-weight:400;letter-spacing:-.025em}h1{font-size:clamp(3rem,6vw,5rem);line-height:1;margin:0 0 18px;color:var(--deep)}.lead{font:1.2rem/1.6 Georgia,serif;color:#4e5b53;max-width:720px}.btn{display:inline-block;background:var(--green);color:white;text-decoration:none;padding:13px 18px;font-size:.76rem;letter-spacing:.06em;text-transform:uppercase;font-weight:800;margin-top:20px}.next{padding:58px 0 72px}.next h2{font-size:2.35rem;color:var(--deep);margin:0 0 9px}.nextLead{color:#66716a;margin:0 0 26px}.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:15px}.card{display:block;text-decoration:none;background:white;border:1px solid var(--line);padding:24px}.card small{display:block;text-transform:uppercase;letter-spacing:.12em;color:#88683b;font-weight:800;margin-bottom:7px}.card strong{display:block;font:1.35rem/1.25 Georgia,serif;color:var(--deep);font-weight:400;margin-bottom:8px}.card span{font-size:.82rem;color:#66716a}@media(max-width:760px){.cards{grid-template-columns:1fr}}footer{background:#10251b;color:rgba(255,255,255,.7);padding:24px 0;font-size:.76rem}</style><script>window.va=window.va||function(){(window.vaq=window.vaq||[]).push(arguments)};</script><script defer src="/_vercel/insights/script.js"></script></head><body><header><div class="wrap"><a class="brand" href="/">Answers<small>for a Broken Heart</small></a></div></header><main><section class="hero"><div class="wrap"><p class="eyebrow">You’re in</p><h1>Your guide is ready.</h1><p class="lead">Thank you for trusting me with your inbox. Start with the free <em>2:00 A.M. Guide</em> now. You do not have to wait for an email — it is ready for you here.</p><a class="btn" href="/2am-guide">Open the 2:00 A.M. Guide →</a></div></section><section class="next"><div class="wrap"><p class="eyebrow">While you’re here</p><h2>What does your heart need next?</h2><p class="nextLead">If one of these sounds close to what you are carrying, start there.</p><div class="cards"><a class="card" href="/answer-03"><small>Answer 03 · God Feels Far Away</small><strong>Why can’t I see what God is doing right now?</strong><span>You’ll See It Looking Back →</span></a><a class="card" href="/answer-15"><small>Answer 15 · Grief &amp; Loss</small><strong>How long am I allowed to still be sad about this?</strong><span>You’re Allowed to Grieve as Long as It Takes →</span></a><a class="card" href="/answer-19"><small>Answer 19 · Anger &amp; Unanswered Prayer</small><strong>What do I even say to God right now?</strong><span>Bring Him the Real Prayer, Not the Polished One →</span></a></div></div></section></main><footer><div class="wrap">Answers for a Broken Heart · Tate Throndson · Psalm 34:18</div></footer></body></html>'''

patch_index(Path("index.html"))
for path in sorted(Path(".").glob("answer-*.html")):
    patch_answer(path)
Path("2am-guide.html").write_text(GUIDE)
Path("hope-thanks.html").write_text(THANKS)
print("Hope conversion layer complete: guide, signup invitations, and thank-you pathway are current.")
