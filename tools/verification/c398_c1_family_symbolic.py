"""c398 — 把 c=1 层在 q=3 上的判定做成符号计算（家族 D = span{e1 + s e2}, s ∈ P^1）。

若该家族的 gcd（在 Q(s)[lambda] 上）次数为正，且 rank H ≡ 3 在整族上成立，
则由满秩首项系数引理，**整条 P^1 都坏** => q=3 的 c=1 层不可行。
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
import c352_number_field_decider as d  # noqa: E402

lam = sp.symbols("lam")
s = sp.symbols("s")


def build():
    A, C = d.build_instance(4242)
    A = sp.Matrix(A)
    for i in range(4):
        for j in range(4):
            A[4 + i, 4 + j] = sp.diag(1, 1, 2, 3)[i, j]
    N = m.ker_basis(sp.Matrix.vstack(C, C * A))
    k = N.cols
    G = N.T * N
    return A, N, k, G


def main() -> None:
    A, N, k, G = build()
    I = sp.eye(k)
    # D = span{e1 + s e2}（K 坐标），V = D^{perp_K}
    Dk = I.col(0) + s * I.col(1)
    sys_ = (Dk.T * G)                 # 1×k，s 为符号
    comp = sys_.nullspace()           # 3 个基向量（含 s 的有理式）
    comp = [sp.simplify(c) for c in comp]
    V = [sp.simplify(N * c) for c in comp]
    Vm = sp.Matrix.hstack(*V)
    H = sp.simplify(Vm.T * N)
    HA = sp.simplify(Vm.T * A * N)
    print("H 的条目（s 的有理式）：")
    for i in range(H.rows):
        print("   ", [sp.simplify(H[i, j]) for j in range(k)])
    print(f"rank H（符号） = {H.rank()}")
    om = 3
    polys = []
    P = sp.Matrix(H.rows, k, lambda i, j: lam * H[i, j] - HA[i, j])
    for rs in itertools.combinations(range(H.rows), om):
        for cs in itertools.combinations(range(k), om):
            det = sp.simplify(P.extract(list(rs), list(cs)).det())
            if det != 0:
                polys.append(sp.together(det))
    print(f"非零 {om} 阶子式个数 = {len(polys)}")
    # 清分母（对 s）后取 gcd（在 Q[s,lam] 上）
    poly_lam = []
    for p in polys:
        num, den = sp.fraction(sp.together(p))
        poly_lam.append(sp.expand(num))
    g = poly_lam[0]
    for pp in poly_lam[1:]:
        g = sp.gcd(g, pp)
    g = sp.factor(g)
    print("gcd（清分母后，Q[s,lam] 上） =", sp.sstr(g))
    print("作为 lambda 的多项式次数 =", sp.degree(g, lam) if g != 0 else "n/a")
    print("在 s=0,1,2 处取值：", [sp.simplify(g.subs(s, v)) for v in (0, 1, 2)])


if __name__ == "__main__":
    main()
