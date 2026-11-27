r"""
c69_sympy_complex.py -- 用 sympy 在 ℂ 上重测 A11（修复此前"只有有理特征值"的缺陷）

A11: (5b) ⟺ Λ 无特征向量 z 满足 <z,φ>=0  （λ ∈ ℂ）

此前 c66 只用有理特征值 ⟹ 假阳性。本脚本用 sympy 精确求复特征值。
"""
import os, io, contextlib, random, itertools, sys
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
def gcd_all(ps):
    g=ps[0]
    for q in ps[1:]:
        g=Pg(g,q)
        if len(g)==1: break
    return g
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
    g=gcd_all(ps)
    return len(Pt(g))==1 and any(x!=0 for x in g)

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

def A11_sympy(M,F,q,d):
    """(5b) 的 A11 形式：Λ 无特征向量 z 满足 <z,φ>=0 ？在 ℂ 上精确判定"""
    Mt=[[M[i][j] for i in range(q)] for j in range(d)]
    ns=nullspace_rows(Mt)
    if not ns: return None
    phi=ns[0]
    Lam=solve_lambda(M,F,q,d)
    if Lam is None: return None
    t=sp.symbols("t")
    LamS=sp.Matrix([[sp.Rational(Lam[i][j].numerator, Lam[i][j].denominator) for j in range(q)] for i in range(q)])
    phiS=sp.Matrix([sp.Rational(x.numerator, x.denominator) for x in phi])
    bad=False
    for lam, mult in LamS.eigenvals().items():
        K = LamS - lam*sp.eye(q)
        nsK = K.nullspace()
        if not nsK: continue
        if len(nsK)>=2:
            bad=True; break
        z=nsK[0]
        if sp.simplify((z.T*phiS)[0])==0:
            bad=True; break
    return (not bad)

def main():
    print("=== 用 sympy 在 ℂ 上判定 A11 ===\n")
    print("%-8s %3s %8s %10s %6s" % ("#","d","(5b)","A11(ℂ)","一致"))
    print("-"*40)
    ok=0; bad=0; tot=0
    rng=random.Random(98765)
    for trial in range(400):
        d=rng.choice([2,3]); q=d+1
        M=[[Fr(rng.randint(-1,1)) for _ in range(d)] for _ in range(q)]
        if rk(M)!=d: continue
        F=[[Fr(rng.randint(-1,1)) for _ in range(d)] for _ in range(q)]
        g=cond_5b(M,F)
        a11=A11_sympy(M,F,q,d)
        if a11 is None: continue
        agree=(g==a11)
        if agree: ok+=1
        else:
            bad+=1
            print("%-8d %3d %8s %10s %6s **✗**" % (trial,d,str(g),str(a11),"✗"))
        tot+=1
        if tot>=40: break
    print()
    print("共 %d ；一致 %d ；不一致 %d" % (tot,ok,bad))
    if bad==0 and tot>0:
        print("\n⟹ **A11 在 ℂ 上成立**（sympy 精确判定）✓")
        print("   这修复了 c66 的缺陷（当时只有有理特征值）")


if __name__=="__main__":
    main()
