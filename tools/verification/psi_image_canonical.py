"""psi_image_canonical.py —— B.18d：标准（循环）坐标下 $\\operatorname{im}\\psi$ 的精确刻画

**设定**：$p=r=1$、$(c,A)$ 可观测，取循环基使 $c=e_1^{\\mathsf T}$、$cA=e_2^{\\mathsf T}$、…、$cA^{n-1}=e_n^{\\mathsf T}$。
则 $A$ 呈伴矩阵形式：$A e_1=-a_0e_n$，$A e_j=e_{j-1}-a_{j-1}e_n\\ (j\\ge2)$，而
$$V=\\ker[c;cA]=\\operatorname{span}\\{e_3,\\dots,e_n\\}.$$
对 $x=\\sum_{k\\ge3}x_ke_k$：
$$(\\lambda I-A)x=\\Bigl(0,\\ -x_3,\\ \\lambda x_3-x_4,\\ \\dots,\\ \\lambda x_{n-1}-x_n,\\
\\lambda x_n+\\sum_{k\\ge3}a_{k-1}x_k\\Bigr).$$
故 $w\\in\\ker c$（坐标 $(0,w_2,\\dots,w_n)$）属于 $\\operatorname{im}\\psi$ $\\iff$ 递归
$$x_3=-w_2,\\qquad x_{k+1}=\\lambda x_k-w_k\\ (k=3,\\dots,n-1),$$
代入最后一条得**一个**关于 $\\lambda$ 的多项式方程
$$P(\\lambda):=\\lambda x_n(\\lambda)+\\sum_{k\\ge3}a_{k-1}x_k(\\lambda)-w_n=0 .$$
于是（$w\\ne0$ 时）
$$w\\in\\operatorname{im}\\psi\\iff w_2\\ne0\\ \\text{且}\\ P\\ \\text{不是非零常数}.$$

本脚本：用**精确 gcd 判据**（增广铅笔极大子式）核验上述刻画。

用法：python -u tools/verification/psi_image_canonical.py
"""

import os
import sys
import itertools
import random
from fractions import Fraction
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import sympy as sp                        # noqa: E402
import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import membership_test as MT              # noqa: E402

F = Fraction
lam = sp.symbols('lam')


def companion(coeffs, n):
    """伴矩阵：A e_1 = -a_0 e_n, A e_j = e_{j-1} - a_{j-1} e_n。"""
    A = [[F(0)] * n for _ in range(n)]
    for j in range(2, n + 1):
        A[j - 2][j - 1] = F(1)          # e_{j-1} 系数
    for j in range(1, n + 1):
        A[n - 1][j - 1] = -coeffs[j - 1]
    return A


def formula_member(w, coeffs, n):
    """B.18d 的判据：w_2 ≠ 0 且 P(λ) 不是非零常数。"""
    if all(x == 0 for x in w):
        return True
    # 递归 x_k(λ)（注意 w_2 = 0 只给 x_3 = 0，**不**使其余 x_k 为零）
    xs = {3: -w[1]}
    for k in range(3, n):
        xs[k + 1] = sp.expand(lam * xs[k] - sp.Rational(w[k - 1].numerator, w[k - 1].denominator))
    # P(λ) = λ x_n + Σ_{k≥3} a_{k-1} x_k − w_n
    P = lam * xs[n] + sum(sp.Rational(coeffs[k - 1].numerator, coeffs[k - 1].denominator) * xs[k]
                          for k in range(3, n + 1)) - sp.Rational(w[n - 1].numerator, w[n - 1].denominator)
    P = sp.expand(P)
    if P == 0:
        return True
    return sp.degree(P, lam) >= 1


def main():
    rng = random.Random(20261105)
    st = Counter()
    for n in (4, 5, 6):
        for trial in range(25):
            coeffs = [F(rng.randrange(-2, 3)) for _ in range(n)]
            A = companion(coeffs, n)
            C = [[F(1)] + [F(0)] * (n - 1)]
            O = QR.observability_matrix(A, C)
            if LQ.rank(O) != n:
                continue
            for _ in range(4):
                # 随机 w ∈ ker c（即 w_1 = 0）
                w = [F(0)] + [F(rng.randrange(-3, 4)) for _ in range(n - 1)]
                if all(x == 0 for x in w):
                    continue
                member, deg = MT.in_im_psi(A, C, w)
                pred = formula_member(w, coeffs, n)
                st['样本'] += 1
                if member == pred:
                    st['一致'] += 1
                else:
                    st['不一致'] += 1
                    if st['不一致'] <= 5:
                        print(f'  不一致 n={n}：gcd 判据={member}（deg {deg}），公式={pred}，w={[str(x) for x in w]}')
    print('统计：', dict(st))
    print('  一致 = B.18d 的公式刻画 == 精确 gcd 判据')


if __name__ == '__main__':
    main()
