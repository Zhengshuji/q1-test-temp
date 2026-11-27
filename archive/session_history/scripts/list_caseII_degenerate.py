# -*- coding: utf-8 -*-
"""
C 的可完成部分 + B 的路线 3：把情形 II 的退化代数集**完全列出**并逐个精确检验。

设定：dimTheta = 1 且 d_CA = q0 时， {rank H < q0} = {det H = 0}（单变量多项式）。
  1. 精确写出 det H(Θ) 的系数（通过多点求值 + 插值，用有理数）
  2. 求全部**实根**（数值 + 精确复核）
  3. 对每个根精确检验 rank H < q0、(A)、(S)
  4. 统计"好点"个数 —— 若恒 ≥1，则情形 II 在该子情形下**答案恒为 YES**

形状锁定 n=5,p=1,r=2（d_CA = q0 = 3，dimΘ = 1）。
"""
import itertools
import random
from fractions import Fraction as F

import numpy as np

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\test_caseII_YES.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random(11223344)")[0]
exec(head)


def detH_exact(t, D):
    """det H(Θ) 的精确值（要求 d_CA = q0）"""
    WJ = WJ_of_f(t, D['r'], D['k'], D['s'], D['dC'])
    Lred = mm(mm(WJ, D['Ti']), D['MC'])
    Hm = mm(Lred, D['NCA'])
    q0 = D['q0']
    # 用精确行列式
    def det(M):
        n = len(M)
        if n == 1: return M[0][0]
        if n == 2: return M[0][0]*M[1][1] - M[0][1]*M[1][0]
        tot = F(0)
        for j in range(n):
            sub = [[M[i][k] for k in range(n) if k != j] for i in range(1, n)]
            tot += ((-1) ** j) * M[0][j] * det(sub)
        return tot
    return det(Hm)


def coeffs_univariate(D, deg_max=8):
    """通过 deg_max+1 个点插值求 det H(Θ) 的精确系数（Θ 单变量）"""
    pts = [F(i) for i in range(deg_max + 1)]
    vals = [detH_exact([p], D) for p in pts]
    # Lagrange 插值 -> 系数
    coef = [F(0)] * (deg_max + 1)
    for i, xi in enumerate(pts):
        # 基多项式 L_i(x) = prod_{j!=i} (x - xj)/(xi - xj)
        num = [F(1)]
        den = F(1)
        for j, xj in enumerate(pts):
            if j == i: continue
            newnum = [F(0)] * (len(num) + 1)
            for a, c in enumerate(num):
                newnum[a + 1] += c
                newnum[a] -= c * xj
            num = newnum
            den *= (xi - xj)
        for a in range(len(num)):
            coef[a] += vals[i] * num[a] / den
    while len(coef) > 1 and coef[-1] == 0:
        coef.pop()
    return coef


rng = random.Random(556677)
print("情形 II 退化代数集的完全列举（dimTheta = 1, d_CA = q0）")
print()
print(f"{'#':>2} {'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'deg detH':>8} | "
      f"{'实根数':>6} {'好点(A∧S)':>10} {'结论':>18}")
print("-" * 84)
n_inst = 0
for trial in range(60000):
    if n_inst >= 8:
        break
    n, p, r = 5, 1, 2
    for _ in range(40):
        Am = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
        Cm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)]
        Lm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(r)]
        Ac, Cc, Lc = toF(Am), toF(Cm), toF(Lm)
        if rk(Cc) != p or rk(Lc) != r: continue
        if rk(Lc + Cc) != r + p: continue
        Z = orb(Lc, Ac, n) + orb(Cc, Ac, n); OC = orb(Cc, Ac, n)
        if rk(Z + OC) != rk(OC): continue
        try:
            Lx, eta = p1(Ac, Cc, Lc)
        except Exception:
            continue
        if not condA(Ac, Cc, Lx): continue
        q0 = sum(eta)
        dC = n - p; s = dC - r; k = q0 - r
        if k < 1 or k > s or k * (s - k) != 1: continue
        if 2 * p + q0 < n: continue
        D = build(Ac, Cc, Lc, Lx)
        if D is None: continue
        if not (D['dCA'] == q0): continue
        coef = coeffs_univariate(D, deg_max=8)
        deg = len(coef) - 1
        # 求实根（数值），再精确复核
        cf = [float(c) for c in coef]
        roots = np.roots(cf[::-1]) if deg >= 1 else np.array([])
        real = [rt.real for rt in roots if abs(rt.imag) < 1e-7]
        good = 0
        tot_roots = 0
        for rr in real:
            t = [F(rr).limit_denominator(10 ** 6)]
            # 精确复核：det H 是否 ≈ 0（用有理数近似验证 rank H < q0）
            Lred, Hm = exact_H(t, D)
            rH = rk(Hm) if (Hm and Hm[0]) else 0
            if rH >= q0:
                # 尝试微调（用连分数近邻）
                cands = [F(rr).limit_denominator(d) for d in (10, 100, 1000, 10**5)]
                found = False
                for c in cands:
                    for eps in [F(1, 10**5), F(-1, 10**5), F(1, 10**3), F(-1, 10**3)]:
                        t2 = [c + eps]
                        Lred2, Hm2 = exact_H(t2, D)
                        rH2 = rk(Hm2) if (Hm2 and Hm2[0]) else 0
                        if rH2 < q0:
                            t, Lred, Hm, rH = t2, Lred2, Hm2, rH2
                            found = True
                            break
                    if found: break
                if not found:
                    continue
            tot_roots += 1
            okA = exact_A(t, D)
            okS = False
            if okA:
                okS = S_holds(Hm, mm(mm(Lred, Ac), D['NCA']))
            if okA and okS:
                good += 1
        n_inst += 1
        concl = ("恒有 YES（好点≥1）" if good >= 1 else "好点=0")
        print(f"{n_inst:>2} {n:>2} {p:>2} {r:>2} {q0:>3} {deg:>8} | "
              f"{len(real):>6} {good:>10} {concl:>18}")
        break

print()
print("判读：")
print("  · 若所有实例都有『好点 ≥ 1』⟹ 该子情形下 ν_min = q0 恒为 YES ⟹ 可判定（甚至平凡）")
print("  · 若某些实例好点 = 0 ⟹ 该子情形下答案两种都可能 ⟹ 需真正的代数判定")
print("  （注：deg detH 为奇次时必有实根，故 {rankH<q0} ≠ ∅ 必然；关键在 (A)∧(S) 是否也成立）")
