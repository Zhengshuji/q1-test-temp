r"""
audit_independent.py -- 独立复核 P1（两侧判据）/ A19（rho<=obs）/ P4b（rho<=q-1）

设计原则（与项目内脚本的区别）：
  1. **不 import 项目任何库**：本文件自带 Fraction 线代与多项式算术。
  2. **在原始形式上判**，不经过项目归约：
       (5a)  rank[LA; L; CA; C] == rank[L; CA; C]          （4 块，原样）
       (5b)  [λL-LA; CA; C] 的 r0 阶子式 gcd 为非零常数  （r0 = rank[L;CA;C]）
     即：不调用 (A)/(S) 的等价表述。
  3. 判据侧只用定义：
       N = ker[C;CA] 的基,  A' = (NᵀN)^{-1}NᵀAN,  R0 = AN - NA',
       V = row(R0) 在 A' 下的最小不变包,  α0 = L0·N.

跑法： python scripts/core/audit_independent.py
输出： 各检验的计数与断言结果（全过则 exit 0）
"""
import random
from fractions import Fraction as Fr
from itertools import combinations

# ---------------------------------------------------------------- 线代（Fraction）

def rows(M): return len(M)
def cols(M): return len(M[0]) if M else 0

def mul(A, B):
    assert cols(A) == rows(B), (rows(A), cols(A), rows(B), cols(B))
    Bt = list(zip(*B))
    return [[sum(A[i][k] * Bt[j][k] for k in range(cols(A))) for j in range(cols(B))]
            for i in range(rows(A))]

def tr(A): return [list(r) for r in zip(*A)]

def vstack(Ms):
    out = []
    for M in Ms:
        assert M, "empty block"
        out.extend([list(r) for r in M])
    return out

def sub(A, B): return [[A[i][j] - B[i][j] for j in range(cols(A))] for i in range(rows(A))]

def rref(M):
    A = [[Fr(x) for x in r] for r in M]
    if not A: return A, []
    m, n = rows(A), cols(A)
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c] != 0), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(n)]
        piv.append(c); r += 1
        if r == m: break
    return A, piv

def rank(M):
    if not M or not M[0]: return 0
    return len(rref(M)[1])

def inv(M):
    m = rows(M); assert m == cols(M)
    A = [list(map(Fr, M[i])) + [Fr(1) if j == i else Fr(0) for j in range(m)] for i in range(m)]
    R, piv = rref(A)
    assert len(piv) == m, "singular"
    return [R[i][m:] for i in range(m)]

def nullspace(M):
    """基（每个列向量用 list 表示），并**强制残差校验**"""
    A, piv = rref(M)
    m, n = rows(A), cols(A)
    free = [c for c in range(n) if c not in piv]
    basis = []
    for f in free:
        v = [Fr(0)] * n
        v[f] = Fr(1)
        for i, p in enumerate(piv):
            v[p] = -A[i][f]
        basis.append(v)
    # 残差校验
    for v in basis:
        for i in range(m):
            s = sum(M[i][j] * v[j] for j in range(n))
            assert s == 0, "nullspace residual != 0"
    return basis   # 每个是长度 n 的列向量

def row_basis(M):
    """行空间的一组基（rref 非零行）"""
    if not M or not M[0]: return []
    R, piv = rref(M)
    return [R[i] for i in range(len(piv))]

def in_span(v, basis):
    if not basis: return all(x == 0 for x in v)
    return rank(vstack([basis, [v]])) == rank(basis)

# ---------------------------------------------------------------- 多项式（升序系数）

def ptrim(p):
    q = list(p)
    while len(q) > 1 and q[-1] == 0: q.pop()
    return q

def pzero(p):  return ptrim(p) == [Fr(0)]
def pconst_nonzero(p):
    p = ptrim(p)
    return len(p) == 1 and p[0] != 0

def padd(a, b):
    n = max(len(a), len(b))
    return ptrim([(a[i] if i < len(a) else Fr(0)) + (b[i] if i < len(b) else Fr(0)) for i in range(n)])

def psub(a, b):
    n = max(len(a), len(b))
    return ptrim([(a[i] if i < len(a) else Fr(0)) - (b[i] if i < len(b) else Fr(0)) for i in range(n)])

def pmul(a, b):
    if pzero(a) or pzero(b): return [Fr(0)]
    r = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == 0: continue
        for j, y in enumerate(b):
            if y != 0: r[i + j] += x * y
    return ptrim(r)

def pdivmod(a, b):
    a = ptrim(a); b = ptrim(b)
    if pzero(b): raise ZeroDivisionError
    if len(a) < len(b): return [Fr(0)], a
    q = [Fr(0)] * (len(a) - len(b) + 1)
    r = list(a)
    while not pzero(r) and len(r) >= len(b):
        d = len(r) - len(b)
        c = r[-1] / b[-1]
        q[d] = c
        for i in range(len(b)):
            r[d + i] -= c * b[i]
        r = ptrim(r)
    return ptrim(q), r

def pgcd(a, b):
    a = ptrim(a); b = ptrim(b)
    if pzero(a): return ptrim(b) if not pzero(b) else [Fr(0)]
    if pzero(b): return a
    while not pzero(b):
        _, r = pdivmod(a, b)
        a, b = b, r
    return [x / a[-1] for x in a] if a[-1] != 0 else a

# ---------------------------------------------------------------- 原始 (5a)/(5b)

def cond_5a_orig(A, C, L):
    """rank[LA;L;CA;C] == rank[L;CA;C]"""
    CA = mul(C, A); LA = mul(L, A)
    return rank(vstack([LA, L, CA, C])) == rank(vstack([L, CA, C]))

def cond_5b_orig(A, C, L):
    """[λL-LA; CA; C] 的 r0 阶子式 gcd 为非零常数（r0 = rank[L;CA;C]）"""
    CA = mul(C, A); LA = mul(L, A)
    base = vstack([L, CA, C]); r0 = rank(base)
    q, n = rows(L), cols(L)
    # pencil 的第 i 行：λ L_i - (LA)_i ; 其后两行块与 λ 无关
    P = []
    for i in range(q):
        P.append([psub([Fr(0), L[i][j]], [LA[i][j]]) for j in range(n)])
    for M in (CA, C):
        for r in M:
            P.append([[Fr(x)] for x in r])
    mins = []
    for rs in combinations(range(rows(P)), r0):
        for cs in combinations(range(n), r0):
            # 子式（Laplace，r0 很小）
            det = [[P[rs[i]][cs[j]] for j in range(r0)] for i in range(r0)]
            val = _det_poly(det)
            if not pzero(val): mins.append(val)
    if not mins: return False
    g = mins[0]
    for m in mins[1:]:
        g = pgcd(g, m)
        if pconst_nonzero(g): return True
    return pconst_nonzero(g)

def _det_poly(M):
    k = len(M)
    if k == 1: return ptrim(M[0][0])
    if k == 2:
        return psub(pmul(M[0][0], M[1][1]), pmul(M[0][1], M[1][0]))
    acc = [Fr(0)]
    for j in range(k):
        if pzero(M[0][j]): continue
        minor = [[M[i][c] for c in range(k) if c != j] for i in range(1, k)]
        term = pmul(M[0][j], _det_poly(minor))
        acc = padd(acc, term) if j % 2 == 0 else psub(acc, term)
    return ptrim(acc)

# ---------------------------------------------------------------- 判据侧

def build_data(A, C, L0):
    CA = mul(C, A)
    Nc = nullspace(vstack([C, CA]))          # 列向量基：长度 n 的列表
    n = cols(A); d = len(Nc)
    N = [[Nc[j][i] for j in range(d)] for i in range(n)]   # n x d
    NtN = mul(tr(N), N)
    Ap = mul(inv(NtN), mul(tr(N), mul(A, N)))
    R0 = sub(mul(A, N), mul(N, Ap))
    V = row_basis(R0)                         # row(R0) 的基（行向量，长度 d）
    while V:                                  # R0=0 时 V=[]（obs=0），不进入循环
        V2 = row_basis(vstack([V, mul(V, Ap)]))
        if len(V2) == len(V): break
        V = V2
    alpha0 = mul(L0, N)[0]
    return dict(N=N, d=d, Ap=Ap, R0=R0, V=V, obs=len(V), alpha0=alpha0,
                inV=in_span(alpha0, V))

def rho_of(L, N): return rank(mul(L, N))

# ---------------------------------------------------------------- 检验

def rand_instance(rng, n):
    while True:
        A = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        L0 = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        try:
            D = build_data(A, C, L0)
        except AssertionError:
            continue
        if D["d"] == 0: continue
        if all(x == 0 for x in D["alpha0"]): continue   # L0N ≠ 0（非退化）
        if rank(C) < 1: continue
        return A, C, L0, D

def block_instance(rng, n, m):
    """A 在 W=span{e_1..e_m} 上不变（左下块为 0），L0 支撑在 W 内。
    ⟹ 任何行都在 W 内的 L 都满足 (5a)（因为 row(LA) ⊆ W ⊆ row(L,C,CA)）。"""
    A = [[Fr(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i >= m and j < m:      # 左下块置 0 ⟹ W 是 A-不变子空间
                continue
            A[i][j] = Fr(rng.randint(-1, 1))
    C = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
    L0 = [[Fr(rng.randint(-1, 1)) if j < m else Fr(0) for j in range(n)]]
    return A, C, L0

def w_row(rng, n, m):
    """W 内的随机行"""
    return [Fr(rng.randint(-2, 2)) if j < m else Fr(0) for j in range(n)]

def test_A(seed=1, n_inst=40, n_try=400, qmax=2):
    """检验： (5a)∧(5b) ⟹ α0∈V, ρ≤obs, ρ≤q-1
    实例两半：一般实例（随机 L，作对照）+ 块实例（L 行在不变子空间内 ⟹ (5a) 必成立）。"""
    rng = random.Random(seed)
    pos = 0; neg_5a = 0; struct_used = 0
    pos_inV = pos_not = 0
    inst_inV = inst_not = 0
    viol = []
    for k in range(n_inst):
        n = 5
        if k % 2 == 0:
            A, C, L0 = block_instance(rng, n, 3)
            D = build_data(A, C, L0)
            if D["d"] == 0 or all(x == 0 for x in D["alpha0"]): continue
            if D["inV"]: inst_inV += 1
            else: inst_not += 1
        else:
            A, C, L0, D = rand_instance(rng, n)
        for t in range(n_try):
            if k % 2 == 0:
                # q = m = 3：三行都在 W 内且张成 W ⟹ row(LA) ⊆ W = row(L) ⟹ (5a)
                L = [list(L0[0])] + [w_row(rng, n, 3) for _ in range(2)]
                if rank(L) != 3: continue
                q = 3
                struct_used += 1
            else:
                q = 2 + rng.randint(0, qmax - 1)
                L = [list(L0[0])] + [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(q - 1)]
            if not cond_5a_orig(A, C, L):
                neg_5a += 1; continue
            if not cond_5b_orig(A, C, L):
                continue
            pos += 1
            rho = rho_of(L, D["N"])
            if D["inV"]: pos_inV += 1
            else: pos_not += 1
            if not D["inV"]: viol.append(("5a&5b but alpha0 notin V", D["obs"], rho))
            if rho > D["obs"]: viol.append(("rho>obs", rho, D["obs"]))
            if rho > q - 1: viol.append(("rho>q-1", rho, q))
    return dict(pos=pos, pos_inV=pos_inV, pos_not=pos_not, neg_5a=neg_5a,
                struct=struct_used, inst_inV=inst_inV, inst_not=inst_not, viol=viol)

def brute_force_solution(A, C, L0, grid, max_extra):
    """穷举 |R|<=max_extra 的候选（条目取自 grid），返回第一个满足 (5a)∧(5b) 的 L"""
    n = cols(A)
    for k in range(max_extra + 1):
        if k == 0:
            L = [list(r) for r in L0]
            if cond_5a_orig(A, C, L) and cond_5b_orig(A, C, L): return L
            continue
        for combo in __import__("itertools").product(grid, repeat=k):
            L = [list(r) for r in L0] + [[Fr(v) for v in x] for x in combo]
            if cond_5a_orig(A, C, L) and cond_5b_orig(A, C, L): return L
    return None

def p7_criterion(A, C, L0, D):
    """RESULTS §2.7 的 rho<=1 判据（用定义独立实现）：
       S = {ℓ : ℓN ∈ span{α0}, ℓAN ∈ span{α0}}
       可达 ⟺ L0 ∈ S 且  (ℓ ↦ (u,w)) 的像维数 = 2
    """
    N, d = D["N"], D["d"]; al = D["alpha0"]; n = cols(A)
    AN = mul(A, N)
    # 未知量 (ℓ_1..ℓ_n, u, w)；方程 ℓN - u α0 = 0 与 ℓAN - w α0 = 0
    M = []
    for i in range(d):
        M.append([N[j][i] for j in range(n)] + [-al[i], Fr(0)])
    for i in range(d):
        M.append([AN[j][i] for j in range(n)] + [Fr(0), -al[i]])
    sols = nullspace(M)                    # 每个是 (ℓ, u, w)
    if not sols: return False, 0
    UW = [s[n:] for s in sols]
    S_basis = row_basis([s[:n] for s in sols])
    has_L0 = in_span(list(L0[0]), S_basis)
    uw_dim = rank(UW)
    return (has_L0 and uw_dim == 2), uw_dim

def nilpotent_instance(rng, n=4):
    r"""构造 $\rho\le1$ 可能达成的实例：取 $A^2=0$（$A=uv^{\mathsf T}$, $v^{\mathsf T}u=0$）。
    则 $CA^2=0$ ⟹ $K$ 是 $A$-不变 ⟹ $A'^2=0$ ⟹ 可取 $\\alpha_0$ 为 $A'$ 的左零向量
    （于是 $\\beta_0=\\alpha_0A'=0\\in\\operatorname{span}\\{\\alpha_0\\}$），再由 $L_0N=\\alpha_0$ 反解 $L_0$。
    ⟹ 这是"$\\rho\\le1$ 可达"的**非空**一侧样本。"""
    while True:
        u = [[Fr(rng.randint(-1, 1))] for _ in range(n)]
        v = [[Fr(rng.randint(-2, 2)) for _ in range(n)]]
        if all(x == 0 for x in [u[i][0] for i in range(n)]): continue
        # vᵀu = 0 保证 A²=0
        s = sum(v[0][i] * u[i][0] for i in range(n))
        if s != 0:
            k = next(i for i in range(n) if u[i][0] != 0)
            v[0][k] -= s / u[k][0]
            if all(x == 0 for x in v[0]): continue
        A = [[u[i][0] * v[0][j] for j in range(n)] for i in range(n)]
        C = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        try:
            CA = mul(C, A)
            Nc = nullspace(vstack([C, CA]))
        except AssertionError:
            continue
        d = len(Nc)
        if d == 0: continue
        N = [[Nc[j][i] for j in range(d)] for i in range(n)]
        NtN = mul(tr(N), N)
        Ap = mul(inv(NtN), mul(tr(N), mul(A, N)))
        # 拒绝：A' 必须是幂零（应当自动成立），且核非零
        if any(x != 0 for r in mul(Ap, Ap) for x in r): continue
        ys = nullspace(tr(Ap))          # A'ᵀ y = 0  ⟹ α = yᵀ 满足 αA' = 0
        if not ys: continue
        al = [ys[0][j] for j in range(d)]     # 长度 d 的行向量
        # L0 = α (NᵀN)^{-1} Nᵀ
        L0 = mul([al], mul(inv(NtN), tr(N)))
        D = build_data(A, C, L0)
        if all(x == 0 for x in D["alpha0"]): continue
        return A, C, L0, D

def test_C(seed=3, n_inst=20, n=4):
    """小实例：P7 的 rho<=1 判据 vs 穷举（|R|≤1）。
    一半是幂零构造（$\\rho\\le1$ 可达的非空侧），一半随机（空侧）。
    ⟹ 两侧都有点，避免"两边都 False"的空洞一致。"""
    rng = random.Random(seed)
    grid = [(a, b, c, e) for a in (-1, 0, 1) for b in (-1, 0, 1)
            for c in (-1, 0, 1) for e in (-1, 0, 1)]
    agree = disagree = 0; details = []
    checked = 0; ct = bt = 0
    for k in range(n_inst):
        try:
            if k % 2 == 0:
                A, C, L0, D = nilpotent_instance(rng, n)
            else:
                A, C, L0, D = rand_instance(rng, n)
        except AssertionError:
            continue
        checked += 1
        crit, uw = p7_criterion(A, C, L0, D)
        sol = brute_force_solution(A, C, L0, grid, 1)
        brute = sol is not None and rho_of(sol, D["N"]) <= 1
        ct += bool(crit); bt += bool(brute)
        if brute == crit: agree += 1
        else:
            disagree += 1; details.append((D["obs"], crit, brute, uw))
    return dict(checked=checked, agree=agree, disagree=disagree, details=details,
                crit_true=ct, brute_true=bt)

def test_B(seed=2, n_inst=12, n=4):
    """小实例上：判据 vs 穷举（|R|≤1）一致性；obs=1 时两人都能给结论"""
    rng = random.Random(seed)
    grid = [(a, b, c, e) for a in (-1, 0, 1) for b in (-1, 0, 1)
            for c in (-1, 0, 1) for e in (-1, 0, 1)]
    agree = 0; disagree = []; found_yes = 0; found_no = 0
    checked = 0
    while checked < n_inst:
        A, C, L0, D = rand_instance(rng, n)
        if D["obs"] != 1:      # 只在 obs=1 时，判据说 "q<=2 就够"
            continue
        checked += 1
        sol = brute_force_solution(A, C, L0, grid, 1)
        crit = D["inV"]
        if sol is not None: found_yes += 1
        else: found_no += 1
        ok = (sol is not None) == crit
        if ok: agree += 1
        else: disagree.append((A, C, L0, crit, sol is not None, D["obs"]))
    return dict(checked=checked, agree=agree, disagree=disagree,
                found_yes=found_yes, found_no=found_no)

if __name__ == "__main__":
    print("=" * 74)
    print("A. (5a)∧(5b) ⟹ α0∈V / ρ≤obs / ρ≤q-1   （原始 4 块与原始铅笔上判）")
    ra = test_A(seed=1, n_inst=30, n_try=200, qmax=3)
    print(f"   结构化候选 {ra['struct']}，随机候选 {ra['neg_5a']} 个未过 (5a)")
    print(f"   (5a)∧(5b) 成立的样本: {ra['pos']}  （其中 α0∈V: {ra['pos_inV']}, α0∉V: {ra['pos_not']}）")
    print(f"   实例: α0∈V {ra['inst_inV']} 个, α0∉V {ra['inst_not']} 个")
    print(f"   违规: {len(ra['viol'])}")
    for v in ra["viol"][:5]: print("     ", v)

    print("=" * 74)
    print("B. 判据 vs 穷举（n=4, obs=1, |R|≤1）")
    rb = test_B(seed=2, n_inst=14)
    print(f"   实例 {rb['checked']}；一致 {rb['agree']}；不一致 {len(rb['disagree'])}")
    print(f"   穷举: 找到解 {rb['found_yes']} / 未找到 {rb['found_no']}")

    print("=" * 74)
    print("C. P7（ρ≤1 判据）—— **本轮未接入结论**")
    print("   说明：随机实例只能给出 False 点；幂零构造虽能造出 L0∈S，")
    print("   但 (ℓ↦(u,w)) 的像维数恒为 1 ⟹ 判据与穷举**两边都是 False**（空洞）。")
    print("   按项目规则（等价性检验必含 True 点），本节不计入复核结论。")
    rc = None

    print("=" * 74)
    ok = (len(ra["viol"]) == 0 and ra["pos"] > 0
          and ra["pos_not"] == 0 and len(rb["disagree"]) == 0)
    print("RESULT:", "PASS" if ok else "FAIL")
