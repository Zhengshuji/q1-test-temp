"""c195_P_q.py -- exact rational implementation of the recursion algorithm for
    P(A,B,S) = min { dim U | S <= U, A U <= U + B }
and a cross-check against exhaustive enumeration over F_p (p = 5, 7, 11, 13).

WHY THIS IS ONE-SIDED OVER Q
----------------------------
Gr(k, n) over Q is infinite, so `P` cannot be verified by exhaustive enumeration over Q.
What CAN be checked exactly over Q:
  * the algorithm's value `P_alg` (rational arithmetic, no rounding);
  * agreement with the exhaustive value of the SAME integer instance reduced mod p,
    for several primes -- a disagreement means either a bug or a degenerate reduction.
The lower bound itself is a theorem (dim T + dim(pi U) <= dim U, Lean-checked), so the
cross-check is mainly a bug detector for the implementation.

USAGE
    python tools/p_algorithm/c195_P_q.py            # n = 4,5 ; p = 5,7,11
    python tools/p_algorithm/c195_P_q.py --n 6
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

# ---------------------------------------------------------------- rational linear algebra
def rref(M):
    """reduced row echelon form over Q"""
    A = [[Fr(x) for x in row] for row in M]
    m = len(A)
    if m == 0:
        return [], []
    n = len(A[0])
    piv, r = [], 0
    for c in range(n):
        pr = None
        for i in range(r, m):
            if A[i][c] != 0:
                pr = i
                break
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        iv = A[r][c]
        A[r] = [x / iv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(n)]
        piv.append(c)
        r += 1
        if r == m:
            break
    return A[:r], piv


def rank(M):
    return len(rref(M)[1])


def basis(rows):
    return [list(r) for r in rref(rows)[0]] if rows else []


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
            for i in range(len(A))]


def vstack(*Ms):
    out = []
    for M in Ms:
        out.extend([list(r) for r in M])
    return out


def complement(B, n):
    """a complement of span(B) in Q^n, as a list of row vectors"""
    Bb = basis(B)
    C = []
    for i in range(n):
        v = [Fr(0)] * n
        v[i] = Fr(1)
        if rank(vstack(Bb, C + [v])) == len(Bb) + len(C) + 1:
            C.append(v)
    return C


def coords_in(bas, x):
    """coordinates of x in the basis `bas` (rows), or None"""
    if not bas:
        return [] if all(Fr(v) == 0 for v in x) else None
    k = len(bas)
    Mx = [[bas[j][i] for j in range(k)] + [Fr(x[i])] for i in range(len(x))]
    R, piv = rref(Mx)
    co = [Fr(0)] * k
    for i, pc in enumerate(piv):
        if pc < k:
            co[pc] = R[i][k]
    chk = [sum(co[j] * bas[j][i] for j in range(k)) for i in range(len(x))]
    if all(chk[i] == Fr(x[i]) for i in range(len(x))):
        return co
    return None


# ---------------------------------------------------------------- the algorithm over Q
def P_alg(A, B, S):
    """exact rational value of P via the iterated one-step recursion"""
    n = len(A)
    dy = n
    C = basis(B)
    Phi = [[Fr(x) for x in r] for r in A]
    T = basis(S)
    total = 0
    steps = 0
    while T and dy > 0 and steps <= n + 2:
        total += len(T)
        steps += 1
        M = basis(vstack(T, C))
        if len(M) == dy:
            break
        N = complement(M, dy)
        dy2 = len(N)
        base = M + N

        def toY2(x):
            co = coords_in(base, x)
            return co[len(M):] if co is not None else None

        def lift(y):
            return [sum(y[k] * N[k][i] for k in range(len(N))) for i in range(dy)]

        C2 = basis([toY2([sum(m[i] * Phi[i][j] for i in range(dy)) for j in range(dy)])
                    for m in M])
        T2 = basis([toY2([sum(tt[i] * Phi[i][j] for i in range(dy)) for j in range(dy)])
                    for tt in T])
        Phi2 = []
        for i in range(dy2):
            e = [Fr(1) if k == i else Fr(0) for k in range(dy2)]
            img = [sum(lift(e)[a] * Phi[a][j] for a in range(dy)) for j in range(dy)]
            Phi2.append(toY2(img))
        C, T, Phi, dy = C2, T2, Phi2, dy2
    return total


# ---------------------------------------------------------------- exhaustive over F_p
def rref_p(M, p):
    A = [[x % p for x in r] for r in M]
    m = len(A)
    if m == 0:
        return [], []
    n = len(A[0])
    piv, r = [], 0
    for c in range(n):
        pr = None
        for i in range(r, m):
            if A[i][c]:
                pr = i
                break
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        iv = pow(A[r][c], p - 2, p)
        A[r] = [(x * iv) % p for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [(A[i][j] - f * A[r][j]) % p for j in range(n)]
        piv.append(c)
        r += 1
        if r == m:
            break
    return A[:r], piv


def rank_p(M, p):
    return len(rref_p(M, p)[1])


def mul_p(A, B, p):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) % p for j in range(len(B[0]))]
            for i in range(len(A))]


def subspaces(m, p, k):
    if k == 0:
        yield []
        return
    if k > m:
        return
    for piv in itertools.combinations(range(m), k):
        free = [[c for c in range(piv[i] + 1, m) if c not in piv] for i in range(k)]
        for vals in itertools.product(*[itertools.product(range(p), repeat=len(f)) for f in free]):
            rows = []
            for i in range(k):
                row = [0] * m
                row[piv[i]] = 1
                for c, v in zip(free[i], vals[i]):
                    row[c] = v
                rows.append(row)
            yield rows


def P_exh_p(A, B, S, p):
    """exhaustive P over F_p (all subspaces enumerated)"""
    n = len(A)
    ds = len(S)
    for k in range(ds, n + 1):
        for U in subspaces(n, p, k - ds):
            W = vstack(S, U)
            if rank_p(W, p) != k:
                continue
            if rank_p(vstack(W, B, mul_p(W, A, p)), p) == rank_p(vstack(W, B), p):
                return k
    return None


def main():
    n = 4
    if "--n" in sys.argv:
        n = int(sys.argv[sys.argv.index("--n") + 1])
    primes = [5, 7, 11]
    rng = random.Random(2027)
    print("=" * 96)
    print(f"c195 -- exact rational P_alg  vs  exhaustive over F_p   (n = {n})")
    print("=" * 96)
    print("  instance | P_alg (Q) | P_exh(F_5) | P_exh(F_7) | P_exh(F_11) | verdict")
    agree = total = 0
    for t in range(12):
        A = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
        b = rng.choice([1, 2])
        B = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(b)]
        ds = rng.choice([1, 2])
        S = []
        while len(S) < ds:
            v = [rng.randint(-2, 2) for _ in range(n)]
            if rank(S + [v]) == len(S) + 1:
                S.append(v)
        if rank(B) != b:
            continue
        pq = P_alg(A, B, S)
        vals = []
        for p in primes:
            Ap = [[x % p for x in r] for r in A]
            Bp = [[x % p for x in r] for r in B]
            Sp = [[x % p for x in r] for r in S]
            if rank_p(Bp, p) != b or rank_p(Sp, p) != ds:
                vals.append(None)
                continue
            vals.append(P_exh_p(Ap, Bp, Sp, p))
        total += 1
        good = all(v is None or v == pq for v in vals)
        agree += good
        print(f"     {t:2d}   |    {pq:3d}     |     {vals[0]}      |     {vals[1]}      "
              f"|      {vals[2]}      | {'OK' if good else '**MISMATCH**'}")
    print()
    print(f"agreement: {agree}/{total}")
    print("note: a 'None' entry means the reduction mod p was degenerate (rank dropped).")


if __name__ == "__main__":
    main()
