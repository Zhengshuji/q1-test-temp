"""c177_n6_grid.py — n=6 上对 (T) 做网格穷举

对每个随机可实现实例（A=diag(1..6)、J=row[C;CA]、K0=span{e_0}）：
  1. 算 q_coord；
  2. 若 q_coord >= 3：穷举 u in {-1,0,1}^6（去掉 u_0 分量与重复），检查 V=span{e_0,u}；
  3. 若 q_coord >= 4：再随机搜 dim-3 的 V=span{e_0,u,w}。
出现更小可行维数即为 (T) 反例。

用法：python q1_true/scripts/c177_n6_grid.py
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
    rng = random.Random(11)
    n = 6
    A = [[Fr(i + 1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    K0 = [Fr(1)] + [Fr(0)] * (n - 1)
    stats = {}
    counter = []
    checked = 0
    grid = [x for x in itertools.product([-1, 0, 1], repeat=n)]
    for trial in range(60):
        p = rng.choice([1, 2])
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        J = AI.row_basis(C + mul(C, A))
        qc = q_coord_of(A, J, n)
        stats[qc] = stats.get(qc, 0) + 1
        if qc is None or qc <= 2:
            continue
        checked += 1
        hit = None
        # 穷举 dim-2（u 的 e_0 分量可置 0，因为 V ∋ e_0）
        for u0 in grid:
            u = [Fr(0)] + [Fr(x) for x in u0[1:]]
            if all(x == 0 for x in u):
                continue
            L = [K0[:], u]
            if rank(L) == 2 and conds(L, A, J):
                hit = (2, u)
                break
        if hit is None and qc >= 4:
            for _ in range(200):
                u = [Fr(0)] + [Fr(rng.randint(-2, 2)) for _ in range(n - 1)]
                w = [Fr(0)] + [Fr(rng.randint(-2, 2)) for _ in range(n - 1)]
                L = [K0[:], u, w]
                if rank(L) == 3 and conds(L, A, J):
                    hit = (3, u, w)
                    break
        if hit is not None:
            counter.append((trial, qc, hit))
    print("n=6, q_coord 分布:", stats)
    print("q_coord>=3 的实例数:", checked)
    print("找到反例:", len(counter))
    for t, qc, hit in counter[:5]:
        print("   trial", t, "q_coord", qc, "hit dim", hit[0])


if __name__ == "__main__":
    main()
