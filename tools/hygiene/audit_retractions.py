"""一致性检查（**只扫 docs/ 与 proof/**；archive/ 是历史记录，编号体系不同，不扫）：所有**已撤回**的结论，在文档里每次出现都必须带"撤回/作废/不成立"之类的标记。

动机：本会话有 9 次撤回，分布在多个文件里。若某一处残留"正面引用"，以后就会有人（包括我自己）
把它当成已证结论。这个脚本把那种情况找出来。

用法：python tools/hygiene/audit_retractions.py
退出码：0 = 全部带标记；1 = 有正面引用残留。
"""
import io
import os
import re
import sys

# (名字, 匹配模式, 允许/要求的标记词)
CLAIMS = [
    ('定理 8（层级别 iff）', r'定理\s*8', ['撤回', '作废', '不要引用', '错', '失效', '降级', '阅读警告', 'withdrawn', 'retracted', 'false', 'does not']),
    ('定理 13（层级别 iff）', r'定理\s*13', ['撤回', '作废', '不要引用', '错', '失效', '降级', '阅读警告', '待重述']),
    ('c.i. 交封闭 / 最小元', r'交封闭|最小元|推论\s*15', ['撤回', '作废', '错', '不成立', '反例', '失效', 'withdrawn', 'retracted', 'false', 'counterexample']),
    ('引理 37.1', r'引理\s*37\.1|37\.1（', ['撤回', '作废', '错', '不成立', '反例', '失效', 'withdrawn', 'retracted', 'false', 'counterexample']),
    ('定理 37.2', r'定理\s*37\.2', ['撤回', '作废', '错', '失效', '依赖', 'withdrawn', 'retracted', 'used it']),
    ('§43 的 232/232', r'232/232', ['不可信', '撤回', '不成立', '未验', '作废', 'withdrawn', 'retracted', 'fatal', 'does not']),
]

ROOTS = ['docs', 'proof', '.']   # archive/ 是历史记录，编号体系与本项目不同，不扫（见 docstring）
EXTS = ('.md',)


def iter_md():
    seen = set()
    for root in ROOTS:
        for dirpath, _, files in os.walk(root):
            parts = dirpath.replace('\\', '/').split('/')
            if 'trash' in parts or 'archive' in parts or 'literature' in parts:
                continue
            for f in files:
                if f.endswith(EXTS):
                    p = os.path.normpath(os.path.join(dirpath, f))
                    if p in seen:
                        continue
                    seen.add(p)
                    yield p


def main():
    issues = []
    checked = 0
    for path in iter_md():
        try:
            text = io.open(path, encoding='utf-8').read()
        except Exception:
            continue
        lines = text.split('\n')
        for name, pat, markers in CLAIMS:
            for i, ln in enumerate(lines):
                if not re.search(pat, ln):
                    continue
                checked += 1
                # 上下文 = 所属 ## 小节**整段**（标题 + 正文）+ 文件前 6 行（总说明）
                start = 0
                for k in range(i, -1, -1):
                    if lines[k].startswith('## '):
                        start = k
                        break
                end = len(lines)
                for k in range(i + 1, len(lines)):
                    if lines[k].startswith('## '):
                        end = k
                        break
                ctx = '\n'.join(lines[:6]) + '\n' + '\n'.join(lines[start:end])
                if any(m in ctx for m in markers):
                    continue
                issues.append((path, i + 1, name, ln.strip()[:90]))
    print('=' * 76)
    print(f'audit_retractions: 检查了 {checked} 处提及，{len(issues)} 处可能缺少撤回标记')
    print('=' * 76)
    for p, n, name, line in issues[:20]:
        print(f'  [{name}] {p}:{n}')
        print(f'      {line}')
    if issues:
        print(f'\n共 {len(issues)} 处。若确认这些不是"正面引用"，请在附近加上撤回/作废标记。')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
