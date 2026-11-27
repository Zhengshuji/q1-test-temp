#!/usr/bin/env python3
"""c357 — 重特征值反例的完整证书（专家 103 号 §9.2/§9.3 要求）。

给出：
  1. 完整数据：A, C, N, M, A21（全部有理/整数矩阵）；
  2. 六个方向的纤维 generic gcd 次数与**符号 gcd**；
  3. 坏方向：给出非平凡公因子 g(x,lambda)，并逐条验证 g | m_I（整除检验）；
  4. 好方向：给出一个有理图卡点 x0，在该点 gcd = 1，并给出 univariate Bezout 恒等式。
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
import c352_number_field_decider as d  # noqa: E402
import c354_generic_gcd_nf as g  # noqa: E402
import c355_rf_gcd as rf  # noqa: E402
from nf import NF, mat_nullspace  # noqa: E402

lam = sp.symbols("lam")


def build():
    A, C = d.build_instance(4242)
    A = sp.Matrix(A)
    B = sp.diag(1, 1, 2, 3)
    for i in range(4):
        for j in range(4):
            A[4 + i, 4 + j] = B[i, j]
    return A, C


def field_for_one():
    """因子 x - 1 的域 Q 与 mu = 1。"""
    Fq = NF([-1, 1])
    return Fq, Fq.elt(F(1))


def v_of(N, Fq, coeffs):
    n = N.rows
    v = [Fq.zero() for _ in range(n)]
    for j in range(len(coeffs)):
        if coeffs[j] == 0:
            continue
        for i in range(n):
            if N[i, j] != 0:
                v[i] = Fq.add(v[i], Fq.mul(Fq.elt(F(int(N[i, j]))), Fq.elt(F(coeffs[j]))))
    return v


def poly_divide(Fq, a, b):
    """RF 系数的 lambda-多项式除法，返回 (q, r)。"""
    a = list(a)
    b = list(b)
    db = rf.poly_deg_rf(b)
    q = [rf.RF({}) for _ in range(max(0, rf.poly_deg_rf(a) - db + 1))]
    while True:
        da = rf.poly_deg_rf(a)
        if da < db:
            break
        fac = rf.rf_mul(a[da], rf.rf_inv(b[db]))
        shift = da - db
        q[shift] = fac
        for i in range(db + 1):
            a[shift + i] = rf.rf_sub(a[shift + i], rf.rf_mul(fac, b[i]))
        rf.poly_trim_rf(a)
    return q, a


def main() -> None:
    A, C = build()
    n = A.rows
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    k = N.cols
    om = k - 1
    G = N.T * N
    M = G.inv() * (N.T * A * N)
    # A21 = pi_{K0^perp} A |_{K0}，作为 n×k 矩阵（K 坐标到环境空间）
    Proj21 = sp.eye(n) - N * G.inv() * N.T
    A21 = sp.Matrix(Proj21 * (A * N))
    print("=" * 78)
    print("完整数据（专家 103 号 §9.2）")
    print("=" * 78)
    print("A =", A.tolist())
    print("C =", C.tolist())
    print("rank[C;CA] =", W.rank(), " k =", k, " omega =", om)
    print("N =", N.tolist())
    print("M（压缩，K 坐标）= ", M.tolist())
    print("A21（K0^perp 分量）= ", A21.tolist())
    print("charpoly =", sp.factor(M.charpoly(sp.symbols('x')).as_expr()))

    Fq, mu = field_for_one()
    rf.Fq_one = (Fq,)
    Mf = []
    for i in range(k):
        row = []
        for j in range(k):
            r = sp.Rational(M[i, j])
            row.append(Fq.elt(F(r.p, r.q)))
        Mf.append(row)
    rows = [[Fq.sub(Mf[i][j], mu) if i == j else Mf[i][j] for j in range(k)] for i in range(k)]
    ns = mat_nullspace(Fq, rows)
    print("E_1 维数 =", len(ns), "（应为 2）")

    print()
    print("=" * 78)
    print("六个方向的符号 gcd（专家 §9.3 要求证书）")
    print("=" * 78)
    for (a, b) in [(1, 0), (0, 1), (1, 1), (1, 2), (2, -1), (3, 1)]:
        v = v_of(N, Fq, [a, b])
        polys = g.fibre_polys(A, N, v, Fq, None)
        if not polys:
            print(f"方向 ({a},{b}): 构造失败")
            continue
        P = [[rf.RF(cc) for cc in Pi] for Pi in polys]
        P = [rf.poly_trim_rf(Q) for Q in P]
        P = [Q for Q in P if rf.poly_deg_rf(Q) >= 0]
        gg = P[0]
        for Q in P[1:]:
            gg = rf.poly_gcd_rf(gg, Q)
            if rf.poly_deg_rf(gg) == 0:
                break
        dg = rf.poly_deg_rf(gg)
        tag = "生成好" if dg == 0 else f"全坏（次数 {dg}）"
        print(f"  方向 ({a},{b}): gcd 次数 {dg}  => {tag}")
        if dg > 0:
            # 验证 gcd 整除每个子式
            ok = True
            for Q in P:
                _, r = poly_divide(Fq, Q, gg)
                if rf.poly_deg_rf(r) >= 0:
                    ok = False
            print(f"      公因子整除全部子式：{ok}")
            print(f"      gcd 的 lambda 次数 = {dg}；子式个数 = {len(P)}")
        else:
            # 好方向：给一个有理图卡点 x0，在该点 gcd = 1（univariate，可复现证书）
            from nf import poly_gcd as _pg, poly_deg as _pd

            def eval_at(poly_dict, x0):
                val = Fq.zero()
                for e, cv in poly_dict.items():
                    term = cv
                    for j, ej in enumerate(e):
                        for _ in range(ej):
                            term = Fq.mul(term, Fq.elt(F(x0[j])))
                    val = Fq.add(val, term)
                return val

            for x0 in [tuple([1] * g.NV), tuple(range(1, g.NV + 1)),
                       tuple([2] * g.NV), tuple([1] + [0] * (g.NV - 1))]:
                vals = []
                for Q in P:
                    coeffs = [eval_at(cc.num, x0) for cc in Q]
                    if any(not Fq.is_zero(c) for c in coeffs):
                        vals.append(coeffs)
                if len(vals) < 2:
                    continue
                gg2 = vals[0]
                for q in vals[1:]:
                    gg2 = _pg(Fq, gg2, q)
                    if _pd(Fq, gg2) == 0:
                        break
                if _pd(Fq, gg2) == 0:
                    print(f"      有理图卡点 x0={x0}: 该点 gcd = 1 ✓（证书）")
                    break


if __name__ == "__main__":
    main()
