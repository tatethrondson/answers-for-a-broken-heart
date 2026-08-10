from pathlib import Path
import re
p=Path('index.html')
s=p.read_text(encoding='utf-8')

# Keep the static app shell empty. Dynamic home() should own homepage content.
s=re.sub(r'(<main id="app">).*?(</main>)', r'\1\2', s, count=1, flags=re.S)

# Make mobile Start Here point to the true first-visit route.
s=re.sub(r'<a class="mobileMenu" href="[^"]+">Start Here</a>', '<a class="mobileMenu" href="/start-here">Start Here</a>', s, count=1)

# Reduce top-navigation competition.
nav=re.search(r'<nav class="navlinks">.*?</nav>',s,re.S)
if nav:
    new='<nav class="navlinks"><a class="active" href="/start-here">Start Here</a><a href="/what-hurts-today">What Hurts Today?</a><a href="/free-guides">Free Guides</a><a href="/?view=book">The Book</a><a href="/church-resources">For Churches</a></nav>'
    s=s[:nav.start()]+new+s[nav.end():]

# Styles for the focused first-visit bridge.
css='''.firstVisit{padding:30px 0;background:#183024;color:white;border-bottom:1px solid rgba(255,255,255,.08)}.firstVisitGrid{display:grid;grid-template-columns:1fr auto;gap:42px;align-items:center}.firstVisit .eyebrow{color:#d8bd87}.firstVisit h2{font-size:1.9rem;line-height:1.08;margin:0 0 8px;color:white}.firstVisit p{margin:0;max-width:720px;font-size:.84rem;color:rgba(255,255,255,.8)}.firstVisitActions{display:flex;align-items:center;gap:18px;white-space:nowrap}.firstVisit .btn.primary{background:#f6f1e8;color:#20372a;border-color:#f6f1e8}.quietLink{font-size:.72rem;font-weight:800;color:white;text-decoration:none}@media(max-width:760px){.firstVisitGrid{grid-template-columns:1fr;gap:18px}.firstVisitActions{align-items:flex-start;flex-direction:column;gap:10px}}'''
if '.firstVisit{' not in s:
    s=s.replace('</style>',css+'</style>',1)

# Update the dynamic homepage hero buttons.
s=re.sub(r'<div class="heroButtons">.*?</div>', '<div class="heroButtons"><a class="btn primary" href="/start-here">I’m Hurting — Start Here</a> <a class="btn outline" href="/all-answers">Browse the 24 Answers</a></div>', s, count=1, flags=re.S)

# Insert the first-visit bridge into home() directly after the hero.
bridge='''<!-- HOME-FIRST-VISIT-START --><section class="firstVisit"><div class="wrap firstVisitGrid"><div><p class="eyebrow">First time here?</p><h2>You do not have to figure out the whole site.</h2><p>If you are hurting, begin with one simple question: <strong>What hurts today?</strong> Start Here will help you find the most useful Answer, Scripture, guide, or conversation for what you are carrying right now.</p></div><div class="firstVisitActions"><a class="btn primary" href="/start-here">Start Here</a><a class="quietLink" href="/what-hurts-today">Or tell me where it hurts →</a></div></div></section><!-- HOME-FIRST-VISIT-END -->'''
# Remove any prior dynamic bridge before reinserting.
s=re.sub(r'<!-- HOME-FIRST-VISIT-START -->.*?<!-- HOME-FIRST-VISIT-END -->','',s,flags=re.S)
hero_marker='</div></div></section><!-- CARE-PATHS-HOME-START -->'
if hero_marker in s:
    s=s.replace(hero_marker,'</div></div></section>'+bridge+'<!-- CARE-PATHS-HOME-START -->',1)

# Move the book launch offer into the natural book-interest area instead of above the hero.
launch='''<!-- BOOK-LAUNCH-LIST-START --><section class="launchBand" id="launch-list"><div class="wrap launchGrid"><div><p class="eyebrow">The book is coming</p><h2>Be among the first to know when <em>Answers for a Broken Heart</em> is available.</h2><p>This book is being written for the person who reaches for answers when the room is quiet and the pain is loud. It walks through 24 questions people actually ask in grief, suffering, doubt, disappointment, and unanswered prayer—with Scripture, honesty, and pastoral hope.</p><div class="launchBenefits"><div class="launchBenefit"><strong>Release-day notice</strong>Know as soon as the book is available.</div><div class="launchBenefit"><strong>Early previews</strong>Receive selected excerpts and behind-the-book updates.</div><div class="launchBenefit"><strong>Launch opportunities</strong>Hear about early-reader and launch-team opportunities as they become available.</div></div></div><div class="launchForm"><p class="eyebrow">Join the book list</p><h3>I want to know when the book is ready.</h3><p>No preorder yet. No pressure. Just a simple way to stay close to the project and be notified when the next step is available.</p><form action="https://formsubmit.co/tatethrondson@gmail.com" method="POST"><input type="email" name="email" placeholder="Your email address" aria-label="Your email address" autocomplete="email" required><input type="text" name="_honey" class="launchHoney" tabindex="-1" autocomplete="off"><input type="hidden" name="_subject" value="New Answers for a Broken Heart book launch signup"><input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="_next" value="https://answersforabrokenheart.com/?view=book"><input type="hidden" name="interest" value="Answers for a Broken Heart book launch list"><input type="hidden" name="source" value="Homepage book launch section"><button type="submit">Join the Launch List</button><div class="launchPrivacy">Occasional book updates only. You can leave the list anytime.</div></form></div></div></section><!-- BOOK-LAUNCH-LIST-END -->'''
s=re.sub(r'<!-- BOOK-LAUNCH-LIST-START -->.*?<!-- BOOK-LAUNCH-LIST-END -->','',s,flags=re.S)
# Place after the book bridge if available; otherwise before the newsletter.
book_end='<!-- BOOK-BRIDGE-HOME-END -->'
if book_end in s:
    s=s.replace(book_end,book_end+launch,1)
elif '<section class="newsletter"' in s:
    s=s.replace('<section class="newsletter"',launch+'<section class="newsletter"',1)

p.write_text(s,encoding='utf-8')
print('Homepage conversion flow corrected')