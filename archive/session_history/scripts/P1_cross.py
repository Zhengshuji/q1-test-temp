# -*- coding: utf-8 -*-
"""同一命名空间内对照：同一实例分别走 (i) 手工 rkmat 探测 与 (ii) test_caseII_YES.build"""
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\test_C2_conic_sq.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random(90090009)")[0]
exec(head)


def matpow(M, k):
    n = len(M)
    R = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = mm(R, M)
    return R


rng = random.Random(11235813)
print("同一命名空间对照（seed 与 test_C2_gen_final.py 相同）")
print()
shown = 0
for t in range(400):
    if shown >= 3: break
    m = 2
    n, p, r = 5, 1, 1
    Amat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
    Cmat = [[rng.randint(-2, 2) for _ in range(n)]]
    Ac, Cc = toF(Amat), toF(Cmat)
    if rk(Cc) != p: continue
    Lc = mm(Cc, matpow(Ac, m))
    if rk(Lc) != r: continue
    if rk(Lc + Cc) != r + p: continue
    if rk(Cc + mm(Cc, Ac)) != 2: continue
    Z = orb(Lc, Ac, n) + orb(Cc, Ac, n); OC = orb(Cc, Ac, n)
    if rk(Z + OC) != rk(OC): continue
    try:
        Lx, eta = p1(Ac, Cc, Lc)
    except Exception:
        continue
    if not condA(Ac, Cc, Lx): continue
    q0 = sum(eta); dC = n - p; s = dC - r; k = q0 - r
    if k != 2 or s != 3: continue
    shown += 1
    # (i) 手工探测
    NC = ker_basis(Cc)
    L0NC = mm(Lc, NC)
    R = Lx[len(Lc):]; RNC = mm(R, NC)
    K = ker_basis(L0NC); mK = len(K[0]) if (K and K[0]) else 0
    Kr = [[K[a][j] for a in range(dC)] for j in range(mK)]
    rkmat = [[mm(RNC, [[Kr[j][a] for a in range(dC)]])[ii][0] for j in range(mK)]
             for ii in range(k)]
    solv = all(solve(rkmat, [[F(1) if ii == j else F(0)] for ii in range(k)]) is not None
               for j in range(k))
    print(f"--- 实例 {shown} ---")
    print(f"  q0={q0} k={k} s={s} dC={dC} mK={mK}  rank[rkmat]={rk(rkmat)}  全部 e_j 可解={solv}")
    # (ii) 调用 test_caseII_YES.build
    D = build(Ac, Cc, Lc, Lx)
    print(f"  build(...) -> {'None' if D is None else 'dict(dCA=%s)' % D.get('dCA')}")
    if D is None:
        bt = build_norm_T(Ac, Cc, Lc, Lx)
        print(f"  build_norm_T -> {'None' if bt is None else bt[:4]}")
