"""CORRECTION of attempt 258: the 2x2 minor test was insufficient.

For P of size q x k with q=3, k=5, the maximal minors are 3x3, not 2x2.
The instance from 258 actually has gcd of its 3x3 maximal minors
    lambda (lambda-1)(lambda-2),
so (5b) FAILS.  The instance is not a feasible offset gate.

Run: python tools/verification/c258_offset_gate.py
"""
import itertools
import sympy as sp

lam = sp.symbols('lam')


def main():
    # same instance as 258
    P = sp.Matrix([[0, 0, 0, 0, lam],
                   [0, 0, 2 - lam, 2 - lam, lam],
                   [lam - 1, 1 - lam, 2 - lam, 2 - lam, lam]])

    # correct maximal minors: 3x3 for q=3, k=5
    mins = []
    for rs in itertools.combinations(range(3), 3):
        for cs in itertools.combinations(range(5), 3):
            mins.append(sp.expand(P.extract(rs, cs).det()))
    g = mins[0]
    for m in mins[1:]:
        g = sp.gcd(g, m)
    print('number of 3x3 maximal minors =', len(mins))
    print('gcd =', sp.factor(g))
    print('rank P(0), P(1), P(2) =', P.subs(lam, 0).rank(),
          P.subs(lam, 1).rank(), P.subs(lam, 2).rank())
    assert sp.degree(sp.factor(g), lam) > 0, 'expected (5b) to fail'
    assert P.subs(lam, 1).rank() < 3
    print('CORRECTED: attempt 258 is retracted; (5b) fails for this instance')


if __name__ == '__main__':
    main()
