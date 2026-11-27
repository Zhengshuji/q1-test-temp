# -*- coding: utf-8 -*-
"""
第②项收尾（强化版）：稠密有理网格扫 λ11，判定 (I)∧(II) 是否有**任何**相容点

对每个 λ11：
    (I)   π(L0A − λ11 L0) = λ12 π(w)      （取 λ12 = 1，WLOG——见下）
    (II)  π(wA − λ21 L0 − λ22 w) = 0
WLOG 说明：若 λ12 ≠ 0，令 w→w/λ12、λ21→λ21/λ12 即归为 λ12=1；
          u = π(L0A)−λ11 π(L0) = 0 时另处理（π(w) 任取）。

输出：相容的 λ11 个数（若为 0 ⟹ 强烈支持「不存在 2 行 (A)-增广」）
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


def consistent_at(Ac, Cc, Lc, l11, extra_pw=None):
    """给定 λ11，判 (I)∧(II) 是否相容；返回可行 w 或 None"""
    n = len(Ac)
    L0 = Lc[0]
    L0A = mm(Lc, Ac)[0]
    CA = mm(Cc, Ac)
    W = Cc + CA
    NA = ker_basis(W)
    d = len(NA[0])
    rkW = rk(W)

    def pv(v):
        return [sum(v[i] * NA[i][j] for i in range(n)) for j in range(d)]

    u = [pv(L0A)[j] - l11 * pv(L0)[j] for j in range(d)]
    if all(x == 0 for x in u):
        cands = [[F(0)] * d]
        if extra_pw is not None:
            cands.append(extra_pw)
    else:
        cands = [u[:]]
    ANA = mm(Ac, NA)
    pL0 = pv(L0)
    for pw in cands:
        rows, rhs = [], []
        for j in range(d):                                  # (I)
            rows.append([NA[i][j] for i in range(n)] + [F(0), F(0)])
            rhs.append([pw[j]])
        for j in range(d):                                  # (II)
            r = [ANA[i][j] for i in range(n)] + [F(0), F(0)]
            r[n] = -pL0[j]
            r[n + 1] = -pw[j]
            rows.append(r); rhs.append([F(0)])
        sol = solve(rows, rhs)
        if sol is None:
            continue
        x = sol[0]
        w = [x[i] for i in range(n)]
        # 精确复核
        if rk(mm(Lc + [w], Ac) + Lc + [w] + W) == rk(Lc + [w] + W):
            return w
    return None


rng = random.Random(31415)
print("第②项收尾：稠密有理网格扫 λ11")
print()
print(f"{'#':>2} {'η':>6} {'q0':>3} {'k':>2} | {'rank(RN_C K)':>12} | "
      f"{'扫过的 λ11 数':>13} {'相容数':>7} {'结论':>26}")
print("-" * 92)
shown = 0
for t in range(40000):
    if shown >= 5:
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
    NC = ker_basis(Cc); dC = len(NC[0])
    R = Lx[len(Lc):]; RNC = mm(R, NC)
    L0NC = mm(Lc, NC)
    K = ker_basis(L0NC); mK = len(K[0]) if (K and K[0]) else 0
    Kr = [[K[a][j] for a in range(dC)] for j in range(mK)]
    rkmat = [[mm(RNC, [[Kr[j][a] for a in range(dC)]])[ii][0] for j in range(mK)]
             for ii in range(k)]
    rr = rk(rkmat)
    # 稠密网格：p/q, |p|<=24, 1<=q<=12  ⟹ 约 1200 个
    lams = []
    for q in range(1, 13):
        for pnum in range(-24, 25):
            lams.append(F(pnum, q))
    good = 0
    for l11 in lams:
        if consistent_at(Ac, Cc, Lc, l11) is not None:
            good += 1
            break
    shown += 1
    concl = "**找到可行 2 行增广**" if good else "网格内全不相容"
    print(f"{shown:>2} {str(eta):>6} {q0:>3} {k:>2} | {rr:>12} | "
          f"{len(lams):>13} {good:>7} {concl:>26}")

print()
print("判读：")
print("  · 有相容点 ⟹ 2 行 (A)-增广存在 ⟹ p1 的 η 高估")
print("  · 全部不相容 ⟹ 强烈支持『这类实例是图卡外的最小增广』")
print("    （若相容性条件关于 λ 是多项式的，有解时通常存在小分母有理点）")
