"""verify.py —— 可观性链引理的精确验证

(1) $(5b)$ 对每个 $k$ 成立：rank Q_{L_k}(λ) = rank H_k 对样本 λ 全过；
(2) $(5a)$ 成立 ⟺ rank H_k = rank H_{k-1}（链闭合）。
另给 $n=3$ 的反例：$k=2$ 时 $(5a)$ 失败。

验证不是证明；证明见 README.md。
"""
import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import linalg_q as LQ                     # noqa: E402
from find_layer_instance import make_instance  # noqa: E402

F = Fraction
LAMS = [F(k) for k in range(-4, 5)] + [F(1, 2), F(-1, 2), F(2, 3)]


def chain(C, A, k):
    rows = []
    cur = [row[:] for row in C]
    for _ in range(k):
        rows += cur
        cur = LQ.mul(cur, A)
    return rows


def main():
    bad5b = bad_chain = 0
    tested = 0
    for seed in (1000, 1002, 1007, 1015):
        A, C, L0 = make_instance(6, seed)
        for k in range(1, 7):
            L = chain(C, A, k)
            H = chain(C, A, k + 1)
            h = LQ.rank(H)
            P0, P1, _ = __import__('observer_pencils').pencil_from_L(A, C, L)
            for lam in LAMS:
                M = [[lam * P1[i][j] + P0[i][j] for j in range(len(P1[0]))] for i in range(len(P1))]
                if LQ.rank(M) != h:
                    bad5b += 1
                    print(f'  (5b) 失败 seed={seed} k={k} λ={lam}')
                    break
            tested += 1
            # (5a) ⟺ 闭合
            cond5a = LQ.condA(A, C, L)
            # k=1 时 (5a) 恒真；k>=2 时 (5a) <=> 链闭合
            closed = (k == 1) or (LQ.rank(H) == LQ.rank(chain(C, A, k)))
            if cond5a != closed:
                bad_chain += 1
                print(f'  (5a)⟺闭合 失败 seed={seed} k={k}: 5a={cond5a} closed={closed}')
    print(f'检验 {tested} 个 (实例,k)；(5b) 失败 {bad5b}，"(5a)⟺闭合" 失败 {bad_chain}')

    # n=3 反例
    A = [[F(0), F(1), F(0)], [F(0), F(0), F(1)], [F(0), F(0), F(0)]]
    C = [[F(1), F(0), F(0)]]
    L = chain(C, A, 2)          # [C; CA]
    print(f'n=3 反例：k=2 时 (5a) = {LQ.condA(A, C, L)}（应为 False），'
          f'rank H_2={LQ.rank(chain(C, A, 2))} vs rank H_1={LQ.rank(chain(C, A, 1))}')
    assert LQ.condA(A, C, L) is False
    assert bad5b == 0 and bad_chain == 0
    print('✓ 通过')


if __name__ == '__main__':
    main()
