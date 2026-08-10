from pathlib import Path
import base64
import re

CSS_START = "/* FREE-GUIDES-HOME-START */"
CSS_END = "/* FREE-GUIDES-HOME-END */"
HTML_START = "<!-- FREE-GUIDES-HOME-START -->"
HTML_END = "<!-- FREE-GUIDES-HOME-END -->"
BRIDGE_START = "<!-- BOOK-BRIDGE-HOME-START -->"
BRIDGE_END = "<!-- BOOK-BRIDGE-HOME-END -->"

CSS = f'''{CSS_START}
.freeGuidesHome{{padding:64px 0 58px;background:#fbf8f2;border-top:1px solid #eee7db}}
.freeGuidesHead{{display:flex;align-items:end;justify-content:space-between;gap:24px;margin-bottom:25px}}
.freeGuidesHome h2{{font:2.65rem/1.05 Georgia,"Times New Roman",serif;font-weight:400;color:#183024;margin:0 0 9px}}
.freeGuidesHome .guideIntro{{margin:0;color:#667068;max-width:680px;font-size:.9rem;line-height:1.62}}
.guideCards{{display:grid;grid-template-columns:1fr 1fr;gap:15px}}
.guideCard{{display:flex;flex-direction:column;text-decoration:none;background:#fff;border:1px solid #ded8cd;padding:29px;min-height:236px;box-shadow:0 12px 30px rgba(30,44,35,.06);transition:.2s ease}}
.guideCard:hover{{transform:translateY(-2px);box-shadow:0 15px 34px rgba(30,44,35,.10)}}
.guideCard small{{display:block;text-transform:uppercase;letter-spacing:.13em;color:#8b6939;font-weight:800;font-size:.65rem;margin-bottom:8px}}
.guideCard strong{{display:block;font:1.78rem/1.12 Georgia,"Times New Roman",serif;font-weight:400;color:#183024;margin-bottom:10px}}
.guideCard span{{display:block;color:#657068;font-size:.84rem;line-height:1.58}}
.guideCard b{{display:block;margin-top:auto;padding-top:20px;color:#294533;font-size:.74rem;letter-spacing:.04em;text-transform:uppercase}}
.guideCard.featured{{border-top:3px solid #b69258}}
.freeGuidesAll{{font-size:.73rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em;color:#294533;text-decoration:none;white-space:nowrap}}
.homeNote{{margin-top:18px;background:#183024;color:#fff;padding:34px 36px;display:grid;grid-template-columns:1fr .92fr;gap:44px;align-items:center}}
.homeNote .eyebrow{{color:#d8bd87;margin-bottom:8px}}
.homeNote h3{{font:2rem/1.06 Georgia,"Times New Roman",serif;font-weight:400;color:#fff;margin:0 0 8px}}
.homeNote p{{margin:0;color:rgba(255,255,255,.8);font-size:.83rem;line-height:1.58;max-width:590px}}
.homeNoteForm{{display:grid;grid-template-columns:1fr 146px;gap:8px;align-items:start}}
.homeNoteForm input[type="email"]{{width:100%;border:0;background:white;color:#28332d;padding:13px 14px;font-size:.86rem;min-height:47px}}
.homeNoteForm button{{border:1px solid #d8bd87;background:#d8bd87;color:#183024;padding:12px 13px;min-height:47px;font-size:.69rem;letter-spacing:.06em;text-transform:uppercase;font-weight:800;cursor:pointer}}
.homeNoteForm button:hover{{background:#ead9b7}}
.homeNotePrivacy{{grid-column:1/-1;font-size:.64rem;line-height:1.45;color:rgba(255,255,255,.65)}}
.homeNoteHoney{{position:absolute!important;left:-5000px!important;width:1px!important;height:1px!important;overflow:hidden!important}}
.bookBridgeHome{{background:#f0ece4;border-top:1px solid #ded8cd;border-bottom:1px solid #ded8cd;padding:46px 0}}
.bookBridgeInner{{display:grid;grid-template-columns:150px 1fr auto;gap:30px;align-items:center}}
.bookBridgeKicker{{text-transform:uppercase;letter-spacing:.16em;font-size:.66rem;font-weight:800;color:#8b6939}}
.bookBridgeCopy h2{{font:2.15rem/1.08 Georgia,"Times New Roman",serif;font-weight:400;color:#183024;margin:0 0 8px}}
.bookBridgeCopy p{{margin:0;color:#5f6862;font-size:.86rem;line-height:1.58;max-width:670px}}
.bookBridgeActions{{display:flex;gap:9px;flex-wrap:wrap;justify-content:flex-end}}
.bookBridgeActions a{{display:inline-flex;align-items:center;justify-content:center;text-decoration:none;padding:11px 16px;text-transform:uppercase;letter-spacing:.055em;font-size:.68rem;font-weight:800;white-space:nowrap}}
.bookBridgeActions .bookPrimary{{background:#294533;color:#fff;border:1px solid #294533}}
.bookBridgeActions .bookSecondary{{background:transparent;color:#294533;border:1px solid #294533}}
/* Preserve the portrait's native 5:7 framing rather than forcing a short crop. */
.authorInner{{grid-template-columns:180px 1fr;gap:30px;align-items:start}}
.authorPhoto{{width:180px;height:252px;border-radius:6px;object-fit:cover;object-position:center center;box-shadow:0 10px 28px rgba(33,47,38,.14);border:1px solid rgba(41,69,51,.08);background:#eee9df}}
.authorPage img{{width:100%;max-width:350px;height:auto;object-fit:contain;object-position:center;border-radius:6px;box-shadow:var(--shadow);background:#eee9df}}
@media(max-width:900px){{.homeNote{{grid-template-columns:1fr;gap:22px}}.bookBridgeInner{{grid-template-columns:1fr;gap:12px}}.bookBridgeActions{{justify-content:flex-start;margin-top:5px}}}}
@media(max-width:760px){{.freeGuidesHead{{align-items:start;flex-direction:column}}.guideCards{{grid-template-columns:1fr}}.homeNote{{padding:29px 25px}}.homeNoteForm{{grid-template-columns:1fr}}.homeNoteForm button{{width:100%}}.authorInner{{grid-template-columns:1fr;gap:20px}}.authorPhoto{{width:160px;height:224px;object-position:center center}}.authorPage img{{max-width:320px}}}}
{CSS_END}'''

HOME = f'''{HTML_START}<section class="freeGuidesHome"><div class="wrap"><div class="freeGuidesHead"><div><p class="eyebrow">Free Help</p><h2>Start with something useful.</h2><p class="guideIntro">You do not have to buy anything to find help here. These short pastoral guides are designed for the hard moment you are in right now—read one, print one, or send one to somebody you love.</p></div><a class="freeGuidesAll" href="/free-guides">View All Free Guides →</a></div><div class="guideCards"><a class="guideCard featured" href="/2am-guide"><small>Best place to start tonight · 7 Scriptures</small><strong>The 2:00 A.M. Guide</strong><span>Something true to hold onto when the room is quiet, your thoughts are loud, and you do not know what else to do.</span><b>Read the free guide →</b></a><a class="guideCard" href="/can-christians-be-depressed"><small>A Note from Pastor Tate · Depression</small><strong>Can Christians Be Depressed?</strong><span>A gentle biblical answer for the Christian who feels low—and then feels guilty for feeling low. Includes three practical steps for this week.</span><b>Read the free guide →</b></a></div><div class="homeNote"><div><p class="eyebrow">A Note from Pastor Tate</p><h3>Get the next note from Pastor Tate.</h3><p>Every so often, I’ll send a short pastoral note for a question people are actually carrying—grief, doubt, depression, unanswered prayer, forgiveness, and more. I’ll also let you know when <em>Answers for a Broken Heart</em> is ready.</p></div><form class="homeNoteForm" action="https://formsubmit.co/tatethrondson@gmail.com" method="POST"><input type="email" name="email" placeholder="Your email address" aria-label="Your email address" autocomplete="email" required><input type="text" name="_honey" class="homeNoteHoney" tabindex="-1" autocomplete="off"><input type="hidden" name="_subject" value="New Answers for a Broken Heart homepage signup"><input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="_next" value="https://answersforabrokenheart.com/hope-thanks"><input type="hidden" name="interest" value="A Note from Pastor Tate + free guides + book release updates"><input type="hidden" name="source" value="Homepage Free Guides"><button type="submit">Send Me the Next Note</button><div class="homeNotePrivacy">No daily emails. Just occasional pastoral encouragement, new free guides, and book-release updates.</div></form></div></div></section>{HTML_END}'''

BRIDGE = f'''{BRIDGE_START}<section class="bookBridgeHome"><div class="wrap bookBridgeInner"><div class="bookBridgeKicker">The deeper journey</div><div class="bookBridgeCopy"><h2>The guides help with one hard moment. The book goes deeper.</h2><p><em>Answers for a Broken Heart</em> walks through 24 questions people ask when pain makes easy answers feel too small. A website can help you find the question. The book is being written to walk with you through it.</p></div><div class="bookBridgeActions"><a class="bookPrimary" href="?view=book">Explore the Book</a><a class="bookSecondary" href="/answer-04">Read a Sample</a></div></div></section>{BRIDGE_END}'''


def author_data_uri():
    # This is the verified portrait source already proven to render reliably in Safari.
    parts = [Path(f'portrait-clean-v2/part0{i}.b64') for i in range(1, 4)]
    if not all(part.exists() for part in parts):
        raise RuntimeError('Verified clean author portrait chunks are missing; refusing to publish.')
    encoded = ''.join(''.join(part.read_text().split()) for part in parts)
    try:
        image = base64.b64decode(encoded, validate=True)
    except Exception as exc:
        raise RuntimeError('Verified clean author portrait chunks are not valid base64.') from exc
    if len(image) != 6393:
        raise RuntimeError(f'Clean author portrait has unexpected size: {len(image)} bytes.')
    if not (image.startswith(b'\xff\xd8\xff') and image.endswith(b'\xff\xd9')):
        raise RuntimeError('Verified clean author portrait is not a complete JPEG.')
    return 'data:image/jpeg;base64,' + encoded


def patch_index(path):
    text = path.read_text()

    text = re.sub(re.escape(CSS_START) + r".*?" + re.escape(CSS_END) + r"\s*", "", text, flags=re.S)
    text = re.sub(re.escape(HTML_START) + r".*?" + re.escape(HTML_END), "", text, flags=re.S)
    text = re.sub(re.escape(BRIDGE_START) + r".*?" + re.escape(BRIDGE_END), "", text, flags=re.S)
    text = text.replace("</style>", CSS + "\n</style>", 1)

    text = text.replace('<a href="/what-hurts-today">Resources</a>', '<a href="/free-guides">Free Guides</a>')

    embedded_author = author_data_uri()
    text, count = re.subn(r'const AUTHOR="[^"]*";', f'const AUTHOR="{embedded_author}";', text, count=1)
    if count != 1:
        raise RuntimeError('Could not find the homepage AUTHOR source; refusing to publish a partial portrait fix.')

    if '!href.startsWith("/free-guides")' not in text:
        text = text.replace(
            '&&!href.startsWith("/contact")){',
            '&&!href.startsWith("/contact")&&!href.startsWith("/free-guides")&&!href.startsWith("/can-christians-be-depressed")&&!href.startsWith("/2am-guide")){',
            1,
        )

    book_anchor = '<section class="bookBand">'
    if book_anchor in text:
        text = text.replace(book_anchor, HOME + book_anchor, 1)
    else:
        raise RuntimeError('Could not find homepage book band; refusing to publish a partial integration.')

    boundary = '`}\nfunction hurts(){'
    if boundary in text:
        text = text.replace(boundary, BRIDGE + boundary, 1)
    else:
        raise RuntimeError('Could not find homepage function boundary; refusing to publish a partial integration.')

    path.write_text(text)


def patch_thanks(path):
    if not path.exists():
        return
    text = path.read_text()
    if '/can-christians-be-depressed' not in text:
        marker = '</div></div></section></main>'
        extra = '<div style="margin-top:24px;padding:26px;border:1px solid #ddd6c9;background:#fff"><p class="eyebrow">A Note from Pastor Tate</p><h2 style="font-size:2rem;margin:0 0 8px">Can Christians Be Depressed?</h2><p style="margin:0 0 14px;color:#66716a">If emotional heaviness is part of what you are carrying, this new pastoral guide may be the best place to go next.</p><a class="btn" href="/can-christians-be-depressed">Read the Depression Guide →</a></div>'
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
print('Homepage conversion layer current: free help, Pastor Tate invitation, book bridge, nav, sitemap, proven portrait source, and corrected 5:7 portrait framing are current.')
