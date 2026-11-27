# -*- coding: utf-8 -*-
"""
B-ii 第一步：对反例实例，随机搜索所有满足 (A) 的行空间 V，
看 rank(R·N_C·K) 能否达到 k（即 V 是否落在 P1 图卡内）

若能达到 ⟹ 图卡内的最小增广存在 ⟹ Θ 框架仍可用
若始终 <k ⟹ 该实例本质上是图卡外的
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


def rho_of(Ac, Cc, L):
    """rank(R·N_C·K)"""
    n = len(Ac)
    NC = ker_basis(Cc); dC = len(NC[0])
    r = len(L) - (len(L) - 1)                     # 占位
    # 这里需要知道 r（L0 的行数）：由调用方传入更稳 —— 用参数外传
    return None


rng = random.Random(778899)
print("B-ii：反例实例中，是否存在**图卡内**的 (A)-可行行空间？")
print()
print(f"{'#':>2} {'n':>2} {'r':>2} {'q0':>3} {'k':>2} | {'采样':>6} {'(A) 命中':>8} "
      f"{'rank(RN_CK) 取值':>16} {'最大':>5} {'图卡内存在?':>12}")
print("-" * 88)
shown = 0
chart_in_found = 0
for t in range(60000):
    if shown >= 6:
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
    if k != 2: continue
    W = Cc + mm(Cc, Ac)
    NC = ker_basis(Cc); dC = len(NC[0])
    L0NC = mm(Lc, NC)
    K = ker_basis(L0NC); mK = len(K[0]) if (K and K[0]) else 0
    Kr = [[K[a][j] for a in range(dC)] for j in range(mK)]

    def rho(L):
        R = L[len(Lc):]
        RNC = mm(R, NC)
        rkmat = [[mm(RNC, [[Kr[j][a] for a in range(dC)]])[ii][0] for j in range(mK)]
                 for ii in range(k)]
        return rk(rkmat) if rkmat and rkmat[0] else 0

    vals = {}
    nA = 0
    tot = 0
    for _ in range(400):
        rows = Lc[:]
        for _i in range(k):
            rows.append([F(rng.randint(-4, 4), rng.randint(1, 3)) for _ in range(n)])
        L = rows
        tot += 1
        if rk(mm(L, Ac) + L + W) != rk(L + W):     # 不含 (A)
            continue
        nA += 1
        v = rho(L)
        vals[v] = vals.get(v, 0) + 1
    shown += 1
    mx = max(vals) if vals else None
    ok = (mx == k)
    if ok: chart_in_found += 1
    print(f"{shown:>2} {n:>2} {r:>2} {q0:>3} {k:>2} | {tot:>6} {nA:>8} "
          f"{str(sorted(vals.items())):>16} {str(mx):>5} {str(ok):>12}")

print()
print(f"=== 图卡内 (A)-可行点存在的实例数：{chart_in_found} / {shown} ===")
print()
print("判读：")
print("  · 存在（最大 = k）⟹ 图卡内的最小增广存在 ⟹ Θ 框架仍适用 ⟹ 重大缓解")
print("  · 全部 < k ⟹ 该实例本质上是图卡外的 ⟹ 必须先完成 B")
