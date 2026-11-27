r"""
c118_genuine_ab.py -- 真检验 (a) 与 (b)：n=5,p=1,d=3,q=2（ρ≤2<3）

需要 obs ≤ 2 才有可能有解（否则 ρ=obs 要求 ρ≥obs>2）。
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
    print("=== 真检验 (a)(b)：n=5,p=1,d=3,q=2 ===\n")
    n=5; p=1
    t0=time.time(); t=0; inst=0
    tot=0; both=0; only_b=0; only_a=0; neither=0; viol=0
    while time.time()-t0<430 and inst<8:
        t+=1
        rng=random.Random(970000+t)
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A); Mrows=Cc+CA
        if rk(Mrows)!=2: continue
        N=ker_basis(Mrows)
        if not N or not N[0]: continue
        d=len(N[0])
        if d!=3: continue
        AN=mm(A,N)
        Nt=[[N[i][j] for i in range(n)] for j in range(d)]
        iNtN=minv(mm(Nt,N))
        if iNtN is None: continue
        Ap=mm(mm(iNtN,Nt),AN)
        NAp=mm(N,Ap)
        R0=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
        Vb=invcl(R0,Ap,d); obs=len(Vb)
        if obs>2: continue      # 否则 q=2 下 ρ=obs 不可能
        inst+=1
        Mcol=[N[i][:]+AN[i][:] for i in range(n)]
        resB=rowspace_basis(Mcol); mB=len(resB)
        L0=None
        for _x in range(80):
            cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(cand)!=1: continue
            if rk(cand+Cc)!=2: continue
            if rk(mm(cand,N))==0: continue
            L0=cand; break
        if L0 is None: continue
        H0=mm(L0,N); F0=mm(mm(L0,A),N)
        q=2; kk=q-1; npar=kk*mB
        rr=random.Random(91+7*inst)
        if npar<=5:
            pts=list(itertools.product([-2,-1,0,1,2],repeat=npar))
        else:
            pts=[[rr.randint(-2,2) for _ in range(npar)] for _ in range(4000)]
        loc=0; locboth=0
        for vals in pts:
            A0=[H0[0][:]]; A1=[F0[0][:]]
            for ti in range(kk):
                z=vals[ti*mB:(ti+1)*mB]
                if len(z)<mB: break
                w=[sum(z[tt]*resB[tt][j] for tt in range(mB)) for j in range(2*d)]
                A0.append(w[:d]); A1.append(w[d:])
            if len(A0)!=q: continue
            if not cond_5a(A0,A1): continue
            if not cond_5b(A0,A1):
                # 非解：也记录 (a)(b) 以便对比
                pass
            rho=rk(A0)
            if rho==0: continue
            if rho==obs and rho>0: viol+=0
            kerM=ker_basis(A0)
            if not kerM or not kerM[0]:
                # ρ=d=3，但 q=2 使 ρ≤2，不会发生
                continue
            # kerM 是 d×m，其**列**是核向量
            R0K=mm(R0,kerM)
            a_ok = all(all(x==0 for x in r) for r in R0K)
            ApK=mm(Ap,kerM)
            cols=[[r[:] for r in kerM][i] for i in range(len(kerM))]+[[ApK[i][j] for i in range(d)] for j in range(len(ApK[0]))]
            b_ok = rk(cols)==rk(kerM)
            is5b=cond_5b(A0,A1)
            if is5b:
                loc+=1; tot+=1
                if a_ok and b_ok: both+=1; locboth+=1
                elif b_ok: only_b+=1
                elif a_ok: only_a+=1
                else: neither+=1
                if not (a_ok and b_ok):
                    print("   **解但 (a)(b) 不全**：ρ=%d obs=%d a=%s b=%s" % (rho,obs,a_ok,b_ok))
        print("[实例 %d] obs=%d d=3 ；解 %d ；(a)∧(b) 成立 %d" % (inst,obs,loc,locboth))
    print()
    print("解 %d ：(a)∧(b) %d ；仅(b) %d ；仅(a) %d ；都无 %d" % (tot,both,only_b,only_a,neither))
    if both==tot and tot>0:
        print("\n⟹ *** 真检验（ρ≤2<d=3）：所有解都满足 (a)∧(b) *** ✓")
        print("   这是第一次在 ρ<d 且 q 受限的情形下真检验缺口")
    elif tot==0:
        print("\n⟹ 无解（该实例族可能无 ρ<3 的解）")
    else:
        print("\n⟹ 有解不满足 (a)∧(b) ⟹ 缺口假 ✗")

if __name__=="__main__":
    main()
