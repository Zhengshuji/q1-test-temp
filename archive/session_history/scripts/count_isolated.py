# -*- coding: utf-8 -*-
"""
统计 2p+q0 < n 时 Omega* 的孤立点数（0 维解集大小）。

方法：用一般有理数在 Theta 空间做细网格 + 局部扰动，
      估计 Omega* 的点数随 (n, p, q0) 的增长。
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


def orb(M, A, n):
    o = []; cur = M
    for _ in range(n):
        o += cur; cur = mm(cur, A)
    return o


rng = random.Random(600613)


print("统计 2p+q0 < n 时 Omega* 的孤立点数（在 Theta 图上搜索）")
print()
print(f"{'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'k':>2} {'s':>2} {'dimT':>4} | {'网格命中':>8} {'说明':>22}")
print("-" * 70)
seen = set()
count = 0
for trial in range(3000):
    if count >= 14:
        break
    n = rng.randint(3, 6)
    p = rng.randint(1, n - 1)
    r = rng.randint(1, n - p)
    got = None
    for _ in range(400):
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
    if 2 * p + q0 >= n:
        continue                      # 只要 2p+q0 < n
    if (k, s) in seen:
        continue
    seen.add((k, s)); count += 1
    # 在 Theta 图上细密搜索（k x (s-k) 维）
    NC = ker(Cc)
    MC = mm(inv(mm(tr(NC), NC)), tr(NC))
    L0NC = mm(Lc, NC)
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
    Ti = inv(T)
    if Ti is None:
        continue
    Abar = mm(mm(MC, Ac), NC); BA = mm(mm(Cc, Ac), NC)
    AT = mm(mm(Ti, Abar), T); BAT = mm(BA, T)
    dimT = k * (s - k)
    hits = 0
    GRID = [F(a, 3) for a in range(-8, 9)]
    if dimT <= 3:
        if dimT == 0:
            combos = [()]
        else:
            combos = itertools.product(GRID, repeat=dimT)
        for cc in combos:
            Y = [[F(0)] * s for _ in range(k)]
            idx = 0
            for i in range(k):
                for j in range(k, s):
                    Y[i][j] = cc[idx]; idx += 1
                Y[i][i] = F(1) if i < k else F(0)
            # 归位：pivot 在对角（i<k）
            W = [[F(1) if jj == ii else F(0) for jj in range(dC)] for ii in range(r)]
            for i in range(k):
                W.append([F(0)] * r + Y[i])
            if rk(W + BAT + mm(W, AT)) == rk(W + BAT):
                hits += 1
    else:
        # 维数太高，随机采样
        for _ in range(3000):
            Y = [[F(0)] * s for _ in range(k)]
            for i in range(k):
                Y[i][i] = F(1)
                for j in range(k, s):
                    Y[i][j] = F(rng.randint(-9, 9), rng.randint(1, 9))
            W = [[F(1) if jj == ii else F(0) for jj in range(dC)] for ii in range(r)]
            for i in range(k):
                W.append([F(0)] * r + Y[i])
            if rk(W + BAT + mm(W, AT)) == rk(W + BAT):
                hits += 1
    print(f"{n:>2} {p:>2} {r:>2} {q0:>3} {k:>2} {s:>2} {dimT:>4} | {hits:>8} "
          f"{'穷举' if dimT<=3 else '随机3000':>22}")
