r"""实现专家 QA10 的"抽象商铅笔"例子（Q2 的第一步）。

专家给的抽象对：$\iota(x)=\binom{x}{0}$、$\bar A(x)=\binom{0}{x}$（$t=1$、$q=2$），此时 $\lambda\iota-\bar A$
对所有 $\lambda$ 满列秩。问题是它能否来自功能可观测的 $(A,C,L_0)$ 且满足 $(A)$。

本脚本构造一个**显式实例**：
- $n=5$、$p=1$、$r=1$、$q=2$；$C=e_1^T$；$L_0=e_2^T$；
- $A e_1=e_2$、$A e_2=e_5$、$A e_3=e_3$、$A e_4=e_4$、$A e_5=e_1$；
- $\mathcal V=\ker[C;CA]=\operatorname{span}(e_2,e_3,e_4)$、$K_L=\ker[C;L_0]=\operatorname{span}(e_3,e_4,e_5)$、
  $Z=\operatorname{span}(e_3,e_4)$（$d=2$）。

于是：$S=\mathcal V\cap Z=Z$（$s=2$）、$t=1$、$q=2>t$；$A e_2=e_5\notin\mathcal V+Z$ ⟹ $\bar A$ 有落在 $\iota$ 像外的分量
（正是专家的抽象机制）。检查 $(A)$、$(S)$、功能可观测性。

用法：python proof/layer_program/c231_realize_abstract.py
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

N, P = 5, 1
C = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)]]
L0 = [[Fr(0), Fr(1), Fr(0), Fr(0), Fr(0)]]
A = [[Fr(0)] * N for _ in range(N)]
A[1][0] = Fr(1)   # A e1 = e2
A[4][1] = Fr(1)   # A e2 = e5
A[2][2] = Fr(1)   # A e3 = e3
A[3][3] = Fr(1)   # A e4 = e4
A[0][4] = Fr(1)   # A e5 = e1


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
    funcobs = AI.rank(n0rows + [L0[0]]) == n0
    print(f'CA = {[[str(x) for x in row] for row in CA]}')
    print(f'r1 = {r1}、dim V = {len(Vv)}、dim K_L = {len(KLv)}、n0 = {n0}、n0-p = {n0 - P}、'
          f'n-r1 = {N - r1}、功能可观测 = {funcobs}')
    # Z = span(e3,e4)
    Z = [[Fr(0), Fr(0)], [Fr(0), Fr(0)], [Fr(1), Fr(0)], [Fr(0), Fr(1)], [Fr(0), Fr(0)]]
    d = 2
    q = N - P - d
    CAZ = AI.mul(CA, Z)
    Rv = AI.nullspace(CAZ)
    R = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
    AZ = SG.apply_col(A, Z)
    AZR = AI.mul(AZ, R)
    M1 = [list(Z[i]) + list(AZR[i]) for i in range(N)]
    okA = AI.rank(M1) == d
    Vrows = [[Vv[k][i] for k in range(len(Vv))] for i in range(N)]
    both = [list(Vrows[i]) + list(Z[i]) for i in range(N)]
    s = len(Vv) + d - AI.rank(both)
    t = len(Vv) - s
    print(f'q = {q}、d = {d}、s = {s}、t = {t}、q>t = {q > t}')
    print(f'(A)：rank[Z,AZR] = {AI.rank(M1)}（d={d}）⟹ {okA}')
    # AZ ∉ Z（即 AV ⊄ V+Z 的体现）
    print(f'AZ ⊆ Z ? {AI.rank([list(Z[i]) + list(AZ[i]) for i in range(N)]) == d}')
    AVc = SG.apply_col(A, Vrows)
    rVZ = AI.rank([list(Vrows[i]) + list(Z[i]) for i in range(N)])
    rVZAV = AI.rank([list(Vrows[i]) + list(Z[i]) + list(AVc[i]) for i in range(N)])
    print(f'AV ⊆ V+Z ? {rVZAV == rVZ}（rank[V,Z]={rVZ}、rank[V,Z,AV]={rVZAV}）')
    g, h, _c = SG.spectral_gcd_Z(A, C, Z)
    print(f'(S)：h = {h}、gcd 次数 = {SG.pdeg(g)} ⟹ {"成立" if SG.pdeg(g) == 0 else "失败"}')


if __name__ == '__main__':
    main()
