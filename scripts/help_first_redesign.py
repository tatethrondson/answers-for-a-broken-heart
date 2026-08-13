from pathlib import Path
import re

HOME_MARK_START = '<!-- HELP-FIRST-HOME-START -->'
HOME_MARK_END = '<!-- HELP-FIRST-HOME-END -->'
BOOK_MARK_START = '<!-- HELP-FIRST-BOOK-START -->'
BOOK_MARK_END = '<!-- HELP-FIRST-BOOK-END -->'

HOME_CSS = '''<!-- HELP-FIRST-HOME-START -->
<style>
.helpHero .helpHeroInner{min-height:510px;display:flex;align-items:center;position:relative;z-index:2}
.helpHero .heroCopy{max-width:690px;padding:58px 0 64px}
.helpHero .heroLead{max-width:560px;font-size:1.18rem;line-height:1.62}
.helpHero .heroReassure{margin-top:19px;font-size:.78rem;color:#59655e;max-width:540px}
.helpHero .heroReassure strong{color:#294533}
@media(max-width:760px){.helpHero .helpHeroInner{min-height:500px;align-items:flex-start}.helpHero .heroCopy{padding:54px 0 72px}.helpHero .heroLead{font-size:1.08rem}}
</style>
<!-- HELP-FIRST-HOME-END -->'''

BOOK_CSS = '''<!-- HELP-FIRST-BOOK-START -->
<style>
.bookHelpFirst{background:#183024;color:white;padding:31px 34px;margin:0 0 28px;display:grid;grid-template-columns:1.15fr auto;gap:28px;align-items:center}
.bookHelpFirst h2{color:white!important;font:400 2rem/1.08 Georgia,"Times New Roman",serif;margin:0 0 8px!important}
.bookHelpFirst p{color:rgba(255,255,255,.82)!important;margin:0!important;font-size:.88rem}
.bookHelpFirst a{display:inline-block;text-decoration:none;background:#fff;color:#183024;padding:11px 15px;font-size:.7rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em;white-space:nowrap}
.bookBand{border:1px solid #ded8cd!important;background:#f5f0e7!important}
.bookStage{background:linear-gradient(140deg,#f1ece3,#fbf8f2)!important}
.coverTitle,.coverAuthor{color:#294533!important}.coverHeart{color:#ad823d!important}
.bookBandCopy{background:#f5f0e7!important}.bookBandCopy h2{color:#183024!important}
.bookAction{border-radius:2px!important}.bookAction.primary{background:#294533!important;color:#fff!important}.bookAction.secondary{border-color:#294533!important;color:#294533!important;background:#fffefb!important}
.salesCard{border-radius:2px!important;border-color:#ded8cd!important}.salesCard strong{color:#294533!important}
.bookUpdates{background:#183024!important;border-radius:2px!important}.bookUpdatesForm input,.bookUpdatesForm button{border-radius:0!important}.bookUpdatesForm button{background:#d8bd87!important;color:#183024!important}
@media(max-width:820px){.bookHelpFirst{grid-template-columns:1fr}.bookHelpFirst a{justify-self:start}}
</style>
<!-- HELP-FIRST-BOOK-END -->'''

NEW_HERO = '''<section class="hero helpHero"><div class="wrap helpHeroInner"><div class="heroCopy"><p class="eyebrow">Biblical hope for hard places</p><h1>When your heart is broken, you need more than a cliché.</h1><p class="heroLead">No pretending. No shallow answers. Just Scripture, honesty, and a path toward hope.</p><div class="heroButtons"><a class="btn primary" href="/start-here">I’m Hurting — Start Here</a> <a class="btn outline" href="/all-answers">Browse the 24 Answers</a></div><div class="promise"><span class="promiseIcon">⌁</span><span>Biblical answers. Real hope. Lasting healing.</span></div><div class="heroReassure"><strong>You do not have to buy anything to find help here.</strong> Start with the hurt, find the question underneath it, and take one faithful next step.</div></div></div></section>'''

HELP_FIRST_BOX = '''<div class="bookHelpFirst"><div><h2>Help first. Book second.</h2><p>If you came here hurting, you do not need to buy anything to begin. Start with a free answer or guide today; the book is here for the deeper journey when you are ready.</p></div><a href="/start-here">Start With What Hurts</a></div>'''

def strip_block(text, start, end):
    return re.sub(re.escape(start) + r'.*?' + re.escape(end), '', text, flags=re.S)

def add_css(text, start, end, css):
    text = strip_block(text, start, end)
    return text.replace('</head>', css + '\n</head>', 1)

home = Path('index.html')
text = home.read_text(encoding='utf-8')
text = add_css(text, HOME_MARK_START, HOME_MARK_END, HOME_CSS)
text = re.sub(r'<section class="hero"><div class="wrap heroGrid">.*?</section>\s*(<!-- CARE-PATHS-HOME-START -->)', NEW_HERO + r'\1', text, count=1, flags=re.S)
text = re.sub(r'<!-- BOOK-LAUNCH-LIST-START -->.*?<!-- BOOK-LAUNCH-LIST-END -->', '', text, flags=re.S)
text = text.replace('href="?view=book"', 'href="/book"')
home.write_text(text, encoding='utf-8')

book = Path('book.html')
text = book.read_text(encoding='utf-8')
text = add_css(text, BOOK_MARK_START, BOOK_MARK_END, BOOK_CSS)
text = text.replace('<section class="section"><div class="wrap"><div class="bookBand">', '<section class="section"><div class="wrap">' + HELP_FIRST_BOX + '<div class="bookBand">', 1)
text = text.replace('The site and the book work together: begin with an answer here, then go deeper in the full book.', 'The site and the book work together: begin with help here, then go deeper in the full book when you are ready.')
book.write_text(text, encoding='utf-8')

print('Applied help-first homepage and book redesign')
