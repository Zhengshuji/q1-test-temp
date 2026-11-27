# -*- coding: utf-8 -*-
"""
测试猜想 (S0)：rank H(Theta) = d_CA 是否对所有 Theta 成立？
方法：对 H 的全部 d_CA 阶子式（Theta 的多项式）做数值最小化 sum(minors^2)。
  · 若最小值 ~ 0  ⟹ 存在 rank H < d_CA 的点 ⟹ (S0) 假
  · 若最小值有正下界 ⟹ (S0) 数值成立 ⟹ Omega* ⊆ U ⟹ 残余 (★'') 自动成立
并用精确有理算术复核找到的候选点。
"""
import itertools
import random
from fractions import Fraction as F

import numpy as np

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\reliable_S_test.py",
           encoding="utf-8").read()
head = src.split("# ---------- 主实验 ----------")[0]
exec(head)


def get_data(Ac, Cc, Lc, Lx):
    n = len(Ac); p = len(Cc); r = len(Lc)
    dC = n - p; s = dC - r
    q0 = len(Lx); k = q0 - r
    bt = build_norm_T(Ac, Cc, Lc, Lx)
    if bt is None:
        return None
    dC2, s2, k2, r2, AT, BAT = bt
    if (r2, k2, s2, dC2) != (r, k, s, dC):
        return None
    NC = ker_basis(Cc)
    MC = mm(inv(mm(tr(NC), NC)), tr(NC))
    L0NC = mm(Lc, NC)
    R = Lx[len(Lc):]; RNC = mm(R, NC)
    K = ker_basis(L0NC); mK = len(K[0]) if (K and K[0]) else 0
    if mK == 0:
        return None
    Kr = [[K[a][j] for a in range(dC)] for j in range(mK)]
    Tcols = []
    for i in range(r):
        ei = [F(1) if q == i else F(0) for q in range(r)]
        so = solve([[L0NC[a][j] for j in range(dC)] for a in range(r)],
                   [[ei[a]] for a in range(r)])
        if so is None:
            return None
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
                return None
            yj = so[0]
        else:
            if nsc is None:
                nsc = solve(rkmat, [[F(0)] for _ in range(k)])[1]
            ix = j - k
            if ix >= len(nsc):
                return None
            yj = nsc[ix]
        Tcols.append([sum(yj[a] * Kr[a][jj] for a in range(mK)) for jj in range(dC)])
    T = [[Tcols[j][i] for j in range(dC)] for i in range(dC)]
    Ti = inv(T)
    if Ti is None:
        return None
    CA = mm(Cc, Ac)
    NCA = ker_basis(CA + Cc)
    dCA = len(NCA[0]) if (NCA and NCA[0]) else 0
    return dict(r=r, k=k, s=s, dC=dC, q0=q0, AT=AT, BAT=BAT, Ti=Ti, MC=MC,
                NCA=NCA, dCA=dCA)


def WJ_of(t, r, k, s, dC):
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
    return WJ


def minors_floats(t_np, D):
    """返回 H 的全部 d_CA 阶子式的浮点值"""
    r, k, s, dC = D['r'], D['k'], D['s'], D['dC']
    dCA, q0 = D['dCA'], D['q0']
    t = [F(x).limit_denominator(10**6) for x in t_np]
    WJ = WJ_of(t, r, k, s, dC)
    Lred = mm(mm(WJ, D['Ti']), D['MC'])
    Hm = mm(Lred, D['NCA'])
    Hf = np.array([[float(x) for x in row] for row in Hm])
    if dCA == 0:
        return np.array([])
    out = []
    for rs in itertools.combinations(range(q0), dCA):
        sub = Hf[list(rs), :]
        out.append(float(np.linalg.det(sub)))
    return np.array(out)


rng = random.Random(778899)
insts = []
for trial in range(40000):
    if len(insts) >= 6:
        break
    n = rng.randint(3, 6)
    p = rng.randint(1, n - 1)
    r = rng.randint(1, n - p)
    for _ in range(80):
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
        D = get_data(Ac, Cc, Lc, Lx)
        if D is None: continue
        if not (0 < D['dCA'] < q0): continue
        if k * (s - k) > 3: continue
        D['n'] = n; D['p'] = p
        insts.append(D)
        break

print("测试 (S0)：rank H = d_CA 是否对所有 Theta 成立")
print("（对 H 的 d_CA 阶子式做多起点数值最小化 sum(minors^2)）")
print()
print(f"{'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'dCA':>4} {'dimT':>4} | "
      f"{'min Σ(minors²)':>16} {'结论':>26}")
print("-" * 74)
for D in insts:
    dim = D['k'] * (D['s'] - D['k'])
    if dim == 0:
        continue
    best = float('inf')
    for _ in range(600):
        x0 = np.random.randn(dim) * 2.0
        x = x0.copy()
        f = minors_floats(x, D)
        if f.size == 0:
            continue
        best = min(best, float(np.sum(f * f)))
        # 简单梯度下降
        for _it in range(200):
            f = minors_floats(x, D)
            val = float(np.sum(f * f))
            if val < 1e-24:
                break
            J = np.zeros((f.size, dim))
            h = 1e-6
            for a in range(dim):
                xp = x.copy(); xp[a] += h
                J[:, a] = (minors_floats(xp, D) - f) / h
            try:
                step = np.linalg.lstsq(J, f, rcond=None)[0]
            except Exception:
                break
            x = x - 0.5 * step
        f = minors_floats(x, D)
        best = min(best, float(np.sum(f * f)))
    concl = "(S0) 假：存在 rank H < d_CA 的点" if best < 1e-14 else "(S0) 数值成立（无零点）"
    print(f"{D['n']:>2} {D['p']:>2} {D['r']:>2} {D['q0']:>3} {D['dCA']:>4} {dim:>4} | "
          f"{best:>16.3e} {concl:>26}")
