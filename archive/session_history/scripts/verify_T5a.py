# -*- coding: utf-8 -*-
"""
独立验证 T5a： rank(L·N_CA) < q0  ⟺  row(L) ∩ row(C,CA) ≠ ∅

两个判据的**独立**实现：
  判据 A（用 N_CA）：  rk(L·N_CA) < q0
  判据 B（修正后）：    ker L ∩ ker[C;CA] ≠ 0   ⟺   rk[L;C;CA] < n
对**随机 L**（含 q0 行、含 L0）逐点比较，必须完全一致。
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


rng = random.Random(8080808)
print("独立验证 T5a：rank(L·N_CA) < q0  ⟺  row(L) ∩ row(C,CA) ≠ ∅")
print()
print(f"{'#':>2} {'n':>2} {'p':>2} {'q0':>3} {'d_CA':>4} | "
      f"{'样本数':>7} {'判据A 秩降数':>12} {'判据B(修正)':>14} {'一致?':>6}")
print("-" * 82)
shown = 0
for t in range(30000):
    if shown >= 6:
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
    CA = mm(Cc, Ac)
    W = Cc + CA
    NCA = ker_basis(W)
    dCA = len(NCA[0])
    rkW = rk(W)
    agree = 0; tot = 0; nA = 0; nB = 0
    for _ in range(120):
        # 随机 L：含 L0，共 q0 行，**故意常取到退化点**（用小整数 + 有时把某行设成 W 的组合）
        rows = Lc[:]
        for _i in range(k):
            if rng.random() < 0.35:
                coef = [F(rng.randint(-3, 3)) for _ in range(rkW)]
                rows.append([sum(coef[j] * W[j][c] for j in range(rkW)) for c in range(n)])
            else:
                rows.append([F(rng.randint(-3, 3)) for _ in range(n)])
        L = rows
        if len(L) != q0: continue
        # 判据 A
        H = mm(L, NCA)
        a = (rk(H) < q0) if (H and H[0]) else (0 < q0)
        # 判据 B：交维数 > 0
        inter = n - rk(L + W)          # ker L ∩ ker[C;CA] 的维数
        b = (inter > 0)
        tot += 1
        if a: nA += 1
        if b: nB += 1
        if a == b: agree += 1
    shown += 1
    print(f"{shown:>2} {n:>2} {p:>2} {q0:>3} {dCA:>4} | {tot:>7} {nA:>12} {nB:>14} "
          f"{str(agree == tot):>6}")

print()
print("判读：")
print("  · 全部『一致 = True』⟹ T5a 得到独立验证 ✓")
print("  · 若不一致 ⟹ T5a 有错，需撤回")
