"""kron_dinfty_stats.py —— 可行铅笔的 $d_\\infty$ 与左指标统计（T4-b / T4-c）

对每个**可行**（$(5b)$ 成立）的观测器铅笔记录：
  $h$、$\\operatorname{rank}L$、$d_\\infty$（无穷初等因子的总次数 = 反转铅笔非零不变因子的次数和）、
  $\\sum\\varepsilon$、$\\#\\varepsilon=q+2p-h$、$\\sum\\eta$（按 B.6 定理应为 0）。

检验两条关系：
  (i) 恒等式：$\\sum\\eta+\\sum\\varepsilon+d_\\infty=h$；
  (ii) **$d_\\infty=0\\iff\\operatorname{rank}L=h$**（$Q_1=[L;0;0]$ 的秩 = normal rank 的判据）。

用法：python tools/verification/kron_dinfty_stats.py
"""

import os
import sys
from collections import Counter, defaultdict
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import linalg_q as LQ                     # noqa: E402
import observer_pencils as OP             # noqa: E402
import modJ_candidates as MJ              # noqa: E402
import kronecker_pencil as KP             # noqa: E402
import kron_sweep as KS                   # noqa: E402
from find_layer_instance import make_instance  # noqa: E402

F = Fraction


def all_candidates(A, C, L0, n, seed, trials=2):
    out = []
    CAk = [row[:] for row in C]
    for k in range(1, n + 1):
        out.append([row[:] for row in CAk])
        CAk = CAk + LQ.mul(C, KS._pow(A, k))
    try:
        out += list(OP.candidate_Ls(A, C, L0, n_extra=1, trials=trials, seed=seed))
    except AssertionError:
        pass
    try:
        out += list(MJ.candidate_Ls_modJ(A, C, L0, trials=trials, seed=seed))
    except AssertionError:
        pass
    return out


def main():
    rows = []
    for n in (6, 7, 8):
        for k in range(6):
            seed = 1000 + k
            try:
                A, C, L0 = make_instance(n, seed)
            except Exception:
                continue
            seen = set()
            for L in all_candidates(A, C, L0, n, seed):
                key = tuple(tuple(str(x) for x in r) for r in L)
                if key in seen:
                    continue
                seen.add(key)
                if not LQ.condA(A, C, L):
                    continue
                try:
                    info = OP.observer_pencil(A, C, L)
                except AssertionError:
                    continue
                if not info['five_b']:
                    continue
                kk = info['kron']
                rho, c = KS.rho_c(L, A, C)
                d_inf = kk['d_infinity']
                sum_eta = sum(kk['right_min_indices'])
                sum_eps = sum(kk['left_min_indices'])
                rows.append(dict(n=n, seed=seed, q=len(L), rho=rho, c=c, h=info['h'],
                                 rankL=LQ.rank(L), d_inf=d_inf,
                                 sum_eta=sum_eta, sum_eps=sum_eps,
                                 n_eps=len(kk['left_min_indices']),
                                 n_eta=len(kk['right_min_indices'])))

    print(f'可行铅笔总数：{len(rows)}')
    # (i) 恒等式
    bad = [r for r in rows if r['sum_eta'] + r['sum_eps'] + r['d_inf'] != r['h']]
    print(f'(i) 恒等式 sum(eta)+sum(eps)+d_inf = h：{len(rows) - len(bad)}/{len(rows)} 通过')
    for r in bad[:3]:
        print('   **失败**', r)
    # (ii) d_inf = 0 <=> rank L = h
    bad2 = [r for r in rows if (r['d_inf'] == 0) != (r['rankL'] == r['h'])]
    print(f'(ii) d_inf=0 <=> rank L = h：{len(rows) - len(bad2)}/{len(rows)} 通过')
    for r in bad2[:3]:
        print('   **失败**', r)
    # (iii) B.6: sum_eta = 0
    bad3 = [r for r in rows if r['sum_eta'] != 0]
    print(f'(iii) B.6（sum_eta=0）：{len(rows) - len(bad3)}/{len(rows)} 通过')

    # 按 (rho,c) 分组看 d_inf 的分布
    print('\nd_inf 按 (rho,c) 分组：')
    by = defaultdict(list)
    for r in rows:
        by[(r['rho'], r['c'])].append(r['d_inf'])
    for key in sorted(by):
        vals = by[key]
        print(f'  (rho,c)={key}: {len(vals)} 个，d_inf 取值 {Counter(vals)}')
    print('\nd_inf 按 q 分组（各 n）：')
    by2 = defaultdict(list)
    for r in rows:
        by2[(r['n'], r['q'])].append(r['d_inf'])
    for key in sorted(by2)[:12]:
        print(f'  (n,q)={key}: {Counter(by2[key])}')
    print(f'\n形如 (h, rankL, d_inf) 的组合：{Counter((r["h"], r["rankL"], r["d_inf"]) for r in rows)}')


if __name__ == '__main__':
    main()
