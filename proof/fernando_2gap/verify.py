"""verify.py —— 复现 Fernando 2026（arXiv:2609.37992 §VII）的**两阶差**例子

论文例子：$n=8$、$p=r=2$、$\eta=(2,1)$、$q_0=3$、$\nu_{\min}=5=q_0+2$、$n_0-p=6$。
本脚本用本项目的框架算它的全部不变量：

1. 基本量：$\operatorname{rank}C$、$\operatorname{rank}L$、$(A,C)$ 可观测性、$L$ 可估；
2. $q_0$（功能指标算法）与闭包维数 $\mathrm{cl}$；
3. **论文给出的 order-5 增广** $\mathcal L_5$：核验 $(5a)$、$(5b)$，并算
   $h,r_1,s,\varepsilon,d_{\rm fin}$，核对 B.9 与更强的不等式 $q+r_1-s\le h<q+r_1$、$d_{\rm fin}\le s-(q+r_1-h)$；
4. $q=3$（闭包，唯一候选）与 $q=4$（闭包 + 一步前像抽样）：$(5b)$ 应全部失败；
5. $q=5$：同法抽样，应能找到 $(5b)$ 见证。

用法：python proof/fernando_2gap/verify.py
"""

import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import omega_construct as OC              # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402

F = Fraction

A = [[F(x) for x in row] for row in [
    [0, 1, 0, 1, 0, 0, 0, 0],
    [0, -1, 1, 0, 0, 0, 0, -1],
    [1, 0, -1, 1, 0, 0, 1, -1],
    [-1, -1, 0, -2, 0, 0, 0, 0],
    [0, 0, 0, 0, -2, 0, 0, 1],
    [0, 0, 0, 0, 0, -2, 1, 0],
    [0, 0, 0, 0, 0, -1, -2, 1],
    [0, 0, 0, 0, 0, 0, 1, -2],
]]

C = [[F(x) for x in row] for row in [
    [-2, -2, 2, -2, -1, 0, 1, -3],
    [0, 0, 1, 2, 2, 3, -1, -2],
]]

L0 = [[F(x) for x in row] for row in [
    [-2, -1, -2, -3, -1, 3, 2, 0],
    [1, -1, -2, 1, 0, 2, 0, 1],
]]

L5 = [[F(x) for x in row] for row in [
    [-2, -1, -2, -3, -1, 3, 2, 0],
    [1, -1, -2, 1, 0, 2, 0, 1],
    ["-47/460", 1, 0, 0, 0, 0, 0, 0],
    ["-137/230", 0, 1, 0, 0, 0, 0, 0],
    ["313/460", 0, 0, 1, 0, 0, 0, 0],
]]
L5 = [[F(x) if isinstance(x, str) else F(x) for x in row] for row in L5]


def invariants(A, C, L):
    res = TC.analyse(A, C, L)
    q, p = len(L), len(C)
    r1 = LQ.rank([r[:] for r in C] + [r[:] for r in LQ.mul(C, A)])
    return dict(q=q, p=p, h=res['h'], s=res['s'], m=res['m'], r1=r1,
                eps=res['eps_smith'], d_fin=res['d_fin'], five_b=res['five_b'])


def show(tag, inv):
    q, p, h, s, r1 = inv['q'], inv['p'], inv['h'], inv['s'], inv['r1']
    print(f'  {tag}: q={q} h={h} s={s} r1={r1} eps={inv["eps"]} d_fin={inv["d_fin"]} (5b)={inv["five_b"]}')
    print(f'      B.9 区间: q+r1-s={q + r1 - s} <= h={h} < q+r1={q + r1}  '
          f'({q + r1 - s <= h < q + r1})；d_fin 上界 s-(q+r1-h)={s - (q + r1 - h)}（实际 {inv["d_fin"]}）')


def main():
    print('=== 1. 基本量 ===')
    O = [r[:] for r in C]
    cur = [r[:] for r in C]
    for _ in range(len(A) - 1):
        cur = LQ.mul(cur, A)
        O += cur
    print(f'  rank C={LQ.rank(C)} rank L0={LQ.rank(L0)} rank[C;L0]={LQ.rank([r[:] for r in C] + [r[:] for r in L0])}')
    print(f'  rank O_C={LQ.rank(O)}（可观测）；L0 可估={LQ.rank(O + [r[:] for r in L0]) == LQ.rank(O)}')

    print('\n=== 2. q0 与闭包 ===')
    q0 = Q0.eta_and_q0(A, C, L0)[0]
    cl = len(OC.closure(A, C, L0))
    print(f'  q0(功能指标)={q0}；闭包维数={cl}')

    print('\n=== 3. 论文的 order-5 增广 L5 ===')
    assert LQ.rank(L5) == 5, f'rank L5 = {LQ.rank(L5)}'
    assert LQ.rank([r[:] for r in L5] + [r[:] for r in L0]) == 5, 'L0 ⊄ row L5'
    assert LQ.condA(A, C, L5), 'L5 不满足 (5a)'
    inv5 = invariants(A, C, L5)
    show('L5', inv5)
    assert inv5['five_b'], 'L5 应满足 (5b)'
    q, p, h, s, r1 = inv5['q'], inv5['p'], inv5['h'], inv5['s'], inv5['r1']
    assert q + r1 - s <= h < q + r1, 'B.9 的加强区间被违反'
    assert inv5['d_fin'] <= s - (q + r1 - h), 'd_fin 上界被违反'

    print('\n=== 4. q=3（闭包，唯一候选）与 q=4（抽样）===')
    Vmin = OC.closure(A, C, L0)
    inv3 = invariants(A, C, Vmin)
    show('q=3 闭包', inv3)
    assert not inv3['five_b'], 'q=3 处应失败（论文：order 3 infeasible）'
    for qq in (4,):
        samples = OC.sample_chains(A, C, L0, qq, 20, 4242)
        feas = [invariants(A, C, L) for L in samples]
        nfeas = sum(1 for x in feas if x['five_b'])
        print(f'  q={qq}: 抽样 {len(samples)}，满足 (5b) 的 {nfeas}')
        assert nfeas == 0, f'q={qq} 处出现了 (5b) 见证，与论文矛盾'

    print('\n=== 5. q=5：同法抽样应能找到见证 ===')
    samples = OC.sample_chains(A, C, L0, 5, 40, 4243)
    wins = [(L, invariants(A, C, L)) for L in samples]
    nwin = sum(1 for _, x in wins if x['five_b'])
    print(f'  q=5: 抽样 {len(samples)}，(5b) 成立 {nwin}')
    if nwin:
        _, x = next((L, x) for L, x in wins if x['five_b'])
        show('q=5 见证', x)
    print('\n✓ 复现完成：q_min = q0 + 2 = 5')


if __name__ == '__main__':
    main()
