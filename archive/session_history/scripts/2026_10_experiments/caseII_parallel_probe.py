# -*- coding: utf-8 -*-
"""
情形 II 平行（k=1）：是否存在**秩降**的 (A)-可行解？

用已校准的通用构造器（`gen_A_system.py`）+ T5a 的线性条件：
   k=1 时  T5a ⟺ π(w) ∥ π(L0)   ⟺ (d_CA − 1) 个**线性**方程
⟹ 整个系统对 (R, Λ 前 r 列) 仍是**线性**的 ✓ ⟹ 一次求解即严格判定 ✓

ℓ（Λ 的后 k=1 列，q0 维）取自 p1 的解（校准过的 ℓ*）+ 若干变体
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


def extract_Lambda(Ac, Cc, Lx):
    q0, n = len(Lx), len(Ac)
    p = len(Cc)
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


def build_with_T5a(Ac, Cc, Lc, ell):
    """通用构造器 + T5a 线性条件（k=1：π(w) ∥ π(L0)）"""
    n = len(Ac); r = len(Lc); k = 1; q0 = r + k
    W = Cc + MM(Cc, Ac); N = ker_basis(W); d = len(N[0])

    def pv(v):
        return [sum(v[i] * N[i][j] for i in range(n)) for j in range(d)]

    L0A = MM(Lc, Ac)
    pL0 = [pv(Lc[i]) for i in range(r)]
    pL0A = [pv(L0A[i]) for i in range(r)]
    pL0_first = pv(Lc[0])                    # T5a 用它（π(L0) 的第一行）

    nR = k * n; nL = q0 * r
    nv = nR + nL

    def idxR(a, j): return a * n + j
    def idxL(i, j): return nR + i * r + j

    ANA = MM(Ac, N)
    rows, rhs = [], []
    for i in range(q0):
        if i < r:
            base = pL0A[i][:]; aR = None
        else:
            base = [F(0)] * d; aR = i - r
        for c in range(d):
            row = [F(0)] * nv
            if aR is not None:
                for t in range(n):
                    row[idxR(aR, t)] += ANA[t][c]
            for j in range(r):
                row[idxL(i, j)] -= pL0[j][c]
            for a in range(k):
                coef = ell[i][a]
                if coef:
                    for t in range(n):
                        row[idxR(a, t)] -= coef * N[t][c]
            rows.append(row); rhs.append([base[c]])
    # T5a：π(w) ∥ π(L0) ⟹ 对 i<j： π(w)_i pL0_j − π(w)_j pL0_i = 0
    for i in range(d):
        for j in range(i + 1, d):
            row = [F(0)] * nv
            for t in range(n):
                row[idxR(0, t)] += N[t][i] * pL0_first[j] - N[t][j] * pL0_first[i]
            rows.append(row); rhs.append([F(0)])
    return rows, rhs, nv, (n, r, k, q0, d, N, W)


def check_all(Ac, Cc, L):
    W = Cc + MM(Cc, Ac)
    N = ker_basis(W)
    okA = rk(MM(L, Ac) + L + W) == rk(L + W)
    H = MM(L, N)
    rd = rk(H) < len(L)
    return okA, rd


rng = random.Random(112233)
print("情形 II 平行（k=1）：是否存在**秩降**的 (A)-可行解？")
print()
print(f"{'#':>2} {'q0':>3} {'d_CA':>4} | {'ℓ* 前 3 分量':>16} | {'系统可解?':>9} "
      f"{'(A)':>5} {'秩降':>5} | {'结论':>18}")
print("-" * 84)
shown = 0
yes = 0
for t in range(300000):
    if shown >= 6:
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
    W = Cc + MM(Cc, Ac); dCA = n - rk(W)
    if dCA < q0: continue
    NCA = ker_basis(W)
    L0 = Lc[0]; L0A = MM(Lc, Ac)[0]
    pL0 = [sum(L0[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]
    pL0A = [sum(L0A[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]
    if rk([pL0, pL0A]) != 1: continue              # 平行
    Lam = extract_Lambda(Ac, Cc, Lx)
    if Lam is None: continue
    ell = [[Lam[i][r]] for i in range(q0)]         # 后 k=1 列
    rows, rhs, nv, meta = build_with_T5a(Ac, Cc, Lc, ell)
    sol = solve(rows, rhs)
    n_, r_, k_, q0_, d_, N_, W_ = meta
    gotA = gotR = False
    if sol is not None:
        for cand in [sol[0]] + list(sol[1])[:40]:
            R = [cand[j] for j in range(n_)]
            Lnew = [row[:] for row in Lc] + [R]
            if all(v == 0 for v in R): continue
            a_, rd_ = check_all(Ac, Cc, Lnew)
            if a_:
                gotA = True
                if rd_:
                    gotR = True
                    break
    shown += 1
    if gotR: yes += 1
    print(f"{shown:>2} {q0:>3} {dCA:>4} | {str([ell[i][0] for i in range(min(3,q0))]):>16} | "
          f"{str(sol is not None):>9} {str(gotA):>5} {str(gotR):>5} | "
          f"{('**秩降解存在**' if gotR else '无秩降解'):>18}")

print()
print(f"=== 存在秩降的 (A)-可行解：{yes} / {shown} ===")
print()
print("判读：")
print("  · 有 ⟹ 情形 II 平行 → YES 的可能（需再查 (S)）")
print("  · 全无 ⟹ 在 ℓ* 这一支上无秩降 ⟹ 需扫/插值 ℓ（下一步）")
