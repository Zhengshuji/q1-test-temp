"""tools/layer_search/c199_floor_gap.py

MAINLINE (docs/05 Q1): how far is the (5a)-floor from the truth?

    rho_ci = P(T, B, U0)        the smallest rho allowed by (5a) alone  [computable, O(n^4)]
    rho*   = min rho over all (5a)&(5b) solutions                       [exhaustive here]

If rho_ci = rho* generically, the layer scan collapses to one layer and q1 is
"one polynomial test away" from a polynomial algorithm.  If the gap is often > 0,
we must understand which layers the floor misses.

Both quantities are computed over the same field F_p, so the comparison is internally
consistent (the F_p-vs-Q caveat applies to both equally).

USAGE
    python tools/layer_search/c199_floor_gap.py            # n=4,5 ; p=5,7
"""
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import c192_reduced_search as R  # noqa: E402


# ---------------------------------------------------------------- small helpers (F_p)
def basis(rows, p):
    return [list(r) for r in R.rref(rows, p)[0]] if rows else []


def complement(B, m, p):
    Bb = basis(B, p)
    C = []
    for i in range(m):
        v = [0] * m
        v[i] = 1
        if R.rank(Bb + C + [v], p) == len(Bb) + len(C) + 1:
            C.append(v)
    return C


def coords(base, x, p):
    k = len(base)
    Mx = [[base[t][s] for t in range(k)] + [x[s]] for s in range(len(x))]
    Rm, piv = R.rref(Mx, p)
    co = [0] * k
    for t, pc in enumerate(piv):
        if pc < k:
            co[pc] = Rm[t][k]
    chk = [sum(co[t] * base[t][s] for t in range(k)) % p for s in range(len(x))]
    return co if chk == [v % p for v in x] else None


def P_alg(T, B, S, p):
    """exact F_p implementation of the recursion for P(A,B,S) = min{dim U : U>=S, T(U) <= U+B}"""
    dy = len(T)
    C = basis(B, p)
    Phi = [list(r) for r in T]
    Tt = basis(S, p)
    total = 0
    steps = 0
    while Tt and dy > 0 and steps <= dy + 2:
        total += len(Tt)
        steps += 1
        M = basis(Tt + C, p)
        if len(M) == dy:
            break
        N = complement(M, dy, p)
        dy2 = len(N)
        base = M + N

        def toY2(x):
            co = coords(base, x, p)
            return co[len(M):] if co is not None else None

        def lift(y):
            return [sum(y[k] * N[k][i] for k in range(len(N))) % p for i in range(dy)]

        C2 = basis([toY2([sum(m[i] * Phi[i][j] for i in range(dy)) % p for j in range(dy)]) for m in M], p)
        T2 = basis([toY2([sum(t[i] * Phi[i][j] for i in range(dy)) % p for j in range(dy)]) for t in Tt], p)
        Phi2 = []
        for i in range(dy2):
            e = [0] * dy2
            e[i] = 1
            img = [sum(lift(e)[a] * Phi[a][j] for a in range(dy)) % p for j in range(dy)]
            Phi2.append(toY2(img))
        C, Tt, Phi, dy = C2, T2, Phi2, dy2
    return total


def main():
    rng = random.Random(2027)
    print("=" * 92)
    print("c199 -- (5a)-floor rho_ci vs true rho*   (P(T,B,U0) vs the exhaustive layer search)")
    print("=" * 92)
    rows = []
    for (n, p, n_inst) in ((4, 5, 8), (4, 7, 6), (5, 5, 8)):
        for _ in range(n_inst):
            A = [[rng.randrange(p) for _ in range(n)] for _ in range(n)]
            pr = rng.choice([1, 1, 2])
            C = [[rng.randrange(p) for _ in range(n)] for _ in range(pr)]
            if R.rank(C, p) != pr:
                continue
            ds = rng.choice([1, 1, 2])
            S = []
            while len(S) < ds:
                v = [rng.randrange(p) for _ in range(n)]
                if R.rank(S + [v], p) == len(S) + 1:
                    S.append(v)
            L0 = [list(x) for x in S]
            D = R.setup(A, C, p)
            if D is None or D['d'] == 0:
                continue
            # reduced data
            Tw = [list(x) for x in D['TW']]
            Bj = [list(x) for x in D['Bj']]
            U0 = [D['pi'](s) for s in S]
            U0 = basis(U0, p)
            rho_ci = P_alg(Tw, Bj, U0, p)
            trials = int(sys.argv[sys.argv.index('--trials')+1]) if '--trials' in sys.argv else 12
            res = R.search(A, C, L0, p, trials=trials)
            if res is None or not res['reach']:
                continue
            reach = sorted(res['reach'])
            rhos = sorted(set(k[0] for k in reach))
            rho_star = min(rhos)
            rows.append((n, p, pr, ds, D['d'], rho_ci, rho_star, reach))
    print(f"  {'n':>2} {'p':>2} {'r':>2} {'dimS':>4} {'d':>2} {'rho_ci':>6} {'rho*':>4} "
          f"{'gap':>4}  reachable (rho,c)")
    gaps = {}
    for (n, p, pr, ds, d, rci, rs, reach) in rows:
        g = rs - rci
        gaps[g] = gaps.get(g, 0) + 1
        print(f"  {n:>2} {p:>2} {pr:>2} {ds:>4} {d:>2} {rci:>6} {rs:>4} {g:>4}  {reach}")
    print()
    print("gap distribution (rho* - rho_ci):", dict(sorted(gaps.items())))
    print("note: rho_ci = P(T,B,U0) is the (5a)-only floor; rho* is the exhaustive truth.")
    print("      gap = 0 means the floor is tight on that instance.")


if __name__ == "__main__":
    main()
