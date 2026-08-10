from pathlib import Path
import html
import json
import re

BASE = "https://answersforabrokenheart.com"
SITE_NAME = "Answers for a Broken Heart"
AUTHOR = "Tate Throndson"
AUTHOR_URL = BASE + "/about"

ANSWERS = {
1: ("Has God really been here the whole time, or have I just told myself that to feel better?", "He’s Always Been There", "God Feels Far Away", "When God feels absent in pain, Scripture shows a God who comes looking for people. A pastoral answer for the night you wonder whether He has really been there."),
2: ("If God is real, why doesn’t He just show Himself?", "He Showed You His Face", "God Feels Far Away", "Creation points toward a Creator, but Jesus shows us His heart. A biblical answer to the question of why God does not simply make Himself visible."),
3: ("Why can’t I see what God is doing right now?", "You’ll See It Looking Back", "God Feels Far Away", "God’s presence is often clearer in the rearview mirror than through the windshield. Biblical hope for seasons that make no sense while you are living them."),
4: ("If God is good, why did He make a world with so much suffering in it?", "This Is Not the World He Made", "Why Did This Happen?", "A biblical answer to the problem of suffering: God called creation very good, sin fractured it, and the world we ache for is the world He intends to restore."),
5: ("Is it wrong that I keep asking God why?", "Honest Questions Are Not Unbelief", "Why Did This Happen?", "Asking God why is not automatically unbelief. Scripture makes room for wounded faith, honest questions, and people who keep turning toward God while they hurt."),
6: ("Why won’t God just tell me why this is happening?", "He Knows More Than You Do", "Why Did This Happen?", "You may not receive the explanation you want, but limited perspective is not evidence of divine neglect. A pastoral biblical answer for unanswered why questions."),
7: ("Can anything good actually come out of this?", "All Things — Even This", "Why Did This Happen?", "Romans 8:28 does not call evil good. It promises that God can redeem even what He never asks you to celebrate. Hope for finding purpose after pain."),
8: ("What do I do when the explanation never comes?", "Sometimes He Gives You Himself Instead of an Explanation", "Why Did This Happen?", "Some suffering never receives a tidy explanation. Job shows that God may answer our deepest questions with His presence rather than a reason."),
9: ("Does God actually know what this feels like?", "He Wept With You", "God Feels Far Away", "Jesus did not observe grief from a distance. He wept at a grave, suffered rejection, and entered human sorrow. Biblical comfort for the person who feels unseen."),
10: ("Isn’t His sympathy enough?", "He Didn’t Just Enter It — He Ended It", "God Feels Far Away", "Jesus did more than sympathize with suffering. At the cross He carried sin and death, and in the resurrection He changed the ending of the story."),
11: ("Does God even care that they’re getting away with it?", "His Silence Isn’t His Approval", "Anger & Unanswered Prayer", "God’s patience is not approval and His silence is not indifference. A biblical answer for injustice, delayed accountability, and the ache of watching wrong go unanswered."),
12: ("Am I just as guilty as the person who hurt me?", "Your Pain and Their Guilt Are Not the Same Conversation", "People Who Hurt Me", "Being a sinner does not make you equally culpable with someone who abused, betrayed, or harmed you. A careful biblical answer about guilt, safety, and justice."),
13: ("What do I do when God says no?", "A ‘No’ Is Not the End of the Story", "Anger & Unanswered Prayer", "Jesus and Paul both prayed prayers God did not answer the way they asked. Biblical hope for trusting God when the answer to your specific prayer is no."),
14: ("Is this really the end?", "Death Does Not Get the Final Word", "Grief & Loss", "The resurrection does not make grief unreal; it makes death temporary. Christian hope for the empty chair, the graveside, and the fear that this is the end."),
15: ("How long am I allowed to still be sad about this?", "You’re Allowed to Grieve as Long as It Takes", "Grief & Loss", "Scripture does not put a timer on grief. The Psalms lament, Jesus weeps, and mourners are promised comfort—not a deadline for feeling better."),
16: ("Why did this happen to me?", "Ask a Different Question", "Grief & Loss", "When you are ready, moving from ‘Why did this happen?’ to ‘What can God do with this?’ can open a door forward without denying what hurt."),
17: ("Why does it feel like I’m getting worse instead of better?", "Grief That Stops Moving Becomes Bitterness", "Grief & Loss", "Healing is not a straight line. Learn the difference between grief that keeps moving toward God and pain that hardens into bitterness."),
18: ("Am I allowed to be furious with God?", "Anger at God Is Not the Opposite of Faith", "Anger & Unanswered Prayer", "Naomi, Habakkuk, Job, and the Psalms show that honest anger can still be addressed to God. Your fury is not automatic proof that faith is gone."),
19: ("What do I even say to God right now?", "Bring Him the Real Prayer, Not the Polished One", "Anger & Unanswered Prayer", "God does not require polished prayers from hurting people. Bring Him the actual anger, confusion, grief, and words you have tonight."),
20: ("Why does loving people hurt so much?", "To Be Loved Is to Be Woundable", "People Who Hurt Me", "Real relationship requires vulnerability, and vulnerability creates the possibility of being wounded. A pastoral answer for betrayal, relational grief, and loss."),
21: ("How am I supposed to forgive someone who never even said sorry?", "Forgiving Them Lets You Look Like Your Father", "People Who Hurt Me", "Forgiveness does not call evil good or require an apology first. It releases personal vengeance to God and reflects the character of the Father."),
22: ("Does forgiving them mean I have to let them back in?", "Forgiveness Is Not Reconciliation", "People Who Hurt Me", "Forgiveness and reconciliation are not the same. You can release a debt before God while maintaining boundaries, consequences, distance, and safety."),
23: ("Am I walking away from God, or from something else wearing His name?", "Make Sure You’re Rejecting the Real Thing", "Doubt & Faith", "Before you reject Christianity, separate Jesus from hypocrisy, abuse, legalism, and promises Scripture never made. You may be rejecting a counterfeit."),
24: ("Does my doubt mean I was never really a believer?", "Your Doubt Is Not Disqualifying", "Doubt & Faith", "Thomas doubted and Jesus moved toward him. Biblical faith can tremble, question, and struggle while still reaching toward Christ."),
}

# Search-facing titles use the plain-language questions people are most likely to type.
# The article H1s stay pastoral and conversational.
SEO_TITLES = {
1: "Why Does God Feel Far Away? | Biblical Answer",
2: "If God Is Real, Why Doesn’t He Show Himself? | Biblical Answer",
3: "Why Can’t I See What God Is Doing? | Biblical Answer",
4: "Why Does God Allow Suffering? | Biblical Answer",
5: "Is It Wrong to Ask God Why? | Biblical Answer",
6: "Why Won’t God Tell Me Why This Is Happening? | Biblical Answer",
7: "Can Anything Good Come From Suffering? | Romans 8:28",
8: "What If God Never Tells Me Why? | Biblical Hope",
9: "Does God Understand My Pain? | Jesus and Suffering",
10: "What Did Jesus Do About Suffering? | Cross and Resurrection",
11: "Does God Care About Injustice? | Biblical Answer",
12: "Am I as Guilty as the Person Who Hurt Me? | Biblical Answer",
13: "What Do I Do When God Says No? | Unanswered Prayer",
14: "Where Is Hope When Someone Dies? | Christian Hope",
15: "How Long Is It Okay to Grieve? | Biblical Grief",
16: "Why Did This Happen to Me? | Biblical Help After Pain",
17: "Why Does Grief Feel Worse Over Time? | Biblical Help",
18: "Is It Okay to Be Angry With God? | Biblical Answer",
19: "What Do I Say to God When I’m Angry? | Honest Prayer",
20: "Why Do People I Love Hurt Me? | Biblical Help",
21: "How to Forgive Someone Who Never Apologized | Biblical Help",
22: "Does Forgiveness Mean Reconciliation? | Biblical Boundaries",
23: "Church Hurt: Am I Walking Away From God? | Biblical Help",
24: "Can Christians Have Doubts? | Doubt and Salvation",
}

RELATED = {
1:[2,3,9], 2:[1,3,10], 3:[1,6,7], 4:[5,6,7], 5:[6,8,18], 6:[5,7,8],
7:[6,8,13], 8:[5,6,10], 9:[10,14,15], 10:[9,13,14], 11:[12,21,22], 12:[11,21,22],
13:[7,8,14], 14:[9,13,15], 15:[14,16,17], 16:[15,17,7], 17:[15,16,18], 18:[19,5,17],
19:[18,8,17], 20:[21,22,15], 21:[20,22,11], 22:[20,21,12], 23:[24,2,10], 24:[23,5,8],
}

HEAD_START = "<!-- SEO-ENHANCEMENTS-START -->"
HEAD_END = "<!-- SEO-ENHANCEMENTS-END -->"
REL_START = "<!-- RELATED-ANSWERS-START -->"
REL_END = "<!-- RELATED-ANSWERS-END -->"
BYLINE_START = "<!-- AUTHOR-BYLINE-START -->"
BYLINE_END = "<!-- AUTHOR-BYLINE-END -->"


def remove_marked(text, start, end):
    return re.sub(re.escape(start) + r".*?" + re.escape(end) + r"\s*", "", text, flags=re.S)


def head_block(title, description, canonical, page_type="article", number=None, question=None):
    graph = []
    if page_type == "website":
        graph.append({
            "@type": "WebSite",
            "@id": BASE + "/#website",
            "url": BASE + "/",
            "name": SITE_NAME,
            "description": description,
            "publisher": {"@type": "Person", "name": AUTHOR, "url": AUTHOR_URL},
        })
    else:
        graph.append({
            "@type": "Article",
            "@id": canonical + "#article",
            "headline": question or title,
            "description": description,
            "mainEntityOfPage": canonical,
            "author": {"@type": "Person", "name": AUTHOR, "url": AUTHOR_URL},
            "publisher": {"@type": "Organization", "name": SITE_NAME, "url": BASE + "/"},
            "isPartOf": {"@type": "WebSite", "name": SITE_NAME, "url": BASE + "/"},
        })
        graph.append({
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type":"ListItem","position":1,"name":"Home","item":BASE + "/"},
                {"@type":"ListItem","position":2,"name":"What Hurts Today?","item":BASE + "/what-hurts-today"},
                {"@type":"ListItem","position":3,"name":f"Answer {number:02d}","item":canonical},
            ],
        })
    data = json.dumps({"@context":"https://schema.org", "@graph":graph}, ensure_ascii=False)
    return f'''{HEAD_START}
<link rel="canonical" href="{html.escape(canonical, quote=True)}">
<meta property="og:type" content="{page_type}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{html.escape(title, quote=True)}">
<meta property="og:description" content="{html.escape(description, quote=True)}">
<meta property="og:url" content="{html.escape(canonical, quote=True)}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{html.escape(title, quote=True)}">
<meta name="twitter:description" content="{html.escape(description, quote=True)}">
<script type="application/ld+json">{data}</script>
<style>
.relatedAnswers{{padding:52px 0;background:#f6f1e8;border-top:1px solid #ddd6c9}}
.relatedAnswers h2{{font:2.15rem/1.1 Georgia,"Times New Roman",serif;font-weight:400;color:#20372a;margin:0 0 8px}}
.relatedAnswers .relatedLead{{margin:0 0 24px;color:#657068}}
.relatedGrid{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}
.relatedCard{{display:block;text-decoration:none;background:#fff;border:1px solid #ddd6c9;padding:22px;transition:.2s ease}}
.relatedCard:hover{{transform:translateY(-2px);box-shadow:0 12px 28px rgba(30,44,35,.08)}}
.relatedCard small{{display:block;text-transform:uppercase;letter-spacing:.12em;color:#88683b;font-weight:800;margin-bottom:7px}}
.relatedCard strong{{display:block;font:1.28rem/1.25 Georgia,"Times New Roman",serif;color:#20372a;font-weight:400;margin-bottom:8px}}
.relatedCard span{{font-size:.82rem;color:#657068}}
.answerByline{{margin-top:10px;font-size:.78rem;line-height:1.5;color:#5f6862}}
.answerByline a{{font-weight:800;color:#294533;text-decoration:none}}
@media(max-width:760px){{.relatedGrid{{grid-template-columns:1fr}}}}
</style>
{HEAD_END}'''


def related_block(number):
    cards = []
    for n in RELATED[number]:
        question, short, category, _ = ANSWERS[n]
        cards.append(
            f'''<a class="relatedCard" href="/answer-{n:02d}"><small>Answer {n:02d} · {html.escape(category)}</small><strong>{html.escape(question)}</strong><span>{html.escape(short)} →</span></a>'''
        )
    return f'''{REL_START}
<section class="relatedAnswers"><div class="wrap"><p class="eyebrow">Related questions</p><h2>You may also be carrying one of these.</h2><p class="relatedLead">Pain rarely asks only one question. Keep going wherever your heart needs to go next.</p><div class="relatedGrid">{''.join(cards)}</div></div></section>
{REL_END}'''


def byline_block():
    return f'''{BYLINE_START}<div class="answerByline">Written by <a href="/about" rel="author">{AUTHOR}</a> · Pastor and author of <em>Answers for a Broken Heart</em></div>{BYLINE_END}'''


def patch_answer(number):
    path = Path(f"answer-{number:02d}.html")
    if not path.exists():
        raise SystemExit(f"Missing {path}")

    question, short, category, description = ANSWERS[number]
    title = SEO_TITLES[number]
    canonical = f"{BASE}/answer-{number:02d}"

    text = path.read_text()
    text = remove_marked(text, HEAD_START, HEAD_END)
    text = remove_marked(text, REL_START, REL_END)
    text = remove_marked(text, BYLINE_START, BYLINE_END)

    text = re.sub(
        r"<title>.*?</title>",
        f"<title>{html.escape(title)}</title>",
        text,
        count=1,
        flags=re.S,
    )

    if re.search(r'<meta\s+name="description"[^>]*>', text, flags=re.I):
        text = re.sub(
            r'<meta\s+name="description"[^>]*>',
            f'<meta name="description" content="{html.escape(description, quote=True)}">',
            text,
            count=1,
            flags=re.I,
        )
    else:
        text = text.replace(
            "</title>",
            f'</title>\n<meta name="description" content="{html.escape(description, quote=True)}">',
            1,
        )

    text = text.replace(
        "</head>",
        head_block(title, description, canonical, "article", number, question) + "\n</head>",
        1,
    )

    text, count = re.subn(
        r'(<div class="meta">.*?</div>)',
        r"\1" + byline_block(),
        text,
        count=1,
        flags=re.S,
    )
    if count != 1:
        raise RuntimeError(f"Could not place author byline in {path}")

    related = related_block(number)
    if '<section class="cta">' in text:
        text = text.replace('<section class="cta">', related + '\n<section class="cta">', 1)
    elif "</main>" in text:
        text = text.replace("</main>", related + "\n</main>", 1)
    else:
        text = text.replace("</footer>", related + "\n</footer>", 1)

    path.write_text(text)


def patch_home():
    path = Path("index.html")
    text = path.read_text()
    text = remove_marked(text, HEAD_START, HEAD_END)

    # Permanent standalone author page. Keep navigation crawlable instead of routing it through the SPA query string.
    text = text.replace('href="?view=about"', 'href="/about"')
    text = text.replace(
        '&&!href.startsWith("/unsafe"))',
        '&&!href.startsWith("/unsafe")&&!href.startsWith("/about"))',
        1,
    )

    title = "Answers for a Broken Heart | Biblical Hope for Life’s Hardest Questions"
    description = (
        "Pastoral, biblical answers for grief, suffering, doubt, unanswered prayer, "
        "relational wounds, and the questions pain asks—without clichés or shallow answers."
    )

    text = re.sub(
        r"<title>.*?</title>",
        f"<title>{html.escape(title)}</title>",
        text,
        count=1,
        flags=re.S,
    )

    if re.search(r'<meta\s+name="description"[^>]*>', text, flags=re.I):
        text = re.sub(
            r'<meta\s+name="description"[^>]*>',
            f'<meta name="description" content="{html.escape(description, quote=True)}">',
            text,
            count=1,
            flags=re.I,
        )
    else:
        text = text.replace(
            "</title>",
            f'</title>\n<meta name="description" content="{html.escape(description, quote=True)}">',
            1,
        )

    text = text.replace(
        "</head>",
        head_block(title, description, BASE + "/", "website") + "\n</head>",
        1,
    )
    path.write_text(text)


def write_sitemap():
    entries = [
        ("/", "monthly", "1.0"),
        ("/what-hurts-today", "weekly", "0.9"),
        ("/about", "monthly", "0.7"),
    ]
    entries.extend((f"/answer-{n:02d}", "monthly", "0.8") for n in range(1, 25))
    entries.extend([
        ("/free-guides", "weekly", "0.7"),
        ("/2am-guide", "monthly", "0.7"),
        ("/can-christians-be-depressed", "monthly", "0.7"),
        ("/help-someone", "monthly", "0.7"),
        ("/contact", "monthly", "0.5"),
    ])

    body = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for path, changefreq, priority in entries:
        url = BASE + path
        body.append(
            f"  <url><loc>{url}</loc><changefreq>{changefreq}</changefreq><priority>{priority}</priority></url>"
        )
    body.append("</urlset>")
    Path("sitemap.xml").write_text("\n".join(body) + "\n")


def write_robots():
    Path("robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n"
    )


patch_home()
for number in range(1, 25):
    patch_answer(number)
write_sitemap()
write_robots()
print(
    "SEO strengthened: custom-domain canonicals, search-intent titles, visible authorship, "
    "structured author data, related answers, complete sitemap, and robots.txt updated."
)
