"""avoid_control.py —— J5 对照实验：把 $V,K$ 换成**随机子空间**，看谱失败率如何变化

**问题（J1 的可检验形式）**：整族/逐候选的谱失败，是"$V=\\ker[C;CA]$、$K=\\ker[C;L_0]$ 这两条**结构约束**"
造成的，还是铅笔结构本身就会给出高失败率？

**做法**：固定同一个 $A$、同样的维数 $(d_V=d_K=\\dim V,\\ d)$，比较两组样本的失败率：

* **结构组**：$V=\\ker[C;CA]$、$K=\\ker[C;L_0]$（$C,L_0$ 随机，$A$ 固定）；
* **随机组**：$V,K$ 取**随机子空间**（与 $A,C,L_0$ 无关），维数相同。

对每个随机 $\\mathcal Z\\subseteq K$（$\\dim d$、且 $s=\\dim(V\\cap\\mathcal Z)=0$）用 **B.16(b)** 的精确判据：
失败 $\\iff$ 极大子式 $\\gcd$ 有正次数（$M(\\lambda)=P_{\\mathcal Z}(\\lambda I-A)B_V$）。

用法：python -u tools/verification/avoid_control.py
"""

import os
import sys
import itertools
import random
from fractions import Fraction
from collections import Counter, defaultdict

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import sympy as sp                        # noqa: E402
import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402

F = Fraction
lam = sp.symbols('lam')


def rand_subspace(n, d, rng):
    """随机 d 维子空间（n×d，列满秩）。"""
    while True:
        M = [[F(rng.randrange(-3, 4)) for _ in range(d)] for _ in range(n)]
        if d == 0 or ZG.bool_rank(ZG.cols_to_rows(M)) == d:
            return M


def rand_in_span(K, d, rng):
    """在 span(K) 里随机取 d 维子空间。"""
    n = len(K)
    dK = len(K[0]) if (K and K[0]) else 0
    while True:
        coef = [[F(rng.randrange(-3, 4)) for _ in range(d)] for _ in range(dK)]
        M = [[sum(K[i][t] * coef[t][j] for t in range(dK)) for j in range(d)] for i in range(n)]
        if d == 0 or ZG.bool_rank(ZG.cols_to_rows(M)) == d:
            return M


def fails(M_pencil, dV):
    """B.16(b)：极大子式 gcd 有正次数 ⟹ 失败。"""
    rows = M_pencil.rows
    mins = []
    for rs in itertools.combinations(range(rows), dV):
        m = sp.expand(M_pencil[list(rs), :].det())
        if m != 0:
            mins.append(sp.Poly(m, lam))
    if not mins:
        return None                  # 全部恒零：退化，跳过
    g = mins[0]
    for mm in mins[1:]:
        g = sp.gcd(g, mm)
    return sp.degree(g.as_expr(), lam) > 0


def pencil(A, V, Z):
    """M(λ) = P_Z (A − λI) B_V，P_Z 满行秩、ker P_Z = Z。"""
    n = len(A)
    dV = len(V[0]) if (V and V[0]) else 0
    d = len(Z[0]) if (Z and Z[0]) else 0
    if dV == 0:
        return None
    Zt = [[Z[i][k] for i in range(n)] for k in range(d)] if d else []
    ns = ZG.ker_cols(Zt) if d else [[F(1) if i == j else F(0) for i in range(n)] for j in range(n)]
    dP = len(ns[0]) if (ns and ns[0]) else 0
    P = [[ns[i][j] for i in range(n)] for j in range(dP)]
    As = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in A])
    Ps = sp.Matrix([[sp.Rational(F(x).numerator, F(x).denominator) for x in row] for row in P])
    Bs = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in V])
    return sp.expand(Ps * (As - lam * sp.eye(n)) * Bs)


def main():
    rng = random.Random(20261104)
    st = Counter()
    for trial in range(120):
        n = rng.choice([6, 7])
        p = rng.choice([1, 2])
        r = rng.choice([1, 2])
        if p + r >= n:
            continue
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(p)]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(r)]
        if LQ.rank(C) != p or LQ.rank(L0) != r:
            continue
        if LQ.rank(QR.observability_matrix(A, C)) != n:
            continue
        if LQ.rank(QR.observability_matrix(A, L0)) != n:
            continue
        CA = LQ.mul(C, A)
        Vs = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
        Ks = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (Vs and Vs[0] and Ks and Ks[0]):
            continue
        dV = len(Vs[0]); dK = len(Ks[0])
        # 随机组：同维数的随机子空间
        Vr = rand_subspace(n, dV, rng)
        Kr = rand_subspace(n, dK, rng)
        for q in range(1, n - p):
            d = n - p - q
            if d <= 0 or d > dK:
                continue
            for group, V, K in (('structured', Vs, Ks), ('random', Vr, Kr)):
                for _ in range(3):
                    if d == 0:
                        Z = [[] for _ in range(n)]
                    else:
                        Z = rand_in_span(K, d, rng)
                    # s = dim(V∩Z)
                    VZ = [[V[i][k] for k in range(dV)] + [Z[i][j] for j in range(d)] for i in range(n)]
                    rk = LQ.rank([[VZ[i][j] for i in range(n)] for j in range(dV + d)])
                    s = dV + d - rk
                    if s != 0:
                        st[f'{group}:s>0 跳过'] += 1
                        continue
                    Mp = pencil(A, V, Z)
                    if Mp is None:
                        continue
                    res = fails(Mp, dV)
                    if res is None:
                        st[f'{group}:退化'] += 1
                        continue
                    st[f'{group}:samples'] += 1
                    st[f'{group}:fails' if res else f'{group}:feasible'] += 1
    print('统计：')
    for k in sorted(st):
        print(f'  {k}: {st[k]}')
    for group in ('structured', 'random'):
        tot = st[f'{group}:samples']
        fl = st[f'{group}:fails']
        if tot:
            print(f'\n{group}：失败率 {fl}/{tot} = {fl/tot:.1%}')


if __name__ == '__main__':
    main()
