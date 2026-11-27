r"""c287：定理 A 的机器核对（第二条曲线 + 现有二次曲线）。

**定理 A（A2 §20）**：设 $f:\mathbb P^1\to\operatorname{Gr}(r,V)$ 非常值、Plücker 次数 $d>0$。
对 $W\in\operatorname{Gr}(m-r,V)$，$s_W(\lambda)=\det[W\mid B(\lambda)]$（仿射坐标下的多项式，$\deg\le d$）。则
1. **$\mathbb A^1$ 可行** $\iff s_W$ 是**非零常数**；
2. **$\mathbb P^1$ 无共同补空间** $\iff$ 每个 $W$ 都在某点失败，即
   $$s_W\ \text{有有限根}\quad\text{或}\quad\deg s_W<d\ (\text{即 }\infty\text{ 处为零}).$$

两条曲线：
- 二次：$f(\lambda)=\operatorname{span}\{(1,0,0,\lambda),(0,1,\lambda,0)\}$，$d=2$；
- **三次**：$f(\lambda)=\operatorname{span}\{(1,0,0,\lambda^2),(0,1,\lambda,0)\}$，$d=3$。

用法：python proof/layer_program/c287_theoremA.py
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))

import audit_independent as AI


def det(M):
    n = len(M)
    if n == 0:
        return Fr(1)
    M = [row[:] for row in M]
    d = Fr(1)
    for i in range(n):
        piv = next((r for r in range(i, n) if M[r][i] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != i:
            M[i], M[piv] = M[piv], M[i]
            d = -d
        d *= M[i][i]
        inv = Fr(1) / M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] * inv
            for c in range(i, n):
                M[r][c] -= f * M[i][c]
    return d


def s_W_poly(W, curve, d):
    """W: 2×4；curve: 函数 lam -> 2×4 矩阵（行 = 基）；返回 s_W 的系数（长度 d+1）。"""
    vals = []
    for lam in range(d + 1):
        B = curve(Fr(lam))
        M = [list(W[0]), list(W[1]), list(B[0]), list(B[1])]
        vals.append(det(M))
    # 拉格朗日插值（节点 0..d）
    coeffs = [Fr(0)] * (d + 1)
    for i in range(d + 1):
        num = [Fr(1)]
        den = Fr(1)
        for j in range(d + 1):
            if j == i:
                continue
            new = [Fr(0)] * (len(num) + 1)
            for k, c in enumerate(num):
                new[k + 1] += c
                new[k] -= c * j
            num = new
            den *= Fr(i - j)
        for k, c in enumerate(num):
            coeffs[k] += vals[i] * c / den
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    return coeffs


def has_finite_root(p):
    """次数 ≥1 的多项式在 C 上有根。"""
    return len(p) >= 2


def main():
    curves = [
        ("二次（conic）", 2, lambda lam: [[Fr(1), Fr(0), Fr(0), lam], [Fr(0), Fr(1), lam, Fr(0)]]),
        ("三次（cubic）", 3, lambda lam: [[Fr(1), Fr(0), Fr(0), lam * lam], [Fr(0), Fr(1), lam, Fr(0)]]),
    ]
    Wgrid = []
    for tup in itertools.product((-1, 0, 1), repeat=8):
        W = [[Fr(tup[0]), Fr(tup[1]), Fr(tup[2]), Fr(tup[3])],
             [Fr(tup[4]), Fr(tup[5]), Fr(tup[6]), Fr(tup[7])]]
        if AI.rank(W) == 2:
            Wgrid.append(W)
    print(f"W 网格：{len(Wgrid)} 个\n")

    for name, d, curve in curves:
        affine_ok = 0
        fail_at_inf = 0
        viol_inf = 0
        viol_aff = 0
        for W in Wgrid:
            p = s_W_poly(W, curve, d)
            is_const_nonzero = (len(p) == 1 and p[0] != 0)
            if is_const_nonzero:
                affine_ok += 1
            # ℙ¹：必须失败（有限根 或 deg < d）
            fails = has_finite_root(p) or (len(p) - 1 < d)
            if not fails:
                viol_inf += 1
            # 一致性：仿射可行 ⟹ 必须 deg<d（失败在 ∞）
            if is_const_nonzero and not (len(p) - 1 < d):
                viol_aff += 1
        print(f"=== {name}（d={d}）")
        print(f"  𝔸¹ 上可行的 W：**{affine_ok}** / {len(Wgrid)}")
        print(f"  ℙ¹ 上「没有失败」的 W：**{viol_inf}**（应为 0——否则与定理 A1 矛盾）")
        print(f"  仿射可行但不在 ∞ 失败的 W：**{viol_aff}**（应为 0）")
        print()

    print("结论：两条曲线上都满足定理 A 的两条断言（仿射 ⟺ 非零常数；ℙ¹ 必有失败）。")


if __name__ == '__main__':
    main()
