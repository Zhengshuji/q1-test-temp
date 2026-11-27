"""observer_pencils.py —— 从实例与候选 L 构造**观测器铅笔**，并给出它的 Kronecker 数据

背景（Workstream B）：docs/02 B.1 的铅笔是
    $$Q_L(\\lambda)=[\\lambda L-LA;\\ CA;\\ C]\\quad((q+2p)\\times n).$$
对给定的 $L$（$q\\times n$、$\\operatorname{row}L_0\\subseteq\\operatorname{row}L$、满足 $(5a)$），
这就是**真实的观测器铅笔**（不是"随便挑的铅笔"）。(5b) $\\iff$ 该铅笔的秩恒为 $h=\\operatorname{rank}[L;CA;C]$。

本文件提供：
  * `pencil_from_L`      ：(A,C,L) -> (P0,P1) 与 $h$；
  * `observer_pencil`    ：再调用 `kronecker_pencil.pencil_kronecker` 得到 Kronecker 数据；
  * `candidate_Ls`       ：枚举/抽样满足 $\\operatorname{row}L_0\\subseteq\\operatorname{row}L$ 与 $(5a)$ 的候选 $L$；
  * `crosscheck`         ：与"独立路径"核对 —— 方阵时用 det 的次数，任意时用采样秩（`linalg_q.S_holds`）。

谨慎：`crosscheck` 的采样方向只能**反驳**（若采样到秩降，则 $\\operatorname{no\\_fin}$ 必须为 False）。
"""

import os
import random
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import linalg_q as LQ                     # noqa: E402
import poly_smith as PS                   # noqa: E402
import spectral_gcd as SG                 # noqa: E402
import kronecker_pencil as KP             # noqa: E402

F = Fraction


def _zeros(m, n):
    return [[F(0)] * n for _ in range(m)]


def pencil_from_L(A, C, L):
    """$Q_L(\\lambda)=[\\lambda L-LA;CA;C]$；返回 (P0, P1, h)。"""
    n = len(A)
    p = len(C)
    assert len(L[0]) == n, 'L 的列数必须等于 n'
    LA = LQ.mul(L, A)
    CA = LQ.mul(C, A)
    P1 = [row[:] for row in L] + _zeros(p, n) + _zeros(p, n)
    P0 = [[-LA[i][j] for j in range(n)] for i in range(len(L))] + \
         [[CA[i][j] for j in range(n)] for i in range(p)] + \
         [[C[i][j] for j in range(n)] for i in range(p)]
    h = LQ.rank(LQ.stack(L, CA, C))
    assert len(P0) == len(P1) and len(P0[0]) == n
    return P0, P1, h


def observer_pencil(A, C, L):
    """铅笔的 Kronecker 数据 + 元信息（含 (5a)/(5b) 判定）。"""
    P0, P1, h = pencil_from_L(A, C, L)
    k = KP.pencil_kronecker(P0, P1)
    assert k['normal_rank'] == h, (f'Kronecker 的 normal rank {k["normal_rank"]} != h = rank[L;CA;C] = {h}'
                                 '（这通常意味着 (5a) 失败：铅笔的一般秩超过了 [L;CA;C] 的秩）')
    return dict(
        kron=k,
        h=h,
        rows=len(P0), cols=len(P0[0]),
        condA=LQ.condA(A, C, L),
        five_b=(k['normal_rank'] == h and k['no_finite_elementary_divisors']),
    )


def crosscheck(A, C, L, info, lams=None):
    """独立路径核对；返回 (ok, msg)。

    * 方阵（q+2p == n）：用 det 的次数（SG.pdet）——det 是常数 ⟺ 无有限初等因子；
    * 否则：用采样秩 `LQ.S_holds`（**只能反驳**）。
    """
    P0, P1, h = pencil_from_L(A, C, L)
    nf = info['kron']['no_finite_elementary_divisors']
    # (i) 方阵且 det ≢ 0：det 是常数 ⟺ 无有限初等因子（独立路径）
    if len(P0) == len(P0[0]):
        Q = KP._pencil_poly_rows(P0, P1)
        d = SG.pdet(Q)
        if SG.pdeg(d) >= 0:   # det ≢ 0（正则方阵）
            det_const = (SG.pdeg(d) == 0)
            ok = (det_const == nf)
            return ok, f'正则方阵：det 次数={SG.pdeg(d)} ⟺ no_fin={nf}'
        # det ≡ 0（奇异方阵）⟹ 退化为采样
    # (ii) 采样：若某 λ 处秩降，则 no_fin 必须 False
    lams = lams or [F(k) for k in range(-4, 5)] + [F(1, 2), F(-1, 2), F(1, 3), F(2, 3), F(5, 7)]
    bad = []
    for lam in lams:
        M = [[lam * P1[i][j] + P0[i][j] for j in range(len(P1[0]))] for i in range(len(P1))]
        if LQ.rank(M) < h:
            bad.append(lam)
            break
    if bad and nf:
        return False, f'采样在 λ={bad[0]} 发现秩降但 no_fin=True ⟹ 矛盾'
    if not bad and not nf:
        return True, '采样未发现秩降（根可能非有理）——不构成矛盾'
    return True, f'采样与 no_fin 一致（秩降点={bad}, no_fin={nf}）'


def _apply_row_A(A, row):
    """行向量右乘 A（等价于 A^T 作用在列上）。"""
    n = len(A)
    return [sum(row[i] * A[i][j] for i in range(n)) for j in range(n)]


def invariant_closure_rows(A, seed_rows):
    """最小的"对 x↦xA 不变"的行空间，含 seed_rows。"""
    U = LQ.rank(seed_rows) and [r[:] for r in LQ.nullspace(LQ.stack(seed_rows))] or []
    # 用 rref 直接取 seed_rows 的基
    U = []
    for r in seed_rows:
        if LQ.rank(U + [r]) > len(U):
            U.append(r[:])
    while True:
        ext = U + [_apply_row_A(A, u) for u in U]
        newU = []
        for r in ext:
            if LQ.rank(newU + [r]) > len(newU):
                newU.append(r)
        if len(newU) == len(U):
            return U
        U = newU
        assert len(U) <= len(A), '闭包维数超过 n（不可能）'


def candidate_Ls(A, C, L0, n_extra=1, trials=60, seed=0, require_condA=True):
    r"""产生满足 $(5a)$ 与 $\operatorname{row}L_0\subseteq\operatorname{row}L$ 的候选 $L$。

    做法：取"对 $x\mapsto xA$ 不变"且含 $\operatorname{row}L_0$ 的子空间 $\mathcal V$，
    其基即为 $L$ 的行（$\mathcal V A\subseteq\mathcal V\subseteq\mathcal V+\mathcal J$ ⟹ $(5a)$ 自动 ✓）。
    变体：在闭包里再加随机向量的不变闭包（得更大的 $\mathcal V$）。
    """
    rng = random.Random(seed)
    n = len(A)
    base = invariant_closure_rows(A, [r[:] for r in L0])
    yield [r[:] for r in base]
    for t in range(trials):
        extra = [[F(rng.choice([-1, 0, 1, 2])) for _ in range(n)] for _ in range(n_extra)]
        V = invariant_closure_rows(A, [r[:] for r in base] + extra)
        if require_condA and not LQ.condA(A, C, V):
            continue
        yield [r[:] for r in V]


def selftest():
    print('=== 自检：从真实实例构造铅笔 ===')
    sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))
    from find_layer_instance import make_instance
    A, C, L0 = make_instance(6, 1002)
    print('  实例 seed=1002；L0 行数 =', len(L0))
    found = 0
    for L in candidate_Ls(A, C, L0, n_extra=1, trials=200, seed=7):
        info = observer_pencil(A, C, L)
        ok, msg = crosscheck(A, C, L, info)
        print(f'  q={len(L)} h={info["h"]} 5a={info["condA"]} 5b={info["five_b"]} | '
              f'{KP.summary(info["kron"])}')
        print(f'    交叉核对: {"OK" if ok else "FAIL"} — {msg}')
        assert ok, '交叉核对失败'
        found += 1
        if found >= 3:
            break
    if found == 0:
        print('  没有找到满足 (5a) 的候选 L（记录，不静默）')
    print('自检完成')


if __name__ == '__main__':
    selftest()
