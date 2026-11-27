#!/usr/bin/env python3
"""c348 — 把 Bézout 证书推广到多个 n=8, p=2 实例。

对每个种子构造一个实例（结构同 341/347），在 U^⊥ 的超平面族里找一个好点，
并给出 Σ g_i f_i = 1 的精确证书。输出一张表：ω、是否找到证书、证书的次数。
"""

from __future__ import annotations

import os
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import c347_bezout_certificate as bz  # noqa: E402
import c335_lambda_movement as m  # noqa: E402

lam = sp.symbols("lam")


def run(seed: int, trial: int = 0):
    A, C = bz.build(seed=seed, trial=trial)
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
    Q = m.orth_basis([v, A * v])
    fv = (v.T * N)
    ns = sp.Matrix([[fv[0, i] for i in range(k)]]).nullspace()
    K0v = sp.Matrix.hstack(*ns)
    if K0v.cols != k - 1:
        return None
    import random
    rng = random.Random(seed * 31 + 7)
    for t in range(120):
        coeffs = [rng.randint(-2, 2) for _ in range(Q.rows)]
        x = Q.T * sp.Matrix(coeffs)
        if (N.T * x).norm() == 0:
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
        polys = bz.gcd_of_minors(P, om)
        if not polys:
            continue
        g = polys[0]
        for q in polys[1:]:
            g = sp.gcd(g, q)
        if g.degree() != 0:
            continue
        coefs, h = bz.bezout(polys)
        if coefs is None:
            continue
        total = sp.expand(sum(c * p.as_expr() for c, p in zip(coefs, polys)))
        if sp.simplify(total - 1) != 0:
            continue
        return dict(seed=seed, omega=om, nmin=len(polys), coeffs=coeffs,
                    degmax=max(sp.degree(c, lam) for c in coefs), ok=True)
    return dict(seed=seed, omega=om, ok=False)


def main() -> None:
    print("=" * 74)
    print("多实例 Bézout 证书（n=8, p=2, 富余档 n-2-p=4 > omega=3）")
    print("=" * 74)
    wins = 0
    total = 0
    for seed in (4242, 4243, 4244, 4245, 4246, 4247):
        r = run(seed)
        if r is None:
            print(f"  seed {seed}: 构造未通过（跳过）")
            continue
        total += 1
        if r["ok"]:
            wins += 1
            print(f"  seed {seed}: 证书成立（子式 {r['nmin']} 个，max deg g_i = {r['degmax']}，omega = {r['omega']}）")
        else:
            print(f"  seed {seed}: 未找到好点")
    print()
    print(f"  {wins}/{total} 个实例找到并验证了 Bézout 证书")


if __name__ == "__main__":
    main()
