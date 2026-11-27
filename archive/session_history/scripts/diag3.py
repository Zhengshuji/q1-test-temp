from fractions import Fraction as F
def rref(M):
    M=[r[:] for r in M]
    if not M: return M,[]
    nr,nc=len(M),len(M[0]); piv=[]; r=0
    for c in range(nc):
        p=None
        for i in range(r,nr):
            if M[i][c]!=0: p=i;break
        if p is None: continue
        M[r],M[p]=M[p],M[r]; pv=M[r][c]; M[r]=[x/pv for x in M[r]]
        for i in range(nr):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[a-f*b for a,b in zip(M[i],M[r])]
        piv.append(c); r+=1
        if r==nr: break
    return M,piv
def mm(X,Y):
    n,k,m=len(X),len(Y),len(Y[0])
    return [[sum(X[i][t]*Y[t][j] for t in range(k)) for j in range(m)] for i in range(n)]
def inv(M):
    n=len(M)
    R,piv=rref([M[i][:]+[F(1) if i==j else F(0) for j in range(n)] for i in range(n)])
    print("   inv: piv =",piv, " len=n?",len(piv)==n)
    return [row[n:] for row in R] if len(piv)==n else None
# 用一个已知可逆矩阵测试
M=[[F(1),F(2)],[F(3),F(4)]]
Mp=inv(M)
print("   M*M^-1 =",[[str(x) for x in row] for row in mm(M,Mp)])
# 复现 build_T_normalized 的 T
src=open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\build_T_normalized.py",encoding="utf-8").read()
src=src.split("MC = mm(inv(mm(transpose(NC), NC)), transpose(NC))\n        Abar")[0]
src+='''
print()
print("T =", [[str(x) for x in row] for row in T])
print("Tinv =", [[str(x) for x in row] for row in Tinv])
print("T*Tinv =", [[str(x) for x in row] for row in mm(T, Tinv)])
print("Tinv*T =", [[str(x) for x in row] for row in mm(Tinv, T)])
print("RNCT =", [[str(x) for x in row] for row in RNCT])
print("RNCT*Tinv =", [[str(x) for x in row] for row in mm(RNCT, Tinv)])
print("RNC      =", [[str(x) for x in row] for row in RNC])
'''
exec(compile(src,"x","exec"))
