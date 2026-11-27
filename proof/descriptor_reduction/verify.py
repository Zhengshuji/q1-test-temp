"""descriptor_pencil.py —— 约化 descriptor 铅笔 $R(\\lambda)$（专家 2026-11-02 §4）

给定 $(A,C,L)$（$L$ 满足 $(5a)$），构造专家给出的约化铅笔
$$R(\\lambda)=J\\,D(\\lambda)^{\\mathsf T}=[\\lambda E-E X^{\\mathsf T}\\ \\ B],$$
其中 $H=[L;CA;C]$、$J$ 取 $H$ 的 $h$ 个独立行（$\\ker J=\\ker H^{\\mathsf T}$）、
$D(\\lambda)=\\operatorname{diag}(\\lambda I_q-X,I_p,I_p)$、$J=[J_1\\ J_2\\ J_3]$、$E=J_1$、$B=[J_2\\ J_3]$。

**要核对的引理**（专家 §4.1）：$R$ 的**右**最小指标 = $Q_L$ 的**左**最小指标。

用法：python tools/verification/descriptor_pencil.py
"""

import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import linalg_q as LQ                     # noqa: E402
import kronecker_pencil as KP             # noqa: E402
import observer_pencils as OP             # noqa: E402
import modJ_candidates as MJ              # noqa: E402
import kron_sweep as KS                   # noqa: E402
from find_layer_instance import make_instance  # noqa: E402

F = Fraction


def solve_lc(rows, target):
    """把 target 写成 rows 的线性组合（返回系数），失败返回 None。"""
    m, n = len(rows), len(rows[0])
    aug = [[rows[i][j] for i in range(m)] + [target[j]] for j in range(n)]
    R, piv = LQ.rref(aug)
    for row in R:
        if all(row[i] == 0 for i in range(m)) and row[m] != 0:
            return None
    c = [F(0)] * m
    for i, p in enumerate(piv):
        if p < m:
            c[p] = R[i][m]
    return c


def decomposition(A, C, L):
    """$LA=XL+Y_1CA+Y_2C$；返回 (X, Y1, Y2)，不存在返回 None。"""
    q, p = len(L), len(C)
    CA = LQ.mul(C, A)
    H = [row[:] for row in L] + [row[:] for row in CA] + [row[:] for row in C]
    LA = LQ.mul(L, A)
    X = [[F(0)] * q for _ in range(q)]
    Y1 = [[F(0)] * p for _ in range(q)]
    Y2 = [[F(0)] * p for _ in range(q)]
    for i in range(q):
        c = solve_lc(H, LA[i])
        if c is None:
            return None
        for j in range(q):
            X[i][j] = c[j]
        for j in range(p):
            Y1[i][j] = c[q + j]
            Y2[i][j] = c[q + p + j]
    return X, Y1, Y2


def row_basis(rows):
    out = []
    for r in rows:
        if LQ.rank(out + [r]) > len(out):
            out.append(list(r))
    return out


def descriptor_pencil(A, C, L):
    """返回 (P0, P1, meta)：$R(\\lambda)=P_0+\\lambda P_1$ 以及 $E,B,J$。"""
    q, p, n = len(L), len(C), len(A)
    CA = LQ.mul(C, A)
    H = [row[:] for row in L] + [row[:] for row in CA] + [row[:] for row in C]
    # 专家 §4.1：取 H^T 的 h 个独立**行**（即 H 的 h 个独立**列**）作为 J
    Ht = [[H[i][j] for i in range(len(H))] for j in range(n)]
    J = row_basis(Ht)
    h = len(J)
    dec = decomposition(A, C, L)
    assert dec is not None, '(5a) 应保证分解存在'
    X, _, _ = dec
    J1 = [row[:q] for row in J]
    B = [row[q:] for row in J]
    # R = [lambda E - E X^T, B]
    EXt = LQ.mul(J1, [[X[i][j] for i in range(q)] for j in range(q)])
    P0 = [[-EXt[i][j] for j in range(q)] + [B[i][j] for j in range(2 * p)] for i in range(h)]
    P1 = [J1[i][:] + [F(0)] * (2 * p) for i in range(h)]
    assert len(P0) == h and len(P0[0]) == q + 2 * p
    return P0, P1, dict(J=J, E=J1, B=B, h=h, rankE=LQ.rank(J1))


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
    tested = bad = 0
    samples = []
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
                P0, P1, meta = descriptor_pencil(A, C, L)
                kR = KP.pencil_kronecker(P0, P1)
                Q0, Q1, h = OP.pencil_from_L(A, C, L)
                kQ = KP.pencil_kronecker(Q0, Q1)
                etaR = kR['right_min_indices']
                epsQ = kQ['left_min_indices']
                assert meta['rankE'] == LQ.rank(L), 'rank E 应等于 rank L'
                if etaR != epsQ:
                    bad += 1
                    print(f'  **不一致** n={n} seed={seed} q={len(L)}: '
                          f'eta(R)={etaR} vs eps(Q_L)={epsQ}')
                elif len(samples) < 5:
                    samples.append((n, seed, len(L), etaR, epsQ, meta['rankE'], meta['h']))
    print(f'\n核对 {tested} 个铅笔')
    for s in samples:
        print(f'  样本 n={s[0]} seed={s[1]} q={s[2]}: eta(R)={s[3]} = eps(Q_L)={s[4]}'
              f'（rank E=rank L={s[5]}, h={s[6]}）')
    print(f'不一致：{bad} 个')
    assert bad == 0, '引理在样本上不成立'
    print('✓ 引理："R 的右最小指标 = Q_L 的左最小指标"在全部样本上成立（验证不是证明）')


if __name__ == '__main__':
    main()
