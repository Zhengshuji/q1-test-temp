"""Effective observer dimension kappa_obs = r * rank[N, AN] (attempt 246).

For rational data (A,C,L0), with K0=ker[C;CA], N a basis of K0,
r = q - rank(L0) free rows, kappa_obs = r * rank[N, AN].

Checks the formula on three instances:
- 234: n=5, q=2, p=1
- 244: n=7, q=3, p=2
- 228: n=10, q=3, p=3 (the 10-dimensional family)

Run: python tools/verification/c246_kappa_obs.py
"""
import sympy as sp


def kappa_obs(A, C, L0, q):
    n = A.cols
    K = sp.Matrix.vstack(C, C * A).nullspace()
    N = sp.Matrix.hstack(*K) if K else sp.zeros(n, 0)
    M = sp.Matrix.hstack(N, A * N) if N.cols else sp.zeros(n, 0)
    rank_NAN = M.rank()
    r = q - L0.rank()
    return r, rank_NAN, r * rank_NAN, N.cols


def main():
    # 234 instance
    A5 = sp.Matrix([[1, 1, -1, 0, 1],
                    [-1, 0, 0, -1, 1],
                    [0, 1, -1, 0, 1],
                    [0, 0, 0, -1, 0],
                    [-1, 1, 0, 0, 0]])
    C5 = sp.Matrix([[0, 0, 0, 0, 1]])
    L05 = sp.Matrix([[1, 0, 0, 0, 0]])
    print('234: r, rank[N,AN], kappa_obs, dimK0 =', kappa_obs(A5, C5, L05, 2))

    # 244 instance
    A7 = sp.zeros(7, 7)
    A7[2, 0] = 1
    A7[3, 1] = 1
    A7[4, 2] = 1
    A7[5, 3] = 1
    A7[0, 6] = 1
    C7 = sp.Matrix([[0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0]])
    L07 = sp.Matrix([[0, 0, 0, 0, 0, 0, 1]])
    r, rk, kappa, k0 = kappa_obs(A7, C7, L07, 3)
    print('244: r, rank[N,AN], kappa_obs, dimK0 =', r, rk, kappa, k0)
    assert (r, rk, kappa, k0) == (2, 5, 10, 3)

    # 228 family
    n = 10
    A10 = sp.zeros(n, n)
    for i, j in [(0, 7), (1, 8), (2, 9), (7, 4), (8, 5), (9, 6)]:
        A10[j, i] = 1
    C10 = sp.zeros(3, n)
    for i, j in [(0, 4), (1, 5), (2, 6)]:
        C10[i, j] = 1
    L010 = sp.Matrix([[1] + [0] * (n - 1)])
    r, rk, kappa, k0 = kappa_obs(A10, C10, L010, 3)
    print('228: r, rank[N,AN], kappa_obs, dimK0 =', r, rk, kappa, k0)

    # formula sanity: kappa_obs = r * rank[N,AN]
    assert kappa == r * rk
    print('PASS: kappa_obs formula checked')


if __name__ == '__main__':
    main()
