from pathlib import Path
import re
p=Path('index.html')
s=p.read_text(encoding='utf-8')

# Keep the static app shell empty. Dynamic home() should own homepage content.
s=re.sub(r'(<main id="app">).*?(</main>)', r'\1\2', s, count=1, flags=re.S)

# Make mobile Start Here point to the true first-visit route.
s=re.sub(r'<a class="mobileMenu" href="[^"]+">Start Here</a>', '<a class="mobileMenu" href="/start-here">Start Here</a>', s, count=1)

# Reduce top-navigation competition without falsely marking Start Here active on the homepage.
nav=re.search(r'<nav class="navlinks">.*?</nav>',s,re.S)
if nav:
    new='<nav class="navlinks"><a href="/start-here">Start Here</a><a href="/what-hurts-today">What Hurts Today?</a><a href="/free-guides">Free Guides</a><a href="/?view=book">The Book</a><a href="/church-resources">For Churches</a></nav>'
    s=s[:nav.start()]+new+s[nav.end():]

# Update the dynamic homepage hero buttons.
s=re.sub(r'<div class="heroButtons">.*?</div>', '<div class="heroButtons"><a class="btn primary" href="/start-here">I’m Hurting — Start Here</a> <a class="btn outline" href="/all-answers">Browse the 24 Answers</a></div>', s, count=1, flags=re.S)

# Remove the extra first-visit bridge so the hero flows directly into the care-path choices.
s=re.sub(r'<!-- HOME-FIRST-VISIT-START -->.*?<!-- HOME-FIRST-VISIT-END -->','',s,flags=re.S)

# Ensure new standalone routes are never swallowed by the homepage SPA router.
needle='&&!href.startsWith("/about")&&!href.startsWith("/about")'
replacement='&&!href.startsWith("/about")&&!href.startsWith("/start-here")&&!href.startsWith("/all-answers")&&!href.startsWith("/church-resources")'
s=s.replace(needle,replacement)

# Keep the footer useful without crowding the primary navigation.
footer=re.search(r'<div class="footerLinks">.*?</div>',s,re.S)
if footer:
    new_footer='<div class="footerLinks"><a href="/start-here">Start Here</a><a href="/what-hurts-today">What Hurts Today?</a><a href="/all-answers">All 24 Answers</a><a href="/free-guides">Free Guides</a><a href="/?view=book">The Book</a><a href="/church-resources">For Churches</a><a href="/about">About Tate</a><a href="/contact">Contact</a></div>'
    s=s[:footer.start()]+new_footer+s[footer.end():]

# Move the book launch offer into the natural book-interest area instead of above the hero.
launch='''<!-- BOOK-LAUNCH-LIST-START --><section class="launchBand" id="launch-list"><div class="wrap launchGrid"><div><p class="eyebrow">The book is coming</p><h2>Be among the first to know when <em>Answers for a Broken Heart</em> is available.</h2><p>This book is being written for the person who reaches for answers when the room is quiet and the pain is loud. It walks through 24 questions people actually ask in grief, suffering, doubt, disappointment, and unanswered prayer—with Scripture, honesty, and pastoral hope.</p><div class="launchBenefits"><div class="launchBenefit"><strong>Release-day notice</strong>Know as soon as the book is available.</div><div class="launchBenefit"><strong>Early previews</strong>Receive selected excerpts and behind-the-book updates.</div><div class="launchBenefit"><strong>Launch opportunities</strong>Hear about early-reader and launch-team opportunities as they become available.</div></div></div><div class="launchForm"><p class="eyebrow">Join the book list</p><h3>I want to know when the book is ready.</h3><p>No preorder yet. No pressure. Just a simple way to stay close to the project and be notified when the next step is available.</p><form action="https://formsubmit.co/tatethrondson@gmail.com" method="POST"><input type="email" name="email" placeholder="Your email address" aria-label="Your email address" autocomplete="email" required><input type="text" name="_honey" class="launchHoney" tabindex="-1" autocomplete="off"><input type="hidden" name="_subject" value="New Answers for a Broken Heart book launch signup"><input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="_next" value="https://answersforabrokenheart.com/?view=book"><input type="hidden" name="interest" value="Answers for a Broken Heart book launch list"><input type="hidden" name="source" value="Homepage book launch section"><button type="submit">Join the Launch List</button><div class="launchPrivacy">Occasional book updates only. You can leave the list anytime.</div></form></div></div></section><!-- BOOK-LAUNCH-LIST-END -->'''
s=re.sub(r'<!-- BOOK-LAUNCH-LIST-START -->.*?<!-- BOOK-LAUNCH-LIST-END -->','',s,flags=re.S)
book_end='<!-- BOOK-BRIDGE-HOME-END -->'
if book_end in s:
    s=s.replace(book_end,book_end+launch,1)
elif '<section class="newsletter"' in s:
    s=s.replace('<section class="newsletter"',launch+'<section class="newsletter"',1)

p.write_text(s,encoding='utf-8')
print('Homepage routing, navigation, and CTA hierarchy corrected')