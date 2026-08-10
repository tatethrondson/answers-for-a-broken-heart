from pathlib import Path
import re

GUIDE_PUBLIC = Path('2am-guide.html')
GUIDE_ACCESS = Path('2am-guide-access.html')
ACCESS_NEXT = 'https://answersforabrokenheart.com/2am-guide-access?welcome=1'
ACCESS_PATH = '/2am-guide-access'

LANDING = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#294533">
<title>Free 2:00 A.M. Guide | 7 Scriptures for a Hard Night</title>
<meta name="description" content="Get the free 2:00 A.M. Guide: seven KJV Scriptures, short pastoral reminders, and simple prayers for the nights when your thoughts are loud.">
<link rel="canonical" href="https://answersforabrokenheart.com/2am-guide">
<style>
:root{--deep:#183024;--green:#294533;--cream:#f6f1e8;--paper:#fffdf9;--ink:#24312b;--muted:#667068;--gold:#b69258;--line:#ddd6c9}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:Arial,Helvetica,sans-serif;line-height:1.7}a{color:inherit}.wrap{width:min(1020px,calc(100% - 40px));margin:auto}header{background:var(--deep);color:white;padding:21px 0}.brand{color:white;text-decoration:none;font:1.42rem/.88 Georgia,serif}.brand small{display:block;font-size:.72rem;color:rgba(255,255,255,.72)}.hero{padding:68px 0 62px;background:linear-gradient(120deg,#f7f2e9,#edf1eb)}.eyebrow{text-transform:uppercase;letter-spacing:.17em;font-size:.68rem;color:#88683b;font-weight:800;margin:0 0 12px}h1,h2,h3{font-family:Georgia,"Times New Roman",serif;font-weight:400;letter-spacing:-.025em}.heroGrid{display:grid;grid-template-columns:1.08fr .92fr;gap:58px;align-items:center}.hero h1{font-size:clamp(3.2rem,6vw,5.45rem);line-height:.99;color:var(--deep);margin:0 0 18px}.lead{font:1.2rem/1.58 Georgia,serif;color:#4d5a52;max-width:680px;margin:0 0 18px}.promise{font-size:.84rem;color:#657068}.card{background:white;border:1px solid var(--line);border-top:4px solid var(--gold);padding:30px;box-shadow:0 18px 42px rgba(30,44,35,.1)}.card h2{font-size:2rem;line-height:1.08;color:var(--deep);margin:0 0 9px}.card p{font-size:.88rem;color:#5d6761;margin:0 0 18px}.form{display:grid;gap:9px}.form input[type=email]{width:100%;border:1px solid #d7d0c5;background:#fffefb;padding:14px 15px;font-size:.93rem;min-height:50px}.form button{border:0;background:var(--green);color:white;padding:14px 15px;min-height:50px;font-size:.73rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;cursor:pointer}.form button:hover{background:var(--deep)}.honey{position:absolute!important;left:-5000px!important;width:1px!important;height:1px!important;overflow:hidden!important}.privacy{font-size:.66rem;color:#737b76;line-height:1.45}.inside{padding:54px 0 66px}.insideHead{text-align:center;max-width:700px;margin:0 auto 28px}.insideHead h2{font-size:2.45rem;color:var(--deep);margin:0 0 10px}.insideHead p{color:var(--muted);margin:0}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.item{border:1px solid var(--line);background:#fff;padding:24px}.item small{display:block;text-transform:uppercase;letter-spacing:.12em;font-size:.62rem;font-weight:800;color:#88683b;margin-bottom:7px}.item h3{font-size:1.45rem;line-height:1.14;color:var(--deep);margin:0 0 8px}.item p{font-size:.82rem;color:#626b65;margin:0}.night{background:var(--deep);color:white;padding:42px 0}.night h2{color:white;font-size:2.25rem;margin:0 0 10px}.night p{color:rgba(255,255,255,.8);max-width:780px;margin:0}.returning{display:none;margin-top:13px;font-size:.75rem}.returning a{font-weight:800;color:var(--green)}footer{background:#10251b;color:rgba(255,255,255,.72);padding:25px 0;font-size:.75rem}@media(max-width:780px){.heroGrid,.grid{grid-template-columns:1fr}.hero{padding:52px 0}.card{padding:25px}.hero h1{font-size:3.5rem}}
</style>
<script>window.va=window.va||function(){(window.vaq=window.vaq||[]).push(arguments)};</script><script defer src="/_vercel/insights/script.js"></script>
</head><body>
<header><div class="wrap"><a class="brand" href="/">Answers<small>for a Broken Heart</small></a></div></header>
<main>
<section class="hero"><div class="wrap heroGrid"><div><p class="eyebrow">Free resource · 7 Scriptures</p><h1>Something true to hold onto at 2:00 a.m.</h1><p class="lead">When the room is quiet and your thoughts are loud, you probably do not need another lecture. You need one true thing to hold onto. This free guide gives you seven Scriptures, short pastoral reminders, and simple prayers for the hardest hour of the night.</p><p class="promise">Free. Printable. Written to help before it promotes anything.</p></div><div class="card"><p class="eyebrow">Get the free guide</p><h2>Send me the 2:00 A.M. Guide.</h2><p>Enter your email and you’ll go straight to the guide. I’ll also send occasional pastoral encouragement and let you know when <em>Answers for a Broken Heart</em> is ready.</p><form data-email-segment="guide_2am" class="form" action="https://formsubmit.co/tatethrondson@gmail.com" method="POST"><input type="email" name="email" placeholder="Your email address" aria-label="Your email address" autocomplete="email" required><input type="text" name="_honey" class="honey" tabindex="-1" autocomplete="off"><input type="hidden" name="_subject" value="New 2:00 A.M. Guide signup"><input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="_next" value="https://answersforabrokenheart.com/2am-guide-access?welcome=1"><input type="hidden" name="interest" value="2:00 A.M. Guide + occasional pastoral notes + book release updates"><input type="hidden" name="source" value="2:00 A.M. Guide landing page"><input type="hidden" name="segment" value="guide_2am"><button type="submit">Send Me the Free Guide</button><div class="privacy">No daily emails. Just occasional pastoral encouragement, new resources, and book-release updates.</div></form><div class="returning" id="returning">Already requested the guide on this device? <a href="/2am-guide-access">Open it again →</a></div></div></div></section>
<section class="inside"><div class="wrap"><div class="insideHead"><p class="eyebrow">Inside the guide</p><h2>Seven Scriptures for the moment you cannot solve tonight.</h2><p>Each passage includes a short reminder and a simple prayer so you can slow down, tell God the truth, and take one faithful next step.</p></div><div class="grid"><div class="item"><small>When God feels far away</small><h3>Psalm 34:18</h3><p>God’s nearness is not measured by whether you can feel Him in the moment.</p></div><div class="item"><small>When fear keeps talking</small><h3>Isaiah 41:10</h3><p>The answer to fear is not pretending there is nothing frightening. It is remembering who is with you.</p></div><div class="item"><small>When morning feels far away</small><h3>Lamentations 3:22–23</h3><p>Pain has not exhausted the compassion of God. There will be mercy for the morning when it comes.</p></div></div></div></section>
<section class="night"><div class="wrap"><p class="eyebrow" style="color:#d8bd87">You do not have to solve everything tonight</p><h2>Read one passage. Pray one honest sentence. Take the next faithful step.</h2><p>The guide is designed to be useful in the moment—not to make you sort through a course, watch a long video, or pretend your pain is simple.</p></div></section>
</main><footer><div class="wrap">Answers for a Broken Heart · Tate Throndson · Psalm 34:18</div></footer>
<script>try{if(localStorage.getItem('afabh_2am_access')==='1'){document.getElementById('returning').style.display='block'}}catch(e){}</script>
</body></html>'''

GATE_SCRIPT = '''<script>
(function(){
  try{
    var key='afabh_2am_access';
    var params=new URLSearchParams(window.location.search);
    if(params.get('welcome')==='1'){
      localStorage.setItem(key,'1');
      history.replaceState({},'', '/2am-guide-access');
      return;
    }
    if(localStorage.getItem(key)!=='1'){
      window.location.replace('/2am-guide');
    }
  }catch(e){
    if(new URLSearchParams(window.location.search).get('welcome')!=='1'){
      window.location.replace('/2am-guide');
    }
  }
})();
</script>'''


def build_access(source):
    text = source
    # The full guide is a private-after-signup resource, not a search landing page.
    text = re.sub(r'<meta name="robots" content="[^"]*">', '', text)
    text = re.sub(r'<link rel="canonical" href="[^"]*">', '', text)
    if '<meta name="robots" content="noindex,follow">' not in text:
        text = text.replace('<meta name="theme-color" content="#294533">', '<meta name="robots" content="noindex,follow"><meta name="theme-color" content="#294533">', 1)
    text = text.replace('<title>The 2:00 A.M. Guide | Answers for a Broken Heart</title>', '<title>Your 2:00 A.M. Guide | Answers for a Broken Heart</title>', 1)
    # Keep the unlock check early so a fresh visitor cannot simply browse to the access URL.
    text = text.replace('</head>', GATE_SCRIPT + '</head>', 1)
    text = text.replace('<a class="btn" href="/what-hurts-today">Browse All 24 Answers</a>', '<a class="btn" href="/all-answers">Browse All 24 Answers</a>')
    return text


# First capture the current full guide before replacing the public URL with the signup page.
if GUIDE_PUBLIC.exists():
    current = GUIDE_PUBLIC.read_text(encoding='utf-8')
    if '<section class="entry">' in current and '<!-- 2AM-GATE-LANDING -->' not in current:
        GUIDE_ACCESS.write_text(build_access(current), encoding='utf-8')
        print('Created gated 2:00 A.M. guide access page')
    GUIDE_PUBLIC.write_text('<!-- 2AM-GATE-LANDING -->\n' + LANDING, encoding='utf-8')
    print('Converted /2am-guide to email signup landing page')

for path in Path('.').glob('*.html'):
    text = path.read_text(encoding='utf-8')
    original = text

    # Retire the legacy homepage router URL now that /about is a real page.
    text = text.replace('href="/?view=about"', 'href="/about"')

    # Any existing 2:00 A.M. Guide signup should unlock the guide after FormSubmit records the email.
    text = text.replace(
        'name="_next" value="https://answersforabrokenheart.com/2am-guide"',
        f'name="_next" value="{ACCESS_NEXT}"'
    )

    # Public calls to action should accurately describe the gated lead magnet.
    text = text.replace('Open the 2:00 A.M. Guide', 'Get the 2:00 A.M. Guide')
    text = text.replace('Read the free guide →', 'Get the free guide →') if path.name in {'index.html','free-guides.html'} else text
    text = text.replace('Open the guide →', 'Get the guide →') if path.name == 'church-resources.html' else text

    if text != original:
        path.write_text(text, encoding='utf-8')
        print('Polished', path.name)
