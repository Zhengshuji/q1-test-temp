#!/usr/bin/env python3
"""c340 — 符号证书的族级推广：多个 $A$（均带 $A e_1=\\lambda_0 e_1$）上，$t$ 仍为符号。

设置：$n=5$, $p=1$, $C=e_5^{\\mathsf T}$；$A$ 的第一列为 $(\\lambda_0,0,0,0,0)$，其余条目随机。
$U=\\operatorname{span}(e_1)$、$U^\\perp=e_1^\\perp$（基 $e_2,e_3,e_4,e_5$）。
行空间取 $V_t=\\langle e_2,e_3,e_4+t e_5\\rangle$，$L_t=[e_2;e_3;e_4+t e_5]$。

对每个 $A$：在 $\\mathbb Q(t)[\\lambda]$ 上算 $\\lambda H_t-H_{A,t}$ 的 2-子式 gcd，看是否恒为 1。
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

lam, t = sp.symbols("lam t")


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
    return sp.simplify(g)


def main() -> None:
    print("=" * 74)
    print("族级符号证书：多个 A（A e1 = lam0 e1），t 为符号")
    print("=" * 74)
    C = sp.Matrix([[0, 0, 0, 0, 1]])
    e = [sp.eye(5)[:, i].T for i in range(5)]
    rng = random.Random(340)
    ok = 0
    tried = 0
    for trial in range(12):
        lam0 = rng.choice([2, 3, -1, 5])
        A = sp.Matrix(5, 5, lambda i, j: rng.randint(-2, 2))
        for i in range(5):
            A[i, 0] = lam0 if i == 0 else 0
        W = sp.Matrix.vstack(C, C * A)
        if W.rank() != 2:
            continue
        N = m.ker_basis(W)
        if N.cols != 3:
            continue
        # 检查 e1 in K_0 且是特征向量
        e1 = sp.Matrix([1, 0, 0, 0, 0])
        if not (W * e1).is_zero_matrix:
            continue
        if not (A * e1 - lam0 * e1).is_zero_matrix:
            continue
        L = sp.Matrix.vstack(e[1], e[2], e[3] + t * e[4])
        H = L * N
        HA = L * A * N
        # 数值检查 rank H = 2、(5a)（取 t=1）
        H1 = H.subs(t, 1)
        if H1.rank() != 2:
            continue
        HA1 = HA.subs(t, 1)
        KH1 = m.ker_basis(H1)
        if not (HA1 * KH1).is_zero_matrix:
            continue
        tried += 1
        P = sp.Matrix(3, 3, lambda i, j: lam * H[i, j] - HA[i, j])
        g = gcd_of_minors(P, 2)
        deg = 0 if g in (0, 1) else sp.Poly(g, lam).degree()
        tag = "OK" if g == 1 else f"gcd={sp.sstr(g)}"
        print(f"  A#{trial} (lam0={lam0}): {tag}")
        if g == 1:
            ok += 1
        if tried >= 5:
            break
    print()
    print(f"  {ok}/{tried} 个 A 上整条 P^1 的 gcd 恒为 1")
    if ok == tried and tried > 0:
        print("  => 族级证据：这些 A 上都能给出符号证书（仍未证一般 A）")


if __name__ == "__main__":
    main()
