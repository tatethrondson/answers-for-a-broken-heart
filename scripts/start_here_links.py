from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
# Add Start Here to the first main navigation if it is not already present.
if 'href="/start-here">Start Here</a>' not in s:
    s=s.replace('<div class="navlinks">','<div class="navlinks"><a href="/start-here">Start Here</a>',1)
# Add a visible first-visit button to the homepage hero.
if 'I’m Hurting — Start Here' not in s and "I'm Hurting — Start Here" not in s:
    marker='<div class="heroButtons">'
    if marker in s:
        s=s.replace(marker,marker+'<a class="btn primary" href="/start-here">I’m Hurting — Start Here</a> ',1)
# Add a small first-visit link near homepage topic content as a fallback.
if 'New here? Start with one simple question.' not in s:
    marker='<section class="newsletter"'
    insert='<div style="text-align:center;padding:22px 20px;background:#f6f1e8;border-top:1px solid #ddd6c9"><strong style="font-family:Georgia,serif;font-weight:400;color:#20372a">New here? Start with one simple question.</strong> <a href="/start-here" style="font-size:.78rem;font-weight:800;color:#294533;text-decoration:none;margin-left:8px">Start Here →</a></div>\n'
    if marker in s:
        s=s.replace(marker,insert+marker,1)
p.write_text(s,encoding='utf-8')
print('Start Here links added')