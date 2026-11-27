r"""
c92_routeB.py -- 路线 B：检验 ker(L) ∩ im(R₀) = 0 在解上是否成立

若成立 ⟹ 结合已证的 R₀(ker M) ⊆ ker L，得 ker M ⊆ ker R₀
       ⟹ ρ = obs ⟹ q_min = obs+1 ⟹ q1 为假
"""
import os, io, contextlib, random, itertools, sys
from fractions import Fraction as Fr
_HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,_HERE)
from exact_gcd import cond_5b

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

def colspace(M):
    if not M or not M[0]: return []
    Mt=[[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]
    return rowspace_basis(Mt)

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

def build_L(A0,H0,L0,resB,mB,d,vals,kk,q_r):
    """从参数构造 L（按 resB 展开的 q_r 行额外行）"""
    L=[L0[0][:]]
    extra=[]
    for ti in range(kk):
        z=vals[ti*mB:(ti+1)*mB]
        w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
        L.append(w[:d]); extra.append(w[d:])
    return L

def main():
    print("=== 路线 B 检验：ker(L) ∩ im(R₀) = 0 ？ ===\n")
    n=4
    rng=random.Random(707070)
    got=0; tot_sol=0; zero_int=0; nonzero_int=0
    t0=__import__("time").time()
    while got<6 and __import__("time").time()-t0<300:
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A)
        if rk(CA)!=1: continue
        W=Cc+CA; N=ker_basis(W)
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
        V=invariant_closure=rowspace_basis
        # 用 invariant closure 计算 obs
        def invcl(M0):
            b=rowspace_basis(M0); cur=[r[:] for r in b]
            while len(b)<d and b:
                cur=mm(cur,Ap)
                if rk(b+[r[:] for r in cur])==len(b): break
                b=b+[r[:] for r in cur]
            return rowspace_basis(b)
        Vb=invcl(R0); obs=len(Vb)
        L0=None
        for _x in range(60):
            cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(cand)!=1: continue
            if rk(cand+Cc)!=2: continue
            pv=[sum(cand[0][i]*N[i][j] for i in range(n)) for j in range(d)]
            if all(x==0 for x in pv): continue
            if Vb and rk([r[:] for r in Vb]+[pv])!=len(Vb): continue
            L0=cand; break
        if L0 is None: continue
        if rk(L0+Cc)!=2: continue
        try:
            _Lx,eta=p1(A,Cc,L0)
        except Exception:
            continue
        if not eta: continue
        Mcol=[N[i][:]+AN[i][:] for i in range(n)]
        resB=rowspace_basis(Mcol); mB=len(resB)
        H0=mm(L0,N); F0=mm(mm(L0,A),N)
        q=d+1; kk=q-1; npar=kk*mB
        pts=list(itertools.product([-1,0,1],repeat=npar)) if npar<=6 else \
            [[rng.randint(-2,2) for _ in range(npar)] for _ in range(600)]
        cnt=0; zi=0; ni=0
        for vals in pts:
            A0=[H0[0][:]]; A1=[F0[0][:]]
            Lrows=[L0[0][:]]
            for ti in range(kk):
                z=vals[ti*mB:(ti+1)*mB]
                w=[sum(z[t]*resB[t][j] for t in range(mB)) for j in range(2*d)]
                A0.append(w[:d]); A1.append(w[d:])
                # 还原 n 维行：w = [α|γ]，其中 α=L·N, γ=L·AN
                # 解 L_row·[N|AN] = w  （在 resB 的坐标系下）
                # 已知 w = Σ z_t resB_t，且 resB_t = e_t·[N|AN]  ⟹ L_row = Σ z_t e_t
                Lr=[Fr(0)]*n
                for t in range(mB):
                    if z[t]!=0:
                        # e_t 是第 t 个基向量（在 ℝ^n 的坐标下）
                        Lr[t]+=z[t]
                Lrows.append(Lr)
            if not cond_5a(A0,A1): continue
            if not cond_5b(A0,A1): continue
            cnt+=1
            # ker(L) 与 im(R0) 的交
            Lb=rowspace_basis(Lrows)            # L 的行空间
            kerL=nullspace_rows(Lb)             # L 的零空间（n 维）
            imR=colspace(R0)                    # im(R0)
            if not kerL or not imR:
                zi+=1; continue
            # dim(ker L ∩ im R0) = dim kerL + dim imR − dim(kerL+imR)
            comb=[r[:] for r in kerL]+[r[:] for r in imR]
            dim_int=len(kerL)+len(imR)-rk(comb)
            if dim_int==0: zi+=1
            else: ni+=1
        tot_sol+=cnt; zero_int+=zi; nonzero_int+=ni
        print("[#%d] d=%d obs=%d | 解 %3d | 交集为 0: %3d ; 非零: %d" %
              (got,d,obs,cnt,zi,ni))
        got+=1
    print()
    print("总解数 %d ；ker(L)∩im(R₀)=0 的解 %d ；非零 %d" % (tot_sol,zero_int,nonzero_int))
    if nonzero_int==0 and tot_sol>0:
        print("\n⟹ **ker(L)∩im(R₀)=0 对所有解成立** ⟹ 路线 B 可行 ✓")
        print("   ⟹ 结合已证的 R₀(ker M)⊆ker L ⟹ ker M ⊆ ker R₀ ⟹ ρ=obs ⟹ q1 为假")
    else:
        print("\n⟹ 存在交集非零的解 ⟹ 路线 B **不成立**，需转路线 A ✗")


if __name__=="__main__":
    main()
