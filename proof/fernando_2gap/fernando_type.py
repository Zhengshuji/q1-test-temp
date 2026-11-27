"""fernando_type.py —— 判定公开例子在 $q_0$ 与 $q_0+1$ 的失败是 Type I 还是 Type III

对公开例子（$n=8$、$p=r=2$、$r_1=4$、$q_0=3$）：设 $K=\\ker[C;L_0]$（$\\dim4$）、
$S=K^{\\perp}+W=\\operatorname{row}[C;L_0]+\\operatorname{row}[C;CA]$（$\\dim6$），商空间 $\\mathbb C^8/S\\cong\\mathbb C^2$。

对 $q=3$：$\\mathcal Z\\subseteq K$（$\\dim3$）⟹ $\\mathcal Z^{\\perp}=K^{\\perp}+\\operatorname{span}(v)$，$v\\notin K^{\\perp}$。
$(5a)$ 等价于 $(\\mathcal Z^{\\perp})A\\subseteq\\mathcal Z^{\\perp}+W=S+\\operatorname{span}(v)$。
在 $\\mathbb C^2$ 中：$\\operatorname{row}C$ 的像的类为 $0$，$\\operatorname{row}L_0$ 的像的类为 $c\\ne0$（两行同类）。
于是 $(5a)$ 迫使 $\\operatorname{class}(v)\\propto c\\ne0$，即 $v\\notin S$，从而
$$h=\\dim(S+\\operatorname{span}v)=6+1=7=q+r_1\\quad\\Longrightarrow\\quad\\textbf{Type I}.$$

本脚本：算类、解线性条件、给出**显式**的 $q_0$ 阶 $(5a)$-可行 $\\mathcal L$，并核验 $h=7$、$(5b)$ 失败。

用法：python proof/fernando_2gap/fernando_type.py
"""

import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import importlib.util as iu               # noqa: E402

F = Fraction


def load():
    spec = iu.spec_from_file_location('F2', os.path.join(_ROOT, 'proof', 'fernando_2gap', 'verify.py'))
    m = iu.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.A, m.C, m.L0


def rowspace(rows):
    out = []
    for r in rows:
        if LQ.rank(out + [r]) > len(out):
            out.append(list(r))
    return out


def complement(S, n):
    B = rowspace(S)
    Q = []
    for i in range(n):
        e = [F(1) if j == i else F(0) for j in range(n)]
        if LQ.rank(B + Q + [e]) > LQ.rank(B + Q):
            Q.append(e)
    return Q


def coords_Q(v, basis_S, Q):
    basis = [list(x) for x in basis_S] + [list(x) for x in Q]
    nn = len(basis)
    aug = [[basis[t][j] for t in range(nn)] + [v[j]] for j in range(nn)]
    R, piv = LQ.rref(aug)
    coef = [F(0)] * nn
    for ri, pc in enumerate(piv):
        if pc < nn:
            coef[pc] = R[ri][nn]
    return coef[len(basis_S):]


def main():
    A, C, L0 = load()
    n, p, r = len(A), len(C), len(L0)
    CA = LQ.mul(C, A)
    W = [x[:] for x in C] + [x[:] for x in CA]
    Kp = [x[:] for x in C] + [x[:] for x in L0]
    S = rowspace([x[:] for x in Kp] + [x[:] for x in W])
    Q = complement(S, n)
    print(f'n={n} p={p} r={r}  dim S={len(S)}  codim={len(Q)}')
    # 类
    cls = {}
    for name, rows in (('rowC', [x[:] for x in C]), ('rowL0', [x[:] for x in L0])):
        for b in rows:
            cls[(name, tuple(b))] = coords_Q(LQ.mul([b], A)[0], S, Q)
    c0 = cls[('rowL0', tuple(L0[0]))]
    c1 = cls[('rowL0', tuple(L0[1]))]
    print('  class(L0_1 · A) =', [str(x) for x in c0], ' class(L0_2 · A) =', [str(x) for x in c1])
    assert c0 == c1 and any(x != 0 for x in c0), '两行类应相同且非零'
    c = c0
    # 对每个标准基 e_j 算 class(e_j) 与 class(e_j A)（线性于 v 的系数）
    U = [coords_Q([F(1) if k == j else F(0) for k in range(n)], S, Q) for j in range(n)]
    V = [coords_Q(LQ.mul([[F(1) if k == j else F(0) for k in range(n)]], A)[0], S, Q) for j in range(n)]

    def cross2(a, b):
        return a[0] * b[1] - a[1] * b[0]

    # 条件：class(v) ∧ c = 0 与 class(vA) ∧ c = 0，均线性于 t
    eqs = []
    row1 = [cross2(U[j], c) for j in range(n)]
    eqs.append(row1)
    row2 = [cross2(V[j], c) for j in range(n)]
    eqs.append(row2)
    sols = [list(r) for r in LQ.nullspace(eqs)] if LQ.rank(eqs) > 0 else []
    print(f'  线性条件 rank={LQ.rank(eqs)}，解空间维数={len(sols)}（期望 6）')
    # 取一个解作为 v
    assert sols, '无解'
    v = sols[0]
    print('  v =', [str(x) for x in v])
    # Z^perp = K^perp + span(v)；Z = 它的正交补（dim 3）
    Zp = rowspace([x[:] for x in Kp] + [v])
    print('  dim Z^perp =', len(Zp), '（应 5）')
    Zb = [list(x) for x in LQ.nullspace(Zp)]     # Z = {z : Zp·z^T = 0}
    print('  dim Z =', len(Zb), '（应 3）')
    Z = [[Zb[i][j] for i in range(len(Zb))] for j in range(n)]     # n × 3（列）
    # 构造 L：row L = L0 + 一行，使 [C;L] = Z^perp
    L = [list(x) for x in L0]
    for b in Zp:
        if len(L) == 3:
            break
        if LQ.rank([list(x) for x in C] + L + [b]) > LQ.rank([list(x) for x in C] + L):
            L.append(b)
    assert len(L) == 3
    h = LQ.rank([x[:] for x in L] + [x[:] for x in CA] + [x[:] for x in C])
    cond = LQ.condA(A, C, L)
    res = TC.analyse(A, C, L)
    print(f'  显式 L（3 行）：')
    for row in L:
        print('   ', [str(x) for x in row])
    print(f'  (5a) = {cond}；h = {h}；q+r1 = {3 + LQ.rank(W)}；(5b) = {res["five_b"]}；'
          f'eps = {res["eps_smith"]}；d_fin = {res["d_fin"]}')
    assert cond and h == 3 + LQ.rank(W) == 7 and res['five_b'] is False
    print('\n✓ 公开例子在 q0=3 的失败是 **Type I**（h = q+r1 = 7），且给出了显式的 3 行可行增广')


if __name__ == '__main__':
    main()
