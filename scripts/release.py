from pathlib import Path
import re

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
    text = text.replace(
        '<p>The site and the book work together: read an answer here, then go deeper in the full book.</p>',
        '<p>The site and the book work together: read an answer here, then go deeper in the full book.</p><p><strong>Publication status:</strong> The book is not yet released. It is currently in final preparation, with preorder options opening before publication.</p>',
    )
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

print("Release pass complete: custom domain, coming-soon messaging, author portrait, and Vercel Web Analytics added.")
