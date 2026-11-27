"""c185_directed_speccut.py — 定向构造：固定 n=5, C=e5^T, 让 E∩K 可控

对每个实例：枚举 F_3^5 的全部子空间，算
  d_alg = max dim Z, Z ⊆ E, A(Z∩K) ⊆ Z
  d_true = 再加 (8c)
记录 (E∩K 可行, d_alg, d_true)。

用法：python q1_true/scripts/c185_directed_speccut.py
"""
import sys
import os
import itertools
import random

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "scripts", "core"))
sys.path.insert(0, HERE)

from fractions import Fraction as Fr
import audit_independent as AI
import c183_minAB as C183
import c184_spec_cut as C184

mul, rank = AI.mul, AI.rank


def main():
    p, n = 3, 5
    subs = [C183.rref([list(v) for v in S], p, n) for S in C183.all_subspaces(p, n)]
    print("F_3^5 子空间数", len(subs))
    rng = random.Random(11)
    stats = {}
    for t in range(8):
        # A：最后一行 (0,0,a,b,c)，a != 0
        A = [[Fr(rng.randrange(p)) for _ in range(n)] for _ in range(n - 1)]
        last = [Fr(0), Fr(0), Fr(rng.randrange(1, p)), Fr(rng.randrange(p)), Fr(rng.randrange(p))]
        A.append(last)
        C = [[Fr(0)] * n]
        C[0][n - 1] = Fr(1)
        L0 = [[Fr(rng.randrange(p)) for _ in range(n)]]
        CA = mul(C, A)
        K = AI.nullspace(AI.vstack([C, CA]))
        E = AI.nullspace(AI.vstack([C, L0]))
        if not K or not E:
            continue
        EK = C184.inter(E, K)
        feasible = True
        for v in EK:
            Av = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
            if not C184.in_span(E, Av) or not C184.in_span(EK, Av):
                feasible = False
                break
        d_alg = 0
        d_true = 0
        for Z in subs:
            if rank([list(x) for x in Z] + [list(x) for x in E]) != len(C184.rref_list(E)):
                continue
            ZK = C184.inter(Z, K)
            ok = True
            for v in ZK:
                Av = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
                if not C184.in_span(Z, Av):
                    ok = False
                    break
            if not ok:
                continue
            d_alg = max(d_alg, len(Z))
            if C184.cond_8c(Z, A, K):
                d_true = max(d_true, len(Z))
        key = (feasible, len(K), len(E), d_alg, d_true)
        stats[key] = stats.get(key, 0) + 1
        print("  可行", feasible, "dimK", len(K), "dimE", len(E), "d_alg", d_alg, "d_true", d_true)


if __name__ == "__main__":
    main()
