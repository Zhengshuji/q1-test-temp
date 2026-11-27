# -*- coding: utf-8 -*-
"""
c6_open_region.py -- ⭐⭐⭐ 攻开放区域：非不变 + 退化 + k=1 时 (5b) 能否成立？

【构造（针对 q0=2, r=1）】
  C = e₁ᵀ；A 的前三行 = e₂ᵀ, e₃ᵀ, λ₀e₃ᵀ
  ⟹ C A = e₂ᵀ, C A² = e₃ᵀ, C A³ = λ₀e₃ᵀ   （CA² 是左特征向量）
  ⟹ K = ker C ∩ ker(CA) = span{e₃,…,e₆}，CA²|_K = e₃ᵀ|_K ≠ 0  ⟹ **非 A-不变**
  L₀ = C A = e₂ᵀ                ⟹ π(L₀) = 0  ⟹ **退化** ✓
  R  = e₃ᵀ + b·e₂ᵀ              ⟹ π(R) = π(CA²) = u, π(RA) = (λ₀+b)u ⟹ (5a) ✓
  L  = [L₀; R]                  ⟹ q0 = 2, k = 1 ✓

  ⟹ H 的第 1 行 = 0；H = [[0…],[u]]      ⟹ im H = span{(0,1)}
  ⟹ F 的第 2 行 = (λ₀+b)u, 第 1 行 = u  ⟹ im F = span{(1, λ₀+b)}  ← **不同直线！**
  ⟹ Λ 把 im H 送到**另一条**直线 ⟹ Λ 不保持 im H ⟹ **(S) 可能成立！**

【判定】枚举 (A)-解空间的 Λ，对每个 Λ **直接测 (5b)**
"""
import os, io, contextlib, random, itertools
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]
_lx = {}
with open(os.path.join(_HERE, "linalg_exact.py"), encoding="utf-8") as fh:
    exec(compile(fh.read(), "lx", "exec"), _lx)
solve_exact = _lx["solve_exact"]

_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]

def pt(p):
    while len(p) > 1 and p[-1] == 0: p = p[:-1]
    return p
def padd(a,b):
    n=max(len(a),len(b)); return pt([(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(n)])
def psub(a,b):
    n=max(len(a),len(b)); return pt([(a[i] if i<len(a) else F(0))-(b[i] if i<len(b) else F(0)) for i in range(n)])
def pmul(a,b):
    if a==[F(0)] or b==[F(0)]: return [F(0)]
    r=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]+=x*y
    return pt(r)
def pdivmod(a,b):
    a=a[:]; b=pt(b[:])
    if b==[F(0)]: return None
    db=len(b)-1; q=[F(0)]*max(1,len(a)-db)
    while len(a)-1>=db and not (len(a)==1 and a[0]==0):
        d=len(a)-1-db; co=a[-1]/b[-1]; q[d]+=co
        for i in range(len(b)): a[d+i]-=co*b[i]
        a=pt(a)
    return pt(q),a
def pgcd(a,b):
    a=pt(a[:]); b=pt(b[:])
    while not (len(b)==1 and b[0]==0):
        r=pdivmod(a,b)
        if r is None: break
        a,b=b,r[1]
    if len(a)>1 and a[-1]!=0:
        lc=a[-1]; a=[x/lc for x in a]
    return a
def pdet(M,k):
    if k==1: return M[0][0][:]
    tot=[F(0)]
    for j in range(k):
        sub=[row[:j]+row[j+1:] for row in M[1:]]
        d=pdet(sub,k-1); pr=pmul(M[0][j],d)
        tot=padd(tot,pr) if j%2==0 else psub(tot,pr)
    return pt(tot)

def solve_lin(Amat, bvec):
    b = [[x] for x in bvec]
    r = solve_exact(Amat, b)
    if r is None: return None
    y = r[0] if isinstance(r, tuple) else r
    for i in range(len(Amat)):
        if sum(Amat[i][k]*y[k] for k in range(len(Amat[0]))) != bvec[i]:
            return None
    return y

def all_A_solutions(Lm, Ac, Cc):
    """枚举 (A) 解空间中 Λ 的"自由部分"。

    逐行解 L A[i] = Σ_k Λ[i][k] L[k] + G0[i] C + G1[i] CA
    返回 Λ 的列表（只取一个特解 + 若干基本方向组合）。
    """
    CAc = mm(Cc, Ac); LA = mm(Lm, Ac); q0 = len(Lm); p = len(Cc); n = len(Lm[0])
    rows = []
    for i in range(q0):
        cols = []
        for kk in range(q0): cols.append([Lm[kk][j] for j in range(n)])
        for kk in range(p): cols.append([Cc[kk][j] for j in range(n)])
        for kk in range(p): cols.append([CAc[kk][j] for j in range(n)])
        Amat = [[cols[u][j] for u in range(len(cols))] for j in range(n)]
        sol = solve_lin(Amat, [LA[i][j] for j in range(n)])
        if sol is None: return None
        rows.append(sol)
    Lam = [[rows[i][k] for k in range(q0)] for i in range(q0)]
    return Lam

def check_5b(Lm, Ac, Cc, maxminors=3000):
    CAc = mm(Cc, Ac); LA = mm(Lm, Ac)
    base = [r[:] for r in Lm] + [r[:] for r in CAc] + [r[:] for r in Cc]
    r0 = rk(base); m = len(base); n = len(base[0])
    nL = len(Lm)
    P = [[ ([-LA[i][j], Lm[i][j]] if i < nL else [base[i][j]]) for j in range(n)] for i in range(m)]
    polys=[]; cnt=0
    for rows in itertools.combinations(range(m), r0):
        for cols in itertools.combinations(range(n), r0):
            d = pdet([[P[i][j] for j in cols] for i in rows], r0)
            if d is not None and not all(x==0 for x in d): polys.append(d)
            cnt += 1
            if cnt > maxminors: break
        if cnt > maxminors: break
    if not polys: return True, r0
    g = polys[0]
    for q in polys[1:]:
        g = pgcd(g, q)
        if len(g)==1: break
    return (len(g)==1), r0

def make_A(n, lam0, rng):
    A = [[F(0)]*n for _ in range(n)]
    A[0][1] = F(1); A[1][2] = F(1); A[2][2] = F(lam0)
    for i in range(3, n):
        for j in range(n): A[i][j] = F(rng.randint(-1,1))
    return A

def main():
    print("=== 开放区域：非不变 + 退化 + k=1（q0=2）===\n")
    print("%-6s %4s %5s %5s %4s %8s %8s %10s" %
          ("lam0","b","q0","k","rkH","(5a)","(5b)","结论"))
    print("-" * 62)
    rng = random.Random(20250901)
    yes = 0; tot = 0
    for lam0 in [0, 1, 2, -1]:
        for b in [0, 1, 2, -1]:
            n, p = 6, 1
            A = make_A(n, lam0, rng)
            C = [[F(0)]*n]; C[0][0] = F(1)
            CA = mm(C, A)
            ell0 = CA[0][:]                      # L0 = CA = e2^T
            rvec = CA[0][:]                      # CA
            CA2 = mm(CA, A)                      # = CA²
            Rrow = [CA2[0][i] + b*CA[0][i] for i in range(n)]   # R = CA² + b·CA
            L = [ell0[:], Rrow[:]]
            if rk(L) != 2: continue
            if rk(L + C) != 3: continue
            W = C + CA
            dCA = n - rk(W)
            if dCA < 2: continue
            N = ker_basis(W)
            if not N or not N[0] or len(N[0]) != dCA: continue
            try:
                _Lx, eta = p1(A, C, L)
            except Exception:
                continue
            if not eta: continue
            q0 = sum(eta); k = q0 - 1
            if k != 1: continue
            if dCA < q0: continue
            H = mm(L, N)
            if rk(H) == 0 or rk(H) >= q0: continue
            a_ok = (rk(mm(L, A) + L + W) == rk(L + W))
            b_ok, r0 = check_5b(L, A, C)
            tot += 1
            if a_ok and b_ok: yes += 1
            print("%-6d %4d %5d %5d %4d %8s %8s %10s" %
                  (lam0, b, q0, k, rk(H), "✓" if a_ok else "✗",
                   "**成立**" if b_ok else "失败",
                   "**YES ⭐⭐⭐**" if (a_ok and b_ok) else "NO"))
    print()
    print("测试 %d 个：满足 (5a)∧(5b)：%d" % (tot, yes))
    print()
    if yes:
        print("⟹⟹⟹ **开放区域也可是 YES** ⟹ c6′ **完全被证伪**")
        print("     ⟹ 情形 II 的硬度完全开放 ⭐⭐⭐")
    else:
        print("⟹ 未找到 ⟹ c6′ 在开放区域仍成立（与之前 12/12 一致）")


if __name__ == "__main__":
    main()
