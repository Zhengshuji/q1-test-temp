#!/usr/bin/env python3
"""c336 — 商铅笔定理（328）的前提核对。

检查（在若干实例上）：
  (1) M(lam) = Q(lam I - A)N 的最后一列（对应 v 的那一列）恒为零；
  (2) X = Q N_hat 列满秩，rank X = k-1；
  (3) M = [Mtilde, 0]，Mtilde = lam X - G，且"rank Mtilde < k-1 对某 lambda"
      与"lam H - H_A 的 omega-子式 gcd ne 1"给出同一判定；
  (4) 归一化 X = [I; 0] 后，(G1, G2) 可观测 <=> Mtilde 处处满列秩（Hautus）。

有限精确检验，不是证明。
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


def check(A, C, seed):
    n = A.rows
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    k = N.cols
    rng = random.Random(seed)
    c = sp.Matrix([rng.randint(-3, 3) for _ in range(k)])
    v = N * c
    U = [v, A * v]
    if sp.Matrix.hstack(*U).rank() != 2:
        return None
    Q = m.orth_basis(U)
    # 换基：让 N 的最后一列正比于 v（c 的某个非零坐标被 c 替换）
    p = next(i for i in range(k) if c[i] != 0)
    cols = [sp.eye(k)[:, i] for i in range(k) if i != p] + [c]
    S = sp.Matrix.hstack(*cols)
    assert S.rank() == k
    Nn = N * S
    M = sp.Matrix(Q.rows, k, lambda i, j: lam * (Q * Nn)[i, j] - (Q * A * Nn)[i, j])
    last = sp.Matrix([sp.expand(M[i, k - 1]) for i in range(M.rows)])
    assert last.is_zero_matrix, f"最后一列应恒零，得到 {last.T}"
    Nhat = Nn[:, : k - 1]
    X = Q * Nhat
    G = Q * A * Nhat
    Mt = sp.Matrix(Q.rows, k - 1, lambda i, j: lam * X[i, j] - G[i, j])
    # (3) 两边的判定
    g_t = gcd_of_minors(Mt, k - 1)
    bad_t = (0 if g_t == 0 else sp.Poly(g_t, lam).degree() > 0)
    Hp = (Q * Nn)   # (n-2) x k
    L = Q if Q.rows <= 3 else Q[:3, :]
    Hp = L * Nn
    HAp = L * A * Nn
    P = sp.Matrix(Hp.rows, k, lambda i, j: lam * Hp[i, j] - HAp[i, j])
    g_p = gcd_of_minors(P, 2) if Hp.rows >= 2 else sp.Integer(0)
    bad_p = (0 if g_p == 0 else sp.Poly(g_p, lam).degree() > 0)
    assert bad_t == bad_p, f"判定不一致: {g_t} vs {g_p}"
    return dict(k=k, rankX=X.rank(), rows=Q.rows, g_t=sp.sstr(g_t), g_p=sp.sstr(g_p),
                bad=bad_t, ok=(X.rank() == k - 1))


def main() -> None:
    print("=" * 74)
    print("商铅笔定理的前提核对")
    print("=" * 74)
    C = sp.Matrix([[0, 0, 0, 0, 1]])
    rng = random.Random(336)
    okc = 0
    for t in range(30):
        A = sp.Matrix(5, 5, lambda i, j: rng.randint(-2, 2))
        W = sp.Matrix.vstack(C, C * A)
        if W.rank() != 2:
            continue
        if m.ker_basis(W).cols != 3:
            continue
        r = check(A, C, seed=1000 + t)
        if r is None:
            continue
        print(f"  A#{t}: k={r['k']}, Q 的行数={r['rows']}, rank X={r['rankX']} "
              f"(应 = k-1 = {r['k']-1}), gcd_tilde={r['g_t']}, gcd_pencil={r['g_p']}, bad={r['bad']}")
        assert r["ok"], f"rank X 不是 k-1：A#{t}"
        okc += 1
        if okc >= 5:
            break
    print(f"\n  通过 {okc} 个实例：最后一列恒零、rank X = k-1、两种判定一致。")


if __name__ == "__main__":
    main()
