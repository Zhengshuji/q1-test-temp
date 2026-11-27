"""tools/layer_search/c200_q5_probe.py

Q5 probe: does "controllable" (mod B) imply (5b)?

For random exact-rational instances we build a triple (U, H, tau) -> V explicitly and check

    (5a)            exact
    (i)  controllability of (S_tau, beta|_H) on (U+B)/B
    (5b)            exact  (== "(ii) dim R_lambda = rho for all lambda")

and report every case with  (5a) and (i) hold but (5b) fails  -> a Q5 counterexample.
We also record whether B subset U (the case where Q5 is PROVED, see
proof/controllability_equivalence/theorem.md 推论 3.2).

USAGE
    python tools/layer_search/c200_q5_probe.py            # random probes
    python tools/layer_search/c200_q5_probe.py --n 5 --trials 400
"""
import os
import random
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "exact_linalg"))
import audit_independent as AI  # noqa: E402


# ---------------------------------------------------------------- linear algebra helpers
def complement(B, m):
    Bb = AI.row_basis(B) if B else []
    C = []
    for i in range(m):
        v = [Fr(0)] * m
        v[i] = Fr(1)
        if AI.rank(AI.vstack([Bb] + [[c] for c in C] + [[v]])) == len(Bb) + len(C) + 1:
            C.append(v)
    return C


def coords_in(base, x):
    k = len(base)
    Mx = [[base[t][s] for t in range(k)] + [x[s]] for s in range(len(x))]
    R, piv = AI.rref(Mx)
    co = [Fr(0)] * k
    for t, pc in enumerate(piv):
        if pc < k:
            co[pc] = R[t][k]
    chk = [sum(co[t] * base[t][s] for t in range(k)) for s in range(len(x))]
    return co if chk == list(x) else None


def rand_row(n, rng, lo=-2, hi=2):
    return [Fr(rng.randint(lo, hi)) for _ in range(n)]


def span(rows, k, d, rng, tries=200):
    """random k-dim subspace of C^d (as a list of k independent rows)"""
    out = []
    for _ in range(tries):
        if len(out) == k:
            break
        v = rand_row(d, rng)
        if AI.rank(out + [v]) == len(out) + 1:
            out.append(v)
    return out if len(out) == k else None


def build(A, C):
    n = len(A)
    CA = AI.mul(C, A)
    J = AI.row_basis(AI.vstack([C, CA]))
    j, d = len(J), n - len(J)
    W = complement(J, n)
    if len(W) != d:
        return None
    base = J + W

    def pi(x):
        co = coords_in(base, x)
        return co[j:] if co is not None else None

    B = AI.row_basis([pi(AI.mul([r], A)[0]) for r in J]) if j else []
    return dict(n=n, J=J, j=j, d=d, W=W, pi=pi, B=B)


def make_V(D, A, U, H, tau):
    """V = span{ s(u_i) + tau(u_i) } + H   (s = the section through W)"""
    j, d = D['j'], D['d']
    rows = []
    for i, u in enumerate(U):
        vec = [sum(u[k] * D['W'][k][t] for k in range(d)) for t in range(D['n'])]   # s(u)
        tvec = tau[i]                                                              # J-coords
        add = [sum(tvec[k] * D['J'][k][t] for k in range(j)) for t in range(D['n'])]  # tau(u)
        rows.append([vec[t] + add[t] for t in range(D['n'])])
    for h in H:                                                                     # H in J-coords
        rows.append([sum(h[k] * D['J'][k][t] for k in range(j)) for t in range(D['n'])])
    return rows


def controllable(D, A, U, H, tau):
    """(i): reachable set of (S_tau, beta|_H) mod B fills (U+B)/B ?

    Everything is tracked in U-coordinates modulo B: a vector x in U+B is decomposed as
    x = sum c_i u_i + b (b in B) and represented by c.  Then dim of the reached set is
    compared with dim (U+B)/B.
    """
    j, d = D['j'], D['d']
    B = D['B']
    rho = len(U)

    def decompose(x):
        M = [[U[t][s] for t in range(rho)] + [B[t][s] for t in range(len(B))] + [x[s]]
             for s in range(d)]
        R, piv = AI.rref(M)
        k = rho + len(B)
        for t, pc in enumerate(piv):
            if pc == k:
                return None
        co = [Fr(0)] * k
        for t, pc in enumerate(piv):
            if pc < k:
                co[pc] = R[t][k]
        return co[:rho]

    def S_vec(i):
        su = [sum(U[i][k] * D['W'][k][t] for k in range(d)) for t in range(D['n'])]
        Tu = D['pi'](AI.mul([su], A)[0])
        hc = tau[i]
        vec = [sum(hc[k] * D['J'][k][t] for k in range(j)) for t in range(D['n'])]
        b = D['pi'](AI.mul([vec], A)[0])
        return [Tu[q] + b[q] for q in range(d)]

    Scols = [S_vec(i) for i in range(rho)]

    def beta_of(hcoords):
        vec = [sum(hcoords[k] * D['J'][k][t] for k in range(j)) for t in range(D['n'])]
        return D['pi'](AI.mul([vec], A)[0])

    R = []
    for h in H:
        c = decompose(beta_of(h))
        if c is not None:
            R.append(c)
    R = AI.row_basis(R) if R else []
    for _ in range(rho + 2):
        grown = list(R)
        for c in R:
            img = [sum(c[i] * Scols[i][q] for i in range(rho)) for q in range(d)]
            cc = decompose(img)
            if cc is not None:
                grown.append(cc)
        grown = AI.row_basis(grown) if grown else []
        if len(grown) == len(R):
            break
        R = grown
    target = AI.rank([U[i] for i in range(rho)] + [b for b in B]) - len(B)
    return len(R) == target, len(R), target


def solve_tau(D, A, U, H):
    """solve condition (A) of c192 for tau: (5a) <=> T(U) subset U+B  AND  beta(H) subset U"""
    j, d = D['j'], D['d']
    # beta(H) subset U ?
    if H:
        for h in H:
            vec = [sum(h[k] * D['J'][k][t] for k in range(j)) for t in range(D['n'])]
            bh = D['pi'](AI.mul([vec], A)[0])
            if AI.rank(AI.vstack([U, [bh]])) != len(U):
                return None                      # (5a) impossible for this (U,H)
    # unknown tau[i][k], i<rho, k<j   ->  index i*j+k
    rho = len(U)
    rows, rhs = [], []
    Uperp = AI.nullspace(U) if hasattr(AI, 'nullspace') else None
    if Uperp is None:
        # nullspace of U (rows) computed by rref of [U | I]
        M = [list(U[i]) + [Fr(1) if t == i else Fr(0) for t in range(rho)] for i in range(rho)]
        R, piv = AI.rref(M)
        Uperp = [[R[t][d + q] for t in range(len(R))] for q in range(rho)]
        Uperp = [v for v in Uperp if any(x != 0 for x in v)]
    betaJ = [D['pi'](AI.mul([D['J'][k]], A)[0]) for k in range(j)]
    for i, u in enumerate(U):
        su = [sum(u[k] * D['W'][k][t] for k in range(d)) for t in range(D['n'])]
        Tu = D['pi'](AI.mul([su], A)[0])
        for q in Uperp:
            if all(x == 0 for x in q):
                continue
            row = [Fr(0)] * (rho * j)
            for k in range(j):
                row[i * j + k] = sum(q[t] * betaJ[k][t] for t in range(d))
            rows.append(row)
            rhs.append(-sum(q[t] * Tu[t] for t in range(d)))
    if not rows:
        return [[Fr(0)] * j for _ in range(rho)]
    M = [rows[i] + [rhs[i]] for i in range(len(rows))]
    R, piv = AI.rref(M)
    ncol = rho * j
    # inconsistent if a pivot sits in the last column
    for t, pc in enumerate(piv):
        if pc == ncol:
            return None
    sol = [Fr(0)] * ncol
    for t, pc in enumerate(piv):
        if pc < ncol:
            sol[pc] = R[t][ncol]
    return [sol[i * j:(i + 1) * j] for i in range(rho)]


def main():
    rng = random.Random(4242)
    n, trials = 5, 200
    if '--n' in sys.argv:
        n = int(sys.argv[sys.argv.index('--n') + 1])
    if '--trials' in sys.argv:
        trials = int(sys.argv[sys.argv.index('--trials') + 1])
    print('=' * 96)
    print('Q5 probe:  (5a) & controllable(mod B)  but  (5b) fails ?')
    print('=' * 96)
    stats = dict(inst=0, cand=0, viol=0, b_not_in_u=0, i_ok=0)
    examples = []
    for _ in range(trials):
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        p = rng.choice([1, 2])
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        if AI.rank(C) != p:
            continue
        D = build(A, C)
        if D is None or D['d'] < 2 or D['j'] < 1:
            continue
        stats['inst'] += 1
        for _rep in range(6):
            rho = rng.choice([1, 2]) if D['d'] > 2 else 1
            c = rng.choice([1, 1, 2])
            U = span(None, rho, D['d'], rng)
            if U is None:
                continue
            H = span(None, min(c, D['j']), D['j'], rng)
            if H is None:
                continue
            tau = solve_tau(D, A, U, H)
            if tau is None:
                continue
            V = make_V(D, A, U, H, tau)
            if AI.rank(V) != len(V) or not AI.cond_5a_orig(A, C, V):
                continue
            stats['cand'] += 1
            B_in_U = (not D['B']) or AI.rank(AI.vstack([U] + [[b] for b in D['B']])) == len(U)
            if not B_in_U:
                stats['b_not_in_u'] += 1
            ok5b = AI.cond_5b_orig(A, C, V)
            ctrl, r, tgt = controllable(D, A, U, H, tau)
            stats.setdefault('both', 0); stats.setdefault('only5b', 0); stats.setdefault('onlyi', 0)
            if ctrl:
                stats['i_ok'] += 1
            if ctrl and ok5b:
                stats['both'] += 1
            if ok5b and not ctrl:
                stats['only5b'] += 1
            if ctrl and not ok5b:
                stats['onlyi'] += 1
                stats['viol'] += 1
            if False:
                examples.append(dict(A=[[str(x) for x in row] for row in A],
                                     C=[[str(x) for x in row] for row in C],
                                     U=[[str(x) for x in row] for row in U],
                                     H=[[str(x) for x in row] for row in H],
                                     tau=[[str(x) for x in row] for row in tau],
                                     B_in_U=B_in_U))
    print(f"  instances probed        : {stats['inst']}")
    print(f"  (5a)-feasible triples   : {stats['cand']}")
    print(f"  ... with B not subset U : {stats['b_not_in_u']}")
    print(f"  controllable (mod B)    : {stats['i_ok']}")
    print(f"  COUNTEREXAMPLES to Q5   : {stats['viol']}")
    for e in examples:
        print('   ', e)
    print()
    print('a counterexample = "controllable but (5b) fails"  ->  Q5 FALSE in general;')
    print('then the extra condition (ii) of proof/controllability_equivalence §4 is necessary.')


if __name__ == '__main__':
    main()
