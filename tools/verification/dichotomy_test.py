"""dichotomy_test.py —— $d\\ge2$ 的**二分假设**：谱可行与可容许是否互斥？

关键观察（B.13c）：谱条件**只依赖** $\\mathcal Z=\\ker[C;\\mathcal L]$（失败 $\\iff\\exists x\\in V\\setminus\\mathcal Z,\\lambda:(\\lambda I-A)x\\in\\mathcal Z$）。
而 $(5a)$ 依赖整个 $\\mathcal L$。对固定的 $\\mathcal Z$，满足 $\\ker[C;\\mathcal L]=\\mathcal Z$ 的 $\\mathcal L$ 构成
$\\operatorname{Gr}(q,\\mathcal Z^\\perp/\\operatorname{row}C)$ 里的一大族。

本脚本测试：**谱可行的 $\\mathcal Z$（$d\\ge2$）是否根本没有可容许的 $\\mathcal L$？**
做法：取随机 $\\mathcal Z$，先判谱可行性（B.16c 或 B.12 等价式），再在"核 = 𝒵"的 $\\mathcal L$ 族里随机搜索 $(5a)$。

用法：python -u tools/verification/dichotomy_test.py
"""

import os
import sys
import itertools
import random
from fractions import Fraction
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import decide_symbolic as DS              # noqa: E402
import observability_test as OT           # noqa: E402

F = Fraction


def spectral_feasible_Z(A, C, Z):
    """B.13c：$\\mathcal Z$ 谱可行 $\\iff$ 不存在 $x\\in V\\setminus\\mathcal Z,\\lambda$ 使 $(\\lambda I-A)x\\in\\mathcal Z$。

    直接实现：对每个 $\\lambda$ 检查 $\\ker N_{\\mathcal Z}(\\lambda)\\subseteq S$（B.16c），
    用"极大子式 gcd"的形式只在 $s=0$ 时干净；这里用采样 $\\lambda$ 做不到严格，故改用
    **构造 $\\mathcal L$ 再走 B.12** 的方式——但那需要可容许 $\\mathcal L$ 存在。
    折中：只对"恰好存在可容许 $\\mathcal L$"的样本判谱可行（用 B.12），其余记为 unknown。
    """
    return None


def rand_L_with_kernel(A, C, L0, Z, q, rng, tries=200):
    """随机构造 $\\mathcal L$（$q$ 行）使 $\\operatorname{row}\\mathcal L\\subseteq\\mathcal Z^\\perp$、含 $L_0$、且 $\\operatorname{rank}[C;\\mathcal L]=p+q$。"""
    n = len(A)
    p, r = len(C), len(L0)
    d = len(Z[0]) if (Z and Z[0]) else 0
    # 𝒵^⊥ 的基：解 Z^T y = 0
    Zt = [[Z[i][j] for i in range(n)] for j in range(d)] if d else []
    ns = ZG.ker_cols(Zt) if d else [[F(1) if i == j else F(0) for i in range(n)] for j in range(n)]
    dZ = len(ns[0]) if (ns and ns[0]) else 0
    if dZ < q:
        return None
    for _ in range(tries):
        R = []
        for _i in range(q - r):
            coef = [F(rng.randrange(-2, 3)) for _ in range(dZ)]
            R.append([sum(ns[i][t] * coef[t] for t in range(dZ)) for i in range(n)])
        L = [list(x) for x in L0] + R
        if LQ.rank(L) != q:
            continue
        if LQ.rank([list(x) for x in C] + L) != p + q:
            continue
        # 核恰好是 Z：rank[C;L] = p+q 且 rows ⊥ Z ⟹ ker 的维数 = n-(p+q) = d ✓
        return L
    return None


def main():
    rng = random.Random(20261117)
    st = Counter()
    for trial in range(3000):
        n = rng.choice([5, 6])
        p = r = 1
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        if LQ.rank(C) != 1 or LQ.rank(L0) != 1:
            continue
        if LQ.rank([list(x) for x in C] + L0) != 2:
            continue
        O = QR.observability_matrix(A, C)
        n0 = LQ.rank(O)
        if n0 != n or LQ.rank(O + [list(x) for x in L0]) != n:
            continue
        CA = LQ.mul(C, A)
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (K and K[0]):
            continue
        k = len(K[0])
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        for q in range(q0, n0):
            d = n - 1 - q
            if d < 2 or d > k:
                continue
            for rows in itertools.combinations(range(k), d):
                Z = DS.Z_from_theta(A, C, L0, q, rows, [F(0)] * (d * (k - d)))
                if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                    continue
                st['样本'] += 1
                # 在"核 = Z"的 L 族里找可容许者
                adm = 0
                feas = 0
                for _ in range(30):
                    L = rand_L_with_kernel(A, C, L0, Z, q, rng)
                    if L is None:
                        break
                    if not LQ.condA(A, C, L):
                        continue
                    adm += 1
                    ok, _w = OT.observability_ok(A, C, L)
                    if ok:
                        feas += 1
                st['有可容许 L 的 Z'] += 1 if adm > 0 else 0
                st['谱可行（在可容许中）'] += 1 if feas > 0 else 0
                if adm > 0 and feas == 0:
                    st['可容许但全失败'] += 1
                break
    print('统计：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')


if __name__ == '__main__':
    main()
