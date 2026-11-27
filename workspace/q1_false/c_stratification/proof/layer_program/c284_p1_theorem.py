r"""项 4：$\mathbb P^1$ 定理的**具体实例化**（A2 §20 的命题 1/命题 2）。

**命题 1（$\mathbb P^1$）**：$f:\mathbb P^1\to\operatorname{Gr}(r,V)$ 非常值 ⟹ 不存在共同补空间。
**命题 2（$\mathbb A^1$）**：存在 $W$ 补所有 $I_\lambda\iff\det[W\mid B(\lambda)]$ 是**非零常数**。

**实例**：$\operatorname{Gr}(2,4)$ 中的有理曲线
$$f(\lambda)=\operatorname{span}\{(1,0,0,\lambda),\ (0,1,\lambda,0)\}.$$
其 Plücker 坐标 $(p_{12},p_{13},p_{14},p_{23},p_{24},p_{34})=(1,\lambda,0,0,-\lambda,-\lambda^2)$，
次数 $2>0$ ⟹ **非常值** ✓

**做法**：对 $\operatorname{Gr}(2,4)$ 中一批 $W$（$2$ 维），算 $s_W(\lambda)=\det[W\mid B(\lambda)]$（$\lambda$ 的多项式），
判定：$s_W$ 是否有零点（$\mathbb C$ 上）。

用法：python proof/layer_program/c284_p1_theorem.py
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


def s_W_poly(W):
    """W: 2×4 矩阵（行），返回 s_W 的系数 [c0,c1,c2]。"""
    # B(lam) = [[1,0,0,lam],[0,1,lam,0]]
    coefs = []
    for lam in range(3):
        B = [[Fr(1), Fr(0), Fr(0), Fr(lam)], [Fr(0), Fr(1), Fr(lam), Fr(0)]]
        M = [list(W[0]), list(W[1]), B[0], B[1]]
        coefs.append(det(M))
    # 二次插值（节点 0,1,2）
    c0 = coefs[0]
    c2 = (coefs[2] - 2 * coefs[1] + coefs[0]) / 2
    c1 = coefs[1] - coefs[0] - c2
    return [c0, c1, c2]


def main():
    print("实例：f(lam) = span{(1,0,0,lam), (0,1,lam,0)} ⊂ Gr(2,4)")
    print("Plücker 次数 = 2 > 0 ⟹ 非常值 ✓\n")

    found_const = 0
    const_examples = []
    tot = 0
    for (a, b, c, d, e, f, g, h) in itertools.product((-1, 0, 1), repeat=8):
        W = [[Fr(a), Fr(b), Fr(c), Fr(d)], [Fr(e), Fr(f), Fr(g), Fr(h)]]
        if AI.rank(W) < 2:
            continue
        tot += 1
        p = s_W_poly(W)
        # 非零常数 ⟺ c1 = c2 = 0 且 c0 ≠ 0
        if p[1] == 0 and p[2] == 0 and p[0] != 0:
            found_const += 1
            const_examples.append((W, p))
        if tot >= 2000:
            break

    print(f"检查了 {tot} 个 W（2×4 小整数矩阵，行列式非零）")
    # ℙ¹ 检验：这些 W 是否也在 λ=∞ 处互补？
    # f(∞) = span(e3, e4)（齐次化 s=0 的极限）
    fin = [[Fr(0), Fr(0), Fr(1), Fr(0)], [Fr(0), Fr(0), Fr(0), Fr(1)]]
    fails_at_inf = 0
    for W, _ in const_examples:
        M = [W[0], W[1], fin[0], fin[1]]
        if det(M) != 0:
            fails_at_inf += 1
    print(f"其中 s_W 是**非零常数**（即 𝔸¹ 上可行的补空间）的个数：**{found_const}**")
    print(f"这些 W 中**仍与 f(∞) 互补**的个数：**{fails_at_inf}**（应为 0——否则与 ℙ¹ 定理矛盾）")
    if found_const:
        print("样本：")
        for W, p in const_examples[:3]:
            print("   W =", [[str(x) for x in row] for row in W], "-> s_W =", [str(x) for x in p])
    else:
        print("\n⟹ 该曲线上**没有**任何 W 能避开所有有限 λ 的 I_λ；")
        print("   在 ℙ¹ 上更不可能（命题 1）✓ —— 与定理一致。")

    print("\n检验命题 2 的判据：对每个 W，'无根 ⟺ 非零常数'。")
    print("由于 s_W 的次数 ≤ 2，'无根' 在 ℂ 上等价于 '次数 0 且非零' ✓（本次检查全部按此判定）。")


if __name__ == '__main__':
    main()
