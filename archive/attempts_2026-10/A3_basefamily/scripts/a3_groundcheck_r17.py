r"""A-3：地基检查——harness 在**已知可行**的 R17 上必须给出非空的 $(A)\wedge(S)$。

**为什么要做**：c282 与第二实例上 $(A)\wedge(S)$ 都是空集。若 harness 有系统性错误（例如把 $(S)$ 判得太严），
我们会把"可行"也误判成"不可行"。**R17 是项目里唯一有已知可行解（$q=3$）的实例**，必须通过。

**做法**：
- R17：$S=\\operatorname{span}(e_5,e_6)$、$q=3$（$d=3$、$r=1$、$m=3$），枚举 $u\\in H/S$ 的格点;
- 对每个 $u$：$(A)$ = $\\operatorname{rank}[Z|AZR]=d$，$(S)$ = `spectral_gcd_Z` 的 gcd 次数 0。

用法：python workspace/A3_basefamily/scripts/a3_groundcheck_r17.py
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import coeff_of_S as CS_
import spectral_gcd as SG


def r17():
    N = 8
    def unit(i):
        return [Fr(1) if k == i else Fr(0) for k in range(N)]
    C = [unit(0), unit(1)]
    L0 = [unit(2)]
    A = [[Fr(0)] * N for _ in range(N)]
    A[6][2] = Fr(1); A[7][3] = Fr(1); A[4][4] = Fr(1)
    A[5][5] = Fr(1); A[0][6] = Fr(1); A[1][7] = Fr(1)
    S = [unit(4), unit(5)]
    return A, C, L0, S


def main():
    A, C, L0, S = r17()
    q = 3
    st = CS_.setup(A, C, L0, q, S)
    m = st['m']
    wm = st['w'] - st['s']
    n = st['n']
    hvecs = [[sum(st['HS'][j][k] * st['WB'][st['s'] + k][i] for k in range(wm))
              for i in range(n)] for j in range(m)]
    print(f'R17: n={n}, s={st["s"]}, d={st["d"]}, m={m}, q={q}')

    def lift(u):
        return [sum(u[j] * hvecs[j][i] for j in range(m)) for i in range(n)]

    def condA(u):
        Z = list(S) + [lift(u)]
        Zmat = [[Z[j][i] for j in range(len(Z))] for i in range(n)]
        CA = AI.mul(C, A)
        CAZ = AI.mul(CA, Zmat)
        Rv = AI.nullspace(CAZ)
        d = len(Z)
        R = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
        AZ = SG.apply_col(A, Zmat)
        AZR = AI.mul(AZ, R) if (R and R[0]) else [[Fr(0)] * d for _ in range(n)]
        M = [list(Zmat[i]) + list(AZR[i]) for i in range(n)]
        return AI.rank(M) == d

    nA = nS = nAS = tot = 0
    wit = None
    for cs in itertools.product((-1, 0, 1), repeat=m):
        if all(c == 0 for c in cs):
            continue
        u = [Fr(c) for c in cs]
        Z = list(S) + [lift(u)]
        Zmat = [[Z[j][i] for j in range(len(Z))] for i in range(n)]
        a = condA(u)
        g, _h, _c = SG.spectral_gcd_Z(A, C, Zmat)
        s_ok = (SG.pdeg(g) == 0)
        tot += 1
        nA += a
        nS += s_ok
        if a and s_ok:
            nAS += 1
            if wit is None:
                wit = (cs, u)
    print(f'  扫 {tot} 个 u：(A) {nA}、(S) {nS}、(A)∧(S) **{nAS}**')
    if wit:
        print(f'  见证：u 坐标 = {wit[0]}（(A) 与 (S) 同时成立）✓ 地基检查通过')
    else:
        print('  *** 地基检查失败：已知可行的 R17 上 (A)∧(S) 为空 — harness 有问题 ***')


if __name__ == '__main__':
    main()
