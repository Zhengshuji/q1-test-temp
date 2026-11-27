# -*- coding: utf-8 -*-
"""
c6 的正确（ℓ-free）严格判定

推导（平行情形，k=1）：
   (A)  ⟺ ∀i: π((L·A)_i) ∈ span{π(L_j)}_j
   T5a  ⟹ π(w) ∥ π(L0)
   合并 ⟹ (A)∧T5a  ⟺  π(w) ∥ π(L0)  且  π(w·A) ∥ π(L0)
   —— **关于 w 的线性系统** ⟹ 一次求解即严格判定 ✓

⚠️ 前几轮"固定 ℓ 再扫"的做法是错误的（ℓ 本应自由 ⟹ 那是对 (A)-轨迹的**子集**取样）
"""
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\exact_count_thm7.py",
           encoding="utf-8").read()
exec(src.split("rng = random.Random")[0])
srcS = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\reliable_S_test.py",
            encoding="utf-8").read()
exec(srcS.split("# ---------- 主实验 ----------")[0])


def MM(X, Y):
    assert X and Y and len(X[0]) == len(Y), "维数错配"
    return mm(X, Y)


def matpow(M, k):
    n = len(M)
    R = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = MM(R, M)
    return R


def solve_parallel(Ac, Cc, Lc):
    """解 π(w)∥π(L0) ∧ π(wA)∥π(L0)；返回 w 或 None"""
    n = len(Ac)
    W = Cc + MM(Cc, Ac); N = ker_basis(W); d = len(N[0])

    def pv(v):
        return [sum(v[i] * N[i][j] for i in range(n)) for j in range(d)]

    pf = pv(Lc[0])                          # π(L0) 的第一行
    if all(x == 0 for x in pf):
        return None                          # 退化：π(L0)=0 ⟹ 条件自动，另处理
    ANA = MM(Ac, N)                          # π(wA) = w·(A N)
    rows, rhs = [], []
    for i in range(d):                       # π(w) ∥ π(L0)
        for j in range(i + 1, d):
            rows.append([N[t][i] * pf[j] - N[t][j] * pf[i] for t in range(n)])
            rhs.append([F(0)])
    for i in range(d):                       # π(wA) ∥ π(L0)
        for j in range(i + 1, d):
            rows.append([ANA[t][i] * pf[j] - ANA[t][j] * pf[i] for t in range(n)])
            rhs.append([F(0)])
    if not rows:
        return None
    sol = solve(rows, rhs)
    if sol is None:
        return None
    y, ns = sol
    # 在解空间中找非零 w（并优先要秩降 + (S)）
    cands = []
    for v in [y] + list(ns):
        w = [v[t] for t in range(n)]
        if any(x != 0 for x in w):
            cands.append(w)
    rng = random.Random(12345)
    for _ in range(200):
        w = y[:]
        for v in ns:
            c = F(rng.randint(-3, 3))
            w = [w[t] + c * v[t] for t in range(n)]
        if any(x != 0 for x in w):
            cands.append(w)
    for w in cands:
        Ln = [row[:] for row in Lc] + [w]
        if rk(MM(Ln, Ac) + Ln + W) != rk(Ln + W):
            continue                          # 需 (A)
        H = MM(Ln, N)
        if rk(H) >= len(Ln):
            continue                          # 需秩降
        Fm = MM(MM(Ln, Ac), N)
        if S_holds(H, Fm):
            return w, H, Fm
    return "nodrop"


rng = random.Random(246813)
print("c6 的 ℓ-free 严格判定：(A)∧T5a ⟺ π(w)∥π(L0) ∧ π(wA)∥π(L0)")
print()
print(f"{'#':>2} {'n':>2} {'r':>2} {'q0':>3} {'k':>2} {'d_CA':>4} | {'线性系统':>8} "
      f"{'秩降+(S) 见证':>13} | {'结论':>26}")
print("-" * 84)
shown = 0
cnt = {"yes": 0, "nodrop": 0, "none": 0}
for t in range(400000):
    if shown >= 10:
        break
    n, p, r = rng.randint(4, 6), 1, rng.randint(1, 4)
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
    W = Cc + MM(Cc, Ac); dCA = n - rk(W)
    if dCA < q0: continue                       # 情形 II
    NCA = ker_basis(W)
    L0 = Lc[0]; L0A = MM(Lc, Ac)[0]
    pL0 = [sum(L0[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]
    pL0A = [sum(L0A[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]
    if rk([pL0, pL0A]) != 1: continue           # 只做平行
    res = solve_parallel(Ac, Cc, Lc)
    shown += 1
    if res is None:
        cnt["none"] += 1
        print(f"{shown:>2} {n:>2} {r:>2} {q0:>3} {k:>2} {dCA:>4} | {'无解':>8} "
              f"{'—':>13} | {'(A)∧T5a 不可行':>26}")
    elif res == "nodrop":
        cnt["nodrop"] += 1
        print(f"{shown:>2} {n:>2} {r:>2} {q0:>3} {k:>2} {dCA:>4} | {'有解':>8} "
              f"{'无':>13} | {'有解但无秩降/(S)':>26}")
    else:
        cnt["yes"] += 1
        print(f"{shown:>2} {n:>2} {r:>2} {q0:>3} {k:>2} {dCA:>4} | {'有解':>8} "
              f"{'**有**':>13} | {'**情形 II 平行 ⟹ YES**':>26}")

print()
print(f"=== 汇总：YES {cnt['yes']} / 无秩降 {cnt['nodrop']} / 不可行 {cnt['none']} "
      f"（共 {shown}）===")
print()
print("判读：")
print("  · 出现 YES ⟹ **c6 被否证**（情形 II 平行可为 YES）")
print("  · 全『不可行』⟹ c6 得到严格支持")
