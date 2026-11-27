# -*- coding: utf-8 -*-
"""
A2 调试：为什么三块约化与原始 4 块不一致？
最小诊断：单实例、Θ=0，打印各量并检验重构是否正确。
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
    LA = mm(L, Ac); CA = mm(Cc, Ac)
    return (rk(LA + L + CA + Cc) == rk(L + CA + Cc),
            rk(LA + L + CA + Cc), rk(L + CA + Cc))


rng = random.Random(20250101)
got = None
for trial in range(4000):
    n, p, r = 5, 1, 1
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
        got = (Ac, Cc, Lc, Lx, eta); break
    if got: break

Ac, Cc, Lc, Lx, eta = got
n, p, r = 5, 1, 1
q0 = sum(eta); dC = n - p; s = dC - r; k = q0 - r
print(f"实例：n={n} p={p} r={r} q0={q0} k={k} s={s} dC={dC}")
print(f"L0 = {[[str(x) for x in row] for row in Lc]}")
print(f"Lx (P1 构造的 [L0;R]) = {[[str(x) for x in row] for row in Lx]}")
print()

D = get_data(Ac, Cc, Lc, Lx)
Ti, MC, AT, BAT = D['Ti'], D['MC'], D['AT'], D['BAT']
NC = ker_basis(Cc)

# 三块约化（Θ=0）
t0 = [F(0)] * (k * (s - k))
WJ = WJ_of(t0, r, k, s, dC)
MB = WJ + BAT
MX = WJ + BAT + mm(WJ, AT)
print(f"三块约化 (A)_red = {rk(MB) == rk(MX)}   (rank MB={rk(MB)}, rank MX={rk(MX)})")

# 重构 L^(0) = W_J T^{-1} M_C
L0c = mm(mm(WJ, Ti), MC)
print(f"\n重构 L^(0) = W_J T^-1 M_C :")
for i, row in enumerate(L0c):
    print(f"   row{i} = {[str(x) for x in row]}")
print(f"   前 r 行是否等于 L0？ {L0c[:r] == Lc}")
diff = [[L0c[i][j] - Lc[i][j] for j in range(n)] for i in range(r)]
print(f"   差 (L0 - L^(0) 前r行) = {[[str(x) for x in row] for row in diff]}")
print(f"   差是否在 row(C) 中？ {rk(Cc + diff) == rk(Cc)}   (rank[ C; diff ]={rk(Cc+diff)}, rank C={rk(Cc)})")

a0 = rawA(Ac, Cc, L0c)
print(f"\n原始 4 块 (A)_raw(L^(0)) = {a0[0]}   rank_lhs={a0[1]}, rank_rhs={a0[2]}")

# 用真正的 [L0; R] 形式重构：前 r 行取 L0，后面取 L^(0) 的后 k 行
Lc2 = Lc[:] + L0c[r:]
a1 = rawA(Ac, Cc, Lc2)
print(f"原始 4 块 (A)_raw([L0; L^(0)后k行]) = {a1[0]}   rank_lhs={a1[1]}, rank_rhs={a1[2]}")

# P1 构造的原解 Lx 本身
a2 = rawA(Ac, Cc, Lx)
print(f"原始 4 块 (A)_raw(P1 构造的 Lx) = {a2[0]}   rank_lhs={a2[1]}, rank_rhs={a2[2]}")

# Lx 与 Lc2 的 reduced 数据是否同一行空间？
WJx = mm(mm(Lx, NC), mm(inv(AT), [[F(1) if a == b else F(0) for b in range(dC)] for a in range(dC)])) if False else None
print(f"\nLx 的行数 = {len(Lx)}, L^(0) 的行数 = {len(L0c)}")
print(f"row(Lx) 与 row(L^(0)) 同维？ rank Lx={rk(Lx)}, rank L^(0)={rk(L0c)}")
print(f"[L0;L^(0)后k行] 与 Lx 的行空间是否相同？ "
      f"{rk(Lc2 + Lx) == rk(Lx) == rk(Lc2)}")
