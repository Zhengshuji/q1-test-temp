"""verify.py —— 零左最小指标计数引理与推论 B.9 的精确验证

**引理**：设 $\\mathcal L$ 行满秩、$h=\\operatorname{rank}[\\mathcal L;CA;C]$、$r_1=\\operatorname{rank}[C;CA]$、
$p$ 为 $C$ 的行数。则 $Q_{\\mathcal L}(\\lambda)=[\\lambda\\mathcal L-\\mathcal LA;CA;C]$ 的**左最小指标**中

* 恰有 $2p-r_1$ 个等于 $0$（$C,CA$ 行之间的线性相关给出**常值**左零向量）；
* 非零左最小指标的个数恰为 $q+r_1-h$（$q$ 为 $\\mathcal L$ 的行数）。

**推论 B.9**：若 $h\\ge q+r_1$（即非零左指标为空），则 $\\sum_j\\varepsilon_j=0$，由 B.8 得
$d_{\\rm fin}=s=\\operatorname{rank}\\mathcal L>0$，故 $(5b)$ **失败**。
等价地：$(5b)\\Rightarrow h<q+r_1$。

本脚本在随机/构造实例上核验这两条（**验证不是证明**；纸面证明见 [theorem.md](theorem.md)）。
"""

import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import kronecker_pencil as KP             # noqa: E402
import observer_pencils as OP             # noqa: E402
import omega_construct as OC              # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402

F = Fraction


def check(A, C, L):
    P0, P1, h = OP.pencil_from_L(A, C, L)
    kk = KP.pencil_kronecker(P0, P1)
    eps = kk['left_min_indices']
    q, p = len(L), len(C)
    r1 = LQ.rank([r[:] for r in C] + [r[:] for r in LQ.mul(C, A)])
    m = len(eps)
    zeros = sum(1 for e in eps if e == 0)
    nonzero = sum(1 for e in eps if e > 0)
    d_fin = sum(x['degree'] for x in kk['finite_divisors'])
    s = LQ.rank(L)
    ok = []
    ok.append(('左指标个数 = q+2p-h', m == q + 2 * p - h, (m, q + 2 * p - h)))
    ok.append(('零指数个数 = 2p-r1', zeros == 2 * p - r1, (zeros, 2 * p - r1)))
    ok.append(('非零个数 = q+r1-h', nonzero == q + r1 - h, (nonzero, q + r1 - h)))
    ok.append(('Σε = s - d_fin', sum(eps) == s - d_fin, (sum(eps), s - d_fin)))
    if h >= q + r1:
        ok.append(('B.9: h≥q+r1 ⟹ d_fin>0', d_fin > 0, (d_fin,)))
    # 加强：d_fin ≤ s-(q+r1-h)（无条件成立，只用到 Σε ≥ 非零左指标个数）
    ok.append(('d_fin ≤ s-(q+r1-h)', d_fin <= s - (q + r1 - h), (d_fin, s - (q + r1 - h))))
    # 加强：若 (5b) 成立，则 q+r1-s ≤ h < q+r1
    if abs(sum(eps) - s) < 10**-9 and d_fin == 0:
        ok.append(('(5b) ⟹ q+r1-s ≤ h < q+r1',
                   q + r1 - s <= h < q + r1, (q + r1 - s, h, q + r1)))
    return ok, dict(q=q, p=p, h=h, r1=r1, eps=eps, d_fin=d_fin, s=s)


def main():
    tested = 0
    bad = []
    band = [0, 0]
    for n in (5, 6):
        for p in (1, 2):
            for r in (1, 2):
                if p + r > n:
                    continue
                for seed in range(3000, 3010):
                    made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
                    if made is None:
                        continue
                    A, C, L0 = made
                    clo = len(OC.closure(A, C, L0))
                    batch = [OC.closure(A, C, L0)]
                    for qq in range(clo, min(n, clo + 2) + 1):
                        batch += OC.sample_chains(A, C, L0, qq, 6, seed * 13 + qq)
                    seen = set()
                    for L in batch:
                        key = tuple(tuple(str(x) for x in row) for row in L)
                        if key in seen:
                            continue
                        seen.add(key)
                        tested += 1
                        res, info = check(A, C, L)
                        for name, good, pair in res:
                            if not good:
                                bad.append((n, p, r, seed, name, pair, info))
                        if info['h'] >= info['q'] + info['r1']:
                            band[0] += 1
                            if info['d_fin'] == 0:
                                band[1] += 1
    print(f'测试铅笔 {tested} 个')
    print(f'不通过的断言：{len(bad)}')
    for b in bad[:5]:
        print('  ', b)
    print(f'B.9 的触发次数（h≥q+r1）：{band[0]}；其中 d_fin=0 的（反例）：{band[1]}')
    assert not bad, '引理或推论在样本上不成立'
    print('✓ 全部断言通过（零指数计数、非零计数、Σε=s-d_fin、B.9）')


if __name__ == '__main__':
    main()
