# -*- coding: utf-8 -*-
"""
验证 T10：若 rank[L0; C; CA] = n，则对**任何**含 L0 的 L，都有 rank(L·N_CA) = q0
        ⟹ 由 T6，(S) 必失败 ⟹ 情形 II 下判定恒为 NO（多项式可判）

与对照：若 rank[L0; C; CA] < n，则**存在** L 使 rank(L·N_CA) < q0（取 R 避开该方向）
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


rng = random.Random(11224488)
print("验证 T10：rank[L0;C;CA]=n  ⟹  任何含 L0 的 L 都有 rank(L·N_CA)=q0")
print()
print(f"{'#':>2} {'n':>2} {'q0':>3} {'d_CA':>4} {'rk[L0;C;CA]':>11} | "
      f"{'样本 L 数':>8} {'秩降个数':>8} {'预期':>18} {'符合?':>6}")
print("-" * 84)
shown = 0
bad = 0
for t in range(40000):
    if shown >= 8:
        break
    n, p, r = 5, 1, 1
    Amat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
    Cmat = [[rng.randint(-2, 2) for _ in range(n)]]
    Ac, Cc = toF(Amat), toF(Cmat)
    if rk(Cc) != p: continue
    Lc = mm(Cc, matpow(Ac, 2))
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
    CA = mm(Cc, Ac)
    W = Cc + CA
    NCA = ker_basis(W)
    dCA = len(NCA[0])
    rkL0W = rk(Lc + W)              # rank[L0; C; CA]
    # 随机造含 L0 的 q0 行 L（**不做** (A) 筛选——T10 对任意 L 都应有结论）
    nlt = 0; tot = 0
    for _ in range(80):
        rows = Lc[:]
        for _i in range(k):
            rows.append([F(rng.randint(-3, 3)) for _ in range(n)])
        L = rows
        H = mm(L, NCA)
        rH = rk(H) if (H and H[0]) else 0
        tot += 1
        if rH < q0:
            nlt += 1
    shown += 1
    expect_zero = (rkL0W == n)
    ok = ((nlt == 0) == expect_zero)
    if not ok:
        bad += 1
    print(f"{shown:>2} {n:>2} {q0:>3} {dCA:>4} {rkL0W:>11} | "
          f"{tot:>8} {nlt:>8} "
          f"{('应=0' if expect_zero else '应>0'):>18} {str(ok):>6}")

print()
print(f"=== 不符合数：{bad} / {shown} ===")
print()
print("判读：")
print("  · 全部符合 ⟹ T10 成立：rank[L0;C;CA]=n 时秩降不可能 ⟹ (S) 必失败 ⟹ 判定恒 NO")
print("  · 出现不符合 ⟹ T10 有误，需撤回")
