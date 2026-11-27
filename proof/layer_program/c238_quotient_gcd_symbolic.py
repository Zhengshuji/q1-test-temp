r"""商铅笔 $T_\lambda=\lambda\iota-\bar A$（$t\times q$）上的**精确 gcd 判据**，与大铅笔对拍。

做法：对每个 $u\in\mathcal V/S$ 与 $\lambda\in\{0,1\}$ 解 $K_b c(\lambda)=\lambda u-Au$，
插值得到 $c(\lambda)=c(0)+\lambda(c(1)-c(0))$；$T(\lambda)$ 的第 $j$ 列 = $c(\lambda)$ 的 $w$-分量。
再算 $T$ 的 $t\times t$ 极大子式的 gcd。$(S)\iff$ gcd 次数 $=0$。

用法：python proof/layer_program/c238_quotient_gcd_symbolic.py
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


def cols(vecs, n):
    return [[vecs[k][i] for k in range(len(vecs))] for i in range(n)]


def extend(base, pool, target):
    cur = [list(v) for v in base]
    for v in pool:
        if len(cur) >= target:
            break
        if AI.rank(cols(cur + [v], len(v))) > len(cur):
            cur.append(list(v))
    return cur


def solve_in(Kb, x):
    n = len(x)
    Kbm = cols(Kb, n)
    aug = [list(Kbm[i]) + [x[i]] for i in range(n)]
    R, piv = AI.rref(aug)
    k = len(Kb)
    c = [Fr(0)] * k
    for row in R:
        pp = next((tt for tt in range(k + 1) if row[tt] != 0), None)
        if pp is None or pp == k:
            continue
        c[pp] = row[k]
    return c


def quotient_gcd(A, C, Z):
    """返回 (gcd 的多项式, t, q)。"""
    n, p = len(A), len(C)
    CA = AI.mul(C, A)
    Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
    V = [list(v) for v in Vv]
    d = len(Z[0])
    Zcols = [[Z[i][j] for i in range(n)] for j in range(d)]
    M = [[cols(V, n)[i][j] for j in range(len(V))] + [-cols(Zcols, n)[i][j] for j in range(d)]
         for i in range(n)]
    Nv = AI.nullspace(M)
    Svecs = []
    for coef in Nv:
        alpha = coef[:len(V)]
        Svecs.append([sum(alpha[j] * V[j][i] for j in range(len(V))) for i in range(n)])
    Sb = extend([], Svecs, AI.rank(cols(Svecs, n)) if Svecs else 0)
    s_dim = len(Sb)
    t = len(V) - s_dim
    q = n - p - d
    Vb = extend(Sb, V, len(V))
    Us = Vb[s_dim:]
    Kv = AI.nullspace([list(C[i]) for i in range(p)])
    Kb = extend(Zcols, [list(v) for v in Kv], n - p)
    w_part = Kb[d:]
    if t == 0:
        return [Fr(1)], t, q
    # T(λ) 的第 j 列：c(λ)[d:]；c(λ) = c0 + λ(c1 - c0)
    colsT = []
    for u in Us:
        Au = [sum(A[i][j] * u[j] for j in range(n)) for i in range(n)]
        c0 = solve_in(Kb, [-Au[i] for i in range(n)])
        c1 = solve_in(Kb, [u[i] - Au[i] for i in range(n)])
        colpolys = []
        for j in range(len(w_part)):
            colpolys.append([c0[d + j], c1[d + j] - c0[d + j]])   # 常数项、λ 系数
        colsT.append(colpolys)
    # T(λ) 是 q×t：T[i][j] = colsT[j][i]
    T = [[colsT[j][i] for j in range(t)] for i in range(q)]
    minors = []
    for rows in itertools.combinations(range(q), t):
        Mx = [[T[r][c] for c in range(t)] for r in rows]
        minors.append(SG.pdet(Mx))
    minors = [m for m in minors if m != [Fr(0)]]
    if not minors:
        return [Fr(0)], t, q
    g = minors[0]
    for m in minors[1:]:
        g = SG.pgcd(g, m)
        if SG.pdeg(g) == 0:
            break
    return g, t, q


def main():
    # R17 实例
    A = [[Fr(0)] * 8 for _ in range(8)]
    A[6][2] = Fr(1); A[7][3] = Fr(1); A[4][4] = Fr(1); A[5][5] = Fr(1)
    A[0][6] = Fr(1); A[1][7] = Fr(1); A[2][0] = Fr(1); A[3][1] = Fr(1)
    C = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)],
         [Fr(0), Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)]]
    L0 = [[Fr(0), Fr(0), Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)]]
    Z = [[Fr(0), Fr(0), Fr(0), Fr(0)],
         [Fr(0), Fr(0), Fr(0), Fr(0)],
         [Fr(0), Fr(0), Fr(0), Fr(0)],
         [Fr(1), Fr(0), Fr(0), Fr(0)],
         [Fr(0), Fr(1), Fr(0), Fr(0)],
         [Fr(0), Fr(0), Fr(1), Fr(0)],
         [Fr(0), Fr(0), Fr(0), Fr(0)],
         [Fr(0), Fr(0), Fr(0), Fr(1)]]
    g_big, h, _c = SG.spectral_gcd_Z(A, C, Z)
    g_q, t, q = quotient_gcd(A, C, Z)
    print(f'R17 的 Z：大铅笔 gcd 次数={SG.pdeg(g_big)}；商铅笔 t={t}、q={q}、gcd 次数={SG.pdeg(g_q)}')
    print('  ⟹ 两者一致 ✓' if (SG.pdeg(g_big) == 0) == (SG.pdeg(g_q) == 0) else '  ⟹ 不一致 ✗')
    # P2 例子
    A2 = [[Fr(x) for x in r] for r in
          [[0, 1, 0, 1, 0, 0, 0, 0], [0, -1, 1, 0, 0, 0, 0, -1], [1, 0, -1, 1, 0, 0, 1, -1],
           [-1, -1, 0, -2, 0, 0, 0, 0], [0, 0, 0, 0, -2, 0, 0, 1], [0, 0, 0, 0, 0, -2, 1, 0],
           [0, 0, 0, 0, 0, -1, -2, 1], [0, 0, 0, 0, 0, 0, 1, -2]]]
    C2 = [[Fr(x) for x in r] for r in [[-2, -2, 2, -2, -1, 0, 1, -3],
                                       [0, 0, 1, 2, 2, 3, -1, -2]]]
    L2 = [[Fr(x) for x in r] for r in [[-2, -1, -2, -3, -1, 3, 2, 0],
                                       [1, -1, -2, 1, 0, 2, 0, 1]]]
    KLv = AI.nullspace([[Fr(x) for x in row] for row in (C2 + L2)])
    KL = cols([list(v) for v in KLv], 8)
    W = [[Fr(1), Fr(0)], [Fr(0), Fr(1)], [Fr(0), Fr(0)], [Fr(0), Fr(0)]]
    Z2 = AI.mul(KL, W)
    g_big, h, _c = SG.spectral_gcd_Z(A2, C2, Z2)
    g_q, t, q = quotient_gcd(A2, C2, Z2)
    print(f'P2 例子 q=4 的一个 (A)-点：大铅笔 h={h}、gcd 次数={SG.pdeg(g_big)}；'
          f'商铅笔 t={t}、q={q}、gcd 次数={SG.pdeg(g_q)}')
    print('  ⟹ 两者一致 ✓' if (SG.pdeg(g_big) == 0) == (SG.pdeg(g_q) == 0) else '  ⟹ 不一致 ✗')


if __name__ == '__main__':
    main()
