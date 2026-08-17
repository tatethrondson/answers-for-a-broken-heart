from pathlib import Path
from html import unescape
import re

from PIL import Image, ImageDraw, ImageFont

ROOT = Path('.')
SOCIAL = ROOT / 'social'
SOCIAL.mkdir(exist_ok=True)

W, H = 1200, 630
PAPER = '#f7f2e9'
PINE = '#294533'
DEEP = '#183024'
GOLD = '#ad823d'
MUTED = '#667068'

SERIF = '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'
SERIF_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
SANS = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
SANS_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'


def font(path, size):
    return ImageFont.truetype(path, size=size)


def plain(text):
    text = re.sub(r'<[^>]+>', '', text, flags=re.S)
    return re.sub(r'\s+', ' ', unescape(text)).strip()


def extract(pattern, text, default=''):
    m = re.search(pattern, text, re.I | re.S)
    return plain(m.group(1)) if m else default


def text_width(draw, text, fnt):
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0]


def wrap(draw, text, fnt, max_width):
    words = text.split()
    lines = []
    line = ''
    for word in words:
        test = word if not line else line + ' ' + word
        if text_width(draw, test, fnt) <= max_width:
            line = test
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def fit_question(draw, text, max_width=930, max_height=330):
    for size in range(72, 43, -2):
        fnt = font(SERIF, size)
        lines = wrap(draw, text, fnt, max_width)
        spacing = int(size * 0.23)
        heights = [draw.textbbox((0, 0), ln, font=fnt)[3] for ln in lines]
        total = sum(heights) + spacing * max(0, len(lines)-1)
        if len(lines) <= 5 and total <= max_height:
            return fnt, lines, spacing
    fnt = font(SERIF, 44)
    return fnt, wrap(draw, text, fnt, max_width), 10


def meta_replace(head, value, new_value):
    pattern = re.compile(r'<meta\s+([^>]*?(?:property|name)=["\']'+re.escape(value)+r'["\'][^>]*)>', re.I)
    m = pattern.search(head)
    if not m:
        return head
    tag = m.group(0)
    if re.search(r'content=["\'][^"\']*["\']', tag, re.I):
        tag2 = re.sub(r'content=["\'][^"\']*["\']', 'content="'+new_value+'"', tag, flags=re.I)
    else:
        tag2 = tag[:-1] + ' content="'+new_value+'">'
    return head[:m.start()] + tag2 + head[m.end():]


def render_card(slug, question, category):
    img = Image.new('RGB', (W, H), PAPER)
    d = ImageDraw.Draw(img)

    d.rectangle((0, 0, W, 12), fill=PINE)
    d.rectangle((0, H-12, W, H), fill=PINE)
    d.line((90, 118, 260, 118), fill=GOLD, width=4)

    brand = font(SERIF_BOLD, 31)
    brand_small = font(SANS_BOLD, 17)
    eyebrow = font(SANS_BOLD, 18)
    footer = font(SANS, 18)
    footer_bold = font(SANS_BOLD, 18)
    heart = font(SERIF, 46)

    d.text((90, 56), 'Answers', font=brand, fill=DEEP)
    d.text((260, 70), 'FOR A BROKEN HEART', font=brand_small, fill=PINE)
    d.text((1054, 54), '♡', font=heart, fill=GOLD)

    cat = category.upper() if category else 'BIBLICAL HOPE FOR HARD PLACES'
    d.text((90, 145), cat, font=eyebrow, fill=GOLD)

    qfont, lines, spacing = fit_question(d, question)
    y = 195
    for line in lines:
        d.text((90, y), line, font=qfont, fill=DEEP)
        bbox = d.textbbox((90, y), line, font=qfont)
        y = bbox[3] + spacing

    d.line((90, 538, 1110, 538), fill='#d8d0c2', width=2)
    d.text((90, 566), 'Tate Throndson', font=footer_bold, fill=PINE)
    d.text((260, 566), '· Pastor & author', font=footer, fill=MUTED)
    d.text((845, 566), 'answersforabrokenheart.com', font=footer, fill=MUTED)

    out = SOCIAL / f'{slug}.png'
    img.save(out, 'PNG', optimize=True)
    return out


def update_head(page, question, image_url):
    text = page.read_text(encoding='utf-8', errors='ignore')
    if '</head>' not in text:
        return False
    head, rest = text.split('</head>', 1)

    head = meta_replace(head, 'og:image', image_url)
    head = meta_replace(head, 'twitter:image', image_url)
    alt = f'{question} — Answers for a Broken Heart'
    head = meta_replace(head, 'og:image:alt', alt)
    head = meta_replace(head, 'twitter:image:alt', alt)

    head = re.sub(r'("image"\s*:\s*)"[^"]+"', r'\1"'+image_url+'"', head, count=1)

    if 'property="og:image:width"' not in head:
        head += '\n<meta property="og:image:width" content="1200">'
    if 'property="og:image:height"' not in head:
        head += '\n<meta property="og:image:height" content="630">'
    if 'property="og:image:type"' not in head:
        head += '\n<meta property="og:image:type" content="image/png">'

    updated = head + '</head>' + rest
    if updated != text:
        page.write_text(updated, encoding='utf-8')
        return True
    return False


changed = []
created = []
for i in range(1, 25):
    page = ROOT / f'answer-{i:02d}.html'
    if not page.exists():
        raise SystemExit(f'Missing {page}')
    text = page.read_text(encoding='utf-8', errors='ignore')
    canonical = extract(r'<link\s+rel=["\']canonical["\']\s+href=["\']https://www\.answersforabrokenheart\.com/([^"\']+)', text)
    if not canonical:
        canonical = extract(r'<meta\s+property=["\']og:url["\']\s+content=["\']https://www\.answersforabrokenheart\.com/([^"\']+)', text)
    slug = canonical.strip('/')
    if not slug:
        raise SystemExit(f'Could not find descriptive slug for {page}')
    question = extract(r'<h1[^>]*>(.*?)</h1>', text)
    category = extract(r'<p\s+class=["\']eyebrow["\'][^>]*>(.*?)</p>', text)
    if not question:
        raise SystemExit(f'Could not find question for {page}')

    out = render_card(slug, question, category)
    created.append(str(out))
    image_url = f'https://www.answersforabrokenheart.com/social/{slug}.png'
    if update_head(page, question, image_url):
        changed.append(page.name)

print(f'Generated {len(created)} social cards.')
print('Updated metadata:', ', '.join(changed) if changed else 'already current')
