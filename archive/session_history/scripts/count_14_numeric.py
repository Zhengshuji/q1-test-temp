# -*- coding: utf-8 -*-
"""
(1,4) 情形的解数 —— 关键数据点。
用最小二乘多起点数值求根，再对每个候选解做**精确有理验证**。
"""
import random
from fractions import Fraction as F

import numpy as np

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\exact_count_thm7.py",
           encoding="utf-8").read()
exec(src.split("rng = random.Random(112233)")[0])


def build_data(AT, BAT, r, k, s, dC):
    return AT, BAT, r, k, s, dC


def minors_val(t, r, k, s, dC, AT, BAT):
    """返回 [P; q_1..q_{r+k}] 的所有 2x2 子式（作为 t 的函数），浮点"""
    WJ = np.zeros((r + k, dC))
    for i in range(r):
        WJ[i, i] = 1.0
    idx = 0
    for i in range(k):
        WJ[r + i, r + i] = 1.0
        for j in range(k, s):
            WJ[r + i, r + j] = t[idx]; idx += 1
    NJ = WJ @ AT
    B2 = BAT[:, r:r + s].astype(float)
    P = B2[:, :k] @ t.reshape(k, s - k) + B2[:, k:]           # p × (s-k)
    rows = [P]
    for i in range(r + k):
        g1 = NJ[i, r:r + k]                                    # 1×k
        g2 = NJ[i, r + k:r + s]                                # 1×(s-k)
        q = g1 @ t.reshape(k, s - k) - g2
        rows.append(q.reshape(1, -1))
    M = np.vstack(rows)                                        # (p+r+k) × (s-k)
    # 所有 2x2 子式（因为 rankP = 1）
    out = []
    for i in range(M.shape[0]):
        for j in range(i + 1, M.shape[0]):
            for a in range(M.shape[1]):
                for b in range(a + 1, M.shape[1]):
                    out.append(M[i, a] * M[j, b] - M[i, b] * M[j, a])
    return np.array(out)


def cond_A_exact(t, r, k, s, dC, AT, BAT):
    WJ = []
    for i in range(r):
        WJ.append([F(1) if j == i else F(0) for j in range(dC)])
    idx = 0
    for i in range(k):
        row = [F(0)] * dC
        row[r + i] = F(1)
        for j in range(k, s):
            row[r + j] = t[idx]; idx += 1
        WJ.append(row)
    return rk(WJ + BAT + mm(WJ, AT)) == rk(WJ + BAT)


rng = random.Random(741852)
found = {}
need = [(1, 3, 4), (1, 4, 5)]      # (k, s, dC)
for trial in range(40000):
    if len(found) >= 2:
        break
    n = rng.randint(5, 7)
    p = rng.randint(1, n - 2)
    r = rng.randint(1, n - p - 1)
    for _ in range(150):
        Am = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
        Cm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)]
        Lm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(r)]
        Ac, Cc, Lc = toF(Am), toF(Cm), toF(Lm)
        if rk(Cc) != p or rk(Lc) != r: continue
        if rk(Lc + Cc) != r + p: continue
        Z_ = orb(Lc, Ac, n) + orb(Cc, Ac, n); OC = orb(Cc, Ac, n)
        if rk(Z_ + OC) != rk(OC): continue
        Lx, eta = p1(Ac, Cc, Lc)
        if not condA(Ac, Cc, Lx): continue
        q0 = sum(eta)
        dC = n - p; s = dC - r; k = q0 - r
        if k < 1 or k > s: continue
        if 2 * p + q0 >= n: continue
        key = (k, s, dC)
        if key not in need or key in found: continue
        bt = build_norm_T(Ac, Cc, Lc, Lx)
        if bt is None: continue
        dC2, s2, k2, r2, AT, BAT = bt
        if (r2, k2, s2, dC2) != (r, k, s, dC): continue
        found[key] = (AT, BAT, r, k, s, dC)
        break
    if len(found) >= 2:
        break

print("在 (k,s) 情形上用多起点数值求根 + 精确验证，统计 (A)-解个数")
print()
for key in need:
    if key not in found:
        print(f"  {key}: 未找到实例")
        continue
    AT, BAT, r, k, s, dC = found[key]
    ATr = [[float(x) for x in row] for row in AT]
    BATr = [[float(x) for x in row] for row in BAT]
    ATr = np.array(ATr); BATr = np.array(BATr)
    dim = k * (s - k)

    def f(t):
        return minors_val(np.array(t), r, k, s, dC, ATr, BATr)

    # 多起点最小二乘
    sols = []
    for _ in range(4000):
        t0 = np.random.randn(dim) * 3.0
        t = t0.copy()
        for _it in range(300):
            g = f(t)
            J = np.zeros((len(g), dim))
            h = 1e-7
            for a in range(dim):
                tp = t.copy(); tp[a] += h
                J[:, a] = (f(tp) - g) / h
            try:
                step = np.linalg.lstsq(J, g, rcond=None)[0]
            except Exception:
                break
            t = t - step
            if np.linalg.norm(f(t)) < 1e-14:
                break
        if np.linalg.norm(f(t)) < 1e-10:
            if not any(np.linalg.norm(t - u) < 1e-5 for u in sols):
                sols.append(t)
    # 精确验证（每个解四舍五入到有理数）
    ok = []
    for t in sols:
        tf = [F(x).limit_denominator(10**7) for x in t]
        if cond_A_exact(tf, r, k, s, dC, AT, BAT):
            ok.append(tf)
    print(f"  (k,s,dC)={key}: 数值候选 {len(sols)} 个，精确验证通过 {len(ok)} 个")
    for t in ok:
        print(f"      Θ = {[str(x) for x in t]}")
