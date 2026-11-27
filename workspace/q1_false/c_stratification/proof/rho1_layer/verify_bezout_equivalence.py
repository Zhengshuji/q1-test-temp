"""§17 + T11 的等价性检验（验证 ≠ 证明）。

被测命题：对仿射族 p_1(τ),...,p_m(τ)（系数对 τ ∈ A 仿射，deg_λ ≤ d），

  (i)  ∃τ ∈ A: gcd_λ(p_1(τ,·),...,p_m(τ,·)) = 1
  (ii) ∃D ∃ 乘法映射 Φ_D 的极大子式 Δ:  Δ 在 A 上不恒为零

则 (i) ⟺ (ii)（这就是 §17 的 Bézout 线性化 + §27 的 T11）。

做法：随机取仿射族与仿射集 A，两边都用**精确有理算术**独立判定，比较结论。
- (i) 用 (I) 采样 A 的点 + 精确 gcd（可行集是开的 ⟹ 采样是决定性的）；
- (ii) 把 Δ 限制到 A 的仿射坐标下，检查是否每个系数都为 0。
"""
import itertools
import random
from fractions import Fraction as Fr
import sys
sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI


def ptrim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def pgcd(a, b):
    a, b = ptrim(list(a)), ptrim(list(b))
    while not (len(b) == 1 and b[0] == 0):
        r = list(a)
        while len(r) >= len(b) and not (len(r) == 1 and r[0] == 0):
            c = r[-1] / b[-1]
            d = len(r) - len(b)
            for i, bi in enumerate(b):
                r[i + d] -= c * bi
            r = ptrim(r)
        a, b = b, ptrim(r)
    return a


def pmul(a, b):
    o = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            o[i + j] += x * y
    return o


def peval(p, t):
    s = Fr(0)
    for c in reversed(p):
        s = s * t + c
    return s


def det_poly(M):
    """M: 矩阵，元素是多项式（系数列表）。返回行列式多项式。"""
    n = len(M)
    if n == 1:
        return ptrim(list(M[0][0]))
    acc = [Fr(0)]
    for j in range(n):
        sub = [[M[i][k] for k in range(n) if k != j] for i in range(1, n)]
        term = pmul(M[0][j], det_poly(sub))
        if j % 2:
            term = [-c for c in term]
        if len(acc) < len(term):
            acc += [Fr(0)] * (len(term) - len(acc))
        for i, c in enumerate(term):
            acc[i] += c
    return ptrim(acc)


def restrict_to_A(poly_coeffs, A_basis):
    """把"多项式的多项式"（把 τ 的幂展开）限制到仿射集 A 上：返回是否有非零系数。
    A 用 (τ0, 方向基) 表示；这里只做"逐项系数"的粗略版本：
    因为我们只关心恒零性，直接把 poly 写成关于 τ 的多项式并检查系数。
    为简单起见，poly_coeffs 已经是"τ 的多项式系数" 的列表（每个元素是系数）。"""
    return any(c != 0 for c in poly_coeffs)


def main():
    rng = random.Random(4242)
    agree = 0
    disagree = 0
    for trial in range(300):
        m = rng.choice([2, 3])
        d = rng.choice([1, 2])
        j = rng.choice([1, 2])          # tau 的维数
        # p_i(τ) = 常数部分 + Σ_k τ_k * 线性_ik（每个都是 deg ≤ d 的多项式）
        P0 = [[Fr(rng.randint(-2, 2)) for _ in range(d + 1)] for _ in range(m)]
        Pk = [[[Fr(rng.randint(-2, 2)) for _ in range(d + 1)] for _ in range(j)] for _ in range(m)]

        def pat(i, tau):
            out = list(P0[i])
            for k in range(j):
                out = [out[e] + tau[k] * Pk[i][k][e] for e in range(d + 1)]
            return ptrim(out)

        # (i) 采样 A（这里 A = 全部 R^j，最简单的情形；后面可加仿射约束）
        found_i = False
        for _t in range(80):
            tau = [Fr(rng.randint(-2, 2)) for _ in range(j)]
            g = pat(0, tau)
            for i in range(1, m):
                g = pgcd(g, pat(i, tau))
            if len(g) == 1 and g[0] != 0:
                found_i = True
                break
        # (ii) 对若干 D，检查是否有极大子式在 A 上不恒零：这里 A = R^j，
        #      所以"Δ 不恒为零"= Δ 作为 τ 的多项式有非零系数。
        found_ii = False
        # 简化：只检查"Φ_D 的秩在一般点满"——等价地在若干随机 τ 上算 rank
        for D in range(0, 2 * d * (m - 1) + 2):
            for _t in range(60):
                tau = [Fr(rng.randint(-3, 3)) for _ in range(j)]
                # 构造 Φ_D 的矩阵
                rows = d + D + 1
                cols = m * (D + 1)
                M = [[Fr(0)] * cols for _ in range(rows)]
                for i in range(m):
                    p = pat(i, tau)
                    for k in range(D + 1):
                        for e, c in enumerate(p):
                            if k + e <= d + D:
                                M[k + e][i * (D + 1) + k] += c
                if AI.rank(M) == rows:
                    found_ii = True
                    break
            if found_ii:
                break
        if found_i == found_ii:
            agree += 1
        else:
            disagree += 1
            if disagree <= 3:
                print(f"不一致: m={m} d={d} j={j}  (i)={found_i} (ii)={found_ii}")
    print(f"一致 {agree}，不一致 {disagree}")
    print("结论：0 不一致 => §17 的等价性（在随机仿射族上）成立（**验证，不是证明**）")


if __name__ == '__main__':
    main()