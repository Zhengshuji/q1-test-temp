# -*- coding: utf-8 -*-
"""
验证定理 7 的推导（r=p=k=1, s=3, dC=4）：
  1. u(θ) = (0, b4θ1-b3θ2, -(b4-b2θ2), b3-b2θ1)  是否真的张成 row(M)^⊥
  2. (A) 是否 ⟺ (u·a1 = 0 且 u·a2 = 0)
  3. 这两个方程是否恰为「线性」+「二次」
  4. 解集是否 ≤ 2 点
全程用精确有理算术。
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


def prep(A, C, L0, Lx):
    n, p, r = len(A), len(C), len(L0)
    NC = ker_basis(C); dC = len(NC[0])
    MC = mm(inv(mm(tr(NC), NC)), tr(NC))
    L0NC = mm(L0, NC); R = Lx[len(L0):]
    k = len(R); s = dC - r
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
    return dC, s, k, r, mm(mm(Ti, Abar), T), mm(BA, T)


rng = random.Random(24680)
found = None
for trial in range(400):
    n, p, r = 5, 1, 1
    for _ in range(200):
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
        pr = prep(Ac, Cc, Lc, Lx)
        if pr is None:
            continue
        dC, s, k, r, AT, BAT = pr
        if (r, p, k, s, dC) != (1, 1, 1, 3, 4):
            continue
        found = (Ac, Cc, Lc, AT, BAT, q0)
        break
    if found:
        break

if not found:
    print("未找到 r=p=k=1,s=3 的实例")
    raise SystemExit

Ac, Cc, Lc, AT, BAT, q0 = found
b = BAT[0]
a1 = AT[0]
a2 = AT[1]; a3 = AT[2]; a4 = AT[3]
print("实例: r=p=k=1, s=3, dC=4,  q0 =", q0)
print("  b  =", [str(x) for x in b])
print("  a1 =", [str(x) for x in a1])
print()

# 检查 b2 != 0（推导中用到除法）
assert b[1] != 0, "b2=0，需换坐标"

def u_of(t1, t2):
    return [F(0), b[3] * t1 - b[2] * t2, -(b[3] - b[1] * t2), b[2] - b[1] * t1]

def M_of(t1, t2):
    return [[F(1), F(0), F(0), F(0)], [F(0), F(1), t1, t2], b[:]]

def Aof(t1, t2):
    W = [[F(1), F(0), F(0), F(0)], [F(0), F(1), t1, t2]]
    N = W + [a1[:], [a2[j] + t1 * a3[j] + t2 * a4[j] for j in range(4)]]
    MB = M_of(t1, t2)
    return rk(MB + N[2:]) == rk(MB)

print("=== 验证 u(θ) 张成 row(M)^⊥ ===")
ok = True
for (t1, t2) in [(F(1), F(2)), (F(-3), F(5)), (F(7, 2), F(-1, 3))]:
    u = u_of(t1, t2)
    for row in M_of(t1, t2):
        s_ = sum(row[i] * u[i] for i in range(4))
        if s_ != 0:
            ok = False
print("  u·M = 0 对所有测试点:", ok)
print()

print("=== 验证 (A) ⟺ u·a1=0 且 u·a2=0 ===")
agree = 0; tot = 0
for t1 in [F(a, 2) for a in range(-8, 9)]:
    for t2 in [F(a, 2) for a in range(-8, 9)]:
        u = u_of(t1, t2)
        e1 = sum(u[i] * a1[i] for i in range(4))
        e2 = sum(u[i] * a2[i] for i in range(4))
        pred = (e1 == 0 and e2 == 0)
        real = Aof(t1, t2)
        tot += 1
        if pred == real:
            agree += 1
        elif tot < 5:
            print(f"   分歧 θ=({t1},{t2}): pred={pred} real={real}")
print(f"  一致: {agree}/{tot}")
print()

print("=== 检查两个方程的次数（作为 θ1,θ2 的多项式）===")
# 用差分判次数
def degree(f):
    # f: (t1,t2)->Fraction ; 在 (0,0) 附近取点做二阶差分
    f00 = f(F(0), F(0)); f10 = f(F(1), F(0)); f01 = f(F(0), F(1))
    f20 = f(F(2), F(0)); f11 = f(F(1), F(1)); f02 = f(F(0), F(2))
    # 线性: f20-2f10+f00=0 且 f02-2f01+f00=0 且 f11-f10-f01+f00=0
    lin = (f20 - 2 * f10 + f00 == 0) and (f02 - 2 * f01 + f00 == 0) and (f11 - f10 - f01 + f00 == 0)
    return "线性" if lin else "非线性(次数≥2)"

def f1(t1, t2):
    u = u_of(t1, t2); return sum(u[i] * a1[i] for i in range(4))
def f2(t1, t2):
    u = u_of(t1, t2); return sum(u[i] * a2[i] for i in range(4))
print(f"  方程1 (u·a1): {degree(f1)}")
print(f"  方程2 (u·a2): {degree(f2)}")
print()

print("=== 求全部解（直线 ∩ 圆锥曲线），精确）===")
sols = []
for t1 in [F(a, 12) for a in range(-96, 97)]:
    for t2 in [F(a, 12) for a in range(-96, 97)]:
        if Aof(t1, t2):
            sols.append((t1, t2))
print(f"  细网格 (步长 1/12) 找到的解数: {len(sols)}")
for s_ in sols[:10]:
    print(f"    ({s_[0]}, {s_[1]})")
