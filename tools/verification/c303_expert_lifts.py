"""Verification of the expert's three full-observer constructions (attempt 303).

Part A: universal lift in dimension 3k.
Part B: lifted multiplication gate (full observer), (5a) <=> z=xy, (5b) <=> beta != 0.
Part C: input-controlled nonzero gate, (5b) <=> x != 0.

Run: python tools/verification/c303_expert_lifts.py
"""
import itertools

import sympy as sp

lam, x, y, z, beta, w = sp.symbols('lam x y z beta w')


def part_a(k=2):
    I = sp.eye(k)
    Z = sp.zeros(k, k)
    C = sp.Matrix.hstack(I, Z, Z)
    A = sp.Matrix.vstack(
        sp.Matrix.hstack(Z, Z, I),
        sp.Matrix.hstack(Z, Z, Z),
        sp.Matrix.hstack(Z, I, Z),
    )
    N = sp.Matrix.vstack(Z, I, Z)
    CA = C * A
    print('A: C A =', CA)
    assert CA == sp.Matrix.hstack(Z, Z, I)
    M = sp.Matrix.vstack(C, CA)
    assert M.rank() == 2 * k
    assert sp.Matrix.hstack(N, A * N).rank() == 2 * k

    # arbitrary compressed data
    H0 = sp.Matrix([[1, 2], [3, 4]]) if k == 2 else sp.eye(k)
    HA0 = sp.Matrix([[5, 6], [7, 8]]) if k == 2 else 2 * sp.eye(k)
    Y = sp.Matrix([[9, 10], [11, 12]]) if k == 2 else 3 * sp.eye(k)
    Zc = sp.Matrix([[13, 14], [15, 16]]) if k == 2 else 4 * sp.eye(k)
    L0 = sp.Matrix.hstack(sp.zeros(2, k), H0, HA0)
    R = sp.Matrix.hstack(sp.zeros(2, k), Y, Zc)
    L = sp.Matrix.vstack(L0, R)
    H = L * N
    HA = L * A * N
    print('lifted H =', H)
    print('lifted HA =', HA)
    assert sp.simplify(H - sp.Matrix.vstack(H0, Y)) == sp.zeros(*H.shape)
    assert sp.simplify(HA - sp.Matrix.vstack(HA0, Zc)) == sp.zeros(*HA.shape)
    print('PASS A: universal lift, row[N AN] has rank 2k =', 2 * k)


def part_b():
    # k=3, n=9, p=3
    k = 3
    e = sp.Matrix([[1, 0, 0]])
    vx = sp.Matrix([[0, 1, x]])
    H = sp.Matrix.vstack(e, e, vx, sp.zeros(1, 3))
    HA = sp.Matrix.vstack(sp.zeros(1, 3), e,
                          sp.Matrix([[0, y, z]]),
                          sp.Matrix([[0, beta, w]]))
    assert H.rank() == 2
    # (5a): the third row is in span(e,vx) iff z=xy; fourth iff w=beta*x
    gate = {z: x * y, w: beta * x}
    assert sp.Matrix.vstack(H, HA).subs(gate).rank() == 2
    off = {z: x * y + 1, w: beta * x}
    assert sp.Matrix.vstack(H, HA).subs(off).rank() == 3

    P = sp.expand(lam * H - HA).subs(gate)
    print('P on gate =', P)
    # rows are lambda e, (lambda-1)e, (lambda-y)vx, -beta vx
    for val in (0, 1, 2, 3, -1):
        pt = {x: 2, y: 3, beta: 1, lam: val}
        r = P.subs(pt).rank()
        print('lambda=%s rank P =' % val, r)
        assert r == 2
    # beta=0: at lambda=y the vx rows vanish
    pt0 = {x: 2, y: 3, beta: 0, lam: 3}
    print('beta=0, lambda=y rank =', P.subs(pt0).rank())
    assert P.subs(pt0).rank() == 1
    print('PASS B: multiplication gate; (5b) <=> beta != 0 on z=xy,w=beta*x')


def part_c():
    # q=2,n=3,p=1,k=1,omega=1
    C = sp.Matrix([[0, 0, 1]])
    A = sp.Matrix([[0, 0, 0], [x, 0, 0], [0, 1, 0]])
    L0 = sp.Matrix([[1, 0, 0]])
    u, v = sp.symbols('u v')
    R = sp.Matrix([[u, v, 0]])
    L = sp.Matrix.vstack(L0, R)
    N = sp.Matrix([[1], [0], [0]])
    assert C * N == sp.zeros(1, 1)
    assert C * A * N == sp.zeros(1, 1)
    H = sp.expand(L * N)
    HA = sp.expand(L * A * N)
    print('H =', H, '; HA =', HA)
    assert sp.simplify(H - sp.Matrix([[1], [u]])) == sp.zeros(2, 1)
    assert sp.simplify(HA - sp.Matrix([[0], [x * v]])) == sp.zeros(2, 1)
    P = sp.expand(lam * H - HA)
    for xv in (0, 1, 2):
        for uu in (0, 1):
            ranks = [P.subs({x: 1, v: xv, u: uu, lam: t}).rank() for t in (0, 1, 2)]
            print('xv=%s u=%s ranks=' % (xv, uu), ranks)
            if xv == 0:
                assert min(ranks) < 1
            else:
                assert all(r == 1 for r in ranks)
    print('PASS C: input-controlled nonzero, (5b) <=> x != 0')


if __name__ == '__main__':
    part_a()
    part_b()
    part_c()
