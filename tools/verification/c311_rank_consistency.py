"""Rank-consistency elimination for parametric linear systems (attempt 311).

Check the identity:
  exists b: M b = c  <=>  rank(M M^T) = rank([M c][M c]^T).
Tested on random exact matrices.

Run: python tools/verification/c311_rank_consistency.py
"""
import random

import sympy as sp


def formula_holds(M, c):
    G = M * M.T
    Gp = G + c * c.T
    return G.rank() == Gp.rank()


def system_consistent(M, c):
    # exists b with M b = c
    aug = M.row_join(c)
    return aug.rank() == M.rank()


def main():
    rng = random.Random(311)
    for trial in range(200):
        m = rng.randint(1, 5)
        n = rng.randint(1, 5)
        M = sp.Matrix([[rng.randint(-2, 2) for _ in range(n)] for _ in range(m)])
        c = sp.Matrix([[rng.randint(-2, 2)] for _ in range(m)])
        a = system_consistent(M, c)
        b = formula_holds(M, c)
        assert a == b, (M, c, a, b)
    print('PASS: 200 random systems, rank(M M^T)=rank([M c][M c]^T) <=> consistency')

    # explicit inconsistent system
    M = sp.Matrix([[1, 0], [0, 1], [1, 1]])
    c = sp.Matrix([[1], [0], [0]])
    print('rank M =', M.rank(), '; rank[M c] =', M.row_join(c).rank())
    print('rank G =', (M * M.T).rank(), '; rank Gp =', (M * M.T + c * c.T).rank())
    assert system_consistent(M, c) is False
    assert formula_holds(M, c) is False
    print('PASS: inconsistent example detected by both sides')


if __name__ == '__main__':
    main()
