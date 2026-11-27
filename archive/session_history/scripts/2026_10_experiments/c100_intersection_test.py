r"""
c100_intersection_test.py -- 决定性检验：
   反例 ⟺ dim( rowspace([N|AN]) ∩ {α₀⊗(·)} ) ≥ 2  且 obs ≥ 2

做法：
 a) 定向构造 γ₀∥α₀ 的 L0（取 w，L0 在 annihilator(col(AN−wN)) 中）
 b) 计算 rowspace([N|AN]) ∩ {α₀⊗v} 的维数
 c) 若 ≥2 且 obs≥2，构造反例并验证
"""
import os, io, contextlib, random, sys, time
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

def invcl(M0,Ap,d):
    b=rowspace_basis(M0); cur=[r[:] for r in b]
    while len(b)<d and b:
        cur=mm(cur,Ap)
        if rk(b+[r[:] for r in cur])==len(b): break
        b=b+[r[:] for r in cur]
    return rowspace_basis(b)

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
    print("=== 决定性检验：交集维数 ≥ 2 是否可能（且 obs≥2）？ ===\n")
    t=0; tested=0; dimge2=0; counter=0
    t0=time.time()
    while time.time()-t0<400:
        t+=1
        n=random.Random(930000+t).choice([4,5,6])
        rng=random.Random(830000+t)
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A)
        if rk(CA)!=1: continue
        N=ker_basis(Cc+CA)
        if not N or not N[0]: continue
        d=len(N[0])
        if d<2: continue
        AN=mm(A,N)
        Nt=[[N[i][j] for i in range(n)] for j in range(d)]
        iNtN=minv(mm(Nt,N))
        if iNtN is None: continue
        Ap=mm(mm(iNtN,Nt),AN)
        NAp=mm(N,Ap)
        R0=[[AN[i][j]-NAp[i][j] for j in range(d)] for i in range(n)]
        Vb=invcl(R0,Ap,d); obs=len(Vb)
        if obs<2: continue
        # [N|AN] 行空间
        NAc=[N[i][:]+AN[i][:] for i in range(n)]
        RS=rowspace_basis(NAc)
        # 定向造 γ₀∥α₀ 的 L0：取 w，L0 ⊥ col(AN−wN)
        for w in (Fr(0),Fr(1),Fr(2),Fr(-1),Fr(1,2),Fr(3)):
            MW=[[AN[i][j]-w*N[i][j] for j in range(d)] for i in range(n)]   # n×d
            MWt=[[MW[i][j] for i in range(n)] for j in range(d)]           # d×n
            ann=nullspace_rows(MWt)                                        # L0 候选
            if not ann: continue
            for k in range(min(2,len(ann))):
                L0=[ann[k][:]]
                if rk(L0)!=1: continue
                if rk(L0+Cc)!=2: continue
                a0=mm(L0,N)[0]
                if all(x==0 for x in a0): continue
                tested+=1
                # 交集 dim：{ℓ ∈ rowspace([N|AN]) : ℓ = α₀⊗v}
                # 即找 v∈ℝ^{2d} 使 (α₀⊗v)∈RS。等价：解线性系统
                # 设 RS 的基为 {r_1..r_mB}，求系数 c 使 Σc_t r_t 的形状 = α₀⊗v
                # 即：对每个 j，第 j 列为 c·(r_t[j])，第 d+j 列为 c·(r_t[d+j])
                # 且比例固定为 α₀_j。用：对 j 使 α₀_j≠0，要求
                #   c·r^(col j) = α₀_j · v_1,  c·r^(col d+j) = α₀_j · v_2
                # 这是一个齐次系统（未知 c∈ℝ^m, v_1,v_2）
                mB=len(RS)
                j0=next(j for j in range(d) if a0[j]!=0)
                eqs=[]; rhs=[]
                # 归一化：令 v_1 = 1（即 α 部分 = α₀）
                for j in range(d):
                    eqs.append([RS[t][j] for t in range(mB)]+[-a0[j], Fr(0)])
                    rhs.append(Fr(0))
                for j in range(d):
                    eqs.append([RS[t][d+j] for t in range(mB)]+[Fr(0), -a0[j]])
                    rhs.append(Fr(0))
                # 齐次：求非零解（含 v1,v2 自由）
                # 用零空间：矩阵 eqs (2d × (mB+2))
                ker=nullspace_rows(eqs)
                # 交集的元素对应每个 ker 基向量的 (c) 部分
                vecs=[]
                for kv in ker:
                    c=kv[:mB]
                    row=[sum(c[t]*RS[t][s] for t in range(mB)) for s in range(2*d)]
                    if any(x!=0 for x in row): vecs.append(row)
                idim=rk(vecs) if vecs else 0
                if idim>=2:
                    dimge2+=1
                    print("[t=%d] n=%d d=%d obs=%d w=%s **交集维数=%d ≥2**" % (t,n,d,obs,str(w),idim))
                    # 构造：取交集的两个独立向量作两行
                    A0=[vecs[0][:d]]; A1=[vecs[0][d:]]
                    A0.append(vecs[1][:d]); A1.append(vecs[1][d:])
                    rho=rk(A0)
                    ok5a=cond_5a(A0,A1); ok5b=cond_5b(A0,A1)
                    print("      ρ=%d (5a)=%s (5b)=%s" % (rho,ok5a,ok5b))
                    if ok5a and ok5b and rho<obs:
                        counter+=1
                        print("      *** 真反例！L0=%s ***" % [str(x) for x in L0[0]])
                        print("      M=",[[str(x) for x in r] for r in A0])
                        print("      F=",[[str(x) for x in r] for r in A1])
                        break
            if counter>0: break
        if counter>0: break
    print()
    print("检查 %d 个 (L0,w)；交维≥2 的 %d 个；**真反例 %d 个**" % (tested,dimge2,counter))
    if counter>0:
        print("\n*** ρ≥obs 为假 ⟹ q1 方向需重新评估 ***")
    elif dimge2==0:
        print("\n⟹ 交集维数**从不 ≥2** ⟹ 反例不可能存在 ⟹ ρ≥obs 成立（在已测范围）")
        print("   这正是 ρ=obs 的**结构性原因**")


if __name__=="__main__":
    main()
