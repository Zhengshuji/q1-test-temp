"""c172_coordinate_vs_full.py — 非坐标 V 会不会比坐标 V 更好？

设 A = diag(1..n)（互异）、J 随机、K0 = span{e_0}。
- q_coord：坐标 V = span{e_i : i in S} 中的最小 |S|（用拟阵条件 / 直接判 (5b)）；
- q_full ：在 V = span{e_0, u}（u 取小整数格点）里搜，看是否有 dim 2 的可行解。

若 q_full < q_coord，则 MIN-ROWS 严格松于 CYCLIC-COVER —— "逼成坐标"不可能靠这个方向。

用法：python q1_true/scripts/c172_coordinate_vs_full.py
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
    """(5a) 与 (5b)，J 直接给（不要求来自 C）"""
    n = len(A)
    LA = mul(L, A)
    if rank(AI.vstack([LA, L, J])) != rank(AI.vstack([L, J])):
        return False
    g = C170.cond5b_with_J(L, A, J)
    return g == 0


def main():
    for seed in (1, 2, 3, 4, 5, 6, 7, 8):
        rng = random.Random(seed)
        n = 4
        A = [[Fr(i + 1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
        # J 必须可实现：J = row[C; CA]
        p = rng.choice([1, 2])
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        J = AI.row_basis(C + mul(C, A))
        K0 = [Fr(1)] + [Fr(0)] * (n - 1)

        # q_coord：S ∋ 0，坐标 V = span{e_i : i in S}，判 (5b)
        qc = None
        for k in range(1, n + 1):
            for S in itertools.combinations(range(n), k):
                if 0 not in S:
                    continue
                L = [[Fr(1) if j == i else Fr(0) for j in range(n)] for i in S]
                if conds(L, A, J):
                    qc = k
                    break
            if qc:
                break

        # q_full：V = span{e_0, u}，u 小整数
        best = qc
        found = []
        rng2 = random.Random(seed + 100)
        for _ in range(4000):
            u = [Fr(rng2.randint(-2, 2)) for _ in range(n)]
            L = [K0[:], u]
            if rank(L) != 2:
                continue
            if conds(L, A, J):
                found.append(u)
                if best is None or 2 < best:
                    best = 2
        print("seed", seed, "J=", [[str(x) for x in r] for r in J])
        print("   q_coord =", qc, " 非坐标 dim-2 可行解:", len(found), " q_full =", best)
        if found:
            print("   例:", [[str(x) for x in u] for u in found[:2]])


if __name__ == "__main__":
    main()
