r"""Stage 2 小规模实验：取 $L_0=CA$（于是 $Z=\ker[C;CA]=\mathcal V$，$Z\subseteq\mathcal V$ 必然成立），
扫图卡参数 $\Theta$，记录 $(A)$/$(S)$ 的分布，看"坏集"是否由低次多项式刻画。

实例：$n=5$、$p=1$、$C=e_1$、$A$ 随机（固定种子）、$L_0=CA$、$q=2$（$d=2$、$m_L=3$）。

用法：python proof/layer_program/c223_stage2_probe.py
"""
import itertools
import os
import random
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


def build(seed=5):
    rng = random.Random(seed)
    A = [[Fr(rng.randint(-2, 2)) for _ in range(N)] for _ in range(N)]
    CA = AI.mul(C, A)
    return A, CA


def main():
    A, L0 = build()
    q, d = 2, 2
    CA = AI.mul(C, A)
    r1 = AI.rank(AI.vstack([C, CA]))
    Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
    KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L0)])
    m_L = len(KLv)
    print(f'rank[C;CA]={r1}、dim V={len(Vv)}、dim ker[C;L0]={m_L}、d={d}')
    print(f'Z⊆V（由 L0=CA 保证）：{AI.rank([list([[KLv[k][i] for k in range(m_L)] for i in range(N)][i]) + list([[Vv[k][i] for k in range(len(Vv))] for i in range(N)][i]) for i in range(N)]) == len(Vv)}')
    KL = [[KLv[k][i] for k in range(m_L)] for i in range(N)]
    Vrows = [[Vv[k][i] for k in range(len(Vv))] for i in range(N)]
    grid = [Fr(x) for x in (-2, -1, 0, 1, 2)]
    print(f'{"chart":>8s} {"Θ":>14s} {"(A)":>4s} {"(S)":>4s} {"h":>3s} {"gdeg":>4s}')
    bad = []
    for I in itertools.combinations(range(m_L), d):
        for t in itertools.product(grid, repeat=(m_L - d) * d):
            theta = [list(t[k * d:(k + 1) * d]) for k in range(m_L - d)]
            W = [[Fr(0)] * d for _ in range(m_L)]
            Iset = set(I)
            for a, ri in enumerate(I):
                W[ri][a] = Fr(1)
            free = [x for x in range(m_L) if x not in Iset]
            for a, ri in enumerate(free):
                for b in range(d):
                    W[ri][b] = theta[a][b]
            Z = AI.mul(KL, W)
            if AI.rank(Z) < d:
                continue
            CAZ = AI.mul(CA, Z)
            Rv = AI.nullspace(CAZ)
            Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
            AZR = AI.mul(AI.mul(A, Z), Rm)
            M1 = [list(Z[i]) + list(AZR[i]) for i in range(N)]
            okA = AI.rank(M1) == d
            g, h, _ = SG.spectral_gcd_Z(A, C, Z)
            okS = SG.pdeg(g) == 0
            print(f'{str(I):>8s} {str(tuple(str(x) for x in t)):>14s} {str(okA):>4s} {str(okS):>4s} {h:3d} {SG.pdeg(g):4d}')
            if okA and not okS:
                bad.append((I, t, h))
    print(f'\n(A)-可行且 (S) 失败的坏点：{len(bad)} 个')


if __name__ == '__main__':
    main()
