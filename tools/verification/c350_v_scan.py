#!/usr/bin/env python3
"""c350 — v-扫描（**注意：随机 v 大多不可容许**，见 attempts/350）。

对给定实例，在 B°（非特征 v ∈ K0）里随机取若干 v，
对每个 v 在纤维里随机取若干 x，检验那一点是否好（零频 + gcd = 1）。

**结论（由 attempts/350 解释）**：可容许的 v 必须是压缩矩阵 M 的特征向量；
随机 v 连层点都没有（本脚本的 "tested 0" 就是这个现象）。
正确做法：只在 M 的特征向量上扫描。
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

import c347_bezout_certificate as bz  # noqa: E402
import c335_lambda_movement as m  # noqa: E402

lam = sp.symbols("lam")


def scan_v(seed: int, nv=6, nx=8, rng_seed=99):
    A, C = bz.build(seed=seed)
    n = A.rows
    W = sp.Matrix.vstack(C, C * A)
    if W.rank() != 4:
        return None
    N = m.ker_basis(W)
    k = N.cols
    om = k - 1
    rng = random.Random(rng_seed + seed)
    rows = []
    for _ in range(nv):
        coeff = sp.Matrix([rng.randint(-2, 2) for _ in range(k)])
        if coeff.norm() == 0:
            continue
        v = N * coeff
        U = sp.Matrix.hstack(v, A * v)
        if U.rank() != 2:
            continue
        Q = m.orth_basis([v, A * v])
        fv = (v.T * N)
        ns = sp.Matrix([[fv[0, i] for i in range(k)]]).nullspace()
        K0v = sp.Matrix.hstack(*ns)
        if K0v.cols != om:
            continue
        good = 0
        tested = 0
        for _ in range(nx):
            cc = [rng.randint(-2, 2) for _ in range(Q.rows)]
            x = Q.T * sp.Matrix(cc)
            if (N.T * x).norm() == 0:
                continue
            L = sp.Matrix.vstack(*[(N * K0v[:, j]).reshape(1, n) for j in range(om)],
                                 x.reshape(1, n))
            H = L * N
            if H.rank() != om:
                continue
            HA = L * A * N
            if not (HA * m.ker_basis(H)).is_zero_matrix:
                continue
            tested += 1
            P = sp.Matrix(L.rows, k, lambda i, j: lam * H[i, j] - HA[i, j])
            polys = bz.gcd_of_minors(P, om)
            if not polys:
                continue
            g = polys[0]
            for q in polys[1:]:
                g = sp.gcd(g, q)
            if g.degree() == 0:
                good += 1
        rows.append((tuple(coeff), tested, good))
    return rows


def main() -> None:
    print("=" * 74)
    print("v-扫描：随机取核方向 v，看其纤维里有没有好点")
    print("=" * 74)
    for seed in (4242, 4245, 4246):
        rows = scan_v(seed)
        if rows is None:
            print(f"  seed {seed}: 构造失败")
            continue
        tot_v = len(rows)
        good_v = sum(1 for _, t, g in rows if g > 0)
        print(f"  seed {seed}: {tot_v} 个 v；其中 {good_v} 个 v 的纤维里找到好点")
        for c, t, g in rows:
            print(f"      v={c}: 测试 {t} 点，好 {g} 个")


if __name__ == "__main__":
    main()
