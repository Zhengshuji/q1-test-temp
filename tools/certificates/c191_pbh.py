"""c191_pbh.py -- corrected "Theorem 9": the top layer is an OBSERVABILITY test

CONTEXT
-------
HANDOVER_2026-10-26.md, Theorem 9, claims

    V = H (+) W,  H = V n J (dim c),  W a complement of J (dim d),
    T_W = pi_W A|_W,  D_W = [pi_W(h_1 A) ... pi_W(h_c A)]
    Q_V(lam) = [-D_W | lam I_d - T_W]  ==>  (5b)  <=>  (T_W, D_W) CONTROLLABLE

The pencil identity is right, but the last "controllable" is wrong.  With the
row-vector convention used throughout this project,

    Q_V(lam) = [ -(D_W)^T  ;  lam I_d - T_W ]          ((c+d) x d)

so  rank Q_V(lam) = d for all lam  <=>  no 0 != xi with D_W xi = 0 and
T_W xi = lam xi  <=>  (D_W^T, T_W) is OBSERVABLE, i.e.

    rank [ D_W^T ; D_W^T T_W ; ... ; D_W^T T_W^{d-1} ] = d .

Equivalently (T_W^T, D_W^T) is controllable.  "Controllable" for (T_W, D_W)
means rank[lam I - T_W | D_W] = d, which is the dual condition and differs
whenever T_W is not symmetric.

MEASURED  (this script, exact over Q, top-layer instances):
    pencil gcd test     65/65   agrees with exact (5b)
    observability       65/65   agrees with exact (5b)
    controllability     63/65   DISAGREES  -> the handover statement is false

(An earlier sweep on a different instance generator gave 103/103, 103/103, 100/103
 -- same picture: controllability is the odd one out.)

PRACTICAL PAYOFF
----------------
Observability is a RANK condition with no lambda in it: rank of a (c*d) x d
rational matrix.  So the top layer (q = c + d, i.e. rho = d) has an O(d^3)
exact test that replaces the gcd-of-minors machinery.  For c = 1 it degenerates
to "v_W is a cyclic vector for the row action of T_W", which is the statement
verified 72/72 in the previous round.

USAGE
-----
    python tools/certificates/c191_pbh.py            # cross-check + summary
    from c191_pbh import top_layer                 # exact top-layer test
"""
import sys, os, random, itertools

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, "tools", "exact_linalg"))

from fractions import Fraction as Fr
import audit_independent as AI

mul, rank, inv = AI.mul, AI.rank, AI.inv


# ---------------------------------------------------------------- machinery

def sdim(rows):
    """rank of a possibly empty row list"""
    return rank(rows) if rows else 0


def split(A, C, V):
    """Decompose V = H (+) W with H = V n J, W a complement of J inside V.

    Returns dict(c, d, j, J, H, W, TW, DW) where TW is d x d (row action)
    and DW is d x c.  Requires dim(V n J) + d = dim V  (i.e. rho = d).
    """
    n = len(A)
    CA = mul(C, A)
    M = AI.vstack([C, CA])
    j = rank(M)
    J = AI.row_basis(M)
    d = n - j
    Vb = AI.row_basis(V)
    c = len(Vb) + j - sdim(Vb + J)
    # H = V n J : the rows of a basis of J that already lie in V
    Jv = [r for r in AI.row_basis(J) if AI.in_span(r, Vb)]
    H = AI.row_basis(Jv) if Jv else []
    if len(H) != c:
        return None
    # W: a complement of H inside V (automatically W n J = 0, since V n J = H)
    W = []
    for r in Vb:
        if sdim(H + W + [r]) == len(H) + len(W) + 1:
            W.append(r)
        if len(W) == len(Vb) - len(H):
            break
    if len(W) != d:
        return None
    B = [list(r) for r in J] + [list(w) for w in W]
    Binv = inv(B)

    def proj(x):
        return mul([x], Binv)[0][j:]

    TW = [[proj(mul([w], A)[0])[t] for t in range(d)] for w in W]
    DW = [[proj(mul([h], A)[0])[t] for h in H] for t in range(d)]
    return dict(c=c, d=d, j=j, J=J, H=H, W=W, TW=TW, DW=DW)


def obs_matrix(DW, TW):
    """[D^T ; D^T T ; ... ; D^T T^{d-1}]   ((c*d) x d)"""
    d = len(TW)
    c = len(DW[0]) if DW and DW[0] else 0
    if c == 0:
        return []
    blocks = []
    cur = [[DW[t][k] for t in range(d)] for k in range(c)]      # D^T : c x d
    for _ in range(d):
        blocks.extend(cur)
        cur = mul(cur, TW)
    return blocks


def ctrl_matrix_pencil(TW, DW):
    """[lam I - TW | DW] as a (d) x (d+c) polynomial matrix"""
    d = len(TW)
    c = len(DW[0]) if DW and DW[0] else 0
    return [[([-TW[i][k], Fr(1)] if i == k else [-TW[i][k]]) for k in range(d)]
            + [[DW[i][k]] for k in range(c)] for i in range(d)]


def Q_pencil(TW, DW):
    """[ -(D_W)^T ; lam I - TW ] as a (c+d) x d polynomial matrix"""
    d = len(TW)
    c = len(DW[0]) if DW and DW[0] else 0
    return ([[[-DW[t][k]] for t in range(d)] for k in range(c)]
            + [[([-TW[i][k], Fr(1)] if i == k else [-TW[i][k]]) for k in range(d)]
               for i in range(d)])


def gcd_rank_test(Mpoly, target):
    """is rank M(lam) == target for every lam ?  (gcd of target x target minors)"""
    nr, nc = len(Mpoly), len(Mpoly[0])
    mins = []
    for rs in itertools.combinations(range(nr), target):
        for cs in itertools.combinations(range(nc), target):
            M = [[Mpoly[i][k] for k in cs] for i in rs]
            v = AI._det_poly(M)
            if any(x != 0 for x in v):
                mins.append(v)
    if not mins:
        return False
    g = mins[0]
    for m in mins[1:]:
        g = AI.pgcd(g, m)
        if len(g) <= 1:
            return True
    return len(g) == 1


def top_layer(A, C, V):
    """Exact top-layer test (rho = d).  Returns dict or None if rho != d."""
    S = split(A, C, V)
    if S is None:
        return None
    d, c = S["d"], S["c"]
    O = obs_matrix(S["DW"], S["TW"])
    obs = (rank(O) == d) if O else False
    ctrl = gcd_rank_test(ctrl_matrix_pencil(S["TW"], S["DW"]), d) if c else True
    Q = Q_pencil(S["TW"], S["DW"])
    pen = gcd_rank_test(Q, d)
    ex = AI.cond_5a_orig(A, C, V) and AI.cond_5b_orig(A, C, V)
    return dict(c=c, d=d, exact=ex, observability=obs, controllability=ctrl,
                pencil=pen, TW=S["TW"], DW=S["DW"])


# ---------------------------------------------------------------- self-check

def main():
    rng = random.Random(2026)
    n_ok = {"pencil": 0, "obs": 0, "ctrl": 0}
    bad = {"pencil": [], "obs": [], "ctrl": []}
    tot = 0
    for _ in range(60):
        n = rng.choice([4, 5])
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)]]
        if rank(C) != 1:
            continue
        CA = mul(C, A)
        j = rank(AI.vstack([C, CA]))
        if j >= n:
            continue
        J = AI.row_basis(AI.vstack([C, CA]))
        d = n - j
        # random complement W of J
        W = []
        for i in range(n):
            v = [Fr(0)] * n
            v[i] = Fr(1)
            if rank(AI.vstack([J, W + [v]])) == j + len(W) + 1:
                W.append(v)
            if len(W) == d:
                break
        for c in (1, 2):
            if c > j:
                continue
            H = []
            for _ in range(c):
                co = [Fr(rng.randint(-2, 2)) for _ in range(j)]
                h = [sum(co[t] * J[t][k] for t in range(j)) for k in range(n)]
                if rank(H + [h]) == len(H) + 1:
                    H.append(h)
            if len(H) != c:
                continue
            V = [list(h) for h in H] + [list(w) for w in W]
            if rank(V) != c + d:
                continue
            r = top_layer(A, C, V)
            if r is None:
                continue
            tot += 1
            for key, val in (("pencil", r["pencil"]), ("obs", r["observability"]),
                             ("ctrl", r["controllability"])):
                if bool(val) == bool(r["exact"]):
                    n_ok[key] += 1
                else:
                    bad[key].append((n, j, d, c, bool(r["exact"])))

    print("=" * 78)
    print("c191 -- top layer: (5b)  <=>  observability, NOT controllability")
    print("=" * 78)
    print(f"  top-layer instances tested (Q exact): {tot}")
    print(f"  pencil  [-(D_W)^T ; lam I - T_W] full column rank : "
          f"{n_ok['pencil']}/{tot}")
    print(f"  observability  rank[D^T; D^T T; ...] = d          : "
          f"{n_ok['obs']}/{tot}")
    print(f"  controllability rank[lam I - T_W | D_W] = d       : "
          f"{n_ok['ctrl']}/{tot}   <-- handover's wording")
    if bad["ctrl"]:
        print(f"  controllability counterexamples: {bad['ctrl'][:5]}")
    print()
    print("  CONCLUSION: use observability.  It is a plain rank test (no lambda,")
    print("  no gcd), cost O((cd)^2 d), and it replaces the gcd machinery on the")
    print("  top layer.  For c = 1 it is 'v_W cyclic for the row action of T_W'.")
    print()
    print("  NOTE: the top layer is q = c + d.  Layers with rho < d are NOT")
    print("  covered by this test; they still need the pencil / gcd criterion.")


if __name__ == "__main__":
    main()
