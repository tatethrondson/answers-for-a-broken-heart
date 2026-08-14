from pathlib import Path
import re

ROOT = Path('.')

SEO_PATH_RE = re.compile(
    r'<!-- SEO-SEARCH-PATHS-START -->.*?<!-- SEO-SEARCH-PATHS-END -->',
    re.S,
)
DEPTH_RE = re.compile(
    r'(<!-- (?P<name>EXACT-QUESTION-DEPTH(?:-WAVE\d+)?)-START -->.*?<!-- (?P=name)-END -->)',
    re.S,
)
WRAP_START = '<!-- ANSWER-DEEP-DIVE-START -->'
WRAP_END = '<!-- ANSWER-DEEP-DIVE-END -->'

for path in sorted(ROOT.glob('answer-??.html')):
    text = path.read_text(encoding='utf-8')
    original = text

    # The curated related-answer/journey components already handle discovery.
    # Remove the keyword-like strip that interrupts the pastoral reading flow.
    text = SEO_PATH_RE.sub('', text)

    # Keep the useful expanded material without making the page feel as if a
    # second article begins after the conclusion.
    if WRAP_START not in text:
        def wrap_depth(match):
            block = match.group(1)
            return (
                WRAP_START
                + '<details class="answerDeepDive">'
                + '<summary><span><strong>Go deeper on this question</strong>'
                + '<small>Explore a few questions people often ask next.</small></span>'
                + '<span class="answerDeepDiveMark" aria-hidden="true">+</span></summary>'
                + '<div class="answerDeepDiveBody">'
                + block
                + '</div></details>'
                + WRAP_END
            )
        text = DEPTH_RE.sub(wrap_depth, text)

    if text != original:
        path.write_text(text, encoding='utf-8')
        print('Refined answer depth:', path.name)

# Keep the depression-page presentation marker idempotent. Older runs could
# leave more than one comment even though the visible content was correct.
path = ROOT / 'can-christians-be-depressed.html'
if path.exists():
    text = path.read_text(encoding='utf-8')
    original = text
    marker = '<!-- CONTENT-PRESENTATION-PRACTICAL-FIRST -->'
    text = text.replace(marker, '')
    heading = '<h2>Three things that might actually help this week.</h2>'
    if heading in text:
        text = text.replace(heading, marker + '\n' + heading, 1)
    if text != original:
        path.write_text(text, encoding='utf-8')
        print('Cleaned depression presentation marker')

# One small presentation stylesheet, inserted only on Answer pages.
STYLE = '''<!-- ANSWER-DEEP-DIVE-CSS-START --><style>
.answerDeepDive{margin:34px 0 42px;border:1px solid #ded8cd;background:#faf8f3}
.answerDeepDive summary{list-style:none;cursor:pointer;display:flex;align-items:center;justify-content:space-between;gap:18px;padding:20px 22px;color:#183024}
.answerDeepDive summary::-webkit-details-marker{display:none}
.answerDeepDive summary strong{display:block;font:400 1.25rem/1.18 Georgia,"Times New Roman",serif;color:#183024}
.answerDeepDive summary small{display:block;margin-top:5px;font-size:.76rem;line-height:1.45;color:#657068}
.answerDeepDiveMark{flex:0 0 auto;font:400 1.8rem/1 Georgia,"Times New Roman",serif;color:#ad823d}
.answerDeepDive[open] .answerDeepDiveMark{transform:rotate(45deg)}
.answerDeepDiveBody{padding:0 22px 25px;border-top:1px solid #e5dfd5}
.answerDeepDiveBody .exactDepth,.answerDeepDiveBody .exactDepth2,.answerDeepDiveBody .exactDepth3,.answerDeepDiveBody .exactDepth4,.answerDeepDiveBody .exactDepth5{margin:0!important;padding:28px 0 0!important;border-top:0!important}
.answerDeepDiveBody .eyebrow:first-child{display:none}
@media(max-width:540px){.answerDeepDive summary{padding:18px}.answerDeepDiveBody{padding:0 18px 20px}}
@media print{.answerDeepDive summary{display:none!important}.answerDeepDive:not([open])>.answerDeepDiveBody{display:block!important}.answerDeepDiveBody{border-top:0;padding:0}.answerDeepDive{border:0;background:#fff}}
</style><!-- ANSWER-DEEP-DIVE-CSS-END -->'''

for path in sorted(ROOT.glob('answer-??.html')):
    text = path.read_text(encoding='utf-8')
    if 'ANSWER-DEEP-DIVE-START' not in text or 'ANSWER-DEEP-DIVE-CSS-START' in text:
        continue
    if '</head>' in text:
        text = text.replace('</head>', STYLE + '\n</head>', 1)
        path.write_text(text, encoding='utf-8')
        print('Added answer deep-dive styles:', path.name)

print('Answer presentation cleanup complete.')
