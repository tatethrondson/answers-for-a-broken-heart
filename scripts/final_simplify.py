from pathlib import Path
import re

TOPIC_HUBS = {
    'grief-and-loss.html': 'Go deeper: what Scripture says about grief',
    'why-god-allows-suffering.html': 'Go deeper: biblical help for suffering and why',
    'god-feels-far-away.html': 'Go deeper: when God feels distant',
    'anger-and-unanswered-prayer.html': 'Go deeper: anger, prayer, and disappointment with God',
    'forgiveness-and-relational-hurt.html': 'Go deeper: forgiveness, trust, and relational wounds',
    'doubt-and-church-hurt.html': 'Go deeper: doubt, faith, and church hurt',
}

DISCLOSURE_STYLE = '''<!-- FINAL-SIMPLIFY-CSS-START --><style>
.deepHelpDisclosure,.podcastDisclosure{border-top:1px solid #ded8cd;border-bottom:1px solid #ded8cd;background:#faf8f3}
.deepHelpDisclosure>summary,.podcastDisclosure>summary{cursor:pointer;list-style:none;max-width:1120px;margin:0 auto;padding:23px 24px;font:400 1.15rem/1.35 Georgia,"Times New Roman",serif;color:#183024;display:flex;align-items:center;justify-content:space-between;gap:20px}
.deepHelpDisclosure>summary::-webkit-details-marker,.podcastDisclosure>summary::-webkit-details-marker{display:none}
.deepHelpDisclosure>summary:after,.podcastDisclosure>summary:after{content:"+";font:400 1.5rem/1 Arial,Helvetica,sans-serif;color:#ad823d}
.deepHelpDisclosure[open]>summary:after,.podcastDisclosure[open]>summary:after{content:"−"}
.deepHelpDisclosure[open]>summary,.podcastDisclosure[open]>summary{border-bottom:1px solid #ded8cd}
.deepHelpDisclosure .deepHelp{border-top:0!important;background:#fff!important;padding-top:48px!important}
.podcastDisclosure{border-top:0}
.podcastDisclosure .podcastResource{margin:0!important;border:0!important;border-top:0!important;background:#fff!important}
@media(max-width:760px){.deepHelpDisclosure>summary,.podcastDisclosure>summary{padding:20px 18px;font-size:1.05rem}}
</style><!-- FINAL-SIMPLIFY-CSS-END -->'''


def read(name):
    return Path(name).read_text(encoding='utf-8')


def write(name, text, original):
    if text != original:
        Path(name).write_text(text, encoding='utf-8')
        print('Simplified visitor flow:', name)


def simplify_home():
    name = 'index.html'
    text = read(name)
    original = text

    # The hero already routes the visitor. Do not ask the same decision twice.
    text = re.sub(
        r'<!-- CARE-PATHS-HOME-START -->.*?<!-- CARE-PATHS-HOME-END -->',
        '', text, flags=re.S
    )

    # One sentence of reassurance is enough; the site itself should demonstrate
    # help-first rather than continuing to explain that positioning.
    text = re.sub(r'<div class="heroReassure">.*?</div>', '', text, count=1, flags=re.S)

    # Replace the vague fifth category with the useful second visitor persona.
    text = text.replace(
        '<h3>Hope &amp; Healing</h3><p>When you’re ready to take the next step forward.</p><a href="/start-here">Find Answers →</a>',
        '<h3>Someone I Love Is Hurting</h3><p>When you want to help without saying the wrong thing.</p><a href="/help-someone">Help Me Help Them →</a>'
    )

    safety_block = '<div class="careSafety">If you do not feel safe or the pain has become dangerous, <a href="/unsafe">start here right now →</a></div>'
    # Make this idempotent across both publishing pipelines.
    while safety_block + safety_block in text:
        text = text.replace(safety_block + safety_block, safety_block)
    if safety_block not in text:
        text = text.replace(
            '<div class="center allTopics"><a class="btn outline" href="/all-answers">View All 24 Answers</a></div>',
            '<div class="center allTopics"><a class="btn outline" href="/all-answers">View All 24 Answers</a></div>' + safety_block
        )

    # Free Resources has its own top-level destination. Keep the homepage from
    # becoming a second resource library and second email-capture page.
    text = re.sub(
        r'<!-- FREE-GUIDES-HOME-START -->.*?<!-- FREE-GUIDES-HOME-END -->',
        '', text, flags=re.S
    )

    # The compact trust strip already establishes who Tate is and why this site
    # can be trusted. Remove the larger repeated author/sample block.
    text = re.sub(
        r'<section class="section"><div class="wrap authorSample">.*?</section>',
        '', text, count=1, flags=re.S
    )

    # Tighten the remaining trust strip without losing credibility.
    text = text.replace(
        'Tate Throndson is senior pastor of Castleview Baptist Church in Castle Rock, Colorado, where he has served since planting the church in 2008. These resources grow out of years of preaching, counseling, hospital rooms, funerals, and walking with hurting people.',
        'Tate Throndson has pastored Castleview Baptist Church since planting it in 2008. These resources grow out of years of preaching, counseling, hospital rooms, funerals, and walking with hurting people.'
    )

    write(name, text, original)


def simplify_start_here():
    name = 'start-here.html'
    text = read(name)
    original = text

    text = text.replace(
        'When your heart is overwhelmed, twenty-four answers can still feel like too many. Start with the sentence that sounds most like what you are carrying today. I’ll point you toward a biblical place to begin.',
        'Choose the sentence that sounds most like what you are carrying today. I’ll point you toward one biblical place to begin.'
    )
    text = text.replace(
        'You can always come back and choose something else. Pain rarely fits neatly into one box.',
        'Choose the closest one. You can always come back later.'
    )
    text = re.sub(r'<p class="reassure">.*?</p>', '', text, count=1, flags=re.S)

    compact = '''<div class="startMore"><div class="startMoreHead"><p class="eyebrow">Other ways to begin</p><h2>Not one of those six?</h2></div><div class="secondaryChoiceGrid"><a class="choice choiceSecondary" href="/can-christians-be-depressed"><small>I feel low, numb, or worn down</small><strong>I’m struggling emotionally.</strong><span>Start with a gentle pastoral note about depression and emotional heaviness.</span></a><a class="choice choiceSecondary" href="/help-someone"><small>I’m here for someone else</small><strong>Someone I love is hurting.</strong><span>Learn what to say, what not to say, and how to be present.</span></a><a class="choice choiceSecondary" href="/all-answers"><small>I already know my question</small><strong>I’d rather browse.</strong><span>Search the complete library of 24 answers.</span></a></div></div><div class="night"><div><p class="eyebrow" style="color:#d8bd87">For the hardest hour</p><h3>You do not have to solve your whole life tonight.</h3><p>Read one passage, pray one honest sentence, and take the next hour as it comes.</p></div><a class="btn light" href="/2am-guide-access">Open the 2:00 A.M. Guide</a></div></div></section>
'''
    text = re.sub(
        r'<!-- PERSONA-FLOW-START-SUPPORT -->.*?(?=<section class="safety">)',
        compact,
        text,
        count=1,
        flags=re.S,
    )

    write(name, text, original)


def simplify_topic_hubs():
    for name, summary in TOPIC_HUBS.items():
        text = read(name)
        original = text

        # The cards themselves tell the reader how to begin.
        text = re.sub(r'<section class="quick">.*?</section>', '', text, count=1, flags=re.S)

        # Keep substantial teaching available, but only when the visitor asks
        # for more. The hub's primary job is helping them choose one question.
        if 'deepHelpDisclosure' not in text:
            m = re.search(r'(<section class="deepHelp">.*?</section>)', text, flags=re.S)
            if m:
                wrapped = (
                    f'<details class="deepHelpDisclosure"><summary>{summary}</summary>'
                    + m.group(1)
                    + '</details>'
                )
                text = text[:m.start()] + wrapped + text[m.end():]

        # These large sections repeated truths already present in the question
        # cards and deeper material.
        text = re.sub(r'<section class="truthSection">.*?</section>', '', text, count=1, flags=re.S)
        text = re.sub(r'<section class="tonight">.*?</section>', '', text, count=1, flags=re.S)

        # Podcast content remains available without competing visually with the
        # question choices.
        if 'podcastDisclosure' not in text:
            m = re.search(r'(<section class="podcastResource".*?</section>)', text, flags=re.S)
            if m:
                wrapped = (
                    '<details class="podcastDisclosure"><summary>Prefer to listen? Hear a conversation about this</summary>'
                    + m.group(1)
                    + '</details>'
                )
                text = text[:m.start()] + wrapped + text[m.end():]

        # Once a visitor has chosen a topic, the page should not immediately
        # present three more topic decisions at the bottom. Global navigation
        # still makes every other topic easy to reach.
        text = re.sub(r'<section class="related">.*?</section>', '', text, count=1, flags=re.S)

        if 'FINAL-SIMPLIFY-CSS-START' in text:
            text = re.sub(
                r'<!-- FINAL-SIMPLIFY-CSS-START -->.*?<!-- FINAL-SIMPLIFY-CSS-END -->',
                DISCLOSURE_STYLE,
                text,
                count=1,
                flags=re.S,
            )
        elif '</head>' in text:
            text = text.replace('</head>', DISCLOSURE_STYLE + '\n</head>', 1)

        write(name, text, original)


def simplify_about():
    name = 'about.html'
    text = read(name)
    original = text

    text = text.replace(
        'Pastor, preacher, and author helping people find biblical hope in the middle of real life—especially when the questions are painful and easy answers are not enough.',
        'Pastor and author helping people find biblical hope when life hurts.'
    )

    # The story already establishes pastoral experience, biblical conviction,
    # and help-first intent. Do not explain the same credibility twice.
    text = re.sub(
        r'<!-- TRUST-CREDIBILITY-START -->.*?<!-- TRUST-CREDIBILITY-END -->',
        '', text, count=1, flags=re.S
    )

    write(name, text, original)


def simplify_book():
    name = 'book.html'
    text = read(name)
    original = text

    text = text.replace(
        'Twenty-four honest questions. Biblical answers. A pastoral voice that does not rush past the hurt or pretend every wound has a simple explanation.',
        'Twenty-four honest questions. Biblical answers. A pastoral voice that does not rush past the hurt.'
    )

    # On the Book page, sell/explain the book rather than re-explaining the
    # entire site's help-first philosophy.
    text = re.sub(r'<div class="bookHeroTrust">.*?</div>', '', text, count=1, flags=re.S)

    text = text.replace(
        'It is one thing to talk about the goodness of God when life is calm. It is another to ask whether He is good while you are standing beside a hospital bed, sitting in a quiet house after a funeral, carrying a prayer that was not answered the way you begged Him to answer it, or trying to make sense of what someone you trusted did to you.',
        'The goodness of God can feel very different beside a hospital bed, after a funeral, or while carrying a prayer that was not answered the way you begged Him to answer it.'
    )
    text = text.replace(
        '<em>Answers for a Broken Heart</em> was written for that moment. It does not begin by asking you to ignore what hurts. It begins with the question the hurt is already asking and brings that question honestly into the light of Scripture.',
        '<em>Answers for a Broken Heart</em> was written for that moment. It begins with the question the hurt is already asking and brings it honestly into the light of Scripture.'
    )
    text = text.replace(
        'The book is structured around twenty-four questions so you can begin with the question closest to your pain rather than feeling like you have to read a theology textbook from page one.',
        'Twenty-four questions let you begin with the one closest to your pain instead of reading from page one.'
    )
    text = text.replace(
        'You should be able to hear the voice of the book before you ever decide whether you want it. Read one of the full sample answers and see the blend of Scripture, pastoral care, honesty, and hope for yourself.',
        'Read one full sample answer and hear the voice of the book before you decide whether you want it.'
    )

    write(name, text, original)


def main():
    simplify_home()
    simplify_start_here()
    simplify_topic_hubs()
    simplify_about()
    simplify_book()


if __name__ == '__main__':
    main()
