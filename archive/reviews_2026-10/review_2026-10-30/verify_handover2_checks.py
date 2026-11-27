"""HANDOVER2 的独立核对脚本（2026-10-30，接手者写，不是本项目原有脚本）。

目的：把 HANDOVER2 里"我独立算过的三件事"变成可复现的命令。

  (A) §82 反例实例的基本不变量：rank(A)=2、j=3、d=3、dim B=1。
  (B) §82 证书脚本的 lift 里有一个 `% 1`，它把整数 1 变成 0 ⟹ lift(e_i)=0
      ⟹ 脚本里的 "V" 实际秩为 1，28 个 6 阶子式**平凡地**全为零。
      （即 "0/28" 不是结论，是 bug 的产物。）
  (C) 修掉 `% 1` 之后同一个 V 在 λ=1 处的铅笔秩 = 6 ⟹ 至少一个子式非零
      ⟹ "全部子式恒为零" 不成立。
  (D) 但这个反例的**结论仍然是对的**，而且是**一行**的：rank(A)=2
      ⟹ dim π(C^n A) = 1 <= 2 = ρ-1 ⟹ 在 λ=0 处
      rank[-LA; CA; C] <= dim J + 1 = 4 < 6 = rank[L; CA; C] ⟹ (5b) 对所有 L 失败。

全部用 fractions.Fraction 精确算术，无第三方依赖。

用法：python workspace/review_2026-10-30/verify_handover2_checks.py
"""
from fractions import Fraction as F
import random

N = 6
A = [[-1, 0, 2, 1, -1, -1],
     [0, 2, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [-2, -1, 4, 2, -2, -2],
     [-2, 0, 4, 2, -2, -2],
     [0, -2, 0, 0, 0, 0]]
C = [[2, 1, -2, 2, -1, -1],
     [2, 2, 2, 1, -1, 1]]
L0 = [[1, 0, 0, 0, 0, 0]]


def mm(X, Y):
    assert len(X[0]) == len(Y), 'dim mismatch'
    return [[sum(F(X[i][k]) * F(Y[k][j]) for k in range(len(Y)))
             for j in range(len(Y[0]))] for i in range(len(X))]


def rank(M):
    if not M:
        return 0
    M = [[F(x) for x in r] for r in M]
    rows, cols, r = len(M), len(M[0]), 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return r


def row_basis(M):
    out = []
    for r in M:
        if rank(out + [r]) > len(out):
            out.append(r)
    return out


def part_A():
    print('(A) 反例实例的不变量')
    CA = mm(C, A)
    J = row_basis(C + CA)
    j = rank(J)
    # dim π(C^n A) = rank[A;J] - rank J
    dim_pi_XA = rank([list(r) for r in A] + J) - j
    # B = π(J A)：dim B = dim(JA+J) - dim J
    JA = mm(J, A)
    dimB = rank(JA + J) - j
    # U = X（d=3 时唯一）；B = π(JA) ⊆ X ⟹ μ = dim(B∩U) = dim B
    mu = dimB
    print(f'    rank(A) = {rank(A)}')
    print(f'    j = dim row[C;CA] = {j}  =>  d = {N - j}')
    print(f'    dim B = {dimB}   =>  μ = dim(B∩U) = {mu}   (P2 = YES)')
    print(f'    dim π(C^n A) = {dim_pi_XA}   (<= 2 是关键)')
    assert rank(A) == 2 and j == 3 and dim_pi_XA <= 2 and mu >= 1
    return CA, J, j, dim_pi_XA


def lift(BUG):
    """复刻 verify_counterexample_certificate.py 的 lift；BUG=True 保留 `% 1`。"""
    def make(Lmat, j):
        def f(u):
            a = [F(0)] * j + list(u)
            v = [sum(a[i] * F(Lmat[i][t]) for i in range(len(Lmat)))
                 for t in range(N)]
            return [x % 1 for x in v] if BUG else v
        return f
    return make


def part_B_C(CA, J, j):
    print('(B)/(C) §82 证书脚本的 lift bug')
    # 补空间 K（与项目脚本同一构造：J 之后按坐标顺序补）
    span = [list(r) for r in J]
    K = []
    for i in range(N):
        e = [F(1) if t == i else F(0) for t in range(N)]
        if rank(span + [e]) > len(span):
            K.append(e)
            span = row_basis(span + [e])
        if len(span) == N:
            break
    Lmat = J + K
    e_i = [[F(1) if t == i else F(0) for t in range(N)] for i in range(3)]

    f_bug = lift(True)(Lmat, j)
    f_ok = lift(False)(Lmat, j)
    bug_rows = [f_bug(x) for x in e_i]
    ok_rows = [f_ok(x) for x in e_i]
    print(f'    buggy lift(e_1) = {[str(x) for x in bug_rows[0]]}')
    print(f'    fixed lift(e_1) = {[str(x) for x in ok_rows[0]]}')
    assert rank(bug_rows) == 0, 'buggy lift 应当把每个 e_i 都打到 0'
    assert rank(ok_rows) == 3, '修正后的 lift 应当是单位截面'

    # 证书里的 V = [lift(x_i) + a_i tau0 (i=1..3)] + [lift(π(e1)) + a4 tau0]
    tau0 = None
    Linv = _inv(Lmat)
    for t in J:
        w = mm([t], A)[0]
        if any(x != 0 for x in _apply(Linv, w, j)):
            tau0 = [F(x) for x in t]
            break
    assert tau0 is not None

    def pencil_rank(V):
        LA = mm(V, A)
        M = [[F(l) * V[i][k] - LA[i][k] for k in range(N)] for i in range(4)] + CA + C
        return [rank(M)]

    pi_e1 = _apply(Linv, L0[0], j)[j:]      # e1 在 X 里的坐标

    def V_with(lift_f, a):
        rows = [[F(lift_f(e_i[i])[k]) + F(a[i]) * tau0[k] for k in range(N)]
                for i in range(3)]
        l0_lift = lift_f(pi_e1)
        rows.append([l0_lift[k] + F(a[3]) * tau0[k] for k in range(N)])
        return rows

    for tag, lf in (('buggy', f_bug), ('fixed', f_ok)):
        V = V_with(lf, [1, 0, 0, 0])
        print(f'    {tag}: rank(V) = {rank(V)}')
        if tag == 'buggy':
            assert rank(V) == 1
        else:
            assert rank(V) == 4
            # (C) 修正后 λ=1 处铅笔秩
            LA = mm(V, A)
            M1 = [[V[i][k] - LA[i][k] for k in range(N)] for i in range(4)] + CA + C
            r1 = rank(M1)
            r0 = rank(V + CA + C)
            print(f'    fixed: rank[λL-LA;CA;C] at λ=1 = {r1},  rank[L;CA;C] = {r0}')
            print(f'    => 存在非零 6 阶子式（λ=1 处秩满），所以"全部 28 个子式恒为零"**不成立**')
            assert r1 == r0 == 6


def _inv(M):
    n = len(M)
    M = [[F(x) for x in r] + [F(1) if i == k else F(0) for k in range(n)]
         for i, r in enumerate(M)]
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, n) if M[i][c] != 0), None)
        assert piv is not None, 'singular'
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(n):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return [row[n:] for row in M]


def _apply(Linv, x, j):
    # x 的行坐标：c = Lmat^{-T} x ；等价地 c_t = Σ_s Linv[s][t] x_s
    return [sum(Linv[s][t] * F(x[s]) for s in range(N)) for t in range(N)]


def part_D(CA, J, j, dim_pi_XA):
    print('(D) λ=0 的一行论证（对**任意** 4×6 的 L）')
    rng = random.Random(20261030)
    tried = ok = 0
    while ok < 200:
        L = [[F(rng.randint(-4, 4)) for _ in range(N)] for _ in range(4)]
        if rank(L) < 4:
            continue
        if 4 + j - rank(L + J) != 1:      # 类型 (3,1)：dim(V∩J)=1
            continue
        tried += 1
        r0 = rank(L + CA + C)             # 应为 6
        LA = mm(L, A)
        M0 = [[-LA[i][k] for k in range(N)] for i in range(4)] + CA + C
        assert r0 == 6
        assert rank(M0) <= j + dim_pi_XA < r0
        ok += 1
    print(f'    {ok}/200 个随机 (3,1) 格子：λ=0 处秩 <= {j + dim_pi_XA} < 6 = r0  ✓')
    print('    => 该实例的 (3,1) 层**不可行**（结论与 §82 相同），但证明不需要 28 个子式。')


if __name__ == '__main__':
    CA, J, j, dim_pi_XA = part_A()
    part_B_C(CA, J, j)
    part_D(CA, J, j, dim_pi_XA)
    print('\nALL CHECKS PASSED')
