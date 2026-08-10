from pathlib import Path
import html
import json
import re

BASE = "https://answersforabrokenheart.com"
SITE_NAME = "Answers for a Broken Heart"
AUTHOR = "Tate Throndson"
AUTHOR_URL = BASE + "/about"

ANSWERS = {
    1: ("Has God really been here the whole time, or have I just told myself that to feel better?", "He’s Always Been There"),
    2: ("If God is real, why doesn’t He just show Himself?", "He Showed You His Face"),
    3: ("Why can’t I see what God is doing right now?", "You’ll See It Looking Back"),
    4: ("If God is good, why did He make a world with so much suffering in it?", "This Is Not the World He Made"),
    5: ("Is it wrong that I keep asking God why?", "Honest Questions Are Not Unbelief"),
    6: ("Why won’t God just tell me why this is happening?", "He Knows More Than You Do"),
    7: ("Can anything good actually come out of this?", "All Things — Even This"),
    8: ("What do I do when the explanation never comes?", "Sometimes He Gives You Himself Instead of an Explanation"),
    9: ("Does God actually know what this feels like?", "He Wept With You"),
    10: ("Isn’t His sympathy enough?", "He Didn’t Just Enter It — He Ended It"),
    11: ("Does God even care that they’re getting away with it?", "His Silence Isn’t His Approval"),
    12: ("Am I just as guilty as the person who hurt me?", "Your Pain and Their Guilt Are Not the Same Conversation"),
    13: ("What do I do when God says no?", "A No Is Not the End of the Story"),
    14: ("Is this really the end?", "Death Does Not Get the Final Word"),
    15: ("How long am I allowed to still be sad about this?", "You’re Allowed to Grieve as Long as It Takes"),
    16: ("Why did this happen to me?", "Ask a Different Question"),
    17: ("Why does it feel like I’m getting worse instead of better?", "Grief That Stops Moving Becomes Bitterness"),
    18: ("Am I allowed to be furious with God?", "Anger at God Is Not the Opposite of Faith"),
    19: ("What do I even say to God right now?", "Bring Him the Real Prayer, Not the Polished One"),
    20: ("Why does loving people hurt so much?", "To Be Loved Is to Be Woundable"),
    21: ("How am I supposed to forgive someone who never even said sorry?", "Forgiving Them Lets You Look Like Your Father"),
    22: ("Does forgiving them mean I have to let them back in?", "Forgiveness Is Not Reconciliation"),
    23: ("Am I walking away from God, or from something else wearing His name?", "Make Sure You’re Rejecting the Real Thing"),
    24: ("Does my doubt mean I was never really a believer?", "Your Doubt Is Not Disqualifying"),
}

HUBS = {
    "grief-and-loss": {
        "name": "Grief & Loss",
        "eyebrow": "Biblical help for grief and loss",
        "title": "Christian Grief & Loss: Biblical Help When Your Heart Is Broken",
        "h1": "When grief changes the shape of your world.",
        "lead": "Loss can make ordinary days feel unfamiliar. Scripture does not rush grieving people past the ache; it gives us room to mourn, hope beyond the grave, and a God who comes near to the brokenhearted.",
        "description": "Biblical help for grief and loss: Christian hope after death, how long grief lasts, why healing can feel worse before better, and how God meets a broken heart.",
        "answers": [14, 15, 16, 17],
        "searches": "Christian grief, biblical help for grief, what the Bible says about grief, grief after death, how long grief lasts",
        "intro": [
            "Grief is not a problem to solve. It is the price love pays when someone or something deeply important is gone. That is why grief can arrive as tears one day, numbness the next, anger after that, and an unexpected ache months later when a song, chair, smell, or date opens the wound again.",
            "The Bible never treats mourning as an embarrassment. Abraham grieved. David grieved. Job grieved. Jesus stood at Lazarus’s grave and wept even though He knew resurrection was coming. Christian hope does not require pretending death is small. It tells the truth about the enemy while refusing to give the enemy the final word.",
        ],
        "truth_title": "Three truths to hold while you grieve",
        "truths": [
            ("Grief is not unbelief.", "You can trust God and still hurt deeply. Tears are not evidence that faith has failed; sometimes they are evidence that love was real."),
            ("There is no biblical stopwatch for sorrow.", "Healing has movement, but not a neat schedule. Scripture gives mourners comfort, companionship, and hope—not a deadline for being over it."),
            ("Death is real, but it is not final.", "The resurrection of Jesus is the center of Christian grief. We mourn honestly because death hurts, and we hope stubbornly because Christ rose."),
        ],
        "tonight": "If tonight is especially hard, do not try to process your entire loss at once. Name what hurts most right now. Tell God the truth about it. Reach for one safe person. Then take the next faithful step—eat something, sleep if you can, step outside, read a Psalm, or simply sit with someone who does not need you to be okay.",
        "related": ["god-feels-far-away", "anger-and-unanswered-prayer", "why-god-allows-suffering"],
    },
    "why-god-allows-suffering": {
        "name": "Why God Allows Suffering",
        "eyebrow": "Suffering, purpose, and the questions pain asks",
        "title": "Why Does God Allow Suffering? Biblical Answers for Pain and Loss",
        "h1": "Why does a good God allow a world that hurts this much?",
        "lead": "This question stops being philosophical when the diagnosis is yours, the funeral is your family’s, or the prayer that went unanswered was the one you could not imagine God saying no to.",
        "description": "Why does God allow suffering? Explore biblical answers about pain, the fall, unanswered why questions, Romans 8:28, purpose, and trusting God without shallow clichés.",
        "answers": [4, 5, 6, 7, 8],
        "searches": "why God allows suffering, why bad things happen, Christian answer to suffering, why God lets us suffer, Romans 8:28 pain",
        "intro": [
            "Pain has a way of turning theology into a personal question. It is one thing to discuss suffering in a classroom. It is another thing to sit beside a hospital bed and ask why God did not stop what He certainly had the power to stop.",
            "Scripture does not answer suffering with one sentence. It gives us a larger story: a world God called very good, a creation fractured by sin, a Savior who entered suffering instead of observing it from a distance, and a promised restoration in which death and pain do not get the final word. That does not answer every why. It does give the why a place to stand.",
        ],
        "truth_title": "A biblical framework for suffering",
        "truths": [
            ("God did not call this broken world very good.", "Genesis begins with goodness. Disease, betrayal, violence, decay, and death belong to a creation Scripture describes as fallen and groaning."),
            ("Questions are not the opposite of faith.", "Job, Habakkuk, David, and the Psalms bring hard questions directly to God. Faith can ask why and still be facing toward Him."),
            ("Redemption is not the same as calling evil good.", "Romans 8:28 does not require you to celebrate what hurt you. It promises God is able to work even through what He never asks you to call good."),
        ],
        "tonight": "If you are searching for a reason tonight, start smaller than a complete explanation. Ask: What part of this feels most impossible to reconcile with God’s goodness? Name that part honestly. Then begin with the answer below that comes closest to the question you are actually carrying.",
        "related": ["grief-and-loss", "god-feels-far-away", "anger-and-unanswered-prayer"],
    },
    "god-feels-far-away": {
        "name": "When God Feels Far Away",
        "eyebrow": "When God seems silent, absent, or hard to recognize",
        "title": "When God Feels Far Away: Biblical Help for God’s Silence",
        "h1": "What do you do when God feels far away?",
        "lead": "Some of the hardest seasons are not the ones in which you stop believing in God, but the ones in which you still believe and cannot seem to find Him.",
        "description": "Biblical help for when God feels far away, silent, absent, or hard to recognize. Explore God’s presence, Jesus in suffering, doubt, and hope when you cannot feel Him.",
        "answers": [1, 2, 3, 9, 10],
        "searches": "God feels far away, why is God silent, where is God in suffering, I cannot feel God, does God understand my pain",
        "intro": [
            "Feeling God’s absence and God actually being absent are not the same thing. Pain can narrow the world until what we feel becomes the only evidence we know how to trust. Scripture repeatedly tells stories of people who could not see what God was doing in the moment and recognized His presence more clearly only later.",
            "Christianity also makes a startling claim: when we ask what God is like in suffering, we do not have to imagine Him from a distance. We look at Jesus. He wept, was rejected, suffered, prayed in agony, died, and rose again. God’s answer to pain is not merely information about Himself. He showed us His face.",
        ],
        "truth_title": "When God feels absent, remember this",
        "truths": [
            ("Presence is not measured by sensation.", "A numb heart can still be held by God. Your inability to feel Him is not proof that He has stopped being near."),
            ("Some of God’s work is clearer looking back.", "Faith often lives through the windshield before it understands in the rearview mirror. Not seeing the plan is not the same as there being no plan."),
            ("Jesus knows suffering from the inside.", "The Christian God did not remain untouched by grief. In Christ, He entered it, wept in it, carried it, and defeated its final claim."),
        ],
        "tonight": "Do not force yourself to manufacture a spiritual feeling. Instead, tell God exactly what His distance feels like. Then anchor yourself to one concrete truth from Scripture, even if your emotions have not caught up yet.",
        "related": ["grief-and-loss", "why-god-allows-suffering", "doubt-and-church-hurt"],
    },
    "anger-and-unanswered-prayer": {
        "name": "Anger & Unanswered Prayer",
        "eyebrow": "For prayers that felt unheard and anger you are afraid to admit",
        "title": "Angry With God? Biblical Help for Unanswered Prayer and God’s Silence",
        "h1": "What do you do with anger when the prayer was not answered?",
        "lead": "You may still love God and be furious about what He allowed. Scripture makes room for prayers that are confused, disappointed, blunt, and painfully honest.",
        "description": "Biblical help for anger at God, unanswered prayer, injustice, and what to say when God says no. Learn how to pray honestly without pretending the hurt is small.",
        "answers": [11, 13, 18, 19],
        "searches": "angry with God, unanswered prayer, when God says no, why God does not answer prayer, what to pray when angry",
        "intro": [
            "Anger can feel dangerous in a Christian life because we assume mature faith should always sound calm. The Bible is much more honest. Habakkuk asks how long God will let injustice continue. Job says things God later corrects. David asks why God has forgotten him. Naomi speaks from deep bitterness. Scripture does not erase these voices; it gives them to us.",
            "The goal is not to make anger the final destination. It is to keep anger moving toward God instead of letting it harden into distance, cynicism, or bitterness. The honest prayer is often safer than the polished silence.",
        ],
        "truth_title": "What honest faith can do with anger",
        "truths": [
            ("God can handle the real prayer.", "Prayer is relationship, not performance. Tell Him what you actually feel before trying to make it sound religious."),
            ("A no is painful without being the end of the story.", "Jesus and Paul both prayed specific prayers that were not answered the way they asked. God’s no did not mean God had left."),
            ("God’s delay is not approval of injustice.", "When wrong appears to go unanswered, Scripture still insists judgment belongs to God. Silence is not the same as indifference."),
        ],
        "tonight": "If you do not know what to pray, use one sentence: “God, this is what hurts, this is what I wanted You to do, and I do not know what to do with the fact that You did not do it.” That is a real prayer. Start there.",
        "related": ["why-god-allows-suffering", "grief-and-loss", "god-feels-far-away"],
    },
    "forgiveness-and-relational-hurt": {
        "name": "Forgiveness & Relational Hurt",
        "eyebrow": "Betrayal, boundaries, forgiveness, and people who wounded you",
        "title": "Biblical Forgiveness, Betrayal and Relational Hurt: Christian Help",
        "h1": "What do you do when the person who hurt you still matters?",
        "lead": "Relational pain is complicated because love, trust, grief, justice, forgiveness, and safety can all be part of the same story—and they are not all the same thing.",
        "description": "Biblical help for betrayal, relational hurt, forgiveness, boundaries, reconciliation, guilt, and loving people after trust has been broken.",
        "answers": [12, 20, 21, 22],
        "searches": "Christian forgiveness, forgive someone who never apologized, forgiveness and reconciliation, biblical boundaries, betrayal and church hurt",
        "intro": [
            "The people who can wound us most deeply are usually the people who were close enough to matter. That is why relational hurt can be so disorienting. You are not only grieving what someone did; you may be grieving what you thought the relationship was, what you hoped it would become, or what you now have to protect yourself from.",
            "Scripture holds truths together that we are tempted to separate. Forgiveness matters. So does justice. Grace matters. So do boundaries. Reconciliation is beautiful when truth and repentance make it possible, but forgiveness and reconciliation are not identical. You can release vengeance to God without pretending trust has been restored.",
        ],
        "truth_title": "Grace and wisdom belong in the same room",
        "truths": [
            ("Your need for grace does not erase their responsibility.", "Being a sinner yourself does not make every wrong equal or require you to minimize specific harm done to you."),
            ("Forgiveness does not call evil good.", "Forgiveness releases personal vengeance to God. It does not rewrite the story, erase consequences, or require an apology before you can begin."),
            ("Forgiveness is not automatic reconciliation.", "Trust can require repentance, truth, safety, and time. Love does not mean universal access to your life."),
        ],
        "tonight": "Name the wound before deciding what the next relationship step should be. Ask two separate questions: What would forgiveness before God look like? And what level of access, if any, would be wise and safe right now? Do not force those into the same answer.",
        "related": ["anger-and-unanswered-prayer", "grief-and-loss", "doubt-and-church-hurt"],
    },
    "doubt-and-church-hurt": {
        "name": "Doubt, Church Hurt & Faith",
        "eyebrow": "When faith feels less certain than it used to",
        "title": "Christian Doubt and Church Hurt: Biblical Help for a Crisis of Faith",
        "h1": "What if the faith you inherited is the thing you are questioning?",
        "lead": "Questions do not automatically mean faith is gone. Sometimes the crisis is intellectual. Sometimes it is grief. Sometimes it is church hurt. And sometimes what is collapsing is a distorted picture of God rather than Christ Himself.",
        "description": "Biblical help for Christian doubt, church hurt, deconstruction, fear of losing faith, and questions about whether doubt means you were never a believer.",
        "answers": [23, 24],
        "searches": "Christian doubt, church hurt, crisis of faith, deconstruction Christianity, can Christians doubt, walking away from God",
        "intro": [
            "A crisis of faith can feel frightening because the questions do not stay in one compartment. A theological question can become an identity question. A painful church experience can become a question about Jesus. A season of suffering can make beliefs that once felt certain suddenly feel borrowed or fragile.",
            "The Bible does not panic around doubters. Thomas said he would not believe without evidence, and Jesus met him. A desperate father prayed, “Lord, I believe; help thou mine unbelief.” Scripture also commends people who tested teaching carefully. Honest examination is not the same thing as rebellion.",
        ],
        "truth_title": "Questions worth separating",
        "truths": [
            ("Church hurt and Jesus are not identical.", "A leader, church, system, or culture can misrepresent Christ. Naming what was wrong is not the same as rejecting Jesus."),
            ("Doubt is not automatic disqualification.", "Faith can tremble and still reach toward Christ. The important question is not whether doubt appeared, but where you take it."),
            ("Test the version of Christianity you are leaving.", "Before rejecting the faith, ask whether the thing collapsing is something Jesus actually taught or something people attached to His name."),
        ],
        "tonight": "Write the doubt in one sentence. Then ask a second question: Is this a question about Jesus, Scripture, suffering, or what someone did in God’s name? Separating those questions can make the next step much clearer.",
        "related": ["god-feels-far-away", "forgiveness-and-relational-hurt", "why-god-allows-suffering"],
    },
}

ANSWER_TO_HUB = {}
for slug, hub in HUBS.items():
    for number in hub["answers"]:
        ANSWER_TO_HUB[number] = slug

HUB_START = "<!-- TOPIC-HUBS-START -->"
HUB_END = "<!-- TOPIC-HUBS-END -->"
ANSWER_HUB_START = "<!-- ANSWER-TOPIC-HUB-START -->"
ANSWER_HUB_END = "<!-- ANSWER-TOPIC-HUB-END -->"

CSS = """
:root{--pine:#294533;--deep:#183024;--cream:#f5f0e7;--paper:#fffefb;--ink:#242a26;--muted:#656d67;--gold:#ad823d;--line:#ded8cd;--soft:#eef2ed}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font-family:Arial,Helvetica,sans-serif;line-height:1.68}a{color:inherit}.wrap{width:min(1120px,calc(100% - 42px));margin:auto}h1,h2,h3{font-family:Georgia,"Times New Roman",serif;font-weight:400;letter-spacing:-.025em}header{position:sticky;top:0;z-index:40;background:rgba(255,254,251,.97);border-bottom:1px solid rgba(33,49,40,.09);backdrop-filter:blur(10px)}.nav{min-height:74px;display:flex;align-items:center;justify-content:space-between;gap:28px}.brand{text-decoration:none;font:1.55rem/.83 Georgia,serif;color:var(--deep)}.brand small{display:block;font-size:.75rem}.navlinks{display:flex;gap:24px;font-size:.78rem;font-weight:700}.navlinks a{text-decoration:none}.hero{background:linear-gradient(120deg,#f7f2e9,#e8efe8);padding:64px 0 58px}.eyebrow{text-transform:uppercase;letter-spacing:.18em;color:var(--gold);font-size:.68rem;font-weight:800;margin:0 0 12px}.hero h1{font-size:clamp(3rem,5.8vw,5.2rem);line-height:1;color:#244432;margin:0 0 18px;max-width:960px}.lead{font:1.18rem/1.58 Georgia,serif;color:#4b5850;max-width:820px;margin:0}.byline{margin-top:18px;font-size:.78rem;color:#5f6862}.byline a{font-weight:800;text-decoration:none;color:var(--pine)}.quick{background:var(--deep);color:white;padding:30px 0}.quickGrid{display:grid;grid-template-columns:.9fr 1.1fr;gap:42px;align-items:center}.quick h2{color:white;font-size:2rem;line-height:1.08;margin:0 0 8px}.quick p{margin:0;color:rgba(255,255,255,.78)}.searchIntent{font-size:.72rem;line-height:1.6;color:rgba(255,255,255,.68);border-left:1px solid rgba(255,255,255,.25);padding-left:24px}.section{padding:54px 0}.intro{font-size:1.03rem;max-width:820px}.intro p{margin:0 0 1.25em}.answerHead{display:flex;justify-content:space-between;gap:24px;align-items:end;margin:44px 0 18px;padding-top:34px;border-top:1px solid var(--line)}.answerHead h2{font-size:2.45rem;line-height:1.08;color:var(--deep);margin:0}.answerHead p{margin:7px 0 0;color:var(--muted);max-width:670px}.answerGrid{display:grid;grid-template-columns:1fr 1fr;gap:14px}.answerCard{display:block;text-decoration:none;background:white;border:1px solid var(--line);padding:24px;transition:.2s ease}.answerCard:hover{transform:translateY(-2px);box-shadow:0 12px 28px rgba(30,44,35,.08)}.answerCard small{display:block;text-transform:uppercase;letter-spacing:.13em;color:#8b6939;font-weight:800;font-size:.64rem}.answerCard h3{font-size:1.45rem;line-height:1.18;margin:7px 0 9px;color:#25382d}.answerCard p{font-size:.83rem;color:#667068;margin:0}.truthSection{background:#f8f5ef;border-top:1px solid #ebe5da;border-bottom:1px solid #e4ded3;padding:55px 0}.truthSection h2{font-size:2.4rem;color:var(--deep);margin:0 0 24px}.truthGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.truth{background:white;border:1px solid var(--line);padding:24px}.truth strong{display:block;font:1.3rem/1.2 Georgia,serif;color:var(--deep);margin-bottom:9px}.truth p{margin:0;color:#5f6862;font-size:.87rem}.tonight{background:var(--deep);color:white;padding:52px 0}.tonightGrid{display:grid;grid-template-columns:.65fr 1.35fr;gap:46px;align-items:start}.tonight h2{font-size:2.35rem;line-height:1.06;color:white;margin:0}.tonight p{font:1.04rem/1.7 Georgia,serif;color:rgba(255,255,255,.86);margin:0}.related{padding:54px 0}.related h2{font-size:2.3rem;color:var(--deep);margin:0 0 20px}.relatedGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.relatedCard{display:block;text-decoration:none;background:#f6f1e8;border:1px solid var(--line);padding:22px}.relatedCard small{display:block;color:#8b6939;font-size:.65rem;font-weight:800;text-transform:uppercase;letter-spacing:.12em;margin-bottom:7px}.relatedCard strong{font:1.3rem/1.2 Georgia,serif;color:var(--deep);font-weight:400}.allHelp{text-align:center;padding-top:26px}.btn{display:inline-block;background:var(--pine);color:white;text-decoration:none;padding:11px 16px;font-size:.74rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em}footer{background:#17291f;color:rgba(255,255,255,.8);padding:31px 0;font-size:.76rem}.footer{display:flex;justify-content:space-between;gap:30px;flex-wrap:wrap}@media(max-width:820px){.navlinks{display:none}.quickGrid,.tonightGrid{grid-template-columns:1fr}.searchIntent{border-left:0;border-top:1px solid rgba(255,255,255,.25);padding:18px 0 0}.answerGrid,.truthGrid,.relatedGrid{grid-template-columns:1fr}.hero h1{font-size:3.25rem}.answerHead{display:block}.truthSection h2{font-size:2rem}}
"""


def esc(value):
    return html.escape(str(value), quote=True)


def structured_data(slug, hub):
    canonical = f"{BASE}/{slug}"
    items = []
    for position, number in enumerate(hub["answers"], start=1):
        question, _ = ANSWERS[number]
        items.append({
            "@type": "ListItem",
            "position": position,
            "name": question,
            "url": f"{BASE}/answer-{number:02d}",
        })
    graph = [
        {
            "@type": "CollectionPage",
            "@id": canonical + "#page",
            "url": canonical,
            "name": hub["title"],
            "description": hub["description"],
            "author": {"@type": "Person", "name": AUTHOR, "url": AUTHOR_URL},
            "isPartOf": {"@type": "WebSite", "name": SITE_NAME, "url": BASE + "/"},
            "mainEntity": {"@id": canonical + "#answers"},
        },
        {
            "@type": "ItemList",
            "@id": canonical + "#answers",
            "numberOfItems": len(items),
            "itemListElement": items,
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
                {"@type": "ListItem", "position": 2, "name": "What Hurts Today?", "item": BASE + "/what-hurts-today"},
                {"@type": "ListItem", "position": 3, "name": hub["name"], "item": canonical},
            ],
        },
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)


def answer_cards(hub):
    cards = []
    for number in hub["answers"]:
        question, short = ANSWERS[number]
        cards.append(
            f'<a class="answerCard" href="/answer-{number:02d}"><small>Answer {number:02d}</small>'
            f'<h3>{esc(question)}</h3><p>{esc(short)} →</p></a>'
        )
    return "".join(cards)


def truth_cards(hub):
    return "".join(
        f'<div class="truth"><strong>{esc(title)}</strong><p>{esc(copy)}</p></div>'
        for title, copy in hub["truths"]
    )


def related_cards(hub):
    cards = []
    for slug in hub["related"]:
        related = HUBS[slug]
        cards.append(
            f'<a class="relatedCard" href="/{slug}"><small>Explore another topic</small>'
            f'<strong>{esc(related["name"])} →</strong></a>'
        )
    return "".join(cards)


def render_hub(slug, hub):
    canonical = f"{BASE}/{slug}"
    paragraphs = "".join(f"<p>{esc(p)}</p>" for p in hub["intro"])
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#294533">
<title>{esc(hub['title'])}</title>
<meta name="description" content="{esc(hub['description'])}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{esc(hub['title'])}">
<meta property="og:description" content="{esc(hub['description'])}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{esc(hub['title'])}">
<meta name="twitter:description" content="{esc(hub['description'])}">
<style>{CSS}</style>
<script type="application/ld+json">{structured_data(slug, hub)}</script>
<script>window.va=window.va||function(){{(window.vaq=window.vaq||[]).push(arguments);}};</script>
<script defer src="/_vercel/insights/script.js"></script>
</head>
<body>
<header><div class="wrap nav"><a class="brand" href="/">Answers<small>for a Broken Heart</small></a><nav class="navlinks"><a href="/what-hurts-today">What Hurts Today?</a><a href="/free-guides">Free Guides</a><a href="/about">About Tate</a><a href="/contact">Contact</a></nav></div></header>
<main>
<section class="hero"><div class="wrap"><p class="eyebrow">{esc(hub['eyebrow'])}</p><h1>{esc(hub['h1'])}</h1><p class="lead">{esc(hub['lead'])}</p><div class="byline">Written by <a href="/about">Tate Throndson</a> · Pastor and author of <em>Answers for a Broken Heart</em></div></div></section>
<section class="quick"><div class="wrap quickGrid"><div><h2>Start with the question closest to today.</h2><p>You do not have to understand the whole story before you take the next step.</p></div><div class="searchIntent"><strong>Common questions this page helps with:</strong><br>{esc(hub['searches'])}</div></div></section>
<section class="section"><div class="wrap"><div class="intro">{paragraphs}</div><div class="answerHead"><div><p class="eyebrow">Choose a question</p><h2>Where does the hurt feel sharpest?</h2><p>Each answer is written to stand on its own. Start with the question that sounds most like the one already running through your mind.</p></div></div><div class="answerGrid">{answer_cards(hub)}</div></div></section>
<section class="truthSection"><div class="wrap"><p class="eyebrow">A place to stand</p><h2>{esc(hub['truth_title'])}</h2><div class="truthGrid">{truth_cards(hub)}</div></div></section>
<section class="tonight"><div class="wrap tonightGrid"><div><p class="eyebrow" style="color:#d8bd87">If this is tonight</p><h2>You only need the next faithful step.</h2></div><p>{esc(hub['tonight'])}</p></div></section>
<section class="related"><div class="wrap"><p class="eyebrow">Related help</p><h2>Pain rarely stays in one category.</h2><div class="relatedGrid">{related_cards(hub)}</div><div class="allHelp"><a class="btn" href="/what-hurts-today">Browse All 24 Answers</a></div></div></section>
</main>
<footer><div class="wrap footer"><div><strong>Answers for a Broken Heart</strong><br>Finding God’s goodness in grief, doubt, and unanswered prayer.</div><div>© 2026 Tate Throndson · Psalm 34:18</div></div></footer>
</body>
</html>'''


def write_hubs():
    for slug, hub in HUBS.items():
        Path(f"{slug}.html").write_text(render_hub(slug, hub))


def topic_cards_block():
    cards = []
    for slug, hub in HUBS.items():
        cards.append(
            f'<a class="topicHubCard" href="/{slug}"><small>Topic guide</small><strong>{esc(hub["name"])}</strong>'
            f'<span>{len(hub["answers"])} biblical answers and a pastoral place to begin →</span></a>'
        )
    return f'''{HUB_START}
<style>
.topicHubs{{padding:42px 0;background:#fff;border-bottom:1px solid #ded8cd}}.topicHubs h2{{font:2.25rem/1.08 Georgia,"Times New Roman",serif;font-weight:400;color:#183024;margin:0 0 8px}}.topicHubs p{{margin:0 0 22px;color:#656d67}}.topicHubGrid{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}}.topicHubCard{{display:block;text-decoration:none;background:#f8f5ef;border:1px solid #ded8cd;padding:20px;transition:.2s ease}}.topicHubCard:hover{{transform:translateY(-2px);box-shadow:0 10px 24px rgba(30,44,35,.08)}}.topicHubCard small{{display:block;text-transform:uppercase;letter-spacing:.12em;color:#8b6939;font-size:.62rem;font-weight:800;margin-bottom:6px}}.topicHubCard strong{{display:block;font:1.3rem/1.18 Georgia,"Times New Roman",serif;color:#183024;font-weight:400;margin-bottom:7px}}.topicHubCard span{{font-size:.78rem;color:#656d67;line-height:1.45}}@media(max-width:820px){{.topicHubGrid{{grid-template-columns:1fr}}}}
</style>
<section class="topicHubs"><div class="wrap"><p class="eyebrow">Explore by topic</p><h2>Start with the kind of hurt you are carrying.</h2><p>These topic guides gather related questions together when you are not sure which single answer to choose first.</p><div class="topicHubGrid">{''.join(cards)}</div></div></section>
{HUB_END}'''


def patch_what_hurts_today():
    path = Path("what-hurts-today.html")
    if not path.exists():
        return
    text = path.read_text()
    text = re.sub(re.escape(HUB_START) + r".*?" + re.escape(HUB_END) + r"\s*", "", text, flags=re.S)
    marker = '<section class="tools" aria-label="Filter answers">'
    if marker in text:
        text = text.replace(marker, topic_cards_block() + "\n" + marker, 1)
    text = text.replace('href="/?view=about"', 'href="/about"')
    path.write_text(text)


def patch_index():
    path = Path("index.html")
    if not path.exists():
        return
    text = path.read_text()
    replacements = {
        'href="/what-hurts-today#grief-loss"': 'href="/grief-and-loss"',
        'href="/what-hurts-today#doubt-faith"': 'href="/doubt-and-church-hurt"',
        'href="/what-hurts-today#why-did-this-happen"': 'href="/why-god-allows-suffering"',
        'href="/what-hurts-today#god-feels-far-away"': 'href="/god-feels-far-away"',
        'href="?view=about"': 'href="/about"',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    # Let the six static topic hubs use normal browser navigation instead of the homepage SPA router.
    if '!href.startsWith("/grief-and-loss")' not in text:
        needle = '&&!href.startsWith("/unsafe")'
        addition = ('&&!href.startsWith("/unsafe")&&!href.startsWith("/grief-and-loss")'
                    '&&!href.startsWith("/why-god-allows-suffering")&&!href.startsWith("/god-feels-far-away")'
                    '&&!href.startsWith("/anger-and-unanswered-prayer")&&!href.startsWith("/forgiveness-and-relational-hurt")'
                    '&&!href.startsWith("/doubt-and-church-hurt")&&!href.startsWith("/about")')
        text = text.replace(needle, addition, 1)
    path.write_text(text)


def patch_answers():
    for number in range(1, 25):
        path = Path(f"answer-{number:02d}.html")
        if not path.exists():
            continue
        text = path.read_text()
        text = re.sub(re.escape(ANSWER_HUB_START) + r".*?" + re.escape(ANSWER_HUB_END) + r"\s*", "", text, flags=re.S)
        slug = ANSWER_TO_HUB[number]
        hub = HUBS[slug]
        link = (
            f'{ANSWER_HUB_START}<div class="answerTopicHub" style="margin-top:6px;font-size:.76rem;color:#657068">'
            f'Explore this topic: <a href="/{slug}" style="font-weight:800;color:#294533;text-decoration:none">{esc(hub["name"])} →</a>'
            f'</div>{ANSWER_HUB_END}'
        )
        marker = '<!-- AUTHOR-BYLINE-END -->'
        if marker in text:
            text = text.replace(marker, marker + link, 1)
        text = text.replace('href="/?view=about"', 'href="/about"')
        path.write_text(text)


def patch_sitemap():
    path = Path("sitemap.xml")
    if not path.exists():
        return
    text = path.read_text()
    lines = []
    for slug in HUBS:
        url = f"{BASE}/{slug}"
        if url not in text:
            lines.append(f'  <url><loc>{url}</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>')
    if lines:
        text = text.replace('</urlset>', '\n'.join(lines) + '\n</urlset>', 1)
    path.write_text(text)


write_hubs()
patch_what_hurts_today()
patch_index()
patch_answers()
patch_sitemap()
print("Six pastoral topic hubs generated and connected to the homepage, What Hurts Today, all 24 answers, and sitemap.")
