r"""c289：$(2,4)$ 上 $\operatorname{rank}(Q|_K)=1$ 是否可能？（QA23 优先级 5 的收尾）

**问题**：A2 §29.2b 的负例分类表有一行"rank 1 ⟹ $a_0|_K\in\operatorname{span}\{L\}$"。
但 40 个随机实例里只出现 rank 2、3。**rank 1 到底可不可能？**

**几何理由**（若不可能）：$Q$ 是光滑的 Klein 二次超曲面。$\operatorname{rank}(Q|_K)=1$ 意味着
$Q\cap\mathbb P(K)$ 是**重超平面**（沿一个 $\mathbb P^2$ 相切），而光滑二次超曲面的 $\mathbb P^3$ 截面
奇点轨迹至多是一个点。所以 rank 1 **应该不可能**。

**做法**：大范围搜索（随机整数 + 结构化：含 $Q$ 的极大各向同性子空间），统计 $\operatorname{rank}(Q|_K)$。

用法：python proof/layer_program/c289_rank1_search.py
"""
import itertools
import os
import random
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))

import audit_independent as AI

PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def Q(p):
    p12, p13, p14, p23, p24, p34 = p
    return p12 * p34 - p13 * p24 + p14 * p23


def rank_restriction(K):
    d = len(K)
    M = [[Fr(0)] * d for _ in range(d)]
    for i in range(d):
        M[i][i] = 2 * Q(K[i])
        for j in range(i + 1, d):
            s = [K[i][k] + K[j][k] for k in range(6)]
            M[i][j] = M[j][i] = Q(s) - Q(K[i]) - Q(K[j])
    return AI.rank(M)


def main():
    rng = random.Random(20261031)
    counts = {}
    tried = 0
    for _ in range(3000):
        a1 = [Fr(rng.randint(-3, 3)) for _ in range(6)]
        a2 = [Fr(rng.randint(-3, 3)) for _ in range(6)]
        if all(x == 0 for x in a1) or all(x == 0 for x in a2):
            continue
        if AI.rank([a1, a2]) < 2:
            continue
        K = AI.nullspace([a1, a2])
        if len(K) != 4:
            continue
        tried += 1
        rk = rank_restriction(K)
        counts[rk] = counts.get(rk, 0) + 1

    print(f"随机搜索：{tried} 个 (2,4) 实例（K = ker{{a1,a2}}，dim 4）")
    print(f"rank(Q|_K) 分布：{counts}")
    print()

    # 结构化：含 Q 的极大各向同性子空间（Gr(2,4) 里的 ℙ²）
    # ℙ² 族 1：{U : e1 ⊂ U} 的 Plücker 坐标
    #   U = span(e1, v)，v ∈ span(e2,e3,e4)：p_ij 由 e1∧v 给出
    iso1 = []
    for j in (1, 2, 3):
        v = [Fr(0)] * 6
        # v = e_{j+1}（0-based index j）
        # U = span(e0, e_j)：p_{0,j} = 1
        v[PAIRS.index((0, j))] = Fr(1)
        iso1.append(v)
    # 加两个"额外"方向，凑成 4 维 K
    extra = [[Fr(1) if k == i else Fr(0) for k in range(6)] for i in (3, 4)]
    K1 = iso1 + extra
    if len(K1) == 4 and AI.rank(K1) == 4:
        print(f"结构化（含 ℙ² 族 1）：rank(Q|_K) = {rank_restriction(K1)}")

    # ℙ² 族 2：{U : U ⊂ e1,e2,e3}（含固定 3-空间）
    iso2 = []
    for j in (1, 2):
        v = [Fr(0)] * 6
        v[PAIRS.index((j, 2)) if j < 2 else PAIRS.index((0, 1))] = Fr(1)
        iso2.append(v)
    print()
    print("结论：若随机搜索从未出现 rank 1，则 (2,4) 上的负例**只能**来自 a_0|_K=0（即 a_0 in span{a_j}），")
    print("§29.2b 表中 rank=1 那一行在 (2,4) 上是**空的**——这是一个更强的定理。")


if __name__ == '__main__':
    main()
