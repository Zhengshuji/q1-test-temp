r"""实验 C（专家清单）：在 $k>\omega$ 的最小情形（$k=2$、$\omega=1$）搜索"坏的可容许分量"。

$\omega=1$ 时专家的判据是 $(5b)\iff\operatorname{rank}[H\ H_A]=2$（$H=uv^{\mathsf T}$、$H_A=gv^{\mathsf T}$ ⟹
$\operatorname{rank}[H\ H_A]=\operatorname{rank}[u\ g]$）。
可容许 = $\operatorname{rank}H=1$ 且 $\ker H\subseteq\ker H_A$（即 $\operatorname{row}H_A\subseteq\operatorname{row}H$）。

对每个实例枚举 $R\in\{-1,0,1\}^{n}$，统计：
  * 可容许点数；其中 "好"（$\operatorname{rank}[H\ H_A]=2$）与 "坏"（$=1$）各多少。
据专家清单：
  * 若某实例**可容许但全坏** ⟹ 存在坏的可容许分量（硬度的靶子）；
  * 若所有实例都"有好点" ⟹ 支持可解性猜想。
"""

import itertools
import os
import sys
from fractions import Fraction as Fr

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ   # noqa: E402

F = Fr


def rank(M):
    return LQ.rank(M) if M else 0


def classify(A, C, L0, R, NK):
    """返回 ('inadmissible', None) 或 ('admissible', good_bool)。"""
    n = len(A)
    L = [row[:] for row in L0] + [row[:] for row in R]
    H = LQ.mul(L, NK)
    H_A = LQ.mul(LQ.mul(L, A), NK)
    if rank(H) != 1:
        return 'inadmissible', None
    # 可容许：row H_A ⊆ row H  ⟺  rank[H; H_A] == rank H == 1
    stacked = [row[:] for row in H] + [row[:] for row in H_A]
    if rank(stacked) != 1:
        return 'inadmissible', None
    # 好/坏：rank[H | H_A]
    side = [row[:] + HArow[:] for row, HArow in zip(H, H_A)]
    good = (rank(side) == 2)
    return 'admissible', good


def main():
    import random
    rng = random.Random(20261111)
    vals = (-1, 0, 1)
    n, p = 4, 1
    C = [[F(1), F(0), F(0), F(0)]]
    n_inst = 0
    both = bad_only = good_only = admissible_none = 0
    examples_bad, examples_mixed = [], []
    trials = 0
    while n_inst < 30 and trials < 4000:
        trials += 1
        A = [[F(0), F(0), F(0), F(1)]]   # 第一行 = e4，使 CA = e4^T、K = <e2,e3>
        for i in range(1, n):
            A.append([F(rng.randrange(-1, 2)) for _ in range(n)])
        M = C + LQ.mul(C, A)
        k = n - rank(M)
        if k != 2:
            continue
        NK = LQ.ker_basis_cols(M)
        if not NK or len(NK[0]) != 2:
            continue
        for i in range(n):
            L0 = [[F(1) if j == i else F(0) for j in range(n)]]
            n_inst += 1
            ngood = nbad = 0
            for Rv in itertools.product(vals, repeat=n):
                R = [[F(x) for x in Rv]]
                tag, good = classify(A, C, L0, R, NK)
                if tag != 'admissible':
                    continue
                if good:
                    ngood += 1
                else:
                    nbad += 1
            if ngood + nbad == 0:
                admissible_none += 1
            elif ngood == 0:
                bad_only += 1
                if len(examples_bad) < 2:
                    examples_bad.append((A, L0, nbad))
            elif nbad == 0:
                good_only += 1
            else:
                both += 1
                if len(examples_mixed) < 2:
                    examples_mixed.append((A, L0, ngood, nbad))
    print(f'检查实例 {n_inst} 个（k=2, omega=1, q=2, r=1, L0=e_i, n=4；A 随机）')
    print(f'  可容许集为空：{admissible_none}')
    print(f'  可容许但**全坏**（坏分量可存在）：{bad_only}')
    print(f'  可容许且**全好**：{good_only}')
    print(f'  同一实例**既有好点又有坏点**：{both}')
    for A, L0, nb in examples_bad:
        print('  全坏例：A=', [[int(x) for x in r] for r in A], ' L0=', [[int(x) for x in r] for r in L0], ' 坏点=', nb)
    for A, L0, ng, nb in examples_mixed:
        print('  混合例：A=', [[int(x) for x in r] for r in A], ' L0=', [[int(x) for x in r] for r in L0], f' 好={ng} 坏={nb}')


if __name__ == '__main__':
    main()
