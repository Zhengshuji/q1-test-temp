# -*- coding: utf-8 -*-
"""
定向确认：在 2p+q0 >= n 的实例上，随机采样的 (A) 命中率应为 100%（因 Omega* 是开集）。
          在 2p+q0 <  n 的实例上，命中率应为 0（孤立点，测度零）。

同时检验 (A)∧(S) 的命中率是否同为 0/1。
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


def condS(A, C, L):
    LA = mm(L, A); rhs = rk(L + C + mm(C, A)); n = len(A)
    cs = set()
    for k in range(-12, 13):
        for d in (1, 2, 3, 4):
            cs.add(F(k, d))
    try:
        import numpy as np
        for ev in np.linalg.eigvals(np.array([[float(x) for x in r] for r in A])):
            if abs(ev.imag) < 1e-7:
                cs.add(F(float(ev.real)).limit_denominator(2000))
        Lf = np.array([[float(x) for x in r] for r in L])
        LAf = Lf @ np.array([[float(x) for x in r] for r in A])
        if Lf.shape[0] == Lf.shape[1]:
            for ev in np.linalg.eigvals(np.linalg.solve(Lf, LAf)):
                if abs(ev.imag) < 1e-7:
                    cs.add(F(float(ev.real)).limit_denominator(2000))
    except Exception:
        pass
    for s in sorted(cs):
        sl = [[s * L[i][j] - LA[i][j] for j in range(n)] for i in range(len(L))]
        if rk(sl + C + mm(C, A)) != rhs:
            return False
    return True


def rowspace_basis(M):
    if not M:
        return []
    R, piv = rref(M)
    return [row[:] for row in R if any(x != 0 for x in row)]


rng = random.Random(777)


def orb(M, A, n):
    o = []; cur = M
    for _ in range(n):
        o += cur; cur = mm(cur, A)
    return o


def rand_subspace(L0, Z, d, n):
    """随机取 d 维 R，row(L0) ⊆ R ⊆ Z"""
    BL = rowspace_basis(L0)
    BZ = rowspace_basis(Z)
    r = len(BL)
    if d < r or d > len(BZ):
        return None
    for _ in range(50):
        rows = [x[:] for x in BL]
        while len(rows) < d:
            c = [F(rng.randint(-3, 3)) for _ in range(len(BZ))]
            v = [sum(c[i] * BZ[i][j] for i in range(len(BZ))) for j in range(n)]
            if any(x != 0 for x in v) and rk(rows + [v]) > len(rows):
                rows.append(v)
        if rk(rows) == d:
            return rows
    return None


print(f"{'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'2p+q0':>5} {'>=n?':>5} | "
      f"{'(A)命中':>12} {'(A)∧(S)命中':>14} {'判定':>10}")
print("-" * 78)
N = 25
cnt = {"ge": 0, "lt": 0}
for trial in range(80):
    n = rng.randint(3, 6)
    p = rng.randint(1, n - 1)
    r = rng.randint(1, n - p)
    got = None
    for _ in range(3000):
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
    if q0 < r or q0 > rk(orb(Lc, Ac, n) + orb(Cc, Ac, n)):
        continue
    Z = orb(Lc, Ac, n) + orb(Cc, Ac, n)
    a_cnt = s_cnt = tt = 0
    for _ in range(N):
        R = rand_subspace(Lc, Z, q0, n)
        if R is None:
            continue
        tt += 1
        if condA(Ac, Cc, R):
            a_cnt += 1
            if condS(Ac, Cc, R):
                s_cnt += 1
    if tt < N * 0.8:
        continue
    ge = (2 * p + q0 >= n)
    verdict = ("开集/全命中" if a_cnt == tt else ("孤立/全不中" if a_cnt == 0 else "中间!"))
    flag = ""
    if ge and a_cnt != tt:
        flag = "  <== 与预测不符!"
    if (not ge) and a_cnt != 0:
        flag = "  <== 与预测不符!"
    print(f"{n:>2} {p:>2} {r:>2} {q0:>3} {2*p+q0:>5} {str(ge):>5} | "
          f"{a_cnt:>5}/{tt:<6} {s_cnt:>6}/{tt:<7} {verdict:>10}{flag}")
    cnt["ge" if ge else "lt"] += 1

print()
print(f"统计：2p+q0>=n 的实例 {cnt['ge']} 个，2p+q0<n 的实例 {cnt['lt']} 个")
