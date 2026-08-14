from pathlib import Path
import re

STYLE_LINK = '<link rel="stylesheet" href="/site-interior-v3.css?v=1">'

for path in Path('.').glob('*.html'):
    if path.name == 'index.html':
        # The homepage is the source of truth and keeps its own design untouched.
        continue

    text = path.read_text(encoding='utf-8')
    original = text

    # Remove the older shared-design links. This keeps one visual source of truth.
    text = re.sub(
        r'<!-- HOMEPAGE-DESIGN-SYSTEM-START -->.*?<!-- HOMEPAGE-DESIGN-SYSTEM-END -->',
        '',
        text,
        flags=re.S,
    )
    text = re.sub(
        r'<link\s+rel=["\']stylesheet["\']\s+href=["\']/site-cohesive\.css(?:\?v=\d+)?["\']\s*/?>',
        '',
        text,
        flags=re.I,
    )
    text = re.sub(
        r'<link\s+rel=["\']stylesheet["\']\s+href=["\']/site-interior-v3\.css(?:\?v=\d+)?["\']\s*/?>',
        '',
        text,
        flags=re.I,
    )

    # The premium shell markup stays, but its duplicated inline CSS no longer needs
    # to be repeated on every page because v3 owns the shell styling globally.
    text = re.sub(
        r'<!-- PREMIUM-SHELL-CSS-START -->.*?<!-- PREMIUM-SHELL-CSS-END -->',
        '',
        text,
        flags=re.S,
    )

    # Insert the single shared visual system at the end of <head>, after legacy
    # page-layout CSS, so unique layout structure remains intact while the visual
    # language is normalized.
    if '</head>' in text:
        text = text.replace('</head>', STYLE_LINK + '\n</head>', 1)

    if text != original:
        path.write_text(text, encoding='utf-8')
        print('Normalized design:', path.name)
