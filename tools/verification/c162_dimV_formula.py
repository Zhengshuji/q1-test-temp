"""
c162_dimV_formula.py — 检验 q_min = dim V + 1

给定 (A, C, L0)：
  1. 算 d, p, A', R0, S, V = <S>_{A'}
  2. 若 alpha0 ∉ V：报告"不可行"
  3. 否则构造 q = dim V + 1 行的 L，使 row(LN) = V（自动满足 (5a)）
  4. 精确验证 (5a) 与 (5b)（(5b) 用子式 gcd 判定）

用法：python c162_dimV_formula.py            # 跑内置的 6 个实例
      python c162_dimV_formula.py --random 20  # 跑 20 个随机实例
"""
import sys, os, json, random, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "exact_linalg"))
from fractions import Fraction as Fr
import audit_independent as AI

mul, tr, rank = AI.mul, AI.tr, AI.rank

# ---------- 基本量 ----------

def reduced_data(A, C, L0):
    D = AI.build_data(A, C, L0)
    d, Ap, R0 = D["d"], D["Ap"], D["R0"]
    S = AI.row_basis(R0)
    p = len(S)
    V = AI.row_basis(S)
    for _ in range(d + 2):
        imgs = [mul([v], Ap)[0] for v in V]
        V2 = AI.row_basis(V + imgs)
        if len(V2) == len(V):
            break
        V = V2
    return dict(d=d, Ap=Ap, R0=R0, S=S, p=p, V=V, alpha0=D["alpha0"], inV=D["inV"])


# ---------- (5a) / (5b) ----------

def cond5a(L, A, C):
    """rank[LA;L;CA;C] == rank[L;CA;C]"""
    CA = mul(C, A)
    LA = mul(L, A)
    return rank(AI.vstack([LA, L, CA, C])) == rank(AI.vstack([L, CA, C]))


def cond5b(L, A, C):
    """rank[lam L - LA; CA; C] == rank[L;CA;C] for all lam  (gcd of maximal minors == const)"""
    q, n = len(L), len(A)
    CA = mul(C, A)
    LA = mul(L, A)
    rows = []
    for i in range(q):
        rows.append([[ -LA[i][j], L[i][j]] for j in range(n)])
    for i in range(len(CA)):
        rows.append([[CA[i][j], Fr(0)] for j in range(n)])
    for i in range(len(C)):
        rows.append([[C[i][j], Fr(0)] for j in range(n)])
    h = rank(AI.vstack([L, CA, C]))
    mins = []
    # 取 h 行 **和 h 列**（方阵子式）
    for rr in itertools.combinations(range(len(rows)), h):
        for cc in itertools.combinations(range(n), h):
            v = AI._det_poly([[rows[r][c] for c in cc] for r in rr])
            if any(x != 0 for x in v):
                mins.append(v)
    if not mins:
        return None
    g = mins[0]
    for v in mins[1:]:
        g = AI.pgcd(g, v)
        if len(g) <= 1:
            break
    return len(g) - 1          # 0 == 常数 == (5b) 成立


# ---------- 构造 ----------

def make_L(A, C, L0, D, rng, tries=300):
    """构造 q = dim V + 1 行的 L，使 row(LN) = V，且 (5a)∧(5b)。
       返回 (L, 尝试次数) 或 (None, tries)"""
    n, d = len(A), D["d"]
    rho = len(D["V"])
    q = rho + 1
    r = len(L0)
    if q <= r:
        # 若 r 已经 >= q，用 L0 的前 q 行（不足补零行）
        L = [row[:] for row in L0[:q]]
        while len(L) < q:
            L.append([Fr(0)] * n)
        if cond5a(L, A, C) and cond5b(L, A, C) == 0:
            return L, 0
        return None, 0
    for t in range(tries):
        L = [row[:] for row in L0]
        for _ in range(q - r):
            L.append([Fr(rng.randint(-2, 2)) for _ in range(n)])
        if cond5a(L, A, C) and cond5b(L, A, C) == 0:
            return L, t
    return None, tries


# ---------- 主流程 ----------

def run(name, A, C, L0, rng):
    D = reduced_data(A, C, L0)
    d, p, rho = D["d"], D["p"], len(D["V"])
    lo = rho + 1
    if not D["inV"]:
        print(f"{name:22s} d={d} p={p} dimV={rho} | 不可行 (alpha0 ∉ V) | 下界 = {lo}")
        return None
    L, t = make_L(A, C, L0, D, rng)
    ok = L is not None
    print(f"{name:22s} d={d} p={p} dimV={rho} | 下界 = {lo} | 构造 q={lo} 成功={ok}"
          + (f" (试了 {t+1} 次)" if ok else f" (试了 {t} 次失败)"))
    if ok:
        print(f"{'':22s}   (5a)={cond5a(L,A,C)}  (5b) gcd={cond5b(L,A,C)}")
    return dict(name=name, d=d, p=p, dimV=rho, lower=lo, found=ok, L=(L if ok else None))


def main():
    rng = random.Random(2024)
    out = []
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "--random":
        m = int(sys.argv[2]) if len(sys.argv) > 2 else 20
        for t in range(m):
            n = rng.choice([4, 5, 6, 7])
            p = rng.choice([1, 2])
            A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
            C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
            L0 = [[Fr(rng.randint(-2, 2)) for _ in range(n)]]
            try:
                out.append(run(f"rand{t}", A, C, L0, rng))
            except Exception as ex:
                print(f"rand{t}: ERR {type(ex).__name__} {ex}")
    else:
        toF = lambda rows: [[Fr(x) for x in r] for r in rows]
        for f, nm in [("counterexample_candidate.json", "cand(d=3,p=1)"),
                      ("counterexample_d4.json", "d4(n=6,p=1)"),
                      ("counterexample_p2.json", "p2(n=8,p=2)")]:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "proof", "refuted", "certificates", f)
            if not os.path.exists(path):
                print(f"{nm}: 文件缺失"); continue
            d0 = json.load(open(path, encoding="utf-8"))
            try:
                out.append(run(nm, toF(d0["A"]), toF(d0["C"]), toF(d0["L0"]), rng))
            except Exception as ex:
                print(f"{nm}: ERR {type(ex).__name__} {ex}")
        # 2010 完整例
        A = [[Fr(0),Fr(1),Fr(0),Fr(1),Fr(0),Fr(0),Fr(0),Fr(0)],[Fr(0),Fr(-1),Fr(1),Fr(0),Fr(0),Fr(0),Fr(0),Fr(-1)],
             [Fr(1),Fr(0),Fr(-1),Fr(1),Fr(0),Fr(0),Fr(1),Fr(-1)],[Fr(-1),Fr(-1),Fr(0),Fr(-2),Fr(0),Fr(0),Fr(0),Fr(0)],
             [Fr(0),Fr(0),Fr(0),Fr(0),Fr(-2),Fr(0),Fr(0),Fr(1)],[Fr(0),Fr(0),Fr(0),Fr(0),Fr(0),Fr(-2),Fr(1),Fr(0)],
             [Fr(0),Fr(0),Fr(0),Fr(0),Fr(0),Fr(-1),Fr(-2),Fr(1)],[Fr(0),Fr(0),Fr(0),Fr(0),Fr(0),Fr(0),Fr(1),Fr(-2)]]
        C = [[Fr(-2),Fr(-2),Fr(2),Fr(-2),Fr(-1),Fr(0),Fr(1),Fr(-3)],[Fr(0),Fr(0),Fr(1),Fr(2),Fr(2),Fr(3),Fr(-1),Fr(-2)]]
        L0 = [[Fr(-2),Fr(-1),Fr(-2),Fr(-3),Fr(-1),Fr(3),Fr(2),Fr(0)],[Fr(1),Fr(-1),Fr(-2),Fr(1),Fr(0),Fr(2),Fr(0),Fr(1)]]
        out.append(run("2010 example", A, C, L0, rng))

    valid = [o for o in out if o]
    feas = [o for o in valid if o["dimV"] >= 0]
    found = [o for o in feas if o["found"]]
    print(f"\n汇总：{len(feas)} 个可行实例，构造成功 {len(found)}，失败 {len(feas)-len(found)}")
    if found:
        print("dimV 分布：", sorted(o["dimV"] for o in found))


if __name__ == "__main__":
    main()
