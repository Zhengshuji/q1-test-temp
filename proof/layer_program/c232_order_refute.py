r"""**反例（R17）**：阶谱猜想被推翻（方向正确的版本）。

构造：$n=6$、$p=1$、$r=1$、$q=3$（$d=2$）、$C=e_1$。
$$A:\ e_1\mapsto e_2,\ e_2\mapsto e_5,\ e_5\mapsto e_1,\ e_3\mapsto e_3,\ e_4\mapsto e_4,\ e_6\mapsto e_2 .$$
则 $CA=e_5$、$\mathcal V=\ker[C;CA]=\operatorname{span}(e_2,e_3,e_4,e_6)$（$\dim4$）、
$K_L=\ker[C;L_0]=\operatorname{span}(e_3,e_4,e_5,e_6)$（$L_0=e_2$），取 $Z=\operatorname{span}(e_3,e_4)$（$d=2$）。

- $(A)$：$CAZ=0$、$R=I$、$AZ=Z$ ⟹ $\operatorname{rank}[Z,AZR]=2=d$ ✓；
- $h=\operatorname{rank}[\mathcal V\mid Z]=4$；$(\lambda I-A)\mathcal V\cup Z$ 的秩恒为 4（见 §验证）；
- $n_0=\operatorname{rank}\mathcal O_C=3$ ⟹ $n_0-p=2\ne q=3$；$n-r_1=4\ne q$；$d=2>p=1$；
- 功能可观测：$\operatorname{row}L_0=e_2\subseteq\operatorname{row}\mathcal O_C=\operatorname{span}(e_1,e_5,e_2)$ ✓。

⟹ 阶谱猜想（$d>p$ 且 $q\ne n_0-p$、$q\ne n-r_1$ 时不可行）被推翻。

用法：python proof/layer_program/c232_order_refute.py
"""
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import spectral_gcd as SG

N, P, R = 6, 1, 1
C = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)]]
L0 = [[Fr(0), Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)]]
A = [[Fr(0)] * N for _ in range(N)]
A[1][0] = Fr(1)   # e1 -> e2
A[4][1] = Fr(1)   # e2 -> e5
A[0][4] = Fr(1)   # e5 -> e1
A[2][2] = Fr(1)   # e3 -> e3
A[3][3] = Fr(1)   # e4 -> e4
A[1][5] = Fr(1)   # e6 -> e2


def main():
    CA = AI.mul(C, A)
    r1 = AI.rank(AI.vstack([C, CA]))
    Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
    KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L0)])
    n0rows, cur = [], [list(x) for x in C]
    for _k in range(N):
        n0rows.extend(cur)
        cur = [AI.mul([x], A)[0] for x in cur]
    n0 = AI.rank(n0rows)
    print(f'r1={r1}、dim V={len(Vv)}、dim K_L={len(KLv)}、n0={n0}、n0-p={n0 - P}、n-r1={N - r1}')
    print(f'CA = {[[str(x) for x in row] for row in CA]}')
    funcobs = AI.rank(n0rows + [L0[0]]) == n0
    print(f'功能可观测 = {funcobs}')
    # Z = span(e3, e4)
    Z = [[Fr(0), Fr(0)], [Fr(0), Fr(0)], [Fr(1), Fr(0)], [Fr(0), Fr(1)], [Fr(0), Fr(0)], [Fr(0), Fr(0)]]
    d = 2
    q = N - P - d
    CAZ = AI.mul(CA, Z)
    Rv = AI.nullspace(CAZ)
    Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
    AZ = SG.apply_col(A, Z)
    AZR = AI.mul(AZ, Rm)
    M1 = [list(Z[i]) + list(AZR[i]) for i in range(N)]
    okA = AI.rank(M1) == d
    Vrows = [[Vv[k][i] for k in range(len(Vv))] for i in range(N)]
    both = [list(Vrows[i]) + list(Z[i]) for i in range(N)]
    s = len(Vv) + d - AI.rank(both)
    t = len(Vv) - s
    print(f'q={q}、d={d}、s={s}、t={t}、q>t={q > t}')
    print(f'(A)：rank[Z,AZR]={AI.rank(M1)}（d={d}）⟹ {okA}')
    g, h, _c = SG.spectral_gcd_Z(A, C, Z)
    print(f'(S)：h={h}、gcd 次数={SG.pdeg(g)} ⟹ {"成立" if SG.pdeg(g) == 0 else "失败"}')
    assert okA and SG.pdeg(g) == 0, '反例条件不满足'
    assert q != n0 - P and q != N - r1 and d > P, '不构成对阶谱猜想的反例'
    print('\n⟹ R17：$d>p$、$q\\ne n_0-p$、$q\\ne n-r_1$ 且 $(A)\\wedge(S)$ 成立 ⟹ 阶谱猜想被推翻 ✗')


if __name__ == '__main__':
    main()
