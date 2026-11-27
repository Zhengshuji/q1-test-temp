r"""无解实例的证书：$\operatorname{rank}(A)\le1$ 的一族实例上，MIN-ROWS **根本没有解**。

依据（docs/02 §F）：
   可行 ⇒ ρ ≤ r(λ0)，而 ρ ≥ ρ_ci；故  ρ_ci > r(λ0)  ⇒  无解。
脚本对每个写死的实例：用有理算术算出 j、r(0)、ρ_ci（= P(T,B,U0)，用 c195 的 P_alg），
断言 ρ_ci > r(0)，并顺带做一次随机搜索（只作旁证，不是证明）。

这些实例来自对 rank(A)=1 的随机族的扫描（58/58 全部 ρ_ci > r(0) ⟹ 无解）。
用法：python proof/rank_barrier/no_solution_certificate.py
"""
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'ledger'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'p_algorithm'))

import audit_independent as AI
import c201_barrier_audit as BAR

INSTANCES = [
    dict(name='rank1_n6_p2_A',
         A=[[-4, -4, -4, -2, -4, -4], [0, 0, 0, 0, 0, 0], [4, 4, 4, 2, 4, 4],
            [4, 4, 4, 2, 4, 4], [-4, -4, -4, -2, -4, -4], [-2, -2, -2, -1, -2, -2]],
         C=[[1, 2, 1, -1, -2, 2], [-2, -2, 0, -2, 1, -2]],
         L0=[[-1, 1, 0, -1, 1, 1]]),
    dict(name='rank1_n6_p2_B',
         A=[[0, 0, 0, 0, 0, 0], [2, 2, 0, 0, 1, -1], [4, 4, 0, 0, 2, -2],
            [-4, -4, 0, 0, -2, 2], [0, 0, 0, 0, 0, 0], [-4, -4, 0, 0, -2, 2]],
         C=[[2, 0, -2, 0, 0, 1], [1, -2, 1, 2, 2, 1]],
         L0=[[0, -1, 2, 2, -1, -1]]),
    dict(name='rank1_n6_p2_C',
         A=[[4, -4, 4, -2, -2, -4], [0, 0, 0, 0, 0, 0], [2, -2, 2, -1, -1, -2],
            [4, -4, 4, -2, -2, -4], [2, -2, 2, -1, -1, -2], [4, -4, 4, -2, -2, -4]],
         C=[[2, -2, 2, 1, 1, -1], [1, -1, -2, 1, 1, 2]],
         L0=[[1, 2, -1, 1, 2, 2]]),
]


def main():
    ok = 0
    for inst in INSTANCES:
        A = [[Fr(x) for x in r] for r in inst['A']]
        C = [[Fr(x) for x in r] for r in inst['C']]
        L0 = [[Fr(x) for x in r] for r in inst['L0']]
        out = BAR.audit(A, C, L0)
        assert AI.rank(A) <= 1
        assert out['no_solution'], f"{inst['name']}: 没有满足 ρ_ci > r(0)"
        print(f"{inst['name']}: rank(A)={AI.rank(A)}、j={out['j']}、d={out['d']}、"
              f"r(0)={out['rmin']}、ρ_ci={out['rho_ci']}  ⟹  可证无解 ✓")
        ok += 1
    print(f'\n{ok}/{len(INSTANCES)} 个实例：ρ_ci > r(0) ⟹ 无解（[已证-纸面] + 精确计算）')


if __name__ == '__main__':
    main()
