"""z_determines_spectrum.py —— 检验：$(5b)$ 是否只依赖 $\\mathcal Z$（与补的选取无关）

若固定 $\\mathcal Z$（$\\operatorname{row}[C;\\mathcal L]=\\mathcal Z^{\\perp}$）后，
无论怎样选 $\\operatorname{row}\\mathcal L$（$\\operatorname{row}C$ 在 $\\mathcal Z^{\\perp}$ 里的、含 $\\operatorname{row}L_0$ 的补），
$(5a)$ 与 $(5b)$ 的判定都不变，则"谱可行性"是 $\\mathcal Z$ 的函数——一个纯几何对象。

做法：固定 $\\mathcal Z$，从 $\\mathcal Z^{\\perp}$ 的基出发，随机生成 200 个不同的补（含 $L_0$、行满秩），
逐个判 $(5a)$、$(5b)$，统计判定分布。

用法：python -u tools/verification/z_determines_spectrum.py
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


def annih(Z):
    n = len(Z)
    d = len(Z[0])
    ZT = [[Z[i][j] for i in range(n)] for j in range(d)]
    return [list(x) for x in LQ.nullspace(ZT)]


def random_complement(A, C, L0, Z, q, rng, trials=200):
    """固定 Z，随机生成 $\\operatorname{row}C$ 在 $Z^{\\perp}$ 中的、含 $L_0$ 的补（$q$ 行）。"""
    n, p = len(A), len(C)
    B = annih(Z)                                   # 基（行），dim p+q
    out = []
    for _ in range(trials):
        L = [list(x) for x in L0]
        pool = B[:]
        rng.shuffle(pool)
        # 先放 L0，再从 pool 里挑，使 [C;L] 秩 = p+q
        for b in pool:
            if len(L) == q:
                break
            if LQ.rank([list(x) for x in C] + L + [b]) > LQ.rank([list(x) for x in C] + L):
                L.append(b)
        if len(L) != q:
            continue
        # 随机扰动：把最后一行换成 pool 里其它向量的组合
        if q > len(L0):
            u = [F(0)] * n
            for b in pool:
                coef = F(rng.randrange(-2, 3))
                if coef:
                    for j in range(n):
                        u[j] += coef * b[j]
            cand = L[:-1] + [u]
            if LQ.rank([list(x) for x in C] + cand) == p + q and \
               LQ.rank([list(x) for x in L0] + cand) == q:
                L = cand
        if LQ.rank([list(x) for x in C] + L) != p + q:
            continue
        out.append(L)
    return out


def main():
    spec = iu.spec_from_file_location('F2', os.path.join(_ROOT, 'proof', 'fernando_2gap', 'verify.py'))
    m = iu.module_from_spec(spec)
    spec.loader.exec_module(m)
    A, C, L0 = m.A, m.C, m.L0
    n, p, r = len(A), len(C), len(L0)
    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    mm = len(K[0])
    import random
    for q in (4, 5):
        d = n - p - q
        rng = random.Random(31 + q)
        # 取 3 个不同的 Z
        for trial in range(3):
            Wm = [[F(rng.randrange(-3, 4)) for _ in range(d)] for _ in range(mm)]
            Z = [[sum(K[i][t] * Wm[t][j] for t in range(mm)) for j in range(d)] for i in range(n)]
            if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                continue
            variants = random_complement(A, C, L0, Z, q, rng)
            verdicts = Counter()
            hs = Counter()
            for L in variants:
                ok = LQ.condA(A, C, L)
                if not ok:
                    verdicts['no_(5a)'] += 1
                    continue
                h, s, mm2, d_fin = T3.fast_dfin(A, C, L)
                hs[h] += 1
                verdicts['5b' if d_fin == 0 else 'no_5b'] += 1
            print(f'q={q} Z#{trial}：{len(variants)} 个不同的补 → 判定 {dict(verdicts)}；h 分布 {dict(hs)}')


if __name__ == '__main__':
    main()
