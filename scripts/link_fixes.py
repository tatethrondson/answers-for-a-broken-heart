from pathlib import Path

# Keep semantic destinations current. These are links that may technically redirect,
# but send the visitor somewhere different from what the visible CTA promises.
fixes = {
    'help-someone.html': [
        (
            '<a class="btn" href="/what-hurts-today">Browse What Hurts Today?</a>',
            '<a class="btn" href="/all-answers">Browse All 24 Answers</a>'
        ),
    ],
}

for filename, replacements in fixes.items():
    path = Path(filename)
    if not path.exists():
        continue
    text = path.read_text(encoding='utf-8')
    original = text
    for old, new in replacements:
        text = text.replace(old, new)
    if text != original:
        path.write_text(text, encoding='utf-8')
        print('Fixed semantic link:', filename)
