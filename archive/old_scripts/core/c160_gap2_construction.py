r"""
c160_gap2_construction.py -- Gap 2 的显式构造检验

**目标**（[proof/S](../proof/S_维数下界定理_2026-10-21.md) §7）：
对固定的 admissible 的 A（dim = d+1-p、|A∩S| = 1），在 lift 空间里给出 (b) 成立的点。

**构造**（本脚本检验的形式）：

  取 A 的基 v_1 = α0, v_2, ..., v_ρ，L = A∩S（1 维，取 l 为其非零元）。
  令
  $$\Lambda v_i := a_i + \eta_i\, l,\qquad v_iA' = a_i + s_i\ (a_i\in\mathcal A,\ s_i\in S)$$
  （分解存在因为 $\mathcal A+S=\mathbb{R}^d$），$\eta_i$ 任意（这是**自由度**）。
  取 $q=\rho+1$ 行：
  $$\ell_i := v_iN^{+} + k_i,\qquad k_iR_0 = \Lambda v_i + c_i l - v_iA' - v_iN^{+}R_0$$
  （右边 $\in S$，而 $k\mapsto kR_0$ 满射到 $S$，故 $k_i$ 存在）。
  最后 $\ell_{q} := v_\rho N^+ + k_\rho$（$\rho$ 个自由行 + 首行 $L_0$，共 $q=\rho+1$）。

  $(a)$ 自动成立（$f_i=\Lambda v_i+c_il\in\mathcal A$）；$(b)$ 取决于 $(\eta,c)$。

跑法：python scripts/core/c160_gap2_construction.py
"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr

import audit_independent as AI
import c141_invariant_family as F

mul = AI.mul


def make_instance(rng, n=8, d_t=4, p=2):
    for _ in range(80):
        A_ = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if AI.rank(C) != p:
            continue
        if AI.rank(AI.vstack([C, mul(C, A_)])) != n - d_t:
            continue
        L0 = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        D = AI.build_data(A_, C, L0)
        if D["d"] != d_t or not D["inV"]:
            continue
        if all(x == 0 for x in D["alpha0"]):
            continue
        return A_, C, L0, D
    return None


def decompose(w, Ar, S):
    """把 w = a + s 分解（a∈A, s∈S）：用 S^⊥ 判定 a∈A"""
    n = len(w)
    Sa = AI.nullspace(S)                # S^⊥：{y : s·y = 0 ∀s∈S}
    # 求 c 使 a = sum c_i Ar_i 满足 (w - a) ⊥ S^⊥
    rows = []
    rhs = []
    for y in Sa:
        rows.append([sum(Ar[i][j] * y[j] for j in range(n)) for i in range(len(Ar))])
        rhs.append(sum(w[j] * y[j] for j in range(n)))
    if not rows:
        a = [Fr(0)] * n
        return a, list(w)
    sol = F.solve_affine(rows, rhs, len(Ar))
    if sol is None:
        return None
    x0, _ = sol
    a = [sum(x0[i] * Ar[i][j] for i in range(len(Ar))) for j in range(n)]
    s = [w[j] - a[j] for j in range(n)]
    return a, s


def main():
    print("=" * 74)
    print("Gap 2：显式构造 + (b) 的检验")
    print("=" * 74)
    got = make_instance(random.Random(0))
    if got is None:
        print("no instance")
        return
    A_, C, L0, D = got
    n, d = 8, 4
    N, Ap, R0 = D["N"], D["Ap"], D["R0"]
    AN = mul(A_, N)
    al, be = D["alpha0"], mul(L0, AN)[0]
    S = AI.row_basis(R0)
    # 选 L ⊆ S 使 A = span{al,be}+L 是 3 维且 |A∩S| = 1
    best = None
    for k in range(len(S)):
        l = S[k]
        Ar = AI.row_basis([al, be, l])
        if len(Ar) != 3:
            continue
        inter = 3 + len(S) - AI.rank(AI.row_basis(Ar + S))
        if inter == 1:
            best = (Ar, l)
            break
    if best is None:
        print("找不到 |A∩S|=1 的 A")
        return
    Ar, l = best
    print(f"dimA={len(Ar)} dimS={len(S)} |A∩S|=1")
    # 基：v_1 = al，其余
    basis = [al]
    for v in Ar:
        if len(AI.row_basis(basis + [v])) > len(basis):
            basis.append(v)
        if len(basis) == 3:
            break
    basis = AI.row_basis(basis)
    # N^+
    NtN = mul(AI.tr(N), N)
    iNtN = AI.inv(NtN)
    Npinv = mul(iNtN, AI.tr(N))       # d×n
    ok = 0
    tot = 0
    for trial in range(12):
        rr = random.Random(trial)
        # Λ v_i = a_i + η_i l
        Lam_rows = []
        phi = []          # φ(v_i) = Λ v_i（用于后面组装）
        for i, v in enumerate(basis):
            w = mul([v], Ap)[0]
            dec = decompose(w, basis, S)
            if dec is None:
                phi = None
                break
            a, _ = dec
            eta = Fr(rr.randint(-2, 2))
            Lam_rows.append([a[j] + eta * l[j] for j in range(d)])
        if not phi and Lam_rows == []:
            continue
        # 自由行：ℓ_i N = v_i（i=0..2），共用 3 行 + 首行 = q=4
        Lrows = []
        good = True
        for i in range(3):
            v = basis[i]
            viNp = mul([v], Npinv)[0]      # 1×n
            # k_i R0 = Λv_i + c_i l - v_i A' - (viNp) R0
            c_i = Fr(rr.randint(-2, 2))
            rhs = [Lam_rows[i][j] + c_i * l[j] - mul([v], Ap)[0][j]
                   - mul([viNp], R0)[0][j] for j in range(d)]
            # 解 k R0 = rhs **且 k N = 0**（k ∈ R^n）
            m = n
            rows = [[R0[j][t] for j in range(m)] + [rhs[t]] for t in range(d)]
            rows += [[N[j][t] for j in range(m)] + [Fr(0)] for t in range(d)]
            R, piv = AI.rref(rows)
            if any(p == m for p in piv):
                good = False
                break
            k = [Fr(0)] * m
            for r, cc in enumerate(piv):
                k[cc] = R[r][m]
            ell = [viNp[j] + k[j] for j in range(n)]
            Lrows.append(ell)
        if not good:
            continue
        L = [list(L0[0])] + Lrows
        M = mul(L, N)
        tot += 1
        if AI.rank(M) != 3:
            continue
        a5 = AI.cond_5a_orig(A_, C, L)
        b5 = AI.cond_5b_orig(A_, C, L)
        ok += (a5 and b5)
        if trial < 6:
            print(f"  trial{trial}: rankM={AI.rank(M)} (5a)={a5} (5b)={b5}")
    print(f"\n构造的 lift：{tot} 个，其中 (a)∧(b) 成立 {ok} 个")


if __name__ == "__main__":
    main()
