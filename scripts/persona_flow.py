from pathlib import Path
import re

ROOT = Path('.')


def save(path: Path, text: str, original: str, label: str):
    if text != original:
        path.write_text(text, encoding='utf-8')
        print(f'{label}: {path.name}')


def inject_css(text: str, marker: str, css: str) -> str:
    if marker in text or '</head>' not in text:
        return text
    return text.replace('</head>', css + '\n</head>', 1)


# ---------------------------------------------------------------------------
# PERSONA 1 — A grieving visitor arriving through the homepage.
# Keep the guided path consistent: "I'm hurting" should go to Start Here,
# not suddenly drop the reader into the full 24-answer library.
# ---------------------------------------------------------------------------
path = ROOT / 'index.html'
if path.exists():
    text = path.read_text(encoding='utf-8')
    original = text

    text = text.replace(
        '<a class="careChoiceCard" href="/all-answers"><small>I’m hurting</small><strong>Help me find the question underneath the pain.</strong><span>Search grief, depression, anger, doubt, betrayal, unanswered prayer, loneliness, and more in your own words.</span></a>',
        '<a class="careChoiceCard" href="/start-here"><small>I’m hurting</small><strong>Help me name what hurts and find one place to begin.</strong><span>Choose the sentence closest to what you are carrying, then follow one clear path instead of sorting through everything at once.</span></a>',
    )

    # A person who chooses the middle-of-the-night resource from the homepage
    # should reach help immediately, not another gate.
    home_guides = re.search(r'<!-- FREE-GUIDES-HOME-START -->(.*?)<!-- FREE-GUIDES-HOME-END -->', text, re.S)
    if home_guides:
        block = home_guides.group(1)
        block = block.replace(
            '<a class="guideCard featured" href="/2am-guide"><small>Best place to start tonight · 7 Scriptures</small>',
            '<a class="guideCard featured" href="/2am-guide-access"><small>Best place to start tonight · 7 Scriptures</small>',
            1,
        )
        block = block.replace('<b>Get the free guide →</b>', '<b>Open the guide now →</b>', 1)
        block = block.replace(
            '<h3>Get the free 2:00 A.M. Guide.</h3><p>Seven Scriptures, short pastoral reminders, and simple prayers for the nights when your thoughts are loud and you do not know what else to do. I’ll also send occasional pastoral notes and let you know when <em>Answers for a Broken Heart</em> is ready.</p>',
            '<h3>Want occasional pastoral encouragement like this?</h3><p>The 2:00 A.M. Guide is already free to open—no email required. If you would like occasional pastoral notes, new resources, and book-release updates, you can leave your email here.</p>',
            1,
        )
        block = block.replace('<button type="submit">Send Me the Free Guide</button>', '<button type="submit">Keep Me Encouraged</button>', 1)
        block = block.replace(
            '<div class="homeNotePrivacy">You’ll go straight to the guide after signing up. No daily emails—just occasional pastoral encouragement and book-release updates.</div>',
            '<div class="homeNotePrivacy">Optional. No daily emails—just occasional pastoral encouragement, new resources, and book-release updates.</div>',
            1,
        )
        block = block.replace(
            'value="2:00 A.M. Guide + occasional pastoral notes + book release updates"',
            'value="Pastoral encouragement + new resources + book release updates"',
            1,
        )
        text = text[:home_guides.start(1)] + block + text[home_guides.end(1):]

    save(path, text, original, 'Aligned homepage help-first funnel')


# ---------------------------------------------------------------------------
# START HERE — six core hurt pathways, one quieter emotional-health option,
# and the hard-night resource in its own immediate-help band.
# ---------------------------------------------------------------------------
path = ROOT / 'start-here.html'
if path.exists():
    text = path.read_text(encoding='utf-8')
    original = text

    text = text.replace(
        '<small>I prayed and the answer was not what I wanted</small><h3>I’m angry, disappointed, or confused with God.</h3>',
        '<small>I prayed, waited, or watched something happen I cannot accept</small><h3>I’m angry, disappointed, or confused with God.</h3>',
        1,
    )

    # Any hard-night CTA on Start Here should open help immediately.
    text = text.replace('href="/2am-guide"', 'href="/2am-guide-access"')
    text = text.replace('>Give Me Something for Tonight</a>', '>Open the 2:00 A.M. Guide</a>', 1)

    if 'PERSONA-FLOW-START-SUPPORT' not in text:
        match = re.search(r'<div class="grid">\s*(.*?)\s*</div><div class="night">', text, re.S)
        if match:
            anchors = re.findall(r'<a class="choice"[^>]*>.*?</a>', match.group(1), re.S)
            primary = [a for a in anchors if '/can-christians-be-depressed' not in a and '/2am-guide' not in a and '/2am-guide-access' not in a]
            emotional = [a for a in anchors if '/can-christians-be-depressed' in a]
            if len(primary) == 6 and len(emotional) == 1:
                support_card = emotional[0].replace('class="choice"', 'class="choice choiceSupport"', 1)
                replacement = (
                    '<div class="grid">\n' + '\n'.join(primary) + '\n</div>'
                    '<!-- PERSONA-FLOW-START-SUPPORT -->'
                    '<section class="startSupport" aria-labelledby="start-support-heading">'
                    '<div class="startSupportCopy"><p class="eyebrow">If the category is not the main problem</p>'
                    '<h2 id="start-support-heading">Maybe you simply feel low, numb, or worn down.</h2>'
                    '<p>You do not have to force what you are feeling into grief, doubt, anger, or another category. Start with the emotional weight itself.</p></div>'
                    '<div class="supportGrid">' + support_card + '</div>'
                    '</section><!-- PERSONA-FLOW-START-SUPPORT-END -->'
                    '<div class="night">'
                )
                text = text[:match.start()] + replacement + text[match.end():]

    start_css = '''<!-- PERSONA-FLOW-CSS-START --><style>
body.page-start-here .startSupport{margin:30px 0 0;padding:27px 29px;background:#eef2ed;border:1px solid #d9e0d8;display:grid;grid-template-columns:1fr minmax(320px,.85fr);gap:28px;align-items:center}
body.page-start-here .startSupportCopy h2{font:400 1.85rem/1.1 Georgia,"Times New Roman",serif;color:#183024;margin:0 0 9px}
body.page-start-here .startSupportCopy p:last-child{margin:0;color:#5f6862;font-size:.86rem;line-height:1.58}
body.page-start-here .supportGrid{display:block}
body.page-start-here .choiceSupport{min-height:0!important;background:#fff!important;padding:21px 22px!important}
body.page-start-here .choiceSupport h3{font-size:1.42rem!important}
body.page-start-here .night{margin-top:18px!important}
@media(max-width:800px){body.page-start-here .startSupport{grid-template-columns:1fr;padding:24px 22px}}
</style><!-- PERSONA-FLOW-CSS-END -->'''
    text = inject_css(text, 'PERSONA-FLOW-CSS-START', start_css)
    save(path, text, original, 'Reduced Start Here decision load')


# ---------------------------------------------------------------------------
# PERSONA 2 — Someone who is angry with God.
# Name the emotion immediately and put the most emotionally direct questions
# before the more situational ones.
# ---------------------------------------------------------------------------
path = ROOT / 'anger-and-unanswered-prayer.html'
if path.exists():
    text = path.read_text(encoding='utf-8')
    original = text
    text = text.replace(
        '<p class="eyebrow">For prayers that felt unheard and anger you are afraid to admit</p><h1>What do you do with anger when the prayer was not answered?</h1><p class="lead">You may still love God and be furious about what He allowed. Scripture makes room for prayers that are confused, disappointed, blunt, and painfully honest.</p>',
        '<p class="eyebrow">For prayers that felt unheard, injustice that feels unanswered, and anger you are afraid to admit</p><h1>What do you do when you’re angry with God?</h1><p class="lead">Maybe He said no. Maybe He seemed silent. Maybe He allowed something you cannot make sense of. You do not have to hide the anger before you bring it to Him.</p>',
        1,
    )
    text = text.replace('Anger at God is not the opposite of faith. →', 'You are allowed to tell God you are angry. →')

    grid = re.search(r'<div class="answerGrid">(.*?)</div>', text, re.S)
    if grid:
        cards = re.findall(r'<a class="answerCard"[^>]*>.*?</a>', grid.group(1), re.S)
        by_href = {}
        for card in cards:
            href = re.search(r'href="([^"]+)"', card)
            if href:
                by_href[href.group(1)] = card
        order = ['/answer-18', '/answer-19', '/answer-13', '/answer-11']
        if all(h in by_href for h in order):
            new_grid = '<div class="answerGrid">' + ''.join(by_href[h] for h in order) + '</div>'
            text = text[:grid.start()] + new_grid + text[grid.end():]

    save(path, text, original, 'Made anger pathway emotionally direct')


path = ROOT / 'answer-18.html'
if path.exists():
    text = path.read_text(encoding='utf-8')
    original = text
    text = text.replace('<h2>Anger at God is not the opposite of faith.</h2>', '<h2>You are allowed to tell God you are angry.</h2>', 1)
    text = text.replace(
        '<p>Scripture contains prayers, laments, accusations, and cries from people who were deeply angry with God. Honest anger brought to Him is not the same as rejecting Him. In many cases, the very fact that you are still arguing with God means you still believe He is there and that what happened matters to Him.</p>',
        '<p>That does not make every angry thought right, but anger is not automatic proof that faith is gone. Scripture contains prayers, laments, accusations, and cries from people who were deeply angry with God. Honest anger brought to Him is not the same as rejecting Him. God may correct what is wrong in us, but He does not require fake calm before we come. In many cases, the fact that you are still arguing with God means you still believe He is there and that what happened matters to Him.</p>',
        1,
    )
    save(path, text, original, 'Strengthened anger Answer opening')


# ---------------------------------------------------------------------------
# PERSONA 3 — A Google visitor at 1:00 a.m.
# Remove the email gate from the hard-night resource. Help comes first;
# email becomes an optional relationship/conversion step after value.
# ---------------------------------------------------------------------------
path = ROOT / '2am-guide.html'
if path.exists():
    text = path.read_text(encoding='utf-8')
    original = text

    text = text.replace(
        '<h2>Send me the 2:00 A.M. Guide.</h2><p>Enter your email and you’ll go straight to the guide. I’ll also send occasional pastoral encouragement and let you know when <em>Answers for a Broken Heart</em> is ready.</p>',
        '<h2>Open the guide now.</h2><p>No email is required to get help tonight. The guide is available immediately. If you would also like occasional pastoral encouragement, new resources, and book updates, the email form below is optional.</p><a class="openNow" href="/2am-guide-access">Open the 2:00 A.M. Guide</a><div class="orLine">Optional: stay connected after tonight</div>',
        1,
    )
    text = text.replace('<button type="submit">Send Me the Free Guide</button>', '<button type="submit">Keep Me Encouraged</button>', 1)
    text = text.replace(
        '<div class="privacy">No daily emails. Just occasional pastoral encouragement, new resources, and book-release updates.</div>',
        '<div class="privacy">Optional. No daily emails—just occasional pastoral encouragement, new resources, and book-release updates.</div>',
        1,
    )
    text = text.replace(
        'value="2:00 A.M. Guide + occasional pastoral notes + book release updates"',
        'value="Pastoral encouragement + new resources + book release updates"',
        1,
    )
    text = re.sub(r'<div class="returning" id="returning">.*?</div>', '', text, count=1, flags=re.S)
    text = re.sub(r'<script>try\{if\(localStorage\.getItem\(\'afabh_2am_access\'\).*?</script>', '', text, count=1, flags=re.S)

    if 'PERSONA-FLOW-URGENT-HELP' not in text:
        form_start = text.find('<form data-email-segment="guide_2am" class="form"')
        if form_start >= 0:
            form_end = text.find('</form>', form_start)
            if form_end >= 0:
                insert_at = form_end + len('</form>')
                urgent = '<!-- PERSONA-FLOW-URGENT-HELP --><div class="urgentHelp">If you are afraid you may hurt yourself or you do not feel safe, <a href="/unsafe">use the immediate safety pathway →</a></div><!-- PERSONA-FLOW-URGENT-HELP-END -->'
                text = text[:insert_at] + urgent + text[insert_at:]

    guide_css = '''<!-- PERSONA-FLOW-2AM-CSS-START --><style>
body.page-2am-guide .openNow{display:block;text-align:center;text-decoration:none;background:#183024;color:#fff;padding:14px 16px;margin:4px 0 15px;font-size:.73rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em}
body.page-2am-guide .orLine{text-align:center;font-size:.66rem;letter-spacing:.11em;text-transform:uppercase;color:#7a746d;margin:0 0 12px}
body.page-2am-guide .urgentHelp{margin-top:16px;padding-top:14px;border-top:1px solid #ded8cd;font-size:.72rem;line-height:1.5;color:#686f6a}
body.page-2am-guide .urgentHelp a{font-weight:800;color:#294533;text-decoration:none}
</style><!-- PERSONA-FLOW-2AM-CSS-END -->'''
    text = inject_css(text, 'PERSONA-FLOW-2AM-CSS-START', guide_css)
    save(path, text, original, 'Removed hard-night email gate')


path = ROOT / '2am-guide-access.html'
if path.exists():
    text = path.read_text(encoding='utf-8')
    original = text

    # Remove the localStorage redirect gate entirely.
    text = re.sub(
        r"<script>\s*\(function\(\)\{\s*try\{\s*var key='afabh_2am_access';.*?</script>\s*",
        '',
        text,
        count=1,
        flags=re.S,
    )

    if 'PERSONA-FLOW-NIGHT-SAFETY' not in text:
        text = text.replace(
            '</section><main class="guide">',
            '</section><!-- PERSONA-FLOW-NIGHT-SAFETY --><section class="nightSafety"><div class="wrap">If you are afraid you may hurt yourself or you do not feel safe, <a href="/unsafe">use the immediate safety pathway →</a></div></section><!-- PERSONA-FLOW-NIGHT-SAFETY-END --><main class="guide">',
            1,
        )

    if 'PERSONA-FLOW-KEEP-IN-TOUCH' not in text:
        keep = '''<!-- PERSONA-FLOW-KEEP-IN-TOUCH -->
<section class="keepGuide" id="keep-guide"><div class="wrap keepGuideGrid"><div><p class="eyebrow">After tonight</p><h2>Want occasional pastoral encouragement like this?</h2><p>You already have full access to the guide. If you would like occasional pastoral notes, new resources, and book-release updates, you can leave your email here.</p><div class="keepThanks" id="keepThanks" hidden>Thank you. You can keep using the guide right here.</div></div><form data-email-segment="pastoral_notes" class="keepForm" action="https://formsubmit.co/tatethrondson@gmail.com" method="POST"><input type="email" name="email" placeholder="Your email address" aria-label="Your email address" autocomplete="email" required><input type="text" name="_honey" class="keepHoney" tabindex="-1" autocomplete="off"><input type="hidden" name="_subject" value="New pastoral encouragement signup from 2:00 A.M. Guide"><input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="_next" value="https://answersforabrokenheart.com/2am-guide-access?sent=1#keep-guide"><input type="hidden" name="interest" value="Pastoral encouragement + new resources + book release updates"><input type="hidden" name="source" value="2:00 A.M. Guide access page"><input type="hidden" name="segment" value="pastoral_notes"><button type="submit">Keep Me Encouraged</button><div class="keepPrivacy">Optional. No daily emails—just occasional pastoral encouragement, new resources, and book updates.</div></form></div></section>
<script>(function(){try{var p=new URLSearchParams(window.location.search);if(p.get('sent')==='1'){var el=document.getElementById('keepThanks');if(el)el.hidden=false;}}catch(e){}})();</script>
<!-- PERSONA-FLOW-KEEP-IN-TOUCH-END -->'''
        text = text.replace('</main><section class="closing">', '</main>' + keep + '<section class="closing">', 1)

    text = text.replace(
        '<a class="btn" href="/all-answers">Browse All 24 Answers</a><a class="btn" href="/book">About the Book</a>',
        '<a class="btn" href="/start-here">Tell Me Where It Hurts</a><a class="btn" href="/all-answers">Browse All 24 Answers</a>',
        1,
    )

    access_css = '''<!-- PERSONA-FLOW-ACCESS-CSS-START --><style>
body.page-2am-guide-access .nightSafety{padding:13px 0;background:#f5f0e7;border-top:1px solid #ded8cd;border-bottom:1px solid #ded8cd;font-size:.75rem;color:#5f6862}
body.page-2am-guide-access .nightSafety a{font-weight:800;color:#294533;text-decoration:none}
body.page-2am-guide-access .keepGuide{padding:42px 0;background:#eef2ed;border-top:1px solid #d9e0d8}
body.page-2am-guide-access .keepGuideGrid{display:grid;grid-template-columns:1.05fr .95fr;gap:34px;align-items:center}
body.page-2am-guide-access .keepGuide h2{font-size:2rem;line-height:1.08;margin:0 0 9px;color:#183024}
body.page-2am-guide-access .keepGuide p{margin:0;color:#5f6862;font-size:.87rem;line-height:1.6}
body.page-2am-guide-access .keepForm{display:grid;grid-template-columns:1fr 150px;gap:8px}
body.page-2am-guide-access .keepForm input[type="email"]{border:1px solid #d7d0c5;background:#fff;padding:13px 14px;min-height:47px;font-size:.86rem}
body.page-2am-guide-access .keepForm button{border:0;background:#294533;color:#fff;min-height:47px;padding:12px;font-size:.68rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em;cursor:pointer}
body.page-2am-guide-access .keepPrivacy{grid-column:1/-1;font-size:.64rem;color:#68716b}
body.page-2am-guide-access .keepHoney{position:absolute!important;left:-5000px!important;width:1px!important;height:1px!important;overflow:hidden!important}
body.page-2am-guide-access .keepThanks{margin-top:13px;color:#294533;font-weight:800;font-size:.82rem}
@media(max-width:720px){body.page-2am-guide-access .keepGuideGrid,body.page-2am-guide-access .keepForm{grid-template-columns:1fr}}
</style><!-- PERSONA-FLOW-ACCESS-CSS-END -->'''
    text = inject_css(text, 'PERSONA-FLOW-ACCESS-CSS-START', access_css)
    save(path, text, original, 'Made hard-night help immediate and conversion optional')


print('Persona conversion and emotional-flow pass complete.')
