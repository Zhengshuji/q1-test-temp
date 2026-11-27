"""c198_graphic_matroid.py -- targeted test of the "coordinate is optimal" gadget.

Setting (the coordinate layer of MATROID_LEMMA.md):
  * A = diag(1,...,n) with distinct eigenvalues,
  * J = row[C; CA]  (realisable observation space),
  * V coordinate (span of e_j, j in S)  =>  (5a) automatic and
        (5b)  <=>  S is a union of circuits of the matroid M = (pi(e_j)),
    pi : Q^n -> Q^n / J.

The "hardness" route in MATROID_LEMMA.md wants M to be a GRAPHIC matroid (then the
coordinate-layer problem contains the Tree Augmentation Problem).  This script:

  1. builds M = M(K_4) explicitly (incidence matrix of K_4, 6 edges, rank 3),
  2. finds C with row[C; CA] = J = ker(incidence),
  3. verifies the matroid of the instance really is M(K_4) (rank 3, the four triangles
     are circuits),
  4. computes q_coord = min |S| over unions of circuits containing a prescribed edge,
  5. searches over NON-coordinate V = span(e_1, u), u in a box, for feasible ones
     with dim 2 < q_coord     -- a hit would break the "coordinate is optimal" gadget.

USAGE
    python tools/p_algorithm/c198_graphic_matroid.py
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.join("tools", "exact_linalg"))
import audit_independent as AI

# ---------------------------------------------------------------- K_4
# vertices 0..3, edges as (vertex pair); index them 0..5
EDGES = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
n = 6
VERT = 4


def incidence():
    """4 x 6 vertex-edge incidence matrix over Q"""
    B = [[Fr(0)] * n for _ in range(VERT)]
    for j, (a, b) in enumerate(EDGES):
        B[a][j] = Fr(1)
        B[b][j] = Fr(-1)
    return B


def kernel_basis(M):
    """basis of {x in Q^cols : M x = 0}, as row vectors of length cols"""
    R, piv = AI.rref(M)
    cols = len(M[0])
    free = [c for c in range(cols) if c not in piv]
    out = []
    for f in free:
        v = [Fr(0)] * cols
        v[f] = Fr(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][f]
        out.append(v)
    return out


def main():
    A = [[Fr(1 + i) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    B = incidence()
    J = AI.row_basis(kernel_basis(B))          # J = ker B, dim 3
    j = AI.rank(J)
    print("=" * 90)
    print("c198 -- graphic matroid M(K_4) inside the coordinate layer")
    print("=" * 90)
    print(f"  n={n}  rank of incidence = {AI.rank(B)}  dim J = {j}")

    # --- find C with row[C; CA] = J :  try all subsets of a basis of J
    Jb = [list(x) for x in J]
    gens = [list(x) for x in Jb]
    for a in range(len(Jb)):
        for b in range(a + 1, len(Jb)):
            gens.append([Jb[a][t] + Jb[b][t] for t in range(n)])
            gens.append([Jb[a][t] - Jb[b][t] for t in range(n)])
    C = None
    for k in (1, 2, 3):
        for combo in itertools.combinations(range(len(gens)), k):
            cand = [gens[i] for i in combo]
            if AI.rank(cand) != k:
                continue
            R = AI.row_basis(AI.vstack([cand, AI.mul(cand, A)]))
            if AI.rank(R) == j and AI.rank(AI.vstack([R, J])) == j:
                C = cand
                break
        if C is not None:
            break
    print(f"  C found with row[C;CA] = J : {C is not None}, |C| = {len(C) if C else 0}, "
          f"dim row[C;CA] = {AI.rank(AI.vstack(C, AI.mul(C, A))) if C else 0}")

    # --- the matroid M = (pi(e_i)) :  coordinates of e_i modulo J
    N = None
    comp = []
    for i in range(n):
        v = [Fr(0)] * n
        v[i] = Fr(1)
        if AI.rank(AI.vstack([J] + [[c] for c in comp] + [[v]])) == j + len(comp) + 1:
            comp.append(v)
    base = AI.vstack(J, comp)
    d = len(comp)

    def pi(x):
        """coordinates of x in V/J (basis comp)"""
        k = len(base)
        Mx = [[base[t][s] for t in range(k)] + [x[s]] for s in range(n)]
        R, piv = AI.rref(Mx)
        co = [Fr(0)] * k
        for t, pc in enumerate(piv):
            if pc < k:
                co[pc] = R[t][k]
        return co[j:]

    vec = [pi([Fr(1) if s == i else Fr(0) for s in range(n)]) for i in range(n)]
    print(f"  d = {d},  ranks: r(all) = {AI.rank(vec)}")
    # circuits of M(K_4) = the four triangles
    tri = []
    for a, b, c in itertools.combinations(range(VERT), 3):
        e = []
        for pair in ((a, b), (a, c), (b, c)):
            e.append(EDGES.index(pair))
        tri.append(sorted(e))
    print("  triangles (should be circuits of the instance matroid):")
    for T in tri:
        rT = AI.rank([vec[i] for i in T])
        rTm = AI.rank([vec[i] for i in T if i != T[0]])
        print(f"    edges {T}: rank {rT}, rank minus one {rTm} "
              f"{'circuit' if rT == rTm else 'NOT a circuit'}")

    # --- q_coord : min |S| with supp in S and S a union of circuits (no coloop)
    supp0 = [0]                       # K_0 = span{e_0}
    def no_coloop(S):
        rS = AI.rank([vec[i] for i in S])
        return all(AI.rank([vec[j] for j in S if j != i]) == rS for i in S)

    qc = None
    for k in range(len(supp0), n + 1):
        for S in itertools.combinations(range(n), k):
            if not set(supp0) <= set(S):
                continue
            if AI.rank([vec[i] for i in S]) < len(S) and no_coloop(list(S)):
                qc = k
                break
        if qc is not None:
            break
    print(f"\n  q_coord (min union of circuits containing e_0) = {qc}")

    # --- non-coordinate search: V = span(e_0, u), u in a box, exact over Q
    e0 = [Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)]
    hits = []
    tested = 0
    if qc is not None and qc > 2:
        box = 2
        for u in itertools.product(range(-box, box + 1), repeat=n):
            if all(x == 0 for x in u):
                continue
            uu = [Fr(x) for x in u]
            V = [e0, uu]
            if AI.rank(V) != 2:
                continue
            tested += 1
            if AI.rank(AI.vstack([V, AI.mul(V, A)])) != AI.rank(V):
                continue                                  # (5a) fails
            if AI.cond_5b_orig(A, C, V):
                hits.append((u, V))
                break
    print(f"  non-coordinate scan: tested {tested} subspaces span(e0,u), u in [-2,2]^6")
    if hits:
        u, V = hits[0]
        print(f"  ** HIT **: V = span(e0, {list(u)}) is feasible with dim 2 < q_coord = {qc}")
        print("     => non-coordinate is strictly better; the 'coordinate is optimal' gadget fails here")
    else:
        print("  no non-coordinate feasible subspace of dim 2 found")
        print("  => consistent with the gadget (coordinate optimal on this instance)")


if __name__ == "__main__":
    main()
