# -*- coding: utf-8 -*-
"""
验证精确判据：
   K_exact:  k + dim(E + row(B_{A,T})) >= dC
其中 E = span(e_1..e_r)（在约化坐标下）， B_{A,T} = CA N_C T。

同时记录 dim(E + row B) 与 r + beta 的关系（beta = rank B）。
用**一般有理数**采样。
"""
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


def orb(M, A, n):
    o = []; cur = M
    for _ in range(n):
        o += cur; cur = mm(cur, A)
    return o


def rowspace_basis(M):
    if not M:
        return []
    R, piv = rref(M)
    return [row[:] for row in R if any(x != 0 for x in row)]


rng = random.Random(20250101)


def rand_subspace_generic(L0, Z, d, n):
    BL = rowspace_basis(L0); BZ = rowspace_basis(Z)
    r = len(BL)
    if d < r or d > len(BZ):
        return None
    for _ in range(80):
        rows = [x[:] for x in BL]
        while len(rows) < d:
            c = [F(rng.randint(-97, 97), rng.randint(1, 89)) for _ in range(len(BZ))]
            v = [sum(c[i] * BZ[i][j] for i in range(len(BZ))) for j in range(n)]
            if any(x != 0 for x in v) and rk(rows + [v]) > len(rows):
                rows.append(v)
        if rk(rows) == d:
            return rows
    return None


print(f"{'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'dC':>3} {'beta':>4} {'k':>2} | "
      f"{'dimV':>4} {'r+beta':>6} | {'k+dimV>=dC':>10} {'2p+q0>=n':>8} | {'(A)命中':>9} {'行为':>7}")
print("-" * 96)
rows = []
for trial in range(500):
    n = rng.randint(3, 6)
    p = rng.randint(1, n - 1)
    r = rng.randint(1, n - p)
    got = None
    for _ in range(1200):
        Am = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
        Cm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)]
        Lm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(r)]
        Ac, Cc, Lc = toF(Am), toF(Cm), toF(Lm)
        if rk(Cc) != p or rk(Lc) != r:
            continue
        if rk(Lc + Cc) != r + p:
            continue
        Z = orb(Lc, Ac, n) + orb(Cc, Ac, n); OC = orb(Cc, Ac, n)
        if rk(Z + OC) != rk(OC):
            continue
        got = (Ac, Cc, Lc); break
    if got is None:
        continue
    Ac, Cc, Lc = got
    Lx, eta = p1(Ac, Cc, Lc)
    if not condA(Ac, Cc, Lx):
        continue
    q0 = sum(eta)
    dC = n - p; s = dC - r; k = q0 - r
    if k < 1 or k > s:
        continue
    NC = ker(Cc)
    MC = mm(inv(mm(tr(NC), NC)), tr(NC))
    L0NC = mm(Lc, NC)
    # 构造 T（使 L0NC T = [I|0]）
    Tcols = []
    okT = True
    for i in range(r):
        ei = [F(1) if q == i else F(0) for q in range(r)]
        so = solve([[L0NC[a][j] for j in range(dC)] for a in range(r)], [[ei[a]] for a in range(r)])
        if so is None:
            okT = False; break
        Tcols.append(so[0])
    if not okT:
        continue
    KN = ker(L0NC)
    for j in range(len(KN[0])):
        Tcols.append([KN[i][j] for i in range(dC)])
    T = [[Tcols[j][i] for j in range(dC)] for i in range(dC)]
    if rk(T) != dC:
        continue
    BAT = mm(mm(mm(Cc, Ac), NC), T)
    beta = rk(BAT)
    # E = span(e_1..e_r)
    E = [[F(1) if j == i else F(0) for j in range(dC)] for i in range(r)]
    dimV = rk(E + BAT)
    C_exact = (k + dimV >= dC)
    C_prev = (2 * p + q0 >= n)
    # 行为
    Z = orb(Lc, Ac, n) + orb(Cc, Ac, n)
    a_cnt = tt = 0
    for _ in range(20):
        R = rand_subspace_generic(Lc, Z, q0, n)
        if R is None:
            continue
        tt += 1
        if condA(Ac, Cc, R):
            a_cnt += 1
    if tt < 16:
        continue
    beh = "满测度" if a_cnt == tt else ("零测度" if a_cnt == 0 else "中间!")
    rows.append((C_exact, C_prev, a_cnt == tt, beh))
    if C_exact != C_prev or beh == "中间!" or C_exact != (a_cnt == tt):
        print(f"{n:>2} {p:>2} {r:>2} {q0:>3} {dC:>3} {beta:>4} {k:>2} | "
              f"{dimV:>4} {r+beta:>6} | {str(C_exact):>10} {str(C_prev):>8} | "
              f"{a_cnt:>4}/{tt:<4} {beh:>7}")

print()
okE = okP = tot = 0
mid = 0
for (ce, cp, isopen, beh) in rows:
    tot += 1
    if ce == isopen:
        okE += 1
    if cp == isopen:
        okP += 1
    if beh == "中间!":
        mid += 1
print(f"=== 汇总（{tot} 个实例）===")
print(f"  精确判据 k+dim(E+rowB)>=dC 正确: {okE}/{tot}")
print(f"  先前判据 2p+q0>=n          正确: {okP}/{tot}")
print(f"  出现'中间'的实例数: {mid}")
