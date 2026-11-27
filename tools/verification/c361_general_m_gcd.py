#!/usr/bin/env python3
"""c361 — 任意 m 的图卡 + 多变量 gcd（双向判定）。

对 Gr(m, R) 的图卡（X 为 m×(R-m) 符号矩阵）构造 L(X)，把铅笔子式转成
"系数为有理函数"的 lambda-多项式，做 K(X)[lambda] 上的 gcd：
  deg = 0 => 生成好；> 0 => 该图卡全坏。
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
import c354_generic_gcd_nf as g  # noqa: E402
import c355_rf_gcd as rf  # noqa: E402
from nf import NF  # noqa: E402

lam = sp.symbols("lam")


def basis(sub, n):
    if not sub:
        return []
    M = sp.Matrix.vstack(*[sp.Matrix(r).reshape(1, n) for r in sub])
    return [sp.Matrix(M.rowspace()[i]).reshape(1, n) for i in range(len(M.rowspace()))]


def quotient(all_basis, sub_basis, n):
    chosen = list(sub_basis)
    out = []
    for w in all_basis:
        M = sp.Matrix.vstack(*[sp.Matrix(x).reshape(1, n) for x in chosen + [w]])
        if M.rank() > len(chosen):
            chosen.append(w)
            out.append(w)
    return out


def poly_to_dicts(expr, Xs, Fq):
    """把 lambda-多项式（系数是 X 的多项式）转成 [dict(低次在前)]。"""
    P = sp.Poly(sp.expand(expr), lam)
    coeffs = P.all_coeffs()          # 高次 -> 低次
    out = []
    for c in reversed(coeffs):       # 低次在前
        if sp.simplify(c) == 0:
            out.append({})
            continue
        Q = sp.Poly(sp.expand(c), *Xs) if Xs else sp.Poly(sp.expand(c), lam)
        d = {}
        if Xs:
            for exps, val in zip(Q.monoms(), Q.coeffs()):
                r = sp.Rational(val)
                d[tuple(int(e) for e in exps)] = Fq.elt(F(r.p, r.q))
        else:
            r = sp.Rational(c)
            d[()] = Fq.elt(F(r.p, r.q))
        out.append(d)
    return out


def chart_decide(A, C, L0, q, verbose=True):
    n = A.rows
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    k = N.cols
    om = k - 1
    G = N.T * N
    M = G.inv() * (N.T * A * N)
    r0 = L0.rows if L0 is not None else 0
    V0 = [sp.Matrix(L0.row(i)).reshape(1, n) for i in range(r0)] if r0 else []
    Cons = sp.Matrix.vstack(L0 * N, L0 * A * N) if r0 else sp.zeros(0, k)
    x = sp.symbols("x")
    Fq = NF([-1, 1])          # 只处理有理根：域为 Q（mu=1）
    rf.Fq_one = (Fq,)
    out = []
    for mu in sp.roots(sp.Poly(M.charpoly(x).as_expr(), x), x):
        mu = sp.simplify(mu)
        if not mu.is_rational:
            continue
        for e in (M - mu * sp.eye(k)).nullspace():
            if r0 and not (Cons * e).is_zero_matrix:
                continue
            v = N * e
            Qv = m.orth_basis([v, A * v])
            all_basis = [sp.Matrix(Qv.row(i)).reshape(1, n) for i in range(Qv.rows)]
            Msys = sp.Matrix.vstack((v.T * N), ((A * v).T * N))
            Dv = [sp.Matrix(N * col).reshape(1, n) for col in Msys.nullspace()]
            if len(Dv) != om:
                continue
            V0red = quotient(V0, Dv, n) if V0 else []
            base = Dv + V0red
            comp = quotient(all_basis, base, n)
            mfree = q - len(base)
            R = len(comp)
            if mfree < 0 or mfree > R:
                continue
            nvars = mfree * (R - mfree)
            if mfree == 0:
                Xs = []
                L = sp.Matrix.vstack(*[sp.Matrix(r).reshape(1, n) for r in base])
            else:
                Xs = sp.symbols(f"X0:{nvars}")
                rows = [sp.Matrix(r).reshape(1, n) for r in base]
                for i in range(mfree):
                    row = comp[i].copy()
                    for j in range(R - mfree):
                        row = row + Xs[i * (R - mfree) + j] * comp[mfree + j]
                    rows.append(row)
                L = sp.Matrix.vstack(*rows)
            H = L * N
            if H.rank() != om:
                continue
            HA = L * A * N
            KH = H.nullspace()
            if KH and not all((HA * kv).is_zero_matrix for kv in KH):
                continue
            P = sp.Matrix(L.rows, k, lambda i, j: lam * H[i, j] - HA[i, j])
            polys = []
            for rs in itertools.combinations(range(L.rows), om):
                for cs in itertools.combinations(range(k), om):
                    det = sp.expand(P.extract(list(rs), list(cs)).det())
                    if sp.simplify(det) != 0:
                        polys.append(det)
            if not polys:
                continue
            if verbose:
                print(f"  mu={sp.sstr(mu)}: m={mfree}, R={R}, 变量数={nvars}, 子式={len(polys)}")
            if nvars > 0:
                g.NV = nvars
            else:
                g.NV = 0
            try:
                Pdicts = [poly_to_dicts(pp, Xs, Fq) for pp in polys]
                Prf = [[rf.RF(c) for c in pd] for pd in Pdicts]
                Prf = [rf.poly_trim_rf(Q) for Q in Prf]
                Prf = [Q for Q in Prf if rf.poly_deg_rf(Q) >= 0]
                gg = Prf[0]
                for Q in Prf[1:]:
                    gg = rf.poly_gcd_rf(gg, Q)
                    if rf.poly_deg_rf(gg) == 0:
                        break
                dg = rf.poly_deg_rf(gg)
            except Exception as ex:
                out.append((sp.sstr(mu), mfree, R, f"异常: {ex}"))
                continue
            out.append((sp.sstr(mu), mfree, R, "生成好" if dg == 0 else f"全坏（次数 {dg}）"))
    return out


def main() -> None:
    print("=" * 74)
    print("任意 m 的图卡 + 多变量 gcd")
    print("=" * 74)
    import c352_number_field_decider as d
    A, C = d.build_instance(4242)
    L0 = sp.Matrix([[0, 0, 0, 0, 0, 1, 0, 0]])
    for q in (4, 5, 6):
        print()
        print(f"--- L0 = e_6, q = {q} ---")
        for mu, mfree, R, verdict in chart_decide(A, C, L0, q):
            print(f"  mu={mu}: m={mfree}, R={R} => {verdict}")


if __name__ == "__main__":
    main()
