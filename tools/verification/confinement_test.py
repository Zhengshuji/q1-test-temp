"""confinement_test.py —— 大样本检验"$q_0+1$ 阶的可行族是否全落在 $h=q+r_1$ 上"

专家 2026-11-03 §Q7/§B 要求：把"公开例子在 $q=4$ 处所有可行增广都有 $h=q+r_1=8$"
从抽样观察变成更可靠的结论。本脚本做两件事：

1. **$q=4$**：在 $\\operatorname{Gr}(2,4)$（$\\mathcal Z\\subseteq\\ker[C;L_0]$，$\\dim=4$）中大量抽 $\\mathcal Z$，
   构造 $\\mathcal L$，筛 $(5a)$，统计 $h$ 的分布——若全部为 $8$，则"禁闭"在 $2000$ 样本上成立；
2. **$q=3$**：同法检验 $(5a)$ 的薄性（预期 0 个可行），并说明为什么抽样判不了最阶。

用法：python -u tools/verification/confinement_test.py
"""

import os
import sys
from collections import Counter
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import type3_structured as T3             # noqa: E402
import importlib.util as iu               # noqa: E402

F = Fraction


def load_example():
    spec = iu.spec_from_file_location('F2', os.path.join(_ROOT, 'proof', 'fernando_2gap', 'verify.py'))
    m = iu.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.A, m.C, m.L0


def sample_Z(K, d, m, rng):
    W = [[F(rng.randrange(-3, 4)) for _ in range(d)] for _ in range(m)]
    Z = [[sum(K[i][t] * W[t][j] for t in range(m)) for j in range(d)] for i in range(len(K))]
    if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
        return None
    return Z


def main():
    import random
    A, C, L0 = load_example()
    n, p, r = len(A), len(C), len(L0)
    CA = LQ.mul(C, A)
    r1 = LQ.rank([x[:] for x in C] + [x[:] for x in CA])
    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    m = len(K[0])
    print(f'公开例子：n={n} p={p} r={r} r1={r1} dim K={m}')
    for q, trials in ((4, 2000), (3, 2000)):
        d = n - p - q
        rng = random.Random(20261103 + q)
        adm = 0
        hs = Counter()
        for _ in range(trials):
            Z = sample_Z(K, d, m, rng)
            if Z is None:
                continue
            L = ZG.L_from_Z(A, C, L0, Z, q)
            if L is None:
                continue
            if LQ.rank([list(x) for x in L] + [list(x) for x in L0]) != LQ.rank(L):
                continue
            if not LQ.condA(A, C, L):
                continue
            adm += 1
            h, s, mm, d_fin = T3.fast_dfin(A, C, L)
            hs[h] += 1
        print(f'q={q}（d={d}）：{trials} 次抽样 → 代数可行 {adm}；h 分布 {dict(hs)}；q+r1={q + r1}')


if __name__ == '__main__':
    main()
