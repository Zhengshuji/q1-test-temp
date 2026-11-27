"""family_sequences.py —— 固定 $(A,C,L_0,q)$ 的增广族内，左指标序列是否变化？（专家 §12 第 3–4 步）

专家 2026-11-02 把"同一固定 $(A,C,L_0,q)$ 的族内是否出现不同指标序列"列为**最重要的实验**
（答复 §12 第 4 步）。本脚本：

  1. 对每个实例算 $q_0$（`tools/ledger/c208_q0_lower_bound.py: eta_and_q0`，P1 Thm 2 的算法）；
  2. 对 $q\\in\\{q_0,q_0+1,q_0+2\\}$ 收集**恰好 $q$ 行**且满足 $(5a)$ 的候选 $L$（三个来源：
     可观性链、$A$-不变闭包、模 $\\mathcal J$ 不变提升）；
  3. 对每个 $L$ 用 **Toeplitz 判据**（[toeplitz_criterion.py](toeplitz_criterion.py)）算
     $(\\varepsilon,\\ \\sum\\varepsilon,\\ d_{\\rm fin},\\ (5b))$；
  4. 按 $(\\text{seed},q)$ 分组，报告不同序列 / 不同 $\\sum\\varepsilon$ / 不同 $(5b)$ 判定。

**边界声明**：候选族**不全**（专家 §6.1：参数化必须完备，否则否定结果无意义）。因此
"样本内序列唯一"**不能**推出"序列由聚合数据决定"；只有"同族内出现不同序列"才是硬结论。

用法：python tools/verification/family_sequences.py
输出：workspace/kronecker/data/family_sequences.tsv + 终端摘要。
"""

import os
import sys
from collections import defaultdict
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger', 'tools/p_algorithm'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import observer_pencils as OP             # noqa: E402
import modJ_candidates as MJ              # noqa: E402
import kron_sweep as KS                   # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import p1_family as P1F                   # noqa: E402
from find_layer_instance import make_instance  # noqa: E402

F = Fraction


def chain_L(A, C, k):
    """可观性链 $[C;CA;\\dots;CA^{k-1}]$（$k$ 行）。"""
    rows = []
    cur = [row[:] for row in C]
    for _ in range(k):
        rows += [row[:] for row in cur]
        cur = LQ.mul(cur, A)
    return rows


def candidate_Ls_fixed_q(A, C, L0, n, seed, q, trials=3):
    r"""收集恰好 $q$ 行、行满秩、含 $L_0$ 且满足 $(5a)$ 的候选（去重）。

    主来源：**P1 §V 的族在阶 $q$ 上的推广**（`p1_family.sample_q`，$k=q-r$）；
    补充来源：可观性链、$A$-不变闭包、模 $\mathcal J$ 不变提升。
    """
    out, seen = [], set()
    # 0) P1 族（任意阶）
    try:
        for _J, _th, L in P1F.sample_q(A, C, L0, q, n_per_chart=5, seed=seed):
            if len(L) != q:
                continue
            rL = LQ.rank(L)
            if rL != len(L):
                continue
            if LQ.rank([r[:] for r in L] + [r[:] for r in L0]) != rL:
                continue
            if LQ.condA(A, C, L):
                key = tuple(tuple(str(x) for x in r) for r in L)
                if key not in seen:
                    seen.add(key)
                    out.append(L)
    except AssertionError:
        pass

    def push(L):
        if len(L) != q:
            return
        key = tuple(tuple(str(x) for x in r) for r in L)
        if key in seen:
            return
        seen.add(key)
        # 行满秩（否则有冗余行，去掉后 q 更小 ⟹ 不可能是最小 q 的解）
        rL = LQ.rank(L)
        if rL != len(L):
            return
        # CLAUDE 纪律 5：显式检查 row(L0) ⊆ row(L)（正确形式：与 rank(L) 比，不是与 len(L) 比）
        if LQ.rank([r[:] for r in L] + [r[:] for r in L0]) != rL:
            return
        if LQ.condA(A, C, L):
            out.append(L)

    # 1) 可观性链（长度 = q）
    if 1 <= q <= n:
        push(chain_L(A, C, q))
    # 2) A-不变闭包 + 扩张
    try:
        for L in OP.candidate_Ls(A, C, L0, n_extra=1, trials=trials, seed=seed):
            push(L)
    except AssertionError:
        pass
    # 3) 模 J 不变提升
    try:
        for L in MJ.candidate_Ls_modJ(A, C, L0, trials=trials, seed=seed):
            push(L)
    except AssertionError:
        pass
    return out


def main():
    rows = []
    groups = defaultdict(list)
    tested = 0
    inst_used = 0
    for n in (5, 6, 7):
        for k in range(3):
            seed = 1000 + k
            try:
                A, C, L0 = make_instance(n, seed)
            except Exception:
                continue
            q0 = Q0.eta_and_q0(A, C, L0)[0]
            inst_used += 1
            for q in (q0, q0 + 1, q0 + 2):
                if q < len(L0) or q > n:
                    continue
                cands = candidate_Ls_fixed_q(A, C, L0, n, seed, q)
                for L in cands:
                    r = TC.analyse(A, C, L)
                    assert r['eps_agree'] and r['crit_agree'], 'Toeplitz 与 Smith 不一致'
                    assert len(r['eps_smith']) == r['m']
                    assert sum(r['eps_smith']) == r['s'] - r['d_fin']
                    assert r['nu_s'] == (r['s'] + 1) * r['m'] - r['s'] + r['d_fin']
                    tested += 1
                    rec = dict(n=n, seed=seed, q=q, q0=q0, h=r['h'], s=r['s'], m=r['m'],
                               d_fin=r['d_fin'], eps=tuple(r['eps_smith']),
                               sum_eps=sum(r['eps_smith']), five_b=r['five_b'])
                    rows.append(rec)
                    groups[(n, seed, q)].append(rec)

    out_dir = os.path.join(_ROOT, 'workspace', 'kronecker', 'data')
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, 'family_sequences.tsv')
    with open(out, 'w', encoding='utf-8', newline='') as fh:
        fh.write('n\tseed\tq\tq0\th\ts\tm\td_fin\teps\tsum_eps\tfive_b\n')
        for r in rows:
            fh.write(f'{r["n"]}\t{r["seed"]}\t{r["q"]}\t{r["q0"]}\t{r["h"]}\t{r["s"]}\t{r["m"]}\t'
                     f'{r["d_fin"]}\t{list(r["eps"])}\t{r["sum_eps"]}\t{r["five_b"]}\n')

    print(f'实例 {inst_used} 个，铅笔 {tested} 个，分组 {len(groups)} 个 → {os.path.relpath(out, _ROOT)}')
    multi_eps, multi_sum, multi_5b = [], [], []
    for key, recs in sorted(groups.items()):
        eps_set = {r['eps'] for r in recs}
        sum_set = {r['sum_eps'] for r in recs}
        fb_set = {r['five_b'] for r in recs}
        if len(eps_set) >= 2:
            multi_eps.append((key, eps_set, len(recs)))
        if len(sum_set) >= 2:
            multi_sum.append((key, sum_set, len(recs)))
        if len(fb_set) >= 2:
            multi_5b.append((key, fb_set, len(recs)))
    print(f'\n同一 (n,seed,q) 内出现 ≥2 种指标序列的组：{len(multi_eps)}')
    for key, s_set, cnt in multi_eps[:6]:
        print(f'  (n,seed,q)={key}（{cnt} 个铅笔）：{sorted(s_set)}')
    print(f'同一 (n,seed,q) 内 sum(eps) 取 ≥2 个值的组：{len(multi_sum)}')
    for key, s_set, cnt in multi_sum[:6]:
        print(f'  (n,seed,q)={key}（{cnt} 个铅笔）：{sorted(s_set)}')
    print(f'同一 (n,seed,q) 内 (5b) 判定不一致的组：{len(multi_5b)}')
    for key, s_set, cnt in multi_5b[:6]:
        print(f'  (n,seed,q)={key}（{cnt} 个铅笔）：{sorted(s_set)}')
    if not multi_eps and not multi_sum and not multi_5b:
        print('  （样本内未发现同族差异；候选族不全，不能据此下结论）')
    print('\n注：候选族不全（专家 §6.1）；只有"同族内出现不同序列"是硬结论。')


if __name__ == '__main__':
    main()
