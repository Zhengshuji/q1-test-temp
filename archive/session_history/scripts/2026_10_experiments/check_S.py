# -*- coding: utf-8 -*-
"""
check_S.py —— 对构造出的 (A)∧T5a 实例，补上第三个条件 (S)

步骤：
 (1) 重建实例（A^2=0, C, L0 两行）
 (2) 确认 (A)：rank[LA;L;C;CA] == rank[L;C;CA]
 (3) 解出 Λ, G0, G1：   L·A = Λ·L + G0·C + G1·CA     （L 已知 ⟹ 线性 ✓）
 (4) 由 T2： H = L·N_CA,  F = L·A·N_CA,  且 F = Λ·H ✓
 (5) 由 T5（已机器验证 ✓）：(S) ⟺ im(H) 不含 Λ 的特征向量
     具体检验：对 Λ 的每个（有理）特征值 λ，ker(λI-Λ) ∩ im(H) = {0} ？
"""
import os, io, contextlib, itertools
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    s = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(s, "lib", "exec"), _ns)
mm, ker, rk_lib = _ns["mm"], _ns["ker_basis"], _ns["rk"]

_ns2 = {}
with open(os.path.join(_HERE, "linalg_exact.py"), encoding="utf-8") as fh:
    exec(compile(fh.read(), "lx", "exec"), _ns2)
rk2, se, mm2 = _ns2["rank_exact"], _ns2["solve_exact"], _ns2["matmul"]


def mat(r):
    return [[F(x) for x in q] for q in r]


def hcat(X, Y):
    return [X[i] + Y[i] for i in range(len(X))]


def nullspace(N):
    """N 的零空间基（列向量的列表）"""
    if not N:
        return []
    k = len(N[0])
    r = se(N, [[F(0)] for _ in range(len(N))])
    if r is None:
        return []
    return r[1]


def main():
    print("=== 补上 (S)：对构造出的 (A)∧T5a 实例做检验 ===\n")
    A = mat([[0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]])
    C = mat([[0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 0]])
    CA = mm2(C, A)
    R = C + CA
    B = ker(R)                       # N_CA
    n, p, d = len(A), len(C), len(B[0])
    print("n=%d p=%d d_CA=%d  rank[C;CA]=%d" % (n, p, d, rk2(R)))

    l0 = [F(1), F(0), F(0), F(0), F(0), F(0)]
    l1 = [F(0), F(0), F(0), F(1), F(0), F(0)]
    L = [l0, l1]
    LA = mm2(L, A)
    okA = rk2(LA + L + R) == rk2(L + R)
    print("(A) 成立？", okA)
    H = mm2(L, B)
    print("H = L·N_CA =", [[str(x) for x in r] for r in H], " rank =", rk2(H))
    print("T5a：rank(H) = %d < r = %d ？ %s" % (rk2(H), len(L), rk2(H) < len(L)))

    # (3) 解 Λ (r×r), G0 (r×p), G1 (r×p)： L·A - Λ·L - G0·C - G1·CA = 0
    r = len(L)
    nunk = r * r + r * p + r * p
    rows = []
    for i in range(r):
        for j in range(n):
            row = [F(0)] * nunk
            # Λ·L 的第 (i,j) 项： sum_k Λ[i][k]·L[k][j]
            for k in range(r):
                row[k * r + i] = L[k][j]
            # G0·C
            for k in range(p):
                row[r * r + i * p + k] = C[k][j]
            # G1·CA
            for k in range(p):
                row[r * r + r * p + i * p + k] = CA[k][j]
            rows.append(row)
    rhs = [[LA[i][j]] for i in range(r) for j in range(n)]   # ← 原为 -LA ✗（符号错：会得到 -Λ）
    res = se(rows, rhs)
    if res is None:
        print("\n❌ 解 Λ 失败（(A) 应保证可解；请检查实现）"); return
    y, nsol = res
    print("\nΛ,G0,G1 的解空间维数 =", len(nsol))

    results = []
    for t, sol in enumerate(([y] if any(x != 0 for x in y) else []) + nsol):
        Lam = [[sol[k * r + i] for k in range(r)] for i in range(r)]
        G0 = [[sol[r * r + i * p + k] for k in range(p)] for i in range(r)]
        G1 = [[sol[r * r + r * p + i * p + k] for k in range(p)] for i in range(r)]
        # 验证 F = Λ·H
        Fm = mm2(LA, B)
        FH = mm2(Lam, H)
        consistent = (Fm == FH)
        # (S)：对 Λ 的（有理）特征值 λ，检查 ker(λI-Λ) ∩ im(H) = {0}
        S_ok = True
        eigs = []
        for lam in [F(k) for k in range(-3, 4)] + [F(1, 2), F(-1, 2)]:
            M = [[Lam[i][j] - (lam if i == j else 0) for j in range(r)] for i in range(r)]
            if rk2(M) == r:      # λ 不是特征值
                continue
            kerM = nullspace(M)
            if not kerM:
                continue
            eigs.append(lam)
            # 交：kerM 的向量是否在 im(H) 中？（im(H) 是 H 的列空间）
            # 判 v ∈ im(H)：rk([H | v]) == rk(H)
            for v in kerM:
                col = [[v[i]] for i in range(r)]
                if rk2(hcat(H, col)) == rk2(H):
                    S_ok = False
        results.append((Lam, consistent, S_ok, eigs))
        print("\n--- 解 %d ---" % t)
        print("  Λ =", [[str(x) for x in q] for q in Lam])
        print("  F = Λ·H ？", consistent)
        print("  Λ 的有理特征值：", [str(x) for x in eigs])
        print("  (S) 成立？", S_ok)

    print("\n=== 结论 ===")
    good = [x for x in results if x[1] and x[2]]
    print("满足 F=ΛH 且 (S) 的解数：%d / %d" % (len(good), len(results)))
    if good:
        print("⟹ **该实例同时满足 (A) ∧ T5a ∧ (S)** ✓✓✓")
        print("⟹ **情形 II 平行 可为 YES** ⟹ c6 被否定 ✗")
    else:
        print("⟹ (S) 不成立 ⟹ 该实例不是 YES；c6 暂未被动摇")
    return results


if __name__ == "__main__":
    main()
