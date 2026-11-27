"""c397 — 同一阶 q 下比较 c=1 与 c=2 层（K-split 判定器的第一档）。

关键算术（本实例 k=4）：
  c = k - rho  =>  c=1: rho=3, q = rho + t = 3 + t;  c=2: rho=2, q = 2 + t.
  K-split 纤维：Gr(t - w0, rho - r)，w0=0（L0 为空），r = rank(A21|_D).
  => q=3 是两层都可出现的唯一阶：
       c=1, t=0: 纤维 Gr(0, 3-r) = 单点（V = D^{perp_K}，3 维，落在 K 内）
       c=2, t=1: 纤维 Gr(1, 2-r)：r=0 时为 P^1（1 参数），r=1 时为单点

本脚本在 q=3 上：
  * c=1：枚举 D = E_1 内的直线（采样）+ e3, e4；V = D^{perp_K}；测 gcd；
  * c=2：枚举 M-不变 2-平面（E_1 本身；span{u,e3}、span{u,e4}（u∈E_1，采样）；span{e3,e4}）；
          W 在 T_D 内取 1 维（采样），V = D^{perp_K} ⊕ W；测 gcd。
报告每个候选的 (5a)/精确核/omega/gcd 次数。
"""

from __future__ import annotations

import itertools
import os
import sys
from fractions import Fraction as F

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
    n = A.rows
    G = N.T * N
    M = sp.simplify(sp.Matrix(G.inv() * (N.T * A * N)))
    Proj = sp.eye(n) - N * sp.Matrix(G.inv()) * N.T
    A21 = sp.simplify(Proj * A * N)
    return A, N, M, A21, k, n, G


def perp_in_K(N, G, Dk):
    """Dk: k×c（K 坐标）。返回 D^{perp_K} 的基（K 坐标，列）。"""
    sys_ = (Dk.T * G)          # c×k
    return sys_.nullspace()


def T_D(A21, N, n, Dk):
    """K^perp ∩ (A21 D)^perp 的基（环境列向量）。"""
    AD = A21 * Dk              # n×c
    blk = sp.Matrix.vstack(N.T, AD.T)
    return blk.nullspace()


def gcd_deg(Vcols, N, A, k):
    Vm = sp.Matrix.hstack(*Vcols) if Vcols else sp.zeros(N.rows, 0)
    H = Vm.T * N
    om = H.rank()
    if om == 0:
        return om, None, Vm.cols
    HA = Vm.T * A * N
    P = sp.Matrix(Vm.cols, k, lambda i, j: lam * H[i, j] - HA[i, j])
    polys = []
    for rs in itertools.combinations(range(Vm.cols), om):
        for cs in itertools.combinations(range(k), om):
            det = sp.expand(P.extract(list(rs), list(cs)).det())
            if sp.simplify(det) != 0:
                polys.append(det)
    if not polys:
        return om, None, Vm.cols
    gg = polys[0]
    for pp in polys[1:]:
        gg = sp.gcd(gg, pp)
    return om, sp.degree(sp.simplify(gg), lam), Vm.cols


def main() -> None:
    A, N, M, A21, k, n, G = build()
    I = sp.eye(k)
    print(f"n={n}, k={k}, M=diag(1,1,2,3)")
    print("rho = k - c：c=1 -> rho=3, q=3+t；c=2 -> rho=2, q=2+t")
    print()
    # ---------- c = 1, t = 0, q = 3 ----------
    print("=== c=1, t=0, q=3：D = 一条线，V = D^{perp_K}（3 维，在 K 内） ===")
    lines = {
        "e1": I.col(0), "e2": I.col(1), "e1+e2": I.col(0) + I.col(1),
        "e1-e2": I.col(0) - I.col(1), "2e1+e2": 2 * I.col(0) + I.col(1),
        "e3": I.col(2), "e4": I.col(3),
    }
    for tag, D in lines.items():
        Dk = sp.Matrix(D)
        comp = perp_in_K(N, G, Dk)
        V = [N * c for c in comp]
        om, dg, q = gcd_deg(V, N, A, k)
        print(f"  D={tag:8s} q={q} omega={om} gcd次数={dg}"
              + ("  <= 可行" if dg == 0 else ""))
    print()
    # ---------- c = 2, t = 1, q = 3 ----------
    print("=== c=2, t=1, q=3：D = M-不变 2-平面，W 取 T_D 内的 1 维 ===")
    E1 = [I.col(0), I.col(1)]
    u = sp.Matrix(I.col(0) + I.col(1))     # E_1 内的方向
    planes = {
        "E1": sp.Matrix.hstack(*E1),
        "span{e3,e4}": sp.Matrix.hstack(I.col(2), I.col(3)),
        "span{u,e3}": sp.Matrix.hstack(u, I.col(2)),
        "span{u,e4}": sp.Matrix.hstack(u, I.col(3)),
        "span{e1,e3}": sp.Matrix.hstack(I.col(0), I.col(2)),
    }
    for tag, Dk in planes.items():
        comp = perp_in_K(N, G, Dk)
        TD = T_D(A21, N, n, Dk)
        r = sp.Matrix(A21 * Dk).rank()
        print(f"  D={tag:12s} r={r} dim T_D={len(TD)} -> W 有 {len(TD)} 个候选（1 维）")
        found = False
        for w in TD:
            V = [N * c for c in comp] + [w]
            om, dg, q = gcd_deg(V, N, A, k)
            if dg == 0:
                found = True
                print(f"       W={sp.Matrix(w).T.tolist()} q={q} omega={om} gcd=0  <= 可行")
        if not found:
            print(f"       全部 W 不可行")


if __name__ == "__main__":
    main()
