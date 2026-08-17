from pathlib import Path

TAG='<!-- ANSWER-AUDIO-RUNTIME -->\n<script defer src="/answer-audio.js?v=1"></script>'
changed=[]
for n in range(1,25):
    p=Path(f'answer-{n:02d}.html')
    if not p.exists():
        raise SystemExit(f'Missing {p}')
    text=p.read_text(encoding='utf-8')
    if '/answer-audio.js' in text:
        continue
    if '</body>' not in text:
        raise RuntimeError(f'No </body> in {p}')
    text=text.replace('</body>',TAG+'\n</body>',1)
    p.write_text(text,encoding='utf-8')
    changed.append(str(p))
print('Audio runtime enabled:', ', '.join(changed) if changed else 'already current')
