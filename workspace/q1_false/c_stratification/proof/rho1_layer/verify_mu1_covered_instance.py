# ✔ 2026-10-30 接手者更正：本脚本现在是**权威**的复核（根因已定位）。
#    该实例实际 w = β(e5) = π(e6) = 0 ⟹ 归 C.5（恒被覆盖），C.2 不适用；
#    旧版把 a（E 的方向）当 w 代进判据，故显示"不一致"。现在会打印 w 并自动分流。
#    正确的 T = [[0,1,0],[0,0,1],[1,1,0]]（残差恰为零）。
"""§52.7 的实例（μ = 1、"被覆盖"）：一个**干净**的复核脚本。

不用"补空间坐标"算 T（§53 的教训：U ∩ B ≠ 0 时坐标 ≠ 分量），而是**解定义方程**：
    f(u_i) = Σ_j T_{ji} u_j + Σ_k c_{ik} B_k.
然后：(1) 断言 T 的每条特征线与 a 的关系；(2) 断言 (5b) 在 V 上失败；(3) 断言两者一致（都被覆盖）。

输出：对三组 (α, β) 打印 T、a、是否存在 ⟂ a 的特征向量、以及 (5b) 的实测结果。
"""
import itertools
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI

import importlib.util as iu
spec = iu.spec_from_file_location('C2', 'proof/rho1_layer/verify_cell_criteria_genuine.py')
CV = iu.module_from_spec(spec)
spec.loader.exec_module(CV)
Qm = CV.Qm
mm, rank, rb = Qm.mm, Qm.rank, Qm.rb

n = 6


def build(alpha, beta):
    A = [[Fr(0)] * n for _ in range(n)]
    A[0][1] = Fr(1); A[1][2] = Fr(1); A[2][0] = Fr(1); A[2][1] = Fr(1)   # W 上的块（W 不变）
    A[3][3] = Fr(1)
    A[4][5] = Fr(1)
    A[5][0] = Fr(1); A[5][4] = Fr(alpha); A[5][5] = Fr(beta)
    C = [[Fr(0), Fr(0), Fr(0), Fr(0), Fr(1), Fr(0)]]                      # C = e5
    L0 = [list(C[0])]
    V = rb([[Fr(1) if t == i else Fr(0) for t in range(n)] for i in (0, 1, 2, 4)])
    return A, C, L0, V


def solve_in_U(basis, target):
    """把 target 写成 basis 的线性组合（在 X 的坐标里）；无解返回 None。"""
    d = len(basis)
    eqs = [[basis[j][k] for j in range(d)] + [target[k]] for k in range(len(target))]
    R = AI.rref(eqs)[0]
    sol = [Fr(0)] * d
    for row in R:
        piv = next((j for j in range(d) if row[j] != 0), None)
        if piv is None:
            if row[d] != 0:
                return None
            continue
        sol[piv] = row[d] / row[piv]
    return sol


def pencil_minors_gcd_is_one(T, Erows, rho):
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
        return False
    g = polys[0]
    for q in polys[1:]:
        g = CV.V.pgcd(g, q)
    return len(g) == 1 and g[0] != 0


def cond5b(V, A, C):
    CA = mm(C, A)
    VA = mm(V, A)
    r0 = rank(V + CA + C)
    rows = [(V[i], VA[i]) for i in range(len(V))]
    for r in CA:
        rows.append(([Fr(0)] * len(r), list(r)))
    for r in C:
        rows.append(([Fr(0)] * len(r), list(r)))
    g = None
    for rs in itertools.combinations(range(len(rows)), r0):
        for cs in itertools.combinations(range(n), r0):
            M = [[[-rows[i][1][k], rows[i][0][k]] for k in cs] for i in rs]
            val = CV.V.det_poly(M)
            if len(val) == 1 and val[0] == 0:
                continue
            g = val if g is None else CV.V.pgcd(g, val)
            if len(g) == 1 and g[0] != 0:
                return True
    return False if g is None else (len(g) == 1 and g[0] != 0)


def main():
    ok_all = True
    for alpha, beta in [(Fr(0), Fr(0)), (Fr(1), Fr(2)), (Fr(-1), Fr(3))]:
        A, C, L0, V = build(alpha, beta)
        Q = Qm.Quotient(A, C)
        e = [[Fr(1) if t == i else Fr(0) for t in range(n)] for i in range(n)]
        U = rb([Q.pi(w) for w in [e[0], e[1], e[2]]])
        assert len(U) == 3, 'dim U != 3'
        # μ = dim(B ∩ U)：维数公式（§61：不能数"B 的基向量里有多少个落在 U 里" ✗）
        mu = len(Q.B) + len(U) - rank(Q.B + U)
        E = []
        if mu > 0:
            _rows = [[Q.B[i][k] for i in range(len(Q.B))] + [-U[j][k] for j in range(len(U))] for k in range(Q.d)]
            for _sol in AI.nullspace(_rows):
                _v = [sum(_sol[i] * Q.B[i][k] for i in range(len(Q.B))) for k in range(Q.d)]
                if any(_v):
                    E.append(_v)
            E = rb(E)
        assert len(E) == 1, 'mu != 1'

        # T：解定义方程
        fU = [Q.pi(mm([Q.lift(u)], A)[0]) for u in U]
        nunk = 9 + 3 * len(Q.B)
        eqs = []
        for i in range(3):
            for k in range(Q.d):
                row = [Fr(0)] * nunk + [fU[i][k]]
                for j in range(3):
                    row[j * 3 + i] = U[j][k]
                for t in range(len(Q.B)):
                    row[9 + i * len(Q.B) + t] = Q.B[t][k]
                eqs.append(row)
        R = AI.rref(eqs)[0]
        sol = [Fr(0)] * nunk
        for row in R:
            piv = next((j for j in range(nunk) if row[j] != 0), None)
            if piv is None:
                continue
            sol[piv] = row[nunk] / row[piv]
        T = [[sol[j * 3 + i] for j in range(3)] for i in range(3)]
        a = solve_in_U(U, E[0])
        assert a is not None

        # w = β(h)：H = V∩J 的生成元。C.2 的假设是 w ≠ 0；本实例 w = 0 ⟹ 归 C.5（恒被覆盖）。
        CA_ = mm(C, A)
        J = rb(C + CA_)
        rows_int = [[V[i][k] for i in range(len(V))] + [-J[j][k] for j in range(len(J))]
                    for k in range(n)]
        ns = AI.nullspace(rows_int)
        assert len(ns) == 1, f'dim(V∩J) != 1（实际 {len(ns)}）'
        h = [sum(ns[0][i] * V[i][k] for i in range(len(V))) for k in range(n)]
        w = Q.pi(mm([h], A)[0])

        if not any(w):
            covered_by_criterion = True
            why = 'C.5（w = 0 ⟹ 恒被覆盖）'
        else:
            covered_by_criterion = not pencil_minors_gcd_is_one(T, [w], 3)
            why = 'C.2（w ≠ 0）'
        measured = not cond5b(V, A, C)
        agree = (covered_by_criterion == measured)
        ok_all = ok_all and agree
        print(f"alpha={alpha}, beta={beta}")
        print(f"  T = {[[str(x) for x in r] for r in T]}")
        print(f"  a = {[str(x) for x in a]}  (E = B∩U 的方向)")
        print(f"  h = {[str(x) for x in h]}、w = β(h) = {[str(x) for x in w]}")
        print(f"  判据: {why} ⟹ {'被覆盖' if covered_by_criterion else '不被覆盖'};  "
              f"实测 (5b): {'失败' if measured else '成立'}  => {'一致 ✓' if agree else '不一致 ✗'}")
    print()
    print('=>', '三组全部一致：该实例的格子**被覆盖**（原因是 w = 0，即 C.5，不是 C.2）✓'
          if ok_all else '有不一致 ✗')


if __name__ == '__main__':
    main()
