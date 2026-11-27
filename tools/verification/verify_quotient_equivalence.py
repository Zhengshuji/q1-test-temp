r"""Theorem Q（商等价定理）与系数恒等式的机器核对。

## 定理 Q（[已证-纸面]，证明见 proof/quotient_equivalence/README.md）

设 $Z\subseteq H=\ker[C;L_0]$、$\dim Z=d$、$S=Z\cap V$（$V=\ker[C;CA]$）、
$U=Z/S\subseteq W_m=W/S$、$P(\lambda)=(A-\lambda I)|_{V/S}$。若 $A(S)\subseteq Z$，则对每个 $\lambda\in\mathbb C$
$$\operatorname{rank}\big[(\lambda I-A)V\ \big|\ Z\big]=\dim(V+Z)
\iff \operatorname{rank}\big[U\mid P(\lambda)\big]=r+t .$$

## 系数恒等式（[精确验证]，仅 $q=t$ 域）

$\det[U\mid P(\lambda)]=\sum_j\lambda^j\langle a_j,p_U\rangle$，$a_j$ 来自 `coeff_forms_full`，
符号按 Laplace 展开（`laplace_sign`）计入。

## 做法（构造，不采样）

1. 取 $S\subseteq V\cap D$（$D=\{x:Ax\in H\}$），小整数组合；
2. 取 $U\supseteq A(S)/S$、$\dim U=r$、$U\cap V/S=0$、$U\subseteq H/S$
   ⟹ $Z=S\oplus U$ 自动满足 $(A)$；
3. 在 $\lambda\in\{0,\pm1,\pm2,3,1/2\}$ 上逐点比较两个秩（含"同时失败"的方向）。

**等级**：精确验证（有理算术、有限 $\lambda$ 点数）。逐点检查不能替代 $\forall\lambda$ 的推导；
定理本身的证明在 README（纸面）。

用法：python tools/verification/verify_quotient_equivalence.py
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
import coeff_of_S as CS
import spectral_gcd as SG

LAMBDAS = [Fr(0), Fr(1), Fr(-1), Fr(2), Fr(-2), Fr(3), Fr(1, 2)]


def unit(n, i):
    return [Fr(1) if k == i else Fr(0) for k in range(n)]


def r17():
    N = 8
    C = [unit(N, 0), unit(N, 1)]
    L0 = [unit(N, 2)]
    A = [[Fr(0)] * N for _ in range(N)]
    A[6][2] = Fr(1); A[7][3] = Fr(1); A[4][4] = Fr(1)
    A[5][5] = Fr(1); A[0][6] = Fr(1); A[1][7] = Fr(1)
    return A, C, L0


def c282():
    N = 8
    C = [unit(N, 0), unit(N, 1)]
    L0 = [unit(N, 2)]
    A = [[Fr(0)] * N for _ in range(N)]
    for (i, j) in [(0, 2), (1, 3), (4, 4), (3, 5), (5, 6), (6, 7)]:
        A[i][j] = Fr(1)
    return A, C, L0


def second():
    n = 6
    C = [unit(n, 0)]
    L0 = [unit(n, 1)]
    A = [[Fr(0)] * n for _ in range(n)]
    A[0][5] = Fr(1)
    for i in (1, 2, 3, 4):
        A[i][i] = Fr(1)
    return A, C, L0


def matvec(M, x):
    return [sum(M[i][k] * x[k] for k in range(len(x))) for i in range(len(M))]


def rank_of(cols):
    """cols：列向量列表（同长度 n）。返回秩。"""
    if not cols:
        return 0
    n = len(cols[0])
    return AI.rank([[cols[j][i] for j in range(len(cols))] for i in range(n)])


def det(M):
    """精确行列式（Fraction，Gauss 消元，就地修改副本）。"""
    n = len(M)
    if n == 0:
        return Fr(1)
    A = [list(row) for row in M]
    d = Fr(1)
    for i in range(n):
        p = next((k for k in range(i, n) if A[k][i] != 0), None)
        if p is None:
            return Fr(0)
        if p != i:
            A[i], A[p] = A[p], A[i]
            d = -d
        d *= A[i][i]
        inv = Fr(1) / A[i][i]
        for k in range(i + 1, n):
            f = A[k][i] * inv
            for j in range(i, n):
                A[k][j] -= f * A[i][j]
    return d


def prune_cols(cols):
    """去掉冗余的列向量（保秩）。"""
    out = []
    for c in cols:
        if rank_of(out + [c]) > len(out):
            out.append(c)
    return out


def plucker(U, m):
    """U：r 个长度为 m 的列向量。返回 p[I]（I 按字典序），p[I]=det(U[I,:])。"""
    r = len(U)
    return [det([[U[b][i] for b in range(r)] for i in I])
            for I in itertools.combinations(range(m), r)]


def intersect_V_D(A, V, H):
    """V ∩ {x : Ax ∈ H} 的基。"""
    n = len(A)
    Hperp = AI.nullspace([list(x) for x in H])          # H 的零化子（y·h=0）
    rows = AI.nullspace([list(x) for x in V])           # V 的零化子
    for y in Hperp:
        rows.append([sum(A[i][k] * y[i] for i in range(n)) for k in range(n)])  # (Aᵀy)
    return AI.nullspace(rows)


def check_instance(name, A, C, L0, q, s, nS=3, nU=3, verbose=True):
    n = len(A)
    CA = AI.mul(C, A)
    V = AI.nullspace([row[:] for row in (C + CA)])
    W = AI.nullspace([row[:] for row in C])
    H = AI.nullspace([row[:] for row in (C + L0)])
    v, w, h = len(V), len(W), len(H)
    d = w - q
    if d < 0 or d > h:
        return dict(checked=0, bad=0, det_checks=0, det_bad=0, note='d 越界')
    r, t, wm = d - s, v - s, w - s
    if r < 0 or t < 0:
        return dict(checked=0, bad=0, det_checks=0, det_bad=0, note='r/t < 0')
    hth = v + d - s
    VD = intersect_V_D(A, V, H)
    # S 还要 ⊆ H（S=Z∩V，Z⊆H）；取 VD ∩ H 作采样池
    VDH = AI.nullspace(AI.nullspace([list(x) for x in VD]) + AI.nullspace([list(x) for x in H]))
    if s > 0 and len(VDH) < s:
        return dict(checked=0, bad=0, det_checks=0, det_bad=0, note='dim(V∩D∩H)<s')

    # ---- 枚举 S（VD 的随机小整数组合；每行是一个 s 维子空间的基组合） ----
    import random
    rng = random.Random(20261101)
    Ss = [[]] if s == 0 else []
    if s > 0:
        seen = set()
        for _trial in range(4000):
            if len(Ss) >= nS:
                break
            combos = [[rng.randint(-2, 2) for _ in range(len(VDH))] for _ in range(s)]
            S = [[sum(Fr(c[j]) * VDH[j][i] for j in range(len(VDH))) for i in range(n)] for c in combos]
            if rank_of(S) != s:
                continue
            if rank_of(H + S) != h:
                continue
            key = tuple(tuple(x) for x in S)
            if key in seen:
                continue
            seen.add(key)
            Ss.append(S)

    checked = bad = det_checks = det_bad = 0
    for S in Ss:
        st = CS.setup(A, C, L0, q, S)
        assert st['r'] == r and st['t'] == t and st['wm'] == wm
        assert (r + t == wm) == (q == t), '方阵条件 r+t=w_m ⟺ q=t 失败'
        # A(S) 在 W/S 的坐标
        AS = []
        for x in S:
            Ax = matvec(A, x)
            AS.append(CS._solve_in_basis(st['WB'], Ax)[s:])
        rkAS = rank_of(AS) if AS else 0
        if rkAS > r:
            continue
        # U：含 A(S)/S，补到 dim r，与 V/S 不交
        ASb = prune_cols(AS)
        need = r - len(ASb)
        assert need >= 0
        pool = []
        for coefs in itertools.product((-1, 0, 1), repeat=len(st['HS'])):
            if all(c == 0 for c in coefs):
                continue
            pool.append([sum(Fr(coefs[j]) * st['HS'][j][k] for j in range(len(st['HS'])))
                         for k in range(wm)])
        best = None
        for combo in itertools.combinations(pool, need):
            U = list(ASb) + list(combo)
            if len(U) != r or rank_of(U) != r:
                continue
            if rank_of(st['VS'] + U) != t + r:
                continue
            best = U
            break
        if best is None:
            continue
        U = best
        Uvec = [[sum(U[j][k] * st['WB'][s + k][i] for k in range(wm)) for i in range(n)]
                for j in range(r)]
        Z = [list(x) for x in S] + Uvec
        if rank_of(Z) != d:
            continue
        # 定理 Q
        AV = [matvec(A, x) for x in V]
        cols = CS.pencil_cols(A, st)
        nok = 0
        for lam in LAMBDAS:
            Mcols = [[lam * V[j][i] - AV[j][i] for i in range(n)] for j in range(v)] + Z
            rM = rank_of(Mcols)
            Qc = [list(u) for u in U] + [[c0[i] + lam * c1[i] for i in range(wm)] for (c0, c1) in cols]
            rQ = rank_of(Qc)
            if rM != s + rQ:
                nok += 1
            elif (rM == hth) != (rQ == r + t):
                nok += 1
        checked += 1
        if nok:
            bad += 1
            if verbose:
                print(f'  !! {name} q={q} s={s}: {nok}/{len(LAMBDAS)} 个 λ 不符')
        # 系数恒等式（q=t）
        if q == t:
            a, (P0, P1), info = CS.coeff_forms_full(A, C, L0, q, S)
            idxs = info['idxs']
            p = plucker(U, wm)
            for lam in (Fr(0), Fr(1), Fr(2)):
                M = [[U[j][i] for j in range(r)] + [P0[i][j] + lam * P1[i][j] for j in range(t)]
                     for i in range(wm)]
                lhs = det(M)
                rhs = sum((lam ** j) * sum(CS.laplace_sign(I, r, wm) * p[k] * a[j][k]
                                           for k, I in enumerate(idxs))
                          for j in range(len(a)))
                det_checks += 1
                if lhs != rhs:
                    det_bad += 1
                    if verbose:
                        print(f'  !! det 恒等式不符：{name} q={q} s={s} λ={lam} {lhs} != {rhs}')
    return dict(checked=checked, bad=bad, det_checks=det_checks, det_bad=det_bad)


def main():
    print('Theorem Q：rank[(λI−A)V|Z] = dim(V+Z)  ⟺  rank[U|P(λ)] = r+t\n')
    cases = [
        ('R17', r17(), 3, 2),
        ('R17', r17(), 2, 2),
        ('R17', r17(), 2, 3),
        ('c282', c282(), 4, 1),
        ('c282', c282(), 3, 1),
        ('second', second(), 2, 2),
        ('second', second(), 3, 1),
    ]
    total = 0
    wrong = 0
    dc = db = 0
    for name, (A, C, L0), q, s in cases:
        res = check_instance(name, A, C, L0, q, s, nS=3, nU=3)
        total += res['checked']
        wrong += res['bad']
        dc += res['det_checks']
        db += res['det_bad']
        print(f'{name:7s} q={q} s={s}: 核对 {res["checked"]:2d} 个 Z，不符 {res["bad"]}；'
              f'det 恒等式 {res["det_checks"]:2d} 例，不符 {res["det_bad"]}'
              + (f'  [{res["note"]}]' if res.get('note') else ''))
    print(f'\n合计：Z {total} 个，Rank 不符 {wrong}；det {dc} 例，不符 {db}')
    assert wrong == 0 and db == 0, 'Theorem Q 或系数恒等式在核对中失败'
    print('Theorem Q ✓  系数恒等式 ✓')
    d0 = check_d0()
    print(f'\n命题 D0（d=0 边界）：随机实例 {d0["checked"]} 个，一致 {d0["ok"]} 个')
    assert d0['ok'] == d0['checked'], '命题 D0 在随机实例上失败'
    print('命题 D0 ✓')


def check_d0(trials=40):
    r"""命题 D0：$d=0$（$q=w$，$Z=0$）时

    $$(S)\iff V\cap\ker(\\lambda I-A)=0\ \\ \\forall\\lambda
    \iff A\ \text{在}\ V\ \text{里没有特征向量}.$$

    核对方式：随机对角整数 $A$（特征值已知）、随机 $C,L_0$；比较
    $\gcd\{\text{所有 } v\times v \text{ 子式 of }[(\lambda I-A)V]\}$ 的次数
    与"每个特征值 $\mu$ 都有 $V\cap\ker(\mu I-A)=0$"。
    """
    import random
    rng = random.Random(20261101)
    ok = 0
    checked = 0
    for _ in range(trials):
        n = rng.choice([4, 5, 6])
        p = rng.choice([1, 2])
        diag = [rng.randint(-2, 2) for _ in range(n)]
        A = [[Fr(0)] * n for _ in range(n)]
        for i in range(n):
            A[i][i] = Fr(diag[i])
        C = [unit(n, i) for i in range(p)]
        L0 = [unit(n, p)]
        V = AI.nullspace([row[:] for row in (C + AI.mul(C, A))])
        v = len(V)
        if v == 0:
            continue
        # [(λI−A)V] 的 v×v 子式的 gcd（多项式）
        cols = []
        for j in range(v):
            AV = matvec(A, V[j])
            cols.append([[-AV[i], V[j][i]] for i in range(n)])   # c0 + c1·λ
        g = None
        for rows in itertools.combinations(range(n), v):
            M = [[cols[j][i] for j in range(v)] for i in rows]
            d = SG.pdet(M)
            if SG.pdeg(d) >= 0:
                g = d if g is None else SG.pgcd(g, d)
        deg0 = SG.pdeg(g) == 0 if g is not None else False
        # 直接判据：每个特征值 μ，V ∩ ker(μI−A) = 0
        good = True
        for mu in sorted(set(diag)):
            K = AI.nullspace([[mu * (1 if i == k else 0) - A[i][k] for k in range(n)]
                              for i in range(n)])
            if rank_of(K + [list(x) for x in V]) < rank_of(K) + len(V):
                good = False
        checked += 1
        if deg0 == good:
            ok += 1
        else:
            print(f'  !! D0 不符：n={n} diag={diag} gcd常数={deg0} 无特征向量={good}')
    return dict(checked=checked, ok=ok)


if __name__ == '__main__':
    main()
