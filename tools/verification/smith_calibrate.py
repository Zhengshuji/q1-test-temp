r"""标定 Smith 实现与"反转铅笔"约定（用两个已知小例）。

期望：
  diag(λ,1)：Smith 不变因子 {1, λ} ⟹ d_fin = 1；反转 diag(1,μ) ⟹ d_inf = 1；和 = 2 = 阶数 ✓
  [λ  1]  ：Smith {1} ⟹ d_fin = 0；反转 [1  μ] ⟹ d_inf = 0；右最小指标 1（[λ,1]·(-1,λ)ᵀ = 0）
"""

import os
import sys
from fractions import Fraction as Fr

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import spectral_gcd as SG     # noqa: E402
import poly_smith as PS       # noqa: E402

F = Fr


def show(name, Q):
    inv = PS.smith_invariants(Q)
    degs = [SG.pdeg(d) for d in inv]
    print(f'{name}: Smith 不变因子个数 = {len(inv)}，次数 = {degs}，总次数 = {sum(degs)}')
    return len(inv), sum(degs)


def poly(c0, c1):
    return SG.ptrim([F(c0), F(c1)])


def one():
    return SG.ptrim([F(1)])


def zero():
    return SG.ptrim([F(0)])


def main():
    # diag(λ, 1)
    Q1 = [[poly(0, 1), zero()], [zero(), one()]]
    n1, d1 = show('diag(λ,1)', Q1)
    # 反转 diag(1, μ)
    R1 = [[one(), zero()], [zero(), poly(0, 1)]]
    n1r, d1r = show('rev diag(1,μ)', R1)
    print(f'  ⟹ d_fin={d1}, d_inf={d1r}，和={d1 + d1r}（应 = 2）\n')

    # [λ  1]
    Q2 = [[poly(0, 1), one()]]
    n2, d2 = show('[λ 1]', Q2)
    R2 = [[one(), poly(0, 1)]]
    n2r, d2r = show('rev [1 μ]', R2)
    print(f'  ⟹ d_fin={d2}, d_inf={d2r}；右最小指标应为 1（列数 2 − 秩 1）\n')

    # 断言：若实现正确，d_fin(diag)=1、d_inf(diag)=1
    ok = (d1 == 1 and d1r == 1 and d2 == 0)
    print('标定通过' if ok else '标定**未通过**：实现或约定有误，需先修')


if __name__ == '__main__':
    main()
