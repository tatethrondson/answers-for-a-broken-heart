from pathlib import Path
import re

START = "<!-- EXACT-QUESTION-DEPTH-WAVE4-START -->"
END = "<!-- EXACT-QUESTION-DEPTH-WAVE4-END -->"

STYLE = '''
<style>
.exactDepth4{margin:54px 0 18px;padding:38px 0 0;border-top:1px solid #ddd6c9}
.exactDepth4 h2{font:2.2rem/1.08 Georgia,"Times New Roman",serif;font-weight:400;color:#20372a;margin:38px 0 14px}
.exactDepth4 h2:first-of-type{margin-top:0}
.exactDepth4 p{margin:0 0 1.28em}
.exactDepth4 a{color:#2d4937;font-weight:800;text-underline-offset:2px}
.exactScripture4{background:#f6f1e8;border-left:3px solid #b69258;padding:21px 24px;margin:22px 0 27px;font:1.08rem/1.62 Georgia,"Times New Roman",serif;color:#20372a}
.exactScripture4 small{display:block;margin-top:7px;font:700 .68rem/1.35 Arial,Helvetica,sans-serif;letter-spacing:.1em;text-transform:uppercase;color:#88683b}
.exactQuestions4{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:22px 0 4px}
.exactQuestion4{background:#fffdf9;border:1px solid #ddd6c9;padding:20px}
.exactQuestion4 strong{display:block;font:1.18rem/1.25 Georgia,"Times New Roman",serif;font-weight:400;color:#20372a;margin-bottom:7px}
.exactQuestion4 span{display:block;font-size:.84rem;line-height:1.55;color:#657068}
.exactPastoral4{background:#eef2ed;border-top:3px solid #789078;padding:24px 26px;margin:30px 0}
.exactPastoral4 strong{display:block;color:#20372a;margin-bottom:7px}
@media(max-width:700px){.exactQuestions4{grid-template-columns:1fr}.exactDepth4 h2{font-size:1.95rem}}
</style>
'''

BLOCKS = {
    3: STYLE + '''
<section class="exactDepth4">
<p class="eyebrow">Questions that usually come next</p>
<h2>Why does God’s work often make more sense later?</h2>
<p>Because we experience life one moment at a time. We know what happened today, but we do not know every consequence tomorrow will bring. Scripture repeatedly shows people interpreting events with incomplete information and only later recognizing a larger story.</p>
<p>Joseph could not see Genesis 50 from the pit. Ruth could not see David from the funeral. The disciples could not see Easter from Friday afternoon. Looking back does not make the painful part unreal; it simply gives us a wider field of vision.</p>
<div class="exactScripture4">“Surely the LORD is in this place; and I knew it not.”<small>Genesis 28:16 · KJV</small></div>

<h2>Does trusting God mean I should pretend I understand?</h2>
<p>No. Trust is not pretending the map makes sense. Proverbs 3:5 does not say, “Understand everything.” It says not to make your own understanding the final support for your faith. You can say, “I do not know what God is doing,” without turning that uncertainty into, “Therefore God is doing nothing.”</p>
<p>Faith can live with an unfinished explanation.</p>

<h2>What if I never get the rearview-mirror moment?</h2>
<p>Some stories become clearer with time. Others remain painful and unresolved for the rest of this life. Christianity should not promise that every tragedy will eventually become obvious to us. Scripture gives hope larger than present understanding: God sees what we do not, resurrection is real, justice is not finished, and the story extends beyond the years we can presently observe.</p>
<div class="exactPastoral4"><strong>A gentler way to live with uncertainty:</strong> do not demand that today explain the whole story. Ask for enough light to take the next faithful step.</div>

<h2>How do I trust God when I cannot see what He is doing?</h2>
<p>Return to what is already clear. God’s character in Christ. The promises Scripture actually makes. The people He has given you. The next responsibility in front of you. Trust is often less dramatic than we imagine. Sometimes it looks like refusing to make a permanent conclusion about God from a chapter that is still being written.</p>
<div class="exactQuestions4">
<div class="exactQuestion4"><strong>God feels absent, not merely confusing?</strong><span><a href="/answer-01">Read Answer 01 →</a></span></div>
<div class="exactQuestion4"><strong>Still asking for an explanation?</strong><span><a href="/answer-06">Read Answer 06 →</a></span></div>
<div class="exactQuestion4"><strong>What if the explanation never comes?</strong><span><a href="/answer-08">Read Answer 08 →</a></span></div>
<div class="exactQuestion4"><strong>Need the broader topic?</strong><span><a href="/god-feels-far-away">Explore When God Feels Far Away →</a></span></div>
</div>
</section>
''',
    6: STYLE + '''
<section class="exactDepth4">
<p class="eyebrow">Questions that usually come next</p>
<h2>Why won’t God explain why this happened?</h2>
<p>Sometimes Scripture gives a reason for suffering. Often it does not. Job never receives the tidy explanation his friends kept trying to manufacture. Instead, God confronts the limits of Job’s perspective and reminds him that the universe is larger than the portion he can presently see.</p>
<p>That can feel unsatisfying when what you want is an answer. But the biblical response is not, “Stop asking.” It is, “Do not confuse the absence of an explanation with the absence of God.”</p>
<div class="exactScripture4">“For my thoughts are not your thoughts, neither are your ways my ways, saith the LORD.”<small>Isaiah 55:8 · KJV</small></div>

<h2>Would knowing why actually make the pain easier?</h2>
<p>Sometimes it would help. Clarity matters. But explanation and comfort are not identical. You can understand why a surgery was necessary and still hurt afterward. You can know why a relationship ended and still grieve it. Some wounds are not healed merely by receiving more information.</p>
<p>That is why Scripture often gives hurting people more than answers. It gives presence, promises, community, lament, and ultimately Christ Himself.</p>

<h2>Is God withholding an explanation because He is angry with me?</h2>
<p>Not necessarily. Silence is not a reliable indicator of divine displeasure. Faithful people throughout Scripture lived through long stretches when they did not understand what God was doing. Do not build an accusation against yourself from information God has not given you.</p>
<p>If Scripture exposes a sin, respond to it. But do not assume every unanswered question is a coded message of condemnation.</p>

<h2>What should I do while I wait for clarity?</h2>
<p>Keep the question open without letting it become the only question you ask. Alongside “Why?” ask, “What is faithful today?” “Who do I need?” “What truth do I know?” “What help should I receive?” and “What kind of person do I want this pain to shape me into?”</p>
<div class="exactQuestions4">
<div class="exactQuestion4"><strong>Is it wrong that you keep asking why?</strong><span><a href="/answer-05">Read Answer 05 →</a></span></div>
<div class="exactQuestion4"><strong>Wondering whether good can still come?</strong><span><a href="/answer-07">Read Answer 07 →</a></span></div>
<div class="exactQuestion4"><strong>What if the answer never arrives?</strong><span><a href="/answer-08">Read Answer 08 →</a></span></div>
<div class="exactQuestion4"><strong>Need the broader framework?</strong><span><a href="/why-god-allows-suffering">Explore Why God Allows Suffering →</a></span></div>
</div>
</section>
''',
    8: STYLE + '''
<section class="exactDepth4">
<p class="eyebrow">Questions that usually come next</p>
<h2>What if God never tells me why?</h2>
<p>Then faith may eventually have to live without the explanation you wanted. That is not the same thing as saying the question did not matter. It means you refuse to make understanding the price God must pay before you will let Him remain God.</p>
<p>There are losses we may carry to the end of this life without knowing why they were permitted. Christianity does not promise that every mystery will be solved on our timetable. It promises that God can be known even while some of His ways remain beyond us.</p>
<div class="exactScripture4">“For now we see through a glass, darkly; but then face to face.”<small>1 Corinthians 13:12 · KJV</small></div>

<h2>How do I stop obsessing over an answer I cannot get?</h2>
<p>You may not be able to stop the question from returning, but you can stop giving it unlimited control over every hour. Give the question a place to go: write it, pray it, discuss it with wise people, and then return to the part of life you can actually live today.</p>
<p>A mystery can remain open without becoming the only open tab in your mind.</p>

<h2>Does accepting mystery mean I am giving up intellectually?</h2>
<p>No. Christianity has room for investigation, evidence, theology, and hard questions. Humility simply recognizes that a finite person will not possess exhaustive knowledge of an infinite God or every hidden chain of cause and consequence.</p>
<p>You can think seriously and still admit, “I do not know.” Those words are not intellectual surrender. Sometimes they are intellectual honesty.</p>

<h2>What can I hold onto when explanation is gone?</h2>
<p>Hold onto what God has made clear in Christ. He is not indifferent to suffering. He has entered it. He has borne evil rather than merely commenting on it. He has risen from death. And He has promised a future in which death, tears, and injustice do not have the last word.</p>
<div class="exactPastoral4"><strong>When the answer never comes:</strong> you may have to stop asking the explanation to carry a weight only a Person can carry. Sometimes God does not give you the sentence you wanted. He gives you Himself to walk with through the unanswered sentence.</div>
<div class="exactQuestions4">
<div class="exactQuestion4"><strong>Still asking God why?</strong><span><a href="/answer-05">Read Answer 05 →</a></span></div>
<div class="exactQuestion4"><strong>Wondering whether anything good can come?</strong><span><a href="/answer-07">Read Answer 07 →</a></span></div>
<div class="exactQuestion4"><strong>God feels far away in the silence?</strong><span><a href="/answer-01">Read Answer 01 →</a></span></div>
<div class="exactQuestion4"><strong>Need the broader framework?</strong><span><a href="/why-god-allows-suffering">Explore Why God Allows Suffering →</a></span></div>
</div>
</section>
''',
    11: STYLE + '''
<section class="exactDepth4">
<p class="eyebrow">Questions that usually come next</p>
<h2>Does God care when someone gets away with what they did?</h2>
<p>Yes. Scripture does not treat injustice as a small thing. God repeatedly identifies Himself as a righteous Judge, condemns oppression and abuse of power, and tells wounded people that final vengeance does not belong in their hands because judgment belongs to Him.</p>
<p>The difficult part is timing. God’s justice is real, but it is not always immediate. A delayed reckoning can feel like no reckoning at all when you are the one living with the consequences.</p>
<div class="exactScripture4">“Vengeance is mine; I will repay, saith the Lord.”<small>Romans 12:19 · KJV</small></div>

<h2>Does forgiveness mean I should stop wanting justice?</h2>
<p>No. Forgiveness and justice are not enemies. Forgiveness releases personal vengeance; justice names wrongdoing truthfully and seeks appropriate accountability. You can forgive someone and still report abuse, cooperate with authorities, maintain boundaries, tell the truth, or believe consequences are appropriate.</p>
<p>What forgiveness changes is who carries the final ledger.</p>

<h2>Why does God sometimes seem silent about evil?</h2>
<p>Silence is not approval. Scripture contains long stretches where wicked people appeared to prosper and faithful people asked exactly that question. Psalm 73 wrestles with it. Habakkuk wrestles with it. The Bible does not hide the scandal of delayed justice.</p>
<p>Christian hope is that delay is not the same thing as indifference. God sees more than the visible outcome, and no human being gets the final word on his or her own conduct.</p>

<h2>What do I do when justice may never happen in this life?</h2>
<p>Tell the truth. Protect yourself and others. Use legitimate avenues of accountability where they exist. Refuse to make revenge your vocation. And grieve the fact that some wrongs remain visibly unresolved.</p>
<p>Trusting God with judgment is not pretending the wrong did not matter. It is admitting that your soul cannot survive being both the wounded person and the final judge.</p>
<div class="exactQuestions4">
<div class="exactQuestion4"><strong>Trying to forgive without an apology?</strong><span><a href="/answer-21">Read Answer 21 →</a></span></div>
<div class="exactQuestion4"><strong>Wondering about boundaries and reconciliation?</strong><span><a href="/answer-22">Read Answer 22 →</a></span></div>
<div class="exactQuestion4"><strong>Angry with God about the injustice?</strong><span><a href="/answer-18">Read Answer 18 →</a></span></div>
<div class="exactQuestion4"><strong>Need the broader topic?</strong><span><a href="/anger-and-unanswered-prayer">Explore Anger &amp; Unanswered Prayer →</a></span></div>
</div>
</section>
''',
    16: STYLE + '''
<section class="exactDepth4">
<p class="eyebrow">Questions that usually come next</p>
<h2>Why did this happen to me?</h2>
<p>Sometimes there is a direct answer: a decision had consequences, another person acted wrongly, a body became sick, or an accident occurred. But even when we know the immediate cause, the deeper question remains: <em>Why was this allowed to become part of my story?</em></p>
<p>Scripture does not give a personalized hidden reason for every painful event. That means we should be very cautious about inventing one. Not every tragedy is a secret punishment, not every loss is a divine lesson we can identify, and not every wound arrives with an explanation.</p>
<div class="exactScripture4">“And his disciples asked him, saying, Master, who did sin, this man, or his parents, that he was born blind? Jesus answered, Neither hath this man sinned, nor his parents...”<small>John 9:2–3 · KJV</small></div>

<h2>Did this happen because I did something wrong?</h2>
<p>Possibly some suffering is connected to our choices, but pain itself is not proof of personal guilt. Job’s friends assumed suffering meant Job had committed some hidden offense, and Scripture exposes how badly they misread him. Jesus rejected the disciples’ simplistic attempt to reduce one man’s suffering to a blame equation.</p>
<p>If there is something to confess, confess it. But do not manufacture guilt merely because you hurt.</p>

<h2>Why me—and not someone else?</h2>
<p>That comparison rarely produces peace because there is no distribution chart of suffering that we are able to inspect. Pain feels especially unjust when we watch others live the version of life we wanted. Scripture gives permission to grieve that disparity without promising that we will understand it.</p>
<p>The more useful question is not, “What did I do to deserve a life different from theirs?” but, “Given the life I actually have, where is God inviting me to live faithfully now?”</p>

<h2>What is a better question than “Why me?”</h2>
<p>Not because “why” is forbidden, but because it can become a room with no door. Try adding questions that create movement: “What do I need now?” “Who can walk with me?” “What is this revealing about my heart?” “What kind of person do I want to become?” “Where could God still bring redemption?”</p>
<div class="exactPastoral4"><strong>You are allowed to keep the why-question.</strong> You simply do not have to let it be the only question in the room.</div>
<div class="exactQuestions4">
<div class="exactQuestion4"><strong>Wondering whether God will ever explain it?</strong><span><a href="/answer-06">Read Answer 06 →</a></span></div>
<div class="exactQuestion4"><strong>Wondering whether any good can come from it?</strong><span><a href="/answer-07">Read Answer 07 →</a></span></div>
<div class="exactQuestion4"><strong>Your grief feels heavier over time?</strong><span><a href="/answer-17">Read Answer 17 →</a></span></div>
<div class="exactQuestion4"><strong>Need the broader grief framework?</strong><span><a href="/grief-and-loss">Explore Grief &amp; Loss →</a></span></div>
</div>
</section>
''',
}


def apply_block(number, block):
    path = Path(f"answer-{number:02d}.html")
    if not path.exists():
        print(f"Skipping missing {path}")
        return
    html = path.read_text(encoding="utf-8")
    wrapped = f"{START}\n{block}\n{END}"
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if pattern.search(html):
        new_html = pattern.sub(wrapped, html)
    else:
        marker = "</article>"
        if marker not in html:
            raise RuntimeError(f"Could not find article close in {path}")
        new_html = html.replace(marker, wrapped + "\n" + marker, 1)
    if new_html != html:
        path.write_text(new_html, encoding="utf-8")
        print(f"Strengthened {path}")
    else:
        print(f"Already current: {path}")


for number, block in BLOCKS.items():
    apply_block(number, block)
