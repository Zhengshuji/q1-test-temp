r"""
c73_general_rho.py -- 检验推广猜想：
   (5b) ⟹ dim Fᵀ(K) = ρ，其中 K = Krylov(Λᵀ, ker Mᵀ)

若成立 ⟹ ρ ≤ obs（因 Fᵀ(K) ⊆ Ṽ，dim Ṽ = obs）⟹ 缺口①闭合
"""
import os, io, contextlib, random, itertools
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]

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
    g=ps[0]
    for q in ps[1:]:
        g=Pg(g,q)
        if len(g)==1: break
    return g
def const_nz(g):
    return g is not None and len(Pt(g))==1 and any(x!=0 for x in g)

def cond_5b(M,F):
    q=len(M); d=len(M[0]); rho=rk(M)
    if rho==0: return True
    P=[[[-F[i][j], M[i][j]] for j in range(d)] for i in range(q)]
    ps=[]
    for rows in itertools.combinations(range(q),rho):
        for cols in itertools.combinations(range(d),rho):
            dd=Pdet([[P[i][j] for j in cols] for i in rows],rho)
            if dd!=[Fr(0)]: ps.append(dd)
    if not ps: return False
    return const_nz(gcd_all(ps))

def nullspace_rows(M):
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
    """Λ 使 ΛM = F（需 (5a)；此处检测 row(F)⊆row(M)）"""
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

def krylov_closure(seed_basis, Lam, q):
    """Krylov 闭包（在 Λᵀ 下）：(Λᵀu)_j = Σ_k Λ_{kj} u_k"""
    basis=[r[:] for r in seed_basis]
    cur=[r[:] for r in seed_basis]
    while basis:
        nxt=[[sum(cur[i][k]*Lam[k][j] for k in range(q)) for j in range(q)] for i in range(len(cur))]
        if rk(basis+[r[:] for r in nxt])==len(basis): break
        basis=basis+[r[:] for r in nxt]
        cur=nxt
    return basis

def main():
    print("=== 推广猜想：(5b) ⟹ dim Fᵀ(K) = ρ ===\n")
    print("%-8s %3s %4s %4s %8s %10s" % ("#","d","ρ","q","(5b)","dimFᵀ(K)"))
    print("-"*44)
    ok=0; bad=0; tot=0; n5b=0
    rng=random.Random(54321)
    for trial in range(600):
        d=rng.choice([2,3]); q=d+1
        M=[[Fr(rng.randint(-1,1)) for _ in range(d)] for _ in range(q)]
        rho=rk(M)
        if rho==0: continue
        F=[[Fr(rng.randint(-1,1)) for _ in range(d)] for _ in range(q)]
        Lam=solve_lambda(M,F,q,d)
        if Lam is None: continue          # 需 (5a)
        g=cond_5b(M,F)
        Mt=[[M[i][j] for i in range(q)] for j in range(d)]
        Ns=nullspace_rows(Mt)
        if not Ns: continue
        K=krylov_closure(Ns,Lam,q)
        Ft=[[F[i][j] for i in range(q)] for j in range(d)]
        FK=[[sum(Ft[j][i]*u[i] for i in range(q)) for j in range(d)] for u in K]
        dimFK=rk(FK)
        tot+=1
        if g:
            n5b+=1
            if dimFK==rho: ok+=1
            else:
                bad+=1
                print("%-8d %3d %4d %4d %8s %10d **反例**" % (trial,d,rho,q,str(g),dimFK))
        else:
            if dimFK<=rho: ok+=1
            else: bad+=1
        if tot>=100: break
    print()
    print("共 %d ；其中 (5b) 成立 %d 个" % (tot,n5b))
    print("一致 %d ；反例 %d" % (ok,bad))
    if bad==0 and n5b>0:
        print("\n⟹ **猜想成立**：(5b) ⟹ dim Fᵀ(K) = ρ ⟹ ρ ≤ obs ✓")


if __name__=="__main__":
    main()
