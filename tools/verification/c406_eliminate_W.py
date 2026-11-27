"""c406 — 消 W：铅笔对 W 的依赖只通过 Φ(W) = π(W) ⊆ D°（dim D° = c = 2）。

观察（待验证）：
  V = D^{⊥_K} ⊕ W，H = VᵀN 的 W 行**全为零**（W ⊆ K^⊥），
  H_A 的 W 行是 φ_w(·) = <w, A21 ·>（因为 <w, Mx> = 0）。
  故 pencil 的行空间 = row(D 部分) + Φ(W)，其中 Φ(W) = span{φ_w : w ∈ W} ⊆ D°（dim c = 2）。
⇒ 铅笔条件只通过 Φ(W) 依赖 W；c=2 时 Φ 只有 0 / 直线 / 全空间三种，直线是 P¹ 族。

本脚本：固定 D，采样若干 W，算 Φ(W)，按 Φ 分组，核对同组内 gcd 相同。
"""

from __future__ import annotations

import itertools
import os
import random
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
    Proj = sp.eye(A.rows) - N * sp.Matrix(G.inv()) * N.T
    A21 = sp.simplify(Proj * A * N)
    return A, N, k, G, A21


def gcd_deg(H, HA, k):
    om = H.rank()
    if om == 0:
        return om, None
    P = sp.Matrix(H.rows, k, lambda i, j: lam * H[i, j] - HA[i, j])
    polys = []
    for rs in itertools.combinations(range(H.rows), om):
        for cs in itertools.combinations(range(k), om):
            det = sp.expand(P.extract(list(rs), list(cs)).det())
            if sp.simplify(det) != 0:
                polys.append(det)
    if not polys:
        return om, None
    gg = polys[0]
    for pp in polys[1:]:
        gg = sp.gcd(gg, pp)
    return om, sp.degree(sp.simplify(gg), lam)


def as_col(t, n):
    """把 nullspace 返回的元素统一成 n×1 列向量。"""
    M = sp.Matrix(t)
    if M.shape == (n, 1):
        return M
    if M.shape == (1, n):
        return M.T
    if M.shape == (n,):
        return M.reshape(n, 1)
    raise ValueError(f"unexpected shape {M.shape}")


def main() -> None:
    A, N, k, G, A21 = build()
    n = A.rows
    I = sp.eye(k)
    Dk = sp.Matrix.hstack(I.col(0) + I.col(1), I.col(2))     # c=2 的 D
    comp = [sp.simplify(x) for x in (Dk.T * G).nullspace()]   # D^{⊥_K} 的基（K 坐标）
    TD = sp.Matrix.vstack(N.T, (A21 * Dk).T).nullspace()      # T_D 的基（环境列）
    print(f"n={n}, k={k}, dim T_D = {len(TD)}, D 的 K 坐标 = {Dk.tolist()}")
    # 校验：Φ(W) 落在 D° 里（即 φ_w 在 D 上为零）
    print("校验 φ_w 在 D 上为零：")
    for t in TD[:3]:
        phi = as_col(t, n).T * A21       # 1×k：φ_w 在 K 各基上的值
        vals = sp.Matrix(phi * Dk)          # 1×c
        print(f"   w = {as_col(t, n).T.tolist()}: φ_w(D) = {vals.tolist()}  (应全 0)")
    print()
    rng = random.Random(77)
    print("采样 W（1 维），按 Φ(W) 分组，看 gcd：")
    groups = {}
    for trial in range(10):
        coef = [rng.randint(-2, 2) for _ in TD]
        w = sum((c * t for c, t in zip(coef, TD)), sp.zeros(n, 1))
        if w.is_zero_matrix:
            continue
        V = [sp.simplify(N * x) for x in comp] + [sp.Matrix(w)]
        Vm = sp.Matrix.hstack(*V)
        if Vm.rank() != 3:
            continue
        H = sp.simplify(Vm.T * N)
        HA = sp.simplify(Vm.T * A * N)
        phi = sp.simplify(sp.Matrix(w).T * A21)   # 1×k
        # 把 Φ 归一化（除以第一个非零元），便于分组
        nz = next((x for x in phi if sp.simplify(x) != 0), None)
        key = tuple(sp.simplify(sp.nsimplify(x / nz)) for x in phi) if nz is not None else None
        om, dg = gcd_deg(H, HA, k)
        groups.setdefault(key, []).append((trial, om, dg, sp.Matrix(w).T.tolist()))
        print(f"  trial {trial}: omega={om} gcd={dg}  Φ∝{key}")
    print()
    print("=== 分组结果（同一 Φ 内 gcd 是否相同）===")
    ok = True
    for key, lst in groups.items():
        dgs = {x[2] for x in lst}
        if len(dgs) > 1:
            ok = False
        print(f"  Φ∝{key}: {len(lst)} 个 W，gcd 次数集合 = {dgs}")
    print("同组内 gcd 恒同：" + ("是 ✓" if ok else "否 ✗"))


if __name__ == "__main__":
    main()
