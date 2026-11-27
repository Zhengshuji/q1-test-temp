r"""μ=1、$w\ne0$ 的真实实例：格子被覆盖 —— C.2 的"被覆盖"方向。

背景（2026-10-30）：§52.7 那个实例其实 $w=0$（归 C.5），所以 C.2 一直**没有** $w\ne0$ 的真实实例
（见 proof/rho1_layer/VERIFICATION_STATUS.md §5.3 的更正）。本脚本给一个，并且两条路都验：

  (1) **判据**（C.2）：$[\lambda I-T;\,w]$ 的最大子式 $\gcd$ 非常量 ⟺ 存在 $\lambda$ 使秩降 ⟺ 被覆盖；
  (2) **直接**验 $(5b)$：对提升族里的每个 $\mathcal L$，算商铅笔 $Q_{\mathcal L}(\lambda)=\lambda\pi(\mathcal L)-\pi(\mathcal LA)$
      的 $3\times3$ 子式 $\gcd$（B.1：$(5b)\iff$ 该铅笔对所有 $\lambda$ 满秩 $\rho=3$），非常量 ⟹ $(5b)$ 失败 ⟹ 被覆盖。

全部有理算术；多项式用"在 $\rho+1$ 个点上取值 + Lagrange 插值 + Euclid"处理（根的讨论在 $\mathbb C$ 上）。

实例（写死）：$n=6$、
$$A=\begin{pmatrix}1&0&0&0&-1&2\\0&2&1&1&-1&0\\2&-1&1&2&-1&1\\0&0&0&0&0&1\\0&0&0&0&0&0\\-1&0&0&1&2&1\end{pmatrix},\quad
C=\begin{pmatrix}0&0&0&1&0&0\\0&0&0&0&1&0\end{pmatrix},\quad L_0=e_1 .$$
于是 $\mathcal J=\langle e_4,e_5,e_6\rangle$、$d=3$、$\rho=3$（$U=X$）、$B=\langle\pi(e_1)\rangle$、$\mu=1$、
$H=\mathcal V\cap\mathcal J=\langle e_6\rangle$、$w=\beta(e_6)=\pi(e_1)\ne0$，
$T=\begin{pmatrix}1&0&0\\0&2&1\\2&-1&1\end{pmatrix}$ 在 $w^\perp$（$v_1=0$）里有特征向量。

用法：python proof/rho1_layer/verify_mu1_w_ne_0_instance.py
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))

import audit_independent as AI

mul, rank, vstack, row_basis, nullspace = AI.mul, AI.rank, AI.vstack, AI.row_basis, AI.nullspace

N = 6
A_MAT = [[1, 0, 0, 0, -1, 2],
         [0, 2, 1, 1, -1, 0],
         [2, -1, 1, 2, -1, 1],
         [0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0],
         [-1, 0, 0, 1, 2, 1]]
C_MAT = [[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0]]
L0_MAT = [[1, 0, 0, 0, 0, 0]]


# ---------------------------------------------------------------- 多项式小工具
def _det(M):
    M = [r[:] for r in M]
    n = len(M)
    val = Fr(1)
    for c in range(n):
        piv = next((i for i in range(c, n) if M[i][c] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            val = -val
        val *= M[c][c]
        for i in range(c + 1, n):
            f = M[i][c] / M[c][c]
            M[i] = [M[i][k] - f * M[c][k] for k in range(n)]
    return val


def _trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def _polmul(p, q):
    out = [Fr(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def _polrem(p, q):
    p = _trim(p[:])
    while len(p) >= len(q) and p != [Fr(0)]:
        f = p[-1] / q[-1]
        sh = len(p) - len(q)
        for k in range(len(q)):
            p[sh + k] -= f * q[k]
        p = _trim(p)
    return p


def _polygcd(p, q):
    p, q = _trim(p), _trim(q)
    while q != [Fr(0)]:
        p, q = q, _polrem(p, q)
    return _trim(p)


def _interp(xs, ys):
    coef = [Fr(0)] * len(xs)
    for i in range(len(xs)):
        basis = [Fr(1)]
        den = Fr(1)
        for j in range(len(xs)):
            if j == i:
                continue
            basis = _polmul(basis, [-xs[j], Fr(1)])
            den *= (xs[i] - xs[j])
        fac = ys[i] / den
        for k in range(len(basis)):
            coef[k] += fac * basis[k]
    return _trim(coef)


def minors_gcd_degree(eval_rows, nrows, size):
    """给 eval_rows(lam) -> nrows×size 的行列表，返回 size 阶子式 gcd 的次数。

    子式对 λ 的次数 ≤ size（每个元素 ≤ 一次），所以在 0..size 取值即可插值。
    """
    xs = [Fr(k) for k in range(size + 1)]
    polys = []
    for rs in itertools.combinations(range(nrows), size):
        ys = []
        for lam in xs:
            R = eval_rows(lam)
            ys.append(_det([[R[i][k] for k in range(size)] for i in rs]))
        polys.append(_interp(xs, ys))
    g = polys[0]
    for q in polys[1:]:
        g = _polygcd(g, q)
    return len(_trim(g)) - 1


# ---------------------------------------------------------------- 实例与格子数据
def build():
    return ([[Fr(x) for x in r] for r in A_MAT],
            [[Fr(x) for x in r] for r in C_MAT],
            [[Fr(x) for x in r] for r in L0_MAT])


def cell_data(A, C):
    M = vstack([C, mul(C, A)])
    j = rank(M)
    J = row_basis(M)
    d = N - j
    Nv = nullspace(M)
    Nm = [[Nv[k][i] for k in range(len(Nv))] for i in range(N)]

    def pi(x):
        return mul([x], Nm)[0]

    G = [[sum(Nm[a][i] * Nm[a][k] for a in range(N)) for k in range(d)] for i in range(d)]
    Ginv = AI.inv(G)

    def lift(u):
        eG = [sum(u[k] * Ginv[k][i] for k in range(d)) for i in range(d)]
        return [sum(eG[k] * Nm[a][k] for k in range(d)) for a in range(N)]

    e = [[Fr(1) if t == i else Fr(0) for t in range(N)] for i in range(N)]
    U = row_basis([pi(e[0]), pi(e[1]), pi(e[2])])
    B = row_basis([pi(mul([jj], A)[0]) for jj in J])
    mu = len(B) + len(U) - rank(B + U)

    a = None
    rows = [[B[i][k] for i in range(len(B))] + [-U[j2][k] for j2 in range(len(U))]
            for k in range(d)]
    for sol in nullspace(rows):
        er = [sum(sol[i] * B[i][k] for i in range(len(B))) for k in range(d)]
        if not any(er):
            continue
        eq = [[U[j2][k] for j2 in range(len(U))] + [er[k]] for k in range(d)]
        cand = [Fr(0)] * len(U)
        for row in AI.rref(eq)[0]:
            piv = next((t for t in range(len(U)) if row[t] != 0), None)
            if piv is None:
                continue
            cand[piv] = row[len(U)] / row[piv]
        if all(sum(cand[t] * U[t][k] for t in range(len(U))) == er[k] for k in range(d)):
            a = cand
            break
    assert a is not None, 'B∩U 的向量写不成 U 的坐标'

    V = row_basis([e[0], e[1], e[2], e[5]])          # V = <e1,e2,e3,e6>，含 row(L0)=e1
    rows_int = [[V[i][k] for i in range(len(V))] + [-J[j2][k] for j2 in range(len(J))]
                for k in range(N)]
    ns = nullspace(rows_int)
    assert len(ns) == 1, f'dim(V∩J) != 1（{len(ns)}）'
    h = [sum(ns[0][i] * V[i][k] for i in range(len(V))) for k in range(N)]
    w = pi(mul([h], A)[0])

    fU = [pi(mul([lift(u)], A)[0]) for u in U]
    nunk = len(U) ** 2 + len(U) * len(B)
    eqs = []
    for i in range(len(U)):
        for k in range(d):
            row = [Fr(0)] * nunk + [fU[i][k]]
            for j2 in range(len(U)):
                row[j2 * len(U) + i] = U[j2][k]
            for t in range(len(B)):
                row[len(U) ** 2 + i * len(B) + t] = B[t][k]
            eqs.append(row)
    sol = [Fr(0)] * nunk
    for row in AI.rref(eqs)[0]:
        piv = next((t for t in range(nunk) if row[t] != 0), None)
        if piv is None:
            continue
        sol[piv] = row[nunk] / row[piv]
    T = [[sol[j2 * len(U) + i] for j2 in range(len(U))] for i in range(len(U))]
    for i in range(len(U)):
        res = [fU[i][k] - sum(T[i][j2] * U[j2][k] for j2 in range(len(U))) for k in range(d)]
        assert rank(B + [res]) == len(B), 'T 不满足格子定义（残差不在 B 里）'
    return dict(j=j, d=d, J=J, U=U, B=B, mu=mu, a=a, h=h, w=w, T=T, pi=pi)


def main():
    A, C, L0 = build()
    D = cell_data(A, C)
    print(f"j={D['j']}、d={D['d']}、μ={D['mu']}、a={[str(x) for x in D['a']]}")
    print(f"h={[str(x) for x in D['h']]}、w=β(h)={[str(x) for x in D['w']]}")
    print(f"T={[[str(x) for x in r] for r in D['T']]}")
    assert D['mu'] == 1, 'μ != 1'
    assert any(D['w']), 'w = 0（本脚本要的是 w ≠ 0）'

    # (1) C.2 的判据：[λI − T; w] 的 3 阶子式 gcd
    def cell_pencil(lam):
        R = [[(lam if i == k else Fr(0)) - D['T'][i][k] for k in range(3)] for i in range(3)]
        R.append([Fr(x) for x in D['w']])
        return R
    deg = minors_gcd_degree(cell_pencil, 4, 3)
    print(f"判据（C.2）：gcd 次数 = {deg}（>0 ⟹ 有公共根 ⟹ 被覆盖）{'✓' if deg > 0 else '✗'}")
    assert deg > 0

    # (2) 直接验 (5b)：商铅笔 λπ(L) − π(LA) 的 3 阶子式 gcd（B.1）
    e = [[Fr(1) if t == i else Fr(0) for t in range(N)] for i in range(N)]
    h = D['h']
    pi = D['pi']
    CA = mul(C, A)
    total = covered = 0
    for s1 in range(-2, 3):
        for s2 in range(-2, 3):
            L = [e[0],
                 [e[1][k] + Fr(s1) * h[k] for k in range(N)],
                 [e[2][k] + Fr(s2) * h[k] for k in range(N)],
                 h]
            PL = [pi(r) for r in L]
            PLA = [pi(mul([r], A)[0]) for r in L]

            def q_pencil(lam, PL=PL, PLA=PLA):
                return [[lam * PL[i][k] - PLA[i][k] for k in range(len(PL[0]))]
                        for i in range(len(PL))]
            total += 1
            if minors_gcd_degree(q_pencil, len(L), 3) > 0:
                covered += 1
    print(f"直接验 (5b)：{covered}/{total} 个提升的商铅笔子式 gcd 非常量（被覆盖）"
          f"{'✓' if covered == total else '✗'}")
    assert covered == total
    print('\n=> μ=1、w≠0 的真实实例：格子被覆盖 ✓（C.2 的"被覆盖"方向现在有真实实例了）')


if __name__ == '__main__':
    main()
