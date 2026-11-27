#!/usr/bin/env python3
"""c362 — 直和（块对角）能否把两个"非空性条件"AND 起来？

架构：变量进实例数据 (A,C,L0)，R 只当见证；"可行"（∃R）承载条件。
本脚本检验最自然的组合方式——块对角直和——是否满足
    直和实例可行  <=>  两个块各自可行。

每块用 303C 的输入非零门（变量 x 在 A 里，块内可行 <=> x != 0）：
  n=3, C=[0 0 1], A(x)=[[0,0,0],[x,0,0],[0,1,0]], L0=[1 0 0].
直和：n=6, C=[C1 C2], A=diag(A(x1),A(x2)), L0=[L01 L02]。

对 (x1,x2) ∈ {0,1}^2，采样自由行 R（2x6，条目 ∈ {-1,0,1}），检验 (5a)(5b)。
"""

from __future__ import annotations

import itertools
import os
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import c335_lambda_movement as m  # noqa: E402

lam = sp.symbols("lam")


def gcd_minors(P, r):
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


def block(x):
    C = sp.Matrix([[0, 0, 1]])
    A = sp.Matrix([[0, 0, 0], [x, 0, 0], [0, 1, 0]])
    L0 = sp.Matrix([[1, 0, 0]])
    return C, A, L0


def direct_sum(x1, x2):
    C1, A1, L1 = block(x1)
    C2, A2, L2 = block(x2)
    # C 必须**堆叠**成块对角（不能拼接），否则 K_0 被耦合
    C = sp.Matrix([[0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1]])
    A = sp.Matrix.diag(A1, A2)
    L0 = sp.Matrix.hstack(L1, L2)
    return C, A, L0


def feasible_exists(x1, x2, m_rows=2, budget=400):
    C, A, L0 = direct_sum(x1, x2)
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    if N.cols == 0:
        return False, 0, None
    AN = A * N
    H0 = L0 * N
    HA0 = L0 * AN
    rng = __import__("random").Random(362)
    found = None
    tried = 0
    for _ in range(budget):
        R = sp.Matrix(m_rows, 6, lambda i, j: rng.randint(-1, 1))
        H = sp.Matrix.vstack(H0, R * N)
        w = H.rank()
        if w == 0:
            continue
        HA = sp.Matrix.vstack(HA0, R * AN)
        if not (HA * m.ker_basis(H)).is_zero_matrix:
            continue
        P = sp.Matrix(H.rows, N.cols, lambda i, j: lam * H[i, j] - HA[i, j])
        tried += 1
        if gcd_minors(P, w) == 1:
            found = (R.tolist(), w)
            break
    return found is not None, tried, found


def main() -> None:
    print("=" * 74)
    print("直和能否 AND 组合两个非空性条件（303C 块，x_i ∈ {0,1}）")
    print("=" * 74)
    for x1 in (0, 1):
        for x2 in (0, 1):
            ok, tried, found = feasible_exists(x1, x2)
            expect = (x1 != 0) and (x2 != 0)
            tag = "OK" if ok == expect else "**不符**"
            print(f"  (x1,x2)=({x1},{x2}): 直和可行={ok}（期望 {expect}）{tag}；检查了 {tried} 个层点")
            if found:
                print(f"      见证 R={found[0]}（ω={found[1]}）")


if __name__ == "__main__":
    main()
