from pathlib import Path

about = Path('about.html')
if about.exists():
    text = about.read_text(encoding='utf-8')
    original = text
    text = text.replace('grid-template-columns:1fr 230px', 'grid-template-columns:1fr 210px')
    text = text.replace('width:220px;height:308px', 'width:200px;height:280px')
    text = text.replace('width:180px;height:252px', 'width:170px;height:238px')
    if text != original:
        about.write_text(text, encoding='utf-8')
        print('Refined About portrait scale')

contact = Path('contact.html')
if contact.exists():
    text = contact.read_text(encoding='utf-8')
    original = text
    text = text.replace('Fill this out and we’ll prepare an email addressed directly to Tate.', 'Fill this out and your message will be sent directly to Tate.')
    if text != original:
        contact.write_text(text, encoding='utf-8')
        print('Refined direct contact copy')
