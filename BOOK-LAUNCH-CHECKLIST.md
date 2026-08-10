# Answers for a Broken Heart — Website Launch Activation Checklist

The public site should remain in **coming soon** mode until verified publication information is available. Launch facts are controlled from `data/book-launch.json`.

## Before preorder is activated

- Final book title and subtitle confirmed
- Final cover image uploaded to the repository
- Publication / release date confirmed
- Amazon or retailer preorder URL verified
- `preorder_enabled` set to `true`
- `amazon_url` populated with the verified URL
- Any format shown publicly is actually available for preorder
- Launch-list form tested after the change
- SITE-QA.md returns 0 errors

## Before available-now mode is activated

- Amazon product page is live and purchase-tested
- `purchase_enabled` set to `true`
- `preorder_enabled` set to `false`
- Paperback / hardcover / eBook flags match actual availability
- Audiobook flag and URL remain off until the audiobook is actually live
- Spanish flag and URL remain off until the Spanish edition is actually live
- Release date text is accurate
- Book links from homepage, Answer pages, and Church Resources checked
- Analytics event for book-interest clicks confirmed

## Launch team

Keep `launch_team_enabled` false until there is a real signup destination and a defined expectation for launch-team members. When ready, populate `launch_team_url` and turn the flag on.

Suggested launch-team expectations when activated:
- Read an advance or early copy
- Leave an honest Amazon review after Amazon permits reviews
- Share launch-week content voluntarily
- Recommend the book to someone who may benefit from it

## Church / bulk distribution

Keep `bulk_orders_enabled` false until pricing, ordering method, and fulfillment are decided. The existing `/church-resources` page can become the destination once bulk information is real.

## Endorsements

Only add endorsements after the endorser has supplied or approved the exact wording. Store approved endorsements in the `endorsements` array in `data/book-launch.json`. Do not use placeholder names or paraphrased endorsements publicly.

## Formats planned but not promised

The configuration supports paperback, hardcover, eBook, audiobook, and Spanish edition. A format should only be enabled when its availability is verified.

## Final launch-day QA

1. Homepage primary book CTA goes to the correct verified destination.
2. Mobile book CTA works.
3. All 24 Answer pages still pass the automated QA audit.
4. `/start-here`, `/what-hurts-today`, `/all-answers`, `/free-guides`, `/church-resources`, and `/about` remain accessible.
5. 2:00 A.M. Guide signup still redirects correctly.
6. Book launch list is either retained for updates or intentionally changed after launch.
7. Sitemap contains all desired public pages.
8. No Coming Soon language remains in places where Available Now is intended.
