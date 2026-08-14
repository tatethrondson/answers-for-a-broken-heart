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

    # The hero already routes a hurting reader well. Remove the second routing
    # section so the page does not ask the same decision twice.
    text = re.sub(
        r'<!-- CARE-PATHS-HOME-START -->.*?<!-- CARE-PATHS-HOME-END -->',
        '', text, flags=re.S
    )

    # Replace the vague fifth category with the useful second visitor persona.
    text = text.replace(
        '<h3>Hope &amp; Healing</h3><p>When you’re ready to take the next step forward.</p><a href="/start-here">Find Answers →</a>',
        '<h3>Someone I Love Is Hurting</h3><p>When you want to help without saying the wrong thing.</p><a href="/help-someone">Help Me Help Them →</a>'
    )

    # Keep immediate safety visible without making it another full section.
    text = text.replace(
        '<div class="center allTopics"><a class="btn outline" href="/all-answers">View All 24 Answers</a></div>',
        '<div class="center allTopics"><a class="btn outline" href="/all-answers">View All 24 Answers</a></div><div class="careSafety">If you do not feel safe or the pain has become dangerous, <a href="/unsafe">start here right now →</a></div>'
    )

    # Free Resources has its own clear top-level destination. The large homepage
    # resource/email block was turning the homepage into another resource hub.
    text = re.sub(
        r'<!-- FREE-GUIDES-HOME-START -->.*?<!-- FREE-GUIDES-HOME-END -->',
        '', text, flags=re.S
    )

    # About/author credibility is already handled by the compact trust strip.
    # Remove the larger two-column author/sample block that repeated it.
    text = re.sub(
        r'<section class="section"><div class="wrap authorSample">.*?</section>',
        '', text, count=1, flags=re.S
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

        # The question cards already explain how to begin. Remove the separate
        # dark instruction band that says essentially the same thing.
        text = re.sub(r'<section class="quick">.*?</section>', '', text, count=1, flags=re.S)

        # Keep substantial SEO/pastoral depth, but make it optional. The hub's
        # primary job is routing a hurting reader to one question.
        if 'deepHelpDisclosure' not in text:
            m = re.search(r'(<section class="deepHelp">.*?</section>)', text, flags=re.S)
            if m:
                wrapped = (
                    f'<details class="deepHelpDisclosure"><summary>{summary}</summary>'
                    + m.group(1)
                    + '</details>'
                )
                text = text[:m.start()] + wrapped + text[m.end():]

        write(name, text, original)


def simplify_about():
    name = 'about.html'
    text = read(name)
    original = text

    text = text.replace(
        'Pastor, preacher, and author helping people find biblical hope in the middle of real life—especially when the questions are painful and easy answers are not enough.',
        'Pastor and author helping people find biblical hope when life hurts.'
    )

    # The story itself establishes experience and approach. The three-card trust
    # section repeats those same claims, so let the story carry the credibility.
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

    # The free site itself demonstrates "help first." On the Book page this
    # extra positioning paragraph delays the actual book story.
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
