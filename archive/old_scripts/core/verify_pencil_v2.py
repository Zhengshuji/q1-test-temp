# -*- coding: utf-8 -*-
"""
从头重做并严格验证铅笔既约形式。

推导： γ ∈ span{Y_J(Θ), B_2}  （Y_J = [I_k | Θ]）
  <=> ∃z,w: γ = z Y_J + w B_2
  <=> γ1 = z + w B21,  γ2 = zΘ + w B22      (γ = (γ1,γ2))
  <=> γ1 Θ - γ2 = w (B21 Θ - B22)  =: w P(Θ)
  <=> q(Θ) := γ1 Θ - γ2  ∈  row P(Θ)

所以 (A) <=> 对所有 i: q_i(Θ) ∈ row P(Θ)。

本脚本对照：
  (a) 三块既约形式   rank[W;B;W Abar_T] == rank[W;B]
  (d) 正确的铅笔条件  ∀i: q_i ∈ row P
若二者逐点一致 => 铅笔形式成立。
"""
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\exact_count_thm7.py",
           encoding="utf-8").read()
exec(src.split("rng = random.Random(112233)")[0])


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


def cond_a(t, r, k, s, dC, AT, BAT):
    WJ = WJ_of(t, r, k, s, dC)
    MB = WJ + BAT
    MX = WJ + BAT + mm(WJ, AT)
    return rk(MB) == rk(MX)


def cond_d(t, r, k, s, dC, AT, BAT):
    p = len(BAT)
    WJ = WJ_of(t, r, k, s, dC)
    NJ = mm(WJ, AT)                                   # (r+k) × dC
    # 商空间坐标 r..r+s-1
    B2 = [[BAT[i][r + j] for j in range(s)] for i in range(p)]
    B21 = [[B2[i][j] for j in range(k)] for i in range(p)]          # p × k
    B22 = [[B2[i][k + j] for j in range(s - k)] for i in range(p)]  # p × (s-k)
    Th = [[t[i * (s - k) + j] for j in range(s - k)] for i in range(k)]
    # P(Θ) = B21 Θ - B22
    P = [[sum(B21[i][a] * Th[a][j] for a in range(k)) - B22[i][j]
          for j in range(s - k)] for i in range(p)]
    for i in range(r + k):
        g1 = [NJ[i][r + j] for j in range(k)]              # 1×k
        g2 = [NJ[i][r + k + j] for j in range(s - k)]      # 1×(s-k)
        q = [sum(g1[a] * Th[a][j] for a in range(k)) - g2[j] for j in range(s - k)]
        if s - k == 0:
            continue
        if rk(P + [q]) != rk(P):
            return False
    return True


rng = random.Random(20240607)
print("严格验证铅笔形式 (a) <=> (d)")
print(f"{'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'k':>2} {'s':>2} | {'一致':>8} {'(a)命中':>8} {'(d)命中':>8}")
print("-" * 62)
insts = 0
for trial in range(4000):
    if insts >= 8:
        break
    n = rng.randint(4, 6)
    p = rng.randint(1, n - 2)
    r = rng.randint(1, n - p - 1)
    got = None
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
        q0 = sum(eta)
        dC = n - p; s = dC - r; k = q0 - r
        if k < 1 or k > s or k * (s - k) > 3: continue
        if 2 * p + q0 >= n: continue          # 只要 <n 情形！
        bt = build_norm_T(Ac, Cc, Lc, Lx)
        if bt is None: continue
        dC2, s2, k2, r2, AT, BAT = bt
        if (r2, k2, s2, dC2) != (r, k, s, dC): continue
        got = (AT, BAT, q0, n, p, r, k, s, dC); break
    if got is None:
        continue
    AT, BAT, q0, n, p, r, k, s, dC = got
    agree = tot = a_hit = d_hit = 0
    for _p in range(31):
        if _p == 0:
            t = [F(0)] * (k * (s - k))          # 关键非平凡点：P1 解
        else:
            t = [F(rng.randint(-97, 97), rng.randint(1, 89)) * (1 if rng.random() < 0.5 else -1)
                 for _ in range(k * (s - k))]
        ra = cond_a(t, r, k, s, dC, AT, BAT)
        rd = cond_d(t, r, k, s, dC, AT, BAT)
        tot += 1
        if ra == rd: agree += 1
        a_hit += ra; d_hit += rd
    insts += 1
    print(f"{n:>2} {p:>2} {r:>2} {q0:>3} {k:>2} {s:>2} | "
          f"{agree:>3}/{tot:<4} {a_hit:>4}/{tot:<3} {d_hit:>4}/{tot:<3}")
