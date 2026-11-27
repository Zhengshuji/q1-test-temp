"""521：两个 520 gadget 的块对角组合，检查 soundness（可行 ⇔ 两条乘法都成立）。"""
import sympy as sp

x1, y1, z1, x2, y2, z2, lam = sp.symbols('x1 y1 z1 x2 y2 z2 lam')

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
A2, L2 = block(x2, y2, z2)
A = sp.diag(A1, A2)
C = sp.zeros(2, 10)
C[0, 4] = 1
C[1, 9] = 1
L = sp.diag(L1, L2)
CA = C * A

def check(vals, tag):
    sub = dict(zip([x1, y1, z1, x2, y2, z2], vals))
    Am = A.subs(sub); Lm = L.subs(sub); CAm = CA.subs(sub)
    base = sp.Matrix.vstack(Lm, CAm, C).rank()
    fivea = sp.Matrix.vstack(Lm * Am, Lm, CAm, C).rank()
    ranks = [sp.Matrix.vstack(lam * Lm - Lm * Am, CAm, C).subs(lam, lv).rank() for lv in [0, 1, 2, 3]]
    print(tag, 'rank base=', base, '(5a)=', fivea, 'ranks=', ranks)

check((2, 3, 6, 2, 3, 6), 'both gates hold:')
check((2, 3, 7, 2, 3, 6), 'gate1 fails only:')
check((2, 3, 6, 2, 3, 7), 'gate2 fails only:')
check((2, 3, 7, 2, 3, 7), 'both fail:')
