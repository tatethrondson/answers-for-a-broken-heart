from pathlib import Path
import re

START = "<!-- EXACT-QUESTION-DEPTH-WAVE2-START -->"
END = "<!-- EXACT-QUESTION-DEPTH-WAVE2-END -->"

STYLE = '''
<style>
.exactDepth2{margin:54px 0 18px;padding:38px 0 0;border-top:1px solid #ddd6c9}
.exactDepth2 h2{font:2.2rem/1.08 Georgia,"Times New Roman",serif;font-weight:400;color:#20372a;margin:38px 0 14px}
.exactDepth2 h2:first-of-type{margin-top:0}
.exactDepth2 p{margin:0 0 1.28em}
.exactDepth2 a{color:#2d4937;font-weight:800;text-underline-offset:2px}
.exactScripture2{background:#f6f1e8;border-left:3px solid #b69258;padding:21px 24px;margin:22px 0 27px;font:1.08rem/1.62 Georgia,"Times New Roman",serif;color:#20372a}
.exactScripture2 small{display:block;margin-top:7px;font:700 .68rem/1.35 Arial,Helvetica,sans-serif;letter-spacing:.1em;text-transform:uppercase;color:#88683b}
.exactQuestions2{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:22px 0 4px}
.exactQuestion2{background:#fffdf9;border:1px solid #ddd6c9;padding:20px}
.exactQuestion2 strong{display:block;font:1.18rem/1.25 Georgia,"Times New Roman",serif;font-weight:400;color:#20372a;margin-bottom:7px}
.exactQuestion2 span{display:block;font-size:.84rem;line-height:1.55;color:#657068}
.exactPastoral2{background:#eef2ed;border-top:3px solid #789078;padding:24px 26px;margin:30px 0}
.exactPastoral2 strong{display:block;color:#20372a;margin-bottom:7px}
@media(max-width:700px){.exactQuestions2{grid-template-columns:1fr}.exactDepth2 h2{font-size:1.95rem}}
</style>
'''

BLOCKS = {
    1: STYLE + '''
<section class="exactDepth2">
<p class="eyebrow">Questions that usually come next</p>
<h2>If God feels far away, does that mean He actually left?</h2>
<p>No. Scripture regularly separates what a believer feels from what God has promised. David could ask why God seemed hidden while still praying to Him. The experience of distance is real, but the feeling of absence is not proof of actual abandonment.</p>
<div class="exactScripture2">“I will never leave thee, nor forsake thee.”<small>Hebrews 13:5 · KJV</small></div>
<p>One of the hardest things about pain is that it can shrink your field of vision. What hurts becomes loud; what is still true can become hard to feel. Faith in that moment is not pretending you feel God. It is choosing not to make your present feeling the final definition of His presence.</p>

<h2>Why can’t I feel God when I pray or read the Bible?</h2>
<p>Spiritual life is not always emotionally vivid. Exhaustion, grief, anxiety, disappointment, unanswered prayer, and prolonged stress can make familiar spiritual practices feel flat. That does not mean prayer has stopped being prayer or Scripture has stopped being true.</p>
<p>Sometimes the most faithful season is a quiet one: reading a Psalm without feeling much, praying one honest sentence, showing up to worship, or letting someone else remind you of truth when your own emotions cannot carry it.</p>

<h2>What if God seems silent?</h2>
<p>Silence is one of the most painful forms of waiting because it invites us to fill in the blank ourselves: <em>He does not care. He forgot me. I did something wrong. Nothing is happening.</em> Scripture gives us many people who lived through long stretches in which God’s activity was clearer later than it was in the moment.</p>
<p>If you are trying to understand what God may be doing when you cannot see it, <a href="/answer-03">Why can’t I see what God is doing right now?</a> is the natural next question.</p>

<h2>Is it wrong to tell God I feel abandoned?</h2>
<p>No. The Psalms give you language for exactly that kind of prayer. Biblical lament is not pretending God has failed; it is bringing the experience of His apparent absence back to Him. You can say, “God, I know what You have promised, but this is what it feels like tonight.”</p>
<div class="exactPastoral2"><strong>For tonight:</strong> do not force yourself to manufacture a spiritual feeling. Name one thing that is true even if you cannot feel it yet. Then pray one honest sentence from there.</div>
<div class="exactQuestions2">
<div class="exactQuestion2"><strong>Wish God would simply show Himself?</strong><span><a href="/answer-02">Read Answer 02 →</a></span></div>
<div class="exactQuestion2"><strong>Cannot see what He is doing?</strong><span><a href="/answer-03">Read Answer 03 →</a></span></div>
<div class="exactQuestion2"><strong>Wondering whether Jesus understands?</strong><span><a href="/answer-09">Read Answer 09 →</a></span></div>
<div class="exactQuestion2"><strong>Need the broader topic?</strong><span><a href="/god-feels-far-away">Explore When God Feels Far Away →</a></span></div>
</div>
</section>
''',
    9: STYLE + '''
<section class="exactDepth2">
<p class="eyebrow">Questions that usually come next</p>
<h2>Does Jesus really understand grief and emotional pain?</h2>
<p>Yes. The Gospels do not present Jesus as emotionally untouched. He wept at Lazarus’s grave. He was moved with compassion. He experienced rejection, betrayal, loneliness, anguish in Gethsemane, physical suffering, and the death of people He loved.</p>
<div class="exactScripture2">“For we have not an high priest which cannot be touched with the feeling of our infirmities...”<small>Hebrews 4:15 · KJV</small></div>
<p>Christian comfort is not merely that God knows facts about suffering. In Jesus, God entered a human life in which pain could be felt from the inside.</p>

<h2>Why did Jesus weep if He knew Lazarus would rise?</h2>
<p>That may be one of the most comforting details in John 11. Jesus knew resurrection was minutes away, and He still wept. Future hope did not make present sorrow unreal. He did not tell Mary and Martha that because the ending would be good, the grief in front of them did not matter.</p>
<p>That gives Christians permission to hold two truths at once: resurrection is real, and the empty chair still hurts.</p>

<h2>Did Jesus experience more than physical pain?</h2>
<p>Yes. He was despised and rejected. Friends abandoned Him. Judas betrayed Him. Peter denied Him. In Gethsemane He told His disciples that His soul was “exceeding sorrowful, even unto death.” The cross was physical agony, but the Gospel accounts also show relational, emotional, and spiritual anguish.</p>

<h2>What good is God’s sympathy if my circumstances do not change?</h2>
<p>Sympathy does not answer every why, but it changes who is beside you in the question. Christianity does not offer a God who asks suffering people to trust Someone who has remained untouched by pain. Jesus entered it—and then went beyond sympathy through the cross and resurrection.</p>
<p>If you are asking whether Jesus did more than understand suffering, <a href="/answer-10">What did Jesus actually do about suffering?</a> carries that question forward.</p>
<div class="exactQuestions2">
<div class="exactQuestion2"><strong>Grieving someone who died?</strong><span><a href="/answer-14">Read Answer 14 →</a></span></div>
<div class="exactQuestion2"><strong>Wondering what Jesus did about suffering?</strong><span><a href="/answer-10">Read Answer 10 →</a></span></div>
<div class="exactQuestion2"><strong>God still feels far away?</strong><span><a href="/answer-01">Read Answer 01 →</a></span></div>
<div class="exactQuestion2"><strong>Need the broader topic?</strong><span><a href="/god-feels-far-away">Explore When God Feels Far Away →</a></span></div>
</div>
</section>
''',
    14: STYLE + '''
<section class="exactDepth2">
<p class="eyebrow">Questions that usually come next</p>
<h2>What does the Bible say about death for a Christian?</h2>
<p>The New Testament never treats death as harmless, but it does treat it as defeated. Jesus called Himself “the resurrection, and the life.” Paul could acknowledge real sorrow while telling believers not to grieve as people who have no hope.</p>
<div class="exactScripture2">“I am the resurrection, and the life: he that believeth in me, though he were dead, yet shall he live.”<small>John 11:25 · KJV</small></div>
<p>Christian hope is not that death is less painful than it feels. It is that death does not get to be permanent for those who are in Christ.</p>

<h2>Is grieving a lack of faith?</h2>
<p>No. Jesus wept. The believers in Acts mourned. Paul did not say Christians never sorrow; he said our sorrow is different because hope stands on the other side of it. You can believe every promise about resurrection and still deeply miss someone today.</p>

<h2>Will I see a believing loved one again?</h2>
<p>First Thessalonians 4 grounds Christian comfort in reunion with Christ and with believers who have died. The center of the promise is not simply “we get our old life back.” It is that those who belong to Christ will be with the Lord, and death will no longer separate His people forever.</p>
<p>That hope should be stated carefully when we do not know another person’s relationship with Christ. But where there is a credible Christian hope, Scripture gives grieving believers real reason to look beyond the grave.</p>

<h2>What does resurrection change about grief right now?</h2>
<p>It does not erase the funeral. It changes the word <em>final</em>. Resurrection allows you to grieve honestly without treating the grave as the last chapter. That is why Christian funerals can contain tears and worship in the same room.</p>
<div class="exactPastoral2"><strong>Hold both:</strong> you do not have to minimize the loss in order to magnify the hope. The resurrection is strong enough to sit beside real grief.</div>
<div class="exactQuestions2">
<div class="exactQuestion2"><strong>Wondering how long grief is allowed to last?</strong><span><a href="/answer-15">Read Answer 15 →</a></span></div>
<div class="exactQuestion2"><strong>Need to know Jesus understands this loss?</strong><span><a href="/answer-09">Read Answer 09 →</a></span></div>
<div class="exactQuestion2"><strong>Grief seems to be getting worse?</strong><span><a href="/answer-17">Read Answer 17 →</a></span></div>
<div class="exactQuestion2"><strong>Need the broader topic?</strong><span><a href="/grief-and-loss">Explore Grief &amp; Loss →</a></span></div>
</div>
</section>
''',
    15: STYLE + '''
<section class="exactDepth2">
<p class="eyebrow">Questions that usually come next</p>
<h2>Does the Bible give grief a timetable?</h2>
<p>No single timetable is given for every loss. Scripture includes seasons of mourning, tears that return, anniversaries of sorrow, and people whose lives were permanently changed by what happened. Ecclesiastes simply says there is “a time to weep, and a time to laugh; a time to mourn, and a time to dance.”</p>
<div class="exactScripture2">“A time to weep, and a time to laugh; a time to mourn, and a time to dance.”<small>Ecclesiastes 3:4 · KJV</small></div>
<p>Healthy grief moves, but movement is not the same as speed. The goal is not to prove you are over it. The goal is to keep walking with God and people while learning how to carry a loss that may always matter.</p>

<h2>Does a hard day mean I am going backward?</h2>
<p>Not necessarily. Grief can be stirred by a date, song, place, smell, holiday, photograph, or ordinary moment you did not see coming. A wave of sadness after several better weeks does not automatically erase the progress that came before it.</p>
<p>Grief often moves more like a winding road than a straight line.</p>

<h2>What if people think I should be over it by now?</h2>
<p>Other people often become uncomfortable with grief before the grieving person is finished carrying it. Their discomfort does not establish a biblical deadline for your sorrow. You can be gracious with people who do not know what to say without accepting pressure to perform recovery for them.</p>
<p>At the same time, grief should not become a reason to isolate indefinitely from every relationship, responsibility, or source of help. You are allowed to move slowly, but you were not meant to carry grief alone.</p>

<h2>How do I know whether grief is becoming stuck?</h2>
<p>There is no simple test, but pay attention to direction. Are you still able, over time, to receive love, talk honestly, remember the person or loss with more than one emotion, pray, and remain connected to life? Or is grief increasingly hardening into isolation, bitterness, revenge, hopelessness, or complete withdrawal?</p>
<p>If you are worried that the pain is becoming heavier instead of simply different, <a href="/answer-17">Why does grief feel worse over time?</a> goes directly into that question.</p>
<div class="exactPastoral2"><strong>You are not on a stopwatch.</strong> Healing is not measured by how quickly you stop missing someone. It is seen in whether sorrow is slowly learning to coexist with love, hope, truth, and life.</div>
<div class="exactQuestions2">
<div class="exactQuestion2"><strong>Need hope beyond the grave?</strong><span><a href="/answer-14">Read Answer 14 →</a></span></div>
<div class="exactQuestion2"><strong>Grief feels heavier instead of lighter?</strong><span><a href="/answer-17">Read Answer 17 →</a></span></div>
<div class="exactQuestion2"><strong>Still asking why this happened?</strong><span><a href="/answer-16">Read Answer 16 →</a></span></div>
<div class="exactQuestion2"><strong>Need the broader topic?</strong><span><a href="/grief-and-loss">Explore Grief &amp; Loss →</a></span></div>
</div>
</section>
''',
    19: STYLE + '''
<section class="exactDepth2">
<p class="eyebrow">Questions that usually come next</p>
<h2>Is it disrespectful to pray honestly when I am angry?</h2>
<p>Honesty is not the same as irreverence. Scripture gives us prayers in which hurting people ask how long, why, where God is, and why He seems hidden. God does not need a cleaned-up version of emotions He already knows are present.</p>
<div class="exactScripture2">“Trust in him at all times; ye people, pour out your heart before him: God is a refuge for us.”<small>Psalm 62:8 · KJV</small></div>
<p>Reverence means God remains God even while you tell Him the truth. You can speak plainly without treating your own interpretation of the situation as infallible.</p>

<h2>What if I do not have the right words?</h2>
<p>Then use small words. “God, I am hurt.” “I do not understand.” “I am angry.” “Help me.” Romans 8 says the Spirit helps our infirmities when we do not know what we should pray for as we ought. A prayer does not become more real because it becomes more eloquent.</p>

<h2>Can I use the Psalms when my own prayers feel impossible?</h2>
<p>Yes. The Psalms can loan you language when your own words fail. Read Psalm 13 when God feels hidden. Read Psalm 42 when your soul feels cast down. Read Psalm 62 when you need permission to pour out your heart. Read Psalm 88 when the night has not yet turned into morning.</p>
<p>You do not have to make every prayer end in emotional resolution. Sometimes faith is simply continuing the conversation.</p>

<h2>How do I move from lament toward trust without pretending?</h2>
<p>Do not rush the turn. Biblical lament usually tells the truth about pain before it reaches for trust. Name what hurts. Ask what you need to ask. Then remind your heart of one thing you know about God even if you do not yet understand what He allowed.</p>
<p>Trust is not saying, “I am no longer hurt.” It is saying, “I am still bringing the hurt to You.”</p>
<div class="exactPastoral2"><strong>A simple prayer pattern:</strong> Tell God what happened. Tell Him what it did to you. Tell Him what you wish He had done. Ask for what you need now. Then anchor the prayer in one truth you are not willing to surrender.</div>
<div class="exactQuestions2">
<div class="exactQuestion2"><strong>Still furious with God?</strong><span><a href="/answer-18">Read Answer 18 →</a></span></div>
<div class="exactQuestion2"><strong>God said no to a specific prayer?</strong><span><a href="/answer-13">Read Answer 13 →</a></span></div>
<div class="exactQuestion2"><strong>Wondering whether God cares about injustice?</strong><span><a href="/answer-11">Read Answer 11 →</a></span></div>
<div class="exactQuestion2"><strong>Need the broader topic?</strong><span><a href="/anger-and-unanswered-prayer">Explore Anger &amp; Unanswered Prayer →</a></span></div>
</div>
</section>
''',
}


def strengthen(number, block):
    path = Path(f"answer-{number:02d}.html")
    if not path.exists():
        raise RuntimeError(f"Missing {path}")
    text = path.read_text()
    text = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\s*", "", text, flags=re.S)
    marker = "</article>"
    if marker not in text:
        raise RuntimeError(f"Could not find article end in {path}")
    text = text.replace(marker, START + "\n" + block + "\n" + END + "\n" + marker, 1)
    path.write_text(text)


for number, block in BLOCKS.items():
    strengthen(number, block)

print("Strengthened Answers 01, 09, 14, 15, and 19 with second-wave exact-question pastoral depth.")
