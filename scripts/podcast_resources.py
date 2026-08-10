from pathlib import Path
import re

START = "<!-- PODCAST-RESOURCE-START -->"
END = "<!-- PODCAST-RESOURCE-END -->"

STYLE = '''
<style>
.podcastResource{margin:50px 0 22px;padding:30px 32px;background:#f6f1e8;border:1px solid #ddd6c9;border-top:4px solid #b69258}
.podcastResource .podcastEyebrow{margin:0 0 8px;text-transform:uppercase;letter-spacing:.14em;font-size:.67rem;font-weight:800;color:#88683b}
.podcastResource h2{font:2rem/1.08 Georgia,"Times New Roman",serif;font-weight:400;color:#20372a;margin:0 0 10px}
.podcastResource .podcastIntro{margin:0 0 22px;color:#5f6862;font-size:.94rem;line-height:1.65}
.podcastEpisode{background:#fffdf9;border:1px solid #ded8cd;padding:22px 24px}
.podcastEpisode small{display:block;text-transform:uppercase;letter-spacing:.11em;font-size:.65rem;font-weight:800;color:#88683b;margin-bottom:7px}
.podcastEpisode h3{font:1.45rem/1.2 Georgia,"Times New Roman",serif;font-weight:400;color:#20372a;margin:0 0 9px}
.podcastEpisode p{margin:0 0 16px!important;color:#4f5a53;font-size:.91rem;line-height:1.6}
.podcastButton{display:inline-block;background:#294533;color:#fff!important;text-decoration:none!important;padding:10px 15px;font-size:.76rem;font-weight:800;letter-spacing:.03em}
.podcastButton:hover{background:#183024}
@media(max-width:700px){.podcastResource{padding:25px 22px}.podcastResource h2{font-size:1.75rem}}
</style>
'''

RESOURCES = {
    "why-god-allows-suffering.html": {
        "title": "Ava's Story: How God Is Still Good in the Hardest Trials",
        "blurb": "Ava Johnson and her parents talk honestly about sudden physical loss, adjustment, Scripture, and where they have seen God's presence and goodness in the middle of suffering.",
        "url": "https://www.youtube.com/watch?v=JpQrjWxY4Ys",
    },
    "grief-and-loss.html": {
        "title": "When Everything Falls Apart: How Ron & Nancy Are Still Trusting God",
        "blurb": "Ron and Nancy Sutton share about betrayal, financial pressure, serious health challenges, and learning to trust the God who sees them when life feels like it is coming apart.",
        "url": "https://www.youtube.com/watch?v=mOayIZ01R5w",
    },
    "god-feels-far-away.html": {
        "title": "When Life Doesn't Let Up... Listen to This",
        "blurb": "Pastor Harley Snode talks with Pastor Tate about long-term caregiving, carrying burdens that do not quickly disappear, and finding God's grace in the middle rather than only after the trial.",
        "url": "https://www.youtube.com/watch?v=UP_nNGjbvNY",
    },
    "forgiveness-and-relational-hurt.html": {
        "title": "Overcoming Bitterness with Pastor Tate Throndson",
        "blurb": "A practical conversation from James 3:14-16 about how bitterness takes root, what it damages, and how Christ gives us a different way to respond when we have been hurt.",
        "url": "https://youtu.be/opc26tntVRc",
    },
    "answer-04.html": {
        "title": "Ava's Story: How God Is Still Good in the Hardest Trials",
        "blurb": "If the question of God's goodness has become personal, hear one family's honest account of suffering, adjustment, Scripture, community, and the ways they have seen God meet them there.",
        "url": "https://www.youtube.com/watch?v=JpQrjWxY4Ys",
    },
    "answer-06.html": {
        "title": "When Life Doesn't Let Up... Listen to This",
        "blurb": "Pastor Harley Snode shares from a long season of caregiving and uncertainty—helpful for anyone who is still waiting for the burden to make sense or to finally get lighter.",
        "url": "https://www.youtube.com/watch?v=UP_nNGjbvNY",
    },
    "answer-07.html": {
        "title": "When Everything Falls Apart: How Ron & Nancy Are Still Trusting God",
        "blurb": "This conversation does not pretend the hard chapter is good. It shows what trusting God can look like while betrayal, health struggles, and uncertainty are still very real.",
        "url": "https://www.youtube.com/watch?v=mOayIZ01R5w",
    },
    "answer-11.html": {
        "title": "When Everything Falls Apart: How Ron & Nancy Are Still Trusting God",
        "blurb": "Ron and Nancy speak candidly about betrayal and unfair pressure without choosing retaliation—a fitting conversation for the painful space between being wronged and waiting for justice.",
        "url": "https://www.youtube.com/watch?v=mOayIZ01R5w",
    },
    "answer-13.html": {
        "title": "John & Carol Johnson: Faith Through a Cancer Journey",
        "blurb": "John and Carol talk about cancer, uncertainty, hope, and continuing to trust God's goodness when the outcome is not something you can control.",
        "url": "https://youtu.be/fkPXcbH79-c",
    },
    "answer-17.html": {
        "title": "Bitter No More: 4 Signs God's Wisdom Is Winning in You",
        "blurb": "Pastor Tate walks through four biblical ways to recognize that hurt is not getting the last word and that God's wisdom is beginning to shape the way you respond.",
        "url": "https://www.youtube.com/watch?v=C-gKb_skcUg",
    },
    "answer-21.html": {
        "title": "Overcoming Bitterness with Pastor Tate Throndson",
        "blurb": "Forgiveness is difficult when the wound is real. This teaching looks at the roots and results of bitterness and the freedom Christ offers when resentment wants to take over.",
        "url": "https://youtu.be/opc26tntVRc",
    },
    "answer-22.html": {
        "title": "Turn the Other Cheek... or Protect Your Family?",
        "blurb": "A careful biblical conversation about why forgiveness is not the same as enabling abuse, why meekness is not passivity, and why protecting people can coexist with a Christlike heart.",
        "url": "https://www.youtube.com/watch?v=-Tj-7LsEAUY",
    },
}


def block(data):
    return f'''{START}\n{STYLE}\n<section class="podcastResource" aria-label="Related Castleview Baptist Church Podcast episode">\n<p class="podcastEyebrow">Prefer to listen?</p>\n<h2>Listen to a conversation about this.</h2>\n<p class="podcastIntro">Sometimes you do not need another article. You need to hear someone talk through the hard part with you.</p>\n<div class="podcastEpisode">\n<small>Castleview Baptist Church Podcast</small>\n<h3>{data["title"]}</h3>\n<p>{data["blurb"]}</p>\n<a class="podcastButton" href="{data["url"]}" target="_blank" rel="noopener noreferrer">Listen on YouTube →</a>\n</div>\n</section>\n{END}'''


def patch(path, data):
    p = Path(path)
    if not p.exists():
        print(f"Missing {path}; skipping")
        return
    text = p.read_text(encoding="utf-8")
    text = re.sub(re.escape(START) + r".*?" + re.escape(END), "", text, flags=re.S)
    addition = block(data)

    if path.startswith("answer-"):
        anchor = "</article>"
    else:
        anchor = '<section class="related">'
        if anchor not in text:
            anchor = "</main>"

    if anchor not in text:
        print(f"No insertion anchor in {path}; skipping")
        return

    text = text.replace(anchor, addition + "\n" + anchor, 1)
    p.write_text(text, encoding="utf-8")
    print(f"Podcast resource added to {path}")


for filename, data in RESOURCES.items():
    patch(filename, data)
