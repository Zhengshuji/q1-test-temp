"""530：p=2 落地无坏集 gadget（n=7,q=3），原始矩阵核验。"""
import sympy as sp

x, y, z, lam = sp.symbols('x y z lam')

A = sp.zeros(7, 7)
A[3, 0] = -2 * y
A[3, 1] = -2
A[3, 2] = 2
A[4, 2] = -2
A[5, 3] = 1          # row6 = e4
A[6, 4] = 1          # row7 = e5

C = sp.zeros(2, 7)
C[0, 5] = 1
C[1, 6] = 1

L0 = sp.zeros(3, 7)
L0[0, 0] = z; L0[0, 1] = x; L0[0, 3] = 1
L0[1, 0] = y; L0[1, 1] = 1; L0[1, 4] = 1
L0[2, 2] = 1

def check(vals, tag):
    sub = dict(zip([x, y, z], vals))
    Am = A.subs(sub); L = L0.subs(sub); Cm = C
    CA = Cm * Am
    r0 = sp.Matrix.vstack(L, CA, Cm).rank()
    r5 = sp.Matrix.vstack(L * Am, L, CA, Cm).rank()
    ranks = [sp.Matrix.vstack(lam * L - L * Am, CA, Cm).subs(lam, lv).rank() for lv in [0, 1, 2, 3]]
    d = sp.factor(sp.expand(sp.Matrix.vstack(lam * L - L * Am, CA, Cm).det()))
    print(tag, 'r0=', r0, '(5a)=', r5, 'ranks=', ranks, 'det=', d)

check((2, 3, 6), 'gate (2,3,6):')
check((2, 3, 7), 'off-gate (2,3,7):')
check((-sp.Rational(1, 2), 2, -1), 'gate x=-1/2:')
