"""left_inverse_check.py —— 独立复核承重引理（G.1 的"引理 2"，不重用项目已有脚本）

**引理 2**：设 $P(\\lambda)=P_0+\\lambda P_1\\in\\mathbb Q[\\lambda]^{n\\times m}$，$\\operatorname{rank}_{\\mathbb Q(\\lambda)}P=m$
（满列秩）。则
$$\\operatorname{rank}P(\\lambda)=m\\ \\ \\forall\\lambda\\in\\mathbb C
\\iff\\exists X(\\lambda)\\in\\mathbb Q[\\lambda]^{m\\times n}:\\ X(\\lambda)P(\\lambda)=I_m,\\ \\deg X\\le m-1 .$$

本脚本用**精确有理/整数算术**独立测试两侧：
* (a) 精确判据：$P$ 的全部 $m\\times m$ 极大子式的 gcd 是否为常数；
* (b) 左逆线性系统（未知数 = $X$ 的系数，$\\deg\\le m-1$）是否可解（精确高斯消元/秩判据）。
两侧必须一致；并统计**最小可行次数**与界 $m-1$ 的紧性。

用法：python -u tools/verification/left_inverse_check.py
"""

import os
import sys
import random
import itertools
from fractions import Fraction
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import sympy as sp                        # noqa: E402

lam = sp.symbols('lam')
F = Fraction


def const_rank(P, m):
    """(a) 全部 m×m 极大子式的 gcd 是否为非零常数。返回 (是否常秩, gcd)。"""
    n = P.rows
    g = None
    for rs in itertools.combinations(range(n), m):
        d0 = sp.expand(P[list(rs), :].det())
        if d0 == 0:
            continue
        p0 = sp.Poly(d0, lam)
        g = p0 if g is None else sp.gcd(g, p0)
    if g is None:
        return False, None
    return sp.degree(g.as_expr(), lam) == 0, g.as_expr()


def left_inv_solvable(P, m, D):
    """(b) deg ≤ D 的左逆是否存在。返回 (可解, 最小次数或 None)。"""
    n = P.rows
    xs = [[[sp.Symbol(f'x_{a}_{b}_{t}') for t in range(D + 1)] for b in range(n)]
          for a in range(m)]
    degP = max(sp.degree(sp.expand(P[i, j]), lam) for i in range(n) for j in range(m))
    eqs = []
    for kk in range(D + degP + 1):
        for a in range(m):
            for j in range(m):
                acc = sp.Integer(0)
                for b in range(n):
                    pd = sp.Poly(sp.expand(P[b, j]), lam).as_dict()
                    for t in range(D + 1):
                        c = pd.get((kk - t,), sp.Integer(0))
                        if c != 0:
                            acc += xs[a][b][t] * c
                rhs = sp.Integer(1) if (kk == 0 and a == j) else sp.Integer(0)
                eqs.append(sp.expand(acc - rhs))
    eqs = [e for e in eqs if e != 0]
    vars_ = [xs[a][b][t] for a in range(m) for b in range(n) for t in range(D + 1)]
    M = sp.Matrix([[sp.expand(e).coeff(v) for v in vars_] for e in eqs])
    bb = sp.Matrix([-sp.expand(e).subs({v: 0 for v in vars_}) for e in eqs])
    return M.rank() == M.row_join(bb).rank()


def min_degree(P, m, Dmax=6):
    for D in range(Dmax + 1):
        if left_inv_solvable(P, m, D):
            return D
    return None


def random_pencil(n, m, rng, degenerate=False, bound=3):
    P0 = sp.Matrix([[rng.randrange(-bound, bound + 1) for _ in range(m)] for _ in range(n)])
    P1 = sp.Matrix([[rng.randrange(-bound, bound + 1) for _ in range(m)] for _ in range(n)])
    P = P0 + lam * P1
    if degenerate and m >= 1 and n > m:
        # 强制 rank P 在 λ=0 掉：把最后一行设为前 m 行的组合（常数部分）
        row = sum((P0[i, j] for i in range(m) for j in range(m)), sp.Integer(0))
        P = P.copy()
        for j in range(m):
            P[m, j] = P[m, j] - P[m, j]      # 占位
        P = P0 + lam * P1
        for j in range(m):
            P[m, j] = P[0, j]                # 与第一行相同 ⟹ 常数项处掉秩
    return P


def main():
    rng = random.Random(20261104)
    stat = Counter()
    for n, m in [(3, 1), (3, 2), (4, 2), (4, 3), (5, 2), (5, 3)]:
        for trial in range(6):
            P = random_pencil(n, m, rng, degenerate=(trial % 3 == 2))
            ok_const, g = const_rank(P, m)
            D = min_degree(P, m, Dmax=min(6, m + 2))
            solvable = D is not None
            stat['samples'] += 1
            if ok_const == solvable:
                stat['agree'] += 1
            else:
                stat['disagree'] += 1
                print(f'  不一致 n={n} m={m} trial={trial}: 常秩={ok_const}(gcd={g}) 左逆可解={solvable}')
            if solvable:
                stat['solvable'] += 1
                if D <= m - 1:
                    stat['within_bound'] += 1
                if D == m - 1:
                    stat['tight'] += 1
            else:
                stat['not_solvable'] += 1
    print('\n统计：', dict(stat))
    print('  agree = (a)常秩 与 (b)存在 deg≤m−1 左逆 一致；disagree 应为 0')
    print('  within_bound = 最小可行次数 ≤ m−1；tight = 恰为 m−1')


if __name__ == '__main__':
    main()
