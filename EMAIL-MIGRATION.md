# Email Platform Migration Plan

The site currently uses FormSubmit as a temporary collection layer. Do not remove it until the replacement provider is tested end-to-end.

## Provider decision

Use **Kit** as the first dedicated email platform for Answers for a Broken Heart.

Why it fits this stage:

- The free Newsletter plan is large enough for the current audience and early book-launch growth.
- Unlimited forms and broadcasts are available on the free plan.
- The free plan includes one basic visual automation and one email sequence, enough to build the first welcome path before paying for more advanced automation.
- Kit is creator/newsletter oriented, which fits a pastoral author platform better than a heavier CRM-first setup.

The live website should remain on FormSubmit until the Kit account, forms, API key, and welcome sequence are configured and tested.

## Standard segments

- `pastoral_notes` — general readers asking for occasional biblical encouragement and new resources
- `guide_2am` — optional dedicated segment if we later want a separate 2:00 A.M. Guide follow-up path
- `book_launch` — people explicitly joining the Answers for a Broken Heart book launch list
- `church_resources` — pastors/church leaders requesting ministry resources and bulk-book updates
- `launch_team` — future explicit opt-in only; currently disabled

Every marketing signup should submit at least:

- `email`
- `segment`
- `source`

No email address, name, message, or other form-entered personal information should be sent to Vercel Analytics.

## Kit server-side integration

The repository contains `api/subscribe-kit.js`. It is intentionally **not wired to the live forms yet**.

Configure these Vercel environment variables after the Kit account is created:

- `KIT_API_KEY`
- `KIT_FORM_PASTORAL_NOTES`
- `KIT_FORM_BOOK_LAUNCH`
- `KIT_FORM_CHURCH_RESOURCES`
- `KIT_FORM_GUIDE_2AM` only if a separate guide form is created
- `KIT_FORM_LAUNCH_TEAM` only when the launch team is enabled
- `KIT_ENABLE_LAUNCH_TEAM=true` only when launch-team signup is intentionally opened

The endpoint creates/upserts the subscriber through Kit API v4, then adds that email address to the form associated with the submitted segment. Keeping Kit credentials server-side prevents exposing the API key in page source.

## Migration sequence

1. Create the Kit account and authenticate the sending domain.
2. Create forms for `pastoral_notes`, `book_launch`, and `church_resources`. Create `guide_2am` only if we decide it needs a separate follow-up path.
3. Add the Kit API key and form IDs to Vercel environment variables.
4. Build the first welcome email sequence and automation.
5. Import existing FormSubmit subscribers and tag/group them by original source when known.
6. Test `api/subscribe-kit.js` with a controlled email address.
7. Replace FormSubmit actions with the serverless Kit endpoint one form at a time.
8. Test each form on mobile and desktop.
9. Confirm delivery, form assignment, double-opt-in/incentive-email behavior, unsubscribe behavior, and redirects.
10. Only after successful testing, remove FormSubmit-specific fields.

## First welcome sequence

Because the free Kit plan includes one email sequence, start with one broad **Pastoral Welcome** sequence that can serve general readers while the list is small:

### Email 1 — Immediately
**Subject direction:** You do not have to solve everything today

Thank them for trusting the resource, explain that Answers for a Broken Heart exists to offer biblical help without rushing past the hurt, and point them to Start Here.

### Email 2 — 2 days later
**Subject direction:** When what you feel and what is true collide

Introduce the Faith & Feelings exercise and link to the free journals.

### Email 3 — 5 days later
**Subject direction:** What do you do when God feels far away?

Link to the strongest relevant Answer and gently reinforce that difficult questions do not disqualify faith.

### Email 4 — 8 days later
**Subject direction:** Why I am writing Answers for a Broken Heart

Tell the pastoral reason behind the book and invite readers who want release information to explicitly join the `book_launch` group/form.

## Book-launch subscribers

People who explicitly join `book_launch` can receive broadcasts about manuscript progress, a future sample chapter, preorder availability, release information, and signed-copy options when those items are verified. Do not silently move general pastoral subscribers into the launch list.

## Church-resource subscribers

Keep pastors/church leaders distinct so future resources can be ministry-specific: grief-care tools, counseling handouts, QR cards, group resources, and verified bulk-order information.

## Important guardrails

- Do not email-gate resources that are currently promised as free and immediate.
- Do not silently move a general subscriber into `book_launch` or `launch_team`.
- Do not promise a preorder, publication date, audiobook, Spanish edition, endorsement, or bulk-order program before it is verified.
- Keep unsubscribe access clear in every campaign once Kit is active.
- Keep FormSubmit live until Kit has been tested end-to-end.
