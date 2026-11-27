"""§55：**好**的 mu=1 实例（($\rho$,c) = (3,1)，(5a) 与 (5b) 都成立）。

构造（n=6）：
  W = <e1,e2,e3> 是 A-不变块，A_W = 友矩阵 of x^3 - x^2 - 2x - 3（不可约）；
  e4 -> e4；e5 -> e6；e6 -> e1 + e5（跨块）；
  C = (-1,-2,0,0,0,-1)；
  V = <e1,e2,e3,e5>（4 维）；固定行 L0 = e5。
结论：类型 (3,1)、mu = 1、(5a) ✓、(5b) ✓ —— 即这个格子是**好**的。
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
mm, rank, rb = CV.Qm.mm, CV.Qm.rank, CV.Qm.rb

n = 6


def instance():
    def companion(cf):
        M = [[Fr(0)] * 3 for _ in range(3)]
        for i in range(2):
            M[i][i + 1] = Fr(1)
        for j in range(3):
            M[2][j] = Fr(cf[j])
        return M

    A = [[Fr(0)] * n for _ in range(n)]
    Aw = companion([3, 2, 1])
    for i in range(3):
        for j in range(3):
            A[i][j] = Aw[i][j]
    A[3][3] = Fr(1)
    A[4][5] = Fr(1)
    A[5][0] = Fr(1)
    A[5][4] = Fr(1)
    C = [[Fr(-1), Fr(-2), Fr(0), Fr(0), Fr(0), Fr(-1)]]
    L0 = [[Fr(0), Fr(0), Fr(0), Fr(0), Fr(1), Fr(0)]]
    e = [[Fr(1) if t == i else Fr(0) for t in range(n)] for i in range(n)]
    V = rb([e[0], e[1], e[2], e[4]])
    return A, C, L0, V


def cond5a(V, A, C):
    CA = mm(C, A)
    VA = mm(V, A)
    return rank(VA + V + CA + C) == rank(V + CA + C)


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
            Mx = [[[-rows[i][1][k], rows[i][0][k]] for k in cs] for i in rs]
            val = CV.V.det_poly(Mx)
            if len(val) == 1 and val[0] == 0:
                continue
            g = val if g is None else CV.V.pgcd(g, val)
            if len(g) == 1 and g[0] != 0:
                return True
    return False if g is None else (len(g) == 1 and g[0] != 0)


def main():
    A, C, L0, V = instance()
    CA = mm(C, A)
    J = rb(C + CA)
    j = len(J)
    rho = rank(V + CA + C) - j
    c = len(V) + j - rank(V + J)
    Q = CV.Qm.Quotient(A, C)
    e = [[Fr(1) if t == i else Fr(0) for t in range(n)] for i in range(n)]
    U = rb([Q.pi(w) for w in [e[0], e[1], e[2]]])
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
    conds = {
        'dim V = 4': len(V) == 4,
        'row(L0) ⊆ V': all(rank(V + [list(r)]) == len(V) for r in L0),
        'type (3,1)': (rho, c) == (3, 1),
        'mu = 1': len(E) == 1,
        '(5a)': cond5a(V, A, C),
        '(5b)': cond5b(V, A, C),
        'w != 0': bool(E) and any(E[0]),
    }
    for k, v in conds.items():
        print(f"  [{'PASS' if v else 'FAIL'}] {k}")
    print("=>", "全部 PASS —— 这是一个**好**的 mu=1 实例" if all(conds.values()) else "有失败")


if __name__ == '__main__':
    main()
