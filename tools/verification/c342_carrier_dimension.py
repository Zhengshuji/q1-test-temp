#!/usr/bin/env python3
"""c342 — ARM 翻译的载体维数必要条件 $n \\le d_0 = 2k-\\delta$ 的核对。

q1 的自由行只通过 $\\Phi = R[N\\ AN] \\in \\mathbb C^{m\\times d_0}$ 进入条件，
$d_0 = \\dim\\operatorname{row}[N\\ AN] = 2k-\\delta$，$\\delta=\\dim(K_0\\cap A^{-1}K_0)$。
若要把 ARM 的 $X\\in\\mathbb R^{m\\times n}$ 用 $\\Phi$ **线性**编码，需要 $n\\le d_0$。

本脚本在若干 $(n,p)$ 模式上算 $d_0$，并输出 $n\\le d_0$ 是否成立。
"""

from __future__ import annotations

import os
import random
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import c335_lambda_movement as m  # noqa: E402


def one(n: int, p: int, seed: int):
    rng = random.Random(seed)
    A = sp.Matrix(n, n, lambda i, j: rng.randint(-2, 2))
    C = sp.zeros(p, n)
    for i in range(p):
        C[i, n - p + i] = 1
    W = sp.Matrix.vstack(C, C * A)
    r = W.rank()
    if r >= n:
        return None
    N = m.ker_basis(W)
    k = N.cols
    T = sp.Matrix.hstack(N, A * N)   # n x 2k
    d0 = T.rank()
    delta = 2 * k - d0
    return dict(n=n, p=p, r=r, k=k, d0=d0, delta=delta, ok=(n <= d0))


def main() -> None:
    print("=" * 74)
    print("载体维数：$n \\le d_0 = 2k-\\delta$ ?")
    print("=" * 74)
    print(f"  {'n':>2} {'p':>2} {'rank[C;CA]':>10} {'k':>2} {'d0':>3} {'n-p':>3}  d0<=n-p?")
    bad = 0
    tot = 0
    for n, p in [(5, 1), (6, 1), (6, 2), (7, 2), (8, 2), (8, 1), (10, 2)]:
        for seed in range(40):
            res = one(n, p, seed)
            if res is None:
                continue
            ok = res["d0"] <= n - p
            print(f"  {res['n']:>2} {res['p']:>2} {res['r']:>10} {res['k']:>2} "
                  f"{res['d0']:>3} {n - p:>3}   {ok}")
            tot += 1
            if not ok:
                bad += 1
            break
    print()
    print(f"  共 {tot} 个模式；其中 {bad} 个违反 $d_0\\le n-p$")
    print("  命题：C 消去 [N AN] 的所有列 => 列落在 ker C（n-p 维）=> d0 <= n-p")


if __name__ == "__main__":
    main()
