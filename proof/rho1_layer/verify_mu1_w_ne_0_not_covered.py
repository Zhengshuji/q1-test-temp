r"""μ=1、$w\ne0$ 的真实实例（**不被覆盖**）：格子里真的搜得到 $(5b)$。

这是 C.2 的另一半（2026-10-30 补）：之前只有"被覆盖"方向的真实实例
（[verify_mu1_w_ne_0_instance.py](verify_mu1_w_ne_0_instance.py)），"不被覆盖"方向一直缺 ✗。

实例（写死）：$n=6$、
$$A=\begin{pmatrix}0&0&1&-1&0&0\\-1&2&2&-1&2&-1\\0&-1&1&1&2&-1\\0&0&0&0&0&1\\0&0&0&0&0&0\\1&0&0&-1&2&0\end{pmatrix},\quad
C=\begin{pmatrix}0&0&0&1&0&0\\0&0&0&0&1&0\end{pmatrix},\quad L_0=e_1 .$$
于是 $\mathcal J=\langle e_4,e_5,e_6\rangle$、$d=3$、$\rho=3$（$U=X$）、$B=\langle\pi(e_1)\rangle$、$\mu=1$、
$H=\mathcal V\cap\mathcal J=\langle e_6\rangle$、$w=\beta(e_6)\ne0$、$T=\begin{pmatrix}0&0&1\\-1&2&2\\0&-1&1\end{pmatrix}$。

验三件事：
  (1) 判据（C.2）：$[\lambda I-T;w]$ 的子式 $\gcd$ 是**常数** ⟹ 不被覆盖 ✓；
  (2) 找到一个**具体提升** $\mathcal L$，其商铅笔 $\lambda\pi(\mathcal L)-\pi(\mathcal LA)$ 对所有 $\lambda$ 满秩 $\rho$ ⟹ $(5b)$ 成立 ✓；
  (3) 该 $\mathcal L$ 满足 $(5a)$、类型 $(3,1)$、$\operatorname{row}(L_0)\subseteq\operatorname{row}\mathcal L$ ✓。

用法：python proof/rho1_layer/verify_mu1_w_ne_0_not_covered.py
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, _HERE)

import audit_independent as AI
import verify_mu1_w_ne_0_instance as LIB     # 复用 det / 插值 / 子式 gcd

mul, rank, vstack, row_basis, nullspace = AI.mul, AI.rank, AI.vstack, AI.row_basis, AI.nullspace

N = 6
A_MAT = [[0, 0, 1, -1, 0, 0],
         [-1, 2, 2, -1, 2, -1],
         [0, -1, 1, 1, 2, -1],
         [0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0],
         [1, 0, 0, -1, 2, 0]]
C_MAT = [[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0]]
L0_MAT = [[1, 0, 0, 0, 0, 0]]


def build():
    return ([[Fr(x) for x in r] for r in A_MAT],
            [[Fr(x) for x in r] for r in C_MAT],
            [[Fr(x) for x in r] for r in L0_MAT])


def cell_data(A, C):
    D = LIB.cell_data(A, C)          # 与上一脚本同一套计算（j、B、μ、a、h、w、T、π）
    return D


def main():
    A, C, L0 = build()
    D = cell_data(A, C)
    print(f"j={D['j']}、d={D['d']}、μ={D['mu']}、a={[str(x) for x in D['a']]}")
    print(f"h={[str(x) for x in D['h']]}、w=β(h)={[str(x) for x in D['w']]}")
    print(f"T={[[str(x) for x in r] for r in D['T']]}")
    assert D['mu'] == 1 and any(D['w']), '要 μ=1 且 w≠0'

    # (1) 判据：不被覆盖 ⟺ gcd 是常数
    def cell_pencil(lam):
        R = [[(lam if i == k else Fr(0)) - D['T'][i][k] for k in range(3)] for i in range(3)]
        R.append([Fr(x) for x in D['w']])
        return R
    deg = LIB.minors_gcd_degree(cell_pencil, 4, 3)
    print(f"(1) 判据：gcd 次数 = {deg}（=0 ⟹ 不被覆盖）{'✓' if deg == 0 else '✗'}")
    assert deg == 0

    # (2) 找见证提升：L = [e1; e2+s1 h; e3+s2 h; h]，要求商铅笔对所有 λ 满秩 ρ=3
    e = [[Fr(1) if t == i else Fr(0) for t in range(N)] for i in range(N)]
    h = D['h']
    pi = D['pi']
    CA = mul(C, A)
    best = None
    for s1 in range(-2, 3):
        for s2 in range(-2, 3):
            L = [e[0],
                 [e[1][k] + Fr(s1) * h[k] for k in range(N)],
                 [e[2][k] + Fr(s2) * h[k] for k in range(N)],
                 h]
            PL = [pi(r) for r in L]
            PLA = [pi(mul([r], A)[0]) for r in L]

            def q_pencil(lam, PL=PL, PLA=PLA):
                return [[lam * PL[i][k] - PLA[i][k] for k in range(3)] for i in range(4)]
            if LIB.minors_gcd_degree(q_pencil, 4, 3) == 0:
                score = abs(s1) + abs(s2)
                if best is None or score < best[0]:
                    best = (score, s1, s2, L)
    assert best is not None, '没找到见证（判据说不被覆盖，应存在）'
    score, s1, s2, L = best
    print(f"(2) 见证提升：(s1,s2)=({s1},{s2}) 的商铅笔子式 gcd 次数 = 0 ⟹ (5b) 成立 ✓")

    # (3) 该 L 的其它条件
    print(f"    rank L = {rank(L)}（应 4）、row(L0)⊆row(L): "
          f"{AI.in_span(L0[0], L)}、dim(row L + J) = {rank(L + D['J'])}（应 6）")
    assert rank(L) == 4
    assert AI.in_span(L0[0], L)
    assert rank(L + D['J']) == 6           # ⟹ ρ=3、c=1（类型 (3,1)）
    # (5a)：π(VA) ⊆ π(V)
    V = L
    VA = mul(V, A)
    ok5a = rank([[pi(VA[i])[k] for k in range(3)] for i in range(4)] + D['U']) == rank(D['U'])
    print(f"    (5a)：π(VA) ⊆ π(V) = X ✓" if ok5a else "    (5a) 失败 ✗")
    assert ok5a

    print('\n=> μ=1、w≠0、**不被覆盖**的真实实例：格子里确实有满足 (5a)∧(5b) 的 L ✓')


if __name__ == '__main__':
    main()
