#!/usr/bin/env python3
"""c362 — 数域上的图卡判定（任意 m，任意特征值的不可约因子）。

流程：分解压缩的特征多项式 → 对每个因子建数域 K = Q[mu]/(f) → 特征向量 v →
D_v = K0 ∩ U_v^perp（K 上）→ V0 的像 → Grassmannian 图卡（X 为符号）→
铅笔子式（系数是 K 上的 X-多项式）→ K(X)[lambda] 上的 gcd。
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


# ---------- K 上向量/矩阵的小工具 ----------
def rank_rows(Fq, rows):
    return g.rank_rows(Fq, rows)


def mat_apply(Fq, mat, vec):
    """mat（整数矩阵，行列表）作用于 vec（K 上）的行——用于 L·N 这类。"""
    out = []
    for i in range(len(mat)):
        acc = Fq.zero()
        for j, v in enumerate(vec):
            c = mat[i][j]
            if c != 0:
                acc = Fq.add(acc, Fq.mul(Fq.elt(F(int(c))), v))
        out.append(acc)
    return out


def column_apply(Fq, mat, vec, nrows, ncols):
    """y = M · vec，M 为 nrows×ncols 的整数矩阵（行列表），vec 长度 ncols。"""
    out = []
    for i in range(nrows):
        acc = Fq.zero()
        for j in range(ncols):
            c = mat[i][j]
            if c != 0:
                acc = Fq.add(acc, Fq.mul(Fq.elt(F(int(c))), vec[j]))
        out.append(acc)
    return out


def nf_decision(A, C, L0, q, verbose=True):
    n = A.rows
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    k = N.cols
    om = k - 1
    G = N.T * N
    M = G.inv() * (N.T * A * N)
    r0 = L0.rows if L0 is not None else 0
    Amat = [[int(A[i, j]) for j in range(n)] for i in range(n)]
    Nmat = [[int(N[i, j]) for j in range(k)] for i in range(n)]
    AN = sp.Matrix(A * N)
    ANmat = [[int(AN[i, j]) for j in range(k)] for i in range(n)]
    x = sp.symbols("x")
    cp = sp.Poly(M.charpoly(x).as_expr(), x)
    out = []
    for f, mult in sp.factor_list(cp.as_expr())[1]:
        fp = sp.Poly(f, x)
        deg = fp.degree()
        coeffs = [int(fp.coeff_monomial(x**i)) for i in range(deg)] + [1]
        Fq = NF(coeffs)
        if deg == 1:
            mu = Fq.elt(F(-int(fp.coeff_monomial(1))))
        else:
            mu = Fq.elt(*([0] + [1] + [0] * (deg - 2)))
        Mf = []
        for i in range(k):
            row = []
            for j in range(k):
                r = sp.Rational(M[i, j])
                row.append(Fq.elt(F(r.p, r.q)))
            Mf.append(row)
        rows = [[Fq.sub(Mf[i][j], mu) if i == j else Mf[i][j] for j in range(k)] for i in range(k)]
        ns = mat_nullspace(Fq, rows)
        if verbose:
            print(f"  因子 {sp.sstr(f)}（次数 {deg}）: 特征空间维数 = {len(ns)}")
        for cdir in ns:
            v = column_apply(Fq, Nmat, cdir, n, k)          # v = N c
            Av = column_apply(Fq, Amat, v, n, n)
            if rank_rows(Fq, [v, Av]) < 1:
                continue
            # 预设行：L0 v = 0 且 L0 A v = 0
            if r0:
                ok = True
                for i in range(r0):
                    row = [int(L0[i, j]) for j in range(n)]
                    s1 = Fq.zero()
                    s2 = Fq.zero()
                    for j in range(n):
                        if row[j] != 0:
                            s1 = Fq.add(s1, Fq.mul(Fq.elt(F(row[j])), v[j]))
                            s2 = Fq.add(s2, Fq.mul(Fq.elt(F(row[j])), Av[j]))
                    if not (Fq.is_zero(s1) and Fq.is_zero(s2)):
                        ok = False
                        break
                if not ok:
                    continue
            # D_v = K0 ∩ U_v^perp（K 坐标）
            fv = [Fq.zero() for _ in range(k)]
            fa = [Fq.zero() for _ in range(k)]
            for j in range(k):
                s1 = Fq.zero()
                s2 = Fq.zero()
                for i in range(n):
                    if Nmat[i][j] != 0:
                        s1 = Fq.add(s1, Fq.mul(Fq.elt(F(Nmat[i][j])), v[i]))
                        s2 = Fq.add(s2, Fq.mul(Fq.elt(F(Nmat[i][j])), Av[i]))
                fv[j] = s1
                fa[j] = s2
            DvK = mat_nullspace(Fq, [fv, fa])
            if len(DvK) != om:
                if verbose:
                    print(f"    方向被跳过：dim D_v = {len(DvK)} != {om}")
                continue
            if verbose:
                print(f"    可容许方向：dim D_v = {om}")
            out.append(sp.sstr(f))
            break
    return out


def main() -> None:
    print("=" * 74)
    print("数域上的可容许方向（含预设行筛）")
    print("=" * 74)
    import c352_number_field_decider as d
    A, C = d.build_instance(4245)
    L0 = sp.Matrix([[0, 0, 0, 0, 0, 1, 0, 0]])
    print("L0 = e_6, q = 4")
    res = nf_decision(A, C, L0, 4)
    print("  可容许方向来自因子：", res)


if __name__ == "__main__":
    main()
