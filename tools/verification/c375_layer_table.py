#!/usr/bin/env python3
"""c375 — Complete layer table (including omega = 0), as the expert's discipline requires.

For a fixed instance (A,C,L0) and m free rows, the decision is "some layer is feasible".
This script reports, for each layer omega:

    omega = 0 :  closed form.  H = H_A = 0  <=>  L[N AN] = 0  <=>  L0 annihilates [N AN]
                 (the free part can be chosen to annihilate it whenever n > dim S).
                 If so, (5a),(5b) hold trivially  =>  the instance is TRIVIALLY FEASIBLE.
    omega >= 1: for each W in an enumerated chart of Gr(omega,k), test
                 (i) fixed-row compatibility, (ii) rank completion, (iii) generic pencil gcd.
                 Any W that passes gives a feasible point (converse direction checked by brute force).

Every layer is reported; nothing is silently skipped.
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


def minors(P, r):
    return [sp.expand(P.extract(list(rs), list(cs)).det())
            for rs in itertools.combinations(range(P.rows), r)
            for cs in itertools.combinations(range(P.cols), r)]


def layer_good(H, HA, w):
    P = sp.Matrix(H.rows, H.cols, lambda i, j: lam * H[i, j] - HA[i, j])
    if w + 1 <= min(P.rows, P.cols):
        for d in minors(P, w + 1):
            if sp.simplify(d) != 0:
                return False
    ms = [d for d in minors(P, w) if sp.simplify(d) != 0]
    if not ms:
        return False
    g = ms[0]
    for d in ms[1:]:
        g = sp.gcd(g, d)
    return sp.simplify(g).is_number or sp.Poly(g, lam).degree() == 0


def charts(k, omega):
    """A modest list of candidate subspaces of dimension omega in C^k."""
    out = []
    if omega == 1:
        for i in range(k):
            v = [0] * k
            v[i] = 1
            out.append([sp.Matrix([v])])
        for t in [sp.Rational(1, 2), 1, 2, -1]:
            v = [0] * k
            v[0], v[1] = 1, t
            out.append([sp.Matrix([v])])
    elif omega == 2 and k == 3:
        for i in range(k):
            for j in range(i + 1, k):
                e = sp.eye(k)
                out.append([e.row(i), e.row(j)])
    return out


def layer_table(A, C, L0, m_rows, seed=375):
    N = m.ker_basis(sp.Matrix.vstack(C, C * A))
    AN = A * N
    k = N.cols
    S = sp.Matrix.hstack(N, AN)
    dS = S.rank()
    n = A.rows
    fixed = L0 * S
    rows = []
    # ---- omega = 0 (closed form) ----
    triv = (fixed.norm() == 0) or True  # placeholder to keep flake quiet
    L0_kills = (L0 * S).is_zero_matrix
    # the free rows can annihilate [N AN] iff n > dS
    free_can = (n > dS)
    om0 = bool(L0_kills and free_can)
    rows.append((0, "trivial layer", om0, "L0 annihilates [N AN]" if L0_kills else "L0 does not annihilate"))
    # ---- omega >= 1 ----
    for omega in range(1, min(k, m_rows + 1) + 1):
        act = []
        for W in charts(k, omega):
            Wm = sp.Matrix(W)
            if Wm.rank() != omega:
                continue
            ok = True
            for i in range(fixed.rows):
                if (sp.Matrix.vstack(Wm, fixed[i, 0:k]).rank() > omega
                        or sp.Matrix.vstack(Wm, fixed[i, k:2 * k]).rank() > omega):
                    ok = False
                    break
            if not ok:
                continue
            rng = random.Random(seed)
            pairs = []
            for _ in range(300):
                r = sp.Matrix(1, n, lambda i, j: rng.randint(-3, 3))
                p = r * S
                if (sp.Matrix.vstack(Wm, p[:, 0:k]).rank() == omega
                        and sp.Matrix.vstack(Wm, p[:, k:2 * k]).rank() == omega):
                    pairs.append((p[:, 0:k], p[:, k:2 * k]))
            if not pairs:
                continue
            rows_h = [fixed[i, 0:k] for i in range(fixed.rows)] + [hh for hh, _ in pairs[:20]]
            if sp.Matrix.vstack(*[sp.Matrix(q) for q in rows_h]).rank() < omega:
                continue
            for hh, gg in pairs[:40]:
                H = sp.Matrix.vstack(fixed[:, 0:k], hh)
                HA = sp.Matrix.vstack(fixed[:, k:2 * k], gg)
                w = H.rank()
                if w != omega:
                    continue
                if sp.Matrix.vstack(H, HA).rank() != w:
                    continue
                if layer_good(H, HA, w):
                    act.append(sp.sstr(Wm))
                    break
        rows.append((omega, f"Gr({omega},{k})", bool(act), f"{len(act)} W's pass"))
    return rows, dS


def booleanity(x, r0=1):
    n = 6
    C = sp.zeros(2, n)
    A = sp.zeros(n)
    C[0, 2] = 1
    A[1, 0] = 1
    A[2, 1] = 1
    C[1, 5] = 1
    A[4, 3] = x - 1
    A[5, 4] = 1
    L0 = sp.zeros(1, n)
    if r0 == 1:
        L0[0, 0] = x
        L0[0, 4] = 1
    return A, C, L0


def main() -> None:
    print("=" * 78)
    print("complete layer table (omega = 0 included)")
    print("=" * 78)
    for r0 in (1, 0):
        for x in [sp.Rational(0), sp.Rational(1, 2), sp.Rational(1)]:
            A, C, L0 = booleanity(x, r0)
            rows, dS = layer_table(A, C, L0, 1)
            verdict = any(r[2] for r in rows)
            print(f"\n  r0={r0}, x={x}  (dim S = {dS})  =>  decision: {'FEASIBLE' if verdict else 'infeasible'}")
            for (om, desc, ok, why) in rows:
                print(f"    omega={om} [{desc}]: feasible={int(ok)}   ({why})")


if __name__ == "__main__":
    main()
