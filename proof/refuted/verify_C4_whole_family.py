"""verify_C4_whole_family.py —— C4 实例在 $q_0$ 阶"整族不可行"的证书

两部分：

1. **$(5a)$ 自动**：$h=s_0+t=5+1=6=n$，故 $\\mathcal Z^{\\perp}+W=\\mathbb C^6$，任意 $\\mathcal Z$ 都满足 $(5a)$。
   抽样核验：$\\mathbb P(K)$ 上多条直线的 $(5a)$ 全为真。
2. **每个 $\\mathcal Z$ 都有掉秩 $\\lambda$**：映射 $x\\mapsto\\operatorname{span}z(x)$
   （$z(x)=(\\lambda(x)I-A)x$，$\\lambda(x)=L_0Ax/L_0x$）在 $\\mathbb P(V)$ 上**非常数**
   ⟹ 满射 ⟹ 每个 $\\mathcal Z$ 被某个 $x$ 命中 ⟹ 该 $\\mathcal Z$ 对应的 $\\mathcal L$ 在 $\\lambda(x)$ 处掉秩 ⟹ $(5b)$ 失败。

用法：python proof/refuted/verify_C4_whole_family.py
"""

import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import importlib.util as iu               # noqa: E402

F = Fraction


def main():
    spec = iu.spec_from_file_location('V4', os.path.join(_ROOT, 'proof', 'refuted', 'verify_C4_type3.py'))
    V4 = iu.module_from_spec(spec)
    spec.loader.exec_module(V4)
    A, C, L0, q0, _ = V4.build()
    n, p, r = len(A), len(C), len(L0)
    CA = LQ.mul(C, A)
    W = [x[:] for x in C] + [x[:] for x in CA]
    r1 = LQ.rank(W)
    S = [x[:] for x in C] + [x[:] for x in L0] + [x[:] for x in W]
    s0 = LQ.rank(S)
    t = q0 - r
    h_pred = s0 + min(t, n - s0)
    print(f'n={n} p={p} r={r} q0={q0} r1={r1} s0={s0} t={t} ⟹ h={h_pred}（应 = n = {n}）')
    assert h_pred == n, 'h 应等于 n'
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    assert len(V[0]) == 2 and len(K[0]) == 2, 'V 与 K 都应为 2 维'

    def vec(mat, coeff):
        m = len(mat[0])
        return [sum(coeff[j] * mat[i][j] for j in range(m)) for i in range(len(mat))]

    def rowspace(rows):
        out = []
        for r0 in rows:
            if LQ.rank(out + [r0]) > len(out):
                out.append(list(r0))
        return out

    def class_in_K(z):
        basis = [[K[i][j] for i in range(n)] for j in range(len(K[0]))]
        m = len(basis)
        aug = [[basis[j][tt] for j in range(m)] + [z[tt]] for tt in range(n)]
        R, piv = LQ.rref(aug)
        for row in R:
            if all(row[tt] == 0 for tt in range(m)) and row[m] != 0:
                return None
        c = [F(0)] * m
        for ri, pc in enumerate(piv):
            if pc < m:
                c[pc] = R[ri][m]
        return c

    print('\n=== 1. (5a) 自动：扫多条直线 ===')
    adm = 0
    total = 0
    for a in (F(1), F(2), F(-1), F(3), F(0)):
        for b in (F(1), F(-1), F(2)):
            v = [a * K[i][0] + b * K[i][1] for i in range(n)]
            Zp = rowspace([x[:] for x in C] + [x[:] for x in L0] + [v])
            if len(Zp) != p + q0:
                continue
            Zb = [list(x) for x in LQ.nullspace(Zp)]
            Z = [[Zb[i][j] for i in range(len(Zb))] for j in range(n)]
            L = ZG.L_from_Z(A, C, L0, Z, q0)
            if L is None:
                continue
            total += 1
            if LQ.condA(A, C, L):
                adm += 1
    print(f'  扫到 {total} 条直线，(5a) 成立 {adm} 条')
    assert adm == total > 0

    print('\n=== 2. 映射非常数 ===')
    images = []
    for tt in (F(0), F(1), F(2), F(-2), F(5)):
        x = vec(V, [F(1), tt])
        L0x = sum(L0[0][i] * x[i] for i in range(n))
        if L0x == 0:
            continue
        Ax = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]
        L0Ax = sum(L0[0][i] * Ax[i] for i in range(n))
        lam = L0Ax / L0x
        z = [lam * x[i] - Ax[i] for i in range(n)]
        cz = class_in_K(z)
        print(f'  t={tt}: λ={lam}，z 的 K-坐标={[str(v) for v in cz] if cz else None}')
        if cz and any(v != 0 for v in cz):
            images.append(tuple(str(v) for v in cz))
    assert len(set(images)) >= 2, '映射应非常数'
    print(f'  不同像 {len(set(images))} 个 ⟹ 映射非常数 ⟹ 满射 ⟹ 每个 Z 都有掉秩 λ')

    print('\n=== 3. 取一个由 z(x) 生成的 Z，验证掉秩与 (5b) 失败 ===')
    tt = F(0)
    x = vec(V, [F(1), tt])
    L0x = sum(L0[0][i] * x[i] for i in range(n))
    Ax = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]
    lam = sum(L0[0][i] * Ax[i] for i in range(n)) / L0x
    z = [lam * x[i] - Ax[i] for i in range(n)]
    assert all(v == 0 for v in [sum(C[j][i] * z[i] for i in range(n)) for j in range(p)])
    assert all(v == 0 for v in [sum(L0[j][i] * z[i] for i in range(n)) for j in range(r)])
    Z = [[z[i]] for i in range(n)]                 # Z = span(z)（n×1 列）
    L = ZG.L_from_Z(A, C, L0, Z, q0)
    assert L is not None and LQ.condA(A, C, L)
    h = LQ.rank([v[:] for v in L] + [v[:] for v in CA] + [v[:] for v in C])
    LA = LQ.mul(L, A)
    Qm = [[lam * L[i][j] - LA[i][j] for j in range(n)] for i in range(len(L))]
    Qm = Qm + [v[:] for v in CA] + [v[:] for v in C]
    rank_at = LQ.rank(Qm)
    res = TC.analyse(A, C, L)
    print(f'  (5a) ✓；h={h}；rank Q(λ)={rank_at} < h；d_fin={res["d_fin"]}；(5b)={res["five_b"]}')
    assert rank_at < h and res['five_b'] is False
    print('\n✓ C4 实例在 q0 阶整族不可行（(5a) 自动 + 映射满射 ⟹ 每个 Z 掉秩）')


if __name__ == '__main__':
    main()
