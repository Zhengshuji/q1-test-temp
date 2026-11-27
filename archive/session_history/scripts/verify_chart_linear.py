# -*- coding: utf-8 -*-
"""
验证图卡条件的线性刻画：
    rank(R·N_C·K) < k  ⟺  ∃ 0≠y ∈ Q^k : y^T·(R·N_C) ∈ row(L0·N_C)

两个独立判据：
   判据 A： rk(R·N_C·K) < k
   判据 B： ∃0≠y : y^T(R N_C) ∈ row(L0 N_C)   （线性方程组是否有非零解）
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


def crit_B(RNC, L0NC):
    """
    ∃ 0≠y : y^T(RNC) ∈ row(L0NC)?
    y^T(RNC) ∈ row(L0NC) ⟺ ∃z: y^T(RNC) = z^T(L0NC)
    ⟺ (y,z) 满足 RNC^T y − L0NC^T z = 0，且 y ≠ 0
    ⟺ 解空间在 y-坐标上的投影非零
    实现：解齐次系统 M·[y;z]=0，检查是否存在解的 y 部分非零。
    """
    m1 = len(RNC)                       # k
    m2 = len(L0NC)                      # r
    d = len(RNC[0])
    nv = m1 + m2
    rows = []
    for j in range(d):                  # 第 j 个坐标
        r = [F(0)] * nv
        for i in range(m1):
            r[i] = RNC[i][j]            # y^T RNC 的系数
        for i in range(m2):
            r[m1 + i] = -L0NC[i][j]
        rows.append(r)
    if not rows:
        return True
    sol = solve(rows, [[F(0)] for _ in rows])
    if sol is None:
        return False                     # 只有零解（但齐次系统总有零解）
    y0, ns = sol
    # 检查零解之外：ns 里是否有 y 部分非零的向量
    for v in ns:
        if any(v[i] != 0 for i in range(m1)):
            return True
    # 特解 y 部分非零也算
    if any(y0[i] != 0 for i in range(m1)):
        return True
    return False


rng = random.Random(2468013579)
print("验证：rank(R·N_C·K) < k  ⟺  ∃0≠y: y^T(R N_C) ∈ row(L0 N_C)")
print()
print(f"{'#':>2} {'n':>2} {'r':>2} {'q0':>3} {'k':>2} {'d_C':>4} | {'样本':>5} "
      f"{'判据A<k':>8} {'判据B':>6} {'一致?':>6}")
print("-" * 66)
shown = 0
for t in range(60000):
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
    if k < 1: continue
    NC = ker_basis(Cc); dC = len(NC[0])
    L0NC = mm(Lc, NC)
    K = ker_basis(L0NC); mK = len(K[0]) if (K and K[0]) else 0
    W = Cc + mm(Cc, Ac)
    agree = 0; tot = 0; nA = 0; nB = 0
    for _ in range(60):
        rows = Lc[:]
        for _i in range(k):
            rows.append([F(rng.randint(-3, 3)) for _ in range(n)])
        L = rows
        R = L[len(Lc):]
        RNC = mm(R, NC)
        # 判据 A
        if mK == 0:
            a = False
        else:
            Kr = [[K[a_][j] for a_ in range(dC)] for j in range(mK)]
            rkmat = [[mm(RNC, [[Kr[j][a_] for a_ in range(dC)]])[ii][0] for j in range(mK)]
                     for ii in range(k)]
            a = (rk(rkmat) < k)
        # 判据 B
        b = crit_B(RNC, L0NC)
        tot += 1
        if a: nA += 1
        if b: nB += 1
        if a == b: agree += 1
    shown += 1
    print(f"{shown:>2} {n:>2} {r:>2} {q0:>3} {k:>2} {dC:>4} | {tot:>5} "
          f"{nA:>8} {nB:>6} {str(agree == tot):>6}")

print()
print("判读：全部『一致 = True』⟹ 线性刻画成立 ✓；否则需撤回")
