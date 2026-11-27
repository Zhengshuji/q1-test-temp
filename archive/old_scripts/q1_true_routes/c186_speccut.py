"""c186_speccut.py — 定向：n=6, p=2, r=1；E 3维、K 2维、E∩K 1维

C = [e6; e5]，L0 支撑在 e1..e4 上；A 使 A e1, A e2 的后两坐标为 0（⇒ e1,e2 ∈ K），
A e1 ∉ E（⇒ E∩K 不可行）。

只枚举 Z ⊆ E 的子空间（E 为 3 维，共 28 个），算 d_alg 与 d_true。

用法：python q1_true/scripts/c186_speccut.py
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
    p, n = 3, 6
    rng = random.Random(3)
    stats = {}
    for t in range(10):
        A = [[Fr(rng.randrange(p)) for _ in range(n)] for _ in range(4)]
        # 后两行（e5,e6 方向的像）
        A.append([Fr(rng.randrange(p)) for _ in range(n)])
        A.append([Fr(rng.randrange(p)) for _ in range(n)])
        # 强制 A e1, A e2 的后两坐标为 0
        for j in (0, 1):
            A[4][j] = Fr(0)
            A[5][j] = Fr(0)
        # 强制 A e3 的后两坐标非全零
        if A[4][2] == 0 and A[5][2] == 0:
            A[4][2] = Fr(1)
        C = [[Fr(0)] * n, [Fr(0)] * n]
        C[0][5] = Fr(1)
        C[1][4] = Fr(1)
        L0 = [[Fr(rng.randrange(p)) for _ in range(4)] + [Fr(0), Fr(0)]]
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
        # 枚举 E 内的子空间（把 E 当坐标系）
        Eb = AI.rref(E)[0]
        subsE = []
        for S in C183.all_subspaces(p, len(Eb)):
            # S 是 F_p^{dimE} 的子空间（坐标），映射到 E
            rows = []
            for v in C183.rref([list(x) for x in S], p, len(Eb)):
                rows.append([sum(Fr(int(v[i])) * Eb[i][j] for i in range(len(Eb))) for j in range(n)])
            if not rows:
                subsE.append([])
            else:
                subsE.append(AI.rref(rows)[0])
        d_alg = 0
        d_true = 0
        for Z in subsE:
            if not Z:
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
        key = (feasible, len(K), len(E), len(EK), d_alg, d_true)
        stats[key] = stats.get(key, 0) + 1
        print("可行", feasible, "dimK", len(K), "dimE", len(E), "dimEK", len(EK),
              "d_alg", d_alg, "d_true", d_true)
    print("汇总:", stats)


if __name__ == "__main__":
    main()
