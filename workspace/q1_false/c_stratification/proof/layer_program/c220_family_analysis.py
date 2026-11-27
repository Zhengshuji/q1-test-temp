r"""R14 族的系统枚举：在 $W=\operatorname{span}(e_2,e_3,e_4)$（$A$-不变）里，
对 **所有** $d$ 维子空间 $Z\subseteq W$ 检查 $(A)$ 与 $(S)$（不采样，小网格穷举）。

问：$(A)$ 成立是否恰好等价于 "$Z$ 是 $A$-不变的"？失败的 $(S)$ 是否恰好是这些？

实例：$n=5$、$p=1$、$C=e_1$、$L_0=e_5$；$A$ 有两种（3-循环 / 对角）。
$q=2 \Rightarrow d=2$；$q=3 \Rightarrow d=1$。

用法：python proof/layer_program/c220_family_analysis.py
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


def analyze(A, d, grid=(-1, 0, 1)):
    CA = AI.mul(C, A)
    KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L0)])
    m_L = len(KLv)
    KL = [[KLv[k][i] for k in range(m_L)] for i in range(N)]
    Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
    Vrows = [[Vv[k][i] for k in range(len(Vv))] for i in range(N)]
    stat = dict(total=0, A=0, S=0, A_and_S=0, A_and_inv=0, A_not_inv=0, inv=0)
    for cols in itertools.product(grid, repeat=m_L * d):
        W = [[Fr(cols[k * d + j]) for j in range(d)] for k in range(m_L)]
        Z = AI.mul(KL, W)
        if AI.rank(Z) < d:
            continue
        stat['total'] += 1
        # 是否 A-不变：A Z ⊆ im Z
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
        stat['A'] += okA
        stat['S'] += okS
        stat['inv'] += inv
        if okA and okS:
            stat['A_and_S'] += 1
        if okA and inv:
            stat['A_and_inv'] += 1
        if okA and not inv:
            stat['A_not_inv'] += 1
    return stat


def main():
    A1 = [[Fr(x) for x in row] for row in
          [[0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]]
    A2 = [[Fr(x) for x in row] for row in
          [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 2, 0, 0], [0, 0, 0, 3, 0], [0, 0, 0, 0, 0]]]
    for tag, A in [('3-循环', A1), ('对角', A2)]:
        for q, d in [(2, 2), (3, 1)]:
            st = analyze(A, d)
            print(f'{tag}，q={q}（d={d}）：总数 {st["total"]}；(A) {st["A"]}；(S) {st["S"]}；'
                  f'两者 {st["A_and_S"]}；A-不变 {st["inv"]}；(A)∧不变 {st["A_and_inv"]}；(A)∧非不变 {st["A_not_inv"]}')


if __name__ == '__main__':
    main()
