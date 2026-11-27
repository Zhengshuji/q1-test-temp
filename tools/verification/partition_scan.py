"""partition_scan.py —— 左指标划分的可实现性（专家优先级 5）

背景：专家 2026-11-02 §3 把剩余问题定为"左指标 $\varepsilon_1\ge\cdots\ge\varepsilon_s\ge0$ 的划分"，
$s=q+2p-h$，且（$(5a)+(5b)$ 时）$\sum_j\varepsilon_j=\operatorname{rank}L$；必要条件 $\operatorname{rank}L\le s$。

本脚本：
  1. 在大量满足 $(5a)+(5b)$ 的实例$\\times$候选上收集 $(\operatorname{rank}L,\ s,\ \varepsilon)$；
  2. 对每个 $(r,s)$ 对，列出**观测到的**划分集合，与**全部**划分（把 $r$ 分成 $s$ 个非负整数、
     降序、允许零）的总数比较；
  3. 报告：是否每个观测都满足必要条件的等式/不等式；哪些划分从没出现。

**注意**：采样只能"发现反例/缺失"，不能证明"全部可实现"。
"""

import os
import sys
from collections import defaultdict
from fractions import Fraction
from itertools import combinations_with_replacement

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


def all_partitions(r, s):
    """把 r 分成至多 s 个非负整数的降序序列（补零到长度 s）的集合。"""
    out = set()
    if s == 0:
        return {()} if r == 0 else set()
    if r == 0:
        return {tuple([0] * s)}
    # 枚举长度 <= s 的正整数降序划分
    def gen(rem, maxv, parts):
        if rem == 0:
            out.add(tuple(sorted(parts + [0] * (s - len(parts)), reverse=True)))
            return
        if len(parts) == s:
            return
        for v in range(min(rem, maxv), 0, -1):
            gen(rem - v, v, parts + [v])
    gen(r, r, [])
    return out


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
    seen = defaultdict(set)      # (r, s) -> {partition}
    tested = feas = 0
    violated = []
    for n in (6, 7, 8, 9):
        for k in range(6):
            seed = 1000 + k
            try:
                A, C, L0 = make_instance(n, seed)
            except Exception:
                continue
            seenL = set()
            for L in candidates(A, C, L0, n, seed):
                key = tuple(tuple(str(x) for x in r) for r in L)
                if key in seenL:
                    continue
                seenL.add(key)
                if not LQ.condA(A, C, L):
                    continue
                tested += 1
                P0, P1, h = OP.pencil_from_L(A, C, L)
                kk = KP.pencil_kronecker(P0, P1)
                d_fin = sum(d['degree'] for d in kk['finite_divisors'])
                if d_fin != 0:          # 只要 (5b) 的
                    continue
                feas += 1
                r = LQ.rank(L)
                s = len(kk['left_min_indices'])      # = q+2p-h
                eps = tuple(kk['left_min_indices'])
                assert len(eps) == s
                if sum(eps) != r:
                    violated.append(dict(n=n, seed=seed, q=len(L), r=r, s=s, eps=eps))
                # 注意（2026-11-02 更正）：曾经以为必有 rankL <= s（专家 §2），**那是错的**——
                # 反例：n=6, seed=1001, q=6, rankL=6, s=2, eps=[5,1]。单个左指标可以很大，
                # 所以 "rankL <= s" 不成立。这里不把它当约束。
                seen[(r, s)].add(eps)
    print(f'满足 (5a) 的铅笔 {tested} 个，其中 (5b) 成立 {feas} 个')
    print(f'违反必要条件（sum(eps)=rankL 或 rankL<=s 或长度=s）：{len(violated)} 个')
    for v in violated[:5]:
        print('  ', v)
    assert not violated

    print('\n(r, s) | 观测到的划分个数 | 全部划分的个数 | 是否全覆盖')
    total_seen = total_all = 0
    missing_examples = []
    for (r, s) in sorted(seen):
        obs = seen[(r, s)]
        allp = all_partitions(r, s)
        total_seen += len(obs)
        total_all += len(allp)
        cover = 'YES' if obs >= allp else f'no（缺 {len(allp - obs)}）'
        print(f'  ({r},{s}) | {len(obs)} | {len(allp)} | {cover}')
        if obs < allp and len(missing_examples) < 5:
            miss = sorted(allp - obs)
            missing_examples.append(((r, s), miss[:3]))
    print(f'\n合计：观测到 {total_seen} 个不同划分，全部可能的合计 {total_all} 个')
    if missing_examples:
        print('缺失划分的例子：')
        for key, miss in missing_examples:
            print(f'  (r,s)={key}: {miss}')


if __name__ == '__main__':
    main()
