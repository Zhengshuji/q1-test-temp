"""two_copy_gap.py —— 专家 2026-11-04 §8 第三项实验：两个 gap-2 例子的直和，检验阶差可加性

**构造**：把 gap-2 实例（$n=6,p=r=2$）与自身作直和：
$$A=A_1\\oplus A_1\\ (12\\times12),\\quad C=\\operatorname{diag}(C_1,C_1)\\ (4\\times12),\\quad
L_0=\\operatorname{diag}(L_{0,1},L_{0,1})\\ (4\\times12).$$
预期：代数最小阶 $q_0$ 加倍（$2\\times2=4$）；块对角增广 $\\mathcal L=L_1\\oplus L_1$（$4+4=8$ 行）可行。
**问题（Lemma A）**：是否存在**混合**（非块对角）增广以更低阶（$q<8$）可行？

**做法**：对 $q=q_0,\\dots,n_0-p$ 逐阶在图卡上采样（每参数取若干有理值），
用 B.12 可观性检验判 $(5b)$（比 Toeplitz 快两个数量级）。

用法：python -u tools/verification/two_copy_gap.py
"""

import os
import sys
import itertools
import random
from fractions import Fraction
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import observability_test as OT           # noqa: E402
import decide_symbolic as DS              # noqa: E402

F = Fraction

A1 = [[F(2), F(1), F(2), F(-1), F(2), F(-1)],
      [F(2), F(-2), F(1), F(-2), F(1), F(1)],
      [F(12), F(-8), F(-1), F(0), F(1), F(-1)],
      [F(6), F(-4), F(-2), F(2), F(2), F(-1)],
      [F(-2), F(1), F(0), F(2), F(1), F(2)],
      [F(1), F(-1), F(0), F(1), F(0), F(-1)]]
C1 = [[F(0), F(0), F(0), F(1), F(2), F(-2)],
      [F(0), F(0), F(-1), F(1), F(-2), F(2)]]
L01 = [[F(-6), F(9), F(8), F(-11), F(-2), F(-28)],
       [F(7), F(-8), F(-4), F(11), F(25), F(20)]]


def direct_sum(A, C, L0):
    n, p, r = len(A), len(C), len(L0)
    N = 2 * n
    AA = [[F(0)] * N for _ in range(N)]
    for i in range(n):
        for j in range(n):
            AA[i][j] = A[i][j]
            AA[n + i][n + j] = A[i][j]
    CC = [[F(0)] * N for _ in range(2 * p)]
    for i in range(p):
        for j in range(n):
            CC[i][j] = C[i][j]
            CC[p + i][n + j] = C[i][j]
    LL = [[F(0)] * N for _ in range(2 * r)]
    for i in range(r):
        for j in range(n):
            LL[i][j] = L0[i][j]
            LL[r + i][n + j] = L0[i][j]
    return AA, CC, LL


def search_order(A, C, L0, q, trials_per_chart=6, rng=None):
    """在 q 阶采样：返回 (测试数, 可行数, 一个可行见证或 None)。"""
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    if not K or not K[0]:
        return 0, 0, None
    k = len(K[0])
    if d <= 0 or d > k:
        return 0, 0, None
    nv = d * (k - d)
    tot = feas = 0
    witness = None
    for rows in itertools.combinations(range(k), d):
        ths = [[F(b)] * nv for b in range(trials_per_chart)]
        for _ in range(trials_per_chart):
            ths.append([F(rng.randrange(-4, 5)) for _ in range(nv)])
        for th in ths:
            Z = DS.Z_from_theta(A, C, L0, q, rows, th)
            if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                continue
            L = ZG.L_from_Z(A, C, L0, Z, q)
            if L is None or not LQ.condA(A, C, L):
                continue
            tot += 1
            ok, _ = OT.observability_ok(A, C, L)
            if ok:
                feas += 1
                if witness is None:
                    witness = L
    return tot, feas, witness


def main():
    rng = random.Random(20261104)
    A, C, L0 = direct_sum(A1, C1, L01)
    n, p, r = len(A), len(C), len(L0)
    O = QR.observability_matrix(A, C)
    n0 = LQ.rank(O)
    print(f'直和实例：n={n}, p={p}, r={r}, 可观测指数 n0={n0}')
    try:
        q0 = Q0.eta_and_q0(A, C, L0)[0]
    except Exception as e:
        print('q0 计算失败：', type(e).__name__, e)
        return
    print(f'q0 = {q0}（单副本 q0 = 2，若可加则应为 4）；阶区间 [{q0}, {n0 - p}]')
    # 块对角见证（q = 4+4 = 8）：用单副本的 4 行见证拼起来
    R1 = [[F(0), F(1), F(4), F(-4), F(3), F(-1)],
          [F(-4), F(-2), F(-3), F(1), F(3), F(-1)]]
    L1 = [list(x) for x in L01] + R1
    # 拼成直和：12×12 的 L，行数 8
    N = 2 * 6
    Lblk = [[F(0)] * N for _ in range(8)]
    for i in range(4):
        for j in range(6):
            Lblk[i][j] = L1[i][j]
            Lblk[4 + i][6 + j] = L1[i][j]
    okA = LQ.condA(A, C, Lblk)
    okb, why = OT.observability_ok(A, C, Lblk)
    print(f'块对角见证（q=8）：(5a)={okA}，(5b)={okb}（{why}）')
    print()
    for q in range(q0, n0 - p + 1):
        tot, feas, wit = search_order(A, C, L0, q, trials_per_chart=5, rng=rng)
        print(f'  q={q}：测试 {tot} 个候选，可行 {feas}' + (f'（找到见证）' if wit else ''))


if __name__ == '__main__':
    main()
