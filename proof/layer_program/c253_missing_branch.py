r"""验证专家 QA13 的两条：(1) 缺失的 rank-one 分支；(2) 引理 ker(CAZ)=Z∩V=S。

分支 $a=b=c=0$、$(d,e,f)\ne(0,0,0)$：条件应为 $d\ne0$、$e(d+1)=0$、$f(d+1)=0$。
例：$d=-1,e=0,f=1$ ⟹ $Z_*=\operatorname{span}(e_4-e_8,\ e_5,\ e_6+e_8)$，$(A)$ 成立但 $(S)$ 失败。

用法：python proof/layer_program/c253_missing_branch.py
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import spectral_gcd as SG

N, P = 8, 2
C = [[Fr(1) if k == 0 else Fr(0) for k in range(N)],
     [Fr(1) if k == 1 else Fr(0) for k in range(N)]]
A = [[Fr(0)] * N for _ in range(N)]
A[6][2] = Fr(1); A[7][3] = Fr(1); A[4][4] = Fr(1); A[5][5] = Fr(1)
A[0][6] = Fr(1); A[1][7] = Fr(1); A[2][0] = Fr(1); A[3][1] = Fr(1)
L0 = [[Fr(1) if k == 2 else Fr(0) for k in range(N)]]


def build(a, b, c, d, e, f):
    """Z 的列 = e4+a e7+d e8, e5+b e7+e e8, e6+c e7+f e8。"""
    Z = [[Fr(0)] * 3 for _ in range(N)]
    Z[3][0] = Fr(1); Z[6][0] = Fr(a); Z[7][0] = Fr(d)
    Z[4][1] = Fr(1); Z[6][1] = Fr(b); Z[7][1] = Fr(e)
    Z[5][2] = Fr(1); Z[6][2] = Fr(c); Z[7][2] = Fr(f)
    return Z


def check(Z):
    d = 3
    if AI.rank(Z) < d:
        return None
    CA = AI.mul(C, A)
    CAZ = AI.mul(CA, Z)
    Rv = AI.nullspace(CAZ)
    Rm = [[Rv[k][i] for k in range(len(Rv))] for i in range(d)]
    AZ = SG.apply_col(A, Z)
    AZR = AI.mul(AZ, Rm)
    M1 = [list(Z[i]) + list(AZR[i]) for i in range(N)]
    okA = AI.rank(M1) == d
    g, h, _c = SG.spectral_gcd_Z(A, C, Z)
    Vv = AI.nullspace([[Fr(x) for x in row] for row in (C + CA)])
    Vc = [[Vv[k][i] for k in range(len(Vv))] for i in range(N)]
    both = [list(Vc[i]) + list(Z[i]) for i in range(N)]
    s = len(Vv) + d - AI.rank(both)
    return AI.rank(CAZ), len(Rv), okA, SG.pdeg(g), s


def main():
    # 专家的 Z_*
    Zs = build(0, 0, 0, -1, 0, 1)
    print('Z_* = span(e4-e8, e5, e6+e8)：', check(Zs), '（r, dim ker, (A), gcd 次数, dim S）')
    # 分支条件扫描：a=b=c=0，(d,e,f) 小范围
    ok_pts = []
    for d, e, f in itertools.product((-2, -1, 0, 1, 2), repeat=3):
        if (d, e, f) == (0, 0, 0):
            continue
        Z = build(0, 0, 0, d, e, f)
        res = check(Z)
        if res and res[2]:
            ok_pts.append((d, e, f, res[3]))
    print(f'\n分支 a=b=c=0 上 (A) 成立的点（d,e,f,gcd 次数）：')
    for t in ok_pts:
        print('  ', t)
    print('\n专家的条件 d≠0、e(d+1)=0、f(d+1)=0 的检验：')
    bad = [t for t in ok_pts if t[0] == 0 or (t[1] != 0 and t[0] + 1 != 0) or (t[2] != 0 and t[0] + 1 != 0)]
    print('  违反条件的 (A) 点：', bad if bad else '无 ✓')


if __name__ == '__main__':
    main()
