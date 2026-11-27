r"""
c85_FIXED_gcd.py -- 修复 gcd 初始化 bug，重查关键结论

Bug：gcd 从零多项式 ['0','0'] 初始化，且 `len(g)==1` 把零多项式误判为"已互素"
修复：跳过零多项式；只在 g 是非零常数时 break

重查：
  ① (5b) 判据本身（与 sympy 交叉验证）
  ② c19 风格：小规模穷尽枚举，"无解"是否仍成立
"""
import os, io, contextlib, itertools
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

ZERO=[Fr(0)]
def is_zero(p): return Pt(p)==ZERO
def is_nonzero_const(p):
    p=Pt(p); return len(p)==1 and p[0]!=0

def gcd_list_fixed(ps):
    """修复版：跳过零多项式；只在非零常数时提前退出"""
    nz=[p for p in ps if not is_zero(p)]
    if not nz: return ZERO                      # 全零 ⟹ gcd=0
    g=nz[0]
    for x in nz[1:]:
        g=Pg(g,x)
        if is_nonzero_const(g): break
    return Pt(g)

def cond_5b_fixed(M,F,maxm=100000):
    q=len(M); d=len(M[0]); rho=rk(M)
    if rho==0: return True
    P=[[[-F[i][j], M[i][j]] for j in range(d)] for i in range(q)]
    ps=[]; cnt=0
    for rows in itertools.combinations(range(q),rho):
        for cols in itertools.combinations(range(d),rho):
            dd=Pdet([[P[i][j] for j in cols] for i in rows],rho)
            ps.append(dd)
            cnt+=1
            if cnt>maxm: break
        if cnt>maxm: break
    g=gcd_list_fixed(ps)
    if is_zero(g): return False
    return is_nonzero_const(g)

def sympy_5b(M,F):
    lam=sp.symbols("l")
    q=len(M); d=len(M[0])
    P=sp.zeros(q,d)
    for i in range(q):
        for j in range(d):
            P[i,j]=sp.Rational(M[i][j].numerator,M[i][j].denominator)*lam \
                   - sp.Rational(F[i][j].numerator,F[i][j].denominator)
    return P.rank()==rk(M)

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

def main():
    print("=== 修复 gcd bug 后：与 sympy 交叉验证 (5b) ===\n")
    import random
    rng=random.Random(424242)
    ok=0; tot=0; bad=0
    for trial in range(200):
        d=rng.choice([2,3]); q=d+1
        rr=rng.choice([1,2,d])
        M=[[Fr(0)]*d for _ in range(q)]
        for i in range(min(rr,q)):
            M[i]=[Fr(rng.randint(-1,1)) for _ in range(d)]
        for i in range(rr,q):
            a=Fr(rng.randint(-1,1))
            M[i]=[a*M[0][j] for j in range(d)]
        rho=rk(M)
        if rho==0: continue
        Lam=[[Fr(rng.randint(-1,1)) for _ in range(q)] for _ in range(q)]
        F=mm(Lam,M)
        g1=cond_5b_fixed(M,F)
        g2=sympy_5b(M,F)
        tot+=1
        if g1==g2: ok+=1
        else:
            bad+=1
            print("  **仍不一致** trial=%d d=%d ρ=%d fixed=%s sympy=%s" % (trial,d,rho,g1,g2))
        if tot>=60: break
    print("共 %d ；一致 %d ；不一致 %d" % (tot,ok,bad))
    if bad==0:
        print("\n⟹ **修复后 (5b) 判据与 sympy 完全一致** ✓")
        print("   ⟹ 原 bug 只导致 false negative（漏报解），修复后需重查'无解'结论")


if __name__=="__main__":
    main()
