from pathlib import Path
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')
root = Path(r'C:\Users\gowen\OneDrive\Desktop\downloaded_sites\site-1\pages')
phone_re = re.compile(r'55\d{10,11}')
address_re = re.compile(r'\b(?:Rua|Avenida|Av\.) [A-Za-zÀ-ÿ0-9\s\.]+')
keywords = ['whatsapp', 'contato', 'telefone', 'endereço', 'tatuapé', 'zona leste', 'são paulo', 'vila formosa', 'mooca']
phones = set()
addresses = set()
matches = []
for path in sorted(root.glob('*.html')):
    text = path.read_text(encoding='utf-8', errors='ignore')
    for m in phone_re.findall(text):
        phones.add(m)
    for m in address_re.findall(text):
        addresses.add(m.strip())
    lower = text.lower()
    if any(k in lower for k in keywords):
        lines = [line.strip() for line in text.splitlines() if any(k in line.lower() for k in keywords)]
        if lines:
            matches.append((path.name, sorted(set(lines))[:10]))
print('PHONES:')
for p in sorted(phones):
    print(' ', p)
print('\nADDRESSES:')
for a in sorted(addresses):
    print(' ', a)
print('\nMATCHED FILES:')
for fname, lines in matches:
    print('FILE:', fname)
    for line in lines:
        print(' ', line)
    print()