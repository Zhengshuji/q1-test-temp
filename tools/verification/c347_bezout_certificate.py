#!/usr/bin/env python3
"""c347 — n=8, p=2 富余档实例的**显式有理好点 + Bézout 证书**。

目的（专家意见 §6–§8）：把"18/27 采样"升级为该实例的**定理**：
只要给出**一个**有理好点并附 Bézout 证书 Σ g_i f_i = 1（f_i 为铅笔的 ω×ω 极大子式），
再由"坏集闭 + 参数族不可约"即得"好点构成非空 Zariski 开稠密集"。

构造与 341 一致：C = [e1; e2]，A 的前两行 = e3, e4，K0 = span{e5..e8}，
A 在 K0 上的 K0-部分为 B（B[:,0] = μ e1，使 v = e5 是"K0 部分"的特征向量），
第 3、4 行取一般随机（使 Av ∉ K0，从而非特征）。
"""

from __future__ import annotations

import itertools
import os
import random
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
if os.path.join(_ROOT, "tools/verification") not in sys.path:
    sys.path.insert(0, os.path.join(_ROOT, "tools/verification"))

import c335_lambda_movement as m  # noqa: E402

lam = sp.symbols("lam")


def build(n=8, seed=4242, trial=0, mu=1):
    rng = random.Random(seed)
    p = 2
    C = sp.zeros(p, n)
    C[0, 0] = 1
    C[1, 1] = 1
    A = sp.zeros(n, n)
    for _ in range(trial + 1):
        A = sp.zeros(n, n)
        A[0, 2] = 1
        A[1, 3] = 1
        for j in range(n):
            A[2, j] = rng.randint(-2, 2)
            A[3, j] = rng.randint(-2, 2)
        k = n - 4
        B = sp.Matrix(k, k, lambda i, j: rng.randint(-2, 2))
        for i in range(k):
            B[i, 0] = mu if i == 0 else 0
        for i in range(k):
            for j in range(k):
                A[4 + i, 4 + j] = B[i, j]
        mu = rng.choice([1, 2, -1])
    return A, C


def gcd_of_minors(P, r):
    ms = []
    for rows in itertools.combinations(range(P.rows), r):
        for cols in itertools.combinations(range(P.cols), r):
            d = sp.expand(P.extract(list(rows), list(cols)).det())
            if sp.simplify(d) != 0:
                ms.append(sp.Poly(d, lam))
    return ms


def bezout(polys):
    """返回 a_i 使 sum a_i f_i = 1（若 gcd = 1）；迭代线性组合。"""
    a = [sp.Integer(1)]
    g = polys[0].as_expr()
    for i in range(1, len(polys)):
        fi = polys[i].as_expr()
        u, v, h = sp.gcdex(g, fi)
        a = [sp.expand(u * aj) for aj in a] + [sp.expand(v)]
        g = sp.expand(h)
    if sp.degree(g, lam) != 0:
        return None, g
    return [sp.expand(aj / g) for aj in a], g


def main() -> None:
    print("=" * 74)
    print("n=8, p=2 富余档：显式有理好点 + Bézout 证书")
    print("=" * 74)
    A, C = build()
    n = A.rows
    W = sp.Matrix.vstack(C, C * A)
    assert W.rank() == 4, W.rank()
    N = m.ker_basis(W)
    k = N.cols
    om = k - 1
    print(f"  rank[C;CA] = {W.rank()}, k = {k}, omega = {om}, n-2-p = {n - 2 - 2}")
    v = N * sp.Matrix([1] + [0] * (k - 1))
    U = sp.Matrix.hstack(v, A * v)
    assert U.rank() == 2, "v 应为非特征"
    print(f"  v 非特征 ✓（dim U = {U.rank()}）")
    Q = m.orth_basis([v, A * v])

    rng = random.Random(341 * 7)
    found = None
    for t in range(60):
        coeffs = sp.Matrix([rng.randint(-2, 2) for _ in range(Q.rows)])
        x = Q.T * coeffs
        if (N.T * x).norm() == 0:
            continue
        fv = (v.T * N)
        ns = sp.Matrix([[fv[0, i] for i in range(k)]]).nullspace()
        K0v = sp.Matrix.hstack(*ns)
        if K0v.cols != k - 1:
            continue
        L = sp.Matrix.vstack(*[(N * K0v[:, j]).reshape(1, n) for j in range(k - 1)],
                             x.reshape(1, n))
        H = L * N
        if H.rank() != om:
            continue
        HA = L * A * N
        if not (HA * m.ker_basis(H)).is_zero_matrix:
            continue
        P = sp.Matrix(L.rows, k, lambda i, j: lam * H[i, j] - HA[i, j])
        polys = gcd_of_minors(P, om)
        if not polys:
            continue
        g = polys[0]
        for q in polys[1:]:
            g = sp.gcd(g, q)
        if g.degree() == 0:
            found = (L, H, HA, P, polys, coeffs)
            break

    if found is None:
        print("  !! 未找到好点（可换 seed/trial）")
        return

    L, H, HA, P, polys, coeffs = found
    print(f"  找到好点：超平面法向坐标 = {sp.Matrix(coeffs).T.tolist()}")
    print(f"  极大子式个数 = {len(polys)}（3×3，来自 4×4 铅笔）")

    coefs, h = bezout(polys)
    if coefs is None:
        print(f"  !! Bézout 未成功（gcd 次数 {h.degree()}）")
        return
    # 核对 Σ g_i f_i = 1
    total = sp.expand(sum(c * p.as_expr() for c, p in zip(coefs, polys)))
    assert sp.simplify(total - 1) == 0, "Bézout 恒等式不成立"
    print("  Bézout 证书：Σ g_i f_i = 1 ✓（精确整数/有理运算）")
    print(f"  deg g_i 最大 = {max(sp.degree(c, lam) for c in coefs)}（应 < omega = {om}）")

    # 记录：H 与 H_A（有理）
    print("  H =", H.tolist())
    print("  H_A =", HA.tolist())


if __name__ == "__main__":
    main()
