r"""**反例**：宽矩阵情形下，"$h=n-p\Rightarrow(S)$ 必失败"是**错的**。

上一轮 [../h_bound/README.md](../h_bound/README.md) 的定理（$h=n-p\Rightarrow(S)$ 失败）只在**方阵情形**成立：
当 $(n-r_1)+d>h$ 时，极大子式不是单个行列式，定理的论证失效。

本脚本在 $n=5,p=1,r=1,q=2$ 上随机搜索，找到并固定一个反例：
$h=n-p=4$ 且精确 $(S)$ 成立（gcd 为常数）。它同时说明"可行 $\Rightarrow h<n-p$"**不能**作为普遍必要条件。

用法：python proof/layer_program/c217_wide_counterexample.py
"""
import random
import sys
import os
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import spectral_gcd as SG


def main():
    rng = random.Random(2026)
    n, p, r, q = 5, 1, 1, 2
    for trial in range(200):
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        L0 = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(r)]
        CA = AI.mul(C, A)
        r1 = AI.rank(AI.vstack([C, CA]))
        if r1 == n:
            continue
        KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L0)])
        m_L, d = len(KLv), n - p - q
        if m_L < d:
            continue
        KL = [[KLv[k][i] for k in range(m_L)] for i in range(n)]
        Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
        Vrows = [[Vv[k][i] for k in range(len(Vv))] for i in range(n)]
        for _ in range(4):
            I = tuple(sorted(rng.sample(range(m_L), d)))
            theta = [[Fr(rng.randint(-3, 3)) for _ in range(d)] for _ in range(m_L - d)]
            W = [[Fr(0)] * d for _ in range(m_L)]
            Iset = set(I)
            for a, ri in enumerate(I):
                W[ri][a] = Fr(1)
            free = [x for x in range(m_L) if x not in Iset]
            for a, ri in enumerate(free):
                for b in range(d):
                    W[ri][b] = theta[a][b]
            Z = AI.mul(KL, W)
            if AI.rank(Z) < d:
                continue
            h = AI.rank([Vrows[i] + list(Z[i]) for i in range(n)])
            if h != n - p:
                continue
            g, h2, _ = SG.spectral_gcd_Z(A, C, Z)
            if SG.pdeg(g) == 0:
                ncols = (n - r1) + d
                print(f'找到反例（trial {trial}）：n={n}, p={p}, r1={r1}, d={d}, h={h}=n-p, 列数={ncols}（宽）')
                print(f'  A = {[[str(x) for x in row] for row in A]}')
                print(f'  C = {[[str(x) for x in row] for row in C]}')
                print(f'  L0 = {[[str(x) for x in row] for row in L0]}')
                print(f'  Z 的列：{[[str(Z[i][j]) for j in range(d)] for i in range(n)]}')
                print(f'  gcd = {g}（常数）⟹ (A)?（未检查）+ (S) 成立，且 h = n-p')
                print('\n⟹ "h=n-p ⟹ (S) 必失败"在宽矩阵情形**不成立**；"可行 ⟹ h<n-p"不是普遍必要条件 ✗')
                return
    print('未找到（提高 trial 数）')


if __name__ == '__main__':
    main()
