#!/usr/bin/env python3
"""c358 — m=2、ω=2：搜索两个可行点，其**中点满秩**，从而否证 CLP 的"闭包线性"形式。

实例（79 号 3k 通用提升，k=3, n=9, p=3）：
  C = [I_3 0 0]，A = [[0,0,I_3],[0,0,0],[0,I_3,0]] ⟹ 每行自由对 (h,g) ∈ C^3 x C^3 任意。
  固定行只有一行：H_0 = [e1]、H_{A,0} = [e1]（协调条件成立）。
  ω = 2：rank H = 2 是**降秩**条件，det H = 0 是一个不可约三次超曲面。

搜索：h1,g1,h2,g2 的条目取 {-1,0,1}，筛出 (5a)+(5b) 成立、rank H = 2 的点；
再找两个点 p,q 使 rank((H_p + H_q)/2) = 3（中点不在 {det H = 0} 里）。
"""

from __future__ import annotations

import itertools
import os
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import c335_lambda_movement as m  # noqa: E402

lam = sp.symbols("lam")
VALS = (-1, 0, 1)


def gcd_minors(P, r):
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


def build():
    k = 3
    n = 3 * k
    C = sp.zeros(3, n)
    for i in range(3):
        C[i, i] = 1
    A = sp.zeros(n, n)
    A[0:3, 6:9] = sp.eye(3)
    A[6:9, 3:6] = sp.eye(3)
    L0 = sp.Matrix.hstack(sp.zeros(1, 3), sp.Matrix([[1, 0, 0]]), sp.Matrix([[1, 0, 0]]))
    return k, C, A, L0


def main() -> None:
    print("=" * 74)
    print("m=2, ω=2：找中点满秩的两个可行点")
    print("=" * 74)
    k, C, A, L0 = build()
    Wm = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(Wm)
    AN = A * N
    assert N.cols == k and sp.Matrix.hstack(N, AN).rank() == 2 * k
    H0 = L0 * N
    HA0 = L0 * AN

    feas = []
    vecs = [sp.Matrix([[v for v in c]]) for c in itertools.product(VALS, repeat=k)]
    vecs = [v for v in vecs if v.rank() == 1]          # 非零行
    for h1 in vecs:
        for g1 in vecs:
            for h2 in vecs:
                for g2 in vecs:
                    H = sp.Matrix.vstack(H0, h1, h2)
                    if H.rank() != 2:
                        continue
                    HA = sp.Matrix.vstack(HA0, g1, g2)
                    if not (HA * m.ker_basis(H)).is_zero_matrix:
                        continue
                    gg = gcd_minors(sp.Matrix(H.rows, k, lambda i, j: lam * H[i, j] - HA[i, j]), 2)
                    if gg != 1:
                        continue
                    feas.append((h1, g1, h2, g2, H, HA))
                    if len(feas) >= 300:
                        break
                if len(feas) >= 300:
                    break
            if len(feas) >= 300:
                break
        if len(feas) >= 300:
            break
    print(f"  可行点（ω=2、条目 ∈ {{-1,0,1}}）找到 {len(feas)} 个")
    assert len(feas) >= 2

    # 找中点满秩的一对
    hit = None
    for a in range(len(feas)):
        for b in range(a + 1, len(feas)):
            Hm = (feas[a][4] + feas[b][4]) / 2
            if Hm.rank() == 3:
                hit = (a, b)
                break
        if hit:
            break
    assert hit is not None, "没找到中点满秩的一对"
    a, b = hit
    Ha, HAb = feas[a][4], feas[a][5]
    Hb, HBb = feas[b][4], feas[b][5]
    Hm = (Ha + Hb) / 2
    print(f"  找到一对：p = #{a}、q = #{b}")
    print(f"    H_p = {Ha.tolist()}")
    print(f"    (H_A)_p = {HAb.tolist()}")
    print(f"    H_q = {Hb.tolist()}")
    print(f"    (H_A)_q = {HBb.tolist()}")
    for tag, Hx, HAx in [("p", Ha, HAb), ("q", Hb, HBb)]:
        P = sp.Matrix(Hx.rows, k, lambda i, j: lam * Hx[i, j] - HAx[i, j])
        ms = []
        for rows in itertools.combinations(range(P.rows), 2):
            for cols in itertools.combinations(range(k), 2):
                d = sp.expand(P.extract(list(rows), list(cols)).det())
                if sp.simplify(d) != 0:
                    ms.append(d)
        g = ms[0]
        for d in ms[1:]:
            g = sp.gcd(g, d)
        print(f"    {tag}: 非零极大子式 = {[sp.sstr(x) for x in ms]}, gcd = {sp.sstr(sp.Poly(g, lam).monic().as_expr())}")
    print(f"    det H_p = {sp.sstr(Ha.det())}, det H_q = {sp.sstr(Hb.det())}")
    print(f"    中点 H_m 的 det = {sp.sstr(sp.expand(Hm.det()))}（≠0 ⟹ rank 3）")
    assert Ha.det() == 0 and Hb.det() == 0 and Hm.det() != 0
    print()
    print("  结论：两个可行点满足 det H = 0，它们的中点 det ≠ 0。")
    print("  任何同时含 p、q 的线性空间必含中点，故不可能整体落在 {det H = 0} 内。")
    print("  ⟹ **CLP 的“可行集闭包是一个线性空间”形式为假**（分量级别的问题另论）。")


if __name__ == "__main__":
    main()
