r"""按 $d$ 与 $p$ 的关系分层：$d\le p$（顶层非空）vs $d>p$（顶层为空）。

观察（R15 及 c218 数据提示）：$d>p$ 时 $\operatorname{rank}(CAZ)\le p<d$，故"顶层自动成立"永远不适用，
$(A)$ 只能靠薄层满足 —— 这些阶更容易 all-bad。

本脚本：随机实例、随机 $Z$，按 $(d\le p)$ / $(d>p)$ 分组统计 $(A)$ 与 $(S)$（精确 gcd）。

用法：python proof/layer_program/c224_d_vs_p.py [--trials 30]
"""
import os
import random
import sys
from collections import Counter
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import spectral_gcd as SG


def main():
    trials = 30
    if '--trials' in sys.argv:
        trials = int(sys.argv[sys.argv.index('--trials') + 1])
    rng = random.Random(20261030)
    stats = Counter()
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
        Vrows = [[Vv[k][i] for k in range(len(Vv))] for i in range(n)]
        for q in range(r + 1, n - p):
            d = n - p - q
            if d < 1 or d > m_L:
                continue
            for _ in range(4):
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
                if AI.rank(Z) < d:
                    continue
                CAZ = AI.mul(CA, Z)
                Rv = AI.nullspace(CAZ)
                Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
                AZR = AI.mul(AI.mul(A, Z), Rm)
                M1 = [list(Z[i]) + list(AZR[i]) for i in range(n)]
                okA = AI.rank(M1) == d
                g, h, _ = SG.spectral_gcd_Z(A, C, Z)
                okS = SG.pdeg(g) == 0
                key = ('d<=p' if d <= p else 'd>p', okA, okS)
                stats[key] += 1
    print(f'{"组":<6s} {"(A)":>5s} {"(S)":>5s} {"计数":>5s}')
    for k in sorted(stats):
        print(f'{k[0]:<6s} {str(k[1]):>5s} {str(k[2]):>5s} {stats[k]:5d}')
    print()
    print('按组汇总（只看 (A) 成立的点）：')
    for grp in ('d<=p', 'd>p'):
        a = stats[(grp, True, True)] + stats[(grp, True, False)]
        s = stats[(grp, True, True)]
        print(f'  {grp}: (A) 成立 {a} 个，其中 (S) 成立 {s} 个'
              + ('  ← 全坏' if a and s == 0 else ''))


if __name__ == '__main__':
    main()
