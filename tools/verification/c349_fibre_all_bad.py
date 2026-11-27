#!/usr/bin/env python3
"""c349 — 把"120 个候选全坏"升级为"整条纤维全坏"。

对 seed 4245 / 4246 的实例，固定非特征 v，纤维参数化：
  V = (K0 ∩ v^⊥) ⊕ <x>，x ∈ U^⊥/(K0 ∩ v^⊥) —— 3 维商空间，x 用符号 c=(c1,c2,c3) 表示。
在该参数族上算 λH − H_A 的 ω×ω 极大子式的 gcd（在 Q(c)[λ] 上）。
若 gcd ≠ 1，则由"坏集闭 + 纤维不可约"得**整条纤维全坏**（不是采样结论）。
"""

from __future__ import annotations

import itertools
import os
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import c347_bezout_certificate as bz  # noqa: E402
import c335_lambda_movement as m  # noqa: E402

lam = sp.symbols("lam")
c1, c2, c3 = sp.symbols("c1 c2 c3")


def fibre_gcd(seed: int):
    A, C = bz.build(seed=seed)
    n = A.rows
    W = sp.Matrix.vstack(C, C * A)
    if W.rank() != 4:
        return None
    N = m.ker_basis(W)
    k = N.cols
    om = k - 1
    v = N * sp.Matrix([1] + [0] * (k - 1))
    if sp.Matrix.hstack(v, A * v).rank() != 2:
        return None
    Q = m.orth_basis([v, A * v])          # U^⊥ 的基（n-2 行）
    # K0 ∩ v^⊥ 的基（3 行）
    fv = (v.T * N)
    ns = sp.Matrix([[fv[0, i] for i in range(k)]]).nullspace()
    K0v = sp.Matrix.hstack(*ns)            # k × (k-1)，在 K 坐标
    W0 = [N * K0v[:, j] for j in range(k - 1)]   # 3 个环境向量
    if len(W0) != om:
        return None
    # 商空间：把 Q 的行对 W0 张成的空间投影，取补方向
    Wmat = sp.Matrix.hstack(*[w for w in W0])          # n × 3
    # 在 Q 的坐标系里：Q^T? 用最小二乘找与 W0 线性独立的方向
    basis = Wmat.columnspace()
    cand = []
    for i in range(Q.rows):
        cand.append(Q.row(i).T)
    # 逐个挑，凑够 3 个与 W0 独立的方向
    sel = []
    cur = sp.Matrix.hstack(*basis) if basis else sp.zeros(n, 0)
    for xv in cand:
        test = sp.Matrix.hstack(cur, xv)
        if test.rank() > cur.cols:
            cur = test
            sel.append(xv)
        if len(sel) == 3:
            break
    if len(sel) != 3:
        return None
    x = sel[0] * c1 + sel[1] * c2 + sel[2] * c3
    L = sp.Matrix.vstack(*[w.reshape(1, n) for w in W0], x.reshape(1, n))
    H = L * N
    HA = L * A * N
    P = sp.Matrix(L.rows, k, lambda i, j: lam * H[i, j] - HA[i, j])
    polys = []
    for rows in itertools.combinations(range(P.rows), om):
        for cols in itertools.combinations(range(P.cols), om):
            d = sp.expand(P.extract(list(rows), list(cols)).det())
            if sp.simplify(d) != 0:
                polys.append(d)
    if not polys:
        return None
    g = polys[0]
    for q in polys[1:]:
        g = sp.gcd(g, q)
    return sp.factor(sp.simplify(g)), len(polys)


def main() -> None:
    print("=" * 74)
    print("整条纤维全坏？——在 P^2 参数族上算 generic gcd")
    print("=" * 74)
    for seed in (4245, 4246, 4242):
        r = fibre_gcd(seed)
        if r is None:
            print(f"  seed {seed}: 构造失败（跳过）")
            continue
        g, npolys = r
        deg = sp.degree(g, lam) if g != 0 else -1
        print(f"  seed {seed}: 非零子式 {npolys} 个；gcd = {g}（lambda 次数 {deg}）")


if __name__ == "__main__":
    main()
