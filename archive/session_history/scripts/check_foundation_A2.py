# -*- coding: utf-8 -*-
"""
A2 —— 地基检查：P1 的三块约化是否真的等价于原始 4 块 (A)？

  原始 4 块：  (A)_raw:  rank[LA; L; CA; C] == rank[L; CA; C]
  三块约化：   (A)_red:  rank[W_J;B;W_J Abar_T] == rank[W_J;B]

其中 L 由参数化重建： L = W_J(Theta) · T^{-1} · M_C   （K 自由度对 (A) 无影响，取 K=0）

对每个 (实例, Theta) 同时算两个判据并比较。
**必须包含 True 与 False 两类点**（否则"一致"是平凡的）。
"""
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\test_S0_conjecture.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random(778899)")[0]
exec(head)


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


def rawA(Ac, Cc, L):
    """原始 4 块 (A)"""
    LA = mm(L, Ac); CA = mm(Cc, Ac)
    lhs = LA + L + CA + Cc
    rhs = L + CA + Cc
    return rk(lhs) == rk(rhs)


def redA(t, D):
    """三块约化"""
    WJ = WJ_of(t, D['r'], D['k'], D['s'], D['dC'])
    MB = WJ + D['BAT']
    MX = WJ + D['BAT'] + mm(WJ, D['AT'])
    return rk(MB) == rk(MX)


rng = random.Random(20250101)
print("A2 地基检查：三块约化 (A)_red  vs  原始 4 块 (A)_raw")
print()
print(f"{'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'k':>2} {'s':>2} {'dimT':>4} | "
      f"{'一致':>9} {'_raw True':>10} {'_red True':>10}")
print("-" * 74)
tot_ag = tot = 0
T_true = T_false = 0
n_inst = 0
for trial in range(40000):
    if n_inst >= 12:
        break
    n = rng.randint(3, 6)
    p = rng.randint(1, n - 1)
    r = rng.randint(1, n - p)
    for _ in range(60):
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
        if k < 1 or k > s or k * (s - k) > 3: continue
        D = get_data(Ac, Cc, Lc, Lx)
        if D is None: continue
        dim = k * (s - k)
        # 采样 Theta：含 0（P1 解，True 点）与一般有理点（多半 False）
        pts = [[F(0)] * dim]
        for _ in range(25):
            pts.append([F(rng.randint(-97, 97), rng.randint(1, 89)) *
                        (1 if rng.random() < 0.5 else -1) for _ in range(dim)])
        ag = 0; tt = 0; tr = 0; fr = 0; frr = 0
        for t in pts:
            WJ = WJ_of(t, r, k, s, dC)
            Lco = mm(mm(WJ, D['Ti']), D['MC'])          # L = W_J T^{-1} M_C
            a_raw = rawA(Ac, Cc, Lco)
            a_red = redA(t, D)
            tt += 1
            tr += a_raw; fr += a_red
            if a_raw == a_red: ag += 1
        n_inst += 1
        tot_ag += ag; tot += tt
        T_true += tr; T_false += fr
        print(f"{n:>2} {p:>2} {r:>2} {q0:>3} {k:>2} {s:>2} {dim:>4} | "
              f"{ag:>4}/{tt:<4} {tr:>5}/{tt:<4} {fr:>5}/{tt:<4}")

print()
print(f"=== 汇总 ===")
print(f"  逐点一致：{tot_ag}/{tot}")
print(f"  (A)_raw 为 True 的点数：{T_true}")
print(f"  (A)_red 为 True 的点数：{T_false}")
print()
print("判读：")
print("  · 若一致 = tot 且 True 点数 > 0（含 False 点）⟹ 三块约化等价于原始 4 块 ✓ 地基稳固")
print("  · 若 True 点数 = 0 ⟹ 全是 False 点，一致性平凡，需另找 True 点")
