"""c403 — 两层的可行性：r=0 层唯一（D0 = ker A21 ∩ E1），纤维 P^3；r=1 层 2 参数。

依据：可行集在每张图卡上是**开集**（满秩 + 无公根都是开条件），所以
  * 采到可行点 => 该层可行（**sound**）；
  * 大量采样都没采到 => 强证据不可行（但**不是证明**）。

本脚本对夹具（A21 秩 1）逐层大量采样：
  r=0：D = D0（唯一），W 在 T_D（4 维）里取 1 维 => P^3；
  r=1：D 随机在 Gr(2,E1) 且 r=1，W 在 T_D（3 维）里取 1 维。
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

lam = sp.symbols("lam")


def build():
    C1 = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0]])
    C = sp.Matrix.hstack(C1, sp.zeros(2, 4))
    A11 = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]])
    u = sp.Matrix([0, 0, 1, 0])
    v = sp.Matrix([1, 0, 0, 0])
    A12 = u * v.T
    M = sp.diag(1, 1, 1, 2)
    A = sp.Matrix.vstack(sp.Matrix.hstack(A11, A12), sp.Matrix.hstack(A12, M))
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    k = N.cols
    G = N.T * N
    Proj = sp.eye(A.rows) - N * sp.Matrix(G.inv()) * N.T
    A21 = sp.simplify(Proj * A * N)
    return A, N, k, G, A21


def gcd_deg(Vm, N, A, k):
    H = Vm.T * N
    om = H.rank()
    if om == 0:
        return om, None
    HA = Vm.T * A * N
    P = sp.Matrix(Vm.cols, k, lambda i, j: lam * H[i, j] - HA[i, j])
    polys = []
    for rs in itertools.combinations(range(Vm.cols), om):
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


def design(A, N, k, G, Dk, TD, rng):
    comp = [sp.simplify(x) for x in (Dk.T * G).nullspace()]
    coef = [rng.randint(-3, 3) for _ in TD]
    w = sum((c * t for c, t in zip(coef, TD)), sp.zeros(N.rows, 1))
    if w.is_zero_matrix:
        return None
    V = [sp.simplify(N * x) for x in comp] + [sp.Matrix(w)]
    Vm = sp.Matrix.hstack(*V)
    if Vm.rank() != Vm.cols:
        return None
    return Vm


def main() -> None:
    A, N, k, G, A21 = build()
    n = A.rows
    print(f"n={n}, k={k}, rank A21 = {A21.rank()}")
    I = sp.eye(k)
    D0 = I.col(1)  # ker A21 ∩ E1 = span{e2,e3} 太大；先用 e2,e3 组成的唯一 2-平面
    D0 = sp.Matrix.hstack(I.col(1), I.col(2))
    print("r=0 层的唯一候选 D0 = span{e2,e3}（应满足 A21 D0 = 0）：",
          (A21 * D0).is_zero_matrix)
    rng = random.Random(2024)
    for tag, Dk, nsamp in (("r=0（D0 固定，W ∈ P^3）", D0, 200),):
        r = sp.Matrix(A21 * Dk).rank()
        TD = sp.Matrix.vstack(N.T, (A21 * Dk).T).nullspace()
        print(f"\n{tag}: r={r}, dim T_D={len(TD)}")
        cnt = {}
        best = None
        for _ in range(nsamp):
            Vm = design(A, N, k, G, Dk, TD, rng)
            if Vm is None:
                continue
            om, dg = gcd_deg(Vm, N, A, k)
            cnt[(om, dg)] = cnt.get((om, dg), 0) + 1
            if dg == 0 and best is None:
                best = Vm
        for key, c in sorted(cnt.items(), key=lambda kv: str(kv[0])):
            print(f"   (omega, gcd)={key}: {c} 例")
        if best is not None:
            print("   ** 找到可行设计，V 的基：")
            for i in range(best.cols):
                print("      ", sp.Matrix(best.col(i)).T.tolist())

    # r=1 层：随机 D（r=1），W ∈ T_D（3 维）
    print("\nr=1 层（D 随机、r=1，W ∈ P^2）：")
    E1 = [sp.Matrix(I.col(0)), sp.Matrix(I.col(1)), sp.Matrix(I.col(2))]
    cnt = {}
    found = None
    tried = 0
    while tried < 200:
        v1 = E1[0] * rng.randint(-3, 3) + E1[1] * rng.randint(-3, 3) + E1[2] * rng.randint(-3, 3)
        v2 = E1[0] * rng.randint(-3, 3) + E1[1] * rng.randint(-3, 3) + E1[2] * rng.randint(-3, 3)
        Dk = sp.Matrix.hstack(v1, v2)
        if Dk.rank() < 2:
            continue
        r = sp.Matrix(A21 * Dk).rank()
        if r != 1:
            continue
        tried += 1
        TD = sp.Matrix.vstack(N.T, (A21 * Dk).T).nullspace()
        Vm = design(A, N, k, G, Dk, TD, rng)
        if Vm is None:
            continue
        om, dg = gcd_deg(Vm, N, A, k)
        cnt[(om, dg)] = cnt.get((om, dg), 0) + 1
        if dg == 0 and found is None:
            found = Vm
    for key, c in sorted(cnt.items(), key=lambda kv: str(kv[0])):
        print(f"   (omega, gcd)={key}: {c} 例")
    if found is not None:
        print("   ** 找到可行设计")


if __name__ == "__main__":
    main()
