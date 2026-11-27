r"""
c18_clean_correlate.py -- ⭐⭐⭐⭐ 干净的相关性实验（判据与成功率在同一轮内测）

【修正 c17 的错误】
  c14 的采样用**同一个 rng** 消耗随机数 ⟹ 实例序列被扰动 ⟹ c17 的标签错位！
  本脚本：**实例生成**用 rng，**采样**用独立 rng2 ⟹ 判据与成功率严格对齐。

【测的判据】
  C1: m − d > 0            （K 非不变；m = rank[N | AN] 列拼接）
  C2: rank[N; AN] > rank(AN)   （row(N) ⊄ row(AN)；新判据）
  C3: ρ0 = rank(L0·N) ≥ 1  （L0 非退化）
"""
import os
import io
import contextlib
import random
import itertools
import time
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
def Pd(a,b):
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
        _,r=Pd(a,b); a,b=b,r
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
    assert len(A1[0])==len(K)
    return rk(mm(A1,K))==0

def cond_5b(A0,A1,maxminors=400):
    q=len(A0); d=len(A0[0]); rho=rk(A0)
    if rho==0: return True
    P=[[[-A1[i][j], A0[i][j]] for j in range(d)] for i in range(q)]
    ps=[]; cnt=0
    for rows in itertools.combinations(range(q),rho):
        for cols in itertools.combinations(range(d),rho):
            dd=Pdet([[P[i][j] for j in cols] for i in rows],rho)
            if dd!=[Fr(0)]: ps.append(dd)
            cnt+=1
            if cnt>maxminors: break
        if cnt>maxminors: break
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


def main():
    print("=== 干净相关性：判据 vs q=d+1 处成功率 ===\n")
    print("%-3s %-5s %3s %3s %3s %5s %5s %5s %5s %8s %8s" %
          ("n","inst","q0","d","m","C1","C2","C3","ρ0","采样","成功率"))
    print("-"*70)
    rows_out=[]
    for n in [5,6]:
        rng=random.Random(555000+n)          # 仅用于实例生成
        done=0; t_all=time.time()
        for trial in range(80000):
            if done>=5 or time.time()-t_all>350: break
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
            q0=sum(eta); r=1
            AN=mm(A,N)
            Mcol=[N[i][:]+AN[i][:] for i in range(n)]
            m=rk(Mcol)
            Mrow=[r2[:] for r2 in N]+[r2[:] for r2 in AN]
            rAN=rk(AN); rRow=rk(Mrow)
            H0=mm(L0,N); F0=mm(mm(L0,A),N)
            rho0=rk(H0)
            C1 = (m-d>0); C2 = (rRow>rAN); C3 = (rho0>=1)
            B=row_space_basis(Mcol); mm_=len(B)
            q=d+1; k=q-r
            # **独立 rng2** 用于采样
            rng2=random.Random(900000+97*trial+q)
            ns=0; n5a=0; nboth=0
            tt=time.time()
            while ns<300 and time.time()-tt<30:
                ns+=1
                rr=[[Fr(rng2.randint(-2,2)) for _ in range(mm_)] for _ in range(k)]
                A0=[H0[i][:] for i in range(r)]; A1=[F0[i][:] for i in range(r)]
                for z in rr:
                    w=[sum(z[t]*B[t][j] for t in range(mm_)) for j in range(2*d)]
                    A0.append(w[:d]); A1.append(w[d:])
                if not cond_5a(A0,A1): continue
                n5a+=1
                if cond_5b(A0,A1): nboth+=1
            rate=100.0*nboth/ns if ns else -1
            done+=1
            print("%-3d %-5d %3d %3d %3d %5s %5s %5s %5d %8d %7.1f%%" %
                  (n,trial,q0,d,m,"T" if C1 else "F","T" if C2 else "F",
                   "T" if C3 else "F",rho0,ns,rate))
            rows_out.append((C1,C2,C3,rate))
        print()
    print("【相关性】")
    for i,lab in [(0,"C1: m−d>0"),(1,"C2: row(N)⊄row(AN)"),(2,"C3: ρ0≥1")]:
        T=[r[3] for r in rows_out if r[i]]
        F=[r[3] for r in rows_out if not r[i]]
        print("  %-22s: T组 均值%.1f%% (n=%d) ; F组 均值%.1f%% (n=%d)" %
              (lab, sum(T)/len(T) if T else -1, len(T),
               sum(F)/len(F) if F else -1, len(F)))
    print()
    print("【判读】若某个判据的 T 组成功率≈100% 且 F 组≈0% ⟹ 它就是类型判据")


if __name__ == "__main__":
    main()
