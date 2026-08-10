from pathlib import Path

for path in Path('.').glob('*.html'):
    text = path.read_text(encoding='utf-8')
    original = text

    # Retire the legacy homepage router URL now that /about is a real page.
    text = text.replace('href="/?view=about"', 'href="/about"')

    if path.name == '2am-guide.html':
        # The guide is public, linked throughout the site, and included in the sitemap.
        # Make its indexability consistent with that architecture.
        text = text.replace('<meta name="robots" content="noindex,follow">', '')
        if 'rel="canonical"' not in text:
            text = text.replace(
                '<title>The 2:00 A.M. Guide | Answers for a Broken Heart</title>',
                '<title>The 2:00 A.M. Guide | Answers for a Broken Heart</title>'
                '<meta name="description" content="Seven KJV Scriptures, short pastoral reminders, and simple prayers for the middle of the night when your thoughts are loud and you need something true to hold onto.">'
                '<link rel="canonical" href="https://answersforabrokenheart.com/2am-guide">',
                1,
            )
        text = text.replace(
            '<a class="btn" href="/what-hurts-today">Browse All 24 Answers</a>',
            '<a class="btn" href="/all-answers">Browse All 24 Answers</a>',
        )

    if text != original:
        path.write_text(text, encoding='utf-8')
        print('Polished', path.name)
