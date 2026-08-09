from pathlib import Path

CONTACT_PATH = "/contact"
BASE = "https://answersforabrokenheart.com"


def patch_index():
    path = Path("index.html")
    text = path.read_text()

    # Main navigation: turn the old newsletter anchor into a real author contact page.
    text = text.replace('href="#newsletter">Contact</a>', f'href="{CONTACT_PATH}">Contact Tate</a>')

    # Footer: add Contact Tate after Resources if not already present.
    if f'href="{CONTACT_PATH}">Contact Tate</a>' not in text.split('<footer', 1)[-1]:
        text = text.replace(
            '<a href="/what-hurts-today">Resources</a></div>',
            f'<a href="/what-hurts-today">Resources</a><a href="{CONTACT_PATH}">Contact Tate</a></div>',
            1,
        )

    # Let the static contact page use normal navigation instead of the homepage SPA router.
    if '!href.startsWith("/contact")' not in text:
        text = text.replace(
            '&&!href.startsWith("/what-hurts-today")',
            '&&!href.startsWith("/what-hurts-today")&&!href.startsWith("/contact")',
            1,
        )

    path.write_text(text)


def patch_sitemap():
    path = Path("sitemap.xml")
    if not path.exists():
        return
    text = path.read_text()
    url = BASE + CONTACT_PATH
    if url not in text:
        marker = '</urlset>'
        line = f'  <url><loc>{url}</loc><changefreq>monthly</changefreq><priority>0.6</priority></url>\n'
        text = text.replace(marker, line + marker)
    path.write_text(text)


patch_index()
patch_sitemap()
print("Contact Tate page linked from homepage navigation/footer and added to sitemap.")
