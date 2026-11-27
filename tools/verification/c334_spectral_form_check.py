#!/usr/bin/env python3
"""c334 — 326 谱形式引理的实例核对（$n=5,p=1,r_0=1,q=3$，超平面层 $k=3,\\omega=2$）。

要核对的三件事：
  (1) 秩记账：$\\omega=\\dim(V\\cap K_0)$、$V\\subseteq U^\\perp$、层条件 $\\omega=k-1$；
      **非特征 $v$**（$\\dim U=2$）时是否 $V=U^\\perp$；**特征 $v$**（$\\dim U=1$）时是否 $V\\subsetneq U^\\perp$。
  (2) 326 的引理：坏 $\\iff\\exists\\lambda:\\operatorname{rank}M(\\lambda)\\le k-2$，
      其中 $M(\\lambda)=Q(\\lambda I-A)N$、$Q$ 是 $U^\\perp$ 的基；与"$\\lambda H-H_A$ 的 $2$-子式 gcd $\\ne1$"对照。
  (3) $\\Lambda(v)$ 是否随 $v$ 移动（三分的第 2/3 类是否出现）。

有限精确检验，不是证明。
"""

from __future__ import annotations

import itertools
import os
import random
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
lam = sp.symbols("lam")


def orth_basis(vectors, n):
    """返回 U^perp 的一组整数/有理基（行向量），U = span(vectors)。"""
    U = sp.Matrix.hstack(*[sp.Matrix(v) for v in vectors])
    ns = U.T.nullspace()          # {x : U^T x = 0} = U^perp
    assert ns, "U 应真子空间"
    return sp.Matrix.hstack(*ns).T  # 行 = 基


def ker_basis(M):
    ns = sp.Matrix(M).nullspace()
    return sp.Matrix.hstack(*ns) if ns else sp.zeros(M.cols, 0)


def gcd_of_minors(P, r):
    """P 为 lambda 的多项式矩阵（sympy），取全部 r x r 子式的 gcd。"""
    P = sp.Matrix(P)
    ms = []
    for rows in itertools.combinations(range(P.rows), r):
        for cols in itertools.combinations(range(P.cols), r):
            d = sp.expand(P.extract(list(rows), list(cols)).det())
            if sp.simplify(d) != 0:
                ms.append(d)
    if not ms:
        return sp.Integer(0)
    g = ms[0]
    for d in ms[1:]:
        g = sp.gcd(g, d)
    return sp.Poly(g, lam).monic().as_expr()


def build(A, C, L0, R, N):
    """由 (A,C,L0,R,N) 给出 H, H_A 与若干诊断量。"""
    n = A.rows
    L = sp.Matrix.vstack(sp.Matrix(L0), sp.Matrix(R))
    H = L * N
    HA = L * A * N
    return L, H, HA


def study(A, C, L0, R, N, label):
    n = A.rows
    L, H, HA = build(A, C, L0, R, N)
    k = N.cols
    om = H.rank()
    kH = k - om                     # dim ker H
    ok_5a = (HA.row_join(H)).rank() == H.rank() or (H.col_join(HA)).rank() == H.rank()
    # 用零空间判 (5a): ker H ⊆ ker H_A
    KH = ker_basis(H)
    ok_5a = all((HA * KH).is_zero_matrix for _ in [0]) if KH.cols else True
    ok_5a = (HA * KH).is_zero_matrix
    # 坏性：2-子式 gcd
    P = sp.Matrix(H.rows, H.cols, lambda i, j: lam * H[i, j] - HA[i, j])
    g = gcd_of_minors(P, 2)
    bad_gcd = sp.Poly(g, lam).degree() > 0
    print(f"  [{label}] rankH={om} (k={k}), dim ker H={kH}, (5a)={ok_5a}, "
          f"gcd(2-子式)={sp.sstr(g)}, bad={bad_gcd}")
    return dict(L=L, H=H, HA=HA, om=om, g=g, bad=bad_gcd, ok_5a=ok_5a)


def lemma_side(A, N, U, k):
    """条件: exists lam, rank M(lam) <= k-2, M(lam) = Q(lam I - A) N，Q 为 U^perp 的基。"""
    n = A.rows
    Q = orth_basis(U, n)
    P1 = Q * N
    P0 = -Q * A * N
    M = sp.Matrix(P1.rows, P1.cols, lambda i, j: lam * P1[i, j] + P0[i, j])
    g = gcd_of_minors(M, k - 1)
    return dict(Q=Q, M=M, g=g, holds=(0 if g == 0 else sp.Poly(g, lam).degree() > 0))


def main() -> None:
    print("=" * 74)
    print("实例构造：n=5, p=1, C=e5^T；要求 rank[C;CA]=2 ⟹ k=3（超平面层 ω=2）")
    print("=" * 74)

    # ---------- 情形 A：非特征 v（dim U = 2） ----------
    A = sp.Matrix([[0, 1, 0, 0, 0],
                   [0, 0, 1, 0, 0],
                   [0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1],
                   [1, 2, 3, 5, 7]])          # 任意整数矩阵；row5 不平行 e5
    C = sp.Matrix([[0, 0, 0, 0, 1]])
    W = sp.Matrix.vstack(C, C * A)
    print(f"  rank[C;CA] = {W.rank()}")
    assert W.rank() == 2
    K0 = ker_basis(W)
    N = K0
    k = N.cols
    print(f"  k = dim K0 = {k}")

    # 取 v ∈ K0（非特征：Av ∉ K0）
    v = N * sp.Matrix([1, 0, 0])
    U = [v, A * v]
    Umat = sp.Matrix.hstack(*U)
    print(f"  v = {sp.Matrix(v).T.tolist()}, Av = {sp.Matrix(A*v).T.tolist()}, dim U = {Umat.rank()}")
    assert Umat.rank() == 2

    # L0：U^perp 里的一般一行
    Q = orth_basis(U, 5)
    assert Q.rows == 5 - Umat.rank()
    L0 = Q.row(0)
    # 自由行：U^perp 里的一般两行
    R = sp.Matrix([[Q[i, j] + Q[i + 1, j] for j in range(5)] for i in range(2)])
    study(A, C, L0, R, N, "A: 非特征 v")

    # 检查 V = U^perp ?
    L, H, HA = build(A, C, L0, R, N)
    V = L
    print(f"  dim row L = {V.rank()}, dim U^perp = {Q.rows}, "
          f"row L ⊆ U^perp? {all((V * sp.Matrix(u)).is_zero_matrix for u in U)}")

    # 引理侧
    res = lemma_side(A, N, U, k)
    print(f"  引理侧: gcd((k-1)-子式 of M(lam)) = {sp.sstr(res['g'])}, "
          f"条件成立 = {res['holds']}")

    # ---- 多个随机 R：验证「引理 ⟺ 坏」（V = U^perp 时）----
    print()
    print("  多个随机 R（row L 仍张满 U^perp）：")
    rng = random.Random(7)
    agree = 0
    for t in range(4):
        coef = sp.Matrix([[rng.randint(-2, 2) for _ in range(Q.rows)] for _ in range(2)])
        R_t = coef * Q
        if (sp.Matrix.vstack(sp.Matrix(L0), R_t)).rank() < 3:
            continue
        st = study(A, C, L0, R_t, N, f"A.R{t}")
        ls = lemma_side(A, N, U, k)
        if st["bad"] == ls["holds"]:
            agree += 1
        else:
            print(f"    !! 不一致: bad={st['bad']} lemma={ls['holds']}")
    print(f"    {agree} 个一致（引理与 gcd 判定同进同出）")

    # ---- 退化的 R：两行相同（取 Q 的第二行）⟹ V ⊊ U^perp，此时引理只应给「充分」----
    Rd = sp.Matrix.vstack(Q.row(1), Q.row(1))
    Ld = sp.Matrix.vstack(sp.Matrix(L0), Rd)
    print(f"  退化 R（两行相同，取 Q.row(1)）：dim row L = {Ld.rank()} < dim U^perp = {Q.rows}")
    std = study(A, C, Ld, Rd, N, "A.Rdeg")
    lsd = lemma_side(A, N, U, k)
    print(f"    引理侧条件 = {lsd['holds']}，gcd 判定 bad = {std['bad']} "
          f"（充分方向要求：条件 True ⟹ bad True）")
    assert std["om"] == k - 1, "这个点应仍在超平面层（rank H = k-1）"
    assert std["ok_5a"], "这个点应满足 (5a)"
    if lsd["holds"]:
        assert std["bad"], "充分方向失败！"
        print("    充分方向成立 ✓")

    # ---------- 情形 B：特征 v（dim U = 1） ----------
    print()
    print("-" * 74)
    print("情形 B：让 v = e1 是 A 的特征向量（A e1 = 2 e1），且 e1 ∈ K0")
    A2 = sp.Matrix([[2, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1],
                    [0, 3, 5, 7, 11]])       # row5 的第一列为 0 ⟹ CA e1 = 0
    W2 = sp.Matrix.vstack(C, C * A2)
    print(f"  rank[C;CA] = {W2.rank()}")
    assert W2.rank() == 2
    N2 = ker_basis(W2)
    k2 = N2.cols
    print(f"  k = {k2}")
    v2 = sp.Matrix([1, 0, 0, 0, 0])
    assert (W2 * v2).is_zero_matrix, "e1 应在 K0 内"
    assert (A2 * v2 - 2 * v2).is_zero_matrix, "e1 应是 A 的特征向量"
    U2 = [v2]
    Q2 = orth_basis(U2, 5)
    print(f"  dim U = 1, dim U^perp = {Q2.rows}")
    L0b = Q2.row(0)
    Rb = sp.Matrix([[Q2[i, j] + Q2[i + 1, j] for j in range(5)] for i in range(2)])
    study(A2, C, L0b, Rb, N2, "B: 特征 v")
    resb = lemma_side(A2, N2, U2, k2)
    print(f"  引理侧: gcd = {sp.sstr(resb['g'])}, 条件成立 = {resb['holds']}")
    Lb, Hb, HAb = build(A2, C, L0b, Rb, N2)
    print(f"  dim row L = {Lb.rank()}, dim U^perp = {Q2.rows}")


if __name__ == "__main__":
    main()
