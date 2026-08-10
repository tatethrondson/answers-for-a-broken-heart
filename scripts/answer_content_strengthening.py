from pathlib import Path
import re

START = "<!-- EXACT-QUESTION-DEPTH-START -->"
END = "<!-- EXACT-QUESTION-DEPTH-END -->"

STYLE = '''
<style>
.exactDepth{margin:54px 0 18px;padding:38px 0 0;border-top:1px solid #ddd6c9}
.exactDepth h2{font:2.2rem/1.08 Georgia,"Times New Roman",serif;font-weight:400;color:#20372a;margin:38px 0 14px}
.exactDepth h2:first-of-type{margin-top:0}
.exactDepth h3{font:1.48rem/1.2 Georgia,"Times New Roman",serif;font-weight:400;color:#20372a;margin:29px 0 10px}
.exactDepth p{margin:0 0 1.28em}
.exactDepth a{color:#2d4937;font-weight:800;text-underline-offset:2px}
.exactScripture{background:#f6f1e8;border-left:3px solid #b69258;padding:21px 24px;margin:22px 0 27px;font:1.08rem/1.62 Georgia,"Times New Roman",serif;color:#20372a}
.exactScripture small{display:block;margin-top:7px;font:700 .68rem/1.35 Arial,Helvetica,sans-serif;letter-spacing:.1em;text-transform:uppercase;color:#88683b}
.exactQuestions{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:22px 0 4px}
.exactQuestion{background:#fffdf9;border:1px solid #ddd6c9;padding:20px}
.exactQuestion strong{display:block;font:1.18rem/1.25 Georgia,"Times New Roman",serif;font-weight:400;color:#20372a;margin-bottom:7px}
.exactQuestion span{display:block;font-size:.84rem;line-height:1.55;color:#657068}
.exactPastoral{background:#eef2ed;border-top:3px solid #789078;padding:24px 26px;margin:30px 0}
.exactPastoral strong{display:block;color:#20372a;margin-bottom:7px}
@media(max-width:700px){.exactQuestions{grid-template-columns:1fr}.exactDepth h2{font-size:1.95rem}}
</style>
'''

BLOCKS = {
    4: STYLE + '''
<section class="exactDepth">
<p class="eyebrow">Questions that usually come next</p>
<h2>If God is good, why doesn’t He simply stop suffering?</h2>
<p>That is the question underneath many versions of this conversation. Christians believe God is powerful enough to intervene, which means suffering cannot be dismissed with, “God could not do anything about it.” Scripture instead gives us a world in which human choices are real, creation is fallen, bodies break, people hurt one another, and God has not yet removed every consequence of that brokenness.</p>
<p>The Bible does not give us the private reason behind every tragedy. It does give us enough to reject two conclusions: suffering does not prove God is powerless, and suffering does not prove He enjoys what hurts us. The cross shows a God who entered suffering; the resurrection shows a God who intends to defeat it.</p>
<div class="exactScripture">“In the world ye shall have tribulation: but be of good cheer; I have overcome the world.”<small>John 16:33 · KJV</small></div>

<h2>Did God create suffering?</h2>
<p>Genesis begins with a world God called “very good.” Sin enters the story in Genesis 3, and Scripture traces alienation, decay, pain, and death into a creation that is now described as groaning. That matters because Christianity does not ask you to look at cancer, abuse, violence, betrayal, or death and call those things good.</p>
<p>The world is not as it was meant to be, and it is not yet what God promises it will become.</p>

<h2>Is suffering always punishment for something I did?</h2>
<p>No. Sometimes our choices have painful consequences, but Scripture repeatedly warns against treating every sufferer as though pain proves personal guilt. Job’s friends made that mistake. In John 9, Jesus rejected the disciples’ assumption that a man’s blindness could be reduced to a simple question of who sinned.</p>
<p>You may need repentance in some area of life, but pain itself is not a reliable measuring stick for God’s displeasure.</p>

<h2>What about innocent suffering?</h2>
<p>This is where easy answers become especially offensive. When a child suffers, when someone is harmed by another person’s evil, or when tragedy seems completely disconnected from any choice the sufferer made, it is not enough to say, “Everything happens for a reason.” Scripture is more careful than that. It recognizes evil as evil, grief as grief, and injustice as injustice.</p>
<p>Christian hope is not that every terrible event will make sense to us now. It is that evil will be judged, creation will be restored, resurrection is real, and God can redeem what He never asks us to call good.</p>

<div class="exactQuestions">
<div class="exactQuestion"><strong>Still asking “Why me?”</strong><span><a href="/answer-16">Start with Answer 16 →</a></span></div>
<div class="exactQuestion"><strong>Wondering whether any good can come from this?</strong><span><a href="/answer-07">Start with Answer 07 →</a></span></div>
<div class="exactQuestion"><strong>What if God never explains it?</strong><span><a href="/answer-08">Start with Answer 08 →</a></span></div>
<div class="exactQuestion"><strong>Need the broader framework?</strong><span><a href="/why-god-allows-suffering">Explore the Suffering topic guide →</a></span></div>
</div>
</section>
''',
    18: STYLE + '''
<section class="exactDepth">
<p class="eyebrow">Questions that usually come next</p>
<h2>Is anger at God a sin?</h2>
<p>Feeling anger is not the same thing as deciding God is evil, refusing correction, or using pain as permission to sin. Scripture records deeply emotional prayers from Job, David, Habakkuk, Jeremiah, and others. They questioned. They protested. They lamented. The Bible does not edit those prayers out.</p>
<p>But biblical honesty is not the same as making anger our final authority. Faith brings anger into God’s presence and lets truth speak back. You can tell God, “I hate what happened. I do not understand why You allowed it. I am angry,” while still remaining open to His character, His Word, and His correction.</p>
<div class="exactScripture">“How long, O LORD? wilt thou forget me for ever? how long wilt thou hide thy face from me?”<small>Psalm 13:1 · KJV</small></div>

<h2>Will God reject me because I am angry with Him?</h2>
<p>The Psalms suggest the opposite response: bring the real heart to God rather than disappearing from Him. God already knows what you feel. The danger is not that He will discover your anger; the danger is allowing anger to become distance, bitterness, or a settled refusal to trust anything He says.</p>
<p>Wounded faith can still be faith. Sometimes the most faithful thing you can do is keep talking to God while you are hurt.</p>

<h2>What do I pray when I am too angry to pray?</h2>
<p>Start with one honest sentence. “God, I am angry because I wanted You to stop this.” Then tell Him what you lost, what you expected, what feels unfair, and what you are afraid your pain means about Him. You do not need to manufacture calm before you pray.</p>
<p>If you need words for that moment, <a href="/answer-19">What do I even say to God right now?</a> is written specifically for the prayer you cannot polish.</p>

<h2>What if the anger does not go away quickly?</h2>
<p>Do not confuse an emotion that returns with a moral decision to stay bitter. Grief and anger often come in waves. Keep bringing the same wound into the light. Talk with wise people. Pay attention to whether anger is moving toward honesty, lament, wisdom, and surrender—or whether it is becoming isolation, contempt, revenge, and hardness.</p>
<div class="exactPastoral"><strong>A helpful distinction:</strong> anger can be a signal that something precious was lost or something wrong occurred. Let it tell you where the wound is, but do not let it become the only voice that tells you who God is.</div>
<div class="exactQuestions">
<div class="exactQuestion"><strong>God said no to a specific prayer?</strong><span><a href="/answer-13">Read Answer 13 →</a></span></div>
<div class="exactQuestion"><strong>Injustice seems unanswered?</strong><span><a href="/answer-11">Read Answer 11 →</a></span></div>
<div class="exactQuestion"><strong>You cannot find words to pray?</strong><span><a href="/answer-19">Read Answer 19 →</a></span></div>
<div class="exactQuestion"><strong>Need the broader topic?</strong><span><a href="/anger-and-unanswered-prayer">Explore Anger &amp; Unanswered Prayer →</a></span></div>
</div>
</section>
''',
    21: STYLE + '''
<section class="exactDepth">
<p class="eyebrow">Questions that usually come next</p>
<h2>Can I forgive someone who never apologized?</h2>
<p>Yes—but we need to be careful about what we mean by forgiveness. Biblical forgiveness is not pretending the offense did not matter, erasing consequences, or waiting until the offender deserves mercy. It is releasing personal vengeance to God and refusing to make repayment the condition for your own obedience.</p>
<p>An apology can make reconciliation possible. It can acknowledge truth. It can begin rebuilding trust. But your ability to release revenge to God does not have to remain imprisoned by another person’s willingness to say, “I was wrong.”</p>
<div class="exactScripture">“Dearly beloved, avenge not yourselves... Vengeance is mine; I will repay, saith the Lord.”<small>Romans 12:19 · KJV</small></div>

<h2>Does forgiveness mean I have to trust them again?</h2>
<p>No. Forgiveness can be given; trust is rebuilt. Trust depends on truth, character, consistency, repentance, and time. Someone may be forgiven and still not be trustworthy.</p>
<p>That distinction matters especially when the offense was repeated, manipulative, abusive, or unsafe. Forgiveness is not permission for another person to continue harming you.</p>

<h2>Do I have to feel forgiving before I forgive?</h2>
<p>Not necessarily. Forgiveness often begins as obedience before it feels like emotional release. You may decide before God, “I am giving up my right to revenge,” and then discover that the emotions need to be surrendered again tomorrow. That does not make the decision fake. Some wounds require repeated acts of release as healing unfolds.</p>

<h2>Can I forgive and still want justice?</h2>
<p>Yes. Personal vengeance and justice are not identical. Romans 12 tells believers not to avenge themselves; Scripture also recognizes legitimate authority, consequences, truth-telling, and protection of others. Forgiveness does not require hiding what happened or preventing appropriate accountability.</p>

<h2>What if they never change?</h2>
<p>Then reconciliation may never become possible. You can still refuse to let their refusal to repent dictate the condition of your heart before God. Forgiveness allows you to hand the debt to the Judge who sees perfectly. It does not force you to pretend the relationship is restored.</p>
<div class="exactQuestions">
<div class="exactQuestion"><strong>Do I have to let them back in?</strong><span><a href="/answer-22">Read Answer 22 →</a></span></div>
<div class="exactQuestion"><strong>Still wrestling with guilt comparisons?</strong><span><a href="/answer-12">Read Answer 12 →</a></span></div>
<div class="exactQuestion"><strong>Why does loving people hurt this much?</strong><span><a href="/answer-20">Read Answer 20 →</a></span></div>
<div class="exactQuestion"><strong>Need the broader framework?</strong><span><a href="/forgiveness-and-relational-hurt">Explore Forgiveness &amp; Relational Hurt →</a></span></div>
</div>
</section>
''',
    22: STYLE + '''
<section class="exactDepth">
<p class="eyebrow">Questions that usually come next</p>
<h2>What is the difference between forgiveness and reconciliation?</h2>
<p>Forgiveness is what you do with the debt before God. Reconciliation is what happens in the relationship between two people. Forgiveness can begin with one willing heart. Reconciliation requires something from both sides: truth, willingness, and enough safety and trust to move toward restored relationship.</p>
<p>That is why “I forgive you” and “everything is back to normal” are not the same sentence.</p>
<div class="exactScripture">“If it be possible, as much as lieth in you, live peaceably with all men.”<small>Romans 12:18 · KJV</small></div>
<p>Notice the realism in that verse: <em>if it be possible</em> and <em>as much as lieth in you</em>. Peace is worth pursuing, but Scripture recognizes that you do not control the other person.</p>

<h2>Can I forgive someone and still have boundaries?</h2>
<p>Yes. A boundary is not automatically bitterness. Sometimes it is wisdom. You may forgive and still limit contact, change access, require accountability, avoid private situations, or decide that a relationship cannot return to what it was.</p>
<p>Boundaries should not become disguised revenge, but neither should forgiveness become a spiritual excuse for ignoring danger or repeated harm.</p>

<h2>Does reconciliation require repentance?</h2>
<p>Meaningful reconciliation requires truth. If someone refuses to acknowledge what happened, continues the behavior, or demands restored access without changed conduct, the ingredients needed to rebuild a trustworthy relationship are missing.</p>
<p>You can keep your own heart free from vengeance while recognizing that repentance and changed behavior matter when trust is being rebuilt.</p>

<h2>Do I have to restore the relationship?</h2>
<p>Not every relationship can or should return to its previous form. Some relationships can be restored deeply. Others may become cordial but limited. Some may require long-term distance. In situations involving abuse, coercion, threats, or ongoing danger, safety matters, and forgiveness should never be used to pressure someone back into harm.</p>
<div class="exactPastoral"><strong>Keep these separate:</strong> forgiveness answers, “Will I personally live for revenge?” Reconciliation asks, “Can this relationship be restored?” Trust asks, “Has this person become safe and reliable?” Those questions are related, but they are not identical.</div>
<div class="exactQuestions">
<div class="exactQuestion"><strong>No apology ever came?</strong><span><a href="/answer-21">Read Answer 21 →</a></span></div>
<div class="exactQuestion"><strong>Still carrying relational grief?</strong><span><a href="/answer-20">Read Answer 20 →</a></span></div>
<div class="exactQuestion"><strong>Need help separating guilt?</strong><span><a href="/answer-12">Read Answer 12 →</a></span></div>
<div class="exactQuestion"><strong>Need the broader framework?</strong><span><a href="/forgiveness-and-relational-hurt">Explore Forgiveness &amp; Relational Hurt →</a></span></div>
</div>
</section>
''',
    24: STYLE + '''
<section class="exactDepth">
<p class="eyebrow">Questions that usually come next</p>
<h2>Can a real Christian struggle with doubt?</h2>
<p>Yes. Scripture includes people who believed and still wrestled with uncertainty. Thomas wanted evidence. The father in Mark 9 could say, “Lord, I believe; help thou mine unbelief.” The Psalms include believers asking questions that sound much more fragile than polished certainty.</p>
<p>Doubt should be taken seriously, but its presence does not automatically prove faith was never real. Sometimes doubt grows out of intellectual questions. Sometimes it comes from suffering, disappointment, spiritual exhaustion, or what another Christian did in God’s name.</p>
<div class="exactScripture">“Lord, I believe; help thou mine unbelief.”<small>Mark 9:24 · KJV</small></div>

<h2>What is the difference between doubt and unbelief?</h2>
<p>Doubt says, “I am struggling to know whether this is true.” Unbelief can become a settled refusal to trust what God has revealed. Those are not always easy to separate emotionally, but Scripture does not treat every question as rebellion.</p>
<p>The direction of the heart matters. Are you bringing the question toward truth, Scripture, Christ, and wise people—or only looking for permission to stop listening? Honest doubt can ask hard questions and still be willing to follow evidence where it leads.</p>

<h2>What if church hurt caused my doubts?</h2>
<p>Then separate the questions before trying to answer them. What a pastor, church, parent, teacher, or Christian community did may need to be named truthfully. But a Christian misrepresenting Jesus is not the same thing as Jesus being false.</p>
<p>Before you reject God, make sure the thing you are rejecting is actually Him. <a href="/answer-23">Church Hurt: Am I walking away from God?</a> is designed to help make that distinction.</p>

<h2>Does doubt mean I am not saved?</h2>
<p>Assurance should ultimately rest in Christ and His promises, not in your ability to maintain a perfectly steady emotional state. A season of questions does not by itself settle the question of salvation. At the same time, doubt is worth engaging rather than ignoring. Bring the actual question into the light and examine it honestly.</p>

<h2>What should I do with my doubts?</h2>
<p>Write the question in one sentence. Decide what kind of question it is: evidence, Scripture, suffering, morality, church hurt, assurance, or something else. Then pursue that specific question instead of letting a cloud of anxiety stand in for an argument. Read carefully. Ask someone who will not shame you for asking. Pray honestly. Keep looking at Jesus Himself.</p>
<div class="exactPastoral"><strong>You do not need to be afraid of the question.</strong> Truth is not strengthened by pretending questions do not exist. Bring the real doubt into the light where it can be examined.</div>
<div class="exactQuestions">
<div class="exactQuestion"><strong>Church hurt is tangled into the doubt?</strong><span><a href="/answer-23">Read Answer 23 →</a></span></div>
<div class="exactQuestion"><strong>God feels absent rather than intellectually doubtful?</strong><span><a href="/god-feels-far-away">Explore When God Feels Far Away →</a></span></div>
<div class="exactQuestion"><strong>You keep asking God why?</strong><span><a href="/answer-05">Read Answer 05 →</a></span></div>
<div class="exactQuestion"><strong>Need the broader topic?</strong><span><a href="/doubt-and-church-hurt">Explore Doubt &amp; Church Hurt →</a></span></div>
</div>
</section>
''',
}


def patch(number, block):
    path = Path(f"answer-{number:02d}.html")
    if not path.exists():
        raise RuntimeError(f"Missing {path}")
    text = path.read_text()
    text = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\s*", "", text, flags=re.S)
    marker = "</article>"
    if marker not in text:
        raise RuntimeError(f"Could not find article boundary in {path}")
    text = text.replace(marker, START + block + END + "\n" + marker, 1)
    path.write_text(text)


for number, block in BLOCKS.items():
    patch(number, block)

print("Strengthened Answers 04, 18, 21, 22, and 24 around exact-question search intent and natural follow-up questions.")
