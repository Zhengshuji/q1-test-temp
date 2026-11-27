# -*- coding: utf-8 -*-
"""
c6_k_ge1b.py -- ⭐⭐⭐ **构造**非退化平行 + k≥1 实例，并检验 (5a)∧(5b)

【构造（保证成功）】
  n=6, p=1, 取 C = e₁ᵀ
  令 A 的前三行为：  A[0]=e₂ᵀ, A[1]=e₃ᵀ, A[2]=λ₀·e₃ᵀ,  其余三行随机
  ⟹ C A = e₂ᵀ, C A² = e₃ᵀ, C A³ = λ₀ e₃ᵀ  ⟹ **CA² 是左特征向量** ✓
  ⟹ K = ker C ∩ ker(CA) = span{e₃,e₄,e₅,e₆}
  ⟹ CA²|_K = e₃ᵀ|_K ≠ 0  ⟹ **非 A-不变** ✓
  ⟹ CA³|_K = λ₀·CA²|_K ∥ CA²|_K ✓

  L0 := [CA² + CA ; CA²] = [e₃ᵀ+e₂ᵀ ; e₃ᵀ]
     π(L0)  = [(1,0,0,0); (1,0,0,0)]        ⟹ 平行、非退化 ✓
     π(L0A) = [(λ₀+1)(1,0,0,0); λ₀(1,0,0,0)]  ⟹ 仍成比例 ✓
     c = (1,1), d = (λ₀+1, λ₀) ∦ c  ⟹ **L0 本身不满足 (A)** ⟹ k ≥ 1 ✓
"""
import os, io, contextlib, random, itertools
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]

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

def check_5ab(Lm, Ac, Cc, maxminors=2000):
    CAc = mm(Cc, Ac)
    LA = mm(Lm, Ac)
    base = [r[:] for r in Lm] + [r[:] for r in CAc] + [r[:] for r in Cc]
    r0 = rk(base)
    m = len(base); n = len(base[0])
    a_ok = (rk([r[:] for r in LA] + base) == r0)
    if r0 == 0: return a_ok, True
    nL = len(Lm)
    P = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append([-LA[i][j], Lm[i][j]] if i < nL else [base[i][j]])
        P.append(row)
    polys = []; cnt = 0
    for rows in itertools.combinations(range(m), r0):
        for cols in itertools.combinations(range(n), r0):
            sub = [[P[i][j] for j in cols] for i in rows]
            d = pdet(sub, r0)
            if d is not None and not all(x == 0 for x in d): polys.append(d)
            cnt += 1
            if cnt > maxminors: break
        if cnt > maxminors: break
    if not polys: return a_ok, True
    g = polys[0]
    for q in polys[1:]:
        g = pgcd(g, q)
        if len(g) == 1: break
    return a_ok, (len(g) == 1)

def obs(M, A, n):
    rows=[list(x) for x in M]; cur=[list(x) for x in M]
    for _ in range(n-1): cur=mm(cur,A); rows+=cur
    return rows


def make_instance(n, lam0, rng):
    """构造 A（前 3 行固定），C = e1^T"""
    A = [[F(0)]*n for _ in range(n)]
    A[0][1] = F(1)                  # A[0] = e2^T
    A[1][2] = F(1)                  # A[1] = e3^T
    A[2][2] = F(lam0)               # A[2] = lam0 e3^T
    for i in range(3, n):
        for j in range(n):
            A[i][j] = F(rng.randint(-1, 1))
    C = [[F(0)]*n]
    C[0][0] = F(1)                  # C = e1^T
    return A, C


def main():
    print("=== 构造的非退化平行 + k≥1 实例：(5a)∧(5b) 能否满足？ ===\n")
    print("%-6s %4s %4s %4s %6s %8s %8s %10s" %
          ("lam0","n","q0","k","r=2","L0满足5a","(5b)可能","结论"))
    print("-" * 66)
    rng = random.Random(20250401)
    tot = 0; found_yes = 0; found_no = 0
    for lam0 in [0, 1, -1, 2, -2]:
        for trial in range(40):
            n, p = 6, 1
            Ac, Cc = make_instance(n, lam0, rng)
            CA = mm(Cc, Ac)
            W = Cc + CA
            dCA = n - rk(W)
            if dCA < 2: continue
            N = ker_basis(W)
            if not N or not N[0] or len(N[0]) != dCA: continue
            ell0 = mm(CA, Ac)[0][:]      # CA²
            rvec = CA[0][:]              # CA
            L0 = [[ell0[i] + rvec[i] for i in range(n)], ell0[:]]
            if rk(L0) != 2: continue
            if rk(L0 + Cc) != 3: continue
            pv = lambda v: [sum(v[i]*N[i][j] for i in range(n)) for j in range(dCA)]
            pL = [pv(L0[0]), pv(L0[1])]
            pLA = [pv(mm([L0[0]], Ac)[0]), pv(mm([L0[1]], Ac)[0])]
            if all(all(x == 0 for x in w) for w in pL): continue
            if rk(pL + pLA) != 1: continue
            if rk(obs(L0, Ac, n) + obs(Cc, Ac, n)) != rk(obs(Cc, Ac, n)): continue
            try:
                _Lx, eta = p1(Ac, Cc, L0)
            except Exception:
                continue
            if not eta: continue
            q0 = sum(eta); k = q0 - 2
            if k < 1: continue
            tot += 1
            a0, b0 = check_5ab(L0, Ac, Cc)
            # 搜索 R
            hit = None
            for _ in range(60):
                rows = [r[:] for r in L0]
                for _i in range(k):
                    rows.append([F(rng.randint(-3,3)) for _ in range(n)])
                a_ok, b_ok = check_5ab(rows, Ac, Cc)
                if a_ok and b_ok:
                    hit = rows; break
            concl = "**YES ✓**" if hit is not None else "NO"
            if hit is not None: found_yes += 1
            else: found_no += 1
            print("%-6d %4d %4d %4d %6s %8s %8s %10s" %
                  (lam0, n, q0, k, "2", "是" if a0 else "否",
                   "✓" if b0 else "—", concl))
            if tot >= 12: break
        if tot >= 12: break
    print()
    print("构造实例数：%d   (5a)∧(5b) 找到：%d   未找到：%d" % (tot, found_yes, found_no))
    print()
    if found_yes:
        print("⟹⟹⟹ **非退化平行 + k≥1 也可为 YES** ⟹ c6′ 的证伪扩展到硬度相关范围 ⭐⭐⭐")
    else:
        print("⟹ 未找到 ⟹ c6′ 在 k≥1 范围可能仍成立 ⟹ 证伪只影响 k=0")


if __name__ == "__main__":
    main()
