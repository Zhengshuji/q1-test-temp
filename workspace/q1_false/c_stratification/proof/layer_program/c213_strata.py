r"""$\Omega^\star$（$(A)$-集）的分层结构：$\operatorname{rank}(CAZ)=d$ 时 $(A)$ **自动成立**。

命题（[../spectral_locus/README.md](../spectral_locus/README.md) §8）：在 P2 的图卡里，
$$r:=\operatorname{rank}(CAZ(\Theta)),\qquad \text{若 }r=d\ \text{则 }\ker(CAZ)=0\ \Rightarrow\ R_Z\ \text{为空}\ \Rightarrow\ (8b)\ \text{退化为}\ \operatorname{rank}Z=d\ \Rightarrow\ (A)\ \text{恒成立}.$$
于是 $\Omega^\star=\bigcup_{r=0}^{d}\{\operatorname{rank}(CAZ)=r\}\cap\{\text{相应的秩条件}\}$，而 $r=d$ 这一层是**开稠密**的：在那里只剩 $(S)$ 要检验。

本脚本在 P2 的例子（arXiv:2609.37992 §VII）上核对：
- $q=4$（$d=2$）：采样点应全部 $r=d$ 且 $(A)$ 成立；
- $q=3$（$d=3$）：出现 $r=2<d$，(A) 变成非平凡条件。

用法：python proof/layer_program/c213_strata.py
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, _HERE)

import audit_independent as AI
import importlib.util as iu

_spec = iu.spec_from_file_location('C211', os.path.join(_HERE, 'c211_allbad_scan.py'))
M211 = iu.module_from_spec(_spec)
_spec.loader.exec_module(M211)

A, C, L, n, p = M211.A, M211.C, M211.L, M211.n, M211.p


def main():
    KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L)])
    m_L = len(KLv)
    KL = [[KLv[k][i] for k in range(m_L)] for i in range(n)]
    grid = [Fr(-1), Fr(0), Fr(1)]
    for q in (4, 3):
        d = n - p - q
        stats = {}
        for I in itertools.combinations(range(m_L), d):
            for t in itertools.product(grid, repeat=(m_L - d) * d):
                theta = [list(t[k * d:(k + 1) * d]) for k in range(m_L - d)]
                W = M211.chart_matrix(d, I, theta)
                Z = AI.mul(KL, W)
                CAZ = AI.mul(AI.mul(C, A), Z)
                r = AI.rank(CAZ)
                Rv = AI.nullspace(CAZ)
                R = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
                AZR = AI.mul(AI.mul(A, Z), R)
                M1 = [list(Z[i]) + list(AZR[i]) for i in range(n)]
                okA = AI.rank(M1) == d
                stats.setdefault(r, [0, 0])
                stats[r][0] += 1
                stats[r][1] += 1 if okA else 0
        print(f'q={q}（d={d}）：按 r=rank(CAZ) 分层')
        for r in sorted(stats):
            cnt, ok = stats[r]
            print(f'  r={r}：{cnt} 个采样点，(A) 成立 {ok} 个' + ('  ← 应全成立' if r == d else ''))
        print()


if __name__ == '__main__':
    main()
