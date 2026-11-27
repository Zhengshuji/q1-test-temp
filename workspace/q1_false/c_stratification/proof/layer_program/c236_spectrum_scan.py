r"""R17 实例上的阶谱扫描：记录每个 $(q,Z)$ 的 $(A)/(S)$、$r=\operatorname{rank}(CAZ)$、$s$、$t$、
是否 $Z\subseteq\mathcal V$，寻找"可行"的模式。

实例（R17）：$n=8$、$p=2$、$r=1$、$C=[e_1;e_2]$，
$A: e_1\to e_3,e_2\to e_4,e_3\to e_7,e_4\to e_8,e_5\to e_5,e_6\to e_6,e_7\to e_1,e_8\to e_2$，$L_0=e_3$。
$n_0=6$（$n_0-p=4$）、$r_1=4$、$\mathcal V=\operatorname{span}(e_3,e_4,e_5,e_6)$、$m_L=n-p-r=5$。

用法：python proof/layer_program/c236_spectrum_scan.py [--samples 120]
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

N, P, R = 8, 2, 1
C = [[Fr(1) if k == 0 else Fr(0) for k in range(N)],
     [Fr(1) if k == 1 else Fr(0) for k in range(N)]]
A = [[Fr(0)] * N for _ in range(N)]
A[6][2] = Fr(1)
A[7][3] = Fr(1)
A[4][4] = Fr(1)
A[5][5] = Fr(1)
A[0][6] = Fr(1)
A[1][7] = Fr(1)
A[2][0] = Fr(1)
A[3][1] = Fr(1)
L0 = [[Fr(1) if k == 2 else Fr(0) for k in range(N)]]


def main():
    samples = 120
    if '--samples' in sys.argv:
        samples = int(sys.argv[sys.argv.index('--samples') + 1])
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
    print(f'n0={n0}、n0-p={n0 - P}、dim V={len(Vv)}、m_L={m_L}')
    rng = random.Random(7)
    for q in (1, 2, 3, 4):
        d = N - P - q
        if d < 0 or d > m_L:
            continue
        stats = Counter()
        rows = []
        for _ in range(samples):
            I = tuple(sorted(rng.sample(range(m_L), d))) if d else ()
            th = [[Fr(rng.randint(-3, 3)) for _ in range(d)] for _ in range(m_L - d)] if d else []
            W = [[Fr(0)] * d for _ in range(m_L)]
            Iset = set(I)
            for a, ri in enumerate(I):
                W[ri][a] = Fr(1)
            free = [x for x in range(m_L) if x not in Iset]
            for a, ri in enumerate(free):
                for b in range(d):
                    W[ri][b] = th[a][b]
            Z = AI.mul(KL, W) if d else [[Fr(0)] for _ in range(N)]
            if d and AI.rank(Z) < d:
                continue
            CAZ = AI.mul(CA, Z) if d else [[Fr(0)]]
            Rv = AI.nullspace(CAZ) if d else []
            Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
            AZ = SG.apply_col(A, Z) if d else [[Fr(0)] for _ in range(N)]
            AZR = AI.mul(AZ, Rm) if d else [[] for _ in range(N)]
            M1 = [list(Z[i]) + list(AZR[i]) for i in range(N)]
            okA = (AI.rank(M1) == d) if d else True
            g, h, _c = SG.spectral_gcd_Z(A, C, Z) if d else (None, 0, 0)
            okS = (SG.pdeg(g) == 0) if d else True
            both = [list(Vc[i]) + list(Z[i]) for i in range(N)]
            s = len(Vv) + d - AI.rank(both)
            ZinV = (AI.rank(both) == len(Vv))
            r = AI.rank(CAZ) if d else 0
            key = (okA, okS, ZinV)
            stats[key] += 1
            if okA and okS:
                rows.append((d, r, s, len(Vv) - s, ZinV))
        print(f'\nq={q}（d={d}）：(A, S, Z⊆V) 统计 {dict(stats)}')
        if rows:
            print(f'  可行点 {len(rows)} 个；前几个 (d, r, s, t, Z⊆V)：{rows[:5]}')
        else:
            print('  可行点 0 个')


if __name__ == '__main__':
    main()
