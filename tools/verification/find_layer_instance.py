"""find_layer_instance.py —— 搜索"正维线性解集"的真实实例，并跑比较实验

背景（attempts/10 §8.3）：
  之前的三个真实实例上，图卡内"U_0 ⊆ U"把 U 钉死（线性解集 0 维），比较实验没有信息量。
  要在**真实** (A,C,L0) 实例上检验"线性条件是否蕴含行列式条件"，需要
      (d - rho_ci) * (rho_ci - 1) > 0，即 2 <= rho_ci <= d - 1。

做法：确定性伪随机搜索小的整数 A（n=6, p=1, C=e0, L0=e1），用闭包算 rho_ci，
  筛出 2 <= rho_ci <= d-1 的实例，然后调用 layer_min_affine.analyse 做比较。

谨慎：搜索是"筛"不是"证"；找到的实例只作为**反例**或**证据**，不构成定理。
"""

import os
import random
import sys
from fractions import Fraction

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _here)

from min_layer_closure import quotient_data, closure, unit  # noqa: E402
from layer_min_affine import analyse  # noqa: E402


def make_instance(n, seed, density=0.3):
    rng = random.Random(seed)
    A = [[Fraction(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if rng.random() < density:
                A[i][j] = Fraction(rng.choice([-1, 0, 1, 2]))
    C = [unit(n, 0)]
    L0 = [unit(n, 1)]
    return A, C, L0


def scan(n=6, trials=400, seed0=1000):
    good = []
    for s in range(trials):
        A, C, L0 = make_instance(n, seed0 + s)
        try:
            T, B, U0, info = quotient_data(A, C, L0)
        except AssertionError:
            continue
        d = info['d']
        if d < 3:
            continue
        Ustar = closure(T, B, U0, verbose=False)
        rho = len(Ustar)
        if 2 <= rho <= d - 1 and len(U0) >= 1:
            good.append((seed0 + s, d, rho, len(B), len(U0)))
    return good


def main():
    print('=== 搜索 n=6, p=1, C=e0, L0=e1：找 2 <= rho_ci <= d-1 的实例 ===')
    good = scan()
    print(f'命中 {len(good)} 个：')
    for g in good[:12]:
        print(f'  seed={g[0]}, d={g[1]}, rho_ci={g[2]}, dim B={g[3]}, dim U0={g[4]}')
    if not good:
        print('（无命中：可能需要更多 trial 或更大 n）')
        return
    # 对前两个候选做比较实验
    for g in good[:2]:
        seed, d, rho, db, du0 = g
        A, C, L0 = make_instance(6, seed)
        print(f'\n=== 比较实验：seed={seed}（d={d}, rho_ci={rho}）===')
        T, B, U0, info = quotient_data(A, C, L0)
        analyse(T, B, U0, name=f'seed{seed}')


if __name__ == '__main__':
    main()
