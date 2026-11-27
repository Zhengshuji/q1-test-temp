# -*- coding: utf-8 -*-
"""
决定性实验（快速版）：见证能否**只**存在于秩跳变点（rank H < d_CA）？

若找到这样的见证 Θ*：rank H(Θ*) < d_CA 且 (A)∧(S) 成立，
而**附近所有常秩点 (rank H = d_CA) 上 (S) 都失败** ⟹ (★''') 被证伪 ⟹ 分支 A 需再修正。

实现：浮点做优化（快），只在最后对候选点用精确有理算术复核。
"""
import itertools
import random
from fractions import Fraction as F

import numpy as np

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\test_S0_conjecture.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random(778899)")[0]
exec(head)


def to_f(M):
    return np.array([[float(x) for x in row] for row in M])


def condA_at(t, r, k, s, dC, D):
    WJ = WJ_of(t, r, k, s, dC)
    return rk(WJ + D['BAT'] + mm(WJ, D['AT'])) == rk(WJ + D['BAT'])


def WJ_f(t, r, k, s, dC):
    W = np.zeros((r + k, dC))
    for i in range(r):
        W[i, i] = 1.0
    idx = 0
    for i in range(k):
        W[r + i, r + i] = 1.0
        for j in range(k, s):
            W[r + i, r + j] = t[idx]; idx += 1
    return W


def setup(Ac, Cc, Lc, Lx):
    D = get_data(Ac, Cc, Lc, Lx)
    if D is None:
        return None
    CA = mm(Cc, Ac)
    NCA = ker_basis(CA + Cc)
    dCA = len(NCA[0]) if (NCA and NCA[0]) else 0
    D['NCA'] = NCA; D['dCA'] = dCA
    D['M1f'] = (to_f(D['Ti']) @ to_f(D['MC'])) if dCA else None
    D['NCAf'] = to_f(NCA) if dCA else None
    D['ATf'] = to_f(D['AT']); D['BATf'] = to_f(D['BAT'])
    return D


def Hf(t, D):
    W = WJ_f(t, D['r'], D['k'], D['s'], D['dC'])
    return W @ D['M1f'] @ D['NCAf']


def minorsf(t, D):
    H = Hf(t, D)
    q, d = H.shape
    return np.array([float(np.linalg.det(H[list(rs), :]))
                     for rs in itertools.combinations(range(q), d)])


def condA_f(t, D):
    W = WJ_f(t, D['r'], D['k'], D['s'], D['dC'])
    M = np.vstack([W, D['BATf']])
    MX = np.vstack([W, D['BATf'], W @ D['ATf']])
    s1 = np.linalg.svd(M, compute_uv=False)
    s2 = np.linalg.svd(MX, compute_uv=False)
    r1 = int(np.sum(s1 > 1e-9 * max(M.shape) * s1[0]))
    r2 = int(np.sum(s2 > 1e-9 * max(MX.shape) * s2[0]))
    return r1 == r2


rng = random.Random(24681357)
print("决定性实验：见证能否只存在于秩跳变点？（浮点优化 + 精确复核）")
print()
print(f"{'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'dCA':>4} {'dimT':>4} | "
      f"{'找到Θ*':>7} {'rankH*':>7} {'(A)':>5} {'(S)':>5} | {'附近常秩点 (S)':>16}")
print("-" * 88)
n_case = 0
for trial in range(30000):
    if n_case >= 5:
        break
    n = 6
    p = 2
    r = 2
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
        if k < 1 or k > s: continue
        if 2 * p + q0 < n: continue
        dim = k * (s - k)
        if dim > 3: continue
        D = setup(Ac, Cc, Lc, Lx)
        if D is None: continue
        dCA = D['dCA']
        if not (2 <= dCA < q0): continue
        # --- 浮点优化求子式公共零点 ---
        best = (float('inf'), None)
        for _s3 in range(300):
            x = np.random.randn(dim) * 2.0
            for _it in range(400):
                f = minorsf(x, D)
                val = float(f @ f)
                if val < 1e-26:
                    break
                J = np.zeros((f.size, dim)); h = 1e-6
                for a in range(dim):
                    xp = x.copy(); xp[a] += h
                    J[:, a] = (minorsf(xp, D) - f) / h
                try:
                    step = np.linalg.lstsq(J, f, rcond=None)[0]
                except Exception:
                    break
                x = x - 0.7 * step
            val = float(minorsf(x, D) @ minorsf(x, D))
            if val < best[0]:
                best = (val, x.copy())
        if best[1] is None or best[0] > 1e-18:
            continue
        tf = [F(v).limit_denominator(10 ** 4) for v in best[1]]
        # --- 精确复核 rank H(Θ*) < dCA ---
        WJt = WJ_of(tf, r, k, s, dC)
        Lred = mm(mm(WJt, D['Ti']), D['MC'])
        Hm = mm(Lred, D['NCA'])
        rH = rk(Hm) if (Hm and Hm[0]) else 0
        if rH >= dCA:
            continue
        A_ok = condA_at(tf, r, k, s, dC, D)
        S_ok = S_holds(Hm, mm(mm(Lred, Ac), D['NCA']))
        # --- 附近常秩点 ---
        keep = 0; tot = 0
        for _p3 in range(12):
            t2 = tf[:]
            for a in range(len(t2)):
                t2[a] += F(rng.randint(-9, 9), rng.randint(10, 100))
            WJ2 = WJ_of(t2, r, k, s, dC)
            Lred2 = mm(mm(WJ2, D['Ti']), D['MC'])
            Hm2 = mm(Lred2, D['NCA'])
            if (rk(Hm2) if (Hm2 and Hm2[0]) else 0) != dCA:
                continue
            tot += 1
            if S_holds(Hm2, mm(mm(Lred2, Ac), D['NCA'])):
                keep += 1
        n_case += 1
        print(f"{n:>2} {p:>2} {r:>2} {q0:>3} {dCA:>4} {dim:>4} | "
              f"{'是':>7} {rH:>7} {str(A_ok):>5} {str(S_ok):>5} | "
              f"{keep:>6}/{tot:<9}")
        break

print()
print("判读：")
print("  · 若 (S) 在 Θ* 成立、而附近常秩点 keep = 0 ⟹ (★''') 被证伪")
print("  · 若附近常秩点 keep ≈ tot ⟹ (S) 在 Θ* 邻域内开 ⟹ (★''') 成立")
