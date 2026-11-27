"""531：两个 530 gadget 的块对角组合（p=4,q=6），验证合取 soundness。"""
import sympy as sp

x1, y1, z1, x2, y2, z2, lam = sp.symbols('x1 y1 z1 x2 y2 z2 lam')

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

A1, C1, L1 = block(x1, y1, z1)
A2, C2, L2 = block(x2, y2, z2)
A = sp.diag(A1, A2)
C = sp.diag(C1, C2)
L = sp.diag(L1, L2)
CA = C * A

def check(vals, tag):
    sub = dict(zip([x1, y1, z1, x2, y2, z2], vals))
    Am = A.subs(sub); Lm = L.subs(sub); CAm = CA.subs(sub); Cm = C
    base = sp.Matrix.vstack(Lm, CAm, Cm).rank()
    fivea = sp.Matrix.vstack(Lm * Am, Lm, CAm, Cm).rank()
    ranks = [sp.Matrix.vstack(lam * Lm - Lm * Am, CAm, Cm).subs(lam, lv).rank() for lv in [0, 1, 2, 3]]
    print(tag, 'base=', base, '(5a)=', fivea, 'ranks=', ranks)

check((2, 3, 6, 2, 3, 6), 'both gates:')
check((2, 3, 7, 2, 3, 6), 'gate1 fails:')
check((2, 3, 6, 2, 3, 7), 'gate2 fails:')
check((2, 3, 6, -sp.Rational(1, 2), 2, -1), 'gate2 at x=-1/2:')
