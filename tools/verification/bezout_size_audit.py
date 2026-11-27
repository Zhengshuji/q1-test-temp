r"""Bézout 编码的**规模审计**（专家第六轮 §6.3 的第 2 点）。

对 $m=q+2p$、$n$、法秩 $h$ 计算
  N_minors = C(m,h) * C(n,h)                     # 要枚举的 h×h 子式个数
  vars     = (q-r)*n + (D+1)*N_minors,  D = h    # Bézout 编码的变量数上界
并判断"多项式规模"何时可能：

  C(n,h) = C(n,n-h)，故 N_minors 在 min(h, n-h) 固定时是 n 的多项式；
  当 h ≈ n/2 时由 Stirling 公式为指数级。

输出：p=1 时的表（n=4..10，q 从 1 到 n-1，h=max 取 min(q+2p, n)），以及 p=2 的对照。
"""

import math


def C(a, b):
    if b < 0 or b > a:
        return 0
    return math.comb(a, b)


def count(n, p, q, r, h):
    m = q + 2 * p
    nm = C(m, h) * C(n, h)
    D = h
    vars_ = (q - r) * n + (D + 1) * nm
    return m, h, nm, vars_


def main():
    print('=== p=1, r=1：h 取 min(q+2, n)（生成实例的典型最大法秩） ===')
    print(f'{"n":>3} {"q":>3} {"m":>3} {"h":>3} {"#h-minors":>14} {"Bézout 变量数":>18}')
    worst = []
    for n in range(4, 11):
        for q in range(1, n):
            p, r = 1, 1
            h = min(q + 2 * p, n)
            m, hh, nm, v = count(n, p, q, r, h)
            print(f'{n:>3} {q:>3} {m:>3} {hh:>3} {nm:>14} {v:>18}')
            worst.append((nm, n, q, hh))

    print()
    print('=== 何时是多项式规模？（min(h, n-h, m-h) 有界时） ===')
    for n in (6, 8, 10, 12):
        # 情形 A：h = n-1（余维 1）⟹ C(n,n-1)=n
        nmA = C(n + 2, n - 1) * C(n, n - 1)
        # 情形 B：h = n/2（中间）
        h2 = n // 2
        nmB = C(n + 2, h2) * C(n, h2)
        print(f'n={n:>2}:  h=n-1 ⟹ #minors={nmA:>12}   |   h=n/2 ⟹ #minors={nmB:>16}')

    print()
    print('=== p=2, r=1 的对照（m=q+4） ===')
    print(f'{"n":>3} {"q":>3} {"m":>3} {"h":>3} {"#h-minors":>16}')
    for n in (6, 8, 10):
        for q in (1, 2, n // 2, n - 1):
            p = 2
            h = min(q + 2 * p, n)
            m = q + 2 * p
            print(f'{n:>3} {q:>3} {m:>3} {h:>3} {C(m, h) * C(n, h):>16}')


if __name__ == '__main__':
    main()
