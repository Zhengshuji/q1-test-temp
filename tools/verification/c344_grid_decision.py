#!/usr/bin/env python3
"""c344 — 网格判定（第一级零频 + 第二级结式/gcd）的机器证据。

参数化：特征纤维里 V 是 v^perp 的超平面，V = {x in v^perp : n·x = 0}，n 取整数格点。
对每个 n：
  1. 行空间 V 的基（q = n_dim - 2 行）；
  2. 第一级：rank H = omega 且 rank H_A = omega（零频）；
  3. 第二级：lambda H - H_A 的 omega x omega 子式 gcd 是否为 1。
判定：存在格点通过两级 ⟺ 可行；全部不通过 ⟹ 不可行（Schwartz-Zippel 保证，若网格足够大）。

实例：
  (A1,C1)：336 的反例（应：无格点通过）
  (A2,C2)：333 的好实例（应：有格点通过）
"""

from __future__ import annotations

import itertools
import os
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
if os.path.join(_ROOT, "tools/verification") not in sys.path:
    sys.path.insert(0, os.path.join(_ROOT, "tools/verification"))

import c335_lambda_movement as m  # noqa: E402

lam = sp.symbols("lam")


def gcd_of_minors(P, r):
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


def basis_of_hyperplane(v, n_vec):
    """v^perp 里满足 n·x = 0 的超平面的一组基（行向量），n 用 Q 坐标给出。"""
    Q = m.orth_basis([v])                  # Q.rows x n，行张成 v^perp
    f = sp.Matrix([[n_vec[i] for i in range(Q.rows)]])   # 1 x Q.rows
    ns = f.nullspace()                     # {c in C^{Q.rows} : c·n = 0} 的基
    if not ns:
        return None
    rows = [(Q.T * c).T for c in ns]       # 映回环境空间，每个 1 x n
    return sp.Matrix.vstack(*[r.reshape(1, Q.cols) for r in rows])


def decide(A, C, v, grid_range=2):
    n = A.rows
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    k = N.cols
    om = k - 1
    Q = m.orth_basis([v])
    good_points = []
    level1_pass = 0
    for coeffs in itertools.product(range(-grid_range, grid_range + 1), repeat=Q.rows):
        if all(c == 0 for c in coeffs):
            continue
        if coeffs[0] < 0:                    # 去掉 ± 重复
            continue
        L = basis_of_hyperplane(v, coeffs)
        if L is None:
            continue
        H = L * N
        if H.rank() != om:
            continue
        HA = L * A * N
        if HA.rank() != om:                  # 第一级：零频
            continue
        level1_pass += 1
        P = sp.Matrix(L.rows, k, lambda i, j: lam * H[i, j] - HA[i, j])
        g = gcd_of_minors(P, om)             # 第二级
        if g != 0 and sp.Poly(g, lam).degree() == 0:
            good_points.append(coeffs)
    return good_points, level1_pass


def main() -> None:
    print("=" * 74)
    print("网格判定：零频筛 + gcd（n=5 模式，超平面参数，整数格点）")
    print("=" * 74)
    C = sp.Matrix([[0, 0, 0, 0, 1]])
    v = sp.Matrix([1, 0, 0, 0, 0])

    A1 = sp.Matrix([[2, 2, -1, 0, 0],
                    [0, -2, 1, 0, 1],
                    [0, 1, -2, 0, -1],
                    [0, 0, 0, 0, 2],
                    [0, -1, 2, 0, -1]])
    good1, l1 = decide(A1, C, v)
    print(f"  反例 336：零频通过 {l1} 个，两级通过 {len(good1)} 个  -> 判定 {'可行' if good1 else '不可行'}")
    assert not good1

    A2 = sp.Matrix([[2, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1],
                    [0, 3, 5, 7, 11]])
    good2, l2 = decide(A2, C, v)
    print(f"  好实例 333：零频通过 {l2} 个，两级通过 {len(good2)} 个  -> 判定 {'可行' if good2 else '不可行'}")
    assert good2
    print(f"    见证（超平面法向的坐标）: {good2[0]}")


if __name__ == "__main__":
    main()
