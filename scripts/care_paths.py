from pathlib import Path
import re
import html

CARE_CSS_START = "/* CARE-PATHS-START */"
CARE_CSS_END = "/* CARE-PATHS-END */"
CARE_HOME_START = "<!-- CARE-PATHS-HOME-START -->"
CARE_HOME_END = "<!-- CARE-PATHS-HOME-END -->"
SAFETY_SEARCH_START = "<!-- SAFETY-SEARCH-START -->"
SAFETY_SEARCH_END = "<!-- SAFETY-SEARCH-END -->"
SAFETY_LINK_START = "<!-- SAFETY-LINK-START -->"
SAFETY_LINK_END = "<!-- SAFETY-LINK-END -->"
AUDIO_START = "<!-- PASTOR-TATE-AUDIO-START -->"
AUDIO_END = "<!-- PASTOR-TATE-AUDIO-END -->"

SEARCH_TAGS = {
1: 'god absent alone abandoned lonely forsaken silence silent numb dry disconnected cannot feel god far away rejected by god god hates me unloved unseen forgotten empty',
2: 'god real proof evidence show himself invisible jesus doubt skeptical agnostic atheist is god there prove god faith questions',
3: 'confused direction unclear future waiting cannot see what god is doing uncertainty lost stuck decision next step no direction',
4: 'suffering pain evil cancer disease diagnosis illness tragedy why bad things world broken innocent accident disability chronic pain hospital',
5: 'why questions questioning god confused angry doubt wrong to ask why god why me questions faith',
6: 'no answer explanation mystery unanswered why silence waiting confused closure god will not tell me',
7: 'purpose good from pain meaning suffering redeem use this trauma growth brokenness something good',
8: 'no explanation closure unanswered questions mystery presence why no answers never know',
9: 'grief empathy does god understand pain jesus wept lonely sorrow loss heartbroken misunderstood',
10: 'death resurrection suffering end hope heaven grief final word dying fear death eternity',
11: 'justice unfair abuse wrongdoer gets away revenge anger injustice consequences wicked evil accountability',
12: 'victim blame guilt guilty ashamed shame abuse responsibility their fault my fault self blame condemnation',
13: 'unanswered prayer no denied prayer disappointment god said no waiting infertility job lost rejection prayer not answered',
14: 'death died funeral grief loss heaven goodbye bereavement spouse parent child friend mom mother dad father miscarriage stillbirth widow widower cemetery',
15: 'grief timeline still sad years mourning miss them anniversary not over it crying sadness lonely holidays birthday',
16: 'why me unfair suffering purpose meaning happened to me trauma accident diagnosis loss singled out',
17: 'grief stuck worse bitterness healing not getting better depression depressed anxiety anxious panic attack numb hopeless hopelessness exhausted burnout insomnia sleep cannot sleep cant sleep awake 2am overwhelmed',
18: 'angry at god furious mad rage disappointed prayer resentment bitter why god mad at god hate this',
19: 'cannot pray cant pray words prayer numb silence what say god no words exhausted prayer feels impossible',
20: 'betrayal relationship heartbreak people hurt me trust wound divorce divorced marriage marital spouse husband wife breakup rejected rejection affair cheating infidelity friendship church hurt abandonment',
21: 'forgive forgiveness unforgiveness apology no sorry bitterness revenge betrayal abuse resentment cannot forgive',
22: 'boundaries reconciliation trust forgive toxic unsafe abuse apology repentance access contact relationship protect myself manipulation',
23: 'church hurt hypocrisy abuse legalism deconstruction leaving faith reject christianity pastor hurt spiritual abuse religion',
24: 'doubt assurance salvation unbelief questions faith weak believer deconstruction am i saved losing faith doubt god'
}

STOPWORDS = "i im ive id me my mine myself we our you your the a an and or but is are was were be been being to of for in on at with from this that it its do does did have has had feel feels feeling just really very so still am can could would should there here about like what why how when where who not".split()

CARE_CSS = f'''{CARE_CSS_START}
.careChoice{{padding:46px 0 50px;background:#eef2ed;border-top:1px solid #dde5dc;border-bottom:1px solid #d7dfd6}}
.careChoiceHead{{text-align:center;max-width:760px;margin:0 auto 24px}}
.careChoiceHead h2{{font:2.5rem/1.08 Georgia,"Times New Roman",serif;font-weight:400;color:#183024;margin:0 0 9px}}
.careChoiceHead p{{margin:0;color:#5f6862;font-size:.9rem}}
.careChoiceGrid{{display:grid;grid-template-columns:1fr 1fr;gap:14px;max-width:900px;margin:auto}}
.careChoiceCard{{display:block;text-decoration:none;background:#fff;border:1px solid #d9d4ca;padding:25px 27px;transition:.2s ease}}
.careChoiceCard:hover{{transform:translateY(-2px);box-shadow:0 12px 28px rgba(30,44,35,.08)}}
.careChoiceCard small{{display:block;color:#8b6939;text-transform:uppercase;letter-spacing:.13em;font-size:.65rem;font-weight:800;margin-bottom:7px}}
.careChoiceCard strong{{display:block;font:1.65rem/1.12 Georgia,"Times New Roman",serif;font-weight:400;color:#183024;margin-bottom:7px}}
.careChoiceCard span{{display:block;color:#657068;font-size:.84rem;line-height:1.55}}
.careSafety{{text-align:center;margin-top:18px;font-size:.74rem;color:#59645d}}
.careSafety a{{font-weight:800;color:#294533;text-decoration:none}}
.audioNote{{margin:0 0 28px;padding:20px 22px;border:1px solid #ddd6c9;background:#f6f1e8}}
.audioNote strong{{display:block;font:1.25rem/1.2 Georgia,"Times New Roman",serif;color:#20372a;margin-bottom:8px}}
.audioNote audio{{width:100%;display:block}}
.answerSafety{{margin:28px 0 0;padding:16px 18px;background:#f8f5ef;border:1px solid #e3ddd2;font-size:.78rem;color:#5d665f}}
.answerSafety a{{font-weight:800;color:#294533;text-decoration:none}}
@media(max-width:760px){{.careChoiceGrid{{grid-template-columns:1fr}}.careChoice{{padding:38px 0 42px}}.careChoiceHead h2{{font-size:2.1rem}}}}
{CARE_CSS_END}'''

CARE_HOME = f'''{CARE_HOME_START}<section class="careChoice"><div class="wrap"><div class="careChoiceHead"><p class="eyebrow">Choose where to begin</p><h2>Are you hurting—or trying to help someone who is?</h2><p>You do not have to know the right question yet. Choose the path that is closest to why you came.</p></div><div class="careChoiceGrid"><a class="careChoiceCard" href="/what-hurts-today"><small>I’m hurting</small><strong>Help me find the question underneath the pain.</strong><span>Search grief, depression, anger, doubt, betrayal, unanswered prayer, loneliness, and more in your own words.</span></a><a class="careChoiceCard" href="/help-someone"><small>Someone I love is hurting</small><strong>Help me know what to say—and what not to say.</strong><span>A practical pastoral guide for showing up, listening well, and helping without trying to explain away someone else’s pain.</span></a></div><div class="careSafety">If the hurt has become dangerous or you do not feel safe, <a href="/unsafe">start here right now →</a></div></div></section>{CARE_HOME_END}'''

HELP_SOMEONE_HTML = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#294533"><title>When Someone You Love Is Hurting | What to Say and What Not to Say</title><meta name="description" content="A practical pastoral guide from Pastor Tate for helping someone who is grieving, suffering, depressed, angry, confused, or heartbroken."><link rel="canonical" href="https://answersforabrokenheart.com/help-someone"><style>:root{--deep:#183024;--green:#294533;--cream:#f6f1e8;--paper:#fffdf9;--ink:#24312b;--muted:#667068;--gold:#b69258;--line:#ddd6c9}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:Arial,Helvetica,sans-serif;line-height:1.72}a{color:inherit}.wrap{width:min(860px,calc(100% - 40px));margin:auto}header{background:var(--deep);color:#fff;padding:21px 0}.brand{color:#fff;text-decoration:none;font:1.42rem/.88 Georgia,serif}.brand small{display:block;font-size:.72rem;color:rgba(255,255,255,.72)}.hero{padding:66px 0 58px;background:linear-gradient(120deg,#f7f2e9,#edf1eb)}.eyebrow{text-transform:uppercase;letter-spacing:.17em;font-size:.69rem;color:#88683b;font-weight:800;margin:0 0 12px}h1,h2,h3{font-family:Georgia,"Times New Roman",serif;font-weight:400;letter-spacing:-.025em}h1{font-size:clamp(3rem,7vw,5.35rem);line-height:1.01;color:var(--deep);margin:0 0 18px}.lead{font:1.22rem/1.58 Georgia,serif;color:#4d5a52;max-width:780px;margin:0}.article{padding:52px 0 72px;font-size:1.02rem}.article p{margin:0 0 1.3em}.article h2{font-size:2.25rem;line-height:1.08;color:var(--deep);margin:46px 0 15px}.keyline{font:1.48rem/1.45 Georgia,serif;border-left:3px solid var(--gold);padding:8px 0 8px 21px;margin:30px 0;color:var(--deep)}.pairs{margin:28px 0}.pair{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:12px 0}.dont,.say{padding:21px;border:1px solid var(--line)}.dont{background:#faf4ee}.say{background:#eef3ee}.pair strong{display:block;text-transform:uppercase;letter-spacing:.1em;font-size:.68rem;color:#88683b;margin-bottom:7px}.pair p{margin:0;font-size:.91rem}.steps{counter-reset:care}.step{padding:24px 0;border-top:1px solid var(--line)}.step h3{font-size:1.55rem;color:var(--deep);margin:0 0 8px}.prayer{background:var(--cream);border-left:3px solid var(--gold);padding:24px 26px;font:1.04rem/1.65 Georgia,serif;margin:31px 0}.safety{background:#f4f0e8;border:1px solid var(--line);padding:24px 26px;margin-top:34px}.safety a{font-weight:800;color:var(--green)}.cta{background:var(--deep);color:white;padding:42px 0}.cta h2{color:white;font-size:2rem;margin:0 0 8px}.cta p{color:rgba(255,255,255,.8);margin:0 0 15px}.btn{display:inline-block;text-decoration:none;background:#d8bd87;color:var(--deep);padding:11px 15px;font-size:.74rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em;margin-right:7px}footer{background:#10251b;color:rgba(255,255,255,.72);padding:24px 0;font-size:.75rem}@media(max-width:700px){.pair{grid-template-columns:1fr}.hero{padding:52px 0 46px}}</style><script>window.va=window.va||function(){(window.vaq=window.vaq||[]).push(arguments)};</script><script defer src="/_vercel/insights/script.js"></script></head><body><header><div class="wrap"><a class="brand" href="/">Answers<small>for a Broken Heart</small></a></div></header><section class="hero"><div class="wrap"><p class="eyebrow">A guide from Pastor Tate</p><h1>When Someone You Love Is Hurting</h1><p class="lead">What not to say, what to say instead, and how to be present when you cannot fix what happened.</p></div></section><main class="article"><div class="wrap"><p>When someone you love is hurting, the pressure to say the right thing can make you talk too much. We reach for explanations because silence feels awkward. We offer advice because helplessness feels uncomfortable. We try to make the pain smaller because we desperately want the person we love to hurt less.</p><p>But hurting people usually do not need you to solve the mystery of their suffering. They need to know they will not have to carry it alone.</p><p class="keyline">Presence is often more helpful than explanation.</p><h2>Five things not to say—and what to say instead.</h2><div class="pairs"><div class="pair"><div class="dont"><strong>Try not to say</strong><p>“Everything happens for a reason.”</p></div><div class="say"><strong>Say instead</strong><p>“I do not know why this happened. I am so sorry. I am here with you.”</p></div></div><div class="pair"><div class="dont"><strong>Try not to say</strong><p>“At least…” followed by anything that makes the loss sound smaller.</p></div><div class="say"><strong>Say instead</strong><p>“This hurts. You do not have to make it sound better for me.”</p></div></div><div class="pair"><div class="dont"><strong>Try not to say</strong><p>“God will not give you more than you can handle.”</p></div><div class="say"><strong>Say instead</strong><p>“You do not have to carry all of this by yourself. How can I help carry something today?”</p></div></div><div class="pair"><div class="dont"><strong>Try not to say</strong><p>“You just need more faith.”</p></div><div class="say"><strong>Say instead</strong><p>“You do not have to be strong with me. I can sit with you while this is hard.”</p></div></div><div class="pair"><div class="dont"><strong>Try not to say</strong><p>“Let me know if you need anything.”</p></div><div class="say"><strong>Say instead</strong><p>“I can bring dinner Tuesday, sit with you Thursday, or make that phone call with you. Which would help most?”</p></div></div></div><h2>What helpful love looks like.</h2><div class="steps"><div class="step"><h3>1. Show up without demanding a conversation.</h3><p>A text that says, “You do not need to reply. I just wanted you to know I am thinking about you,” can be a gift. Presence does not always need words.</p></div><div class="step"><h3>2. Listen longer than feels natural.</h3><p>Do not rush to correct every theological sentence spoken through tears. Pain often speaks before theology catches up. Listen for the hurt underneath the words.</p></div><div class="step"><h3>3. Let them say the name and tell the story.</h3><p>When grief is involved, do not be afraid to mention the person who died. Remembering them usually does not create the pain; the pain is already there. Your willingness to remember tells the grieving person that their loved one has not disappeared from everyone else's world.</p></div><div class="step"><h3>4. Offer specific practical help.</h3><p>Bring food. Take the kids somewhere. Sit in a waiting room. Mow the yard. Drive them to an appointment. Make one hard phone call with them. Pain drains decision-making energy, so specific offers are often kinder than open-ended ones.</p></div><div class="step"><h3>5. Stay after everybody else goes home.</h3><p>The first week often brings messages, flowers, meals, and attention. The sixth week can feel very quiet. Put a reminder on your calendar to check in again after the funeral, after the diagnosis becomes old news, after the crisis has moved off everyone else's radar.</p></div></div><p class="keyline">You do not need a perfect answer to be a faithful friend.</p><h2>A prayer for the person trying to help.</h2><div class="prayer">“Father, help me love without trying to control the outcome. Give me wisdom to know when to speak and when to listen. Keep me from reaching for easy answers simply because their pain makes me uncomfortable. Help me show up with the patience, truth, and compassion of Christ. Amen.”</div><div class="safety"><strong>If you are worried they may not be safe:</strong> do not leave them alone with that concern or treat it as something you must manage privately. Ask directly whether they feel safe, stay physically near them when possible, involve another trusted person, and connect them with immediate crisis or emergency support. <a href="/unsafe">Use the safety pathway →</a></div></div></main><section class="cta"><div class="wrap"><h2>Not sure which question they are carrying?</h2><p>Browse the 24 answers and send them the one that sounds closest to what they are actually asking.</p><a class="btn" href="/what-hurts-today">Browse What Hurts Today?</a><a class="btn" href="/free-guides">Free Guides</a></div></section><footer><div class="wrap">Answers for a Broken Heart · Pastor Tate Throndson · Psalm 34:18</div></footer></body></html>'''

UNSAFE_HTML = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#294533"><title>If You Feel Unsafe Right Now | Answers for a Broken Heart</title><meta name="description" content="A simple immediate safety pathway for someone in emotional crisis or who is afraid they may hurt themselves."><meta name="robots" content="noindex,follow"><style>:root{--deep:#183024;--green:#294533;--cream:#f6f1e8;--paper:#fffdf9;--ink:#24312b;--muted:#667068;--gold:#b69258;--line:#ddd6c9}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:Arial,Helvetica,sans-serif;line-height:1.7}.wrap{width:min(760px,calc(100% - 38px));margin:auto}header{background:var(--deep);color:#fff;padding:21px 0}.brand{color:#fff;text-decoration:none;font:1.38rem/.9 Georgia,serif}.brand small{display:block;font-size:.72rem;color:rgba(255,255,255,.72)}.hero{padding:64px 0 50px;background:#eef2ed}.eyebrow{text-transform:uppercase;letter-spacing:.17em;font-size:.69rem;color:#88683b;font-weight:800;margin:0 0 12px}h1,h2{font-family:Georgia,"Times New Roman",serif;font-weight:400;letter-spacing:-.025em}h1{font-size:clamp(3rem,7vw,5rem);line-height:1.01;color:var(--deep);margin:0 0 16px}.lead{font:1.2rem/1.58 Georgia,serif;color:#4d5a52;margin:0}.main{padding:44px 0 64px}.first{background:var(--deep);color:white;padding:27px 29px;margin-bottom:28px}.first h2{color:white;margin:0 0 8px;font-size:2rem}.first p{margin:0;color:rgba(255,255,255,.86)}.step{padding:23px 0;border-bottom:1px solid var(--line)}.step h2{font-size:1.8rem;color:var(--deep);margin:0 0 8px}.step p{margin:0}.callout{background:var(--cream);border-left:4px solid var(--gold);padding:24px 26px;margin-top:30px}.buttons{display:flex;gap:9px;flex-wrap:wrap;margin-top:16px}.btn{display:inline-block;text-decoration:none;background:var(--green);color:#fff;padding:12px 16px;font-size:.75rem;text-transform:uppercase;letter-spacing:.05em;font-weight:800}.btn.light{background:#d8bd87;color:var(--deep)}.note{margin-top:28px;color:var(--muted);font-size:.82rem}footer{background:#10251b;color:rgba(255,255,255,.7);padding:24px 0;font-size:.75rem}</style><script>window.va=window.va||function(){(window.vaq=window.vaq||[]).push(arguments)};</script><script defer src="/_vercel/insights/script.js"></script></head><body><header><div class="wrap"><a class="brand" href="/">Answers<small>for a Broken Heart</small></a></div></header><section class="hero"><div class="wrap"><p class="eyebrow">If the hurt has become dangerous</p><h1>If you feel unsafe right now</h1><p class="lead">You do not need to solve your life tonight. The goal for this moment is simpler: stay alive, get near another person, and let someone help carry the next hour with you.</p></div></section><main class="main"><div class="wrap"><div class="first"><h2>Do not stay alone with this.</h2><p>Move toward another person now—a spouse, parent, friend, pastor, neighbor, coworker, emergency department, or another safe public place. Tell someone plainly: “I do not feel safe being alone right now.”</p></div><div class="step"><h2>1. Put distance between you and anything you could use to hurt yourself.</h2><p>Move away from it or ask another person to secure it for you. Make the next few minutes safer while help is being connected.</p></div><div class="step"><h2>2. Tell one real person exactly what is happening.</h2><p>You do not need a polished explanation. Use direct words: “I am afraid I might hurt myself,” or “I do not trust myself to be alone right now.”</p></div><div class="step"><h2>3. Connect with immediate crisis support.</h2><p>In the United States and its territories, the 988 Suicide &amp; Crisis Lifeline is available by call, text, or online chat. You do not have to wait until things get worse to use it.</p><div class="buttons"><a class="btn" href="tel:988">Call 988</a><a class="btn" href="sms:988">Text 988</a><a class="btn light" href="https://988lifeline.org/chat/">Chat with 988</a></div></div><div class="step"><h2>4. If there is immediate danger or a medical emergency, call emergency services now.</h2><p>In the United States, call 911 or go to the nearest emergency department. If you are outside the United States, contact your local emergency service or crisis line.</p></div><div class="callout"><strong>For the person helping:</strong> stay with them when you can, take statements about self-harm seriously, and bring in additional help rather than trying to carry the situation by yourself.</div><p class="note">This page is for immediate support and does not replace professional medical or mental-health care. Once the immediate danger has passed, continue with qualified professional and pastoral support rather than treating the crisis as finished simply because the worst moment eased.</p></div></main><footer><div class="wrap">Answers for a Broken Heart · A simple path toward the next safe step</div></footer></body></html>'''

def patch_index(path):
    text = path.read_text()
    text = re.sub(re.escape(CARE_CSS_START) + r'.*?' + re.escape(CARE_CSS_END) + r'\s*', '', text, flags=re.S)
    text = re.sub(re.escape(CARE_HOME_START) + r'.*?' + re.escape(CARE_HOME_END), '', text, flags=re.S)
    text = text.replace('</style>', CARE_CSS + '\n</style>', 1)

    # Replace the older one-path Start Here strip with a two-path choice.
    text = re.sub(r'<!-- START-HERE-CTA-START -->.*?<!-- START-HERE-CTA-END -->', CARE_HOME, text, count=1, flags=re.S)
    if CARE_HOME_START not in text:
        # Fallback: put the choice before the What Hurts section.
        marker = '<section class="section hurts">'
        if marker in text:
            text = text.replace(marker, CARE_HOME + marker, 1)
        else:
            raise RuntimeError('Could not place homepage care pathway')

    # Static care pages must bypass the homepage SPA router.
    if '!href.startsWith("/help-someone")' not in text:
        text = text.replace('&&!href.startsWith("/2am-guide")){', '&&!href.startsWith("/2am-guide")&&!href.startsWith("/help-someone")&&!href.startsWith("/unsafe")){', 1)
    path.write_text(text)

def patch_search(path):
    text = path.read_text()
    # Replace tags with a richer emotional vocabulary.
    text = re.sub(r' data-search="[^"]*"', '', text)
    for n, keywords in SEARCH_TAGS.items():
        num = f'{n:02d}'
        pattern = rf'(<a class="card" href="/answer-{num}" data-category="[^"]+")'
        text, count = re.subn(pattern, lambda m, kw=keywords: m.group(1) + f' data-search="{html.escape(kw, quote=True)}"', text, count=1)
        if count != 1:
            raise RuntimeError(f'Could not enrich answer {num} search tags')

    text = text.replace('placeholder="Use your own words — depressed, lonely, angry, divorce, doubt, can’t sleep…"', 'placeholder="Use your own words — I feel numb, my marriage is over, I can’t sleep, I’m mad at God…"', 1)

    # Add a gentle immediate-safety result beneath the search tools.
    text = re.sub(re.escape(SAFETY_SEARCH_START) + r'.*?' + re.escape(SAFETY_SEARCH_END), '', text, flags=re.S)
    tools_end = '</section>\n<section class="library">'
    safety = f'''{SAFETY_SEARCH_START}<div id="safetySearch" style="display:none;background:#183024;color:#fff;padding:15px 0"><div class="wrap" style="display:flex;justify-content:space-between;gap:18px;align-items:center;flex-wrap:wrap"><div><strong>If you feel unsafe right now, you do not have to search for the perfect article.</strong><div style="font-size:.78rem;color:rgba(255,255,255,.76)">Start with the next safe step and another person.</div></div><a href="/unsafe" style="color:#183024;background:#d8bd87;text-decoration:none;padding:9px 13px;font-size:.72rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em">Use the safety pathway →</a></div></div>{SAFETY_SEARCH_END}'''
    if tools_end in text:
        text = text.replace(tools_end, '</section>\n' + safety + '\n<section class="library">', 1)

    old_draw = "function draw(){const term=search.value.trim().toLowerCase();let shown=0;cards.forEach(card=>{const category=card.dataset.category;const matchCat=active==='all'||category===active;const haystack=(card.textContent+' '+(card.dataset.search||'')).toLowerCase();const matchText=!term||haystack.includes(term);const show=matchCat&&matchText;card.style.display=show?'block':'none';if(show)shown++});groups.forEach(group=>{const visible=[...group.querySelectorAll('.card')].some(c=>c.style.display!=='none');group.style.display=visible?'block':'none'});empty.style.display=shown?'none':'block'}"
    stopwords = ' '.join(STOPWORDS)
    new_draw = "const stop=new Set('" + stopwords + "'.split(' '));function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').replace(/[’']/g,'').replace(/[^a-z0-9\\s]/g,' ').replace(/\\s+/g,' ').trim()}function terms(s){return norm(s).split(' ').filter(w=>w.length>1&&!stop.has(w))}function draw(){const raw=search.value.trim();const q=terms(raw);const normalized=norm(raw);const danger=/\\b(suicide|suicidal|self harm|selfharm|kill myself|hurt myself|end my life|dont want to live|not safe|unsafe)\\b/.test(normalized);const safety=document.getElementById('safetySearch');if(safety)safety.style.display=danger?'block':'none';let shown=0;cards.forEach(card=>{const category=card.dataset.category;const matchCat=active==='all'||category===active;const haystack=norm(card.textContent+' '+(card.dataset.search||''));const matchText=!raw||(q.length?q.every(t=>haystack.includes(t)):haystack.includes(normalized));const show=matchCat&&matchText;card.style.display=show?'block':'none';if(show)shown++});groups.forEach(group=>{const visible=[...group.querySelectorAll('.card')].some(c=>c.style.display!=='none');group.style.display=visible?'block':'none'});empty.style.display=shown?'none':'block'}"
    if old_draw in text:
        text = text.replace(old_draw, new_draw, 1)
    elif 'function terms(s)' not in text:
        raise RuntimeError('Could not install sentence-friendly emotional search')
    path.write_text(text)

def patch_free_guides(path):
    text = path.read_text()
    if '/help-someone' not in text:
        card = '<a class="card" href="/help-someone"><span class="cardTag">For Friends · Family · Pastors</span><h3>When Someone You Love Is Hurting</h3><p>What not to say, what to say instead, and five practical ways to show up when you cannot fix what happened.</p><span class="cardLink">Read the free guide →</span></a>'
        text = text.replace('</div><div class="series">', card + '</div><div class="series">', 1)
    text = text.replace('.grid{display:grid;grid-template-columns:1fr 1fr;gap:18px}', '.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}')
    text = text.replace('@media(max-width:760px){.navlinks{display:none}.grid,.signupGrid{grid-template-columns:1fr}', '@media(max-width:900px){.grid{grid-template-columns:1fr 1fr}}@media(max-width:760px){.navlinks{display:none}.grid,.signupGrid{grid-template-columns:1fr}')
    path.write_text(text)

def patch_answer(path, n):
    text = path.read_text()
    text = re.sub(re.escape(SAFETY_LINK_START) + r'.*?' + re.escape(SAFETY_LINK_END), '', text, flags=re.S)
    text = re.sub(re.escape(AUDIO_START) + r'.*?' + re.escape(AUDIO_END), '', text, flags=re.S)

    # Discreet safety path after the 60-second section.
    safety = f'''{SAFETY_LINK_START}<div class="answerSafety">If your pain has become dangerous or you are afraid you may hurt yourself, do not carry that moment alone. <a href="/unsafe">Use the immediate safety pathway →</a></div>{SAFETY_LINK_END}'''
    marker = '<!-- HURTING-HELP-END -->'
    if marker in text:
        text = text.replace(marker, marker + safety, 1)

    # Voice-ready architecture: an actual player appears only when Pastor Tate's real recording exists.
    audio_path = Path(f'audio/answer-{n:02d}.mp3')
    if audio_path.exists():
        audio = f'''{AUDIO_START}<section class="audioNote"><strong>Listen to Pastor Tate — about 2 minutes</strong><audio controls preload="none" src="/audio/answer-{n:02d}.mp3">Your browser does not support audio playback.</audio></section>{AUDIO_END}'''
        if '<section class="short" id="short">' in text:
            text = text.replace('<section class="short" id="short">', audio + '<section class="short" id="short">', 1)
    else:
        # Invisible slot documents exactly what file activates this feature later.
        slot = f'{AUDIO_START}<!-- Add /audio/answer-{n:02d}.mp3 to activate “Listen to Pastor Tate — about 2 minutes” on this page. -->{AUDIO_END}'
        if '<section class="short" id="short">' in text:
            text = text.replace('<section class="short" id="short">', slot + '<section class="short" id="short">', 1)
    path.write_text(text)

def patch_sitemap(path):
    text = path.read_text()
    for url in ['https://answersforabrokenheart.com/help-someone']:
        if url not in text and '</urlset>' in text:
            text = text.replace('</urlset>', f'<url><loc>{url}</loc></url></urlset>', 1)
    path.write_text(text)

Path('help-someone.html').write_text(HELP_SOMEONE_HTML)
Path('unsafe.html').write_text(UNSAFE_HTML)
patch_index(Path('index.html'))
patch_search(Path('what-hurts-today.html'))
patch_free_guides(Path('free-guides.html'))
for n in range(1, 25):
    patch_answer(Path(f'answer-{n:02d}.html'), n)
patch_sitemap(Path('sitemap.xml'))
print('Care pathways current: sentence-friendly search, helper guide, safety path, homepage choices, and voice-ready audio slots.')
