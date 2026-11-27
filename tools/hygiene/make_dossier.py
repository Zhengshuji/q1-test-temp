"""批量生成"命题卷宗"：从 docs/02 抽取条目 → proof/<条目>/README.md，并把 docs 条目改成"陈述 + 指针"。

用法：python tools/hygiene/make_dossier.py A.1 B.1 B.2 ...
（脚本自身放在 tools/hygiene/ 下，可复用；不移动任何支撑目录。）
"""
import io
import os
import re
import sys

DOCS = 'docs/02_theorems_proven.md'

TEMPLATE = '''# {main} · {title}

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `{main}` 条目（§0.1 归并表）。

## 命题

{statement}

## 纸面证明

{proof}

## Lean

{lean}

## 精确验证

{check}

## 状态与历史

{status}

## 支撑目录

{sup}
'''


def split_entry(lines, main):
    i = None
    for k, l in enumerate(lines):
        if l.startswith(f'### {main} ·'):
            i = k
            break
    if i is None:
        return None
    j = len(lines)
    for k in range(i + 1, len(lines)):
        if lines[k].startswith('### ') or lines[k].startswith('## 附录'):
            j = k
            break
    while j > i and (lines[j - 1].strip() == '' or lines[j - 1].strip() == '---'):
        j -= 1
    return i, j


def title_of(line):
    return line.split('·', 1)[1].strip() if '·' in line else ''


def level_lines(body):
    """把"等级"信息从行里剥出来：支持 `*等级*：…`、`**等级**：…`、以及
    `*证明*：…**等级**：…` 这种同行混排（返回等级片段，正文保留证明部分）。"""
    out = []
    for l in body.split('\n'):
        for marker in ('**等级**', '*等级*'):
            k = l.find(marker)
            if k >= 0:
                out.append(l[k:].strip())
                break
    return out


def strip_level(body):
    """从正文里删掉等级片段（只留证明）。"""
    keep = []
    for l in body.split('\n'):
        cut = len(l)
        for marker in ('**等级**', '*等级*'):
            k = l.find(marker)
            if k >= 0:
                cut = min(cut, k)
        keep.append(l[:cut].rstrip())
    return '\n'.join(keep)


def main():
    targets = sys.argv[1:]
    if not targets:
        print('用法：python tools/hygiene/make_dossier.py A.1 B.1 …')
        return 1
    text = io.open(DOCS, encoding='utf-8').read()
    lines = text.split('\n')
    for main_ in targets:
        sp = split_entry(lines, main_)
        if not sp:
            print(f'[{main_}] 找不到条目，跳过')
            continue
        i, j = sp
        head = lines[i]
        title = title_of(head)
        body = '\n'.join(lines[i + 1:j]).strip('\n')

        m = re.search(r'^\*证明\*', body, re.M)
        if m:
            statement = body[:m.start()].rstrip()
            proof = body[m.start():].strip()
        else:
            statement, proof = body, '*（证明内联于下方等级行与支撑目录，未单独拆出）*'

        lvls = level_lines(proof)
        proof_wo_lvl = strip_level(proof).rstrip()

        # Lean 段
        lean_hits = re.findall(r'`([A-Za-z][A-Za-z0-9_.]*)`', '\n'.join(lvls))
        if '[Lean' in '\n'.join(lvls):
            lean = '* 等级行引用的 Lean 声明：' + '、'.join(f'`{x}`' for x in lean_hits) if lean_hits else '* 见下方"状态与历史"的等级行'
            lean += '\n* 差在哪里：见等级行括注（内核一般只覆盖代数/维数骨架，矩阵实例化多为纸面）'
        else:
            lean = '* 无独立 Lean 内核（该条为纸面证明）。'

        # 精确验证段
        paths = re.findall(r'`(tools/[A-Za-z0-9_./\-]+)`', '\n'.join(lvls))
        if paths:
            check = '\n'.join(f'* `{p}`' for p in paths)
        elif '[精确验证' in '\n'.join(lvls):
            check = '* 见等级行给出的精确验证数字。'
        else:
            check = '* 该条暂无独立精确验证脚本（纸面证明 + 支撑目录）。'

        status = '\n'.join(lvls) if lvls else '* 等级：见 docs/02 同条目。'
        status += '\n* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。'

        # 支撑目录：从 proof/README.md 索引里找该条目那一行
        idx = io.open('proof/README.md', encoding='utf-8').read()
        sup = '—'
        for ln in idx.split('\n'):
            if ln.startswith(f'| {main_} ·'):
                cells = [c.strip() for c in ln.strip().strip('|').split('|')]
                if len(cells) >= 3 and cells[2] not in ('—', ''):
                    sup = cells[2]
                break
        if sup != '—':
            # 索引里的链接是相对 proof/ 的；卷宗在 proof/<条目>/ 下，需要 ../
            sup = re.sub(r'\]\(proof/', '](../', sup)
            sup = re.sub(r'\]\((?![./])', '](../', sup)
            sup = re.sub(r'\]\(\.\./(tools|workspace|literature|archive|trash|docs)/', r'](../../\1/', sup)
            sup = sup + '\n\n（本卷宗只汇总证据；支撑目录里的脚本与文档保持原位。）'
        else:
            sup = '无（证据全部在本卷宗内）。'

        d = os.path.join('proof', main_)
        os.makedirs(d, exist_ok=True)
        rendered = TEMPLATE.format(main=main_, title=title, statement=statement,
                                   proof=proof_wo_lvl, lean=lean, check=check,
                                   status=status, sup=sup)
        # 卷宗位于 proof/<条目>/：把仓库根相对的链接改成正确层级
        rendered = rendered.replace('](../proof/', '](../')
        rendered = rendered.replace('](proof/', '](../')
        rendered = re.sub(r'\]\((tools|workspace|literature|archive|trash|docs)/',
                          r'](../../\1/', rendered)
        rendered = re.sub(r'\]\(\.\./(tools|workspace|literature|archive|trash|docs)/',
                          r'](../../\1/', rendered)
        io.open(os.path.join(d, 'README.md'), 'w', encoding='utf-8', newline='\n').write(rendered)

        # docs 条目 → 陈述 + 指针 + 等级
        new = [head, '', statement, '',
               f'*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 '
               f'[proof/{main_}/](../proof/{main_}/README.md)。']
        new += lvls
        lines[i:j] = new
        print(f'[{main_}] 卷宗写好（陈述 {len(statement)} 字符，证明 {len(proof_wo_lvl)} 字符，等级行 {len(lvls)}）')

    io.open(DOCS, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines))
    print('docs/02 已更新')
    return 0


if __name__ == '__main__':
    sys.exit(main())
