# -*- coding: utf-8 -*-
"""
第②项补缺口：α = A 的特征值 的情形

思路：不求精确解，只要**找到一个**可行的 w 即可（用精确有理算术复核 (A)）。
  1. 数值求 A 的特征值 α
  2. 对 span(L0, C, CA) 的一组基向量 v，数值解 w(A−αI) = v
  3. 把 w 取有理近似（多种分母），**精确**检验 [L0; w] 是否满足 (A)
  只要有一次精确通过 ⟹ 2 行 (A)-增广存在 ⟹ η 高估（严重）
"""
import random
from fractions import Fraction as F
import numpy as np

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


def satisfies_A(Ac, Cc, L):
    return rk(mm(L, Ac) + L + Cc + mm(Cc, Ac)) == rk(L + Cc + mm(Cc, Ac))


def to_np(M):
    return np.array([[float(x) for x in row] for row in M])


def search_eigvec(Ac, Cc, L0, nround=6, nv=8, seed=7):
    """在 A 的特征值处找候选 w，精确复核"""
    n = len(Ac)
    A = to_np(Ac); C = to_np(Cc); L = to_np(L0)
    rng = random.Random(seed)
    ev = np.linalg.eigvals(A)
    CA = mm(Cc, Ac)
    base = [L0[0], Cc[0], CA[0]]
    vs = list(base)
    for _ in range(nv):
        coef = [F(rng.randint(-6, 6), rng.randint(1, 9)) for _ in range(3)]
        vs.append([sum(coef[j] * base[j][i] for j in range(3)) for i in range(n)])
    hits = []
    for al in ev:
        if abs(al.imag) > 1e-9:
            continue
        al = al.real
        M = A - al * np.eye(n)
        for v in vs:
            vn = np.array([float(x) for x in v])
            # 最小二乘解 w M = vn  （行向量）
            try:
                w, *_ = np.linalg.lstsq(M.T, vn, rcond=None)
            except Exception:
                continue
            for den in (10, 100, 1000, 10 ** 4, 10 ** 5, 10 ** 6):
                wr = [F(float(np.real(x))).limit_denominator(den) for x in w]
                if satisfies_A(Ac, Cc, L0 + [wr]):
                    hits.append((al, den, wr))
                    return hits
    return hits


rng = random.Random(1234321)
print("第②项补缺口：在 A 的特征值处搜索 2 行 (A)-增广")
print()
print(f"{'#':>2} {'tag':>11} | {'η':>6} {'q0':>3} {'k':>2} | {'rank(RN_C K)':>12} | "
      f"{'特征值处命中':>12} {'结论':>30}")
print("-" * 96)
shown = 0
for t in range(30000):
    if shown >= 8:
        break
    n, p, r, m = 5, 1, 1, 2
    Amat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
    Cmat = [[rng.randint(-2, 2) for _ in range(n)]]
    Ac, Cc = toF(Amat), toF(Cmat)
    if rk(Cc) != p: continue
    if rng.random() < 0.7:
        Lc = mm(Cc, matpow(Ac, m)); tag = "gen C A^2"
    else:
        Lc = toF([[rng.randint(-2, 2) for _ in range(n)]]); tag = "random"
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
    hits = search_eigvec(Ac, Cc, Lc, seed=100 + t)
    shown += 1
    concl = "**2行可行 ⟹ η 高估！**" if hits else "特征值处也无 ⟹ 最小=3"
    print(f"{shown:>2} {tag:>11} | {str(eta):>6} {q0:>3} {k:>2} | {rr:>12} | "
          f"{str(len(hits)):>12} {concl:>30}")

print()
print("判读：")
print("  · 任一实例出现『2行可行』⟹ p1 的 η 高估，q0 需重算")
print("  · 全部『最小=3』且 rank(RN_C K)<k ⟹ 与『非特征值 α 全不命中』合计")
print("    ⟹ 生成器实例是**图卡外的最小增广** ⟹ P1 Theorem 3 不完整（结论成立）")
