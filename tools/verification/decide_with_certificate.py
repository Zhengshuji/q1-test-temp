"""decide_with_certificate.py —— 带证书的逐阶判定（落实专家 §8.1：网格 ≠ 完整扫描）

对给定实例与阶 $q$，只在**拿到证书**时才下结论，否则输出 `UNKNOWN`：

| 结论 | 证书 |
|---|---|
| `INFEASIBLE_INTEGER` | 整数障碍：$s_0+\\min(t,n-s_0)<q+r_1$ 不成立且 $h\\ge q+r_1$ 由 $h=s_0+t$ 强制（$V'\\cap S=0$）|
| `INFEASIBLE_OCCLUSION` | $h=n$ 且 $\\dim\\overline{\\Phi(\\mathbb P(V))}\\ge q-r$（射影维数定理）|
| `FEASIBLE` | 显式见证 $\\mathcal L$（逐个通过七条一致性检查，含 $(5b)$ 的 gcd 判据）|
| `UNKNOWN` | 以上都没有：网格/抽样没找到**不**构成结论 |

单点情形（$q=r$，可行族只有一个点）与 $d=0$ 情形也直接给出结论。

用法：python -u tools/verification/decide_with_certificate.py [n p r seed]
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
import dim_Y as DY                        # noqa: E402
import consistency_checks as CC           # noqa: E402

F = Fraction


def rowspace(rows):
    out = []
    for r0 in rows:
        if LQ.rank(out + [r0]) > len(out):
            out.append(list(r0))
    return out


def instance_data(A, C, L0):
    CA = LQ.mul(C, A)
    W = [x[:] for x in C] + [x[:] for x in CA]
    r1 = LQ.rank(W)
    s0 = len(rowspace([x[:] for x in C] + [x[:] for x in L0] + [x[:] for x in W]))
    q0 = Q0.eta_and_q0(A, C, L0)[0]
    n0 = LQ.rank(QR.observability_matrix(A, C))
    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    return dict(CA=CA, W=W, r1=r1, s0=s0, q0=q0, n0=n0, k=len(K[0]), K=K)


def decide(A, C, L0, q, samples=80, verbose=True):
    """返回 (结论, 说明, 见证或 None)。"""
    n, p, r = len(A), len(C), len(L0)
    D = instance_data(A, C, L0)
    d = n - p - q
    t = q - r
    note = []
    # 情形 0：单点（可行族 = 一个点 L0）
    if d == D['k']:
        L = [list(x) for x in L0]
        if len(L) != q:
            return 'UNKNOWN', 'd=k 但 q≠r（不应发生）', None
        CC.check_candidate(A, C, L0, L, tag=f'q={q} single')
        res = TC.analyse(A, C, L)
        ok = res['five_b']
        kind = 'FEASIBLE' if ok else ('INFEASIBLE_INTEGER' if res['h'] >= q + D['r1'] else 'INFEASIBLE_SPECTRAL')
        return kind, f'单点（q=r）：h={res["h"]}，q+r1={q + D["r1"]}，(5b)={ok}', (L if ok else None)
    # 情形 1：整数障碍（V'∩S=0 时 h=s0+t 恒定）
    hmax = D['s0'] + min(t, n - D['s0']) if t >= 0 else None
    if t >= 0 and D['s0'] + t >= q + D['r1']:
        note.append(f'整数障碍：s0+t={D["s0"] + t} ≥ q+r1={q + D["r1"]}（若 V\'∩S=0 则 h 恒定）')
        return 'INFEASIBLE_INTEGER', '；'.join(note), None
    # 情形 2：遮蔽（h=n 且 dim Y ≥ q−r）
    if hmax == n and t >= 0:
        mY, info = DY.dim_Y(A, C, L0)
        if mY is not None and mY >= q - r:
            return 'INFEASIBLE_OCCLUSION', f'h=n 且 dim Y={mY} ≥ q−r={q - r}（{info}）', None
        note.append(f'遮蔽不适用/不足：dim Y={mY}，q−r={q - r}')
    # 情形 3：找见证
    if d <= 0:
        return 'UNKNOWN', 'd≤0：需直接构造补（本脚本不覆盖）', None
    rng = __import__('random').Random(q * 7919 + 13)
    for _ in range(samples):
        Wm = [[F(rng.randrange(-3, 4)) for _ in range(d)] for _ in range(D['k'])]
        Z = [[sum(D['K'][i][tt] * Wm[tt][j] for tt in range(D['k'])) for j in range(d)]
             for i in range(n)]
        if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
            continue
        L = ZG.L_from_Z(A, C, L0, Z, q)
        if L is None or not LQ.condA(A, C, L):
            continue
        if TC.analyse(A, C, L)['five_b']:
            CC.check_candidate(A, C, L0, L, tag=f'q={q} witness')
            return 'FEASIBLE', f'见证（{samples} 次抽样内找到）', L
    return 'UNKNOWN', '；'.join(note) + f'；{samples} 次抽样未见见证（不构成否证）', None


def main():
    if len(sys.argv) >= 5:
        n, p, r, seed = (int(x) for x in sys.argv[1:5])
        made = QR.make_instance(n, p, r, seed * 23 + p * 11 + r)
    else:
        n, p, r, seed = 7, 2, 2, 4004
        made = QR.make_instance(n, p, r, seed * 23 + p * 11 + r)
    A, C, L0 = made
    D = instance_data(A, C, L0)
    print(f'实例 n={n} p={p} r={r} seed={seed}：q0={D["q0"]}、n0={D["n0"]}、'
          f'r1={D["r1"]}、s0={D["s0"]}、dim K={D["k"]}；阶区间 [{D["q0"]},{D["n0"] - p}]')
    for q in range(D['q0'], D['n0'] - p + 1):
        if q - r < 0 or n - p - q < 0:
            continue
        verdict, why, wit = decide(A, C, L0, q)
        print(f'  q={q}: {verdict} —— {why}')
        if wit:
            for row in wit:
                print('     ', [str(x) for x in row])


if __name__ == '__main__':
    main()
