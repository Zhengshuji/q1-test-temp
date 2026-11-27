#!/usr/bin/env python3
"""c335 — 三分的实测：v 在 B 上跑，看 Lambda(v) 是固定根、有限覆盖、还是真移动。

设置：n=5, p=1, r_0=0（无固定行），q=3，故 m=3、B=P(K_0)=P^2（二维底，v 可以真的动）。
超平面层 k=3, omega=2。

对每个 v ∈ K_0：
  U(v) = span(v, Av)，Q = U^perp 的基（行），
  M(lam) = Q (lam I - A) N        （(n-dim U) x k 的仿射铅笔）
  Lambda(v) = gcd 的零点，gcd 取 M 的 (k-1)-子式；
  并**直接**构造 L（3 行张满 U^perp），算 lam H - H_A 的 2-子式 gcd 作对照。

判定：
  * gcd 在所有 v 上相同（作为多项式）      -> 第 1 类（固定根）
  * gcd 变，但零点落在固定有限集内          -> 第 2 类（有限覆盖）
  * 零点随 v 真正移动                      -> 第 3 类（需要 S3 的 PIT）
"""

from __future__ import annotations

import itertools
import os
import random
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
lam = sp.symbols("lam")


def orth_basis(vectors):
    U = sp.Matrix.hstack(*[sp.Matrix(v) for v in vectors])
    ns = U.T.nullspace()
    return sp.Matrix.hstack(*ns).T if ns else sp.zeros(0, U.rows)


def ker_basis(M):
    ns = sp.Matrix(M).nullspace()
    return sp.Matrix.hstack(*ns) if ns else sp.zeros(M.cols, 0)


def gcd_of_minors(P, r):
    P = sp.Matrix(P)
    ms = []
    for rows in itertools.combinations(range(P.rows), r):
        for cols in itertools.combinations(range(P.cols), r):
            d = sp.expand(P.extract(list(rows), list(cols)).det())
            if sp.simplify(d) != 0:
                ms.append(d)
    if not ms:
        return sp.Integer(0)
    g = ms[0]
    for d in ms[1:]:
        g = sp.gcd(g, d)
    return sp.Poly(g, lam).monic().as_expr()


def analyze(A, C, N, v, label):
    n = A.rows
    k = N.cols
    U = [sp.Matrix(v), A * sp.Matrix(v)]
    du = sp.Matrix.hstack(*U).rank()
    U = U[:du] if du < 2 else U
    Q = orth_basis(U)
    M = sp.Matrix(Q.rows, k, lambda i, j: lam * (Q * N)[i, j] - (Q * A * N)[i, j])
    gM = gcd_of_minors(M, k - 1)

    # 直接构造 L：Q 的 3 行（若 dim U=2，Q 恰 3 行）
    if Q.rows >= 3:
        L = Q[:3, :]
    else:
        L = Q
    H = L * N
    HA = L * A * N
    P = sp.Matrix(H.rows, k, lambda i, j: lam * H[i, j] - HA[i, j])
    gH = gcd_of_minors(P, 2) if H.rows >= 2 else sp.Integer(0)

    KH = ker_basis(H)
    ok5a = (HA * KH).is_zero_matrix
    roots = sp.roots(sp.Poly(gM, lam), lam) if gM not in (0, 1) else {}
    print(f"  {label}: v={sp.Matrix(v).T.tolist()} dimU={du} rankH={H.rank()} (5a)={ok5a} "
          f"gcd_M={sp.sstr(gM)} gcd_pencil={sp.sstr(gH)} roots={list(roots.keys())}")
    return dict(dimU=du, gM=sp.sstr(gM), gH=sp.sstr(gH), roots=tuple(sorted(sp.sstr(r) for r in roots)))


def main() -> None:
    print("=" * 74)
    print("实例：n=5, p=1, r_0=0, q=3, k=3, omega=2；B = P(K_0) = P^2")
    print("=" * 74)
    A = sp.Matrix([[0, 1, 0, 0, 0],
                   [0, 0, 1, 0, 0],
                   [0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1],
                   [1, 2, 3, 5, 7]])
    C = sp.Matrix([[0, 0, 0, 0, 1]])
    W = sp.Matrix.vstack(C, C * A)
    assert W.rank() == 2
    N = ker_basis(W)
    print(f"  k = {N.cols}")

    rng = random.Random(335)
    recs = []
    # 采样 v ∈ K_0（P^2 上的点）
    for t in range(10):
        coeff = sp.Matrix([rng.randint(-3, 3), rng.randint(-3, 3), rng.randint(-3, 3)])
        if coeff.is_zero_matrix:
            continue
        v = N * coeff
        recs.append(analyze(A, C, N, v, f"v{t}"))

    print()
    gMs = {r["gM"] for r in recs}
    rootsets = {r["roots"] for r in recs}
    print(f"  不同 gcd 的个数：{len(gMs)} -> {sorted(gMs)}")
    print(f"  不同零点集的个数：{len(rootsets)} -> {sorted(rootsets)}")

    if len(gMs) == 1:
        print("  => 第 1 类：固定根（在所有采样点上 gcd 相同）")
    elif len(rootsets) == 1:
        print("  => 第 2 类：有限覆盖（gcd 变，但零点集固定）")
    else:
        print("  => 第 3 类：零点随 v 移动（需要 S3 的 PIT）")


if __name__ == "__main__":
    main()
