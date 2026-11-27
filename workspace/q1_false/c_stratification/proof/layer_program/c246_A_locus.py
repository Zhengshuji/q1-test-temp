r"""$(A)$-轨迹的分层探针：R17 实例、$q=3$（$d=3$）。

按 $r=\operatorname{rank}(CAZ)\in\{0,1,2\}$ 分层，记录每层的 $(A)$ 点数与其中 $(S)$ 成立的点数，
并记录 $Z\subseteq\mathcal V$ 与否。

用法：python proof/layer_program/c246_A_locus.py
"""
import os
import random
import sys
from collections import Counter
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import spectral_gcd as SG

N, P = 8, 2
C = [[Fr(1) if k == 0 else Fr(0) for k in range(N)],
     [Fr(1) if k == 1 else Fr(0) for k in range(N)]]
A = [[Fr(0)] * N for _ in range(N)]
A[6][2] = Fr(1); A[7][3] = Fr(1); A[4][4] = Fr(1); A[5][5] = Fr(1)
A[0][6] = Fr(1); A[1][7] = Fr(1); A[2][0] = Fr(1); A[3][1] = Fr(1)
L0 = [[Fr(1) if k == 2 else Fr(0) for k in range(N)]]


def main():
    rng = random.Random(3)
    CA = AI.mul(C, A)
    Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
    Vc = [[Vv[k][i] for k in range(len(Vv))] for i in range(N)]
    KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L0)])
    m_L = len(KLv)
    KL = [[KLv[k][i] for k in range(m_L)] for i in range(N)]
    n0rows, cur = [], [list(x) for x in C]
    for _k in range(N):
        n0rows.extend(cur)
        cur = [AI.mul([x], A)[0] for x in cur]
    n0 = AI.rank(n0rows)
    q, d = 3, N - P - 3
    print(f'n0={n0}、n0-p={n0 - P}、dim V={len(Vv)}、m_L={m_L}、q={q}、d={d}')
    stats = Counter()
    rstats = Counter()
    for _ in range(400):
        I = tuple(sorted(rng.sample(range(m_L), d)))
        th = [[Fr(rng.randint(-3, 3)) for _ in range(d)] for _ in range(m_L - d)]
        W = [[Fr(0)] * d for _ in range(m_L)]
        Iset = set(I)
        for a, ri in enumerate(I):
            W[ri][a] = Fr(1)
        free = [x for x in range(m_L) if x not in Iset]
        for a, ri in enumerate(free):
            for b in range(d):
                W[ri][b] = th[a][b]
        Z = AI.mul(KL, W)
        if AI.rank(Z) < d:
            continue
        r = AI.rank(AI.mul(CA, Z))
        CAZ = AI.mul(CA, Z)
        Rv = AI.nullspace(CAZ)
        Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
        AZ = SG.apply_col(A, Z)
        AZR = AI.mul(AZ, Rm)
        M1 = [list(Z[i]) + list(AZR[i]) for i in range(N)]
        okA = AI.rank(M1) == d
        rstats[(r, okA)] += 1
        if not okA:
            continue
        g, h, _c = SG.spectral_gcd_Z(A, C, Z)
        okS = SG.pdeg(g) == 0
        both = [list(Vc[i]) + list(Z[i]) for i in range(N)]
        ZinV = (AI.rank(both) == len(Vv))
        stats[(r, okS, ZinV)] += 1
    print('\n按 r 的 (A) 统计（点数, 是否 (A)）：')
    for k in sorted(rstats):
        print(f'  r={k[0]}, (A)={k[1]}: {rstats[k]}')
    print('\n(A)-点上按 (r, (S), Z⊆V) 的统计：')
    for k in sorted(stats):
        print(f'  r={k[0]}, (S)={k[1]}, Z⊆V={k[2]}: {stats[k]}')


if __name__ == '__main__':
    main()
