"""c404 — 专家 108 号要求：补齐 c=1 反例的缺失射影点，并输出两侧的完整证书。

(c=1 侧) 专家指出 D = span{e1 + s e2} 漏掉 [0:1] = span{e2}。本脚本：
  * 算 D = span{e2} 的 V、H、HA、全部非零 3 阶子式与 gcd；
  * 用齐次做法复核：对 D = span{a e1 + b e2} 取 (a,b) = (1,0), (1,1), (0,1), (2,-1) 等，看 gcd；
  * 打印 H 与 HA、以及非零极大子式与 gcd（专家 §10 要求）。

(c=2 侧) 打印 N、A 的块、V、H、HA、六个 2 阶子式与 gcd（专家 §11 要求）。
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


def gcd_of_minors(H, HA, om, k, label):
    P = sp.Matrix(H.rows, k, lambda i, j: lam * H[i, j] - HA[i, j])
    polys = []
    for rs in itertools.combinations(range(H.rows), om):
        for cs in itertools.combinations(range(k), om):
            det = sp.expand(P.extract(list(rs), list(cs)).det())
            if sp.simplify(det) != 0:
                polys.append(sp.simplify(det))
    print(f"   {label}: {len(polys)} 个非零 {om} 阶子式")
    gg = polys[0]
    for pp in polys[1:]:
        gg = sp.gcd(gg, pp)
    gg = sp.factor(sp.simplify(gg))
    print(f"   gcd = {sp.sstr(gg)}   次数 = {sp.degree(gg, lam)}")
    return polys, gg


def main() -> None:
    A, N, k, G = build()
    print(f"k = {k};  K0 的基 N = {N.tolist()}")
    print()
    # ---------- c=1 侧：补齐射影点 ----------
    print("=== c=1 侧：q=3，D = span{a e1 + b e2} 的全部射影方向（含 (0,1)）===")
    for (a, b) in [(1, 0), (1, 1), (1, 2), (0, 1), (2, -1), (-1, 3)]:
        Dk = sp.Matrix(k, 1, [a, b, 0, 0])
        comp = [sp.simplify(x) for x in (Dk.T * G).nullspace()]
        Vm = sp.Matrix.hstack(*[sp.simplify(N * x) for x in comp])
        H = Vm.T * N
        HA = Vm.T * A * N
        om = H.rank()
        print(f"  D = span{{({a}) e1 + ({b}) e2}}: dim V = {Vm.cols}, omega = {om}")
        print(f"    H  = {sp.simplify(H).tolist()}")
        print(f"    HA = {sp.simplify(HA).tolist()}")
        gcd_of_minors(H, HA, om, k, f"(a,b)=({a},{b})")
        print()
    # 两个孤立方向
    for j in (2, 3):
        Dk = sp.Matrix(sp.eye(k).col(j))
        comp = [sp.simplify(x) for x in (Dk.T * G).nullspace()]
        Vm = sp.Matrix.hstack(*[sp.simplify(N * x) for x in comp])
        H = Vm.T * N
        HA = Vm.T * A * N
        om = H.rank()
        print(f"  D = span{{e_{j+1}}}: dim V = {Vm.cols}, omega = {om}")
        gcd_of_minors(H, HA, om, k, f"e{j+1}")
        print()
    # ---------- c=2 侧：完整证书 ----------
    print("=== c=2 侧：q=3，D = span{e1+e2, e3}，W = (0,0,1,1,0,0,0,0) ===")
    I = sp.eye(k)
    Dk = sp.Matrix.hstack(I.col(0) + I.col(1), I.col(2))
    comp = [sp.simplify(x) for x in (Dk.T * G).nullspace()]
    W = sp.Matrix([[0], [0], [1], [1], [0], [0], [0], [0]])
    Vm = sp.Matrix.hstack(*([sp.simplify(N * x) for x in comp] + [W]))
    print(f"  N 的行列 = {N.tolist()}")
    print(f"  D 的 K 坐标 = {Dk.tolist()}")
    print(f"  V 的基（环境坐标，列）= {Vm.tolist()}")
    H = sp.simplify(Vm.T * N)
    HA = sp.simplify(Vm.T * A * N)
    print(f"  H  = {H.tolist()}")
    print(f"  HA = {HA.tolist()}")
    print(f"  dim V = {Vm.rank()}, omega = rank H = {H.rank()}, K0 ∩ V^perp 的维数 = "
          f"{k + Vm.rank() - sp.Matrix.hstack(N, Vm).rank()}")
    AD = A * (N * Dk)
    print(f"  (5a) AD ⟂ V : {(Vm.T * AD).is_zero_matrix}")
    polys, gg = gcd_of_minors(H, HA, H.rank(), k, "c=2 设计")
    print("  非零 2 阶子式：")
    for pp in polys:
        print("    ", sp.sstr(sp.factor(pp)))


if __name__ == "__main__":
    main()
