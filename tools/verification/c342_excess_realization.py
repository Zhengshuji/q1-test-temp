#!/usr/bin/env python3
"""c342 — 用"反解"造富余档实例：p=2、r=4、n-2-p > k-1。

构造（n=8, p=2）：
  C 的两行取 e1, e2；A 的前两行取 e3, e4。
  则 [C;CA] = [e1;e2;e3;e4]，rank = 4 = r，ker = span{e5..e8} =: K0（k = 4）。
  A 在 K0 上取 B = diag(1,2,3,4)，v = e5 ⟹ Bv = v。
  于是 Av = (0,0,α,β,1,0,0,0) = v + w，w = (0,0,α,β,0,0,0,0) ∈ K0^perp ⟹ v 非特征。

层：ω = k-1 = 3；行空间 V ⊆ U^perp（U = span(v,Av)），dim(V∩K0) = 3。
  取 V = (K0 ∩ v^perp) ⊕ <x>，x ∈ U^perp \\ K0。
  reduced pencil 是 (n-2-p) × (k-1) = 4 × 3 —— **高**矩阵（富余档）。
"""

from __future__ import annotations

import itertools
import os
import random
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
for _p in ("tools/verification",):
    _c = os.path.join(_HERE, "..", "..", _p)
_HERE_ABS = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE_ABS))
if os.path.join(_ROOT, "tools/verification") not in sys.path:
    sys.path.insert(0, os.path.join(_ROOT, "tools/verification"))

import c335_lambda_movement as m  # noqa: E402

lam = sp.symbols("lam")


def gcd_of_minors(P, r):
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


def build(alpha, beta, B):
    n = 8
    C = sp.Matrix([[1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 0, 0]])
    A = sp.zeros(n, n)
    A[0, 2] = 1   # row1 = e3^T
    A[1, 3] = 1   # row2 = e4^T
    # rows 3,4：只取 K0 方向，产生 K0^perp 分量
    A[2, 4] = alpha
    A[3, 4] = beta
    # rows 5..8：K0 上的 B
    for i in range(4):
        for j in range(4):
            A[4 + i, 4 + j] = B[i, j]
    return A, C


def main() -> None:
    print("=" * 74)
    print("反解造富余档：n=8, p=2, r=4, k=4, omega=3, n-2-p=4 > k-1=3")
    print("=" * 74)
    B = sp.diag(1, 2, 3, 4)
    A, C = build(sp.Integer(2), sp.Integer(3), B)
    W = sp.Matrix.vstack(C, C * A)
    print(f"  rank[C;CA] = {W.rank()} (应为 4)")
    assert W.rank() == 4
    N = m.ker_basis(W)
    print(f"  k = dim K0 = {N.cols} (应为 4)")
    assert N.cols == 4

    v = N * sp.Matrix([1, 0, 0, 0])       # K0 的基里 e5 对应第一列
    print(f"  v = {sp.Matrix(v).T.tolist()}")
    Av = A * v
    print(f"  Av = {sp.Matrix(Av).T.tolist()}")
    U = sp.Matrix.hstack(v, Av)
    print(f"  dim U = {U.rank()} (应为 2 ⟹ v 非特征)")
    assert U.rank() == 2

    # U^perp 与 K0 ∩ v^perp
    Q = m.orth_basis([v, Av])
    print(f"  dim U^perp = {Q.rows}")
    # K0 里的 v^perp：在 K 坐标下解 v·(N a) = 0
    fv = (v.T * N)  # 1 x k
    Kv = sp.Matrix([[fv[0, i] for i in range(4)]])
    ns = Kv.nullspace()
    K0v = sp.Matrix.hstack(*ns)            # k x 3（K 坐标下 K0 ∩ v^perp 的基）
    print(f"  dim(K0 ∩ v^perp) = {K0v.cols} (应为 3)")
    assert K0v.cols == 3

    # 行空间 V = (K0∩v^perp) ⊕ <x>，x ∈ U^perp \ K0
    # 取 x = Q 里与 K0 不共线的方向：把 Q 的行投影到 K0^perp 找非零者
    Nc = sp.Matrix.hstack(*N.T.nullspace()).T if False else None
    # 简化：x 取 U^perp 里 K0 分量外的组合；先试 Q 的每一行
    cands = []
    for i in range(Q.rows):
        x = Q.row(i).T
        if (N.T * x).norm() != 0:          # x 不在 K0 内（投影非零）
            cands.append(x)
    print(f"  U^perp 里不在 K0 的候选方向数：{len(cands)}")

    for idx, x in enumerate(cands[:3]):
        Lrows = [N * K0v[:, j] for j in range(3)] + [x]
        L = sp.Matrix.vstack(*[r.reshape(1, 8) for r in Lrows])
        H = L * N
        if H.rank() != 3:
            print(f"  候选 {idx}: rank H = {H.rank()}（要 3，跳过）")
            continue
        HA = L * A * N
        KH = m.ker_basis(H)
        ok5a = (HA * KH).is_zero_matrix
        P = sp.Matrix(4, 4, lambda i, j: lam * H[i, j] - HA[i, j])
        g = gcd_of_minors(P, 3)
        print(f"  候选 {idx}: rank H = {H.rank()}, (5a) = {ok5a}, gcd(3-子式) = {sp.sstr(g)}")


if __name__ == "__main__":
    main()
