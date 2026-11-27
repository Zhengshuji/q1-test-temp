"""检验 §13 的猜想（Q 侧，抽象层模型）：

  "型层被完全覆盖（所有 tau 都失败）时，各成员的 gcd 次数是否**恒定**？"

在抽象层模型里（行 = lam*u_i - (T u_i + beta(tau_i))，再加 -beta(h)）：
  * 所有行都在 U 里（dim rho）=> rank <= rho 自动；
  * 取全部 rho x rho 子式，gcd 为非零常数 <=> (5b) 成立；
  * gcd 的次数 = 公共根个数（计重数）。
对每个实例抽 8 个 tau，记录 gcd 次数；分类：
  - "有成功"（某个 tau 的 gcd 次数 = 0 且非常数零）=> 层可行（该 (U,H)）
  - "全失败"  => 该 (U,H) 被覆盖（在抽样意义上）
再检查：全失败的实例里，gcd 次数是否全部相等。
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


def gcd_data(rows, rho, d):
    polys = []
    for rs in itertools.combinations(range(len(rows)), rho):
        for cs in itertools.combinations(range(d), rho):
            M = [[[-rows[i][1][j], rows[i][0][j]] for j in cs] for i in rs]
            v = det_poly(M)
            if not (len(v) == 1 and v[0] == 0):
                polys.append(v)
    if not polys:
        return None, None
    g = polys[0]
    for q in polys[1:]:
        g = pgcd(g, q)
    return len(g) - 1, (len(g) == 1 and g[0] != 0)


def main():
    rng = random.Random(987654)
    stats = {'all_fail': 0, 'some_ok': 0}
    const_in_all_fail = 0
    nonconst_in_all_fail = 0
    examples = []
    import os
    NT = int(os.environ.get('NTRIALS', '400'))
    for trial in range(NT):
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
        degs = []
        any_ok = False
        for _t in range(8):
            rr = []
            for i in range(rho):
                tv = [sum(Fr(rng.randint(-2, 2)) * b[k] for b in BU) for k in range(d)]
                rr.append((U[i], [Tu[i][k] + tv[k] for k in range(d)]))
            rr.append(([Fr(0)] * d, list(w)))
            gd, ok = gcd_data(rr, rho, d)
            if gd is None:
                degs.append(None)
                continue
            degs.append(gd)
            if ok:
                any_ok = True
        if any_ok:
            stats['some_ok'] += 1
        else:
            stats['all_fail'] += 1
            vals = [g for g in degs if g is not None]
            if vals and len(set(vals)) == 1:
                const_in_all_fail += 1
            else:
                nonconst_in_all_fail += 1
                if len(examples) < 3:
                    examples.append(vals)
    print(f"全失败实例: {stats['all_fail']}；有成功实例: {stats['some_ok']}")
    print(f"  全失败中 gcd 次数**恒定**: {const_in_all_fail}")
    print(f"  全失败中 gcd 次数**不恒定**: {nonconst_in_all_fail}")
    for e in examples:
        print("   不恒定例子:", e)


if __name__ == '__main__':
    main()
