# Answers for a Broken Heart — Pastoral Welcome Sequence

This is the first broad welcome sequence for readers who explicitly request occasional pastoral encouragement. It should feel like a pastor continuing a conversation, not a marketing funnel.

Do not automatically enroll a general pastoral subscriber into the book-launch segment. Email 4 may invite them to opt into book updates separately.

---

## Email 1 — Immediately

**Subject:** You do not have to solve everything today

**Preview text:** Start with the hurt that is actually in front of you.

Hi,

If you found Answers for a Broken Heart because something hurts, I want to begin with this: you do not have to solve everything today.

Pain has a way of making us feel as though we need answers to every question all at once. Why did this happen? Where is God? What am I supposed to do now? Am I ever going to feel normal again?

Those are real questions. But you do not have to answer all of them before you can take the next faithful step.

That is why I built the site around a simple place to begin: **tell me where it hurts.** You can choose the question that sounds closest to the one you are already carrying, and start there.

**Start here:** https://www.answersforabrokenheart.com/start-here

One of the verses that has shaped this entire project is Psalm 34:18:

> “The LORD is nigh unto them that are of a broken heart; and saveth such as be of a contrite spirit.”

God does not describe the brokenhearted as people He avoids. He says He is near.

So for today, do not pressure yourself to fix the whole story. Take the next step in front of you. Read one passage. Pray one honest sentence. Call one safe person. Let today be today.

I’m glad you’re here.

Tate Throndson
Pastor · Answers for a Broken Heart

P.S. These emails are meant to be occasional pastoral encouragement, not another noisy newsletter. If something here is not helpful, you should always be free to unsubscribe once the email platform is active.

---

## Email 2 — 2 days later

**Subject:** When what you feel and what is true collide

**Preview text:** Feelings are real. They just cannot carry the whole weight of truth.

Hi,

One of the hardest parts of pain is that what you feel can become so loud that it starts telling you what is true.

“I feel alone, so God must have left me.”

“I feel hopeless, so nothing is going to change.”

“I feel guilty, so God must be finished with me.”

“I feel afraid, so I must not have enough faith.”

Your feelings are real. They matter. They tell you something about what is happening inside you.

But they do not know everything.

That is the idea behind a free resource I put together called **Faith & Feelings**. It gives you room to name what you actually feel, put a KJV Scripture beside it, and take one small action that day.

**Get the free Faith & Feelings journals:** https://www.answersforabrokenheart.com/free-guides#faith-feelings-journals

There is a women’s edition and a men’s edition. Both are free, printable, and available without giving me another email address.

The goal is not to talk yourself out of a feeling. It is to refuse to make the feeling responsible for deciding what is ultimately true.

Sometimes faith sounds like this:

“I am afraid—and God is still faithful.”

“I am grieving—and God is still near.”

“I do not understand—and I am still going to bring the question to Him.”

**Faith is refusing to let the feeling decide what is true.**

Tate

---

## Email 3 — 5 days later

**Subject:** What if God feels far away?

**Preview text:** Difficulty recognizing His presence is not the same thing as His absence.

Hi,

There are seasons when God feels close, and there are seasons when you pray and hear what feels like silence.

If you are in the second kind of season, I do not want to give you a slogan.

I want to give you a promise.

Psalm 34:18 says:

> “The LORD is nigh unto them that are of a broken heart; and saveth such as be of a contrite spirit.”

Near.

That does not mean you will always *feel* held. It means you have not been abandoned.

Pain can make God difficult to recognize. Grief can make the Bible feel flat. Anxiety can make silence feel like absence. None of that makes you a bad Christian.

And difficulty recognizing God is not the same thing as God being gone.

I wrote a full answer for that exact question here:

**Why does God feel far away when I’m hurting?**
https://www.answersforabrokenheart.com/why-does-god-feel-far-away

If you only do one thing after reading it, let it be this: tell God one honest sentence about where He feels absent. Then read Psalm 34:18 slowly twice.

You do not have to manufacture a spiritual feeling.

Let the promise be stronger than the feeling for today.

Tate

---

## Email 4 — 8 days later

**Subject:** Why I’m writing Answers for a Broken Heart

**Preview text:** Some questions only become real when they become personal.

Hi,

I have preached about suffering for years. I have sat with hurting families. I have stood beside hospital beds and graves. And I have learned that some questions sound very different when they stop being theoretical and become personal.

“Why would God allow this?” is one kind of question in a Bible study.

It is another kind of question when you are asking it at 2:00 in the morning.

That is why I’m writing **Answers for a Broken Heart**.

The book is built around twenty-four questions people ask when pain makes easy answers feel too small. The goal is not to explain hurt away. It is to take the question seriously, open Scripture carefully, and help the reader recognize the God who has been present all along.

You can read about the book—and read a full sample Answer—here:

**Explore Answers for a Broken Heart:**
https://www.answersforabrokenheart.com/book

If you specifically want updates as the book moves toward publication, the Book page has a separate release list. I keep that separate intentionally; receiving these pastoral emails does not automatically put you on a book-marketing list.

Whether you ever buy the book or not, I hope the resources on the site continue to help.

Help first.

That is what this project is supposed to be.

Tate Throndson

---

# Automation notes for Kit

When Kit is connected:

- Enroll only explicit `pastoral_notes` subscribers in this sequence.
- Email 1: immediately.
- Email 2: delay 2 days.
- Email 3: delay 3 additional days (day 5).
- Email 4: delay 3 additional days (day 8).
- Keep `book_launch` as a separate explicit opt-in.
- Do not send email-address values, names, or message contents to Vercel Analytics.
- Before activation, replace the temporary unsubscribe sentence in Email 1 with Kit’s standard unsubscribe handling if needed.
