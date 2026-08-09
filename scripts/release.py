from pathlib import Path
import re

# Vercel Web Analytics enabled in the project dashboard; this commit refreshes production tracking.
OLD_BASE = "https://answers-for-a-broken-heart.vercel.app"
NEW_BASE = "https://answersforabrokenheart.com"

ANALYTICS_START = "<!-- VERCEL-WEB-ANALYTICS-START -->"
ANALYTICS_END = "<!-- VERCEL-WEB-ANALYTICS-END -->"
ANALYTICS = f'''{ANALYTICS_START}
<script>
  window.va = window.va || function () {{ (window.vaq = window.vaq || []).push(arguments); }};
</script>
<script defer src="/_vercel/insights/script.js"></script>
{ANALYTICS_END}'''

START_HERE_CSS_START = "/* START-HERE-CTA-START */"
START_HERE_CSS_END = "/* START-HERE-CTA-END */"
START_HERE_CSS = f'''{START_HERE_CSS_START}
.startHere{{background:#183024;color:white;border-top:1px solid rgba(255,255,255,.08);border-bottom:1px solid rgba(255,255,255,.08)}}
.startHereInner{{min-height:150px;display:grid;grid-template-columns:140px 1fr auto;gap:30px;align-items:center;padding:24px 0}}
.startHereLabel{{font-size:.68rem;letter-spacing:.18em;text-transform:uppercase;font-weight:800;color:#d8bd87}}
.startHereCopy h2{{font-size:2rem;line-height:1.05;color:white;margin:0 0 7px}}
.startHereCopy p{{font-size:.88rem;line-height:1.55;color:rgba(255,255,255,.82);margin:0;max-width:650px}}
.startHere .startBtn{{display:inline-flex;align-items:center;justify-content:center;text-decoration:none;white-space:nowrap;background:white;color:#183024;border:1px solid white;padding:13px 20px;text-transform:uppercase;letter-spacing:.07em;font-size:.72rem;font-weight:800}}
.startHere .startBtn:hover{{background:#f5f0e7}}
@media(max-width:760px){{.startHereInner{{grid-template-columns:1fr;gap:10px;padding:27px 0 30px}}.startHereCopy h2{{font-size:1.85rem}}.startHere .startBtn{{justify-self:start;margin-top:5px}}}}
{START_HERE_CSS_END}'''

START_HERE_HTML_START = "<!-- START-HERE-CTA-START -->"
START_HERE_HTML_END = "<!-- START-HERE-CTA-END -->"
START_HERE_HTML = f'''{START_HERE_HTML_START}<section class="startHere"><div class="wrap startHereInner"><div class="startHereLabel">Start Here</div><div class="startHereCopy"><h2>What hurts today?</h2><p>You don’t need to read this site in order. Start with the question that sounds closest to what you’re carrying, and begin there.</p></div><a class="startBtn" href="/what-hurts-today">Find My Question →</a></div></section>{START_HERE_HTML_END}'''

BADGE_CSS_START = "/* HERO-BADGE-START */"
BADGE_CSS_END = "/* HERO-BADGE-END */"
BADGE_CSS = f'''{BADGE_CSS_START}
.hero .badge{{right:-5px;top:146px;width:158px;height:158px;padding:24px 20px 22px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;text-align:center;font-family:Georgia,"Times New Roman",serif;line-height:1.12}}
.hero .badgeKicker{{display:block;font:800 .56rem/1.1 Arial,Helvetica,sans-serif;letter-spacing:.17em;text-transform:uppercase;color:#e6d2a8;margin-bottom:4px}}
.hero .badgeText{{display:block;max-width:112px;font:1rem/1.16 Georgia,"Times New Roman",serif;color:#fff}}
.hero .badgeTime{{display:block;font:700 1.28rem/1 Georgia,"Times New Roman",serif;color:#fff;margin-top:6px;letter-spacing:-.02em}}
@media(max-width:760px){{.hero .badge{{right:2px;top:132px;width:136px;height:136px;padding:20px 16px}}.hero .badgeKicker{{font-size:.49rem}}.hero .badgeText{{font-size:.89rem;max-width:98px}}.hero .badgeTime{{font-size:1.1rem;margin-top:4px}}}}
{BADGE_CSS_END}'''

BADGE_HTML = '<div class="badge"><span class="badgeKicker">A book for</span><span class="badgeText">the person hurting at</span><span class="badgeTime">2:00 a.m.</span></div>'

PUBLICATION_STATUS = '<p><strong>Publication status:</strong> The book is not yet released. It is currently in final preparation, with preorder options opening before publication.</p>'
BOOK_BRIDGE = '<p>The site and the book work together: read an answer here, then go deeper in the full book.</p>'


def inject_analytics(text):
    text = re.sub(
        re.escape(ANALYTICS_START) + r".*?" + re.escape(ANALYTICS_END) + r"\s*",
        "",
        text,
        flags=re.S,
    )
    if "</head>" in text:
        text = text.replace("</head>", ANALYTICS + "\n</head>", 1)
    return text


def inject_start_here(text):
    # Keep the homepage pathway idempotent across generated deployments.
    text = re.sub(
        re.escape(START_HERE_CSS_START) + r".*?" + re.escape(START_HERE_CSS_END) + r"\s*",
        "",
        text,
        flags=re.S,
    )
    text = re.sub(
        re.escape(START_HERE_HTML_START) + r".*?" + re.escape(START_HERE_HTML_END),
        "",
        text,
        flags=re.S,
    )

    # Add the CTA styling to the main stylesheet.
    if "</style>" in text:
        text = text.replace("</style>", START_HERE_CSS + "\n</style>", 1)

    # Strengthen the hero CTA language.
    text = text.replace(
        '<a class="btn primary" href="/what-hurts-today">What Hurts Today?</a>',
        '<a class="btn primary" href="/what-hurts-today">Start Here — What Hurts Today?</a>',
        1,
    )

    # Place a second, unmistakable pathway immediately below the hero.
    text = text.replace(
        '</section><section class="section hurts">',
        '</section>' + START_HERE_HTML + '<section class="section hurts">',
        1,
    )
    return text


def inject_badge(text):
    # Replace any previous badge enhancement and re-add it cleanly.
    text = re.sub(
        re.escape(BADGE_CSS_START) + r".*?" + re.escape(BADGE_CSS_END) + r"\s*",
        "",
        text,
        flags=re.S,
    )
    if "</style>" in text:
        text = text.replace("</style>", BADGE_CSS + "\n</style>", 1)

    text = re.sub(
        r'<div class="badge">.*?</div>',
        BADGE_HTML,
        text,
        count=1,
        flags=re.S,
    )
    return text


def patch_index(path):
    text = path.read_text()
    text = text.replace(OLD_BASE, NEW_BASE)

    # Use Tate's actual uploaded portrait as an inline JPEG so Safari/Vercel
    # cannot misidentify the file type or serve a stale/broken image path.
    portrait = Path("portrait-inline.b64").read_text().strip()
    author_value = f'data:image/jpeg;base64,{portrait}'
    text = re.sub(
        r'const AUTHOR="[^"]*";',
        lambda _: f'const AUTHOR="{author_value}";',
        text,
        count=1,
    )

    # Make publication status unmistakable everywhere the book is featured.
    text = text.replace(
        '<p class="eyebrow">About the book</p>',
        '<p class="eyebrow">Coming Soon · About the book</p>',
    )
    text = text.replace(
        '<p class="eyebrow">Answers for a Broken Heart</p><h1>A book written for the person who is hurting at 2:00 a.m.</h1>',
        '<p class="eyebrow">Coming Soon · Answers for a Broken Heart</p><h1>A book written for the person who is hurting at 2:00 a.m.</h1>',
    )

    # Normalize the status paragraph so repeated deployments never duplicate it.
    text = text.replace(PUBLICATION_STATUS, "")
    text = text.replace(BOOK_BRIDGE, BOOK_BRIDGE + PUBLICATION_STATUS, 1)

    text = text.replace(
        '<div class="salesCard"><p class="eyebrow">Amazon</p><h3>Buy on Amazon</h3><p>Best for launch-week support, reviews, Prime convenience, Kindle, and standard retail purchasing.</p><strong>Activates when the Amazon listing is live.</strong></div>',
        '<div class="salesCard"><p class="eyebrow">Amazon</p><h3>Kindle preorder — coming soon</h3><p>The Kindle edition can open for preorder before release. The link will appear here as soon as the Amazon listing is ready.</p><strong>Preorders are not open yet.</strong></div>',
    )
    text = text.replace(
        '<div class="salesCard"><p class="eyebrow">Direct</p><h3>Signed copies</h3><p>Order directly for signed copies and future special bundles.</p><strong>Checkout activates before release.</strong></div>',
        '<div class="salesCard"><p class="eyebrow">Direct</p><h3>Signed-copy preorder — coming soon</h3><p>A direct preorder option for signed print copies and future special bundles is being prepared.</p><strong>Direct print preorders will open before release.</strong></div>',
    )
    text = text.replace(
        '<div class="salesCard"><p class="eyebrow">Churches</p><h3>Church & bulk orders</h3><p>Quantity options for pastors, counseling ministries, small groups, conferences, and churches.</p><strong>Bulk ordering is being prepared.</strong></div>',
        '<div class="salesCard"><p class="eyebrow">Churches</p><h3>Church & bulk reservations</h3><p>Quantity options are being prepared for pastors, counseling ministries, small groups, conferences, and churches.</p><strong>Bulk preorder details are coming soon.</strong></div>',
    )

    text = inject_start_here(text)
    text = inject_badge(text)
    path.write_text(inject_analytics(text))


def patch_html(path):
    text = path.read_text().replace(OLD_BASE, NEW_BASE)
    path.write_text(inject_analytics(text))


def patch_text_file(path):
    if path.exists():
        path.write_text(path.read_text().replace(OLD_BASE, NEW_BASE))


index = Path("index.html")
patch_index(index)

for path in Path(".").glob("*.html"):
    if path.name != "index.html":
        patch_html(path)

patch_text_file(Path("sitemap.xml"))
patch_text_file(Path("robots.txt"))

print("Release pass complete: custom domain, coming-soon messaging, author portrait, Start Here pathway, refined hero badge, and Vercel Web Analytics added.")
