# -*- coding: utf-8 -*-
"""
系统验证：Omega*_{A,J} 的行为是否由 s-k（= dim Theta / k）决定。

对大量随机实例，记录 (n,p,r,q0,k,s,dimTheta) 与 (A) 的命中率，
并同时记录若干候选不变量（d_C, d_CA = n - rank[C;CA]）。
"""
import itertools
import random
from fractions import Fraction as F


def rref(M):
    M = [r[:] for r in M]
    if not M:
        return M, []
    nr, nc = len(M), len(M[0]); piv = []; r = 0
    for c in range(nc):
        p = None
        for i in range(r, nr):
            if M[i][c] != 0:
                p = i; break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]; pv = M[r][c]; M[r] = [x / pv for x in M[r]]
        for i in range(nr):
            if i != r and M[i][c] != 0:
                f = M[i][c]; M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c); r += 1
        if r == nr:
            break
    return M, piv


def rk(M):
    return 0 if not M or not M[0] else len(rref(M)[1])


def mm(X, Y):
    n, k, m = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def toF(M):
    return [[F(int(x)) for x in row] for row in M]


def tr(M):
    return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]


def inv(M):
    n = len(M)
    R, piv = rref([M[i][:] + [F(1) if i == j else F(0) for j in range(n)] for i in range(n)])
    if len(piv) != n or any(p >= n for p in piv):
        return None
    return [row[n:] for row in R]


def ker(M):
    if not M:
        return []
    n = len(M[0]); R, piv = rref(M); free = [c for c in range(n) if c not in piv]
    if not free:
        return []
    so = []
    for fc in free:
        v = [F(0)] * n; v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][fc]
        so.append(v)
    m = len(so)
    return [[so[j][i] for j in range(m)] for i in range(n)]


def solve(Des, b):
    m, k = len(Des), len(Des[0])
    R, piv = rref([Des[i][:] + [b[i][0]] for i in range(m)])
    for row in R:
        if all(x == 0 for x in row[:k]) and row[k] != 0:
            return None
    y = [F(0)] * k
    for i, pc in enumerate(piv):
        if pc < k:
            y[pc] = R[i][k]
    ns = []
    free = [c for c in range(k) if c not in piv]
    for fc in free:
        v = [F(0)] * k; v[fc] = F(1)
        for i, pc in enumerate(piv):
            if pc < k:
                v[pc] = -R[i][fc]
        ns.append(v)
    return y, ns


def cand(target, basis):
    if not basis:
        return [] if all(x == 0 for x in target) else None
    m, k = len(target), len(basis)
    R, piv = rref([[basis[i][j] for i in range(k)] + [target[j]] for j in range(m)])
    for row in R:
        if all(x == 0 for x in row[:k]) and row[k] != 0:
            return None
    phi = [F(0)] * k
    for i, pc in enumerate(piv):
        if pc < k:
            phi[pc] = R[i][k]
    return phi


def tm(v, A, q):
    o = v[:]
    for _ in range(q):
        o = mm([o], A)[0]
    return o


def p1(A, C, L0):
    n, p, r = len(A), len(C), len(L0)
    gens = [x[:] for x in C] + [x[:] for x in L0]; ng = p + r
    M, MI, rej = [], [], {}
    for q in range(n + 1):
        for i in range(ng):
            if i in rej:
                continue
            v = tm(gens[i], A, q)
            if rk(M + [v]) > rk(M):
                M.append(v); MI.append((i, q))
            else:
                rej[i] = q
        if len(rej) == ng:
            break
    al = [rej.get(i, n + 1) for i in range(ng)]; eta = [al[p + j] for j in range(r)]
    RR = []
    for j in range(r):
        i = p + j; ai = al[i]
        if ai > n:
            continue
        Mm, Mi = [], []
        for (ii, qq), row in zip(MI, M):
            if (qq < ai) or (qq == ai and ii < i):
                Mm.append(row); Mi.append((ii, qq))
        phi = cand(tm(gens[i], A, ai), Mm)
        if phi is None:
            continue
        ej = eta[j]
        for t in range(1, ej):
            sh = ej - t; row = tm(gens[i], A, t)
            for q in range(sh + 1, ej + 1):
                for idx, (ii, qq) in enumerate(Mi):
                    if qq != q or phi[idx] == 0:
                        continue
                    term = tm(gens[ii], A, q - sh)
                    row = [row[k] - phi[idx] * term[k] for k in range(n)]
            RR.append(row)
    return toF(L0) + RR, eta


def condA(A, C, L):
    LA = mm(L, A); W = L + C + mm(C, A)
    return rk(W + LA) == rk(W)


rng = random.Random(2024)


def orb(M, A, n):
    o = []; cur = M
    for _ in range(n):
        o += cur; cur = mm(cur, A)
    return o


def rand_inst(n, p, r):
    for _ in range(6000):
        Am = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
        Cm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)]
        Lm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(r)]
        A, C, L0 = toF(Am), toF(Cm), toF(Lm)
        if rk(C) != p or rk(L0) != r:
            continue
        if rk(L0 + C) != r + p:
            continue
        Z = orb(L0, A, n) + orb(C, A, n); OC = orb(C, A, n)
        if rk(Z + OC) != rk(OC):
            continue
        return A, C, L0
    return None


def build_T(A, C, L0, Lx):
    n, p, r = len(A), len(C), len(L0)
    NC = ker(C); dC = len(NC[0])
    MC = mm(inv(mm(tr(NC), NC)), tr(NC))
    L0NC = mm(L0, NC); R = Lx[len(L0):]; RNC = mm(R, NC)
    K = ker(L0NC); mK = len(K[0]) if (K and K[0]) else 0
    if mK == 0:
        return None
    k = len(R); s = dC - r
    Kr = [[K[a][j] for a in range(dC)] for j in range(mK)]
    Tc = []
    for i in range(r):
        ei = [F(1) if q == i else F(0) for q in range(r)]
        sol = solve([[L0NC[a][j] for j in range(dC)] for a in range(r)],
                    [[ei[a]] for a in range(r)])
        xi = sol[0]
        tgt = mm(RNC, [[xi[j]] for j in range(dC)])[0][0]
        rkl = [mm(RNC, [[Kr[j][a]] for a in range(dC)])[0][0] for j in range(mK)]
        c = [F(0)] * mK
        for j in range(mK):
            if rkl[j] != 0:
                c[j] = -tgt / rkl[j]; break
        z = [sum(c[j] * Kr[j][a] for j in range(mK)) for a in range(dC)]
        Tc.append([xi[a] + z[a] for a in range(dC)])
    rkmat = [[mm(RNC, [[Kr[j][a]] for a in range(dC)])[ii][0] for j in range(mK)] for ii in range(k)]
    nsc = None
    for j in range(s):
        if j < k:
            ej = [[F(1) if ii == j else F(0)] for ii in range(k)]
            so = solve(rkmat, ej)
            if so is None:
                return None
            yj = so[0]
        else:
            if nsc is None:
                nsc = solve(rkmat, [[F(0)] for _ in range(k)])[1]
            ix = j - k
            if ix >= len(nsc):
                return None
            yj = nsc[ix]
        Tc.append([sum(yj[a] * Kr[a][jj] for a in range(mK)) for jj in range(dC)])
    T = [[Tc[j][i] for j in range(dC)] for i in range(dC)]
    Ti = inv(T)
    if Ti is None:
        return None
    Abar = mm(mm(MC, A), NC); BA = mm(mm(C, A), NC)
    return Ti, mm(mm(Ti, Abar), T), mm(BA, T), dC, s, k


summary = {}
print(f"{'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'k':>2} {'s':>2} {'dimTh':>5} | {'命中/总':>10} {'行为':>10}")
print("-" * 62)
for trial in range(120):
    n = rng.randint(2, 6)
    p = rng.randint(1, n - 1)
    r = rng.randint(1, n - p)
    got = rand_inst(n, p, r)
    if got is None:
        continue
    A, C, L0 = got
    Lx, eta = p1(A, C, L0)
    if not condA(A, C, Lx):
        continue
    q0 = sum(eta); k = q0 - r
    dC = n - p; s = dC - r
    if k < 1 or k > s:
        continue
    bt = build_T(A, C, L0, Lx)
    if bt is None:
        continue
    Ti, AT, BAT, dC, s, k = bt
    dimTh = k * (s - k)
    total = 0; ncell = 0
    for J in itertools.combinations(range(s), k):
        rest = [i for i in range(s) if i not in J]
        for a in range(-6, 7):
            th = F(a, 2); ncell += 1
            Y = [F(0)] * s
            for a2, jj in enumerate(J):
                Y[jj] = F(1) if a2 == 0 else th
            for pos in rest:
                Y[pos] = th
            W = [[F(1) if jj == ii else F(0) for jj in range(dC)] for ii in range(r)]
            W.append([F(0)] * r + Y)
            if rk(W + BAT + mm(W, AT)) == rk(W + BAT):
                total += 1
    beh = "全空间" if total == ncell else ("单点/有限" if total <= 3 else f"部分({total})")
    flag = "" if (dimTh == 1) == (beh == "全空间") else "   <== 不符"
    print(f"{n:>2} {p:>2} {r:>2} {q0:>3} {k:>2} {s:>2} {dimTh:>5} | {total:>4}/{ncell:<5} {beh:>10}{flag}")
    summary.setdefault((dimTh, beh), 0)
    summary[(dimTh, beh)] += 1

print()
print("汇总 (dimTheta, 行为) -> 次数:")
for kk in sorted(summary):
    print(f"   dimTheta={kk[0]:>3}  {kk[1]:>12} : {summary[kk]}")
