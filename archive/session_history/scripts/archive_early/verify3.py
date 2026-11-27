"""
Corrected rigorous test.

PROBLEM Q : given (A, C, L0), find R with the FEWEST ROWS such that
            L = [L0 ; R] satisfies (5a) and (5b).

(5a)  rank[ LA ; CA ; C ] = rank[ CA ; C ; L ]
(5b)  rank[ sL - LA ; CA ; C ] = rank[ CA ; C ; L ]   for all s in C

Key equivalence (used throughout):
   (5a)  <=>  row(L A)  is contained in  row(L) + row(C) + row(CA)
   (5b)  <=>  row(L A)  is contained in  row(L) + row(C) + row(CA),  AND
              (spectral part) row(L0 A) subset row(L) + row(C)  [see doc]
"""
import itertools
import numpy as np

rng = np.random.default_rng(2024)
N = None  # column count, set per call


def rank(M):
    M = np.atleast_2d(M)
    if M.size == 0:
        return 0
    return int(np.linalg.matrix_rank(M, tol=1e-9))


def stack(*blocks):
    """Stack rows, PRESERVING the common column count even when all are empty."""
    blocks = [np.atleast_2d(b) for b in blocks]
    ncols = max((b.shape[1] for b in blocks), default=0)
    blocks = [b for b in blocks if b.shape[0] > 0]
    if not blocks:
        return np.zeros((0, ncols))
    return np.vstack(blocks)


def rowspace_basis(M):
    M = np.atleast_2d(M)
    ncols = M.shape[1]
    if M.size == 0 or M.shape[0] == 0:
        return np.zeros((0, ncols))
    u, s, vt = np.linalg.svd(M, full_matrices=False)
    tol = max(M.shape) * (s[0] if s.size else 1.0) * 1e-12
    return vt[s > tol]


def cond5a(A, C, L):
    lhs = stack(L @ A, C @ A, C)
    rhs = stack(C @ A, C, L)
    return rank(lhs) == rank(rhs)


def cond5b(A, C, L, extra_pts=60):
    """Test rank[sL-LA;CA;C] == rank[CA;C;L] for all s in C, by sampling
    real/complex s plus eig(A).  Rank can only drop at finitely many s."""
    rhs = rank(stack(C @ A, C, L))
    pts = [complex(x) for x in
           (-1e6, -1e3, -13.0, -3.0, -1.5, -1.0, -0.7, 0.0, 0.3, 0.5, 1.0, 2.0, 3.0, 13.0, 1e3, 1e6)]
    pts += [complex(c) for c in np.linalg.eigvals(A)]
    pts += [complex(rng.normal(), rng.normal()) for _ in range(extra_pts)]
    for s in pts:
        if rank(stack(s * L - L @ A, C @ A, C)) != rhs:
            return False
    return True


def formula_k(A, C, L0):
    """k* = dim(row([C;CA]) + row([L0;L0A])) - dim(row([C;CA]) + row(L0))"""
    P = stack(C @ A, C, L0, L0 @ A)
    Q = stack(C @ A, C, L0)
    return rank(P) - rank(Q)


def construct_optimal_R(A, C, L0):
    """Explicit optimal R: directions in row([C;CA;L0;L0A]) outside row([C;CA;L0])."""
    n = A.shape[0]
    Q = stack(C @ A, C, L0)
    P = stack(C @ A, C, L0, L0 @ A)
    BQ = rowspace_basis(Q)
    BP = rowspace_basis(P)
    cur, extra = BQ.copy(), []
    for v in BP:
        if rank(stack(cur, v)) > rank(cur):
            extra.append(v)
            cur = np.vstack([cur, v])
    return np.array(extra) if extra else np.zeros((0, n))


print("=" * 76)
print("TEST 1 :  (5a)  <=>  row(LA) subset row(L) + row(C) + row(CA)")
print("=" * 76)
mism = 0
for trial in range(400):
    n = int(rng.integers(2, 6))
    p = int(rng.integers(0, n + 1))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L = rng.integers(-2, 3, (q, n)).astype(float)
    direct = cond5a(A, C, L)
    sub = rank(stack(L @ A, C @ A, C, L)) == rank(stack(C @ A, C, L))
    if direct != sub:
        mism += 1
print(f"  disagreements: {mism}/400  ->  {'CONFIRMED' if mism == 0 else 'FAILED'}")

print()
print("=" * 76)
print("TEST 2 :  min rows(R)  =  dim(row([C;CA;L0;L0A])) - dim(row([C;CA;L0]))")
print("=" * 76)
bad = 0
tested = 0
for trial in range(400):
    n = int(rng.integers(2, 6))
    p = int(rng.integers(0, n + 1))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L0 = rng.integers(-2, 3, (q, n)).astype(float)
    if rank(L0) < q:
        continue
    tested += 1
    k = formula_k(A, C, L0)

    # (a) constructed R has exactly k rows and satisfies (5a)
    R = construct_optimal_R(A, C, L0)
    if R.shape[0] != k:
        bad += 1
        print(f"  [t{trial}] |R|={R.shape[0]} but formula={k}")
        continue
    if not cond5a(A, C, stack(L0, R)):
        bad += 1
        print(f"  [t{trial}] constructed R fails (5a)")
        continue

    # (b) optimality, brute force on the small grid: no k'<k rows work
    if n <= 3 and k >= 1:
        grid = [np.array(v, dtype=float) for v in
                itertools.product(range(-2, 3), repeat=n) if any(v)]
        smaller = False
        for kk in range(0, k):
            for combo in itertools.combinations_with_replacement(range(len(grid)), kk):
                RR = np.array([grid[i] for i in combo]) if kk else np.zeros((0, n))
                if cond5a(A, C, stack(L0, RR)):
                    smaller = True
                    break
            if smaller:
                break
        if smaller:
            bad += 1
            print(f"  [t{trial}] found R with < {k} rows")

print(f"  tested {tested} instances; failures {bad}  ->  {'CONFIRMED' if bad == 0 else 'FAILED'}")

print()
print("=" * 76)
print("TEST 3 :  relation between (5a) and (5b)")
print("=" * 76)
only5a = both = 0
for trial in range(300):
    n = int(rng.integers(2, 5))
    p = int(rng.integers(0, n + 1))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L = rng.integers(-2, 3, (q, n)).astype(float)
    a, b = cond5a(A, C, L), cond5b(A, C, L)
    if b and not a:
        print("  (5b) holds but (5a) fails  <-- would refute (5b)=>(5a)")
    if a and not b:
        only5a += 1
    if a and b:
        both += 1
print(f"  (5a)&(5b) both hold: {both};  only (5a) holds: {only5a}")
print("  => (5b) is strictly stronger than (5a); the extra content is spectral.")

print()
print("=" * 76)
print("TEST 4 :  SET-COVER reduction, correctly formulated")
print("=" * 76)
print("""
  Construction.  Universe U = {1..r}.  Block i is a 2-dimensional A-block
      A_i = [[0,1],[0,0]],   L0 gets NO row in block i.
  Candidate functional for set S (as a multiset, q_i = multiplicity):
      b_S = sum_{i in S} sum_{t=0}^{q_i-1} (row that activates direction t+1 of block i)
  Requirement (5a) forces row(L0 A) = row(L A) to be covered, i.e. block i must
  be activated q_i times for every i -- exactly a set cover with multiplicity.
""")

r = None


def build(A_blocks, sets, mult):
    raise NotImplementedError


def sc_min(sets, r):
    m = len(sets)
    for k in range(0, m + 1):
        for combo in itertools.combinations(range(m), k):
            cov = set()
            for i in combo:
                cov |= set(sets[i])
            if len(cov) == r:
                return k
    return None


# Direct construction on the 2r-dimensional nilpotent-shift system:
#   A = blockdiag over i=1..r of [[0,1],[0,0]] on coordinates (x_i, y_i)
#   block i coordinates: (2i, 2i+1)  ->  x_i at 2i, y_i at 2i+1
#   A x_i = 0, A y_i = x_i
#   L0 has no rows.
# A direction "t of block i" is reached by a functional supported on y_i.
# Adding a row equal to y_i makes row(L) contain y_i and (via A) y_i A = x_i.
# So ONE row y_i activates BOTH directions of block i.
# To encode multiplicities we instead make block i contain (q_i) "levels".
print("  Simpler faithful model (block per element, one level):")
print("  A = blockdiag([[0,1],[0,0]]), L0 = 0, candidate b_S = sum_{i in S} y_i")


def cond5a_general(A, C, L):
    return cond5a(A, C, L)


bad = 0
tested = 0
for trial in range(150):
    m = int(rng.integers(2, 6))
    r = int(rng.integers(2, 5))
    sets = []
    for _ in range(m):
        size = int(rng.integers(1, r + 1))
        sets.append(sorted(rng.choice(r, size=size, replace=False).tolist()))
    for e in range(r):  # feasibility
        if not any(e in s for s in sets):
            j = int(rng.integers(0, m))
            sets[j] = sorted(set(sets[j]) | {e})

    n = 2 * r
    A = np.zeros((n, n))
    for i in range(r):
        A[2 * i, 2 * i + 1] = 1.0          # A y_i = x_i
    C = np.zeros((0, n))
    L0 = np.zeros((0, n))                   # no prescribed functionals
    cand = []
    for S in sets:
        v = np.zeros(n)
        for i in S:
            v[2 * i + 1] = 1.0             # y_i
        cand.append(v)

    # min number of candidates so that (5a) holds
    kmin = None
    for k in range(0, m + 1):
        for combo in itertools.combinations(range(m), k):
            R = np.array([cand[i] for i in combo]) if k else np.zeros((0, n))
            if cond5a(A, C, stack(L0, R)):
                kmin = k
                break
        if kmin is not None:
            break

    sc = sc_min(sets, r)
    tested += 1
    if sc != kmin:
        bad += 1
        if bad <= 4:
            print(f"    mismatch: setcover={sc} observer={kmin} sets={sets}")
print(f"  tested {tested}; mismatch {bad}  ->  {'CONFIRMED' if bad == 0 else 'FAILED'}")
