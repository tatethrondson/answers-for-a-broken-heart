from pathlib import Path
import re

for filename in ('index.html', 'free-guides.html'):
    path = Path(filename)
    if not path.exists():
        continue
    text = path.read_text(encoding='utf-8')
    original = text

    # Only the 2:00 A.M. Guide is email-gated. Keep the depression guide clearly open.
    text = re.sub(
        r'(<strong>Can Christians Be Depressed\?</strong>.*?<b>)Get the free guide →(</b>)',
        r'\1Read the free guide →\2',
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(
        r'(<h3>Can Christians Be Depressed\?</h3>.*?<span class="cardLink">)Get the free guide →(</span>)',
        r'\1Read the free guide →\2',
        text,
        count=1,
        flags=re.S,
    )

    if text != original:
        path.write_text(text, encoding='utf-8')
        print('Corrected open-guide CTA in', filename)
