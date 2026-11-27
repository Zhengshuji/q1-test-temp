r"""命题 2 的阈值 $m\ge r+t+1$ 与 $r$ 的关系：$r\le p-1$。

**推导**（纸面）：
$m=h-s$、$t=v-s$、$r=w-q-s$，故
$$m\ge r+t+1\iff h\ge w-q+v-s+1\iff q\ge w-h+v-s+1 .$$
于是
$$r=w-q-s\le w-(w-h+v-s+1)-s=h-v-1 .$$
又 $h=n-p-r_{L_0}$、$v\ge n-2p$（因 $\operatorname{rank}[C;CA]\le 2p$），故
$$r\le h-v-1\le (n-p-r_{L_0})-(n-2p)-1=p-r_{L_0}-1\le p-1 .$$

$$\boxed{\ \text{只要命题 2 的阈值成立，就有 } r\le p-1\ }$$

**推论**：$p=2$ 时命题 2 **只**能覆盖 $r\le1$——这与 campaign 中"$r\ge2$ 没有谱正例"一致，
说明那个空白**不是**采样的偶然，而是**结构性的**。

本脚本在全随机实例上核对这个不等式。

用法：python proof/layer_program/c281_r2_positive.py
"""
import os
import random
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))

import audit_independent as AI


def analyze(n, p, rL0, A):
    C = [[Fr(1) if k == i else Fr(0) for k in range(n)] for i in range(p)]
    L0 = [[Fr(1) if k == p + i else Fr(0) for k in range(n)] for i in range(rL0)]
    CA = AI.mul(C, A)
    V = AI.nullspace([row[:] for row in (C + CA)])
    H = AI.nullspace([row[:] for row in (C + L0)])
    W = AI.nullspace([row[:] for row in C])
    return len(V), len(H), len(W)


def main():
    rng = random.Random(2026)
    checked = 0
    violations = 0
    threshold_cases = 0
    for _ in range(60):
        n = rng.choice([7, 8, 9])
        p = rng.choice([1, 2])
        rL0 = 1
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        v, h, w = analyze(n, p, rL0, A)
        s = 1
        for q in range(1, w):
            d = w - q
            r = d - s
            t = v - s
            m = h - s
            if r < 0:
                continue
            checked += 1
            if m >= r + t + 1:
                threshold_cases += 1
                if r > p - 1:
                    violations += 1
                    print(f"违反！n={n} p={p} v={v} h={h} w={w} s={s} q={q} r={r} t={t} m={m}")
    print(f"检查 {checked} 个 (实例,q,s) 组合；阈值成立的有 {threshold_cases} 个；")
    print(f"其中违反 r ≤ p−1 的：**{violations}** 个")
    print("\n结论：", "不等式 r ≤ p−1 在阈值成立时全部满足 ✓" if violations == 0 else "存在反例，需重新推导")


if __name__ == '__main__':
    main()
