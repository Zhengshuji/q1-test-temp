# -*- coding: utf-8 -*-
"""P2：独立核对 q0 = Ση_j —— 与闭式候选量并排比较

候选量：
  Z  = 含 row(L0)+row(C) 的最小 A-不变空间  ⟹ dim Z = rank(orb(L0)+orb(C))
  候选1: dim Z
  候选2: dim Z − r          （r = rows(L0)）
  候选3: dim Z − dim row(C) = dim Z − p
对照量：q0 = Ση_j（P1 Thm 2，本项目实现的版本）
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


def report(Ac, Cc, Lc, Lx, tag):
    n, p, r = len(Ac), len(Cc), len(Lc)
    eta = None
    try:
        _, eta = p1(Ac, Cc, Lc)
    except Exception:
        pass
    q0 = sum(eta) if eta else None
    Z = orb(Lc, Ac, n) + orb(Cc, Ac, n)
    OC = orb(Cc, Ac, n)
    dZ = rk(Z); dOC = rk(OC)
    print(f"{tag:>22} | r={r} p={p} n={n} | η={eta} q0={q0} | "
          f"dimZ={dZ} dimZ−r={dZ-r} dimZ−p={dZ-p} dimOC={dOC} | "
          f"Lx行数={len(Lx)} condA={condA(Ac, Cc, Lx)}")


rng = random.Random(2468)
print("独立核对：q0 = Ση_j  与  A-不变空间维数 的关系")
print()
print(f"{'类型':>22} | {'r/p/n':>9} | {'η / q0':>12} | "
      f"{'dimZ':>6} {'dimZ-r':>7} {'dimZ-p':>7} {'dimOC':>6} | {'Lx行数':>6} {'condA':>6}")
print("-" * 118)

# 生成器实例 L0 = C A^m
cnt = 0
for t in range(4000):
    if cnt >= 4: break
    n, p, r, m = 5, 1, 1, 2
    Amat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
    Cmat = [[rng.randint(-2, 2) for _ in range(n)]]
    Ac, Cc = toF(Amat), toF(Cmat)
    if rk(Cc) != p: continue
    Lc = mm(Cc, matpow(Ac, m))
    if rk(Lc) != r: continue
    if rk(Lc + Cc) != r + p: continue
    Z0 = orb(Lc, Ac, n) + orb(Cc, Ac, n); OC0 = orb(Cc, Ac, n)
    if rk(Z0 + OC0) != rk(OC0): continue
    try:
        Lx, eta = p1(Ac, Cc, Lc)
    except Exception:
        continue
    if not condA(Ac, Cc, Lx): continue
    if len(Lx) - len(Lc) != 2: continue
    cnt += 1
    report(Ac, Cc, Lc, Lx, f"生成器#{cnt}(L0=C A^2)")

# 随机构造（作为对照，含 k=1 与 k=2）
cnt = 0
for t in range(6000):
    if cnt >= 4: break
    n = rng.randint(4, 6); p = rng.randint(1, n - 1); r = rng.randint(1, n - p)
    Amat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
    Cmat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)]
    Lmat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(r)]
    Ac, Cc, Lc = toF(Amat), toF(Cmat), toF(Lmat)
    if rk(Cc) != p or rk(Lc) != r: continue
    if rk(Lc + Cc) != r + p: continue
    Z0 = orb(Lc, Ac, n) + orb(Cc, Ac, n); OC0 = orb(Cc, Ac, n)
    if rk(Z0 + OC0) != rk(OC0): continue
    try:
        Lx, eta = p1(Ac, Cc, Lc)
    except Exception:
        continue
    if not condA(Ac, Cc, Lx): continue
    cnt += 1
    report(Ac, Cc, Lc, Lx, f"随机#{cnt}")

print()
print("判读：")
print("  · 若 q0 恒等于 dimZ（或 dimZ−r 等固定候选）⟹ q0 有独立公式支撑，η 未高估")
print("  · 若生成器实例的 q0=3 但 dimZ 明显不是 3 ⟹ η 与实际最小行数不符，需查 p1")
