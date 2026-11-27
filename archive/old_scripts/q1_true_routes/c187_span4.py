"""c187_span4.py — 定向搜索：可行集 Plücker 张成维数 = 4（斜倍增需要的维数）

n=4, p=3, C 单行；随机 A, L0；对每个实例：
  1. 先按 (5a) 过滤 2-平面（便宜的秩判定）；
  2. 再对通过的做 (5b)；
  3. 记录可行集的 Plücker 张成维数。
目标：找到张成维数 4 的实例。

用法：python q1_true/scripts/c187_span4.py
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
import c162_dimV_formula as M
import c183_minAB as C

mul, rank = AI.mul, AI.rank


def plvec(V):
    n = len(V[0])
    u, v = V[0], V[1]
    return [(u[i] * v[j] - u[j] * v[i]) for i in range(n) for j in range(i + 1, n)]


def main():
    p, n = 3, 4
    subs = [C.rref([list(v) for v in S], p, n) for S in C.all_subspaces(p, n)]
    planes = [S for S in subs if len(S) == 2]
    rng = random.Random(2026)
    from collections import Counter
    dims = Counter()
    found = []
    for t in range(300):
        A = [[Fr(rng.randrange(p)) for _ in range(n)] for _ in range(n)]
        Cm = [[Fr(rng.randrange(p)) for _ in range(n)] for _ in range(rng.choice([1, 2, 3]))]
        L0 = [[Fr(rng.randrange(p)) for _ in range(n)]]
        P = []
        for V in planes:
            if rank([list(x) for x in V] + L0) != len(V):
                continue
            if not M.cond5a(V, A, Cm):
                continue
            if M.cond5b(V, A, Cm) == 0:
                P.append(plvec(V))
        if not P:
            continue
        d = len(C.rref(P, p, 6))
        dims[d] += 1
        if t % 20 == 0:
            print("progress", t, "dims", dict(sorted(dims.items())), flush=True)
        if d == 4:
            found.append((t, A, Cm, L0, P))
            print("找到张成维数 4：实例", t, " 可行数", len(P), flush=True)
            if len(found) >= 3:
                break
    print("张成维数分布:", dict(sorted(dims.items())))
    for t, A, Cm, L0, P in found[:3]:
        print("=== 实例", t)
        print("A =", [[str(x) for x in r] for r in A])
        print("C =", [[str(x) for x in r] for r in Cm])
        print("L0 =", [[str(x) for x in r] for r in L0])
        print("可行数", len(P), " 张成维数", len(C.rref(P, p, 6)))


if __name__ == "__main__":
    main()
