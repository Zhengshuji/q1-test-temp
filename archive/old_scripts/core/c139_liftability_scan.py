r"""
c139_liftability_scan.py -- 卡点扫描：固定实例下，逐个合格子空间 A 判定 "(b)-liftable"

背景：见 proof/H_卡点定位_2026-10-20.md。
  * 坐标形式：$\mathcal A=\mathrm{row}(M)\subseteq\mathbb{R}^d$（$\rho=\dim\mathcal A$），
    $M$ 首行 $=\alpha_0$，$F=MA'+G$，$G$ 首行 $=L_0R_0$ 固定。
  * **P4b 强制** $q\ge\rho+1$，所以 $\rho=2$ 时最小可行行数是 $q=3$（本脚本取 $q=3$）。
  * 对固定 $\mathcal A$：把 $L=[L_0;\ell_2;\ell_3]$ 的约束写成对 $(\ell_2,\ell_3)$ 的**线性**条件
       (a)  $\ell_iN\in\mathcal A$ 且 $\ell_iAN\in\mathcal A$（$i=2,3$）
    再用取样点检验 (b)（Zariski-开）。命中的点用**原始 4 块 (5a)** 与**原始铅笔 (5b)** 直接复核。

结论口径：
  * 找到见证 ⟹ 该 $\mathcal A$ 可 lift（**可验证**，非统计）。
  * 取样全失败 ⟹ 只报"未找到"（不声称不可能），并记录解空间维数。

跑法：python scripts/core/c139_liftability_scan.py
"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr

import audit_independent as AI

mul, tr, rank, rref = AI.mul, AI.tr, AI.rank, AI.rref
vstack, sub, row_basis, in_span = AI.vstack, AI.sub, AI.row_basis, AI.in_span
cond_5a_orig, cond_5b_orig = AI.cond_5a_orig, AI.cond_5b_orig


def cross3(u, v):
    return [u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0]]


def solve_affine(rows_eq, rhs, n):
    """{x : A x = rhs} 的仿射描述 (x0, null_basis)；不相容返回 None"""
    A = [list(rows_eq[i]) + [rhs[i]] for i in range(len(rows_eq))]
    R, piv = rref(A)
    if n in piv: return None
    x0 = [Fr(0)] * n
    for i, p in enumerate(piv): x0[p] = R[i][n]
    free = [c for c in range(n) if c not in piv]
    basis = []
    for f in free:
        v = [Fr(0)] * n; v[f] = Fr(1)
        for i, p in enumerate(piv): v[p] = -R[i][f]
        basis.append(v)
    return x0, basis


def constraints_for_A(A_, N, AN, al, m2, m3):
    r"""$(\ell_2,\ell_3)$ 的线性约束：(a) 的 $\ell_iN\in\mathcal A$、$\ell_iAN\in\mathcal A$。
    $\mathcal A=\mathrm{span}\{\alpha_0,m\}$（$m$ 与 $\alpha_0$ 独立），用叉积 $\alpha_0\times m$ 表示其零化向量。"""
    n, d = AI.cols(A_), AI.cols(N)
    nA = cross3(al, m2)
    rows, rhs = [], []
    for m in (m2, m3):
        # ℓN = m 的**分量形式**太强（A 是 2 维，m 未必可达）；改为：ℓN ∈ A（1 个线性方程）
        rows.append([sum(N[j][k] * nA[k] for k in range(d)) for j in range(n)]); rhs.append(Fr(0))
        rows.append([sum(AN[j][k] * nA[k] for k in range(d)) for j in range(n)]); rhs.append(Fr(0))
    # 拼成 2n 列的方程组
    big = []
    for i, r in enumerate(rows):
        e = [Fr(0)] * (2 * n)
        off = 0 if i < 2 else n
        for j in range(n): e[off + j] = r[j]
        big.append(e)
    return big, rhs


def try_A(A_, C, L0, D, m, rng, n_trials=8):
    r"""对 $\mathcal A=\mathrm{span}\{\alpha_0,m\}$ 判定 liftable（q=3）。返回 (L, dim, tried)"""
    al, N, Ap = D["alpha0"], D["N"], D["Ap"]
    n, d = AI.cols(A_), AI.cols(N)
    AN = mul(A_, N)
    m2 = m
    m3 = [al[j] + m[j] for j in range(d)]        # 第三个方向（在 A 内）
    big, rhs = constraints_for_A(A_, N, AN, al, m2, m3)
    sol = solve_affine(big, rhs, 2 * n)
    if sol is None: return None, 0, 0
    x0, basis = sol
    for _ in range(n_trials):
        x = list(x0)
        for v in basis:
            c = Fr(rng.randint(-2, 2))
            x = [x[j] + c * v[j] for j in range(2 * n)]
        l2, l3 = x[:n], x[n:]
        L = [list(L0[0]), l2, l3]
        M = mul(L, N)
        if rank(M) != 2: continue               # 需要 row(M) 恰为 A
        if cond_5a_orig(A_, C, L) and cond_5b_orig(A_, C, L):
            return L, len(basis), n
    return None, len(basis), n_trials


def scan(seed, n=5, rng_dirs=4, nilpotent=False):
    rng = random.Random(seed)
    if nilpotent:
        A_, C, L0, D = AI.nilpotent_instance(rng, n)
    else:
        # 一般实例（CA²≠0 的情形才可能 liftable；A²=0 时 Lean 定理给出 (5b) 必败）
        A_, C, L0, D = AI.rand_instance(rng, n)
    if D["d"] != 3: return None
    S = row_basis(D["R0"]) if rank(D["R0"]) > 0 else []
    al = D["alpha0"]
    be = mul(L0, mul(A_, D["N"]))[0]
    par = in_span(be, [al])
    out = dict(seed=seed, d=D["d"], obs=D["obs"], dimS=len(S), beta_par=par, cases=[],
               nilpotent=nilpotent)
    ms = []
    if not par:
        ms = [be]                                   # A 被强制
    else:
        for k in range(-rng_dirs, rng_dirs + 1):
            t = Fr(k, 3)
            m = [(Fr(1) if j == 0 else Fr(0)) + t * al[j] for j in range(D["d"])]
            if rank([al, m]) == 2: ms.append(m)
    for m in ms:
        basisAS = row_basis(vstack([S, [al], [m]])) if S else row_basis([[al], [m]])
        va, vm = mul([al], D["Ap"])[0], mul([m], D["Ap"])[0]
        adm = in_span(va, basisAS) and in_span(vm, basisAS)
        basisA = row_basis([al, m])
        leak = (not in_span(va, basisA)) or (not in_span(vm, basisA))
        inter = rank([al, m]) + rank(S) - rank(basisAS)
        wit, dim, tried = try_A(A_, C, L0, D, m, rng)
        out["cases"].append(dict(adm=adm, leak=leak, inter=inter, lift=wit is not None,
                                 dim=dim, tried=tried))
    return out


if __name__ == "__main__":
    print("=" * 78)
    print("扫描 d=3, rho=2, q=3（P4b 的最小可行行数）")
    print("每个 A 检查：admissible? A∩S≠0? AA'⊄A? liftable?（见证用原始 (5a)/(5b) 复核）")
    print("=" * 78)
    tot = dict(cases=0, adm=0, live=0, lift=0, inst=0, inst_live=0)
    for seed in range(20):
        o = scan(seed)
        if o is None: continue
        tot["inst"] += 1
        any_live = False
        for c in o["cases"]:
            tot["cases"] += 1; tot["adm"] += c["adm"]
            live = c["adm"] and c["inter"] >= 1
            tot["live"] += live; tot["lift"] += c["lift"]
            any_live |= live
        tot["inst_live"] += any_live
        print(f"[seed {seed}] obs={o['obs']} dimS={o['dimS']} β0∝α0={o['beta_par']} "
              f"#A={len(o['cases'])} 活区A={any_live} liftable={sum(c['lift'] for c in o['cases'])}")
    print("\n" + "=" * 78)
    print(f"实例 {tot['inst']} 个；试探的 A 共 {tot['cases']} 个")
    print(f"admissible {tot['adm']}；落在活区(admissible 且 A∩S≠0) {tot['live']}；liftable {tot['lift']}")
    print(f"至少有一个活区 A 的实例：{tot['inst_live']}/{tot['inst']}")
    print("=" * 78)
    print("读法：随机实例的强制 A=span{a0,b0} 多数有 A∩S=0；注意 P6 的『A∩S=0 ⟹ (b) 必败』")
    print("      还需 ℓ↦(ℓN,ℓR0) 单射才成立（2026-10-20 更正），故只作提示。")
