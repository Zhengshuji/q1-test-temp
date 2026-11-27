r"""
c38_reduction_check.py -- 验证"充分性化归到 obs=d 情形"

【归约】
   若 α0 ∈ V（V = 含 rowR 的最小 A'-不变子空间，dim V = obs）：
   把问题**限制到 V** 上：
     · V ≅ ℝ^obs，A'_V := A'|_V
     · rowR ⊆ V，故 β_i 可取在 V 内
     · **obs' = dim V = d'**（因为 V 是全部闭包）⟹ 归约后是"obs=d"的满情形
   ⟹ 充分性 ⟺ "obs=d ⇒ YES"

【本脚本】对每个 α0∈V 的实例：
   (a) 构造 V 的基，算 A'_V 与 rowR 在 V 坐标下的表示
   (b) 确认 obs' = d'
   (c) 在 V 上做 (5a)∧(5b) 采样，看成功率（应与原问题相当）
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

def solve_in_basis(basis, v):
    """v 在 basis（行向量组）下的坐标；假定 v ∈ span(basis)"""
    k=len(basis)
    # 解 x·basis = v
    Bt=[[basis[i][j] for i in range(k)] for j in range(len(v))]
    n=len(Bt); m=len(Bt[0])
    A2=[[Fr(Bt[i][j]) for j in range(m)]+[Fr(v[i])] for i in range(n)]
    piv=[]; r=0
    for c in range(m):
        p=None
        for i in range(r,n):
            if A2[i][c]!=0: p=i; break
        if p is None: continue
        A2[r],A2[p]=A2[p],A2[r]
        pv=A2[r][c]; A2[r]=[x/pv for x in A2[r]]
        for i in range(n):
            if i!=r and A2[i][c]!=0:
                f=A2[i][c]
                A2[i]=[A2[i][j]-f*A2[r][j] for j in range(m+1)]
        piv.append(c); r+=1
        if r==n: break
    x=[Fr(0)]*m
    for i,c in enumerate(piv):
        x[c]=A2[i][m]
    return x


def main():
    print("=== 验证：α0∈V ⟹ 归约到 V 上是 obs'=d' 的满情形 ===\n")
    hdr = "%-12s %3s %5s %5s %9s %9s %8s" % ("实例","d","obs","dimV","原成功率","归约后","obs'=d'")
    print(hdr); print("-"*len(hdr))
    for (n,seed,trials) in [(4,70052,[0,5]),(5,70065,[0,7])]:
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
            Rrow=row_space_basis(R)
            V=invariant_closure(R, Ap, d)
            dv=len(V)
            def rate_on(Rrows, Aop, dcur, nsamp, seedv, fixrow):
                # 允许的 β 空间 = row(Rrows) 在 dcur 维里
                Bsp=row_space_basis(Rrows) if Rrows else []
                mB=len(Bsp)
                rngv=random.Random(seedv)
                ns=0; nb=0
                k=dcur   # 自由行数（总 q=dcur+1，固定 1 行）
                tt=time.time()
                while ns<nsamp and time.time()-tt<15:
                    ns+=1
                    A0=[fixrow[0][:]]; A1=[fixrow[1][:]]
                    for _i in range(k):
                        al=[Fr(rngv.randint(-2,2)) for _ in range(dcur)]
                        be=[sum((Fr(rngv.randint(-2,2)))*Bsp[t][j] for t in range(mB)) for j in range(dcur)] if mB else [Fr(0)]*dcur
                        alAp=[sum(al[i]*Aop[i][j] for i in range(dcur)) for j in range(dcur)]
                        A0.append(al[:]); A1.append([alAp[j]+be[j] for j in range(dcur)])
                    if not cond_5a(A0,A1): continue
                    if cond_5b(A0,A1): nb+=1
                return (100.0*nb/ns if ns else -1), ns
            # 原问题
            r_orig,ns1 = rate_on(R, Ap, d, 100, 111111+97*trial+n, [mm(L0,N)[0][:], mm(mm(L0,A),N)[0][:]])
            # 归约到 V：坐标化
            Vb=V
            AopV=[[ (solve_in_basis(Vb, [sum(Vb[i][t]*Ap[t][j] for t in range(d)) for j in range(d)]) )[i]
                    for i in range(dv)] for _ in [0]]
            # 更简单地：A'_V 的矩阵 = 对每个基向量 v_i，v_i·A' 的坐标
            AopV=[]
            for i in range(dv):
                w=[sum(Vb[i][t]*Ap[t][j] for t in range(d)) for j in range(d)]
                AopV.append(solve_in_basis(Vb, w))
            # row(R) 的坐标
            RrowV=[solve_in_basis(Vb, r[:]) for r in Rrow] if Rrow else []
            # α0 的坐标
            a0=mm(L0,N)[0]
            g0=mm(mm(L0,A),N)[0]
            a0V=solve_in_basis(Vb, a0)
            g0V=solve_in_basis(Vb, g0)
            # 归约后的 obs'
            Vp=invariant_closure(RrowV, AopV, dv) if RrowV else []
            obsp=len(Vp)
            r_red,ns2 = rate_on(RrowV, AopV, dv, 100, 222222+97*trial+n, [a0V, g0V])
            print("%-12s %3d %5d %5d %8.0f%% %8.0f%% %9s" %
                  ("n=%d t=%d"%(n,trial), d, dv, dv, r_orig, r_red,
                   "✓ %d=%d" % (obsp, dv) if obsp==dv else "✗ %d≠%d" % (obsp, dv)))
    print()
    print("【判读】若每个实例都 obs'=d'（满）且归约后成功率仍高 ⟹ 充分性化归成立 ✓")


if __name__=="__main__":
    main()
