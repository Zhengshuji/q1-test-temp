"""claim_index.py —— 命题索引：把所有"已提出的结论"抽成一张可检索的表

**为什么需要它**（2026-11-02 的重复研究事故）：本会话在 `proof/5a_archive/`、`proof/5b_upper_bound/`
里早已有 $(5a)$ 的三等价形式、$LA=\\Lambda L+G_0C+G_1CA$ 的 Lean 证明、以及 $P=(\\lambda I-\\Lambda)H$，
但没有人（包括我）在读 `STATUS.md` / `ATTEMPTS.md` 时看到它们，于是重复推导 + 重复形式化。

本脚本把四类来源抽成一张表（`tools/hygiene/claims.tsv`）：

  1. `proof/<claim>/README.md` 的标题行与"状态"行；
  2. `docs/02_theorems_proven.md` 的编号命题（`**A.1 …**` 之类）；
  3. `docs/03_theorems_cited.md` 的引用条目（若可解析）；
  4. `ATTEMPTS.md` 的路线表行。

用法：
    python tools/hygiene/claim_index.py                 # 重建索引并打印统计
    python tools/hygiene/claim_index.py --grep 5a       # 在索引里检索（大小写不敏感）
    python tools/hygiene/claim_index.py --check         # 索引过期则退出码 1（可作提交前闸门）
"""

import io
import os
import re
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(_HERE))
OUT = os.path.join(ROOT, 'tools', 'hygiene', 'claims.tsv')


def _first_match(lines, pattern):
    rx = re.compile(pattern)
    for ln in lines:
        m = rx.search(ln)
        if m:
            return ln.strip()
    return ''


def _clean(t, width=180):
    t = re.sub(r'\s+', ' ', t).strip()
    return t[:width]


def scan_proof():
    rows = []
    base = os.path.join(ROOT, 'proof')
    if not os.path.isdir(base):
        return rows
    for name in sorted(os.listdir(base)):
        d = os.path.join(base, name)
        if not os.path.isdir(d):
            continue
        rd = os.path.join(d, 'README.md')
        if not os.path.isfile(rd):
            rows.append(('proof', f'proof/{name}', '(无 README)', ''))
            continue
        lines = io.open(rd, encoding='utf-8', errors='replace').read().split('\n')[:40]
        title = _first_match(lines, r'^#\s+')
        status = _first_match(lines, r'状态|Status')
        rows.append(('proof', f'proof/{name}', _clean(title), _clean(status)))
    return rows


def scan_docs02():
    rows = []
    p = os.path.join(ROOT, 'docs', '02_theorems_proven.md')
    if not os.path.isfile(p):
        return rows
    for ln in io.open(p, encoding='utf-8', errors='replace'):
        if re.match(r'^\*\*[A-Z]\.\d', ln.strip()):
            rows.append(('docs/02', 'docs/02_theorems_proven.md', _clean(ln), ''))
    return rows


def scan_docs03():
    rows = []
    p = os.path.join(ROOT, 'docs', '03_theorems_cited.md')
    if not os.path.isfile(p):
        return rows
    for ln in io.open(p, encoding='utf-8', errors='replace'):
        s = ln.strip()
        if s.startswith('**') and len(s) > 6:
            rows.append(('docs/03', 'docs/03_theorems_cited.md', _clean(s), ''))
    return rows


def scan_attempts():
    rows = []
    p = os.path.join(ROOT, 'ATTEMPTS.md')
    if not os.path.isfile(p):
        return rows
    for ln in io.open(p, encoding='utf-8', errors='replace'):
        s = ln.strip()
        if s.startswith('|') and '---' not in s and not s.startswith('| 方向') and not s.startswith('| id'):
            cells = [c.strip() for c in s.strip('|').split('|')]
            if len(cells) >= 3:
                rows.append(('attempts', 'ATTEMPTS.md', _clean(' | '.join(cells[:3])), _clean(' | '.join(cells[3:]))))
    return rows


def build():
    rows = scan_proof() + scan_docs02() + scan_docs03() + scan_attempts()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('kind\tpath\ttitle\tstatus\n')
        for r in rows:
            fh.write('\t'.join(c.replace('\t', ' ') for c in r) + '\n')
    return rows


def grep(pattern):
    if not os.path.isfile(OUT):
        build()
    rx = re.compile(pattern, re.I)
    hits = []
    with io.open(OUT, encoding='utf-8') as fh:
        header = fh.readline()
        for ln in fh:
            if rx.search(ln):
                hits.append(ln.rstrip('\n').split('\t'))
    print(f'检索 {pattern!r}：命中 {len(hits)} 条')
    for h in hits:
        kind, path, title, status = (h + ['', '', '', ''])[:4]
        print(f'  [{kind}] {path}')
        print(f'      {title[:150]}')
        if status:
            print(f'      status: {status[:120]}')
    return hits


def check():
    """索引不存在或比任何 proof/*/README.md 旧 ⟹ 退出码 1。"""
    if not os.path.isfile(OUT):
        print('claims.tsv 不存在；请先运行 python tools/hygiene/claim_index.py')
        return 1
    idx_m = os.path.getmtime(OUT)
    newest, newest_path = 0.0, ''
    for root, _, files in os.walk(os.path.join(ROOT, 'proof')):
        for f in files:
            if f in ('README.md', 'theorem.md'):
                p = os.path.join(root, f)
                m = os.path.getmtime(p)
                if m > newest:
                    newest, newest_path = m, p
    if newest > idx_m + 1:
        print(f'claims.tsv 过期：{os.path.relpath(newest_path, ROOT)} 比它新 '
              f'({time.ctime(newest)} > {time.ctime(idx_m)})')
        print('请运行 python tools/hygiene/claim_index.py 重建')
        return 1
    print(f'claims.tsv 是最新的（{time.ctime(idx_m)}）')
    return 0


def main():
    args = sys.argv[1:]
    if args and args[0] == '--grep':
        pat = ' '.join(args[1:]) or '.'
        grep(pat)
        return 0
    if args and args[0] == '--check':
        return check()
    rows = build()
    kinds = {}
    for r in rows:
        kinds[r[0]] = kinds.get(r[0], 0) + 1
    print(f'已写入 {os.path.relpath(OUT, ROOT)}：{len(rows)} 条')
    for k, v in sorted(kinds.items()):
        print(f'  {k}: {v}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
