r"""宽矩阵情形：$h=n-p$ 但 $N_c=(n-r_1)+d>h$ 时，$(S)$ 是否能成立？

上一轮登记了 R13（宽矩阵反例）。本脚本系统统计：
- 每个采样点记录 $h$、$N_c$、是否方阵（$N_c=h$）、$(S)$ 是否成立（精确 gcd）；
- 按 (方阵/宽) × ($h$ 是否 $=n-p$) 分类统计。

用法：python proof/layer_program/c218_wide_case.py [--trials 25]
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


def run_instance(A, C, L0, q, rng, samples=6):
    n, p = len(A), len(C)
    CA = AI.mul(C, A)
    r1 = AI.rank(AI.vstack([C, CA]))
    KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L0)])
    m_L, d = len(KLv), n - p - q
    if m_L < d or d < 0:
        return []
    KL = [[KLv[k][i] for k in range(m_L)] for i in range(n)]
    Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
    Vrows = [[Vv[k][i] for k in range(len(Vv))] for i in range(n)]
    out = []
    for _ in range(samples):
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
        h = AI.rank([Vrows[i] + list(Z[i]) for i in range(n)])
        Nc = (n - r1) + d
        g, _, _ = SG.spectral_gcd_Z(A, C, Z)
        out.append(dict(h=h, Nc=Nc, square=(Nc == h), h_is_nminusp=(h == n - p),
                        s_ok=(SG.pdeg(g) == 0), deg=SG.pdeg(g)))
    return out


def main():
    trials = 25
    if '--trials' in sys.argv:
        trials = int(sys.argv[sys.argv.index('--trials') + 1])
    rng = random.Random(4321)
    stats = {}
    for _ in range(trials):
        n = rng.choice([5, 6])
        p = rng.choice([1, 2])
        r = 1
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        L0 = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(r)]
        for q in range(r, n - p):
            for rec in run_instance(A, C, L0, q, rng):
                key = ('方阵' if rec['square'] else '宽',
                       'h=n-p' if rec['h_is_nminusp'] else 'h<n-p')
                s = stats.setdefault(key, [0, 0, []])
                s[0] += 1
                s[1] += 1 if rec['s_ok'] else 0
                s[2].append(rec['deg'])
    print(f"{'类型':<10s} {'点数':>5s} {'(S)成立':>7s}   gcd 次数分布")
    for k in sorted(stats):
        cnt, ok, degs = stats[k]
        from collections import Counter
        print(f'{k[0]+"/"+k[1]:<10s} {cnt:5d} {ok:7d}   {dict(Counter(degs))}')


if __name__ == '__main__':
    main()
