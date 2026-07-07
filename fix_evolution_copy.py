#!/usr/bin/env python3
"""Run from ~/portfolio: python3 fix_evolution_copy.py"""
import re, os

path = os.path.expanduser('~/portfolio/case-studies.html')
with open(path, 'r') as f:
    html = f.read()

m = re.search(r'<section class="project evolution">.*?</section>', html, re.DOTALL)
if not m:
    raise SystemExit('Could not find evolution section')
evo = m.group(0)
original = evo

def tolerant(text):
    """Build a regex that matches the text with any whitespace between words."""
    return re.compile(r'\s+'.join(re.escape(w) for w in text.split()))

replacements = [
    # (old TFG text, new Evolution text, label)
    ('TWENTY FIRST GROUP', 'EVOLUTION', 'eyebrow'),
    ('Twenty First Group is a global sports consultancy advising the Premier League, European Tour and FIFA. I led their rebrand from a house of brands into one unified consultancy.',
     'Evolution is an AI-powered talent identification platform used by leading football clubs. I led product design, turning dense scouting data into transfer decisions worth millions.',
     'headline'),
    ('The business had outgrown its house-of-brands structure. As leader of the in-house studio, I directed the move to a single consultancy identity with global appeal.',
     'Clubs needed to compare players across global markets and move fast in transfer windows, but the underlying data science was impenetrable to the people making the calls.',
     'para 1'),
    ('Beyond the rebrand, I was Creative Director on client platforms including the Titleist Hub, a data product for tracking and supporting sponsored athletes.',
     'I led product design across squad analysis, player comparison, and AI-driven transfer recommendations, working directly with data scientists to make the models usable.',
     'para 2'),
    ('Brand Architecture', '@@T1@@', 'tag 1'),
    ('Creative Direction', '@@T2@@', 'tag 2'),
    ('Product Design', '@@T3@@', 'tag 3'),
]

results = []
for old, new, label in replacements:
    pat = tolerant(old)
    evo, n = pat.subn(new, evo)
    results.append((label, n))

# Resolve temp tokens
evo = evo.replace('@@T1@@', 'Product Design')
evo = evo.replace('@@T2@@', 'Data Visualisation')
evo = evo.replace('@@T3@@', 'AI Features')

for label, n in results:
    print(('OK  ' if n else 'MISS') + '  ' + label + (' (replaced ' + str(n) + ')' if n else ''))

if evo != original:
    html = html.replace(original, evo)
    with open(path, 'w') as f:
        f.write(html)
    print('\nSaved changes to case-studies.html')

missed = [label for label, n in results if n == 0 and label not in ('tag 1', 'tag 2', 'tag 3')]
if missed:
    print('\nSome text did not match. Here is the current evolution section so Claude can see the markup:')
    print('=' * 60)
    print(evo)
    print('=' * 60)
else:
    print('All copy updated. Push when ready.')
