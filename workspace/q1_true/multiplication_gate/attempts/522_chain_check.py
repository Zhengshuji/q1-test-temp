"""522：链式/共享变量的检查器组合：gate2 的 x 取 gate1 的 z（x2 := z1）。
验证整体可行 ⇔ z1=x1y1 且 z2=z1*y2。"""
import sympy as sp

x1, y1, z1, y2, z2, lam = sp.symbols('x1 y1 z1 y2 z2 lam')

def block(x, y, z):
    return (sp.Matrix([[-2, 0, 0, 0, 0],
                       [0, -2, 0, 0, 0],
                       [0, 0, 2, 0, 0],
                       [2 * y, 2, -2, 0, 0],
                       [0, 0, 0, 1, 0]]),
            sp.Matrix([[z, x, 0, -1, 0],
                       [y, 1, 0, 2, 0],
                       [0, 0, 1, 2, 0]]))

A1, L1 = block(x1, y1, z1)
A2, L2 = block(z1, y2, z2)          # x2 := z1
A = sp.diag(A1, A2)
C = sp.zeros(2, 10); C[0, 4] = 1; C[1, 9] = 1
L = sp.diag(L1, L2)
CA = C * A

def check(vals, tag):
    sub = dict(zip([x1, y1, z1, y2, z2], vals))
    Am = A.subs(sub); Lm = L.subs(sub); CAm = CA.subs(sub)
    base = sp.Matrix.vstack(Lm, CAm, C).rank()
    fivea = sp.Matrix.vstack(Lm * Am, Lm, CAm, C).rank()
    ranks = [sp.Matrix.vstack(lam * Lm - Lm * Am, CAm, C).subs(lam, lv).rank() for lv in [0, 1, 2, 3]]
    print(tag, 'base=', base, '(5a)=', fivea, 'ranks=', ranks)

check((2, 3, 6, 5, 30), 'chain holds (z2=z1*y2):')
check((2, 3, 6, 5, 31), 'z2 wrong:')
check((2, 3, 7, 5, 35), 'z1 wrong, z2 adjusted:')
