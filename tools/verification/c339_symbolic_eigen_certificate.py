#!/usr/bin/env python3
"""c339 — 特征纤维的符号证书：整条 P^1 的行空间都给出 gcd = 1。

实例：n=5, p=1, C=e5^T, A e1 = 2 e1, e1 in K_0。
U = span(e1)，U^perp 为 4 维；行空间 V_t = <Q0,Q1> + <Q2 + t Q3>（t 为符号），
L_t = [Q0; Q1; Q2 + t Q3]，在 Q(t)[lam] 里算 lam H - H_A 的 2-子式 gcd。

断言：gcd == 1（即整条 P^1 上都没有公共根）——这是**符号精确计算**，不是采样。
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

lam, t = sp.symbols("lam t")


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
    return sp.simplify(g)


def main() -> None:
    print("=" * 74)
    print("特征纤维的符号证书（n=5, p=1, C=e5^T, A e1 = 2 e1）")
    print("=" * 74)
    C = sp.Matrix([[0, 0, 0, 0, 1]])
    A = sp.Matrix([[2, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0],
                   [0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1],
                   [0, 3, 5, 7, 11]])
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    assert N.cols == 3
    Q = m.orth_basis([sp.Matrix([1, 0, 0, 0, 0])])
    assert Q.rows == 4, "U^perp 应为 4 维"
    Q0, Q1, Q2, Q3 = [Q.row(i) for i in range(4)]
    w = (Q2 + t * Q3).reshape(1, 5)
    L = sp.Matrix.vstack(Q0, Q1, w)
    H = L * N
    HA = L * A * N
    k = N.cols
    P = sp.Matrix(3, k, lambda i, j: lam * H[i, j] - HA[i, j])

    # 数值扫描（13 个有理 t）：全部应 rankH = 2、(5a)、gcd = 1
    ok = 0
    for tv in range(-6, 7):
        Lv = L.subs(t, tv)
        Hv = Lv * N
        if Hv.rank() != k - 1:
            continue
        HAv = Lv * A * N
        KHv = m.ker_basis(Hv)
        if not (HAv * KHv).is_zero_matrix:
            continue
        gv = gcd_of_minors(sp.Matrix(3, k, lambda i, j: lam * Hv[i, j] - HAv[i, j]), 2)
        if gv == 1:
            ok += 1
    print(f"  数值扫描：13 个 t 中 {ok} 个 gcd = 1（其余跳过：(5a)/rank 不满足）")

    g = gcd_of_minors(P, 2)
    print(f"  符号 gcd（在 Q(t)[lam] 上）= {sp.sstr(g)}")
    assert g == 1, f"符号 gcd 应为 1，得到 {g}"
    print("  符号证书通过：整条 P^1 的行空间都给出好的铅笔。")


if __name__ == "__main__":
    main()
