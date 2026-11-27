# -*- coding: utf-8 -*-
"""
修正后重算 rank(R·N_C·K)（真正的矩阵乘法：mm(RNC, K)）

同时对照两个判据：
   判据 A： rk(RNC · K) < k              （K 是 d_C × m_K）
   判据 B： ∃0≠y : y^T(RNC) ∈ row(L0NC)   （线性方程组）
若两者一致 ⟹ 线性刻画成立 ✓（第 13 处就此解决）
"""
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\exact_count_thm7.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random")[0]
exec(head)


def matpow(M, k):
    n = len(M)
    R = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = mm(R, M)
    return R


def crit_B(RNC, L0NC):
    m1 = len(RNC); m2 = len(L0NC); d = len(RNC[0])
    nv = m1 + m2
    rows = []
    for j in range(d):
        r = [F(0)] * nv
        for i in range(m1):
            r[i] = RNC[i][j]
        for i in range(m2):
            r[m1 + i] = -L0NC[i][j]
        rows.append(r)
    sol = solve(rows, [[F(0)] for _ in rows])
    if sol is None:
        return False
    y0, ns = sol
    for v in ns:
        if any(v[i] != 0 for i in range(m1)):
            return True
    return any(y0[i] != 0 for i in range(m1))


rng = random.Random(13572468)
print("修正后重算：rk(RNC·K) vs 线性判据 ∃0≠y: y^T(RNC) ∈ row(L0NC)")
print()
print(f"{'#':>2} {'n':>2} {'r':>2} {'q0':>3} {'k':>2} {'d_C':>4} {'m_K':>4} | "
      f"{'样本':>5} {'A:rk<k':>7} {'B':>5} {'一致?':>6} | {'rk(RNC·K) 取值':>16}")
print("-" * 96)
shown = 0
allagree = True
for t in range(60000):
    if shown >= 8:
        break
    n, p, r, m = 5, 1, 1, 2
    Amat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
    Cmat = [[rng.randint(-2, 2) for _ in range(n)]]
    Ac, Cc = toF(Amat), toF(Cmat)
    if rk(Cc) != p: continue
    Lc = mm(Cc, matpow(Ac, m))
    if rk(Lc) != r: continue
    if rk(Lc + Cc) != r + p: continue
    Z = orb(Lc, Ac, n) + orb(Cc, Ac, n); OC = orb(Cc, Ac, n)
    if rk(Z + OC) != rk(OC): continue
    try:
        Lx, eta = p1(Ac, Cc, Lc)
    except Exception:
        continue
    if not condA(Ac, Cc, Lx): continue
    q0 = sum(eta); k = q0 - r
    if k < 1: continue
    NC = ker_basis(Cc); dC = len(NC[0])
    L0NC = mm(Lc, NC)
    K = ker_basis(L0NC)                      # d_C × m_K
    mK = len(K[0]) if (K and K[0]) else 0
    agree = 0; tot = 0; nA = 0; nB = 0; vals = {}
    for _ in range(60):
        rows = Lc[:]
        for _i in range(k):
            rows.append([F(rng.randint(-3, 3)) for _ in range(n)])
        R = rows[len(Lc):]
        RNC = mm(R, NC)                       # k × d_C
        if mK == 0:
            a = True
            av = 0
        else:
            M2 = mm(RNC, K)                   # ✅ 修正：直接用 K（d_C × m_K）
            av = rk(M2)
            a = (av < k)
        b = crit_B(RNC, L0NC)
        tot += 1
        if a: nA += 1
        if b: nB += 1
        vals[av if mK else 0] = vals.get(av if mK else 0, 0) + 1
        if a == b: agree += 1
        else: allagree = False
    shown += 1
    print(f"{shown:>2} {n:>2} {r:>2} {q0:>3} {k:>2} {dC:>4} {mK:>4} | {tot:>5} "
          f"{nA:>7} {nB:>5} {str(agree == tot):>6} | {str(sorted(vals.items())):>16}")

print()
print(f"=== 结论：{'两判据完全一致 ✓ 线性刻画成立' if allagree else '仍不一致 ✗ 需继续查'} ===")
