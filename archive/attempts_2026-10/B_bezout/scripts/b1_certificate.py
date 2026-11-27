r"""B-1：Bézout 证书 + 统一**次数界**（分支 2）。

**检验的命题**（A2 §27 的 gcd 判据 + Bézout 对偶）：
$$\gcd(f_1,\dots,f_N)\in\mathbb C^\times\iff\exists g_i:\ \sum_i g_i f_i=1,$$
其中 $f_i$ 是 $[U\mid P(\lambda)]$ 的 $(r+t)$ 阶极大子式。

**本脚本**（c282 实例，$r=1$）：
1. 取**一般位置**的 $U$（不是坐标方向）⟹ $N>1$，证书非平凡；
2. 算证书并**精确验证** $\sum g_i f_i=1$；
3. 与直接判据 `feasible_by_minors`（同一条 gcd 判据的另一实现）对照；
4. 记录实测 $\deg g_i$ 与保守界 $(N-1)\cdot\max\deg f_i$。

**注**：$U$ 必须落在 $H/S$ 里（$A$ 的可容许性），且 $U\cap G=S$。

用法：python workspace/B_bezout/scripts/b1_certificate.py
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import coeff_of_S as CS_
import bezout_cert as BC
import spectral_gcd as SG


def c282():
    N = 8
    def unit(i):
        return [Fr(1) if k == i else Fr(0) for k in range(N)]
    C = [unit(0), unit(1)]
    L0 = [unit(2)]
    A = [[Fr(0)] * N for _ in range(N)]
    for (i, j) in [(0, 2), (1, 3), (4, 4), (3, 5), (5, 6), (6, 7)]:
        A[i][j] = Fr(1)
    return A, C, L0, [unit(4)]


def main():
    A, C, L0, S = c282()
    st = CS_.setup(A, C, L0, 4, S)
    cols = CS_.pencil_cols(A, st)
    wm = st['w'] - st['s']
    m = st['m']
    r = st['d'] - st['s']
    t = len(cols)
    print(f"c282：W/S 维数={wm}，H/S 维数={m}，r={r}，t={t}，N=C({wm},{r+t})={len(list(itertools.combinations(range(wm), r+t)))}")
    print(f"{'U（H/S 坐标）':<26}{'N':<4}{'D':<4}{'deg g':<7}{'unit?':<7}{'cert':<6}{'deg gs':<8}{'bound':<7}{'与直接判据一致?':<10}")
    mism = 0
    nontrivial = 0
    checked = 0
    cases = []
    # 一般位置：HS 基向量的组合（坐标化后仍要落在 H/S，这里直接在 W/S 坐标里构造）
    HS = st['HS']
    combos = [(1, 1, 0, 0), (1, 0, 1, 0), (0, 1, 1, 0), (1, 1, 1, 0), (1, 2, 3, 0)]
    for cs in combos:
        u = [sum(Fr(cs[i]) * HS[i][k] for i in range(m)) for k in range(wm)]
        cases.append((cs, u))
    for cs, u in cases:
        info = BC.analyse([u], cols, wm, r)
        # 与 feasible_by_minors 对照（用 n 维向量）
        unw = [sum(u[j] * st['WB'][st['s'] + j][k] for j in range(wm)) for k in range(st['n'])]
        direct, _g = CS_.feasible_by_minors(A, C, L0, 4, S, [unw])
        same = (direct == info['is_unit'])
        if not same:
            mism += 1
        checked += 1
        if info['N'] > 1:
            nontrivial += 1
        print(f"{str(cs):<26}{info['N']:<4}{info['D']:<4}{info['deg_g']:<7}{str(info['is_unit']):<7}"
              f"{str(info['cert_ok']):<6}{info['cert_degree']:<8}{info['bound']:<7}{'✓' if same else '✗'}")
    print(f"\n检查 {checked} 个 U；与直接判据不一致 **{mism}**；N>1 的实例 **{nontrivial}**")
    print("（N=1 时 Bézout 证书退化为单个多项式，不是真正的 Bézout 证书。）")


if __name__ == '__main__':
    main()
