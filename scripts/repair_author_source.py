from pathlib import Path
import re

path = Path('scripts/guides.py')
text = path.read_text()

replacement = '''def author_data_uri():
    # Use the verified portrait source that is already rendering reliably in browsers.
    # Presentation/cropping is handled separately in CSS so image reliability stays stable.
    parts = [Path(f'portrait-clean-v2/part0{i}.b64') for i in range(1, 4)]
    if not all(part.exists() for part in parts):
        raise RuntimeError('Verified clean author portrait chunks are missing; refusing to publish.')
    encoded = ''.join(''.join(part.read_text().split()) for part in parts)
    try:
        image = base64.b64decode(encoded, validate=True)
    except Exception as exc:
        raise RuntimeError('Verified clean author portrait chunks are not valid base64.') from exc
    if len(image) != 6393:
        raise RuntimeError(f'Clean author portrait has unexpected size: {len(image)} bytes.')
    if not (image.startswith(b'\\xff\\xd8\\xff') and image.endswith(b'\\xff\\xd9')):
        raise RuntimeError('Verified clean author portrait is not a complete JPEG.')
    return 'data:image/jpeg;base64,' + encoded'''

pattern = r'def author_data_uri\(\):\n.*?\n\n\ndef patch_index'
text, count = re.subn(pattern, replacement + '\n\n\ndef patch_index', text, count=1, flags=re.S)
if count != 1:
    raise RuntimeError('Could not locate author_data_uri in scripts/guides.py')

path.write_text(text)
print('Restored proven author portrait source while preserving corrected portrait CSS.')
