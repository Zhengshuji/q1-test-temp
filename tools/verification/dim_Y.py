"""dim_Y.py —— 计算坏点映射像的闭包维数 $\\dim Y$，并检验专家的遮蔽判据

坏点映射：$x\\in V=\\ker[C;CA]$（$L_0x\\ne0$）↦ $z(x)=(\\lambda(x)I-A)x\\in K=\\ker[C;L_0]$，
$\\lambda(x)=L_0Ax/L_0x$。$Y=\\overline{\\Phi(\\mathbb P(V))}\\subseteq\\mathbb P(K)$。

本脚本用**精确有理插值**算 $x\\mapsto z(x)$ 在一般点处的 Jacobian 秩，从而得到 $\\dim Y$：
沿每个坐标方向 $x_0+t\\,e_j$ 取 4 个点插值多项式，求 $t=0$ 处的导数，拼成 $k\\times\\dim V$ 矩阵，秩减一即投影维数。

然后检验专家 2026-11-03 §4.2 的判据：
$$h=n\\ \\text{（该阶每个候选）}\\quad\\text{且}\\quad \\dim Y\\ge q-r\\ \\Longrightarrow\\ \\text{该阶无解}.$$

用法：python -u tools/verification/dim_Y.py
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
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402

F = Fraction


def vec(mat, coeff):
    m = len(mat[0])
    return [sum(coeff[j] * mat[i][j] for j in range(m)) for i in range(len(mat))]


def z_of(A, L0, x):
    """$z(x)=(\\lambda(x)I-A)x$，$\\lambda(x)=L_0Ax/L_0x$；返回 z 或 None（分母为零）。"""
    n = len(x)
    L0x = sum(L0[0][i] * x[i] for i in range(n))
    if L0x == 0:
        return None
    Ax = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]
    L0Ax = sum(L0[0][i] * Ax[i] for i in range(n))
    lam = L0Ax / L0x
    return [lam * x[i] - Ax[i] for i in range(n)]


def lands_in_K(z, C, L0):
    """检查 $z\in K=\ker[C;L_0]$（$Cz=0$ 且 $L_0z=0$）。"""
    n = len(z)
    okC = all(sum(C[j][i] * z[i] for i in range(n)) == 0 for j in range(len(C)))
    okL = all(sum(L0[j][i] * z[i] for i in range(n)) == 0 for j in range(len(L0)))
    return okC and okL


def interp_deriv(vals, ts):
    """给定 t=ts 上的取值 vals，返回 t=0 处的导数（拉格朗日插值）。"""
    m = len(ts)
    d = F(0)
    for i in range(m):
        num = F(0)
        for j in range(m):
            if j == i:
                continue
            term = F(1)
            for k2 in range(m):
                if k2 == i or k2 == j:
                    continue
                term *= (0 - ts[k2])
            num += term
        den = F(1)
        for k2 in range(m):
            if k2 != i:
                den *= (ts[i] - ts[k2])
        d += vals[i] * num / den
    return d


def dim_Y(A, C, L0):
    """返回 (dim Y, 说明)。在 V 的参数空间上求 Jacobian 秩（投影维数 = 秩 − 1）。"""
    n, p, r = len(A), len(C), len(L0)
    CA = LQ.mul(C, A)
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    dv, k = len(V[0]), len(K[0])
    Kbasis = [[K[i][j] for i in range(n)] for j in range(k)]
    import random
    rng = random.Random(20261103)
    c0 = None
    for _ in range(300):
        co = [F(rng.randrange(-2, 3)) for _ in range(dv)]
        if all(c == 0 for c in co):
            continue
        if z_of(A, L0, vec(V, co)) is not None:
            c0 = co
            break
    if c0 is None:
        return None, 'V 上处处 L_0x=0（坏点映射不定义）'
    z0 = z_of(A, L0, vec(V, c0))
    if not lands_in_K(z0, C, L0):
        return None, 'z(x) 不落在 K=ker[C;L_0]（r≥2 时 λ 不能同时消掉 L_0 的所有行）'
    ts = [F(0), F(1), F(2), F(3)]
    cols = []
    for j in range(dv):
        rows = []
        for t in ts:
            co = [c0[i] + (t if i == j else F(0)) for i in range(dv)]
            x = vec(V, co)
            z = z_of(A, L0, x)
            if z is None:
                return None, '沿该方向出现 L_0x=0'
            aug = [[Kbasis[q][i] for q in range(k)] + [z[i]] for i in range(n)]
            R, piv = LQ.rref(aug)
            coef = [F(0)] * k
            for ri, pc in enumerate(piv):
                if pc < k:
                    coef[pc] = R[ri][k]
            rows.append(coef)
        cols.append(rows)
    J = [[interp_deriv([cols[j][t][i] for t in range(len(ts))], ts) for j in range(dv)]
         for i in range(k)]
    rk = LQ.rank(J)
    return rk - 1, f'dim V={dv}, dim K={k}, Jacobian 秩={rk}'


def report(tag, A, C, L0, q):
    CA = LQ.mul(C, A)
    W = [x[:] for x in C] + [x[:] for x in CA]
    r1 = LQ.rank(W)
    m, note = dim_Y(A, C, L0)
    print(f'  {tag}（q={q}，r={len(L0)}，r1={r1}）：dim Y = {m}；q−r = {q - len(L0)}；{note}')
    return m


def main():
    import importlib.util as iu
    print('=== C4 实例（已知 $q_0=3$ 整族失败）===')
    spec = iu.spec_from_file_location('V4', os.path.join(_ROOT, 'proof', 'refuted', 'verify_C4_type3.py'))
    V4 = iu.module_from_spec(spec)
    spec.loader.exec_module(V4)
    A, C, L0 = V4.build()[:3]
    for q in (3,):
        report('C4', A, C, L0, q)
    print('\n=== 公开例子（q=4 整族失败、q=5 可行）===')
    spec2 = iu.spec_from_file_location('F2', os.path.join(_ROOT, 'proof', 'fernando_2gap', 'verify.py'))
    m2 = iu.module_from_spec(spec2)
    spec2.loader.exec_module(m2)
    for q in (4, 5):
        report('Fernando', m2.A, m2.C, m2.L0, q)
    print('\n=== 异常实例（q=3 可行）===')
    A2, C2, L02 = QR.make_instance(7, 2, 2, 4004 * 23 + 2 * 11 + 2)
    for q in (3,):
        report('anomaly', A2, C2, L02, q)


if __name__ == '__main__':
    main()
