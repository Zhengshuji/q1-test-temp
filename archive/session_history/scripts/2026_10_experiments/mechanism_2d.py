# -*- coding: utf-8 -*-
"""
机制检验（强化版）：情形 II 平行中，是否存在 Λ_{13} ≠ 0 的 (A)∧T5a 解？

ℓ ∈ P^2（q0=3, k=1）：归一化后扫**二维网格**
   ℓ = (1, a, b)  ∪  (0, 1, b)  ∪  (0, 0, 1)
对每个 ℓ：解 (A)+T5a 线性系统；若可解 ⟹ 构造 w ⟹ **精确验证** (A)∧秩降∧(S)
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


def extract_Lambda(Ac, Cc, Lx):
    q0, n, p = len(Lx), len(Ac), len(Cc)
    CA = MM(Cc, Ac); LxA = MM(Lx, Ac)
    nLam = q0 * q0; nG = q0 * p
    nv = nLam + 2 * nG
    rows, rhs = [], []
    for a in range(q0):
        for c in range(n):
            row = [F(0)] * nv
            for j in range(q0):
                row[a * q0 + j] += Lx[j][c]
            for b in range(p):
                row[nLam + a * p + b] += Cc[b][c]
                row[nLam + nG + a * p + b] += CA[b][c]
            rows.append(row); rhs.append([LxA[a][c]])
    sol = solve(rows, rhs)
    if sol is None:
        return None
    x = sol[0]
    return [[x[a * q0 + j] for j in range(q0)] for a in range(q0)]


def solve_for_ell(Ac, Cc, Lc, ell):
    n, r, k = len(Ac), len(Lc), 1
    q0 = r + k
    W = Cc + MM(Cc, Ac); N = ker_basis(W); d = len(N[0])

    def pv(v):
        return [sum(v[i] * N[i][j] for i in range(n)) for j in range(d)]

    L0A = MM(Lc, Ac)
    pL0 = [pv(Lc[i]) for i in range(r)]
    pL0A = [pv(L0A[i]) for i in range(r)]
    pf = pv(Lc[0])
    nR, nL = k * n, q0 * r
    nv = nR + nL
    ANA = MM(Ac, N)
    rows, rhs = [], []
    for i in range(q0):
        base = pL0A[i][:] if i < r else [F(0)] * d
        aR = None if i < r else i - r
        for c in range(d):
            row = [F(0)] * nv
            if aR is not None:
                for t in range(n):
                    row[aR * n + t] += ANA[t][c]
            for j in range(r):
                row[nR + i * r + j] -= pL0[j][c]
            for a in range(k):
                coef = ell[i][a]
                if coef:
                    for t in range(n):
                        row[a * n + t] -= coef * N[t][c]
            rows.append(row); rhs.append([base[c]])
    for i in range(d):                       # T5a
        for j in range(i + 1, d):
            row = [F(0)] * nv
            for t in range(n):
                row[t] += N[t][i] * pf[j] - N[t][j] * pf[i]
            rows.append(row); rhs.append([F(0)])
    return solve(rows, rhs), (n, r, k, q0, d, N, W)


GRID = [F(a, b) for b in (1, 2, 3) for a in range(-4, 5)]

rng = random.Random(556677)
print("机制检验（二维网格）：情形 II 平行，是否存在 Λ13≠0 的 (A)∧T5a 解？")
print()
print(f"{'#':>2} {'q0':>3} {'d_CA':>4} | {'扫过 ℓ 数':>9} {'Λ13≠0 中':>9} {'命中':>5} | "
      f"{'结论':>26}")
print("-" * 78)
shown = 0
hits_total = 0
for t0 in range(400000):
    if shown >= 5:
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
    if k != 1 or q0 != 3: continue
    W = Cc + MM(Cc, Ac); dCA = n - rk(W)
    if dCA < q0: continue
    NCA = ker_basis(W)
    L0 = Lc[0]; L0A = MM(Lc, Ac)[0]
    pL0 = [sum(L0[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]
    pL0A = [sum(L0A[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]
    if rk([pL0, pL0A]) != 1: continue
    # 候选 ℓ（q0=3）：归一化扫网格
    ells = []
    for a in GRID:
        for b in GRID:
            ells.append([[F(1)], [a], [b]])          # Λ13 = 1
    for b in GRID:
        ells.append([[F(0)], [F(1)], [b]])           # Λ13 = 0
    ells.append([[F(0)], [F(0)], [F(1)]])
    n13 = 0; hit = None; tried = 0
    for ell in ells:
        if ell[0][0] != 0:
            n13 += 1
        tried += 1
        res, meta = solve_for_ell(Ac, Cc, Lc, ell)
        if res is None: continue
        n_, r_, k_, q0_, d_, N_, W_ = meta
        for cand in [res[0]] + list(res[1])[:20]:
            w = [cand[j] for j in range(n_)]
            if all(v == 0 for v in w): continue
            Ln = [row[:] for row in Lc] + [w]
            if rk(MM(Ln, Ac) + Ln + W_) != rk(Ln + W_): continue
            H = MM(Ln, N_)
            if rk(H) >= q0_: continue
            Fm = MM(MM(Ln, Ac), N_)
            if S_holds(H, Fm):
                hit = (ell, w); break
        if hit: break
    shown += 1
    if hit: hits_total += 1
    e13 = "1" if hit and hit[0][0][0] != 0 else ("0" if hit else "—")
    print(f"{shown:>2} {q0:>3} {dCA:>4} | {tried:>9} {n13:>9} "
          f"{('是(Λ13=%s)' % e13) if hit else '否':>5} | "
          f"{('**情形 II 平行 ⟹ YES**' if hit else '无命中'):>26}")

print()
print(f"=== 命中实例数：{hits_total} / {shown} ===")
print()
print("判读：")
print("  · 命中且 Λ13≠0 ⟹ 机制『平行 ⟹ Λ13=0』**被否证**")
print("  · 全无命中 ⟹ 机制得到二维网格的强力支持（⟹ c6 支持）")
