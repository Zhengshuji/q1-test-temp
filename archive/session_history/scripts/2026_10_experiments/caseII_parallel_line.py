# -*- coding: utf-8 -*-
"""
情形 II 平行（k=1）：沿 ℓ 的直线搜索 (A)∧T5a 相容点

ℓ(t) = ℓ* + t·ℓ1  （ℓ* 来自 p1 的解；ℓ1 取若干方向）
对每个 (方向, t)：
   解 (A)+T5a 线性系统 ⟹ 若可解，构造 w ⟹ **精确验证** (A) ∧ 秩降 ∧ (S)
一旦某个点通过 ⟹ 情形 II 平行 ⟹ YES（正向结果，成功即严格 ✓）
"""
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\exact_count_thm7.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random")[0]
exec(head)

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


def solve_for_ell(Ac, Cc, Lc, ell, with_T5a=True):
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
    if with_T5a:
        for i in range(d):
            for j in range(i + 1, d):
                row = [F(0)] * nv
                for t in range(n):
                    row[t] += N[t][i] * pf[j] - N[t][j] * pf[i]
                rows.append(row); rhs.append([F(0)])
    return solve(rows, rhs), (n, r, k, q0, d, N, W)


rng = random.Random(314159)
print("情形 II 平行：沿 ℓ 的直线搜索 (A)∧T5a 相容点")
print()
print(f"{'#':>2} {'q0':>3} {'d_CA':>4} | {'方向数':>6} {'t 数':>5} {'相容点':>7} "
      f"{'(A)精确':>8} {'秩降':>5} {'(S)':>6} | {'结论':>20}")
print("-" * 92)
shown = 0
found_any = 0
for t0 in range(400000):
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
    if rk([pL0, pL0A]) != 1: continue
    Lam = extract_Lambda(Ac, Cc, Lx)
    if Lam is None: continue
    ell0 = [[Lam[i][r]] for i in range(q0)]
    hit = None
    dirs = 0; ts = 0
    for dvec in range(6):
        e = [F(rng.randint(-2, 2)) for _ in range(q0)]
        if all(v == 0 for v in e): continue
        dirs += 1
        for tt in [F(a, b) for b in (1, 2, 3) for a in range(-6, 7)]:
            ts += 1
            ell = [[ell0[i][0] + tt * e[i]] for i in range(q0)]
            res, meta = solve_for_ell(Ac, Cc, Lc, ell)
            if res is None: continue
            n_, r_, k_, q0_, d_, N_, W_ = meta
            for cand in [res[0]] + list(res[1])[:30]:
                w = [cand[j] for j in range(n_)]
                if all(v == 0 for v in w): continue
                Ln = [row[:] for row in Lc] + [w]
                if rk(MM(Ln, Ac) + Ln + W_) != rk(Ln + W_): continue
                H = MM(Ln, N_)
                if rk(H) >= q0_: continue
                Fm = MM(MM(Ln, Ac), N_)
                if S_holds(H, Fm):
                    hit = (w, H, Fm)
                    break
            if hit: break
        if hit: break
    shown += 1
    if hit: found_any += 1
    print(f"{shown:>2} {q0:>3} {dCA:>4} | {dirs:>6} {ts:>5} "
          f"{('是' if hit else '否'):>7} "
          f"{('通过' if hit else '—'):>8} {('是' if hit else '—'):>5} "
          f"{('True' if hit else '—'):>6} | "
          f"{('**情形 II 平行 ⟹ YES**' if hit else '未找到'):>20}")

print()
print(f"=== 找到 (A)∧秩降∧(S) 见证的实例数：{found_any} / {shown} ===")
print()
print("判读：")
print("  · 找到 ⟹ 情形 II 平行可为 YES（正向结果，已精确验证 ⟹ 严格）")
print("  · 未找到 ⟹ 需换方向/更系统地插值 ℓ（下一步）")
