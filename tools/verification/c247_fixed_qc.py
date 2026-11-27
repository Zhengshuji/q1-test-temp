"""Fixed-(q,c) bound: k = omega + c <= q - 1 + c (attempt 247).

For the compressed matrices H=LN, omega=rank H, c=k-omega.
The spectral criterion (5b) implies omega <= q-1, hence k <= q-1+c.

Checks:
- 244: q=3, c=1, k=3, bound 3.
- 228: q=3, c=2, k=4, bound 4.
- kappa_obs = r * rank[N, AN] is bounded by r * 2k.

Run: python tools/verification/c247_fixed_qc.py
"""
import sympy as sp


def data_244():
    A = sp.zeros(7, 7)
    A[2, 0] = 1
    A[3, 1] = 1
    A[4, 2] = 1
    A[5, 3] = 1
    A[0, 6] = 1
    C = sp.Matrix([[0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0]])
    L0 = sp.Matrix([[0, 0, 0, 0, 0, 0, 1]])
    l1 = sp.Matrix([[1, 2, 3, 6, 0, 0, 0]])
    l2 = sp.Matrix([[3, 6, 3, 6, 0, 0, 1]])
    L = sp.Matrix.vstack(L0, l1, l2)
    return A, C, L0, L


def data_228():
    n = 10
    A = sp.zeros(n, n)
    for i, j in [(0, 7), (1, 8), (2, 9), (7, 4), (8, 5), (9, 6)]:
        A[j, i] = 1
    C = sp.zeros(3, n)
    for i, j in [(0, 4), (1, 5), (2, 6)]:
        C[i, j] = 1
    L0 = sp.Matrix([[1] + [0] * (n - 1)])
    l2 = sp.Matrix([[0, 1, 0, 0, 0, 0, 0, 1, 0, 0]])
    l3 = sp.Matrix([[1, 1, 0, 0, 0, 0, 0, 1, 1, 0]])
    L = sp.Matrix.vstack(L0, l2, l3)
    return A, C, L0, L


def check(name, A, C, L0, L, q, c):
    n = A.cols
    K = sp.Matrix.vstack(C, C * A).nullspace()
    N = sp.Matrix.hstack(*K)
    k = N.cols
    H = sp.expand(L * N)
    omega = H.rank()
    r = q - L0.rank()
    M = sp.Matrix.hstack(N, A * N)
    rk = M.rank()
    kappa = r * rk
    bound = q - 1 + c
    print(f'{name}: n={n}, q={q}, c={c}, k={k}, omega={omega}, r={r}, '
          f'rank[N,AN]={rk}, kappa_obs={kappa}, bound k<= {bound}')
    assert k == omega + c, 'c = k - omega'
    assert k <= bound, 'k should be <= q-1+c'
    assert kappa <= r * 2 * k
    return k, omega, kappa


def main():
    A, C, L0, L = data_244()
    check('244', A, C, L0, L, 3, 1)
    A, C, L0, L = data_228()
    check('228', A, C, L0, L, 3, 2)
    print('PASS: k <= q-1+c and kappa_obs <= 2rk on the tested instances')


if __name__ == '__main__':
    main()
