"""c178_verify_counterexample.py — 复现并验证 c177 的 (T) 反例（trial 47）

重放 c177 的随机流，取出 trial 47 的 (A, C)，再重做 dim-2 搜索拿到 u，
然后逐条独立验证：J=row[C;CA]、(5a)、(5b)、以及 q_coord=3。

用法：python q1_true/scripts/c178_verify_counterexample.py
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
import c177_n6_grid as C177

mul, rank = AI.mul, AI.rank


def main():
    rng = random.Random(11)
    n = 6
    A = [[Fr(i + 1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    K0 = [Fr(1)] + [Fr(0)] * (n - 1)
    grid = [x for x in itertools.product([-1, 0, 1], repeat=n)]
    target = 47
    inst = None
    for trial in range(60):
        p = rng.choice([1, 2])
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        if trial == target:
            inst = C
            break
        # 消耗与 c177 相同的随机数：c177 在 q_coord>=4 时会用 rng 搜 dim-3，
        # 为完全重放，这里也照做
        J = AI.row_basis(C + mul(C, A))
        qc = C177.q_coord_of(A, J, n)
        if qc is not None and qc >= 4:
            for _ in range(200):
                [Fr(rng.randint(-2, 2)) for _ in range(n - 1)]
                [Fr(rng.randint(-2, 2)) for _ in range(n - 1)]
    if inst is None:
        print("重放失败")
        return
    C = inst
    J = AI.row_basis(C + mul(C, A))
    print("C =", [[str(x) for x in r] for r in C])
    print("J =", [[str(x) for x in r] for r in J])
    qc = C177.q_coord_of(A, J, n)
    print("q_coord =", qc)
    # dim-2 搜索
    hit = None
    for u0 in grid:
        u = [Fr(0)] + [Fr(x) for x in u0[1:]]
        if all(x == 0 for x in u):
            continue
        L = [K0[:], u]
        if rank(L) == 2 and C177.conds(L, A, J):
            hit = u
            break
    if hit is None:
        print("未复现 dim-2 解")
        return
    print("u =", [str(x) for x in hit])
    L = [K0[:], hit]
    # 独立验证
    CA = mul(C, A)
    LA = mul(L, A)
    print("rank[LA;L;CA;C] =", rank(AI.vstack([LA, L, CA, C])),
          " rank[L;CA;C] =", rank(AI.vstack([L, CA, C])))
    print("(5b) gcd 次数 =", C170.cond5b_with_J(L, A, J))
    # 坐标解：dim<=2 是否有？
    for S in [(0, k) for k in range(1, n)]:
        Lc = [[Fr(1) if j == i else Fr(0) for j in range(n)] for i in S]
        if C177.conds(Lc, A, J):
            print("坐标解 dim2 存在:", S)
            break
    else:
        print("坐标解 dim<=2 不存在（q_coord=3 确认）")


if __name__ == "__main__":
    main()
