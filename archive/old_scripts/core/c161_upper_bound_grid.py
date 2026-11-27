r"""
c161_upper_bound_grid.py -- 上界构造在任意 (p,d) 上的验证（推广 c160）

**目标**：对给定的 $(p,d,n)$，构造
$$\mathcal A\ \ (\dim=d+1-p,\ \mathcal A\supseteq\operatorname{span}\{\alpha_0,\beta_0\},\ |\mathcal A\cap S|=1)$$
再用 c160 的公式造 lift，精确检验 $(a)\wedge(b)$、$\operatorname{rank}M=\rho=d+1-p$。

构造：
  1. 取 $L\subseteq S$ 一条线（扫 $S$ 的基向量），令 $\mathcal A_0=\operatorname{span}\{\alpha_0,\beta_0,L\}$；
  2. 用 $\mathcal A_0$ 的补向量把 $\mathcal A$ 撑到 $d+1-p$ 维（补向量取一般位置、且避开 $S$ 方向）；
  3. 校验 $\dim(\mathcal A+S)=d$、$|\mathcal A\cap S|=1$；
  4. 造 lift（c160 的 S1–S4），精确判 $(5a)\wedge(5b)$。

跑法：python scripts/core/c161_upper_bound_grid.py
"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr

import audit_independent as AI
import c141_invariant_family as F
import c160_gap2_construction as C

mul = AI.mul


def make_instance(rng, n, d_t, p):
    """构造**可行**实例：先取 (A,C)，再用 alpha0 ∈ V 反解 L0"""
    for _ in range(60):
        A_ = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cm = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if AI.rank(Cm) != p:
            continue
        if AI.rank(AI.vstack([Cm, mul(Cm, A_)])) != n - d_t:
            continue
        D0 = AI.build_data(A_, Cm, [[Fr(0)] * n])
        V = D0["V"]
        if not V:
            continue
        # alpha0 = V 的随机非零组合
        coeff = [Fr(rng.randint(-2, 2)) for _ in range(len(V))]
        if all(x == 0 for x in coeff):
            coeff[0] = Fr(1)
        al = [sum(coeff[i] * V[i][j] for i in range(len(V))) for j in range(d_t)]
        if all(x == 0 for x in al):
            continue
        # 解 L0 N = al
        N = D0["N"]
        rows = [[N[j][k] for j in range(n)] + [al[k]] for k in range(d_t)]
        R, piv = AI.rref(rows)
        if any(pp == n for pp in piv):
            continue
        L0v = [Fr(0)] * n
        for r, cc in enumerate(piv):
            L0v[cc] = R[r][n]
        L0 = [L0v]
        D = AI.build_data(A_, Cm, L0)
        if D["d"] != d_t or not D["inV"]:
            continue
        return A_, Cm, L0, D
    return None


def build_A(D, rng, d_t, p):
    """构造 dim = d+1-p 的 A：含 al,be，|A∩S|=1，A+S=R^d"""
    N, Ap, R0 = D["N"], D["Ap"], D["R0"]
    al, be = D["alpha0"], mul([D["L0"][0]] if "L0" in D else [], N)[0] if False else None
    return None


def build_A2(A_, L0, D, rng, d_t, p):
    N, Ap, R0 = D["N"], D["Ap"], D["R0"]
    AN = mul(A_, N)
    al, be = D["alpha0"], mul(L0, AN)[0]
    S = AI.row_basis(R0)
    if len(S) != p:
        return None
    target = d_t + 1 - p
    for k in range(len(S)):
        l = S[k]
        base = AI.row_basis([al, be, l])
        if len(base) < 3 and target >= 3:
            continue
        # 补向量：避开 S，直到 target 维
        cur = [list(v) for v in base]
        tries = 0
        while len(AI.row_basis(cur)) < target and tries < 60:
            u = [Fr(rng.randint(-2, 2)) for _ in range(d_t)]
            cand = AI.row_basis(cur + [u])
            if len(cand) > len(cur):
                # 不许把 A∩S 撑大
                AS = AI.row_basis(cand + S)
                inter = len(cand) + len(S) - len(AS)
                if inter == 1:
                    cur = cand
            tries += 1
        Ar = AI.row_basis(cur)
        if len(Ar) != target:
            continue
        AS = AI.row_basis(Ar + S)
        if len(AS) != d_t:
            continue
        inter = len(Ar) + len(S) - len(AS)
        if inter != 1:
            continue
        adm = all(AI.in_span(mul([v], Ap)[0], AS) for v in Ar)
        if not adm:
            continue
        return Ar, l
    return None


def build_lift(A_, L0, D, Ar, l, cvec=None):
    n = len(A_[0])
    N, Ap, R0 = D["N"], D["Ap"], D["R0"]
    d_t = D["d"]
    S = AI.row_basis(R0)
    rho = len(Ar)
    NtN = mul(AI.tr(N), N)
    try:
        iN = AI.inv(NtN)
    except AssertionError:
        return None
    Npinv = mul(iN, AI.tr(N))
    # Λ v_i = A-分量
    Lam = []
    for v in Ar:
        dec = C.decompose(mul([v], Ap)[0], Ar, S)
        if dec is None:
            return None
        Lam.append(dec[0])
    if cvec is None:
        cvec = [Fr(1)] * rho
    Lrows = []
    for i in range(rho):
        v = Ar[i]
        viNp = mul([v], Npinv)[0]
        rhs = [Lam[i][j] + cvec[i] * l[j] - mul([v], Ap)[0][j] - mul([viNp], R0)[0][j]
               for j in range(d_t)]
        rows = [[R0[j][t] for j in range(n)] + [rhs[t]] for t in range(d_t)]
        rows += [[N[j][t] for j in range(n)] + [Fr(0)] for t in range(d_t)]
        R, piv = AI.rref(rows)
        if any(pp == n for pp in piv):
            return None
        k = [Fr(0)] * n
        for r, cc in enumerate(piv):
            k[cc] = R[r][n]
        Lrows.append([viNp[j] + k[j] for j in range(n)])
    return [list(L0[0])] + Lrows


def main():
    print("=" * 78)
    print("上界构造：任意 (p,d) 上的验证")
    print("=" * 78)
    grid = [(1, 3), (1, 4), (2, 4), (2, 5)]
    for (p, d_t) in grid:
        n = d_t + 2 * p          # 使 rank[C;CA] = 2p ⟹ d = n-2p ✓
        got = make_instance(random.Random(hash((p, d_t)) % 1000), n, d_t, p)
        if got is None:
            print(f"  (p={p},d={d_t},n={n}): 无法生成实例")
            continue
        A_, Cm, L0, D = got
        rng = random.Random(7 * p + d_t)
        gotA = build_A2(A_, L0, D, rng, d_t, p)
        if gotA is None:
            print(f"  (p={p},d={d_t},n={n}): 找不到合格 A")
            continue
        Ar, l = gotA
        L = build_lift(A_, L0, D, Ar, l)
        if L is None:
            print(f"  (p={p},d={d_t},n={n}): lift 构造失败")
            continue
        M = mul(L, D["N"])
        a5 = AI.cond_5a_orig(A_, Cm, L)
        b5 = AI.cond_5b_orig(A_, Cm, L)
        rho = AI.rank(M)
        tgt = d_t + 1 - p
        print(f"  (p={p},d={d_t},n={n}): rankM={rho}(目标 {tgt})  (5a)={a5}  (5b)={b5}"
              f"  {'✓' if (a5 and b5 and rho == tgt) else '✗'}")


if __name__ == "__main__":
    main()
