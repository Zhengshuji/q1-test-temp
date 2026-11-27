"""Uniform stratum solver for MIN-ROWS (attempts/165,166,179).

For given (A,C,L0,q) and omega (default q-1), c=k-omega:
  enumerate V in Gr(c,W_L) (finite rational search; W_L may force V),
  build H (q x k) with kernel V and rank omega, solve H_A|_V=0 row-wise,
  test the q x k pencil rank omega (gcd of omega-minors), construct L and verify.

This is the uniform method, not a complete decision procedure: the search over V
and over the free parameters is finite.  A returned witness is exact; "none" is
not a proof of infeasibility.

Run: python tools/verification/stratum_solver.py
"""
import sys, itertools, random
sys.path.insert(0, '.')
sys.path.insert(0, 'tools/verification')
sys.path.insert(0, 'tools/exact_linalg')
sys.path.insert(0, 'tools/ledger')
from fractions import Fraction as F
import linalg_q as LQ
import z_generator as ZG
from tools.verification.consistency_checks import check_candidate


# ---------- polynomials ----------
def pt(a):
    a = [F(x) for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def pa(a, b):
    n = max(len(a), len(b))
    return pt([(a[i] if i < len(a) else F(0)) + (b[i] if i < len(b) else F(0)) for i in range(n)])


def ps(a, c):
    return pt([F(x) * c for x in a])


def pm(a, b):
    o = [F(0)] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            o[i + j] += a[i] * b[j]
    return pt(o)


def pdm(a, b):
    a = pt(a); b = pt(b)
    if len(a) < len(b):
        return [F(0)], a
    q = [F(0)] * (len(a) - len(b) + 1)
    while len(a) >= len(b) and not (len(a) == 1 and a[0] == 0):
        d = a[-1] / b[-1]
        sh = len(a) - len(b)
        q[sh] = d
        for i in range(len(b)):
            a[sh + i] -= d * b[i]
        a = pt(a)
    return pt(q), a


def pgcd(a, b):
    a = pt(a); b = pt(b)
    while not (len(b) == 1 and b[0] == 0):
        a, b = b, pdm(a, b)[1]
    if len(a) == 1 and a[0] == 0:
        return a
    return ps(a, F(1) / a[-1])


def det_poly(entries):
    """entries: s x s list of [c0,c1] pairs (polynomials of degree <=1)."""
    s = len(entries)
    total = [F(0)]
    for perm in itertools.permutations(range(s)):
        inv = sum(1 for i in range(s) for j in range(i + 1, s) if perm[i] > perm[j])
        term = [F(1 if inv % 2 == 0 else -1)]
        for i in range(s):
            term = pm(term, entries[i][perm[i]])
        total = pa(total, term)
    return total


def gcd_minors(P, q, k, om):
    """P: q x k list of pairs (c0,c1); gcd of all om x om minors."""
    polys = []
    for rows in itertools.combinations(range(q), om):
        for cols in itertools.combinations(range(k), om):
            M = [[P[i][j] for j in cols] for i in rows]
            p = det_poly(M)
            if not (len(p) == 1 and p[0] == 0):
                polys.append(p)
    if not polys:
        return [F(0)]
    g = polys[0]
    for p in polys[1:]:
        g = pgcd(g, p)
        if len(g) == 1:
            break
    return g


# ---------- instance setup ----------
def prepare(A, C, L0):
    n = len(A)
    N = [r[:] for r in ZG.ker_cols([r[:] for r in C] + [r[:] for r in LQ.mul(C, A)])]
    k = len(N[0]) if N and N[0] else 0
    AN = LQ.mul(A, N)
    L0N = [F(x) for x in LQ.mul(L0, N)[0]]
    L0AN = [F(x) for x in LQ.mul(LQ.mul(L0, A), N)[0]]
    RD = LQ.rowspace([r[:] for r in C] + [r[:] for r in LQ.mul(C, A)])
    G = [[sum(F(r[u]) * F(AN[u][t]) for u in range(n)) for t in range(k)] for r in RD]
    return N, k, AN, L0N, L0AN, RD, G, n


def planes(WL, k, c, rng, tries=200, mode='random'):
    """Finite rational search of c-planes in W_L (columns of WL are a basis)."""
    d = len(WL[0]) if WL and WL[0] else 0
    if d < c:
        return []
    B = [[WL[i][j] for i in range(k)] for j in range(d)]
    if d == c:
        return [[B[j][:] for j in range(c)]]
    if mode == 'grid':
        out, seen = [], set()
        for flat in itertools.product([-1, 0, 1], repeat=d * c):
            coeff = [[F(flat[j * c + i]) for i in range(c)] for j in range(d)]
            V = [[sum(coeff[j][i] * B[j][t] for j in range(d)) for t in range(k)] for i in range(c)]
            R, _ = LQ.rref([r[:] for r in V])
            R = [r[:] for r in R if any(x != 0 for x in r)]
            if len(R) != c:
                continue
            key = tuple(tuple(x for x in r) for r in R)
            if key in seen:
                continue
            seen.add(key)
            out.append(R)
            if len(out) >= tries:
                break
        return out
    out, seen = [], set()
    for _ in range(tries):
        coeff = [[F(rng.randint(-2, 2)) for _ in range(c)] for _ in range(d)]
        # V rows = coeff^T applied to basis? build c vectors in C^k
        V = [[sum(coeff[j][i] * B[j][t] for j in range(d)) for t in range(k)] for i in range(c)]
        R, _ = LQ.rref([r[:] for r in V])
        R = [r[:] for r in R if any(x != 0 for x in r)]
        if len(R) != c:
            continue
        key = tuple(tuple(x for x in r) for r in R)
        if key in seen:
            continue
        seen.add(key)
        out.append(R)
    return out


def solve(A, C, L0, q, omega=None, seed=0, mode='random'):
    N, k, AN, L0N, L0AN, RD, G, n = prepare(A, C, L0)
    m = len(RD)
    rng = random.Random(seed)
    if omega is None:
        omega = q - 1
    c = k - omega
    if c < 0 or omega <= 0 or omega > q:
        return None, 'bad parameters'
    WL = ZG.ker_cols([L0N[:], L0AN[:]])
    dWL = len(WL[0]) if WL and WL[0] else 0
    if dWL < c:
        return None, f'dim W_L={dWL} < c={c}'
    last_cert = None
    p0 = LQ.solve([[N[t][j] for t in range(n)] for j in range(k)], [[L0N[j]] for j in range(k)])[0]
    A0 = [sum(F(p0[u]) * F(AN[u][t]) for u in range(n)) for t in range(k)]
    for V in planes(WL, k, c, rng, mode=mode):
        # Ann(V): kernel of the c x k matrix V
        Ann = ZG.ker_cols([V[i][:] for i in range(c)])
        acols = [[F(Ann[i][j]) for i in range(k)] for j in range(len(Ann[0]) if Ann and Ann[0] else 0)]
        if len(acols) < omega:
            continue
        if any(sum(L0N[t] * V[i][t] for t in range(k)) != 0 for i in range(c)):
            continue
        # choose u_1..u_{omega-1} extending h0 to a basis of Ann(V)
        basis = [L0N]
        for u in acols:
            if len(basis) == omega:
                break
            if LQ.rank(basis + [u]) > len(basis):
                basis.append(u)
        if len(basis) != omega:
            continue
        us = basis[1:]
        lifts = [p0]
        for u in us:
            l = LQ.solve([[N[t][j] for t in range(n)] for j in range(k)], [[u[j]] for j in range(k)])[0]
            lifts.append(l)
        # H_A base rows for the basis rows
        Abase = [[sum(F(l[u]) * F(AN[u][t]) for u in range(n)) for t in range(k)] for l in lifts]
        # Build the (q-1) systems, each with c equations (evaluate on V basis)
        sols = []
        ok = True
        forced_alphas = []
        all_forced = True
        for i in range(q - 1):
            rows = []
            for r in range(c):
                row = [sum(F(Abase[0][t]) * F(V[r][t]) for t in range(k))]
                for j in range(omega - 1):
                    row.append(sum(F(Abase[j + 1][t]) * F(V[r][t]) for t in range(k)))
                for j in range(m):
                    row.append(sum(F(G[j][t]) * F(V[r][t]) for t in range(k)))
                rows.append(row)
            eb = [F(0), F(1)] + [F(0)] * (omega - 2 + m)
            r0 = LQ.rank(rows)
            rb = LQ.rank(rows + [eb])
            if rb == r0:
                # b is forced to 0 for every admissible solution: row-space certificate
                Dt = [[rows[r][j] for r in range(c)] for j in range(len(rows[0]))]
                s = LQ.solve(Dt, [[x] for x in eb])
                forced_alphas.append(s[0] if s is not None else None)
                sols.append(None)
            else:
                all_forced = False
                s = LQ.solve(rows, [[F(0)] for _ in range(c)])
                if s is None:
                    ok = False
                    break
                sols.append(s)
        if not ok:
            continue
        if all_forced:
            # this V cannot give rank omega; record the certificate and move on
            last_cert = {'V': V, 'alphas': forced_alphas}
            continue
        # sample free parameters; need the (q-1) x (omega-1) b-matrix to have rank omega-1
        if mode == 'grid':
            free_dims = [len(sols[i][1]) for i in range(q - 1)]
            total = sum(free_dims)
            if total <= 6:
                trials = list(itertools.product([-1, 0, 1], repeat=total))[:300]
            else:
                base = [0] * total
                trials = [tuple(base)]
                for i in range(total):
                    for sgn in (1, -1):
                        tv = list(base); tv[i] = sgn; trials.append(tuple(tv))
                for i in range(total):
                    for j in range(i + 1, total):
                        for a, b in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                            tv = list(base); tv[i] = a; tv[j] = b; trials.append(tuple(tv))
        else:
            trials = list(range(100))
        for trial in trials:
            coefs = []
            idx = 0
            for i in range(q - 1):
                co = [F(x) for x in sols[i][0]]
                for z in range(len(sols[i][1])):
                    if mode == 'grid':
                        r = trial[idx]
                        idx += 1
                    else:
                        r = rng.randint(-2, 2)
                    if r:
                        co = [co[j] + F(r) * F(sols[i][1][z][j]) for j in range(len(co))]
                coefs.append(co)
            Bmat = [[coefs[i][1 + j] for j in range(omega - 1)] for i in range(q - 1)]
            if LQ.rank(Bmat) != omega - 1:
                continue
            H = [L0N]; HA = [L0AN]
            for co in coefs:
                a = co[0]; bs = co[1:omega]; g = co[omega:]
                h = [a * L0N[t] + sum(bs[j] * us[j][t] for j in range(omega - 1)) for t in range(k)]
                ha = [a * Abase[0][t] + sum(bs[j] * Abase[j + 1][t] for j in range(omega - 1))
                      + sum(g[j] * G[j][t] for j in range(m)) for t in range(k)]
                H.append(h); HA.append(ha)
            if LQ.rank(H) != omega:
                continue
            if any(sum(HA[i][t] * V[r][t] for t in range(k)) != 0 for i in range(q) for r in range(c)):
                continue
            P = [[(-HA[i][t], H[i][t]) for t in range(k)] for i in range(q)]
            g = gcd_minors(P, q, k, omega)
            if not (len(g) == 1 and g[0] != 0):
                continue
            Lrows = [L0[0][:]]
            for co in coefs:
                a = co[0]; bs = co[1:omega]; g = co[omega:]
                l = [a * F(p0[u]) + sum(bs[j] * F(lifts[j + 1][u]) for j in range(omega - 1))
                     + sum(g[j] * F(RD[j][u]) for j in range(m)) for u in range(n)]
                Lrows.append(l)
            if LQ.rank([x[:] for x in C] + Lrows) != len(C) + len(Lrows):
                continue
            try:
                res = check_candidate(A, C, L0, Lrows, tag='stratum', verbose=False)
            except AssertionError:
                continue
            if res['cond'] and res['five_b']:
                return Lrows, {'omega': omega, 'c': c, 'dimWL': dWL, 'status': 'feasible'}
    info = {'omega': omega, 'c': c, 'dimWL': dWL, 'status': 'none in search'}
    if last_cert is not None and dWL == c:
        info['infeasible'] = True
        info['certificate'] = last_cert
    return None, info


if __name__ == '__main__':
    from tools.verification.p2_stratification_check import data
    for seed in (10, 16, 21):
        A, C, L0, k, d, NK, U0, V0, Z1, Z2 = data(seed)
        L, info = solve(A, C, [r[:] for r in L0], q=3, omega=2, seed=seed)
        print(seed, 'FOUND' if L else 'none', info)
