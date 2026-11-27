r"""挑战阶谱猜想的边界：块对角族里，$d>p$ 的中间阶是否有 $(A)\wedge(S)$ 的点？

族：$A=\operatorname{diag}(A_1,A_2)$、$C=[C_1,0]$（$C$ 杀掉块 2）⟹ 块 2 ⊆ $\mathcal V$ 是"不可观测块"。
$n=5$、$n_1=2$（可观测）、$n_2=3$、$p=1$、$r=1$。
则 $n_0=n_1=2$（若 $(C_1,A_1)$ 可观测）、$n_0-p=1$、$n-r_1=3$（$r_1=2$）。
阶 $q$：$d=4-q$；**中间阶 $q=2$（$d=2>p$）、$q=4$（$d=0$）** 是猜想未覆盖的薄层。

对每个随机实例、每个 $q$，枚举 $Z\subseteq\ker[C;L_0]$ 的 $d$ 维子空间，精确检验 $(A)$ 与 $(S)$。

用法：python proof/layer_program/c226_thin_probe.py [--trials 20]
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

N, P, R, N1 = 5, 1, 1, 2


def rand_instance(rng):
    A = [[Fr(0)] * N for _ in range(N)]
    for i in range(N1):
        for j in range(N1):
            A[i][j] = Fr(rng.randint(-2, 2))
    for i in range(N1, N):
        for j in range(N1, N):
            A[i][j] = Fr(rng.randint(-2, 2))
    C = [[Fr(rng.randint(-2, 2)) if j < N1 else Fr(0) for j in range(N)]]
    L0 = [[Fr(rng.randint(-2, 2)) for _ in range(N)]]
    return A, C, L0


def main():
    trials = 20
    if '--trials' in sys.argv:
        trials = int(sys.argv[sys.argv.index('--trials') + 1])
    rng = random.Random(2026)
    findings = []
    checked = 0
    for _ in range(trials):
        A, C, L0 = rand_instance(rng)
        if AI.rank(C + L0) < P + R:
            continue
        CA = AI.mul(C, A)
        r1 = AI.rank(AI.vstack([C, CA]))
        Rows, cur = [], [list(x) for x in C]
        for _k in range(N):
            Rows.extend(cur)
            cur = [AI.mul([x], A)[0] for x in cur]
        n0 = AI.rank(Rows)
        KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L0)])
        m_L = len(KLv)
        KL = [[KLv[k][i] for k in range(m_L)] for i in range(N)]
        Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
        Vrows = [[Vv[k][i] for k in range(len(Vv))] for i in range(N)]
        for q in (2, 4):
            d = N - P - q
            if d < 0 or d > m_L:
                continue
            for I in itertools.combinations(range(m_L), d):
                for t in itertools.product((-1, 0, 1), repeat=(m_L - d) * d):
                    W = [[Fr(0)] * d for _ in range(m_L)]
                    Iset = set(I)
                    for a, ri in enumerate(I):
                        W[ri][a] = Fr(1)
                    free = [x for x in range(m_L) if x not in Iset]
                    for a, ri in enumerate(free):
                        for b in range(d):
                            W[ri][b] = Fr(t[a * d + b])
                    Z = AI.mul(KL, W) if d > 0 else [[Fr(0)] for _ in range(N)]
                    if d > 0 and AI.rank(Z) < d:
                        continue
                    checked += 1
                    CAZ = AI.mul(CA, Z) if d > 0 else [[Fr(0)]]
                    Rv = AI.nullspace(CAZ) if d > 0 else []
                    Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
                    AZR = AI.mul(AI.mul(A, Z), Rm) if d > 0 else [[] for _ in range(N)]
                    M1 = [list(Z[i]) + list(AZR[i]) for i in range(N)]
                    okA = AI.rank(M1) == d if d > 0 else True
                    if not okA:
                        continue
                    if d > 0:
                        g, h, _c = SG.spectral_gcd_Z(A, C, Z)
                        okS = SG.pdeg(g) == 0
                    else:
                        okS = True
                        g, h = None, 0
                    if okS:
                        findings.append((q, d, n0 - P, N - r1))
    print(f'检查 {checked} 个 (q,Z) 点；找到 (A)∧(S) 的薄层点 {len(findings)} 个')
    thin = [f for f in findings if f[1] > P]
    if thin:
        print('  前几个 (q,d,n0-p,n-r1)：', thin[:8])
        print('  ⟹ 阶谱猜想的"薄层不可行"部分被**推翻**（存在 d>p 的 (A)∧(S) 点）')
    else:
        print('  ⟹ 所有可行点都满足 d≤p（不构成对猜想的反驳）')
        if findings:
            print('  可行点的 (q,d,n0-p,n-r1)：', findings[:6])


if __name__ == '__main__':
    main()

