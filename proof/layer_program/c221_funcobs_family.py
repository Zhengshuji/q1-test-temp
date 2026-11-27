r"""在**功能可观测**的实例上检验"唯一障碍"（互补）猜想。

构造：$n=5$、$p=1$、$C=e_1$、$L_0=e_5$；
$A$ 的列：$e_1\mapsto e_2$、$e_2\mapsto e_4$、$e_3\mapsto e_2$、$e_4\mapsto e_3$、$e_5\mapsto e_1$。
于是 $\mathcal O_C=[e_1;\,e_5;\,0;\dots]$ ⟹ $n_0=2$、$\operatorname{row}\mathcal O_C=\operatorname{span}(e_1,e_5)$、
$\operatorname{row}L_0=e_5\subseteq\operatorname{row}\mathcal O_C$ ⟹ **功能可观测** ✓；
$V=\ker[C;CA]=\ker[e_1;e_5]=\operatorname{span}(e_2,e_3,e_4)=W$（$\dim3$）；$\ker[C;L_0]=W$。
$W$ 是 $A$-不变的（$e_2\to e_4\to e_3\to e_2$）。

阶 $q$：$d=4-q$；$Z$ 取 $W$ 的所有 $d$ 维子空间（小网格穷举）。

用法：python proof/layer_program/c221_funcobs_family.py
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

N, P, R = 5, 1, 1
C = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)]]
L0 = [[Fr(0), Fr(0), Fr(0), Fr(0), Fr(1)]]
A = [[Fr(0)] * N for _ in range(N)]
A[1][0] = Fr(1)   # A e1 = e2
A[3][1] = Fr(1)   # A e2 = e4
A[1][2] = Fr(1)   # A e3 = e2
A[2][3] = Fr(1)   # A e4 = e3
A[0][4] = Fr(1)   # A e5 = e1


def main():
    CA = AI.mul(C, A)
    o, row = [], list(C[0])
    for _ in range(N):
        o.append(row)
        row = AI.mul([row], A)[0]
    n0 = AI.rank(o)
    func_obs = AI.rank(o + [L0[0]]) == n0
    KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L0)])
    m_L = len(KLv)
    KL = [[KLv[k][i] for k in range(m_L)] for i in range(N)]
    Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
    Vrows = [[Vv[k][i] for k in range(len(Vv))] for i in range(N)]
    print(f'n0={n0}、功能可观测={func_obs}、dim V={len(Vv)}、dim ker[C;L0]={m_L}')
    for q in (1, 2, 3, 4):
        d = 4 - q
        if d > m_L:
            continue
        tot = a_cnt = s_cnt = both = ainv = 0
        first_bad = None
        if d == m_L:
            cand = [tuple(1 if k == j else 0 for k in range(m_L) for j in range(d))]
        else:
            cand = list(itertools.product((-1, 0, 1), repeat=m_L * d))
        for cols in cand:
            Wm = [[Fr(cols[k * d + j]) for j in range(d)] for k in range(m_L)]
            Z = AI.mul(KL, Wm)
            if AI.rank(Z) < d:
                continue
            tot += 1
            AZ = AI.mul(A, Z)
            inv = AI.rank([list(Z[i]) + list(AZ[i]) for i in range(N)]) == d
            CAZ = AI.mul(CA, Z)
            Rv = AI.nullspace(CAZ)
            Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
            AZR = AI.mul(AZ, Rm)
            M1 = [list(Z[i]) + list(AZR[i]) for i in range(N)]
            okA = AI.rank(M1) == d
            g, h, _ = SG.spectral_gcd_Z(A, C, Z)
            okS = SG.pdeg(g) == 0
            a_cnt += okA
            s_cnt += okS
            both += okA and okS
            ainv += okA and inv
            if okA and not okS and first_bad is None:
                first_bad = (h, len(Vv) + d, inv)
        print(f'q={q}（d={d}）：枚举 {tot}；(A) {a_cnt}；(S) {s_cnt}；(A)∧(S) {both}；(A)∧不变 {ainv}'
              + (f'；首个 (A)∧¬(S)：h={first_bad[0]}、N_c={first_bad[1]}、A-不变={first_bad[2]}' if first_bad else ''))


if __name__ == '__main__':
    main()

