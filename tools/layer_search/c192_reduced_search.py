"""c192_reduced_search.py -- exhaustive search in the d-dimensional quotient (F_p)

WHY
---
c191 validated, on every ci subspace of F_5^5, the reduced-coordinate criterion

    V = (s+tau)(U) (+) H,   U subset X = C^n/J (dim rho), H subset J (dim c)
    (5a)  <=>  beta(H) subset U   and   T(U) subset U + B          B = pi(J A)
    (5b)  <=>  (S_tau, beta|_H) controllable,  S_tau = (T + beta tau)|_U

So MIN-ROWS = min(rho + c) over (U, H, tau).  This script enumerates (U,H)
completely (Gr(rho,d) x Gr(c,j), d = n - j <= 5) and SOLVES for tau linearly
(no sampling): the two conditions on tau are

    (A) for every q in U^perp:  <q,T(u_i)> + sum_k tau[i][k] <q, beta(J_k)> = 0
    (B) for every s in S and every q in H^perp (in J-coords):
            <q, jcomp(s)> - sum_i co_i(s) <q, tau[i]> = 0

then, inside the affine space of admissible tau, tests controllability (an open
condition, so a handful of points in the affine space suffices in practice --
and every hit is verified exactly against (5a)/(5b) before it is reported).

OUTPUT: for each instance the reachable set of (rho,c) pairs, q_min, rho*, and
whether q_min = max(r+eps, rho* + max(c0,1)) (the surviving closed form F3).

USAGE
    python tools/layer_search/c192_reduced_search.py            # n=6
    python tools/layer_search/c192_reduced_search.py --n 7 --k 2
"""
import sys, os, itertools, random, time

P = 5


# ------------------------------------------------------------------ F_p algebra
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


def minv(M, p):
    n = len(M)
    A = [[M[i][j] % p for j in range(n)] + [1 if j == i else 0 for j in range(n)] for i in range(n)]
    R, piv = rref(A, p)
    assert len(piv) == n
    return [x[n:] for x in R]


def nullsp(M, p):
    if not M:
        return []
    R, piv = rref(M, p)
    n = len(M[0])
    out = []
    for f in [c for c in range(n) if c not in piv]:
        v = [0] * n
        v[f] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-R[i][f]) % p
        out.append(v)
    return out


def subspaces(m, p, k):
    """all k-dim subspaces of F_p^m, as rref row lists"""
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


# ------------------------------------------------------------------ polynomials
def pn(a, p):
    a = list(a)
    while len(a) > 1 and a[-1] % p == 0:
        a = a[:-1]
    return [x % p for x in a] if a else [0]


def padd(a, b, p):
    n = max(len(a), len(b), 1)
    return pn([((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p
               for i in range(n)], p)


def psub(a, b, p):
    n = max(len(a), len(b), 1)
    return pn([((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % p
               for i in range(n)], p)


def pmul(a, b, p):
    o = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                o[i + j] = (o[i + j] + x * y) % p
    return pn(o, p)


def pdivmod(a, b, p):
    a = pn(list(a), p)
    b = pn(list(b), p)
    q = [0] * max(0, len(a) - len(b) + 1)
    iv = pow(b[-1], p - 2, p)
    while len(a) >= len(b) and a != [0]:
        d = len(a) - len(b)
        co = a[-1] * iv % p
        q[d] = co
        for i in range(len(b)):
            a[d + i] = (a[d + i] - co * b[i]) % p
        a = pn(a, p)
        if a == [0]:
            break
    return pn(q, p), a


def pgcd(a, b, p):
    a = pn(list(a), p)
    b = pn(list(b), p)
    while b != [0]:
        _, r = pdivmod(a, b, p)
        a, b = b, r
    if a != [0]:
        iv = pow(a[-1], p - 2, p)
        a = [x * iv % p for x in a]
    return a


def detp(M, p):
    k = len(M)
    if k == 0:
        return [1]
    if k == 1:
        return pn(M[0][0], p)
    acc = [0]
    for j in range(k):
        if pn(M[0][j], p) == [0]:
            continue
        mi = [[M[i][c] for c in range(k) if c != j] for i in range(1, k)]
        t = pmul(M[0][j], detp(mi, p), p)
        acc = padd(acc, t, p) if j % 2 == 0 else psub(acc, t, p)
    return pn(acc, p)


def constrank(Q, rr, width, p):
    """is rank Q(lam) == rr for all lam ?  (gcd of rr x rr minors)"""
    if rr == 0:
        return all(all(z == 0 for z in e) for row in Q for e in row)
    g = None
    for rs in itertools.combinations(range(len(Q)), rr):
        for cs in itertools.combinations(range(width), rr):
            v = detp([[Q[i][t] for t in cs] for i in rs], p)
            if v == [0]:
                continue
            g = v if g is None else pgcd(g, v, p)
            if len(g) <= 1:
                return True
    return g is not None and len(g) <= 1


# ------------------------------------------------------------------ the search
def setup(A, C, p):
    n = len(A)
    CA = mul(C, A, p)
    M = vstack(C, CA)
    J, _ = rref(M, p)
    J = [list(r) for r in J]
    j = rank(M, p)
    d = n - j
    W = []
    for i in range(n):
        v = [0] * n
        v[i] = 1
        if rank(vstack(J, W + [v]), p) == len(J) + len(W) + 1:
            W.append(v)
        if len(W) == d:
            break
    if len(W) != d:
        return None
    Binv = minv(J + W, p)
    pi = lambda x: mul([list(x)], Binv, p)[0][j:]
    jc = lambda x: mul([list(x)], Binv, p)[0][:j]
    TW = [pi(mul([w], A, p)[0]) for w in W]        # TW[l] = pi(W_l A), length d
    Bj = [pi(mul([r], A, p)[0]) for r in J]        # beta(J_k), length d
    return dict(n=n, J=J, j=j, d=d, W=W, pi=pi, jc=jc, TW=TW, Bj=Bj, CA=CA)


def solve_affine(eqs, rhs, nu, p):
    A = [list(eqs[i]) + [rhs[i] % p] for i in range(len(eqs))]
    if not A:
        return [0] * nu, [[1 if k == i else 0 for k in range(nu)] for i in range(nu)]
    R, piv = rref(A, p)
    for row in R:
        if all(x % p == 0 for x in row[:nu]) and row[nu] % p:
            return None
    part = [0] * nu
    for i, pc in enumerate(piv):
        if pc < nu:
            part[pc] = R[i][nu] % p
    free = [c for c in range(nu) if c not in piv]
    nb = []
    for f in free:
        v = [0] * nu
        v[f] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-R[i][f]) % p
        nb.append(v)
    return part, nb


def coords_in(w, U, p):
    """coordinates of w in the span of the rows of U (None if not inside)"""
    if not U:
        return [] if all(x % p == 0 for x in w) else None
    M = [[U[i][x] for i in range(len(U))] + [w[x]] for x in range(len(w))]
    R, piv = rref(M, p)
    sol = [0] * len(U)
    for i, pc in enumerate(piv):
        if pc < len(U):
            sol[pc] = R[i][len(U)] % p
    chk = [sum(sol[i] * U[i][x] for i in range(len(U))) % p for x in range(len(w))]
    return sol if chk == [x % p for x in w] else None


def search(A, C, L0, p=P, trials=25):
    D = setup(A, C, p)
    if D is None:
        return None
    n, j, d = D["n"], D["j"], D["d"]
    J, W, pi, jc, TW, Bj, CA = D["J"], D["W"], D["pi"], D["jc"], D["TW"], D["Bj"], D["CA"]
    S = [list(r) for r in rref(L0, p)[0]]
    if not S:
        return None
    Spo = [pi(s) for s in S]
    Sjo = [jc(s) for s in S]
    zero_d = [0] * d

    def amb(jv, wv):
        x = [0] * n
        for k in range(j):
            if jv[k]:
                for t in range(n):
                    x[t] = (x[t] + jv[k] * J[k][t]) % p
        for l in range(d):
            if wv[l]:
                for t in range(n):
                    x[t] = (x[t] + wv[l] * W[l][t]) % p
        return x

    reach = {}
    for rho in range(0, d + 1):
        for U in subspaces(d, p, rho):
            # S-constraint (i): pi(s) in U
            ok = True
            for x in Spo:
                if coords_in(list(x), U, p) is None:
                    ok = False
                    break
            if not ok:
                continue
            Up = nullsp(U, p) if rho else [list(e) for e in
                                           [[1 if i == k else 0 for i in range(d)] for k in range(d)]]
            for c in range(0, j + 1):
                if (rho, c) in reach:
                    continue
                for H in subspaces(j, p, c):
                    # beta(H) subset U
                    BHcoords = []
                    ok = True
                    for h in H:
                        w = [sum(h[k] * Bj[k][x] for k in range(j)) % p for x in range(d)]
                        co = coords_in(w, U, p)
                        if co is None:
                            ok = False
                            break
                        BHcoords.append(co)
                    if not ok:
                        continue
                    # linear system for tau  (rho x j unknowns)
                    nu = rho * j
                    eqs, rhs = [], []
                    # (A) T(u_i) + sum_k tau[i][k] Bj[k] in U
                    for ui in range(rho):
                        Tu = [sum(U[ui][t] * TW[t][x] for t in range(d)) for x in range(d)]
                        for q in Up:
                            eq = [0] * nu
                            for k in range(j):
                                eq[ui * j + k] = sum(q[x] * Bj[k][x] for x in range(d)) % p
                            eqs.append(eq)
                            rhs.append((-sum(q[x] * Tu[x] for x in range(d))) % p)
                    # (B) S-constraint (ii):  jcomp(s) - tau(pi s) in H
                    for si in range(len(S)):
                        co = coords_in(list(Spo[si]), U, p)
                        if co is None:
                            ok = False
                            break
                        Hperp = nullsp(H, p) if c else [[1 if i == k else 0 for i in range(j)]
                                                        for k in range(j)]
                        for q in Hperp:
                            eq = [0] * nu
                            for i2 in range(rho):
                                for k in range(j):
                                    eq[i2 * j + k] = (-co[i2] * q[k]) % p
                            eqs.append(eq)
                            rhs.append((-sum(q[k] * Sjo[si][k] for k in range(j))) % p)
                    if not ok:
                        continue
                    sol = solve_affine(eqs, rhs, nu, p)
                    if sol is None:
                        continue
                    part, nb = sol
                    got = False
                    for _ in range(trials if nb else 1):
                        cf = [random.randrange(p) for _ in range(len(nb))] if nb else []
                        tau = [(part[t] + sum(cf[s2] * nb[s2][t] for s2 in range(len(nb)))) % p
                               for t in range(nu)]
                        tauM = [tau[i * j:(i + 1) * j] for i in range(rho)]
                        # S_tau and beta|H in U-coordinates
                        Stau, BH = [], BHcoords
                        ok = True
                        for ui in range(rho):
                            w = [sum(U[ui][t] * TW[t][x] for t in range(d)) for x in range(d)]
                            w = [(w[x] + sum(tauM[ui][k] * Bj[k][x] for k in range(j))) % p
                                 for x in range(d)]
                            co = coords_in(w, U, p)
                            if co is None:
                                ok = False
                                break
                            Stau.append(co)
                        if not ok:
                            continue
                        Qc = [[([-Stau[i][k2], 1] if i == k2 else [-Stau[i][k2]]) for k2 in range(rho)]
                              + [[BH[k3][i]] for k3 in range(len(BH))] for i in range(rho)]
                        if not constrank(Qc, rho, rho + len(BH), p):
                            continue
                        # build V and VERIFY exactly
                        V = [amb(list(h), zero_d) for h in H] + \
                            [amb(tauM[ui], list(U[ui])) for ui in range(rho)]
                        if rank(V, p) != rho + c:
                            continue
                        if rank(vstack(mul(V, A, p), V, CA, C), p) != rank(vstack(V, CA, C), p):
                            continue
                        cc = len(V) + j - rank(vstack(V, J), p)
                        rr = len(V) - cc
                        if (rr, cc) != (rho, c):
                            continue
                        Q = [[[(-pi(mul([x], A, p)[0])[t2]) % p, pi(x)[t2] % p]
                              for t2 in range(d)] for x in V]
                        if constrank(Q, rr, d, p):
                            got = True
                            break
                    if got:
                        reach[(rho, c)] = 1
    return dict(j=j, d=d, reach=reach)


def main():
    n = 6
    K = 3
    seed = 777
    if "--n" in sys.argv:
        n = int(sys.argv[sys.argv.index("--n") + 1])
    if "--k" in sys.argv:
        K = int(sys.argv[sys.argv.index("--k") + 1])
    if "--seed" in sys.argv:
        seed = int(sys.argv[sys.argv.index("--seed") + 1])
    random.seed(12345)
    rng = random.Random(seed)
    print("=" * 96)
    print(f"c192 -- full enumeration of (U,H) in the d-dim quotient, tau SOLVED linearly  "
          f"(n={n}, p={P})")
    print("=" * 96)
    for t in range(K):
        A = [[rng.randrange(P) for _ in range(n)] for _ in range(n)]
        C = [[rng.randrange(P) for _ in range(n)]]
        L0 = [[rng.randrange(P) for _ in range(n)]]
        if rank(C, P) != 1:
            continue
        t0 = time.time()
        R = search(A, C, L0, P)
        if R is None:
            print(f" inst {t}: skipped")
            continue
        reach = R["reach"]
        q = min((k[0] + k[1] for k in reach), default=None)
        rs = min((k[0] for k in reach), default=None)
        print(f" inst {t}: j={R['j']} d={R['d']} | reachable (rho,c): {sorted(reach)}")
        print(f"          q_min={q}  rho*={rs}   ({time.time()-t0:.1f}s)")


if __name__ == "__main__":
    main()
