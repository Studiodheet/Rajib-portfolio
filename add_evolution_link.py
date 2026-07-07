#!/usr/bin/env python3
"""Run from ~/portfolio: python3 add_evolution_link.py"""
import re, os

path = os.path.expanduser('~/portfolio/case-studies.html')
with open(path, 'r') as f:
    html = f.read()

# Find the brightlocal section and its 'Read the case study' link
bl = re.search(r'<section class="project brightlocal">.*?</section>', html, re.DOTALL)
if not bl:
    raise SystemExit('Could not find brightlocal section')

links = re.findall(r'<a[^>]*href="brightlocal\.html"[^>]*>.*?</a>', bl.group(0), re.DOTALL)
link = next((l for l in links if 'Read the case study' in l), None)
if not link:
    raise SystemExit('Could not find the Read the case study link in the brightlocal card')

evo_link = link.replace('brightlocal.html', 'evolution.html')

# Insert into the evolution section just before its closing tag
evo = re.search(r'<section class="project evolution">.*?</section>', html, re.DOTALL)
if not evo:
    raise SystemExit('Could not find evolution section')

if 'evolution.html' in evo.group(0):
    print('Evolution card already has a link. Nothing to do.')
else:
    new_evo = evo.group(0).replace('</section>', '      ' + evo_link + '\n    </section>')
    html = html.replace(evo.group(0), new_evo)
    with open(path, 'w') as f:
        f.write(html)
    print('Added Read the case study link to the Evolution card.')
print('Done.')
