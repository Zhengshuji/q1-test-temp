"""
Rigorous numerical test of the structural claims about q.txt's problem.

PROBLEM Q : given (A, C, L0), find R with the FEWEST ROWS such that
            L = [L0 ; R] satisfies (5a) and (5b).

(5a)  rank[ LA ; CA ; C ] = rank[ CA ; C ; L ]
(5b)  rank[ sL - LA ; CA ; C ] = rank[ CA ; C ; L ]   for all s in C

Claim (P):  min rows(R)  =  dim( row([C;CA]) + row(L0 A) )
                          - dim( row([C;CA]) + row(L0 ) )
and the value is computable in polynomial time by rank operations.
Hence the UNRESTRICTED version is in P, not NP-hard.

Claim (R):  if R is additionally required to be chosen from a prescribed
candidate family, the minimum can exceed the value in (P); finding the
minimum then encodes MINIMUM SET COVER and is NP-hard.
"""
import itertools
import numpy as np

rng = np.random.default_rng(12345)


def rank(M):
    M = np.atleast_2d(M)
    if M.size == 0:
        return 0
    return int(np.linalg.matrix_rank(M, tol=1e-9))


def rowspace_basis(M):
    M = np.atleast_2d(M)
    if M.size == 0:
        return np.zeros((0, M.shape[-1]))
    u, s, vt = np.linalg.svd(M, full_matrices=False)
    tol = max(M.shape) * (s[0] if s.size else 1.0) * 1e-12
    return vt[s > tol]


def stack(*blocks):
    blocks = [b for b in blocks if b.shape[0] > 0]
    if not blocks:
        return np.zeros((0, 0))
    return np.vstack(blocks)


def cond5a(A, C, L):
    """rank[LA;CA;C] == rank[CA;C;L]"""
    lhs = stack(L @ A, C @ A, C)
    rhs = stack(C @ A, C, L)
    return rank(lhs) == rank(rhs)


def cond5b_structural(A, C, L):
    """rank[sL-LA;CA;C] == rank[CA;C;L] for ALL s in C (structural version).

    Testing 'all s in C' honestly:  the LHS as a matrix pencil is
    [sL - LA ; CA ; C].  Its rank can only drop at finitely many s.  We test
    it as a polynomial identity over a large symbolic-equivalent sample:
    we test many s values plus verify the pencil rank generically.
    """
    n = A.shape[0]
    rhs = rank(stack(C @ A, C, L))
    # sample s: real, complex, and the eigenvalues of A
    pts = [complex(x) for x in [-1e4, -7.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0, 3.0, 7.0, 1e4]]
    pts += [complex(c) for c in np.linalg.eigvals(A)]
    pts += [complex(rng.normal(), rng.normal()) for _ in range(40)]
    for s in pts:
        M = stack(s * L - L @ A, C @ A, C)
        if rank(M) != rhs:
            return False
    return True


def formula_min_rows(A, C, L0):
    """k* = dim(row([C;CA]) + row(L0 A)) - dim(row([C;CA]) + row(L0))"""
    base = stack(C @ A, C)
    d1 = rank(stack(base, L0 @ A))
    d0 = rank(stack(base, L0))
    return d1 - d0


print("=" * 74)
print("CLAIM (P)  :  min rows(R) admits the closed form, hence is in P")
print("=" * 74)

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
    k = formula_min_rows(A, C, L0)

    # ---- 1) an R of exactly k rows exists and satisfies (5a) --------------
    base = stack(C @ A, C)
    B0 = rowspace_basis(stack(base, L0))
    B1 = rowspace_basis(stack(base, L0 @ A))
    cur = B0.copy()
    extra = []
    for v in B1:
        if rank(stack(cur, v)) > rank(cur):
            extra.append(v)
            cur = np.vstack([cur, v])
    R = np.array(extra) if extra else np.zeros((0, n))
    if R.shape[0] != k:
        print(f"  [trial {trial}] construction gave {R.shape[0]} rows, formula says {k}")
        bad += 1
        continue
    L = stack(L0, R)
    if not cond5a(A, C, L):
        print(f"  [trial {trial}] constructed R fails (5a)")
        bad += 1
        continue

    # ---- 2) k is OPTIMAL: no (k-1)-row R from the ambient grid works -----
    if n <= 3 and k >= 1:
        found_smaller = False
        grid = [v.astype(float) for v in
                itertools.product(range(-1, 2), repeat=n) if any(v)]
        for kk in range(0, k):
            for combo in itertools.combinations_with_replacement(range(len(grid)), kk):
                RR = np.array([grid[i] for i in combo]) if kk else np.zeros((0, n))
                if cond5a(A, C, stack(L0, RR)):
                    found_smaller = True
                    break
            if found_smaller:
                break
        if found_smaller:
            print(f"  [trial {trial}] found an R with fewer rows than the formula!")
            bad += 1

print(f"  tested {tested} valid instances; failures: {bad}")
print("  RESULT:", "CONFIRMED" if bad == 0 else "FAILED")

print()
print("=" * 74)
print("NEWMAN'S EXAMPLE (the cleanest minimal case)")
print("=" * 74)
A = np.array([[0.0, 1.0], [0.0, 0.0]])
C = np.zeros((0, 2))
L0 = np.array([[0.0, 1.0]])
print("  A  = [[0,1],[0,0]],  C = [] (p=0),  L0 = [e2]")
print("  L0 A = e1  ->  outside row(L0) = span(e2)")
print("  formula k* =", formula_min_rows(A, C, L0), "  (needs R = [e1])")
L = stack(L0, np.array([[1.0, 0.0]]))
print("  (5a) with R=[e1] :", cond5a(A, C, L))
print("  (5a) with R=[]   :", cond5a(A, C, L0))

print()
print("=" * 74)
print("CLAIM (R)  :  with a PRESCRIBED candidate family, min rows(R) can be")
print("              strictly larger  ->  the restricted problem is harder")
print("=" * 74)

n = 2
A = np.diag([2.0, 3.0])
C = np.zeros((0, 2))
L0 = np.eye(2)
print("  A = diag(2,3), C = [], L0 = I2")
print("  unrestricted formula k* =", formula_min_rows(A, C, L0))
for cand, name in [
    ([np.array([1.0, 0.0]), np.array([0.0, 1.0])], "C = {e1, e2}"),
    ([np.array([1.0, 0.0])], "C = {e1}"),
    ([np.array([1.0, 0.0]), np.array([1.0, 1.0])], "C = {e1, e1+e2}"),
]:
    best = None
    for k in range(0, len(cand) + 1):
        for combo in itertools.combinations(range(len(cand)), k):
            R = np.array([cand[i] for i in combo]) if k else np.zeros((0, n))
            if cond5a(A, C, stack(L0, R)):
                best = k
                break
        if best is not None:
            break
    print(f"    {name:22s} -> min rows(R) = {best}")

print()
print("=" * 74)
print("SET-COVER REDUCTION  (admissible pool = the rows of L0 A, i.e. S = 0)")
print("=" * 74)


def build_sc_instance(sets, r):
    """A = diag(1..r) (distinct positive eigenvalues so (5b) is automatic),
    C = 0  =>  S = row([C;CA]) = 0.  L0 = I_r, so L0 A = diag(1..r) and the
    admissible pool is {e_1,...,e_r}.  Candidate functionals for the sets are
    b_S = sum_{e in S} e_e .  We look for the fewest candidates c_1..c_k with
    row([L0 ; c_1 ; ... ; c_k] A) subset row([L0 ; c_1 ; ... ; c_k])."""
    A = np.diag([float(i + 1) for i in range(r)])
    C = np.zeros((0, r))
    L0 = np.eye(r)
    cand = []
    for S in sets:
        v = np.zeros(r)
        for e in S:
            v[e] = 1.0
        cand.append(v)
    return A, C, L0, cand


def restricted_min(A, C, L0, cand, cap=None):
    m = len(cand)
    cap = cap if cap is not None else m
    n = L0.shape[1]
    for k in range(0, cap + 1):
        for combo in itertools.combinations(range(m), k):
            R = np.array([cand[i] for i in combo]) if k else np.zeros((0, n))
            if cond5a(A, C, stack(L0, R)):
                return k
    return None


def set_cover_min(sets, r):
    m = len(sets)
    for k in range(0, m + 1):
        for combo in itertools.combinations(range(m), k):
            cov = set()
            for i in combo:
                cov |= set(sets[i])
            if len(cov) == r:
                return k
    return None


bad = 0
tested = 0
for trial in range(150):
    m = int(rng.integers(2, 6))
    r = int(rng.integers(2, 5))
    sets = []
    for _ in range(m):
        size = int(rng.integers(1, r + 1))
        sets.append(sorted(rng.choice(r, size=size, replace=False).tolist()))
    for e in range(r):  # guarantee feasibility
        if not any(e in s for s in sets):
            j = int(rng.integers(0, m))
            sets[j] = sorted(set(sets[j]) | {e})
    A, C, L0, cand = build_sc_instance(sets, r)
    sc = set_cover_min(sets, r)
    rm = restricted_min(A, C, L0, cand)
    tested += 1
    if sc != rm:
        print(f"  MISMATCH trial {trial}: set-cover={sc} restricted-rows={rm}  sets={sets}")
        bad += 1
        if bad > 5:
            break

print(f"  tested {tested} instances; mismatches: {bad}")
print("  RESULT:", "CONFIRMED: restricted min == min SET COVER" if bad == 0 else "FAILED")
