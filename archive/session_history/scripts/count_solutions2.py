# -*- coding: utf-8 -*-
"""计数 2p+q0<n 时 Omega* 的孤立点：用稳健的秩比较 + 网格聚类。"""
import random
from fractions import Fraction as F

import numpy as np


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


def ker_basis(M):
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


def prep(A, C, L0, Lx):
    n, p, r = len(A), len(C), len(L0)
    NC = ker_basis(C); dC = len(NC[0])
    MC = mm(inv(mm(tr(NC), NC)), tr(NC))
    L0NC = mm(L0, NC); R = Lx[len(L0):]
    k = len(R); s = dC - r
    if k < 1 or k > s:
        return None
    Tcols = []
    for i in range(r):
        ei = [F(1) if q == i else F(0) for q in range(r)]
        so = solve([[L0NC[a][j] for j in range(dC)] for a in range(r)], [[ei[a]] for a in range(r)])
        if so is None:
            return None
        Tcols.append(so[0])
    KN = ker_basis(L0NC)
    for j in range(len(KN[0])):
        Tcols.append([KN[i][j] for i in range(dC)])
    T = [[Tcols[j][i] for j in range(dC)] for i in range(dC)]
    Ti = inv(T)
    if Ti is None:
        return None
    Abar = mm(mm(MC, A), NC); BA = mm(mm(C, A), NC)
    return dC, s, k, r, np.array([[float(x) for x in row] for row in mm(mm(Ti, Abar), T)]), \
        np.array([[float(x) for x in row] for row in mm(BA, T)])


def rk_np(M, tol=1e-9):
    if M.size == 0:
        return 0
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s > tol * max(M.shape) * (s[0] if s.size else 1)))


rng = random.Random(271828)
insts = []
for trial in range(6000):
    if len(insts) >= 3:
        break
    n = rng.randint(3, 6)
    p = rng.randint(1, n - 1)
    r = rng.randint(1, n - p)
    for _ in range(250):
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
        Lx, eta = p1(Ac, Cc, Lc)
        if not condA(Ac, Cc, Lx):
            continue
        q0 = sum(eta)
        if 2 * p + q0 >= n:
            continue
        dC = n - p; s = dC - r; k = q0 - r
        if k < 1 or k > s or k * (s - k) != 2:
            continue
        pr = prep(Ac, Cc, Lc, Lx)
        if pr is None:
            continue
        insts.append((n, p, r, q0, k, s, pr))
        break

print(f"找到 {len(insts)} 个 (2p+q0<n, dimTheta=2) 的实例\n")
for (n, p, r, q0, k, s, pr) in insts:
    dC, s2, k2, r2, AT, BAT = pr

    def ok(th):
        W = np.zeros((r + k, dC))
        for i in range(r):
            W[i, i] = 1.0
        idx = 0
        for i in range(k):
            W[r + i, i] = 1.0
            for j in range(k, s):
                W[r + i, r + j] = th[idx]; idx += 1
        MB = np.vstack([W, BAT])
        MX = np.vstack([W, BAT, W @ AT])
        return rk_np(MB) == rk_np(MX)

    G = 81
    xs = np.linspace(-8, 8, G)
    hits = []
    for a in xs:
        for b in xs:
            if ok(np.array([a, b])):
                hits.append((a, b))
    print(f"实例 n={n} p={p} r={r} q0={q0} k={k} s={s} dC={dC}: "
          f"网格 {G}x{G} 命中 {len(hits)} 个点")
    # 聚类
    clusters = []
    for (a, b) in hits:
        placed = False
        for c in clusters:
            if abs(c[0][0] - a) < 0.5 and abs(c[0][1] - b) < 0.5:
                c.append((a, b)); placed = True; break
        if not placed:
            clusters.append([(a, b)])
    print(f"   聚类后簇数 = {len(clusters)}")
    for c in clusters[:8]:
        cx = sum(t[0] for t in c) / len(c); cy = sum(t[1] for t in c) / len(c)
        print(f"     簇中心 ≈ ({cx:+.3f}, {cy:+.3f})  含 {len(c)} 格")
    print()
