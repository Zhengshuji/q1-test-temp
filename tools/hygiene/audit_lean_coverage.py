"""audit_lean_coverage.py —— `proof/lean_coverage.md` 与 `docs/02` 的 **Lean 覆盖一致性**闸门

**为什么要有这个**：`proof/lean_coverage.md` 是手工维护的"命题 × 支撑等级"表，历史上多次滞后
（2026-11-04 查出 B.1、B.2、B.3、B.5、A.2、C.1、D.1、H.2 八行写着 ✗ 但其实早有 Lean）。
本脚本把两边对齐，防止再漂移：

* 从 `docs/02_theorems_proven.md` 抽出每条命题（`**X.n（...）**` 形式）的正文块，
  看块里是否出现 `[Lean]`；
* 从 `proof/lean_coverage.md` 抽出表格行 `| X.n | ... | ... | ✓/✗ | ... |`；
* 比对：docs 说 `[Lean]` 而表说 ✗（漏标），或反向（虚标）。

退出码 0 = 一致，1 = 有不一致（逐条打印）。

用法：python tools/hygiene/audit_lean_coverage.py
"""

import io
import os
import re
import sys

DOCS = os.path.join('docs', '02_theorems_proven.md')
COV = os.path.join('proof', 'lean_coverage.md')

# docs/02 里的命题块起点：**A.1**、**B.9b（...）**、**C.1–C.5** 等
PROP_RE = re.compile(r'^\*\*([A-Z]\.(?:\d+[a-z]?|[0-9]+(?:–[0-9]+)?))(?:（|\*\*|\s)')
# coverage 表的行：| B.9b | ... | ... | **✓** | ... |
ROW_RE = re.compile(r'^\|\s*([A-Z]\.(?:\d+[a-z]?|[0-9]+(?:–[0-9]+)?))\s*\|(.*)$')
# docs/02 §0.1 的归并表行：| 旧编号 | 新主条目 · 标题 | （a）|
ALIAS_RE = re.compile(r'^\|\s*([A-Z]\.\d+[a-z]?)\s*\|\s*([A-Z]\.\d+[a-z]?)\s*·')


def aliases():
    """从 docs/02 §0.1 读出 `旧标签 -> 新主条目`，供覆盖表按别名对账。"""
    if not os.path.exists(DOCS):
        return {}
    out = {}
    for ln in io.open(DOCS, encoding='utf-8'):
        m = ALIAS_RE.match(ln.strip())
        if m:
            old, new = m.group(1), m.group(2)
            if old != new:
                out[old] = new
    return out


def docs_props():
    """返回 {id: has_lean}。块按下一个命题起点切分。"""
    text = io.open(DOCS, encoding='utf-8').read()
    lines = text.split('\n')
    starts = []          # (line_index, id)
    for i, ln in enumerate(lines):
        m = PROP_RE.match(ln)
        if m:
            starts.append((i, m.group(1)))
    out = {}
    for k, (i, pid) in enumerate(starts):
        j = starts[k + 1][0] if k + 1 < len(starts) else len(lines)
        block = '\n'.join(lines[i:j])
        # 只认 [Lean] / [Lean 内核]；[已证-纸面] 不算
        has = ('[Lean' in block) or ('[Lean 内核' in block)
        # 同一主条目有多个分部时按"或"累积（分部顺序不影响结论）
        out[pid] = out.get(pid, False) or has
    return out


def coverage_rows(alias=None):
    """返回 {id: cell} —— 第 4 列（Lean？）的内容。id 已按 §0.1 归并表规范化。"""
    alias = alias or {}
    text = io.open(COV, encoding='utf-8').read()
    out = {}
    for ln in text.split('\n'):
        m = ROW_RE.match(ln.strip())
        if not m:
            continue
        pid = m.group(1)
        pid = alias.get(pid, pid)
        cells = [c.strip() for c in ln.strip().strip('|').split('|')]
        if len(cells) >= 4:
            prev = out.get(pid)
            # 同一主条目多行合并：任一写 ✓ 即视为 ✓
            cur = cells[3]
            if prev is None or '✓' in cur:
                out[pid] = cur if prev is None or '✓' not in prev else prev
    return out


def main():
    if not os.path.exists(DOCS):
        print(f'[coverage] 缺 {DOCS}')
        return 1
    if not os.path.exists(COV):
        print(f'[coverage] 缺 {COV}')
        return 1
    d = docs_props()
    al = aliases()
    c = coverage_rows(al)
    # docs 侧也按别名规范化（分部块已并入主条目，理论上不需要，但保留以防单列分部）
    d = {al.get(k, k): v for k, v in d.items()} if False else d
    issues = []
    for pid, has in sorted(d.items()):
        cell = c.get(pid)
        if cell is None:
            continue                    # 表里没有这一行不报错（表可以选择性收录）
        cell_lean = ('✓' in cell)
        if has and not cell_lean:
            issues.append(f'[coverage] docs/02 标了 [Lean] 但覆盖表写 ✗：{pid}')
        if cell_lean and not has:
            issues.append(f'[coverage] 覆盖表写 ✓ 但 docs/02 没有 [Lean]：{pid}')
    for x in issues:
        print(x)
    print(f'覆盖表行 {len(c)} 条；docs/02 命题 {len(d)} 条；不一致 {len(issues)} 处')
    return 0 if not issues else 1


if __name__ == '__main__':
    sys.exit(main())
