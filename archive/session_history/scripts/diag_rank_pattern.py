# -*- coding: utf-8 -*-
"""
第②项严格化：判定 (I)∧(II) 是否有**严格**的依据说明"恒不相容"

系统： 7 个未知量 (w∈Q^5, λ21, λ22)，6 个方程  ⟹ 若 rank M(λ)=6 则**必相容**
故：
   (a) 若 ∃λ: rank M(λ)=6  ⟹ 相容 ⟹ 2 行增广存在（η 高估）
   (b) 若 ∀λ: rank M(λ)≤5 ⟹ 仍需看 [M|b] 的相容性

本脚本：对若干 λ 精确求 rank M(λ) 与 rank[M(λ)|b(λ)]，并**统计**
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


def build_system(Ac, Cc, Lc, l11):
    n = len(Ac)
    L0 = Lc[0]
    L0A = mm(Lc, Ac)[0]
    W = Cc + mm(Cc, Ac)
    NA = ker_basis(W)
    d = len(NA[0])

    def pv(v):
        return [sum(v[i] * NA[i][j] for i in range(n)) for j in range(d)]

    u = [pv(L0A)[j] - l11 * pv(L0)[j] for j in range(d)]
    pw = u[:]
    ANA = mm(Ac, NA)
    pL0 = pv(L0)
    rows, rhs = [], []
    for j in range(d):                                   # (I)
        rows.append([NA[i][j] for i in range(n)] + [F(0), F(0)])
        rhs.append([pw[j]])
    for j in range(d):                                   # (II)
        r = [ANA[i][j] for i in range(n)] + [F(0), F(0)]
        r[n] = -pL0[j]
        r[n + 1] = -pw[j]
        rows.append(r); rhs.append([F(0)])
    return rows, rhs


rng = random.Random(99991)
print("第②项严格化：rank M(λ) 与 rank[M|b] 的分布")
print()
print(f"{'#':>2} {'d_CA':>4} {'rkW':>4} | {'rank M 取值':>18} | {'rank[M|b] 取值':>18} | "
      f"{'相容数/样本数':>13}")
print("-" * 84)
shown = 0
for t in range(40000):
    if shown >= 4:
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
    if sum(eta) - r != 2: continue
    W = Cc + mm(Cc, Ac); rkW = rk(W); dCA = n - rkW
    rankM = {}; rankMb = {}; ok = 0; tot = 0
    for q in range(1, 10):
        for pnum in range(-16, 17):
            l11 = F(pnum, q)
            rows, rhs = build_system(Ac, Cc, Lc, l11)
            rM = rk(rows)
            aug = [rows[i] + rhs[i] for i in range(len(rows))]
            rMb = rk(aug)
            rankM[rM] = rankM.get(rM, 0) + 1
            rankMb[rMb] = rankMb.get(rMb, 0) + 1
            tot += 1
            if rM == rMb:
                ok += 1
    shown += 1
    print(f"{shown:>2} {dCA:>4} {rkW:>4} | {str(sorted(rankM.items())):>18} | "
          f"{str(sorted(rankMb.items())):>18} | {ok:>6}/{tot:<6}")

print()
print("判读：")
print("  · 若 rank M 恒 ≤5 且 rank[M|b] 恒 > rank M ⟹ 系统恒不相容")
print("    ⟹ 与前面五条证据合计，『不存在 2 行增广』在采样范围内是确定的")
print("  · 若 rank M 曾达 6 ⟹ 该 λ 必相容 ⟹ 我们漏掉了可行解（需改搜索）")
