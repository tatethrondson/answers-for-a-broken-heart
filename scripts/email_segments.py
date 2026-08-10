from pathlib import Path
import re

MARKETING = [
    ('guide_2am', lambda t: '2:00 A.M. Guide' in t or '2AM Guide' in t or '2:00 A.M.' in t),
    ('book_launch', lambda t: 'book launch list' in t.lower() or 'Join the Launch List' in t or 'New Answers for a Broken Heart book launch signup' in t),
    ('church_resources', lambda t: 'Church and Pastor Resources' in t or 'New Church Resources interest' in t),
]

def infer_segment(form):
    for seg,check in MARKETING:
        if check(form): return seg
    return None

def add_hidden(form,name,value):
    if re.search(fr'name=["\']{re.escape(name)}["\']',form):
        return re.sub(fr'(<input[^>]+name=["\']{re.escape(name)}["\'][^>]*value=["\'])[^"\']*',fr'\1{value}',form,count=1)
    return form.replace('</form>',f'<input type="hidden" name="{name}" value="{value}"></form>',1)

changed=[]
for p in Path('.').glob('*.html'):
    s=p.read_text(encoding='utf-8',errors='ignore')
    original=s
    def repl(m):
        form=m.group(0)
        if 'formsubmit.co' not in form: return form
        seg=infer_segment(form)
        if not seg: return form
        if 'data-email-segment=' not in form:
            form=form.replace('<form','<form data-email-segment="'+seg+'"',1)
        form=add_hidden(form,'segment',seg)
        if not re.search(r'name=["\']source["\']',form):
            source=p.stem if p.stem!='index' else 'homepage'
            form=add_hidden(form,'source',source)
        return form
    s=re.sub(r'<form\b.*?</form>',repl,s,flags=re.S|re.I)
    if s!=original:
        p.write_text(s,encoding='utf-8')
        changed.append(p.name)
print('Email segmentation updated:', ', '.join(changed) if changed else 'no changes')