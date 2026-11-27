"""c171_cyclic_cover.py — CYCLIC-COVER 的小规模实验

问题：给定线性拟阵 M（n 个元素，秩 r）与 S0，求
    min |S|  s.t.  S ⊇ S0 且 S 无 coloop（即 S 是并环集）。

本脚本：
  1. 随机线性拟阵（n=5,6）；
  2. 穷举所有 S0，用暴力求最优；
  3. 与"贪心"比较（每次给一个 coloop 补一个含它的最小环）；
  4. 看贪心是否总最优；若不然，打印反例。

用法：python q1_true/scripts/c171_cyclic_cover.py
"""
import sys
import os
import itertools
import random

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "scripts", "core"))

from fractions import Fraction as Fr
import audit_independent as AI


def rank_of(S, cols):
    if not S:
        return 0
    return len(AI.row_basis([cols[e] for e in S]))


def make_matroid(n, r, seed):
    rng = random.Random(seed)
    # 每列是 r 维向量，用行表示
    rows = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(r)]
    rows = AI.row_basis(rows)
    cols = [[rows[i][j] for i in range(len(rows))] for j in range(n)]
    return cols


def is_cyclic(S, cols):
    if not S:
        return True
    rS = rank_of(S, cols)
    return all(rank_of([x for x in S if x != e], cols) == rS for e in S)


def circuits(cols, n):
    out = []
    for k in range(1, n + 1):
        for C in itertools.combinations(range(n), k):
            rC = rank_of(C, cols)
            if rC == k:
                continue
            if all(rank_of([x for x in C if x != e], cols) == k - 1 for e in C):
                out.append(frozenset(C))
    return out


def brute(S0, cols, n):
    S0 = frozenset(S0)
    for k in range(len(S0), n + 1):
        for extra in itertools.combinations([x for x in range(n) if x not in S0], k - len(S0)):
            S = S0 | frozenset(extra)
            if is_cyclic(S, cols):
                return k, S
    return None, None


def greedy(S0, cols, cirs, n):
    S = frozenset(S0)
    for _ in range(n + 1):
        rS = rank_of(S, cols)
        coloops = [e for e in S if rank_of([x for x in S if x != e], cols) < rS]
        if not coloops:
            return len(S), S
        e = coloops[0]
        cands = [C for C in cirs if e in C]
        if not cands:
            return None, None
        best = min(cands, key=lambda C: len(S | C))
        S = S | best
    return len(S), S


def main():
    for (n, r, seed) in [(5, 2, 1), (5, 3, 2), (6, 2, 3), (6, 3, 4)]:
        cols = make_matroid(n, r, seed)
        cirs = circuits(cols, n)
        print("=" * 60)
        print("n", n, "r", r, "seed", seed, "circuits", len(cirs))
        bad = 0
        for k in range(n + 1):
            for S0 in itertools.combinations(range(n), k):
                opt, _ = brute(S0, cols, n)
                g, _ = greedy(S0, cols, cirs, n)
                if opt != g:
                    bad += 1
                    if bad <= 5:
                        print("  贪心失败 S0=", S0, "opt=", opt, "greedy=", g)
        print("  贪心与最优不一致:", bad, "/", 2 ** n)


if __name__ == "__main__":
    main()
