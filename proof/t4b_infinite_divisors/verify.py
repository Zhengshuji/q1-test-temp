"""verify.py —— T4-b / B.7 的精确验证（**含有限部分的更正**，专家 2026-11-02 §2）

定理（[theorem.md](theorem.md)）：
  * **B.7**：设 $L$ 满足 $(5a)$，$h=\\operatorname{rank}[L;CA;C]$。则 $Q_L$ 的无穷初等因子全是 1 次，且
    $$d_\\infty=h-\\operatorname{rank}L .$$
  * **正确的推论**（**只用 $(5a)$**）：由 B.6（$\\sum\\eta=0$）与全局恒等式
    $$\\sum\\eta+\\sum\\varepsilon+d_{\\rm fin}+d_\\infty=h$$
    得
    $$\\sum_j\\varepsilon_j=\\operatorname{rank}L-d_{\\rm fin}.$$
    只有在 $(5a)+(5b)$（即 $d_{\\rm fin}=0$）时才有 $\\sum\\varepsilon=\\operatorname{rank}L$。

本脚本对**所有**满足 $(5a)$ 的候选核对四条：
  1. $d_\\infty=h-\\operatorname{rank}L$；
  2. $\\sum\\varepsilon=\\operatorname{rank}L-d_{\\rm fin}$；
  3. $\\sum\\varepsilon+d_{\\rm fin}+d_\\infty=h$（且 $\\sum\\eta=0$）；
  4. 若 $d_{\\rm fin}=0$（即 $(5b)$ 成立）则 $\\sum\\varepsilon=\\operatorname{rank}L$。

**验证不是证明**；证明见 theorem.md。
"""

import os
import sys
from collections import Counter
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import linalg_q as LQ                     # noqa: E402
import kronecker_pencil as KP             # noqa: E402
import observer_pencils as OP             # noqa: E402
import modJ_candidates as MJ              # noqa: E402
import kron_sweep as KS                   # noqa: E402
from find_layer_instance import make_instance  # noqa: E402

F = Fraction


def candidates(A, C, L0, n, seed, trials=2):
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
    tested = feas = 0
    bad = []
    d_fin_dist = Counter()
    for n in (6, 7, 8, 9, 10):
        for k in range(4):
            seed = 1000 + k
            try:
                A, C, L0 = make_instance(n, seed)
            except Exception:
                continue
            seen = set()
            for L in candidates(A, C, L0, n, seed):
                key = tuple(tuple(str(x) for x in r) for r in L)
                if key in seen:
                    continue
                seen.add(key)
                if not LQ.condA(A, C, L):
                    continue
                tested += 1
                P0, P1, h = OP.pencil_from_L(A, C, L)
                kk = KP.pencil_kronecker(P0, P1)
                rankL = LQ.rank(L)
                d_inf = kk['d_infinity']
                d_fin = sum(d['degree'] for d in kk['finite_divisors'])
                sum_eta = sum(kk['right_min_indices'])
                sum_eps = sum(kk['left_min_indices'])
                d_fin_dist[d_fin] += 1
                if d_fin == 0:
                    feas += 1
                # 1. B.7
                if d_inf != h - rankL:
                    bad.append(dict(kind='B.7', n=n, seed=seed, q=len(L), h=h, rankL=rankL, d_inf=d_inf))
                # 2. 正确的左指标公式
                if sum_eps != rankL - d_fin:
                    bad.append(dict(kind='sum_eps', n=n, seed=seed, q=len(L),
                                    rankL=rankL, d_fin=d_fin, sum_eps=sum_eps))
                # 3. 全局恒等式
                if sum_eps + d_fin + d_inf != h or sum_eta != 0:
                    bad.append(dict(kind='identity', n=n, seed=seed, q=len(L),
                                    sum_eta=sum_eta, sum_eps=sum_eps, d_fin=d_fin, d_inf=d_inf, h=h))
                # 4. (5b) 时更强
                if d_fin == 0 and sum_eps != rankL:
                    bad.append(dict(kind='feasible', n=n, seed=seed, q=len(L),
                                    rankL=rankL, sum_eps=sum_eps))
                # 每个无穷因子次数为 1
                if any(d['mu_valuation'] > 1 for d in kk['infinite_divisors']):
                    bad.append(dict(kind='degree>1', n=n, seed=seed, q=len(L),
                                    vals=[d['mu_valuation'] for d in kk['infinite_divisors']]))
    print(f'满足 (5a) 的铅笔：{tested} 个（其中 d_fin=0，即 (5b) 成立：{feas} 个）')
    print(f'反例：{len(bad)} 个')
    for b in bad[:6]:
        print('  ', b)
    print(f'd_fin 的分布（截断）：{dict(sorted(d_fin_dist.items())[:8])}')
    assert not bad, '出现反例'
    print('✓ 全部通过：B.7（d_inf=h-rankL）、sum_eps=rankL-d_fin、恒等式、以及 (5b) 时的 sum_eps=rankL')


if __name__ == '__main__':
    main()
