"""kron_layer_relation.py —— 原始铅笔 vs 商铅笔：到底是什么变换（专家 2026-11-02 §5）

三个铅笔：
  * **原始**：$Q_L(\\lambda)=[\\lambda L-LA;\\ CA;\\ C]$（$(q+2p)\\times n$，B.1 的陈述对象）；
  * **商铅笔**（docs/02 B.1）：$Q_{\\rm quot}(\\lambda)=\\lambda\\Pi-\\Pi T$（$q\\times d$，$\\Pi=\\pi(\\mathcal L)$ 的 $W$-坐标、$T$ 是诱导映射）；
  * **层铅笔**（c229）：$T_\\lambda=\\lambda\\iota-\\bar A:\\ \\mathcal V/S\\to\\ker C/Z$（更压缩，本脚本不构造）。

本脚本检验的性质：
  1. 秩恒等式 $\\operatorname{rank}Q_L(\\lambda)=j+\\operatorname{rank}Q_{\\rm quot}(\\lambda)$ 对一切 $\\lambda$（逐点精确 + 两端 normal rank）；
  2. 两者的 Kronecker 数据是否"只差 $j$"（若否，说明不是严格等价，不能直接搬不变量）。

结论形式：证据（精确），并给出"能搬/不能搬"的判定说明。
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
from find_layer_instance import make_instance  # noqa: E402

F = Fraction
LAMS = [F(k) for k in range(-5, 6)] + [F(1, 2), F(-1, 2), F(3, 2), F(2, 3), F(5, 7), F(7, 3)]


def row_basis(rows):
    out = []
    for r in rows:
        if LQ.rank(out + [r]) > len(out):
            out.append(list(r))
    return out


def complement(J, n):
    """把 J 的基补成 C^n 的一组基；返回 J 基与补空间 W 的基。"""
    Jb = row_basis(J)
    W = []
    for i in range(n):
        e = [F(1) if k == i else F(0) for k in range(n)]
        if LQ.rank(Jb + W + [e]) > len(Jb) + len(W):
            W.append(e)
        if len(W) == n - len(Jb):
            break
    return Jb, W


def project(x, Jb, W):
    """x = w + j（w ∈ span W, j ∈ span Jb）；返回 w 在 W 坐标下的系数。"""
    cols = [[W[i][t] for t in range(len(x))] for i in range(len(W))] + \
           [[Jb[i][t] for t in range(len(x))] for i in range(len(Jb))]
    k = len(cols)
    n = len(x)
    aug = [[cols[i][r] for i in range(k)] + [x[r]] for r in range(n)]
    R, piv = LQ.rref(aug)
    for row in R:
        if all(row[i] == 0 for i in range(k)) and row[k] != 0:
            raise AssertionError('x 不在 span(W) + span(J) 里')
    c = [F(0)] * k
    for i, p in enumerate(piv):
        if p < k:
            c[p] = R[i][k]
    return c[:len(W)]


def build(A, C, L):
    n = len(A)
    CA = LQ.mul(C, A)
    J = LQ.stack(C, CA)
    Jb, W = complement(J, n)
    d = len(W)
    # T: W -> W, T(w) = pi(wA)
    T = [[F(0)] * d for _ in range(d)]
    for j in range(d):
        w = W[j]
        wA = [sum(w[i] * A[i][t] for i in range(n)) for t in range(n)]
        c = project(wA, Jb, W)
        for i in range(d):
            T[i][j] = c[i]
    # Pi: q x d
    Pi = [[F(0)] * d for _ in range(len(L))]
    for i, ell in enumerate(L):
        c = project(list(ell), Jb, W)
        Pi[i] = c
    return dict(Jb=Jb, W=W, d=d, T=T, Pi=Pi, j=len(Jb), h=None)


def main():
    for seed in (1002, 1010):
        A, C, L0 = make_instance(6, seed)
        for L in OP.candidate_Ls(A, C, L0, n_extra=1, trials=4, seed=seed):
            if not LQ.condA(A, C, L):
                continue
            dat = build(A, C, L)
            P0, P1, h = OP.pencil_from_L(A, C, L)
            # 商铅笔：P1' = Pi, P0' = -Pi T
            PiT = LQ.mul(dat['Pi'], dat['T'])
            Q0 = [[-PiT[i][j] for j in range(dat['d'])] for i in range(len(L))]
            Q1 = [[dat['Pi'][i][j] for j in range(dat['d'])] for i in range(len(L))]
            # 1) 秩恒等式，逐点
            ok = True
            for lam in LAMS:
                M1 = [[lam * P1[i][j] + P0[i][j] for j in range(len(P1[0]))] for i in range(len(P1))]
                M2 = [[lam * Q1[i][j] + Q0[i][j] for j in range(len(Q1[0]))] for i in range(len(Q1))]
                if LQ.rank(M1) != dat['j'] + LQ.rank(M2):
                    ok = False
                    print(f'  秩恒等式在 λ={lam} 失败: {LQ.rank(M1)} != {dat["j"]}+{LQ.rank(M2)}')
                    break
            k1 = KP.pencil_kronecker(P0, P1)
            k2 = KP.pencil_kronecker(Q0, Q1)
            five_b = OP.observer_pencil(A, C, L)['five_b']
            print(f'\n[seed {seed}] q={len(L)} j={dat["j"]} d={dat["d"]} h={h} (5b)={five_b}')
            print(f'  秩恒等式 rank Q_L = j + rank Q_quot：{"全部通过" if ok else "**失败**"}（{len(LAMS)} 个 λ）')
            print(f'  原始: {KP.summary(k1)}   (shape {k1["shape"]})')
            print(f'  商  : {KP.summary(k2)}   (shape {k2["shape"]})')
            print(f'  → 右指标: 原 {k1["right_min_indices"]} vs 商 {k2["right_min_indices"]}'
                  f'；左指标: 原 {k1["left_min_indices"]} vs 商 {k2["left_min_indices"]}'
                  f'；有限因子次数: 原 {[x["degree"] for x in k1["finite_divisors"]]}'
                  f' vs 商 {[x["degree"] for x in k2["finite_divisors"]]}')
            assert ok, '秩恒等式失败'
            break


if __name__ == '__main__':
    main()
