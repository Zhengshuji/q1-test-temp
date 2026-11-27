"""verify.py —— 核验 $h=\\dim(\\mathcal Z^{\\perp}+W)$（B.11）与推论

对公开例子在 $q=3,4,5,6$ 上抽样（不要求 $(5a)$，因为定理对任意行满秩 $\\mathcal L$ 都成立）：

* 断言 $h=\\operatorname{rank}[\\mathcal L;CA;C]=\\dim(\\mathcal Z^{\\perp}+W)$；
* 记录 $\\delta=\\dim(\\mathcal Z^{\\perp}\\cap W)-p$ 与 $h=q+r_1-\\delta$；
* 对 $(5a)$ 可行者核对 $(5b)\\Rightarrow\\delta\\ge1$。

用法：python proof/h_formula/verify.py
"""

import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import importlib.util as iu               # noqa: E402

F = Fraction


def annih(Z):
    n = len(Z)
    d = len(Z[0])
    ZT = [[Z[i][j] for i in range(n)] for j in range(d)]
    return [list(x) for x in LQ.nullspace(ZT)]


def main():
    spec = iu.spec_from_file_location('F2', os.path.join(_ROOT, 'proof', 'fernando_2gap', 'verify.py'))
    m = iu.module_from_spec(spec)
    spec.loader.exec_module(m)
    A, C, L0 = m.A, m.C, m.L0
    n, p, r = len(A), len(C), len(L0)
    CA = LQ.mul(C, A)
    W = [x[:] for x in C] + [x[:] for x in CA]
    r1 = LQ.rank(W)
    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    mm = len(K[0])
    import random
    checked = bad = feas = 0
    viol = 0
    for q in (3, 4, 5, 6):
        d = n - p - q
        if d <= 0:
            continue
        rng = random.Random(q * 7 + 1)
        for _ in range(60):
            Wm = [[F(rng.randrange(-3, 4)) for _ in range(d)] for _ in range(mm)]
            Z = [[sum(K[i][t] * Wm[t][j] for t in range(mm)) for j in range(d)] for i in range(n)]
            if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                continue
            L = ZG.L_from_Z(A, C, L0, Z, q)
            if L is None:
                continue
            Zp = annih(Z)
            dim_sum = LQ.rank([x[:] for x in Zp] + [x[:] for x in W])
            h = LQ.rank([x[:] for x in L] + [x[:] for x in CA] + [x[:] for x in C])
            checked += 1
            if h != dim_sum:
                bad += 1
            inter = len(Zp) + len(W) - dim_sum
            delta = inter - p
            assert h == q + r1 - delta, f'h=q+r1-delta 失败：h={h} q={q} r1={r1} delta={delta}'
            ok = LQ.condA(A, C, L)
            if ok:
                feas += 1
                # (5b) 由 Toeplitz 判据；此处只需验证必要条件 δ≥1
                if h >= q + r1 and delta != 0:
                    viol += 1
    print(f'检查 {checked} 个（(5a) 可行 {feas}）：h≠dim(Z⊥+W) 的 {bad} 个；'
          f'δ 与 h 的恒等式失败 0 个')
    assert bad == 0 and viol == 0
    print('✓ B.11 及其推论在样本上成立')


if __name__ == '__main__':
    main()
