from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]

ANSWER_SLUGS = {
    1: "why-does-god-feel-far-away",
    2: "why-doesnt-god-show-himself",
    3: "why-cant-i-see-what-god-is-doing",
    4: "why-did-god-make-a-world-with-suffering",
    5: "is-it-wrong-to-ask-god-why",
    6: "why-wont-god-tell-me-why",
    7: "can-anything-good-come-from-suffering",
    8: "what-if-the-explanation-never-comes",
    9: "does-god-know-what-this-feels-like",
    10: "is-sympathy-all-god-offers",
    11: "does-god-care-about-injustice",
    12: "am-i-as-guilty-as-the-person-who-hurt-me",
    13: "what-do-i-do-when-god-says-no",
    14: "is-death-really-the-end",
    15: "how-long-am-i-allowed-to-grieve",
    16: "why-did-this-happen-to-me",
    17: "why-does-grief-feel-worse",
    18: "am-i-allowed-to-be-angry-with-god",
    19: "what-do-i-say-to-god-right-now",
    20: "why-does-loving-people-hurt",
    21: "how-do-i-forgive-someone-who-isnt-sorry",
    22: "does-forgiveness-mean-reconciliation",
    23: "am-i-walking-away-from-god-or-church-hurt",
    24: "does-doubt-mean-i-was-never-a-believer",
}

SOCIAL_IMAGE = "https://answersforabrokenheart.com/tate-throndson-portrait-2026.jpg"
SOCIAL_ALT = "Answers for a Broken Heart — biblical hope for hard places"

HOME_CSS = r'''<!-- STATIC-HOME-UPGRADE-CSS-START -->
<style>
.homeImmediate{padding:54px 0 58px;background:#f7f3eb;border-top:1px solid #e7e0d5;border-bottom:1px solid #e3dccf}.homeImmediateHead{display:grid;grid-template-columns:.85fr 1.15fr;gap:44px;align-items:end;margin-bottom:24px}.homeImmediateHead h2{font:400 2.35rem/1.08 Georgia,"Times New Roman",serif;color:#183024;margin:0}.homeImmediateHead p{margin:0;color:#5d6761;font-size:.92rem;line-height:1.65}.homeResourceGrid{display:grid;grid-template-columns:1fr 1fr;gap:14px}.homeResource{display:grid;grid-template-columns:88px 1fr;gap:18px;align-items:center;text-decoration:none;background:#fffefb;border:1px solid #ded8cd;padding:22px 24px;transition:.2s ease}.homeResource:hover{transform:translateY(-2px);box-shadow:0 12px 28px rgba(30,44,35,.08)}.homeResourceIcon{width:78px;height:78px;display:flex;align-items:center;justify-content:center;background:#183024;color:#fff;font:400 1.7rem/1 Georgia,"Times New Roman",serif}.homeResource:nth-child(2) .homeResourceIcon{background:#f3dce4;color:#6d4b55}.homeResource small{display:block;text-transform:uppercase;letter-spacing:.13em;color:#88683b;font-size:.62rem;font-weight:800;margin-bottom:5px}.homeResource strong{display:block;font:400 1.38rem/1.18 Georgia,"Times New Roman",serif;color:#183024;margin-bottom:5px}.homeResource span{display:block;color:#657068;font-size:.8rem;line-height:1.5}.homeResource b{display:block;color:#294533;font-size:.72rem;margin-top:8px;text-transform:uppercase;letter-spacing:.04em}@media(max-width:760px){.homeImmediateHead,.homeResourceGrid{grid-template-columns:1fr}.homeImmediateHead{gap:12px}.homeResource{grid-template-columns:70px 1fr;padding:20px}.homeResourceIcon{width:62px;height:62px}}
</style>
<!-- STATIC-HOME-UPGRADE-CSS-END -->'''

STATIC_HOME = r'''<main>
<section class="hero helpHero"><div class="wrap helpHeroInner"><div class="heroCopy"><p class="eyebrow">Biblical hope for hard places</p><h1>Something hurts. You don’t have to know where to begin.</h1><p class="heroLead">Tell me where it hurts, and I’ll help you find a biblical place to begin.</p><div class="heroButtons"><a class="btn primary" href="/start-here">Tell Me Where It Hurts</a> <a class="btn outline" href="/all-answers">Browse the 24 Answers</a></div><div class="promise"><span class="promiseIcon">⌁</span><span>Biblical answers. Real hope. Lasting healing.</span></div></div></div></section>
<section class="section hurts"><div class="wrap"><div class="center"><h2>What Hurts Today?</h2><div class="divider"></div><p class="centerIntro">Pain has a way of isolating us. You don’t have to walk through it alone.<br>Find biblical answers for whatever you’re facing.</p></div><div class="hurtGrid">
<div class="hurtItem"><div class="iconWrap"><svg viewBox="0 0 64 64"><path d="M32 54S8 39 8 21c0-8 5-13 12-13 6 0 10 4 12 8 2-4 6-8 12-8 7 0 12 5 12 13 0 18-24 33-24 33Z"/></svg></div><h3>Grief &amp; Loss</h3><p>When the pain of losing someone feels unbearable.</p><a href="/grief-and-loss">Find Answers →</a></div>
<div class="hurtItem"><div class="iconWrap"><svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="23"/><path d="M25 24c0-5 3-8 8-8 5 0 8 3 8 7 0 4-2 6-6 9-3 2-4 4-4 8"/><path d="M31 47h.01"/></svg></div><h3>Questions &amp; Doubt</h3><p>When you don’t understand what God is doing.</p><a href="/doubt-and-church-hurt">Find Answers →</a></div>
<div class="hurtItem"><div class="iconWrap"><svg viewBox="0 0 64 64"><path d="M18 41h28c7 0 11-4 11-10s-5-10-11-10h-2C42 14 37 10 30 10c-8 0-14 6-15 14-6 1-10 5-10 10 0 4 3 7 7 7h6"/><path d="m32 32-5 11h7l-4 11"/></svg></div><h3>Suffering &amp; Trials</h3><p>When life is hard and you don’t know how much more.</p><a href="/why-god-allows-suffering">Find Answers →</a></div>
<div class="hurtItem"><div class="iconWrap"><svg viewBox="0 0 64 64"><circle cx="32" cy="20" r="10"/><path d="M14 55c1-13 7-20 18-20s17 7 18 20"/></svg></div><h3>Loneliness</h3><p>When you feel forgotten, unseen, or unwanted.</p><a href="/god-feels-far-away">Find Answers →</a></div>
<div class="hurtItem"><div class="iconWrap"><svg viewBox="0 0 64 64"><path d="M18 53c6-18 16-31 31-42"/><path d="M26 39c-8 0-13-4-14-12 8 0 13 4 14 12Z"/><path d="M35 29c0-8 4-13 12-15 0 8-4 13-12 15Z"/><path d="M20 47c-7 1-12-2-15-9 7-1 12 2 15 9Z"/><path d="M42 21c1-7 5-11 12-11-1 7-5 11-12 11Z"/></svg></div><h3>Someone I Love Is Hurting</h3><p>When you want to help without saying the wrong thing.</p><a href="/help-someone">Help Me Help Them →</a></div>
</div><div class="center allTopics"><a class="btn outline" href="/all-answers">View All 24 Answers</a></div><div class="careSafety">If you do not feel safe or the pain has become dangerous, <a href="/unsafe">start here right now →</a></div></div></section>
<section class="homeImmediate"><div class="wrap"><div class="homeImmediateHead"><div><p class="eyebrow">Need something for right now?</p><h2>Something true to hold onto today.</h2></div><p>You do not have to read the whole site to get help. Start with one practical resource you can open, print, or come back to when your thoughts feel heavy.</p></div><div class="homeResourceGrid"><a class="homeResource" href="/2am-guide"><div class="homeResourceIcon">2AM</div><div><small>7 Scriptures · immediate help</small><strong>The 2:00 A.M. Guide</strong><span>For the hour when the room is quiet and your thoughts will not slow down.</span><b>Open the free guide →</b></div></a><a class="homeResource" href="/free-guides#faith-feelings-journals"><div class="homeResourceIcon">♡</div><div><small>30 days · printable journal</small><strong>Faith &amp; Feelings</strong><span>Tell the truth about what you feel, then anchor your heart in what God says is true.</span><b>Get the free journal →</b></div></a></div></div></section>
<!-- HOME-TRUST-START --><section class="trustStrip"><div class="wrap trustStripInner"><img src="/tate-throndson-portrait-2026.jpg?v=1" alt="Tate Throndson"><div><strong>Written from a pastor’s chair, not an ivory tower.</strong><p>Tate Throndson has pastored Castleview Baptist Church since planting it in 2008. These resources grow out of years of preaching, counseling, hospital rooms, funerals, and walking with hurting people.</p></div><a href="/about">Meet Tate →</a></div></section><!-- HOME-TRUST-END -->
<!-- BOOK-BRIDGE-HOME-START --><section class="bookBridgeHome"><div class="wrap bookBridgeInner"><div class="bookBridgeKicker">The deeper journey</div><div class="bookBridgeCopy"><h2>The guides help with one hard moment. The book goes deeper.</h2><p><em>Answers for a Broken Heart</em> walks through 24 questions people ask when pain makes easy answers feel too small. The website can help you find the question. The book goes deeper—walking through all 24 questions with Scripture, pastoral care, and hope.</p></div><div class="bookBridgeActions"><a class="bookPrimary" href="/book">Explore the Book</a><a class="bookSecondary" href="/why-did-god-make-a-world-with-suffering">Read a Sample</a></div></div></section><!-- BOOK-BRIDGE-HOME-END -->
</main>'''

FREE_RESOURCE_CSS = r'''<!-- FAITH-FEELINGS-FEATURE-CSS-START -->
<style>
.featuredJournal{display:grid;grid-template-columns:minmax(0,1.08fr) minmax(340px,.92fr);gap:34px;align-items:stretch;background:#fff;border:1px solid #ded8cd;padding:34px;margin-top:28px}.featuredJournalCopy{padding:8px 4px}.featuredJournalCopy h3{font-size:2.35rem;line-height:1.06;color:#183024;margin:9px 0 14px}.featuredJournalCopy .journalPromise{font:italic 1.12rem/1.55 Georgia,"Times New Roman",serif;color:#5f4d52;border-left:3px solid #be748b;padding-left:18px;margin:20px 0}.featuredJournalCopy p{color:#5e6861}.featuredPills{display:flex;gap:7px;flex-wrap:wrap;margin:18px 0 22px}.featuredPills span{border:1px solid #decfd4;background:#fff8fa;padding:6px 9px;font-size:.67rem;font-weight:800;color:#704f58}.journalPreviewStack{position:relative;min-height:390px;background:linear-gradient(145deg,#f9e8ee,#fff8fa);overflow:hidden;padding:30px;display:flex;align-items:center;justify-content:center}.journalPreviewStack:before{content:"✿";position:absolute;right:22px;top:17px;color:rgba(190,116,139,.35);font-size:3rem}.journalPreviewStack:after{content:"✿";position:absolute;left:18px;bottom:17px;color:rgba(190,116,139,.28);font-size:2rem}.journalPage{position:absolute;width:235px;min-height:315px;background:#fffdfb;border:1px solid #e0d4d6;box-shadow:0 15px 30px rgba(77,53,60,.12);padding:30px 25px;color:#604951}.journalPage.back{transform:translate(28px,-8px) rotate(5deg);opacity:.72}.journalPage.mid{transform:translate(-22px,7px) rotate(-4deg);opacity:.86}.journalPage.front{position:relative;transform:rotate(-1deg);z-index:3}.journalPage small{display:block;text-transform:uppercase;letter-spacing:.13em;font-size:.58rem;color:#a76077;font-weight:800}.journalPage h4{font:400 2.05rem/.97 Georgia,"Times New Roman",serif;margin:12px 0 22px;color:#684d55}.truthPair{display:grid;gap:12px;margin-top:18px}.truthBox{border-top:1px solid #ddcbd0;padding-top:9px}.truthBox strong{display:block;font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;color:#a76077;margin-bottom:8px}.truthLine{height:1px;background:#eadfe2;margin:10px 0}.menJournalCompact{margin-top:18px;background:#183024;color:white;border:1px solid #183024;padding:27px 30px;display:grid;grid-template-columns:1fr auto;gap:28px;align-items:center}.menJournalCompact h3{color:#fff;font-size:1.8rem;margin:5px 0 8px}.menJournalCompact p{margin:0;color:rgba(255,255,255,.78);font-size:.85rem}.menJournalCompact .journalButton{background:#d8bd87;color:#183024;border-color:#d8bd87;white-space:nowrap}.journalNoGate{margin:16px 0 0;font-size:.74rem;color:#657068}.journalNoGate strong{color:#294533}@media(max-width:820px){.featuredJournal{grid-template-columns:1fr;padding:25px}.journalPreviewStack{min-height:350px}.menJournalCompact{grid-template-columns:1fr}.menJournalCompact .journalButton{justify-self:start}}@media(max-width:480px){.journalPreviewStack{min-height:330px;padding:18px}.journalPage{width:205px;min-height:285px;padding:25px 21px}.journalPage h4{font-size:1.75rem}}
</style>
<!-- FAITH-FEELINGS-FEATURE-CSS-END -->'''

FEATURED_JOURNALS = r'''<section class="journals" id="faith-feelings-journals"><div class="wrap"><div class="journalHead"><p class="eyebrow">30-Day Printable Journals</p><h2>Faith &amp; Feelings</h2><p class="intro">Your feelings are real, but they do not have to have the final word. For thirty days, tell the truth about what you feel, place it beside what God says is true, and take one faithful next step.</p></div>
<article class="featuredJournal"><div class="featuredJournalCopy"><small class="cardTag">Free PDF · Women’s Edition</small><h3>Tell the truth about the feeling. Anchor your heart in what is true.</h3><p>Each day gives you room to name what is heavy, a KJV Scripture to bring beside it, a brief word of hope, and one action you can take that day.</p><div class="journalPromise">“Faith is refusing to let the feeling decide what is true.”</div><div class="featuredPills"><span>30 days</span><span>Printable PDF</span><span>KJV Scripture</span><span>One daily action</span><span>No email gate</span></div><button class="journalButton" type="button" onclick="generateFaithFeelingsJournal('women',this)">Download Women’s Journal</button><p class="journalNoGate"><strong>100% free.</strong> Instant PDF download. No email required.</p></div><div class="journalPreviewStack" aria-label="Preview of the Faith and Feelings journal for women"><div class="journalPage back"></div><div class="journalPage mid"></div><div class="journalPage front"><small>Faith &amp; Feelings</small><h4>30-Day Journal<br>for Women</h4><div class="truthPair"><div class="truthBox"><strong>This is how I feel</strong><div class="truthLine"></div><div class="truthLine"></div><div class="truthLine"></div></div><div class="truthBox"><strong>This is what God says is true</strong><div class="truthLine"></div><div class="truthLine"></div><div class="truthLine"></div></div></div></div></div></article>
<article class="menJournalCompact"><div><small style="text-transform:uppercase;letter-spacing:.13em;color:#d8bd87;font-weight:800;font-size:.64rem">Free PDF · Men’s Edition</small><h3>Faith &amp; Feelings for Men</h3><p>The same thirty-day biblical journey in a restrained, straightforward format—with honest prompts, KJV Scripture, room to write, and one concrete action each day.</p></div><button class="journalButton" type="button" onclick="generateFaithFeelingsJournal('men',this)">Download Men’s Journal</button></article><p class="journalNoGate"><strong>No email required.</strong> These journals are free to use, print, and share with someone who needs them.</p><div class="series"><h3>Help first.</h3><p>These resources are here to serve before they promote anything. Use the journal, read an answer, or send a guide to a friend. If it helps you take one honest, faithful step toward hope, it is doing what it was made to do.</p></div></div></section>'''


def write_if_changed(path: Path, text: str):
    old = path.read_text(encoding="utf-8")
    if old != text:
        path.write_text(text, encoding="utf-8")
        print(f"updated {path.name}")


def make_home_static():
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    if "STATIC-HOME-UPGRADE-CSS-START" not in text:
        text = text.replace("</head>", HOME_CSS + "\n</head>", 1)
    if '<main id="app"></main>' in text:
        pattern = re.compile(r'<main id="app"></main>\s*<script>.*?</script>', re.S)
        text, count = pattern.subn(STATIC_HOME, text, count=1)
        if count != 1:
            raise RuntimeError("Could not replace dynamic homepage app exactly once")
    text = text.replace("The book is being written to walk with you through it.", "The book goes deeper—walking through all 24 questions with Scripture, pastoral care, and hope.")
    write_if_changed(path, text)


def feature_free_resources():
    path = ROOT / "free-guides.html"
    text = path.read_text(encoding="utf-8")
    if "FAITH-FEELINGS-FEATURE-CSS-START" not in text:
        text = text.replace("</head>", FREE_RESOURCE_CSS + "\n</head>", 1)
    start = text.find('<section class="journals" id="faith-feelings-journals">')
    signup = text.find('<section class="signup">', start)
    if start == -1 or signup == -1:
        if "featuredJournal" not in text:
            raise RuntimeError("Could not locate Faith & Feelings section")
    else:
        text = text[:start] + FEATURED_JOURNALS + "\n" + text[signup:]
    text = text.replace('/journal-pdf.js?v=1', '/journal-pdf.js?v=2')
    write_if_changed(path, text)


def migrate_answer_urls():
    # Replace internal, canonical, OpenGraph and JSON-LD answer URLs everywhere.
    html_files = list(ROOT.glob("*.html"))
    js_answer_pattern = r'^\/(?:' + '|'.join(re.escape(s) for s in ANSWER_SLUGS.values()) + r'|answer-\d{2})$'
    for path in html_files:
        text = path.read_text(encoding="utf-8")
        for n, slug in ANSWER_SLUGS.items():
            old = f"/answer-{n:02d}"
            text = text.replace(old, f"/{slug}")
        text = text.replace(r'^\/answer-\d{2}$', js_answer_pattern.replace('/', r'\/'))
        # If an answer Article already has schema, give it an image property too.
        if path.name.startswith("answer-") and '"@type": "Article"' in text and '"image":' not in text:
            text = text.replace('"publisher":', f'"image": "{SOCIAL_IMAGE}", "publisher":', 1)
        write_if_changed(path, text)

    sitemap = ROOT / "sitemap.xml"
    text = sitemap.read_text(encoding="utf-8")
    for n, slug in ANSWER_SLUGS.items():
        text = text.replace(f"/answer-{n:02d}", f"/{slug}")
    write_if_changed(sitemap, text)

    config_path = ROOT / "vercel.json"
    config = json.loads(config_path.read_text(encoding="utf-8"))
    redirects = config.setdefault("redirects", [])
    rewrites = config.setdefault("rewrites", [])
    redirect_sources = {x.get("source") for x in redirects}
    rewrite_sources = {x.get("source") for x in rewrites}
    for n, slug in ANSWER_SLUGS.items():
        for source in (f"/answer-{n:02d}", f"/answer-{n:02d}.html"):
            if source not in redirect_sources:
                redirects.append({"source": source, "destination": f"/{slug}", "permanent": True})
                redirect_sources.add(source)
        source = f"/{slug}"
        if source not in rewrite_sources:
            rewrites.append({"source": source, "destination": f"/answer-{n:02d}.html"})
            rewrite_sources.add(source)
    new_config = json.dumps(config, indent=2, ensure_ascii=False) + "\n"
    write_if_changed(config_path, new_config)


def add_social_metadata():
    for path in ROOT.glob("*.html"):
        text = path.read_text(encoding="utf-8")
        if "</head>" not in text:
            continue
        text = text.replace('<meta name="twitter:card" content="summary">', '<meta name="twitter:card" content="summary_large_image">')
        additions = []
        if 'property="og:image"' not in text:
            additions.append(f'<meta property="og:image" content="{SOCIAL_IMAGE}">')
            additions.append(f'<meta property="og:image:alt" content="{SOCIAL_ALT}">')
        if 'name="twitter:card"' not in text:
            additions.append('<meta name="twitter:card" content="summary_large_image">')
        if 'name="twitter:image"' not in text:
            additions.append(f'<meta name="twitter:image" content="{SOCIAL_IMAGE}">')
            additions.append(f'<meta name="twitter:image:alt" content="{SOCIAL_ALT}">')
        if additions:
            block = "<!-- SOCIAL-SHARE-IMAGE-START -->\n" + "\n".join(additions) + "\n<!-- SOCIAL-SHARE-IMAGE-END -->\n"
            text = text.replace("</head>", block + "</head>", 1)
        write_if_changed(path, text)


def validate():
    index = (ROOT / "index.html").read_text(encoding="utf-8")
    assert '<main id="app"></main>' not in index
    assert "STATIC-HOME-UPGRADE-CSS-START" in index
    assert "Need something for right now?" in index
    free = (ROOT / "free-guides.html").read_text(encoding="utf-8")
    assert "featuredJournal" in free and "No email required" in free
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    for n, slug in ANSWER_SLUGS.items():
        assert f"https://answersforabrokenheart.com/{slug}" in sitemap
        assert f"https://answersforabrokenheart.com/answer-{n:02d}" not in sitemap
    config = json.loads((ROOT / "vercel.json").read_text(encoding="utf-8"))
    for n, slug in ANSWER_SLUGS.items():
        assert any(r.get("source") == f"/answer-{n:02d}" and r.get("destination") == f"/{slug}" for r in config["redirects"])
        assert any(r.get("source") == f"/{slug}" and r.get("destination") == f"/answer-{n:02d}.html" for r in config["rewrites"])
    for path in ROOT.glob("answer-*.html"):
        text = path.read_text(encoding="utf-8")
        assert 'property="og:image"' in text
    print("five-part site upgrade validation passed")


if __name__ == "__main__":
    make_home_static()
    feature_free_resources()
    migrate_answer_urls()
    add_social_metadata()
    validate()
