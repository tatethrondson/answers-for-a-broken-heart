from pathlib import Path
import re
import html

CSS_START = "/* HURTING-HELP-START */"
CSS_END = "/* HURTING-HELP-END */"
BOX_START = "<!-- HURTING-HELP-START -->"
BOX_END = "<!-- HURTING-HELP-END -->"

HELP = {1: ('God has not abandoned you just because you cannot feel Him.', 'Psalm 34:18', 'The LORD is nigh unto them that are of a broken heart; and saveth such as be of a contrite spirit.', 'Lord, I cannot feel You clearly right now. Help me trust Your promise more than my perception.', 'Tell God one honest sentence about where He feels absent, then read Psalm 34:18 slowly twice.'), 2: ('God has made Himself known most clearly in Jesus.', 'John 1:14', 'And the Word was made flesh, and dwelt among us...', 'Jesus, if I am struggling to know what God is like, help me look at You clearly.', 'Read one Gospel scene today and ask, What does this show me about the heart of God?'), 3: ('You do not have to understand the whole story to trust the next step.', 'Proverbs 3:5', 'Trust in the LORD with all thine heart; and lean not unto thine own understanding.', 'God, I do not see what You are doing. Give me enough light for the step in front of me.', 'Write down the one thing you do know is faithful today, and do only that next thing.'), 4: ('The brokenness you see is not the world God called very good.', 'Genesis 1:31', 'And God saw every thing that he had made, and, behold, it was very good.', 'God, I hate what pain and death have done. Help me grieve what is broken without believing You delight in it.', 'Name the part of this suffering that feels most wrong. You do not have to call it good in order to trust God.'), 5: ('Asking why is not the same as walking away.', 'Psalm 13:1', 'How long wilt thou forget me, O LORD? for ever? how long wilt thou hide thy face from me?', 'God, I have questions I cannot silence. Help me bring them to You instead of carrying them alone.', 'Write your hardest why-question exactly as you would say it to God. Do not soften it.'), 6: ('God may not give you every explanation, but He has not stopped being God.', 'Isaiah 55:8', 'For my thoughts are not your thoughts, neither are your ways my ways, saith the LORD.', 'Father, I want an explanation. When I do not receive one, help me trust Your character.', 'Separate what you know from what you do not know. Hold tightly to the first list.'), 7: ('Pain is not good, but God is able to work in what hurts.', 'Romans 8:28', 'And we know that all things work together for good to them that love God...', 'God, I would never have chosen this. Please do something redemptive in me and through me here.', 'Ask one question today: What kind of person could God be forming me into through this?'), 8: ("Sometimes the answer you receive is God's presence before it is an explanation.", 'Psalm 46:1', 'God is our refuge and strength, a very present help in trouble.', 'God, if I cannot have the answer yet, please make Your presence enough for this moment.', 'Stop trying to solve the entire story for ten minutes. Sit quietly with Psalm 46:1.'), 9: ('Jesus knows grief from the inside.', 'John 11:35', 'Jesus wept.', 'Jesus, thank You for entering human sorrow. Sit with me in mine.', "Picture Christ at Lazarus's grave. Let yourself grieve without apologizing for it."), 10: ('Jesus did more than sympathize with suffering; He entered death and rose.', 'Revelation 21:4', 'And God shall wipe away all tears from their eyes; and there shall be no more death...', 'Jesus, help me remember that suffering is real, but it is not final.', 'When your mind says, This is all there is, answer it with Revelation 21:4.'), 11: ("God's delay is not proof that injustice does not matter to Him.", 'Romans 12:19', 'Vengeance is mine; I will repay, saith the Lord.', 'God, I want justice. Keep me from becoming consumed by vengeance while I wait on You.', 'Name what was wrong without minimizing it, then consciously hand the right to final vengeance back to God.'), 12: ("Your need for grace does not erase another person's responsibility.", 'Isaiah 5:20', 'Woe unto them that call evil good, and good evil...', 'God, keep me humble about my own sin without making me dishonest about what was done to me.', "Write two separate sentences: What they did was wrong. I still need God's grace too. Do not collapse them into one."), 13: ('A no from God can break your heart without ending your story.', '2 Corinthians 12:9', 'My grace is sufficient for thee: for my strength is made perfect in weakness.', 'Lord, I wanted a different answer. Meet me in the disappointment and give me grace for what is.', 'Let yourself name what you hoped God would do. Grieve that honestly before trying to find a lesson.'), 14: ('For the Christian, death is an enemy, but it is not the end.', 'John 11:25', 'I am the resurrection, and the life: he that believeth in me, though he were dead, yet shall he live.', 'Jesus, the separation hurts. Hold my grief inside the hope of Your resurrection.', "Say the person's name today and thank God for one specific memory. Grief does not require forgetting."), 15: ('There is no stopwatch on grief.', 'Psalm 56:8', 'Thou tellest my wanderings: put thou my tears into thy bottle...', 'God, receive the grief I am still carrying. Keep me from shaming myself for missing someone I loved.', 'Give yourself permission to be sad today without measuring whether you should be over it by now.'), 16: ('You may never get a satisfying answer to why me, but your life can still have purpose here.', '2 Corinthians 1:4', 'Who comforteth us in all our tribulation, that we may be able to comfort them which are in any trouble...', 'God, I do not understand why this became part of my story. Show me how not to waste the pain.', 'Ask, Who might I understand differently now because of what I have walked through?'), 17: ('Healing is not always linear, but pain must be allowed to move.', 'Ecclesiastes 3:4', 'A time to weep, and a time to laugh; a time to mourn, and a time to dance.', 'God, help me grieve honestly without making grief my permanent home.', 'Notice one small sign of movement: a conversation, a walk, a laugh, a prayer, a moment of rest. Do not dismiss it.'), 18: ('You can be angry with God and still be talking to God.', 'Psalm 62:8', 'Pour out your heart before him: God is a refuge for us.', 'God, I am angry. I do not want anger to drive me away from You, so I am bringing it to You.', 'Pray the sentence you have been censoring. God already knows it; honesty keeps the conversation open.'), 19: ('God does not need a polished prayer.', 'Romans 8:26', 'The Spirit also helpeth our infirmities: for we know not what we should pray for as we ought...', 'God, I do not even know what to say. Hear what I cannot put into words.', 'Set a timer for two minutes and talk to God without editing yourself. Silence counts too.'), 20: ('Love makes us woundable, but being wounded does not mean loving was a mistake.', 'Psalm 147:3', 'He healeth the broken in heart, and bindeth up their wounds.', 'God, people have hurt places in me that mattered because I loved them. Please heal what I cannot repair alone.', 'Tell one safe person what hurts instead of rehearsing the wound only in your own head.'), 21: ('Forgiveness releases vengeance; it does not pretend the wound was small.', 'Ephesians 4:32', "And be ye kind one to another, tenderhearted, forgiving one another, even as God for Christ's sake hath forgiven you.", 'Father, I do not want what they did to keep shaping me. Help me release vengeance without denying the truth.', 'Do not force a feeling of forgiveness today. Begin by telling God exactly what you are releasing to His justice.'), 22: ('Forgiveness and reconciliation are not the same thing.', 'Matthew 3:8', 'Bring forth therefore fruits meet for repentance.', 'God, give me grace to forgive and wisdom about trust, access, and boundaries.', 'Do not make a major reconciliation decision while pressured. Ask: Has repentance produced trustworthy fruit?'), 23: ('Before rejecting Jesus, make sure you are not rejecting a distortion of Him.', 'John 6:68', 'Lord, to whom shall we go? thou hast the words of eternal life.', 'Jesus, help me separate You from the hypocrisy, abuse, legalism, or disappointment I have associated with Your name.', 'Write down what you are actually questioning: Jesus Himself, or something people did while using His name.'), 24: ('Doubt can tremble and still reach toward Christ.', 'Mark 9:24', 'Lord, I believe; help thou mine unbelief.', 'Jesus, I believe and I have questions. Meet me in both.', 'Choose one doubt instead of fighting all of them at once. Write it down and begin there.')}
SEARCH_TAGS = {1: 'absent alone abandoned lonely silence silent prayer numb dry disconnected cannot feel god far away', 2: 'god real proof evidence show himself invisible jesus doubt skeptical agnostic atheist', 3: 'confused direction unclear future waiting cannot see what god is doing uncertainty lost', 4: 'suffering pain evil cancer disease tragedy why bad things world broken innocent', 5: 'why questions questioning god confused angry doubt wrong to ask', 6: 'no answer explanation mystery unanswered why silence waiting confused', 7: 'purpose good from pain meaning suffering redeem use this trauma', 8: 'no explanation closure unanswered questions mystery presence why', 9: 'grief empathy does god understand pain jesus wept lonely sorrow loss', 10: 'death resurrection suffering end hope heaven grief final word', 11: 'justice unfair abuse wrongdoer gets away revenge anger injustice', 12: 'victim blame guilt abuse responsibility shame their fault my fault', 13: 'unanswered prayer no denied prayer disappointment god said no waiting', 14: 'death died funeral grief loss heaven goodbye bereavement spouse parent child friend', 15: 'grief timeline still sad years mourning miss them anniversary not over it', 16: 'why me unfair suffering purpose meaning happened to me trauma', 17: 'grief stuck worse bitterness healing not getting better depression numb', 18: 'angry at god furious mad rage disappointed prayer', 19: 'cannot pray words prayer numb silence what say god', 20: 'betrayal relationship heartbreak people hurt me trust wound divorce friendship church hurt', 21: 'forgive unforgiveness apology no sorry bitterness revenge betrayal abuse', 22: 'boundaries reconciliation trust forgive toxic unsafe abuse apology repentance', 23: 'church hurt hypocrisy abuse legalism deconstruction leaving faith reject christianity', 24: 'doubt assurance salvation unbelief questions faith weak believer deconstruction'}

CSS = f"""{CSS_START}
.minuteHelp{{margin:0 0 38px;border:1px solid #ddd6c9;border-top:4px solid #b69258;background:#fffdf9;padding:28px 30px}}
.minuteHelpHead{{display:flex;justify-content:space-between;gap:18px;align-items:end;margin-bottom:18px}}
.minuteHelpHead h2{{font:2rem/1.08 Georgia,"Times New Roman",serif;font-weight:400;color:#20372a;margin:0}}
.minuteHelpHead span{{font-size:.67rem;letter-spacing:.14em;text-transform:uppercase;color:#88683b;font-weight:800;white-space:nowrap}}
.minuteGrid{{display:grid;grid-template-columns:1fr 1fr;gap:12px}}
.minuteItem{{background:#f6f1e8;padding:19px 20px}}
.minuteItem strong{{display:block;font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:#88683b;margin-bottom:7px}}
.minuteItem p{{margin:0!important;font-size:.92rem;line-height:1.55}}
.minuteScripture{{font-family:Georgia,"Times New Roman",serif;color:#20372a}}
.minutePrayer{{font-family:Georgia,"Times New Roman",serif;font-style:italic}}
@media(max-width:700px){{.minuteGrid{{grid-template-columns:1fr}}.minuteHelp{{padding:24px 22px}}.minuteHelpHead{{display:block}}.minuteHelpHead span{{display:block;margin-top:7px}}}}
{CSS_END}"""

def help_box(n):
    truth, ref, verse, prayer, step = HELP[n]
    return f"""{BOX_START}<section class="minuteHelp" id="minute-help" aria-label="60-second help"><div class="minuteHelpHead"><h2>If you only have 60 seconds</h2><span>One truth · One Scripture · One prayer · One step</span></div><div class="minuteGrid"><div class="minuteItem"><strong>One truth</strong><p>{html.escape(truth)}</p></div><div class="minuteItem"><strong>One Scripture · {html.escape(ref)}</strong><p class="minuteScripture">“{html.escape(verse)}”</p></div><div class="minuteItem"><strong>Pray this</strong><p class="minutePrayer">“{html.escape(prayer)}”</p></div><div class="minuteItem"><strong>One next step</strong><p>{html.escape(step)}</p></div></div></section>{BOX_END}"""

def patch_answer(path, n):
    text = path.read_text()
    text = re.sub(re.escape(CSS_START) + r".*?" + re.escape(CSS_END) + r"\s*", "", text, flags=re.S)
    text = re.sub(re.escape(BOX_START) + r".*?" + re.escape(BOX_END), "", text, flags=re.S)
    text = text.replace("</style>", CSS + "\n</style>", 1)

    pattern = r'(<section class="short" id="short">.*?</section>)'
    if not re.search(pattern, text, flags=re.S):
        raise RuntimeError(f"Could not find short-answer section in {path}")
    text = re.sub(pattern, lambda m: m.group(1) + help_box(n), text, count=1, flags=re.S)

    if 'href="#minute-help"' not in text:
        text = text.replace('<a href="#short">The short answer</a>', '<a href="#short">The short answer</a><a href="#minute-help">The 60-second version</a>', 1)

    path.write_text(text)

def patch_search(path):
    text = path.read_text()
    text = re.sub(r' data-search="[^"]*"', '', text)

    for n, keywords in SEARCH_TAGS.items():
        num = f"{n:02d}"
        pattern = rf'(<a class="card" href="/answer-{num}" data-category="[^"]+")'
        text, count = re.subn(pattern, lambda m, kw=keywords: m.group(1) + f' data-search="{html.escape(kw, quote=True)}"', text, count=1)
        if count != 1:
            raise RuntimeError(f"Could not tag answer {num} on What Hurts Today")

    text = text.replace(
        'placeholder="Type what you’re carrying — grief, anger, doubt, unanswered prayer…"',
        'placeholder="Use your own words — depressed, lonely, angry, divorce, doubt, can’t sleep…"',
        1,
    )

    old = "const matchText=!term||card.textContent.toLowerCase().includes(term);"
    new = "const haystack=(card.textContent+' '+(card.dataset.search||'')).toLowerCase();const matchText=!term||haystack.includes(term);"
    if old in text:
        text = text.replace(old, new, 1)
    elif new not in text:
        raise RuntimeError("Could not upgrade emotional-language search")

    path.write_text(text)

for n in range(1, 25):
    patch_answer(Path(f"answer-{n:02d}.html"), n)

patch_search(Path("what-hurts-today.html"))
print("Hurting-person experience updated: 60-second help on all 24 answers and emotional-language search enabled.")
