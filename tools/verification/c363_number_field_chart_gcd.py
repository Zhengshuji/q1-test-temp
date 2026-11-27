#!/usr/bin/env python3
"""c363 — 数域上的图卡 gcd（把无理特征值接进图卡判定）。

与 c361 相同的图卡，但所有向量/矩阵元素都在 K = Q[mu]/(f) 上：
  - 特征向量 c（K 上）、v = N c、D_v = K0 ∩ U_v^perp（K 上零空间）；
  - 补基、图卡行（X 为符号）→ 行空间的每个条目是 "K 系数的 X-多项式"；
  - H = L N、H_A = L A N；
  - 铅笔子式（λ-多项式，系数是 K 上的 X-多项式）→ K(X)[λ] 上的 gcd。
"""

from __future__ import annotations

import itertools
import os
import sys
from fractions import Fraction as F

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import c335_lambda_movement as m  # noqa: E402
import c354_generic_gcd_nf as g  # noqa: E402
import c355_rf_gcd as rf  # noqa: E402
from nf import NF, mat_nullspace  # noqa: E402


def kek(Fq, c):
    """整数/有理 -> 域元素。"""
    return Fq.elt(F(c))


def vecK(Fq, mat, vec, n):
    """K 上：y = mat · vec（mat 为整数矩阵的行列表，vec 是 K 向量）。"""
    out = []
    for i in range(n):
        acc = Fq.zero()
        for j, w in enumerate(vec):
            if mat[i][j] != 0:
                acc = Fq.add(acc, Fq.mul(kek(Fq, mat[i][j]), w))
        out.append(acc)
    return out


def rankK(Fq, rows):
    return g.rank_rows(Fq, rows)


def completion(Fq, all_rows, sub_rows):
    """在 all_rows 张成的空间里，给出模 sub_rows 的补基（K 上）。"""
    chosen = list(sub_rows)
    out = []
    for w in all_rows:
        if rankK(Fq, chosen + [w]) > len(chosen):
            chosen.append(w)
            out.append(w)
    return out


def minors_nf(A, N, Lrows, Fq, nvars):
    """Lrows: 每个元素是"K 系数的 X-多项式"（dict）；返回 lambda-多项式列表（系数是 dict）。"""
    n = A.rows
    k = N.cols
    om = k - 1
    Amat = [[int(A[i, j]) for j in range(n)] for i in range(n)]
    Nmat = [[int(N[i, j]) for j in range(k)] for i in range(n)]
    ANmat = [[sum(Amat[i][t] * Nmat[t][j] for t in range(n)) for j in range(k)] for i in range(n)]

    def rowdot(r, Mat, ncols, nrows):
        outr = []
        for j in range(ncols):
            acc = {}
            for i in range(nrows):
                if Mat[i][j] != 0:
                    acc = g.p_add(Fq, acc, g.p_scalar_mul(Fq, r[i], kek(Fq, Mat[i][j])))
            outr.append(acc)
        return outr

    H = [rowdot(r, Nmat, k, n) for r in Lrows]
    HA = [rowdot(r, ANmat, k, n) for r in Lrows]
    polys = []
    for rs in itertools.combinations(range(len(Lrows)), om):
        for cs in itertools.combinations(range(k), om):
            total = []
            for perm in itertools.permutations(range(om)):
                sign = 1
                pl = list(perm)
                for a in range(om):
                    for b in range(a + 1, om):
                        if pl[a] > pl[b]:
                            sign = -sign
                prod = [g.p_const(Fq, Fq.one())]
                for t in range(om):
                    i = rs[t]
                    j = cs[perm[t]]
                    entry = [g.p_neg(Fq, HA[i][j]), H[i][j]]
                    new = [{} for _ in range(len(prod) + 1)]
                    for a, ca in enumerate(prod):
                        for b, cb in enumerate(entry):
                            new[a + b] = g.p_add(Fq, new[a + b], g.p_mul(Fq, ca, cb))
                    prod = new
                if sign < 0:
                    prod = [g.p_neg(Fq, z) for z in prod]
                if not total:
                    total = prod
                else:
                    if len(total) < len(prod):
                        total = total + [{} for _ in range(len(prod) - len(total))]
                    for a, c in enumerate(prod):
                        total[a] = g.p_add(Fq, total[a], c)
            if total and any(not g.p_is_zero(c) for c in total):
                polys.append(total)
    return polys


def decide_nf(A, C, L0, q, verbose=True):
    n = A.rows
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    k = N.cols
    om = k - 1
    G = N.T * N
    M = G.inv() * (N.T * A * N)
    r0 = L0.rows if L0 is not None else 0
    Nmat = [[int(N[i, j]) for j in range(k)] for i in range(n)]
    Amat = [[int(A[i, j]) for j in range(n)] for i in range(n)]
    x = sp.symbols("x")
    cp = sp.Poly(M.charpoly(x).as_expr(), x)
    res = []
    for f, mult in sp.factor_list(cp.as_expr())[1]:
        fp = sp.Poly(f, x)
        deg = fp.degree()
        coeffs = [int(fp.coeff_monomial(x**i)) for i in range(deg)] + [1]
        Fq = NF(coeffs)
        rf.Fq_one = (Fq,)
        mu = Fq.elt(F(-int(fp.coeff_monomial(1)))) if deg == 1 else Fq.elt(*([0] + [1] + [0] * (deg - 2)))
        Mf = []
        for i in range(k):
            row = []
            for j in range(k):
                r = sp.Rational(M[i, j])
                row.append(Fq.elt(F(r.p, r.q)))
            Mf.append(row)
        rows = [[Fq.sub(Mf[i][j], mu) if i == j else Mf[i][j] for j in range(k)] for i in range(k)]
        ns = mat_nullspace(Fq, rows)
        for cdir in ns:
            v = vecK(Fq, Nmat, cdir, n)
            Av = vecK(Fq, Amat, v, n)
            if rankK(Fq, [v, Av]) < 1:
                continue
            if r0:
                ok = True
                for i in range(r0):
                    row = [int(L0[i, j]) for j in range(n)]
                    s1 = Fq.zero()
                    s2 = Fq.zero()
                    for j in range(n):
                        if row[j] != 0:
                            s1 = Fq.add(s1, Fq.mul(kek(Fq, row[j]), v[j]))
                            s2 = Fq.add(s2, Fq.mul(kek(Fq, row[j]), Av[j]))
                    if not (Fq.is_zero(s1) and Fq.is_zero(s2)):
                        ok = False
                        break
                if not ok:
                    continue
            # D_v（K 坐标）
            fv = []
            fa = []
            for j in range(k):
                s1 = Fq.zero()
                s2 = Fq.zero()
                for i in range(n):
                    if Nmat[i][j] != 0:
                        s1 = Fq.add(s1, Fq.mul(kek(Fq, Nmat[i][j]), v[i]))
                        s2 = Fq.add(s2, Fq.mul(kek(Fq, Nmat[i][j]), Av[i]))
                fv.append(s1)
                fa.append(s2)
            DvK = mat_nullspace(Fq, [fv, fa])
            if len(DvK) != om:
                continue
            Dv = [vecK(Fq, Nmat, col, n) for col in DvK]
            # U^perp（K 上）
            U = [v, Av]
            Qall = mat_nullspace(Fq, U)
            V0 = [ [kek(Fq, int(L0[i, j])) for j in range(n)] for i in range(r0)] if r0 else []
            V0red = completion(Fq, V0, Dv) if V0 else []
            base = Dv + V0red
            comp = completion(Fq, Qall, base)
            mfree = q - len(base)
            R = len(comp)
            if mfree < 0 or mfree > R:
                continue
            g.NV = mfree * (R - mfree)
            def const_poly(vec):
                return [{(0,) * g.NV: e} for e in vec]
            Lrows = [const_poly(w) for w in base]
            if mfree > 0:
                for i in range(mfree):
                    row = []
                    for t in range(n):
                        acc = {(0,) * g.NV: comp[i][t]}
                        for j in range(R - mfree):
                            e = [0] * g.NV
                            e[i * (R - mfree) + j] = 1
                            acc = g.p_add(Fq, acc, {tuple(e): comp[mfree + j][t]})
                        row.append(acc)
                    Lrows.append(row)
            if len(Lrows) != q:
                continue
            polys = minors_nf(A, N, Lrows, Fq, g.NV)
            if not polys:
                continue
            P = [[rf.RF(c) for c in pol] for pol in polys]
            P = [rf.poly_trim_rf(Q) for Q in P]
            P = [Q for Q in P if rf.poly_deg_rf(Q) >= 0]
            gg = P[0]
            for Q in P[1:]:
                gg = rf.poly_gcd_rf(gg, Q)
                if rf.poly_deg_rf(gg) == 0:
                    break
            dg = rf.poly_deg_rf(gg)
            res.append((sp.sstr(f), deg, mfree, R, "生成好" if dg == 0 else f"全坏（次数 {dg}）"))
    return res


def main() -> None:
    print("=" * 74)
    print("数域上的图卡 gcd")
    print("=" * 74)
    import c352_number_field_decider as d
    A, C = d.build_instance(4245)
    print("--- 4245, L0 空, q=4 ---")
    for item in decide_nf(A, C, None, 4):
        print("   ", item)


if __name__ == "__main__":
    main()
