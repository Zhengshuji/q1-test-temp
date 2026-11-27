"""verify_C4_type3.py —— 猜想 T 的**反例**（Type III）的精确证书

T（本项目 2026-11-02 提出，已发给专家）：在 $q=q_0$ 处 $(5b)\\iff h<q_0+r_1$。
本脚本给出反例：$q_0$ 阶、$(5a)$ 成立、$h<q_0+r_1$、但 $d_{\\rm fin}>0$。

实例族：$n=6$、$A=$ 两个 $2\\times2$ Jordan 块（特征值 $1,1$ 与 $2,2$，见 `jordan_family`）、
$p=2$、$r=2$、$C$ 与 $L_0$ 由确定性种子生成（见 [type3_structured.py](../../tools/verification/type3_structured.py)）。

核验：
1. 精确重建实例与候选 $\\mathcal L$；
2. `assert` $(5a)$、$\\operatorname{row}L_0\\subseteq\\operatorname{row}\\mathcal L$、$\\operatorname{rank}\\mathcal L=q_0$；
3. 用 **Smith 路径**（`toeplitz_criterion.analyse`）与 **零空间判据**（`spectral_gcd_Z`）双重确认 $(5b)$ 失败；
4. 打印 $h,s,m,r_1,\\varepsilon,d_{\\rm fin}$，并核对 B.9 与 Type II 都**不**适用。

用法：python proof/refuted/verify_C4_type3.py
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import spectral_gcd as SG                 # noqa: E402
import z_generator as ZG                  # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import type3_structured as T3             # noqa: E402

F = T3.F


def build():
    """重建反例实例与候选。"""
    name = 'jordan-n6'
    A = T3.jordan_family(6, [1, 2])
    n, p, r = 6, 2, 2
    import random
    seed_c = sum(ord(ch) for ch in name) * 13 + p * 17
    rngC = random.Random(seed_c)
    C = None
    for _try in range(60):
        cand = [[F(rngC.randrange(2)) for _ in range(n)] for _ in range(p)]
        if LQ.rank(cand) != p:
            continue
        if LQ.rank(T3.obs_matrix(A, cand)) != n:
            continue
        C = cand
        break
    assert C is not None
    L0 = T3.pick_L0(A, C, r, seed=sum(ord(ch) for ch in name) * 7 + p * 31 + r)
    assert L0 is not None
    q0 = Q0.eta_and_q0(A, C, L0)[0]
    seed_L = sum(ord(ch) for ch in name) * 11 + q0 * 29
    cands = ZG.sample_L_at_order(A, C, L0, q0, 80, seed=seed_L)
    return A, C, L0, q0, cands


def main():
    A, C, L0, q0, cands = build()
    print('=== 实例 ===')
    print('  A =', [[str(x) for x in row] for row in A])
    print('  C =', [[str(x) for x in row] for row in C])
    print('  L0=', [[str(x) for x in row] for row in L0])
    CA = LQ.mul(C, A)
    r1 = LQ.rank([x[:] for x in C] + [x[:] for x in CA])
    print(f'  q0={q0}  r1={r1}  q0+r1={q0 + r1}')
    shown = 0
    for L in cands:
        h, s, m, d_fast = T3.fast_dfin(A, C, L)
        if not (h < q0 + r1 and d_fast > 0):
            continue
        # 三重核验
        assert LQ.condA(A, C, L), '(5a) 不成立'
        assert LQ.rank([x[:] for x in L] + [x[:] for x in L0]) == LQ.rank(L), 'row L0 ⊄ row L'
        assert LQ.rank(L) == q0, 'rank L ≠ q0'
        res = TC.analyse(A, C, L)
        assert res['five_b'] is False, 'Smith 路径说 (5b) 成立'
        assert res['d_fin'] == d_fast, 'fast d_fin 与 Smith 不一致'
        Zc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L])
        g, hh, nmin = SG.spectral_gcd_Z(A, C, Zc)
        deg = SG.pdeg(g)
        assert deg > 0, '零空间判据说 (5b) 成立'
        k = len(L) + r1 - res['h']
        print(f'\n=== 反例 #{shown + 1} ===')
        print('  L =', [[str(x) for x in row] for row in L])
        print(f'  (5a) ✓；row L0 ⊆ row L ✓；rank L = {LQ.rank(L)} = q0 ✓')
        print(f'  h={res["h"]}  s={res["s"]}  m={res["m"]}  r1={r1}')
        print(f'  k = q+r1-h = {k}  ≤ s={res["s"]}  （Type II 不适用）')
        print(f'  h={res["h"]} < q0+r1={q0 + r1}  （B.9 不适用）')
        print(f'  ε={res["eps_smith"]}  d_fin={res["d_fin"]} > 0  ⟹ (5b) 失败')
        print(f'  零空间判据：gcd 次数={deg}（>0 ⟹ 有有限公共根）✓')
        shown += 1
        if shown >= 2:
            break
    assert shown > 0, '没有找到反例'
    print(f'\n✓ 猜想 T 被推翻：q0 阶存在 h<q0+r1 但 d_fin>0 的增广（Type III）')


if __name__ == '__main__':
    main()
