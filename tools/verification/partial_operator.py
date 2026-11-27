"""partial_operator.py —— 核验专家的"偏算子"判据（B.24'）与 Direction A 的诊断

**B.24'**：$W=\\mathcal LV\\subseteq\\mathbb C^q$，$\\Phi(\\mathcal Lx)=\\mathcal LAx$。则
$(5b)$ 失败 $\\iff\\exists0\\ne u\\in W:\\Phi(u)\\in\\operatorname{span}\\{u\\}$ $\\iff$ 矩形铅笔 $D-\\lambda U$ 的极大子式有公根（$U$ 为 $W$ 的基、
$D$ 为 $\\Phi$ 作用在 $U$ 各列上的像）。

**Direction A（专家的诊断性猜想）**：是否**每个**可容许候选都有非零的 $\\Phi$-不变子空间 $W_0\\subseteq W$？
最简版本：是否 $\\Phi(W)\\subseteq W$？若是，则 $\\Phi|_W$ 是普通自同态 ⟹ 必有特征向量 ⟹ 必失败。

用法：python -u tools/verification/partial_operator.py
"""

import os
import sys
import itertools
import random
from fractions import Fraction
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import sympy as sp                        # noqa: E402
import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import decide_symbolic as DS              # noqa: E402
import observability_test as OT           # noqa: E402

F = Fraction
lam = sp.symbols('lam')


def basis_of_columns(M, n):
    """n×m 矩阵的列空间基（n×k）。"""
    m = len(M[0]) if (M and M[0]) else 0
    keep = []
    for j in range(m):
        cand = keep + [j]
        sub = [[M[i][t] for t in cand] for i in range(n)]
        if ZG.bool_rank(ZG.cols_to_rows(sub)) == len(cand):
            keep = cand
    return [[M[i][j] for j in keep] for i in range(n)], len(keep)


def gcd_degree_of_pencil(U, D, q):
    """矩形铅笔 D − λU（q×k）的 k 阶极大子式 gcd 的次数（None=全零）。"""
    k = len(U[0]) if (U and U[0]) else 0
    if k == 0:
        return None
    Us = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in U])
    Ds = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in D])
    P = Ds - lam * Us
    mins = []
    for rs in itertools.combinations(range(q), k):
        m = sp.expand(P[list(rs), :].det())
        if m != 0:
            mins.append(sp.Poly(m, lam))
    if not mins:
        return None
    g = mins[0]
    for mm in mins[1:]:
        g = sp.gcd(g, mm)
    return sp.degree(g.as_expr(), lam)


def main():
    rng = random.Random(20261116)
    st = Counter()
    for trial in range(2500):
        n = rng.choice([5, 6])
        p = rng.choice([1, 2])
        r = rng.choice([1, 2])
        if p + r >= n:
            continue
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(p)]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(r)]
        if LQ.rank(C) != p or LQ.rank(L0) != r:
            continue
        if LQ.rank([list(x) for x in C] + L0) != p + r:
            continue
        O = QR.observability_matrix(A, C)
        n0 = LQ.rank(O)
        if n0 != n or LQ.rank(O + [list(x) for x in L0]) != n:
            continue
        CA = LQ.mul(C, A)
        V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
        if not (V and V[0]):
            continue
        dV = len(V[0])
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (K and K[0]):
            continue
        k = len(K[0])
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        for q in range(q0, n0 - p + 1):
            d = n - p - q
            if d <= 0 or d > k:
                continue
            for rows in itertools.combinations(range(k), d):
                Z = DS.Z_from_theta(A, C, L0, q, rows, [F(0)] * (d * (k - d)))
                if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                    continue
                try:
                    L = ZG.L_from_Z(A, C, L0, Z, q)
                except AssertionError:
                    continue
                if L is None or not LQ.condA(A, C, L):
                    continue
                st['可容许样本'] += 1
                # W = L·V
                LV = [[sum(L[i][t] * V[t][j] for t in range(n)) for j in range(dV)] for i in range(q)]
                U, kW = basis_of_columns(LV, q)
                if kW == 0:
                    st['W=0（d=0 情形）'] += 1
                    continue
                # D：Φ 作用在 U 的列上 —— 需要把 U 的列表达成 L·v 的形式
                # 直接用 L A · V，再取与 U 相同的列组合：因为 U 的列是 LV 的列的子集组合
                LA = LQ.mul(L, A)
                LAV = [[sum(LA[i][t] * V[t][j] for t in range(n)) for j in range(dV)] for i in range(q)]
                # 找 U = LV 的列空间基在原列下的组合：用解方程得系数
                # 简化：取 D 的列为 Φ(u)，其中 u = U 的列（用最小二乘解系数）
                Us = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in U])
                LVs = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in LV])
                LAVs = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in LAV])
                # 解 LV c = u_i（最小二乘不适用；用 sympy 的 linsolve）
                Dcols = []
                ok = True
                for i in range(kW):
                    u = Us[:, i]
                    sol = sp.linsolve((LVs, u))
                    if sol == sp.EmptySet:
                        ok = False
                        break
                    cs = list(sol)[0]
                    dvec = LAVs * sp.Matrix(cs)
                    Dcols.append([dv for dv in dvec])
                if not ok:
                    st['D 构造失败'] += 1
                    continue
                D = [[Dcols[j][i] for j in range(kW)] for i in range(q)]
                st['D 构造成功'] += 1
                # Direction A：Φ(W) ⊆ W ?
                DW = [[D[i][j] for j in range(kW)] for i in range(q)]
                stack = [[D[i][j] for j in range(kW)] + [U[i][j2] for j2 in range(kW)] for i in range(q)]
                if LQ.rank(stack) == kW:
                    st['Φ(W) ⊆ W（方向 A 成立，必失败）'] += 1
                else:
                    st['Φ(W) ⊄ W'] += 1
                # B.24' 判据：gcd(D − λU) 有正次数？
                deg = gcd_degree_of_pencil(U, D, q)
                okb, why = OT.observability_ok(A, C, L)
                fails = not okb if okb is not None else None
                if deg is None:
                    st['gcd 全零'] += 1
                    pred = True
                else:
                    pred = (deg > 0)
                if fails is not None:
                    st['判据一致'] += 1 if pred == fails else 0
                    if pred != fails:
                        st['判据不一致'] += 1
                break
    print('统计：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')


if __name__ == '__main__':
    main()
