"""c411 — 十类测试集里可立即算出的六类的数据（class 1,2,3,4,9,10）。

底座：n=8, K0=span{e5..e8}, C=[C1 0]（C1=[[1,0,0,0],[0,1,0,0]]），
A = [[A11, A12],[A21, M]]（4x4 块），A21 := A12（保证 C1 A12 = 0 => K0 由 A12 的核决定；
这里统一取 A12=0 或秩 1，故 K0 恒为 span{e5..e8}）。
对给定的 D（K 坐标）与 W（环境列向量），输出 H、H_A、omega、非零 omega 阶子式与 gcd 次数。
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
C1 = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0]])
A11 = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]])


def build(A12, M):
    A = sp.Matrix.vstack(sp.Matrix.hstack(A11, A12), sp.Matrix.hstack(A12, M))
    C = sp.Matrix.hstack(C1, sp.zeros(2, 4))
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    k = N.cols
    G = N.T * N
    return A, C, N, k, G


def cert(A, N, k, G, Dk, Wcols):
    comp = [sp.simplify(x) for x in (Dk.T * G).nullspace()]
    V = [sp.simplify(N * x) for x in comp] + [sp.Matrix(w) for w in Wcols]
    Vm = sp.Matrix.hstack(*V)
    H = sp.simplify(Vm.T * N)
    HA = sp.simplify(Vm.T * A * N)
    om = H.rank()
    P = sp.Matrix(Vm.cols, k, lambda i, j: lam * H[i, j] - HA[i, j])
    polys = []
    for rs in itertools.combinations(range(Vm.cols), om):
        for cs in itertools.combinations(range(k), om):
            det = sp.expand(P.extract(list(rs), list(cs)).det())
            if sp.simplify(det) != 0:
                polys.append(sp.factor(det))
    gg = polys[0]
    for pp in polys[1:]:
        gg = sp.gcd(gg, pp)
    inter = k + Vm.rank() - sp.Matrix.hstack(N, Vm).rank()
    return dict(q=Vm.rank(), om=om, c=k - om, exact=(inter == Dk.cols),
                gcd=sp.degree(sp.simplify(gg), lam), nmin=len(polys),
                polys=polys, H=H, HA=HA)


def main() -> None:
    I4 = sp.eye(4)
    z = sp.zeros(4, 4)
    Wstd = [sp.Matrix([[0], [0], [1], [1], [0], [0], [0], [0]])]
    D12 = sp.Matrix.hstack(I4.col(0), I4.col(1))
    D13 = sp.Matrix.hstack(I4.col(0), I4.col(2))
    D34 = sp.Matrix.hstack(I4.col(2), I4.col(3))
    # 类 2 的旋转块
    R = sp.Matrix([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 2, 0], [0, 0, 0, 3]])
    u = sp.Matrix([0, 0, 1, 0])
    v = sp.Matrix([1, 0, 0, 0])
    A12r1 = u * v.T

    cases = [
        ("类1 简单实谱 M=diag(1,2,3,4)", z, sp.diag(1, 2, 3, 4), D12, Wstd),
        ("类2 共轭复 M=diag(R,2,3) D=ker(M^2+I)", z, R, D12, Wstd),
        ("类2 共轭复 同上, D=span{e3,e4}", z, R, D34, Wstd),
        ("类3 重复实谱 M=diag(1,1,2,3) D=span{e1,e2}", z, sp.diag(1, 1, 2, 3), D12, Wstd),
        ("类4 A21 秩1 M=diag(1,1,1,2) D=span{e1,e3} (r=1)", A12r1, sp.diag(1, 1, 1, 2), D13, Wstd),
        ("类4 A21 秩1 M=diag(1,1,1,2) D=span{e2,e3} (r=0)", A12r1, sp.diag(1, 1, 1, 2),
         sp.Matrix.hstack(I4.col(1), I4.col(2)), Wstd),
        ("类10 可行设计 M=diag(1,1,2,3) D=span{e1+e2,e3}",
         z, sp.diag(1, 1, 2, 3), sp.Matrix.hstack(I4.col(0) + I4.col(1), I4.col(2)), Wstd),
    ]
    for tag, A12, M, Dk, Wc in cases:
        A, C, N, k, G = build(A12, M)
        r = cert(A, N, k, G, Dk, Wc)
        print(f"{tag}")
        print(f"   k={k}, q={r['q']}, omega={r['om']}, c={r['c']}, exact={r['exact']}, "
              f"gcd次数={r['gcd']}, 非零子式数={r['nmin']}")
        print(f"   H={r['H'].tolist()}")
        print()
    # 类 9：c=1 侧（q=3, D=span{e1}）用同一实例
    A, C, N, k, G = build(z, sp.diag(1, 1, 2, 3))
    r = cert(A, N, k, G, sp.Matrix(I4.col(0)), [])
    print(f"类9 c=1 D=span{{e1}}: q={r['q']}, omega={r['om']}, c={r['c']}, gcd次数={r['gcd']}")
    print(f"   非零 3 阶子式：{[sp.sstr(x) for x in r['polys']]}")


if __name__ == "__main__":
    main()
