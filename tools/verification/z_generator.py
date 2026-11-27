r"""z_generator.py —— 用**零空间参数化**生成任意阶（含最小阶 $q_0$）的可行增广

难点：闭包（$V_{\\min}$）会**加多行**，因此无法生成 $q_0$ 行的候选。改用文献的几何参数化：

$$\mathcal Z=\\ker\\begin{pmatrix}C\\\\ \\mathcal L\\end{pmatrix}\\subseteq\\ker[C;L_0],\\qquad \\dim\\mathcal Z=n-p-q .$$

反过来：给定 $\\mathcal Z$（$n\\times d$，$d=n-p-q$，$\\operatorname{im}\\mathcal Z\\subseteq\\ker[C;L_0]$），
$[C;\\mathcal L]$ 的行就是 $\\mathcal Z^{\\perp}$ 的基（维数 $p+q$，含 $\\operatorname{row}C$）。
取 $\\mathcal L$ 的 $q$ 行把 $C$ 补成 $\\mathcal Z^{\\perp}$ 的一组基即可。

于是"任意阶的候选"可以通过在 $\\operatorname{Gr}(d,\\,n-p-r)$ 中抽 $\\mathcal Z$ 得到——
**包括 $q=q_0$**，这是闭包路线做不到的。

用法：python tools/verification/z_generator.py
"""

import itertools
import os
import random
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402

F = Fraction


def ker_cols(M):
    rows = [list(r) for r in LQ.nullspace(M)]
    if not rows:
        return []
    return [[row[j] for row in rows] for j in range(len(rows[0]))]


def cols_to_rows(cols):
    return [[cols[i][t] for i in range(len(cols))] for t in range(len(cols[0]))]


def bool_rank(rows):
    return LQ.rank([list(r) for r in rows])


def L_from_Z(A, C, L0, Z, q):
    """由 $\\mathcal Z$ 构造 $q$ 行的 $\\mathcal L$（$[C;\\mathcal L]$ 的基为 $\\mathcal Z^\\perp$）。"""
    n = len(A)
    if not Z:                      # d = 0：Z = {0}，此时 Z^⊥ = 全空间
        B = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
        L = [list(x) for x in L0]
        for b in B:
            if len(L) == q:
                break
            if bool_rank([list(r) for r in C] + L + [b]) > bool_rank([list(r) for r in C] + L):
                L.append(b)
        return L if len(L) == q else None
    # 左零空间 {x : x Z = 0} = ker(Z^T)，Z^T 是 d × n
    ZT = [[Z[i][j] for i in range(n)] for j in range(len(Z[0]))]
    B = [list(r) for r in LQ.nullspace(ZT)]     # 每行长度 n，个数 n-d
    if len(B) != len(C) + q:
        return None
    # 本项目的问题要求 row(L0) ⊆ row(L)：先放 L0 的基，再用 B 的行把 [C;L] 补满
    L = [list(x) for x in L0]
    for b in B:
        if len(L) == q:
            break
        if bool_rank([list(r) for r in C] + L + [b]) > bool_rank([list(r) for r in C] + L):
            L.append(b)
    if len(L) != q:
        return None
    # 断言 [C;L] 与 B 张成同一空间
    assert bool_rank([list(r) for r in C] + L) == len(B)
    return L


def sample_L_at_order(A, C, L0, q, n_samples, seed):
    """在 $\\operatorname{Gr}(n-p-q,\\ \\ker[C;L_0])$ 中抽样，返回满足 $(5a)$ 的 $\\mathcal L$。"""
    rng = random.Random(seed)
    n, p, r = len(A), len(C), len(L0)
    K = ker_cols([list(x) for x in C] + [list(x) for x in L0])   # n × (n-p-r)
    if not K:
        return []
    m = len(K[0])
    d = n - p - q
    if d < 0 or d > m:
        return []
    out, seen = [], set()
    for _ in range(n_samples * 6):
        if d == 0:
            W = [[] for _ in range(m)]
            Zc = []
        else:
            W = [[F(rng.randrange(-3, 4)) for _ in range(d)] for _ in range(m)]
            # Z = K W
            Zc = [[sum(K[i][t] * W[t][j] for t in range(m)) for j in range(d)] for i in range(n)]
            if bool_rank(cols_to_rows(Zc)) != d:
                continue
        L = L_from_Z(A, C, L0, Zc, q)
        if L is None:
            continue
        if LQ.rank([list(x) for x in L] + [list(x) for x in L0]) != LQ.rank(L):
            continue
        key = tuple(tuple(str(x) for x in row) for row in L)
        if key in seen:
            continue
        seen.add(key)
        if not LQ.condA(A, C, L):
            continue
        out.append(L)
        if len(out) >= n_samples:
            break
    return out


def main():
    import importlib.util as iu
    spec = iu.spec_from_file_location('F2', os.path.join(_ROOT, 'proof', 'fernando_2gap', 'verify.py'))
    m = iu.module_from_spec(spec)
    spec.loader.exec_module(m)
    A, C, L0 = m.A, m.C, m.L0
    q0 = Q0.eta_and_q0(A, C, L0)[0]
    print(f'公开例子：n={len(A)} p={len(C)} r={len(L0)} q0={q0}')
    for q in (q0, q0 + 1, q0 + 2, q0 + 3):
        if q > len(A) - len(C):
            continue
        cands = sample_L_at_order(A, C, L0, q, 40, 777 + q)
        feas = 0
        for L in cands:
            res = TC.analyse(A, C, L)
            if res['five_b']:
                feas += 1
        print(f'  q={q}: 代数可行样本 {len(cands)}，其中 (5b) 成立 {feas}')
    print('\n注：这是**抽样**；论文用全部 Grassmann 图卡证明 q=3、4 全失败。')


if __name__ == '__main__':
    main()
