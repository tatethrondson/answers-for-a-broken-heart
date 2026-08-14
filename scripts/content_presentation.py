from pathlib import Path
import re

ROOT = Path('.')

TOPIC_HUBS = [
    'grief-and-loss.html',
    'why-god-allows-suffering.html',
    'god-feels-far-away.html',
    'anger-and-unanswered-prayer.html',
    'forgiveness-and-relational-hurt.html',
    'doubt-and-church-hurt.html',
]


def write_if_changed(path: Path, text: str, original: str, label: str):
    if text != original:
        path.write_text(text, encoding='utf-8')
        print(f'{label}: {path.name}')


def balanced_div(text: str, start: int):
    """Return (block, end_index) for the div beginning at start."""
    if start < 0 or not text.startswith('<div', start):
        return None, None
    token = re.compile(r'<div\b[^>]*>|</div>', re.I)
    depth = 0
    for m in token.finditer(text, start):
        if m.group(0).lower().startswith('<div'):
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                return text[start:m.end()], m.end()
    return None, None


def balanced_section(text: str, start: int):
    if start < 0 or not text.startswith('<section', start):
        return None, None
    token = re.compile(r'<section\b[^>]*>|</section>', re.I)
    depth = 0
    for m in token.finditer(text, start):
        if m.group(0).lower().startswith('<section'):
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                return text[start:m.end()], m.end()
    return None, None


# 1) START HERE — reduce nine equal-weight choices to six core pathways plus
#    three clearly secondary ways to begin.
for filename in ('begin-here.html', 'start-here.html'):
    path = ROOT / filename
    if not path.exists():
        continue
    text = path.read_text(encoding='utf-8')
    original = text
    if 'CONTENT-PRESENTATION-START-MORE' not in text:
        m = re.search(r'<div class="choiceGrid">(.*?)</div><section class="night">', text, re.S)
        if m:
            inner = m.group(1)
            anchors = re.findall(r'(?:<!-- START-HERE-DEPRESSION-PATH -->)?\s*(<a class="choice"[^>]*>.*?</a>)\s*(?:<!-- START-HERE-DEPRESSION-PATH-END -->)?', inner, re.S)
            secondary = []
            primary = []
            for a in anchors:
                if any(href in a for href in ('href="/can-christians-be-depressed"', 'href="/answer-17"', 'href="/help-someone"')):
                    secondary.append(a.replace('class="choice"', 'class="choice choiceSecondary"', 1))
                else:
                    primary.append(a)
            if len(primary) >= 6 and len(secondary) == 3:
                replacement = (
                    '<div class="choiceGrid">' + ''.join(primary) + '</div>'
                    '<!-- CONTENT-PRESENTATION-START-MORE -->'
                    '<section class="startMore" aria-labelledby="start-more-heading">'
                    '<div class="startMoreHead"><p class="eyebrow">Or maybe this is closer</p>'
                    '<h2 id="start-more-heading">A few other ways to begin.</h2></div>'
                    '<div class="secondaryChoiceGrid">' + ''.join(secondary) + '</div>'
                    '</section><!-- CONTENT-PRESENTATION-START-MORE-END -->'
                    '<section class="night">'
                )
                text = text[:m.start()] + replacement + text[m.end():]
    write_if_changed(path, text, original, 'Simplified Start Here choices')


# 2) ALL ANSWERS — put search/filter tools immediately after the hero. The
#    reassurance/explanation remains, but no longer blocks the user's task.
path = ROOT / 'all-answers.html'
if path.exists():
    text = path.read_text(encoding='utf-8')
    original = text
    intro_start = text.find('<section class="intro">')
    tools_start = text.find('<section class="tools">')
    if 0 <= intro_start < tools_start:
        intro, intro_end = balanced_section(text, intro_start)
        tools, tools_end = balanced_section(text, tools_start)
        if intro and tools:
            before = text[:intro_start]
            between = text[intro_end:tools_start]
            after = text[tools_end:]
            text = before + tools + between + intro + after
    write_if_changed(path, text, original, 'Moved Answer search above explanation')


# 3) TOPIC HUBS — users arrive to choose an answer, so put the question cards
#    before the longer contextual paragraphs. Also remove the search-engine-ish
#    question list from the dark quick bar in favor of one human sentence.
for filename in TOPIC_HUBS:
    path = ROOT / filename
    if not path.exists():
        continue
    text = path.read_text(encoding='utf-8')
    original = text

    text = re.sub(
        r'<div class="searchIntent">.*?</div>',
        '<div class="searchIntent"><strong>Choose one question.</strong><br>Start with the one that sounds most like the thought already running through your mind. You can read one answer and stop there.</div>',
        text,
        count=1,
        flags=re.S,
    )

    # Reorder only when intro precedes the answer chooser.
    sec = re.search(
        r'(<section class="section"><div class="wrap">)'
        r'(<div class="intro">.*?</div>)'
        r'(<div class="answerHead">.*?</div>)'
        r'(<div class="answerGrid">.*?</div>)'
        r'(</div></section>)',
        text,
        re.S,
    )
    if sec:
        intro = sec.group(2).replace('class="intro"', 'class="intro topicIntro"', 1)
        replacement = sec.group(1) + sec.group(3) + sec.group(4) + intro + sec.group(5)
        text = text[:sec.start()] + replacement + text[sec.end():]

    # The visible numbering is organizational, not helpful to a hurting reader.
    text = re.sub(r'<small>Answer\s+\d+</small>', '<small>Read this answer</small>', text)
    write_if_changed(path, text, original, 'Moved topic questions earlier')


# 4) INDIVIDUAL ANSWERS — reduce top-of-page administrative clutter and make
#    the short answer + one-minute help feel like one progressive-help module.
for path in sorted(ROOT.glob('answer-??.html')):
    text = path.read_text(encoding='utf-8')
    original = text

    # Topic, not serial number, should be the first label the reader sees.
    text = re.sub(
        r'<p class="eyebrow">Answer\s+\d+\s*·\s*([^<]+)</p>',
        r'<p class="eyebrow">\1</p>',
        text,
        count=1,
    )

    # Keep read time, remove the string of category labels.
    text = re.sub(
        r'<div class="meta">(About an?\s+\d+\s+minute read)(?:\s*·[^<]*)?</div>',
        r'<div class="meta">\1</div>',
        text,
        count=1,
    )

    # Keep trust information, but do not make the byline a mini biography.
    if '<!-- AUTHOR-BYLINE-START -->' in text:
        text = re.sub(
            r'<!-- AUTHOR-BYLINE-START -->.*?<!-- AUTHOR-BYLINE-END -->',
            '<!-- AUTHOR-BYLINE-START --><div class="answerByline">Written by <a href="/about" rel="author">Tate Throndson</a> · Pastor and author of <em>Answers for a Broken Heart</em></div><!-- AUTHOR-BYLINE-END -->',
            text,
            count=1,
            flags=re.S,
        )

    # The short answer already supplies the core truth. Remove the duplicative
    # "One truth" tile from the very next module and make the remaining items a
    # simple Scripture / prayer / next-step progression.
    if '<section class="minuteHelp"' in text:
        text = re.sub(
            r'<div class="minuteItem"><strong>One truth</strong><p>.*?</p></div>',
            '',
            text,
            count=1,
            flags=re.S,
        )
        text = text.replace('<h2>If you only have 60 seconds</h2>', '<h2>Take one minute with this.</h2>', 1)
        text = text.replace('One truth · One Scripture · One prayer · One step', 'One Scripture · One prayer · One next step', 1)

    write_if_changed(path, text, original, 'Streamlined answer opening')


# 5) DEPRESSION GUIDE — the practical next steps were buried after a long FAQ.
#    Move them directly after the opening reassurance, then let the deeper
#    biblical/FAQ material follow for readers who want it.
path = ROOT / 'can-christians-be-depressed.html'
if path.exists():
    text = path.read_text(encoding='utf-8')
    original = text
    steps_heading = '<h2>Three things that might actually help this week.</h2>'
    hpos = text.find(steps_heading)
    opening_key = '<p class="keyline"><strong>Yes. Christians can be depressed.</strong>'
    kpos = text.find(opening_key)
    if hpos > 0 and kpos >= 0:
        steps_start = text.find('<div class="steps">', hpos)
        if steps_start > 0:
            steps_block, steps_end = balanced_div(text, steps_start)
            key_end = text.find('</p>', kpos)
            if steps_block and steps_end and key_end > 0 and hpos > key_end:
                move_block = text[hpos:steps_end]
                text = text[:hpos] + text[steps_end:]
                insert_at = key_end + len('</p>')
                text = text[:insert_at] + '\n<!-- CONTENT-PRESENTATION-PRACTICAL-FIRST -->\n' + move_block + '\n' + text[insert_at:]
    write_if_changed(path, text, original, 'Moved depression next steps earlier')


# 6) ABOUT — remove two sections that repeat the same "help first" and ministry
#    experience ideas already established in the main story and trust cards.
path = ROOT / 'about.html'
if path.exists():
    text = path.read_text(encoding='utf-8')
    original = text
    text = text.replace(
        'This site is not written from a distance. Tate has spent more than twenty-five years in full-time ministry and has pastored Castleview Baptist Church since planting it in 2008. The perspective here has been shaped not only in sermon preparation, but in hospital rooms, funerals, counseling conversations, family crises, and years of walking with people through questions that do not disappear when the service ends.',
        'The perspective here is pastoral, biblical, and intentionally careful with questions Scripture does not fully explain. The goal is not to rush pain toward a tidy answer, but to tell the truth and keep pointing toward Christ.',
    )
    # Remove the later "Why this site exists" block; its content is already made
    # clearly in the story and "Help before promotion" trust card.
    why_marker = '<section class="section"><div class="wrap why">'
    wpos = text.find(why_marker)
    if wpos >= 0:
        block, end = balanced_section(text, wpos)
        if block:
            text = text[:wpos] + text[end:]
    write_if_changed(path, text, original, 'Removed repeated About-page messaging')


# 7) BOOK — explain the value before asking for an email address. Move release
#    signup beneath the three concise "what you get" cards.
path = ROOT / 'book.html'
if path.exists():
    text = path.read_text(encoding='utf-8')
    original = text
    ustart = text.find('<div class="bookUpdates" id="book-updates">')
    sstart = text.find('<div class="salesGrid">')
    if 0 <= ustart < sstart:
        updates, uend = balanced_div(text, ustart)
        sales, send = balanced_div(text, sstart)
        if updates and sales:
            # Remove updates from its original position. Locate sales again after removal.
            text = text[:ustart] + text[uend:]
            sstart2 = text.find('<div class="salesGrid">')
            sales2, send2 = balanced_div(text, sstart2)
            if sales2:
                text = text[:send2] + '\n' + updates + text[send2:]
    write_if_changed(path, text, original, 'Moved book signup after value')


# 8) CHURCH RESOURCES — surface ready-to-share material immediately after the
#    hero; move explanatory philosophy after it and remove the final repeated
#    vision section.
path = ROOT / 'church-resources.html'
if path.exists():
    text = path.read_text(encoding='utf-8')
    original = text
    intro_start = text.find('<section class="intro">')
    grid_start = text.find('<section class="gridSec">')
    if 0 <= intro_start < grid_start:
        intro, intro_end = balanced_section(text, intro_start)
        grid, grid_end = balanced_section(text, grid_start)
        if intro and grid:
            text = text[:intro_start] + grid + text[intro_end:grid_start] + intro + text[grid_end:]
    future_start = text.find('<section class="future">')
    if future_start >= 0:
        future, future_end = balanced_section(text, future_start)
        if future:
            text = text[:future_start] + text[future_end:]
    write_if_changed(path, text, original, 'Moved church resources before explanation')

print('Content presentation pass complete.')
