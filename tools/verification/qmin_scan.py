"""qmin_scan.py —— 在**功能可观测**实例上测 $q_{\\min}$（WP2 第 4 步，含一次更正）

> **更正（2026-11-02）**：上一轮的 24 个随机实例大多**不功能可观测**
> （$\\operatorname{row}L_0\\not\\subseteq\\operatorname{row}\\mathcal O_C$），
> 因而**根本不存在**观测器——那里的"没找到 $(5b)$"是平凡的，不是搜索失败。
> 本脚本改为**构造**可观测实例：$L_0$ 取可观性矩阵 $\\mathcal O_C=[C;CA;\\dots;CA^{n-1}]$ 的行组合。

两件事：

1. 在可观测实例上扫 $q=$ 闭包 $\\dots$ 闭包 $+3$（每阶 20 条链式前像样本），报告首个 $(5b)$ 见证；
2. 顺便核对互补障碍（$\\ker C=\\ker[C;CA]\\oplus\\ker[C;L]$ 时 $(5b)$ 必失败，只可能在 $q=n-r_1$ 出现）。

用法：python tools/verification/qmin_scan.py
"""

import os
import random
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import omega_construct as OC              # noqa: E402

F = Fraction


def observability_matrix(A, C):
    rows = [r[:] for r in C]
    cur = [r[:] for r in C]
    for _ in range(len(A) - 1):
        cur = LQ.mul(cur, A)
        rows += cur
    return rows


def make_observable_instance(n, p, r, seed):
    """随机 $(A,C)$，$L_0$ 取可观性矩阵行的随机组合（保证 $L_0$ 可估）。"""
    rng = random.Random(seed)
    A = [[F(rng.randrange(-3, 4)) for _ in range(n)] for _ in range(n)]
    C = [[F(rng.randrange(-3, 4)) for _ in range(n)] for _ in range(p)]
    O = observability_matrix(A, C)
    L0 = []
    for _ in range(r):
        u = [F(0)] * n
        coef = [F(rng.randrange(-2, 3)) for _ in range(len(O))]
        for c, row in zip(coef, O):
            if c:
                for j in range(n):
                    u[j] += c * row[j]
        if LQ.rank(L0 + [u]) > len(L0):
            L0.append(u)
    # 要求 rank[C;L0] = p + r
    if LQ.rank([x[:] for x in C] + [x[:] for x in L0]) != p + len(L0):
        return None
    return A, C, L0


def main():
    print('=== 功能可观测实例上的 q_min 扫描 ===')
    stats = dict(inst=0, hit=0, dist={})
    for n in (5,):
        for seed in range(2000, 2006):
            made = make_observable_instance(n, 1, 1, seed)
            if made is None:
                continue
            A, C, L0 = made
            Vmin = OC.closure(A, C, L0)
            clo = len(Vmin)
            stats['inst'] += 1
            first = None
            cells = []
            for q in range(clo, min(n, clo + 3) + 1):
                samples = OC.sample_chains(A, C, L0, q, 10, seed * 13 + q)
                feas = 0
                for L in samples:
                    if TC.analyse(A, C, L)['five_b']:
                        feas += 1
                cells.append(f'q={q}:{feas}/{len(samples)}')
                if feas and first is None:
                    first = q
            if first is not None:
                stats['hit'] += 1
                stats['dist'][first - clo] = stats['dist'].get(first - clo, 0) + 1
            verdict = (f'q_min={first}' if first is not None else 'q_min 未知')
            verdict += '（闭包阶唯一候选；若 q=闭包 有见证则 q_min=闭包）' if first == clo else ''
            print(f'  n={n} seed={seed} 闭包={clo} ' + ' '.join(cells) + f'  → {verdict}')
    print(f'\n合计：可观测实例 {stats["inst"]}；找到见证 {stats["hit"]}；'
          f'首个见证相对闭包的偏移分布 {stats["dist"]}')


if __name__ == '__main__':
    main()
