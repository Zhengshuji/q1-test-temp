"""regression_Lstar.py —— 专家 2026-11-03 给出的 $q=3$ 见证的**回归测试**

实例（$n=7$、$p=r=2$、seed 4004）：我们曾错误地报告"所有阶都无解"；专家给出

$$\\mathcal L_*=\\begin{pmatrix}-1&0&0&0&-1&0&0\\\\ 1&0&0&0&0&0&1\\\\ 1&0&0&-1&0&-1&1\\end{pmatrix},$$

其第三行恰是 $CA$ 的第二行。本脚本核验（全部精确有理算术）：

1. $\\mathcal L_*$ 的前两行等于 $L_0$，第三行等于 $CA$ 的第二行；
2. $\\operatorname{rank}[C;\\mathcal L_*]=5$、$\\operatorname{rank}[\\mathcal L_*;CA;C]=5=h$、
   $\\operatorname{rank}[\\mathcal L_*A;\\mathcal L_*;CA;C]=5$ ⟹ $(5a)$；
3. **两个常数极大子式**（$5\\times5$）：行 $1,2,3,4,7$、列 $1,2,4,5,7$ 的行列式为 $-1$；
   行 $1,2,3,4,7$、列 $1,2,5,6,7$ 的行列式为 $+1$ ⟹ $\\operatorname{rank}Q_*(\\lambda)\\ge5$ 对所有 $\\lambda$；
   结合 $(5a)$ 给出的 $\\operatorname{rank}Q_*(\\lambda)\\le h=5$，得 $(5b)$；
4. 与 Toeplitz / 极大子式 gcd 两路判据一致；
5. 并核验 $q=2$（$\\mathcal L=L_0$）的 $h=5$（不是 6）与 $\\gcd=\\lambda-1$（在 $\\lambda=1$ 处失败）。

用法：python tools/verification/regression_Lstar.py
"""

import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import spectral_gcd as SG                 # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import consistency_checks as CC           # noqa: E402

F = Fraction


def det(M):
    n = len(M)
    M = [row[:] for row in M]
    detv = F(1)
    for i in range(n):
        piv = next((r for r in range(i, n) if M[r][i] != 0), None)
        if piv is None:
            return F(0)
        if piv != i:
            M[i], M[piv] = M[piv], M[i]
            detv = -detv
        detv *= M[i][i]
        inv = M[i][i]
        for r in range(i + 1, n):
            if M[r][i]:
                f = M[r][i] / inv
                for c in range(i, n):
                    M[r][c] -= f * M[i][c]
    return detv


def main():
    n, p, r, seed = 7, 2, 2, 4004
    A, C, L0 = QR.make_instance(n, p, r, seed * 23 + p * 11 + r)
    CA = LQ.mul(C, A)
    Ls = [[F(-1), F(0), F(0), F(0), F(-1), F(0), F(0)],
          [F(1), F(0), F(0), F(0), F(0), F(0), F(1)],
          [F(1), F(0), F(0), F(-1), F(0), F(-1), F(1)]]
    print('1) 结构：')
    assert Ls[:2] == [list(x) for x in L0], '前两行应等于 L0'
    assert Ls[2] == list(CA[1]), '第三行应等于 CA 的第二行'
    print('   ✓ 前两行 = L0，第三行 = CA 的第二行')
    print('2) 秩：')
    rCL = LQ.rank([x[:] for x in C] + Ls)
    h = LQ.rank([x[:] for x in Ls] + [x[:] for x in CA] + [x[:] for x in C])
    r5a = LQ.rank([x[:] for x in LQ.mul(Ls, A)] + [x[:] for x in Ls]
                  + [x[:] for x in CA] + [x[:] for x in C])
    print(f'   rank[C;L_*]={rCL}  h=rank[L_*;CA;C]={h}  rank[L_*A;L_*;CA;C]={r5a}')
    assert (rCL, h, r5a) == (5, 5, 5), '三个秩都应等于 5'
    assert LQ.condA(A, C, Ls), '(5a) 应成立'
    print('   ✓ (5a) 成立（$h=5$）')
    print('3) 常数极大子式：')
    Qsl = [[F(0)] * n for _ in range(len(Ls))]
    LA = LQ.mul(Ls, A)
    # Q_*(λ) = [λL_* − L_*A; CA; C]；行列式与 λ 无关则直接取 λ=0 与 λ=1 两个值比较
    def Q_at(lam):
        Q = [[lam * Ls[i][j] - LA[i][j] for j in range(n)] for i in range(len(Ls))]
        return Q + [x[:] for x in CA] + [x[:] for x in C]
    rows = [0, 1, 2, 3, 6]                       # 1,2,3,4,7（0-based）
    for cols in ([0, 1, 3, 4, 6], [0, 1, 4, 5, 6]):
        d0 = det([[Q_at(F(0))[i][j] for j in cols] for i in rows])
        d1 = det([[Q_at(F(1))[i][j] for j in cols] for i in rows])
        d2 = det([[Q_at(F(5, 3))[i][j] for j in cols] for i in rows])
        print(f'   列 {[c + 1 for c in cols]}：det(λ=0)={d0}，det(λ=1)={d1}，det(λ=5/3)={d2}')
        assert d0 == d1 == d2 != 0, '该子式应为非零常数'
    print('   ✓ 两个非零常数极大子式 ⟹ rank Q_*(λ) ≥ 5 = h 对所有 λ')
    print('4) 与两路判据一致：')
    res = TC.analyse(A, C, Ls)
    gcd = SG.spectral_gcd(A, C, Ls)
    print(f'   Toeplitz: (5b)={res["five_b"]}，ε={res["eps_smith"]}，d_fin={res["d_fin"]}；gcd={gcd}')
    assert res['five_b'] is True and gcd[0] == [F(1)]
    print('5) q=2（L=L0）的修正：')
    L2 = [list(x) for x in L0]
    h2 = LQ.rank([x[:] for x in L2] + [x[:] for x in CA] + [x[:] for x in C])
    r2 = TC.analyse(A, C, L2)
    g2 = SG.spectral_gcd(A, C, L2)
    print(f'   h={h2}（应为 5）；(5a)={LQ.condA(A, C, L2)}；(5b)={r2["five_b"]}；gcd={g2}')
    assert h2 == 5 and r2['five_b'] is False and g2[0] == [F(-1), F(1)]
    print('   ✓ h=5、gcd=λ−1（在 λ=1 处失败）')
    print('\n   [一致性] 七条检查：')
    CC.check_candidate(A, C, L0, Ls, tag='Lstar')
    CC.check_candidate(A, C, L0, L2, tag='L0@q=2')
    print('\n✓ 回归测试通过：q_min = 3（此前"所有阶无解"的结论作废）')


if __name__ == '__main__':
    main()
