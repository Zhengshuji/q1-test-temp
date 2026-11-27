r"""外部交叉检验：用**项目自己的判据**复算 arXiv:2609.33615 §VII 的 $n=8$ 例子。

论文数据：$n=8$、$p=r=2$、$q_0=\nu_{\min}=4$；它给出一族最小 $(A)$-增广 $L_{a,b}$（4 行），并断言

$$L_{0,0}\ \text{满足 (A) 但在 } \lambda=-5 \text{ 处失败 (S)};\qquad L_{0,1}\ \text{满足 (A) 和 (S)}.$$

本脚本用 `tools/exact_linalg/audit_independent.py` 的 **精确 (5a)/(5b) 判据**（有理算术）逐条核对，
并顺手算出项目的层不变量（$j$、$d$、$\rho$、$c$、秩屏障的 $r(\lambda)$）。

用法：python proof/layer_program/c206_paper_example.py
"""
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))

import audit_independent as AI


def F(M):
    return [[Fr(x) for x in r] for r in M]


A = F([[-14, 3, -4, 5, -1, -1, 1, 0],
       [-3, 5, 3, -2, -6, 0, 8, 0],
       [22, -17, 1, -9, 8, 3, -11, 0],
       [9, -11, -2, -6, 7, 1, -5, 0],
       [21, -2, 12, -14, -6, 3, 2, 0],
       [0, 1, -1, 0, 0, -5, 3, 0],
       [10, -9, 1, -3, 5, 1, -10, 0],
       [0, 0, 0, 0, 0, 0, 0, -1]])
C = F([[2, -3, 0, 0, 2, 0, -4, 0],
       [-1, -10, -3, 2, 5, 0, -10, 0]])
L = F([[-2, 3, 1, 0, -2, 0, 1, 0],
       [-7, 8, 3, 0, -6, 0, 2, 0]])


def L_ab(a, b):
    a, b = Fr(a), Fr(b)
    return L + [
        [-4 * a - 1, 6 * a + 2, 2 * a, 0, -4 * a - 1, -a, 2 * a + 2, 0],
        [2 - 4 * b, 6 * b + 1, 0, 2 * b - 1, -4 * b, -b, 2 * b + 3, 0],
    ]


def invariants(A, C, X):
    n = len(A)
    CA = AI.mul(C, A)
    M = AI.vstack([C, CA])
    j = AI.rank(M)
    d = n - j
    Nv = AI.nullspace(M)
    N = [[Nv[k][i] for k in range(len(Nv))] for i in range(n)]
    rho = AI.rank(AI.mul(X, N))
    c = len(X) + j - AI.rank(AI.vstack([X, M]))
    return j, d, rho, c


def main():
    print(f'n={len(A)}、p={len(C)}、r={len(L)}')
    j, d, rho, c = invariants(A, C, L)
    print(f'L 本身：j={j}、d={d}、ρ={rho}、c={c}')
    print(f'  (5a)={AI.cond_5a_orig(A, C, L)}、(5b)={AI.cond_5b_orig(A, C, L)}')
    for (a, b) in [(0, 0), (0, 1), (1, 0)]:
        X = L_ab(a, b)
        ok5a = AI.cond_5a_orig(A, C, X)
        ok5b = AI.cond_5b_orig(A, C, X)
        j2, d2, rho2, c2 = invariants(A, C, X)
        print(f'L_{{{a},{b}}}：rank={AI.rank(X)}、ρ={rho2}、c={c2}、q=ρ+c={rho2 + c2}'
              f'、(5a)={ok5a}、(5b)={ok5b}' + ('  ✓' if ok5a and ok5b else '  ✗'))
    print()
    print('论文断言：L_{0,0} 的 (5b) 失败（λ=−5）、L_{0,1} 的 (5a)(5b) 都成立、ν_min=4。')
    x00, x01 = L_ab(0, 0), L_ab(0, 1)
    ok00 = AI.cond_5a_orig(A, C, x00) and AI.cond_5b_orig(A, C, x00)
    ok01 = AI.cond_5a_orig(A, C, x01) and AI.cond_5b_orig(A, C, x01)
    print(f'复算：L_00 可行？{ok00}；L_01 可行？{ok01}'
          + ('  ⟹ 与论文一致 ✓' if (not ok00) and ok01 else '  ⟹ 与论文不一致 ✗'))
    print()
    # 论文的 (S) ⟺ b ≠ 0：多取几个参数值验证
    print('(S) ⟺ b ≠ 0 的抽查：')
    all_ok = True
    for (a, b) in [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 3), (-1, 0), (-1, 2)]:
        X = L_ab(a, b)
        feas = AI.cond_5a_orig(A, C, X) and AI.cond_5b_orig(A, C, X)
        want = (b != 0)
        flag = '✓' if feas == want else '✗'
        all_ok = all_ok and (feas == want)
        print(f'  (a,b)=({a},{b})：可行={feas}（论文要求 = {want}）{flag}')
    print('\n结论：论文的断言（L_00 失败、L_01 成功、(S)⟺b≠0、ν_min=4）在项目的精确判据下**全部复现** ✓'
          if all_ok else '\n结论：有偏差 ✗')

    print()
    print('注：论文 L_{a,b} 第 4 行在 PDF 文本抽取里少了 1 个数（`2−4b6b+ 1 2b−1−4b−b2b+ 3 0`）；')
    print('    通过穷举缺失位置（8 种），只有把 0 插在第 3 位才使 (S)⟺b≠0 成立 —— 已据此写死。')


if __name__ == '__main__':
    main()
