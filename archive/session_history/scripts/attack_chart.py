# -*- coding: utf-8 -*-
"""
攻 FINAL §9 第②项：最小 (A)-增广是否必有 rank(R·N_C·K)=k？

对 r=1、候选 2 行增广 L=[L0; w] 的情形：
  (A)  ⟺  row(L_A) ⊆ row(L, C, CA)
       ⟺  (1) L0·A ∈ row(L0, w, C, CA)  且  (2) w·A ∈ row(L0, w, C, CA)

  条件 (2) 展开： w·A = α w + β L0 + γ C + δ CA
              ⟺  w·(A − αI) = β L0 + γ C + δ CA
  当 α 不是 A 的特征值时 (A−αI) 可逆 ⟹ 取 β=1,γ=δ=0 得
              w = L0·(A − αI)^{-1}
  ⟹ 存在**单参数族**的候选 w ✓（把 5 维零测搜索降为 1 维）

本脚本：对每个实例，扫一批有理 α，检查 [L0; w(α)] 是否满足 (A)。
  · 若某个 α 命中 ⟹ 2 行 (A)-增广存在 ⟹ 该实例的最小行数是 2 而非 3
    ⟹ p1 的 η 高估 ⟹ 图卡限定问题变成"η 有 bug"
  · 若所有（足够多的）α 都不命中 ⟹ 支持"3 行确实是最小"
    ⟹ 该实例是**最小增广但 rank(R N_C K) < k** 的真实反例
    ⟹ P1 参数化（Theorem 3）覆盖不全
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


def satisfies_A(Ac, Cc, L):
    """(A): row(L·A) ⊆ row(L, C, CA)"""
    return rk(mm(L, Ac) + L + Cc + mm(Cc, Ac)) == rk(L + Cc + mm(Cc, Ac))


def try_two_rows(Ac, Cc, L0, nalpha=400, seed=1):
    """扫 α，检查 w = L0 (A−αI)^{-1} 是否给出可行的 2 行增广"""
    n = len(Ac)
    rng = random.Random(seed)
    hits = []
    CA = mm(Cc, Ac)
    # 候选 v（**行向量**）在 span(L0, C, CA) 中取一批
    base = [L0[0], Cc[0], CA[0]]
    vs = list(base)
    vs.append([a + b for a, b in zip(L0[0], Cc[0])])
    vs.append([a + b for a, b in zip(L0[0], CA[0])])
    vs.append([a + b for a, b in zip(Cc[0], CA[0])])
    for _q in range(4):
        coef = [F(rng.randint(-6, 6), rng.randint(1, 9)) for _ in range(3)]
        vs.append([sum(coef[j] * base[j][i] for j in range(3)) for i in range(n)])
    for _ in range(nalpha):
        # α 取一般有理数（避开特征值——一般有理数几乎必然不是特征值）
        al = F(rng.randint(-40, 40), rng.randint(1, 20))
        M = [[Ac[i][j] - (al if i == j else F(0)) for j in range(n)] for i in range(n)]
        Mi = inv(M)
        if Mi is None:
            continue
        for v in vs:
            if rk([v]) == 0:
                continue
            w = mm([v], Mi)
            if satisfies_A(Ac, Cc, L0 + w):
                hits.append(al)
                break
        if len(hits) >= 3:
            break
    return hits


rng = random.Random(271828)
print("攻第②项：寻找『最小增广但 rank(R N_C K) < k』的真实反例")
print()
print(f"{'tag':>12} | {'r/p/n':>7} | {'η':>7} {'q0':>3} {'k':>2} | "
      f"{'rank(R N_C K)':>13} {'2行增广命中 α':>14} {'结论':>28}")
print("-" * 104)
shown = 0
for t in range(30000):
    if shown >= 8:
        break
    n, p, r, m = 5, 1, 1, 2
    Amat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
    Cmat = [[rng.randint(-2, 2) for _ in range(n)]]
    Ac, Cc = toF(Amat), toF(Cmat)
    if rk(Cc) != p: continue
    if rng.random() < 0.6:
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
    # rank(R N_C K)
    NC = ker_basis(Cc); dC = len(NC[0])
    R = Lx[len(Lc):]; RNC = mm(R, NC)
    L0NC = mm(Lc, NC)
    K = ker_basis(L0NC); mK = len(K[0]) if (K and K[0]) else 0
    Kr = [[K[a][j] for a in range(dC)] for j in range(mK)]
    rkmat = [[mm(RNC, [[Kr[j][a] for a in range(dC)]])[ii][0] for j in range(mK)]
             for ii in range(k)]
    rr = rk(rkmat)
    hits = try_two_rows(Ac, Cc, Lc, nalpha=500, seed=1000 + t)
    shown += 1
    if hits:
        concl = "2行可行 ⟹ η 高估！"
    else:
        concl = "3行确为最小 ⟹ 图卡外反例"
    print(f"{tag:>12} | {r}/{p}/{n:>1} | {str(eta):>7} {q0:>3} {k:>2} | "
          f"{rr:>13} {str(len(hits)):>14} {concl:>28}")

print()
print("判读：")
print("  · 若出现『2行可行』⟹ p1 的 η 高估，q0 需重算（严重）")
print("  · 若全部『3行确为最小』且 rank(R N_C K) < k ⟹ 存在图卡外的**最小**增广")
print("     ⟹ P1 的 Theorem 3（参数化覆盖所有最小增广）不成立")
print("  · 若 rank(R N_C K) = k ⟹ 该实例在图卡内，无矛盾")
