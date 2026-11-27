# -*- coding: utf-8 -*-
"""
计数（2p+q0 < n 时）：把 (A) 的失败条件化为标量方程，数值求解并计数孤立点。

要点： (A) 成立 <=> ker[W_J;B] ∩ ker(W_J Abar_T) = {0}
      rank[W_J;B] = dC-1 时该核一维；用 f(Theta)=||W_J Abar_T y|| (y 为单位核向量) 度量。
      f=0 即 (A) 成立。
"""
import itertools
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


def tofloat(M):
    return np.array([[float(x) for x in row] for row in M])


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
    K = ker_basis(L0NC); mK = len(K[0]) if (K and K[0]) else 0
    if mK == 0:
        return None
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


rng = random.Random(271828)

inst = None
for trial in range(4000):
    n = rng.randint(3, 6)
    p = rng.randint(1, n - 1)
    r = rng.randint(1, n - p)
    for _ in range(300):
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
        if k < 1 or k > s or k * (s - k) > 2:
            continue
        pr = prep(Ac, Cc, Lc, Lx)
        if pr is None:
            continue
        inst = (n, p, r, q0, k, s, pr)
        break
    if inst:
        break

if inst is None:
    print("未找到合适的实例")
    raise SystemExit
n, p, r, q0, k, s, pr = inst
dC, s2, k2, r2, AT, BAT = pr
print(f"实例: n={n} p={p} r={r} q0={q0} k={k} s={s} dC={dC}  (2p+q0={2*p+q0} < n={n})")
print(f"Theta 维数 dimT = k(s-k) = {k*(s-k)}")
print()


def Wmat(th):
    """th: dict/array -> W_J (k+r) x dC"""
    W = np.zeros((r + k, dC))
    for i in range(r):
        W[i, i] = 1.0
    idx = 0
    for i in range(k):
        W[r + i, i] = 1.0
        for j in range(k, s):
            W[r + i, r + j] = th[idx] if np.isscalar(th) is False else th
            idx += 1
    return W


def fval(th):
    """||W Abar_T y||, y = 单位核向量 of [W;B]; 返回 nan 若核平凡"""
    W = Wmat(th)
    MB = np.vstack([W, BAT])
    u, sv, vt = np.linalg.svd(MB)
    tol = max(MB.shape) * (sv[0] if sv.size else 1) * 1e-10
    dimk = int(np.sum(sv < tol))
    if dimk == 0:
        return 0.0                     # 核平凡 => (A) 成立
    y = vt[-1]
    v = W @ (AT @ y)
    return float(np.linalg.norm(v))


# 网格扫描 + 局部精化
G = 61
lo, hi = -6.0, 6.0
xs = np.linspace(lo, hi, G)
cands = []
for a in xs:
    for b in xs:
        f = fval(np.array([a, b]))
        if f < 1e-6:
            cands.append((a, b, f))
print(f"网格 {G}x{G} 上 f<1e-6 的点数: {len(cands)}")
if cands:
    from scipy.optimize import minimize
    uniq = []
    for (a, b, f) in cands:
        r_ = minimize(lambda t: fval(t) ** 2, [a, b], method="Nelder-Mead",
                      options={"xatol": 1e-14, "fatol": 1e-20, "maxiter": 4000})
        if r_.fun < 1e-18:
            pt = r_.x
            if not any(np.linalg.norm(pt - q) < 1e-4 for q in uniq):
                uniq.append(pt)
    print(f"精化后相异的解点数: {len(uniq)}")
    for q in uniq:
        print(f"   Theta = ({q[0]:.10f}, {q[1]:.10f})   f = {fval(q):.3e}")
else:
    print("网格未找到；说明解在网格分辨率之外或是代数点（分母较大）")
