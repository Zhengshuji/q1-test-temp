#!/usr/bin/env python3
"""c337 — 特征纤维 F_lambda 是否 generically 可行（H4 的反例搜索）。

构造：n=5, p=1, C=e5^T，A 使 v=e1 是特征向量（A e1 = 2 e1），且 e1 ∈ K_0。
此时 U = span(v)（1 维），U^perp 是 4 维；自由行只受 rv = 0 一个独立条件（rAv = lambda0 rv 自动）。

在该纤维里采样多组行（要求 rank H = k-1 = 2 且 (5a) 成立），算 lambda H - H_A 的 2-子式 gcd：
  * 全部 gcd = 1  -> 该纤维 generically 好（H4 在此实例成立）
  * 出现 gcd != 1 -> 需要判断是"特殊行"还是"generical 坏"（后者即 H4 的反例）
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


def main() -> None:
    print("=" * 74)
    print("特征纤维 F_lambda 的可行性测试（H4）")
    print("=" * 74)
    C = sp.Matrix([[0, 0, 0, 0, 1]])
    A = sp.Matrix([[2, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0],
                   [0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1],
                   [0, 3, 5, 7, 11]])
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    k = N.cols
    v = sp.Matrix([1, 0, 0, 0, 0])
    assert (W * v).is_zero_matrix and (A * v - 2 * v).is_zero_matrix
    print(f"  k={k}; v=e1, A e1 = 2 e1, e1 in K_0")
    Q = m.orth_basis([v])          # U^perp 的基（4 行）
    print(f"  dim U^perp = {Q.rows}")

    rng = random.Random(337)
    good = bad = 0
    rows_checked = 0
    for t in range(40):
        # 3 行：第 0 行当"固定行"，另 2 行当自由行；都取 U^perp 里的随机组合
        L = sp.Matrix(3, 5, lambda i, j: sum(rng.randint(-2, 2) * Q[b, j] for b in range(Q.rows)))
        H = L * N
        if H.rank() != k - 1:
            continue
        HA = L * A * N
        KH = m.ker_basis(H)
        if not (HA * KH).is_zero_matrix:
            continue          # (5a) 不成立，不在层内
        rows_checked += 1
        P = sp.Matrix(H.rows, k, lambda i, j: lam * H[i, j] - HA[i, j])
        g = gcd_of_minors(P, 2)
        deg = 0 if g in (0, 1) else sp.Poly(g, lam).degree()
        print(f"  L#{t}: gcd = {sp.sstr(g)}  (deg {deg})")
        if deg == 0:
            good += 1
        else:
            bad += 1

    print()
    print(f"  样本：{rows_checked} 组行；好 {good}，坏 {bad}")
    if bad == 0 and good > 0:
        print("  => 该特征纤维的所有样本都**好**（H4 在此实例成立；需符号化才能称定理）")
    elif good == 0 and bad > 0:
        print("  => 该特征纤维的样本全**坏**（可能是 H4 的反例，需确认 genericity）")
    else:
        print("  => 混合：需要判断坏集是否为薄集")


if __name__ == "__main__":
    main()
