r"""
c120_obs3_rho2.py -- 决定性：obs=3, d=4, 构造 ρ=2 的 (5a)-候选，查 (5b)

κ = dim(ker L0N ∩ ker L0AN) = d−2 = 2  ⟹ ρ = 2 < obs = 3
若找到 (5b)-解 ⟹ 缺口假（ρ<obs 有解）
"""
import os, io, contextlib, random, itertools, sys, time
from fractions import Fraction as Fr
_HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,_HERE)
from exact_gcd import cond_5b

_ns={}
with open(os.path.join(_HERE,"exact_count_thm7.py"),encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(),"lib","exec"),_ns)
rk=_ns["rk"]; mm=_ns["mm"]; ker_basis=_ns["ker_basis"]

def rowspace_basis(M):
    if not M or not M[0]: return []
    mr=len(M); nc=len(M[0])
    A=[[Fr(x) for x in row] for row in M]
    piv=[]; r=0
    for c in range(nc):
        p=None
        for i in range(r,mr):
            if A[i][c]!=0: p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for i in range(mr):
            if i!=r and A[i][c]!=0:
                f=A[i][c]; A[i]=[A[i][j]-f*A[r][j] for j in range(nc)]
        piv.append(r); r+=1
        if r==mr: break
    return [A[i][:] for i in piv]

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
                f=A[i][c]; A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
        piv.append(c); r+=1
        if r==m: break
    free=[c for c in range(n) if c not in piv]
    out=[]
    for fc in free:
        v=[Fr(0)]*n; v[fc]=Fr(1)
        for i,c in enumerate(piv): v[c]=-A[i][fc]
        out.append(v)
    return out

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
                f=A2[i][c]; A2[i]=[A2[i][j]-f*A2[c][j] for j in range(2*n)]
    return [row[n:] for row in A2]

def cond_5a(A0,A1):
    K=ker_basis(A0)
    if not K or not K[0]: return True
    if len(A1[0])!=len(K): return False
    return rk(mm(A1,K))==0

def invcl(M0,Ap,d):
    b=rowspace_basis(M0); cur=[r[:] for r in b]
    while len(b)<d and b:
        cur=mm(cur,Ap)
        if rk(b+[r[:] for r in cur])==len(b): break
        b=b+[r[:] for r in cur]
    return rowspace_basis(b)

def main():
    print("=== obs=3, d=4, ρ=2（非平凡） ===\n")
    n=6; p=1
    t0=time.time(); t=0; inst=0; okinst=0
    tot=0; sol=0
    while time.time()-t0<430 and okinst<4:
        t+=1
        rng=random.Random(990000+t)
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A); Mrows=Cc+CA
        if rk(Mrows)!=2: continue
        N=ker_basis(Mrows)
        if not N or not N[0]: continue
        d=len(N[0])
        if d!=4: continue
        AN=mm(A,N)
        Nt=[[N[i][j] for i in range(n)] for j in range(d)]
        iNtN=minv(mm(Nt,N))
        if iNtN is None: continue
        Ap=mm(mm(iNtN,Nt),AN)
        NAp=mm(N,Ap)
        R0=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
        Vb=invcl(R0,Ap,d); obs=len(Vb)
        if obs!=3: continue
        L0=None
        for _x in range(100):
            cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(cand)!=1: continue
            if rk(cand+Cc)!=2: continue
            if rk(mm(cand,N))==0: continue
            L0=cand; break
        if L0 is None: continue
        okinst+=1
        L0N=mm(L0,N)[0]; L0AN=mm(mm(L0,A),N)[0]
        K0=nullspace_rows([L0N[:],L0AN[:]])
        kap=len(K0)
        print("[实例 %d] dim(ker L0N∩ker L0AN)=%d  rho目标=%d" % (okinst,kap,d-kap))
        if kap!=2: continue
        rows=[]
        for kv in K0:
            kv_c=[[kv[j]] for j in range(d)]
            Nkv=mm(N,kv_c); ANkv=mm(AN,kv_c)
            rows.append([Nkv[i][0] for i in range(n)])
            rows.append([ANkv[i][0] for i in range(n)])
        ann=rowspace_basis(nullspace_rows(rows))
        if not ann: continue
        if rk([r[:] for r in ann]+[L0[0][:]])!=len(ann): 
            print("   (L0 不在正交补中，跳过)")
            continue
        diag={}; diag5a={}
        for q in (2,3):
            kk=q-1
            rr=random.Random(111+13*okinst+q)
            pts=[[rr.randint(-2,2) for _ in range(kk*len(ann))] for _ in range(1500)]
            loc=0; locs=0
            for vals in pts:
                Lm=[L0[0][:]]
                for ti in range(kk):
                    z=vals[ti*len(ann):(ti+1)*len(ann)]
                    Lm.append([sum(z[s]*ann[s][j] for s in range(len(ann))) for j in range(n)])
                if rk(Lm)!=q: continue
                A0=mm(Lm,N); A1=mm(mm(Lm,A),N)
                rho=rk(A0)
                diag[rho]=diag.get(rho,0)+1
                if rho!=2: continue
                if not cond_5a(A0,A1):
                    diag5a[0]=diag5a.get(0,0)+1
                    continue
                diag5a[1]=diag5a.get(1,0)+1
                loc+=1; tot+=1
                if cond_5b(A0,A1):
                    locs+=1; sol+=1
                    if sol<=5:
                        print("   *** 找到 ρ=2 < obs=3 且 (5b) 成立的解！***")
                        print("      L =", [[str(x) for x in r] for r in Lm])
                        print("      M =", [[str(x) for x in r] for r in A0])
                        print("      F =", [[str(x) for x in r] for r in A1])
            print("   q=%d：rho分布=%s  (5a)通过=%s  => (5a)&rho=2 的候选 %d ；(5b) 成立 %d" % (q,sorted(diag.items()),sorted(diag5a.items()),loc,locs))
    print()
    print("(5a)∧ρ=2 候选总数 %d ；**(5b) 成立（即 ρ<obs 的解）%d**" % (tot,sol))
    if sol>0:
        print("\n⟹ *** 缺口假！（ρ < obs 且有解）*** ⟹ q1 可能为真")
    elif tot>0:
        print("\n⟹ *** 非平凡证据：obs=3 时所有 ρ=2 的 (5a)-候选都使 (5b) 失败 *** ✓")
        print("   这正是缺口（ρ≥obs）所预测的")

if __name__=="__main__":
    main()
