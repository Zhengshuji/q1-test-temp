# -*- coding: utf-8 -*-
"""
决定性实验：验证残余 (★''')
   见证是否存在且仅存在于**秩跳变点**（rank H < d_CA）？

步骤（对 d_CA >= 2 且 d_CA < q0 的实例）：
  1. 用多起点最小化找到 H 的 d_CA 阶子式的公共零点 Θ*（即 rank H(Θ*) < d_CA）
  2. 精确复核 rank H(Θ*) < d_CA
  3. 在该点检验 (A) 与 (S)（可靠判据）
  4. 在该点附近取常秩点（rank H = d_CA），检验 (S)
"""
import itertools
import random
from fractions import Fraction as F

import numpy as np

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\test_S0_conjecture.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random(778899)")[0]
exec(head)


def data_from(Ac, Cc, Lc, Lx):
    D = get_data(Ac, Cc, Lc, Lx)
    if D is None:
        return None
    CA = mm(Cc, Ac)
    NCA = ker_basis(CA + Cc)
    D['NCA'] = NCA
    D['dCA'] = len(NCA[0]) if (NCA and NCA[0]) else 0
    return D


def H_at(t, D):
    WJ = WJ_of(t, D['r'], D['k'], D['s'], D['dC'])
    Lred = mm(mm(WJ, D['Ti']), D['MC'])
    return mm(Lred, D['NCA'])


def condA_at(t, D):
    WJ = WJ_of(t, D['r'], D['k'], D['s'], D['dC'])
    return rk(WJ + D['BAT'] + mm(WJ, D['AT'])) == rk(WJ + D['BAT'])


def cand_from_float(x, D):
    return [F(v).limit_denominator(10 ** 5) for v in x]


def pol_ish(t, D):
    """返回 H 的子式浮点值（用精确 H 再转浮点）"""
    Hm = H_at([F(v).limit_denominator(10 ** 5) for v in t], D)
    Hf = np.array([[float(x) for x in row] for row in Hm])
    if Hf.size == 0 or D['dCA'] == 0:
        return np.array([])
    return np.array([float(np.linalg.det(Hf[list(rs), :]))
                     for rs in itertools.combinations(range(D['q0']), D['dCA'])])


rng = random.Random(314159)
print("验证 (★''')：见证能否只存在于秩跳变点 (rank H < d_CA)")
print()
print(f"{'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'dCA':>4} {'dimT':>4} | "
      f"{'找到零点':>8} {'rankH(Θ*)':>9} {'(A)(Θ*)':>8} {'(S)(Θ*)':>8} | "
      f"{'附近常秩 (S) 命中':>18}")
print("-" * 96)
found_any = 0
for trial in range(60000):
    if found_any >= 5:
        break
    n = rng.randint(4, 6)
    p = rng.randint(1, n - 1)
    r = rng.randint(1, n - p)
    for _ in range(60):
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
        if k < 1 or k > s: continue
        if 2 * p + q0 < n: continue
        if k * (s - k) > 3: continue
        D = data_from(Ac, Cc, Lc, Lx)
        if D is None: continue
        dCA = D['dCA']
        if not (2 <= dCA < q0): continue          # 只要 d_CA >= 2 的**情形 I**
        dim = k * (s - k)
        # 1. 寻找子式公共零点
        best = (float('inf'), None)
        for _s2 in range(800):
            x = np.random.randn(dim) * 2.0
            for _it in range(300):
                f = pol_ish(x, D)
                if f.size == 0:
                    break
                val = float(np.sum(f * f))
                if val < 1e-24:
                    break
                J = np.zeros((f.size, dim)); h = 1e-6
                for a in range(dim):
                    xp = x.copy(); xp[a] += h
                    J[:, a] = (pol_ish(xp, D) - f) / h
                try:
                    step = np.linalg.lstsq(J, f, rcond=None)[0]
                except Exception:
                    break
                x = x - 0.6 * step
            f = pol_ish(x, D)
            val = float(np.sum(f * f))
            if val < best[0]:
                best = (val, x.copy())
        zero_found = best[0] < 1e-16 and best[1] is not None
        tstar = cand_from_float(best[1], D) if zero_found else None
        # 2. 精确复核
        if zero_found:
            Hm = H_at(tstar, D)
            rH = rk(Hm) if (Hm and Hm[0]) else 0
            zero_found = (rH < dCA)
        if not zero_found:
            continue
        A_ok = condA_at(tstar, D)
        Hm = H_at(tstar, D)
        Fm = mm(mm(mm(WJ_of(tstar, D['r'], D['k'], D['s'], D['dC']), D['Ti']), D['MC']), 
                 mm(Ac, D['NCA'])) if False else None
        # 精确 (S)
        WJt = WJ_of(tstar, D['r'], D['k'], D['s'], D['dC'])
        Lred = mm(mm(WJt, D['Ti']), D['MC'])
        Hm = mm(Lred, D['NCA'])
        Fm = mm(mm(Lred, Ac), D['NCA'])
        S_at_star = S_holds(Hm, Fm)
        # 3. 附近常秩点
        keep = 0; tot = 0
        for _p2 in range(15):
            t2 = tstar[:]
            for a in range(len(t2)):
                t2[a] += F(rng.randint(-9, 9), rng.randint(10, 100))
            Hm2 = H_at(t2, D)
            if (rk(Hm2) if (Hm2 and Hm2[0]) else 0) != dCA:
                continue
            tot += 1
            if S_holds(Hm2, mm(mm(mm(WJ_of(t2, D['r'], D['k'], D['s'], D['dC']),
                                      D['Ti']), D['MC']), Ac), D['NCA']) if False else False:
                pass
            WJ2 = WJ_of(t2, D['r'], D['k'], D['s'], D['dC'])
            Lred2 = mm(mm(WJ2, D['Ti']), D['MC'])
            if S_holds(mm(Lred2, D['NCA']), mm(mm(Lred2, Ac), D['NCA'])):
                keep += 1
        found_any += 1
        rHs = rk(Hm) if (Hm and Hm[0]) else 0
        print(f"{n:>2} {p:>2} {r:>2} {q0:>3} {dCA:>4} {dim:>4} | "
              f"{'是':>8} {rHs:>9} {str(A_ok):>8} {str(S_at_star):>8} | "
              f"{keep:>7}/{tot:<9}")
        break

print()
print("解读：")
print("  · 若 rankH(Θ*) < d_CA 且 (A)∧(S) 在 Θ* 成立  ⟹ 存在「只可能」在跳变点的见证候选")
print("  · 关键看最后一列：附近常秩点 (rankH = d_CA) 上 (S) 是否也成立")
print("    若 keep/tot ≈ tot ⟹ (S) 在 Θ* 附近的开集上成立 ⟹ (★''') 成立")
print("    若 keep = 0      ⟹ 见证只在跳变点 ⟹ (★''') 假，分支 A 需再修正")
