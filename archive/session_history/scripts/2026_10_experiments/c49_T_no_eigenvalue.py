r"""
c49_T_no_eigenvalue.py -- 验证 (5b) 的"算子形式"：

   (5a) ⇒ Λ 在 im(A0) 上唯一确定 ⇒ T := Λ|_im(A0) 由数据决定
   (5b) ⟺ T 在基域上无特征值 ⟺ charpoly(T) 无有理根

【为什么重要】这统一解释了此前所有"charpoly 无有理根"的观察（充分性构造等）
"""
import os, io, contextlib, random, itertools
from fractions import Fraction as Fr
from math import gcd as ig

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

def cond_5b(A0,A1,maxm=300):
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

def cond_5a(A0,A1):
    K=ker_basis(A0)
    if not K or not K[0]: return True
    if len(A1[0])!=len(K): return False
    return rk(mm(A1,K))==0

def charpoly(M):
    n=len(M)
    if n==0: return [Fr(1)]
    I=[[Fr(1) if i==j else Fr(0) for j in range(n)] for i in range(n)]
    cs=[]; Acur=[r[:] for r in I]
    for k in range(1,n+1):
        Mk=mm(M,Acur)
        c=-sum(Mk[i][i] for i in range(n))/k
        cs.append(c)
        Acur=[[Mk[i][j]+(c if i==j else Fr(0)) for j in range(n)] for i in range(n)]
    return [Fr(1)]+[cs[-1-i] for i in range(len(cs))]

def has_rat_root(coef):
    c=Pt(coef)
    if len(c)<=1: return False
    if c[0]==0: return True
    L=1
    for x in c:
        dd=x.denominator; L=L*dd//ig(L,dd)
    ints=[int(x*L) for x in c]
    g=0
    for x in ints: g=ig(g,abs(x))
    if g: ints=[x//g for x in ints]
    if ints[0]==0: return True
    def divs(m):
        m=abs(m); out=[]
        for i in range(1,int(m**0.5)+1):
            if m%i==0:
                out.append(i)
                if i!=m//i: out.append(m//i)
        return out
    for pnum in divs(ints[0])[:50]:
        for qden in divs(abs(ints[-1]))[:25]:
            for s in (1,-1):
                x=Fr(s*pnum,qden); v=Fr(0)
                for cc in reversed(ints): v=v*x+cc
                if v==0: return True
    return False

def solve_col(Mat, rhs):
    """解 Mat · x = rhs（x 长度 L）"""
    rows=len(Mat); L=len(Mat[0])
    A2=[[Fr(Mat[i][j]) for j in range(L)]+[Fr(rhs[i])] for i in range(rows)]
    piv=[]; r=0
    for c in range(L):
        p=None
        for i in range(r,rows):
            if A2[i][c]!=0: p=i; break
        if p is None: continue
        A2[r],A2[p]=A2[p],A2[r]
        pv=A2[r][c]; A2[r]=[x/pv for x in A2[r]]
        for i in range(rows):
            if i!=r and A2[i][c]!=0:
                f=A2[i][c]
                A2[i]=[A2[i][j]-f*A2[r][j] for j in range(L+1)]
        piv.append(c); r+=1
        if r==rows: break
    for i in range(r,rows):
        if all(A2[i][j]==0 for j in range(L)) and A2[i][L]!=0:
            return None
    x=[Fr(0)]*L
    for i,c in enumerate(piv): x[c]=A2[i][L]
    return x

def T_matrix(A0,A1):
    """T = Λ|_im(A0)：取 im(A0) 的基 {A0 e_j}（选主元列），解 Λ(A0 v)=A1 v"""
    q=len(A0); d=len(A0[0])
    # 选 A0 的 rho 个线性无关列
    cols=[]
    for j in range(d):
        cand=[A0[i][j] for i in range(q)]
        trial_cols=cols+[j]
        M=[[A0[i][c] for c in trial_cols] for i in range(q)]
        if rk(M)==len(trial_cols): cols=trial_cols
        if len(cols)==rk(A0): break
    rho=len(cols)
    if rho==0: return None
    # im(A0) 的基 b_1..b_rho = A0 的第 cols 列
    B=[[A0[i][c] for c in cols] for i in range(q)]        # q×rho
    # 对每个基向量 b_k，求 T b_k = A1·e_{cols[k]} 在基 B 下的坐标
    T=[[Fr(0)]*rho for _ in range(rho)]
    for k,c in enumerate(cols):
        rhs=[A1[i][c] for i in range(q)]
        co=solve_col(B, rhs)          # rhs = B·co
        if co is None: return None
        for i in range(rho): T[i][k]=co[i]
    return T


def main():
    print("=== 验证：(5b) ⟺ T=Λ|_im(A0) 无有理特征值 ===\n")
    print("%-14s %4s %5s %10s %10s %6s" % ("实例","ρ","d","gcd(5b)","T 无有理根?","一致"))
    print("-"*56)
    ok=0; bad=0; tot=0
    for (n,seed) in [(4,70052),(5,70065)]:
        rng=random.Random(seed)
        got=0
        for trial in range(120000):
            if got>=8: break
            A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
            Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(Cc)!=1: continue
            CA=mm(Cc,A)
            if rk(CA)!=1: continue
            W=Cc+CA
            N=ker_basis(W)
            if not N or not N[0]: continue
            d=len(N[0])
            if d<2: continue
            L0=None
            for _x in range(40):
                cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
                if rk(cand)!=1: continue
                if rk(cand+Cc)!=2: continue
                pv=[sum(cand[0][i]*N[i][j] for i in range(n)) for j in range(len(N[0]))]
                if all(x==0 for x in pv): continue
                L0=cand; break
            if L0 is None: continue
            if rk(L0+Cc)!=2: continue
            try:
                _Lx,eta=p1(A,Cc,L0)
            except Exception:
                continue
            if not eta: continue
            AN=mm(A,N)
            Mcol=[N[i][:]+AN[i][:] for i in range(n)]
            resB=_ns.get("ker_basis")
            # rowspace basis
            def rsb(M):
                if not M or not M[0]: return []
                mr=len(M); nc=len(M[0])
                AA=[[Fr(x) for x in row] for row in M]
                piv=[]; r=0
                for c in range(nc):
                    p=None
                    for i in range(r,mr):
                        if AA[i][c]!=0: p=i; break
                    if p is None: continue
                    AA[r],AA[p]=AA[p],AA[r]
                    pv=AA[r][c]; AA[r]=[x/pv for x in AA[r]]
                    for i in range(mr):
                        if i!=r and AA[i][c]!=0:
                            f=AA[i][c]
                            AA[i]=[AA[i][j]-f*AA[r][j] for j in range(nc)]
                    piv.append(r); r+=1
                    if r==mr: break
                return [AA[i][:] for i in piv]
            resB=rsb(Mcol); mB=len(resB)
            H0=mm(L0,N); F0=mm(mm(L0,A),N)
            q=d+1; k=q-1
            rng2=random.Random(7531+97*trial+n)
            rr=[[Fr(rng2.randint(-2,2)) for _ in range(mB)] for _ in range(k)]
            A0=[H0[0][:]]; A1=[F0[0][:]]
            for z in rr:
                w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                A0.append(w[:d]); A1.append(w[d:])
            if not cond_5a(A0,A1): continue      # 只要 (5a) 成立的（T 才有定义）
            g=cond_5b(A0,A1)
            T=T_matrix(A0,A1)
            if T is None: continue
            noroot = not has_rat_root(charpoly(T))
            agree = (g == noroot)
            if agree: ok+=1
            else: bad+=1
            tot+=1
            print("%-14s %4d %5d %10s %10s %6s" %
                  ("n=%d t=%d"%(n,trial), rk(A0), d, str(g), str(noroot),
                   "✓" if agree else "✗"))
            got+=1
        print()
    print("总 %d ；一致 %d ；不一致 %d" % (tot,ok,bad))
    if bad==0 and tot>0:
        print("\n⟹ **(5b) ⟺ T 无有理特征值** 成立 ✓")
        print("   统一解释了此前所有 'charpoly 无有理根' 的观察（含充分性构造）")


if __name__=="__main__":
    main()
