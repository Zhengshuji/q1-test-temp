r"""
c84_REPRO.py -- 复现 c82 的失败实例并 dump 数据，用 sympy 裁判
"""
import os, io, contextlib, random, itertools
from fractions import Fraction as Fr
import sympy as sp

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
def const_nz(g): return g is not None and len(Pt(g))==1 and any(x!=0 for x in g)
def gcd_all(ps):
    if not ps: return None
    g=ps[0]
    for x in ps[1:]:
        g=Pg(g,x)
        if len(g)==1: break
    return g

def cond_5b(M,F,maxm=400):
    q=len(M); d=len(M[0]); rho=rk(M)
    if rho==0: return True
    P=[[[-F[i][j], M[i][j]] for j in range(d)] for i in range(q)]
    ps=[]; cnt=0
    for rows in itertools.combinations(range(q),rho):
        for cols in itertools.combinations(range(d),rho):
            dd=Pdet([[P[i][j] for j in cols] for i in rows],rho)
            if dd!=[Fr(0)]: ps.append(dd)
            cnt+=1
            if cnt>maxm: break
        if cnt>maxm: break
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

def pbh_form(M,F,q,d,Lam):
    Mt=[[M[i][j] for i in range(q)] for j in range(d)]
    Ns=nullspace_rows(Mt)
    if not Ns: return None
    m=len(Ns)
    P=[]
    for i in range(q):
        row=[]
        for j in range(q):
            a=Lam[j][i]
            if i==j: row.append([a, Fr(-1)])
            else:    row.append([a])
        for t in range(m):
            row.append([Ns[t][i]])
        P.append(row)
    ps=[]
    for cols in itertools.combinations(range(q+m),q):
        dd=Pdet([[P[i][j] for j in cols] for i in range(q)],q)
        if dd!=[Fr(0)]: ps.append(dd)
    return const_nz(gcd_all(ps))

def sympy_5b(M,F):
    lam=sp.symbols("l")
    q=len(M); d=len(M[0])
    P=sp.zeros(q,d)
    for i in range(q):
        for j in range(d):
            P[i,j]=sp.Rational(M[i][j].numerator,M[i][j].denominator)*lam \
                   - sp.Rational(F[i][j].numerator,F[i][j].denominator)
    return P.rank()==rk(M)

def sympy_pbh(M,F,Lam):
    lam=sp.symbols("l")
    q=len(M); d=len(M[0])
    Mt=[[M[i][j] for i in range(q)] for j in range(d)]
    Ns=nullspace_rows(Mt)
    m=len(Ns); cols=q+m
    Ms=sp.zeros(q,cols)
    for i in range(q):
        for j in range(q):
            a=sp.Rational(Lam[j][i].numerator,Lam[j][i].denominator)
            Ms[i,j]=a-(lam if i==j else 0)
        for t in range(m):
            Ms[i,q+t]=sp.Rational(Ns[t][i].numerator,Ns[t][i].denominator)
    ps=[]
    for cs in itertools.combinations(range(cols),q):
        m2=sp.expand(Ms[:,list(cs)].det())
        if m2!=0: ps.append(m2)
    if not ps: return False
    g=sp.gcd_list(ps)
    return bool(g.is_number)

def main():
    rng=random.Random(555999)
    tot=0; shown=0
    for trial in range(3000):
        d=rng.choice([2,3]); q=d+1
        rr=rng.choice([1,2])
        if rr>=d: continue
        M=[[Fr(0)]*d for _ in range(q)]
        for i in range(rr):
            M[i]=[Fr(rng.randint(-1,1)) for _ in range(d)]
        for i in range(rr,q):
            a,b=Fr(rng.randint(-1,1)),Fr(rng.randint(-1,1))
            M[i]=[a*M[0][j]+b*M[1][j] for j in range(d)] if rr==2 else [a*M[0][j] for j in range(d)]
        rho=rk(M)
        if rho==0 or rho>=d: continue
        Lam=[[Fr(rng.randint(-1,1)) for _ in range(q)] for _ in range(q)]
        F=mm(Lam,M)
        g=cond_5b(M,F)
        p=pbh_form(M,F,q,d,Lam)
        if p is None: continue
        tot+=1
        if g!=p:
            shown+=1
            print("="*60)
            print("不一致实例 trial=%d  d=%d ρ=%d q=%d" % (trial,d,rho,q))
            print("M =", [[str(x) for x in r] for r in M])
            print("F =", [[str(x) for x in r] for r in F])
            print("Λ =", [[str(x) for x in r] for r in Lam])
            print(" 我的 cond_5b =", g)
            print(" 我的 pbh_form =", p)
            print(" sympy 判 (5b) =", sympy_5b(M,F))
            print(" sympy 判 PBH  =", sympy_pbh(M,F,Lam))
        if tot>=40: break

if __name__=="__main__":
    main()
