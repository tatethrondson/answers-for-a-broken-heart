from pathlib import Path

p = Path('book.html')
text = p.read_text(encoding='utf-8')
original = text

old_actions = '<div class="bookHeroActions"><a class="primary" href="/why-did-god-make-a-world-with-suffering">Read a Sample Answer</a><a class="secondary" href="#book-updates">Get Release Updates</a></div>'
new_actions = '<div class="bookHeroActions"><a class="primary" href="/why-did-god-make-a-world-with-suffering">Read a Sample Answer</a><a class="secondary" href="#book-updates">Join the Release List</a></div><div class="bookHeroTrust"><strong>Read before you join anything.</strong> Start with the sample. If the voice of the book is helpful, the release list is there when you want it.</div>'
if old_actions in text:
    text = text.replace(old_actions, new_actions, 1)
elif 'Read before you join anything.' not in text:
    raise SystemExit('Could not find hero action block to tune')

old_release = '<p><em>Answers for a Broken Heart</em> is in final preparation. Leave your email and I’ll let you know when preorders open, when the book releases, and when signed-copy options become available.</p>'
new_release = '<p><em>Answers for a Broken Heart</em> is in final preparation. Leave your email and I’ll send the confirmed release details when they are ready, along with occasional updates as the book moves toward publication.</p>'
if old_release in text:
    text = text.replace(old_release, new_release, 1)
elif 'confirmed release details' not in text:
    raise SystemExit('Could not find release-list promise to tune')

text = text.replace('<button type="submit">Notify Me</button>', '<button type="submit">Join Release List</button>', 1)

if text != original:
    p.write_text(text, encoding='utf-8')
    print('Book funnel tuned.')
else:
    print('Book funnel already current.')
