#!/usr/bin/env python3
"""Run from ~/portfolio: python3 fix_evolution_v2.py"""
import re, os

path = os.path.expanduser('~/portfolio/case-studies.html')
with open(path, 'r') as f:
    html = f.read()

m = re.search(r'<section class="project evolution">.*?</section>', html, re.DOTALL)
if not m:
    raise SystemExit('Could not find evolution section')
evo = m.group(0)
original = evo

# Separator that matches whitespace AND any html tags between words
SEP = r'(?:\s|<[^>]*>)+'
def loose(text):
    return re.compile(SEP.join(re.escape(w) for w in text.split()), re.IGNORECASE)

# 1. Headline (do this BEFORE the eyebrow so 'Twenty First Group is...' still matches)
old_headline = 'Twenty First Group is a global sports consultancy advising the Premier League, European Tour and FIFA. I led their rebrand from a house of brands into one unified consultancy.'
new_headline = 'Evolution is an AI-powered talent identification platform used by leading football clubs. I led product design, turning dense scouting data into transfer decisions worth millions.'
evo, n1 = loose(old_headline).subn(new_headline, evo)
print(('OK  ' if n1 else 'MISS') + '  headline')

# 2. Eyebrow: any remaining Twenty First Group reference in this section
evo, n2 = re.subn(r'Twenty\s+First\s+Group', 'Evolution', evo, flags=re.IGNORECASE)
print(('OK  ' if n2 else 'MISS') + '  eyebrow (replaced ' + str(n2) + ')')

# 3. First tag: first occurrence of 'AI Features' in this section should be 'Product Design'
evo, n3 = re.subn(r'AI Features', 'Product Design', evo, count=1)
print(('OK  ' if n3 else 'MISS') + '  tag 1')

html = html.replace(original, evo)

# 4. Page title
html, n4 = re.subn(r'<title>[^<]*</title>', '<title>Case Studies | Studio Dheet</title>', html, count=1)
print(('OK  ' if n4 else 'MISS') + '  page title')

with open(path, 'w') as f:
    f.write(html)

if not n1:
    print('\nHeadline still did not match. Current section markup:')
    print('=' * 60)
    print(evo)
    print('=' * 60)
else:
    print('\nAll done. Push when ready.')
