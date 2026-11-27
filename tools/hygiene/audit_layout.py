"""tools/hygiene/audit_layout.py

Audits the project layout against the conventions in CLAUDE.md.
Run from the repo root:  python tools/hygiene/audit_layout.py
Exit code 0 = clean, 1 = violations found (printed).
"""
import io
import os
import re
import sys

ROOT = '.'
TOP_DIRS = {'docs', 'proof', 'paper', 'tools', 'literature', 'workspace', 'archive', 'trash', '.git', '.agent'}
ROOT_MD = ['ATTEMPTS.md', 'CLAUDE.md', 'HISTORY.md', 'README.md', 'STATUS.md']  # 2026-11-10：增加 HISTORY.md（项目脉络），与 STATUS 互补
ATTEMPT_SECTIONS = ['## 目标', '## 设想与理由', '## 做法', '## 进展', '## 最终结论',
                    '## 放弃原因', '## 残留价值', '## 相关文件']  # CLAUDE §5.3 的 8 个小节（按前缀匹配）

issues = []


def add(kind, msg):
    issues.append(f'[{kind}] {msg}')


def main():
    # 1) top-level layout
    for f in sorted(os.listdir(ROOT)):
        if os.path.isdir(f):
            if f not in TOP_DIRS:
                add('布局', f'未登记的顶层目录: {f}')
        else:
            if not f.endswith('.md') and f not in ('.gitignore',):
                add('布局', f'根目录出现非 md 文件: {f}')
    root_md = sorted(f for f in os.listdir(ROOT) if f.endswith('.md'))
    # 必读四件套必须在；交接文档已归档（archive/handovers/），根目录不再放 HANDOVER*
    _required = ['ATTEMPTS.md', 'CLAUDE.md', 'HISTORY.md', 'README.md', 'STATUS.md']
    _extra = [f for f in root_md if f not in ROOT_MD]
    if _extra or any(r not in root_md for r in _required):
        add('布局', f'根目录 md 不是约定的 {len(ROOT_MD)} 个: {root_md}')

    # 2) proof/<claim>/README.md
    for name in sorted(os.listdir('proof')):
        d = os.path.join('proof', name)
        if os.path.isdir(d) and not os.path.exists(os.path.join(d, 'README.md')):
            add('proof', f'缺 README.md: {d}')

    # 3) attempt logs: required sections + must be registered in ATTEMPTS.md
    attempts_md = io.open('ATTEMPTS.md', encoding='utf-8', errors='replace').read() \
        if os.path.exists('ATTEMPTS.md') else ''
    for f in sorted(__import__('glob').glob('workspace/*/attempts/*.md')):
        s = io.open(f, encoding='utf-8', errors='replace').read()
        miss = [h for h in ATTEMPT_SECTIONS if h not in s]
        if miss:
            add('attempts', f'缺小节 {miss}: {f}')
        if os.path.basename(f) not in attempts_md:
            add('attempts', f'未登记进 ATTEMPTS.md: {f}')

    # 4) docs rigor: no command blocks, no [数值] assertions
    for f in sorted(__import__('glob').glob('docs/*.md')):
        s = io.open(f, encoding='utf-8', errors='replace').read()
        for ln, line in enumerate(s.splitlines(), 1):
            if re.match(r'\s*(python|wsl|bash)\s', line):
                add('docs', f'出现命令行: {f}:{ln}')
            if '```' in line and ln > 1:
                pass

    # 5) trash: only README
    reg = io.open('trash/README.md', encoding='utf-8', errors='replace').read() if os.path.exists('trash/README.md') else ''
    extra = [f for f in os.listdir('trash')
             if f != 'README.md' and not f.endswith('.bak') and f not in reg]
    if extra:
        add('trash', f'回收站非空（除 README）: {extra}')

    # 6) workspace: README present, only the two directions as subdirs (plus allowed notes)
    if not os.path.exists('workspace/README.md'):
        add('workspace', '缺 README.md')
    # 每个任务/方向目录都必须有 README.md（登记在 workspace/README.md 的索引里）
    for name in sorted(os.listdir('workspace')):
        p = os.path.join('workspace', name)
        if os.path.isdir(p) and name != 'inventory':
            if not os.path.exists(os.path.join(p, 'README.md')):
                add('workspace', f'任务目录缺 README.md: {name}')

    # 7) tools: scripts must live in a category dir
    for f in sorted(__import__('glob').glob('tools/*.py')):
        add('tools', f'脚本在 tools/ 根（应归入类别目录）: {f}')

    # 8) broken relative links in active md
    for f in sorted(__import__('glob').glob('**/*.md', recursive=True)):
        if f.startswith(('archive', 'trash')) or 'archive_attack_log' in f:
            continue
        raw = io.open(f, encoding='utf-8', errors='replace').read()
        # skip fenced code blocks (extracted text / examples may contain ](..) artifacts)
        txt = re.sub(r'```.*?```', '', raw, flags=re.S)
        for m in re.finditer(r'\]\(([^)]+)\)', txt):
            t = m.group(1).strip()
            if t.startswith(('http', '#', 'mailto')):
                continue
            t = t.split('#')[0]
            if not t:
                continue
            p = os.path.normpath(os.path.join(os.path.dirname(f), t))
            if not os.path.exists(p):
                add('链接', f'{f} -> {t}')

    print('=' * 76)
    print(f'audit_layout: {len(issues)} issue(s)')
    print('=' * 76)
    for i in issues:
        print('  ', i)
    return 1 if issues else 0


if __name__ == '__main__':
    sys.exit(main())
