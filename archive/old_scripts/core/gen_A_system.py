# -*- coding: utf-8 -*-
"""
通用 (A)-系统构造器（适用于任意 q0 = r + k）

(A) ⟺ ∃Λ ∈ Q^{q0×q0}, G0, G1:  L·A = Λ·L + G0·C + G1·CA      （L = [L0; R]）
投影形式（π = 到 row(C,CA)^⊥ 的投影，π(v) = v·N_CA）：
      ∀i=1..q0 :  π((L·A)_i) = Σ_j Λ_ij π(L_j)

⚠️ 双线性：Λ 的**后 k 列** × R 的未知行
⟹ **固定 Λ 的后 k 列为 ℓ ∈ Q^{q0×k}** ⟹ 系统对 (R, Λ 的前 r 列) **线性** ✓

本文件先实现构造器 + 在 q0=2 上校准（k=1）
"""
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\exact_count_thm7.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random")[0]
exec(head)


def MM(X, Y):
    assert X and Y and len(X[0]) == len(Y), \
        f"维数错配 {len(X)}x{len(X[0])} 乘 {len(Y)}x{len(Y[0])}"
    return mm(X, Y)


def matpow(M, k):
    n = len(M)
    R = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = MM(R, M)
    return R


def build_general(Ac, Cc, Lc, ell):
    """
    构造线性系统  M·x = b
      L = [L0; R]，L0 是 r×n（已知），R 是 k×n（未知）
      ell: q0×k 的固定矩阵（Λ 的后 k 列）
    未知量 x = [ R 的 k·n 个分量 ,  Λ 的前 r 列的 q0·r 个分量 ]
    返回 (rows, rhs, ncols, nmeta)
    """
    n = len(Ac)
    r = len(Lc)
    k = ell[0].__len__() if ell else 0
    q0 = r + k
    assert len(ell) == q0, f"ell 应为 {q0}×{k}"
    W = Cc + MM(Cc, Ac)
    N = ker_basis(W)                 # n × d_CA
    d = len(N[0])

    def pv(v):
        assert len(v) == n
        return [sum(v[i] * N[i][j] for i in range(n)) for j in range(d)]

    L0A = MM(Lc, Ac)                 # r × n
    pL0 = [pv(Lc[i]) for i in range(r)]        # r 个 d 维
    pL0A = [pv(L0A[i]) for i in range(r)]

    nR = k * n                       # R 的未知量
    nL = q0 * r                      # Λ 前 r 列的未知量
    nv = nR + nL

    def idxR(a, j):                  # R[a][j]  （a=0..k-1, j=0..n-1）
        return a * n + j

    def idxL(i, j):                  # Λ[i][j] （i=0..q0-1, j=0..r-1）
        return nR + i * r + j

    rows, rhs = [], []
    # 方程 i=1..q0（每个 d 个坐标）
    for i in range(q0):
        # 左端 π((L·A)_i)
        if i < r:
            lhs_base = pL0A[i][:]                    # 已知
            lhs_R = None
        else:
            lhs_base = [F(0)] * d                    # R[i-r]·A 未知
            lhs_R = i - r
        # 右端 Σ_j Λ_ij π(L_j)
        #   j<r : π(L0)_j 已知，Λ_ij 未知
        #   j>=r: π(R_{j-r}) 未知，Λ_ij = ell[i][j-r] 已知
        for c in range(d):
            row = [F(0)] * nv
            if lhs_R is not None:
                # π((R[a]·A))_c = Σ_t (A·N)[t][c] · R[a][t]
                for t in range(n):
                    row[idxR(lhs_R, t)] += MM(Ac, N)[t][c]
            # 右端：移项到左边（带负号）
            for j in range(r):
                row[idxL(i, j)] -= pL0[j][c]
            for a in range(k):
                coef = ell[i][a]
                if coef == 0:
                    continue
                for t in range(n):
                    row[idxR(a, t)] -= coef * N[t][c]
            rows.append(row)
            rhs.append([lhs_base[c]])
    return rows, rhs, nv, (n, r, k, q0, d, N, W)


def check_A_raw(Ac, Cc, L):
    W = Cc + MM(Cc, Ac)
    return rk(MM(L, Ac) + L + W) == rk(L + W)


if __name__ == "__main__":
    print("通用 (A)-系统构造器：在 q0=2（r=1,k=1）上校准")
    print()
    rng = random.Random(2718281)
    shown = 0
    for t in range(200000):
        if shown >= 5:
            break
        n, p, r, m = 5, 1, 1, 2
        Amat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
        Cmat = [[rng.randint(-2, 2) for _ in range(n)]]
        Ac, Cc = toF(Amat), toF(Cmat)
        if rk(Cc) != p: continue
        Lc = MM(Cc, matpow(Ac, m))
        if rk(Lc) != r: continue
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
        # 用 ell 的网格扫（q0=2 时 ell ∈ P^1，取若干代表）
        hit = None
        for lam12 in (F(1), F(0), F(2), F(1, 2), F(-1), F(3)):
            ell = [[F(0)], [lam12]]            # Λ 的后 k=1 列
            rows, rhs, nv, meta = build_general(Ac, Cc, Lc, ell)
            sol = solve(rows, rhs)
            if sol is None:
                continue
            n_, r_, k_, q0_, d_, N_, W_ = meta
            x = sol[0]
            R = [[x[a * n_ + j] for j in range(n_)] for a in range(k_)]
            Lnew = [row[:] for row in Lc] + R
            if all(all(v == 0 for v in row) for row in R):
                continue                        # 排除零解
            if check_A_raw(Ac, Cc, Lnew):
                hit = (lam12, Lnew)
                break
        shown += 1
        print(f"  #{shown}  q0={q0} k={k} d_CA={n - rk(Cc + MM(Cc, Ac))}: "
              f"{'找到 (A)-解 (λ12=%s)' % hit[0] if hit else '未找到'}")
    print()
    print("判读：q0=2 校准的目的是确认构造器能复现『(A)-可行解存在』这一侧；")
    print("      真正的校准目标是与 attack_chart_rigorous.py 的结论对照。")
