# -*- coding: utf-8 -*-
"""
重验 K/K' 判据（修正两处错误）：
  (i) 正确的「图」是 Γ' = {(Θv, v) : v ∈ R^{s-k}}，维数 = s-k（不是 k）
  (ii) 正确的零空间矩阵是 [B^(1) | −B^(2)]（带负号）

  K  = ker[ B2^(1) | −B2^(2) ]
  K' = ker[ Γ^(1) | −Γ^(2) ]
  (A) <=> Γ' ∩ K ⊆ K'

对照 (a) = 三块既约形式。包含 True 点 Θ=0。
"""
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\exact_count_thm7.py",
           encoding="utf-8").read()
exec(src.split("rng = random.Random(112233)")[0])


def sub_basis_cols(M):
    """返回列向量形式的核基（n × m）"""
    return ker_basis(M)


def intersect(Gcols, Kcols, n):
    """Gcols, Kcols: n×m 列基。返回交集的列基 n×t"""
    dG = len(Gcols[0]) if Gcols and Gcols[0] else 0
    dK = len(Kcols[0]) if Kcols and Kcols[0] else 0
    if dG == 0 or dK == 0:
        return []
    # 交 = ker[ A | -B ] 映射回
    # 解 sum a_i G_i = sum b_j K_j  =>  用标准法：
    # 令 Z = [G | -K]，求 ker(Z) 分成 (a,b)，x = G a
    Z = [[Gcols[i][a] for a in range(dG)] + [-Kcols[i][b] for b in range(dK)]
         for i in range(n)]
    Zb = ker_basis(Z)                      # (dG+dK) × t  列基
    if not Zb or not Zb[0]:
        return []
    t = len(Zb[0])
    out = []
    for s_ in range(t):
        coef = [Zb[i][s_] for i in range(dG)]
        vec = [sum(coef[a] * Gcols[i][a] for a in range(dG)) for i in range(n)]
        out.append(vec)
    return out


rng = random.Random(24680)
print("重验 K/K' 判据（修正版）")
print(f"{'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'k':>2} {'s':>2} | {'一致':>8} {'(a)命中':>8} {'(b)命中':>8}")
print("-" * 62)
insts = 0
for trial in range(6000):
    if insts >= 8:
        break
    n = rng.randint(5, 6)
    p = 1
    r = 1
    got = None
    for _ in range(200):
        Am = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
        Cm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)]
        Lm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(r)]
        Ac, Cc, Lc = toF(Am), toF(Cm), toF(Lm)
        if rk(Cc) != p or rk(Lc) != r: continue
        if rk(Lc + Cc) != r + p: continue
        Z_ = orb(Lc, Ac, n) + orb(Cc, Ac, n); OC = orb(Cc, Ac, n)
        if rk(Z_ + OC) != rk(OC): continue
        Lx, eta = p1(Ac, Cc, Lc)
        if not condA(Ac, Cc, Lx): continue
        q0 = sum(eta)
        dC = n - p; s = dC - r; k = q0 - r
        if k < 1 or k > s: continue
        if 2 * p + q0 >= n: continue
        bt = build_norm_T(Ac, Cc, Lc, Lx)
        if bt is None: continue
        dC2, s2, k2, r2, AT, BAT = bt
        if (r2, k2, s2, dC2) != (r, k, s, dC): continue
        got = (AT, BAT, n, p, r, k, s, dC); break
    if got is None:
        continue
    AT, BAT, n, p, r, k, s, dC = got
    B2 = [[BAT[i][r + j] for j in range(s)] for i in range(p)]
    B21 = [[B2[i][j] for j in range(k)] for i in range(p)]
    B22 = [[B2[i][k + j] for j in range(s - k)] for i in range(p)]
    Kmat = [[B21[i][a] for a in range(k)] + [-B22[i][b] for b in range(s - k)]
            for i in range(p)]
    Kcols = sub_basis_cols(Kmat)
    agree = tot = a_hit = b_hit = 0
    for pt in range(21):
        t = [F(0)] * (k * (s - k)) if pt == 0 else \
            [F(rng.randint(-97, 97), rng.randint(1, 89)) * (1 if rng.random() < 0.5 else -1)
             for _ in range(k * (s - k))]
        # (a)
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
        ra = (rk(WJ + BAT + mm(WJ, AT)) == rk(WJ + BAT))
        # (b)
        Th = [[t[i * (s - k) + j] for j in range(s - k)] for i in range(k)]
        Gcols = []
        for j in range(s - k):
            vec = [Th[i][j] for i in range(k)] + [F(1) if a == j else F(0) for a in range(s - k)]
            Gcols.append(vec)
        Gcols = [[Gcols[j][i] for j in range(s - k)] for i in range(s)]   # s × (s-k)
        NJ = mm(WJ, AT)
        G1 = [[NJ[i][r + a] for a in range(k)] for i in range(r + k)]
        G2 = [[NJ[i][r + k + b] for b in range(s - k)] for i in range(r + k)]
        Kpmat = [[G1[i][a] for a in range(k)] + [-G2[i][b] for b in range(s - k)]
                 for i in range(r + k)]
        Kp = sub_basis_cols(Kpmat)
        inter = intersect(Gcols, Kcols, s)
        if not inter:
            rb = True
        else:
            dKp = len(Kp[0]) if Kp and Kp[0] else 0
            rb = all(rk([[Kp[i][a] for a in range(dKp)] for i in range(s)] + [[v[i] for i in range(s)]])
                     == dKp for v in inter)
        tot += 1
        if ra == rb: agree += 1
        a_hit += ra; b_hit += rb
    insts += 1
    print(f"{n:>2} {p:>2} {r:>2} {k+r:>3} {k:>2} {s:>2} | "
          f"{agree:>3}/{tot:<4} {a_hit:>4}/{tot:<3} {b_hit:>4}/{tot:<3}")
