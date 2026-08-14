from pathlib import Path
import re

ROOT = Path('.')


def write_if_changed(path, text, original, label):
    if text != original:
        path.write_text(text, encoding='utf-8')
        print(f'{label}: {path.name}')


def make_pastoral_signup(form):
    form = re.sub(r'data-email-segment=["\'][^"\']+["\']', 'data-email-segment="pastoral_notes"', form, count=1)
    form = re.sub(r'(<input[^>]+name=["\']segment["\'][^>]+value=["\'])[^"\']*', r'\1pastoral_notes', form, count=1)
    return form


# Homepage: immediate-help resource stays ungated; the email form is a distinct,
# optional relationship step rather than a disguised guide-access requirement.
path = ROOT / 'index.html'
if path.exists():
    text = path.read_text(encoding='utf-8')
    original = text
    block = re.search(r'<!-- FREE-GUIDES-HOME-START -->(.*?)<!-- FREE-GUIDES-HOME-END -->', text, re.S)
    if block:
        section = block.group(1)
        def fix_form(m):
            form = m.group(0)
            if 'Pastoral encouragement + new resources + book release updates' not in form:
                return form
            form = make_pastoral_signup(form)
            form = form.replace('New 2:00 A.M. Guide homepage signup', 'New pastoral encouragement signup from homepage')
            form = form.replace('https://answersforabrokenheart.com/2am-guide-access?welcome=1', 'https://answersforabrokenheart.com/2am-guide-access?sent=1')
            return form
        section = re.sub(r'<form\b.*?</form>', fix_form, section, flags=re.S|re.I)
        text = text[:block.start(1)] + section + text[block.end(1):]
    write_if_changed(path, text, original, 'Clarified homepage signup intent')


# 2:00 A.M. landing page: make the hierarchy visually and semantically clear—
# immediate access is primary; joining the ongoing pastoral list is optional.
path = ROOT / '2am-guide.html'
if path.exists():
    text = path.read_text(encoding='utf-8')
    original = text
    text = text.replace('<p class="eyebrow">Get the free guide</p><h2>Open the guide now.</h2>', '<p class="eyebrow">Immediate access</p><h2>Open the guide now.</h2>', 1)
    def fix_2am_form(m):
        form = m.group(0)
        if 'Pastoral encouragement + new resources + book release updates' not in form:
            return form
        form = make_pastoral_signup(form)
        form = form.replace('New 2:00 A.M. Guide signup', 'New pastoral encouragement signup from 2:00 A.M. Guide')
        form = form.replace('https://answersforabrokenheart.com/2am-guide-access?welcome=1', 'https://answersforabrokenheart.com/2am-guide-access?sent=1')
        return form
    text = re.sub(r'<form\b.*?</form>', fix_2am_form, text, flags=re.S|re.I)
    write_if_changed(path, text, original, 'Clarified hard-night conversion intent')


# Individual Answers: the unified answerJourney is now the deliberate stopping
# point. Remove older stacks of related cards, a full-width book promotion, and
# sequential "keep going" blocks that appeared after it. Those duplicated the
# choices the reader had just been given and weakened the promise that stopping
# is allowed.
for path in sorted(ROOT.glob('answer-??.html')):
    text = path.read_text(encoding='utf-8')
    original = text

    # Normalize the optional signup audience after all generators have run.
    def normalize_answer_form(m):
        form = m.group(0)
        if 'data-email-segment="pastoral_notes"' in form or 'Pastoral encouragement + new resources + book release updates' in form:
            return make_pastoral_signup(form)
        return form
    text = re.sub(r'<form\b.*?</form>', normalize_answer_form, text, flags=re.S|re.I)

    marker = '<!-- ANSWER-JOURNEY-END -->'
    pos = text.find(marker)
    if pos >= 0:
        head = text[:pos + len(marker)]
        tail = text[pos + len(marker):]
        tail = re.sub(r'\s*<!-- RELATED-ANSWERS-START -->.*?<!-- RELATED-ANSWERS-END -->', '', tail, count=1, flags=re.S)
        tail = re.sub(r'\s*<section class="cta">.*?</section>', '', tail, count=1, flags=re.S)
        tail = re.sub(r'\s*<section class="next">.*?</section>', '', tail, count=1, flags=re.S)
        text = head + tail

    write_if_changed(path, text, original, 'Removed duplicate post-answer decisions')


print('Final persona funnel cleanup complete.')
