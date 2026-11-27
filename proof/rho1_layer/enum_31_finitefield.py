"""在有限域 F_p 上**穷尽**判定候选反例实例的 (3,1) 层（p=3）。

为什么要有限域：整数的 Grassmannian 不可枚举，但 F_p 上的 4 维子空间是有限个（RREF 枚举）。
关键点：本实例的矩阵条目都是整数 ±1/0 ✓，把问题**模 p** 后仍是同一个组合实例；
"铅笔在 _F_p 的代数闭包上常秩" 与 "_C 上常秩" 用同一个 gcd 判据 ✓（gcd 在 F_p[lam] 里是否为非零常数）。

输出：
  * 枚举到的满足 (5a)、类型 (3,1)、且 V ⊇ row L0 的子空间个数；
  * 其中使 (5b) 成立的个数（**>0 就说明该实例的层可行 ⟹ C31 的候选反例被推翻**）。
"""
import io
import itertools
import json
import sys

P = 3


def inv(a):
    return pow(a % P, P - 2, P)


def rref(M):
    M = [[x % P for x in row] for row in M]
    r, c = len(M), len(M[0])
    piv = []
    i = 0
    for j in range(c):
        p = None
        for t in range(i, r):
            if M[t][j] % P:
                p = t
                break
        if p is None:
            continue
        M[i], M[p] = M[p], M[i]
        iv = inv(M[i][j])
        M[i] = [(x * iv) % P for x in M[i]]
        for t in range(r):
            if t != i and M[t][j] % P:
                f = M[t][j]
                M[t] = [(a - f * b) % P for a, b in zip(M[t], M[i])]
        piv.append(j)
        i += 1
        if i == r:
            break
    return M, piv


def rank(M):
    return len(rref(M)[1]) if M else 0


def vstack(*Ms):
    out = []
    for M in Ms:
        out.extend([list(r) for r in M])
    return out


def mm(X, Y):
    r, k, c = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) % P for j in range(c)] for i in range(r)]


def row_basis(M):
    R, piv = rref(M)
    return [R[i] for i in range(len(piv))]


def in_span(basis, v):
    if not basis:
        return all(x % P == 0 for x in v)
    return rank([r[:] for r in basis] + [v[:]]) == rank([r[:] for r in basis])


# ---------- 多项式（F_p[lam]） ----------
def ptrim(a):
    a = [x % P for x in a]
    while len(a) > 1 and a[-1] % P == 0:
        a.pop()
    return a


def pdivmod(a, b):
    a, b = ptrim(a), ptrim(b)
    inv_b = inv(b[-1])
    q = [0] * max(1, len(a) - len(b) + 1)
    r = a[:]
    while len(r) >= len(b) and not (len(r) == 1 and r[0] % P == 0):
        c = (r[-1] * inv_b) % P
        dd = len(r) - len(b)
        q[dd] = c
        for i, bi in enumerate(b):
            r[i + dd] = (r[i + dd] - c * bi) % P
        r = ptrim(r)
    return q, r


def pgcd(a, b):
    a, b = ptrim(a), ptrim(b)
    while not (len(b) == 1 and b[0] % P == 0):
        _, r = pdivmod(a, b)
        a, b = b, r
    return a


def pmul(a, b):
    o = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            o[i + j] = (o[i + j] + x * y) % P
    return ptrim(o)


def padd(a, b):
    o = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        o[i] = (o[i] + x) % P
    for i, y in enumerate(b):
        o[i] = (o[i] + y) % P
    return ptrim(o)


def det_poly(M):
    n = len(M)
    if n == 1:
        return ptrim(list(M[0][0]))
    acc = [0]
    for j in range(n):
        sub = [[M[i][k] for k in range(n) if k != j] for i in range(1, n)]
        term = pmul(M[0][j], det_poly(sub))
        if j % 2:
            term = [(-c) % P for c in term]
        acc = padd(acc, term)
    return ptrim(acc)


def cond_5b(L, A, C, n):
    CA = mm(C, A)
    LA = mm(L, A)
    base = vstack(L, CA, C)
    r0 = rank(base)
    q = len(L)
    Ppoly = []
    for i in range(q):
        Ppoly.append([[(-LA[i][j]) % P, L[i][j] % P] for j in range(n)])
    for M in (CA, C):
        for r in M:
            Ppoly.append([[x % P] for x in r])
    mins = []
    for rs in itertools.combinations(range(len(Ppoly)), r0):
        for cs in itertools.combinations(range(n), r0):
            M = [[Ppoly[rs[i]][cs[j]] for j in range(r0)] for i in range(r0)]
            val = det_poly(M)
            if not (len(val) == 1 and val[0] % P == 0):
                mins.append(val)
    if not mins:
        return False
    g = mins[0]
    for m in mins[1:]:
        g = pgcd(g, m)
    return len(g) == 1 and g[0] % P != 0


def cond_5a(L, A, C):
    CA = mm(C, A)
    LA = mm(L, A)
    return rank(vstack(LA, L, CA, C)) == rank(vstack(L, CA, C))


def main():
    d = json.load(io.open('proof/rho1_layer/candidate_c31_counterexample.json', encoding='utf-8'))[0]
    A = [[int(x) for x in r] for r in d['A']]
    C = [[int(x) for x in r] for r in d['C']]
    L0 = [[int(x) for x in r] for r in d['L0']]
    n = len(A)
    CA = mm(C, A)
    J = row_basis(vstack(C, CA))
    j = len(J)
    print(f"F_{P}: n={n}, dim J={j}")

    # 枚举所有 4 维子空间（RREF 唯一表示）
    count_type = 0
    count_feas = 0
    all_valid = []
    examples = []
    for pivots in itertools.combinations(range(n), 4):
        free = [c for c in range(n) if c not in pivots]
        for vals in itertools.product(range(P), repeat=4 * len(free)):
            M = [[0] * n for _ in range(4)]
            for i, pc in enumerate(pivots):
                M[i][pc] = 1
            idx = 0
            for i in range(4):
                for fc in free:
                    M[i][fc] = vals[idx]
                    idx += 1
            L = row_basis(M)
            if len(L) != 4:
                continue
            # V ⊇ row L0 ?
            if not all(in_span(L, r) for r in L0):
                continue
            # 类型 (3,1) ?
            rho = rank(vstack(L, CA, C)) - j
            c = len(L) + j - rank(vstack(L, J))
            if (rho, c) != (3, 1):
                continue
            if not cond_5a(L, A, C):
                continue
            count_type += 1
            b5 = cond_5b(L, A, C, n)
            if b5:
                count_feas += 1
                if len(examples) < 2:
                    examples.append(L)
            all_valid.append([[int(x) % P for x in r] for r in L] + [[1 if b5 else 0]])
    print(f"  满足 (5a) 且类型 (3,1)、V ⊇ row L0 的子空间: {count_type}")
    print(f"  其中 (5b) 成立: {count_feas}")
    import json as _json
    io.open('proof/rho1_layer/f3_18_candidates.json', 'w', encoding='utf-8', newline='\n').write(
        _json.dumps(all_valid, ensure_ascii=False))
    print(f"  已缓存 {len(all_valid)} 个候选到 proof/rho1_layer/f3_18_candidates.json")
    if count_feas:
        print("  => 该实例的层**可行** ⟹ C31 的候选反例被推翻 ✓")
        for L in examples:
            print("   例:", L)
    else:
        print("  => 在 F_3 的穷尽范围内**没有**可行解 ⟹ 候选反例被加强（但仍非 C 上的证明）")


if __name__ == '__main__':
    main()
