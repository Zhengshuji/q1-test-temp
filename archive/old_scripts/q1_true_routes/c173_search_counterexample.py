"""c173_search_counterexample.py — 批量搜索 (T) 的反例（J 必须可实现）

(T)：min_V dim V = min_{坐标 V} dim V（A 对角互异、K0 坐标）。

做法：随机 C（p=1,2）→ J = row[C;CA]（保证可实现）→ 算 q_coord；
      对每个实例，再搜 V = span{e_0, u}（u 小整数）看是否有 dim 2 的可行解。
      只要出现 q_full < q_coord 就是 (T) 的反例。

用法：python q1_true/scripts/c173_search_counterexample.py
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
    n = len(A)
    LA = mul(L, A)
    if rank(AI.vstack([LA, L, J])) != rank(AI.vstack([L, J])):
        return False
    return C170.cond5b_with_J(L, A, J) == 0


def q_coord_of(A, J, K0idx, n):
    for k in range(1, n + 1):
        for S in itertools.combinations(range(n), k):
            if K0idx not in S:
                continue
            L = [[Fr(1) if j == i else Fr(0) for j in range(n)] for i in S]
            if conds(L, A, J):
                return k
    return None


def main():
    rng = random.Random(0)
    n = 4
    A = [[Fr(i + 1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    K0 = [Fr(1)] + [Fr(0)] * (n - 1)
    stats = {}
    found_counter = []
    tested = 0
    for trial in range(400):
        p = rng.choice([1, 2])
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        J = AI.row_basis(C + mul(C, A))
        qc = q_coord_of(A, J, 0, n)
        stats[qc] = stats.get(qc, 0) + 1
        if qc is None or qc <= 2:
            continue
        tested += 1
        # 搜 dim-2 非坐标 V
        for _ in range(3000):
            u = [Fr(rng.randint(-2, 2)) for _ in range(n)]
            L = [K0[:], u]
            if rank(L) != 2:
                continue
            if conds(L, A, J):
                found_counter.append((trial, qc, u))
                break
    print("q_coord 分布:", stats)
    print("q_coord>=3 的实例数:", tested)
    print("其中找到 dim-2 非坐标可行解（即 (T) 反例）:", len(found_counter))
    for t, qc, u in found_counter[:5]:
        print("   trial", t, "q_coord", qc, "u", [str(x) for x in u])


if __name__ == "__main__":
    main()
