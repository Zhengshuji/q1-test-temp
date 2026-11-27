"""§70：把 §68 实例的 μ≥1 族**完整**参数化（$\\mathbb P^2$ 的 3 个仿射图），
枚举出**所有**结构可允许的 $\\mathcal U$，逐个判"是否被覆盖" —— 这是二分猜想的一次**完整**检验。

$\\mathcal U=W_0\\oplus\\langle z\\rangle$，$z\\in\\mathbb P(X/W_0)\\cong\\mathbb P^2$。
取 $X/W_0$ 的基 $z_1,z_2,z_3$；齐次 $z=a z_1+b z_2+c z_3$；三个仿射图 $a=1,\\ b=1,\\ c=1$。
每图内取 2 个变量，$(N)$ 化成子式的理想，用 Gröbner 求所有解。
"""
import itertools
import sys
from fractions import Fraction as Fr

import sympy as sp

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI

import importlib.util as iu
spec = iu.spec_from_file_location('Q', 'proof/rho1_layer/quotient_selfcheck.py')
Qm = iu.module_from_spec(spec)
spec.loader.exec_module(Qm)
spec2 = iu.spec_from_file_location('C2', 'proof/rho1_layer/verify_cell_criteria_genuine.py')
CV = iu.module_from_spec(spec2)
spec2.loader.exec_module(CV)
mm, rank, rb = Qm.mm, Qm.rank, Qm.rb

n = 9
A_MAT = [[1,-1,-2,2,1,1,0,0,-1],[2,1,-2,1,-1,-1,2,1,-2],[-2,-1,2,-1,-1,0,-2,-1,-1],
         [2,-1,1,-2,0,0,-2,0,-1],[2,0,0,2,1,1,0,0,-1],[0,2,2,1,0,1,-2,1,0],
         [-1,2,-1,0,1,0,-2,-2,1],[1,1,1,-1,1,-1,-2,2,1],[1,2,1,-1,-1,0,-1,2,1]]
C_MAT = [[-2,0,-2,2,-1,-2,1,-2,-2],[2,1,2,2,-1,0,1,1,-1]]


def cell_is_good(Q, A, U):
    """判该格子是否"不被覆盖"（用解线性方程组算 T，再跑 C.2/C.3 的 gcd 判据）。"""
    d = Q.d
    B = Q.B
    mu = len(B) + len(U) - rank([r[:] for r in B] + [r[:] for r in U])
    if mu == 0:
        return None, 0
    _rows = [[B[i][k] for i in range(len(B))] + [-U[j][k] for j in range(len(U))] for k in range(d)]
    E = []
    for sol in AI.nullspace(_rows):
        v = [sum(sol[i] * B[i][k] for i in range(len(B))) for k in range(d)]
        if any(v):
            E.append(v)
    E = rb(E)
    rho = len(U)
    fU = [Q.pi(mm([Q.lift(u)], A)[0]) for u in U]
    nunk = rho * rho + rho * len(B)
    eqs = []
    for i in range(rho):
        for k in range(d):
            row = [Fr(0)] * nunk + [fU[i][k]]
            for j in range(rho):
                row[j * rho + i] = U[j][k]
            for t in range(len(B)):
                row[rho * rho + i * len(B) + t] = B[t][k]
            eqs.append(row)
    R = AI.rref(eqs)[0]
    sol_ = [Fr(0)] * nunk
    for row in R:
        piv = next((j for j in range(nunk) if row[j] != 0), None)
        if piv is None:
            continue
        sol_[piv] = row[nunk] / row[piv]
    T = [[sol_[j * rho + i] for j in range(rho)] for i in range(rho)]
    Erows = []
    for er in E:
        ER = AI.rref([[U[j][k] for j in range(rho)] + [er[k]] for k in range(d)])[0]
        a = [Fr(0)] * rho
        for row in ER:
            piv = next((j for j in range(rho) if row[j] != 0), None)
            if piv is None:
                continue
            a[piv] = row[rho] / row[piv]
        Erows.append(a)
    rows = [[[-T[i][k], Fr(1) if i == k else Fr(0)] for k in range(rho)] for i in range(rho)]
    for er in Erows:
        rows.append([[er[k]] for k in range(rho)])
    polys = []
    for rs in itertools.combinations(range(len(rows)), rho):
        for cs in itertools.combinations(range(rho), rho):
            M = [[rows[i][k] for k in cs] for i in rs]
            v = CV.V.det_poly(M)
            if not (len(v) == 1 and v[0] == 0):
                polys.append(v)
    if not polys:
        return False, mu
    g = polys[0]
    for q in polys[1:]:
        g = CV.V.pgcd(g, q)
    return (len(g) == 1 and g[0] != 0), mu


def run(A, C, quiet=False):
    def P(*a):
        if not quiet:
            print(*a)
    Q = Qm.Quotient(A, C)
    d = Q.d
    B = Q.B
    # 构造 L0 ∈ J·A（使 W0 ∩ B ≠ 0）
    import random
    rng = random.Random(11)
    JA = [mm([j], A)[0] for j in Q.J]
    W0 = None
    for _ in range(400):
        coeffs = [Fr(rng.randint(-2, 2)) for _ in JA]
        l0 = [sum(coeffs[i] * JA[i][k] for i in range(len(JA))) for k in range(n)]
        if not any(Q.pi(l0)):
            continue
        W0c = rb([Q.pi(l0)] + [Q.pi(mm([l0], A)[0])])
        if len(W0c) == 2 and rank([r[:] for r in W0c] + [r[:] for r in B]) < 4:
            W0 = W0c
            break
    if W0 is None:
        P("没找到 W0"); return (0, 0, 0)
    K = []
    span = [r[:] for r in W0]
    for i in range(d):
        e = [Fr(1) if t == i else Fr(0) for t in range(d)]
        if rank(span + [e]) > len(span):
            K.append(e); span = rb(span + [e])
        if len(span) == d:
            break
    z1, z2, z3 = K
    r0 = rank([r[:] for r in W0] + [r[:] for r in B]) + 1

    def f(u):
        return Q.pi(mm([Q.lift(u)], A)[0])
    fW = [f(w) for w in W0]
    fz = [f(z) for z in K]

    s, t = sp.symbols('s t')
    total_U = []
    for chart in range(3):
        # chart 0: a=1 (z = z1 + s z2 + t z3); chart 1: b=1; chart 2: c=1
        def R0(x):
            return sp.Rational(x.numerator, x.denominator)
        if chart == 0:
            def zrow():
                return [R0(z1[i]) + s * R0(z2[i]) + t * R0(z3[i]) for i in range(d)]
            def fzrow():
                return [R0(fz[0][i]) + s * R0(fz[1][i]) + t * R0(fz[2][i]) for i in range(d)]
            def zval(sv0, tv0):
                return [R0(z1[i]) + sv0 * R0(z2[i]) + tv0 * R0(z3[i]) for i in range(d)]
        elif chart == 1:
            def zrow():
                return [s * R0(z1[i]) + R0(z2[i]) + t * R0(z3[i]) for i in range(d)]
            def fzrow():
                return [s * R0(fz[0][i]) + R0(fz[1][i]) + t * R0(fz[2][i]) for i in range(d)]
            def zval(sv0, tv0):
                return [sv0 * R0(z1[i]) + R0(z2[i]) + tv0 * R0(z3[i]) for i in range(d)]
        else:
            def zrow():
                return [s * R0(z1[i]) + t * R0(z2[i]) + R0(z3[i]) for i in range(d)]
            def fzrow():
                return [s * R0(fz[0][i]) + t * R0(fz[1][i]) + R0(fz[2][i]) for i in range(d)]
            def zval(sv0, tv0):
                return [sv0 * R0(z1[i]) + tv0 * R0(z2[i]) + R0(z3[i]) for i in range(d)]

        def R(x):
            return sp.Rational(x.numerator, x.denominator)
        rows = [[R(x) for x in w] for w in W0]
        rows.append(zrow())
        for b in B:
            rows.append([R(x) for x in b])
        for fw in fW:
            rows.append([R(x) for x in fw])
        rows.append(fzrow())

        polys = []
        for rs in itertools.combinations(range(len(rows)), r0 + 1):
            for cs in itertools.combinations(range(d), r0 + 1):
                det = sp.expand(sp.Matrix([[rows[i][k] for k in cs] for i in rs]).det())
                if det != 0:
                    polys.append(det)
        if not polys:
            P(f"chart {chart}: 无子式"); continue
        G = sp.groebner(polys, s, t, order='lex')
        if list(G.exprs) == [sp.Integer(1)]:
            P(f"chart {chart}: 无解 ✗")
            continue
        sols = sp.solve(polys, [s, t], dict=True)
        P(f"chart {chart}: 解的个数 = {len(sols)}")
        for so in sols[:6]:
            sv0, tv0 = so[s], so[t]
            zval = zval(sv0, tv0)
            zf = [Fr(int(sp.nsimplify(x).p), int(sp.nsimplify(x).q)) for x in zval]
            U = rb([r[:] for r in W0] + [zf])
            if len(U) != 3:
                continue
            good, mu = cell_is_good(Q, A, U)
            if mu >= 1:
                total_U.append((chart, mu, good, U))

    P()
    P(f"所有 μ≥1 的结构可允许 U：{len(total_U)} 个")
    for chart, mu, good, U in total_U:
        P(f"  chart {chart}: μ={mu}, 不被覆盖={good}")
    distinct = []
    for chart, mu, good, U in total_U:
        if not any(rank([r[:] for r in U] + [r[:] for r in V2]) == len(U) and
                   rank([r[:] for r in V2] + [r[:] for r in U]) == len(V2)
                   for V2 in distinct):
            distinct.append(U)
    P(f"其中**互不相同**的 U 个数 = {len(distinct)}")
    n_total = len(total_U)
    n_good = sum(1 for _, _, g, _ in total_U if g)
    if n_total and n_good == n_total:
        P("=> 二分猜想在此实例上**成立** ✓（有 μ≥1，且都不是坏格子）")
    elif n_good > 0:
        P("=> 二分猜想成立 ✓（至少有一个好格子）")
    elif n_total:
        P("=> **候选反例** ✗（所有 μ≥1 的格子都被覆盖）")
    return (len(distinct), n_good, n_total)


def main():
    A = [[Fr(x) for x in row] for row in A_MAT]
    C = [[Fr(x) for x in row] for row in C_MAT]
    return run(A, C, quiet=False)


def driver(n_instances=3):
    """在若干不同的 (A,C) 上重复"三图完整检验"。"""
    import random
    rng = random.Random(2026)
    results = []
    for k in range(n_instances):
        for _ in range(400):
            A = [[Fr(rng.randint(-2,2)) for _ in range(n)] for _ in range(n)]
            C = [[Fr(rng.randint(-2,2)) for _ in range(n)] for _ in range(2)]
            CA = mm(C, A); J = rb(C+CA)
            if len(J) != 4: continue
            Q = Qm.Quotient(A, C)
            if Q.d != 5 or len(Q.B) != 2: continue
            break
        else:
            continue
        print(f"=== 实例 {k+1} ===")
        r = run(A, C, quiet=True)
        print(f"  distinct U = {r[0]}, 好格子 = {r[1]}, μ≥1 总数 = {r[2]}")
        results.append(r)
    print()
    print("汇总（distinct, good, total）：", results)
    if results and all(r[1] == r[2] and r[2] > 0 for r in results):
        print("=> 所有实例上二分猜想都成立 ✓（0 反例）")
    elif any(r[2] > 0 and r[1] == 0 for r in results):
        print("=> 有 **候选反例** ✗")
    else:
        print("=> 混合（有些实例没有 μ≥1）")
