# -*- coding: utf-8 -*-
"""验证 build_norm_T 的返回与 build 的期望是否不匹配"""
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


rng = random.Random(4242)
shown = 0
for t in range(3000):
    if shown >= 3: break
    n, p, r, m = 5, 1, 1, 2
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
    except Exception as e:
        print("p1 err", e); continue
    if not condA(Ac, Cc, Lx): continue
    shown += 1
    q0 = len(Lx); dC_exp = n - p; s_exp = dC_exp - r; k_exp = q0 - r
    print(f"--- 实例 {shown} ---")
    print(f"  r={r} p={p} n={n}  q0={q0}  k_期望={k_exp}  s_期望={s_exp}  dC_期望={dC_exp}")
    NC = ker_basis(Cc)
    print(f"  ker_basis(C) 的类型: 基向量个数={len(NC)}, 每个基向量长度={len(NC[0])}")
    L0NC = mm(Lc, NC)
    print(f"  L0·NC 的形状: {len(L0NC)} x {len(L0NC[0])}")
    print(f"  L0·NC = {[[str(z) for z in row] for row in L0NC]}")
    K = ker_basis(L0NC)
    mK = len(K[0]) if (K and K[0]) else 0
    print(f"  ker(L0NC): 基个数={len(K) if K else 0}, mK(len(K[0]) if 按行约定)={mK}")
    bt = build_norm_T(Ac, Cc, Lc, Lx)
    if bt is None:
        print("  build_norm_T -> None")
    else:
        dC2, s2, k2, r2, _, _ = bt
        print(f"  build_norm_T -> (dC2,s2,k2,r2) = ({dC2},{s2},{k2},{r2})")
        print(f"  期望           (dC,s,k,r)  = ({dC_exp},{s_exp},{k_exp},{r})")
        print(f"  匹配? {(r2,k2,s2,dC2) == (r,k_exp,s_exp,dC_exp)}")
