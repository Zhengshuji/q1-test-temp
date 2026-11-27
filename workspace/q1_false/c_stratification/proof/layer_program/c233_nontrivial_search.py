r"""搜索**非终端**薄层可行点（$d>p$、$q<n_0-p$）。

结构约束（本轮推出）：
- 非终端 ⟹ $Z\not\subseteq\ker\mathcal O_C$；而 $Z\subseteq\mathcal V$ + $A$-不变 ⟹ $Z\subseteq\ker\mathcal O_C$，
  所以非终端**必须 $Z\not\subseteq\mathcal V$**（$(A)$ 不再是"不变性"）。
- Theorem D：$q>t=\dim\mathcal V-\dim(\mathcal V\cap Z)$；在 $Z\subseteq\mathcal V$ 且 $\dim Z>\dim\mathcal V$ 时
  需 $\dim(\mathcal V\cap Z)>p+d-r_1$。

本脚本：$n=6,7$、$p=2$、随机 $A,C,L_0$，$Z$ 取 $K_L=\ker[C;L_0]$ 的 $d$ 维子空间；
记录 $(q,d,s,t,n_0-p,r=\operatorname{rank}CAZ)$ 与 $(A)/(S)$，挑出 $q<n_0-p$ 且 $(A)\wedge(S)$ 的点。

用法：python proof/layer_program/c233_nontrivial_search.py [--trials 40]
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
    rng = random.Random(20261031)
    hits = []
    checked = 0
    for _ in range(trials):
        n = rng.choice([6, 7])
        p = 2
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
        Vc = [[Vv[k][i] for k in range(len(Vv))] for i in range(n)]
        n0rows, cur = [], [list(x) for x in C]
        for _k in range(n):
            n0rows.extend(cur)
            cur = [AI.mul([x], A)[0] for x in cur]
        n0 = AI.rank(n0rows)
        for q in range(r, n - p):
            d = n - p - q
            if d < 1 or d > m_L:
                continue
            pts = []
            if d * (m_L - d) <= 4:
                for I in itertools.combinations(range(m_L), d):
                    for t in itertools.product((-1, 0, 1), repeat=(m_L - d) * d):
                        pts.append((I, [list(t[k * d:(k + 1) * d]) for k in range(m_L - d)]))
            else:
                for _2 in range(80):
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
                # 命中：记录细节
                both = [list(Vc[i]) + list(Z[i]) for i in range(n)]
                s = len(Vv) + d - AI.rank(both)
                t = len(Vv) - s
                hits.append(dict(n=n, p=p, q=q, d=d, s=s, t=t, n0=n0, n0_minus_p=n0 - p,
                                 r=AI.rank(CAZ), nonterminal=(q < n0 - p), thin=(d > p)))
                print(f'  HIT: n={n},p={p},q={q},d={d},s={s},t={t},n0-p={n0-p},r={AI.rank(CAZ)},'
                      f' nonterminal={q < n0 - p}, thin={d > p}')
    print(f'\n检查 {checked} 个 (A)-点；找到 (A)∧(S) 的 {len(hits)} 个')
    nt = [h for h in hits if h['nonterminal'] and h['thin']]
    print(f'其中**非终端且薄**（$q<n_0-p$ 且 $d>p$）：{len(nt)} 个'
          + ('  ⟹ **阶谱猜想被推翻**' if nt else '  ⟹ 无反例'))


if __name__ == '__main__':
    main()
