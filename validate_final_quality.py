import json
import re

with open(r'C:\Users\mm\.gemini\antigravity\scratch\book_project\book_data_full.json', 'r', encoding='utf-8') as f:
    units = json.load(f)

print(f"Total units: {len(units)}")
total_items = sum(len(u['items']) for u in units)
print(f"Total items: {total_items}")

digit_in_en = []
mixed_case_en = []
empty_ja = []
empty_en = []

for u in units:
    for it in u['items']:
        en = it['en']
        ja = it['ja']
        if not ja: empty_ja.append((u['unit'], it['num']))
        if not en: empty_en.append((u['unit'], it['num']))
        
        # Check digit inside word
        if re.search(r'[a-zA-Z][0-9]|[0-9][a-zA-Z]', en):
            digit_in_en.append((u['unit'], it['num'], en))
            
        # Check lowercase followed by uppercase
        words = en.split()
        for w in words:
            if not w.isupper() and w not in ['CD', 'PC', 'TV', 'OK', 'ID', 'US', 'USA', 'UK', 'JT']:
                if re.search(r'[a-z][A-Z]', w):
                    mixed_case_en.append((u['unit'], it['num'], w, en))

print(f"Empty JA: {len(empty_ja)}")
print(f"Empty EN: {len(empty_en)}")
print(f"Digit in EN word: {len(digit_in_en)}")
for d in digit_in_en[:10]:
    print("  Digit:", d)

print(f"Mixed case in EN word: {len(mixed_case_en)}")
for m in mixed_case_en[:10]:
    print("  Mixed case:", m)
