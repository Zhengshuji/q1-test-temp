r"""薄层大搜索（安全版，用 `apply_col` 的列作用）：$d>p$ 的阶上是否**一次**出现 $(A)\wedge(S)$？

族：块对角 $A=\operatorname{diag}(A_1,A_2)$、$C=[C_1,0]$、$L_0=[L_1,0]$（$C,L_0$ 只看块 1），
$n=5,6$、$p=1,2$、$r=1$，全部 $q$。$d\le2$ 时全网格枚举，否则随机抽样。

用法：python proof/layer_program/c228_thin_bigsearch.py [--trials 12]
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


def chart_W(m_L, d, I, theta):
    W = [[Fr(0)] * d for _ in range(m_L)]
    Iset = set(I)
    for a, ri in enumerate(I):
        W[ri][a] = Fr(1)
    free = [x for x in range(m_L) if x not in Iset]
    for a, ri in enumerate(free):
        for b in range(d):
            W[ri][b] = theta[a][b]
    return W


def main():
    trials = 12
    if '--trials' in sys.argv:
        trials = int(sys.argv[sys.argv.index('--trials') + 1])
    rng = random.Random(20261030)
    hits = []
    checked = 0
    for _ in range(trials):
        n = rng.choice([5, 6])
        p = rng.choice([1, 2])
        r = 1
        k1 = rng.randint(1, n - 1)          # 块 1 大小
        k2 = n - k1
        A = [[Fr(0)] * n for _ in range(n)]
        for i in range(k1):
            for j in range(k1):
                A[i][j] = Fr(rng.randint(-2, 2))
        for i in range(k1, n):
            for j in range(k1, n):
                A[i][j] = Fr(rng.randint(-2, 2))
        C = [[Fr(rng.randint(-2, 2)) if j < k1 else Fr(0) for j in range(n)] for _ in range(p)]
        L0 = [[Fr(rng.randint(-2, 2)) if j < k1 else Fr(0) for j in range(n)] for _ in range(r)]
        if AI.rank(C + L0) < p + r:
            continue
        CA = AI.mul(C, A)
        KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L0)])
        m_L = len(KLv)
        KL = [[KLv[k][i] for k in range(m_L)] for i in range(n)]
        for q in range(r + 1, n - p):
            d = n - p - q
            if d < 1 or d > m_L or d <= p:
                continue                 # 只看 d>p
            Rows0, cur0 = [], [list(x) for x in C]
            for _k in range(n):
                Rows0.extend(cur0)
                cur0 = [AI.mul([x], A)[0] for x in cur0]
            if q == AI.rank(Rows0) - p:
                continue                 # 终端阶恒可行（P2 Thm 7），不算薄层证据
            pts = []
            if d * (m_L - d) <= 4:
                for I in itertools.combinations(range(m_L), d):
                    for t in itertools.product((-1, 0, 1), repeat=(m_L - d) * d):
                        pts.append((I, [list(t[k * d:(k + 1) * d]) for k in range(m_L - d)]))
            else:
                for _2 in range(120):
                    I = tuple(sorted(rng.sample(range(m_L), d)))
                    th = [[Fr(rng.randint(-3, 3)) for _ in range(d)] for _ in range(m_L - d)]
                    pts.append((I, th))
            for I, th in pts:
                W = chart_W(m_L, d, I, th)
                Z = AI.mul(KL, W)
                if AI.rank(Z) < d:
                    continue
                CAZ = AI.mul(CA, Z)
                Rv = AI.nullspace(CAZ)
                Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
                AZ = SG.apply_col(A, Z)              # 列作用 ✓
                AZR = AI.mul(AZ, Rm)
                M1 = [list(Z[i]) + list(AZR[i]) for i in range(n)]
                if AI.rank(M1) != d:
                    continue
                checked += 1
                g, h, _c = SG.spectral_gcd_Z(A, C, Z)
                if SG.pdeg(g) == 0:
                    hits.append((n, p, q, d, h))
                    print(f'  HIT: n={n}, p={p}, q={q}, d={d}, h={h}')
                    Rows, cur = [], [list(x) for x in C]
                    for _k in range(n):
                        Rows.extend(cur)
                        cur = [AI.mul([x], A)[0] for x in cur]
                    n0 = AI.rank(Rows)
                    print(f'       n0={n0}, n0-p={n0-p}, n-r1={n-AI.rank(AI.vstack([C, AI.mul(C, A)]))}')
                    print(f'       A={[[str(x) for x in row] for row in A]}')
                    print(f'       C={[[str(x) for x in row] for row in C]}')
                    print(f'       L0={[[str(x) for x in row] for row in L0]}')
    print(f'd>p 的 (A)-点：{checked} 个；(A)∧(S) 成立 {len(hits)} 个')
    if hits:
        print('  反例：', hits[:6])
    else:
        print('  ⟹ 仍无薄层可行点（支持"薄层全坏"的经验定律）')


if __name__ == '__main__':
    main()

