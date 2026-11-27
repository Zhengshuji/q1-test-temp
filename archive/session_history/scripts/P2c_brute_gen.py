# -*- coding: utf-8 -*-
"""P2'': 决定性核对 —— 对**生成器实例**（eta=[3], q0=3）做暴力枚举验证

若暴力最小行数 = 3 ⟹ eta 未高估
若暴力最小行数 < 3 ⟹ eta 高估，q0 需重算（影响全项目阈值表述）
"""
import itertools
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\exact_count_thm7.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random")[0]
exec(head)


def matpow_(M, k):
    nn = len(M)
    R = [[F(1) if i == j else F(0) for j in range(nn)] for i in range(nn)]
    for _ in range(k):
        R = mm(R, M)
    return R


def satisfies_A(Ac, Cc, V):
    VA = mm(V, Ac); W = V + Cc + mm(Cc, Ac)
    return rk(W + VA) == rk(W)


def brute_min(Ac, Cc, Lc, mmax=5):
    n = len(Ac); r = len(Lc)
    cand = []
    curC = Cc[:]; curL = Lc[:]
    for k in range(n):
        cand += curC + curL
        curC = mm(curC, Ac); curL = mm(curL, Ac)
    uniq = []
    for row in cand:
        if any(x != 0 for x in row) and row not in uniq:
            uniq.append(row)
    N = len(uniq)
    for m in range(0, min(N, mmax) + 1):
        for comb in itertools.combinations(range(N), m):
            V = Lc[:] + [uniq[i] for i in comb]
            if satisfies_A(Ac, Cc, V):
                return r + m, m, N
    return None, None, N


rng = random.Random(97531)
print("P2'': 生成器实例 eta=[3] q0=3 的暴力枚举核对")
print()
print(f"{'tag':>14} | {'r/p/n':>7} | {'eta':>8} {'q0':>3} | {'候选行N':>7} {'暴力最小':>8} {'一致?':>6}")
print("-" * 74)
stats = {}
for t in range(30000):
    if sum(stats.values()) >= 12:
        break
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
    if q0 not in (2, 3): continue
    bmin, bm, N = brute_min(Ac, Cc, Lc)
    key = (q0, bmin)
    stats[key] = stats.get(key, 0) + 1
    print(f"{tag:>14} | {r}/{p}/{n:>1} | {str(eta):>8} {q0:>3} | {N:>7} {str(bmin):>8} "
          f"{str(bmin == q0):>6}")

print()
print("=== 按 (q0, 暴力最小) 分组统计 ===")
for k in sorted(stats):
    print(f"  q0={k[0]}  暴力最小={k[1]}  :  {stats[k]} 个")
print()
print("判读：")
print("  · 所有 q0==暴力最小 ⟹ eta 未高估，q0 可信")
print("  · 出现 暴力最小 < q0 ⟹ eta 高估，q0 需重算")
