"""workspace/inventory/make_inventory.py

Walks the whole project and emits one TSV row per file:
    path | bytes | kind | title (first heading / docstring / first statement) | verdict flags

Used for the folder-by-folder audit.  Run from the repo root:
    python workspace/inventory/make_inventory.py            # writes inventory.tsv + prints summary
    python workspace/inventory/make_inventory.py <folder>   # prints only that folder
"""
import io
import os
import re
import sys

ROOT = '.'
SKIP_DIRS = {'__pycache__', '.git'}
FLAGS = []


def first_heading(text):
    for line in text.splitlines():
        s = line.strip()
        if s.startswith('#'):
            return s.lstrip('#').strip()[:110]
    return ''


def first_docstring(text):
    m = re.search(r'"""(.+?)(?:"""|\Z)', text, re.S)
    if m:
        return ' '.join(m.group(1).split())[:110]
    return ''


def first_lean(text):
    m = re.search(r'^(?:theorem|lemma|def|structure|example)\s+([A-Za-z0-9_\.]+)', text, re.M)
    if m:
        return m.group(0)[:110]
    return first_heading(text) or ' '.join(text.split())[:110]


def describe(path):
    ext = os.path.splitext(path)[1].lower()
    try:
        text = io.open(path, encoding='utf-8', errors='replace').read()
    except Exception:
        return ext, ''
    if ext == '.md':
        return ext, first_heading(text)
    if ext == '.py':
        return ext, first_docstring(text)
    if ext == '.lean':
        return ext, first_lean(text)
    if ext == '.json':
        return ext, ' '.join(text.split())[:110]
    if ext in ('.txt', '.tex'):
        return ext, ' '.join(text.split())[:110]
    return ext, ''


def main(only=None):
    rows = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for f in sorted(filenames):
            p = os.path.relpath(os.path.join(dirpath, f), ROOT).replace('\\', '/')
            ext, title = describe(p)
            rows.append((p, os.path.getsize(p), ext, title))
    rows.sort()
    os.makedirs('workspace/inventory', exist_ok=True)
    with io.open('workspace/inventory/inventory.tsv', 'w', encoding='utf-8', newline='\n') as fh:
        for p, n, ext, title in rows:
            fh.write(f'{p}\t{n}\t{ext}\t{title}\n')
    if only:
        rows = [r for r in rows if r[0].startswith(only)]
    for p, n, ext, title in rows:
        print(f'{p}\t{n}\t{ext}\t{title}')
    print(f'\n# {len(rows)} files listed; full list in workspace/inventory/inventory.tsv')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else None)
