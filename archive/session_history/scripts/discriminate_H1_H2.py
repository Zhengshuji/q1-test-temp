# -*- coding: utf-8 -*-
"""
判别实验：区分两个假说
  H1: s = k+1  <=> Omega* 开
  H2: p >= s-k  <=> Omega* 开      （由 rank[W_J;B]=d_C 是开条件推出）

关键：构造 p >= 2 且 s-k >= 2 的实例（此时 H1 假、H2 可能真）。
     以及 p < s-k 的实例（H1/H2 都假）。
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


def prep(A, C, L0, Lx):
    n, p, r = len(A), len(C), len(L0)
    NC = ker(C); dC = len(NC[0])
    MC = mm(inv(mm(tr(NC), NC)), tr(NC))
    L0NC = mm(L0, NC); R = Lx[len(L0):]; RNC = mm(R, NC)
    K = ker(L0NC); mK = len(K[0]) if (K and K[0]) else 0
    if mK == 0:
        return None
    k = len(R); s = dC - r
    if k < 1 or k > s:
        return None
    Kr = [[K[a][j] for a in range(dC)] for j in range(mK)]
    Tc = []
    for i in range(r):
        ei = [F(1) if q == i else F(0) for q in range(r)]
        so = solve([[L0NC[a][j] for j in range(dC)] for a in range(r)], [[ei[a]] for a in range(r)])
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
    Abar = mm(mm(MC, A), NC); BA = mm(mm(C, A), NC)
    RNCT = mm(RNC, T)
    return Ti, mm(mm(Ti, Abar), T), mm(BA, T), dC, s, k, RNCT


rng = random.Random(31337)


def orb(M, A, n):
    o = []; cur = M
    for _ in range(n):
        o += cur; cur = mm(cur, A)
    return o


print("判别实验：H1 (s=k+1) vs H2 (p >= s-k)")
print()
print(f"{'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'k':>2} {'s':>2} | {'s-k':>4} {'p>=s-k':>7} | "
      f"{'Theta0':>7} {'可扰动':>7} {'行为':>8} {'H1':>4} {'H2':>4}")
print("-" * 82)
res = {}
for trial in range(600):
    n = rng.randint(4, 7)
    p = rng.randint(1, n - 1)
    r = rng.randint(1, n - p)
    got = None
    for _ in range(4000):
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
    pr = prep(Ac, Cc, Lc, Lx)
    if pr is None:
        continue
    Ti, AT, BAT, dC, s, k, RNCT = pr
    q0 = sum(eta)
    # 关注 p>=2 且 s-k>=2 的情形（H1 假）
    if not (p >= 2 and s - k >= 2):
        continue
    key = (p, k, s)
    if key in res:
        continue
    Ymat = [[RNCT[i][r + j] for j in range(s)] for i in range(k)]

    def testY(Y):
        W = [[F(1) if jj == ii else F(0) for jj in range(dC)] for ii in range(r)]
        for i in range(k):
            W.append([F(0)] * r + Y[i])
        return rk(W + BAT + mm(W, AT)) == rk(W + BAT)

    ok0 = testY(Ymat)
    dimT = k * (s - k)
    dirs = 0
    for i in range(k):
        for j in range(k, s):
            good = False
            for e in (F(1, 7), F(1, 100), F(1, 1000)):
                Yt = [row[:] for row in Ymat]
                Yt[i][j] += e
                if testY(Yt):
                    good = True; break
            if good:
                dirs += 1
    beh = "开集" if dirs == dimT and dimT > 0 else ("孤立" if dirs == 0 else "中间")
    h1 = (s == k + 1)
    h2 = (p >= s - k)
    res[key] = (n, p, r, q0, k, s, dimT, dirs, beh, h1, h2)
    print(f"{n:>2} {p:>2} {r:>2} {q0:>3} {k:>2} {s:>2} | {s-k:>4} {str(h2):>7} | "
          f"{str(ok0):>7} {dirs:>3}/{dimT:<3} {beh:>8} {str(h1):>4} {str(h2):>4}")

print()
print("汇总：")
for key in sorted(res):
    n, p, r, q0, k, s, dimT, dirs, beh, h1, h2 = res[key]
    pred1 = "开集" if h1 else "非开"
    pred2 = "开集" if h2 else "非开"
    print(f"  (p,k,s)=({p},{k},{s}) 实际={beh:<4} H1预测={pred1:<4} H2预测={pred2:<4} "
          f"{'H1✓' if (beh=='开集')==h1 else 'H1✗'} {'H2✓' if (beh=='开集')==h2 else 'H2✗'}")
