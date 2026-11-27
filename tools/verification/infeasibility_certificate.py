"""Generate the exact infeasibility certificate package for seeds 16/21 (attempt 187).

Outputs (stdout, or a markdown file with --out):
  K0 basis N, W_L basis, W_L subset D witnesses, c=2 row-space certificates,
  c=1 eigenline quadratic and the constraint functional on rational eigenlines,
  c=0 determinant sample.
"""
import sys
sys.path.insert(0, '.')
sys.path.insert(0, 'tools/verification')
sys.path.insert(0, 'tools/exact_linalg')
sys.path.insert(0, 'tools/ledger')
from fractions import Fraction as F
import linalg_q as LQ
import z_generator as ZG
from tools.verification.p2_stratification_check import data


def fmt(x):
    return str(x)


def mat(M):
    return '\n'.join('  [' + ', '.join(fmt(x) for x in row) + ']' for row in M)


def build(seed):
    A, C, L0, k, d, NK, U0, V0, Z1, Z2 = data(seed)
    n = len(A)
    N = [[F(x) for x in r] for r in NK]
    AN = LQ.mul(A, N)
    L0N = [F(x) for x in LQ.mul(L0, N)[0]]
    L0AN = [F(x) for x in LQ.mul(LQ.mul(L0, A), N)[0]]
    WL = ZG.ker_cols([L0N[:], L0AN[:]])
    w0 = [F(WL[i][0]) for i in range(k)]
    w1 = [F(WL[i][1]) for i in range(k)]
    RD = LQ.rowspace([r[:] for r in C] + [r[:] for r in LQ.mul(C, A)])
    G = [[sum(F(r[u]) * F(AN[u][t]) for u in range(n)) for t in range(k)] for r in RD]
    return A, C, L0, N, AN, L0N, L0AN, WL, w0, w1, RD, G, n, k


def main(seed):
    A, C, L0, N, AN, L0N, L0AN, WL, w0, w1, RD, G, n, k = build(seed)
    out = []
    out.append(f'# Infeasibility certificate: seed {seed}')
    out.append('## K0 basis N (n x k)')
    out.append(mat(N))
    out.append('## W_L basis (columns in K0 coordinates)')
    out.append(mat(WL))
    out.append('## W_L subset D: w with A v = N w')
    for name, v in (('w0', w0), ('w1', w1)):
        av = [sum(F(AN[i][t]) * v[t] for t in range(k)) for i in range(n)]
        s = LQ.solve([[N[i][t] for t in range(k)] for i in range(n)], [[x] for x in av])
        out.append(f'{name}: w = ' + str(s[0] if s else None))
    # c=2 row-space certificates
    out.append('## c=2: admissibility rows and alpha certificates')
    V = [[F(WL[i][j]) for i in range(k)] for j in range(2)]
    Ann = ZG.ker_cols([V[0][:], V[1][:]])
    us = [[F(Ann[i][j]) for i in range(k)] for j in range(len(Ann[0]))]
    u1 = next(u for u in us if LQ.rank([L0N, u]) == 2)
    p0 = LQ.solve([[N[t][j] for t in range(n)] for j in range(k)], [[L0N[j]] for j in range(k)])[0]
    p1 = LQ.solve([[N[t][j] for t in range(n)] for j in range(k)], [[u1[j]] for j in range(k)])[0]
    A0 = [sum(F(p0[u]) * F(AN[u][t]) for u in range(n)) for t in range(k)]
    A1 = [sum(F(p1[u]) * F(AN[u][t]) for u in range(n)) for t in range(k)]
    m = len(RD)
    for i in range(2):
        rows = []
        for r in range(2):
            row = [sum(F(A0[t]) * F(V[r][t]) for t in range(k)),
                   sum(F(A1[t]) * F(V[r][t]) for t in range(k))] + \
                  [sum(F(G[j][t]) * F(V[r][t]) for t in range(k)) for j in range(m)]
            rows.append(row)
        eb = [F(0), F(1)] + [F(0)] * m
        Dt = [[rows[r][j] for r in range(len(rows))] for j in range(len(rows[0]))]
        s = LQ.solve(Dt, [[x] for x in eb])
        if s is not None:
            alpha = s[0]
            recon = [sum(alpha[r] * rows[r][j] for r in range(len(rows))) for j in range(len(rows[0]))]
            out.append(f'row {i}: Des =\n{mat(rows)}\nalpha = {alpha}, alpha^T Des = {recon} (e_b = {eb})')
        else:
            out.append(f'row {i}: not forced')
    # c=1 quadratic
    out.append('## c=1: eigenline quadratic det[v, Av] = 0')
    v0 = [sum(F(N[i][t]) * w0[t] for t in range(k)) for i in range(n)]
    v1 = [sum(F(N[i][t]) * w1[t] for t in range(k)) for i in range(n)]
    Aw0 = [sum(F(AN[i][t]) * w0[t] for t in range(k)) for i in range(n)]
    Aw1 = [sum(F(AN[i][t]) * w1[t] for t in range(k)) for i in range(n)]
    quad = None
    for i in range(n):
        for j in range(i + 1, n):
            a2 = v0[i] * Aw0[j] - v0[j] * Aw0[i]
            ab = v0[i] * Aw1[j] + v1[i] * Aw0[j] - v0[j] * Aw1[i] - v1[j] * Aw0[i]
            b2 = v1[i] * Aw1[j] - v1[j] * Aw1[i]
            if (a2, ab, b2) != (0, 0, 0):
                quad = (a2, ab, b2)
                break
        if quad:
            break
    out.append(f'quadratic: {quad[0]} a^2 + ({quad[1]}) a b + ({quad[2]}) b^2')
    disc = quad[1] * quad[1] - 4 * quad[0] * quad[2]
    out.append(f'discriminant = {disc}')
    # rational roots, phi (only actual roots of the quadratic)
    A2, AB, B2 = quad
    cand = [((F(0), F(1)), 'a=0, v=w1'), ((F(1), F(1)), 'a=b, v=w0+w1')]
    for (a, b), label in cand:
        if A2 * a * a + AB * a * b + B2 * b * b != 0:
            continue
        v = [a * w0[i] + b * w1[i] for i in range(k)]
        av = [sum(F(AN[i][t2]) * v[t2] for t2 in range(k)) for i in range(n)]
        sw = LQ.solve([[N[i][t2] for t2 in range(k)] for i in range(n)], [[x] for x in av])
        if sw is None:
            out.append(f'{label}: Av not in K0')
            continue
        w = sw[0]
        AnnL = ZG.ker_cols([v[:]])
        acols = [[F(AnnL[i][j]) for i in range(k)] for j in range(len(AnnL[0]))]
        basis = [L0N]
        for u in acols:
            if len(basis) == 3:
                break
            if LQ.rank(basis + [u]) > len(basis):
                basis.append(u)
        if len(basis) < 3:
            out.append(f'{label}: Ann basis too small')
            continue
        phi = [sum(basis[j + 1][t] * w[t] for t in range(k)) for j in range(2)]
        out.append(f'{label}: v = {v}, w = {w}, phi = {phi} (nonzero: {not (phi==[0,0])})')
    if disc < 0:
        out.append(f'complex eigenlines: b/a = ({-AB} +/- sqrt({disc}))/(2*{A2}); '
                   f'the Q(i) computation gives phi=(1,0) (see attempts/183).')
    return '\n'.join(out)
    return '\n'.join(out)


if __name__ == '__main__':
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    text = main(seed)
    print(text)
