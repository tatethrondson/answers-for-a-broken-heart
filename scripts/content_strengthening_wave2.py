from pathlib import Path
import json
import re

START = '<!-- CONTENT-STRENGTHENING-WAVE2-START -->'
END = '<!-- CONTENT-STRENGTHENING-WAVE2-END -->'
BASE = 'https://answersforabrokenheart.com'

STYLE = '''
<style>
.deepHelp2{padding:58px 0;background:#fff;border-top:1px solid #eee8df}.deepHelp2Inner{max-width:850px}.deepHelp2 h2{font:2.35rem/1.08 Georgia,"Times New Roman",serif;font-weight:400;color:#183024;margin:42px 0 14px}.deepHelp2 h2:first-of-type{margin-top:0}.deepHelp2 p{font-size:1rem;line-height:1.76;color:#364039;margin:0 0 1.22em}.deepHelp2 a{color:#294533;font-weight:800;text-underline-offset:2px}.deepScripture2{background:#f6f1e8;border-left:3px solid #ad823d;padding:20px 23px;margin:23px 0 28px;font:1.08rem/1.65 Georgia,"Times New Roman",serif;color:#20372a}.deepScripture2 small{display:block;margin-top:7px;font:700 .68rem/1.4 Arial,sans-serif;letter-spacing:.1em;text-transform:uppercase;color:#87683a}.scriptureList2{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:18px}.scriptureItem2{background:#f8f5ef;border:1px solid #ded8cd;padding:20px}.scriptureItem2 strong{display:block;font-size:.7rem;letter-spacing:.11em;text-transform:uppercase;color:#87683a;margin-bottom:7px}.scriptureItem2 p{font:1rem/1.55 Georgia,"Times New Roman",serif;color:#20372a;margin:0}.faq2{margin-top:18px;border-top:1px solid #ded8cd}.faq2Item{padding:22px 0;border-bottom:1px solid #ded8cd}.faq2Item strong{display:block;font:1.3rem/1.2 Georgia,"Times New Roman",serif;font-weight:400;color:#183024;margin-bottom:8px}.faq2Item p{margin:0}@media(max-width:760px){.scriptureList2{grid-template-columns:1fr}.deepHelp2 h2{font-size:2rem}}
</style>
'''

FAR = STYLE + '''
<section class="deepHelp2"><div class="wrap"><div class="deepHelp2Inner"><p class="eyebrow">Going deeper</p>
<h2>Why does God feel far away?</h2>
<p>Sometimes God feels distant because pain has made everything feel distant. Grief can numb us. Exhaustion can flatten our emotions. Fear can make the silence feel louder than the promises we once knew. The Bible does not pretend faithful people always feel God’s nearness. David asked, “How long wilt thou forget me, O LORD?” and yet he kept praying.</p>
<div class="deepScripture2">“How long wilt thou forget me, O LORD? for ever? how long wilt thou hide thy face from me?”<small>Psalm 13:1 · KJV</small></div>
<p>The presence of that prayer in Scripture matters. A believer can feel forgotten without actually being forgotten. If that is the question underneath your pain, begin with <a href="/answer-01">Has God really been here the whole time?</a></p>
<h2>Does God’s silence mean He is absent?</h2>
<p>No. Silence and absence are not the same thing. Scripture contains long stretches in which people could not see what God was doing until later. Joseph could not see the ending from the pit. The disciples could not see Easter from Friday. Some of God’s work is only recognizable after enough of the story has unfolded.</p>
<p>That does not mean every mystery will be explained in this life. It means your present inability to trace God is not evidence that He has stopped being present. <a href="/answer-03">Why can’t I see what God is doing right now?</a> explores that tension more fully.</p>
<h2>What if I cannot feel God at all?</h2>
<p>Do not make spiritual sensation the only measure of spiritual reality. Feelings matter, but they are not infallible. A person can feel unloved while being deeply loved. A person can feel alone while someone faithful is sitting beside them. In the same way, the inability to feel God’s nearness does not erase His promise to be near.</p>
<p>When your emotions are quiet, anchor yourself to what God has said. Pray honestly. Read a Psalm slowly. Let another Christian pray with you. Keep showing up before you feel like showing up. Faith sometimes holds onto truth while the heart catches up.</p>
<h2>Does Jesus understand what it feels like to suffer?</h2>
<p>Christianity answers this with Jesus Himself. He knew grief, rejection, betrayal, exhaustion, anguish, physical pain, and death. At Lazarus’s grave He wept. In Gethsemane He prayed in agony. At Calvary He entered suffering rather than explaining it from a safe distance.</p>
<p>That is why <a href="/answer-09">Does God actually know what this feels like?</a> and <a href="/answer-10">What did Jesus do about suffering?</a> belong in this conversation. God’s answer is not merely that He sees pain. In Christ, He stepped into it.</p>
<h2>Four Scriptures for when God feels far away</h2><div class="scriptureList2"><div class="scriptureItem2"><strong>Psalm 34:18</strong><p>“The LORD is nigh unto them that are of a broken heart...”</p></div><div class="scriptureItem2"><strong>Psalm 13:1</strong><p>“How long wilt thou forget me, O LORD?...”</p></div><div class="scriptureItem2"><strong>Hebrews 13:5</strong><p>“I will never leave thee, nor forsake thee.”</p></div><div class="scriptureItem2"><strong>Romans 8:38–39</strong><p>Nothing can separate the believer from the love of God in Christ.</p></div></div>
</div></div></section>'''

ANGER = STYLE + '''
<section class="deepHelp2"><div class="wrap"><div class="deepHelp2Inner"><p class="eyebrow">Going deeper</p>
<h2>Is it wrong to be angry with God?</h2>
<p>Anger at God is not automatically the opposite of faith. Scripture gives us prayers from people who were confused, disappointed, and even furious. Habakkuk asked why God tolerated injustice. David asked why God seemed to hide. Job said things that later needed correction, but he said them to God rather than walking away from Him.</p>
<div class="deepScripture2">“How long shall I cry, and thou wilt not hear!”<small>Habakkuk 1:2 · KJV</small></div>
<p>The goal is not to crown anger as truth. The goal is to bring anger into relationship with God. <a href="/answer-18">Is it okay to be angry with God?</a> is the best place to begin if you are afraid your anger has disqualified you.</p>
<h2>Why doesn’t God answer every prayer the way we ask?</h2>
<p>The Bible never promises that every faithful prayer will receive the exact answer requested. Jesus prayed in Gethsemane for the cup to pass, yet surrendered Himself to the Father’s will. Paul prayed repeatedly for his thorn to be removed and received grace instead of removal. A no from God can be deeply painful without meaning prayer was pointless.</p>
<p>If God has said no—or appears to have—<a href="/answer-13">What do I do when God says no?</a> walks through that disappointment without pretending it does not hurt.</p>
<h2>What do I pray when I am too angry to pray?</h2>
<p>Pray the sentence you actually have. You do not need polished language. You can say, “God, this hurts. I wanted You to stop it. I do not understand why You did not.” Biblical lament gives hurting people language for bringing complaint and trust into the same prayer.</p>
<p>If all you have is one honest sentence, start there. <a href="/answer-19">What do I even say to God right now?</a> gives a practical path for that kind of prayer.</p>
<h2>Does God care when injustice seems to go unanswered?</h2>
<p>Yes. Delayed justice is not divine approval. Scripture repeatedly places final judgment in God’s hands. That does not erase the need for appropriate earthly accountability, wise boundaries, or protection from harm. It means the absence of immediate consequences does not mean God is morally indifferent.</p>
<p>If someone harmed you and appears to be getting away with it, <a href="/answer-11">Does God care about injustice?</a> goes directly to that wound.</p>
<h2>Four Scriptures for anger and unanswered prayer</h2><div class="scriptureList2"><div class="scriptureItem2"><strong>Psalm 13:1–2</strong><p>David brings his sense of abandonment directly to God.</p></div><div class="scriptureItem2"><strong>Habakkuk 1:2</strong><p>“How long shall I cry, and thou wilt not hear!”</p></div><div class="scriptureItem2"><strong>2 Corinthians 12:9</strong><p>“My grace is sufficient for thee...”</p></div><div class="scriptureItem2"><strong>Romans 12:19</strong><p>“Vengeance is mine; I will repay, saith the Lord.”</p></div></div>
</div></div></section>'''

QUESTION_LINES = {
 'god-feels-far-away.html': '<strong>You may be asking:</strong><br>Why does God feel far away? · Is God silent? · What if I cannot feel God? · Has God forgotten me? · Does Jesus understand my pain?',
 'anger-and-unanswered-prayer.html': '<strong>You may be asking:</strong><br>Is it wrong to be angry with God? · Why did God say no? · Why is my prayer unanswered? · What do I pray when I am furious? · Does God care about injustice?',
}
BLOCKS = {'god-feels-far-away.html': FAR, 'anger-and-unanswered-prayer.html': ANGER}

def patch_hub(name, block):
    path = Path(name)
    text = path.read_text()
    text = re.sub(re.escape(START) + r'.*?' + re.escape(END) + r'\s*', '', text, flags=re.S)
    text, count = re.subn(r'<div class="searchIntent">.*?</div>', '<div class="searchIntent">' + QUESTION_LINES[name] + '</div>', text, count=1, flags=re.S)
    if count != 1: raise RuntimeError('Could not update questions in ' + name)
    marker = '<section class="truthSection">'
    if marker not in text: raise RuntimeError('Missing truth section in ' + name)
    text = text.replace(marker, START + block + END + '\n' + marker, 1)
    path.write_text(text)

DEP_START='<!-- DEPRESSION-DEPTH-START -->'
DEP_END='<!-- DEPRESSION-DEPTH-END -->'
DEP_STYLE='''<style>.depDepth{margin:50px 0 12px;padding-top:8px}.depFaq{border-top:1px solid var(--line)}.depFaqItem{padding:25px 0;border-bottom:1px solid var(--line)}.depFaqItem h3{margin:0 0 10px}.depFaqItem p:last-child{margin-bottom:0}.depNote{background:var(--cream);border-left:3px solid var(--gold);padding:22px 24px;margin:26px 0}.depLinks{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:26px 0}.depLinks a{display:block;text-decoration:none;border:1px solid var(--line);padding:18px;background:white;font-weight:800;color:var(--green)}@media(max-width:700px){.depLinks{grid-template-columns:1fr}}</style>'''
DEP_BLOCK=DEP_STYLE+'''<section class="depDepth"><h2>Questions Christians often ask about depression</h2><div class="depFaq">
<div class="depFaqItem"><h3>Is depression a sin?</h3><p>Depression itself is not automatically a sin. Scripture shows faithful people walking through profound emotional darkness. Sin can affect every part of life and sometimes our choices contribute to our pain, but it is neither biblical nor compassionate to assume that every depressed person is depressed because of personal failure.</p><p>A better first question is not, “What is wrong with my faith?” but, “What is happening in my whole life—body, mind, relationships, circumstances, and soul—and what wise help do I need?”</p></div>
<div class="depFaqItem"><h3>Does depression mean I do not have enough faith?</h3><p>No. Faith is not measured by whether you always feel joyful. Psalm 42 shows a believer speaking truth to a soul that feels cast down. The presence of heaviness does not erase the presence of faith. Sometimes faith looks like reaching toward God when you feel almost nothing.</p></div>
<div class="depFaqItem"><h3>Should a Christian see a counselor or doctor for depression?</h3><p>Yes, seeking qualified help can be wise. Christians regularly thank God for medical care in other areas of life; emotional and mental health do not need to be treated as an exception. If depression is persistent, worsening, or interfering with daily life, talking with a qualified doctor or counselor is a reasonable next step alongside pastoral and spiritual care.</p></div>
<div class="depFaqItem"><h3>Is taking medication for depression unbiblical?</h3><p>Scripture does not teach that receiving appropriate medical treatment is a failure of faith. Medication decisions are medical decisions and should be made with a qualified clinician who can evaluate your situation, potential benefits, risks, and alternatives. Prayer, Scripture, community, counseling, healthy rhythms, and medical care do not have to compete with one another.</p></div>
<div class="depFaqItem"><h3>What role should prayer and Scripture play?</h3><p>A real one—but not as a weapon against the person who is hurting. Prayer and Scripture can anchor you to truth when your feelings are unreliable, give language to lament, remind you of God’s presence, and keep you connected to hope. They should not be used to shame someone for still struggling after they have prayed.</p></div>
</div><div class="depNote"><strong>One important distinction:</strong> sadness, grief, exhaustion, and clinical depression can overlap, but they are not always the same thing. You do not need to diagnose yourself from a webpage. If you are concerned about what you are experiencing, bring the full picture to someone qualified to help you evaluate it.</div>
<div class="depLinks"><a href="/god-feels-far-away">When God Feels Far Away →</a><a href="/anger-and-unanswered-prayer">Anger &amp; Unanswered Prayer →</a></div></section>'''

def patch_depression():
    path=Path('can-christians-be-depressed.html')
    text=path.read_text()
    text=re.sub(re.escape(DEP_START)+r'.*?'+re.escape(DEP_END)+r'\s*','',text,flags=re.S)
    text=text.replace('<title>Can Christians Be Depressed? | A Note from Pastor Tate</title>','<title>Can Christians Be Depressed? Biblical Help for Depression and Faith</title>')
    text=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Can Christians be depressed? Biblical, pastoral help for depression and faith, including guilt, counseling, medication, prayer, Scripture, and practical next steps.">',text,count=1)
    text=text.replace('<div class="byline">Tate Throndson · Pastor, Castleview Baptist Church</div>','<div class="byline">Written by <a href="/about" rel="author"><strong>Tate Throndson</strong></a> · Pastor and author of <em>Answers for a Broken Heart</em></div>')
    marker='<h2>Three things that might actually help this week.</h2>'
    if marker not in text: raise RuntimeError('Could not find depression insertion point')
    text=text.replace(marker, DEP_START+DEP_BLOCK+DEP_END+'\n'+marker,1)
    text=text.replace('<div class="gentle"><strong>A gentle note:</strong>', '<div class="gentle"><strong>A gentle note:</strong>')
    text=text.replace('seek professional or emergency help where you live. You do not have to carry that moment alone.</div>','seek professional or emergency help where you live. You do not have to carry that moment alone. <a href="/unsafe"><strong>Use the immediate safety pathway →</strong></a></div>')
    if 'application/ld+json' not in text:
        data={"@context":"https://schema.org","@type":"Article","headline":"Can Christians Be Depressed?","description":"Biblical and pastoral help for Christians walking through depression, guilt, emotional heaviness, counseling, medication, prayer, and Scripture.","mainEntityOfPage":BASE+'/can-christians-be-depressed',"author":{"@type":"Person","name":"Tate Throndson","url":BASE+'/about'},"isPartOf":{"@type":"WebSite","name":"Answers for a Broken Heart","url":BASE+'/'}}
        text=text.replace('</head>','<script type="application/ld+json">'+json.dumps(data)+'</script>\n</head>',1)
    path.write_text(text)

for name, block in BLOCKS.items(): patch_hub(name, block)
patch_depression()
print('Strengthened God Feels Far Away, Anger & Unanswered Prayer, and Can Christians Be Depressed.')
