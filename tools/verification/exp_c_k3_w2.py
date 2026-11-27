r"""实验 C（续）：在**最后战场** $k=3$、$\omega=2$、$k>\omega$ 上搜索"坏的可容许分量"。

设定：$n=5$、$p=1$、$q=3$、$r=1$ ⟹ $k=5-\operatorname{rank}[C;CA]=5-2=3$、$m=q-r=2$。
$C=e_1^{\mathsf T}$；$A$ 第一行 $=e_5^{\mathsf T}$（使 $CA=e_5^{\mathsf T}$ ⟹ $K=\langle e_2,e_3,e_4\rangle$），其余行随机。
$R$ 为 $2\times5$ 共 10 个条目；随机采样 $R\in\{-2,\dots,2\}^{10}$。

每个采样点用 `consistency_checks.check_candidate` 精确判定（含 $(5a)$、$(5b)$），并记录 $\omega=\operatorname{rank}H$。
统计每个实例在 $\omega=2$ 上：可容许点数、好点数、坏点数。

注意：$q=3$、$\omega=2$ 时降阶铅笔是 $3\times2$（非方阵）⟹ 可行**不**被方阵障碍排除。
"""

import os
import sys
import itertools
import random
from fractions import Fraction as Fr

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ              # noqa: E402
import consistency_checks as CC    # noqa: E402

F = Fr


def rank(M):
    return LQ.rank(M) if M else 0


def main():
    n, p, q, r = 5, 1, 3, 1
    C = [[F(1), F(0), F(0), F(0), F(0)]]
    rng = random.Random(20261112)
    n_inst = 0
    stats = {'adm_none': 0, 'all_bad': 0, 'has_good': 0}
    rows = []
    while n_inst < 6:
        A = [[F(0), F(0), F(0), F(0), F(1)]]      # 第一行 = e5
        for i in range(1, n):
            A.append([F(rng.randrange(-1, 2)) for _ in range(n)])
        M = C + LQ.mul(C, A)
        if n - rank(M) != 3:
            continue
        NK = LQ.ker_basis_cols(M)
        L0 = [[F(0), F(0), F(0), F(0), F(1)]]      # L0 = e5
        n_inst += 1
        ngood = nbad = nadm = 0
        for _ in range(600):
            Rv = [F(rng.randrange(-2, 3)) for _ in range((q - r) * n)]
            R = [[Rv[i * n + j] for j in range(n)] for i in range(q - r)]
            L = [row[:] for row in L0] + [row[:] for row in R]
            H = LQ.mul(L, NK)
            if rank(H) != 2:
                continue
            H_A = LQ.mul(LQ.mul(L, A), NK)
            stacked = [row[:] for row in H] + [row[:] for row in H_A]
            if rank(stacked) != 2:
                continue
            nadm += 1
            try:
                res = CC.check_candidate(A, C, L0, L)
                ok = isinstance(res, dict) and res.get('five_b')
            except Exception:
                continue
            if ok:
                ngood += 1
            else:
                nbad += 1
        if nadm == 0:
            stats['adm_none'] += 1
        elif ngood == 0:
            stats['all_bad'] += 1
        else:
            stats['has_good'] += 1
        rows.append((nadm, ngood, nbad))
    print(f'实例数 {n_inst}（n=5,p=1,q=3,r=1 ⟹ k=3, omega=2；每实例 600 个随机 R）')
    for i, (nadm, ngood, nbad) in enumerate(rows, 1):
        print(f'  实例 {i}: 可容许(rank H=2 且 ker 包含) {nadm} 个 → 好 {ngood} / 坏 {nbad}')
    print(f'汇总: 可容许集空 {stats["adm_none"]} · 全坏 {stats["all_bad"]} · 有好点 {stats["has_good"]}')


if __name__ == '__main__':
    main()
