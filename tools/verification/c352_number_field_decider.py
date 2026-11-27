#!/usr/bin/env python3
"""c352 — 数域上的纤维判定（只求 YES：找到一个好点即可）。

流程：压缩 M → 特征多项式分解 → 对每个特征值 mu（代数数）：
  1. c in ker(M - mu I)，v = N c；
  2. v 非特征？；
  3. 纤维里取若干**有理** c-样本（x 的系数），算 lambda H - H_A 的 omega-子式 gcd；
     在 Q(mu)[lam] 上为 1 ⟹ 该纤维生成好 ⟹ 实例可行（Theorem 2）。

只要有一个 mu 的某个样本 gcd = 1，就输出 feasible=True 与见证。
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
c1, c2, c3 = sp.symbols("c1 c2 c3")


def build_instance(seed: int, n: int = 8, mu0: int = 1):
    """与 341/347 相同的构造。"""
    rng = random.Random(seed)
    p = 2
    C = sp.zeros(p, n)
    C[0, 0] = 1
    C[1, 1] = 1
    A = sp.zeros(n, n)
    A[0, 2] = 1
    A[1, 3] = 1
    for j in range(n):
        A[2, j] = rng.randint(-2, 2)
        A[3, j] = rng.randint(-2, 2)
    k = n - 4
    B = sp.Matrix(k, k, lambda i, j: rng.randint(-2, 2))
    for i in range(k):
        B[i, 0] = mu0 if i == 0 else 0
    for i in range(k):
        for j in range(k):
            A[4 + i, 4 + j] = B[i, j]
    return A, C


def fibre_gcd_at(A, N, v, coeffs):
    """在给定 v 与有理 x-样本处，返回 pencil 的 omega-子式 gcd。"""
    n = A.rows
    k = N.cols
    om = k - 1
    Q = m.orth_basis([v, A * v])
    fv = (v.T * N)
    ns = sp.Matrix([[fv[0, i] for i in range(k)]]).nullspace()
    K0v = sp.Matrix.hstack(*ns)
    if K0v.cols != om:
        return None
    W0 = [N * K0v[:, j] for j in range(om)]
    Wmat = sp.Matrix.hstack(*W0)
    cur = Wmat
    sel = []
    for i in range(Q.rows):
        xv = Q.row(i).T
        if sp.Matrix.hstack(cur, xv).rank() > cur.cols:
            cur = sp.Matrix.hstack(cur, xv)
            sel.append(xv)
        if len(sel) == 3:
            break
    if len(sel) < 1:
        return None
    x = sum((sp.simplify(sel[j] * coeffs[j]) for j in range(min(3, len(sel)))), sp.zeros(n, 1))
    L = sp.Matrix.vstack(*[w.reshape(1, n) for w in W0], x.reshape(1, n))
    H = L * N
    if H.rank() != om:
        return None
    HA = L * A * N
    if not (HA * m.ker_basis(H)).is_zero_matrix:
        return None
    P = sp.Matrix(L.rows, k, lambda i, j: lam * H[i, j] - HA[i, j])
    polys = []
    for r in itertools.combinations(range(P.rows), om):
        for cc in itertools.combinations(range(P.cols), om):
            d = sp.expand(P.extract(list(r), list(cc)).det())
            if sp.simplify(d) != 0:
                polys.append(d)
    if not polys:
        return None
    g = polys[0]
    for q in polys[1:]:
        g = sp.gcd(g, q)
    return sp.simplify(g)


def decide(seed: int, samples=3):
    A, C = build_instance(seed)
    n = A.rows
    W = sp.Matrix.vstack(C, C * A)
    if W.rank() != 4:
        return None
    N = m.ker_basis(W)
    k = N.cols
    G = N.T * N
    M = G.inv() * (N.T * A * N)
    x = sp.symbols("x")
    cp = sp.Poly(M.charpoly(x).as_expr(), x)
    facs = sp.factor_list(cp.as_expr())[1]
    rng = random.Random(seed + 5)
    for f, mult in facs:
        fp = sp.Poly(f, x)
        if fp.degree() < 1:
            continue
        roots = sp.roots(fp, x)
        for mu in roots:
            mu = sp.simplify(mu)
            try:
                ns = (M - mu * sp.eye(k)).nullspace()
            except Exception:
                continue
            if not ns:
                continue
            v = sp.simplify(N * ns[0])
            if sp.Matrix.hstack(v, A * v).rank() != 2:
                continue          # 特征方向，另有处理
            for _ in range(samples):
                cc = [rng.randint(-2, 2) for _ in range(3)]
                g = fibre_gcd_at(A, N, v, cc)
                if g is None:
                    continue
                if sp.degree(g, lam) == 0:
                    return dict(seed=seed, mu=sp.sstr(mu), v=sp.sstr(sp.Matrix(v).T),
                                coeffs=cc, feasible=True)
    return dict(seed=seed, feasible=False)


def main() -> None:
    print("=" * 74)
    print("数域上的纤维判定（只求 YES）")
    print("=" * 74)
    for seed in (4246, 4242, 4245):
        r = decide(seed)
        if r is None:
            print(f"  seed {seed}: 构造失败")
        elif r.get("feasible"):
            print(f"  seed {seed}: **可行**（mu = {r['mu']}, x-样本 {r['coeffs']}）")
        else:
            print(f"  seed {seed}: 未找到好点（不构成不可行结论）")


if __name__ == "__main__":
    main()
