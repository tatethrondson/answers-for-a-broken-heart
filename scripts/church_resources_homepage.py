from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
# Add Church Resources to desktop nav after Start Here if not present.
if 'href="/church-resources"' not in s:
    s=s.replace('href="/start-here">Start Here</a>','href="/start-here">Start Here</a><a href="/church-resources">For Churches</a>',1)
# Add footer/resource link near Free Guides where possible.
if 'Church &amp; Pastor Resources' not in s:
    s=s.replace('href="/free-guides">Free Guides</a>','href="/free-guides">Free Guides</a><a href="/church-resources">Church &amp; Pastor Resources</a>',1)
p.write_text(s,encoding='utf-8')
print('Church Resources links added')