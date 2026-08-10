from pathlib import Path

p=Path('index.html')
s=p.read_text(encoding='utf-8')

css='''.launchBand{background:#183024;color:#fff;padding:56px 0}.launchGrid{display:grid;grid-template-columns:1.05fr .95fr;gap:58px;align-items:center}.launchBand .eyebrow{color:#d8bd87}.launchBand h2{font-size:2.7rem;line-height:1.04;margin:0 0 14px;color:#fff}.launchBand p{color:rgba(255,255,255,.82);max-width:620px}.launchBenefits{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:22px}.launchBenefit{border:1px solid rgba(255,255,255,.18);padding:15px;font-size:.74rem;line-height:1.45;color:rgba(255,255,255,.82)}.launchBenefit strong{display:block;color:#fff;font-size:.76rem;margin-bottom:4px}.launchForm{background:#f6f1e8;color:#24312b;padding:28px}.launchForm h3{font-size:1.65rem;margin:0 0 8px;color:#20372a}.launchForm p{color:#5b655f;font-size:.82rem;margin:0 0 16px}.launchForm form{display:grid;grid-template-columns:1fr 142px;gap:8px}.launchForm input[type=email]{border:1px solid #d7d0c5;padding:12px 13px;min-height:45px;font-size:.82rem}.launchForm button{border:0;background:#294533;color:#fff;padding:11px 12px;min-height:45px;font-size:.68rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em;cursor:pointer}.launchPrivacy{grid-column:1/-1;font-size:.63rem;color:#6b736f}.launchHoney{position:absolute!important;left:-5000px!important;width:1px!important;height:1px!important;overflow:hidden!important}@media(max-width:800px){.launchGrid{grid-template-columns:1fr;gap:26px}.launchBenefits{grid-template-columns:1fr}.launchForm form{grid-template-columns:1fr}.launchForm button{width:100%}}'''
if '.launchBand{' not in s:
    s=s.replace('</style>',css+'</style>',1)

block='''<!-- BOOK-LAUNCH-LIST-START -->
<section class="launchBand" id="launch-list"><div class="wrap launchGrid"><div><p class="eyebrow">The book is coming</p><h2>Be among the first to know when <em>Answers for a Broken Heart</em> is available.</h2><p>This book is being written for the person who reaches for answers when the room is quiet and the pain is loud. It walks through 24 questions people actually ask in grief, suffering, doubt, disappointment, and unanswered prayer—with Scripture, honesty, and pastoral hope.</p><div class="launchBenefits"><div class="launchBenefit"><strong>Release-day notice</strong>Know as soon as the book is available.</div><div class="launchBenefit"><strong>Early previews</strong>Receive selected excerpts and behind-the-book updates.</div><div class="launchBenefit"><strong>Launch opportunities</strong>Hear about early-reader and launch-team opportunities as they become available.</div></div></div><div class="launchForm"><p class="eyebrow">Join the book list</p><h3>I want to know when the book is ready.</h3><p>No preorder yet. No pressure. Just a simple way to stay close to the project and be notified when the next step is available.</p><form action="https://formsubmit.co/tatethrondson@gmail.com" method="POST"><input type="email" name="email" placeholder="Your email address" aria-label="Your email address" autocomplete="email" required><input type="text" name="_honey" class="launchHoney" tabindex="-1" autocomplete="off"><input type="hidden" name="_subject" value="New Answers for a Broken Heart book launch signup"><input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="_next" value="https://answersforabrokenheart.com/?view=book"><input type="hidden" name="interest" value="Answers for a Broken Heart book launch list"><input type="hidden" name="source" value="Homepage book launch section"><button type="submit">Join the Launch List</button><div class="launchPrivacy">Occasional book updates only. You can leave the list anytime.</div></form></div></div></section>
<!-- BOOK-LAUNCH-LIST-END -->'''

start='<!-- BOOK-LAUNCH-LIST-START -->'; end='<!-- BOOK-LAUNCH-LIST-END -->'
if start in s:
    a=s.index(start); b=s.index(end,a)+len(end); s=s[:a]+block+s[b:]
else:
    marker='<section class="newsletter"'
    if marker in s:
        s=s.replace(marker,block+'\n'+marker,1)
    else:
        s=s.replace('</main>',block+'\n</main>',1)

# Give book-focused links a direct path to the launch section while preserving the book view.
s=s.replace('href="/?view=book">Explore the book</a>','href="/?view=book#launch-list">Explore the book</a>')
p.write_text(s,encoding='utf-8')
print('Book launch section added')