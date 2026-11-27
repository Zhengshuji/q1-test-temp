#!/usr/bin/env python3
"""c357 — 单自由行（m=1）的候选线性原理：位移脚手架上的精确核对。

实例（79 号 3k 通用提升，k=3, n=9, p=3）：
  C = [I_3 0 0]，A = [[0,0,I_3],[0,0,0],[0,I_3,0]]，
  K_0 = V，N = [0;I_3;0]，A N = [0;0;I_3]，[N AN] 满秩 6 ⟹ 自由对 (h,g) ∈ C^3 x C^3 任意。

固定部分取**位移脚手架**（r0 = 3）：
  H_0 = [v1; v2; 0]，H_{A,0} = [0; v1; v2]，v1 = e1, v2 = e2。
  则 rank H_0 = 2，且固定铅笔 λH_0 - H_{A,0} 的 2-子式 gcd = 1（处处秩 2）。

定理 A（attempts/357）在 m=1 时的两条情形：
  * h ∈ row H_0、g ∈ row H_0：ω = 2，可行（(5b) 成立）；
  * h ∉ row H_0：ω = 3，且 (5a) 迫使 g = αh + w；在 λ=α 处掉秩 ⟹ **不可行**。
    注意此时 λ=0 是过关的（rank H = rank H_A = 3），所以这不是"λ=0 平凡失败"。
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
    A[0:3, 6:9] = sp.eye(3)   # W -> U
    A[6:9, 3:6] = sp.eye(3)   # V -> W
    return C, A, k


def main() -> None:
    print("=" * 74)
    print("单自由行（m=1）的 CLP：位移脚手架实例")
    print("=" * 74)
    C, A, k = build()
    Wm = sp.Matrix.vstack(C, C * A)
    assert Wm.rank() == 6
    N = m.ker_basis(Wm)
    assert N.cols == k
    AN = A * N
    assert sp.Matrix.hstack(N, AN).rank() == 2 * k

    v1 = sp.Matrix([[1, 0, 0]])
    v2 = sp.Matrix([[0, 1, 0]])
    H0 = sp.Matrix.vstack(v1, v2, sp.zeros(1, k))
    HA0 = sp.Matrix.vstack(sp.zeros(1, k), v1, v2)
    P0 = sp.Matrix(3, k, lambda i, j: lam * H0[i, j] - HA0[i, j])
    print(f"  rank H_0 = {H0.rank()}，固定铅笔 gcd = {sp.sstr(gcd_minors(P0, 2))}（应为 1）")
    assert H0.rank() == 2 and gcd_minors(P0, 2) == 1

    # (b) h, g ∈ row H_0 = span{e1,e2}
    for h, g, tag in [(v1, v2, "h=v1,g=v2"), (v1 + v2, v1, "h=v1+v2,g=v1")]:
        H = sp.Matrix.vstack(H0, h)
        HA = sp.Matrix.vstack(HA0, g)
        assert H.rank() == 2, H.rank()
        assert (HA * m.ker_basis(H)).is_zero_matrix, "(5a)"
        gg = gcd_minors(sp.Matrix(H.rows, k, lambda i, j: lam * H[i, j] - HA[i, j]), 2)
        print(f"  (b) {tag}: ω=2, gcd={sp.sstr(gg)}")
        assert gg == 1
    print("  (b) 全部可行 ✓")

    # (a) h ∉ row H_0（取 e3 方向），g = αh + w
    h = sp.Matrix([[0, 0, 1]])
    for alpha in [-2, 1, 3]:
        for wname, w in [("0", sp.zeros(1, k)), ("v1", v1)]:
            g = alpha * h + w
            H = sp.Matrix.vstack(H0, h)
            HA = sp.Matrix.vstack(HA0, g)
            assert H.rank() == 3
            assert HA.rank() == 3, "α≠0 时 λ=0 应当过关"
            assert (HA * m.ker_basis(H)).is_zero_matrix, "(5a)"
            gg = gcd_minors(sp.Matrix(H.rows, k, lambda i, j: lam * H[i, j] - HA[i, j]), 3)
            expect = sp.Poly(lam - alpha, lam).monic().as_expr()
            print(f"  (a) alpha={alpha}, w={wname}: gcd={sp.sstr(gg)}（应为 λ-α）")
            assert sp.simplify(gg - expect) == 0, f"公共根应恰为 α={alpha}"
    # α = 0 的退化情形：g ∈ row H_0，η=3 层在 λ=0 就失败
    g = sp.zeros(1, k)
    H = sp.Matrix.vstack(H0, h)
    HA = sp.Matrix.vstack(HA0, g)
    print(f"  (a') alpha=0, w=0: rank H_A = {HA.rank()} < 3（λ=0 处平凡失败）")
    assert HA.rank() == 2
    print()
    print("  定理 A ✓：h∈row H_0 可行（线性空间中的开集）；h∉row H_0 必坏，公共根恰为 λ=α")


if __name__ == "__main__":
    main()
