# -*- coding: utf-8 -*-
"""
修复 KaTeX 报错：把**含中文的数学片段**转成纯文本/Unicode。

原则：
  · 只处理**包含 CJK 字符**的 $...$ / $$...$$ 片段（纯数学片段不动，KaTeX 能正常渲染）
  · 去掉 $ 定界符，把常见 LaTeX 命令换成 Unicode / 纯文本
  · 保守：只做安全替换，不改动其余正文
用法：
  python fix_katex.py <根目录> [--dry]
"""
import os
import re
import sys

CJK = re.compile(r'[\u3000-\u303f\u4e00-\u9fff\uff00-\uffef]')

# LaTeX 命令 → Unicode / 文本（按长度降序替换，避免前缀冲突）
MAP = [
    (r'\operatorname{rank}', 'rank'), (r'\mathrm{rank}', 'rank'),
    (r'\operatorname{rows}', 'rows'), (r'\operatorname{row}', 'row'),
    (r'\operatorname{im}', 'im'), (r'\operatorname{int}', 'int'),
    (r'\operatorname{vol}', 'vol'), (r'\operatorname{diag}', 'diag'),
    (r'\operatorname{spec}', 'spec'), (r'\operatorname{Gr}', 'Gr'),
    (r'\mathrm{Gr}', 'Gr'), (r'\mathrm{MFOSP}', 'MFOSP'),
    (r'\mathcal L', 'L'), (r'\mathcal R', 'R'), (r'\mathcal N', 'N'),
    (r'\mathcal U', 'U'), (r'\mathcal I', 'I'), (r'\mathcal G', 'G'),
    (r'\mathcal C', 'C'), (r'\mathcal O', 'O'), (r'\mathcal S', 'S'),
    (r'\mathbb C', 'C'), (r'\mathbb R', 'R'), (r'\mathbb N', 'N'),
    (r'\mathbb P', 'P'),
    (r'\Lambda', 'Λ'), (r'\Theta', 'Θ'), (r'\Sigma', 'Σ'), (r'\Omega', 'Ω'),
    (r'\Phi', 'Φ'), (r'\Psi', 'Ψ'), (r'\Delta', 'Δ'), (r'\Gamma', 'Γ'),
    (r'\lambda', 'λ'), (r'\eta', 'η'), (r'\nu', 'ν'), (r'\mu', 'μ'),
    (r'\rho', 'ρ'), (r'\beta', 'β'), (r'\gamma', 'γ'), (r'\alpha', 'α'),
    (r'\varepsilon', 'ε'), (r'\theta', 'θ'), (r'\sigma', 'σ'), (r'\tau', 'τ'),
    (r'\varphi', 'φ'), (r'\phi', 'φ'), (r'\pi', 'π'), (r'\zeta', 'ζ'),
    (r'\iff', ' ⟺ '), (r'\Longleftrightarrow', ' ⟺ '), (r'\longleftrightarrow', ' ↔ '),
    (r'\Longrightarrow', ' ⟹ '), (r'\implies', ' ⟹ '), (r'\Rightarrow', ' ⇒ '),
    (r'\Longleftarrow', ' ⟸ '), (r'\leftarrow', ' ← '), (r'\mapsto', ' ↦ '),
    (r'\subseteq', ' ⊆ '), (r'\supseteq', ' ⊇ '), (r'\subsetneq', ' ⊊ '),
    (r'\subset', ' ⊂ '), (r'\supset', ' ⊃ '), (r'\in', ' ∈ '), (r'\notin', ' ∉ '),
    (r'\ne', ' ≠ '), (r'\neq', ' ≠ '), (r'\le', ' ≤ '), (r'\leq', ' ≤ '),
    (r'\ge', ' ≥ '), (r'\geq', ' ≥ '), (r'\approx', ' ≈ '), (r'\equiv', ' ≡ '),
    (r'\forall', ' ∀ '), (r'\exists', ' ∃ '), (r'\nexists', ' ∄ '),
    (r'\emptyset', '∅'), (r'\varnothing', '∅'), (r'\cap', ' ∩ '), (r'\cup', ' ∪ '),
    (r'\wedge', ' ∧ '), (r'\vee', ' ∨ '), (r'\oplus', ' ⊕ '), (r'\otimes', ' ⊗ '),
    (r'\perp', ' ⊥ '), (r'\parallel', ' ∥ '), (r'\circ', ' ∘ '),
    (r'\sum', 'Σ'), (r'\prod', 'Π'), (r'\int', '∫'),
    (r'\dim', 'dim '), (r'\ker', 'ker '), (r'\det', 'det '), (r'\min', 'min '),
    (r'\max', 'max '), (r'\deg', 'deg '), (r'\gcd', 'gcd '), (r'\lim', 'lim '),
    (r'\operatorname', ''),
    (r'\boxed', ''), (r'\underbrace', ''), (r'\textbf', ''), (r'\text', ''),
    (r'\mathrm', ''), (r'\mathit', ''), (r'\mathbf', ''), (r'\boldsymbol', ''),
    (r'\big', ''), (r'\Big', ''), (r'\bigg', ''), (r'\Bigg', ''),
    (r'\left', ''), (r'\right', ''),
    (r'\qquad', '   '), (r'\quad', '  '), (r'\,', ' '), (r'\;', ' '), (r'\!', ''),
    (r'\colon', ':'), (r'\to', ' → '), (r'\dots', '…'), (r'\cdots', '⋯'),
    (r'\ldots', '…'), (r'\square', ' □ '), (r'\checkmark', ' ✓ '),
    (r'\star', '*'), (r'\ast', '*'), (r'\#', '#'), (r'\%', '%'),
    (r'\begin{cases}', ' '), (r'\end{cases}', ' '),
    (r'\begin{aligned}', ' '), (r'\end{aligned}', ' '),
    (r'\begin{bmatrix}', '['), (r'\end{bmatrix}', ']'),
    (r'\begin{pmatrix}', '('), (r'\end{pmatrix}', ')'),
    (r'\hline', ' '), (r'\times', ' × '), (r'\cdot', ' · '),
    (r'\mathbb', ''), (r'\mathcal', ''), (r'\text{', '{'),
]


def demath(s: str) -> str:
    """把一段 LaTeX（已含中文）转成纯文本"""
    for a, b in MAP:
        s = s.replace(a, b)
    s = s.replace('\\', '')          # 剩余的命令反斜杠
    s = re.sub(r'[{}]', '', s)       # 去掉花括号
    s = re.sub(r'_{([^}]*)}', r'_\1', s)
    s = re.sub(r'\^({[^}]*})', r'^\1', s)
    s = re.sub(r'[ \t]{3,}', '   ', s)
    s = re.sub(r'\n{3,}', '\n\n', s)
    return s.strip()


def fix_text(txt: str):
    """返回 (新文本, 修改数)"""
    n = 0

    def repl_display(m):
        nonlocal n
        body = m.group(1)
        if CJK.search(body):
            n += 1
            return demath(body)
        return m.group(0)

    def repl_inline(m):
        nonlocal n
        body = m.group(1)
        if CJK.search(body):
            n += 1
            return demath(body)
        return m.group(0)

    # 先处理 $$...$$（可跨行），再处理 $...$（单行内）
    txt = re.sub(r'\$\$(.+?)\$\$', repl_display, txt, flags=re.S)
    txt = re.sub(r'(?<!\$)\$([^$\n]+?)\$(?!\$)', repl_inline, txt)
    return txt, n


def main():
    root = sys.argv[1]
    dry = '--dry' in sys.argv
    targets = []
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in ('.git', '__pycache__', 'history')]
        for f in files:
            if f.endswith('.md'):
                targets.append(os.path.join(base, f))
    total = 0
    for p in sorted(targets):
        raw = open(p, encoding='utf-8').read()
        new, n = fix_text(raw)
        if n:
            total += n
            print(f"{'[dry] ' if dry else ''}修 {n:>3} 处  {os.path.relpath(p, root)}")
            if not dry:
                open(p, 'w', encoding='utf-8', newline='').write(new)
    print(f"\n合计修复 {total} 处（{len(targets)} 个 md 文件）")


if __name__ == '__main__':
    main()
