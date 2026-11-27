r"""R17 可行点是否孤立？——在 $r=1$ 层内做扰动探针。

取 R17 的 $Z_0=\operatorname{span}(e_4-e_7-e_8,e_5,e_6)$，在 $K_L=\ker[C;L_0]$ 内加小扰动（$\mathbb Q$ 上精确），
保留 $\operatorname{rank}Z=d$、$\operatorname{rank}(CAZ)=1$、$(A)$，检查 $(S)$。

用法：python proof/layer_program/c247_r17_perturb.py
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

N, P = 8, 2
C = [[Fr(1) if k == 0 else Fr(0) for k in range(N)],
     [Fr(1) if k == 1 else Fr(0) for k in range(N)]]
A = [[Fr(0)] * N for _ in range(N)]
A[6][2] = Fr(1); A[7][3] = Fr(1); A[4][4] = Fr(1); A[5][5] = Fr(1)
A[0][6] = Fr(1); A[1][7] = Fr(1); A[2][0] = Fr(1); A[3][1] = Fr(1)
L0 = [[Fr(1) if k == 2 else Fr(0) for k in range(N)]]


def check(Z):
    d = len(Z[0])
    if AI.rank(Z) < d:
        return None
    CA = AI.mul(C, A)
    CAZ = AI.mul(CA, Z)
    r = AI.rank(CAZ)
    Rv = AI.nullspace(CAZ)
    Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
    AZ = SG.apply_col(A, Z)
    AZR = AI.mul(AZ, Rm)
    M1 = [list(Z[i]) + list(AZR[i]) for i in range(N)]
    okA = AI.rank(M1) == d
    g, h, _c = SG.spectral_gcd_Z(A, C, Z)
    okS = SG.pdeg(g) == 0
    return r, okA, okS


def main():
    rng = random.Random(11)
    # Z0 的列：e4-e7-e8、e5、e6
    Z0 = [[Fr(0), Fr(0), Fr(0)],
          [Fr(0), Fr(0), Fr(0)],
          [Fr(0), Fr(0), Fr(0)],
          [Fr(1), Fr(0), Fr(0)],
          [Fr(0), Fr(1), Fr(0)],
          [Fr(0), Fr(0), Fr(1)],
          [Fr(-1), Fr(0), Fr(0)],
          [Fr(-1), Fr(0), Fr(0)]]
    print('基准 Z0：', check(Z0))
    KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L0)])
    m_L = len(KLv)
    KL = [[KLv[k][i] for k in range(m_L)] for i in range(N)]
    # 在 K_L 坐标下把 Z0 表示为 5x3 的 W0（前 5 个 K_L 基向量？）
    # 用最小二乘：把 Z0 的列在 KL 基下展开
    def coords(x):
        aug = [list(KL[i]) + [x[i]] for i in range(N)]
        R, piv = AI.rref(aug)
        c = [Fr(0)] * m_L
        for row in R:
            pp = next((t for t in range(m_L + 1) if row[t] != 0), None)
            if pp is None or pp == m_L:
                continue
            c[pp] = row[m_L]
        return c
    W0 = [coords([Z0[i][j] for i in range(N)]) for j in range(3)]
    stats = {}
    found = 0
    for trial in range(60):
        W1 = []
        for j in range(3):
            v = [W0[j][k] + Fr(rng.randint(-2, 2)) * Fr(1, 7) for k in range(m_L)]
            v = [Fr(x) for x in v]
            W1.append(v)
        Z = AI.mul(KL, [[W1[j][k] for j in range(3)] for k in range(m_L)])
        res = check(Z)
        if res is None:
            continue
        r, okA, okS = res
        stats[(r, okA, okS)] = stats.get((r, okA, okS), 0) + 1
        if okA and okS:
            found += 1
    print('\n扰动统计 (r, (A), (S)) -> 个数：')
    for k in sorted(stats):
        print(f'  r={k[0]}, (A)={k[1]}, (S)={k[2]}: {stats[k]}')
    print(f'\n(A)∧(S) 的扰动点：{found} 个（若 >0 ⟹ R17 可行点不孤立）')


if __name__ == '__main__':
    main()
