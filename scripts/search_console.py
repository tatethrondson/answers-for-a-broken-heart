from pathlib import Path
import re

INDEX = Path("index.html")
VERIFICATION = '<meta name="google-site-verification" content="mi3x3E0Ctmdgl8uN4RhmtikDMflwrzSzzLbfFeYDO8w" />'

text = INDEX.read_text()
text = re.sub(r'\n?<meta name="google-site-verification"[^>]*>\n?', '\n', text)

anchor = '<meta name="theme-color" content="#294533">'
if anchor in text:
    text = text.replace(anchor, anchor + '\n' + VERIFICATION, 1)
else:
    viewport = '<meta name="viewport" content="width=device-width,initial-scale=1">'
    if viewport not in text:
        raise RuntimeError('Could not find a safe <head> insertion point for Search Console verification.')
    text = text.replace(viewport, viewport + '\n' + VERIFICATION, 1)

INDEX.write_text(text)
print('Google Search Console verification tag is present on the homepage.')
