r"""
c98_construct_counterexample.py -- 构造 ρ<obs 的反例（用户的建议）

构造（ρ=1）：
   M = u·α₀ᵀ  (q×d, rank 1)
   F = u'·α₀ᵀ (q×d, rank 1)
  (5a): rowM = rowF = span(α₀)  ⟹ 自动
  (5b): rank(λM−F) = 1 ∀λ ⟺ (λI−Λ)u ≠ 0 ∀λ ⟺ u 不是 Λ 的特征向量
  ⟹ 只需 u ∦ u'（即 Λu = u' 时 u 非特征向量）

要求：α₀A' + β₀ = w·α₀ 对某 β₀∈W₀（即 α₀A' ∈ span(α₀)+W₀）
"""
import os, io, contextlib, random, itertools, sys, time
from fractions import Fraction as Fr
_HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,_HERE)
from exact_gcd import cond_5b

_ns={}
with open(os.path.join(_HERE,"exact_count_thm7.py"),encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(),"lib","exec"),_ns)
rk=_ns["rk"]; mm=_ns["mm"]; ker_basis=_ns["ker_basis"]

def rowspace_basis(M):
    if not M or not M[0]: return []
    mr=len(M); nc=len(M[0])
    A=[[Fr(x) for x in row] for row in M]
    piv=[]; r=0
    for c in range(nc):
        p=None
        for i in range(r,mr):
            if A[i][c]!=0: p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for i in range(mr):
            if i!=r and A[i][c]!=0:
                f=A[i][c]; A[i]=[A[i][j]-f*A[r][j] for j in range(nc)]
        piv.append(r); r+=1
        if r==mr: break
    return [A[i][:] for i in piv]

def invcl(M0,Ap,d):
    b=rowspace_basis(M0); cur=[r[:] for r in b]
    while len(b)<d and b:
        cur=mm(cur,Ap)
        if rk(b+[r[:] for r in cur])==len(b): break
        b=b+[r[:] for r in cur]
    return rowspace_basis(b)

def minv(M):
    n=len(M)
    A2=[[Fr(M[i][j]) for j in range(n)]+[Fr(1) if i==j else Fr(0) for j in range(n)] for i in range(n)]
    for c in range(n):
        p=None
        for i in range(c,n):
            if A2[i][c]!=0: p=i; break
        if p is None: return None
        A2[c],A2[p]=A2[p],A2[c]
        pv=A2[c][c]; A2[c]=[x/pv for x in A2[c]]
        for i in range(n):
            if i!=c and A2[i][c]!=0:
                f=A2[i][c]; A2[i]=[A2[i][j]-f*A2[c][j] for j in range(2*n)]
    return [row[n:] for row in A2]

def solve_row(Mat, rhs):
    """解 Mat·x = rhs（Mat: 列表的列表，行=方程）"""
    n=len(Mat[0]); m=len(Mat)
    A2=[[Fr(Mat[i][j]) for j in range(n)]+[Fr(rhs[i])] for i in range(m)]
    piv=[]; r=0
    for c in range(n):
        p=None
        for i in range(r,m):
            if A2[i][c]!=0: p=i; break
        if p is None: continue
        A2[r],A2[p]=A2[p],A2[r]
        pv=A2[r][c]; A2[r]=[x/pv for x in A2[r]]
        for i in range(m):
            if i!=r and A2[i][c]!=0:
                f=A2[i][c]; A2[i]=[A2[i][j]-f*A2[r][j] for j in range(n+1)]
        piv.append(c); r+=1
        if r==m: break
    for i in range(r,m):
        if all(A2[i][j]==0 for j in range(n)) and A2[i][n]!=0: return None
    x=[Fr(0)]*n
    for i,c in enumerate(piv): x[c]=A2[i][n]
    return x

def cond_5a(A0,A1):
    K=ker_basis(A0)
    if not K or not K[0]: return True
    if len(A1[0])!=len(K): return False
    return rk(mm(A1,K))==0

def main():
    print("=== 构造 ρ=1 < obs 的反例 ===\n")
    found=0; tried=0; cond_ok=0
    t0=__import__("time").time()
    t=0
    while time.time()-t0<400:
        t+=1
        n=random.Random(830000+t).choice([4,5,6])
        rng=random.Random(730000+t)
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A)
        if rk(CA)!=1: continue
        N=ker_basis(Cc+CA)
        if not N or not N[0]: continue
        d=len(N[0])
        if d<2: continue
        AN=mm(A,N)
        Nt=[[N[i][j] for i in range(n)] for j in range(d)]
        iNtN=minv(mm(Nt,N))
        if iNtN is None: continue
        Ap=mm(mm(iNtN,Nt),AN)
        NAp=mm(N,Ap)
        R0=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
        W0=rowspace_basis(R0)                     # W₀ = row(R0) ⊆ ℝ^d
        Vb=invcl(R0,Ap,d); obs=len(Vb)
        if obs<2: continue                        # 需要 obs ≥ 2
        # L0：要求 α₀ = L0·N ≠ 0
        L0=None
        for _x in range(30):
            cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(cand)!=1: continue
            if rk(cand+Cc)!=2: continue
            pv=[sum(cand[0][i]*N[i][j] for i in range(n)) for j in range(d)]
            if all(x==0 for x in pv): continue
            L0=cand; break
        if L0 is None: continue
        if rk(L0+Cc)!=2: continue
        a0=mm(L0,N)[0]                            # α₀ = L0·N ∈ ℝ^d
        if all(x==0 for x in a0): continue
        tried+=1
        # 条件：α₀A' ∈ span(α₀) + W₀ ？
        g0=[sum(a0[i]*Ap[i][j] for i in range(d)) for j in range(d)]   # α₀A'
        span=[a0[:]]+[r[:] for r in W0]
        if rk(span+[g0])!=rk(span):
            continue
        cond_ok+=1
        # 解：g0 = w·α₀ − β₀，β₀∈W₀ ⟹ g0 + β₀ = w·α₀
        # 用线性系统：找 w 与 β₀ 系数 s：g0 + Σs_i W0_i − w·α₀ = 0
        # 未知量：w, s_1..s_{|W0|}
        k=len(W0)
        Mat=[]; rhs=[]
        for j in range(d):
            Mat.append([a0[j]]+[W0[i][j] for i in range(k)])
            rhs.append(-g0[j])
        sol=solve_row(Mat,rhs)
        if sol is None: continue
        w=sol[0]
        if w==1: continue                         # 需 w≠1（否则 F=M）
        # 构造 q=d+1 行：M_i = u_i·α₀, F_i = u'_i·α₀
        # 取 u = (1,0,...,0)（首行固定），u' = (w, 1, 0, ..., 0)
        q=d+1
        u=[Fr(0)]*q; u[0]=Fr(1)
        up=[Fr(0)]*q; up[0]=w
        if q>1: up[1]=Fr(1)
        A0=[[u[i]*a0[j] for j in range(d)] for i in range(q)]
        A1=[[up[i]*a0[j] for j in range(d)] for i in range(q)]
        rho=rk(A0)
        ok5a=cond_5a(A0,A1)
        ok5b=cond_5b(A0,A1)
        if ok5a and ok5b:
            found+=1
            tag = "**反例!**" if rho<obs else "(ρ=obs)"
            print("[t=%d] n=%d d=%d obs=%d ρ=%d w=%s | (5a)=%s (5b)=%s %s" %
                  (t,n,d,obs,rho,str(w),ok5a,ok5b,tag))
            if rho<obs:
                print("    M =", [[str(x) for x in r] for r in A0])
                print("    F =", [[str(x) for x in r] for r in A1])
                print("    α₀ =", [str(x) for x in a0])
    print()
    print("检查 %d 个实例；满足 α₀A'∈span(α₀)+W₀ 的 %d 个；**构造出解 %d 个**" %
          (tried,cond_ok,found))
    if found>0:
        print("\n*** 构造成功！请检查上面是否出现 ρ<obs ***")
    else:
        print("\n（本轮未构造出 —— 条件可能过强或 q 太小）")


if __name__=="__main__":
    main()
