"""c170_matroid_check.py — 验证：坐标 V + 对角 A 时，(5b) 是否等价于一个拟阵条件

猜想（本会话）：设 A 对角、特征值互异，J 为任意子空间，V = span{e_i : i in S}。
则 (5b) 等价于：对每个 i in S，rank(pi(S\\{i})) = rank(pi(S))，
其中 pi: R^n -> R^n/J 为商映射。

等价说法：S 在「pi(e_j) 的线性拟阵」中没有 coloop（即 S 是一个并环集/union of circuits）。

用法：python q1_true/scripts/c170_matroid_check.py
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
import c162_dimV_formula as M

mul, rank = AI.mul, AI.rank


def cond5b_with_J(L, A, J):
    """rank[lam L - LA; J] == rank[L; J] for all lam  (最大子式的 gcd == 常数)"""
    n = len(A)
    q = len(L)
    LA = mul(L, A)
    rows = [[[-LA[i][j], L[i][j]] for j in range(n)] for i in range(q)]
    for r in J:
        rows.append([[r[j], Fr(0)] for j in range(n)])
    h = rank(AI.vstack([L, J]))
    mins = []
    for rr in itertools.combinations(range(len(rows)), h):
        for cc in itertools.combinations(range(n), h):
            v = AI._det_poly([[rows[r][c] for c in cc] for r in rr])
            if any(x != 0 for x in v):
                mins.append(v)
    if not mins:
        return None
    g = mins[0]
    for v in mins[1:]:
        g = AI.pgcd(g, v)
        if len(g) <= 1:
            break
    return len(g) - 1


def pi_rank(S, J, n):
    """rank{pi(e_i): i in S};  pi: R^n -> R^n/J"""
    if not S:
        return 0
    span_S = [[Fr(1) if k == i else Fr(0) for k in range(n)] for i in S]
    d = len(S) + len(J) - len(AI.row_basis(span_S + J))
    return len(S) - d


def main():
    rng = random.Random(7)
    n = 4
    A = [[Fr(i + 1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    J = AI.row_basis([[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(2)])
    print("J =", [[str(x) for x in r] for r in J])
    print("S".ljust(12), "5b?", " matroid?")
    bad = 0
    for k in range(1, n + 1):
        for S in itertools.combinations(range(n), k):
            L = [[Fr(1) if j == i else Fr(0) for j in range(n)] for i in S]
            g = cond5b_with_J(L, A, J)
            ok = (g == 0)
            mat = all(pi_rank([x for x in S if x != i], J, n) == pi_rank(list(S), J, n)
                      for i in S)
            if ok != mat:
                bad += 1
            print(str(S).ljust(12), str(ok).ljust(6), mat)
    print("不一致:", bad)


if __name__ == "__main__":
    main()
