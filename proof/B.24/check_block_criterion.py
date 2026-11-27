#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""check_block_criterion.py -- 块判据与 q=omega+1 特征空间定理的精确算例检验

验证对象（专家 48 号答复 §3/§4/§5 确认的结果；本脚本只给算例，不是证明）:

  (C1) 块判据. 设 H: C^k -> C^q 满足 rank H = omega, H_A = Z H. 令
       P(lambda) = lambda H - H_A. 则
           gcd{ omega-阶极大子式 of P } 非常数
       <=> 存在 0 != y in ker B 使 A y in C y,
       其中 Z = (A; B) 是 Z 在 W = im H 与补空间 W' 上的块（W' 任选）.

  (C2) q = omega: 恒坏（复域上 A 必有特征向量）.
  (C3) q >= 2 omega 且 B 满列秩: 恒好.
  (C4) omega = 1: 坏 <=> rank[H H_A] = 1（好 <=> 谱判据 rank[H H_A] = 2）.
  (C5) q = omega+1 的一般特征空间定理:
           好 <=> 每个特征空间一维, 且 B 在每条特征线上非零.

  (C6) n=4 全阶障碍实例在 q=4 处的失败（不可见特征向量 e_2 +- e_3）.

方法: 纯 Fraction 精确算术; 随机生成实例, 逐例先断言基本不变量
      (形状 / rank H / ker H <= ker H_A), 再比较两个独立的判据.
      不做薄集采样, 不调用浮点.

注意: 验证 != 证明. 本脚本检验的是上述恒等式在具体实例上的成立,
      不替代 B.24 卷宗里的纸面证明.
"""
from fractions import Fraction
from itertools import combinations, permutations
import random
import sys


# ---------------------------------------------------------------- 多项式
def ptrim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def pdeg(p):
    return len(ptrim(p)) - 1


def padd(a, b):
    n = max(len(a), len(b))
    out = [Fraction(0)] * n
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return ptrim(out)


def psub(a, b):
    return padd(a, [(-x) for x in b])


def pmul(a, b):
    if not a or not b:
        return []
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j, y in enumerate(b):
            out[i + j] += x * y
    return ptrim(out)


def pdivmod(a, b):
    a = ptrim(a)
    b = ptrim(b)
    if not b:
        raise ZeroDivisionError('polynomial division by zero')
    q = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and a:
        d = a[-1] / b[-1]
        shift = len(a) - len(b)
        q[shift] = d
        for i, y in enumerate(b):
            a[shift + i] -= d * y
        a = ptrim(a)
    return ptrim(q), a


def pgcd(a, b):
    a, b = ptrim(a), ptrim(b)
    while b:
        _, r = pdivmod(a, b)
        a, b = b, ptrim(r)
    if a:
        lead = a[-1]
        a = [x / lead for x in a]
    return a


def minors_of_pencil(M, omega):
    """M: q x k 的矩阵, 元素是多项式; 返回全部 omega 阶子式（Ω x Ω, 行/列各选 omega）。"""
    q = len(M)
    k = len(M[0]) if q else 0
    out = []
    for rows in combinations(range(q), omega):
        for cols in combinations(range(k), omega):
            sub = [[M[i][j] for j in cols] for i in rows]
            out.append(det_poly(sub))
    return out


def det_poly(M):
    n = len(M)
    if n == 0:
        return [Fraction(1)]
    total = []
    for perm in permutations(range(n)):
        # 逆序数定符号
        inv = 0
        for i in range(n):
            for j in range(i + 1, n):
                if perm[i] > perm[j]:
                    inv += 1
        term = [Fraction(-1 if inv % 2 else 1)]
        for i in range(n):
            term = pmul(term, M[i][perm[i]])
            if not term:
                break
        total = padd(total, term)
    return ptrim(total)


def gcd_degree(minors):
    # gcd(0, f) = f; 只有「全部子式都是零多项式」才得到空列表（处处秩降）。
    g = []
    for m in minors:
        g = pgcd(g, m)
    if not g:
        return None  # 全部子式为 0: 处处秩降
    return pdeg(g)


def is_bad(minors):
    d = gcd_degree(minors)
    return True if d is None else d >= 1


# ---------------------------------------------------------------- 线性代数
def rref(M):
    A = [[Fraction(x) for x in row] for row in M]
    m = len(A)
    n = len(A[0]) if m else 0
    pivots = []
    r = 0
    for c in range(n):
        p = None
        for i in range(r, m):
            if A[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        pivots.append(c)
        r += 1
        if r == m:
            break
    return A, pivots


def rank(M):
    if not M or not M[0]:
        return 0
    return len(rref(M)[1])


def matmul(A, B):
    m, n, p = len(A), len(A[0]), len(B[0])
    assert len(B) == n
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(p)] for i in range(m)]


def inv(M):
    n = len(M)
    A = [[Fraction(x) for x in row] for row in M]
    I = [[Fraction(1 if i == j else 0) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next(i for i in range(c, n) if A[i][c] != 0)
        A[c], A[p] = A[p], A[c]
        I[c], I[p] = I[p], I[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        I[c] = [x / pv for x in I[c]]
        for i in range(n):
            if i != c and A[i][c] != 0:
                f = A[i][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[c])]
                I[i] = [x - f * y for x, y in zip(I[i], I[c])]
    return I


def unit(q, i):
    return [Fraction(1 if j == i else 0) for j in range(q)]


def rank_cols(cols):
    """cols: 一组 q 维列向量; 返回它们的秩."""
    if not cols:
        return 0
    M = [[cols[j][i] for j in range(len(cols))] for i in range(len(cols[0]))]
    return rank(M)


def rand_mat(r, c, rng, lo=-3, hi=3):
    return [[Fraction(rng.randint(lo, hi)) for _ in range(c)] for _ in range(r)]


# ---------------------------------------------------------------- 构造与判定
def make_instance(q, k, omega, rng):
    """生成 rank H = omega 的 H = U V, 以及 H_A = Z H (自动 ker H <= ker H_A)."""
    U = rand_mat(q, omega, rng)
    V = rand_mat(omega, k, rng)
    H = matmul(U, V)
    if rank(H) != omega:
        return None
    Z = rand_mat(q, q, rng)
    HA = matmul(Z, H)
    return H, HA


def block_decomposition(H, HA, omega):
    """把诱导映射 Z 写成 W/W' 分量的块 (A; B)."""
    q = len(H)
    k = len(H[0])
    cols = [[H[i][j] for i in range(q)] for j in range(k)]
    basis, chosen = [], []
    for j, c in enumerate(cols):
        if rank_cols(basis + [c]) > len(basis):
            basis.append(c)
            chosen.append(j)
        if len(basis) == omega:
            break
    assert len(basis) == omega
    Mcols = [list(c) for c in basis]
    while len(Mcols) < q:
        added = False
        for i in range(q):
            cand = unit(q, i)
            if rank_cols(Mcols + [cand]) > len(Mcols):
                Mcols.append(cand)
                added = True
                break
        assert added
    M = [[Mcols[j][i] for j in range(q)] for i in range(q)]
    assert rank(M) == q
    Minv = inv(M)
    Zmat = [[HA[i][chosen[j]] for j in range(omega)] for i in range(q)]
    C = matmul(Minv, Zmat)
    return [row[:] for row in C[:omega]], [row[:] for row in C[omega:]]


def original_bad(H, HA, omega):
    q, k = len(H), len(H[0])
    P = [[[-HA[i][j], H[i][j]] for j in range(k)] for i in range(q)]
    return is_bad(minors_of_pencil(P, omega))


def block_bad(A, B, omega):
    """块坐标下 (q x omega) 的铅笔 [(A - lambda I); B] 的极大子式 gcd 是否非常数."""
    q = omega + len(B)
    M = []
    for i in range(omega):
        row = []
        for j in range(omega):
            entry = [A[i][j]]
            if i == j:
                entry = psub(entry, [Fraction(0), Fraction(1)])
            row.append(entry)
        M.append(row)
    for i in range(len(B)):
        M.append([[B[i][j]] for j in range(omega)])
    return is_bad(minors_of_pencil(M, omega))


def matrices(H, HA):
    return H, HA


# ---------------------------------------------------------------- 检验组
def check_C1(rng, trials=200):
    """块判据: 原铅笔的极大子式 gcd vs 块判据."""
    n_ok = 0
    n_bad = 0
    for _ in range(trials):
        omega = rng.randint(1, 3)
        q = rng.randint(omega, min(5, omega + 2))
        k = rng.randint(omega, min(5, omega + 2))
        inst = make_instance(q, k, omega, rng)
        if inst is None:
            continue
        H, HA = inst
        assert rank(H) == omega, 'rank H != omega'
        stack = H + HA
        assert rank(stack) == omega, 'ker H not contained in ker H_A'
        A, B = block_decomposition(H, HA, omega)
        b1 = original_bad(H, HA, omega)
        b2 = block_bad(A, B, omega)
        assert b1 == b2, ('block criterion mismatch', q, k, omega, b1, b2)
        n_ok += 1
        n_bad += int(b1)
    print(f'[C1] block criterion: {n_ok}/{n_ok} agree  (bad cases {n_bad})')
    return n_ok


def check_C2(rng, trials=60):
    """q = omega: 恒坏."""
    n = 0
    for _ in range(trials):
        omega = rng.randint(1, 3)
        q = k = omega
        inst = make_instance(q, k, omega, rng)
        if inst is None:
            continue
        H, HA = inst
        A, B = block_decomposition(H, HA, omega)
        assert B == [], 'B should have zero rows when q == omega'
        assert block_bad(A, B, omega), 'q=omega should be bad'
        assert original_bad(H, HA, omega), 'q=omega original side should be bad'
        n += 1
    print(f'[C2] q=omega always bad: {n}/{n}')
    return n


def check_C3(rng, trials=80):
    """q >= 2 omega 且 rank B = omega: 恒好."""
    n = 0
    for _ in range(trials):
        omega = rng.randint(1, 2)
        q = rng.randint(2 * omega, 2 * omega + 2)
        k = rng.randint(omega, omega + 2)
        inst = make_instance(q, k, omega, rng)
        if inst is None:
            continue
        H, HA = inst
        A, B = block_decomposition(H, HA, omega)
        if rank(B) != omega:
            continue
        assert not block_bad(A, B, omega), 'full-column-rank B should be good'
        assert not original_bad(H, HA, omega), 'original side should be good'
        n += 1
    print(f'[C3] q>=2omega & rank B=omega => good: {n}/{n}')
    return n


def check_C4(rng, trials=100):
    """omega = 1: 坏 <=> rank[H H_A] = 1."""
    n = 0
    for _ in range(trials):
        q = rng.randint(2, 5)
        k = rng.randint(1, 4)
        inst = make_instance(q, k, 1, rng)
        if inst is None:
            continue
        H, HA = inst
        HH = [H[i] + HA[i] for i in range(q)]   # 横向拼接 [H | H_A]，q x 2k
        good = (rank(HH) == 2)
        bad = original_bad(H, HA, 1)
        assert bad == (not good), ('omega=1 criterion mismatch', q, k)
        n += 1
    print(f'[C4] omega=1: bad <=> rank[H H_A]=1: {n}/{n}')
    return n


def check_C5(rng):
    """q = omega+1 的一般特征空间定理（结构化 A）. """
    total = 0

    # (i) 互异对角: 好 <=> B 的每个分量非零
    for omega in (2, 3):
        for _ in range(40):
            diag = rng.sample(range(-4, 5), omega)
            A = [[Fraction(diag[i] if i == j else 0) for j in range(omega)] for i in range(omega)]
            B = [[Fraction(rng.choice([0, 1, -2, 3])) for _ in range(omega)]]
            truth = all(x != 0 for x in B[0])
            assert block_bad(A, B, omega) == (not truth), ('distinct diag mismatch', omega, B)
            total += 1

    # (ii) A = mu I: 恒坏
    for omega in (2, 3):
        for _ in range(20):
            mu = rng.randint(-2, 2)
            A = [[Fraction(mu if i == j else 0) for j in range(omega)] for i in range(omega)]
            B = [[Fraction(rng.randint(-2, 2)) for _ in range(omega)]]
            assert block_bad(A, B, omega), ('scalar A should be bad', omega)
            total += 1

    # (iii) Jordan 块 J_omega(0): 特征空间 span{e_1} 一维, 好 <=> B[0] != 0
    for omega in (2, 3):
        for _ in range(40):
            A = [[Fraction(1 if j == i + 1 else 0) for j in range(omega)] for i in range(omega)]
            B = [[Fraction(rng.choice([0, 1, -1])) for _ in range(omega)]]
            assert block_bad(A, B, omega) == (B[0][0] == 0), ('Jordan mismatch', omega, B)
            total += 1

    # (iv) A = 0 (omega>=2): 特征空间整空间, 恒坏
    for omega in (2, 3):
        for _ in range(20):
            A = [[Fraction(0) for _ in range(omega)] for _ in range(omega)]
            B = [[Fraction(rng.randint(-2, 2)) for _ in range(omega)]]
            assert block_bad(A, B, omega), ('zero A should be bad', omega)
            total += 1

    print(f'[C5] q=omega+1 eigenspace theorem: {total}/{total}')
    return total


def check_C6(rng, trials=100):
    """n=4 全阶障碍实例: q=4 时对任意可逆 L, (5b) 在 lambda=+1 或 -1 失败."""
    n = 4
    C = [[Fraction(1 if j == 0 else 0) for j in range(n)]]
    L0 = [[Fraction(1 if j == 2 else 0) for j in range(n)]]
    A = [
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
    ]
    A = [[Fraction(x) for x in row] for row in A]
    CA = matmul(C, A)  # 1 x 4
    pairs = [(Fraction(1), [Fraction(0), Fraction(1), Fraction(1), Fraction(0)]),   # v+ = e2+e3
             (Fraction(-1), [Fraction(0), Fraction(1), Fraction(-1), Fraction(0)])]  # v- = e2-e3
    n_ok = 0
    for _ in range(trials):
        R = rand_mat(n - 1, n, rng)
        L = L0 + R
        if rank(L) != n:
            continue
        for lam, v in pairs:
            # 1) v 确是该特征值的特征向量
            Av = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
            assert all(Av[i] == lam * v[i] for i in range(n)), 'eigenpair mismatch'
            # 2) C v = CA v = 0
            assert sum(C[0][j] * v[j] for j in range(n)) == 0
            assert sum(CA[0][j] * v[j] for j in range(n)) == 0
            # 3) 左手矩阵 [lam L - L A; CA; C] 的秩 <= 3 (它把 v 送到 0)
            M = []
            for i in range(n):
                M.append([lam * L[i][j] - sum(L[i][t] * A[t][j] for t in range(n)) for j in range(n)])
            M.append(CA[0][:])
            M.append(C[0][:])
            assert rank(M) <= 3, 'left matrix rank should be <= 3'
            # 4) v 属于其核
            assert all(sum(M[i][j] * v[j] for j in range(n)) == 0 for i in range(len(M)))
        # 右手秩 = 4 (L 可逆)
        assert rank(L) == 4
        n_ok += 1
    print(f'[C6] n=4 obstruction at q=4: {n_ok}/{n_ok}')
    return n_ok


def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 20261108
    rng = random.Random(seed)
    total = 0
    total += check_C1(rng, 200)
    total += check_C2(rng, 60)
    total += check_C3(rng, 80)
    total += check_C4(rng, 100)
    total += check_C5(rng)
    total += check_C6(rng, 100)
    print(f'ALL CHECKS PASSED  (total instances: {total}, seed={seed})')


if __name__ == '__main__':
    main()
