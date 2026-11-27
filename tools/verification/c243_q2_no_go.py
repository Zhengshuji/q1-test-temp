"""Exact check of the q=2 no-go (attempts 243/245).

1. n=7,p=2,q=2 construction: S rank 5, Q dim 2,
   (5a) <=> l1*l4 - l2*l3 = 0, and this D has rank 4 / signature (2,2).
2. For L0A = alpha*L0 + beta*CA + gamma*C, HA's L0-row = alpha * H's L0-row.
3. Consequently P(alpha) has zero first row; for omega=2, rank P(alpha) <= 1 < 2,
   so (5b) fails. (If omega<=1 the gate is trivial; see 245 for the argument.)

Run: python tools/verification/c243_q2_no_go.py
"""
import sympy as sp

lam = sp.symbols('lam')
l1, l2, l3, l4, l5, l6, l7 = sp.symbols('l1 l2 l3 l4 l5 l6 l7')


def build():
    A = sp.zeros(7, 7)
    A[2, 0] = 1   # col1 = e3
    A[3, 1] = 1   # col2 = e4
    A[4, 2] = 1   # row5 = e3 (C*A)
    A[5, 3] = 1   # row6 = e4 (C*A)
    A[0, 6] = 1   # A[1][7] = 1
    C = sp.Matrix([[0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0]])
    L0 = sp.Matrix([[0, 0, 0, 0, 0, 0, 1]])
    l = sp.Matrix([[l1, l2, l3, l4, l5, l6, l7]])
    L = sp.Matrix.vstack(L0, l)
    return A, C, L0, l, L


def main():
    A, C, L0, l, L = build()
    CA = C * A
    S = sp.Matrix.vstack(L0, CA, C)
    print('rank C, CA, S =', C.rank(), CA.rank(), S.rank())
    assert S.rank() == 5
    assert 7 - S.rank() == 2

    L0A = L0 * A
    assert sp.expand(L0A) == sp.zeros(1, 7), 'expected L0A = 0'

    # (5a): v in span{x} in Q, i.e. l1*l4 - l2*l3 = 0
    D = sp.expand(l1 * l4 - l2 * l3)
    Q = sp.hessian(D, (l1, l2, l3, l4, l5, l6, l7)) / 2
    print('D =', D, '; rank of quadratic form =', Q.rank())
    assert Q.rank() == 4
    # signature over R: eigenvalues of the symmetric matrix
    ev = Q.eigenvals()
    pos = sum(m for e, m in ev.items() if sp.simplify(e) > 0)
    neg = sum(m for e, m in ev.items() if sp.simplify(e) < 0)
    print('signature =', (pos, neg))
    assert (pos, neg) == (2, 2)

    K = sp.Matrix.vstack(C, CA).nullspace()
    N = sp.Matrix.hstack(*K)
    print('dim K0 =', N.cols)
    assert N.cols == 3
    H = sp.expand(L * N)
    HA = sp.expand(L * A * N)
    print('H =', H)
    print('HA =', HA)
    assert sp.expand(HA[0, :]) == sp.zeros(1, N.cols), 'HA first row should be 0'

    # general lemma: L0A = alpha L0 + beta CA + gamma C, then HA1 = alpha H1
    alpha, b1c, b2c, g1c, g2c = sp.symbols('alpha b1c b2c g1c g2c')
    expr = sp.expand(alpha * L0 + b1c * CA[0, :] + b2c * CA[1, :]
                     + g1c * C[0, :] + g2c * C[1, :])
    sol = sp.solve(sp.Eq(expr, L0A), [alpha, b1c, b2c, g1c, g2c], dict=True)
    print('solve L0A = alpha L0 + beta CA + gamma C:', sol)
    assert sol, 'expected a solution'
    a0 = sol[0].get(alpha, 0)
    assert sp.simplify(HA[0, :] - a0 * H[0, :]) == sp.zeros(1, N.cols)

    P = sp.expand(lam * H - HA)
    # at lambda = alpha: first row zero, rank <= 1 < 2
    Pa = sp.simplify(P.subs(lam, a0))
    print('rank P(alpha) =', Pa.rank())
    assert Pa.rank() <= 1
    print('PASS: q=2 rank-4 gate constructed; (5b) fails at lambda=alpha')


if __name__ == '__main__':
    main()
