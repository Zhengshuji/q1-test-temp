r"""$q_0$ 下界：$\dim\mathcal V$ 在 $(5a)$ 下的最小值（秩保留算法，多项式时间）。

**为什么这是 $q1$ 的事**：$q_{\min}\ge q_0$，而 $q_0$ 是**多项式**可算的（论文 arXiv:2609.33615 的定理：
$q_0=\sum_j\eta_j$ 是条件 (A) 下的最小维数）。它比项目现有的 A.3 下界
$q\ge\max(r+\varepsilon,\ \rho_{ci}+\max(c_0,1))$ **更紧**（见本脚本的对比）。

算法（论文 §III 的全局秩保留）：生成行 $g=(C_1,\dots,C_p,L_1,\dots,L_r)$，按
$g_1,\dots,g_{p+r};\ g_1A,\dots;\ g_1A^2,\dots$ 的顺序考察，秩增加就保留；
$q_0=\sum_{j=1}^{r}\eta_j$（只数 $L$-生成行保留下来的行数）。

用法：python tools/ledger/c208_q0_lower_bound.py
"""
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'p_algorithm'))
sys.path.insert(0, _HERE)

import audit_independent as AI
import importlib.util as iu

_spec = iu.spec_from_file_location('C201', os.path.join(_HERE, 'c201_barrier_audit.py'))
BAR = iu.module_from_spec(_spec)
_spec.loader.exec_module(BAR)
import c189_ledger as LED


def eta_and_q0(A, C, L0):
    """返回 (q0, eta_C, eta_L, 保留行数)。A、C、L0 都是 Fraction 矩阵。"""
    n = len(A)
    gens = [list(r) for r in C] + [list(r) for r in L0]
    kept, alive = [], [True] * len(gens)
    eta = [0] * len(gens)
    for q in range(n):
        for i, g in enumerate(gens):
            if not alive[i]:
                continue
            v = g
            for _ in range(q):
                v = AI.mul([v], A)[0]
            if AI.rank(kept + [v]) > len(kept):
                kept.append(v)
                eta[i] += 1
            else:
                alive[i] = False
    p = len(C)
    return sum(eta[p:]), eta[:p], eta[p:], len(kept)


def a3_bound(A, C, L0, rho_ci):
    r = len(L0)
    feasible = AI.cond_5a_orig(A, C, L0) and AI.cond_5b_orig(A, C, L0)
    eps = 0 if feasible else 1
    M = AI.vstack([C, AI.mul(C, A)])
    j = AI.rank(M)
    S = AI.row_basis(L0)
    c0 = len(S) + j - AI.rank(AI.vstack([S, M]))
    return max(r + eps, rho_ci + max(c0, 1))


def main():
    rows = LED.certificates() + LED.directed() + LED.family(k=3)
    print(f"{'instance':32s} {'q0':>3s} {'A.3':>4s} {'q_wit':>5s}  tighter?")
    better = 0
    checked = 0
    for row in rows:
        A, C, L0 = row['A'], row['C'], row['L0']
        try:
            q0, etaC, etaL, kept = eta_and_q0(A, C, L0)
        except Exception as e:
            print(f"{row['name'][:32]:32s}  ERROR {e}")
            continue
        out = BAR.audit(A, C, L0)
        a3 = a3_bound(A, C, L0, out['rho_ci'])
        W = row.get('W')
        qw = len(W) if W else None
        checked += 1
        if qw is not None:
            assert qw >= q0, f'{row["name"]}: 见证 q 小于 q0（不该发生）'
        if q0 > a3:
            better += 1
        print(f"{row['name'][:32]:32s} {q0:3d} {a3:4d} "
              f"{('' if qw is None else str(qw)):>5s}  {'YES' if q0 > a3 else ''}")
    print()
    print(f'检查了 {checked} 个实例；其中 q0 比 A.3 **更紧**：{better} 个')
    print('（所有有见证的实例都满足 q_wit ≥ q0 ✓ —— 与 q_min ≥ q0 一致）')


if __name__ == '__main__':
    main()
