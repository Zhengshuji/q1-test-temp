"""kron_t4b_search.py —— 在 $n=9,10$ 上搜 T4-b 的反例（专家优先级 5）

T4-b（待证）：对满足 $(5a)+(5b)$ 的观测器铅笔，
$$d_\\infty=h-\\operatorname{rank}L\\quad(\\text{等价地 }\\textstyle\\sum_j\\varepsilon_j=\\operatorname{rank}L).$$
一般铅笔只有 $d_\\infty\\ge h-\\operatorname{rank}L$。**反例** = 某个可行铅笔满足 $d_\\infty>h-\\operatorname{rank}L$。

本脚本对指定 $n$ 与若干 seed，枚举候选 $L$（可观性链 / $A$-不变闭包 / 模 $\\mathcal J$ 提升），
用精确 $(5a)$ 过滤，再算 Kronecker 数据，最后统计 T4-b 是否处处成立。

用法：python tools/verification/kron_t4b_search.py [n1 n2 ...]
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


def search(ns, seeds=3):
    feas = 0
    viol = []
    tested = 0
    for n in ns:
        for k in range(seeds):
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
                try:
                    info = OP.observer_pencil(A, C, L)
                except AssertionError:
                    continue
                if not info['five_b']:
                    continue
                feas += 1
                kk = info['kron']
                h = info['h']
                rankL = LQ.rank(L)
                d_inf = kk['d_infinity']
                sum_eta = sum(kk['right_min_indices'])
                sum_eps = sum(kk['left_min_indices'])
                # T4-b 两种等价形式
                ok_b = (d_inf == h - rankL)
                ok_c = (sum_eps == rankL)
                # 恒等式（应恒成立）
                ident = (sum_eta + sum_eps + d_inf == h)
                if not (ok_b and ok_c and ident):
                    viol.append(dict(n=n, seed=seed, q=len(L), h=h, rankL=rankL,
                                     d_inf=d_inf, sum_eta=sum_eta, sum_eps=sum_eps,
                                     ident=ident, ok_b=ok_b, ok_c=ok_c))
    return dict(tested=tested, feas=feas, viol=viol)


def main():
    ns = [int(a) for a in sys.argv[1:]] or [9, 10]
    res = search(ns, seeds=int(os.environ.get('KRON_SEEDS', '6')))
    print(f'\n尺寸 {ns}：合法铅笔 {res["tested"]} 个，可行 {res["feas"]} 个')
    print(f'T4-b 反例（d_inf > h - rankL 或 sum(eps) != rankL）：{len(res["viol"])} 个')
    for v in res["viol"][:5]:
        print('  ', v)
    if res["feas"]:
        print('  （T4-b 在全部可行样本上成立 ⟹ 未找到反例）' if not res["viol"]
              else '  **需要人工核查**')
    return res


if __name__ == '__main__':
    r = main()
    assert not r['viol'], 'T4-b 反例！'
