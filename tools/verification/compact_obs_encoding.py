"""compact_obs_encoding.py —— 用**可观性归约**重建紧凑编码，并在已知见证上显式构造全部辅助变量

**编码（专家 2026-11-04 §4/§7 的 work package 2）**：固定阶 $q$。变量与约束如下（全部为线性/双线性）：

| 变量 | 尺寸 | 含义 |
|---|---|---|
| $W$ | $k\\times d$ | $\\mathcal Z=K W$（$K=\\ker[C;L_0]$ 的基） |
| $Y_W$ | $d\\times k$ | $Y_W W=I_d$（$\\operatorname{rank}W=d$） |
| $T$ | $q\\times(q+2p)$ | $(5a)$：$\\mathcal LA=T[\\mathcal L;CA;C]$ |
| $\\Lambda,G_0,G_1$ | $q\\times q,\\ q\\times p,\\ q\\times p$ | $\\mathcal LA=\\Lambda\\mathcal L+G_0C+G_1CA$ |
| $A,B$ | $q\\times s,\\ s\\times d_V$ | $M:=\\mathcal LV_0=AB$（$\\operatorname{rank}M=s$） |
| $Y_A,Y_B$ | $s\\times q,\\ d_V\\times s$ | $Y_A A=I_s$、$BY_B=I_s$（秩的证书） |
| $E$ | $(q-s)\\times q$ | $\\ker E=\\operatorname{im}M$（经 $EM=0$、$\\operatorname{rank}E=q-s$） |
| $Y_E$ | $q\\times(q-s)$ | $Y_E E=I_{q-s}$ |
| $Y_O$ | $q\\times q(q-s)$ | $Y_O\\,\\mathcal O(E,\\Lambda)=I_q$，$\\mathcal O=[E;E\\Lambda;\\dots;E\\Lambda^{q-1}]$ |

对 $s\\in\\{0,\\dots,q\\}$ 作**有限析取**（$q+1$ 项）。规模：变量 $O(q^3)$、约束 $O(q^3)$、次数 $\\le2$。

本脚本的用途：**必要性方向的可执行证书**——给定一个已知可行的 $\\mathcal L$，显式构造
$(\\Lambda,G_0,G_1,V_0,M,A,B,Y_A,Y_B,E,Y_E,Y_O)$ 并逐条精确核验所有约束（含 $Y_O\\mathcal O=I_q$）。

用法：python -u tools/verification/compact_obs_encoding.py
"""

import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402

F = Fraction


def matmul(X, Y):
    n, m, p = len(X), len(Y), len(Y[0])
    assert len(X[0]) == m, 'matmul 维数不符'
    return [[sum(X[i][k] * Y[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def transpose(X):
    return [[X[i][j] for i in range(len(X))] for j in range(len(X[0]))]


def solve_ls(Amat, bvec):
    """最小二乘无关：解一个相容线性系统（精确），返回一个解或 None。"""
    rows = len(Amat)
    cols = len(Amat[0]) if rows else 0
    M = [row[:] + [bvec[i]] for i, row in enumerate(Amat)]
    piv = []
    r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = M[r][c]
        M[r] = [v / inv for v in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [v - f * w for v, w in zip(M[i], M[r])]
        piv.append(c)
        r += 1
        if r == rows:
            break
    for i in range(r, rows):
        if all(v == 0 for v in M[i][:cols]) and M[i][cols] != 0:
            return None
    x = [F(0)] * cols
    for i, c in enumerate(piv):
        x[c] = M[i][cols]
    return x


def rref(Amat):
    """精确行最简形；返回 (R, pivots)。"""
    R = [row[:] for row in Amat]
    rows = len(R)
    cols = len(R[0]) if rows else 0
    piv = []
    r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if R[i][c] != 0), None)
        if p is None:
            continue
        R[r], R[p] = R[p], R[r]
        inv = R[r][c]
        R[r] = [v / inv for v in R[r]]
        for i in range(rows):
            if i != r and R[i][c] != 0:
                f = R[i][c]
                R[i] = [v - f * w for v, w in zip(R[i], R[r])]
        piv.append(c)
        r += 1
    return R, piv


def nullspace(Amat, ncols):
    R, piv = rref(Amat)
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [F(0)] * ncols
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][fc]
        basis.append(v)
    return basis


def build_and_check(A, C, L0, q, L, verbose=True):
    """给定见证 L，构造全部辅助变量并核验约束。返回 (是否全部通过, 报告列表)。"""
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    qq = len(L)
    CA = LQ.mul(C, A)
    LA = LQ.mul(L, A)
    rep = []

    def check(name, ok, extra=''):
        rep.append((name, ok, extra))
        return ok

    # 0) 增广约束
    check('rank L = q', LQ.rank(L) == qq)
    check('rank[C;L] = p+q', LQ.rank([list(x) for x in C] + L) == p + qq)
    V0 = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    dV = len(V0[0])
    # Z 与 dim
    Zk = ZG.ker_cols([list(x) for x in C] + L)
    dZ = len(Zk[0]) if (Zk and Zk[0]) else 0
    check('dim ker[C;L] = d', dZ == d, f'{dZ} vs {d}')

    # 1) (5a)：T[L;CA;C] = LA
    H = [list(x) for x in L] + [list(x) for x in CA] + [list(x) for x in C]
    nunk = qq * len(H)
    Amat, bvec = [], []
    for i in range(qq):
        for j in range(n):
            row = [F(0)] * nunk
            for k in range(len(H)):
                row[i * len(H) + k] = F(H[k][j])
            Amat.append(row)
            bvec.append(F(LA[i][j]))
    xT = solve_ls(Amat, bvec)
    check('(5a) 可解（T 存在）', xT is not None)

    # 2) 因子化 Λ,G0,G1
    nunk = qq * qq + 2 * qq * p
    Amat, bvec = [], []
    for i in range(qq):
        for j in range(n):
            row = [F(0)] * nunk
            for k in range(qq):
                row[k * qq + i] = F(L[k][j])
            for k in range(p):
                row[qq * qq + i * p + k] = F(C[k][j])
                row[qq * qq + qq * p + i * p + k] = F(CA[k][j])
            Amat.append(row)
            bvec.append(F(LA[i][j]))
    xF = solve_ls(Amat, bvec)
    if not check('因子化 LA = ΛL+G0C+G1CA 可解', xF is not None):
        return False, rep
    Lam = [[xF[k * qq + i] for k in range(qq)] for i in range(qq)]
    G0 = [[xF[qq * qq + i * p + k] for k in range(p)] for i in range(qq)]
    G1 = [[xF[qq * qq + qq * p + i * p + k] for k in range(p)] for i in range(qq)]
    # 验证
    lhs = matmul(Lam, L)
    lhs = [[lhs[i][j] + sum(G0[i][k] * C[k][j] for k in range(p))
            + sum(G1[i][k] * CA[k][j] for k in range(p)) for j in range(n)] for i in range(qq)]
    check('ΛL+G0C+G1CA = LA', lhs == [list(x) for x in LA])

    # 3) M = L V0，秩 s，因子化 M = AB
    M = matmul(L, V0)
    s = LQ.rank(M)
    Rref, piv = rref(M)
    Acols = [[M[i][c] for c in piv] for i in range(qq)]          # q × s
    Brows = [[Rref[i][j] for j in range(dV)] for i in range(s)]  # s × dV
    check('M = A B', matmul(Acols, Brows) == M, f's = {s}')
    # Y_A: A 的左逆；Y_B: B 的右逆
    YA = None
    if s > 0:
        # 解 YA A = I_s：未知数 s*q
        nunk = s * qq
        Am, bv = [], []
        for a in range(s):
            for k in range(s):
                row = [F(0)] * nunk
                for i in range(qq):
                    row[a * qq + i] = F(Acols[i][k])
                Am.append(row)
                bv.append(F(1) if a == k else F(0))
        xYA = solve_ls(Am, bv)
        YA = [[xYA[a * qq + i] for i in range(qq)] for a in range(s)] if xYA else None
    check('Y_A A = I_s 可解', YA is not None or s == 0)
    YB = None
    if s > 0:
        nunk = dV * s
        Am, bv = [], []
        for k in range(dV):
            for a in range(s):
                row = [F(0)] * nunk
                for j in range(s):
                    row[j * s + a] = F(Brows[j][k])
                Am.append(row)
                bv.append(F(1) if a == k else F(0))
        xYB = solve_ls(Am, bv)
        YB = [[xYB[j * s + a] for j in range(s)] for a in range(dV)] if xYB else None
    check('B Y_B = I_s 可解', YB is not None or s == 0)

    # 4) E：ker E = im M；条件 E M = 0、rank E = q−s
    # E 的行 = {y ∈ Q^q : y^T M = 0} 的基
    Am = [[M[i][j] for i in range(qq)] for j in range(dV)]
    Erows = nullspace(Am, qq) if dV else nullspace([], qq)
    E = [[F(v) for v in y] for y in Erows]
    check('E M = 0', (not E) or matmul(E, M) == [[F(0)] * dV for _ in range(len(E))])
    check('rank E = q−s', (LQ.rank(E) if E else 0) == qq - s, f'{LQ.rank(E) if E else 0} vs {qq - s}')
    # Y_E: E 的右逆
    YE = None
    if E:
        mE = len(E)                        # = q − s
        nunk = qq * mE                     # Y_E: q × (q−s)
        Am, bv = [], []
        for a in range(mE):
            for b in range(mE):
                row = [F(0)] * nunk
                for k in range(qq):
                    row[k * mE + b] = F(E[a][k])
                Am.append(row)
                bv.append(F(1) if a == b else F(0))
        xYE = solve_ls(Am, bv)
        YE = [[xYE[k * mE + b] for b in range(mE)] for k in range(qq)] if xYE else None
        if YE is not None:
            prod = matmul(E, YE)
            check('E Y_E = I_{q−s}（数值）',
                  prod == [[F(1) if i == j else F(0) for j in range(mE)] for i in range(mE)])
    check('E Y_E = I_{q−s} 可解', YE is not None or not E)

    # 5) 观测性矩阵：用**递推** E_0 = E、E_{j+1} = E_j Λ（专家 2026-11-04 §4.1 的要求）
    #    这样每条约束都是双线性的（直接展开 EΛ^k 的次数是 k+1，会破坏"次数 ≤2"）
    blocks = [[row[:] for row in E]]
    for _ in range(1, qq):
        blocks.append(matmul(blocks[-1], Lam))
    # 核验递推 E_{j+1} = E_j Λ 与 E_0 = E
    for j in range(qq - 1):
        check(f'E_{j}->E_{j+1} 的递推（双线性）', matmul(blocks[j], Lam) == blocks[j + 1])
    check('E_0 = E', blocks[0] == E)
    O = [row[:] for b in blocks for row in b]           # (q·(q−s)) × q
    check('rank O = q（可观测）', (LQ.rank(O) if O else 0) == qq, f'{LQ.rank(O) if O else 0} vs {qq}')
    YO = None
    if O:
        rowsO = len(O)
        nunk = qq * rowsO
        Am, bv = [], []
        for k in range(qq):
            for a in range(qq):
                row = [F(0)] * nunk
                for i in range(rowsO):
                    row[a * rowsO + i] = F(O[i][k])
                Am.append(row)
                bv.append(F(1) if a == k else F(0))
        xYO = solve_ls(Am, bv)
        YO = [[xYO[a * rowsO + i] for i in range(rowsO)] for a in range(qq)] if xYO else None
        check('Y_O O = I_q 可解', YO is not None)
        if YO is not None:
            check('Y_O O = I_q（数值）', matmul(YO, O) == [[F(1) if i == j else F(0) for j in range(qq)]
                                                         for i in range(qq)])
    allok = all(ok for _, ok, _ in rep)
    if verbose:
        for name, ok, extra in rep:
            print(f'   {"✓" if ok else "✗"} {name}' + (f'（{extra}）' if extra else ''))
        print(f'   s = {s}，Λ 的阶 = {qq}，E 的尺寸 = {len(E)}×{qq}，Y_O 的尺寸 = '
              f'{len(YO) if YO else 0}×{len(O) if O else 0}')
    return allok, rep


def main():
    import importlib.util as iu
    print('=== 紧凑可观性编码：在已知见证上显式构造全部辅助变量 ===')
    spec = iu.spec_from_file_location('V4', os.path.join(_ROOT, 'proof', 'refuted', 'verify_C4_type3.py'))
    V4 = iu.module_from_spec(spec)
    spec.loader.exec_module(V4)
    A, C, L0, q0, _ = V4.build()
    n, p, r = len(A), len(C), len(L0)
    # C4 的 q=4 显式见证
    L4 = [[F(0), F(0), F(8), F(20), F(1), F(4)],
          [F(1), F(3), F(0), F(0), F(0), F(0)],
          [F(-1), F(-2), F(0), F(2), F(-3), F(-3)],
          [F(3), F(1), F(-3), F(-1), F(1), F(-3)]]
    print('C4，q=4（已知可行）：')
    ok, _ = build_and_check(A, C, L0, 4, L4)
    print(f'  ⟹ 全部约束{"通过" if ok else "未通过"}')

    # 第二个实例：n=5,p=2,r=1 seed 3023 在 q0 阶的见证（此前已由 rank_stratified 给出）
    import qmin_scan_pr as QR
    import c208_q0_lower_bound as Q0
    import decide_symbolic as DS
    made = QR.make_instance(5, 2, 1, 3023 * 17 + 2 * 7 + 1)
    if made is not None:
        A2, C2, L02 = made
        qq = Q0.eta_and_q0(A2, C2, L02)[0]
        d2 = 5 - len(C2) - qq
        Kc = ZG.ker_cols([list(x) for x in C2] + [list(x) for x in L02])
        k = len(Kc[0])
        import itertools
        found = None
        for rows in itertools.combinations(range(k), d2):
            for th in ([F(0)], [F(1)], [F(2)]):
                if d2 * (k - d2) != len(th) * (1 if d2 * (k - d2) else 0):
                    pass
                Zv = DS.Z_from_theta(A2, C2, L02, qq, rows, [th[0]] * (d2 * (k - d2)))
                if ZG.bool_rank(ZG.cols_to_rows(Zv)) != d2:
                    continue
                Lw = ZG.L_from_Z(A2, C2, L02, Zv, qq)
                if Lw is None or not LQ.condA(A2, C2, Lw):
                    continue
                import toeplitz_criterion as TC
                if TC.analyse(A2, C2, Lw)['five_b']:
                    found = Lw
                    break
            if found:
                break
        if found:
            print(f'\n第二实例 n=5,p=2,r=1 seed 3023，q={qq}（已知可行）：')
            ok2, _ = build_and_check(A2, C2, L02, qq, found)
            print(f'  ⟹ 全部约束{"通过" if ok2 else "未通过"}')
        else:
            print('\n第二实例：未找到见证，跳过')


if __name__ == '__main__':
    main()
