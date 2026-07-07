#!/usr/bin/env python3
"""Run from ~/portfolio: python3 swap_evolution_images.py"""
import re, os

repo = os.path.expanduser('~/portfolio')
img_dir = os.path.join(repo, 'images/evolution')

# ---- 1. Rename images to web-safe kebab-case ----
renames = {}
for f in os.listdir(img_dir):
    new = f.lower().replace(' ', '-')
    if new != f:
        os.rename(os.path.join(img_dir, f), os.path.join(img_dir, new))
    renames[f] = new
print('Images now:', ', '.join(sorted(renames.values())))

# ---- 2. Swap the six Squarespace TFG images inside the Evolution section only ----
path = os.path.join(repo, 'case-studies.html')
with open(path, 'r') as f:
    html = f.read()

m = re.search(r'<section class="project evolution">.*?</section>', html, re.DOTALL)
if not m:
    raise SystemExit('Could not find the evolution section')
evo = m.group(0)

swap = {
    'abd7ffd7-c360-4ebd-879d-6a4b3a3b1c0f/Hero.png': 'images/evolution/hero.png',
    'aa9b0fc7-166a-4042-8c3f-42293239c4d9/Website-Homepage.png': 'images/evolution/search-and-player-database.png',
    '377bc4b3-8200-4421-80e5-9990197d7d52/Performance-Index.png': 'images/evolution/stats.png',
    '0a744241-adab-4023-88c1-de38db06020a/TFG_Jepordy.png': 'images/evolution/scenario-planning-overview.png',
    'c8386182-7788-42d0-8fb3-88873117f9e4/Newsletter.jpg': 'images/evolution/player-profile.png',
    '2822c744-e013-4b72-97df-746d4b93305e/0d366358-10a3-435c-b651-4c2a84ed7d37.png': 'images/evolution/custom-filters.png',
}

new_evo = evo
count = 0
for key, local in swap.items():
    # Replace the full squarespace URL (any src that contains the unique key)
    pattern = re.compile(r'https://images\.squarespace-cdn\.com/[^"]*' + re.escape(key.split('/')[-1]) + r'[^"]*')
    if pattern.search(new_evo):
        new_evo = pattern.sub(local, new_evo)
        count += 1

html = html.replace(evo, new_evo)
with open(path, 'w') as f:
    f.write(html)

print('Swapped', count, 'of 6 images on the Evolution card')
if count < 6:
    print('Some images did not match - send me the output and I will adjust')
print('Done.')
