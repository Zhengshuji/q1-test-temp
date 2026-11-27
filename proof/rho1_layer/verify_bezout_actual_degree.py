"""验证 C1 的修正：Bézout 判据必须用**实际**最大次数 d_*，不能用松上界 rho。

对每个层样本（抽象模型：行 = lam*u_i - (T u_i + beta(tau_i))，以及 -beta(h)）：
  * 求全部 rho x rho 子式 p_1..p_N（一元多项式，精确有理系数）；
  * d_* = max deg p_i（**实际**最大次数）；
  * g = gcd(p_1..p_N)；(5b) <=> g 是非零常数；
  * Phi_D 的矩阵 M_D：未知量 = 每个 a_i 的系数（deg a_i <= D），方程 = sum a_i p_i 的各次系数
    目标空间 = C[lam]_{<= d_* + D}，维数 = d_* + D + 1；
    满射 <=> rank(M_D) = d_* + D + 1。
  * 分别用 D = 2*d_*(N-1)（正确）与 D = 2*rho*(N-1)（松上界）测。
预期：正确的 D 下 (5b) <=> M_D 满射（全部一致）；松上界下会出现不一致（因为目标空间比实际像大）。
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI


def ptrim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def pdivmod(a, b):
    a, b = ptrim(list(a)), ptrim(list(b))
    q = [Fr(0)] * max(1, len(a) - len(b) + 1)
    r = list(a)
    while len(r) >= len(b) and not (len(r) == 1 and r[0] == 0):
        c = r[-1] / b[-1]
        dd = len(r) - len(b)
        q[dd] = c
        for i, bi in enumerate(b):
            r[i + dd] -= c * bi
        r = ptrim(r)
    return q, r


def pgcd(a, b):
    a, b = ptrim(list(a)), ptrim(list(b))
    while not (len(b) == 1 and b[0] == 0):
        _, r = pdivmod(a, b)
        a, b = b, r
    return a


def pmul(a, b):
    o = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            o[i + j] += x * y
    return ptrim(o)


def padd(a, b):
    o = [Fr(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        o[i] += x
    for i, y in enumerate(b):
        o[i] += y
    return ptrim(o)


def det_poly(M):
    n = len(M)
    if n == 1:
        return ptrim(list(M[0][0]))
    acc = [Fr(0)]
    for j in range(n):
        sub = [[M[i][k] for k in range(n) if k != j] for i in range(1, n)]
        term = pmul(M[0][j], det_poly(sub))
        if j % 2:
            term = [-c for c in term]
        acc = padd(acc, term)
    return ptrim(acc)


def bezout_full_rank(polys, dstar, D):
    """rank(M_D) 是否 = dstar + D + 1。M_D 的列 = 每个 p_i 的位移副本。"""
    rows = dstar + D + 1
    cols = len(polys) * (D + 1)
    M = [[Fr(0)] * cols for _ in range(rows)]
    col = 0
    for p in polys:
        for sh in range(D + 1):
            for k, c in enumerate(p):
                if sh + k < rows:
                    M[sh + k][col] = c
            col += 1
    return AI.rank(M), rows


def main():
    rng = random.Random(2718)
    ok_correct = 0
    bad_loose = 0
    total = 0
    for trial in range(60):
        d = rng.choice([4, 5])
        rho = rng.choice([2, 3])
        U = AI.row_basis([[Fr(rng.randint(-2, 2)) for _ in range(d)] for _ in range(rho + 2)])[:rho]
        if len(U) < rho:
            continue
        m = rng.choice([1, 2])
        B = AI.row_basis([[Fr(rng.randint(-2, 2)) for _ in range(d)] for _ in range(m + 2)])[:m]
        BU = [b for b in B if AI.rank([r[:] for r in U] + [b]) == len(U)]
        if not BU:
            continue
        w = BU[0]
        Cc = [[Fr(rng.randint(-2, 2)) for _ in range(rho)] for _ in range(rho)]
        Tu = [[sum(Cc[i][j] * U[j][k] for j in range(rho)) for k in range(d)] for i in range(rho)]
        tv = [[sum(Fr(rng.randint(-2, 2)) * b[k] for b in BU) for k in range(d)] for _ in range(rho)]
        rows = [(U[i], [Tu[i][k] + tv[i][k] for k in range(d)]) for i in range(rho)]
        rows.append(([Fr(0)] * d, list(w)))
        polys = []
        for rs in itertools.combinations(range(len(rows)), rho):
            for cs in itertools.combinations(range(d), rho):
                M = [[[-rows[i][1][j], rows[i][0][j]] for j in cs] for i in rs]
                val = det_poly(M)
                if not (len(val) == 1 and val[0] == 0):
                    polys.append(val)
        if not polys:
            continue
        g = polys[0]
        for q in polys[1:]:
            g = pgcd(g, q)
        b5 = (len(g) == 1 and g[0] != 0)
        dstar = max(len(p) - 1 for p in polys)
        N = len(polys)
        total += 1
        for D, tag in [(2 * dstar * (N - 1), 'correct'), (2 * rho * (N - 1), 'loose')]:
            rk, rows_ = bezout_full_rank(polys, dstar, D)
            full = (rk == rows_)
            if tag == 'correct' and full == b5:
                ok_correct += 1
            if tag == 'loose' and full != b5:
                bad_loose += 1
    print(f"样本 {total}")
    print(f"  D = 2*d_*(N-1)（正确）: (5b) <=> M_D 满射 的一致数 = {ok_correct}/{total}")
    print(f"  D = 2*rho*(N-1)（松上界）: 出现不一致的样本数 = {bad_loose}/{total}")


if __name__ == '__main__':
    main()
