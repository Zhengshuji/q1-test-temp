r"""P2 例子 $q=4$ 的 all-bad：在 $r<d$ 的除子上，(A) **从不成立**。

背景：$r=\operatorname{rank}(CAZ)<d$ 当且仅当 $\operatorname{im}W$ 与 $N:=\ker(CA K_L)$ 非平凡相交（本实例 $\dim N=2$）。
这给出 $\mathrm{Gr}(2,4)$ 里的一个**除子**（不是单点），随机采样碰不到，必须**显式构造**。
本脚本在 $N$ 上取整数向量 $n$、在 $\{0,\pm1\}^4$ 上扫 $e$，构造 $W=[n,\ e]$，检查 $(A)$。

结论（本实例）：240 个 $r<d$ 候选中 $(A)$ 成立 **0** 个 ⟹ 在 $(A)$ 成立的 $Z$ 上必有 $r=d$，
再由 [../h_bound/README.md](../h_bound/README.md) 的定理（$h=n-p\Rightarrow(S)$ 失败）得
$q=4$ 的 all-bad 是**确定的**（不再依赖概率采样）。

用法：python proof/layer_program/c216_rdivisor.py
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))
sys.path.insert(0, _HERE)

import audit_independent as AI
import spectral_gcd as SG
import importlib.util as iu

_spec = iu.spec_from_file_location('C211', os.path.join(_HERE, 'c211_allbad_scan.py'))
M211 = iu.module_from_spec(_spec)
_spec.loader.exec_module(M211)

A, C, L, n, p = M211.A, M211.C, M211.L, M211.n, M211.p


def main():
    CA = AI.mul(C, A)
    KLv = AI.nullspace([[Fr(x) for x in row] for row in (C + L)])
    m_L = len(KLv)
    KL = [[KLv[k][i] for k in range(m_L)] for i in range(n)]
    K = AI.mul(CA, KL)                     # 2×4
    Nv = AI.nullspace(K)                   # N = ker(CA K_L)（4×2）
    assert len(Nv) == 2, f'dim N 应为 2，实为 {len(Nv)}'
    print(f'dim K = {m_L}，dim N = {len(Nv)}（与 $r<d$ 的除子维数一致）')

    Nvecs = []
    for a, b in itertools.product(range(2), repeat=2):
        if a == 0 and b == 0:
            continue
        v = [Fr(a) * Nv[0][i] + Fr(b) * Nv[1][i] for i in range(m_L)]
        if AI.rank([v]) == 1:
            Nvecs.append(v)

    grid = [Fr(-1), Fr(0), Fr(1)]
    tot = a_ok = as_ok = 0
    for nvec in Nvecs:
        for e in itertools.product(grid, repeat=m_L):
            e = list(e)
            if AI.rank([nvec, e]) < 2:
                continue
            W = [[nvec[i], e[i]] for i in range(m_L)]
            Z = AI.mul(KL, W)
            if AI.rank(Z) < 2:
                continue
            tot += 1
            CAZ = AI.mul(CA, Z)
            r = AI.rank(CAZ)
            assert r < 2, '构造的 W 应满足 r<d'
            Rv = AI.nullspace(CAZ)
            R = [[Rv[k][i] for k in range(len(Rv))] for i in range(2)]
            AZR = AI.mul(AI.mul(A, Z), R)
            M1 = [list(Z[i]) + list(AZR[i]) for i in range(n)]
            if AI.rank(M1) == 2:
                a_ok += 1
                g, h, _ = SG.spectral_gcd_Z(A, C, Z)
                if SG.pdeg(g) == 0:
                    as_ok += 1
    print(f'r<d 的候选 {tot} 个：(A) 成立 {a_ok} 个；其中 (S) 也成立 {as_ok} 个')
    assert a_ok == 0, '(A) 在 r<d 上竟然成立 —— P2 例子的结论需要重新检查'
    print('⟹ 本实例中 (A) ⟹ r=d；结合 h 定理，q=4 的 all-bad 是确定的 ✓')


if __name__ == '__main__':
    main()
