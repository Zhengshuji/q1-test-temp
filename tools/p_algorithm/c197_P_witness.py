"""c197_P_witness.py -- the recursion algorithm for P(A,B,S) WITH a witness.

P(A,B,S) = min { dim W | S <= U, A W <= W + B }.

c195 computes the value by iterating the one-step recursion
    P(T, C, Phi) = dim T + P(T', C', Phi'),   M = T + C,  Y' = Y/M,
    T' = pi(Phi T),  C' = pi(Phi M),  Phi' = Phi mod M
but returns only a number.  This script *constructs* a minimising W by lifting a
feasible subspace back up the recursion, so every computed value comes with a
certificate that can be checked exactly:

    dim W = P   and   A W <= W + B .

The lift uses the construction of the (<=) half:
    U_k = T_k + span{ s(u) + sigma(u) : u in basis of U_{k+1} }
where s is the linear section built from a complement N_k of M_k, and sigma is
obtained by solving an exact linear system
    Q_k Phi_k (s(u) + m)  in  U'      for m in M_k
(solvable because pi(Phi M) = C' and pi(Phi s(u)) lies in U' + C').

USAGE
    python tools/p_algorithm/c197_P_witness.py            # 12 random instances
    python tools/p_algorithm/c197_P_witness.py --n 5
"""
import os
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c195_P_q as Q  # exact rational linear algebra


# ---------------------------------------------------------------- solve a linear system
def solve(M, rhs):
    """solve M x = rhs over Q; returns one solution or None"""
    m = len(M)
    if m == 0:
        return [] if not any(rhs) else None
    n = len(M[0])
    aug = [[Fr(M[i][j]) for j in range(n)] + [Fr(rhs[i])] for i in range(m)]
    R, piv = Q.rref(aug)
    # consistency: a row with all-zero coefficients but nonzero rhs
    for i in range(len(R)):
        if all(R[i][j] == 0 for j in range(n)) and R[i][n] != 0:
            return None
    x = [Fr(0)] * n
    for i, pc in enumerate(piv):
        if pc < n:
            x[pc] = R[i][n]
    return x


def P_with_witness(A, B, S):
    """returns (P, W) with dim W = P and A W <= W + B, or (None, None)"""
    n = len(A)
    d = n
    C = Q.basis(B)
    T = Q.basis(S)
    Phi = [[Fr(x) for x in row] for row in A]
    levels = []
    while True:
        if not T:
            levels.append(dict(d=d, C=C, T=T, Phi=Phi, M=None))
            break
        M = Q.basis(Q.vstack(T, C))
        if len(M) == d:
            levels.append(dict(d=d, C=C, T=T, Phi=Phi, M=M))
            break
        N = Q.complement(M, d)          # rows, len(N) = d - |M|
        base = M + N
        # quotient coordinates: Qmat[i] = N-part of the coordinates of e_i in base
        Qmat = []
        for i in range(d):
            e = [Fr(0)] * d
            e[i] = Fr(1)
            co = Q.coords_in(base, e)
            Qmat.append(co[len(M):])
        Qm = [[Qmat[i][j] for i in range(d)] for j in range(len(N))]  # rows: Q_j(e_i)
        # section: s(u) = sum_j u_j N[j]
        levels.append(dict(d=d, C=C, T=T, Phi=Phi, M=M, N=N, Qm=Qm, base=base))
        # next level data
        def toY2(x):
            co = Q.coords_in(base, x)
            return co[len(M):]
        C2 = Q.basis([toY2([sum(m[i] * Phi[i][j] for i in range(d)) for j in range(d)])
                      for m in M])
        T2 = Q.basis([toY2([sum(t[i] * Phi[i][j] for i in range(d)) for j in range(d)])
                      for t in T])
        Phi2 = []
        for j in range(len(N)):
            img = [sum(N[j][a] * Phi[a][b] for a in range(d)) for b in range(d)]
            Phi2.append(toY2(img))
        d, C, T, Phi = len(N), C2, T2, Phi2

    # bottom: U = 0 if T empty, else U = T (the quotient is zero at this point)
    lv = levels[-1]
    U = [] if not lv["T"] else [list(x) for x in lv["T"]]

    for k in range(len(levels) - 2, -1, -1):
        lv = levels[k]
        d, C, T, Phi, M, N, base = lv["d"], lv["C"], lv["T"], lv["Phi"], lv["M"], lv["N"], lv["base"]
        # quotient map of this level (as a function on ambient coords)
        def pi(x):
            co = Q.coords_in(base, x)
            return co[len(M):]

        # M as a matrix: columns = the M-basis vectors
        Mmat = [[M[i][a] for i in range(len(M))] for a in range(d)]   # d x |M|
        UU = [list(x) for x in U]                                     # basis of U' (Y_{k+1} coords)
        if not UU:
            # nothing to lift except T
            U = [list(x) for x in T]
            continue
        newE = []
        for u in UU:
            su = [sum(u[j] * N[j][a] for j in range(len(N))) for a in range(d)]   # s(u) in Y_k
            # target t = pi(Phi s(u)) ; solve pi(Phi(s(u)+m)) in span(UU)
            phi_su = [sum(su[a] * Phi[a][b] for a in range(d)) for b in range(d)]
            t = pi(phi_su)
            # matrix Bmat = pi(Phi M_i) as columns, plus the UU-basis (to absorb the difference)
            Bcols = []
            for i in range(len(M)):
                v = [sum(M[i][a] * Phi[a][b] for a in range(d)) for b in range(d)]
                Bcols.append(pi(v))
            Umat = [[UU[i][a] for i in range(len(UU))] for a in range(len(UU[0]))]
            # solve  sum c_i Bcols_i - sum y_j UU_j = t
            ncol = len(Bcols) + len(UU)
            rows = [[Bcols[i][r] for i in range(len(Bcols))] +
                    [UU[j][r] for j in range(len(UU))] for r in range(len(t))]
            sol = solve(rows, [-x for x in t])
            if sol is None:
                return None, None
            c = sol[:len(Bcols)]
            m = [sum(c[i] * M[i][a] for i in range(len(M))) for a in range(d)]
            newE.append([su[a] + m[a] for a in range(d)])
        U = Q.basis(Q.vstack(T, newE))

    W = [list(x) for x in U]
    P = Q.rank(W)
    return P, W


def main():
    n = 4
    if "--n" in sys.argv:
        n = int(sys.argv[sys.argv.index("--n") + 1])
    rng = random.Random(424242)
    print("=" * 92)
    print(f"c197 -- P with witness (n = {n}):  dim W = P  and  A W <= W + B  (exact over Q)")
    print("=" * 92)
    ok = tot = 0
    for t in range(12):
        A = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
        b = rng.choice([1, 2])
        B = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(b)]
        ds = rng.choice([1, 2])
        S = []
        while len(S) < ds:
            v = [rng.randint(-2, 2) for _ in range(n)]
            if Q.rank(S + [v]) == len(S) + 1:
                S.append(v)
        if Q.rank(B) != b:
            continue
        Pval, W = P_with_witness(A, B, S)
        tot += 1
        if Pval is None:
            print(f"  {t:2d}: lift failed (sigma solve returned None)")
            continue
        Pc = Q.P_alg(A, B, S)                      # value from c195
        dimW = Q.rank(W)
        admissible = (Q.rank(Q.vstack(W, B, Q.mul(W, A))) == Q.rank(Q.vstack(W, B)))
        containsS = (Q.rank(Q.vstack(W, S)) == dimW)
        good = (dimW == Pc == Pval) and admissible and containsS
        ok += good
        print(f"  {t:2d}: P(c195)={Pc}  dim W={dimW}  admissible={admissible}  W>=S={containsS}"
              f"   {'OK' if good else '**FAIL**'}")
    print()
    print(f"witness check: {ok}/{tot}")


if __name__ == "__main__":
    main()
