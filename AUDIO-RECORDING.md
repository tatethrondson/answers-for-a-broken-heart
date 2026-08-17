# Answer Audio Recording Guide

All 24 Answer pages are audio-ready. The player remains hidden until the matching MP3 exists, so unfinished recordings never create empty controls for visitors.

## Recommended recording format

Aim for **2–3 minutes per Answer**. This is not an audiobook reading of the full page. It should feel like Pastor Tate sat down beside the listener and gave them the clearest pastoral version of the Answer.

Use this simple rhythm:

1. **Name the question** — one sentence that acknowledges what the listener may be carrying.
2. **Give the short answer** — say the core Answer plainly.
3. **Read one KJV Scripture** — usually the verse already featured in “Take one minute with this.”
4. **Pastoral explanation** — explain why that truth matters in this moment, without trying to cover the whole article.
5. **One next step** — a prayer, Scripture to reread, person to call, or small action for today.
6. **Close with hope** — one warm sentence, not a promotional pitch.

### Recording style

- Speak more slowly than a sermon.
- Use a close, conversational tone rather than pulpit projection.
- Leave small pauses after the question and Scripture.
- Avoid background music unless it is subtle and properly licensed.
- Do not add a long intro/outro; the listener has already chosen the Answer.
- Do not make the recording a book advertisement. Help first.
- Export as MP3. A clean spoken-word file around 96–128 kbps is sufficient.

## Exact filenames

Upload each finished file into the repository's `/audio/` directory using the exact filename below. The website will detect it automatically and reveal the player.

| Answer | MP3 filename |
|---|---|
| 01 | `why-does-god-feel-far-away.mp3` |
| 02 | `why-doesnt-god-show-himself.mp3` |
| 03 | `why-cant-i-see-what-god-is-doing.mp3` |
| 04 | `why-did-god-make-a-world-with-suffering.mp3` |
| 05 | `is-it-wrong-to-ask-god-why.mp3` |
| 06 | `why-wont-god-tell-me-why.mp3` |
| 07 | `can-anything-good-come-from-suffering.mp3` |
| 08 | `what-if-the-explanation-never-comes.mp3` |
| 09 | `does-god-know-what-this-feels-like.mp3` |
| 10 | `is-sympathy-all-god-offers.mp3` |
| 11 | `does-god-care-about-injustice.mp3` |
| 12 | `am-i-as-guilty-as-the-person-who-hurt-me.mp3` |
| 13 | `what-do-i-do-when-god-says-no.mp3` |
| 14 | `is-death-really-the-end.mp3` |
| 15 | `how-long-am-i-allowed-to-grieve.mp3` |
| 16 | `why-did-this-happen-to-me.mp3` |
| 17 | `why-does-grief-feel-worse.mp3` |
| 18 | `am-i-allowed-to-be-angry-with-god.mp3` |
| 19 | `what-do-i-say-to-god-right-now.mp3` |
| 20 | `why-does-loving-people-hurt.mp3` |
| 21 | `how-do-i-forgive-someone-who-isnt-sorry.mp3` |
| 22 | `does-forgiveness-mean-reconciliation.mp3` |
| 23 | `am-i-walking-away-from-god-or-church-hurt.mp3` |
| 24 | `does-doubt-mean-i-was-never-a-believer.mp3` |

## Suggested first recording batch

Do not feel pressure to record all 24 before publishing any. Start with the questions most likely to meet someone in an immediate hard moment:

- Answer 01 — God feels far away
- Answer 05 — Is it wrong to ask why?
- Answer 09 — Does God know what this feels like?
- Answer 13 — When God says no
- Answer 14 — Is death really the end?
- Answer 15 — How long may I grieve?
- Answer 18 — Am I allowed to be angry with God?
- Answer 19 — What do I say to God right now?
- Answer 21 — Forgiving someone who is not sorry
- Answer 22 — Forgiveness and reconciliation

That gives the site a strong initial audio library across suffering, grief, prayer, and relational pain.

## Quality check before upload

For each recording:

- Correct Answer/question stated.
- Scripture quotation matches the KJV.
- No private counseling details or identifying stories are included without permission.
- No clipping, excessive room noise, or abrupt cutoffs.
- Filename matches the table exactly.
- After upload and Vercel deployment, open the descriptive Answer URL and confirm the player appears and plays on desktop and mobile.

The runtime records only an `Answer Audio Play` analytics event with the Answer number. It does not send the listener's audio position, email address, or spoken content to Vercel Analytics.
