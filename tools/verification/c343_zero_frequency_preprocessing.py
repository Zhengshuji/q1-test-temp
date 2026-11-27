#!/usr/bin/env python3
"""c343 — 零频预处理的实现与两个实例的对照。

零频条件（Prop C）：对层点，rank(H_A) = ω 是 (5b) 在 λ=0 的必要条件；
且 rank(H_A) = dim(AK0) - dim(AK0 cap V^perp)。

本脚本：
  (1) 在 336 的反例上：所有层点 rank(H_A) <= 1 < ω = 2 ⟹ 零频即全灭（应 0 个通过）；
  (2) 在 333 的好实例上：存在层点 rank(H_A) = 2 = ω ⟹ 有通过者。
这验证"预处理"能把 336 那类实例**在算 gcd 之前**就排除。
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


def scan(A, C, v, nsamples=40, seed=0):
    """在特征纤维里随机取层点，统计零频条件 rank(H_A)=omega 的通过数。"""
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    k = N.cols
    om = k - 1
    Q = m.orth_basis([v])           # v^perp（特征情形：U = span(v)）
    rng = random.Random(seed)
    passed = total = 0
    for _ in range(nsamples):
        L = sp.Matrix(3, A.rows, lambda i, j: sum(rng.randint(-2, 2) * Q[b, j] for b in range(Q.rows)))
        H = L * N
        if H.rank() != om:
            continue
        total += 1
        HA = L * A * N
        if HA.rank() == om:
            passed += 1
    return total, passed, om, N.cols


def main() -> None:
    print("=" * 74)
    print("零频预处理：rank(H_A) = omega 是 (5b) 在 lambda=0 的必要条件")
    print("=" * 74)

    # (1) 336 的反例
    A1 = sp.Matrix([[2, 2, -1, 0, 0],
                    [0, -2, 1, 0, 1],
                    [0, 1, -2, 0, -1],
                    [0, 0, 0, 0, 2],
                    [0, -1, 2, 0, -1]])
    C1 = sp.Matrix([[0, 0, 0, 0, 1]])
    v1 = sp.Matrix([1, 0, 0, 0, 0])
    W1 = sp.Matrix.vstack(C1, C1 * A1)
    N1 = m.ker_basis(W1)
    AK0 = A1 * N1
    print(f"  [反例 336] dim K0 = {N1.cols}, dim(A K0) = {AK0.rank()} (omega = {N1.cols-1})")
    total, passed, om, k = scan(A1, C1, v1)
    print(f"    层点 {total} 个；零频通过 {passed} 个 (omega = {om})")
    assert passed == 0, "反例上不应有零频通过者"

    # (2) 333 的好实例
    A2 = sp.Matrix([[2, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1],
                    [0, 3, 5, 7, 11]])
    C2 = sp.Matrix([[0, 0, 0, 0, 1]])
    v2 = sp.Matrix([1, 0, 0, 0, 0])
    W2 = sp.Matrix.vstack(C2, C2 * A2)
    N2 = m.ker_basis(W2)
    AK02 = A2 * N2
    print(f"  [好实例 333] dim K0 = {N2.cols}, dim(A K0) = {AK02.rank()} (omega = {N2.cols-1})")
    total2, passed2, om2, k2 = scan(A2, C2, v2)
    print(f"    层点 {total2} 个；零频通过 {passed2} 个 (omega = {om2})")
    assert passed2 > 0, "好实例上应有零频通过者"

    print()
    print("  结论：零频预处理能在算 gcd 之前排除 336 那类实例（0 通过），")
    print("        而在 333 那类实例上保留候选（有通过者）。")


if __name__ == "__main__":
    main()
