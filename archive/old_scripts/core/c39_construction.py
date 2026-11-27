r"""
c39_construction.py -- ⭐⭐⭐⭐⭐ 验证 YES 侧的**显式构造**

【构造】
  取 α_i = e_i（i=1..d）—— 可行因 L ↦ L·N 满射到 ℝ^{d×d}
  ⟹ A0 = I_d  ⟹ ker A0 = 0 ⟹ **(5a) 自动成立**
  A1 = A' + B，B 的行 = ℓ_i·R，其中 ℓ_i 解 ℓ_i·N = e_i
  ⟹ **M = A0⁻¹A1 = A1**，故
     **(5b) ⟺ rank(λI − A1) = d ∀λ ⟺ charpoly(A1) 无有理根**

  连同固定行 (α0,γ0)：A0 有 d+1 行，rank = d ✓，ker = 0 ✓
  故只需找 ℓ_i 使 charpoly 无有理根

【本脚本】对 obs=d 的实例：
   随机取 ℓ_i（特解 + 核自由组合），测"charpoly 无有理根"的比例
   并对命中的构造**精确验证** (5a)∧(5b)
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

def has_rat_root(coef):
    c=[x for x in coef]
    while len(c)>1 and c[-1]==0: c.pop()
    if len(c)<=2: return True
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
    for pnum in divs(ints[0])[:60]:
        for qden in divs(abs(ints[-1]))[:24]:
            for s in (1,-1):
                x=Fr(s*pnum,qden); v=Fr(0)
                for cc in reversed(ints): v=v*x+cc
                if v==0: return True
    return False

def cond_5a(A0,A1):
    K=ker_basis(A0)
    if not K or not K[0]: return True
    if len(A1[0])!=len(K): return False
    return rk(mm(A1,K))==0

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

def row_space_basis(M):
    m_rows=len(M); ncols=len(M[0])
    A=[[Fr(x) for x in row] for row in M]
    piv=[]; r=0
    for c in range(ncols):
        p=None
        for i in range(r,m_rows):
            if A[i][c]!=0: p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for i in range(m_rows):
            if i!=r and A[i][c]!=0:
                f=A[i][c]
                A[i]=[A[i][j]-f*A[r][j] for j in range(ncols)]
        piv.append(r); r+=1
        if r==m_rows: break
    return [A[i][:] for i in piv]

def invariant_closure(M, Ap, d):
    basis=row_space_basis(M); cur=[r[:] for r in basis]
    while len(basis)<d:
        cur=mm(cur,Ap)
        if rk(basis+[r[:] for r in cur])==len(basis): break
        basis=basis+[r[:] for r in cur]
    return row_space_basis(basis)

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
                f=A2[i][c]
                A2[i]=[A2[i][j]-f*A2[c][j] for j in range(2*n)]
    return [row[n:] for row in A2]

def solve_full(Mat, rhs):
    """解 x·Mat = rhs；返回 (x0, [核基]) 或 None"""
    n=len(Mat); m=len(Mat[0])          # n×m 矩阵，x 是长度 n
    # 行方程：sum_i x_i Mat[i][j] = rhs[j]
    A2=[[Fr(Mat[i][j]) for i in range(n)]+[Fr(rhs[j])] for j in range(m)]
    rows=len(A2); cols=n+1
    piv=[]; r=0
    for c in range(n):
        p=None
        for i in range(r,rows):
            if A2[i][c]!=0: p=i; break
        if p is None: continue
        A2[r],A2[p]=A2[p],A2[r]
        pv=A2[r][c]; A2[r]=[x/pv for x in A2[r]]
        for i in range(rows):
            if i!=r and A2[i][c]!=0:
                f=A2[i][c]
                A2[i]=[A2[i][j]-f*A2[r][j] for j in range(cols)]
        piv.append(c); r+=1
        if r==rows: break
    # 相容性
    for i in range(r,rows):
        if all(A2[i][j]==0 for j in range(n)) and A2[i][n]!=0:
            return None
    x0=[Fr(0)]*n
    for i,c in enumerate(piv):
        x0[c]=A2[i][n]
    free=[c for c in range(n) if c not in piv]
    kern=[]
    for f in free:
        v=[Fr(0)]*n; v[f]=Fr(1)
        for i,c in enumerate(piv):
            v[c]=-A2[i][f]
        kern.append(v)
    return x0, kern


def main():
    print("=== 验证 YES 侧的显式构造：(A0=I ⟹ 5a 自动；找 charpoly 无有理根) ===\n")
    hdr = "%-12s %3s %5s %5s %8s %8s %7s %6s" % ("实例","d","obs","e","无根率","(5a)","(5b)","构造")
    print(hdr); print("-"*len(hdr))
    for (n,seed,trials) in [(4,70052,[0,2,3]),(5,70065,[0,1])]:
        rng=random.Random(seed)
        for trial in range(300000):
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
            if trial not in trials: continue
            AN=mm(A,N)
            Nt=[[N[i][j] for i in range(n)] for j in range(d)]
            iNtN=minv(mm(Nt,N))
            if iNtN is None: continue
            Ap=mm(mm(iNtN,Nt),AN)
            NAp=mm(N,Ap)
            R=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
            V=invariant_closure(R, Ap, d)
            e=len(row_space_basis(R))
            if len(V)!=d:
                print("%-12s %3d %5d %5d %8s %8s %7s %6s" %
                      ("n=%d t=%d"%(n,trial), d, len(V), e, "-","-","-","obs<d,跳过"))
                continue
            # 构造
            sols=[]
            okc=False
            ns=0; ngood=0
            rng2=random.Random(5150+97*trial+n)
            for _try in range(60):
                Lrows=[]
                good=True
                for i in range(d):
                    ee=[Fr(1) if k==i else Fr(0) for k in range(d)]
                    res=solve_full(N, ee)
                    if res is None: good=False; break
                    x0,kern=res
                    co=[rng2.randint(-2,2) for _ in kern]
                    x=[x0[k]+sum(co[t]*kern[t][k] for t in range(len(kern))) for k in range(n)]
                    Lrows.append(x)
                if not good: continue
                # A0 = I ; A1 = L·AN (因为 A0·A' + L·R = L·N·A' + L·R = L·(N·A'+R) = L·AN)
                A1=[ [sum(Lrows[i][t]*AN[t][j] for t in range(n)) for j in range(d)] for i in range(d)]
                # 检查 A0 = L·N 是否为 I
                LN=[[sum(Lrows[i][t]*N[t][j] for t in range(n)) for j in range(d)] for i in range(d)]
                Id=[[Fr(1) if i==j else Fr(0) for j in range(d)] for i in range(d)]
                if LN != Id:
                    continue          # 数值上应恒等；不等则跳过（防御）
                ns+=1
                cp=charpoly(A1)
                if not has_rat_root(cp):
                    ngood+=1
                    if not sols: sols=(Lrows,A1)
            # 对命中的构造做精确验证
            resa=resb=None
            if sols:
                Lrows,A1=sols
                a0=mm(L0,N)[0]; g0=mm(mm(L0,A),N)[0]
                A0=[a0[:]]+[[Fr(1) if k==i else Fr(0) for k in range(d)] for i in range(d)]
                Afull=[g0[:]]+[r[:] for r in A1]
                resa=cond_5a(A0,Afull); resb=cond_5b(A0,Afull)
            rate=100.0*ngood/ns if ns else -1
            print("%-12s %3d %5d %5d %7.0f%% %8s %7s %6s" %
                  ("n=%d t=%d"%(n,trial), d, len(V), e, rate,
                   str(resa) if resa is not None else "-",
                   str(resb) if resb is not None else "-",
                   "✓" if (resa and resb) else ("—" if resa is None else "✗")))
    print()
    print("【判读】若'无根率'高且命中构造的 (5a)∧(5b) 都 True ⟹ **构造法成立** ✓")


if __name__=="__main__":
    main()
