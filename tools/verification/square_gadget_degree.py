"""square_gadget_degree.py —— 方阵情形：系数映射的次数约束（符号计算，精确有理数）

背景（专家 2026-11-02 §5）：
  方阵情形（q=t）下 (5b) ⟺ D(λ)=det[U | P(λ)] 的**正次数系数为零、常数项非零**。
  要问的是：系数映射 Θ ↦ (a_0,...,a_m) 的表达力够不够编码算术（如 z=xy, u=x+y, v=1-x^2）。

本文件检验一条**设计约束**（不是定理，是对具体小例的符号展开）：
  D 对 U 的每一列**多重线性**（行列式性质）⟹ 每个系数 a_k 对 U 的列至多**一次**、
  故对 U 的行数/参数至多**r 次**（r = U 的列数 = dim U）。
  因此"能被编进系数的方程"次数 ≤ r——编码 z=xy（次数 2）至少需要 r ≥ 2。

做法：取一个 4×4 的方阵 M(λ) = [g1 | g2 | c3 − λ e3 | c4 − λ e4]，
其中 g1,g2 是符号列（各 4 个变量，模拟 U 的两列），c3,c4 是数值列。
展开 det M(λ) 为 λ 的多项式；检查每个系数对 g 变量的**次数 ≤ 2（总次数）且每个变量 ≤ 1**。

注：这里我们**不**声称 M(λ) 来自某个真实的观测器铅笔——只检验"多重线性 ⟹ 次数上界"这条设计约束。
"""

import itertools
from fractions import Fraction


# ---------------------------------------------------------------- 符号多项式（字典表示）


def pzero():
    return {}


def pconst(c):
    c = Fraction(c)
    return {} if c == 0 else {(): c}


def pvar(name):
    return {(name,): Fraction(1)}


def padd(a, b):
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, Fraction(0)) + c
        if out[m] == 0:
            del out[m]
    return out


def pneg(a):
    return {m: -c for m, c in a.items()}


def psub(a, b):
    return padd(a, pneg(b))


def pmul(a, b):
    out = {}
    for m1, c1 in a.items():
        for m2, c2 in b.items():
            m = tuple(sorted(m1 + m2))
            out[m] = out.get(m, Fraction(0)) + c1 * c2
    return {m: c for m, c in out.items() if c != 0}


def deg_total(p):
    return max((len(m) for m in p), default=0)


def deg_in(p, name):
    return max((m.count(name) for m in p), default=0)


def det_symbolic(M):
    """M: 方阵，元素是符号多项式字典。Laplace 展开（n<=4 够用）。"""
    n = len(M)
    if n == 1:
        return M[0][0]
    if n == 2:
        return psub(pmul(M[0][0], M[1][1]), pmul(M[0][1], M[1][0]))
    total = {}
    for j in range(n):
        minor = [[M[i][k] for k in range(n) if k != j] for i in range(1, n)]
        term = pmul(M[0][j], det_symbolic(minor))
        sign = 1 if j % 2 == 0 else -1
        total = padd(total, pconst(sign) and {m: sign * c for m, c in term.items()} if term else {})
    return total


# ---------------------------------------------------------------- λ 的多项式（系数是符号多项式）


def det_lambda(M_func, deg):
    """M_func(lam) 返回符号矩阵；用 deg+1 个有理点插值出 λ 的系数。"""
    # 采 deg+1 个 λ 值，得到符号行列式，再插值
    pts = [Fraction(k, 1) for k in range(deg + 1)]
    vals = [det_symbolic(M_func(t)) for t in pts]
    # 拉格朗日插值：coefficients c_k 使 D(λ)=sum c_k λ^k
    coeffs = [pzero() for _ in range(deg + 1)]
    for i, ti in enumerate(pts):
        # basis_i(λ) = prod_{j!=i} (λ - t_j) / (t_i - t_j)
        basis = [pconst(1)]
        denom = Fraction(1)
        for j, tj in enumerate(pts):
            if j == i:
                continue
            denom *= (ti - tj)
            # 乘 (λ - t_j)
            newb = [pzero() for _ in range(len(basis) + 1)]
            for k, b in enumerate(basis):
                newb[k + 1] = padd(newb[k + 1], b)
                newb[k] = padd(newb[k], {m: -tj * c for m, c in b.items()})
            basis = newb
        for k, b in enumerate(basis):
            coeffs[k] = padd(coeffs[k], {m: c / denom for m, c in pmul(vals[i], b).items()})
    return coeffs


def main():
    # 4x4：g1, g2 是符号列；其余两列放 (A - λI) 的两列
    g1 = [pvar('g10'), pvar('g11'), pvar('g12'), pvar('g13')]
    g2 = [pvar('g20'), pvar('g21'), pvar('g22'), pvar('g23')]
    # 数值列：c3 - λ e3, c4 - λ e4
    def col3(lam):
        return [pconst(1), pconst(2), psub(pconst(3), pconst(lam)), pconst(4)]

    def col4(lam):
        return [pconst(5), pconst(6), pconst(7), psub(pconst(8), pconst(lam))]

    def Mf(lam):
        return [[g1[i], g2[i], col3(lam)[i], col4(lam)[i]] for i in range(4)]

    coeffs = det_lambda(Mf, deg=2)  # 两列含 λ ⟹ 次数 <= 2
    print('det 的 λ-系数个数（应为 3）:', len(coeffs))
    gvars = [f'g1{i}' for i in range(4)] + [f'g2{i}' for i in range(4)]
    ok = True
    for k, c in enumerate(coeffs):
        dt = deg_total(c)
        dg1 = max((deg_in(c, v) for v in [f'g1{i}' for i in range(4)]), default=0)
        dg2 = max((deg_in(c, v) for v in [f'g2{i}' for i in range(4)]), default=0)
        print(f'  a_{k}: 总次数={dt}, 对 g1 各变量最大次数={dg1}, 对 g2 各变量最大次数={dg2}, 单项数={len(c)}')
        # 断言：对每个变量次数 <= 1；总次数 <= 2（=列数）
        if dg1 > 1 or dg2 > 1 or dt > 2:
            ok = False
    print()
    print('设计约束检验：每个系数对每个 U-列变量次数 <= 1 且总次数 <= r=2 ⟹', '成立' if ok else '不成立')
    print('推论（设计层面）：可编进系数的方程次数 <= r；编码 z=xy 需要 r>=2。')
    print('注意：本检验只针对这个 4x4 例子；M(λ) 是否来自真实观测器铅笔未验证。')


if __name__ == '__main__':
    main()
