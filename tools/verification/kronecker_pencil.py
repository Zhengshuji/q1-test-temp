"""kronecker_pencil.py —— 矩阵铅笔的 Kronecker 结构（精确有理算术）

用途（Workstream B，专家 2026-11-02）：
    给定线性铅笔 L(λ)=P0+λP1（P0,P1 为有理矩阵），算出它的 **Kronecker 数据**：

      normal_rank         一般位置秩
      finite_divisors     有限初等因子（正则部分的 Smith 不变因子，按次数与首一多项式给出）
      infinite_divisors   无穷初等因子（把铅笔反转为 P0+μP1 后的 Smith 数据）
      right_min_indices   右最小指标 η（满列秩缺失的方向）
      left_min_indices    左最小指标 ε

算法（全部精确、无浮点）：
  * normal rank 与初等因子：`poly_smith.smith_invariants`（ℚ[λ] 上的 Smith 形）。
  * 最小指标：**按次数截断的线性代数**（不碰多项式算术）——
    设 $n_d$ = "次数 ≤ d 的多项式零向量空间"的维数。构造块矩阵
    (d+2)m × (d+1)n，第 k 块行放 $P_0x_k+P_1x_{k-1}=0$，则 $n_d=\\dim\\ker$。
    于是 $k_d:=n_d-n_{d-1}=\\#\\{i:\\eta_i\\ge d\\}$，故 $\\#\\{\\eta_i=d\\}=k_d-k_{d+1}$。
    左最小指标对转置铅笔做同样计算。
  * 交叉校验（进入即断言）：$\\#\\{\\eta_i\\}=n-$normal_rank，$\\#\\{\\varepsilon_i\\}=m-$normal_rank。

**不做**：主元/符号规范形（我们用不到），也不做数值稳定的 QR 版本。

用法：
    python tools/verification/kronecker_pencil.py --selftest
"""

import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import linalg_q as LQ                     # noqa: E402
import poly_smith as PS                   # noqa: E402
import spectral_gcd as SG                 # noqa: E402

ptrim = SG.ptrim
pdeg = SG.pdeg


def _pzero(p):
    return ptrim(list(p)) == [Fraction(0)]


# ---------------------------------------------------------------- Smith 数据


def _pencil_poly_rows(P0, P1):
    """把 P0+λP1 写成 poly_smith 需要的"系数列表行"（低次在前）。"""
    m, n = len(P0), len(P0[0]) if P0 else 0
    Q = []
    for i in range(m):
        row = []
        for j in range(n):
            c = [Fraction(P0[i][j]), Fraction(P1[i][j])]
            # trim 掉末尾零（但保留至少一个）
            while len(c) > 1 and c[-1] == 0:
                c.pop()
            row.append(c)
        Q.append(row)
    return Q


def smith_invariants_of_pencil(P0, P1):
    """铅笔的 Smith 不变因子（首一多项式，系数列表）。"""
    if not P0 or not P0[0]:
        return []
    Q = _pencil_poly_rows(P0, P1)
    return PS.smith_invariants(Q)


def mu_valuation(p):
    r"""$\mu$-adic 赋值：$p$ 作为 $\mu$ 的多项式，常数项为零的最高前缀长度。

    这是**无穷初等因子的次数**所依据的量：反转铅笔 $Q_1+\mu Q_0$ 的不变因子在 $\mu=0$ 处的阶。"""
    p = ptrim(list(p))
    v = 0
    for c in p:
        if c == 0:
            v += 1
        else:
            break
    return v


def normal_rank(P0, P1):
    """一般位置秩 = 非零 Smith 不变因子的个数（精确）。"""
    inv = smith_invariants_of_pencil(P0, P1)
    return len([d for d in inv if not _pzero(d)])


# ---------------------------------------------------------------- 最小指标


def _kernel_dims(P0, P1, D):
    """返回 [n_0, n_1, ..., n_D]：n_d = 次数 ≤ d 的多项式零向量空间维数。"""
    m = len(P0)
    n = len(P0[0]) if m else 0
    assert all(len(row) == n for row in P0), 'P0 行宽不一致'
    assert len(P1) == m and all(len(row) == n for row in P1), 'P1 与 P0 尺寸不一致'
    out = []
    for d in range(D + 1):
        rows = (d + 2) * m
        cols = (d + 1) * n
        M = [[Fraction(0)] * cols for _ in range(rows)]
        for k in range(d + 2):
            for j in range(d + 1):
                base_r = k * m
                base_c = j * n
                if j == k:          # P0 作用在 x_k 上
                    for i in range(m):
                        for t in range(n):
                            M[base_r + i][base_c + t] = P0[i][t]
                if j == k - 1:      # P1 作用在 x_{k-1} 上
                    for i in range(m):
                        for t in range(n):
                            M[base_r + i][base_c + t] += P1[i][t]
        out.append(cols - LQ.rank(M))
    return out


def _indices_from_dims(dims):
    r"""由 $n_d$ 序列恢复最小指标（降序）。

    正确关系：$n_d=\sum_{i:\eta_i\le d}(d-\eta_i+1)$，
    故 $k_d:=n_d-n_{d-1}=\#\{i:\eta_i\le d\}$（单调不减），且 $\#\{\eta_i=d\}=k_d-k_{d-1}$。
    """
    ks = []
    prev = 0
    for nd in dims:
        ks.append(nd - prev)
        prev = nd
    out = []
    prevk = 0
    for d in range(len(dims)):
        cnt = ks[d] - prevk
        prevk = ks[d]
        assert cnt >= 0, f'最小指标个数为负（d={d}）：{cnt}'
        out.extend([d] * cnt)
    return sorted(out, reverse=True)


def minimal_indices(P0, P1, r=None, max_degree=None):
    r"""右最小指标的**自适应**计算：逐步加大次数 $d$，直到 $k_d=n-r$（全部指标已出现）。

    $r$ = normal rank（不给就现算）。返回 `(indices, stable)`。
    """
    m = len(P0)
    n = len(P0[0]) if m else 0
    if r is None:
        r = normal_rank(P0, P1)
    total = n - r
    if total == 0:
        return [], True
    Dmax = max_degree if max_degree is not None else max(6, n + 2)
    dims = []
    prev = 0
    for d in range(Dmax + 1):
        nd = _kernel_dims(P0, P1, d)[-1]   # 只算到 d（小规模，够快）
        dims.append(nd)
        kd = nd - prev
        prev = nd
        if kd == total:                    # 全部指标已出现 ⟹ 稳定
            return _indices_from_dims(dims), True
    return _indices_from_dims(dims), False


def transpose(M):
    return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))] if M and M[0] else []


# ---------------------------------------------------------------- 主入口


def pencil_kronecker(P0, P1, max_degree=None):
    """返回铅笔的 Kronecker 数据 dict（含交叉校验）。"""
    m = len(P0)
    n = len(P0[0]) if m else 0
    assert m > 0 and n > 0, '空铅笔'
    r = normal_rank(P0, P1)
    inv = smith_invariants_of_pencil(P0, P1)
    finite = [dict(degree=pdeg(d), poly=[str(x) for x in d]) for d in inv if not _pzero(d)]
    # 反转铅笔：无穷初等因子 = 反转后铅笔在 μ=0 处的结构
    inv_rev = smith_invariants_of_pencil(P1, P0)
    infinite = [dict(degree=pdeg(d), mu_valuation=mu_valuation(d), poly=[str(x) for x in d])
                for d in inv_rev if not _pzero(d)]
    # **无穷初等因子的总次数** = 反转铅笔不变因子在 mu=0 处的总阶（不是多项式次数！）
    d_infinity = sum(mu_valuation(d) for d in inv_rev if not _pzero(d))

    eta, eta_ok = minimal_indices(P0, P1, r, max_degree)
    eps, eps_ok = minimal_indices(transpose(P0), transpose(P1), r, max_degree)

    assert len(eta) == n - r, f'右最小指标个数 {len(eta)} != n-r = {n - r}'
    assert len(eps) == m - r, f'左最小指标个数 {len(eps)} != m-r = {m - r}'

    # ---- 全局恒等式（专家 2026-11-02 §3，补全文献）----------------------------
    #   sum_i eta_i + sum_j eps_j + sum_k deg(gamma_k) = normal_rank
    # 其中 sum_k deg(gamma_k) = (有限不变因子的次数和) + (反转铅笔不变因子的次数和)。
    # 这条恒等式对**任何**铅笔都成立，是本模块实现的强自检。
    # 注意（2026-11-02，专家复核后的更正）：
    #   完整的恒等式是 sum(eta) + sum(eps) + sum_k deg(gamma_k) = r，其中 gamma_k 是**齐次**不变因子，
    #   本模块**没有**直接计算 deg(gamma_k)；
    #   "sum(fin deg) + sum(inf deg)" 只是代理量，**一般不等于** sum deg(gamma_k)（反例见
    #   tools/verification/kron_identity_probe.py）。因此这里**不**对一般铅笔断言。
    #   但在 (5b) 型（**没有有限初等因子**）时，deg(gamma_k) 全部由无穷部分贡献，于是有可核对的特例：
    #       sum(eta) + sum(eps) + sum(inf deg) = r     （专家 2026-11-02 的式 (2)）
    sum_fin = sum(d['degree'] for d in finite)
    lhs = sum(eta) + sum(eps) + d_infinity
    if all(pdeg(d) == 0 for d in inv if not _pzero(d)):
        assert lhs == r, (f'(5b) 型恒等式失败: sum(eta)={sum(eta)} + sum(eps)={sum(eps)}'
                          f' + d_inf={d_infinity} = {lhs} != normal_rank {r}')

    # "无有限初等因子" ⟺ 全部非零不变因子是常数（即 (5b) 型的判据）
    no_finite = all(pdeg(d) == 0 for d in inv if not _pzero(d))
    return dict(
        shape=(m, n),
        normal_rank=r,
        finite_divisors=finite,
        infinite_divisors=infinite,
        right_min_indices=eta,
        left_min_indices=eps,
        right_stable=eta_ok,
        left_stable=eps_ok,
        no_finite_elementary_divisors=no_finite,
        d_infinity=d_infinity,
        identity_lhs=lhs,
    )


def summary(k):
    """人类可读的一行摘要。"""
    return (f'{k["shape"][0]}x{k["shape"][1]} rank={k["normal_rank"]} '
            f'fin={[d["degree"] for d in k["finite_divisors"]]} '
            f'inf={[d["degree"] for d in k["infinite_divisors"]]} d_inf={k["d_infinity"]} '
            f'eta={k["right_min_indices"]} eps={k["left_min_indices"]} '
            f'no_fin={k["no_finite_elementary_divisors"]}')


# ---------------------------------------------------------------- 自检


def _block_zeros(m, n):
    return [[Fraction(0)] * n for _ in range(m)]


def _block_L(k):
    """右奇异块 L_k（k × (k+1)）：第 i 行 λ 在第 i 列、1 在第 i+1 列。"""
    P0 = _block_zeros(k, k + 1)
    P1 = _block_zeros(k, k + 1)
    for i in range(k):
        P0[i][i + 1] = Fraction(1)
        P1[i][i] = Fraction(1)
    return P0, P1


def _block_Jk(alpha, k):
    """正则块 J_k(α)：P1 = I, P0 = αI - N（N 为下移一位的移位矩阵）。"""
    P0 = _block_zeros(k, k)
    P1 = _block_zeros(k, k)
    for i in range(k):
        P0[i][i] = Fraction(alpha)
        P1[i][i] = Fraction(1)
        if i + 1 < k:
            P0[i + 1][i] = Fraction(-1)
    return P0, P1


def _diag_blocks(blocks):
    """把若干 (P0,P1) 块拼成块对角。"""
    m = sum(len(b[0]) for b in blocks)
    n = sum(len(b[0][0]) if b[0] else 0 for b in blocks)
    P0 = _block_zeros(m, n)
    P1 = _block_zeros(m, n)
    r0 = c0 = 0
    for (A, B) in blocks:
        mm = len(A)
        nn = len(A[0]) if mm else 0
        for i in range(mm):
            for j in range(nn):
                P0[r0 + i][c0 + j] = A[i][j]
                P1[r0 + i][c0 + j] = B[i][j]
        r0 += mm
        c0 += nn
    return P0, P1


def selftest():
    ok = True

    def check(name, got, want):
        nonlocal ok
        good = (got == want)
        ok = ok and good
        print(f'  [{"OK" if good else "FAIL"}] {name}: got={got} want={want}')

    print('=== 标准块 ===')
    # L_2：右最小指标 2，normal rank 2，无有限初等因子
    P0, P1 = _block_L(2)
    k = pencil_kronecker(P0, P1)
    print('  L_2:', summary(k))
    check('L_2.rank', k['normal_rank'], 2)
    check('L_2.eta', k['right_min_indices'], [2])
    check('L_2.eps', k['left_min_indices'], [])

    # L_1^T：左最小指标 1
    _P0, _P1 = _block_L(1)
    P0t, P1t = transpose(_P0), transpose(_P1)
    k = pencil_kronecker(P0t, P1t)
    print('  L_1^T:', summary(k))
    check('L_1^T.eps', k['left_min_indices'], [1])
    check('L_1^T.eta', k['right_min_indices'], [])

    # J_2(0)：正则，有限初等因子 λ^2
    P0, P1 = _block_Jk(0, 2)
    k = pencil_kronecker(P0, P1)
    print('  J_2(0):', summary(k))
    check('J_2.rank', k['normal_rank'], 2)
    check('J_2.no_fin', k['no_finite_elementary_divisors'], False)
    check('J_2.eta', k['right_min_indices'], [])
    check('J_2.eps', k['left_min_indices'], [])

    # 零块 1x1 与 L_1 的直和：rank 1；右指标 [1,0]（零块贡献一个 0 指标），左指标 [0]
    P0, P1 = _diag_blocks([_block_L(1), (_block_zeros(1, 1), _block_zeros(1, 1))])
    k = pencil_kronecker(P0, P1)
    print('  L_1 ⊕ 0:', summary(k))
    check('L_1+0.rank', k['normal_rank'], 1)
    check('L_1+0.eta', k['right_min_indices'], [1, 0])
    check('L_1+0.eps', k['left_min_indices'], [0])

    # 常值可逆铅笔（P0=I, P1=0）：无有限初等因子
    P0 = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    P1 = _block_zeros(2, 2)
    k = pencil_kronecker(P0, P1)
    print('  I（常数）:', summary(k))
    check('I.no_fin', k['no_finite_elementary_divisors'], True)
    check('I.rank', k['normal_rank'], 2)

    # λI_2：在 λ=0 处秩降 ⟹ **有**有限初等因子（对照项）
    P0 = _block_zeros(2, 2)
    P1 = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    k = pencil_kronecker(P0, P1)
    print('  λI_2（对照，应**有**有限初等因子）:', summary(k))
    check('λI_2.no_fin', k['no_finite_elementary_divisors'], False)
    check('λI_2.rank', k['normal_rank'], 2)

    print('\n自检', '通过' if ok else '**失败**')
    return 0 if ok else 1


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    print(__doc__)
