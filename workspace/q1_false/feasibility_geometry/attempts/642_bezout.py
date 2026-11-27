"""642：Bézout 线性系统——检验 gcd=1 是否能被有限线性系统判定。"""
import itertools
import sympy as sp

lam = sp.symbols('lam')


def bezout_check(H, Z, name):
    P = lam * H - Z * H
    q, k = H.shape
    om = H.rank()
    minors = []
    for idx in itertools.combinations(range(q), om):
        for cidx in itertools.combinations(range(k), om):
            minors.append(sp.expand(P.extract(idx, cidx).det()))
    minors = [m for m in minors if sp.expand(m) != 0]
    D = max(sp.degree(m, lam) for m in minors) if minors else 0
    # unknowns a_{i,k}, i=1..m, k=0..D-1
    m = len(minors)
    unknowns = sp.symbols('a0:%d' % (m * D))
    # sum_i sum_k a_{i,k} lam^k * f_i(lam) - 1 = 0
    expr = -1
    for i, f in enumerate(minors):
        for kk in range(D):
            expr += unknowns[i * D + kk] * lam ** kk * f
    poly = sp.Poly(sp.expand(expr), lam)
    eqs = poly.all_coeffs()
    A, b = sp.linear_eq_to_matrix(eqs, unknowns)
    r = A.rank()
    ra = A.row_join(b).rank()
    print(f'--- {name}: rank H={om}, #minors={m}, D={D}, unknowns={len(unknowns)}')
    print('   system rank =', r, ' augmented rank =', ra, ' -> solvable:', r == ra)


if __name__ == '__main__':
    Zp = sp.Matrix([[0, 0, 0], [1, 0, 0], [0, 0, 0]])
    A_H = sp.Matrix([[-1, -1, 0], [-1, 0, 0], [0, -1, 0]])
    A_Z = sp.Matrix([[1, 0, 0], [1, -1, 0], [1, 0, 0]])
    B_H = sp.Matrix([[-1, -1, 0], [-1, -1, -1], [-1, -1, -1]])
    B_Z = sp.Matrix([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
    bezout_check(A_H, A_Z, 'A (feasible)')
    bezout_check(B_H, B_Z, 'B (infeasible)')
