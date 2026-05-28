from pathlib import Path
import re
root = Path(r'C:\Users\gowen\OneDrive\Desktop\downloaded_sites\site-1\pages')
patterns = ['5511', '948007313', 'whatsapp', 'contato', 'fale', 'telefone']
out = []
for path in sorted(root.glob('*.html')):
    text = path.read_text(encoding='utf-8', errors='ignore')
    if any(p in text.lower() for p in patterns):
        for line in text.splitlines():
            low = line.lower()
            if any(p in low for p in patterns):
                out.append(f'{path.name} | {line.strip()}')
print('\n'.join(out))
