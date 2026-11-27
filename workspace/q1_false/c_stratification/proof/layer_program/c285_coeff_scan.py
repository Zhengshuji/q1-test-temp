r"""c285：系数空间扫描（QA22 §4.3）——把定理 B 的判据与**直接枚举**逐例对照。

**检验的命题**（A2 §25，定理 B）：
$$\text{谱可行}\iff\operatorname{Gr}\cap\mathbb P(K)\not\subseteq\mathbb P(\ker a_0),\qquad K=\bigcap_{j\ge1}\ker a_j,$$
其中 $q_U(\lambda)=\det[U\mid B(\lambda)]=\sum_j\langle a_j,p_U\rangle\lambda^j$。

**做法**：给定 $B(\lambda)$（$I_\lambda$ 的多项式基），用 `coeff_space` 算 $a_j$、$K$，再按
$r=1$（线性代数）或 $(r,m)=(2,4)$（二次型）判可行；**与直接枚举的结果对照**。

三个实例：
- A：`c282` 的实例（$r=1,m=4$）——直接枚举给出 4/624 可行；
- B：二次曲线（$r=2,m=4$）——`c284` 给出 73 个可行 $W$；
- C：**负例** $r=1,m=3$，$I_\lambda=v(\lambda)^\perp$，$v=(1,\lambda,\lambda^2)$——每个 $u$ 都有根，**不可行**。

用法：python proof/layer_program/c285_coeff_scan.py
"""
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import coeff_space as CS


def report(name, Bpolys, m, r, direct, feasible_fn):
    a, idxs = CS.coeff_forms(Bpolys, m, r)
    info = CS.linear_data(a)
    res = feasible_fn(a, m) if r == 1 else feasible_fn(a)
    print(f"\n=== {name}（m={m}, r={r}）")
    print(f"  Plücker 空间维数 C(m,r) = {info['dimPlucker']}，多项式次数 d = {info['d']}")
    print(f"  rank{{a_j}}_{{j>=1}} = {info['rank_ge1']}，dim K = {info['dimK']}，a_0 ≠ 0? {info['rank_a0'] == 1}")
    print(f"  系数判据：可行 = {res['feasible']}" + (f"（dimK={res.get('dimK')}）" if 'dimK' in res else ''))
    print(f"  直接枚举：可行 = {direct}")
    geo = (CS.geometry_r1(a, m) if r == 1 else CS.geometry_24(a))
    print(f"  dim X = {geo['dimX']}，dim F = {geo['dimF']}，分量数 = {geo.get('components')}（{geo['note']}）")
    ok = (res['feasible'] == direct)
    print(f"  ⟹ {'一致 ✓' if ok else '*** 不一致 ***'}")
    return ok


def main():
    allok = True

    # A：c282 的实例，H/S 基 (e4,e6,e7,e8)，I_lam = span(e4-lam e6, e6-lam e7, e7-lam e8)
    B0 = [[Fr(1), Fr(0), Fr(0)],
          [Fr(0), Fr(1), Fr(0)],
          [Fr(0), Fr(0), Fr(1)],
          [Fr(0), Fr(0), Fr(0)]]
    B1 = [[Fr(0), Fr(0), Fr(0)],
          [Fr(-1), Fr(0), Fr(0)],
          [Fr(0), Fr(-1), Fr(0)],
          [Fr(0), Fr(0), Fr(-1)]]
    allok &= report("A: c282 实例", [B0, B1], 4, 1, True, CS.feasible_r1)

    # B：二次曲线 f(lam) = span{(1,0,0,lam),(0,1,lam,0)} ⊂ Gr(2,4)
    B0 = [[Fr(1), Fr(0)],
          [Fr(0), Fr(1)],
          [Fr(0), Fr(0)],
          [Fr(0), Fr(0)]]
    B1 = [[Fr(0), Fr(0)],
          [Fr(0), Fr(0)],
          [Fr(0), Fr(1)],
          [Fr(1), Fr(0)]]
    allok &= report("B: 二次曲线", [B0, B1], 4, 2, True, CS.feasible_24)

    # C：真正的负例 r=1,m=3：v(lam) = (1+lam^2, 1+lam, -(1+lam^2))
    #    （a_0 = a_1 + a_2，且 a_lam 无公根 ⟹ 常数维；每个 u 都有根 ⟹ 不可行）
    #    v^perp 的基：b1 = (-v2, v1, 0), b2 = (0, -v3, v2)
    #    b1 = (-(1+lam), 1+lam^2, 0) = (-1,1,0) + lam(-1,0,0) + lam^2(0,1,0)
    #    b2 = (0, 1+lam^2, 1+lam) = (0,1,1) + lam(0,0,1) + lam^2(0,1,0)
    B0 = [[Fr(-1), Fr(0)],
          [Fr(1), Fr(1)],
          [Fr(0), Fr(1)]]
    B1 = [[Fr(-1), Fr(0)],
          [Fr(0), Fr(0)],
          [Fr(0), Fr(1)]]
    B2 = [[Fr(0), Fr(0)],
          [Fr(1), Fr(1)],
          [Fr(0), Fr(0)]]
    allok &= report("C: 负例 v^perp（无公根）", [B0, B1, B2], 3, 1, False, CS.feasible_r1)

    print("\n总结果：", "全部一致 ✓" if allok else "*** 存在不一致 ***")


if __name__ == '__main__':
    main()
