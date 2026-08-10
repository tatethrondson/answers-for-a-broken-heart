from pathlib import Path
import re

START = "<!-- EXACT-QUESTION-DEPTH-WAVE3-START -->"
END = "<!-- EXACT-QUESTION-DEPTH-WAVE3-END -->"

STYLE = '''
<style>
.exactDepth3{margin:54px 0 18px;padding:38px 0 0;border-top:1px solid #ddd6c9}
.exactDepth3 h2{font:2.2rem/1.08 Georgia,"Times New Roman",serif;font-weight:400;color:#20372a;margin:38px 0 14px}
.exactDepth3 h2:first-of-type{margin-top:0}
.exactDepth3 p{margin:0 0 1.28em}
.exactDepth3 a{color:#2d4937;font-weight:800;text-underline-offset:2px}
.exactScripture3{background:#f6f1e8;border-left:3px solid #b69258;padding:21px 24px;margin:22px 0 27px;font:1.08rem/1.62 Georgia,"Times New Roman",serif;color:#20372a}
.exactScripture3 small{display:block;margin-top:7px;font:700 .68rem/1.35 Arial,Helvetica,sans-serif;letter-spacing:.1em;text-transform:uppercase;color:#88683b}
.exactQuestions3{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:22px 0 4px}
.exactQuestion3{background:#fffdf9;border:1px solid #ddd6c9;padding:20px}
.exactQuestion3 strong{display:block;font:1.18rem/1.25 Georgia,"Times New Roman",serif;font-weight:400;color:#20372a;margin-bottom:7px}
.exactQuestion3 span{display:block;font-size:.84rem;line-height:1.55;color:#657068}
.exactPastoral3{background:#eef2ed;border-top:3px solid #789078;padding:24px 26px;margin:30px 0}
.exactPastoral3 strong{display:block;color:#20372a;margin-bottom:7px}
@media(max-width:700px){.exactQuestions3{grid-template-columns:1fr}.exactDepth3 h2{font-size:1.95rem}}
</style>
'''

BLOCKS = {
2: STYLE + '''
<section class="exactDepth3">
<p class="eyebrow">Questions that usually come next</p>
<h2>Is there evidence for God besides what I feel?</h2>
<p>Yes. Christianity does not ask you to build the existence of God on a mood, a worship experience, or a moment when prayer felt unusually close. Scripture points outward as well as inward—to creation, to conscience, to history, and most clearly to Jesus Christ.</p>
<p>That matters when your emotions are exhausted. If God is real only when you feel Him, then pain gets the final vote. But Christian faith says reality is larger than your present perception.</p>
<div class="exactScripture3">“The heavens declare the glory of God; and the firmament sheweth his handywork.”<small>Psalm 19:1 · KJV</small></div>

<h2>Why doesn’t God make Himself impossible to deny?</h2>
<p>That is a fair question. Scripture certainly portrays moments when God reveals Himself dramatically, but it does not describe faith as God overwhelming every human being with an experience so coercive that response becomes mechanical. Instead, He reveals, calls, invites, warns, and gives people real responsibility for what they do with the light they have received.</p>
<p>The Bible’s claim is not that God has left no evidence. It is that evidence and willingness are not always the same issue. Sometimes we need more information. Sometimes we also need to ask whether we are willing to follow the truth if it leads somewhere costly.</p>

<h2>Has God ever actually shown us what He is like?</h2>
<p>This is where Christianity becomes much more specific than a general argument for a Creator. Christians do not merely say, “Something must be out there.” We say God has made Himself known in Jesus.</p>
<div class="exactScripture3">“No man hath seen God at any time; the only begotten Son... he hath declared him.”<small>John 1:18 · KJV</small></div>
<p>If you want to know what Christians mean when they talk about God’s heart, look at Jesus touching lepers, receiving sinners, weeping with mourners, confronting hypocrisy, forgiving enemies, dying on a cross, and rising from the dead. Jesus is not a distraction from the question of God. He is Christianity’s central answer to it.</p>

<h2>What if I need evidence, not reassurance?</h2>
<p>Then investigate. Read one Gospel slowly. Ask what claims the text is actually making. Look at the resurrection question. Bring intellectual objections into the light rather than feeling guilty for having them. John explicitly says he recorded signs so that readers could examine them and believe.</p>
<div class="exactScripture3">“But these are written, that ye might believe that Jesus is the Christ, the Son of God...”<small>John 20:31 · KJV</small></div>
<div class="exactPastoral3"><strong>You do not have to pretend certainty:</strong> if your question is intellectual, treat it intellectually. If your question is wounded, treat the wound honestly too. God is not honored by pretending you have no questions.</div>
<div class="exactQuestions3">
<div class="exactQuestion3"><strong>God feels absent rather than hidden?</strong><span><a href="/answer-01">Read Answer 01 →</a></span></div>
<div class="exactQuestion3"><strong>Wondering what Jesus reveals about God?</strong><span><a href="/answer-10">Read Answer 10 →</a></span></div>
<div class="exactQuestion3"><strong>Questions are becoming doubts?</strong><span><a href="/answer-24">Read Answer 24 →</a></span></div>
<div class="exactQuestion3"><strong>Need the broader topic?</strong><span><a href="/god-feels-far-away">Explore When God Feels Far Away →</a></span></div>
</div>
</section>
''',
5: STYLE + '''
<section class="exactDepth3">
<p class="eyebrow">Questions that usually come next</p>
<h2>Is asking God “why?” a sin?</h2>
<p>No—not automatically. Scripture gives us faithful people who ask “why,” “how long,” and “where are You?” David asks. Habakkuk asks. Job asks. Even Jesus, quoting Psalm 22 from the cross, speaks the language of “Why hast thou forsaken me?”</p>
<p>A question can be an act of faith because you are still directing it toward God. The presence of a question does not tell the whole story of your heart.</p>
<div class="exactScripture3">“How long, O LORD? wilt thou forget me for ever? how long wilt thou hide thy face from me?”<small>Psalm 13:1 · KJV</small></div>

<h2>What is the difference between honest questioning and unbelief?</h2>
<p>One helpful distinction is direction. Honest questioning keeps turning toward God, even when the questions are sharp. A hardened heart eventually decides no answer, correction, or revelation from God will be allowed to matter.</p>
<p>You can ask hard questions and remain teachable. You can tell God you do not understand while still leaving room for the possibility that your perspective is incomplete.</p>
<p class="keyline">Faith does not require you to stop asking. It asks you not to stop listening.</p>

<h2>Why doesn’t God answer the question?</h2>
<p>Sometimes He does give clarity. Sometimes time changes what we can see. And sometimes Scripture gives no promise that we will receive the specific explanation we want in this life. Job receives God’s presence and perspective, but not a tidy explanation of the conversations behind his suffering.</p>
<p>That can feel unsatisfying because what we want is a reason large enough to make the pain feel acceptable. God does not always give us that. He does promise His character, His presence, and an ending larger than the chapter we are presently living.</p>

<h2>What if I keep asking the same question?</h2>
<p>Bring it again. The Psalms repeat themselves because grief repeats itself. You are not required to manufacture closure before you actually have it. At the same time, do not let “why?” become the only question your soul is willing to ask. Eventually other faithful questions can join it: “What is true today?” “What do You want me to do next?” “Who can help me carry this?” “How do I keep this pain from defining everything?”</p>

<h2>Can faith and unanswered questions live together?</h2>
<p>Yes. One of the most honest prayers in Scripture contains both at once: “Lord, I believe; help thou mine unbelief.” Mature faith is not the absence of every unresolved question. It is a growing willingness to keep bringing those questions to Christ.</p>
<div class="exactQuestions3">
<div class="exactQuestion3"><strong>Wondering why God will not explain?</strong><span><a href="/answer-06">Read Answer 06 →</a></span></div>
<div class="exactQuestion3"><strong>What if the explanation never comes?</strong><span><a href="/answer-08">Read Answer 08 →</a></span></div>
<div class="exactQuestion3"><strong>Your questions have become anger?</strong><span><a href="/answer-18">Read Answer 18 →</a></span></div>
<div class="exactQuestion3"><strong>Need the broader framework?</strong><span><a href="/why-god-allows-suffering">Explore Why God Allows Suffering →</a></span></div>
</div>
</section>
''',
7: STYLE + '''
<section class="exactDepth3">
<p class="eyebrow">Questions that usually come next</p>
<h2>Does Romans 8:28 mean everything happens for a reason?</h2>
<p>Romans 8:28 is often reduced to that sentence, but Paul says something more careful and more hopeful. He does not say every event is good. He says God works in “all things” for good to those who love Him and are called according to His purpose.</p>
<p>That means the Christian claim is not that betrayal becomes good because it happened, cancer becomes good because it happened, or death becomes good because it happened. The claim is that God is so redemptive He can take even what is genuinely broken and refuse to let it have the final word.</p>
<div class="exactScripture3">“And we know that all things work together for good to them that love God, to them who are the called according to his purpose.”<small>Romans 8:28 · KJV</small></div>

<h2>What does “good” mean in Romans 8?</h2>
<p>The next verse helps. Romans 8:29 speaks about being conformed to the image of God’s Son. The “good” God is doing is larger than making circumstances pleasant. He is forming people into Christlikeness and moving history toward the redemption Paul has been describing throughout the chapter.</p>
<p>Sometimes good looks like endurance you did not know you could receive. Sometimes it looks like compassion for people you once would not have understood. Sometimes it looks like changed priorities, deeper dependence, reconciliation, ministry, courage, or a future you could not see while the loss was fresh.</p>
<p>But we should be humble. We cannot always identify the good quickly, and we should never pressure a hurting person to produce a lesson on demand.</p>

<h2>Does God calling something redeemable mean I have to call it good?</h2>
<p>No. Joseph told his brothers, “Ye thought evil against me.” He named evil as evil before speaking of God’s ability to use it for good. Redemption does not require dishonest vocabulary.</p>
<div class="exactScripture3">“But as for you, ye thought evil against me; but God meant it unto good...”<small>Genesis 50:20 · KJV</small></div>
<p>You can say, “This should not have happened,” and still believe God is not helpless before what happened.</p>

<h2>What if I cannot see any good yet?</h2>
<p>Then do not invent it. Hope does not require pretending you can see the finished work while you are still standing in the middle of it. Romans 8 itself contains groaning, waiting, weakness, and prayer too deep for words. The promise of verse 28 lives inside that context—not outside it.</p>
<p class="keyline">You do not have to see the good yet to believe God has not surrendered the story.</p>

<h2>Can God redeem something without ever explaining why it happened?</h2>
<p>Yes. Redemption and explanation are different gifts. You may eventually see fruit without ever receiving a complete answer to “why this?” That does not make the fruit fake, and it does not make the unanswered question unimportant.</p>
<div class="exactQuestions3">
<div class="exactQuestion3"><strong>Still wrestling with the suffering itself?</strong><span><a href="/answer-04">Read Answer 04 →</a></span></div>
<div class="exactQuestion3"><strong>What if God never explains it?</strong><span><a href="/answer-08">Read Answer 08 →</a></span></div>
<div class="exactQuestion3"><strong>Still asking “Why me?”</strong><span><a href="/answer-16">Read Answer 16 →</a></span></div>
<div class="exactQuestion3"><strong>Need the broader framework?</strong><span><a href="/why-god-allows-suffering">Explore Why God Allows Suffering →</a></span></div>
</div>
</section>
''',
13: STYLE + '''
<section class="exactDepth3">
<p class="eyebrow">Questions that usually come next</p>
<h2>Does an unanswered prayer mean I did not have enough faith?</h2>
<p>No. Scripture does not allow that conclusion. Paul asked repeatedly for his thorn to be removed, and God answered differently than Paul wanted. Jesus prayed in Gethsemane for the cup to pass if possible, and still walked toward the cross.</p>
<p>Faith is not a technique for forcing God to give the answer we prefer. Faith trusts God enough to ask boldly and still leave the final answer in His hands.</p>
<div class="exactScripture3">“For this thing I besought the Lord thrice, that it might depart from me. And he said unto me, My grace is sufficient for thee...”<small>2 Corinthians 12:8–9 · KJV</small></div>

<h2>Why would God say no to something good?</h2>
<p>Sometimes we simply do not know. A request can be sincere, loving, and morally good, and still not receive the answer we begged for. That is one reason simplistic explanations hurt so much. We should be cautious about claiming to know God’s private reason when Scripture has not told us.</p>
<p>What Christianity gives us instead is the character of the One answering. A child may not understand every decision of a trustworthy father. The unanswered “why” remains painful, but trust can rest on who God has shown Himself to be even before the reason becomes clear.</p>

<h2>Should I keep praying after God seems silent?</h2>
<p>Yes, unless God has made the answer clear in another way. Scripture encourages persistence in prayer. Persistence is not manipulation; it is continued dependence. You can keep asking while also praying, “Not my will, but thine, be done.”</p>
<p>Those two prayers are not enemies: “Please change this” and “Help me trust You if You do not.”</p>

<h2>What do I do when the answer is not the one I wanted?</h2>
<p>Grieve it honestly. A “no” can create a real loss—the future you expected, the healing you hoped for, the relationship you wanted restored, the door you were sure would open. Do not rush past that grief by pretending surrender means you never cared.</p>
<p>Then ask for the grace needed for the answer you actually received. Paul did not get removal; he received sustaining grace. Sometimes the miracle is changed circumstances. Sometimes it is strength for circumstances that did not change.</p>

<h2>Does God’s “no” mean He does not love me?</h2>
<p>No. The cross prevents us from measuring God’s love by whether a specific request receives the answer we hoped for. Christian faith anchors God’s love in what He has already done in Christ, not in whether today’s circumstances feel like affection.</p>
<div class="exactPastoral3"><strong>You can be surrendered and disappointed at the same time:</strong> trust does not require you to pretend the answer did not hurt. Bring both the surrender and the disappointment to God.</div>
<div class="exactQuestions3">
<div class="exactQuestion3"><strong>The “no” has become anger?</strong><span><a href="/answer-18">Read Answer 18 →</a></span></div>
<div class="exactQuestion3"><strong>You do not know what to pray next?</strong><span><a href="/answer-19">Read Answer 19 →</a></span></div>
<div class="exactQuestion3"><strong>You never received an explanation?</strong><span><a href="/answer-08">Read Answer 08 →</a></span></div>
<div class="exactQuestion3"><strong>Need the broader topic?</strong><span><a href="/anger-and-unanswered-prayer">Explore Anger &amp; Unanswered Prayer →</a></span></div>
</div>
</section>
''',
17: STYLE + '''
<section class="exactDepth3">
<p class="eyebrow">Questions that usually come next</p>
<h2>Why can grief feel worse after the first few weeks?</h2>
<p>Sometimes the earliest days are full of people, decisions, meals, phone calls, arrangements, and sheer survival. Later the house gets quieter. Other people return to normal routines. The reality of what has changed can become more visible when the activity around the loss begins to fade.</p>
<p>That does not automatically mean you are getting worse. Sometimes it means you are finally feeling what the first days did not give you room to feel.</p>

<h2>Does a harder season mean I am grieving wrong?</h2>
<p>No. Grief is not a straight line. Anniversaries, birthdays, holidays, places, smells, songs, photographs, and ordinary moments can reopen pain you thought had become more manageable. A difficult week after several better weeks does not erase the progress that came before it.</p>
<p class="keyline">A wave returning does not mean the ocean has carried you back to the beginning.</p>

<h2>Is deep grief the same thing as bitterness?</h2>
<p>No. This distinction is important. Strong sorrow, recurring tears, anger, exhaustion, or missing someone intensely are not automatically bitterness. Bitterness is less about how much something hurts and more about what we begin doing with the hurt—whether it hardens into a settled posture of resentment, revenge, contempt, or refusal to let truth speak into the wound.</p>
<p>Do not shame yourself for grieving deeply. The goal is not to make the pain smaller on command. The goal is to keep the pain moving toward God, truthful community, wise help, and the next faithful step instead of letting it close every door around you.</p>

<h2>What does healthy movement look like when I still hurt?</h2>
<p>Movement can be very small. Getting out of bed. Eating something. Returning a phone call. Going to church. Taking a walk. Saying the person’s name. Talking honestly with a trusted friend. Making an appointment with a counselor or physician when you need more help. Progress is not measured only by whether you cried today.</p>
<p>You can still miss someone terribly and also begin participating in life again. Those realities are not betrayals of each other.</p>

<h2>When should I stop trying to carry grief by myself?</h2>
<p>You were never meant to carry it entirely by yourself. If grief is becoming increasingly isolating, making ordinary life feel impossible, or leaving you afraid you may not stay safe, involve other people now—a trusted friend, pastor, counselor, physician, or another appropriate professional. Asking for help is not admitting defeat. It is refusing isolation.</p>
<div class="exactPastoral3"><strong>One important correction:</strong> “Grief that stops moving becomes bitterness” is a warning about what pain can become, not a diagnosis of everyone whose grief lasts a long time. Long grief is not automatically bitter grief.</div>
<div class="exactQuestions3">
<div class="exactQuestion3"><strong>Feeling guilty that grief still lasts?</strong><span><a href="/answer-15">Read Answer 15 →</a></span></div>
<div class="exactQuestion3"><strong>Still asking why this happened?</strong><span><a href="/answer-16">Read Answer 16 →</a></span></div>
<div class="exactQuestion3"><strong>Your grief has become anger?</strong><span><a href="/answer-18">Read Answer 18 →</a></span></div>
<div class="exactQuestion3"><strong>Need the broader topic?</strong><span><a href="/grief-and-loss">Explore Grief &amp; Loss →</a></span></div>
</div>
</section>
'''
}


def remove_existing(text):
    return re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\s*", "", text, flags=re.S)


def patch(number):
    path = Path(f"answer-{number:02d}.html")
    if not path.exists():
        raise SystemExit(f"Missing {path}")
    text = remove_existing(path.read_text())
    marker = "</article>"
    if marker not in text:
        raise SystemExit(f"No article close in {path}")
    block = f"{START}\n{BLOCKS[number]}\n{END}\n"
    text = text.replace(marker, block + marker, 1)
    path.write_text(text)


for number in BLOCKS:
    patch(number)

print("Strengthened exact-question wave three:", ", ".join(f"answer-{n:02d}" for n in BLOCKS))
