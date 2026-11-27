# -*- coding: utf-8 -*-
"""
快速验证「单点猜想」：在规范化 T 坐标系下用浮点秩判据统计 Omega* 的点数。
（P1 解在规范化坐标系下恰为 Θ=0，必在网格上 => 计数 >= 1 是自校验。）
"""
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


def build_norm_T(A, C, L0, Lx):
    n, p, r = len(A), len(C), len(L0)
    NC = ker_basis(C); dC = len(NC[0])
    L0NC = mm(L0, NC); R = Lx[len(L0):]; RNC = mm(R, NC)
    k = len(R); s = dC - r
    if k < 1 or k > s:
        return None
    K = ker_basis(L0NC)
    mK = len(K[0]) if (K and K[0]) else 0
    if mK == 0:
        return None
    Kr = [[K[a][j] for a in range(dC)] for j in range(mK)]
    Tc = []
    for i in range(r):
        ei = [F(1) if q == i else F(0) for q in range(r)]
        so = solve([[L0NC[a][j] for j in range(dC)] for a in range(r)], [[ei[a]] for a in range(r)])
        if so is None:
            return None
        xi = so[0]
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
    MC = mm(inv(mm(tr(NC), NC)), tr(NC))
    Abar = mm(mm(MC, A), NC); BA = mm(mm(C, A), NC)
    return (dC, s, k, r,
            np.array([[float(x) for x in row] for row in mm(mm(Ti, Abar), T)]),
            np.array([[float(x) for x in row] for row in mm(BA, T)]))


def rk_np(M, tol=1e-8):
    if M.size == 0:
        return 0
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s > tol * max(M.shape) * (s[0] if s.size else 1.0)))


rng = random.Random(987654321)
STEP = 3
RANGE = 3
print(f"规范化坐标系下浮点网格扫描（步长 1/{STEP}，范围 [{-RANGE},{RANGE}]，"
      f"{(2*RANGE*STEP+1)**2} 点/实例）")
print()
print(f"{'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'k':>2} {'s':>2} | {'2p+q0':>5} {'<n?':>4} | "
      f"{'命中数':>6} {'Θ=0命中':>7}")
print("-" * 70)
done = 0
found_lt = 0
found_ge = 0
for trial in range(40000):
    if found_lt >= 8 and found_ge >= 1:
        break
    n = rng.randint(3, 5)
    p = rng.randint(1, n - 1)
    r = rng.randint(1, n - p)
    hit = None
    for _ in range(60):
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
        dC = n - p; s = dC - r; k = q0 - r
        if k < 1 or k > s or k * (s - k) > 3:
            continue
        sp = 2 * p + q0
        if sp < n and found_lt >= 6:
            continue
        if sp >= n and found_ge >= 2:
            continue
        bt = build_norm_T(Ac, Cc, Lc, Lx)
        if bt is None:
            continue
        hit = (n, p, r, q0, k, s, sp, bt)
        break
    if hit is None:
        continue
    n, p, r, q0, k, s, sp, bt = hit
    dC, s2, k2, r2, AT, BAT = bt
    vals = [t / STEP for t in range(-RANGE * STEP, RANGE * STEP + 1)]
    cnt = 0
    zero_ok = False
    for a in vals:
        for b in vals:
            W = np.zeros((r + k, dC))
            for i in range(r):
                W[i, i] = 1.0
            for i in range(k):
                W[r + i, r + i] = 1.0
            idx = 0
            for i in range(k):
                for j in range(k, s):
                    W[r + i, r + j] = a if idx == 0 else b
                    idx += 1
            MB = np.vstack([W, BAT])
            MX = np.vstack([W, BAT, W @ AT])
            if rk_np(MB) == rk_np(MX):
                cnt += 1
                if a == 0.0 and b == 0.0:
                    zero_ok = True
    print(f"{n:>2} {p:>2} {r:>2} {q0:>3} {k:>2} {s:>2} | {sp:>5} {str(sp<n):>4} | "
          f"{cnt:>6} {str(zero_ok):>7}")
    if sp < n:
        found_lt += 1
    else:
        found_ge += 1
