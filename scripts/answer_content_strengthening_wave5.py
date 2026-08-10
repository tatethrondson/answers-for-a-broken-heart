from pathlib import Path
import re

START = "<!-- EXACT-QUESTION-DEPTH-WAVE5-START -->"
END = "<!-- EXACT-QUESTION-DEPTH-WAVE5-END -->"

STYLE = '''
<style>
.exactDepth5{margin:54px 0 18px;padding:38px 0 0;border-top:1px solid #ddd6c9}
.exactDepth5 h2{font:2.2rem/1.08 Georgia,"Times New Roman",serif;font-weight:400;color:#20372a;margin:38px 0 14px}
.exactDepth5 h2:first-of-type{margin-top:0}
.exactDepth5 p{margin:0 0 1.28em}
.exactDepth5 a{color:#2d4937;font-weight:800;text-underline-offset:2px}
.exactScripture5{background:#f6f1e8;border-left:3px solid #b69258;padding:21px 24px;margin:22px 0 27px;font:1.08rem/1.62 Georgia,"Times New Roman",serif;color:#20372a}
.exactScripture5 small{display:block;margin-top:7px;font:700 .68rem/1.35 Arial,Helvetica,sans-serif;letter-spacing:.1em;text-transform:uppercase;color:#88683b}
.exactQuestions5{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:22px 0 4px}
.exactQuestion5{background:#fffdf9;border:1px solid #ddd6c9;padding:20px}
.exactQuestion5 strong{display:block;font:1.18rem/1.25 Georgia,"Times New Roman",serif;font-weight:400;color:#20372a;margin-bottom:7px}
.exactQuestion5 span{display:block;font-size:.84rem;line-height:1.55;color:#657068}
.exactPastoral5{background:#eef2ed;border-top:3px solid #789078;padding:24px 26px;margin:30px 0}
.exactPastoral5 strong{display:block;color:#20372a;margin-bottom:7px}
@media(max-width:700px){.exactQuestions5{grid-template-columns:1fr}.exactDepth5 h2{font-size:1.95rem}}
</style>
'''

BLOCKS = {
    10: STYLE + '''
<section class="exactDepth5">
<p class="eyebrow">Questions that usually come next</p>
<h2>Is it enough that Jesus understands my pain?</h2>
<p>If Christianity ended with a God who merely understood suffering, His sympathy would matter—but it would not be enough. A compassionate observer can sit beside a hospital bed, weep at a funeral, and share your sorrow. What an observer cannot do is defeat death, forgive sin, restore what evil has broken, or guarantee that suffering will not have the final word.</p>
<p>The Christian claim is larger than “Jesus understands.” It is that the One who entered our suffering also acted to rescue us from the deepest things that make this world broken.</p>
<div class="exactScripture5">“But now is Christ risen from the dead, and become the firstfruits of them that slept.”<small>1 Corinthians 15:20 · KJV</small></div>

<h2>What did the cross actually accomplish?</h2>
<p>The cross is not only proof that God is willing to suffer with us. Scripture presents it as the place where Christ bore our sin and made reconciliation with God possible. That means suffering is not merely something Jesus experienced; He entered the brokenness of this world to deal with its deepest spiritual problem.</p>
<p>Calvary does not turn every tragedy into a tidy explanation. It does tell you that God’s response to evil was not distance. He stepped into history, bore cost Himself, and opened the way home.</p>

<h2>Why does the resurrection matter when I am hurting now?</h2>
<p>Because resurrection means the worst thing is not automatically the last thing. Friday was real. The wounds were real. The grave was real. Easter did not pretend those things never happened—it revealed that they were not final.</p>
<p>That becomes the shape of Christian hope. We are not promised a life without tears. We are promised that death, sin, injustice, and grief do not own eternity.</p>
<div class="exactPastoral5"><strong>Jesus does more than sit beside your wound.</strong> He enters it, carries what only He can carry, and promises a future in which suffering does not get the final sentence.</div>

<h2>If Jesus defeated death, why do I still hurt?</h2>
<p>Because Christianity lives between resurrection begun and restoration completed. Christ has risen, but we still wait for the day Scripture describes when death is finally destroyed and tears are wiped away. Hope does not require pretending the present is already heaven.</p>
<p>You can believe Easter and still cry at the grave. In fact, Christian grief is possible precisely because both truths are real: this hurts terribly, and this is not the end.</p>
<div class="exactQuestions5">
<div class="exactQuestion5"><strong>Need to know whether Jesus really understands?</strong><span><a href="/answer-09">Read Answer 09 →</a></span></div>
<div class="exactQuestion5"><strong>Grieving someone who died?</strong><span><a href="/answer-14">Read Answer 14 →</a></span></div>
<div class="exactQuestion5"><strong>Still asking why suffering exists?</strong><span><a href="/answer-04">Read Answer 04 →</a></span></div>
<div class="exactQuestion5"><strong>Need the broader topic?</strong><span><a href="/god-feels-far-away">Explore When God Feels Far Away →</a></span></div>
</div>
</section>
''',
    12: STYLE + '''
<section class="exactDepth5">
<p class="eyebrow">Questions that usually come next</p>
<h2>Am I just as guilty because I am a sinner too?</h2>
<p>No—not automatically. The biblical truth that every person is a sinner does not mean every person is equally responsible for every particular wound. General human sinfulness and specific moral responsibility are not the same question.</p>
<p>If someone lied about you, betrayed you, abused you, manipulated you, assaulted you, or violated a boundary, saying “we are all sinners” does not make the two sides morally identical. Scripture can call you to examine your own heart without asking you to carry someone else’s guilt.</p>
<div class="exactScripture5">“So then every one of us shall give account of himself to God.”<small>Romans 14:12 · KJV</small></div>

<h2>What if I really did contribute to the conflict?</h2>
<p>Then own your part honestly. Repent where you sinned. Apologize where you were wrong. Make restitution where appropriate. Taking responsibility is healthy when you are taking responsibility for what is actually yours.</p>
<p>But repentance is not the same thing as accepting a false equivalence. Two people can both have sinned while one person still bears far greater responsibility for what happened. “I was wrong too” does not always mean “we did the same thing.”</p>
<p class="keyline">You can own your part without carrying theirs.</p>

<h2>What if the person who hurt me keeps pointing out my failures?</h2>
<p>Your failures may be real and still be used as a distraction. One wrong does not erase another. If someone responds to every concern with “But you did…” the conversation can become a way of avoiding responsibility rather than pursuing truth.</p>
<p>A healthy response is specific: “I am willing to deal honestly with what I did. I also need what happened to me to be addressed honestly.” Both conversations can exist without collapsing into one.</p>

<h2>Does forgiving someone mean I must stop naming what they did?</h2>
<p>No. Forgiveness does not require inaccurate language. In Scripture, mercy never depends on pretending sin was not sin. You can forgive while still naming betrayal as betrayal, abuse as abuse, deception as deception, and harm as harm.</p>
<div class="exactPastoral5"><strong>If shame has made you carry everything:</strong> ask, “What is actually mine to confess, repair, or change—and what belongs to the other person?” Humility accepts your own responsibility. False guilt takes responsibility for things that were never yours.</div>
<div class="exactQuestions5">
<div class="exactQuestion5"><strong>Waiting for justice or accountability?</strong><span><a href="/answer-11">Read Answer 11 →</a></span></div>
<div class="exactQuestion5"><strong>Trying to forgive without an apology?</strong><span><a href="/answer-21">Read Answer 21 →</a></span></div>
<div class="exactQuestion5"><strong>Confused about reconciliation and boundaries?</strong><span><a href="/answer-22">Read Answer 22 →</a></span></div>
<div class="exactQuestion5"><strong>Need the broader relationship topic?</strong><span><a href="/forgiveness-and-relational-hurt">Explore Forgiveness & Relational Hurt →</a></span></div>
</div>
</section>
''',
    20: STYLE + '''
<section class="exactDepth5">
<p class="eyebrow">Questions that usually come next</p>
<h2>Why does loving people hurt so much?</h2>
<p>Because love creates attachment, and attachment creates vulnerability. The people capable of bringing us the deepest joy are often the people whose absence, rejection, betrayal, sickness, or death can wound us most deeply. That is not evidence that love was a mistake. It is part of what makes love meaningful.</p>
<p>A heart that cannot be wounded is usually a heart that has stopped letting anyone close enough to matter.</p>
<div class="exactScripture5">“Jesus wept.”<small>John 11:35 · KJV</small></div>

<h2>Does getting hurt mean I loved the wrong way?</h2>
<p>Not necessarily. Sometimes pain is the consequence of unhealthy attachment, poor boundaries, or trusting someone who proved unsafe. Those things are worth learning from. But sometimes you hurt simply because you loved someone sincerely in a world where people leave, fail, change, sin, and die.</p>
<p>Jesus loved people perfectly and was still betrayed, misunderstood, abandoned, rejected, and grieved. Pain by itself is not proof that love was foolish.</p>

<h2>How do I love again without becoming naïve?</h2>
<p>Wisdom does not require emotional isolation. You can remain loving while becoming more discerning. Trust can be earned gradually. Boundaries can protect what is precious. Reconciliation can require repentance. Forgiveness does not automatically reopen every door.</p>
<p>The goal is not to become impossible to hurt. The goal is to become wise enough that fear does not get to decide whether you will ever love again.</p>
<p class="keyline">Healing does not make you unwoundable. It keeps yesterday’s wound from choosing every relationship tomorrow.</p>

<h2>Can boundaries and love exist at the same time?</h2>
<p>Yes. Love seeks another person’s good; unlimited access is a different thing. Jesus loved people deeply and still withdrew, confronted, refused demands, and did not entrust Himself indiscriminately to everyone around Him.</p>
<p>Sometimes loving someone means remaining close. Sometimes it means telling the truth. Sometimes it means creating distance because the relationship is unsafe or destructive.</p>
<div class="exactPastoral5"><strong>If you are afraid to love again:</strong> you do not have to promise your whole future today. Let one safe relationship, one honest conversation, and one healthy boundary teach your heart that vulnerability and wisdom can live together.</div>
<div class="exactQuestions5">
<div class="exactQuestion5"><strong>Someone hurt you and never apologized?</strong><span><a href="/answer-21">Read Answer 21 →</a></span></div>
<div class="exactQuestion5"><strong>Wondering whether to let them back in?</strong><span><a href="/answer-22">Read Answer 22 →</a></span></div>
<div class="exactQuestion5"><strong>Carrying guilt for what happened?</strong><span><a href="/answer-12">Read Answer 12 →</a></span></div>
<div class="exactQuestion5"><strong>Need the broader relationship topic?</strong><span><a href="/forgiveness-and-relational-hurt">Explore Forgiveness & Relational Hurt →</a></span></div>
</div>
</section>
''',
    23: STYLE + '''
<section class="exactDepth5">
<p class="eyebrow">Questions that usually come next</p>
<h2>Am I walking away from God—or from something that was presented as God?</h2>
<p>That distinction matters. Some people think they are rejecting Christianity when what they are actually rejecting is hypocrisy, spiritual manipulation, legalism, abuse of authority, shallow answers, political tribalism, or rules that were treated as though they carried the same weight as Scripture.</p>
<p>Those experiences can distort the face of God so badly that rejecting the distortion feels like rejecting Him. Before you decide what you believe about Christ, make sure Christ Himself is the One you are evaluating.</p>
<div class="exactScripture5">“He that hath seen me hath seen the Father.”<small>John 14:9 · KJV</small></div>

<h2>What if Christians are the reason I want nothing to do with Christianity?</h2>
<p>Christians can sin grievously. Churches can fail people. Leaders can misuse trust. None of that should be minimized with “people are imperfect.” Some wounds deserve repentance, accountability, protection, and time.</p>
<p>But a Christian’s failure is not automatically an accurate portrait of Christ. The fairest test of Christianity is not whether every Christian has resembled Jesus well. It is whether Jesus is who He claimed to be.</p>

<h2>How do I separate Jesus from church hurt?</h2>
<p>Start with the Gospels. Read Jesus before reading arguments about Jesus. Watch how He handles wounded people, hypocritical religion, abusive power, outsiders, doubters, sinners, and people everyone else has reduced to a label.</p>
<p>Then ask two different questions: “What actually happened to me?” and “What does Jesus Himself say and do?” Keeping those questions separate can expose places where someone attached God’s name to something God never asked you to carry.</p>

<h2>Does questioning what I was taught mean I am losing my faith?</h2>
<p>Not necessarily. Every belief should be able to survive honest examination. Some inherited convictions become stronger when tested. Others turn out to have been tradition, preference, fear, or someone else’s interpretation rather than the center of the gospel.</p>
<p>The goal is not deconstruction for its own sake. The goal is truth. If something false has been attached to Jesus, removing it can bring you nearer to Him rather than farther away.</p>
<div class="exactPastoral5"><strong>Do not confuse Jesus with every person who used His name.</strong> You may need to grieve what people did, question what you were taught, and still leave the door open to discovering Christ more clearly than you saw Him before.</div>

<h2>Where should I begin if I am not sure what I believe anymore?</h2>
<p>Begin smaller than rebuilding your whole theology tonight. Read one Gospel. Write down the specific claims you no longer know whether you believe. Separate questions about God from wounds caused by people. Talk with someone who is safe enough not to panic at your questions.</p>
<p>And give Jesus the courtesy of being examined on His own terms.</p>
<div class="exactQuestions5">
<div class="exactQuestion5"><strong>Your questions have become serious doubts?</strong><span><a href="/answer-24">Read Answer 24 →</a></span></div>
<div class="exactQuestion5"><strong>Wondering why God does not show Himself?</strong><span><a href="/answer-02">Read Answer 02 →</a></span></div>
<div class="exactQuestion5"><strong>God feels distant after what happened?</strong><span><a href="/answer-01">Read Answer 01 →</a></span></div>
<div class="exactQuestion5"><strong>Need the broader topic?</strong><span><a href="/doubt-and-church-hurt">Explore Doubt & Church Hurt →</a></span></div>
</div>
</section>
''',
}


def strengthen_answer(number: int, block: str) -> bool:
    path = Path(f"answer-{number:02d}.html")
    if not path.exists():
        print(f"Missing {path}; skipped")
        return False

    text = path.read_text(encoding="utf-8")
    wrapped = START + "\n" + block.strip() + "\n" + END
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)

    if pattern.search(text):
        new_text = pattern.sub(wrapped, text, count=1)
    elif "</article>" in text:
        new_text = text.replace("</article>", wrapped + "\n</article>", 1)
    else:
        print(f"No </article> marker in {path}; skipped")
        return False

    if new_text == text:
        print(f"Already current: {path}")
        return False

    path.write_text(new_text, encoding="utf-8")
    print(f"Strengthened {path}")
    return True


changed = False
for number, block in BLOCKS.items():
    changed = strengthen_answer(number, block) or changed

print("Final exact-question strengthening complete" if changed else "Final exact-question strengthening already current")
