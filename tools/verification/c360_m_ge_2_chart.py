#!/usr/bin/env python3
"""c360 — m >= 2 的图卡参数化（用结式判"生成好"）。

对 Gr(m, R) 的仿射图卡：m×(R-m) 的符号矩阵 X，
图卡行 = comp[i] + Σ_j X[i][j] * comp[m+j]。
把“纤维生成好”化为：某对 lambda-多项式极大子式的**结式**（关于 X 的多项式）不恒为零。
"""

from __future__ import annotations

import itertools
import os
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import c335_lambda_movement as m  # noqa: E402

lam = sp.symbols("lam")


def basis(sub):
    if not sub:
        return []
    M = sp.Matrix.vstack(*[sp.Matrix(r).reshape(1, sub[0].cols) for r in sub])
    return [sp.Matrix(M.rowspace()[i]).reshape(1, sub[0].cols) for i in range(len(M.rowspace()))]


def quotient(all_basis, sub_basis, n):
    chosen = list(sub_basis)
    out = []
    for w in all_basis:
        M = sp.Matrix.vstack(*[sp.Matrix(x).reshape(1, n) for x in chosen + [w]])
        if M.rank() > len(chosen):
            chosen.append(w)
            out.append(w)
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
    out = []
    for mu in sp.roots(sp.Poly(M.charpoly(x).as_expr(), x), x):
        mu = sp.simplify(mu)
        if not mu.is_rational:
            continue
        for e in (M - mu * sp.eye(k)).nullspace():
            if r0 and not (Cons * e).is_zero_matrix:
                continue
            v = N * e
            U = [v, A * v]
            Qv = m.orth_basis(U)
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
            if verbose:
                print(f"  mu={sp.sstr(mu)}: base={len(base)}, m={mfree}, R={R}")
            if mfree == 0:
                X = []
                L = sp.Matrix.vstack(*[sp.Matrix(r).reshape(1, n) for r in base])
            else:
                syms = sp.symbols(f"X0:{mfree * (R - mfree)}")
                X = [list(syms[i * (R - mfree):(i + 1) * (R - mfree)]) for i in range(mfree)]
                rows = [sp.Matrix(r).reshape(1, n) for r in base]
                for i in range(mfree):
                    row = comp[i].copy()
                    for j in range(R - mfree):
                        row = row + X[i][j] * comp[mfree + j]
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
            good = None
            for a in range(len(polys)):
                for b in range(a + 1, len(polys)):
                    R2 = sp.resultant(polys[a], polys[b], lam)
                    R2 = sp.factor(sp.simplify(R2))
                    if R2 != 0:
                        good = (a, b)
                        break
                if good:
                    break
            out.append((sp.sstr(mu), mfree, R, good is not None))
    return out


def main() -> None:
    print("=" * 74)
    print("m >= 2 的图卡：用结式判生成好")
    print("=" * 74)
    import c352_number_field_decider as d
    A, C = d.build_instance(4242)
    L0 = sp.Matrix([[0, 0, 0, 0, 0, 1, 0, 0]])
    for q in (5, 6):
        print()
        print(f"--- L0 = e_6, q = {q} ---")
        res = chart_decide(A, C, L0, q)
        if not res:
            print("  （没有可处理的候选）")
        for mu, mfree, R, good in res:
            print(f"  mu={mu}: m={mfree}, R={R} => {'生成好（有结式非零）' if good else '所有结式为零（未判定）'}")


if __name__ == "__main__":
    main()
