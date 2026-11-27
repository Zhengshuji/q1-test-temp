# -*- coding: utf-8 -*-
"""
生成器验证：取 L0 = C·A^m 是否能稳定造出 k >= 2（即 η1 >= 3）的实例？

理由：
  · H4（功能可观性）自动满足：L0 A^k = C A^{m+k} ∈ row(O_C)
  · H3 一般满足：m ≥ 1 时 C A^m ∉ span(C)
  · η1 由 m 控制 ⟹ 可控

本脚本先验证 η 分布；命中后（k≥2 且 d_CA ≥ q0）再做 conic 检验。
"""
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\reliable_S_test.py",
           encoding="utf-8").read()
head = src.split("# ---------- 主实验 ----------")[0]
exec(head)

MPOW = None


def matpow(M, k):
    n = len(M)
    R = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = mm(R, M)
    return R


rng = random.Random(51505150)
print("生成器验证：L0 = C·A^m 的 η 分布（n=6, p=1, r=1）")
print()
print(f"{'m':>2} {'尝试':>6} {'H1-4 通过':>9} {'η=1':>6} {'η=2':>6} {'η=3':>6} "
      f"{'η>=3 命中':>9} {'q0=η':>6} {'k=η-1':>6}")
print("-" * 74)
for m in (2, 3, 4, 5):
    tries = passed = 0
    hist = {}
    hits = 0
    for t in range(1500):
        tries += 1
        n, p, r = 5, 1, 1
        Amat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
        Cmat = [[rng.randint(-2, 2) for _ in range(n)]]
        Ac, Cc = toF(Amat), toF(Cmat)
        if rk(Cc) != p: continue
        Lc = mm(Cc, matpow(Ac, m))              # L0 = C A^m
        if rk(Lc) != r: continue
        if rk(Lc + Cc) != r + p: continue       # H3
        Z = orb(Lc, Ac, n) + orb(Cc, Ac, n); OC = orb(Cc, Ac, n)
        if rk(Z + OC) != rk(OC): continue       # H4
        try:
            Lx, eta = p1(Ac, Cc, Lc)
        except Exception:
            continue
        passed += 1
        e1 = eta[0]
        hist[e1] = hist.get(e1, 0) + 1
        if e1 >= 3: hits += 1
    print(f"{m:>2} {tries:>6} {passed:>9} "
          f"{hist.get(1,0):>6} {hist.get(2,0):>6} {hist.get(3,0):>6} "
          f"{hits:>9} {hist.get(3,0)+hist.get(4,0)+hist.get(5,0):>6} "
          f"{'>=2' if hits else '-':>6}")

print()
print("判读：")
print("  · 若某个 m 能稳定产生 η>=3 ⟹ 生成器可用 ⟹ 可造出 k>=2 的实例做 conic 检验")
print("  · 若全部 η=1 ⟹ L0=C A^m 的猜测错误，需另寻构造")
