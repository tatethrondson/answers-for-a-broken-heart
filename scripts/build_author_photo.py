from pathlib import Path
import base64
import re

parts = sorted(Path("portrait-hires").glob("part*.b64"))
if not parts:
    raise SystemExit("No author portrait source found")

encoded = "".join(part.read_text().strip() for part in parts)
outer = base64.b64decode(encoded)

if outer.startswith(b"\xff\xd8"):
    jpeg = outer
else:
    wrapper = outer.decode("utf-8")
    match = re.search(r'data:image/jpeg;base64,([^"<]+)', wrapper, re.I)
    if not match:
        raise SystemExit("Embedded JPEG not found")
    jpeg = base64.b64decode(match.group(1))

if not (jpeg.startswith(b"\xff\xd8") and jpeg.endswith(b"\xff\xd9")):
    raise SystemExit("Author portrait source is not a complete JPEG")

Path("author-tate.jpg").write_bytes(jpeg)

index = Path("index.html")
html = index.read_text()
html = re.sub(
    r'const AUTHOR="[^"]*";',
    'const AUTHOR="/author-tate.jpg?v=6";',
    html,
    count=1,
)
index.write_text(html)

print(f"Built author-tate.jpg ({len(jpeg)} bytes) and wired index.html to the static JPEG.")
