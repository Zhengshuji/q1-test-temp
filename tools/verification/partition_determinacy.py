"""partition_determinacy.py —— 左指标划分是否由聚合数据 $(q,p,h,\\operatorname{rank}L)$ 决定？

专家 2026-11-02 §3 把剩余问题定为"左指标的划分"。一个自然的问题是：
**给定聚合数据 $(q,p,h,\\operatorname{rank}L)$，划分是否唯一？** 若不是，划分就依赖更多结构，
"聚合层面完全确定"的说法要保留（聚合量确定，但划分不）。

本脚本按 $(q,p,h,r)$ 分组，报告每组观测到的不同划分；并打印"同一组里出现 $\ge2$ 种划分"的例子
（若存在），这就是"划分不由聚合数据决定"的**精确证据**。

用法：python tools/verification/partition_determinacy.py
"""

import os
import sys
from collections import defaultdict
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


def candidates(A, C, L0, n, seed, trials=3):
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


def rho_c(L, A, C):
    CA = LQ.mul(C, A)
    J = LQ.stack(C, CA)
    j = LQ.rank(J)
    rv = LQ.rank(L)
    c = rv + j - LQ.rank([r[:] for r in L] + J)
    return rv - c, c


def main():
    groups = defaultdict(set)       # (q,p,h,r) -> {eps}
    examples = defaultdict(list)    # 同上 -> [(n,seed,L,eps)]
    feas = 0
    for n in (6, 7, 8):
        for k in range(8):
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
                try:
                    info = OP.observer_pencil(A, C, L)
                except AssertionError:
                    continue
                if not info['five_b']:
                    continue
                feas += 1
                kk = info['kron']
                r = LQ.rank(L)
                grp = (len(L), len(C), info['h'], r)
                eps = tuple(kk['left_min_indices'])
                groups[grp].add(eps)
                if len(examples[grp]) < 4:
                    examples[grp].append((n, seed, L, eps))
    print(f'可行铅笔 {feas} 个；$(q,p,h,r)$ 组数 {len(groups)}')
    multi = {g: v for g, v in groups.items() if len(v) >= 2}
    print(f'其中出现 ≥2 种划分的组：{len(multi)} 个')
    for g, v in sorted(multi.items())[:8]:
        print(f'  (q,p,h,r)={g}: {sorted(v)}')
        for e in examples[g][:2]:
            print(f'     例：n={e[0]} seed={e[1]} q={len(e[2])} eps={e[3]}')
    if not multi:
        print('  **没有**发现同组多种划分（样本内）；这不能证明"划分由聚合数据决定"，只说明样本不足。')
    else:
        print('\n结论：划分**不由** $(q,p,h,\\operatorname{rank}L)$ 单独决定（上面是精确反例）。')


if __name__ == '__main__':
    main()
