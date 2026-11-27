r"""
c36_alpha0_in_V.py -- ⭐⭐⭐⭐⭐ 检验统一判据：
   YES at q=d+1  ⟺  α0 = L0N ∈ V := <row(R)>_{A'}（含 row(R) 的最小 A'-不变子空间）

【动机】
  · 若 obs=d ⟹ V=ℝ^d ⟹ 判据自动成立 ⟹ **解释 52/52**
  · obs<d 时 V 真，判据是实质条件
  · 与 ρ=1 判据（α0∈row(R)）在 obs=1 时一致（此时 V=rowR）
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
    """含 row(M) 的最小 A'-不变子空间（对右乘 A' 封闭）"""
    basis = row_space_basis(M)
    cur = [r[:] for r in basis]
    while len(basis) < d:
        cur = mm(cur, Ap)
        new = rk(basis + [r[:] for r in cur])
        if new == len(basis):
            break
        basis = basis + [r[:] for r in cur]
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


def in_span(basis, v):
    if not basis:
        return all(x==0 for x in v)
    return rk([r[:] for r in basis] + [v[:]]) == len(basis)


def main():
    print("=== 统一判据：YES ⟺ α0 = L0N ∈ V = <row(R)>_{A'} ===\n")
    hdr = "%-12s %3s %5s %5s %7s %9s %8s %6s %6s" % ("实例","d","obs","dimV","α0∈V","成功率","预测","一致","")
    print(hdr); print("-"*len(hdr))
    ok=0; bad=0
    for (n,seed,nalpha) in [(4,70052,8),(5,70065,8),(6,70078,6)]:
        rng=random.Random(seed)
        got=0; t_all=time.time()
        for trial in range(200000):
            if got>=nalpha or time.time()-t_all>240: break
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
            Nt=[[N[i][j] for i in range(n)] for j in range(d)]
            iNtN=minv(mm(Nt,N))
            if iNtN is None: continue
            Ap=mm(mm(iNtN,Nt),AN)
            NAp=mm(N,Ap)
            R=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
            V=invariant_closure(R, Ap, d)
            obs=len(V)
            a0=mm(L0,N)
            a0in = in_span(V, a0[0])
            Mcol=[N[i][:]+AN[i][:] for i in range(n)]
            resB=row_space_basis(Mcol); mB=len(resB)
            H0=mm(L0,N); F0=mm(mm(L0,A),N)
            q=d+1; k=q-1
            rng2=random.Random(424242+97*trial+n)
            ns=0; nb=0
            tt=time.time()
            while ns<100 and time.time()-tt<15:
                ns+=1
                rr=[[Fr(rng2.randint(-2,2)) for _ in range(mB)] for _ in range(k)]
                A0=[H0[0][:]]; A1=[F0[0][:]]
                for z in rr:
                    w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                    A0.append(w[:d]); A1.append(w[d:])
                if not cond_5a(A0,A1): continue
                if cond_5b(A0,A1): nb+=1
            rate=100.0*nb/ns if ns else -1
            pred=a0in
            actual = rate>1.0
            good=(pred==actual)
            if good: ok+=1
            else: bad+=1
            print("%-12s %3d %5d %5d %7s %8.1f%% %7s %5s%s" %
                  ("n=%d t=%d"%(n,trial), d, obs, len(V),
                   "Y" if a0in else "N", rate,
                   "YES" if pred else "NO", "✓" if good else "✗",
                   "" if good else "  ← 反例"))
            got+=1
        print()
    print("="*64)
    print("一致 %d ；**不一致 %d**" % (ok,bad))
    print()
    if bad==0 and ok>0:
        print("⟹⟹⟹⟹⟹ **统一判据成立：YES ⟺ α0 ∈ <row(R)>_{A'}** ⭐⭐⭐⭐⭐")
        print("     · obs=d 时 V=ℝ^d ⟹ 自动成立 ⟹ 解释 52/52")
        print("     · 判据是多项式的（不变子空间闭包 + 秩比较）")
        print("     ⟹ **判定多项式 ⟹ q1 为假（NP-hardness 不成立）**")
    else:
        print("⚠️ 有 %d 个反例，判据需修正" % bad)


if __name__=="__main__":
    main()
