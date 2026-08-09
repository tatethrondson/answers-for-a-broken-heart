from pathlib import Path
import re

CSS_START = "/* FREE-GUIDES-HOME-START */"
CSS_END = "/* FREE-GUIDES-HOME-END */"
HTML_START = "<!-- FREE-GUIDES-HOME-START -->"
HTML_END = "<!-- FREE-GUIDES-HOME-END -->"

CSS = f'''{CSS_START}
.freeGuidesHome{{padding:58px 0;background:#fbf8f2;border-top:1px solid #eee7db}}
.freeGuidesHead{{display:flex;align-items:end;justify-content:space-between;gap:24px;margin-bottom:25px}}
.freeGuidesHome h2{{font:2.55rem/1.05 Georgia,"Times New Roman",serif;font-weight:400;color:#183024;margin:0 0 7px}}
.freeGuidesHome .guideIntro{{margin:0;color:#667068;max-width:650px;font-size:.88rem}}
.guideCards{{display:grid;grid-template-columns:1fr 1fr;gap:15px}}
.guideCard{{display:block;text-decoration:none;background:#fff;border:1px solid #ded8cd;padding:28px;min-height:225px;box-shadow:0 12px 30px rgba(30,44,35,.06);transition:.2s ease}}
.guideCard:hover{{transform:translateY(-2px);box-shadow:0 15px 34px rgba(30,44,35,.10)}}
.guideCard small{{display:block;text-transform:uppercase;letter-spacing:.13em;color:#8b6939;font-weight:800;font-size:.65rem;margin-bottom:8px}}
.guideCard strong{{display:block;font:1.75rem/1.12 Georgia,"Times New Roman",serif;font-weight:400;color:#183024;margin-bottom:10px}}
.guideCard span{{display:block;color:#657068;font-size:.83rem;line-height:1.55}}
.guideCard b{{display:block;margin-top:18px;color:#294533;font-size:.74rem;letter-spacing:.04em;text-transform:uppercase}}
.freeGuidesAll{{font-size:.73rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em;color:#294533;text-decoration:none;white-space:nowrap}}
@media(max-width:760px){{.freeGuidesHead{{align-items:start;flex-direction:column}}.guideCards{{grid-template-columns:1fr}}}}
{CSS_END}'''

HOME = f'''{HTML_START}<section class="freeGuidesHome"><div class="wrap"><div class="freeGuidesHead"><div><p class="eyebrow">Free Resources</p><h2>Guides for the hard days.</h2><p class="guideIntro">Short, pastoral resources you can read right now, print for later, or share with someone who needs a little hope.</p></div><a class="freeGuidesAll" href="/free-guides">View All Free Guides →</a></div><div class="guideCards"><a class="guideCard" href="/2am-guide"><small>Printable · 7 Scriptures</small><strong>The 2:00 A.M. Guide</strong><span>Something true to hold onto when the room is quiet, your thoughts are loud, and you do not know what else to do.</span><b>Read the guide →</b></a><a class="guideCard" href="/can-christians-be-depressed"><small>A Note from Tate · Depression</small><strong>Can Christians Be Depressed?</strong><span>A biblical answer for the Christian who feels low—and then feels guilty for feeling low. Includes three practical steps for this week.</span><b>Read the guide →</b></a></div></div></section>{HTML_END}'''


def patch_index(path):
    text = path.read_text()
    text = re.sub(re.escape(CSS_START) + r".*?" + re.escape(CSS_END) + r"\s*", "", text, flags=re.S)
    text = re.sub(re.escape(HTML_START) + r".*?" + re.escape(HTML_END), "", text, flags=re.S)
    text = text.replace("</style>", CSS + "\n</style>", 1)

    # Give Resources a real destination instead of sending people back to the question hub.
    text = text.replace('<a href="/what-hurts-today">Resources</a>', '<a href="/free-guides">Free Guides</a>')

    # Static resource pages must bypass the SPA router.
    if '!href.startsWith("/free-guides")' not in text:
        text = text.replace(
            '&&!href.startsWith("/contact")){',
            '&&!href.startsWith("/contact")&&!href.startsWith("/free-guides")&&!href.startsWith("/can-christians-be-depressed")&&!href.startsWith("/2am-guide")){',
            1,
        )

    anchor = '<section class="hopeBand" id="newsletter">'
    if anchor in text:
        text = text.replace(anchor, HOME + anchor, 1)
    elif '</main>' in text:
        text = text.replace('</main>', HOME + '</main>', 1)
    path.write_text(text)


def patch_thanks(path):
    if not path.exists():
        return
    text = path.read_text()
    # Give the thank-you page a second immediate resource without changing the signup promise.
    if '/can-christians-be-depressed' not in text:
        marker = '</div></div></section></main>'
        extra = '<div style="margin-top:24px;padding:26px;border:1px solid #ddd6c9;background:#fff"><p class="eyebrow">A Note from Tate</p><h2 style="font-size:2rem;margin:0 0 8px">Can Christians Be Depressed?</h2><p style="margin:0 0 14px;color:#66716a">If emotional heaviness is part of what you are carrying, this new pastoral guide may be the best place to go next.</p><a class="btn" href="/can-christians-be-depressed">Read the Depression Guide →</a></div>'
        text = text.replace(marker, extra + marker, 1)
    path.write_text(text)


def patch_sitemap(path):
    if not path.exists():
        return
    text = path.read_text()
    additions = []
    for url in [
        'https://answersforabrokenheart.com/free-guides',
        'https://answersforabrokenheart.com/can-christians-be-depressed',
    ]:
        if url not in text:
            additions.append(f'<url><loc>{url}</loc></url>')
    if additions and '</urlset>' in text:
        text = text.replace('</urlset>', ''.join(additions) + '</urlset>', 1)
    path.write_text(text)


patch_index(Path('index.html'))
patch_thanks(Path('hope-thanks.html'))
patch_sitemap(Path('sitemap.xml'))
print('Free Guides integration complete: homepage cards, resource nav, thank-you path, and sitemap are current.')
