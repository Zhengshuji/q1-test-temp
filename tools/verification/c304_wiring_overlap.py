"""Column-overlap wiring criterion (attempt 304).

If A N_j = N_l then (H_A)[:,j] = H[:,l] for every L.
Small k=2 example: A e1=e2, A e2=e3; N=(e1,e2); rank[N AN]=3.

Run: python tools/verification/c304_wiring_overlap.py
"""
import sympy as sp


def main():
    k = 2
    N = sp.Matrix([[1, 0], [0, 1], [0, 0], [0, 0]])
    A = sp.Matrix([[0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]])
    AN = A * N
    print('N =', N.T, '; AN =', AN.T)
    print('rank[N AN] =', sp.Matrix.hstack(N, AN).rank())
    assert sp.Matrix.hstack(N, AN).rank() == 3
    assert sp.simplify(AN[:, 0] - N[:, 1]) == sp.zeros(4, 1)

    # random L
    L = sp.Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
    H = L * N
    HA = L * AN
    print('H =', H)
    print('HA =', HA)
    assert sp.simplify(HA[:, 0] - H[:, 1]) == sp.zeros(2, 1)
    print('PASS: A N_1 = N_2 forces (H_A)[:,1] = H[:,2] for every L')


if __name__ == '__main__':
    main()
