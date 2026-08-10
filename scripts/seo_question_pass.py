from pathlib import Path
import re, html

TITLES={
1:"Why Does God Feel Far Away When I’m Hurting?",
2:"If God Is Real, Why Doesn’t He Show Himself?",
3:"Why Can’t I See What God Is Doing in My Life?",
4:"Why Does God Allow Pain and Suffering?",
5:"Is It Wrong to Ask God Why?",
6:"Why Won’t God Tell Me Why This Is Happening?",
7:"Can God Bring Good Out of Suffering?",
8:"Why Do Bad Things Happen to Good People?",
9:"Does God Understand My Pain and Grief?",
10:"If God Cares, Why Doesn’t He Stop the Pain?",
11:"Is It Wrong to Be Angry at God?",
12:"How Do I Forgive Someone Who Hurt Me Deeply?",
13:"Why Didn’t God Answer My Prayer?",
14:"How Do I Grieve Without Losing My Faith?",
15:"Will I Ever Feel Normal After Grief?",
16:"How Do I Keep Going After Losing Someone I Love?",
17:"How Do I Let Go of Bitterness After Being Hurt?",
18:"What Do I Do When God Says No?",
19:"How Do I Trust God After Unanswered Prayer?",
20:"Does Forgiveness Mean I Have to Trust Them Again?",
21:"How Do I Overcome Bitterness Biblically?",
22:"Can I Set Boundaries and Still Be a Good Christian?",
23:"What Do I Do When Christians or a Church Hurt Me?",
24:"Can I Have Doubts and Still Have Faith?",
}

DESCS={
1:"God can feel far away when you are hurting. See what Scripture says about God’s presence when grief, anxiety, or pain make Him feel absent.",
2:"If God is real, why doesn’t He make Himself more obvious? A pastoral, biblical answer for doubt, evidence, and the feeling that God is hidden.",
3:"When you cannot see what God is doing, faith can feel impossible. Find biblical help for trusting God when your story makes no sense yet.",
4:"Why would a good God allow suffering? Explore a biblical, pastoral answer that takes pain seriously without offering shallow clichés.",
5:"Is questioning God a sign of weak faith? Scripture shows grieving people asking why. Learn how honest questions can coexist with real faith.",
6:"Why won’t God explain what is happening? A biblical answer for seasons when you desperately want reasons but God seems silent.",
7:"Can anything good come from what happened to me? Explore Romans 8, suffering, redemption, and how God can work without calling evil good.",
8:"Why do terrible things happen to people who did nothing to deserve them? A compassionate biblical look at suffering, justice, and a broken world.",
9:"Does God truly understand grief and pain? See how Jesus entered human sorrow, wept, suffered, and meets hurting people with more than sympathy.",
10:"If God loves me, why doesn’t He stop this pain? A pastoral answer about God’s care, Christ’s suffering, and the hope that pain will not have the last word.",
11:"Can a Christian be angry at God? Learn how Scripture makes room for honest lament without letting anger become the end of the story.",
12:"How do you forgive someone who caused deep hurt? Biblical help for forgiveness, healing, reconciliation, trust, and what forgiveness does not require.",
13:"Why didn’t God answer the prayer I begged Him to answer? A pastoral biblical response for disappointment, silence, and unanswered prayer.",
14:"How can I grieve and still trust God? Biblical help for mourning honestly without pretending faith removes sorrow.",
15:"Will grief ever stop feeling this heavy? A compassionate biblical answer about healing, memory, changed normal, and learning to carry loss.",
16:"How do you keep living after someone you love dies? Biblical encouragement for grief, daily faithfulness, and taking the next small step.",
17:"How do I stop bitterness from taking over after I have been hurt? Biblical help for resentment, forgiveness, wisdom, and healing.",
18:"What do you do when God says no to something you desperately wanted? Find biblical help for disappointment, surrender, and trusting God’s heart.",
19:"How can I trust God after prayers go unanswered? A pastoral biblical answer for rebuilding trust when God’s response was not what you hoped.",
20:"Does forgiving someone mean trusting them again? Learn the biblical difference between forgiveness, reconciliation, restored trust, and healthy boundaries.",
21:"How can a Christian overcome bitterness? Practical biblical help for recognizing resentment and replacing it with God’s wisdom and grace.",
22:"Can Christians set boundaries? A biblical look at turning the other cheek, protecting people you love, wisdom, forgiveness, and healthy limits.",
23:"What do I do when a church or Christian hurts me? Pastoral biblical help for church hurt, disappointment, forgiveness, truth, and keeping your faith centered on Christ.",
24:"Can a Christian have doubts and still believe? A pastoral biblical answer for honest questions, wavering faith, and bringing doubt into the light.",
}

TOPIC_LINKS={
range(1,4):[("why God feels far away","/god-feels-far-away"),("help when God feels silent","/god-feels-far-away"),("all 24 questions","/all-answers")],
range(4,9):[("why God allows suffering","/why-god-allows-suffering"),("biblical help for suffering","/why-god-allows-suffering"),("all 24 questions","/all-answers")],
range(9,11):[("God’s presence in pain","/god-feels-far-away"),("why God allows suffering","/why-god-allows-suffering"),("all 24 questions","/all-answers")],
range(11,14):[("anger and unanswered prayer","/anger-and-unanswered-prayer"),("help when prayers go unanswered","/anger-and-unanswered-prayer"),("all 24 questions","/all-answers")],
range(14,17):[("biblical help for grief","/grief-and-loss"),("grief and loss resources","/grief-and-loss"),("all 24 questions","/all-answers")],
range(17,23):[("forgiveness and relational hurt","/forgiveness-and-relational-hurt"),("biblical help for bitterness and boundaries","/forgiveness-and-relational-hurt"),("all 24 questions","/all-answers")],
range(23,25):[("doubt and church hurt","/doubt-and-church-hurt"),("biblical help for faith questions","/doubt-and-church-hurt"),("all 24 questions","/all-answers")],
}

def links_for(n):
    for r,links in TOPIC_LINKS.items():
        if n in r:return links
    return []

for n in range(1,25):
    p=Path(f'answer-{n:02d}.html')
    s=p.read_text(encoding='utf-8')
    title=TITLES[n]+' | Answers for a Broken Heart'
    desc=DESCS[n]
    s=re.sub(r'<title>.*?</title>',f'<title>{html.escape(title)}</title>',s,count=1,flags=re.S)
    s=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{html.escape(desc, quote=True)}">',s,count=1)
    # Keep social metadata aligned with search metadata.
    s=re.sub(r'<meta property="og:title" content="[^"]*">',f'<meta property="og:title" content="{html.escape(title, quote=True)}">',s,count=1)
    s=re.sub(r'<meta property="og:description" content="[^"]*">',f'<meta property="og:description" content="{html.escape(desc, quote=True)}">',s,count=1)
    s=re.sub(r'<meta name="twitter:title" content="[^"]*">',f'<meta name="twitter:title" content="{html.escape(title, quote=True)}">',s,count=1)
    s=re.sub(r'<meta name="twitter:description" content="[^"]*">',f'<meta name="twitter:description" content="{html.escape(desc, quote=True)}">',s,count=1)
    # Add a compact descriptive internal-link cluster just before the answer journey.
    start='<!-- SEO-SEARCH-PATHS-START -->'; end='<!-- SEO-SEARCH-PATHS-END -->'
    if start in s:
        a=s.index(start); b=s.index(end,a)+len(end); s=s[:a]+s[b:]
    links=' · '.join(f'<a href="{url}">{label}</a>' for label,url in links_for(n))
    block=f'''{start}<nav class="seoSearchPaths" aria-label="Related biblical help" style="margin:34px 0;padding:18px 20px;border-left:3px solid #b69258;background:#f6f1e8;font-size:.82rem;line-height:1.65"><strong style="display:block;color:#20372a;margin-bottom:4px">Related biblical help</strong>{links}</nav>{end}'''
    marker='<!-- ANSWER-JOURNEY-START -->'
    if marker in s:s=s.replace(marker,block+marker,1)
    p.write_text(s,encoding='utf-8')
    print('SEO updated',p)
