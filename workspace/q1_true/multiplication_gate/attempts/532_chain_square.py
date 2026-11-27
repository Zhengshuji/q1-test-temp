"""532：530 gadget 的链式/平方电路（共享变量）核验。
- 链：gate2 的 x 取 gate1 的 z（x2:=z1），z2=z1*y2；
- 平方：gate1 的 y 取 x（y1:=x1），z1=x1^2。
"""
import sympy as sp

x1, y1, z1, y2, z2, lam = sp.symbols('x1 y1 z1 y2 z2 lam')

def block(x, y, z):
    A = sp.zeros(7, 7)
    A[3, 0] = -2 * y; A[3, 1] = -2; A[3, 2] = 2
    A[4, 2] = -2
    A[5, 3] = 1
    A[6, 4] = 1
    C = sp.zeros(2, 7); C[0, 5] = 1; C[1, 6] = 1
    L = sp.zeros(3, 7)
    L[0, 0] = z; L[0, 1] = x; L[0, 3] = 1
    L[1, 0] = y; L[1, 1] = 1; L[1, 4] = 1
    L[2, 2] = 1
    return A, C, L

def build(x2expr, tag):
    A1, C1, L1 = block(x1, y1, z1)
    A2, C2, L2 = block(x2expr, y2, z2)
    A = sp.diag(A1, A2); C = sp.diag(C1, C2); L = sp.diag(L1, L2)
    return A, C, L

def check(A, C, L, vals, tag):
    sub = dict(zip([x1, y1, z1, y2, z2], vals))
    Am = A.subs(sub); Lm = L.subs(sub); CAm = (C * A).subs(sub)
    base = sp.Matrix.vstack(Lm, CAm, C).rank()
    fivea = sp.Matrix.vstack(Lm * Am, Lm, CAm, C).rank()
    ranks = [sp.Matrix.vstack(lam * Lm - Lm * Am, CAm, C).subs(lam, lv).rank() for lv in [0, 1, 2, 3]]
    print(tag, 'base=', base, '(5a)=', fivea, 'ranks=', ranks)

# 链：x2 := z1
A, C, L = build(z1, 'chain')
check(A, C, L, (2, 3, 6, 5, 30), 'chain holds:')
check(A, C, L, (2, 3, 6, 5, 31), 'z2 wrong:')
check(A, C, L, (2, 3, 7, 5, 35), 'z1 wrong:')
check(A, C, L, (-sp.Rational(1, 2), 2, -1, 5, -5), 'chain at x1=-1/2:')

# 平方：y1 := x1
A, C, L = build(x1, 'square')
check(A, C, L, (3, 3, 9, 2, 6), 'square holds:')
check(A, C, L, (3, 3, 10, 2, 6), 'square wrong:')
