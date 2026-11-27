# -*- coding: utf-8 -*-
"""
c5 的独立复核：从线性系统的解构造 w，**精确**检验 (A) ∧ 秩降 ∧ (S)

构造：解 z=(λ, γ_1..γ_m, c) ⟹ w = w0(λ) + Σ γ_j b_j
  应满足 π(w)=u(λ) 且 π(wA)=c π(L0)
  ⟹ (I) π(L0A) − λ π(L0) = π(w)          ✓（λ12=1）
  ⟹ (II) π(wA) = λ21 π(L0) + λ22 u        ✓（取 λ21=c, λ22=0，因 u∥π(L0)）
  ⟹ (A) ✓
最后用**原始 4 块秩等式**独立验证 (A)
"""
import random
from fractions import Fraction as F

srcS = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\reliable_S_test.py",
            encoding="utf-8").read()
headS = srcS.split("# ---------- 主实验 ----------")[0]
exec(headS)


def MM(X, Y):
    assert X and Y and len(X[0]) == len(Y), f"维数错配 {len(X)}x{len(X[0])} 乘 {len(Y)}x{len(Y[0])}"
    return mm(X, Y)


def matpow(M, k):
    n = len(M)
    R = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = MM(R, M)
    return R


def construct_w(Ac, Cc, Lc):
    """返回 (w, λ, c) 或 None"""
    n = len(Ac)
    W = Cc + MM(Cc, Ac)
    N = ker_basis(W)
    d = len(N[0])
    L0 = Lc[0]; L0A = MM(Lc, Ac)[0]

    def pv(v):
        assert len(v) == n
        return [sum(v[i] * N[i][j] for i in range(n)) for j in range(d)]

    pL0, pL0A = pv(L0), pv(L0A)
    NT = tr(N)                       # d × n
    G = MM(NT, N)                    # d × d
    Gi = inv(G)
    if Gi is None:
        return None
    P = MM(Gi, NT)                   # d × n

    def w0_of(lam):
        u = [pL0A[j] - lam * pL0[j] for j in range(d)]
        return MM([u], P)[0]

    basis_rows = []
    for v in W:
        if rk(basis_rows + [v]) > rk(basis_rows):
            basis_rows.append(v)
    Sgens = [pv(MM([b], Ac)[0]) for b in basis_rows]
    m = len(Sgens)
    w0_0, w0_1 = w0_of(F(0)), w0_of(F(1))
    dw = [w0_1[i] - w0_0[i] for i in range(n)]
    pA0 = pv(MM([w0_0], Ac)[0])
    pAd = pv(MM([dw], Ac)[0])

    nv = 1 + m + 1
    rows, rhs = [], []
    for j in range(d):
        # 正确方程： Σ γ_i s_i + λ pAd − c pL0 = −pA0
        r = [F(0)] * nv
        r[0] = pAd[j]
        for i in range(m):
            r[1 + i] = Sgens[i][j]
        r[1 + m] = -pL0[j]
        rows.append(r); rhs.append([-pA0[j]])
    sol = solve(rows, rhs)
    if sol is None:
        return None
    z = sol[0]
    lam, gammas, c = z[0], z[1:1 + m], z[1 + m]
    w0 = w0_of(lam)
    w = w0[:]
    for i in range(m):
        for a in range(n):
            w[a] += gammas[i] * basis_rows[i][a]
    return w, lam, c


rng = random.Random(24680246)
print("c5 独立复核：构造 w ⟹ 精确检验 (A) ∧ 秩降 ∧ (S)")
print()
print(f"{'#':>2} {'n':>2} {'r':>2} {'q0':>3} {'k':>2} {'d_CA':>4} | "
      f"{'构造':>5} {'(A) 精确':>8} {'秩降':>5} {'(S)':>7} | {'结论':>22}")
print("-" * 88)
shown = 0
yes = 0
for t in range(300000):
    if shown >= 8:
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
    W = Cc + MM(Cc, Ac)
    dCA = n - rk(W)
    if dCA < q0: continue
    NCA = ker_basis(W)
    L0 = Lc[0]; L0A = MM(Lc, Ac)[0]
    pL0 = [sum(L0[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]
    pL0A = [sum(L0A[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]
    if rk([pL0, pL0A]) != 1: continue                 # 平行
    res = construct_w(Ac, Cc, Lc)
    shown += 1
    if res is None:
        print(f"{shown:>2} {n:>2} {r:>2} {q0:>3} {k:>2} {dCA:>4} | "
              f"{'否':>5} {'—':>8} {'—':>5} {'—':>7} | {'不可构造':>22}")
        continue
    w, lam, c = res
    Ln = Lc + [w]
    # 独立验证：原始 4 块秩等式
    okA = rk(MM(Ln, Ac) + Ln + W) == rk(Ln + W)
    H = MM(Ln, NCA)
    rd = (rk(H) < q0)
    Fm = MM(MM(Ln, Ac), NCA)
    okS = S_holds(H, Fm) if rd else False
    if okA and rd and okS:
        yes += 1
    print(f"{shown:>2} {n:>2} {r:>2} {q0:>3} {k:>2} {dCA:>4} | "
          f"{'是':>5} {str(okA):>8} {str(rd):>5} {str(okS):>7} | "
          f"{('**c5 见证 (YES)**' if (okA and rd and okS) else '有问题'):>22}")

print()
print(f"=== 构造出 (A)∧秩降∧(S) 见证的实例数：{yes} / {shown} ===")
print()
print("判读：")
print("  · 全部 YES ⟹ c5 得到独立验证 ⟹ 平行情形恒 YES ⟹ **情形 II 无硬度**")
print("  · (A) 通过但 (S) 失败 ⟹ c5 的部分成立，需再调整")
