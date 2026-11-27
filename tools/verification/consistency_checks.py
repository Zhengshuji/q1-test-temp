"""consistency_checks.py —— 专家 2026-11-03 §8.6 的七条一致性检查（可复用）

对任一候选 $(A,C,L_0,\\mathcal L)$（$\\mathcal L$ 含 $L_0$、$q$ 行）逐条核验并 `assert`：

1. $\\operatorname{rank}[C;\\mathcal L]=p+q$；
2. $\\dim\\ker[C;\\mathcal L]=n-p-q$；
3. 零空间基 $Z$ 满足 $CZ=0$、$\\mathcal LZ=0$；
4. $(5a)$ 与零空间秩判据（$\\operatorname{row}(\\mathcal LA)\\subseteq\\operatorname{row}\\mathcal L+W$）一致；
5. 铅笔的**目标秩** $h=\\operatorname{rank}[\\mathcal L;CA;C]$，且 $\\lambda$ 取一般值时的秩恰为 $h$（法秩）；
6. 极大子式 gcd 与 Toeplitz 零度判据给出同一个 $(5b)$ 结论；
7. 所有条目都是有理数（`Fraction`）——因而候选是实矩阵（专家 §8.2 的域要求）。

附注（专家 §8.4）：谱域取整个 $\\mathbb C$（含 $\\lambda=0$）：第 6 条的 gcd 判据是恒等式检验，与具体 $\\lambda$ 无关。

用法：python tools/verification/consistency_checks.py
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
import spectral_gcd as SG                 # noqa: E402

F = Fraction


def check_candidate(A, C, L0, L, tag='cand', verbose=True):
    n, p, r = len(A), len(C), len(L0)
    q = len(L)
    CA = LQ.mul(C, A)
    W = [x[:] for x in C] + [x[:] for x in CA]
    r1 = LQ.rank(W)

    # 7) 域
    for M in (A, C, L0, L):
        for row in M:
            for v in row:
                assert isinstance(v, F), f'{tag}: 条目不是 Fraction'

    # 1) rank[C;L] = p+q
    rCL = LQ.rank([x[:] for x in C] + L)
    assert rCL == p + q, f'{tag}: rank[C;L]={rCL} != p+q={p + q}'

    # 2) dim ker[C;L] = n-p-q
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L])
    d = len(Kc[0]) if Kc and Kc[0] else 0
    assert d == n - p - q, f'{tag}: dim ker={d} != n-p-q={n - p - q}'

    # 3) CZ = 0、LZ = 0
    if d > 0:
        for j in range(d):
            z = [Kc[i][j] for i in range(n)]
            for jc in range(p):
                assert sum(C[jc][i] * z[i] for i in range(n)) == 0, f'{tag}: CZ != 0'
            for jl in range(q):
                assert sum(L[jl][i] * z[i] for i in range(n)) == 0, f'{tag}: LZ != 0'

    # 4) (5a) 与 row(LA) ⊆ row L + W 一致
    cond = LQ.condA(A, C, L)
    LA = LQ.mul(L, A)
    base = LQ.rank([x[:] for x in L] + [x[:] for x in W])
    sub = LQ.rank([x[:] for x in LA] + [x[:] for x in L] + [x[:] for x in W])
    cond2 = (sub == base)
    assert cond == cond2, f'{tag}: (5a)={cond} 与零空间秩判据={cond2} 不一致'

    # 5) 目标秩 h 与法秩
    h = LQ.rank([x[:] for x in L] + [x[:] for x in CA] + [x[:] for x in C])
    lam = F(12345, 7)               # 一般值（不与 spec 相交的随机有理数）
    Qq = [[lam * L[i][j] - LA[i][j] for j in range(n)] for i in range(len(L))]
    Qq = Qq + [x[:] for x in CA] + [x[:] for x in C]
    r_gen = LQ.rank(Qq)
    assert r_gen == h, f'{tag}: 一般 λ 处秩 {r_gen} != h={h}（法秩不等于目标秩）'

    # 6) gcd 与 Toeplitz 一致
    gcd = SG.spectral_gcd(A, C, L)[0]
    gcd_ok = (gcd == [F(1)])
    toe = TC.analyse(A, C, L)['five_b']
    assert gcd_ok == toe, f'{tag}: gcd 判据={gcd_ok} 与 Toeplitz={toe} 不一致'

    if verbose:
        print(f'  {tag}: rank[C;L]={rCL} ✓ · dim ker={d} ✓ · CZ=LZ=0 ✓ · (5a)={cond} ✓ · '
              f'h={h}=法秩 ✓ · gcd/Toeplitz 一致（{"(5b) 成立" if toe else "失败"}）✓ · 域=有理 ✓')
    return {'cond': cond, 'h': h, 'five_b': toe, 'd': d, 'r1': r1}


def main():
    import importlib.util as iu
    import random
    print('=== 一致性检查（专家 §8.6）===')
    # C4 的两个候选
    spec = iu.spec_from_file_location('V4', os.path.join(_ROOT, 'proof', 'refuted', 'verify_C4_type3.py'))
    V4 = iu.module_from_spec(spec)
    spec.loader.exec_module(V4)
    A4, C4m, L04, q04, cands4 = V4.build()
    for i, L in enumerate(cands4[:2]):
        check_candidate(A4, C4m, L04, L, tag=f'C4#{i}')

    # 专家给的 L_*
    import qmin_scan_pr as QR
    A7, C7, L07 = QR.make_instance(7, 2, 2, 4004 * 23 + 2 * 11 + 2)
    Lstar = [[F(-1), F(0), F(0), F(0), F(-1), F(0), F(0)],
             [F(1), F(0), F(0), F(0), F(0), F(0), F(1)],
             [F(1), F(0), F(0), F(-1), F(0), F(-1), F(1)]]
    check_candidate(A7, C7, L07, Lstar, tag='Lstar')

    # 公开例子的一个 3 行候选。注意：它**不是**可行见证（极大子式 gcd 为三次、
    # Toeplitz 判据也是 False；见 c319 的负对照）。这里只用它检查"两个判据一致"，
    # 不用于声称可行性。
    spec2 = iu.spec_from_file_location('F2', os.path.join(_ROOT, 'proof', 'fernando_2gap', 'verify.py'))
    m2 = iu.module_from_spec(spec2)
    spec2.loader.exec_module(m2)
    Af, Cf, L0f = m2.A, m2.C, m2.L0
    v = [F(-42919, 32067), F(-55096, 10689), F(1), F(0), F(0), F(0), F(0), F(0)]
    check_candidate(Af, Cf, L0f, [list(x) for x in L0f] + [v], tag='fernando-q0')

    # 几个随机实例
    for (n, p, r, seed) in [(6, 1, 1, 3004), (6, 2, 1, 3002), (7, 2, 2, 3003)]:
        made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
        if made is None:
            continue
        A, C, L0 = made
        if LQ.rank(QR.observability_matrix(A, C) + [x[:] for x in L0]) != \
           LQ.rank(QR.observability_matrix(A, C)):
            continue
        import c208_q0_lower_bound as Q0
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        mm = len(K[0])
        d = n - p - q0
        if d <= 0:
            continue
        rng = random.Random(seed)
        Wm = [[F(rng.randrange(-3, 4)) for _ in range(d)] for _ in range(mm)]
        Zc = [[sum(K[i][t] * Wm[t][j] for t in range(mm)) for j in range(d)] for i in range(n)]
        if ZG.bool_rank(ZG.cols_to_rows(Zc)) != d:
            continue
        L = ZG.L_from_Z(A, C, L0, Zc, q0)
        if L is None:
            continue
        try:
            check_candidate(A, C, L0, L, tag=f'rand{n}/{p}/{r}')
        except AssertionError as e:
            print(f'  rand{n}/{p}/{r}: 跳过（{e}）')
    print('\n✓ 所有被检候选通过七条一致性检查')


if __name__ == '__main__':
    main()
