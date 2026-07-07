#!/usr/bin/env python3
"""Run from ~/portfolio: python3 fix_dead_links.py"""
import re, os

repo = os.path.expanduser('~/portfolio')
path = os.path.join(repo, 'case-studies.html')
with open(path, 'r') as f:
    html = f.read()

# Pages referenced by cards
referenced = set(re.findall(r'href="([a-z-]+\.html)"', html))
existing = {f for f in os.listdir(repo) if f.endswith('.html')}

dead = sorted(p for p in referenced if p not in existing)
print('Dead links found:', ', '.join(dead) if dead else 'none')

removed = 0
for page in dead:
    # Remove any anchor tag pointing at the missing page (the whole <a>...</a>)
    pattern = re.compile(r'<a[^>]+href="' + re.escape(page) + r'"[^>]*>.*?</a>', re.DOTALL)
    html, n = pattern.subn('', html)
    removed += n

with open(path, 'w') as f:
    f.write(html)

print('Removed', removed, 'dead links from case-studies.html')
print('Done.')
