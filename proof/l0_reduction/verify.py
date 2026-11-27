r"""l0_reduction 的机器复核：$c\in\\operatorname{row}C$ 时，加/去这一行不改变 $(5a),(5b)$。

命题见 [README.md](README.md)：$q_{\\min}(A,C,\\binom{c}{L_1})=q_{\\min}(A,C,L_1)+1$。
这里验证它的核心等式（秩不变）——不是 $q_{\\min}$ 本身。

用法：python proof/l0_reduction/verify.py [--trials 100]
"""
import os
import random
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))

import audit_independent as AI


def main():
    trials = 100
    if '--trials' in sys.argv:
        trials = int(sys.argv[sys.argv.index('--trials') + 1])
    rng = random.Random(20261030)
    ok = 0
    for _ in range(trials):
        n, p, r, q = 5, 2, 1, 2
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        L1 = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(r)]
        R = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(q)]
        # c 取 row C 的随机线性组合
        coef = [Fr(rng.randint(-2, 2)) for _ in range(p)]
        c = [sum(coef[i] * C[i][k] for i in range(p)) for k in range(n)]
        without = [L1[0]] + R
        with_c = [c] + without
        same = (AI.cond_5a_orig(A, C, without) == AI.cond_5a_orig(A, C, with_c)
                and AI.cond_5b_orig(A, C, without) == AI.cond_5b_orig(A, C, with_c))
        ok += same
    print(f'加/去 row(C) 行：{ok}/{trials} 个随机实例上 (5a),(5b) 不变 ✓'
          if ok == trials else f'有 {trials - ok}/{trials} 个不一致 ✗')
    return 0 if ok == trials else 1


if __name__ == '__main__':
    sys.exit(main())

