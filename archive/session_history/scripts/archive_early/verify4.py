"""
FINAL verification.

(5a)  rank[LA;CA;C] = rank[CA;C;L]
(5b)  rank[sL-LA;CA;C] = rank[CA;C;L]  for all s in C

KEY EQUIVALENCE (proved + tested):
   (5a)  <=>  row(L A)  subset  row(C) + row(CA) + row(L)

SET-COVER REDUCTION (tested here):
   Universe U = {1..r}.  Elements <-> 2-dim invariant blocks:
       A_i = [[0,0],[1,0]]   acting on (x_i, y_i) :  A x_i = y_i,  A y_i = 0
   All eigenvalues of A are 0 => A nilpotent.
   L0 = [x_1^T ; ... ; x_r^T ]        (one prescribed functional per element)
   candidate functionals b_e := y_e  (e = 1..r)
   candidate for a set S  is the ROW  sum_{e in S} b_e
   Then:
       row(L0 A) = row(y_1,...,y_r)
       row(C) + row(CA) + row(L0) = row(x_1..x_r, y_1..y_r, L0) = row(x_1..x_r, y_1..y_r)
   so (5a) forces  row(sum_{e in S_i or not} y_e)  ... precisely a SET COVER.
"""
import itertools
import numpy as np

rng = np.random.default_rng(7)


def rank(M):
    M = np.atleast_2d(M)
    if M.size == 0:
        return 0
    return int(np.linalg.matrix_rank(M, tol=1e-7))


def stack(*blocks):
    blocks = [np.atleast_2d(b) for b in blocks]
    ncols = max((b.shape[1] for b in blocks), default=0)
    blocks = [b for b in blocks if b.shape[0] > 0]
    if not blocks:
        return np.zeros((0, ncols))
    return np.vstack(blocks)


def rows_in_span(X, Y):
    """True iff every row of X lies in the row space of Y."""
    if X.shape[0] == 0:
        return True
    return rank(stack(Y, X)) == rank(Y)


def cond5a(A, C, L):
    return rank(stack(L @ A, C @ A, C)) == rank(stack(C @ A, C, L))


def cond5a_via_rowspace(A, C, L):
    return rows_in_span(L @ A, stack(C, C @ A, L))


def cond5b(A, C, L, pts=None):
    rhs = rank(stack(C @ A, C, L))
    if pts is None:
        pts = [complex(x) for x in
               (-1e6, -1e3, -11.0, -3.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.5, 3.0, 11.0, 1e3, 1e6)]
        pts += [complex(c) for c in np.linalg.eigvals(A)]
        pts += [complex(rng.normal(), rng.normal()) for _ in range(40)]
    for s in pts:
        if rank(stack(s * L - L @ A, C @ A, C)) != rhs:
            return False
    return True


print("=" * 76)
print("TEST 1 :  (5a)  <=>  row(LA) subset row(C)+row(CA)+row(L)")
print("=" * 76)
mism = 0
for _ in range(500):
    n = int(rng.integers(2, 6))
    p = int(rng.integers(0, n + 1))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L = rng.integers(-2, 3, (q, n)).astype(float)
    if cond5a(A, C, L) != cond5a_via_rowspace(A, C, L):
        mism += 1
        if mism <= 3:
            print("   counterexample instance:", n, p, q)
print(f"  disagreements {mism}/500 -> {'CONFIRMED' if mism == 0 else 'FAILED'}")

print()
print("=" * 76)
print("TEST 2 :  set-cover reduction")
print("=" * 76)


def build_instance(sets, r):
    n = 2 * r
    A = np.zeros((n, n))
    for i in range(r):
        A[2 * i, 2 * i + 1] = 1.0      # A x_i = y_i ,  A y_i = 0
    C = np.zeros((0, n))
    L0 = np.zeros((r, n))
    for i in range(r):
        L0[i, 2 * i] = 1.0             # L0 = [x_1 ; ... ; x_r]
    cand = []
    for S in sets:
        v = np.zeros(n)
        for e in S:
            v[2 * e + 1] = 1.0         # sum of y_e for e in S
        cand.append(v)
    return A, C, L0, cand


def restricted_min(A, C, L0, cand):
    m = len(cand)
    n = L0.shape[1]
    for k in range(0, m + 1):
        for combo in itertools.combinations(range(m), k):
            R = np.array([cand[i] for i in combo]) if k else np.zeros((0, n))
            L = stack(L0, R)
            if cond5a(A, C, L) and cond5b(A, C, L):
                return k
    return None


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


bad = tested = 0
first = None
for trial in range(200):
    m = int(rng.integers(2, 6))
    r = int(rng.integers(2, 5))
    sets = []
    for _ in range(m):
        size = int(rng.integers(1, r + 1))
        sets.append(sorted(rng.choice(r, size=size, replace=False).tolist()))
    for e in range(r):                              # guarantee feasibility
        if not any(e in s for s in sets):
            j = int(rng.integers(0, m))
            sets[j] = sorted(set(sets[j]) | {e})

    A, C, L0, cand = build_instance(sets, r)
    sc = sc_min(sets, r)
    rm = restricted_min(A, C, L0, cand)
    tested += 1
    if sc != rm:
        bad += 1
        if first is None:
            first = (sets, r, sc, rm)
print(f"  tested {tested}, mismatches {bad} -> {'CONFIRMED' if bad == 0 else 'FAILED'}")
if first:
    print("  first mismatch: sets=%s r=%s setcover=%s observer=%s" % first)

print()
print("=" * 76)
print("TEST 3 :  explicit worked example")
print("=" * 76)
sets = [[0, 1], [1, 2], [0, 2]]       # r = 3, min cover = 2
r = 3
A, C, L0, cand = build_instance(sets, r)
print("  U = {0,1,2},  S = [[0,1],[1,2],[0,2]]  -> min set cover =", sc_min(sets, r))
for sub in [[0], [1], [2], [0, 1], [0, 2], [1, 2]]:
    R = np.array([cand[i] for i in sub])
    L = stack(L0, R)
    print(f"    choose S_i for i in {sub}:  (5a)={cond5a(A,C,L)!s:5s} (5b)={cond5b(A,C,L)!s:5s}")
print("  min #candidates =", restricted_min(A, C, L0, cand))

print()
print("=" * 76)
print("TEST 4 :  unrestricted minimum is <= restricted minimum (so NP-hardness")
print("          of the restricted version does NOT follow from the unrestricted one)")
print("=" * 76)
A, C, L0, cand = build_instance([[0, 1, 2]], 3)     # single set covering everything
print("  sets = [[0,1,2]], r = 3")
print("  restricted min =", restricted_min(A, C, L0, cand))
R0 = np.array([cand[0]])
print("  (5a) with the whole set as one row:", cond5a(A, C, stack(L0, R0)))
print("  (5b) with the whole set as one row:", cond5b(A, C, stack(L0, R0)))
print("  -> one row suffices because the candidate pool only has that one row.")
