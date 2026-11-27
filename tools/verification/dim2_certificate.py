"""dim2_certificate.py —— 在 $\\dim V=\\dim K=2$ 的情形检验单-$\\lambda$ 证书（B.13e）

**设定**：$n=4$、$p=r=1$、$r_1=2$ ⟹ $\\dim V=2$、$\\dim K=2$。阶 $q=2$ 时 $d=n-p-q=1$，
$\\mathcal Z$ 是 $K$ 中的**直线**（每张图卡一个参数）。

**单-$\\lambda$ 证书（B.13e）**：若 $\\exists\\lambda_0:(\\lambda_0I-A)V=K$，则每个 $\\mathcal Z\\subseteq K$ 都被打到
（例外需 $(\\lambda_0I-A)^{-1}\\mathcal Z\\subseteq\\mathcal Z$，但原像落在 $V$ 里，故 $V\\cap K=0$ 时无例外）。
判据实现：令 $M_1=K^{\\perp}V$、$M_2=K^{\\perp}AV$（都是 $2\\times2$，$K^{\\perp}$ 为 $2\\times4$ 的零化子），
则 $(\\lambda I-A)V\\subseteq K\\iff\\lambda M_1=M_2$；解出 $\\lambda$ 并核验。

**比较**：证书成立 ⟺ 该阶整族不可行（用 Toeplitz 逐候选核验）。

用法：python -u tools/verification/dim2_certificate.py
"""

import os
import sys
import itertools
import random
from fractions import Fraction
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import decide_symbolic as DS              # noqa: E402

F = Fraction


def annihilator_rows(K, n):
    """返回 K 的零化子的一组行基（(n−dim K) × n 的行）。"""
    Kt = [[K[i][k] for i in range(n)] for k in range(len(K[0]))] if K and K[0] else []
    basis = []
    for e in range(n):
        # 求解 y·K = 0 的第 e 个基向量：用线性系统
        pass
    # 直接用 nullspace：{y : y^T K = 0} ⟺ K^T y = 0
    ns = ZG.ker_cols(Kt) if Kt else None
    if ns is None:
        return None
    d = len(ns[0]) if (ns and ns[0]) else 0
    return [[ns[i][j] for i in range(n)] for j in range(d)]      # d × n


def single_lambda_certificate(A, C, L0):
    """检查 ∃λ: (λI−A)V ⊆ K 且 dim((λI−A)V) = dim K。返回 (成立?, λ, 说明)。"""
    n = len(A)
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    if not (V and V[0] and K and K[0]):
        return None, None, 'V 或 K 为零'
    dV, dK = len(V[0]), len(K[0])
    Kperp = annihilator_rows(K, n)
    if Kperp is None or not Kperp:
        return None, None, '零化子构造失败'
    AV = LQ.mul(A, V)
    M1 = [[sum(Kperp[i][j] * V[j][k] for j in range(n)) for k in range(dV)]
          for i in range(len(Kperp))]
    M2 = [[sum(Kperp[i][j] * AV[j][k] for j in range(n)) for k in range(dV)]
          for i in range(len(Kperp))]
    # 需要 λ M1 = M2：找 λ
    lam = None
    for i in range(len(M1)):
        for k in range(dV):
            if M1[i][k] != 0:
                lam = M2[i][k] / M1[i][k]
                break
        if lam is not None:
            break
    if lam is None:
        # M1 = 0：则需 M2 = 0（对一切 λ 成立）
        if all(M2[i][k] == 0 for i in range(len(M2)) for k in range(dV)):
            return 'all_lambda', None, 'M1=0 且 M2=0（对一切 λ 成立）'
        return False, None, 'M1=0 但 M2≠0（无 λ）'
    ok = all(M2[i][k] == lam * M1[i][k] for i in range(len(M1)) for k in range(dV))
    return ok, lam, f'λ={lam}'


def family_fails(A, C, L0, q, max_theta=6):
    """q 阶整族是否全失败（枚举图卡 × θ）。返回 (全失败?, 候选数, 可行数)。"""
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    if not K or not K[0]:
        return None, 0, 0
    k = len(K[0])
    if d <= 0 or d > k:
        return None, 0, 0
    tot = feas = 0
    for rows in itertools.combinations(range(k), d):
        for b in range(max_theta + 1):
            Z = DS.Z_from_theta(A, C, L0, q, rows, [F(b)] * (d * (k - d)))
            if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                continue
            L = ZG.L_from_Z(A, C, L0, Z, q)
            if L is None or not LQ.condA(A, C, L):
                continue
            tot += 1
            try:
                if TC.analyse(A, C, L)['five_b']:
                    feas += 1
            except AssertionError:
                continue
    return (tot > 0 and feas == 0), tot, feas


def main():
    rng = random.Random(20261104)
    st = Counter()
    n, p, r, q = 4, 1, 1, 2
    for trial in range(4000):
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        if LQ.rank(C) != 1 or LQ.rank(L0) != 1:
            continue
        if LQ.rank([list(x) for x in C] + L0) != 2:
            continue
        CA = LQ.mul(C, A)
        r1 = LQ.rank([list(x) for x in C] + [list(x) for x in CA])
        if r1 != 2:
            continue
        V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if len(V[0]) != 2 or len(K[0]) != 2:
            continue
        # V ∩ K = 0 ？
        VK = [[V[i][j] for j in range(2)] + [K[i][j] for j in range(2)] for i in range(n)]
        if LQ.rank([[VK[i][j] for i in range(n)] for j in range(4)]) != 4:
            st['VcapK_ne0'] += 1
            continue
        cert, lam, why = single_lambda_certificate(A, C, L0)
        fails, tot, feas = family_fails(A, C, L0, q)
        if fails is None:
            continue
        st['tested'] += 1
        if cert == 'all_lambda':
            st['cert_all_lambda'] += 1
            continue
        if bool(cert) == fails:
            st['agree'] += 1
        else:
            st['disagree'] += 1
            if st['disagree'] <= 6:
                print(f'  不一致：证书={cert}({why}) 整族失败={fails}（候选 {tot}，可行 {feas}）')
    print('统计：', dict(st))
    print('  agree = 单-λ 证书 ⟺ 整族不可行；disagree 应为 0')


if __name__ == '__main__':
    main()
