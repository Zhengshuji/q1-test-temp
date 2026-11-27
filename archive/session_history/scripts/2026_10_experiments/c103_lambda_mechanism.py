r"""
c103_lambda_mechanism.py -- λ-机制检验

对每个 (5a) 成立但 W⊄U 的候选：
 1. 确认 (5b) 失败
 2. 找出使 rank(λM−F) < ρ 的 λ（根）
 3. 看这些 λ 与 A' 的谱、以及 x∈ker M\ker R_0 的关系
"""
import os, io, contextlib, random, itertools, sys, time
from fractions import Fraction as Fr
_HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,_HERE)
from exact_gcd import cond_5b, Pdet, Pt, gcd_list, is_nonzero_const

_ns={}
with open(os.path.join(_HERE,"exact_count_thm7.py"),encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(),"lib","exec"),_ns)
rk=_ns["rk"]; mm=_ns["mm"]; ker_basis=_ns["ker_basis"]
_t={}
with open(os.path.join(_HERE,"test_caseII_YES.py"),encoding="utf-8") as fh:
    _src=fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(_src.split("rng = random.Random")[0],"t","exec"),_t)
p1=_t["p1"]

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

def pencil_gcd(A0,A1):
    """返回所有 ρ 阶子式的 gcd（多项式）"""
    q=len(A0); d=len(A0[0]); rho=rk(A0)
    if rho==0: return [Fr(1)]
    P=[[[-A1[i][j], A0[i][j]] for j in range(d)] for i in range(q)]
    ps=[]
    for rows in itertools.combinations(range(q),rho):
        for cols in itertools.combinations(range(d),rho):
            ps.append(Pdet([[P[i][j] for j in cols] for i in rows],rho))
    return gcd_list(ps)

def rat_roots(coef):
    """有理根（简单版）"""
    c=Pt(coef)
    if len(c)<=1: return []
    out=[]
    for num in range(-6,7):
        for den in (1,2,3):
            x=Fr(num,den)
            v=Fr(0)
            for cc in reversed(c): v=v*x+cc
            if v==0: out.append(x)
    return sorted(set(out))

def main():
    print("=== λ-机制检验：W⊄U 时是哪个 λ 杀死 (5b)？ ===\n")
    n=4
    rng=random.Random(151617)
    got=0; found=0; t0=time.time()
    while got<6 and time.time()-t0<350:
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A)
        if rk(CA)!=1: continue
        N=ker_basis(Cc+CA)
        if not N or not N[0]: continue
        d=len(N[0])
        if d!=2: continue
        AN=mm(A,N)
        Nt=[[N[i][j] for i in range(n)] for j in range(d)]
        iNtN=minv(mm(Nt,N))
        if iNtN is None: continue
        Ap=mm(mm(iNtN,Nt),AN)
        NAp=mm(N,Ap)
        R0=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
        R0b=rowspace_basis(R0)
        L0=None
        for _x in range(40):
            cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(cand)!=1: continue
            if rk(cand+Cc)!=2: continue
            pv=[sum(cand[0][i]*N[i][j] for i in range(n)) for j in range(d)]
            if all(x==0 for x in pv): continue
            L0=cand; break
        if L0 is None: continue
        if rk(L0+Cc)!=2: continue
        try: _Lx,eta=p1(A,Cc,L0)
        except Exception: continue
        Mcol=[N[i][:]+AN[i][:] for i in range(n)]
        resB=rowspace_basis(Mcol); mB=len(resB)
        H0=mm(L0,N); F0=mm(mm(L0,A),N)
        q=d+1; kk=q-1; npar=kk*mB
        pts=list(itertools.product([-1,0,1],repeat=npar)) if npar<=6 else \
            [[rng.randint(-2,2) for _ in range(npar)] for _ in range(300)]
        nbad=0
        for vals in pts:
            A0=[H0[0][:]]; A1=[F0[0][:]]
            for ti in range(kk):
                z=vals[ti*mB:(ti+1)*mB]
                w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                A0.append(w[:d]); A1.append(w[d:])
            if not cond_5a(A0,A1): continue
            U=rowspace_basis(A0)
            if rk([r[:] for r in U]+[r[:] for r in R0b])==len(U): continue  # 只看 W⊄U
            nbad+=1
            if nbad<=2:
                g=pencil_gcd(A0,A1)
                roots=rat_roots(g)
                print("[#%d] W⊄U。pencil gcd = %s" % (got,[str(x) for x in g]))
                print("     有理根 λ = %s" % [str(r) for r in roots])
                print("     ρ=%d, A' 的行 = %s" % (rk(A0), [[str(x) for x in r] for r in Ap]))
                # 检查这些 λ 是否 A' 的特征值
                chi=[Fr(1)]
                # 2x2 charpoly of A'
                tr=Ap[0][0]+Ap[1][1]; det=Ap[0][0]*Ap[1][1]-Ap[0][1]*Ap[1][0]
                chiroots=rat_roots([det,-tr,Fr(1)])
                print("     A' 的有理特征值 = %s" % [str(r) for r in chiroots])
        if nbad>0:
            found+=nbad
        got+=1
    print()
    print("检查 %d 个实例；W⊄U 的候选 %d 个" % (got,found))
    print("（观察：pencil gcd 的根 vs A' 的特征值）")

if __name__=="__main__":
    main()
