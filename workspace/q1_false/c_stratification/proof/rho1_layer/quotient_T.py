"""A' 第 1-2 步：商算子 T 的显式矩阵 + **自检** + 特征多项式与有理特征值。

X = C^n / J（J = row[C;CA]）。取 J 的基 + 补基 comp（d 个向量）；对 x ∈ C^n 用基底 (J, comp) 写坐标。
T(pi(x)) = pi(x A)；T 在 comp 坐标下的矩阵记为 Tm（d×d）。

自检（硬门槛）：随机取 V（若干行），令 U = pi(V)（用 comp 坐标表示），比较
    (a) T(U) ⊆ U
    (b) cond_5a_orig(A, C, V)   —— 直接对 C^n 里的 V 检验 (5a) = row(VA) ⊆ V + J
两者必须**逐例一致**；不一致就说明商坐标实现有 bug。
"""
import io
import json
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI


def mm(X, Y):
    r, k, c = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(c)] for i in range(r)]


def rref_solve(M, b):
    """解 M x = b（M 行数=方程数）；返回一个解或 None。"""
    r, c = len(M), len(M[0])
    aug = [list(M[i]) + [b[i]] for i in range(r)]
    R = AI.rref(aug)[0]
    for row in R:
        if all(x == 0 for x in row[:c]) and row[c] != 0:
            return None
    sol = [Fr(0)] * c
    for row in R:
        for k in range(c):
            if row[k] != 0:
                sol[k] = row[c] / row[k]
                break
    return sol


def quotient_data(A, C):
    n = len(A)
    CA = mm(C, A)
    J = AI.row_basis(C + CA)
    j = len(J)
    comp = []
    span = [r[:] for r in J]
    for i in range(n):
        e = [Fr(1) if k == i else Fr(0) for k in range(n)]
        if len(AI.row_basis(span + [e])) > len(span):
            comp.append(e)
            span = AI.row_basis(span + [e])
        if len(comp) == n - j:
            break
    basis = J + comp                    # n×n 的基（行）
    Binv = AI.inv([[basis[r][c] for r in range(n)] for c in range(n)])   # 注意：按列排
    # 坐标：x = sum a_i basis_i  <=>  a = Binv x
    def coords(x):
        return [sum(Binv[i][k] * x[k] for k in range(n)) for i in range(n)]

    # T 的矩阵：对 comp_k，T(pi(comp_k)) = pi(comp_k A)，取 comp 坐标
    Tm = [[Fr(0)] * len(comp) for _ in range(len(comp))]
    jpart_max = Fr(0)
    for k, cvec in enumerate(comp):
        y = mm([cvec], A)[0]
        a = coords(y)
        jpart = a[:j]
        cpart = a[j:]
        jpart_max = max(jpart_max, max(abs(v) for v in jpart))
        for i in range(len(comp)):
            Tm[i][k] = cpart[i]
    return dict(n=n, J=J, comp=comp, j=j, d=len(comp), Tm=Tm, coords=coords,
                jpart_max=jpart_max)


def main():
    d0 = json.load(io.open('proof/rho1_layer/candidate_c31_counterexample.json', encoding='utf-8'))[0]
    A = [[Fr(x) for x in r] for r in d0['A']]
    C = [[Fr(x) for x in r] for r in d0['C']]
    Q = quotient_data(A, C)
    n, j, d = Q['n'], Q['j'], Q['d']
    print(f"n={n}, dim J={j}, d={d}")
    print("T 的 J-分量最大绝对值（应为 0）:", Q['jpart_max'])
    print("Tm =")
    for r in Q['Tm']:
        print("   ", [str(x) for x in r])

    # ---- 自检：T(U) ⊆ U  与  (5a) 一致吗 ----
    rng = random.Random(999)
    bad = 0
    tested = 0
    for _t in range(300):
        k = rng.choice([2, 3, 4])
        rows = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(k)]
        V = AI.row_basis(rows)
        if len(V) != k:
            continue
        # U = pi(V) 在 comp 坐标下
        U = []
        for v in V:
            a = Q['coords'](v)
            U.append(a[j:])
        U = AI.row_basis(U)
        if len(U) != k:
            continue
        # (a) T(U) ⊆ U ?
        ok_a = True
        for u in U:
            Tu = [sum(Q['Tm'][i][t] * u[t] for t in range(d)) for i in range(d)]
            if AI.rank([r[:] for r in U] + [Tu]) > len(U):
                ok_a = False
                break
        # (b) (5a) ?
        ok_b = AI.cond_5a_orig(A, C, V)
        tested += 1
        if ok_a != ok_b:
            bad += 1
            if bad <= 3:
                print("  自检不一致！ U =", U, " T(U)⊆U =", ok_a, " (5a) =", ok_b)
    print(f"\n自检：{tested} 例，T(U)⊆U 与 (5a) 一致率 {tested - bad}/{tested}")

    # ---- 特征多项式与有理特征值 ----
    # det(lam I - Tm)，用多项式（系数升序）表示
    def ptrim(a):
        a = list(a)
        while len(a) > 1 and a[-1] == 0:
            a.pop()
        return a

    def pmul(a, b):
        o = [Fr(0)] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for jj, y in enumerate(b):
                o[i + jj] += x * y
        return ptrim(o)

    def psub(a, b):
        o = [Fr(0)] * max(len(a), len(b))
        for i, x in enumerate(a):
            o[i] += x
        for i, y in enumerate(b):
            o[i] -= y
        return ptrim(o)

    def det_poly(M):
        nn = len(M)
        if nn == 1:
            return ptrim(list(M[0][0]))
        acc = [Fr(0)]
        for jj in range(nn):
            sub = [[M[i][k] for k in range(nn) if k != jj] for i in range(1, nn)]
            term = pmul(M[0][jj], det_poly(sub))
            if jj % 2:
                term = [-c for c in term]
            if len(acc) < len(term):
                acc += [Fr(0)] * (len(term) - len(acc))
            for i, c in enumerate(term):
                acc[i] += c
        return ptrim(acc)

    M = [[ptrim([-Q['Tm'][i][jj], Fr(1)]) if i == jj else ptrim([-Q['Tm'][i][jj]])
          for jj in range(d)] for i in range(d)]
    cp = det_poly(M)
    print("char poly(T) =", [str(x) for x in cp])

    # 有理根（有理根定理：p/q，p | 常数项，q | 首项）
    def divisors(v):
        v = abs(v)
        if v == 0:
            return [1]
        out = []
        for i in range(1, int(v) + 1):
            if v % i == 0:
                out.append(i)
        return out

    lead = cp[-1]
    const = cp[0]
    L = 1
    for cc in cp:
        L = L * cc.denominator // __import__('math').gcd(L, cc.denominator)
    ints = [int(cc * L) for cc in cp]
    cands = set()
    for p in divisors(ints[0]):
        for q in divisors(ints[-1]):
            cands.add(Fr(p, q))
            cands.add(-Fr(p, q))
    roots = []
    for lam in sorted(cands):
        val = Fr(0)
        for cc in reversed(cp):
            val = val * lam + cc
        if val == 0:
            roots.append(lam)
    print("有理特征值:", [str(x) for x in roots])


if __name__ == '__main__':
    main()
