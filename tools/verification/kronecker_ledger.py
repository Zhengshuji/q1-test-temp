r"""【结论：**未定论**】核对 Kronecker 记账恒等式与 $(5b)\iff d_{\rm fin}=0$（专家第五轮 §3.1(6) 的待核项）。

对每个**可容许**实例（满足 (5a)）计算：
  h        = 观测器铅笔 Q_L(λ) 的法秩（= 全 λ 的最大秩）
  rkL      = rank L
  d_fin    = Smith 不变因子中非常数者的次数和（有限初等因子总次数）
  d_inf    = 反转铅笔 Q_rev(μ) 的同一量（无穷初等因子总次数）
  右指标    = b - h - d_fin（Smith 形的列数减秩减有限次数；右最小指标次数和的等价算法）
然后检验：
  (I1)  h = d_fin + d_inf + 右指标次数和 ?
  (I2)  (5b) ⇔ d_fin = 0 ?
  (I3)  d_inf = h - rkL ?
并报告 (5b)（用 spectral_gcd 的极大子式 gcd 判定）与 d_fin 的一致性。

精确有理算术；有限实例检验。

**首轮运行结果（不可用）**：对 n=4 的**方阵**铅笔（q+2p=4）得到 d_fin=2、d_inf=4，
而正则 4×4 一次铅笔应有 d_fin+d_inf=4 —— 6 ≠ 4，说明**反转铅笔的构造或 Smith 实现的约定至少有一处不对**。
在修正之前，本脚本的输出不能用来判定会计恒等式；`spectral_gcd` 也未返回 `fail` 键（判据未被调用）。
**标定结果（`tools/verification/smith_calibrate.py`）**：Smith 实现在两个已知例上**通过**
（diag(λ,1) → $d_{\rm fin}=1$、$d_{\rm inf}=1$；[λ 1] → $d_{\rm fin}=0$）。
所以偏差**不在 Smith 实现**，而在"反转铅笔"这一步：对**行块次数不一致**的铅笔，
$\mu Q(1/\mu)$ 型的反转不保持 $d_{\rm fin}+d_\infty=h$；正确做法须用**齐次化**
$Q(\alpha,\beta)=\alpha Q_1+\beta Q_0$ 并在 $\mathbb P^1$ 上算不变因子。
**结论**：本脚本在改用齐次化之前，其 $d_{\rm inf}$ 列不可用。

**附加疑点（未解决）**：首轮打印的 8 行**完全相同**（$h=4$、$d_{\rm fin}=2$、$d_{\rm inf}=4$），
这在随机实例上不合理，提示脚本里还有别的 bug（很可能是 `pencil()` 的行块顺序或
`smith_invariants` 对矩形输入的处理）。**在修好之前不要引用本脚本的任何数字。**
"""

import os
import sys
import random
from fractions import Fraction as Fr

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ            # noqa: E402
import spectral_gcd as SG        # noqa: E402
import poly_smith as PS          # noqa: E402

F = Fr


def pencil(A, C, L):
    """Q_λ = [λL − LA; CA; C]，元素为多项式（系数列表，c0 + c1 λ）。"""
    n = len(A)
    LA = LQ.mul(L, A)
    CA = LQ.mul(C, A)
    rows = []
    for i in range(len(L)):
        rows.append([SG.ptrim([-LA[i][j], L[i][j]]) for j in range(n)])
    for i in range(len(CA)):
        rows.append([SG.ptrim([CA[i][j]]) for j in range(n)])
    for i in range(len(C)):
        rows.append([SG.ptrim([C[i][j]]) for j in range(n)])
    return rows


def rev_pencil(A, C, L):
    """反转铅笔（μ 变量）：[L − μ LA; μCA; μC]。"""
    n = len(A)
    LA = LQ.mul(L, A)
    CA = LQ.mul(C, A)
    rows = []
    for i in range(len(L)):
        rows.append([SG.ptrim([L[i][j], -LA[i][j]]) for j in range(n)])
    for i in range(len(CA)):
        rows.append([SG.ptrim([F(0), CA[i][j]]) for j in range(n)])
    for i in range(len(C)):
        rows.append([SG.ptrim([F(0), C[i][j]]) for j in range(n)])
    return rows


def normal_rank(Q):
    """法秩：Smith 不变因子个数（非零不变因子数）。"""
    inv = PS.smith_invariants(Q)
    return len(inv)


def dfin(Q):
    inv = PS.smith_invariants(Q)
    return sum(SG.pdeg(d) for d in inv), inv


def admissible(A, C, L):
    LA, CA = LQ.mul(L, A), LQ.mul(C, A)
    big = [r[:] for r in LA] + [r[:] for r in L] + [r[:] for r in CA] + [r[:] for r in C]
    small = [r[:] for r in L] + [r[:] for r in CA] + [r[:] for r in C]
    return LQ.rank(big) == LQ.rank(small)


def main():
    rng = random.Random(20261111)
    n, p, q, r = 4, 1, 2, 1
    cnt = {'adm': 0, 'I1': 0, 'I2': 0, 'I3': 0, 'fiveb': 0, 'dfin0': 0}
    rows = []
    for _ in range(60):
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        L = [row[:] for row in L0] + [[F(rng.randrange(-2, 3)) for _ in range(n)]
                                      for _ in range(q - r)]
        if not admissible(A, C, L):
            continue
        cnt['adm'] += 1
        Q = pencil(A, C, L)
        h = normal_rank(Q)
        dfin_v, inv = dfin(Q)
        Qr = rev_pencil(A, C, L)
        dinf_v, invr = dfin(Qr)
        rkL = LQ.rank(L)
        try:
            res = SG.spectral_gcd(A, C, L, verbose=False)
            fiveb_holds = (res.get('fail') is False) if isinstance(res, dict) else None
        except Exception:
            fiveb_holds = None
        # 右指标次数和：Smith 形的列数 − 秩 − 有限次数
        cols = len(Q[0])
        right_deg = cols - h - dfin_v
        i1 = (h == dfin_v + dinf_v + right_deg)
        i2 = (fiveb_holds == (dfin_v == 0)) if fiveb_holds is not None else None
        i3 = (dinf_v == h - rkL)
        cnt['I1'] += 1 if i1 else 0
        cnt['I2'] += 1 if i2 else 0
        cnt['I3'] += 1 if i3 else 0
        cnt['fiveb'] += 1 if fiveb_holds else 0
        cnt['dfin0'] += 1 if dfin_v == 0 else 0
        rows.append((h, rkL, dfin_v, dinf_v, right_deg, fiveb_holds, i1, i2, i3))
    print('可容许实例:', cnt['adm'])
    print('  满足 (5b):', cnt['fiveb'], '   d_fin=0:', cnt['dfin0'])
    print('  I1  h = d_fin + d_inf + 右指标:', cnt['I1'], '/', cnt['adm'])
    print('  I2  (5b) ⇔ d_fin=0:', cnt['I2'], '/', cnt['adm'])
    print('  I3  d_inf = h − rank L:', cnt['I3'], '/', cnt['adm'])
    print('  前 8 行 (h, rankL, d_fin, d_inf, 右, (5b), I1, I2, I3):')
    for t in rows[:8]:
        print('   ', t)


if __name__ == '__main__':
    main()
