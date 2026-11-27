r"""**R16 更正**：先前的"$q=n-r_1$ 可行"反例是**方向错误**造成的，不是真反例。

错误：c227 用 $\operatorname{row}(v)\cdot A$（行作用）判 $Z=\mathcal V$ 的 $A$-不变性，
而 $(A)$ 需要的是**列作用** $AZ$（$Z$ 的列是基向量）。按列作用重算，原实例
$\operatorname{rank}[Z,AZR]=2\ne d=1$ ⟹ $(A)$ **不成立** ⟹ 反例不成立，R16 撤回。

本脚本按**正确方向**重做搜索：在 $h=d=1$、$Z=\mathcal V$ 的族里找 $(A)\wedge(S)$ 且 $q=n-r_1$ 的点，
并检查它们是否恰好是**终端阶**（$q=n_0-p$，那时不构成反例）。

用法：python proof/layer_program/c227b_order_conj_recheck.py
"""
import itertools
import os
import random
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import spectral_gcd as SG


def main():
    rng = random.Random(5)
    hits = []
    total = 0
    for trial in range(3000):
        n, p, r = 4, 2, 1
        A = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        CA = AI.mul(C, A)
        r1 = AI.rank(AI.vstack([C, CA]))
        if r1 != 3:
            continue
        Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
        if len(Vv) != 1:
            continue
        v = [Vv[0][i] for i in range(n)]
        Rows, cur = [], [list(x) for x in C]
        for _k in range(n):
            Rows.extend(cur)
            cur = [AI.mul([x], A)[0] for x in cur]
        n0 = AI.rank(Rows)
        for Lrows in itertools.combinations(range(n), 1):
            L0 = [[Fr(1) if k == j else Fr(0) for k in range(n)] for j in Lrows]
            if AI.rank(C + L0) != 3:
                continue
            ker = AI.nullspace([[Fr(x) for x in row] for row in (C + L0)])
            if len(ker) != 1 or AI.rank([ker[0], v]) != 1:
                continue
            Av = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]   # 列作用 ✓
            if AI.rank([v, Av]) != 1:
                continue
            Z = [[v[i]] for i in range(n)]
            CAZ = AI.mul(CA, Z)
            Rv = AI.nullspace(CAZ)
            R = [[Rv[k][i] for k in range(len(Rv))] for i in range(1)]
            AZR = AI.mul(AI.mul(A, Z), R)          # A·Z ✓
            M1 = [list(Z[i]) + list(AZR[i]) for i in range(n)]
            okA = AI.rank(M1) == 1
            g, h, _c = SG.spectral_gcd_Z(A, C, Z)
            okS = SG.pdeg(g) == 0
            total += 1
            if okA and okS:
                hits.append(dict(trial=trial, n0=n0, n0_minus_p=n0 - p, q=1, h=h,
                                 terminal=(n0 - p == 1)))
    nt = [h for h in hits if not h['terminal']]
    print(f'检查 {total} 个 (A,Z) 点；找到 (A)∧(S) 的 {len(hits)} 个')
    print(f'  其中**非终端阶**（$n_0-p\\ne q$）：{len(nt)} 个 ⟹ '
          + ('**存在反例**' if nt else '**没有反例**'))
    if hits[:3]:
        print('  前三例：', hits[:3])


if __name__ == '__main__':
    main()
