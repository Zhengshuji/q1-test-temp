r"""顶层 $S_d$ 上的**随机化判定**（单侧误差）：先验概率意义下的"可行/全坏"。

命题（[../spectral_locus/README.md](../spectral_locus/README.md) §10）：
在 $U=\{\Theta:\operatorname{rank}(CAZ)=d\}$（开稠密）上 $(A)$ **自动成立**（引理 4）；
$(S)$ 的失败集在 $U$ 中是闭集。若 $U$ 上存在可行点，则可行集是 $U$ 的非空开子集，
故**均匀随机取 $\Theta$** 落在可行集里的概率 $=1-\deg(R)/S$（Schwartz–Zippel）。

算法：随机取有理 $\Theta$，检查 $\operatorname{rank}(CAZ)=d$、用**精确极大子式 gcd** 检查 $(S)$。
- 命中 ⟹ **可行**（有见证，单侧无误）；
- 全不命中 ⟹ 只有"大概率全坏"（要证全坏需 $R\equiv0$ 的消元，未做）。

用法：python proof/layer_program/c214_top_stratum.py
"""
import os
import random
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))
sys.path.insert(0, _HERE)

import audit_independent as AI
import spectral_gcd as SG
import importlib.util as iu

_spec = iu.spec_from_file_location('C211', os.path.join(_HERE, 'c211_allbad_scan.py'))
M211 = iu.module_from_spec(_spec)
_spec.loader.exec_module(M211)

A, C, L, n, p = M211.A, M211.C, M211.L, M211.n, M211.p


def random_theta(rng, rows, cols, mod=7):
    """随机有理 Θ ∈ (Z/mod)^{rows×cols}（小整数，便于精确算术）。"""
    return [[Fr(rng.randint(-mod, mod)) for _ in range(cols)] for _ in range(rows)]


def top_stratum_trial(q, rng, samples=20, verbose=True):
    KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L)])
    m_L = len(KLv)
    KL = [[KLv[k][i] for k in range(m_L)] for i in range(n)]
    d = n - p - q
    hits = []
    trials = 0
    for _ in range(samples):
        # 随机图卡：随机选 d 行做单位阵
        I = tuple(sorted(rng.sample(range(m_L), d)))
        theta = random_theta(rng, m_L - d, d)
        W = M211.chart_matrix(d, I, theta)
        Z = AI.mul(KL, W)
        CAZ = AI.mul(AI.mul(C, A), Z)
        if AI.rank(CAZ) != d:
            continue          # 不在顶层 S_d
        trials += 1
        # (A) 应自动成立（引理 4）
        Rv = AI.nullspace(CAZ)
        R = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
        AZR = AI.mul(AI.mul(A, Z), R)
        M1 = [list(Z[i]) + list(AZR[i]) for i in range(n)]
        assert AI.rank(M1) == d, '(A) 在顶层应自动成立（引理 4 被违反）'
        g, h, cnt = SG.spectral_gcd_Z(A, C, Z)
        if SG.pdeg(g) == 0:
            hits.append((I, theta))
    if verbose:
        print(f'q={q}：顶层采样 {trials} 个点，其中 (S) 成立 {len(hits)} 个')
        if hits:
            print(f'  首个见证：图卡 {hits[0][0]}、Θ = {hits[0][1]}')
    return len(hits), trials


def main():
    rng = random.Random(20261030)
    for q in (5, 4):
        hits, trials = top_stratum_trial(q, rng, samples=20)
        verdict = '可行（有见证）' if hits else '顶层上全坏（采样范围内）'
        print(f'  ⟹ q={q}：{verdict}\n')


if __name__ == '__main__':
    main()
