"""toeplitz_criterion.py —— 专家 2026-11-02 答复 §9 的"单 Toeplitz 矩阵判据"（WP1）

对约化 descriptor 铅笔 $R(\\lambda)=[\\lambda E-F\\ \\ B]$（$h\\times(q+2p)$），构造块 Toeplitz 矩阵
$T_d$（$h(d+2)\\times(q+2p)(d+1)$），它表示多项式方程 $R(\\lambda)y(\\lambda)=0$、$\\deg y\\le d$：

$$-F x_0+B u_0=0,\\qquad E x_{j-1}-F x_j+B u_j=0\\ (1\\le j\\le d),\\qquad E x_d=0 .$$

记 $\\nu_d=\\dim\\ker T_d$。若 $R$ 的右最小指标是 $\\varepsilon_1,\\dots,\\varepsilon_m$，则

$$\\nu_d=\\sum_{i=1}^{m}\\max\\{0,\\ d-\\varepsilon_i+1\\},\\qquad
\\#\\{i:\\varepsilon_i=d\\}=\\nu_d-2\\nu_{d-1}+\\nu_{d-2}\\ (\\nu_{-1}=\\nu_{-2}=0).$$

取 $s=\\operatorname{rank}\\mathcal L$（于是 $s\\ge\\max_i\\varepsilon_i$），得

$$\\boxed{\\ \\nu_s=(s+1)m-s\\iff d_{\\rm fin}=0\\iff(5b)\\ }$$

本脚本：
  1. 从 $(A,C,L)$ 构造 $R$，逐 $d$ 算 $\\nu_d$，用差分公式恢复 $\\varepsilon$；
  2. 与 Smith 路径（`kronecker_pencil` 的 `left_min_indices`）逐个比对；
  3. 核对 $(5b)\\iff\\nu_s=(s+1)m-s$（与 $d_{\\rm fin}=0$ 比对）；
  4. 在样本集上做交叉验证。

**验证不是证明**；判据的纸面证明见 [theorem.md](../../proof/toeplitz_criterion/theorem.md)。
"""

import os
import sys
from collections import Counter
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import linalg_q as LQ                     # noqa: E402
import kronecker_pencil as KP             # noqa: E402
import observer_pencils as OP             # noqa: E402
import descriptor_pencil as DP            # noqa: E402
import modJ_candidates as MJ              # noqa: E402
import kron_sweep as KS                   # noqa: E402
from find_layer_instance import make_instance  # noqa: E402

F = Fraction


def split_R(P0, P1, q):
    """从 $R=P_0+\\lambda P_1$ 取出 $(E,F,B)$：$P_1=[E\\ 0]$、$P_0=[-F\\ B]$。"""
    h = len(P0)
    E = [[P1[i][j] for j in range(q)] for i in range(h)]
    negF = [[P0[i][j] for j in range(q)] for i in range(h)]
    Fm = [[-negF[i][j] for j in range(q)] for i in range(h)]
    B = [[P0[i][q + j] for j in range(len(P0[0]) - q)] for i in range(h)]
    return E, Fm, B


def toeplitz(E, Fm, B, d):
    """块 Toeplitz 矩阵 $T_d$：第 $k$ 块行是 $P_0 v_k+P_1 v_{k-1}=0$（$P_0=[-F\ B]$、$P_1=[E\ 0]$）。

    即：$k=0$ 行只有 $-F x_0+B u_0$；$1\le k\le d$ 行是 $E x_{k-1}-F x_k+B u_k$；
    $k=d+1$ 行是 $E x_d$。
    """
    h = len(E)
    q = len(E[0])
    two_p = len(B[0]) if B and B[0] else 0
    step = q + two_p
    ncol = (d + 1) * step
    rows = []
    for k in range(d + 2):
        blk = [[F(0)] * ncol for _ in range(h)]
        for i in range(h):
            for t in range(step):
                if k <= d:
                    blk[i][k * step + t] = (-Fm[i][t]) if t < q else B[i][t - q]
                if k >= 1 and k - 1 <= d and t < q:
                    blk[i][(k - 1) * step + t] += E[i][t]
        rows += blk
    return rows


def toeplitz_nullities(E, Fm, B, dmax):
    out = []
    for d in range(dmax + 1):
        M = toeplitz(E, Fm, B, d)
        out.append(len(M[0]) - LQ.rank(M))
    return out


def recover_indices(nus):
    r"""$\#\{i:\varepsilon_i=d\}=\nu_d-2\nu_{d-1}+\nu_{d-2}$。"""
    out = []
    for d in range(len(nus)):
        v_d = nus[d]
        v_d1 = nus[d - 1] if d >= 1 else 0
        v_d2 = nus[d - 2] if d >= 2 else 0
        cnt = v_d - 2 * v_d1 + v_d2
        assert cnt >= 0, f'差分公式给出负数（d={d}）：{cnt}'
        out.extend([d] * cnt)
    return sorted(out, reverse=True)


def analyse(A, C, L, verbose=False):
    P0, P1, h = OP.pencil_from_L(A, C, L)
    q, p = len(L), len(C)
    kk = KP.pencil_kronecker(P0, P1)
    eps_smith = kk['left_min_indices']
    d_fin = sum(x['degree'] for x in kk['finite_divisors'])
    s = LQ.rank(L)
    m = q + 2 * p - h
    assert len(eps_smith) == m, f'左指标个数 {len(eps_smith)} != q+2p-h = {m}'
    assert sum(eps_smith) == s - d_fin, 'B.8 的等式不成立'
    # descriptor 铅笔与 Toeplitz
    Q0, Q1, meta = DP.descriptor_pencil(A, C, L)
    E, Fm, B = split_R(Q0, Q1, q)
    nus = toeplitz_nullities(E, Fm, B, s)
    eps_toep = recover_indices(nus)
    # 判据
    lhs = nus[s]
    rhs = (s + 1) * m - s
    five_b = (d_fin == 0)
    ok_crit = (lhs == rhs) == five_b
    if verbose:
        print(f'  q={q} p={p} h={h} s={s} m={m} d_fin={d_fin}')
        print(f'  eps(smith)={eps_smith}  eps(toeplitz)={eps_toep}')
        print(f'  nu_s={lhs}  (s+1)m-s={rhs}  (5b)={five_b}  判据一致={ok_crit}')
    return dict(q=q, p=p, h=h, s=s, m=m, d_fin=d_fin,
                eps_smith=eps_smith, eps_toep=eps_toep,
                nu_s=lhs, target=rhs, five_b=five_b,
                eps_agree=(eps_smith == eps_toep), crit_agree=ok_crit)


def candidates(A, C, L0, n, seed, trials=2):
    out = []
    CAk = [row[:] for row in C]
    for k in range(1, n + 1):
        out.append([row[:] for row in CAk])
        CAk = CAk + LQ.mul(C, KS._pow(A, k))
    try:
        out += list(OP.candidate_Ls(A, C, L0, n_extra=1, trials=trials, seed=seed))
    except AssertionError:
        pass
    try:
        out += list(MJ.candidate_Ls_modJ(A, C, L0, trials=trials, seed=seed))
    except AssertionError:
        pass
    return out


def main():
    print('=== 1. 单例演示 ===')
    A, C, L0 = make_instance(6, 1002)
    shown = 0
    for L in candidates(A, C, L0, 6, 1002):
        if not LQ.condA(A, C, L):
            continue
        analyse(A, C, L, verbose=True)
        shown += 1
        if shown >= 2:
            break

    print('\n=== 2. 样本集交叉验证 ===')
    tested = 0
    bad = []
    stats = Counter()
    for n in (6, 7, 8):
        for k in range(3):
            seed = 1000 + k
            A, C, L0 = make_instance(n, seed)
            seen = set()
            for L in candidates(A, C, L0, n, seed):
                key = tuple(tuple(str(x) for x in r) for r in L)
                if key in seen:
                    continue
                seen.add(key)
                if not LQ.condA(A, C, L):
                    continue
                tested += 1
                r = analyse(A, C, L)
                stats['crit' if r['crit_agree'] else 'crit_bad'] += 1
                stats['eps' if r['eps_agree'] else 'eps_bad'] += 1
                if not (r['crit_agree'] and r['eps_agree']):
                    bad.append((n, seed, len(L), r))
    print(f'  测试 {tested} 个铅笔：判据一致 {stats["crit"]}，不一致 {stats["crit_bad"]}；'
          f'序列一致 {stats["eps"]}，不一致 {stats["eps_bad"]}')
    for b in bad[:3]:
        print('  **不一致**', b)
    assert not bad, 'Toeplitz 判据与 Smith 路径不一致'
    print('\n✓ Toeplitz 判据（含序列恢复）与 Smith 路径在全部样本上一致')


if __name__ == '__main__':
    main()
