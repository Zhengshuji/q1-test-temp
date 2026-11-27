r"""
c58_krylov_d34.py -- 把 Krylov 判据验证扩展到 d=3, d=4

   判据（ρ=d 时）：(5b) ⟺ dim Krylov(Λᵀ,φ) = q
   其中 M=A0 (q×d) 列满秩，φ = Mᵀ 的左零向量，Λ M = F
"""
import os, io, contextlib, random, itertools, time
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]

_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    _src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(_src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]

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

def cond_5b(A0,A1,maxm=800):
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

def krylov_dim(Lam, phi, q):
    u=phi[:]; basis=[]
    for _ in range(q+1):
        if not any(x!=0 for x in u): break
        if rk(basis+[u[:]])>len(basis): basis.append(u[:])
        else: break
        u=[sum(Lam[i][j]*u[i] for i in range(q)) for j in range(q)]
    return len(basis)

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

def test_d(n_target, n_inst, NP, seed):
    rng=random.Random(seed)
    ok=0; bad=0; tot=0
    t0=time.time()
    while (ok+bad)<n_inst and time.time()-t0<300:
        # 直接构造随机 (M,F) 并随机取一个 Λ（不依赖 LTI 实例）
        q=n_target+1; d=n_target
        M=[[Fr(rng.randint(-1,1)) for _ in range(d)] for _ in range(q)]
        if rk(M)!=d: continue
        F=[[Fr(rng.randint(-1,1)) for _ in range(d)] for _ in range(q)]
        Mt=[[M[i][j] for i in range(q)] for j in range(d)]
        ns=nullspace(Mt)
        if not ns: continue
        phi=ns[0]
        Lam=solve_lambda(M,F,q,d)
        if Lam is None: continue
        g=cond_5b(M,F)
        kd=krylov_dim(Lam,phi,q)
        agree=((kd==q)==g)
        if agree: ok+=1
        else: bad+=1
        tot+=1
        print("   d=%d #%d: (5b)=%-5s Krylov=%d/%d  %s" %
              (d, tot, str(g), kd, q, "✓" if agree else "**✗**"))
    return ok,bad


def main():
    print("=== Krylov 判据：扩展到 d=3, d=4（随机 (M,F)，ρ=d 层）===\n")
    for d in (2,3,4):
        print("--- d = %d (q=%d) ---" % (d,d+1))
        ok,bad = test_d(d, 8, 300, 31337+d)
        print("   → 一致 %d ；不一致 %d\n" % (ok,bad))


if __name__=="__main__":
    main()
