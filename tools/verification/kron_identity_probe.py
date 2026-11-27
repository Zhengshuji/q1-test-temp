"""kron_identity_probe.py —— 检查"恒等式代理量"在一般铅笔上**失效**

背景（专家 2026-11-02 §3）：对任意 $m\\times n$ 铅笔（normal rank $r$），有全局恒等式
    $$\\sum_i\\eta_i+\\sum_j\\varepsilon_j+\\sum_k\\deg\\gamma_k=r,$$
其中 $\\gamma_k$ 是**齐次**不变因子。

**陷阱**：$\\sum\\deg\\gamma_k$ **不等于** "(有限不变因子次数和) + (反转铅笔次数和)"。
本脚本用具体铅笔示范这个失效，避免把它当公式用。

在 (5b) 型（无有限初等因子）时，$\\deg\\gamma_k$ 全由无穷部分贡献，故有可核对的特例
    $$\\sum\\eta+\\sum\\varepsilon+d_\\infty=r,$$
本脚本同时核对这个特例**在可行铅笔上成立**。

用法：python tools/verification/kron_identity_probe.py
"""

import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import kronecker_pencil as KP             # noqa: E402
import observer_pencils as OP             # noqa: E402
import linalg_q as LQ                     # noqa: E402
from find_layer_instance import make_instance  # noqa: E402

F = Fraction


def probe(P0, P1, name):
    r = KP.normal_rank(P0, P1)
    inv = KP.smith_invariants_of_pencil(P0, P1)
    invr = KP.smith_invariants_of_pencil(P1, P0)
    eta, _ = KP.minimal_indices(P0, P1)
    eps, _ = KP.minimal_indices(KP.transpose(P0), KP.transpose(P1))
    fin = sum(KP.pdeg(d) for d in inv if not KP._pzero(d))
    inf = sum(KP.pdeg(d) for d in invr if not KP._pzero(d))
    no_fin = all(KP.pdeg(d) == 0 for d in inv if not KP._pzero(d))
    proxy = sum(eta) + sum(eps) + fin + inf
    print(f'  [{name}] r={r} sum_eta={sum(eta)} sum_eps={sum(eps)} '
          f'fin_deg={fin} inf_deg={inf} no_fin={no_fin}')
    print(f'      代理量 sum(eta)+sum(eps)+fin+inf = {proxy}  vs  r = {r}'
          + ('  ⟹ **不等**（代理量失效）' if proxy != r else '  ✓'))
    if no_fin:
        ok = (sum(eta) + sum(eps) + inf == r)
        print(f'      (5b) 型特例 sum(eta)+sum(eps)+inf = {sum(eta)+sum(eps)+inf} vs r = {r}'
              + ('  ✓' if ok else '  ✗'))
        assert ok, '(5b) 型特例不成立'
    return proxy, r


def main():
    print('=== 1. 解析例：Q(λ) = [λ 1]（1×2，rank 恒 1）===')
    # 专家的反例：常数秩，但右最小指标 = 1（不是 0）
    P0 = [[F(0), F(1)]]
    P1 = [[F(1), F(0)]]
    k = KP.pencil_kronecker(P0, P1)
    print(f'  rank={k["normal_rank"]} eta={k["right_min_indices"]} eps={k["left_min_indices"]}'
          f' fin={[d["degree"] for d in k["finite_divisors"]]}'
          f' inf={[d["degree"] for d in k["infinite_divisors"]]}')
    assert k['right_min_indices'] == [1], '专家反例应给出右最小指标 1'
    print('  ⟹ 常数秩**不**意味着右最小指标为 0（专家 2026-11-02 §1 的反例）')

    print('\n=== 2. 一般铅笔：代理量失效的例子 ===')
    for seed, want_q in [(1000, 5), (1002, 4)]:
        A, C, L0 = make_instance(6, seed)
        for L in OP.candidate_Ls(A, C, L0, n_extra=1, trials=4, seed=seed):
            if len(L) != want_q or not LQ.condA(A, C, L):
                continue
            P0, P1, h = OP.pencil_from_L(A, C, L)
            probe(P0, P1, f'seed{seed} q={len(L)}')
            break

    print('\n=== 3. 可行铅笔：(5b) 型特例成立 ===')
    A, C, L0 = make_instance(6, 1010)
    for L in OP.candidate_Ls(A, C, L0, n_extra=1, trials=4, seed=1010):
        if len(L) != 4 or not LQ.condA(A, C, L):
            continue
        P0, P1, h = OP.pencil_from_L(A, C, L)
        info = OP.observer_pencil(A, C, L)
        if not info['five_b']:
            continue
        probe(P0, P1, 'seed1010 q=4（可行）')
        break

    print('\n完成：代理量在一般情形失效；(5b) 型特例在可行铅笔上成立。')


if __name__ == '__main__':
    main()
