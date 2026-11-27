"""Random exact check of kappa_obs = r * rank[N, AN] (attempt 248 support).

For random small rational A,C,L0 and q, build K0=ker[C;CA], a basis N,
and the linear map on r x n matrices:
    T(Delta R) = (Delta R N, Delta R A N).
Check rank(T) = r * rank[N, AN] and kernel dimension = r*n - rank(T).

Run: python tools/verification/c248_kappa_check.py
"""
import random

import sympy as sp


def one_case(rng, n, p, q):
    A = sp.Matrix([[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)])
    C = sp.Matrix([[rng.randint(-1, 1) for _ in range(n)] for _ in range(p)])
    L0 = sp.Matrix([[1] + [0] * (n - 1)])
    r0 = L0.rank()
    r = q - r0
    if r <= 0:
        return None
    K = sp.Matrix.vstack(C, C * A).nullspace()
    N = sp.Matrix.hstack(*K) if K else sp.zeros(n, 0)
    k = N.cols
    M = sp.Matrix.hstack(N, A * N)
    rank_NAN = M.rank()

    # columns of T: images of the basis matrices E_{i,j}
    cols = []
    for i in range(r):
        for j in range(n):
            E = sp.zeros(r, n)
            E[i, j] = 1
            X = E * N
            Y = E * A * N
            vec = []
            for row in range(r):
                vec.extend([X[row, c] for c in range(k)])
            for row in range(r):
                vec.extend([Y[row, c] for c in range(k)])
            cols.append(sp.Matrix(vec))
    T = sp.Matrix.hstack(*cols) if cols else sp.zeros(0, 0)
    rankT = T.rank()
    kernel_dim = r * n - rankT
    kappa = r * rank_NAN
    print(f'n={n} p={p} q={q} k={k} rank[N,AN]={rank_NAN} r={r} '
          f'rankT={rankT} kappa={kappa} kernel={kernel_dim}')
    assert rankT == kappa, 'rank(T) should equal r*rank[N,AN]'
    assert kernel_dim == r * (n - rank_NAN)
    return True


def main():
    rng = random.Random(248)
    tested = 0
    for n in (4, 5, 6):
        for p in (1, 2):
            for q in (2, 3, 4):
                for _ in range(5):
                    if one_case(rng, n, p, q):
                        tested += 1
    print(f'PASS: {tested} random cases checked')


if __name__ == '__main__':
    main()
