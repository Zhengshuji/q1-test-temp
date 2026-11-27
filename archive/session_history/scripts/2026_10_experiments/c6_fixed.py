# -*- coding: utf-8 -*-
"""
修正版（第 20 处更正后）：用**完整的**平行判据重做"情形 II 平行"的分析

修正点：
   旧（错）： 平行 ⟺ rank[π(L0 第一行); π((L0A) 第一行)] = 1        ✗ 太弱
   新（对）： 平行 ⟺ rank[π(L0); π(L0A)] = 1  （**全部 r 行**）      ✓

判定用 ℓ-free 线性系统：
   (A)∧T5a  ⟺  π(w) ∥ π(L0)  且  π(w·A) ∥ π(L0)
              （π(L0) 取**整块** r×d_CA —— 平行时所有行成比例，取其非零行即可）
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


def pi_of(v, N, n):
    d = len(N[0])
    return [sum(v[i] * N[i][j] for i in range(n)) for j in range(d)]


def solve_parallel(Ac, Cc, Lc, pf):
    """解 π(w)∥pf 且 π(wA)∥pf（pf ≠ 0）；返回 (w,H,F) 或 None / 'nodrop'"""
    n = len(Ac)
    W = Cc + MM(Cc, Ac); N = ker_basis(W); d = len(N[0])
    ANA = MM(Ac, N)
    rows = []
    for i in range(d):
        for j in range(i + 1, d):
            rows.append([N[t][i] * pf[j] - N[t][j] * pf[i] for t in range(n)])
    for i in range(d):
        for j in range(i + 1, d):
            rows.append([ANA[t][i] * pf[j] - ANA[t][j] * pf[i] for t in range(n)])
    if not rows:
        return None
    sol = solve(rows, [[F(0)] for _ in rows])
    if sol is None:
        return None
    y, ns = sol
    rng = random.Random(999)
    cands = [y] + list(ns)
    for _ in range(300):
        w = y[:]
        for v in ns:
            c = F(rng.randint(-3, 3))
            w = [w[t] + c * v[t] for t in range(n)]
        cands.append(w)
    for cand in cands:
        w = [cand[t] for t in range(n)]
        if all(x == 0 for x in w):
            continue
        Ln = [row[:] for row in Lc] + [w]
        if rk(MM(Ln, Ac) + Ln + W) != rk(Ln + W):
            continue
        H = MM(Ln, N)
        if rk(H) >= len(Ln):
            continue
        Fm = MM(MM(Ln, Ac), N)
        if S_holds(H, Fm):
            return (w, H, Fm)
    return "nodrop"


rng = random.Random(13571357)
print("修正版：完整平行判据 ⟹ 重做情形 II 平行")
print()
print(f"{'#':>2} {'n':>2} {'r':>2} {'q0':>3} {'k':>2} {'d_CA':>4} | "
      f"{'系统':>6} {'(A)∧秩降∧(S)':>12} | {'结论':>24}")
print("-" * 80)
shown = 0
stat = {"yes": 0, "nodrop": 0, "none": 0}
for t in range(400000):
    if shown >= 8:
        break
    n, p, r = rng.randint(4, 6), 1, 1          # 限制 r=1（此时真平行判据与旧判据一致）
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
    if dCA < q0: continue
    N = ker_basis(W)
    # ✅ 完整平行判据：rank[π(L0); π(L0A)] = 1
    pL0 = [pi_of(Lc[i], N, n) for i in range(r)]
    pL0A = [pi_of(MM(Lc, Ac)[i], N, n) for i in range(r)]
    if rk(pL0 + pL0A) != 1: continue          # ← 完整判据 ✓
    # 取非零行作为 pf
    pf = None
    for v in pL0 + pL0A:
        if any(x != 0 for x in v):
            pf = v; break
    if pf is None:
        continue                               # π(L0)=0 退化，另处理
    res = solve_parallel(Ac, Cc, Lc, pf)
    shown += 1
    if res is None:
        stat["none"] += 1
        print(f"{shown:>2} {n:>2} {r:>2} {q0:>3} {k:>2} {dCA:>4} | {'无解':>6} "
              f"{'—':>12} | {'(A)∧T5a 不可行':>24}")
    elif res == "nodrop":
        stat["nodrop"] += 1
        print(f"{shown:>2} {n:>2} {r:>2} {q0:>3} {k:>2} {dCA:>4} | {'有解':>6} "
              f"{'无':>12} | {'有解但无秩降/(S)':>24}")
    else:
        stat["yes"] += 1
        print(f"{shown:>2} {n:>2} {r:>2} {q0:>3} {k:>2} {dCA:>4} | {'有解':>6} "
              f"{'**有**':>12} | {'**情形 II 平行 ⟹ YES**':>24}")

print()
print(f"=== YES {stat['yes']} / 无秩降 {stat['nodrop']} / 不可行 {stat['none']} "
      f"（共 {shown}，真平行）===")
print()
print("判读：")
print("  · YES ⟹ c6 被否证（真平行下可为 YES）")
print("  · 全『不可行』⟹ c6 得到（这次正确的）支持")
