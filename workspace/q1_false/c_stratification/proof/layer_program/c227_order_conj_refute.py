r"""**已于 2026-10-30 撤回**：本脚本的 $A$-不变性检查用了**行作用** $\operatorname{row}(v)\cdot A$，
而 $(A)$ 需要**列作用** $A Z$（$Z$ 的列是基向量）。按列作用重算原实例：
$\operatorname{rank}[Z,AZR]=2\ne d=1$ ⟹ $(A)$ 不成立 ⟹ 反例无效。
更正版：[c227b_order_conj_recheck.py](c227b_order_conj_recheck.py)（正确方向，200 个点全为终端阶，无反例）。

**原说明（保留作记录）**：阶谱猜想被推翻 —— 在 $q=n-r_1$ 上存在 $(A)\wedge(S)$ 的点。

构造：$n=4$、$p=2$、$r=1$，取 $r_1=\operatorname{rank}[C;CA]=3$（故 $h=\dim V=1$），
$V=\operatorname{span}(v)$、$L_0$ 使 $\ker[C;L_0]=V$、且 $Av=\lambda v$（$V$ 是一维不变子空间）。
取 $q=1=r$、$Z=V$：$d=n-p-q=1$。

则：
- $(A)$：$CAZ=0$（$Z=V\subseteq\ker CA$）⟹ $R=I$、$AZR=Av=\lambda v$ ⟹ $\operatorname{rank}[Z,AZR]=1=d$ ✓；
- $(S)$：$P(\lambda)=[(\lambda I-A)V\mid Z]=[(\lambda-\lambda_0)v\mid v]$，列空间恒为 $\operatorname{span}(v)$，
  $h=\dim V=1$ ⟹ 秩恒 $=1=h$ ⟹ $(S)$ 成立 ✓。

于是 $q=n-r_1$ 可行。若该实例的 $n_0-p\ne q$，则阶谱猜想"$q=n-r_1$ 不可行"的预测被推翻。

用法：python proof/layer_program/c227_order_conj_refute.py
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
        v = Vv[0]
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
            Az = AI.mul([v], A)[0]
            if AI.rank([v, Az]) != 1:
                continue
            funcobs = AI.rank(Rows + [L0[0]]) == n0
            Z = [[v[i]] for i in range(n)]
            g, h, _c = SG.spectral_gcd_Z(A, C, Z)
            if SG.pdeg(g) != 0:
                continue
            q, d = 1, n - p - 1
            print(f'trial {trial}：n={n}, p={p}, r={r}, r1={r1}, n0={n0}, n-r1={n - r1}, n0-p={n0 - p}'
                  f'（功能可观测={funcobs}）')
            print(f'  A = {[[str(x) for x in row] for row in A]}')
            print(f'  C = {[[str(x) for x in row] for row in C]}')
            print(f'  L0 = {[[str(x) for x in row] for row in L0]}')
            print(f'  v（Z=V 的基）= {[str(x) for x in v]}')
            print(f'  q={q}（=n-r1）、d={d}、h={h}、gcd 次数={SG.pdeg(g)} ⟹ (S) 成立')
            assert n0 - p != q, '该例恰好是终端阶，需继续找'
            assert q == n - r1 and d == 1
            print('\n⟹ 在 q=n-r1 上存在 (A)∧(S) 的点，而 q≠n0-p'
                  ' ⟹ 阶谱猜想的"q=n-r1 不可行"被**推翻**（R16）')
            return
    print('未找到（可换种子）')


if __name__ == '__main__':
    main()
