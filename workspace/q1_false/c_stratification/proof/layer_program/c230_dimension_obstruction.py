r"""Theorem D 的实例核对：$q\le t$ 时 $(S)$ 必失败；$(S)$ 成立的点必满足 $q>t$。

顶层上 $t=\dim(\mathcal V\cap Z)=\dim\mathcal V=n-r_1$（因为 $\mathcal V\cap Z=0$），
所以顶层必须 $q>n-r_1$——这修正了我们之前"顶层失败 $\iff q=n-r_1$"的**不完整**表述。

用法：python proof/layer_program/c230_dimension_obstruction.py [--trials 20]
"""
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
    trials = 20
    if '--trials' in sys.argv:
        trials = int(sys.argv[sys.argv.index('--trials') + 1])
    rng = random.Random(20261030)
    viol = 0
    stats = {'q<=t': [0, 0], 'q>t': [0, 0]}     # [总数, (S) 成立数]
    examples = []
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
        KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L0)])
        m_L = len(KLv)
        KL = [[KLv[k][i] for k in range(m_L)] for i in range(n)]
        Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
        Vcols = [[Vv[k][i] for k in range(len(Vv))] for i in range(n)]
        for q in range(r + 1, n - p):
            d = n - p - q
            if d < 1 or d > m_L:
                continue
            for _2 in range(4):
                I = tuple(sorted(rng.sample(range(m_L), d)))
                th = [[Fr(rng.randint(-3, 3)) for _ in range(d)] for _ in range(m_L - d)]
                W = [[Fr(0)] * d for _ in range(m_L)]
                Iset = set(I)
                for a, ri in enumerate(I):
                    W[ri][a] = Fr(1)
                free = [x for x in range(m_L) if x not in Iset]
                for a, ri in enumerate(free):
                    for b in range(d):
                        W[ri][b] = th[a][b]
                Z = AI.mul(KL, W)
                if AI.rank(Z) < d:
                    continue
                CAZ = AI.mul(CA, Z)
                Rv = AI.nullspace(CAZ)
                R = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
                AZ = SG.apply_col(A, Z)
                AZR = AI.mul(AZ, R)
                M1 = [list(Z[i]) + list(AZR[i]) for i in range(n)]
                if AI.rank(M1) != d:
                    continue
                # t = dim V - dim(V∩Z)
                both = [list(Vcols[i]) + list(Z[i]) for i in range(n)]
                s = len(Vv) + d - AI.rank(both)
                t = len(Vv) - s
                g, h, _c = SG.spectral_gcd_Z(A, C, Z)
                okS = SG.pdeg(g) == 0
                key = 'q<=t' if q <= t else 'q>t'
                stats[key][0] += 1
                stats[key][1] += 1 if okS else 0
                if q <= t and okS:
                    viol += 1
                    examples.append((n, p, q, d, t, AI.rank(CAZ)))
    print('分类统计（只含满足 (A) 的点）：')
    for k in ('q<=t', 'q>t'):
        tot, ok = stats[k]
        print(f'  {k}：{tot} 个点，其中 (S) 成立 {ok} 个' + ('  ← 定理 D 要求 0' if k == 'q<=t' else ''))
    print(f'\n反例（q≤t 但 (S) 成立）：{viol} 个')
    if examples:
        print('  ', examples[:5])


if __name__ == '__main__':
    main()
