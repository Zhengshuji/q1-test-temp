"""c174_n5_counterexample.py — n=5 上继续搜 (T) 的反例（J 可实现）

(T)：min_V dim V = min_{坐标 V} dim V。

对每个随机可实现实例（A 对角互异、J = row[C;CA]、K0 = span{e_0}），
算 q_coord；若 q_coord >= 3，则搜 dim-2 的 V = span{e_0,u}；
若 q_coord >= 4，再搜 dim-3 的 V = span{e_0,u,w}。
出现更小的可行维数即为反例。

用法：python q1_true/scripts/c174_n5_counterexample.py
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
import c170_matroid_check as C170

mul, rank = AI.mul, AI.rank


def conds(L, A, J):
    LA = mul(L, A)
    if rank(AI.vstack([LA, L, J])) != rank(AI.vstack([L, J])):
        return False
    return C170.cond5b_with_J(L, A, J) == 0


def q_coord_of(A, J, n):
    for k in range(1, n + 1):
        for S in itertools.combinations(range(n), k):
            if 0 not in S:
                continue
            L = [[Fr(1) if j == i else Fr(0) for j in range(n)] for i in S]
            if conds(L, A, J):
                return k
    return None


def main():
    rng = random.Random(1)
    n = 5
    A = [[Fr(i + 1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    K0 = [Fr(1)] + [Fr(0)] * (n - 1)
    stats = {}
    counter = []
    checked = 0
    for trial in range(40):
        p = rng.choice([1, 2])
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        J = AI.row_basis(C + mul(C, A))
        qc = q_coord_of(A, J, n)
        stats[qc] = stats.get(qc, 0) + 1
        if qc is None or qc <= 2:
            continue
        checked += 1
        hit = None
        for _ in range(400):
            u = [Fr(rng.randint(-2, 2)) for _ in range(n)]
            L = [K0[:], u]
            if rank(L) == 2 and conds(L, A, J):
                hit = (2, u)
                break
        if hit is None and qc >= 4:
            for _ in range(200):
                u = [Fr(rng.randint(-2, 2)) for _ in range(n)]
                w = [Fr(rng.randint(-2, 2)) for _ in range(n)]
                L = [K0[:], u, w]
                if rank(L) == 3 and conds(L, A, J):
                    hit = (3, u, w)
                    break
        if hit is not None:
            counter.append((trial, qc, hit))
    print("q_coord 分布:", stats)
    print("q_coord>=3 的实例数:", checked)
    print("找到反例:", len(counter))
    for t, qc, hit in counter[:5]:
        print("   trial", t, "q_coord", qc, "hit dim", hit[0])


if __name__ == "__main__":
    main()
