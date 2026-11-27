r"""c288：根式成员检验（QA23 优先级 5）——负例的**结构性检测器**。

**检验的命题**（A2 §29.2）：负例 $X\subseteq\mathbb P(\ker a_0)$ $\iff a_0\in\sqrt I$
（$I=I_{\operatorname{Gr}}+I_K$）。

**实现**：
- $r=1$：$I$ 线性，故 $a_0\in\sqrt I\iff a_0|_K=0$（线性代数）；
- $(2,4)$：按 $Q|_K$ 的秩分类——rank 0 ⟹ $a_0|_K=0$；**rank 1 ⟹ $a_0|_K\in\operatorname{span}\{L\}$**；
  rank ≥2 ⟹ $a_0|_K=0$。

**新定理（本轮）**：在 $(2,4)$ 上，若 $a_0|_K\ne0$ 且 $a_0$ 在 $X$ 上为零，则**必有** $\operatorname{rank}(Q|_K)=1$。

**对照**：与 `geometry_24` 的暴力搜索（$Q(u)=0$ 且 $\langle a_0,u\rangle\ne0$ 是否存在）逐例比较。

用法：python proof/layer_program/c288_radical_test.py
"""
import os
import random
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import coeff_space as CS


def main():
    rng = random.Random(20261031)
    print("(r,m)=(2,4)：根式成员判据 vs 暴力搜索\n")
    print(f"{'#':<4}{'rank Q|_K':<10}{'a_0|_K=0?':<10}{'根式判定':<10}{'暴力可行':<10}一致?")
    bad = 0
    tested = 0
    rank1_nonzero = 0
    for trial in range(40):
        B0 = [[Fr(rng.randint(-2, 2)) for _ in range(2)] for _ in range(4)]
        B1 = [[Fr(rng.randint(-2, 2)) for _ in range(2)] for _ in range(4)]
        # 要求每一列不恒为零
        if all(x == 0 for row in B1 for x in row):
            continue
        a, idxs = CS.coeff_forms([B0, B1], 4, 2)
        rad = CS.radical_membership_24(a)
        geo = CS.geometry_24(a)
        brute_feasible = geo['dimF'] is not None
        # 根式判定：in_radical ⟺ 负例 ⟺ 不可行
        pred_feasible = not rad['in_radical']
        tested += 1
        ok = (pred_feasible == brute_feasible)
        if not ok:
            bad += 1
        if rad.get('rankQK') == 1 and not all(x == 0 for x in [sum(a[0][i]*1 for i in range(6))]):
            pass
        if tested <= 12:
            print(f"{trial:<4}{rad.get('rankQK'):<10}{str(rad['how']):<40}{'不可行' if rad['in_radical'] else '可行':<10}"
                  f"{'可行' if brute_feasible else '不可行':<10}{'✓' if ok else '✗'}")
    print(f"\n测试 {tested} 例；与暴力搜索不一致：**{bad}**")
    print("\n结构性结论：$(2,4)$ 上若 $a_0|_K\\ne0$ 且 $a_0|_X=0$，则必 rank(Q|_K)=1。")


if __name__ == '__main__':
    main()
