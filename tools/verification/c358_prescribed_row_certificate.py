#!/usr/bin/env python3
"""c358 — 带预设行 L0 的显式证书（103 号 §7.8 的机制验证）。

给定 (A, C, L0)，找一条可行的设计 L = [L0; R]，并给出：
  - 可容许方向 v ∈ E_mu^0 = E_mu ∩ ker(L0 N) ∩ ker(L0 A N)；
  - 行空间 V = V0 + D_v + <x>（x 在 Q_v / V0_bar 里取样本）；
  - 验证 L0 ⊆ row L、(5a)、以及 (5b)（极大子式 gcd = 1）。
"""

from __future__ import annotations

import itertools
import os
import sys
from fractions import Fraction as F

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import c335_lambda_movement as m  # noqa: E402
import c352_number_field_decider as d  # noqa: E402

lam = sp.symbols("lam")


def gcd_minors(H, HA, om):
    k = H.cols
    q = H.rows
    P = sp.Matrix(q, k, lambda i, j: lam * H[i, j] - HA[i, j])
    polys = []
    for r in itertools.combinations(range(q), om):
        for c in itertools.combinations(range(k), om):
            det = sp.expand(P.extract(list(r), list(c)).det())
            if sp.simplify(det) != 0:
                polys.append(det)
    if not polys:
        return None
    gg = polys[0]
    for pp in polys[1:]:
        gg = sp.gcd(gg, pp)
    return sp.simplify(gg)


def attempt(A, C, L0, verbose=True):
    n = A.rows
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    k = N.cols
    om = k - 1
    G = N.T * N
    M = G.inv() * (N.T * A * N)
    r0 = L0.rows if L0 is not None else 0
    V0 = L0 if r0 else sp.zeros(0, n)
    # E_mu^0：ker(L0 N) ∩ ker(L0 A N) 限制下的特征空间
    LN = V0 * N if r0 else sp.zeros(0, k)
    LAN = V0 * A * N if r0 else sp.zeros(0, k)
    K0v = sp.Matrix.vstack(LN, LAN) if r0 else sp.zeros(0, k)
    x = sp.symbols("x")
    cp = sp.factor(M.charpoly(x).as_expr())
    if verbose:
        print(f"  k={k}, omega={om}, r0={r0}")
        print(f"  charpoly(M) = {cp}")
        print(f"  预设行的约束矩阵 [L0N; L0AN] 秩 = {K0v.rank() if r0 else 0}")
    roots = sp.roots(sp.Poly(M.charpoly(x).as_expr(), x), x)
    found = []
    for mu in roots:
        mu = sp.simplify(mu)
        # 只处理有理特征值（无理的要走数域，见 c352/c355）
        if not mu.is_rational:
            continue
        E = (M - mu * sp.eye(k)).nullspace()
        if not E:
            continue
        # 在 E 里找满足预设行约束的方向
        cands = []
        for e in E:
            if r0 == 0:
                cands.append(e)
                continue
            if (K0v * e).is_zero_matrix:
                cands.append(e)
        if verbose:
            print(f"  mu={sp.sstr(mu)}: dimE={len(E)}, 满足预设行的方向数={len(cands)}")
        for c in cands:
            v = N * c
            if sp.Matrix.hstack(v, A * v).rank() < 1:
                continue
            U = sp.Matrix.hstack(v, A * v)
            Qv = m.orth_basis([col for col in [v, A * v]])  # U^perp 的基
            # D_v = K0 ∩ U^perp（K 坐标下由 v·N, Av·N 的零空间给）
            fv = (v.T * N)
            fa = (A * v).T * N
            Dv = sp.Matrix.hstack(*sp.Matrix.vstack(fv, fa).nullspace()) if sp.Matrix.vstack(fv, fa).nullspace() else sp.zeros(k, 0)
            if Dv.cols != om:
                continue
            Dv_amb = [N * Dv[:, j] for j in range(Dv.cols)]
            # V = V0 + D_v + <free>（free 取 Q_v 里的方向）
            base = [V0.row(i) for i in range(r0)] if r0 else []
            base += [d.T for d in Dv_amb] if False else [w for w in Dv_amb]
            # 去重取基
            cur = sp.Matrix.vstack(*[b.reshape(1, n) for b in base]) if base else sp.zeros(0, n)
            if cur.rows and cur.rank() < cur.rows:
                cur = sp.Matrix.vstack(*cur.rowspace())
            # 需要的总行数 q = k（本模式）
            q = k
            need = q - cur.rows
            if need < 0:
                continue
            rows = [cur.row(i) for i in range(cur.rows)]
            for j in range(Qv.rows):
                if len(rows) >= q:
                    break
                cand = Qv.row(j)
                test = sp.Matrix.vstack(*[r.reshape(1, n) for r in rows] + [cand.reshape(1, n)])
                if test.rank() > len(rows):
                    rows.append(cand)
            if len(rows) != q:
                continue
            L = sp.Matrix.vstack(*[r.reshape(1, n) for r in rows])
            H = L * N
            HA = L * A * N
            if H.rank() != om:
                continue
            if not (HA * m.ker_basis(H)).is_zero_matrix:
                continue
            g = gcd_minors(H, HA, om)
            if g is None:
                continue
            if sp.degree(g, lam) == 0:
                found.append((mu, c, L))
    return found


def main() -> None:
    print("=" * 74)
    print("带预设行 L0 的显式证书")
    print("=" * 74)
    A, C = d.build_instance(4242)
    n = A.rows

    print()
    print("情形 1：L0 = 全 1 行")
    L0a = sp.Matrix([[1] * n])
    res = attempt(A, C, L0a)
    if res:
        mu, c, L = res[0]
        print("  找到可行设计：mu =", sp.sstr(mu), "；L =", L.tolist())
    else:
        print("  未找到 —— 若所有 E_mu^0 都为零，则这是**不可行证书**（见上：满足预设行的方向数=0）")

    print()
    print("情形 2：L0 取 U_v^perp 里一行，但**不**落在 K0^perp（能进入铅笔）")
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    v = N * sp.Matrix([1, 0, 0, 0])
    Qv = m.orth_basis([v, A * v])
    picked = None
    import itertools as _it
    for r in range(1, Qv.rows + 1):
        for combo in _it.combinations(range(Qv.rows), r):
            cand = sum((Qv.row(i) for i in combo), sp.zeros(1, n))
            if (cand * N).norm() != 0:      # 不落在 K0^perp
                picked = cand
                break
        if picked is not None:
            break
    if picked is None:
        print("  找不到合适的 L0")
        return
    L0b = picked
    print("  L0 =", L0b.tolist(), "  (L0 N ≠ 0:", (L0b * N).norm() != 0, ")")
    res2 = attempt(A, C, L0b)
    if res2:
        mu, c, L = res2[0]
        print()
        print("  找到可行设计（证书）：")
        print("    mu =", sp.sstr(mu))
        print("    L =", L.tolist())
        print("    （已验证 L0 ⊆ row L、(5a)、(5b) gcd = 1）")
    else:
        print("  未找到")


if __name__ == "__main__":
    main()
