r"""
c26_obs_criterion.py -- ⭐⭐⭐⭐ 严格验证判据：Type II ⟺ obs < d_CA

【判据】
  obs := dim Σ_{k=0}^{d-1} row(R)·A'^k
       = 含 row(R) 的**最小 A'-不变子空间**的维数
  A'  := (NᵀN)⁻¹NᵀAN,  R := AN − N·A'

  **Type II（无解）⟺ obs < d_CA**
  **Type I（q=d_CA+1 处 generic YES）⟺ obs = d_CA**

【意义】obs 与 A' 都是**多项式可算**的
  ⟹ 若判据成立，q1 的判定 = 一次不变子空间闭包计算 ⟹ **多项式** ⟹ **q1 为假**

【本脚本】扩大规模（更多实例、更大样本），统计分离度
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


def main():
    print("=== 判据验证：Type II ⟺ obs < d_CA ===\n")
    hdr = "%-3s %-5s %3s %3s %3s %8s %6s %7s %4s" % ("n","inst","d","m","e","obs","obs<d?","成功率","判定")
    print(hdr); print("-"*len(hdr))
    nI=nII=nMis=0
    for n in [5,6]:
        rng=random.Random(864200+n)
        done=0; t_all=time.time()
        for trial in range(120000):
            if done>=10 or time.time()-t_all>500: break
            A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
            Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(Cc)!=1: continue
            CA=mm(Cc,A)
            if rk(CA)!=1: continue
            W=Cc+CA
            N=ker_basis(W)
            if not N or not N[0]: continue
            d=len(N[0])
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
            Rrow=row_space_basis(R); e=len(Rrow)
            if e==0: continue
            # obs = dim 最小 A'-不变子空间 ⊇ row(R)
            acc=[r[:] for r in Rrow]; cur=[r[:] for r in Rrow]
            while len(acc) < d:
                cur=mm(cur,Ap)
                new=rk(acc+[r[:] for r in cur])
                if new==len(acc): break
                acc=acc+[r[:] for r in cur]
            obs=len(acc) if False else rk(acc)
            H0=mm(L0,N); F0=mm(mm(L0,A),N)
            Mcol=[N[i][:]+AN[i][:] for i in range(n)]
            resB=row_space_basis(Mcol); mB=len(resB)
            q=d+1; k=q-1
            rng2=random.Random(975310+97*trial+n)
            ns=0; nb=0
            tt=time.time()
            while ns<250 and time.time()-tt<25:
                ns+=1
                rr=[[Fr(rng2.randint(-2,2)) for _ in range(mB)] for _ in range(k)]
                A0=[H0[i][:] for i in range(1)]; A1=[F0[i][:] for i in range(1)]
                for z in rr:
                    w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                    A0.append(w[:d]); A1.append(w[d:])
                if not cond_5a(A0,A1): continue
                if cond_5b(A0,A1): nb+=1
            rate=100.0*nb/ns if ns else -1
            pred = "II" if obs<d else "I"
            actual = "II" if rate < 1.0 else "I"
            mark = "✓" if pred==actual else "**✗**"
            if pred!=actual: nMis+=1
            if actual=="I": nI+=1
            else: nII+=1
            print("%-3d %-5d %3d %3d %3d %8d %6s %6.1f%% %4s" %
                  (n,trial,d,mB,e,obs,"Y" if obs<d else "N",rate,mark))
            done+=1
        print()
    print("="*58)
    print("Type I 实例：%d ；Type II 实例：%d ；判据失配：%d" % (nI,nII,nMis))
    print()
    if nMis==0 and nI>0 and nII>0:
        print("⟹⟹⟹ **判据成立：Type II ⟺ obs < d_CA**（%d 个实例全部吻合）⭐⭐⭐⭐" % (nI+nII))
        print("     ⟹ obs 与 A' 都多项式可算 ⟹ **判定多项式** ⟹ **q1 为假**")
        print("     ⟹ |R|_min = d_CA+1−r 若 obs=d_CA ；否则无解（恒 NO）")
        print()
        print("     ⭐ 注意：这与 history/49 的 D6 模论对象**同一** ——")
        print("        '含 row(R) 的最小 A'-不变子空间' 正是 q0 下界问题的核心量！")
    else:
        print("⟹ 判据有失配（%d 个）或有组为空 —— 需继续分析" % nMis)


if __name__=="__main__":
    main()
