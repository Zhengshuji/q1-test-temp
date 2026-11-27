"""class_I_d1.py —— Class I 的 $d=1$ 分类：谱上"好"的直线是否**永远不可容许**？

**背景**：$p=r=1$、$q=n-2$（$d=1$）。$\mathcal Z=\langle z\rangle$ 的**谱**条件（B.18c）只依赖 $z$：
* $z\in V$（即 $z\in V\cap K$）⟹ $S=\mathcal Z$ ⟹ $(5b)$ 自动成立（谱上好）；
* $z\notin V$ ⟹ $(5b)$ 失败 $\iff z\in\operatorname{im}\psi$（B.18d 给出精确判据）。

本脚本问：**谱上好的直线**（$z\notin\operatorname{im}\psi$）是否存在**可容许**的 $\mathcal L$？
做法：给定 $z$，令 $\mathcal L=[\ell;R]$（$R$ 有 $n-3$ 行），要求 $\mathcal L z=0$（于是 $\mathcal Z=\langle z\rangle$
当且仅当 $\operatorname{rank}[C;\mathcal L]=n-1$），再检查 $(5a)$。

用法：python -u tools/verification/class_I_d1.py
"""

import os
import sys
import itertools
import random
from fractions import Fraction
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import sympy as sp                        # noqa: E402
import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import membership_test as MT              # noqa: E402
import psi_image_canonical as PIC         # noqa: E402

F = Fraction
lam = sp.symbols('lam')


def companion(coeffs, n):
    A = [[F(0)] * n for _ in range(n)]
    for j in range(2, n + 1):
        A[j - 2][j - 1] = F(1)
    for j in range(1, n + 1):
        A[n - 1][j - 1] = -coeffs[j - 1]
    return A


def orth_basis_rows(z, n):
    """{y : y·z = 0} 的基（作为行向量的列表）。"""
    zt = [[z[i]] for i in range(n)]        # n × 1
    ns = ZG.ker_cols([[z[i] for i in range(n)]])   # 解 y·z = 0 ⟺ z^T y = 0
    d = len(ns[0]) if (ns and ns[0]) else 0
    return [[ns[i][j] for i in range(n)] for j in range(d)], d


def main():
    rng = random.Random(20261105)
    st = Counter()
    for n in (5, 6, 7):
        for trial in range(25):
            coeffs = [F(rng.randrange(-2, 3)) for _ in range(n)]
            A = companion(coeffs, n)
            C = [[F(1)] + [F(0)] * (n - 1)]
            # ℓ 随机、rank[c;ℓ]=2
            ell = [F(0), F(1)] + [F(rng.randrange(-2, 3)) for _ in range(n - 2)]
            L0 = [ell]
            if LQ.rank([list(x) for x in C] + L0) != 2:
                continue
            K = ZG.ker_cols([list(x) for x in C] + L0)
            if not (K and K[0]):
                continue
            dK = len(K[0])
            for _ in range(8):
                coef = [F(rng.randrange(-3, 4)) for _ in range(dK)]
                z = [sum(K[i][t] * coef[t] for t in range(dK)) for i in range(n)]
                if all(x == 0 for x in z):
                    continue
                # 谱条件
                member = PIC.formula_member(z, coeffs, n)      # z ∈ im ψ ?
                z_in_V = all(z[i] == 0 for i in range(2))      # V = span{e3..en}
                spectrally_good = z_in_V or (not member)
                # 可容许性：在 z^⊥ 里取 R 的行
                rows, dr = orth_basis_rows(z, n)
                if dr < n - 3:
                    continue
                found_adm = False
                for _ in range(12):
                    R = []
                    for _r in range(n - 3):
                        cf = [F(rng.randrange(-2, 3)) for _ in range(dr)]
                        R.append([sum(rows[t][i] * cf[t] for t in range(dr)) for i in range(n)])
                    L = [list(x) for x in L0] + R
                    if LQ.rank([list(x) for x in C] + L) != n - 1:
                        continue
                    # 确认 Z = <z>
                    Zc = ZG.ker_cols([list(x) for x in C] + L)
                    dz = len(Zc[0]) if (Zc and Zc[0]) else 0
                    if dz != 1:
                        continue
                    if LQ.condA(A, C, L):
                        found_adm = True
                        break
                st['样本'] += 1
                if spectrally_good:
                    st['谱上好'] += 1
                    if found_adm:
                        st['谱上好∧可容许'] += 1
                        if st['谱上好∧可容许'] <= 3:
                            print(f'  ★ n={n}：谱上好且可容许的直线！z={[str(x) for x in z]}')
                else:
                    st['谱上坏'] += 1
                    if found_adm:
                        st['谱上坏∧可容许'] += 1
    print('统计：', dict(st))
    print('  关键：谱上好∧可容许 是否为 0（为 0 则 d=1 无可行，q_min=n-1 是结构性的）')


if __name__ == '__main__':
    main()
