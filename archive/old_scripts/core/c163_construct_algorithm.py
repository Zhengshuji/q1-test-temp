"""
c163_construct_algorithm.py — 按 LEMMA_LIFT §21 的构造实现 q = dim V + 1 的解

算法：
  1. 算 d, N, A', R0, S, V, rho, p
  2. 检查 alpha0 ∈ V（可行性）
  3. q = rho + 1
  4. 取 v_1..v_rho 为 V 的基；解 ℓ_i N = v_i（i = 1..rho）
  5. 取 ℓ_{rho+1} ∈ ker(ℓ ↦ ℓN)（自由）
  6. 在上述自由度内（ℓ_i ↦ ℓ_i + k_i, k_i N = 0）随机搜索，使 (5a)∧(5b)
  7. 精确验证

与 c162 的区别：本脚本按 §21 的结构**显式**分解 Φ = [Φ_1; φ_2]，
并统计"第一次尝试就成功"的比率（检验 §21 的"一般位置"预测）。
"""
import sys, os, json, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import audit_independent as AI
import c162_dimV_formula as M

mul, rank = AI.mul, AI.rank


def solve_l(Nmat, v, n, d):
    """解行向量 l 使 l·N = v（N 是 n×d）。"""
    Aeq = AI.tr(Nmat)                       # d x n
    aug = [[Aeq[i][j] for j in range(n)] + [v[i]] for i in range(d)]
    R, piv = AI.rref(aug)
    for i in range(len(R)):
        if all(R[i][j] == 0 for j in range(n)) and R[i][n] != 0:
            return None
    l = [Fr(0)] * n
    for i, c in enumerate(piv):
        if i < len(R):
            l[c] = R[i][n]
    return l


def construct(A, C, L0, rng, tries=50):
    """返回 (L, n_tries) 或 (None, tries)"""
    n = len(A)
    D = M.reduced_data(A, C, L0)
    d, S, V, Ap, R0 = D["d"], D["S"], D["V"], D["Ap"], D["R0"]
    rho, p = len(V), len(S)
    if not D["inV"]:
        return None, 0, "不可行 (alpha0 ∉ V)"
    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    Nmat = [[Nv[j][i] for j in range(d)] for i in range(n)]
    Vb = AI.row_basis(V)
    KerN = AI.nullspace(AI.tr(Nmat))          # {l : lN = 0}（n 维向量）

    # 基础行：l_i N = v_i
    base = []
    for i in range(rho):
        l = solve_l(Nmat, Vb[i], n, d)
        if l is None:
            return None, 0, "solve_l 失败"
        base.append(l)
    # 最后一行在 ker(N) 里
    q = rho + 1
    if q <= len(L0):
        q = len(L0)
    for t in range(tries):
        L = [row[:] for row in base]
        # 补足到 q 行
        while len(L) < q:
            coef = [Fr(rng.randint(-2, 2)) for _ in range(len(KerN))]
            last = [sum(coef[k] * KerN[k][j] for k in range(len(KerN))) for j in range(n)]
            L.append(last)
        if rank(mul(L, Nmat)) != rho:
            continue
        if M.cond5a(L, A, C) and M.cond5b(L, A, C) == 0:
            return L, t + 1, "成功"
    return None, tries, "失败"


def main():
    rng = random.Random(20251023)
    ok = 0
    tot = 0
    first_try = 0
    if len(sys.argv) > 1 and sys.argv[1] == "--random":
        m = int(sys.argv[2]) if len(sys.argv) > 2 else 30
        for t in range(m):
            n = rng.choice([4, 5, 6, 7])
            p_ = rng.choice([1, 2])
            A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
            C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p_)]
            L0 = [[Fr(rng.randint(-2, 2)) for _ in range(n)]]
            try:
                L, tries, msg = construct(A, C, L0, rng)
            except Exception as ex:
                print(f"rand{t}: ERR {type(ex).__name__}"); continue
            tot += 1
            if L is not None:
                ok += 1
                if tries == 1:
                    first_try += 1
                print(f"rand{t}: n={n} p={p_} | q={len(L)} ✓ ({tries} 次)")
            else:
                print(f"rand{t}: n={n} p={p_} | {msg}")
    else:
        toF = lambda rows: [[Fr(x) for x in r] for r in rows]
        cases = []
        for f, nm in [("counterexample_candidate.json", "cand"),
                      ("counterexample_d4.json", "d4"),
                      ("counterexample_p2.json", "p2")]:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "lit", f)
            if os.path.exists(path):
                d0 = json.load(open(path, encoding="utf-8"))
                cases.append((nm, toF(d0["A"]), toF(d0["C"]), toF(d0["L0"])))
        A10 = toF([[0,1,0,1,0,0,0,0],[0,-1,1,0,0,0,0,-1],[1,0,-1,1,0,0,1,-1],[-1,-1,0,-2,0,0,0,0],
                   [0,0,0,0,-2,0,0,1],[0,0,0,0,0,-2,1,0],[0,0,0,0,0,-1,-2,1],[0,0,0,0,0,0,1,-2]])
        C10 = toF([[-2,-2,2,-2,-1,0,1,-3],[0,0,1,2,2,3,-1,-2]])
        L10 = toF([[-2,-1,-2,-3,-1,3,2,0],[1,-1,-2,1,0,2,0,1]])
        cases.append(("2010", A10, C10, L10))
        for nm, A, C, L0 in cases:
            L, tries, msg = construct(A, C, L0, rng)
            tot += 1
            print(f"{nm:8s}: {msg}" + (f" q={len(L)} ({tries} 次)" if L else ""))
            if L is not None:
                ok += 1
                if tries == 1:
                    first_try += 1
    print(f"\n汇总：{tot} 个可行实例，成功 {ok}，其中一次命中 {first_try}")


if __name__ == "__main__":
    main()
