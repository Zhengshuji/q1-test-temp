#!/usr/bin/env python3
"""c346 — 左因子改写的最小核对（快版）。

事实：(5a)（row H_A ⊆ row H）⟹ 存在 S 使 H_A = S H，于是 P(λ) = (λI - S) H。
本脚本对若干**可容许**层点：解出 S、核对 (λI-S)H = λH - H_A 在若干有理 λ 处成立，
并用秩-零化度核对 rank P(λ) = ω - dim(im H ⊓ ker(λI - S))。

（符号特征值计算很慢，故这里不枚举特征值，只验证恒等式本身与秩公式。）
"""

from __future__ import annotations

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


def solve_S(H, HA):
    q = H.rows
    HT = H.T
    rows = []
    for i in range(q):
        rhs = sp.Matrix(HA.row(i)).T
        sol = HT.gauss_jordan_solve(rhs)[0]
        rows.append(sol.T)
    return sp.Matrix.vstack(*rows)


def check_instance(A, C, v, nsamples=3, seed=11):
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    k = N.cols
    om = k - 1
    Q = m.orth_basis([v])
    rng = random.Random(seed)
    checked = 0
    for _ in range(nsamples):
        L = sp.Matrix(Q.rows, A.rows,
                      lambda i, j: sum(rng.randint(-2, 2) * Q[b, j] for b in range(Q.rows)))
        H = L * N
        if H.rank() != om:
            continue
        HA = L * A * N
        if not (HA * m.ker_basis(H)).is_zero_matrix:   # 只取可容许点（(5a)）
            continue
        S = solve_S(H, HA)
        assert (S * H - HA).is_zero_matrix, "S H 应等于 H_A"
        for lv in (0, 1, 2, sp.Rational(1, 2)):
            P = lv * H - HA
            lhs = (lv * sp.eye(S.rows) - S) * H
            assert (lhs - P).is_zero_matrix, "（λI-S)H 应等于 λH - H_A"
            # 秩公式：rank P = ω - dim(im H ⊓ ker(λI-S))
            imH = sp.Matrix.hstack(*H.columnspace())
            K = (lv * sp.eye(S.rows) - S).nullspace()
            E = sp.Matrix.hstack(*K) if K else sp.zeros(S.rows, 0)
            inter = len(imH.row_join(-E).nullspace()) if E.cols else 0
            assert P.rank() == om - inter, (P.rank(), om, inter)
            checked += 1
    return checked


def main() -> None:
    print("=" * 74)
    print("左因子改写核对：(λI-S)H = λH - H_A，且 rank P = ω - dim(im H ⊓ ker(λI-S))")
    print("=" * 74)
    C = sp.Matrix([[0, 0, 0, 0, 1]])
    v = sp.Matrix([1, 0, 0, 0, 0])
    A1 = sp.Matrix([[2, 2, -1, 0, 0],
                    [0, -2, 1, 0, 1],
                    [0, 1, -2, 0, -1],
                    [0, 0, 0, 0, 2],
                    [0, -1, 2, 0, -1]])
    A2 = sp.Matrix([[2, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1],
                    [0, 3, 5, 7, 11]])
    n1 = check_instance(A1, C, v)
    n2 = check_instance(A2, C, v)
    print(f"  反例 336：{n1} 个核对点通过")
    print(f"  好实例 333：{n2} 个核对点通过")
    print("  结论：可容许点上 S 存在，且 P(λ) = (λI-S)H 与秩公式成立。")


if __name__ == "__main__":
    main()
