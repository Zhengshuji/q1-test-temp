r"""**反例（R17）**：阶谱猜想被推翻 —— $d>p$、$q<n_0-p$、$Z\not\subseteq\mathcal V$ 且 $(A)\wedge(S)$。

实例：$n=8$、$p=2$、$r=1$、$C=[e_1;e_2]$，
$$A:\ e_1\mapsto e_3,\ e_2\mapsto e_4,\ e_3\mapsto e_7,\ e_4\mapsto e_8,\ e_5\mapsto e_5,\ e_6\mapsto e_6,\ e_7\mapsto e_1,\ e_8\mapsto e_2 .$$
则 $CA=[e_7;e_8]$、$r_1=\operatorname{rank}[C;CA]=4$、$\mathcal V=\ker[C;CA]=\operatorname{span}(e_3,e_4,e_5,e_6)$、$n_0=6$（$n_0-p=4$）。

对 $q=2$（$d=4$）与 $q=3$（$d=3$）分别枚举 $L_0$ 与 $Z\subseteq\ker[C;L_0]$，找到 $(A)\wedge(S)$ 的点，
且 $Z\not\subseteq\mathcal V$、$q<n_0-p$、$d>p$。

用法：python proof/layer_program/c235_order_refute_v2.py
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import spectral_gcd as SG

N, P, R = 8, 2, 1
C = [[Fr(1) if k == 0 else Fr(0) for k in range(N)],
     [Fr(1) if k == 1 else Fr(0) for k in range(N)]]
A = [[Fr(0)] * N for _ in range(N)]
A[6][2] = Fr(1)   # e3 -> e7
A[7][3] = Fr(1)   # e4 -> e8
A[4][4] = Fr(1)   # e5 -> e5
A[5][5] = Fr(1)   # e6 -> e6
A[0][6] = Fr(1)   # e7 -> e1
A[1][7] = Fr(1)   # e8 -> e2
A[2][0] = Fr(1)   # e1 -> e3
A[3][1] = Fr(1)   # e2 -> e4


def main():
    CA = AI.mul(C, A)
    r1 = AI.rank(AI.vstack([C, CA]))
    Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
    Vc = [[Vv[k][i] for k in range(len(Vv))] for i in range(N)]
    n0rows, cur = [], [list(x) for x in C]
    for _k in range(N):
        n0rows.extend(cur)
        cur = [AI.mul([x], A)[0] for x in cur]
    n0 = AI.rank(n0rows)
    print(f'r1={r1}、dim V={len(Vv)}、n0={n0}、n0-p={n0 - P}')
    print(f'CA = {[[str(x) for x in row] for row in CA]}')
    # 需功能可观测：row L0 ⊆ row O_C
    found = []
    for q in (2, 3):
        d = N - P - q
        hit = None
        for Lidx in itertools.combinations(range(N), R):
            L0 = [[Fr(1) if k == j else Fr(0) for k in range(N)] for j in Lidx]
            if AI.rank(C + L0) < P + R:
                continue
            if AI.rank(n0rows + [L0[0]]) != n0:
                continue                     # 功能可观测
            KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L0)])
            if len(KLv) < d:
                continue
            KL = [[KLv[k][i] for k in range(len(KLv))] for i in range(N)]
            for I in itertools.combinations(range(len(KLv)), d):
                for th in itertools.product((-1, 0, 1), repeat=(len(KLv) - d) * d):
                    W = [[Fr(0)] * d for _ in range(len(KLv))]
                    Iset = set(I)
                    for a, ri in enumerate(I):
                        W[ri][a] = Fr(1)
                    free = [x for x in range(len(KLv)) if x not in Iset]
                    for a, ri in enumerate(free):
                        for b in range(d):
                            W[ri][b] = Fr(th[a * d + b])
                    Z = AI.mul(KL, W)
                    if AI.rank(Z) < d:
                        continue
                    CAZ = AI.mul(CA, Z)
                    Rv = AI.nullspace(CAZ)
                    Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
                    AZ = SG.apply_col(A, Z)
                    AZR = AI.mul(AZ, Rm)
                    M1 = [list(Z[i]) + list(AZR[i]) for i in range(N)]
                    if AI.rank(M1) != d:
                        continue
                    g, h, _c = SG.spectral_gcd_Z(A, C, Z)
                    if SG.pdeg(g) != 0:
                        continue
                    both = [list(Vc[i]) + list(Z[i]) for i in range(N)]
                    s = len(Vv) + d - AI.rank(both)
                    ZinV = (AI.rank(both) == len(Vv))
                    if ZinV or not (q < n0 - P) or not (d > P):
                        continue
                    hit = (q, d, s, len(Vv) - s, L0, Z)
                    break
                if hit:
                    break
            if hit:
                break
        if hit:
            found.append(hit)
            q_, d_, s_, t_, L0_, Z_ = hit
            print(f'\nHIT q={q_}：d={d_}、s={s_}、t={t_}、n0-p={n0 - P}、q<n0-p ✓、d>p ✓、Z⊄V ✓')
            print(f'  L0 = {[[str(x) for x in row] for row in L0_]}')
            print(f'  Z 的列 = {[[str(Z_[i][j]) for j in range(d_)] for i in range(N)]}')
    assert found, '未找到反例'
    print(f'\n⟹ R17：在 q = {[f[0] for f in found]} 上存在 (A)∧(S) 的点，而 q<n0-p、d>p'
          ' ⟹ 阶谱猜想的薄层部分被推翻 ✓')


if __name__ == '__main__':
    main()
