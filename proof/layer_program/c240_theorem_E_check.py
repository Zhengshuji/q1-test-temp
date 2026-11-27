r"""Theorem E 的实例验证：$\operatorname{im}\bar A\cap\operatorname{im}\iota=0$ ⟹ $(S)$ 成立；
$\operatorname{im}\bar A\subseteq\operatorname{im}\iota$ ⟹ $(S)$ 失败（Theorem C）。

对给定实例与 $Z$：在 $\ker C/Z$ 的基下计算
- $\iota$ 的矩阵：$\mathcal V$ 的补基 $u_j\mapsto u_j\bmod Z$；
- $\bar A$ 的矩阵：$u_j\mapsto Au_j\bmod Z$；
再比较与精确 $(S)$（商铅笔 gcd）。

用法：python proof/layer_program/c240_theorem_E_check.py
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
import importlib.util as iu

_spec = iu.spec_from_file_location('C238', os.path.join(_HERE, 'c238_quotient_gcd_symbolic.py'))
Q = iu.module_from_spec(_spec)
_spec.loader.exec_module(Q)


def classes(A, C, Z):
    """返回 (I 矩阵, Amat 矩阵, t, q)；列为 im ι 与 im Ā 的坐标（ker C/Z 的 w-基）。"""
    n, p = len(A), len(C)
    CA = AI.mul(C, A)
    Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
    V = [list(v) for v in Vv]
    d = len(Z[0])
    Zcols = [[Z[i][j] for i in range(n)] for j in range(d)]
    M = [[Q.cols(V, n)[i][j] for j in range(len(V))] + [-Q.cols(Zcols, n)[i][j] for j in range(d)]
         for i in range(n)]
    Nv = AI.nullspace(M)
    Svecs = []
    for coef in Nv:
        alpha = coef[:len(V)]
        Svecs.append([sum(alpha[j] * V[j][i] for j in range(len(V))) for i in range(n)])
    Sb = Q.extend([], Svecs, AI.rank(Q.cols(Svecs, n)) if Svecs else 0)
    s_dim = len(Sb)
    t = len(V) - s_dim
    q = n - p - d
    Vb = Q.extend(Sb, V, len(V))
    Us = Vb[s_dim:]
    Kv = AI.nullspace([list(C[i]) for i in range(p)])
    Kb = Q.extend(Zcols, [list(v) for v in Kv], n - p)
    w_part = Kb[d:]
    ImI, ImA = [], []
    for u in Us:
        c = Q.solve_in(Kb, list(u))
        ImI.append(c[d:])
        Au = [sum(A[i][j] * u[j] for j in range(n)) for i in range(n)]
        c2 = Q.solve_in(Kb, [-Au[i] for i in range(n)])
        ImA.append(c2[d:])
    # 转成 q×t
    I = [[ImI[j][i] for j in range(t)] for i in range(len(w_part))]
    Am = [[ImA[j][i] for j in range(t)] for i in range(len(w_part))]
    return I, Am, t, q


def verdict(A, C, Z):
    I, Am, t, q = classes(A, C, Z)
    rI = AI.rank(I)
    rA = AI.rank(Am)
    sub = AI.rank([list(I[i]) + list(Am[i]) for i in range(len(I))]) == rI
    inter0 = AI.rank([list(I[i]) + list(Am[i]) for i in range(len(I))]) == rI + rA
    g, tt, qq = Q.quotient_gcd(A, C, Z)
    okS = (SG.pdeg(g) == 0)
    return dict(t=t, q=q, rI=rI, rA=rA, subset=sub, inter0=inter0, S=okS)


def main():
    # c231 实例（专家抽象例子的实现）
    A1 = [[Fr(0)] * 5 for _ in range(5)]
    A1[1][0] = Fr(1); A1[4][1] = Fr(1); A1[2][2] = Fr(1); A1[3][3] = Fr(1); A1[0][4] = Fr(1)
    C1 = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)]]
    L1 = [[Fr(0), Fr(1), Fr(0), Fr(0), Fr(0)]]
    Z1 = [[Fr(0), Fr(0)], [Fr(0), Fr(0)], [Fr(1), Fr(0)], [Fr(0), Fr(1)], [Fr(0), Fr(0)]]
    print('c231：', verdict(A1, C1, Z1))

    # R17 实例（q=2 的构造点）
    A2 = [[Fr(0)] * 8 for _ in range(8)]
    A2[6][2] = Fr(1); A2[7][3] = Fr(1); A2[4][4] = Fr(1); A2[5][5] = Fr(1)
    A2[0][6] = Fr(1); A2[1][7] = Fr(1); A2[2][0] = Fr(1); A2[3][1] = Fr(1)
    C2 = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)],
          [Fr(0), Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)]]
    Z2 = [[Fr(0), Fr(0), Fr(0), Fr(0)],
          [Fr(0), Fr(0), Fr(0), Fr(0)],
          [Fr(0), Fr(0), Fr(0), Fr(0)],
          [Fr(1), Fr(0), Fr(0), Fr(0)],
          [Fr(0), Fr(1), Fr(0), Fr(0)],
          [Fr(0), Fr(0), Fr(1), Fr(0)],
          [Fr(0), Fr(0), Fr(0), Fr(0)],
          [Fr(0), Fr(0), Fr(0), Fr(1)]]
    print('R17（q=2）：', verdict(A2, C2, Z2))

    # Theorem C 情形的例子（Z ⊆ V 且 A-不变）：R15 族 q=1
    A3 = [[Fr(0)] * 5 for _ in range(5)]
    A3[1][0] = Fr(1); A3[3][1] = Fr(1); A3[1][2] = Fr(1); A3[2][3] = Fr(1); A3[0][4] = Fr(1)
    C3 = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)]]
    L3 = [[Fr(0), Fr(0), Fr(0), Fr(0), Fr(1)]]
    KLv = AI.nullspace([[Fr(x) for x in row] for row in (C3 + L3)])
    Z3 = Q.cols([list(v) for v in KLv], 5)
    print('R15 族 q=1（Z=V）：', verdict(A3, C3, Z3))


if __name__ == '__main__':
    main()
