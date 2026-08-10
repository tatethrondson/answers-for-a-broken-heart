# Email Platform Migration Plan

The site currently uses FormSubmit as a temporary collection layer. Do not remove it until the replacement provider is tested end-to-end.

## Standard segments

- `guide_2am` — people requesting the free 2:00 A.M. Guide
- `book_launch` — people explicitly joining the Answers for a Broken Heart book launch list
- `church_resources` — pastors/church leaders requesting ministry resources and bulk-book updates
- `launch_team` — future explicit opt-in only; currently disabled

Every marketing signup should submit at least:

- `email`
- `segment`
- `source`

No email address, name, message, or other form-entered personal information should be sent to Vercel Analytics.

## Migration sequence

1. Choose the email service provider and authenticate the sending domain.
2. Create the four segments/groups above using the exact IDs where possible.
3. Build a welcome automation for each active segment.
4. Import existing subscribers and tag them by original source when known.
5. Replace FormSubmit actions with the provider endpoint or a serverless subscribe endpoint.
6. Test each form on mobile and desktop with a controlled address.
7. Confirm delivery, segment assignment, unsubscribe behavior, and redirects.
8. Only after successful testing, remove FormSubmit-specific fields.

## Suggested welcome sequences

### `guide_2am`
- Immediately: deliver the guide / direct link.
- 2 days later: short pastoral note and one related Answer.
- 5 days later: one podcast/resource matched to pain and suffering.
- 8 days later: introduce the purpose of the book softly and invite continued connection.

### `book_launch`
- Immediately: thank them and explain what the book is for.
- Later: selected excerpt or behind-the-book note.
- When verified: preorder/release announcement.
- When enabled: launch-team invitation as a separate explicit opt-in.

### `church_resources`
- Immediately: send the Church & Pastor Resources hub.
- Later: one practical grief-care or counseling resource.
- When ready: printable care kit / QR cards.
- When verified: church bulk-order information.

## Important guardrails

- Do not silently move a general subscriber into the future launch-team segment.
- Do not promise a preorder, publication date, audiobook, Spanish edition, endorsement, or bulk-order program before it is verified.
- Keep unsubscribe access clear in every campaign once a dedicated provider is active.
