#!/usr/bin/env python3
"""Run from ~/portfolio: python3 fix_casestudies_footer.py"""
import re, os

path = os.path.expanduser('~/portfolio/case-studies.html')
with open(path, 'r') as f:
    html = f.read()

# 1. Remove the outro section ("Good work, on the record.")
html, n1 = re.subn(r'<section class="outro">.*?</section>', '', html, flags=re.DOTALL)
print(('OK  ' if n1 else 'MISS') + '  removed outro section')

# 2. Remove the existing footer (the copyright line)
html, n2 = re.subn(r'<footer.*?</footer>', '', html, count=1, flags=re.DOTALL)
print(('OK  ' if n2 else 'MISS') + '  removed old footer')

# 3. Insert the global green footer before </body>
footer = '''
  <footer style="background:#A4FCA7;border-radius:28px;margin:14px;padding:clamp(48px,7vw,96px) clamp(24px,5vw,72px) 0;overflow:hidden;font-family:'Inter',-apple-system,sans-serif;color:#0A0A0A;">
    <div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:40px;margin-bottom:clamp(40px,6vw,72px);">
      <div>
        <p style="font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:0.06em;margin:0 0 14px;">Our Studios</p>
        <div style="display:grid;grid-template-columns:120px auto;gap:12px;font-size:14px;padding:4px 0;"><span>London</span><a href="mailto:london@studiodheet.com" style="color:#0A0A0A;text-decoration:none;">london@studiodheet.com</a></div>
        <div style="display:grid;grid-template-columns:120px auto;gap:12px;font-size:14px;padding:4px 0;"><span>Dubai</span><a href="mailto:dubai@studiodheet.com" style="color:#0A0A0A;text-decoration:none;">dubai@studiodheet.com</a></div>
      </div>
      <nav style="display:flex;gap:clamp(32px,5vw,80px);">
        <div style="display:flex;flex-direction:column;gap:10px;">
          <a href="index.html#about" style="font-size:14px;color:#0A0A0A;text-decoration:underline;text-underline-offset:3px;">About</a>
          <a href="index.html#services" style="font-size:14px;color:#0A0A0A;text-decoration:underline;text-underline-offset:3px;">Services</a>
          <a href="index.html#pricing" style="font-size:14px;color:#0A0A0A;text-decoration:underline;text-underline-offset:3px;">Pricing</a>
          <a href="case-studies.html" style="font-size:14px;color:#0A0A0A;text-decoration:underline;text-underline-offset:3px;">Case Studies</a>
        </div>
        <div style="display:flex;flex-direction:column;gap:10px;">
          <a href="index.html#roles" style="font-size:14px;color:#0A0A0A;text-decoration:underline;text-underline-offset:3px;">Roles</a>
          <a href="index.html#contact" style="font-size:14px;color:#0A0A0A;text-decoration:underline;text-underline-offset:3px;">Contact</a>
          <a href="https://www.linkedin.com/company/studiodheet" target="_blank" rel="noopener" style="font-size:14px;color:#0A0A0A;text-decoration:underline;text-underline-offset:3px;">LinkedIn</a>
        </div>
      </nav>
    </div>
    <p aria-hidden="true" style="font-family:'Denton','Cormorant Garamond',Georgia,serif;font-weight:400;font-size:clamp(64px,14.5vw,230px);line-height:0.75;letter-spacing:-0.02em;white-space:nowrap;text-align:center;transform:translateY(12%);margin:0;">studio dheet</p>
  </footer>
'''
html, n3 = re.subn(r'</body>', footer + '\n</body>', html, count=1)
print(('OK  ' if n3 else 'MISS') + '  inserted global footer')

with open(path, 'w') as f:
    f.write(html)
print('Done. Push when ready.')
