# -*- coding: utf-8 -*-
"""
检验引理 6 的结论：情形 I（d_CA < q0）中 (S) 是否**开**（局部扰动保持）。
方法：找到 (A)∧(S) 成立的点，向各坐标方向扰动，检查 (A) 与 (S) 是否仍成立。
用可靠 (S) 判据（ρ 阶子式的多项式 gcd）。
"""
import random
from fractions import Fraction as F

srctxt = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\reliable_S_test.py",
              encoding="utf-8").read()
head = srctxt.split("# ---------- 主实验 ----------")[0]
exec(head)


def build_T_and_data(Ac, Cc, Lc, Lx):
    """返回 (r,k,s,dC, AT, BAT, Ti, MC)"""
    n = len(Ac); p = len(Cc); r = len(Lc)
    dC = n - p; s = dC - r
    q0 = len(Lx)
    k = q0 - r
    bt = build_norm_T(Ac, Cc, Lc, Lx)
    if bt is None:
        return None
    dC2, s2, k2, r2, AT, BAT = bt
    if (r2, k2, s2, dC2) != (r, k, s, dC):
        return None
    NC = ker_basis(Cc)
    MC = mm(inv(mm(tr(NC), NC)), tr(NC))
    L0NC = mm(Lc, NC)
    R = Lx[len(Lc):]; RNC = mm(R, NC)
    K = ker_basis(L0NC); mK = len(K[0]) if (K and K[0]) else 0
    if mK == 0:
        return None
    Kr = [[K[a][j] for a in range(dC)] for j in range(mK)]
    Tcols = []
    for i in range(r):
        ei = [F(1) if q == i else F(0) for q in range(r)]
        so = solve([[L0NC[a][j] for j in range(dC)] for a in range(r)],
                   [[ei[a]] for a in range(r)])
        if so is None:
            return None
        xi = so[0]
        tgt = mm(RNC, [[xi[j]] for j in range(dC)])[0][0]
        rkl = [mm(RNC, [[Kr[j][a] for a in range(dC)]])[0][0] for j in range(mK)]
        c = [F(0)] * mK
        for j in range(mK):
            if rkl[j] != 0:
                c[j] = -tgt / rkl[j]; break
        z = [sum(c[j] * Kr[j][a] for j in range(mK)) for a in range(dC)]
        Tcols.append([xi[a] + z[a] for a in range(dC)])
    rkmat = [[mm(RNC, [[Kr[j][a] for a in range(dC)]])[ii][0] for j in range(mK)]
             for ii in range(k)]
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
        Tcols.append([sum(yj[a] * Kr[a][jj] for a in range(mK)) for jj in range(dC)])
    T = [[Tcols[j][i] for j in range(dC)] for i in range(dC)]
    Ti = inv(T)
    if Ti is None:
        return None
    return r, k, s, dC, AT, BAT, Ti, MC


def WJ_of(t, r, k, s, dC):
    WJ = []
    for i in range(r):
        WJ.append([F(1) if j == i else F(0) for j in range(dC)])
    idx = 0
    for i in range(k):
        row = [F(0)] * dC
        row[r + i] = F(1)
        for j in range(k, s):
            row[r + j] = t[idx]; idx += 1
        WJ.append(row)
    return WJ


rng = random.Random(5309530)
print("检验引理 6：(S) 在情形 I（d_CA < q0）中是否开")
print()
print(f"{'n':>2} {'p':>2} {'r':>2} {'q0':>3} | {'d_CA':>4} | {'(A)∧(S)点':>9} | "
      f"{'扰动后仍(A)∧(S)':>16}")
print("-" * 62)
tested = 0
for trial in range(30000):
    if tested >= 6:
        break
    n = rng.randint(3, 6)
    p = rng.randint(1, n - 1)
    r = rng.randint(1, n - p)
    for _ in range(80):
        Am = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
        Cm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)]
        Lm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(r)]
        Ac, Cc, Lc = toF(Am), toF(Cm), toF(Lm)
        if rk(Cc) != p or rk(Lc) != r: continue
        if rk(Lc + Cc) != r + p: continue
        Z = orb(Lc, Ac, n) + orb(Cc, Ac, n); OC = orb(Cc, Ac, n)
        if rk(Z + OC) != rk(OC): continue
        try:
            Lx, eta = p1(Ac, Cc, Lc)
        except Exception:
            continue
        if not condA(Ac, Cc, Lx): continue
        q0 = sum(eta)
        dC = n - p; s = dC - r; k = q0 - r
        if k < 1 or k > s: continue
        if 2 * p + q0 < n: continue
        bd = build_T_and_data(Ac, Cc, Lx[:0] + Lx, Lx)
        if bd is None: continue
        r2, k2, s2, dC2, AT, BAT, Ti, MC = bd
        CA = mm(Cc, Ac)
        NCA = ker_basis(CA + Cc)
        dCA = len(NCA[0]) if (NCA and NCA[0]) else 0
        if not (dCA < q0): continue          # 只要情形 I
        # 找一个 (A)∧(S) 点
        good = None
        for _try in range(60):
            t = [F(rng.randint(-97, 97), rng.randint(1, 89)) *
                 (1 if rng.random() < 0.5 else -1) for _ in range(k * (s - k))]
            WJ = WJ_of(t, r, k, s, dC)
            if rk(WJ + BAT + mm(WJ, AT)) != rk(WJ + BAT):
                continue
            Lred = mm(mm(WJ, Ti), MC)
            if dCA == 0:
                good = t; break
            Hm = mm(Lred, NCA); Fm = mm(mm(Lred, Ac), NCA)
            if S_holds(Hm, Fm):
                good = t; break
        if good is None:
            continue
        # 扰动检验
        keep = 0; total = 0
        base = good
        for _p2 in range(12):
            t2 = base[:]
            for a in range(len(t2)):
                t2[a] += F(rng.randint(-3, 3), rng.randint(100, 1000)) * \
                    (1 if rng.random() < 0.5 else -1)
            WJ = WJ_of(t2, r, k, s, dC)
            total += 1
            if rk(WJ + BAT + mm(WJ, AT)) != rk(WJ + BAT):
                continue
            Lred = mm(mm(WJ, Ti), MC)
            if dCA == 0 or S_holds(mm(Lred, NCA), mm(mm(Lred, Ac), NCA)):
                keep += 1
        tested += 1
        print(f"{n:>2} {p:>2} {r:>2} {q0:>3} | {dCA:>4} | {str(good)[:9]:>9} | "
              f"{keep:>3}/{total:<12}")
        break

print()
print("预期：若 (S) 开，则扰动后应几乎全部保持 (A)∧(S)（keep ≈ total）")
