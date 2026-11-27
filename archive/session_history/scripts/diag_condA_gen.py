# -*- coding: utf-8 -*-
"""最小诊断：生成器实例为何 condA(Lx) 为 False？"""
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


rng = random.Random(777)
shown = 0
for t in range(4000):
    if shown >= 4: break
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
    except Exception as e:
        print("p1 抛错:", e); continue
    shown += 1
    ok = condA(Ac, Cc, Lx)
    # 原始 4 块的两个秩
    LA = mm(Lx, Ac); CA = mm(Cc, Ac)
    r_lhs = rk(LA + Lx + CA + Cc)
    r_rhs = rk(Lx + CA + Cc)
    print(f"--- 实例 {shown} (m={m}, n={n}) ---")
    print(f"  η = {eta}   q0 = {sum(eta)}   Lx 行数 = {len(Lx)}")
    print(f"  condA(Lx) = {ok}")
    print(f"  rank[LA;L;C;CA] = {r_lhs},  rank[L;C;CA] = {r_rhs}   (差 = {r_lhs - r_rhs})")
    print(f"  C 的秩={rk(Cc)}, [C;CA] 的秩={rk(Cc+CA)}, n={n}, p={p}, r={r}")
    # L0 是否满足 (A)（单用 L0 时）
    ok0 = condA(Ac, Cc, Lc)
    print(f"  condA(L0) = {ok0}")
