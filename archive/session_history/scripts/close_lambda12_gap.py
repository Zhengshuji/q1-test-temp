# -*- coding: utf-8 -*-
"""
封闭第②项最后缺口：λ12 = 0 分支是否为空？

λ12 = 0 时，(I) 变为  u(λ11) = π(L0·A) − λ11 π(L0) = 0
该方程有解 ⟺ 存在 λ11 使 π(L0A) = λ11 π(L0) ⟺ **π(L0A) ∥ π(L0)**
   ⟺ rank[π(L0); π(L0A)] = 1（当 π(L0) ≠ 0）

若对全部实例都不平行 ⟹ 该分支为空 ⟹ 第②项**完全封闭**（无残留缺口）
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


rng = random.Random(606061)
print("封闭 λ12=0 分支：判断 π(L0A) 与 π(L0) 是否平行")
print()
print(f"{'#':>2} {'η':>6} {'q0':>3} {'k':>2} {'d_CA':>4} | "
      f"{'rank[π(L0);π(L0A)]':>18} {'平行?':>6} {'λ12=0 分支':>12}")
print("-" * 78)
shown = 0
npar = 0
for t in range(40000):
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
    if k != 2: continue
    W = Cc + mm(Cc, Ac); rkW = rk(W); dCA = n - rkW
    NA = ker_basis(W)
    d = len(NA[0])
    L0 = Lc[0]; L0A = mm(Lc, Ac)[0]
    pL0 = [sum(L0[i] * NA[i][j] for i in range(n)) for j in range(d)]
    pL0A = [sum(L0A[i] * NA[i][j] for i in range(n)) for j in range(d)]
    rr = rk([pL0, pL0A])
    par = (rr == 1)
    if par: npar += 1
    shown += 1
    print(f"{shown:>2} {str(eta):>6} {q0:>3} {k:>2} {dCA:>4} | "
          f"{rr:>18} {str(par):>6} "
          f"{('**非空！需查**' if par else '为空 ✓'):>12}")

print()
print(f"=== 汇总：平行的实例数 = {npar} / {shown} ===")
print()
print("判读：")
print("  · 全部『为空』⟹ λ12=0 分支不存在 ⟹ 第②项的严格结论**无残留缺口** ✓")
print("  · 出现『非空』⟹ 必须单独解该分支的 (II)（那时 π(w) 自由，可能相容）")
