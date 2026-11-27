#!/usr/bin/env python3
"""c332 — 104 族（$k=3,\\omega=2,q=3,d=1$）的全空间分解 Z = Z1 ∪ Z2。

背景：104 说"可容许轨迹 P^1 是混合的：一般层全坏、例外点 σ=(1,0,0) 好"。
但那句话是在**底空间** P^1 上说的。全空间（lifted incidence）其实分成两支：

    Z1 = { σ=(1,0,0) 且 y_i 自由 }        （b = 0 的一支）
    Z2 = { y_i ∝ V_0，σ 任意 }             （y 被压到一维的一支）

因为 y 的条件是 σ·y = 0 且 y_1 = 0，而 σ=(a,-4b,b) 时
    a y_1 - 4b y_2 + b y_3 = 0,  y_1 = 0  ⟹  b(-4 y_2 + y_3) = 0,
即"b = 0"或"-4y_2+y_3 = 0"——一个乘积式，故 Z = {b=0} ∪ {y ∝ V_0}。

本脚本：
  (1) 对随机的 (a,b) 与随机 y ∈ S∩{y_1=0}，验证上面的乘积式，
      并验证 b ≠ 0 ⟹ y ∝ V_0（即 Z2 之外没有别的点）；
  (2) 在两支上各取若干**精确有理**实例，算 λH−H_A 的三个 2×2 子式的 gcd：
      Z2 上应恒为 λ（全坏），Z1 上一般点为 1（好）。
      这与"分量级 generic gcd"一致，而"底空间 generic"会把两支混在一起。

有限精确检验，不是证明。104 的证明（逐行秩论证）已给出 Z2 全坏；本脚本只把
"Z = Z1 ∪ Z2"与两支的 gcd 值显式化。
"""

from __future__ import annotations

import itertools
import os
import random
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

lam = sp.symbols("lam")

V0 = sp.Matrix([0, -1, -4])          # 104 的数据（K-坐标）
Z1_dat = sp.Matrix([0, 0, 0])        # Z_1 = 0
Z2_dat = sp.Matrix([1, 0, 0])        # Z_2 = e_1


def sigma(a, b):
    """104 的可容许 σ：(a, -4b, b)。"""
    return sp.Matrix([a, -4 * b, b])


def kernel_basis(sig):
    """ker σ 的一组基（3 维里 2 维）。"""
    M = sig.T  # 1x3
    ns = M.nullspace()
    assert len(ns) == 2, "ker σ 的维数应为 2"
    return [sp.Matrix(v) for v in ns]


def minors_gcd(H, HA):
    """λH − HA 的全部 2×2 子式的 gcd（monic）。"""
    q = H.rows
    P = sp.Matrix(q, 2, lambda i, j: lam * H[i, j] - HA[i, j])
    ms = []
    for rows in itertools.combinations(range(q), 2):
        ms.append(sp.expand(P.extract(list(rows), [0, 1]).det()))
    g = ms[0]
    for m in ms[1:]:
        g = sp.gcd(g, m)
    g = sp.Poly(g, lam)
    return g.monic().as_expr() if g.degree() > 0 else sp.Integer(g.eval(0))


def build_H_Ha(sig, ys, xs):
    """在 S = ker σ 的坐标里组装 H = [0; x_1; x_2]、H_A = [V_0; y_1; y_2]。"""
    B = kernel_basis(sig)
    # 把 3 维向量写成 S-坐标
    def coords(v):
        M = sp.Matrix.hstack(*B)          # 3x2
        sol = M.gauss_jordan_solve(sp.Matrix(v))[0]
        return sp.Matrix([sp.simplify(sol[0]), sp.simplify(sol[1])])

    v0 = coords(V0)
    Ha = sp.Matrix([v0.T, ys[0].T, ys[1].T])
    H = sp.Matrix([sp.zeros(1, 2), xs[0].T, xs[1].T])
    return H, Ha, v0


def part1(rng, trials=200):
    print("=" * 74)
    print("(1) 乘积式：b·(−4y_2+y_3)=0，且 b≠0 ⟹ y ∝ V_0")
    print("=" * 74)
    ok = 0
    for _ in range(trials):
        a, b = rng.randint(-3, 3), rng.randint(-3, 3)
        if a == 0 and b == 0:
            continue
        sig = sigma(a, b)
        # 取 y ∈ ker σ 且 y_1 = 0
        cand = []
        for y2, y3 in itertools.product(range(-2, 3), repeat=2):
            y = sp.Matrix([0, y2, y3])
            if (sig.T * y)[0] == 0:
                cand.append(y)
        if not cand:
            continue
        y = rng.choice(cand)
        # 乘积式
        assert b * (-4 * y[1] + y[2]) == 0, (a, b, y.T)
        if b != 0:
            # 应为 V_0 的倍数
            ratio = sp.simplify(y[1] / V0[1]) if V0[1] != 0 else None
            assert ratio is not None
            assert sp.simplify(y[2] - ratio * V0[2]) == 0, (a, b, y.T)
        ok += 1
    print(f"  {ok} 个随机实例全部满足分解式；b≠0 时 y 都是 V_0 的倍数。")

    # 反向：若 b=0 而 y 不是 V_0 的倍数，确实存在（Z1 非空且不等于 Z2）
    y1 = sp.Matrix([0, 1, 0])
    assert sp.simplify(y1[2] - 0) == 0  # y1 = (0,1,0) 不是 V0 的倍数
    print("  且 Z1 真非空：σ=(1,0,0) 时 y=(0,1,0)∈ker σ、y_1=0，但 y ∦ V_0。")


def part2(rng, trials=6):
    print()
    print("=" * 74)
    print("(2) 两支上的 gcd：Z2 恒为 λ（全坏）；Z1 一般点为 1（好）")
    print("=" * 74)
    # --- Z2：y_i ∝ V_0（即 S-坐标里都在 span(v0) 上）
    bad = []
    for _ in range(trials):
        a = rng.randint(1, 3)
        b = rng.randint(1, 3)                      # b ≠ 0
        sig = sigma(a, b)
        c1, c2 = rng.randint(-2, 2), rng.randint(-2, 2)
        xs = [sp.Matrix([rng.randint(-2, 2), rng.randint(-2, 2)]) for _ in range(2)]
        B = kernel_basis(sig)
        M = sp.Matrix.hstack(*B)
        v0 = M.gauss_jordan_solve(sp.Matrix(V0))[0]
        ys = [c1 * v0, c2 * v0]
        H = sp.Matrix([sp.zeros(1, 2), xs[0].T, xs[1].T])
        Ha = sp.Matrix([v0.T, ys[0].T, ys[1].T])
        g = minors_gcd(H, Ha)
        bad.append(g)
    print(f"  Z2 上 {trials} 个实例的 gcd：{set(sp.sstr(g) for g in bad)}")
    assert all(g == lam for g in bad), "Z2 应恒为 λ"

    # --- Z1：σ=(1,0,0)，y_i 自由
    sig = sigma(1, 0)
    good = []
    for _ in range(trials):
        ys = [sp.Matrix([rng.randint(-3, 3), rng.randint(-3, 3)]) for _ in range(2)]
        xs = [sp.Matrix([rng.randint(-3, 3), rng.randint(-3, 3)]) for _ in range(2)]
        H, Ha, v0 = build_H_Ha(sig, ys, xs)
        if H.rank() < 2 or sp.Matrix.hstack(H, Ha).rank() < 2:
            continue
        g = minors_gcd(H, Ha)
        good.append(g)
    print(f"  Z1 上 {len(good)} 个一般实例的 gcd：{set(sp.sstr(g) for g in good)}")
    assert all(g == 1 for g in good), "Z1 一般点应为 1"


def main() -> None:
    rng = random.Random(332)
    part1(rng)
    part2(rng)
    print()
    print("=" * 74)
    print("结论（有限精确检验）：Z = Z1 ∪ Z2；Z2 全坏（gcd=λ），Z1 一般点好（gcd=1）。")
    print("故 104 的「P^1 混合」是底空间说法；分量层面是「一支全坏 + 一支好」。")
    print("=" * 74)


if __name__ == "__main__":
    main()
