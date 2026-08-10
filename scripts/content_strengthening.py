from pathlib import Path
import re

START = "<!-- CONTENT-STRENGTHENING-START -->"
END = "<!-- CONTENT-STRENGTHENING-END -->"

STYLE = '''
<style>
.deepHelp{padding:58px 0;background:#fff;border-top:1px solid #eee8df}
.deepHelpInner{max-width:850px}
.deepHelp h2{font:2.35rem/1.08 Georgia,"Times New Roman",serif;font-weight:400;color:#183024;margin:42px 0 14px}
.deepHelp h2:first-of-type{margin-top:0}
.deepHelp h3{font:1.55rem/1.18 Georgia,"Times New Roman",serif;font-weight:400;color:#20372a;margin:30px 0 10px}
.deepHelp p{font-size:1rem;line-height:1.76;color:#364039;margin:0 0 1.22em}
.deepHelp a{color:#294533;font-weight:800;text-decoration-thickness:1px;text-underline-offset:2px}
.deepScripture{background:#f6f1e8;border-left:3px solid #ad823d;padding:20px 23px;margin:23px 0 28px;font:1.08rem/1.65 Georgia,"Times New Roman",serif;color:#20372a}
.deepScripture small{display:block;margin-top:7px;font:700 .68rem/1.4 Arial,Helvetica,sans-serif;letter-spacing:.1em;text-transform:uppercase;color:#87683a}
.deepQuestions{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:20px 0 8px}
.deepQuestion{border:1px solid #ded8cd;background:#fffdf9;padding:20px}
.deepQuestion strong{display:block;font:1.18rem/1.25 Georgia,"Times New Roman",serif;color:#183024;font-weight:400;margin-bottom:6px}
.deepQuestion span{display:block;font-size:.82rem;line-height:1.55;color:#626b65}
.scriptureList{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:18px}
.scriptureItem{background:#f8f5ef;border:1px solid #ded8cd;padding:20px}
.scriptureItem strong{display:block;font-size:.7rem;letter-spacing:.11em;text-transform:uppercase;color:#87683a;margin-bottom:7px}
.scriptureItem p{font:1rem/1.55 Georgia,"Times New Roman",serif;color:#20372a;margin:0}
@media(max-width:760px){.deepQuestions,.scriptureList{grid-template-columns:1fr}.deepHelp h2{font-size:2rem}}
</style>
'''

GRIEF = STYLE + '''
<section class="deepHelp"><div class="wrap"><div class="deepHelpInner">
<p class="eyebrow">Going deeper</p>
<h2>What does the Bible say about grief?</h2>
<p>The Bible treats grief as a real response to real loss. It does not tell mourners to hurry up, hide their tears, or prove their faith by acting untouched. Abraham mourned Sarah. David lamented people he loved. Job tore his clothes and grieved. Jesus stood at the grave of Lazarus and wept. Scripture is remarkably comfortable telling the truth about sorrow.</p>
<div class="deepScripture">“Jesus wept.”<small>John 11:35 · KJV</small></div>
<p>Those two words matter because Jesus knew Lazarus would rise. He knew death would not win. He knew what He was about to do—and He still wept. Christian hope does not make grief unnecessary. It changes what grief means. Paul did not tell believers not to sorrow; he told them not to sorrow <em>as others which have no hope</em>. We grieve, but we do not grieve as though the grave is all there is.</p>

<h2>Is grief a lack of faith?</h2>
<p>No. Grief and faith can occupy the same heart at the same time. You can know God is good and still miss someone terribly. You can believe in resurrection and still hate the empty chair. You can trust Christ and still have mornings when getting out of bed feels heavier than it should.</p>
<p>Sometimes Christians add a second wound to grief by assuming, “If I trusted God more, this would not hurt so much.” Scripture does not require that conclusion. Love creates attachment, and loss tears at that attachment. The pain may actually tell you something about the depth of the love. If you are wrestling with whether hope changes death, read <a href="/answer-14">Where is hope when someone dies?</a></p>

<h2>How long is it okay to grieve?</h2>
<p>Scripture does not give every grieving person the same timetable. There is movement in healthy grief, but movement is not the same as speed. Some losses alter the shape of a life permanently. The goal is not to reach a day when the person or loss no longer matters. The goal is to learn, over time, how to carry love and sorrow without letting sorrow become the only thing you carry.</p>
<p>That is why anniversaries, holidays, familiar songs, photographs, smells, and ordinary routines can suddenly make old grief feel new. A difficult day does not necessarily mean you have gone backward. Grief often moves more like a winding road than a straight line. If you are wondering whether you have been sad “too long,” start with <a href="/answer-15">How long am I allowed to still be sad about this?</a></p>

<h2>Why can grief feel worse before it feels better?</h2>
<p>In the first days after a loss, there can be arrangements to make, people around you, meals arriving, phone calls, services, decisions, and shock. Later, life around you begins moving again while your world still feels changed. Sometimes that is when the absence becomes more concrete. The quiet after everyone else goes home can be harder than the busy days that came before it.</p>
<p>If the pain seems to be deepening, do not automatically assume you are failing. Pay attention to whether grief is still moving—whether you can talk, pray honestly, receive care, remember with gratitude as well as pain, and remain connected to people. If you feel stuck in bitterness, isolation, or despair, <a href="/answer-17">Why does it feel like I’m getting worse instead of better?</a> goes deeper into that question.</p>

<h2>Four Scriptures to hold onto in grief</h2>
<div class="scriptureList">
<div class="scriptureItem"><strong>Psalm 34:18</strong><p>“The LORD is nigh unto them that are of a broken heart...”</p></div>
<div class="scriptureItem"><strong>John 11:35</strong><p>“Jesus wept.”</p></div>
<div class="scriptureItem"><strong>1 Thessalonians 4:13</strong><p>“...that ye sorrow not, even as others which have no hope.”</p></div>
<div class="scriptureItem"><strong>Revelation 21:4</strong><p>“And God shall wipe away all tears from their eyes...”</p></div>
</div>
</div></div></section>
'''

SUFFERING = STYLE + '''
<section class="deepHelp"><div class="wrap"><div class="deepHelpInner">
<p class="eyebrow">Going deeper</p>
<h2>Why does God allow suffering?</h2>
<p>There is no single sentence in Scripture that explains every tragedy. The Bible gives us something larger: a framework strong enough to hold the questions that do not receive tidy answers. It begins with a God who made the world good, tells the truth about a creation fractured by sin, shows us a Savior who entered suffering Himself, and ends with God making all things new.</p>
<div class="deepScripture">“And God saw every thing that he had made, and, behold, it was very good.”<small>Genesis 1:31 · KJV</small></div>
<p>That starting point matters. Christianity does not ask you to look at cancer, abuse, war, betrayal, disease, or death and call them “very good.” The Bible says something has gone wrong with the world. If you want to begin with that foundation, read <a href="/answer-04">Why does God allow suffering?</a></p>

<h2>Did God create suffering?</h2>
<p>Genesis presents God’s original creation as good. Sin enters the human story in Genesis 3, and with it come shame, alienation, toil, decay, and death. Paul later describes creation itself as groaning. The world we experience now is not presented as the finished expression of what God intends creation to be.</p>
<p>That does not mean every painful event can be traced to one specific sin or one guilty person. It means we live in a world where bodies break, nature groans, people make destructive choices, and death is present. The Christian story begins with creation, explains the fracture through the fall, centers redemption in Christ, and looks toward restoration.</p>

<h2>Is suffering always punishment for something I did?</h2>
<p>No. The Bible repeatedly resists that simplistic equation. In John 9, the disciples saw a man born blind and immediately wanted to know whose sin explained his condition. Jesus refused their either-or assumption. Job’s friends also made the mistake of assuming severe suffering must prove severe personal guilt.</p>
<p>Sometimes our choices do have painful consequences. Sometimes another person’s sin wounds us. Sometimes suffering comes simply because we inhabit a fallen world. Wisdom requires enough humility not to claim an explanation God has not given. If you keep asking why, <a href="/answer-05">Is it wrong that I keep asking God why?</a> and <a href="/answer-06">Why won’t God just tell me why this is happening?</a> address that tension directly.</p>

<h2>Why doesn’t God stop every painful thing?</h2>
<p>This may be the hardest form of the question because Christians believe God is able to intervene. Scripture does not hand us the hidden reason behind every event. It does show that human beings make real choices with real consequences, that creation is broken, and that God can permit what He does not delight in while still working redemptively through it.</p>
<p>Faith is not pretending we know why God allowed one diagnosis, one accident, one betrayal, or one death. Faith is deciding what we will do with the God who has revealed Himself when the explanation remains hidden. Sometimes the answer we receive is not a reason but God’s presence. That is the heart of <a href="/answer-08">What do I do when the explanation never comes?</a></p>

<h2>Can God bring good out of something that was not good?</h2>
<p>Yes—but that must be said carefully. Romans 8:28 does not say everything that happens is good. It says God works in all things for good to those who love Him. Joseph could look back at what his brothers meant for evil and say God meant it unto good. Redemption is one of the great themes of Scripture: God is able to take what sin damaged and make it serve purposes the evil itself never deserved.</p>
<p>That may include compassion you did not have before, ministry born out of a wound, endurance formed under pressure, relationships deepened by hardship, or a clearer view of what matters eternally. None of those things requires calling the original hurt good. If this is the question you are carrying, read <a href="/answer-07">Can anything good actually come out of this?</a></p>

<h2>Where is God in suffering?</h2>
<p>Christianity’s deepest answer is not an argument but a Person. Jesus did not stand outside human suffering and offer observations about it. He experienced rejection, injustice, grief, physical agony, abandonment by friends, and death. At Lazarus’s grave He wept. In Gethsemane He prayed in anguish. At Calvary He suffered.</p>
<p>The cross means we cannot say God knows nothing about pain. The resurrection means suffering does not get the last word. We may not know why every chapter was permitted, but Christians know where the story is going: toward resurrection, restoration, and a world in which God wipes away every tear.</p>

<h2>Four Scriptures to hold onto in suffering</h2>
<div class="scriptureList">
<div class="scriptureItem"><strong>Genesis 1:31</strong><p>“...behold, it was very good.”</p></div>
<div class="scriptureItem"><strong>Romans 8:28</strong><p>“And we know that all things work together for good...”</p></div>
<div class="scriptureItem"><strong>John 16:33</strong><p>“In the world ye shall have tribulation: but be of good cheer...”</p></div>
<div class="scriptureItem"><strong>Revelation 21:4</strong><p>“...there shall be no more death, neither sorrow, nor crying...”</p></div>
</div>
</div></div></section>
'''

QUESTION_LINES = {
    "grief-and-loss.html": "<strong>You may be asking:</strong><br>What does the Bible say about grief? · Is grief a lack of faith? · How long is it okay to grieve? · Why can grief feel worse before it feels better?",
    "why-god-allows-suffering.html": "<strong>You may be asking:</strong><br>Why does God allow suffering? · Did God create pain? · Is suffering punishment? · Why doesn’t God stop it? · Can anything good come from this?",
}

BLOCKS = {
    "grief-and-loss.html": GRIEF,
    "why-god-allows-suffering.html": SUFFERING,
}


def strengthen(path_name, block):
    path = Path(path_name)
    if not path.exists():
        raise RuntimeError(f"Missing {path_name}")
    text = path.read_text()
    text = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\s*", "", text, flags=re.S)

    replacement = QUESTION_LINES[path_name]
    text, count = re.subn(
        r'<div class="searchIntent">.*?</div>',
        f'<div class="searchIntent">{replacement}</div>',
        text,
        count=1,
        flags=re.S,
    )
    if count != 1:
        raise RuntimeError(f"Could not update question line in {path_name}")

    marker = '<section class="truthSection">'
    if marker not in text:
        raise RuntimeError(f"Could not find truth section in {path_name}")
    text = text.replace(marker, START + block + END + "\n" + marker, 1)
    path.write_text(text)


for name, block in BLOCKS.items():
    strengthen(name, block)

print("Strengthened Grief & Loss and Why God Allows Suffering with deeper pastoral search-intent content.")
