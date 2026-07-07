#!/usr/bin/env python3
"""Run from ~/portfolio: python3 add_evolution.py"""
import re, os, shutil, glob

path = os.path.expanduser('~/portfolio/case-studies.html')
with open(path, 'r') as f:
    html = f.read()

# ---- 1. Extract all project sections ----
pattern = re.compile(r'<section class="project ([a-z-]+)">.*?</section>', re.DOTALL)
sections = {}
for m in pattern.finditer(html):
    sections[m.group(1)] = m.group(0)

print('Found sections:', ', '.join(sections.keys()))

# ---- 2. Build the Evolution card from the TFG card's markup ----
evo = sections['tfg']

# Use temp tokens so replacements don't collide
evo = evo.replace('class="project tfg"', 'class="project evolution"')
evo = evo.replace('TWENTY FIRST GROUP', 'EVOLUTION')
evo = evo.replace(
    'Twenty First Group is a global sports consultancy advising the Premier League, European Tour and FIFA. I led their rebrand from a house of brands into one unified consultancy.',
    'Evolution is an AI-powered talent identification platform used by leading football clubs. I led product design, turning dense scouting data into transfer decisions worth millions.'
)
evo = evo.replace(
    'The business had outgrown its house-of-brands structure. As leader of the in-house studio, I directed the move to a single consultancy identity with global appeal.',
    'Clubs needed to compare players across global markets and move fast in transfer windows, but the underlying data science was impenetrable to the people making the calls.'
)
evo = evo.replace(
    'Beyond the rebrand, I was Creative Director on client platforms including the Titleist Hub, a data product for tracking and supporting sponsored athletes.',
    'I led product design across squad analysis, player comparison, and AI-driven transfer recommendations, working directly with data scientists to make the models usable.'
)
evo = evo.replace('Brand Architecture', '@@T1@@')
evo = evo.replace('Creative Direction', '@@T2@@')
evo = evo.replace('Product Design', '@@T3@@')
evo = evo.replace('@@T1@@', 'Product Design')
evo = evo.replace('@@T2@@', 'Data Visualisation')
evo = evo.replace('@@T3@@', 'AI Features')
evo = evo.replace('twenty-first-group.html', 'evolution.html')

# Report any images referenced in the cloned card (will still point at TFG assets)
imgs = re.findall(r'src="([^"]+)"', evo)
if imgs:
    print('NOTE: Evolution card currently references these images (inherited from TFG):')
    for i in imgs:
        print('  -', i)

sections['evolution'] = evo

# ---- 3. Reorder ----
order = ['brightlocal', 'evolution', 'amex', 'nisba', 'taylormade', 'tfg', 'iss', 'nisba-brand', 'skybet']
missing = [k for k in order if k not in sections]
if missing:
    raise SystemExit('Missing sections, aborting: ' + str(missing))

all_matches = list(pattern.finditer(html))
start = all_matches[0].start()
end = all_matches[-1].end()
rebuilt = '\n\n    '.join(sections[k] for k in order)
html = html[:start] + rebuilt + html[end:]

with open(path, 'w') as f:
    f.write(html)
print('case-studies.html updated with new order:', ' > '.join(order))

# ---- 4. Copy Evolution images into the repo ----
src_dir = '/Users/rajibmoazzam/Library/CloudStorage/GoogleDrive-rajib@studiodheet.com/My Drive/Case Studies/TFG - Evolution'
dst_dir = os.path.expanduser('~/portfolio/images/evolution')
os.makedirs(dst_dir, exist_ok=True)
copied = []
for f in glob.glob(os.path.join(src_dir, '*')):
    if os.path.isfile(f):
        shutil.copy2(f, dst_dir)
        copied.append(os.path.basename(f))
if copied:
    print('Copied', len(copied), 'images to images/evolution/:')
    for c in sorted(copied):
        print('  -', c)
else:
    print('WARNING: no files found at', src_dir)

# ---- 5. Scaffold evolution.html from the TFG detail page ----
tfg_page = os.path.expanduser('~/portfolio/twenty-first-group.html')
evo_page = os.path.expanduser('~/portfolio/evolution.html')
if os.path.exists(tfg_page) and not os.path.exists(evo_page):
    shutil.copy2(tfg_page, evo_page)
    print('Created evolution.html as a copy of twenty-first-group.html (content needs rewriting)')

print('\nDone.')
