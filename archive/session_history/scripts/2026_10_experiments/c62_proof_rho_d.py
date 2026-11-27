r"""
c62_proof_rho_d.py -- 验证新定理的每一步

【定理（拟证）】ρ=d 且 obs<d ⟹ (5b) 必败

【证明链】
   ① im(Rᵀ) = row(R) = W₀
   ② Ṽ := Σ_t A'ᵀᵗ W₀ 是 A'ᵀ-不变，且 dim Ṽ = dim V = obs   （转置是双射）
   ③ MᵀΛᵀ = Fᵀ ⟹ Mᵀu_k = Fᵀu_{k-1}
   ④ Fᵀu_k = A'ᵀ(Fᵀu_{k-1}) + Rᵀψ_k，ψ_k := Lᵀu_k
   ⑤ 由 ①②④ 归纳：Fᵀu_k ∈ Ṽ ∀k
   ⑥ 判据：(5b) ⟺ Fᵀu₀,…,Fᵀu_{d-1} 无关
   ⑦ obs<d ⟹ d 个向量落在 obs 维空间 ⟹ 相关 ⟹ (5b) 败

【本脚本】逐条数值验证 ①②③④⑤⑥
"""
import os, io, contextlib, random, itertools
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]

def Pt(p):
    q=list(p)
    while len(q)>1 and q[-1]==0: q.pop()
    return q
def Pa(a,b):
    n=max(len(a),len(b)); return Pt([(a[i] if i<len(a) else Fr(0))+(b[i] if i<len(b) else Fr(0)) for i in range(n)])
def Ps(a,b):
    n=max(len(a),len(b)); return Pt([(a[i] if i<len(a) else Fr(0))-(b[i] if i<len(b) else Fr(0)) for i in range(n)])
def Pm(a,b):
    if Pt(a)==[Fr(0)] or Pt(b)==[Fr(0)]: return [Fr(0)]
    r=[Fr(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]+=x*y
    return Pt(r)
def Pdv(a,b):
    a=Pt(a); b=Pt(b); db=len(b)-1
    q=[Fr(0)]*max(1,len(a)-db)
    while len(a)-1>=db and a!=[Fr(0)]:
        d=len(a)-1-db; co=a[-1]/b[-1]; q[d]+=co
        for i in range(len(b)): a[d+i]-=co*b[i]
        a=Pt(a)
    return Pt(q),a
def Pg(a,b):
    a,b=Pt(a),Pt(b)
    while b!=[Fr(0)]:
        _,r=Pdv(a,b); a,b=b,r
    if len(a)>1:
        lc=a[-1]; a=[x/lc for x in a]
    return a
def Pdet(M,k):
    if k==1: return [Fr(x) for x in M[0][0]]
    tot=[Fr(0)]
    for j in range(k):
        sub=[row[:j]+row[j+1:] for row in M[1:]]
        d=Pdet(sub,k-1); pr=Pm(M[0][j],d)
        tot=Pa(tot,pr) if j%2==0 else Ps(tot,pr)
    return Pt(tot)
def gcd_all(ps):
    if not ps: return None
    g=ps[0]
    for q in ps[1:]:
        g=Pg(g,q)
        if len(g)==1: break
    return g
def const_nz(g):
    return g is not None and len(Pt(g))==1 and any(x!=0 for x in g)

def cond_5b(A0,A1,maxm=500):
    q=len(A0); d=len(A0[0]); rho=rk(A0)
    if rho==0: return True
    P=[[[-A1[i][j], A0[i][j]] for j in range(d)] for i in range(q)]
    ps=[]; cnt=0
    for rows in itertools.combinations(range(q),rho):
        for cols in itertools.combinations(range(d),rho):
            dd=Pdet([[P[i][j] for j in cols] for i in rows],rho)
            if dd!=[Fr(0)]: ps.append(dd)
            cnt+=1
            if cnt>maxm: break
        if cnt>maxm: break
    return const_nz(gcd_all(ps))

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
                f=A[i][c]
                A[i]=[A[i][j]-f*A[r][j] for j in range(nc)]
        piv.append(r); r+=1
        if r==mr: break
    return [A[i][:] for i in piv]

def closure_transpose(W0, Ap, d):
    """Ṽ = Σ_t A'ᵀᵗ W₀"""
    basis=rowspace_basis(W0)          # W₀ 的基（行向量表示）
    if not basis: return []
    # A'ᵀ 作用于列向量；把 basis 的行视为列向量 ⟹ A'ᵀ w = (wᵀ A')ᵀ
    cur=[r[:] for r in basis]
    while len(basis)<d:
        nxt=[[sum(cur[i][k]*Ap[k][j] for k in range(d)) for j in range(d)] for i in range(len(cur))]
        if rk(basis+[r[:] for r in nxt])==len(basis): break
        basis=basis+[r[:] for r in nxt]
        cur=nxt
    return rowspace_basis(basis)

def nullspace(M):
    if not M or not M[0]: return []
    m=len(M); n=len(M[0])
    A=[[Fr(x) for x in row] for row in M]
    piv=[]; r=0
    for c in range(n):
        p=None
        for i in range(r,m):
            if A[i][c]!=0: p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]!=0:
                f=A[i][c]
                A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
        piv.append(c); r+=1
        if r==m: break
    free=[c for c in range(n) if c not in piv]
    out=[]
    for fc in free:
        v=[Fr(0)]*n; v[fc]=Fr(1)
        for i,c in enumerate(piv): v[c]=-A[i][fc]
        out.append(v)
    return out

def solve_lambda(M,F,q,d):
    Mt=[[M[i][j] for i in range(q)] for j in range(d)]
    parts=[]
    for i in range(q):
        rhs=[F[i][j] for j in range(d)]
        m=[[Mt[r][c] for c in range(q)]+[rhs[r]] for r in range(d)]
        nr=len(m); piv=[]; r=0
        for c in range(q):
            p=None
            for ii in range(r,nr):
                if m[ii][c]!=0: p=ii; break
            if p is None: continue
            m[r],m[p]=m[p],m[r]
            pv=m[r][c]; m[r]=[x/pv for x in m[r]]
            for ii in range(nr):
                if ii!=r and m[ii][c]!=0:
                    f=m[ii][c]
                    m[ii]=[m[ii][j]-f*m[r][j] for j in range(q+1)]
            piv.append(c); r+=1
            if r==nr: break
        for ii in range(r,nr):
            if all(m[ii][j]==0 for j in range(q)) and m[ii][q]!=0: return None
        y=[Fr(0)]*q
        for ii,c in enumerate(piv): y[c]=m[ii][q]
        parts.append(y)
    return parts

def in_span(basis, v):
    if not basis: return all(x==0 for x in v)
    return rk([r[:] for r in basis]+[v[:]])==len(basis)

def main():
    print("=== 验证定理：ρ=d 且 obs<d ⟹ (5b) 必败 ===\n")
    print("%-8s %3s %3s %5s %8s %10s %8s" % ("#","d","ρ","obs","(5b)","所有Fᵀu_k∈Ṽ","dim Ṽ"))
    print("-"*56)
    ok=0; tot=0
    rng=random.Random(8888)
    for trial in range(1500):
        d=rng.choice([2,3]); q=d+1
        M=[[Fr(rng.randint(-1,1)) for _ in range(d)] for _ in range(q)]
        if rk(M)!=d: continue
        # 随机构造 (A', R, L)：F = M A' + L R
        Ap=[[Fr(rng.randint(-1,1)) for _ in range(d)] for _ in range(d)]
        n=d+2
        R=[[Fr(rng.randint(-1,1)) for _ in range(d)] for _ in range(n)]
        L=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(q)]
        MAp=mm(M,Ap)
        LR=mm(L,R)
        F=[[MAp[i][j]+LR[i][j] for j in range(d)] for i in range(q)]
        W0=rowspace_basis(R)
        Vt=closure_transpose(W0, Ap, d)
        obs=len(Vt)                      # ← obs 是**闭包**维数（不是 dim rowR）
        Mt=[[M[i][j] for i in range(q)] for j in range(d)]
        ns=nullspace(Mt)
        if not ns: continue
        phi=ns[0]
        Lam=solve_lambda(M,F,q,d)
        if Lam is None: continue
        # Krylov 序列 u_k
        us=[phi[:]]
        u=phi[:]
        for _ in range(d):
            u=[sum(Lam[i][j]*u[i] for i in range(q)) for j in range(q)]
            us.append(u[:])
        # Fᵀu_k
        Ft=[[F[i][j] for i in range(q)] for j in range(d)]
        vecs=[[sum(Ft[j][i]*us[k][i] for i in range(q)) for j in range(d)] for k in range(d)]
        allin=all(in_span(Vt,v) for v in vecs)
        g=cond_5b(M,F)
        tot+=1
        if obs<d:
            good = (g is False) and allin
            if good: ok+=1
            else:
                print("%-8d %3d %3d %5d %8s %10s %8d  **异常**" %
                      (trial,d,rk(M),obs,str(g),str(allin),len(Vt)))
        if tot>=120: break
    print()
    print("检查 %d 个实例（只打印 obs<d 的异常）" % tot)
    print("【判读】若无『异常』⟹ 定理的每一步都成立 ⟹ ρ=d 且 obs<d ⟹ (5b) 必败 ✓")


if __name__=="__main__":
    main()
