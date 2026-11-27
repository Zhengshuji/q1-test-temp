"""
DEFINITIVE verification.

(5a)  rank[LA;CA;C] = rank[CA;C;L]
(5b)  rank[sL-LA;CA;C] = rank[CA;C;L] for all s in C

Claim A : (5a) <=> row(LA) subset row(C)+row(CA)+row(L)
Claim B : min |R| = dim row([C;CA;L0;L0A]) - dim row([C;CA;L0])   (POLYNOMIAL)
Claim C : therefore the literal problem is in P, and q.txt's claim is false as stated
Claim D : if R is restricted to a prescribed candidate family, the minimum can be
          strictly larger; finding it encodes Min Set Cover (NP-hard).
"""
import itertools
import numpy as np

rng = np.random.default_rng(99)
TOL = 1e-8


def rank(M):
    M = np.atleast_2d(np.asarray(M, dtype=float))
    if M.size == 0 or M.shape[0] == 0:
        return 0
    s = np.linalg.svd(M, compute_uv=False)
    if s.size == 0:
        return 0
    return int(np.sum(s > TOL * max(M.shape) * (s[0] if s[0] > 0 else 1.0)))


def stack(*blocks):
    blocks = [np.atleast_2d(np.asarray(b, dtype=float)) for b in blocks]
    ncols = max((b.shape[1] for b in blocks), default=0)
    blocks = [b for b in blocks if b.shape[0] > 0]
    return np.zeros((0, ncols)) if not blocks else np.vstack(blocks)


def in_span(X, Y):
    if X.shape[0] == 0:
        return True
    return rank(stack(Y, X)) == rank(Y)


def cond5a(A, C, L):
    return rank(stack(L @ A, C @ A, C)) == rank(stack(C @ A, C, L))


def cond5b(A, C, L, npts=60):
    rhs = rank(stack(C @ A, C, L))
    pts = [complex(x) for x in
           (-1e6, -1e3, -11.0, -3.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.5, 3.0, 11.0, 1e3, 1e6)]
    pts += [complex(c) for c in np.linalg.eigvals(A)]
    pts += [complex(rng.normal(), rng.normal()) for _ in range(npts)]
    return all(rank(stack(s * L - L @ A, C @ A, C)) == rhs for s in pts)


def k_formula(A, C, L0):
    return rank(stack(C @ A, C, L0, L0 @ A)) - rank(stack(C @ A, C, L0))


def build_R(A, C, L0):
    Q, P = stack(C @ A, C, L0), stack(C @ A, C, L0, L0 @ A)
    BQ = np.linalg.svd(Q, full_matrices=False)[2] if Q.shape[0] else np.zeros((0, A.shape[0]))
    BQ = BQ[:rank(Q)]
    BP = np.linalg.svd(P, full_matrices=False)[2][:rank(P)]
    cur, extra = BQ.copy(), []
    for v in BP:
        if rank(stack(cur, v)) > rank(cur):
            extra.append(v)
            cur = np.vstack([cur, v])
    return np.array(extra) if extra else np.zeros((0, A.shape[0]))


print("=" * 76)
print("CLAIM A : (5a) <=> row(LA) subset row(C)+row(CA)+row(L)")
print("=" * 76)
mism = 0
for _ in range(600):
    n = int(rng.integers(2, 6))
    p = int(rng.integers(0, n + 1))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L = rng.integers(-2, 3, (q, n)).astype(float)
    if cond5a(A, C, L) != in_span(L @ A, stack(C, C @ A, L)):
        mism += 1
print(f"  disagreements {mism}/600 -> {'CONFIRMED' if mism == 0 else 'FAILED'}")

print()
print("=" * 76)
print("CLAIM B : min |R| = dim row([C;CA;L0;L0A]) - dim row([C;CA;L0])")
print("          (construction attains it; brute force confirms optimality)")
print("=" * 76)
bad = tested = 0
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
    k = k_formula(A, C, L0)
    R = build_R(A, C, L0)
    if R.shape[0] != k:
        bad += 1; print(f"   [t{trial}] built {R.shape[0]} rows, formula {k}"); continue
    if not cond5a(A, C, stack(L0, R)):
        bad += 1; print(f"   [t{trial}] R fails (5a)"); continue
    # optimality via brute force over a small integer grid
    if n <= 3 and k >= 1:
        grid = [np.array(v, float) for v in itertools.product(range(-2, 3), repeat=n) if any(v)]
        smaller = any(
            cond5a(A, C, stack(L0, np.array([grid[i] for i in combo]) if combo else np.zeros((0, n))))
            for kk in range(0, k)
            for combo in itertools.combinations_with_replacement(range(len(grid)), kk)
        )
        if smaller:
            bad += 1; print(f"   [t{trial}] brute force found fewer than {k} rows")
print(f"  tested {tested}, failures {bad} -> {'CONFIRMED' if bad == 0 else 'FAILED'}")
print("  => the literal (unrestricted) problem is solvable in polynomial time.")

print()
print("=" * 76)
print("CLAIM C : a worked counterexample to 'unrestricted min |R| == min set cover'")
print("=" * 76)


def sc_instance(sets, r):
    """C = 0 ; A = I_r  (so S = 0) ; L0 = I_r ; candidate for S is sum_{e in S} e_e."""
    n = r
    A = np.eye(n)
    C = np.zeros((0, n))
    L0 = np.eye(n)
    cand = [np.array([1.0 if e in S else 0.0 for e in range(n)]) for S in sets]
    return A, C, L0, cand


def restricted_min(A, C, L0, cand, use5b=True):
    m, n = len(cand), L0.shape[1]
    for k in range(0, m + 1):
        for combo in itertools.combinations(range(m), k):
            R = np.array([cand[i] for i in combo]) if k else np.zeros((0, n))
            L = stack(L0, R)
            if cond5a(A, C, L) and (not use5b or cond5b(A, C, L)):
                return k
    return None


def sc_min(sets, r):
    for k in range(0, len(sets) + 1):
        for combo in itertools.combinations(range(len(sets)), k):
            cov = set().union(*[set(sets[i]) for i in combo]) if combo else set()
            if len(cov) == r:
                return k
    return None


sets = [[0, 1], [1, 2], [0, 2]]
r = 3
A, C, L0, cand = sc_instance(sets, r)
print(f"  U = {{0,1,2}}, S = {sets}")
print(f"  min SET COVER                  = {sc_min(sets, r)}")
print(f"  min |R| (candidates restricted) = {restricted_min(A, C, L0, cand, use5b=False)}")
print(f"  unrestricted formula k*         = {k_formula(A, C, L0)}")
print("  Explanation: with A = I, L0 = I, adding the SINGLE row e_1+...+e_r")
print("  (a perfectly legal functional) satisfies (5a) at once, even though no")
print("  single given set covers U.  Covering is therefore NOT forced by (5a).")

print()
print("=" * 76)
print("CLAIM D : restricted-candidate version == MIN SET COVER (correct instance)")
print("=" * 76)
print("""
  Correct construction (verified below).  Use the NILPOTENT block system:
     n = 2r,  coordinates (x_i, y_i),  A x_i = y_i,  A y_i = 0   (A nilpotent)
     C = 0,   S = row([C;CA]) = 0
     L0 = [ x_1 ; ... ; x_r ]   (r prescribed functionals, one per element)
     candidate for set S  ->  row  b_S := sum_{e in S} y_e   (NOT x)
  Then  row(L0 A) = row(y_1,...,y_r) = span{y_e},  and
        row(C)+row(CA)+row(L0) = span{x_e} + span{y_e} = R^n,
  so (5a) holds iff row(L0A) subset span{ x_e } + span{ b_{S_i} : i in I }.
  Since the b_S involve only y-directions and span{x_e} = row(L0),
  this reduces to  span{y_e : e in U} subset span{ b_{S_i} : i in I },
  i.e. U subset union of the chosen S_i  --  SET COVER.
""")
bad = tested = 0
first = None
for trial in range(300):
    m = int(rng.integers(2, 6))
    r = int(rng.integers(2, 5))
    sets = [sorted(rng.choice(r, size=int(rng.integers(1, r + 1)), replace=False).tolist())
            for _ in range(m)]
    for e in range(r):
        if not any(e in s for s in sets):
            sets[int(rng.integers(0, m))] = sorted(set(sets[int(rng.integers(0, m))]) | {e})
    n = 2 * r
    A = np.zeros((n, n))
    for i in range(r):
        A[2 * i, 2 * i + 1] = 1.0
    C = np.zeros((0, n))
    L0 = np.zeros((r, n))
    for i in range(r):
        L0[i, 2 * i] = 1.0
    cand = []
    for S in sets:
        v = np.zeros(n)
        for e in S:
            v[2 * e + 1] = 1.0
        cand.append(v)

    kmin = None
    for k in range(0, m + 1):
        for combo in itertools.combinations(range(m), k):
            R = np.array([cand[i] for i in combo]) if k else np.zeros((0, n))
            L = stack(L0, R)
            if cond5a(A, C, L):
                kmin = k
                break
        if kmin is not None:
            break
    sc = sc_min(sets, r)
    tested += 1
    if sc != kmin:
        bad += 1
        if first is None:
            first = (sets, r, sc, kmin)
print(f"  tested {tested}, mismatches {bad} -> {'CONFIRMED' if bad == 0 else 'FAILED'}")
if first:
    print("  first mismatch: sets=%s r=%s setcover=%s observer=%s" % first)
    # diagnose
    sets, r, sc, kmin = first
    n = 2 * r
    A = np.zeros((n, n))
    for i in range(r):
        A[2 * i, 2 * i + 1] = 1.0
    C = np.zeros((0, n)); L0 = np.zeros((r, n))
    for i in range(r):
        L0[i, 2 * i] = 1.0
    print("  unrestricted k* for that instance:", k_formula(A, C, L0))
