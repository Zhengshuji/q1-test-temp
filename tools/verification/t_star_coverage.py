"""t_star_coverage.py —— 专家 2026-11-04 §8 的前两项实验

**(1) 证书复杂度**：`common-λ` 测试的正确参考形式是向量化后的秩一条件
$$u=\\operatorname{vec}(M_1),\\ v=\\operatorname{vec}(M_2):\\quad \\operatorname{rank}[u\\ v]\\le1\\ (u\\ne0),\\quad
u=0\\Rightarrow v=0 .$$
本轮先核验它与"13 个二次式"（逐列 $2\\times2$ 子式 + 列间 $\\lambda$ 一致）**是否等价**（含零列/退化情形）。

**(2) 可解类的覆盖**：(T*) 条件
$$\\operatorname{rank}\\bigl(P_K(\\lambda I-A)B_V\\bigr)=\\dim V\\quad \\forall\\lambda$$
（$B_V$ 为 $V$ 的基，$P_K$ 满行秩且 $\\ker P_K=K$）。若成立，则**任何** $\\mathcal Z\\subseteq K$ 在任何阶都谱可行
（一种与候选无关的、矩阵级的可解性证书）。用有理多项式 gcd 精确判定，并在已有实例上测覆盖。

用法：python -u tools/verification/t_star_coverage.py
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

import sympy as sp                        # noqa: E402
import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import observability_test as OT           # noqa: E402
import decide_symbolic as DS              # noqa: E402

F = Fraction
lam = sp.symbols('lam')


def vec(M):
    return [M[i][k] for i in range(len(M)) for k in range(len(M[0]))]


def rank_le_one(u, v):
    """[u v] 秩 ≤1（含零向量情形）。"""
    if all(t == 0 for t in u):
        return all(t == 0 for t in v)
    k = next(i for i, t in enumerate(u) if t != 0)
    if u[k] == 0:
        return all(t == 0 for t in v)
    rata = v[k] / u[k]
    return all(v[i] == rata * u[i] for i in range(len(u)))


def thirteen_equations(M1, M2):
    """旧的"13 个二次式"判据：逐列 2×2 子式全零 + 列间 λ 一致。"""
    dV = len(M1[0])
    lams = []
    for k in range(dV):
        if not M1 or len(M1) < 2:
            return None
        lam_k = None
        for i in range(len(M1)):
            if M1[i][k] != 0:
                lam_k = M2[i][k] / M1[i][k]
                break
        if lam_k is None:
            if any(M2[i][k] != 0 for i in range(len(M2))):
                return False
            continue
        for i in range(len(M1)):
            for j in range(i + 1, len(M1)):
                if M2[i][k] * M1[j][k] - M2[j][k] * M1[i][k] != 0:
                    return False
        lams.append(lam_k)
    if len(set(lams)) > 1:
        return False
    return True


def t_star(A, C, L0):
    """(T*)：rank(P_K (λI−A) B_V) = dim V ∀λ，其中 ker P_K = K。返回 (成立?, gcd 次数, 说明)。"""
    n, p, r = len(A), len(C), len(L0)
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    if not (V and V[0] and K and K[0]):
        return None, None, 'V 或 K 为零'
    dV, dK = len(V[0]), len(K[0])
    # P_K：满行秩且 ker P_K = K：取 K^⊥ 的一组行（(n−dK) × n）
    Kt = [[K[i][k] for i in range(n)] for k in range(dK)]
    ns = ZG.ker_cols(Kt)
    dP = len(ns[0]) if (ns and ns[0]) else 0
    P = [[ns[i][j] for i in range(n)] for j in range(dP)]        # dP × n
    if dP < dV:
        return False, None, f'dim(ker P_K)={dP} < dim V={dV}（必不满秩）'
    As = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in A])
    Ps = sp.Matrix([[sp.Rational(F(x).numerator, F(x).denominator) for x in row] for row in P])
    Bs = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in V])
    M = sp.expand(Ps * (lam * sp.eye(n) - As) * Bs)              # dP × dV
    mins = []
    for rs in itertools.combinations(range(dP), dV):
        m = sp.expand(M[list(rs), :].det())
        if m != 0:
            mins.append(sp.Poly(m, lam))
    if not mins:
        return False, None, '全部极大子式恒零'
    g = mins[0]
    for mm in mins[1:]:
        g = sp.gcd(g, mm)
    deg = sp.degree(g.as_expr(), lam)
    return (deg == 0), deg, f'极大子式 {len(mins)} 个，gcd 次数 {deg}'


def main():
    # ===== 实验 (1)：两种证书形式是否等价 =====
    rng = random.Random(20261104)
    st = Counter()
    for _ in range(3000):
        dP = rng.choice([4, 5])
        dV = 2
        M1 = [[F(rng.randrange(-3, 4)) for _ in range(dV)] for _ in range(dP)]
        M2 = [[F(rng.randrange(-3, 4)) for _ in range(dV)] for _ in range(dP)]
        if rng.random() < 0.2:                 # 制造零列 / 退化
            k = rng.randrange(dV)
            for i in range(dP):
                M1[i][k] = F(0)
                if rng.random() < 0.5:
                    M2[i][k] = F(0)
        a = rank_le_one(vec(M1), vec(M2))
        b = thirteen_equations(M1, M2)
        st['tested'] += 1
        if a == b:
            st['agree'] += 1
        else:
            st['disagree'] += 1
            if st['disagree'] <= 5:
                print(f'  证书形式不一致：向量化={a} 13式={b}')
    print('=== 实验 (1)：common-λ 证书的两种写法 ===')
    print('统计：', dict(st))

    # ===== 实验 (2)：(T*) 的覆盖 =====
    print('\n=== 实验 (2)：(T*) 的覆盖 ===')
    st2 = Counter()
    for trial in range(600):
        n = rng.choice([5, 6, 7])
        p = rng.choice([1, 2])
        r = rng.choice([1, 2])
        if p + r > n:
            continue
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(p)]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(r)]
        if LQ.rank(C) != p or LQ.rank(L0) != r:
            continue
        if LQ.rank(QR.observability_matrix(A, C)) != n:
            continue
        if LQ.rank(QR.observability_matrix(A, L0)) != n:
            continue
        ok, deg, why = t_star(A, C, L0)
        if ok is None:
            continue
        st2['tested'] += 1
        st2['T*_holds' if ok else 'T*_fails'] += 1
        if ok:
            # T* 成立 ⟹ 各阶应有可行解；在 q0 阶找一个见证
            q0 = Q0.eta_and_q0(A, C, L0)[0]
            K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
            d = n - p - q0
            k = len(K[0]) if (K and K[0]) else 0
            found = False
            if 0 < d <= k:
                for rows in itertools.combinations(range(k), d):
                    for b in range(0, 5):
                        Z = DS.Z_from_theta(A, C, L0, q0, rows, [F(b)] * (d * (k - d)))
                        if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                            continue
                        L = ZG.L_from_Z(A, C, L0, Z, q0)
                        if L is None or not LQ.condA(A, C, L):
                            continue
                        okb, _ = OT.observability_ok(A, C, L)
                        if okb:
                            found = True
                            break
                    if found:
                        break
            st2['T*_and_witness' if found else 'T*_no_witness_found'] += 1
    print('统计：', dict(st2))
    print('  说明：T* 是与候选无关的充分条件；成立时应各阶谱可行。')


if __name__ == '__main__':
    main()
