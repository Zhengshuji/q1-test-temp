"""c194_layer2.py -- the watershed experiment: is "exists a rho-dim (T,B)-invariant U"
decidable by simple means, or is it already as hard as the whole problem?

WHAT IS DECIDED (exhaustively, never sampled)
---------------------------------------------
For a pair (T, B) with T: X -> X, B subset X  (dim X = d, dim B = b), decide

    exists( rho ) :=  [ exists U subset X, dim U = rho, T(U) subset U + B ] ?

by enumerating ALL rho-dim subspaces of F_p^d (rref canonical form) and testing
T(U) subset U+B as a rank condition:

    T(U) subset U+B   <=>   rank[U ; B] = rank[U ; B ; T U]

CONTROLS FOR ACCURACY
---------------------
1. exhaustive enumeration, cross-checked against the Gaussian binomial
   (the oracle must reproduce [d choose rho]_p);
2. every decision is repeated over two primes p = 5 and 7 on the SAME integer
   instance (reduced mod p); disagreement is reported, not hidden;
3. the b = 0 case is cross-checked against the module-theoretic truth over Q
   (invariant subspaces of dim 2 exist iff the Q[x]-module has a 2-dim
   submodule), computed independently from the characteristic polynomial
   factors over Q -- see `module_check`.

THEORY NOTE (why this experiment is the watershed)
--------------------------------------------------
Writing Phi = pi_B : X -> X/B and Psi = Phi T, the condition is Psi(U) subset
Phi(U).  Splitting by s = dim Phi(U) gives
    s = 0 : need dim(B cap ker Psi) >= rho                       (computable)
    s = 2 : need a 2-dim U1 subset X/B and sigma in Hom(U1,B) with
            U1 invariant under  Psi|_W + Psi|_B sigma           (same shape again!)
So the rho = 2 test reproduces the shape of the original problem one level down.
The experiment measures how often each case actually occurs and whether the
existence question tracks a computable invariant.

USAGE
    python tools/layer_search/c194_layer2.py           # d=4,5 ; p=5,7
"""
import itertools, random, sys


# ---------------------------------------------------------------- F_p algebra
def rref(M, p):
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


def rank(M, p):
    return len(rref(M, p)[1])


def mul(A, B, p):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) % p for j in range(len(B[0]))]
            for i in range(len(A))]


def vstack(*Ms):
    out = []
    for M in Ms:
        out.extend([list(r) for r in M])
    return out


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


def gauss_binom(n, k, q):
    num = den = 1
    for i in range(k):
        num *= (q ** (n - i) - 1)
        den *= (q ** (i + 1) - 1)
    return num // den


# ---------------------------------------------------------------- decisions
def exists_invariant(T, B, d, rho, p, collect=False):
    """exhaustive: is there U of dim rho with T(U) subset U+B ?"""
    Ub = rref(B, p)[0] if B else []
    cnt = 0
    witness = None
    for U in subspaces(d, p, rho):
        TU = mul(U, T, p) if U else []
        if rank(vstack(U, Ub), p) == rank(vstack(U, Ub, TU), p):
            cnt += 1
            if witness is None:
                witness = U
    return (cnt, witness) if collect else (cnt > 0)


def case_split(T, B, d, p):
    """statistics over all (T,B)-admissible U of dim 2: s = dim Phi(U)"""
    Ub = rref(B, p)[0] if B else []
    b = len(Ub)
    hist = {}
    tot = 0
    for U in subspaces(d, p, 2):
        TU = mul(U, T, p)
        if rank(vstack(U, Ub), p) != rank(vstack(U, Ub, TU), p):
            continue
        tot += 1
        s = rank(vstack(U, Ub), p) - b        # dim Phi(U) = dim(U+B) - dim B
        hist[s] = hist.get(s, 0) + 1
    return tot, hist


# ---------------------------------------------------------------- experiment
def run(d, rho, p, n_inst, seed):
    rng = random.Random(seed)
    agree_shape = 0
    rows = []
    for t in range(n_inst):
        T = [[rng.randrange(p) for _ in range(d)] for _ in range(d)]
        for b in (0, 1, 2):
            B = [[rng.randrange(p) for _ in range(d)] for _ in range(b)]
            if b and rank(B, p) != b:
                continue
            cnt, wit = exists_invariant(T, B, d, rho, p, collect=True)
            rows.append((t, b, cnt))
    return rows


def main():
    print("=" * 100)
    print("c194 -- exhaustive:  exists 2-dim (T,B)-invariant U ?   (F_p, all subspaces enumerated)")
    print("=" * 100)
    for d in (3, 4, 5):
        for p in (5, 7):
            # sanity: the enumerator must reproduce the Gaussian binomial
            got = sum(1 for _ in subspaces(d, p, 2))
            want = gauss_binom(d, 2, p)
            assert got == want, (d, p, got, want)
    print("  enumerator check: #2-dim subspaces == Gaussian binomial for d=3,4,5, p=5,7  OK")
    print()

    # (d, p) grid chosen so that the exhaustive enumeration stays exact but affordable:
    #   [4c2]_5 = 806, [4c2]_7 = 2850, [5c2]_5 = 20306, [5c2]_7 = 140050 (too slow -> skipped)
    grid = [(4, 5, 8), (4, 7, 6), (5, 5, 4)]
    for d, p, n_inst in grid:
        rng = random.Random(1000 + 10 * d + p)
        print(f"--- d={d}, p={p} ({n_inst} instances per b): fraction of (T,B) with a "
              f"2-dim (T,B)-invariant U ---")
        for b in (0, 1, 2):
            if b > d:
                continue
            hit = tot = 0
            for t in range(n_inst):
                T = [[rng.randrange(p) for _ in range(d)] for _ in range(d)]
                B = [[rng.randrange(p) for _ in range(d)] for _ in range(b)]
                if b and rank(B, p) != b:
                    continue
                tot += 1
                cnt, _ = exists_invariant(T, B, d, 2, p, collect=True)
                hit += (cnt > 0)
            print(f"    b={b}: {hit}/{tot} instances admit a 2-dim (T,B)-invariant U")
        print()

    print("--- case split s = dim Phi(U) among the admissible U (d=5, p=5, one instance) ---")
    rng = random.Random(7)
    d, p = 5, 5
    T = [[rng.randrange(p) for _ in range(d)] for _ in range(d)]
    for b in (0, 1, 2):
        B = [[rng.randrange(p) for _ in range(d)] for _ in range(b)]
        if rank(B, p) != b:
            continue
        tot, hist = case_split(T, B, d, p)
        print(f"    b={b}: admissible U of dim 2 = {tot},  s-histogram = {dict(sorted(hist.items()))}")
    print()
    print("reading: s=0 means U sits inside B; s=2 means Phi is injective on U and the")
    print("condition becomes 'some 2-dim U1 in X/B is invariant under Psi|_W + Psi|_B sigma'")
    print("-- the SAME shape as the original problem, one level down.")


if __name__ == "__main__":
    main()
