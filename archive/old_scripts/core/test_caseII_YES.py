# -*- coding: utf-8 -*-
"""
B 的决定性实验：情形 II (d_CA >= q0) 中，ν_min = q0 是否可能为 YES？

即是否存在 Θ 使 (A) ∧ (S) ∧ rank H < q0。

方法：
  1. 多起点浮点最小化 sum(所有 q0 阶子式 of H)^2
  2. 若 min ≈ 0 ⟹ 精确复核 rank H < q0 ⟹ 再精确检验 (A) 与 (S)
  3. 若 min 有正下界 ⟹ {rank H < q0} = ∅ ⟹ 该情形**恒为 NO**（可多项式认证）

形状锁定 n=5,p=1,r=2（已知会产生 d_CA = q0 = 3 的情形 II），dimΘ = k(s-k) = 1。
"""
import itertools
import random
from fractions import Fraction as F

import numpy as np

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\reliable_S_test.py",
           encoding="utf-8").read()
head = src.split("# ---------- 主实验 ----------")[0]
exec(head)


def to_f(M):
    return np.array([[float(x) for x in row] for row in M])


def WJ_of_f(t, r, k, s, dC):
    W = []
    for i in range(r):
        W.append([F(1) if j == i else F(0) for j in range(dC)])
    idx = 0
    for i in range(k):
        row = [F(0)] * dC
        row[r + i] = F(1)
        for j in range(k, s):
            row[r + j] = t[idx]; idx += 1
        W.append(row)
    return W


def build(Ac, Cc, Lc, Lx):
    n = len(Ac); p = len(Cc); r = len(Lc)
    q0 = len(Lx); dC = n - p; s = dC - r; k = q0 - r
    bt = build_norm_T(Ac, Cc, Lc, Lx)
    if bt is None:
        return None
    dC2, s2, k2, r2, AT, BAT = bt
    if (r2, k2, s2, dC2) != (r, k, s, dC):
        print('[T-dbg] 不变式不匹配'); return None
    NC = ker_basis(Cc)
    MC = mm(inv(mm(tr(NC), NC)), tr(NC))
    L0NC = mm(Lc, NC)
    R = Lx[len(Lc):]; RNC = mm(R, NC)
    K = ker_basis(L0NC); mK = len(K[0]) if (K and K[0]) else 0
    if mK == 0:
        print('[T-dbg] mK==0'); return None
    Kr = [[K[a][j] for a in range(dC)] for j in range(mK)]
    Tcols = []
    for i in range(r):
        ei = [F(1) if q == i else F(0) for q in range(r)]
        so = solve([[L0NC[a][j] for j in range(dC)] for a in range(r)],
                   [[ei[a]] for a in range(r)])
        if so is None:
            print('[T-dbg] 第1步solve失败'); return None
        xi = so[0]
        tgt = mm(RNC, [[xi[j]] for j in range(dC)])[0][0]
        rkl = [mm(RNC, [[Kr[j][a] for a in range(dC)]])[0][0] for j in range(mK)]
        c = [F(0)] * mK
        for j in range(mK):
            if rkl[j] != 0:
                c[j] = -tgt / rkl[j]; break
        z = [sum(c[j] * Kr[j][a] for j in range(mK)) for a in range(dC)]
        Tcols.append([xi[a] + z[a] for a in range(dC)])
    rkmat = [[mm(RNC, [[Kr[j][a] for a in range(dC)]])[ii][0] for j in range(mK)]
             for ii in range(k)]
    nsc = None
    for j in range(s):
        if j < k:
            ej = [[F(1) if ii == j else F(0)] for ii in range(k)]
            so = solve(rkmat, ej)
            if so is None:
                print('[T-dbg] 第2步solve失败'); return None
            yj = so[0]
        else:
            if nsc is None:
                nsc = solve(rkmat, [[F(0)] for _ in range(k)])[1]
            ix = j - k
            if ix >= len(nsc):
                print('[T-dbg] nsc 不够 ix=%d len=%d'%(ix,len(nsc))); return None
            yj = nsc[ix]
        Tcols.append([sum(yj[a] * Kr[a][jj] for a in range(mK)) for jj in range(dC)])
    T = [[Tcols[j][i] for j in range(dC)] for i in range(dC)]
    Ti = inv(T)
    if Ti is None:
        print('[T-dbg] T 奇异（inv 失败）'); return None
    CA = mm(Cc, Ac)
    NCA = ker_basis(CA + Cc)
    dCA = len(NCA[0]) if (NCA and NCA[0]) else 0
    return dict(Ac=Ac, Cc=Cc, Lc=Lc, r=r, k=k, s=s, dC=dC, q0=q0, dCA=dCA,
                AT=AT, BAT=BAT, Ti=Ti, MC=MC, NCA=NCA,
                M1f=to_f(mm(Ti, MC)), NCAf=to_f(NCA) if dCA else None)


def Hf(t, D):
    W = to_f(WJ_of_f(t, D['r'], D['k'], D['s'], D['dC']))
    return W @ D['M1f'] @ D['NCAf']


def q0minors(t, D):
    H = Hf(t, D); q0 = D['q0']
    return np.array([float(np.linalg.det(H[list(rs), :]))
                     for rs in itertools.combinations(range(H.shape[0]), q0)])


def exact_H(t, D):
    WJ = WJ_of_f(t, D['r'], D['k'], D['s'], D['dC'])
    Lred = mm(mm(WJ, D['Ti']), D['MC'])
    return Lred, mm(Lred, D['NCA'])


def exact_A(t, D):
    WJ = WJ_of_f(t, D['r'], D['k'], D['s'], D['dC'])
    return rk(WJ + D['BAT'] + mm(WJ, D['AT'])) == rk(WJ + D['BAT'])


rng = random.Random(11223344)
print("B 实验：情形 II 中是否存在 (A)∧(S)∧rank H < q0 ？")
print()
print(f"{'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'dCA':>4} {'dimT':>4} | "
      f"{'min Σ(q0子式)²':>15} {'rankH<q0':>9} {'(A)':>5} {'(S)':>5}")
print("-" * 78)
n_case = 0
for trial in range(60000):
    if n_case >= 6:
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
        if k < 1 or k > s or k * (s - k) > 2: continue
        if 2 * p + q0 < n: continue
        D = build(Ac, Cc, Lc, Lx)
        if D is None: continue
        if not (D['dCA'] >= q0): continue          # 只要情形 II
        dim = k * (s - k)
        t = [F(0)] * dim
        best = float(np.sum(q0minors([float(x) for x in t], D) ** 2))
        for _s2 in range(400):
            x = np.random.randn(dim) * 2.0
            for _it in range(300):
                f = q0minors(x, D)
                val = float(f @ f)
                if val < 1e-26: break
                J = np.zeros((f.size, dim)); h = 1e-6
                for a in range(dim):
                    xp = x.copy(); xp[a] += h
                    J[:, a] = (q0minors(xp, D) - f) / h
                try:
                    step = np.linalg.lstsq(J, f, rcond=None)[0]
                except Exception:
                    break
                x = x - 0.7 * step
            v = float(q0minors(x, D) @ q0minors(x, D))
            if v < best:
                best = v
        # 精确复核最优候选
        tf = [F(v).limit_denominator(10 ** 5) for v in x]
        _, Hm = exact_H(tf, D)
        rH = rk(Hm) if (Hm and Hm[0]) else 0
        lt = (rH < q0)
        okA = exact_A(tf, D) if lt else None
        okS = None
        if lt and okA:
            Lred, Hm2 = exact_H(tf, D)
            okS = S_holds(Hm2, mm(mm(Lred, Ac), D['NCA']))
        n_case += 1
        print(f"{n:>2} {p:>2} {r:>2} {q0:>3} {D['dCA']:>4} {dim:>4} | "
              f"{best:>15.3e} {str(lt):>9} "
              f"{str(okA) if okA is not None else '-':>5} "
              f"{str(okS) if okS is not None else '-':>5}")
        break

print()
print("判读：")
print("  · 若 min ≈ 0 且 rankH<q0 且 (A)∧(S) 成立 ⟹ 情形 II 中 ν_min = q0 **可能为 YES**（需进一步找算法/证明）")
print("  · 若 min 有正下界（{rankH<q0}=∅）⟹ 情形 II **恒为 NO**，且可多项式认证 ⟹ 该情形可判定")
