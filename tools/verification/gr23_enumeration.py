"""gr23_enumeration.py —— 小 Grassmannian 上的**穷举**（$\\operatorname{Gr}(2,3)=\\mathbb P^2$）

专家 2026-11-03 §7 指出：$q_0$ 阶的候选枚举若不穷尽 $\\operatorname{Gr}(d,K)$，就会漏解
（实例 $n=7,p=r=2$ 的 $q=3$ 阶就有一个被漏掉的解 $\\mathcal L_*$，其第三行是 $CA$ 的第二行）。

本脚本给出**穷举**做法：把 $\\mathcal Z$ 写成 $K\\cdot W$（$K$ 的基为 $k_1,k_2,k_3$，$W$ 是 $3\\times2$ 矩阵），
按 $W$ 的三个 $2\\times2$ 主子式选图卡，各图卡上自由参数有 2 个；在有理解网格上扫描，
对每个 $\\mathcal Z$：

1. 检查 $(5a)$（用 $\\operatorname{rank}\\varphi=0$ 或直接 `condA`）；
2. 若可行，构造 $\\mathcal L$ 并判 $(5b)$；
3. 记录"好/坏"分布，并与专家给的 $\\mathcal L_*$ 对照。

用法：python -u tools/verification/gr23_enumeration.py 7 2 2 4004
"""

import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402

F = Fraction


def charts(d, m):
    """Gr(d,m) 的图卡：返回 (rows, cols) 列表，每个图卡由自由参数矩阵填充。"""
    import itertools
    out = []
    for rows in itertools.combinations(range(m), d):
        rest = [i for i in range(m) if i not in rows]
        out.append((rows, rest))
    return out


def build_W(rows, rest, params, d, m):
    """在给定图卡上构造 d×m 的 W：identity 在 rows 上，params 填在 rest 列。"""
    W = [[F(0)] * m for _ in range(d)]
    for a, r0 in enumerate(rows):
        W[a][r0] = F(1)
    idx = 0
    for a in range(d):
        for c in rest:
            W[a][c] = params[idx]
            idx += 1
    return W


def main():
    if len(sys.argv) >= 5:
        n, p, r, seed = (int(x) for x in sys.argv[1:5])
    else:
        n, p, r, seed = 7, 2, 2, 4004
    made = QR.make_instance(n, p, r, seed * 23 + p * 11 + r)
    A, C, L0 = made
    CA = LQ.mul(C, A)
    q0 = Q0.eta_and_q0(A, C, L0)[0]
    q = int(sys.argv[5]) if len(sys.argv) > 5 else q0
    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])   # n × m
    n_, m = len(K), len(K[0])
    d = n - p - q
    print(f'实例 n={n} p={p} r={r} seed={seed}；q={q}；dim K={m}；d={d}')
    if d != 2 or m != 3:
        print('本脚本只处理 Gr(2,3)=P^2 的情形')
        return
    grid = [F(k) for k in range(-3, 4)] + [F(1, 2), F(-1, 2), F(2, 3), F(-2, 3), F(3, 2)]
    good = bad = adm = 0
    seen = set()
    for (rows, rest) in charts(d, m):
        for a in grid:
            for b in grid:
                W = build_W(rows, rest, [a, b], d, m)
                # Z = K·W（列）
                Z = [[sum(K[i][t] * W[j][t] for t in range(m)) for j in range(d)]
                     for i in range(n_)]
                if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                    continue
                key = tuple(str(v) for col in Z for v in col)
                if key in seen:
                    continue
                seen.add(key)
                L = ZG.L_from_Z(A, C, L0, Z, q)
                if L is None or not LQ.condA(A, C, L):
                    continue
                adm += 1
                res = TC.analyse(A, C, L)
                if res['five_b']:
                    good += 1
                else:
                    bad += 1
    print(f'穷举（网格 {len(grid)}^2 × 3 图卡，去重后）：(5a)-可行 {adm} 个，其中 (5b) 成立 {good}、失败 {bad}')
    # 专家给的 L_*
    Ls = [[F(-1), F(0), F(0), F(0), F(-1), F(0), F(0)],
          [F(1), F(0), F(0), F(0), F(0), F(0), F(1)],
          [F(1), F(0), F(0), F(-1), F(0), F(-1), F(1)]]
    res = TC.analyse(A, C, Ls)
    print(f'专家给的 L_*：(5a)={LQ.condA(A, C, Ls)}，h={res["h"]}，(5b)={res["five_b"]}')


if __name__ == '__main__':
    main()
