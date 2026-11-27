# ⚠️ 2026-10-30 接手者警告（已定位根因）：
#    ① 本脚本的 E 取成 "B∖U"（`[b for b in B if rank(U+[b])==len(U)]`），而格子里的 E 应是 **B∩U** ✗；
#    ② 判据行用的是 a（E 的方向），但 C.2 的最后一行应是 **w = β(h)** ✗。
#    该实例实际 **w = 0**（h = e5、π(e5A) = π(e6) = 0）⟹ 归 C.5（恒被覆盖），C.2 不适用。
#    正确的逐条复核见 verify_mu1_covered_instance.py（2026-10-30 已修，三组全部一致 ✓）。
"""§52.7 的实例上，把 **格子判据 C.2** 算出来，并与实测的 (5b) 比对。

实例：n=6；W = <e1,e2,e3> 是 A-不变块；A e5 = e6、A e6 = e1 + α e5 + β e6；
      C = L0 = e5；V = <e1,e2,e3,e5>（4 维）。
性质：dim V = 4、row(L0) ⊆ V、类型 (3,1)、μ = 1、(N)、(5a) 全 PASS；(5b) 失败。

本脚本自包含地实现 π / lift（不依赖别的模块的约定），并**每步断言维数**（纪律 14）。
"""
import itertools
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI

mm = None


def mul(X, Y, tag=''):
    assert X and Y and len(X[0]) == len(Y), f'mm 维数不符 {tag}: {len(X)}x{len(X[0])} * {len(Y)}x{len(Y[0]) if Y else 0}'
    return [[sum(X[i][t] * Y[t][j] for t in range(len(Y))) for j in range(len(Y[0]))]
            for i in range(len(X))]


def rank(M):
    return AI.rank([r[:] for r in M]) if M else 0


def rb(M):
    return AI.row_basis([r[:] for r in M]) if M else []


def complement(B, n):
    out, span = [], [r[:] for r in B]
    for i in range(n):
        e = [Fr(1) if j == i else Fr(0) for j in range(n)]
        if rank(span + [e]) > len(span):
            out.append(e)
            span = rb(span + [e])
        if len(span) == n:
            break
    return out


def build(alpha, beta):
    n = 6
    A = [[Fr(0)] * n for _ in range(n)]
    A[0][1] = Fr(1); A[1][2] = Fr(1); A[2][0] = Fr(1); A[2][1] = Fr(1)
    A[4][5] = Fr(1); A[5][0] = Fr(1); A[5][4] = Fr(alpha); A[5][5] = Fr(beta)
    A[3][3] = Fr(1)
    L0 = [[Fr(0), Fr(0), Fr(0), Fr(0), Fr(1), Fr(0)]]
    C = [list(L0[0])]
    return A, C, L0


def analyze(alpha, beta):
    n = 6
    A, C, L0 = build(alpha, beta)
    CA = mul(C, A, 'CA')
    J = rb(C + CA)
    j = len(J)
    K = complement(J, n)                 # X ≅ span(K)
    d = len(K)
    Lmat = J + K                         # n×n
    assert len(Lmat) == n
    Linv = AI.inv(Lmat)

    def to_x_coords(x):
        """x（C^n 坐标）-> (J 坐标, X 坐标)"""
        c = mul([x], Linv, 'to_x')[0]
        assert len(c) == n
        return c[:j], c[j:]

    def lift(u):
        """X 坐标 -> C^n 中的代表（落在 span(K) 里）"""
        assert len(u) == d
        a = [Fr(0)] * j + list(u)
        return [sum(a[i] * Lmat[i][k] for i in range(n)) for k in range(n)]

    def pi(x):
        return to_x_coords(x)[1]

    B = rb([pi(mul([jj], A, 'JA')[0]) for jj in J])
    e = [[Fr(1) if j2 == i else Fr(0) for j2 in range(n)] for i in range(n)]
    Wt = [e[0], e[1], e[2]]
    U = rb([pi(w) for w in Wt])
    V = rb([e[0], e[1], e[2], e[4]])
    E = [b for b in B if rank(U + [b]) == len(U)]
    mu = len(E)

    # 格子 T：**解线性方程组** f(u_i) = Σ_j T_{ji} u_j + Σ_k c_{ik} B_k
    # （不能用补空间坐标：U ∩ B ≠ 0 时坐标 ≠ 分量 —— 见 §53 的教训）
    fU = [pi(mul([lift(u)], A, 'f(u)')[0]) for u in U]
    dd = len(U)                      # 3（不是 d = dim X）
    nunk = dd * dd + dd * len(B)
    eqs = []
    for i in range(dd):
        for k in range(d):
            row = [Fr(0)] * nunk + [fU[i][k]]
            for j in range(dd):
                row[j * dd + i] = U[j][k]
            for t in range(len(B)):
                row[dd * dd + i * len(B) + t] = B[t][k]
            eqs.append(row)
    R = AI.rref(eqs)[0]
    sol = [Fr(0)] * nunk
    for row in R:
        piv = next((j for j in range(nunk) if row[j] != 0), None)
        if piv is None:
            continue
        sol[piv] = row[nunk] / row[piv]
    Trows = [[sol[j * dd + i] for j in range(dd)] for i in range(dd)]

    rho3 = dd
    # C.2 判据（mu = 1）：[λI - T; E] 的 (rho)×(rho) 子式 gcd
    Erows = []
    for er in E:
        eeqs = [[U[j][k] for j in range(dd)] + [er[k]] for k in range(d)]
        ER = AI.rref(eeqs)[0]
        a = [Fr(0)] * dd
        for row in ER:
            piv = next((j for j in range(dd) if row[j] != 0), None)
            if piv is None:
                continue
            a[piv] = row[dd] / row[piv]
        Erows.append(a)
    rows = [[[-Trows[i][k], Fr(1) if i == k else Fr(0)] for k in range(rho3)] for i in range(rho3)]
    for er in Erows:
        rows.append([[er[k]] for k in range(rho3)])

    # det_poly / pgcd 从 cell-criteria 模块借用
    import importlib.util as iu
    spec = iu.spec_from_file_location('C', 'proof/rho1_layer/verify_cell_criteria_genuine.py')
    CV = iu.module_from_spec(spec)
    spec.loader.exec_module(CV)

    polys = []
    for rs in itertools.combinations(range(len(rows)), rho3):
        for cs in itertools.combinations(range(rho3), rho3):
            M = [[rows[i][k] for k in cs] for i in rs]
            v = CV.V.det_poly(M)
            if not (len(v) == 1 and v[0] == 0):
                polys.append(v)
    g = polys[0]
    for q in polys[1:]:
        g = CV.V.pgcd(g, q)
    criterion_good = (len(g) == 1 and g[0] != 0)

    # 实测 (5b)
    def cond5b(V, A, C):
        CA2 = mul(C, A, 'ca')
        VA2 = mul(V, A, 'VA')
        base = V + CA2 + C
        r0 = rank(base)
        rows2 = [(V[i], VA2[i]) for i in range(len(V))]
        for r in CA2:
            rows2.append(([Fr(0)] * len(r), list(r)))
        for r in C:
            rows2.append(([Fr(0)] * len(r), list(r)))
        gg = None
        for rs in itertools.combinations(range(len(rows2)), r0):
            for cs in itertools.combinations(range(len(V[0])), r0):
                M = [[[-rows2[i][1][j], rows2[i][0][j]] for j in cs] for i in rs]
                val = CV.V.det_poly(M)
                if len(val) == 1 and val[0] == 0:
                    continue
                gg = val if gg is None else CV.V.pgcd(gg, val)
                if len(gg) == 1 and gg[0] != 0:
                    return True
        return False if gg is None else (len(gg) == 1 and gg[0] != 0)

    measured = cond5b(V, A, C)

    # 格子的自由度：给两个自由行各加一个 E 中的元素（τ ∈ E，E 是 1 维）
    # 需要把 E 抬回 C^n：E ⊂ X，取 lift(E 的基)
    any_good = False
    if mu >= 1:
        Ebasis = [lift(er) for er in E]
        for c1 in (Fr(-1), Fr(0), Fr(1)):
            for c2 in (Fr(-1), Fr(0), Fr(1)):
                rows3 = [list(e[0]), list(e[1]), list(e[2]), list(e[4])]
                # 自由行是 e1,e2（前两行）；第三行 e3 也自由？保守起见只动前两行
                for k in range(2):
                    for Eb in Ebasis:
                        coef = c1 if k == 0 else c2
                        rows3[k] = [rows3[k][t] + coef * Eb[t] for t in range(n)]
                V2 = rb(rows3)
                if len(V2) != 4:
                    continue
                if cond5b(V2, A, C):
                    any_good = True
                    break
            if any_good:
                break
    return dict(dimV=len(V), mu=mu, criterion_good=criterion_good, measured_5b=measured,
                any_good=any_good,
                rho=rank(V + CA + C) - j, c=len(V) + j - rank(V + J))


def main():
    for alpha, beta in [(Fr(0), Fr(0)), (Fr(1), Fr(2)), (Fr(-1), Fr(3))]:
        r = analyze(alpha, beta)
        agree = (r['criterion_good'] == r['any_good'])
        print(f"alpha={alpha}, beta={beta}: dimV={r['dimV']}, mu={r['mu']}, (rho,c)=({r['rho']},{r['c']})")
        print(f"   判据说'不被覆盖' = {r['criterion_good']};  "
              f"在格子里搜到 (5b) 成立的 = {r['any_good']}  => {'一致 ✓' if agree else '不一致 ✗'}")


if __name__ == '__main__':
    main()
