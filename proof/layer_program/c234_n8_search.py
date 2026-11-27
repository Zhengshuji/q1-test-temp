r"""在 $p\ge2$、$r_1\ge p+2$ 的窗口里搜索**非终端薄层**可行点。

由前两轮的结构约束：
- 非终端（$q<n_0-p$）⟹ $Z\not\subseteq\mathcal V$ ⟹ $s=\dim(\mathcal V\cap Z)\le d-1$；
- Theorem D：$q>t=\dim\mathcal V-s$。

取 $n=8$、$p=2$、$r_1=4$（$\dim\mathcal V=4$）、$q=3$（$d=5-3=2$？——注意 $d=n-p-q=6-q$）：
$q=3\Rightarrow d=3>p$（薄）；$s\le2\Rightarrow t\ge2$；$q=3>t$ 可能 ✓。

本脚本对随机实例、$q=2,3$ 扫描 $Z$，找 $(A)\wedge(S)$ 且 $Z\not\subseteq\mathcal V$、$q<n_0-p$ 的点。

用法：python proof/layer_program/c234_n8_search.py [--trials 25]
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
    trials = 25
    if '--trials' in sys.argv:
        trials = int(sys.argv[sys.argv.index('--trials') + 1])
    rng = random.Random(20261031)
    hits = []
    checked = 0
    for _ in range(trials):
        n, p, r = 8, 2, 1
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        L0 = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(r)]
        if AI.rank(C + L0) < p + r:
            continue
        CA = AI.mul(C, A)
        r1 = AI.rank(AI.vstack([C, CA]))
        if r1 != 4:
            continue
        KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L0)])
        m_L = len(KLv)
        KL = [[KLv[k][i] for k in range(m_L)] for i in range(n)]
        Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
        Vc = [[Vv[k][i] for k in range(len(Vv))] for i in range(n)]
        n0rows, cur = [], [list(x) for x in C]
        for _k in range(n):
            n0rows.extend(cur)
            cur = [AI.mul([x], A)[0] for x in cur]
        n0 = AI.rank(n0rows)
        for q in (2, 3):
            d = n - p - q
            if d < 1 or d > m_L:
                continue
            pts = []
            if d * (m_L - d) <= 3:
                for I in itertools.combinations(range(m_L), d):
                    for t in itertools.product((-1, 0, 1), repeat=(m_L - d) * d):
                        pts.append((I, [list(t[k * d:(k + 1) * d]) for k in range(m_L - d)]))
            else:
                for _2 in range(60):
                    I = tuple(sorted(rng.sample(range(m_L), d)))
                    th = [[Fr(rng.randint(-3, 3)) for _ in range(d)] for _ in range(m_L - d)]
                    pts.append((I, th))
            for I, th in pts:
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
                Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
                AZ = SG.apply_col(A, Z)
                AZR = AI.mul(AZ, Rm)
                M1 = [list(Z[i]) + list(AZR[i]) for i in range(n)]
                if AI.rank(M1) != d:
                    continue
                checked += 1
                g, h, _c = SG.spectral_gcd_Z(A, C, Z)
                if SG.pdeg(g) != 0:
                    continue
                both = [list(Vc[i]) + list(Z[i]) for i in range(n)]
                s = len(Vv) + d - AI.rank(both)
                t = len(Vv) - s
                ZinV = (AI.rank([list(Vc[i]) + list(Z[i]) for i in range(n)]) == len(Vv))
                rec = dict(n=n, q=q, d=d, s=s, t=t, n0=n0, n0mp=n0 - p, r=AI.rank(CAZ),
                           nonterminal=(q < n0 - p), thin=(d > p), ZinV=ZinV)
                hits.append(rec)
                print(f'  HIT: q={q},d={d},s={s},t={t},n0-p={n0-p},r={rec["r"]},'
                      f'Z⊆V={ZinV}, nonterminal={rec["nonterminal"]}, thin={rec["thin"]}')
    print(f'\n检查 {checked} 个 (A)-点；找到 (A)∧(S) 的 {len(hits)} 个')
    nt = [x for x in hits if x['nonterminal'] and x['thin'] and not x['ZinV']]
    print(f'其中**非终端 ∧ 薄 ∧ Z⊄V**：{len(nt)} 个'
          + ('  ⟹ 阶谱猜想被推翻' if nt else '  ⟹ 无反例'))


if __name__ == '__main__':
    main()
