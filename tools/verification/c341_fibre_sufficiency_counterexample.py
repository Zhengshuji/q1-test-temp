#!/usr/bin/env python3
"""c341 — 纤维充分性猜想的反例（专家 96 号要的"反例"）。

实例：n=5, p=1, C=e5^T,
  A = [[2,2,-1,0,0],[0,-2,1,0,1],[0,1,-2,0,-1],[0,0,0,0,2],[0,-1,2,0,-1]]
此时 v = e1 满足 Av = 2v、Cv = 0、CAv = 0，故 e1 是 K0 中的特征向量。

结构原因（λ = 0 的秩）：
  K0 = span{e1, (0,2,1,0,0), e4}；A K0 = span{Ae1 = (2,0,0,0,0), A(0,2,1,0,0) = (3,-3,0,0,0)}，dim = 2。
  e1 ∈ A K0，而任何层点都有行空间 V ⊆ e1^⊥，故 V^⊥ ⊇ span{e1}，于是
     rank(H_A) = dim(A K0) − dim(A K0 ∩ V^⊥) ≤ 2 − 1 = 1 < ω = 2，
  即在 λ = 0 处 (5b) 已经失败 —— **与 R 无关**。

本脚本：
  (1) 断言上面的结构；
  (2) 对若干随机行空间 V ⊆ e1^⊥，验证 rank H = 2、(5a) 成立，但 rank H_A ≤ 1、gcd 被 λ 整除。
"""

from __future__ import annotations

import itertools
import os
import random
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import c335_lambda_movement as m  # noqa: E402

lam = sp.symbols("lam")


def gcd2(P):
    ms = []
    for rows in itertools.combinations(range(P.rows), 2):
        for cols in itertools.combinations(range(3), 2):
            d = sp.expand(P.extract(list(rows), list(cols)).det())
            if sp.simplify(d) != 0:
                ms.append(d)
    g = ms[0]
    for x in ms[1:]:
        g = sp.gcd(g, x)
    return sp.Poly(g, lam).monic().as_expr()


def main() -> None:
    print("=" * 74)
    print("反例：K_0 含特征向量，但整条特征纤维全坏（λ = 0 的秩）")
    print("=" * 74)
    C = sp.Matrix([[0, 0, 0, 0, 1]])
    A = sp.Matrix([[2, 2, -1, 0, 0],
                   [0, -2, 1, 0, 1],
                   [0, 1, -2, 0, -1],
                   [0, 0, 0, 0, 2],
                   [0, -1, 2, 0, -1]])
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    e1 = sp.Matrix([1, 0, 0, 0, 0])

    # (1) 结构断言
    assert N.cols == 3, N.cols
    assert (C * e1).is_zero_matrix
    assert (A * e1 - 2 * e1).is_zero_matrix
    print(f"  e1 是 K_0 中的特征向量（A e1 = 2 e1）✓")
    AK0 = A * N
    print(f"  dim(A K0) = {AK0.rank()}  ( = ω = 2，临界 )")
    assert AK0.rank() == 2
    # e1 ∈ A K0 ?
    sol = AK0.gauss_jordan_solve(e1)[0]
    assert (AK0 * sol - e1).is_zero_matrix, "e1 应在 A K0 内"
    print("  e1 ∈ A K0 ✓（故 A K0 ∩ V^⊥ 恒非零）")

    # (2) 随机行空间验证
    Q = m.orth_basis([e1])
    rng = random.Random(341)
    good = bad = 0
    checked = 0
    for t in range(20):
        L = sp.Matrix(3, 5, lambda i, j: sum(rng.randint(-2, 2) * Q[b, j] for b in range(Q.rows)))
        H = L * N
        if H.rank() != 2:
            continue
        HA = L * A * N
        if not (HA * m.ker_basis(H)).is_zero_matrix:
            continue
        checked += 1
        assert HA.rank() <= 1, f"rank H_A 应 ≤ 1，得到 {HA.rank()}"
        g = gcd2(sp.Matrix(3, 3, lambda i, j: lam * H[i, j] - HA[i, j]))
        deg = 0 if g in (0, 1) else sp.Poly(g, lam).degree()
        if deg == 0:
            good += 1
        else:
            bad += 1
    print(f"  随机层点 {checked} 个：好 {good}，坏 {bad}；全部 rank H_A ≤ 1（λ=0 即失效）")
    assert good == 0 and checked > 0
    print()
    print("  结论：该实例 K_0 含特征向量，但特征纤维**整条全坏** ⟹ 纤维充分性猜想不成立。")


if __name__ == "__main__":
    main()
