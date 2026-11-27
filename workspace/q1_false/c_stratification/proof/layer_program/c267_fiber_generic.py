r"""纤维生成性实验（专家 QA16 §6）：固定 $S$，在同一条 algebraic-feasible 纤维里采样 $U$，
统计有多少满足 $(S)$。

R17 实例、$q=3$：$G=V\cap H=\operatorname{span}(e_4,e_5,e_6)$、$S=\operatorname{span}(e_5,e_6)$、$r=1$、$k=0$、
$B_S=G/S=\operatorname{span}(e_4)$；纤维 = $H/S$（$\dim 3$）中避开 $B_S$ 的**直线**（$\mathbb P^2$ 的开集）。

用法：python proof/layer_program/c267_fiber_generic.py
"""
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

N = 8
C = [[Fr(1) if k == 0 else Fr(0) for k in range(N)],
     [Fr(1) if k == 1 else Fr(0) for k in range(N)]]
A = [[Fr(0)] * N for _ in range(N)]
A[6][2] = Fr(1); A[7][3] = Fr(1); A[4][4] = Fr(1); A[5][5] = Fr(1)
A[0][6] = Fr(1); A[1][7] = Fr(1); A[2][0] = Fr(1); A[3][1] = Fr(1)
L0 = [[Fr(1) if k == 2 else Fr(0) for k in range(N)]]


def unit(i):
    return [Fr(1) if k == i else Fr(0) for k in range(N)]


def main():
    rng = random.Random(2026)
    # S = span(e5,e6)，Q = span(e3,e4)（S 在 V 中的补），t=2
    S = [unit(4), unit(5)]
    # H/S 的基取 e4, e7, e8（H = span(e4..e8)，S = span(e5,e6)）
    HS = [unit(3), unit(6), unit(7)]
    # B_S = span(e4) ⟹ 在 H/S 坐标里是 e1
    stats = {}
    for _ in range(200):
        w = [Fr(rng.randint(-3, 3)) for _ in range(3)]
        if w == [Fr(0), Fr(0), Fr(0)]:
            continue
        if w[1] == 0 and w[2] == 0:
            continue        # U = B_S，不可行（U∩B_S≠0）
        # U = span(Σ w_i (HS)_i)，Z = S ⊕ U
        u = [sum(w[i] * HS[i][k] for i in range(3)) for k in range(N)]
        Z = [[S[0][k], S[1][k], u[k]] for k in range(N)]
        if AI.rank(Z) < 3:
            continue
        CA = AI.mul(C, A)
        CAZ = AI.mul(CA, Z)
        Rv = AI.nullspace(CAZ)
        Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(3)]
        AZ = SG.apply_col(A, Z)
        AZR = AI.mul(AZ, Rm)
        M1 = [list(Z[i]) + list(AZR[i]) for i in range(N)]
        okA = AI.rank(M1) == 3
        g, h, _c = SG.spectral_gcd_Z(A, C, Z)
        okS = SG.pdeg(g) == 0
        stats[(okA, okS)] = stats.get((okA, okS), 0) + 1
    print('纤维采样统计 (A, S) -> 个数：')
    for k in sorted(stats):
        print(f'  (A)={k[0]}, (S)={k[1]}: {stats[k]}')
    totA = sum(v for k, v in stats.items() if k[0])
    totAS = sum(v for k, v in stats.items() if k[0] and k[1])
    print(f'\n(A)-可行 {totA} 个，其中 (S) 成立 {totAS} 个')


if __name__ == '__main__':
    main()
