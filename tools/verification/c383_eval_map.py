#!/usr/bin/env python3
"""c383 — The evaluation-map criterion  E_lambda : T_W -> W,  (x,y) |-> lambda x - y.

For a fixed compatible W, take a basis p_1,...,p_D of T_W = S cap (W + W) and form the
D x omega matrix  M(lambda) = (lambda x_j - y_j)_j  whose rows are the images of the basis.
Then

    E_lambda is surjective for every lambda   <=>   the omega x omega minors of M(lambda)
    are coprime,

and a necessary condition for layer omega to be feasible on the fibre of W is
dim image(E_lambda) + [fixed row] >= omega at every lambda.

The script tests this on (a) the counterexample, (b) the programmed characteristic family.
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


def minors(P, r):
    return [sp.expand(P.extract(list(rs), list(cs)).det())
            for rs in itertools.combinations(range(P.rows), r)
            for cs in itertools.combinations(range(P.cols), r)]


def eval_map_data(A, C, L0, W, omega):
    """Return (M(lambda) as D x omega matrix, T_W dimension, gcd of omega-minors)."""
    N = m.ker_basis(sp.Matrix.vstack(C, C * A))
    AN = A * N
    k = N.cols
    n = A.rows
    Wp = m.ker_basis(W)
    Y = m.ker_basis(sp.Matrix.hstack(N * Wp, AN * Wp).T)   # basis of T_W (as rows y)
    D = Y.cols
    if D == 0:
        return None, 0, None
    rows = []
    for j in range(D):
        y = Y[:, j].T
        h = (y * N)          # 1 x k
        g = (y * AN)
        rows.append([sp.expand(lam * h[0, c] - g[0, c]) for c in range(k)])
    M = sp.Matrix(rows)      # D x k
    # restrict to the omega coordinates of W: choose a chart where W is spanned by the first
    # omega rows of a transformation; simpler: express the columns in a basis of W
    # take the omega x omega minors of M in coordinates of W: since all rows lie in W
    # (by construction), ranking M itself suffices
    ms = [x for x in minors(M, omega) if sp.simplify(x) != 0]
    if not ms:
        g = sp.Integer(0)
    else:
        g = ms[0]
        for x in ms[1:]:
            g = sp.gcd(g, x)
    return M, D, sp.factor(g)


def nonempty(g):
    return g is not None and g != 0


def surjective(g):
    return g is not None and g != 0 and (sp.simplify(g).is_number or sp.Poly(g, lam).degree() == 0)


def main() -> None:
    print("=" * 80)
    print("evaluation-map criterion  E_lambda : T_W -> W")
    print("=" * 80)
    # (a) the counterexample
    n = 6
    A = sp.zeros(n)
    for i in range(2, 6):
        A[i, i - 2] = 1
    C = sp.zeros(2, n)
    C[0, 4] = 1
    C[1, 5] = 1
    L0 = sp.zeros(1, n)
    W1 = sp.Matrix([[1, 0]])
    M, D, g = eval_map_data(A, C, L0, W1, 1)
    print(f"\n(a) counterexample instance: dim T_W = {D}, gcd of 1-minors = {g}, "
          f"surjective = {surjective(g)}")
    # (b) programmed characteristic family
    for bvals, dvals in [((1, 2, 3), (5, 6, 7)), ((1, 1, 2), (5, 6, 7))]:
        k = len(bvals)
        A = sp.diag(sp.diag(*bvals), sp.diag(*dvals))
        n = A.rows
        C = sp.zeros(k, n)
        for i in range(k):
            C[i, k + i] = 1
        L0 = sp.Matrix([[1, 0, 0, 0, 0, 0]])
        for omega in range(1, k):
            # a compatible W: must contain the fixed pair's parts; take a coordinate plane
            N = m.ker_basis(sp.Matrix.vstack(C, C * A))
            fixed = L0 * sp.Matrix.hstack(N, A * N)
            h0, g0 = fixed[0, 0:k], fixed[0, k:2 * k]
            Kq = m.ker_basis(sp.Matrix.vstack(h0, g0))
            if Kq.cols == 0:
                continue
            for j in range(min(Kq.cols, 2)):
                W = m.ker_basis(Kq[:, j].T).T
                if W.rows != omega:
                    continue
                M, D, g = eval_map_data(A, C, L0, W, omega)
                print(f"  (b) B=diag{bvals}, omega={omega}: dim T_W = {D}, "
                      f"gcd of {omega}-minors of M = {g}, surjective = {surjective(g)}")


if __name__ == "__main__":
    main()
