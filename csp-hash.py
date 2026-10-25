"""Pin the viewer's Content-Security-Policy to the hash of its inline script.

The page only runs a script whose SHA-256 matches the one in its CSP, so any
injected inline script or event handler is refused by the browser. Run this
after every edit to the <script> block, or the page will stop working:

    python3 csp-hash.py reddit-viewer.html
"""
import base64, hashlib, re, sys

path = sys.argv[1] if len(sys.argv) > 1 else 'reddit-viewer.html'
html = open(path, encoding='utf-8').read()
scripts = re.findall(r'<script>(.*?)</script>', html, re.S)
if len(scripts) != 1:
    sys.exit(f'expected exactly one inline <script>, found {len(scripts)}')
digest = base64.b64encode(hashlib.sha256(scripts[0].encode('utf-8')).digest()).decode()
html, n = re.subn(r"script-src 'sha256-[^']*'", f"script-src 'sha256-{digest}'", html)
if n != 1:
    sys.exit("couldn't find script-src 'sha256-…' in the CSP")
open(path, 'w', encoding='utf-8').write(html)
print('script-src pinned to sha256-' + digest)
