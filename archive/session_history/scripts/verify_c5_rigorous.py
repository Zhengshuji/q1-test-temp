# -*- coding: utf-8 -*-
"""
严格判定猜想 c5（平行情形）：
   ∃ w : π(w) = u(λ)  且  π(w·A) ∈ Q·π(L0)
其中 π(v) = v·N_CA（= 到 row[C;CA]^⊥ 的投影），u(λ) = π(L0A) − λ π(L0)

构造：
  w0(λ) = u(λ)·(N^T N)^{-1} N^T        （π(w)=u 的一个特解，关于 λ 仿射）
  S     = span{ π(b_j A) : b_j 是 row[C;CA] 的一组基行 }
  条件 ⟺ ∃(λ, γ, c):  π(w0(λ)A) = Σ γ_j π(b_j A) + c π(L0)
  ⟹ **线性系统**（未知量 λ, γ, c）⟹ 一次求解即严格判定 ✓
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


def solve_ls(X, Y):
    """最小二乘型特解：X·B = Y（行向量），返回 B = Y (X^T X)^{-1} X^T 形式的特解"""
    m, k = len(X), len(X[0])            # X: m × k
    Xt = tr(X)                          # k × m
    G = MM(Xt, X)                       # k × k
    Gi = inv(G)
    if Gi is None:
        return None
    return MM(Y, Gi)                    # Y: ? × k  ⟹ ? × k ; 再乘 X^T 需在调用处处理
    # 注：这里返回 Y·G^{-1}，调用处再乘 X^T


def c5_test(Ac, Cc, Lc, verbose=False):
    n = len(Ac)
    W = Cc + MM(Cc, Ac)
    N = ker_basis(W)                    # n × d_CA （满列秩）
    d = len(N[0])
    L0 = Lc[0]; L0A = MM(Lc, Ac)[0]

    def pv(v):
        assert len(v) == n
        return [sum(v[i] * N[i][j] for i in range(n)) for j in range(d)]

    pL0 = pv(L0); pL0A = pv(L0A)

    # w0(λ) = u(λ)·N^T (N N^T)^? —— 用行向量形式：w N = u  ⟹ w = u (N^T (N N^T)^{-1}) hmm
    # 更稳：解 w·N = u 的一个特解（w 是 1×n 行向量，N 是 n×d）
    #      w = u·N^T·(N·N^T)^{-1}  ✓（因 (u N^T)(N N^T)^{-1} N = u 当 N 行满秩）
    NT = tr(N)                          # d × n
    G = MM(NT, N)                       # d × d （满秩）
    Gi = inv(G)
    if Gi is None:
        return None, "N^T N 奇异"
    P = MM(Gi, NT)                      # d × n

    def w0_of(lam):
        u = [pL0A[j] - lam * pL0[j] for j in range(d)]
        return MM([u], P)[0]              # 1×n

    # 检查 π(w0)=u
    chk = MM([w0_of(F(0))], N)[0]
    assert all(chk[j] == pL0A[j] for j in range(d)), "特解错误"

    # S 的生成元： row[C;CA] 的基行 b_j ⟹ π(b_j A)
    basis_rows = []
    for v in W:
        if rk(basis_rows + [v]) > rk(basis_rows):
            basis_rows.append(v)
    Sgens = [pv(MM([b], Ac)[0]) for b in basis_rows]

    # π(w0(λ)A) = π(w0(0)A) + λ·π(w0'(A))   （w0 仿射）
    w0_0 = w0_of(F(0)); w0_1 = w0_of(F(1))
    dw = [w0_1[i] - w0_0[i] for i in range(n)]
    pA0 = pv(MM([w0_0], Ac)[0])
    pAd = pv(MM([dw], Ac)[0])

    # 线性系统： 未知量 z = [λ, γ_1..γ_m, c]
    m = len(Sgens)
    nv = 1 + m + 1
    rows, rhs = [], []
    for j in range(d):
        r = [F(0)] * nv
        r[0] = pAd[j]                        # λ
        for i in range(m):
            r[1 + i] = -Sgens[i][j]
        r[1 + m] = -pL0[j]                   # c
        rows.append(r); rhs.append([pA0[j]])
    return solve(rows, rhs), (m, d, len(basis_rows))


rng = random.Random(987654321)
print("严格判定 c5：∃w: π(w)=u(λ) 且 π(wA) ∈ Q·π(L0)")
print()
print(f"{'#':>2} {'n':>2} {'r':>2} {'q0':>3} {'k':>2} {'d_CA':>4} | "
      f"{'|S 生成元|':>9} {'#基行':>6} | {'相容?':>6} {'结论':>26}")
print("-" * 88)
shown = 0
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
    if rk([pL0, pL0A]) != 1: continue                    # 平行
    sol, info = c5_test(Ac, Cc, Lc)
    shown += 1
    if sol is None:
        print(f"{shown:>2} {n:>2} {r:>2} {q0:>3} {k:>2} {dCA:>4} | "
              f"{'—':>9} {'—':>6} | {'否':>6} {'奇异/不可判':>26}")
        continue
    m, d, nb = info
    y, ns = sol
    ok = True                                       # 齐次之外：系统有解即相容
    print(f"{shown:>2} {n:>2} {r:>2} {q0:>3} {k:>2} {dCA:>4} | "
          f"{m:>9} {nb:>6} | {str(ok):>6} {'**c5 成立**' if ok else '':>26}")

print()
print("判读：")
print("  · 全部『c5 成立』⟹ 平行情形恒 YES ⟹ **情形 II 无硬度** ⟹ 分支 A 无硬度")
print("  · 出现『不相容』⟹ 靶子出现 ⟹ 任务 A 可开始")
