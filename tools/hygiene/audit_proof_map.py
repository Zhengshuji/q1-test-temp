"""audit_proof_map.py —— `proof/` 与 `docs/02` 的**卷宗对照**闸门（2026-11-06 契约）

分工：`docs/` 对整个项目负责（陈述、结论、论文级整理）；`proof/<条目>/README.md` 是该条目的**卷宗**，
统一管理纸面证明、Lean、精确验证、状态与历史。

**阻塞项**（退出码 1）：
1. `proof/` 下每个目录必须恰好出现一次在 `proof/README.md` 的索引表里；
2. 每个目录的 `README.md` 必须有 `对应 docs` 一行；
3. 索引里出现的目录必须真实存在；
4. 卷宗（目录名形如 `B.22`）必须含六个小节：
   `## 命题`、`## 纸面证明`、`## Lean`、`## 精确验证`、`## 状态与历史`；
5. 待建卷宗数不得超过基线（`tools/hygiene/proof_dossier_baseline.txt`，只许下降）。

用法：python tools/hygiene/audit_proof_map.py
"""

import io
import os
import re
import sys

INDEX = os.path.join('proof', 'README.md')
DOCS = os.path.join('docs', '02_theorems_proven.md')
BASE = os.path.join('tools', 'hygiene', 'proof_dossier_baseline.txt')

LINK_RE = re.compile(r'\[([A-Za-z0-9_.\-]+)/\]\(')
MAIN_RE = re.compile(r'^###\s+([A-K]\.\d+[a-z]?)\s+·')
DOSSIER_RE = re.compile(r'^[A-K]\.\d+[a-z]?$')
SECTIONS = ['## 命题', '## 纸面证明', '## Lean', '## 精确验证', '## 验证状态', '## 状态与历史']


def main():
    issues = []
    if not os.path.exists(INDEX):
        print(f'[proof_map] 缺 {INDEX}')
        return 1
    idx = io.open(INDEX, encoding='utf-8').read()
    listed = LINK_RE.findall(idx)
    dirs = sorted(d for d in os.listdir('proof')
                  if os.path.isdir(os.path.join('proof', d)))

    for d in dirs:
        n = listed.count(d)
        if n == 0:
            issues.append(f'[proof_map] 目录未登记进 proof/README.md：{d}')
        elif n > 1:
            issues.append(f'[proof_map] 目录在索引里出现 {n} 次：{d}')
    for d in set(listed):
        if not os.path.isdir(os.path.join('proof', d)):
            issues.append(f'[proof_map] 索引指向不存在的目录：{d}')

    for d in dirs:
        rd = os.path.join('proof', d, 'README.md')
        if not os.path.exists(rd):
            issues.append(f'[proof_map] 缺 README.md：{d}')
            continue
        s = io.open(rd, encoding='utf-8', errors='ignore').read()
        if '对应 docs' not in s:
            issues.append(f'[proof_map] README 缺"对应 docs"一行：{d}')
        if DOSSIER_RE.match(d):
            for sec in SECTIONS:
                if sec not in s:
                    issues.append(f'[proof_map] 卷宗缺小节 `{sec}`：{d}')
            if '对应 docs' not in s:
                pass

    # docs 主条目 ↔ 卷宗
    mains = []
    if os.path.exists(DOCS):
        for ln in io.open(DOCS, encoding='utf-8'):
            m = MAIN_RE.match(ln)
            if m:
                mains.append(m.group(1))
    missing = [m for m in mains if not os.path.isdir(os.path.join('proof', m))]

    base = None
    if os.path.exists(BASE):
        base = int(io.open(BASE, encoding='utf-8').read().strip() or 0)
    if base is not None and len(missing) > base:
        issues.append(f'[proof_map] 待建卷宗数回退：{len(missing)} > 基线 {base}')

    for x in issues:
        print(x)
    print(f'[proof_map] proof 目录 {len(dirs)} 个；索引登记 {len(set(listed))} 个；'
          f'docs 主条目 {len(mains)} 条；已有卷宗 {len(mains) - len(missing)} 条；'
          f'待建 {len(missing)} 条（基线 {base}）')
    if missing:
        print('[proof_map] 待建卷宗（证明目前内联于 docs）：' + ', '.join(missing))
    print(f'[proof_map] 问题 {len(issues)} 处')
    return 0 if not issues else 1


if __name__ == '__main__':
    sys.exit(main())
