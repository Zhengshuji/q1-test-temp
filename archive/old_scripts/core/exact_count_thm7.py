# -*- coding: utf-8 -*-
"""
(r=p=k=1, s=3) 情形的**严格解数**：直线 ∩ 圆锥曲线，用判别式精确判定。

定理 7 给出 (A) <=> f1(θ)=0 且 f2(θ)=0，其中 f1 一次、f2 二次。
本脚本精确计算这两个多项式，消元后求一元二次方程的判别式 Δ，从而**严格**给出实数解个数。
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
    return dC, s, k, r, mm(mm(Ti, Abar), T), mm(BA, T)


rng = random.Random(112233)
found = None
for trial in range(30000):
    n, p, r = 5, 1, 1
    for _ in range(150):
        Am = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
        Cm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)]
        Lm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(r)]
        Ac, Cc, Lc = toF(Am), toF(Cm), toF(Lm)
        if rk(Cc) != p or rk(Lc) != r: continue
        if rk(Lc + Cc) != r + p: continue
        Z = orb(Lc, Ac, n) + orb(Cc, Ac, n); OC = orb(Cc, Ac, n)
        if rk(Z + OC) != rk(OC): continue
        Lx, eta = p1(Ac, Cc, Lc)
        if not condA(Ac, Cc, Lx): continue
        if sum(eta) != 2: continue
        bt = build_norm_T(Ac, Cc, Lc, Lx)
        if bt is None: continue
        dC, s, k, r2, AT, BAT = bt
        if (r2, p, k, s, dC) != (1, 1, 1, 3, 4): continue
        found = (AT, BAT); break
    if found: break

if not found:
    print("未找到实例"); raise SystemExit
AT, BAT = found
b = BAT[0]
a1, a2, a3, a4 = AT[0], AT[1], AT[2], AT[3]
print("实例 (r=p=k=1, s=3, dC=4)  [规范化 T 坐标系，P1 解应在 Θ=0]")
print("  b  =", [str(x) for x in b])
print("  a1 =", [str(x) for x in a1])
print()

# u(θ) = (0, b4θ1-b3θ2, -(b4-b2θ2), b3-b2θ1)   （要求 b2 != 0）
assert b[1] != 0, "b2=0"
def u(t1, t2):
    return [F(0), b[3]*t1 - b[2]*t2, -(b[3] - b[1]*t2), b[2] - b[1]*t1]

# f1 = u·a1 (一次), f2 = u·a2(θ) (二次)
def f1(t1, t2):
    uu = u(t1, t2); return sum(uu[i]*a1[i] for i in range(4))
def f2(t1, t2):
    uu = u(t1, t2)
    a2v = [a2[j] + t1*a3[j] + t2*a4[j] for j in range(4)]
    return sum(uu[i]*a2v[i] for i in range(4))

# 提取系数
f1_00, f1_10, f1_01 = f1(F(0),F(0)), f1(F(1),F(0)), f1(F(0),F(1))
c1_0, c1_1, c1_2 = f1_00, f1_10 - f1_00, f1_01 - f1_00
print(f"  f1 = ({c1_0}) + ({c1_1})·θ1 + ({c1_2})·θ2   [线性]")

# f2 的系数（二次）
f2_00 = f2(F(0),F(0))
f2_10, f2_01 = f2(F(1),F(0)), f2(F(0),F(1))
f2_20, f2_11, f2_02 = f2(F(2),F(0)), f2(F(1),F(1)), f2(F(0),F(2))
c2_11 = f2_11 - f2_10 - f2_01 + f2_00
c2_20 = (f2_20 - 2*f2_10 + f2_00) / 2      # 注意除 2
c2_02 = (f2_02 - 2*f2_01 + f2_00) / 2      # 注意除 2
c2_10 = f2_10 - f2_00
c2_01 = f2_01 - f2_00
c2_00 = f2_00
# 校验：f2 = c00 + c10 θ1 + c01 θ2 + c20 θ1² + c11 θ1θ2 + c02 θ2²
def f2_check(t1, t2):
    return (c2_00 + c2_10*t1 + c2_01*t2 + c2_20*t1*t1 + c2_11*t1*t2 + c2_02*t2*t2)
mism = [(t1,t2) for t1 in [F(-2),F(0),F(1),F(3)] for t2 in [F(-1),F(0),F(2),F(5)] if f2(t1,t2) != f2_check(t1,t2)]
for mm_ in mism[:3]:
    print("    MISMATCH at", mm_, "f2=", f2(*mm_), "check=", f2_check(*mm_))
print("    c2_20 =", c2_20, " 2*c2_20 =", 2*c2_20)
ok = all(f2(t1,t2) == f2_check(t1,t2)
         for t1 in [F(-2),F(0),F(1),F(3)] for t2 in [F(-1),F(0),F(2),F(5)])
print(f"  f2 的系数分解校验: {ok}")
print(f"  f2 = {c2_00} + {c2_10}θ1 + {c2_01}θ2 + {c2_20}θ1² + {c2_11}θ1θ2 + {c2_02}θ2²")
print()

# 用 f1 消元：c1_1 θ1 + c1_2 θ2 + c1_0 = 0
assert c1_1 != 0 or c1_2 != 0, "f1 退化"
if c1_1 != 0:
    # θ1 = (-c1_0 - c1_2 θ2)/c1_1
    def th1(t2): return (-c1_0 - c1_2*t2)/c1_1
    # 代入 f2 得一元二次 in t2
    A2 = (c2_20*(c1_2/c1_1)**2 - c2_11*(c1_2/c1_1) + c2_02)
    # 展开更稳妥：逐项代入
    Am_ = c2_20; Bm_ = -c1_2/c1_1; Cm_ = -c1_0/c1_1
    # θ1 = Bm_ t2 + Cm_
    Acoef = Am_*Bm_*Bm_ + c2_11*Bm_ + c2_02
    Bcoef = 2*Am_*Bm_*Cm_ + c2_10*Bm_ + c2_11*Cm_ + c2_01
    Ccoef = Am_*Cm_*Cm_ + c2_10*Cm_ + c2_00
    print("  代入后的一元二次（关于 θ2）:")
    print(f"    A={Acoef},  B={Bcoef},  C={Ccoef}")
    if Acoef == 0:
        print(f"  => 退化为一次：解数 = {0 if Bcoef==0 else 1}")
    else:
        Disc = Bcoef*Bcoef - 4*Acoef*Ccoef
        print(f"  判别式 Δ = {Disc}")
        sgn = ">0 => 两个实解" if Disc > 0 else ("=0 => 一个重根" if Disc == 0 else "<0 => 无实解")
        print(f"  => {sgn}")
        if Disc >= 0:
            import math
            d = math.isqrt(Disc.numerator) if Disc >= 0 else 0
            print(f"  Δ 是否为完全平方（有理根）: "
                  f"{Disc >= 0 and (Disc.numerator*Disc.denominator) == 0 or False}")
            # 精确判是否为有理数平方
            def is_sq_frac(x):
                if x < 0: return False
                n, d2 = x.numerator, x.denominator
                rn, rd = math.isqrt(n), math.isqrt(d2)
                return rn*rn == n and rd*rd == d2
            print(f"  Δ 是否为有理平方（=> 解有理）: {is_sq_frac(Disc)}")
            rt = None
            if is_sq_frac(Disc):
                import math as _m
                rn = _m.isqrt(Disc.numerator); rd = _m.isqrt(Disc.denominator)
                rt = F(rn, rd)
            if rt is not None:
                for t2v in [(-Bcoef + rt)/(2*Acoef), (-Bcoef - rt)/(2*Acoef)]:
                    t1v = th1(t2v)
                    print(f"    解: θ=({t1v}, {t2v})   f1={f1(t1v,t2v)}  f2={f2(t1v,t2v)}")
