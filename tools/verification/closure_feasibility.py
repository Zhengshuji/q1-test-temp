"""closure_feasibility.py —— 闭包处 $(5b)$ 何时成立？（WP2 第 6 步）

$q=\\mathrm{cl}$ 时 $(5a)$ 解**唯一**（就是闭包 $V_{\\min}$），所以"闭包处 $(5b)$ 是否成立"
是一个**确定的结构问题**，不是搜索问题。实测 56 个可观测实例：40 个成立、14 个不成立、2 个未定
（见 [proof/refuted/C1_closure_plus_one.md](../../proof/refuted/C1_closure_plus_one.md)）。

本脚本收集每个实例闭包的**全部可算不变量**，并与 $(5b)$ 的判定做交叉表，找能分界的不变量：

* 聚合量：$n,p,r,\\mathrm{cl},h,s,m,d_{\\rm fin}$；
* Kronecker：$\\sum\\varepsilon$、$\\varepsilon$ 的最大元；
* 结构谓词：互补障碍（$\\ker C=\\ker[C;CA]\\oplus\\ker[C;L]$）、$h=n-p$、$\\mathrm{cl}=n-r_1$、
  $\\operatorname{rank}[C;L]=p+\\mathrm{cl}$、$V_{\\min}\\cap\\operatorname{row}C=0$。

用法：python -u tools/verification/closure_feasibility.py
"""

import os
import sys
from collections import defaultdict
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import omega_construct as OC              # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402

F = Fraction


def kernel_basis(M):
    return [list(r) for r in LQ.nullspace(M)]


def features(A, C, L0):
    n, p = len(A), len(C)
    Vmin = OC.closure(A, C, L0)
    cl = len(Vmin)
    CA = LQ.mul(C, A)
    res = TC.analyse(A, C, Vmin)
    # Kronecker / 结构谓词
    Vk = kernel_basis([r[:] for r in C] + [r[:] for r in CA])      # ker[C;CA]
    Zk = kernel_basis([r[:] for r in C] + [r[:] for r in Vmin])    # ker[C;L]
    Kc = kernel_basis([r[:] for r in C])                           # ker C
    inter = len(Vk) + len(Zk) - LQ.rank(Vk + Zk)
    complementary = (inter == 0 and LQ.rank(Vk + Zk) == len(Kc))
    r1 = LQ.rank([r[:] for r in C] + [r[:] for r in CA])
    rowC = LQ.rank([r[:] for r in C])
    return dict(n=n, p=p, r=len(L0), cl=cl,
                h=res['h'], s=res['s'], m=res['m'], d_fin=res['d_fin'],
                eps=tuple(res['eps_smith']), sum_eps=sum(res['eps_smith']),
                five_b=res['five_b'],
                complementary=complementary, h_eq_np=(res['h'] == n - p),
                cl_eq_n_r1=(cl == n - r1), n_r1=n - r1,
                rankCL_full=(LQ.rank([r[:] for r in C] + [r[:] for r in Vmin]) == p + cl),
                Vmin_meets_rowC=(len(Vmin) + rowC - LQ.rank(Vmin + C) > 0))


def main():
    rows = []
    for n in (5, 6):
        for p in (1, 2):
            for r in (1, 2):
                if p + r > n:
                    continue
                for seed in range(3000, 3010):
                    made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
                    if made is None:
                        continue
                    A, C, L0 = made
                    O = QR.observability_matrix(A, C)
                    if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
                        continue
                    rows.append(features(A, C, L0))
    nfeas = sum(1 for x in rows if x['five_b'])
    print(f'实例 {len(rows)}：闭包处 (5b) 成立 {nfeas}，不成立 {len(rows) - nfeas}\n')

    # 交叉表：每个候选不变量
    keys = ['cl', 'h', 's', 'm', 'd_fin', 'sum_eps', 'complementary', 'h_eq_np',
            'cl_eq_n_r1', 'rankCL_full', 'Vmin_meets_rowC']
    for k in keys:
        tab = defaultdict(lambda: [0, 0])
        for x in rows:
            tab[x[k]][0 if x['five_b'] else 1] += 1
        cells = '  '.join(f'{v}:{a}/{b}' for v, (a, b) in sorted(tab.items(), key=lambda t: str(t[0])))
        print(f'  {k:16s} (成立/不成立)  {cells}')

    print('\n不成立（14 个）的实例：')
    for x in rows:
        if not x['five_b']:
            print(f"  n={x['n']} p={x['p']} r={x['r']} cl={x['cl']} h={x['h']} s={x['s']} m={x['m']} "
                  f"d_fin={x['d_fin']} eps={x['eps']} 互补={x['complementary']} h=n-p={x['h_eq_np']} "
                  f"cl=n-r1={x['cl_eq_n_r1']}")
    print('\n成立（前 10 个）：')
    shown = 0
    for x in rows:
        if x['five_b'] and shown < 10:
            print(f"  n={x['n']} p={x['p']} r={x['r']} cl={x['cl']} h={x['h']} s={x['s']} m={x['m']} "
                  f"d_fin={x['d_fin']} eps={x['eps']} 互补={x['complementary']} h=n-p={x['h_eq_np']}")
            shown += 1


if __name__ == '__main__':
    main()
