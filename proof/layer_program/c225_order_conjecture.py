r"""阶谱猜想：可行阶 $=\{n_0-p\}\cup\{q:\ d\le p,\ q\ne n-r_1\}$（在功能可观测前提下）。

对随机实例，逐阶比较"猜想预测"与"采样判定"（$d\le p$ 时 $(A)$ 在顶层自动，可直接采样）。

用法：python proof/layer_program/c225_order_conjecture.py [--trials 40]
"""
import itertools
import os
import random
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import spectral_gcd as SG


def main():
    trials = 40
    if '--trials' in sys.argv:
        trials = int(sys.argv[sys.argv.index('--trials') + 1])
    rng = random.Random(20261030)
    agree = disagree = skipped = 0
    bad = []
    for _ in range(trials):
        n = rng.choice([5, 6])
        p = rng.choice([1, 2])
        r = 1
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        L0 = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(r)]
        if AI.rank(C + L0) < p + r:
            continue
        CA = AI.mul(C, A)
        r1 = AI.rank(AI.vstack([C, CA]))
        Rows, cur = [], [list(x) for x in C]
        for _k in range(n):
            Rows.extend(cur)
            cur = [AI.mul([x], A)[0] for x in cur]
        n0 = AI.rank(Rows)
        if AI.rank(Rows + [L0[0]]) != n0:
            continue                      # 非功能可观测，跳过
        KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L0)])
        m_L = len(KLv)
        KL = [[KLv[k][i] for k in range(m_L)] for i in range(n)]
        Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
        Vrows = [[Vv[k][i] for k in range(len(Vv))] for i in range(n)]
        for q in range(r, n - p):
            d = n - p - q
            if d < 0 or d > m_L:
                continue
            pred = (q == n0 - p) or (d <= p and q != n - r1)
            if d > p:
                skipped += 1
                continue                # 薄层，采样测不到，跳过
            # 采样：顶层随机点
            found = False
            for _2 in range(6):
                if d == 0:
                    Z = [[Fr(0)] for _i in range(n)]
                    cand = True
                    break
                I = tuple(sorted(rng.sample(range(m_L), d)))
                theta = [[Fr(rng.randint(-3, 3)) for _ in range(d)] for _ in range(m_L - d)]
                W = [[Fr(0)] * d for _ in range(m_L)]
                Iset = set(I)
                for a, ri in enumerate(I):
                    W[ri][a] = Fr(1)
                free = [x for x in range(m_L) if x not in Iset]
                for a, ri in enumerate(free):
                    for b in range(d):
                        W[ri][b] = theta[a][b]
                Z = AI.mul(KL, W)
                if d == 0 or AI.rank(Z) == d:
                    cand = True
                else:
                    cand = False
                if not cand:
                    continue
                CAZ = AI.mul(CA, Z)
                if d > 0 and AI.rank(CAZ) != d:
                    continue            # 非顶层（薄）
                Rv = AI.nullspace(CAZ) if d > 0 else []
                Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
                AZR = AI.mul(AI.mul(A, Z), Rm) if d > 0 else [[] for _ in range(n)]
                M1 = [list(Z[i]) + list(AZR[i]) for i in range(n)]
                okA = AI.rank(M1) == d if d > 0 else True
                if d == 0:
                    okS = True
                    g, h = None, 0
                else:
                    g, h, _c = SG.spectral_gcd_Z(A, C, Z)
                    okS = SG.pdeg(g) == 0
                if okA and okS:
                    found = True
                    break
            if found == pred:
                agree += 1
            else:
                disagree += 1
                bad.append((n, p, r1, n0, q, d, pred, found))
    print(f'一致 {agree}、不一致 {disagree}、跳过（d>p 薄层）{skipped}')
    for b in bad[:5]:
        print('  不一致例：', b)


if __name__ == '__main__':
    main()
