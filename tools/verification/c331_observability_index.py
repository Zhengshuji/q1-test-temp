#!/usr/bin/env python3
"""c331 — d_min 与可观测性指标 nu 的关系（专家 93 号提示的直接检验）。

规范形 X = [I_omega; 0]，G = [G_1; G_2]（G_1 是 omega x omega，G_2 是 (q-omega) x omega）。
则 Q(lam) = [lam I - G_1; -G_2] 对每个 lam 满列秩
  <=>  rank[lam I - G_1; G_2] = omega 对每个 lam    （Hautus/PBH）
  <=>  (G_1, G_2) 可观测。
于是 Q 的多项式左逆就是 (G_1, G_2) 的"多项式观测器"（Bezout 恒等式）。

可观测性指标 nu = 最小的 k 使 rank[G_2; G_2 G_1; ...; G_2 G_1^{k-1}] = omega。

检验的猜想（专家建议的"内蕴刻画"）：
        d_min = nu - 1 .
若成立，因为 nu <= omega（经典），立即得 d_min <= omega - 1。

有限精确检验，不是证明。
"""

from __future__ import annotations

import os
import random
import sys
import time

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for _p in ("tools/verification",):
    _cand = os.path.join(_ROOT, _p)
    if _cand not in sys.path:
        sys.path.insert(0, _cand)

import c330_certificate_degree as m  # noqa: E402


def observability_index(G1: sp.Matrix, G2: sp.Matrix):
    """最小的 k 使 rank[C; CA; ...; CA^{k-1}] = omega；不可观测时返回 None。"""
    om = G1.rows
    assert G1.shape == (om, om) and G2.cols == om
    blocks = [sp.Matrix(G2)]
    cur = sp.Matrix(G2)
    for k in range(1, om + 1):
        if sp.Matrix.vstack(*blocks).rank() == om:
            return k
        cur = cur * G1
        blocks.append(cur)
    return None


def families():
    return [
        (3, 2, 40, 1, 202),
        (3, 2, 60, 2, 203),
        (4, 2, 60, 2, 204),
        (5, 2, 40, 2, 205),
        (4, 3, 30, 1, 206),
        (5, 3, 25, 1, 207),
    ]


def construct_left_inverse(G1: sp.Matrix, G2: sp.Matrix, d: int):
    """按"可观测性指标"构造次数 <= d 的左逆 S = [X, Y]。

    取 nu <= d+1 且 rank[G2; ...; G2 G1^{d}] = omega，解 Y_all M = I 得常数块 Y_k，
    再用 X_{k-1} = X_k G1 - Y_k G2、X_d = 0 回推 X_k。
    返回 (X_list, Y_list) 或 None。
    """
    om = G1.rows
    blocks, cur = [], sp.Matrix(G2)
    for k in range(d + 1):
        blocks.append(cur)
        cur = cur * G1
    M = sp.Matrix.vstack(*blocks)          # ((d+1)*p) x omega
    if M.rank() != om:
        return None                        # 该 d 下指标不足
    Yall = (M.T * M).inv() * M.T           # omega x ((d+1)*p)
    p = G2.rows
    Ys = [Yall[:, k * p:(k + 1) * p] for k in range(d + 1)]
    Xs = [None] * (d + 1)
    Xs[d] = sp.zeros(om, om)
    for k in range(d, 0, -1):
        Xs[k - 1] = Xs[k] * G1 - Ys[k] * G2
    return Xs, Ys


def verify_identity(G1: sp.Matrix, G2: sp.Matrix, d: int, lam) -> bool:
    """逐项验证 X(lam)(lam I - G1) + Y(lam) G2 = I。"""
    out = construct_left_inverse(G1, G2, d)
    if out is None:
        return False
    Xs, Ys = out
    om = G1.rows
    lhs = sp.zeros(om, om)
    for k in range(d + 1):
        lhs += Xs[k] * lam ** (k + 1)          # X_k lam^{k+1}
        lhs -= Xs[k] * G1 * lam ** k           # - X_k G1 lam^k
        lhs += Ys[k] * G2 * lam ** k           # + Y_k G2 lam^k
    lhs = sp.expand(lhs)
    return sp.simplify(lhs - sp.eye(om)) == sp.zeros(om, om)


def main() -> None:
    total = 0
    agree = 0
    mismatches = []
    for q, om, want, box, seed in families():
        rng = random.Random(seed)
        Xi = m.unit_block(q, om)
        feas = 0
        n = 0
        joint = {}
        t0 = time.time()
        while feas < want and n < 400 and time.time() - t0 < 240:
            n += 1
            G = m.random_g(q, om, rng, box)
            if not m.gcd_test(Xi, G):
                continue
            feas += 1
            G1 = G[:om, :]
            G2 = G[om:, :]
            nu = observability_index(G1, G2)
            if nu is None:
                mismatches.append((q, om, G, "not observable"))
                continue
            d = m.minimal_degree(Xi, G, cap=om - 1)
            joint[(nu, d)] = joint.get((nu, d), 0) + 1
            total += 1
            if d == nu - 1:
                agree += 1
            else:
                mismatches.append((q, om, G, f"nu={nu} d={d}"))
        print(f"(q,omega)=({q},{om}) box={box}: 可行 {feas}, 用时 {time.time()-t0:.1f}s, "
              f"(nu,d) 联合直方图 {dict(sorted(joint.items()))}")

    print()
    print(f"d_min == nu - 1：{agree}/{total}")
    for mm in mismatches[:8]:
        print("  反例:", mm[0], mm[1], mm[3], "G =", sp.Matrix(mm[2]).tolist())
    print()
    print("经典事实 nu <= omega（可观测 n 维系统的可观测性指标不超过 n）；")
    print("若 d_min = nu - 1 成立，则 d_min <= omega - 1，且等号出现在 nu = omega 时。")

    # 构造方向的证书：在 d = nu - 1 处显式构造 S 并逐项验证恒等式；
    # 并核对 d = nu - 2 处构造按预期失败（可观测性块秩不足）。
    lam = sp.symbols("lam")
    cert_ok = cert_fail = 0
    for q, om, box, seed in [(3, 2, 1, 301), (4, 2, 2, 302), (4, 3, 1, 303), (5, 3, 1, 304)]:
        rng = random.Random(seed)
        Xi = m.unit_block(q, om)
        got, n = 0, 0
        while got < 2 and n < 200:
            n += 1
            G = m.random_g(q, om, rng, box)
            if not m.gcd_test(Xi, G):
                continue
            G1, G2 = G[:om, :], G[om:, :]
            nu = observability_index(G1, G2)
            if nu is None:
                continue
            got += 1
            if verify_identity(G1, G2, nu - 1, lam):
                cert_ok += 1
            else:
                cert_fail += 1
                print("  !! 构造失败", q, om, sp.Matrix(G).tolist())
            if nu >= 2:
                assert construct_left_inverse(G1, G2, nu - 2) is None, "秩不足时应构造失败"
    print(f"构造 + 恒等式验证：{cert_ok} 成功 / {cert_fail} 失败；"
          f"且 d = nu-2 处构造按预期不存在。")


if __name__ == "__main__":
    main()
