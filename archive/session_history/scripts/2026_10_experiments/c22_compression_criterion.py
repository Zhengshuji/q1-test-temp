r"""
c22_compression_criterion.py -- ⭐⭐⭐⭐ 用 (A', row R) 找判据

【结构分解】
  A' := (NᵀN)⁻¹Nᵀ·A·N     （d×d，"压缩"）
  R  := A·N − N·A'        （n×d，"偏离部分"）
  ⟹ W = {(α, αA' + β) : α ∈ R^d, β ∈ row(R)} ,  dim row(R) = m − d

【候选判据（全部只依赖 A' 与 row(R)，均多项式可算）】
  C_a: R = 0                        （K 不变）—— 已知 ⟹ 恒失败
  C_b: A' 无实特征值
  C_c: row(R) 与 A' 的（实）特征空间无交
  C_d: dim row(R) ≥ 1 且 ∃ 实 λ: row(R) ⊄ ker 部分…
  C_e: A' 的极小多项式无实根
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
    if len(A1[0])!=len(K): return False
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

def has_real_root_sq(coef):
    """二次/一次/零次 有理系数多项式是否有实根（判别式；高次用近似）"""
    c=[x for x in coef]
    while len(c)>1 and c[-1]==0: c.pop()
    if len(c)==1: return True
    if len(c)==2: return True                 # 一次：总有一实根
    if len(c)==3:
        a,b,cc=c[2],c[1],c[0]
        return (b*b-4*a*cc)>=0
    return None                                # 高次：不判


def main():
    print("=== 用 (A', row R) 找判据 ===\n")
    print("%-3s %-5s %3s %3s %5s %5s %8s %8s %8s" %
          ("n","inst","d","m","dimR","A'实谱","ρ0","采样","成功率"))
    print("-"*60)
    data=[]
    for n in [5,6]:
        rng=random.Random(313100+n)
        done=0; t_all=time.time()
        for trial in range(80000):
            if done>=7 or time.time()-t_all>400: break
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
            q0=sum(eta)
            AN=mm(A,N)
            # 压缩 A' 与偏离 R
            Nt=[[N[i][j] for i in range(n)] for j in range(d)]
            NtN=mm(Nt,N)
            iNtN=minv(NtN)
            if iNtN is None: continue
            Ap=mm(mm(iNtN,Nt),AN)              # d×d
            NAp=mm(N,Ap)
            R=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
            dimR=rk(R)
            m=d+dimR
            # A' 的实谱？（用 d 阶特征多项式；d ≤ 4，可判）
            coef=None
            try:
                coef=[Fr(0)]
                # 用 Faddeev 求特征多项式
                d2=d
                I=[[Fr(1) if i==j else Fr(0) for j in range(d2)] for i in range(d2)]
                cs=[]; Acur=[r[:] for r in I]
                for k in range(1,d2+1):
                    Mk=mm(Ap,Acur)
                    c=-sum(Mk[i][i] for i in range(d2))/k
                    cs.append(c)
                    Acur=[[Mk[i][j]+(c if i==j else Fr(0)) for j in range(d2)] for i in range(d2)]
                coef=[cs[-1]]+list(reversed(cs[:-1]))+[Fr(1)]
            except Exception:
                coef=None
            rs = has_real_root_sq(coef) if coef else None
            Mcol=[N[i][:]+AN[i][:] for i in range(n)]
            B=row_space_basis(Mcol); mm_=len(B)
            H0=mm(L0,N); F0=mm(mm(L0,A),N)
            rho0=rk(H0)
            q=d+1; k=q-1
            rng2=random.Random(555111+97*trial+n)
            ns=0; nboth=0
            tt=time.time()
            while ns<250 and time.time()-tt<25:
                ns+=1
                rr=[[Fr(rng2.randint(-2,2)) for _ in range(mm_)] for _ in range(k)]
                A0=[H0[i][:] for i in range(1)]; A1=[F0[i][:] for i in range(1)]
                for z in rr:
                    w=[sum(z[t]*B[t][j] for t in range(mm_)) for j in range(2*d)]
                    A0.append(w[:d]); A1.append(w[d:])
                if not cond_5a(A0,A1): continue
                if cond_5b(A0,A1): nboth+=1
            rate=100.0*nboth/ns if ns else -1
            print("%-3d %-5d %3d %3d %5d %8s %5d %6d %7.1f%%" %
                  (n,trial,d,m,dimR,"有" if rs else ("无" if rs is False else "?"),
                   rho0,ns,rate))
            data.append((dimR, rs, rate))
        print()
    print("【按 (dimR, A'实谱) 分组】")
    keys=sorted(set((a,b) for a,b,_ in data), key=lambda z:(z[0],str(z[1])))
    for kk in keys:
        v=[r for a,b,r in data if (a,b)==kk]
        print("  dimR=%d, A'实谱=%-5s : n=%d, 成功率 %s" %
              (kk[0], str(kk[1]), len(v),
               "[%.1f, %.1f] 均值%.1f" % (min(v),max(v),sum(v)/len(v))))
    print()
    print("【判读】若某组全 0% 而另一组全 >50% ⟹ 判据找到")


if __name__ == "__main__":
    main()
