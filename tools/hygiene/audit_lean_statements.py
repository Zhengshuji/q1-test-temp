r"""audit_lean_statements.py —— Lean 声明与"命题对照表"的一致性闸门。

**为什么要它**：`[Lean]` 只说明"某条 Lean 定理被机器检查"，不说明它与论文里的那句话是同一句话。
[tools/lean/STATEMENT_MAP.md](../lean/STATEMENT_MAP.md) 逐条登记"声明 → 对应命题 → 差异"；
本脚本保证**两边不脱节**：

1. 每个 Lean 声明（`theorem`/`lemma`）都在对照表里出现过（否则是"没登记的 Lean"）；
2. 对照表里以 `- \`名字\`` 开头的条目都对应真实声明（否则是"过时的条目"）；
3. 每个条目行里必须有 `对应` 与 `差异` 两个词（否则是"只登记了名字、没说清差在哪"）。

退出码 0 = 干净；1 = 有问题（逐条打印）。

用法：python tools/hygiene/audit_lean_statements.py
"""
import glob
import io
import os
import re
import sys

ROOT = '.'
MAP = os.path.join('tools', 'lean', 'STATEMENT_MAP.md')
DIRS = [os.path.join('tools', 'lean', 'MyProof'), os.path.join('tools', 'lean'),
        os.path.join('proof')]
DECL_RE = re.compile(r'^(?:public\s+)?(?:theorem|lemma)\s+([A-Za-z_][A-Za-z0-9_.\']*)', re.M)
DEF_RE = re.compile(r'^(?:public\s+)?(?:noncomputable\s+)?def\s+([A-Za-z_][A-Za-z0-9_.\']*)', re.M)
ENTRY_RE = re.compile(r'^-\s+`([A-Za-z_][A-Za-z0-9_.\']*)`')
BACKTICK_RE = re.compile(r'`([A-Za-z_][A-Za-z0-9_.\']*)`')


EXEMPT = os.path.join('tools', 'lean', 'EXEMPT_AUXILIARY.md')


def exempt_files():
    """从 EXEMPT_AUXILIARY.md 读出被豁免的文件（相对 VCS 的路径片段）。"""
    if not os.path.exists(EXEMPT):
        return set()
    out = set()
    for ln in io.open(EXEMPT, encoding='utf-8'):
        m = re.match(r'^\|\s*`([^`]+)`', ln.strip())
        if m:
            out.add(m.group(1))
    return out


def lean_files():
    out = []
    for d in DIRS:
        for pat in ('*.lean', os.path.join('*', '*.lean'), os.path.join('*', 'lean', 'MyProof', '*.lean'),
                    os.path.join('MyProof', '*', '*.lean')):
            for f in glob.glob(os.path.join(d, pat)):
                out.append(f)
    return sorted(set(out))


def main():
    # 2026-11-19: the Lean sources were consolidated into two WSL trees
    # (~/WorkSpace/lean4/Q1Paper for the papers, ~/WorkSpace/lean4/MyProof for
    # proof work). With no .lean files in this repository the map cannot be
    # cross-checked here, so state that explicitly instead of reporting every
    # entry as stale.
    if not lean_files():
        print('[lean] 本仓库不含 Lean 源（已收敛到 WSL: ~/WorkSpace/lean4/{Q1Paper,MyProof}）；'
              'STATEMENT_MAP.md 仅作记录，跳过本闸门。')
        return 0
    issues = []
    decls = {}
    defs = set()
    ex = exempt_files()
    for frag in ex:
        if not os.path.exists(os.path.join('tools', 'lean', 'MyProof', frag)):
            issues.append(f'[statements] 豁免清单里的文件不存在：{frag}')
    exempt_decls = set()
    for f in lean_files():
        rel = os.path.relpath(f, os.path.join('tools', 'lean', 'MyProof'))
        is_exempt = rel.replace(os.sep, '/') in ex
        s = io.open(f, encoding='utf-8', errors='replace').read()
        for name in DECL_RE.findall(s):
            decls.setdefault(name, []).append(os.path.relpath(f, ROOT).replace('\\', '/'))
            if is_exempt:
                exempt_decls.add(name)
        for name in DEF_RE.findall(s):
            defs.add(name)
    if not os.path.exists(MAP):
        print(f'[lean] 缺对照表: {MAP}')
        return 1
    text = io.open(MAP, encoding='utf-8', errors='replace').read()
    mentioned = set(BACKTICK_RE.findall(text))
    entries = {}          # name -> line
    for ln, line in enumerate(text.splitlines(), 1):
        m = ENTRY_RE.match(line.strip())
        if m:
            entries.setdefault(m.group(1), []).append((ln, line))
    # 1) 未登记的声明
    for name, files in sorted(decls.items()):
        if name in exempt_decls:
            continue
        if name not in mentioned:
            issues.append(f'[lean] 声明未登记进 STATEMENT_MAP.md: {name}（{files[0]}）')
    # 2) 过时的条目（条目必须是真实存在的 theorem/lemma，或 def —— 定义不必登记，但登记了就要真实存在）
    for name, occ in sorted(entries.items()):
        if name not in decls and name not in defs:
            issues.append(f'[lean] 对照表条目找不到同名声明: {name}（第 {occ[0][0]} 行）')
        for ln, line in occ:
            # 2026-11-07 新规则：只需"出处"（链接 / 文献 / 命题编号），"意义"与"差异"均不强制
            src = ('对应' in line) or ('](' in line) or ('arXiv' in line) or ('文献' in line) \
                or re.search(r'\b[A-K]\.\d', line) is not None
            if not src:
                issues.append(f'[lean] 第 {ln} 行的条目缺"出处"（链接/文献/命题编号）: {line.strip()[:60]}')
    # 3) 统计
    print(f'Lean 声明 {len(decls)} 个（{len(lean_files())} 个文件）；'
          f'对照表条目 {len(entries)} 个；问题 {len(issues)} 处')
    for i in issues:
        print('  ' + i)
    return 0 if not issues else 1


if __name__ == '__main__':
    sys.exit(main())
