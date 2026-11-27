r"""
c66_A10_two_forms.py -- A10 的两个形式是否等价？

形式 I（独立性）：  (5b) ⟺ Fᵀu_0..Fᵀu_{d-1} 线性无关       [已实证 94 实例]
形式 II（特征向量）：(5b) ⟺ Λ 无特征向量 z 满足 <z,φ>=0     [7.27.1 直接推导]

【本脚本】对同一实例分别算两个形式，看是否都等于 (5b)
   注意：形式 II 需要解特征值（可能出 ℚ）⟹ 只在能算出时比较
"""
import os, io, contextlib, random, itertools
from fractions import Fraction as Fr
from math import gcd as ig

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

def charpoly(M):
    n=len(M)
    I=[[Fr(1) if i==j else Fr(0) for j in range(n)] for i in range(n)]
    cs=[]; Acur=[r[:] for r in I]
    for k in range(1,n+1):
        Mk=mm(M,Acur)
        c=-sum(Mk[i][i] for i in range(n))/k
        cs.append(c)
        Acur=[[Mk[i][j]+(c if i==j else Fr(0)) for j in range(n)] for i in range(n)]
    return [Fr(1)]+[cs[-1-i] for i in range(len(cs))]

def rat_roots(coef):
    c=Pt(coef)
    if len(c)<=1: return []
    if c[0]==0: return [Fr(0)]
    L=1
    for x in c:
        dd=x.denominator; L=L*dd//ig(L,dd)
    ints=[int(x*L) for x in c]
    g=0
    for x in ints: g=ig(g,abs(x))
    if g: ints=[x//g for x in ints]
    out=[]
    def divs(m):
        m=abs(m); o=[]
        for i in range(1,int(m**0.5)+1):
            if m%i==0:
                o.append(i)
                if i!=m//i: o.append(m//i)
        return o
    for pn in divs(ints[0])[:40]:
        for qd in divs(abs(ints[-1]))[:20]:
            for s in (1,-1):
                x=Fr(s*pn,qd); v=Fr(0)
                for cc in reversed(ints): v=v*x+cc
                if v==0: out.append(x)
    return sorted(set(out))

def form_I(M,F,q,d):
    Mt=[[M[i][j] for i in range(q)] for j in range(d)]
    ns=nullspace_rows(Mt)
    if not ns: return None
    phi=ns[0]
    Lam=solve_lambda(M,F,q,d)
    if Lam is None: return None
    Ft=[[F[i][j] for i in range(q)] for j in range(d)]
    us=[phi[:]]; u=phi[:]
    for _ in range(d-1):
        u=[sum(Lam[i][j]*u[i] for i in range(q)) for j in range(q)]
        us.append(u[:])
    vecs=[[sum(Ft[j][i]*us[k][i] for i in range(q)) for j in range(d)] for k in range(d)]
    return rk(vecs)==len(vecs)

def form_II(M,F,q,d):
    """Λ 无特征向量 z 满足 <z,φ>=0 ？  只在能解出有理特征值时判定"""
    Mt=[[M[i][j] for i in range(q)] for j in range(d)]
    ns=nullspace_rows(Mt)
    if not ns: return None
    phi=ns[0]
    Lam=solve_lambda(M,F,q,d)
    if Lam is None: return None
    roots=rat_roots(charpoly(Lam))
    bad=False
    for lam in roots:
        K=[[Lam[i][j]-(lam if i==j else Fr(0)) for j in range(q)] for i in range(q)]
        kern=nullspace_rows(K)
        if not kern: continue
        if len(kern)>=2:
            bad=True; break          # ker 维数 ≥2 ⟹ {z: <z,φ>=0} 在 ker 中非零 ✓
        z=kern[0]
        if sum(z[k]*phi[k] for k in range(q))==0:
            bad=True; break          # ker 就 1 维且 ⊥φ
    return (not bad)

def main():
    print("=== A10 的两种形式是否都等于 (5b)？ ===\n")
    print("%-8s %3s %8s %10s %10s" % ("#","d","(5b)","形式I(无关)","形式II(特征向量)"))
    print("-"*46)
    agreeI=agreeII=tot=0; diff=0
    rng=random.Random(31415)
    for trial in range(400):
        d=rng.choice([2,3]); q=d+1
        M=[[Fr(rng.randint(-1,1)) for _ in range(d)] for _ in range(q)]
        if rk(M)!=d: continue
        F=[[Fr(rng.randint(-1,1)) for _ in range(d)] for _ in range(q)]
        g=cond_5b(M,F)
        f1=form_I(M,F,q,d)
        f2=form_II(M,F,q,d)
        if f1 is not None:
            if f1==g: agreeI+=1
        tot+=1
        if f2 is not None:
            if f2==g: agreeII+=1
        if f1 is not None and f2 is not None and f1!=f2:
            diff+=1
            print("%-8d %3d %8s %10s %10s  **两形式不同**" % (trial,d,str(g),str(f1),str(f2)))
        if tot>=50: break
    print()
    print("共 %d ；形式I 与 (5b) 一致 %d ；形式II 与 (5b) 一致 %d" % (tot,agreeI,agreeII))
    print("两形式不同的实例：%d" % diff)
    if diff>0:
        print("\n⚠️ 两形式**不等价** ⟹ A10 的正确形式需重新确认")
    else:
        print("\n⟹ 在所测实例上两形式一致")


if __name__=="__main__":
    main()
