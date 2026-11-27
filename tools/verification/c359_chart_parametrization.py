#!/usr/bin/env python3
"""c359 — 带图卡参数化的纤维判定（Gr(s-delta, Q_v / V0_bar) 的仿射图卡）。

给定 (A, C, L0, q)：
  1. 每个实（先做有理）特征值 mu、每个可容许方向 v ∈ E_mu^0；
  2. 构造 D_v、V0 的像、以及 Q_v/(V0+Dv) 的一组补方向；
  3. 对 Grassmannian Gr(m, R)（m = s-delta, R = r(v)-delta）的每个图卡，
     以符号 X（m×(R-m)）参数化，得到 L(X)；
  4. 算 lambda H - H_A 的 omega-子式的 gcd（在 K(X)[lambda] 上，X 为符号）；
  5. gcd = 1 => 该图卡生成好（可行）；否则该图卡全坏。

本脚本先支持 m = 0（单点）与 m = 1（P^{R-1}）两种情形。
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

lam = sp.symbols("lam")


def basis_of_subspace(rows, n):
    if not rows:
        return []
    M = sp.Matrix.vstack(*[sp.Matrix(r).reshape(1, n) for r in rows])
    return [sp.Matrix(M.rowspace()[i]).reshape(1, n) for i in range(len(M.rowspace()))]


def quotient_basis(all_basis, sub_basis, n):
    """在 all_basis 张成的空间里，给出模 sub_basis 的一组补方向。"""
    chosen = list(sub_basis)
    out = []
    for w in all_basis:
        test = chosen + [w]
        M = sp.Matrix.vstack(*[sp.Matrix(x).reshape(1, n) for x in test])
        if M.rank() > len(chosen):
            chosen.append(w)
            out.append(w)
    return out


def fibre_gcd_certificate(A, C, L0, q, verbose=True):
    n = A.rows
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    k = N.cols
    om = k - 1
    G = N.T * N
    M = G.inv() * (N.T * A * N)
    r0 = L0.rows if L0 is not None else 0
    V0 = [sp.Matrix(L0.row(i)).reshape(1, n) for i in range(r0)] if r0 else []
    LN = L0 * N if r0 else sp.zeros(0, k)
    LAN = L0 * A * N if r0 else sp.zeros(0, k)
    Cons = sp.Matrix.vstack(LN, LAN) if r0 else sp.zeros(0, k)
    x = sp.symbols("x")
    roots = sp.roots(sp.Poly(M.charpoly(x).as_expr(), x), x)
    results = []
    for mu in roots:
        mu = sp.simplify(mu)
        if not mu.is_rational:
            continue
        E = (M - mu * sp.eye(k)).nullspace()
        for e in E:
            if r0 and not (Cons * e).is_zero_matrix:
                continue
            v = N * e
            U = [v, A * v]
            dimU = sp.Matrix.hstack(*U).rank()
            Qv_rows = m.orth_basis(U)                  # U^perp 的基（行）
            all_basis = [sp.Matrix(Qv_rows.row(i)).reshape(1, n) for i in range(Qv_rows.rows)]
            # D_v = K0 ∩ U^perp
            Msys = sp.Matrix.vstack((v.T * N), ((A * v).T * N))
            DvK = Msys.nullspace()
            Dv = [sp.Matrix(N * col).reshape(1, n) for col in DvK]
            if len(Dv) != om:
                continue
            # V0 模 D_v
            V0red = quotient_basis(V0, Dv, n) if V0 else []
            delta = len(V0red)
            base = Dv + V0red
            R_rows = quotient_basis(all_basis, base, n)
            R = len(R_rows)
            m_free = q - len(base)
            if m_free < 0 or m_free > R:
                if verbose:
                    print(f"  mu={sp.sstr(mu)}: 维数不合（需 {q} 行，基 {len(base)}，补 {R}）——跳过")
                continue
            if m_free > 1:
                if verbose:
                    print(f"  mu={sp.sstr(mu)}: m={m_free} > 1，本脚本未实现图卡")
                continue
            if m_free == 0:
                L = sp.Matrix.vstack(*[sp.Matrix(r).reshape(1, n) for r in base])
                cand = [(None, L)]
            else:
                # m_free == 1：图卡参数 t_j，行 = R_rows[0] + sum t_j R_rows[1+j]
                t = sp.symbols(f"t0:{R-1}") if R > 1 else ()
                row = R_rows[0]
                for j in range(R - 1):
                    row = row + t[j] * R_rows[1 + j]
                L = sp.Matrix.vstack(*[sp.Matrix(r).reshape(1, n) for r in base] + [row])
                cand = [(t, L)]
            for tvars, Lx in cand:
                H = Lx * N
                if H.rank() != om:
                    continue
                HA = Lx * A * N
                KH = H.nullspace()
                if KH and not all((HA * kv).is_zero_matrix for kv in KH):
                    continue
                P = sp.Matrix(Lx.rows, k, lambda i, j: lam * H[i, j] - HA[i, j])
                polys = []
                for rs in itertools.combinations(range(Lx.rows), om):
                    for cs in itertools.combinations(range(k), om):
                        det = sp.expand(P.extract(list(rs), list(cs)).det())
                        if sp.simplify(det) != 0:
                            polys.append(det)
                if not polys:
                    continue
                if tvars:
                    # 符号 t 的 gcd：用 c355 的 RF 机制（这里简化：用 sympy 的 gcd）
                    gg = polys[0]
                    for pp in polys[1:]:
                        gg = sp.gcd(gg, pp)
                    results.append(("symbolic", sp.sstr(mu), sp.sstr(sp.factor(gg))))
                else:
                    gg = polys[0]
                    for pp in polys[1:]:
                        gg = sp.gcd(gg, pp)
                    results.append(("point", sp.sstr(mu), sp.sstr(sp.simplify(gg))))
    return results


def main() -> None:
    print("=" * 74)
    print("图卡参数化的纤维判定（m = 0 单点 / m = 1 直线）")
    print("=" * 74)
    import c352_number_field_decider as d
    A, C = d.build_instance(4242)
    n = A.rows
    L0 = sp.Matrix([[0, 0, 0, 0, 0, 1, 0, 0]])   # e_6
    for q in (4, 5):
        print()
        print(f"--- L0 = e_6, q = {q} ---")
        res = fibre_gcd_certificate(A, C, L0, q)
        for kind, mu, gg in res:
            print(f"  [{kind}] mu={mu}: gcd = {gg}")
        if not res:
            print("  （没有可处理的候选）")


if __name__ == "__main__":
    main()
