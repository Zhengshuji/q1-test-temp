# -*- coding: utf-8 -*-
"""P1：T-构造第 2 步失败的数学本质是什么？

条件：solve(rkmat, e_j) 有解 (j<k)，其中
    rkmat[ii][j] = (R·N_C·K_j)[ii],   K_j = ker(L0·N_C) 的基
即要求  rank(R·N_C·K) >= k。

若 rank < k ⟹ P1 构造出的 R 的 k 行在商空间中不独立
  ⟹ 要么 (a) 该实例不在 P1 参数化范围内，要么 (b) 实现有缺口。
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


def probe(Ac, Cc, Lc, Lx, tag):
    n, p, r = len(Ac), len(Cc), len(Lc)
    NC = ker_basis(Cc); dC = len(NC[0])
    L0NC = mm(Lc, NC)
    R = Lx[len(Lc):]; RNC = mm(R, NC)
    k = len(R); s = dC - r
    K = ker_basis(L0NC)
    mK = len(K[0]) if (K and K[0]) else 0
    Kr = [[K[a][j] for a in range(dC)] for j in range(mK)]
    rkmat = [[mm(RNC, [[Kr[j][a]] for a in range(dC)])[ii][0] for j in range(mK)]
             for ii in range(k)]
    print(f"--- {tag} ---")
    print(f"  n={n} p={p} r={r}  η行数 k={k}  s={s}  dC={dC}  mK=dim ker(L0·NC)={mK}")
    print(f"  Lx 行数 = {len(Lx)}   rank(Lx) = {rk(Lx)}")
    print(f"  rank[rkmat] = {rk(rkmat)}   （需要 >= k = {k}）")
    print(f"  rkmat ({k}x{mK}) = {[[str(z) for z in row] for row in rkmat]}")
    # 需要 e_j ∈ im(rkmat) 对所有 j<k
    ok = True
    for j in range(k):
        ej = [[F(1) if ii == j else F(0)] for ii in range(k)]
        if solve(rkmat, ej) is None:
            ok = False
    print(f"  全部 e_j 可解? {ok}")
    return dict(k=k, mK=mK, rank_rkmat=rk(rkmat), ok=ok)


rng = random.Random(31415)
print("=== 对照：通过 build 的实例（k=1）===")
done1 = 0
for t in range(20000):
    if done1 >= 2: break
    n, p, r = 5, 1, 2
    Amat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
    Cmat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)]
    Lmat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(r)]
    Ac, Cc, Lc = toF(Amat), toF(Cmat), toF(Lmat)
    if rk(Cc) != p or rk(Lc) != r: continue
    if rk(Lc + Cc) != r + p: continue
    Z = orb(Lc, Ac, n) + orb(Cc, Ac, n); OC = orb(Cc, Ac, n)
    if rk(Z + OC) != rk(OC): continue
    try:
        Lx, eta = p1(Ac, Cc, Lc)
    except Exception:
        continue
    if not condA(Ac, Cc, Lx): continue
    if len(Lx) - len(Lc) != 1: continue
    probe(Ac, Cc, Lc, Lx, f"随机实例 {done1+1}（k=1）")
    done1 += 1

print()
print("=== 生成器实例 L0 = C·A^m（k=2）===")
done2 = 0
for t in range(20000):
    if done2 >= 2: break
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
    if len(Lx) - len(Lc) != 2: continue
    probe(Ac, Cc, Lc, Lx, f"生成器实例 {done2+1}（k=2）")
    done2 += 1
