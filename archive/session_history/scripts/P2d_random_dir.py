# -*- coding: utf-8 -*-
"""P2''': 修正暴力搜索的不完备 —— 加入**随机方向**的额外行

对 q0=2 (r=1) 的实例：随机取 w ∈ Q^n，检验 [L0; w] 是否满足 (A)。
若命中 ⟹ q0=2 可达 ⟹ 与 η=[2] 一致（此前"暴力最小=3"是搜索不完备的假象）。
"""
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\P2c_brute_gen.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random(97531)")[0]
exec(head)


def satisfies_A(Ac, Cc, V):
    VA = mm(V, Ac); W = V + Cc + mm(Cc, Ac)
    return rk(W + VA) == rk(W)


rng = random.Random(86420)
print("P2''': 加入随机方向后，q0=2 是否可达？")
print()
print(f"{'tag':>12} | {'r/p/n':>7} | {'eta':>6} {'q0':>3} | {'随机尝试':>8} {'命中数':>6} {'最小可达':>8}")
print("-" * 70)
tot = 0; hit = 0; best = {}
for t in range(30000):
    if tot >= 8: break
    n, p, r = 5, 1, 1
    Amat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
    Cmat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)]
    Ac, Cc = toF(Amat), toF(Cmat)
    if rk(Cc) != p: continue
    if rng.random() < 0.5:
        Lc = mm(Cc, matpow_(Ac, 2)); tag = "gen C A^2"
    else:
        Lc = toF([[rng.randint(-2, 2) for _ in range(n)] for _ in range(r)]); tag = "random"
    if rk(Lc) != r: continue
    if rk(Lc + Cc) != r + p: continue
    Z = orb(Lc, Ac, n) + orb(Cc, Ac, n); OC = orb(Cc, Ac, n)
    if rk(Z + OC) != rk(OC): continue
    try:
        Lx, eta = p1(Ac, Cc, Lc)
    except Exception:
        continue
    if not condA(Ac, Cc, Lx): continue
    q0 = sum(eta)
    if q0 != 2: continue
    # 若 r+1 = q0，则需一行可行；随机找
    ntry = 300
    nhit = 0
    for _ in range(ntry):
        w = [[F(rng.randint(-97, 97), rng.randint(1, 89)) for _ in range(n)]]
        if satisfies_A(Ac, Cc, Lc + w):
            nhit += 1
            break
    tot += 1
    hit += (1 if nhit else 0)
    print(f"{tag:>12} | {r}/{p}/{n:>1} | {str(eta):>6} {q0:>3} | {ntry:>8} {nhit:>6} "
          f"{('2' if nhit else '?'):>8}")

print()
print(f"=== 汇总 ===  {hit} / {tot} 个实例在随机方向下找到 r+1 = 2 行的可行增广")
print()
print("判读：")
print("  · 命中 ⟹ q0=2 可达 ⟹ 与 η=[2] 一致；此前'暴力最小=3'确系搜索不完备")
print("  · 全不命中 ⟹ 需进一步查（可能是代数条件太薄，随机采样难命中）")
