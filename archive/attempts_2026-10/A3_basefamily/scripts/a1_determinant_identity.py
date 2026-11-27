r"""A-1：验证"$H/S$ 限制"这一步——$\\det[U_m\\mid P_m]$ 是否等价于 $U\\cap\\operatorname{im}P(\\lambda)=0$？

**待检验的恒等式/等价**（A2 §33 的基础）：
1. $q_U(\\lambda)=\\det[U_m\\mid P_m(\\lambda)]$（adapted basis 的**前 $m$ 行**）；
2. 声称：$q_U(\\lambda)\\ne0\\iff U\\cap\\operatorname{im}P(\\lambda)=0$。

**本脚本要说清的**：$U$ 的支撑在前 $m$ 行时，$[U\\mid P]$ 有分块
$$\\begin{pmatrix}U_E&P_E\\\\ 0&P_{F'}\\end{pmatrix}.$$
于是
- $q_U\\ne0\\Rightarrow U\\cap\\operatorname{im}P=0$ ✓（**充分**）；
- 反之**不成立**：若 $P$ 有 $F'$ 方向的分量、且 $U_E\\cap P_E\\ne0$ 但 $U\\cap\\operatorname{im}P=0$，
  则 $q_U\\equiv0$ 而可行 ⟹ **必要不成立**。

本脚本给出具体实例把这两种情形都跑出来（"地基检查"：必须同时看到 True 与 False 两类）。

用法：python workspace/A3_basefamily/scripts/a1_determinant_identity.py
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


def second_instance():
    N = 6
    def unit(i):
        return [Fr(1) if k == i else Fr(0) for k in range(N)]
    C = [[Fr(0)] * N]
    C[0][0] = Fr(1)
    A = [[Fr(0)] * N for _ in range(N)]
    A[0][5] = Fr(1); A[2][2] = Fr(1); A[3][3] = Fr(1)
    A[1][1] = Fr(1); A[4][4] = Fr(1)
    L0 = [[Fr(0)] * N]
    L0[0][1] = Fr(1)
    return A, C, L0


def c282():
    N = 8
    def unit(i):
        return [Fr(1) if k == i else Fr(0) for k in range(N)]
    C = [unit(0), unit(1)]
    L0 = [unit(2)]
    A = [[Fr(0)] * N for _ in range(N)]
    for (i, j) in [(0, 2), (1, 3), (4, 4), (3, 5), (5, 6), (6, 7)]:
        A[i][j] = Fr(1)
    return A, C, L0


def analyse(A, C, L0, q, S, label):
    st = CS_.setup(A, C, L0, q, S)
    cols = CS_.pencil_cols(A, st)
    wm = st['w'] - st['s']
    m = st['m']
    r = st['d'] - st['s']
    t = len(cols)
    if r + t != m:
        print(f"{label}: 非平衡（r+t={r+t}, m={m}）——跳过")
        return
    T = CS_.adapted_basis(st)
    Ti = CS_._invert(T)
    # 适配坐标下的 P
    Pm = [[sum(Ti[i][j] * cols[k][0][j] for j in range(wm)) for k in range(t)] for i in range(m)]
    Pm1 = [[sum(Ti[i][j] * cols[k][1][j] for j in range(wm)) for k in range(t)] for i in range(m)]
    print(f"\n=== {label}：m={m}, r={r}, t={t}, 平衡 ✓")
    print(f"{'U':<18}{'det[U_m|P_m] 常数?':<22}{'det常?':<12}{'U∩imP=0':<12}{'check_Z':<12}结论")
    seen = set()
    lams = [Fr(0), Fr(1), Fr(-1), Fr(2)]
    for coefs in itertools.product((-1, 0, 1), repeat=m):
        if all(c == 0 for c in coefs):
            continue
        u = [Fr(c) for c in coefs]
        # det[U_m | P_m(lam)] 对各 lam
        vals = []
        ok = True
        for lam in lams:
            M = [[u[i]] + [Pm[i][k] + lam * Pm1[i][k] for k in range(t)] for i in range(m)]
            vals.append(CS_.__dict__.get('det')(M) if 'det' in CS_.__dict__ else _det(M))
        is_const_nonzero = all(v != 0 for v in vals) and len(set(vals)) == 1
        # 三个候选判据（全部**精确**）
        import spectral_gcd as SG
        import base_sweep as BS
        ufull = [sum(u[i] * T[j][i] for i in range(m)) for j in range(wm)]
        Uv = [sum(ufull[j] * st['WB'][st['s'] + j][k] for j in range(wm)) for k in range(st['n'])]
        Uvec = [Uv]
        # b2：U ∩ im P(λ) = 0 ∀λ（gcd of (r+t)-minors of [U|P]，在完整 W/S 坐标）
        b2, _gg = CS_.feasible_by_minors(A, C, L0, q, S, Uvec)
        # b3：Z = S ⊕ U 的 (A)(S)
        Z = list(S) + Uvec
        Zmat = [[Z[j][i] for j in range(len(Z))] for i in range(st['n'])]
        _okA, _okS, _g2 = BS.check_Z(A, C, Zmat)
        b3 = _okA and _okS
        direct = b2
        key = (is_const_nonzero, direct)
        if key in seen:
            continue
        seen.add(key)
        print(f"{str([c for c in coefs]):<18}{str(is_const_nonzero):<12}{str(b2):<12}{str(b3):<12}")
    print("   （只打印每种 (det, 直接) 组合的首次出现）")


def _det(M):
    n = len(M)
    if n == 0:
        return Fr(1)
    M = [row[:] for row in M]
    d = Fr(1)
    for i in range(n):
        p = next((r for r in range(i, n) if M[r][i] != 0), None)
        if p is None:
            return Fr(0)
        if p != i:
            M[i], M[p] = M[p], M[i]
            d = -d
        d *= M[i][i]
        inv = Fr(1) / M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] * inv
            for c in range(i, n):
                M[r][c] -= f * M[i][c]
    return d


def main():
    A, C, L0 = c282()
    N = 8
    def unit(i):
        return [Fr(1) if k == i else Fr(0) for k in range(N)]
    analyse(A, C, L0, 4, [unit(4)], 'c282（im P ⊆ H/S）')
    A, C, L0 = second_instance()
    N = 6
    def unit2(i):
        return [Fr(1) if k == i else Fr(0) for k in range(N)]
    analyse(A, C, L0, 4, [unit2(2)], '第二实例 q=4, S=span(e3)')
    analyse(A, C, L0, 3, [unit2(2), unit2(3)], '第二实例 q=3, S=span(e3,e4)')


if __name__ == '__main__':
    main()
