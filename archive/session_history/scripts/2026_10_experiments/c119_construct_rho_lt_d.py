r"""
c119_construct_rho_lt_d.py -- 构造 ρ<d 的解（不靠采样）

原理：选 K ⊆ ker(L0 N) ∩ ker(L0 A N)，dim K = d−ρ，
      令 L 的行 ⊆ (N K + A N K)^⊥  ⟹ K ⊆ ker M 且 K ⊆ ker F
      再检验完整的 (5a) 与 (5b)。
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
    """返回矩阵 M 的零空间，每行一个基向量"""
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

def main():
    print("=== 构造 ρ<d 的解（K ⊆ ker(L0N)∩ker(L0AN) 方法）===\n")
    n=5; p=1
    t0=time.time(); t=0; inst=0
    found=0; tot=0; rho_hist={}
    while time.time()-t0<420 and inst<10:
        t+=1
        rng=random.Random(980000+t)
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
        # 取 L0
        L0=None
        for _x in range(80):
            cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(cand)!=1: continue
            if rk(cand+Cc)!=2: continue
            if rk(mm(cand,N))==0: continue
            L0=cand; break
        if L0 is None: continue
        inst+=1
        L0N=mm(L0,N)[0]        # length d
        L0AN=mm(mm(L0,A),N)[0] # length d
        # K0 = ker(L0N) ∩ ker(L0AN)
        Mst=[L0N[:],L0AN[:]]
        K0=nullspace_rows(Mst)
        dimK0=len(K0)
        print("[实例 %d] d=%d, dim(ker L0N ∩ ker L0AN)=%d" % (inst,d,dimK0))
        if dimK0<1: continue
        # 对每个 κ = 1..dimK0，取 K = 前 κ 个向量
        for kap in range(1,dimK0+1):
            Kbasis=K0[:kap]
            # 构造 (N K + A N K)^⊥ 的基：即解 [N k ; A N k]^T y = 0
            rows=[]
            for kv in Kbasis:
                kv_c=[[kv[j]] for j in range(d)]      # d×1
                Nkv=mm(N,kv_c)                         # n×1
                ANkv=mm(AN,kv_c)                       # n×1
                rows.append([Nkv[i][0] for i in range(n)])
                rows.append([ANkv[i][0] for i in range(n)])
            ann=nullspace_rows(rows)   # 每个是 n 维向量
            if not ann: continue
            # L0 必须 ∈ span(ann)
            annB=rowspace_basis(ann)
            if rk([r[:] for r in annB]+[L0[0][:]])!=len(annB): continue
            # 候选 L：L0 + (q−1) 个 ann 的组合
            for q in (2,3):
                kk=q-1
                if len(annB)==0: continue
                rr=random.Random(101+13*inst+7*kap+q)
                pts=[[rr.randint(-2,2) for _ in range(kk*len(annB))] for _ in range(1200)]
                for vals in pts:
                    Lm=[L0[0][:]]
                    for ti in range(kk):
                        z=vals[ti*len(annB):(ti+1)*len(annB)]
                        Lm.append([sum(z[s]*annB[s][j] for s in range(len(annB))) for j in range(n)])
                    if rk(Lm)!=q: continue
                    A0=mm(Lm,N); A1=mm(mm(Lm,A),N)
                    rho=rk(A0)
                    if rho!=d-kap: continue    # 核恰好是 K
                    if not cond_5a(A0,A1): continue
                    tot+=1
                    rho_hist[rho]=rho_hist.get(rho,0)+1
                    is5b=cond_5b(A0,A1)
                    if is5b:
                        found+=1
                        if found<=6:
                            print("   *** 解：q=%d ρ=%d (<d=%d) ***" % (q,rho,d))
                            print("      L =", [[str(x) for x in r] for r in Lm])
                            print("      M =", [[str(x) for x in r] for r in A0])
                            print("      F =", [[str(x) for x in r] for r in A1])
                        break
    print()
    print("构造出的 (5a)-候选（核恰好 K）: %d ；其中 (5b) 成立（真解）: %d" % (tot,found))
    print("ρ 分布：", sorted(rho_hist.items()))
    if found>0:
        print("\n⟹ *** 成功构造 ρ<d 的解 *** ⟹ 可用它检验 (a)(b)")
    else:
        print("\n⟹ 该构造未能产生 (5b)-解")

if __name__=="__main__":
    main()
