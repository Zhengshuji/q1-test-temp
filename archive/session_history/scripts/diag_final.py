from fractions import Fraction as F
import numpy as np
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
def rank(M): return 0 if not M or not M[0] else len(rref(M)[1])
def mm(X,Y):
    n,k,m=len(X),len(Y),len(Y[0])
    return [[sum(X[i][t]*Y[t][j] for t in range(k)) for j in range(m)] for i in range(n)]
def toF(M): return [[F(int(x)) for x in row] for row in M]
A=toF([[1,0,2,0,-1],[-1,-2,-1,-1,-2],[0,1,-2,-1,0],[-2,-2,1,-1,1],[-2,-2,-1,0,0]])
C=toF([[2,0,0,0,0]]); L0=toF([[0,2,0,1,0]])
def condA(L):
    LA=mm(L,A); W=L+C+mm(C,A)
    return rank(W+LA)==rank(W), rank(W+LA), rank(W)
R=toF([[-35,8*-6,0,0,0]]) if False else [[F(-35,8),F(-6),F(-7,4),F(-3),F(-21,8)]]
# R_2: 第1分量为 0，后4个分量与 R 的 N_C 分量相同 -> R_2 = R - (R的第1分量/2)*C
c = R[0][0]/C[0][0]
R2=[[R[0][j] - c*C[0][j] for j in range(5)]]
print("R  =",[str(x) for x in R[0]])
print("R2 =",[str(x) for x in R2[0]])
print("R - R2 =",[str(R[0][j]-R2[0][j]) for j in range(5)], "  (应为 C 的倍数)")
print("condA(R) =",condA(L0+R))
print("condA(R2)=",condA(L0+R2))
print()
print("R2 是否 = X_low*M_C 形式（第1分量为0）:",R2[0][0]==0)
