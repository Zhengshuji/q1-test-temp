#!/usr/bin/env python3
"""c338 — 搜"生成坏"的特征纤维（H4 的反例搜索）。

构造族：$n=5$, $p=1$, $C=e_5^{\\mathsf T}$, $A e_1=\\lambda_0 e_1$（第一列 $=(\\lambda_0,0,0,0,0)$），
故 $C e_1=0$、$CA e_1=0$，于是 $e_1\\in K_0$ 且是特征向量。

特征纤维：$v=e_1$、$U=\\operatorname{span}(e_1)$、$U^\\perp=e_1^\\perp$（4 维）；
自由行（$r_0=0$ 时 3 行）取 $U^\\perp$ 里的随机组合，要求 $\\operatorname{rank}H=k-1=2$ 且 $(5a)$ 成立。

对每个 $A$ 取若干组行，算 $\\lambda H-H_A$ 的 2-子式 gcd：
  * 只要出现一个 gcd=1 的点，该分量就**生成好**（坏集闭 + 不可约）；
  * 若一个 $A$ 下**全部**样本都是坏，则该特征纤维"生成坏"的候选（需更多样本确认）。
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


def gcd_of_minors(P, r):
    P = sp.Matrix(P)
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


def try_instance(A, C, lam0, samples, rng):
    n = A.rows
    W = sp.Matrix.vstack(C, C * A)
    if W.rank() != 2:
        return None
    N = m.ker_basis(W)
    if N.cols != 3:
        return None
    v = sp.Matrix([1, 0, 0, 0, 0])
    if not (W * v).is_zero_matrix and False:
        pass
    if not (C * v).is_zero_matrix:
        return None
    Q = m.orth_basis([v])
    k = N.cols
    good = bad = skipped = 0
    for _ in range(samples):
        L = sp.Matrix(3, n, lambda i, j: sum(rng.randint(-2, 2) * Q[b, j] for b in range(Q.rows)))
        H = L * N
        if H.rank() != k - 1:
            skipped += 1
            continue
        HA = L * A * N
        KH = m.ker_basis(H)
        if not (HA * KH).is_zero_matrix:
            skipped += 1
            continue
        P = sp.Matrix(H.rows, k, lambda i, j: lam * H[i, j] - HA[i, j])
        g = gcd_of_minors(P, 2)
        deg = 0 if g in (0, 1) else sp.Poly(g, lam).degree()
        if deg == 0:
            good += 1
        else:
            bad += 1
    return good, bad, skipped


def main() -> None:
    print("=" * 74)
    print("搜「生成坏」的特征纤维：A e1 = lam0 e1, C = e5^T, r_0 = 0")
    print("=" * 74)
    C = sp.Matrix([[0, 0, 0, 0, 1]])
    rng = random.Random(338)
    allbad = []
    for t in range(10):
        lam0 = rng.choice([2, 3, -1])
        A = sp.Matrix(5, 5, lambda i, j: rng.randint(-2, 2))
        for i in range(5):
            A[i, 0] = lam0 if i == 0 else 0
        r = try_instance(A, C, lam0, samples=12, rng=rng)
        if r is None:
            continue
        good, bad, skip = r
        tag = ""
        if good == 0 and bad > 0:
            allbad.append(A)
            tag = "   <== 候选：全坏"
        print(f"  A#{t} (lam0={lam0}): 好 {good} / 坏 {bad} / 跳过 {skip}{tag}")
    print()
    if allbad:
        print(f"  有 {len(allbad)} 个 A 下全部样本都坏——H4 的候选反例，需换更多样本/换行空间确认。")
    else:
        print("  没有找到全坏的 A：每个实例都出现了好点 ⟹ 这些特征纤维都生成好（H4 未被推翻）。")


if __name__ == "__main__":
    main()
