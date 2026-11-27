"""Exact certificates for the forced-plane criterion (attempts/165, expert 60).

For each seed and each bottom row i, output either
  (A) alpha with e_b = alpha^T Des_i   (b_i is forced to 0), or
  (B) x in ker(Des_i) with b_i != 0    (b_i is not forced to 0).

Run: python tools/verification/c2_forced_certificates.py
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


def build(seed):
    A, C, L0, k, d, NK, U0, V0, Z1, Z2 = data(seed)
    n = len(A)
    N = [[F(x) for x in r] for r in NK]
    AN = LQ.mul(A, N)
    L0N = [F(x) for x in LQ.mul(L0, N)[0]]
    L0AN = [F(x) for x in LQ.mul(LQ.mul(L0, A), N)[0]]
    WL = ZG.ker_cols([L0N[:], L0AN[:]])
    V0v = [F(WL[i][0]) for i in range(k)]
    V1v = [F(WL[i][1]) for i in range(k)]
    Ann = ZG.ker_cols([V0v[:], V1v[:]])
    us = [[F(Ann[i][j]) for i in range(k)] for j in range(len(Ann[0]))]
    u1 = next(u for u in us if LQ.rank([L0N, u]) == 2)
    RD = LQ.rowspace([r[:] for r in C] + [r[:] for r in LQ.mul(C, A)])
    p0 = LQ.solve([[N[t][j] for t in range(n)] for j in range(k)], [[L0N[j]] for j in range(k)])[0]
    p1 = LQ.solve([[N[t][j] for t in range(n)] for j in range(k)], [[u1[j]] for j in range(k)])[0]
    A0 = [sum(F(p0[u]) * F(AN[u][t]) for u in range(n)) for t in range(k)]
    A1 = [sum(F(p1[u]) * F(AN[u][t]) for u in range(n)) for t in range(k)]
    G = [[sum(F(r[u]) * F(AN[u][t]) for u in range(n)) for t in range(k)] for r in RD]
    m = len(RD)
    return A, C, L0, N, L0N, u1, p0, p1, A0, A1, G, RD, V0v, V1v, n, k, m


def main():
    for seed in (10, 16, 21):
        A, C, L0, N, L0N, u1, p0, p1, A0, A1, G, RD, V0v, V1v, n, k, m = build(seed)
        print(f'--- seed {seed} ---')
        for i in range(2):
            Des = []
            for Vc in (V0v, V1v):
                Des.append([sum(F(A0[t]) * F(Vc[t]) for t in range(k)),
                            sum(F(A1[t]) * F(Vc[t]) for t in range(k))] +
                           [sum(F(G[j][t]) * F(Vc[t]) for t in range(k)) for j in range(m)])
            eb = [F(0), F(1)] + [F(0)] * m
            # try e_b = alpha^T Des  <=>  Des^T alpha = e_b
            Dt = [[Des[r][j] for r in range(len(Des))] for j in range(len(Des[0]))]
            s = LQ.solve([r[:] for r in Dt], [[x] for x in eb])
            if s is not None:
                alpha = s[0]
                # verify
                recon = [sum(alpha[r] * Des[r][j] for r in range(len(Des))) for j in range(len(Des[0]))]
                assert recon == eb, (seed, i, recon, eb)
                print(f'  row {i}: FORCED b=0, certificate alpha={alpha}')
            else:
                # find x in ker(Des) with b != 0: solve Des x = 0 plus b = 1
                sys2 = [r[:] for r in Des] + [[F(0), F(1)] + [F(0)] * m]
                rhs = [[F(0)], [F(0)], [F(1)]]
                s2 = LQ.solve(sys2, rhs)
                if s2 is None:
                    print(f'  row {i}: NO certificate (unexpected)')
                else:
                    x = s2[0]
                    assert x[1] != 0, (seed, i, x)
                    print(f'  row {i}: NOT forced (b!=0), certificate x={x}')
    print('done')


if __name__ == '__main__':
    main()
