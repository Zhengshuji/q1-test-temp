# -*- coding: utf-8 -*-
"""
决定性收尾：正确判定分支 1（λ12=1）是否相容

关键：M 是 6×7，[M|b] 是 6×8 ⟹ **必须用 5 阶（或实际秩阶）子式**，
      不能像上一轮那样取 min(2d, n+2)=6 阶（那只能证明 rank ≤ 5）
"""
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\exact_count_thm7.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random")[0]
exec(head)


def MM(X, Y):
    assert X and Y and len(X[0]) == len(Y), f"维数错配 {len(X)}x{len(X[0])} 乘 {len(Y)}x{len(Y[0])}"
    return mm(X, Y)


def matpow(M, k):
    n = len(M)
    R = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = MM(R, M)
    return R


def build(NCA, Ac, Lc, l11):
    n = len(Ac)
    d = len(NCA[0])
    L0 = Lc[0]
    L0A = MM(Lc, Ac)[0]

    def pv(v):
        return [sum(v[i] * NCA[i][j] for i in range(n)) for j in range(d)]

    pL0 = pv(L0); pL0A = pv(L0A)
    u = [pL0A[j] - l11 * pL0[j] for j in range(d)]
    ANA = MM(Ac, NCA)
    nv = n + 2
    rows, b = [], []
    for j in range(d):
        rows.append([NCA[i][j] for i in range(n)] + [F(0), F(0)])
        b.append(u[j])
    for j in range(d):
        r = [ANA[i][j] for i in range(n)] + [F(0), F(0)]
        r[n] = -pL0[j]
        r[n + 1] = -u[j]
        rows.append(r); b.append(F(0))
    return rows, b


rng = random.Random(24681357)
print("决定性收尾：分支 1（λ12=1）是否相容？")
print()
print(f"{'#':>2} {'n':>2} {'r':>2} {'q0':>3} {'k':>2} {'d_CA':>4} | "
      f"{'rank M 取值':>14} {'rank[M|b] 取值':>16} | {'相容?':>6} {'结论':>20}")
print("-" * 92)
shown = 0
for t in range(200000):
    if shown >= 8:
        break
    n, p, r = rng.randint(5, 6), 1, 2
    Amat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
    Cmat = [[rng.randint(-2, 2) for _ in range(n)]]
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
    q0 = sum(eta); k = q0 - r
    if k != 1: continue
    W = Cc + MM(Cc, Ac)
    dCA = n - rk(W)
    if dCA < q0: continue
    NCA = ker_basis(W)
    L0 = Lc[0]; L0A = MM(Lc, Ac)[0]
    pL0 = [sum(L0[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]
    pL0A = [sum(L0A[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]
    if rk([pL0, pL0A]) != 1: continue              # 平行
    valsM, valsMb, cons = {}, {}, 0
    tot = 0
    for q in range(1, 13):
        for pnum in range(-20, 21):
            l11 = F(pnum, q)
            rows, b = build(NCA, Ac, Lc, l11)
            rM = rk(rows)
            aug = [rows[i] + [b[i]] for i in range(len(rows))]
            rMb = rk(aug)
            valsM[rM] = valsM.get(rM, 0) + 1
            valsMb[rMb] = valsMb.get(rMb, 0) + 1
            tot += 1
            if rM == rMb: cons += 1
    shown += 1
    ok = (cons == tot)
    print(f"{shown:>2} {n:>2} {r:>2} {q0:>3} {k:>2} {dCA:>4} | "
          f"{str(sorted(valsM.items())):>14} {str(sorted(valsMb.items())):>16} | "
          f"{str(ok):>6} "
          f"{('**恒相容 ⟹ A* 支持**' if ok else '有不相容点 ⟹ 靶子'):>20}")

print()
print("判读：")
print("  · rank[M|b] ≡ rank M（全部采样点）⟹ 分支 1 **相容** ⟹ 该区域恒 YES ⟹ 猜想 A* 支持 ⟹ 无硬度")
print("  · 存在 rank[M|b] > rank M 的点 ⟹ 分支 1 有空隙 ⟹ 靶子需进一步严格化")
