"""探测 (rho,c) = (3,1) 层的坏集几何：固定 U 与 H 时，Bad 何时等于 A？

背景（专家建议的"目标 2"）：rho=2 时容器唯一 ⟹ Bad 仿射 ⟹ 可判；
rho=3 时容器（dim ≤ 2、含 w=beta(h)）不唯一 ⟹ Bad 是"仿射集的并/投影" ⟹ 结构未知。
本脚本**固定 U 与 H**，在仿射集 A 上抽样 tau，精确判定 (5b) 是否成立，
从而区分两种情形：**Bad = A**（所有 tau 都失败）与 **Bad ≠ A**（存在成功的 tau）。

模型（对层是忠实的）：
  X = Q^d；U ⊂ X（dim 3）；T: X → X 且 T(U) ⊆ U（即 (5a) 自动成立）；
  B ⊂ X（dim m）；β: Q^m → B 取同构；h 使 β(h) = w ∈ B ∩ U（dim w = 1，即 c = 1）。
  A = { tau : β(tau_i) ∈ B ∩ U  (i=1,2,3) }（线性子空间）。
  铅笔行： lam*u_i - (T(u_i) + β(tau_i))（i=1,2,3）与 -w（共 4 行，d 列）。
  (5b) <=> 对一切 lam，秩 = 3 <=> 所有 4x4 子式恒为零（自动：行都在 U 里）且 3x3 子式的 gcd 为非零常数。
精确有理数算术。
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


def cond_5b(rows, rho, d):
    """rank = rho 对一切 lam：3x3 子式的 gcd 为非零常数（4x4 子式自动为零，因行都在 U 里）。"""
    mins = []
    for rs in itertools.combinations(range(len(rows)), rho):
        for cs in itertools.combinations(range(d), rho):
            M = [[[-rows[i][1][j], rows[i][0][j]] for j in cs] for i in rs]
            val = det_poly(M)
            if not (len(val) == 1 and val[0] == 0):
                mins.append(val)
    if not mins:
        return False
    g = mins[0]
    for m in mins[1:]:
        g = pgcd(g, m)
    return len(g) == 1 and g[0] != 0


def rand_vec(d, rng):
    while True:
        v = [Fr(rng.randint(-2, 2)) for _ in range(d)]
        if any(v):
            return v


def row_basis(vs):
    return AI.row_basis(vs) if vs else []


def inspan(basis, v):
    if not basis:
        return all(x == 0 for x in v)
    return AI.rank([r[:] for r in basis] + [v[:]]) == AI.rank([r[:] for r in basis])


def mat_vec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


def main():
    rng = random.Random(20261030)
    stat = {}
    for trial in range(400):
        d = rng.choice([3, 4, 5])
        # U：3 维
        U = row_basis([rand_vec(d, rng) for _ in range(6)])
        if len(U) < 3:
            continue
        U = U[:3]
        # T：在 U 的坐标下任意，其它随机；然后强制 T(U) ⊆ U
        T = [[Fr(rng.randint(-2, 2)) for _ in range(d)] for _ in range(d)]
        # 用 U 的坐标表示，构造保 U 的 T
        Cc = [[Fr(rng.randint(-2, 2)) for _ in range(3)] for _ in range(3)]
        T = [[Fr(0)] * d for _ in range(d)]
        # 选一个补基，使 T 在 (U, 补) 上分块
        comp = []
        for i in range(d):
            e = [Fr(1) if k == i else Fr(0) for k in range(d)]
            if not inspan(U + comp, e):
                comp.append(e)
            if len(comp) == d - 3:
                break
        basis = U + comp
        # T 在 U 上 = Cc*U，在 comp 上任意
        Dm = [[Fr(rng.randint(-2, 2)) for _ in range(d)] for _ in range(d)]
        for j, u in enumerate(U):
            img = [sum(Cc[i][j] * U[i][k] for i in range(3)) for k in range(d)]
            for k in range(d):
                T[k][j] = img[k]
        for j, cvec in enumerate(comp):
            img = mat_vec(Dm, cvec)
            for k in range(d):
                T[k][3 + j] = img[k]
        # B：m 维
        m = rng.choice([1, 2, 3, d])
        B = row_basis([rand_vec(d, rng) for _ in range(m + 2)])[:m]
        if len(B) < m:
            continue
        BU = [x for x in B if inspan(U, x)]
        if len(BU) < 1:
            continue
        # w ∈ B ∩ U
        w = BU[0]
        if not any(w):
            continue
        # A 的采样：tau_i ∈ span(B∩U)
        sample = 12
        succ = 0
        for _t in range(sample):
            rows = []
            for i in range(3):
                tv = [sum(Fr(rng.randint(-2, 2)) * b[k] for b in BU) for k in range(d)]
                Tu = mat_vec(T, U[i])
                rows.append((U[i], [Tu[k] + tv[k] for k in range(d)]))
            rows.append(([Fr(0)] * d, list(w)))
            if cond_5b(rows, 3, d):
                succ += 1
        key = (d, m, len(BU))
        st = stat.setdefault(key, [0, 0, 0])       # [全失败, 有成功, 实例数]
        st[2] += 1
        if succ == 0:
            st[0] += 1
        else:
            st[1] += 1
    print("(d, m, mu=dim(B∩U)) -> [Bad=A（全失败）, 有成功, 实例数]")
    mixed = 0
    for k in sorted(stat):
        a, b, n = stat[k]
        flag = "   <== 同一签名两种都有" if (a and b) else ""
        if a and b:
            mixed += 1
        print(f"  {k}: [{a}, {b}, {n}]{flag}")
    print(f"\n共 {len(stat)} 个签名；同一签名下两种情形都出现的有 {mixed} 个")


if __name__ == '__main__':
    main()
