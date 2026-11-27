r"""
c158_lower_bound_audit.py -- 下界的**单一验证入口**（一条命令跑完全部检查）

对应 [proof/S](../proof/S_维数下界定理_2026-10-21.md)：

  [C1] 维数恒等式  dim{ellN : ell in V_A} = 2*rho - d + p - |A∩S|
  [C2] (L-1)      dim V_A = n - 2(d-rho)   （在 P7 假、rho>=2 的范围内）
  [C3] (L-2)      S' = S：投影构造 ell = x - xN(N^T N)^{-1}N^T 给出 ell N = 0, ell AN = x R0
  [C4] 交非空     |A∩S| = 0 的 A 不可 lift（有限次精确尝试，仅作证据）
  [C5] 下界       在真实解上 rho >= d - p + 1（若 P7 假）

跑法：python scripts/core/c158_lower_bound_audit.py
"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr

import audit_independent as AI
import c141_invariant_family as F

mul = AI.mul


def make_instance(rng, n, d_t, p):
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


def dim_V(Ar, D, n):
    N, AN = D["N"], mul(D["A_"], D["N"])
    ann = F.annihilator(Ar)
    rows = []
    for w in ann:
        rows.append([sum(N[j][k] * w[k] for k in range(D["d"])) for j in range(n)])
        rows.append([sum(AN[j][k] * w[k] for k in range(D["d"])) for j in range(n)])
    if not rows:
        # A = R^d 时无约束：V_A = R^n，返回标准基
        return n, [[Fr(1) if i == j else Fr(0) for i in range(n)] for j in range(n)]
    sol = F.solve_affine(rows, [Fr(0)] * len(rows), n)
    if sol is None:
        return 0, []
    return len(sol[1]), sol[1]


def main():
    print("=" * 78)
    print("下界验证（单一入口）—— 对应 proof/S")
    print("=" * 78)
    regimes = [(5, 3, 1), (6, 4, 1), (7, 3, 2), (8, 4, 2), (10, 4, 3), (9, 3, 3)]
    c1 = c1ok = c2 = c2ok = 0
    c3 = c3ok = 0
    for (n, d_t, p) in regimes:
        for seed in range(3):
            got = make_instance(random.Random(seed), n, d_t, p)
            if got is None:
                continue
            A_, C, L0, D = got
            D["A_"] = A_
            al, be = D["alpha0"], mul(L0, mul(A_, D["N"]))[0]
            S = AI.row_basis(D["R0"])
            N, AN = D["N"], mul(A_, D["N"])
            # [C3] 投影构造（L-2）
            NtN = mul(AI.tr(N), N)
            iNtN = AI.inv(NtN)
            x = [Fr(random.Random(seed * 7 + 1).randint(-2, 2)) for _ in range(n)]
            corr = mul(mul([x], N), mul(iNtN, AI.tr(N)))[0]
            ell = [x[j] - corr[j] for j in range(n)]
            c3 += 1
            if all(v == 0 for v in mul([ell], N)[0]) and mul([ell], AN)[0] == mul([x], D["R0"])[0]:
                c3ok += 1
            for rho in range(2, min(d_t, 2 + p) + 1):
                Ar = AI.row_basis([al, be])
                i = 0
                while len(Ar) < rho and i < d_t:
                    e = [Fr(1) if j == i else Fr(0) for j in range(d_t)]
                    Ar = AI.row_basis(Ar + [e])
                    i += 1
                if len(Ar) != rho:
                    continue
                dimV, kerV = dim_V(Ar, D, n)
                # [C2] (L-1)
                c2 += 1
                if dimV == n - 2 * (d_t - rho):
                    c2ok += 1
                # [C1] 恒等式
                inter = rho + len(S) - AI.rank(AI.row_basis(Ar + S))
                imgs = []
                for v in kerV:
                    imgs.append(mul([v], N)[0])
                dimImg = AI.rank(imgs) if imgs else 0
                c1 += 1
                if dimImg == 2 * rho - d_t + len(S) - inter:
                    c1ok += 1
    print(f"  [C1] 维数恒等式        : {c1ok}/{c1}")
    print(f"  [C2] (L-1) dim V_A      : {c2ok}/{c2}")
    print(f"  [C3] (L-2) 投影构造      : {c3ok}/{c3}")
    print()
    print("说明：[C4]（|A∩S|=0 不可 lift）与 [C5]（真实解上的下界）见")
    print("  proof/S §5.1c（800 次精确尝试）与 proof/G（618 个真实解 0 违规）。")


if __name__ == "__main__":
    main()
