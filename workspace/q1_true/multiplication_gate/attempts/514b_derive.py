"""514b：l1=(z,x,1) 时 D1(gate)、D2 的符号形式（p,q,r,a,b,c 为符号）。"""
import sympy as sp

x, y, z, lam = sp.symbols('x y z lam')
a, b, c, p, q, r = sp.symbols('a b c p q r')
r1 = sp.Matrix([[1, 0, 0]])
r2 = sp.Matrix([[1 - y, 0, 1]])
r3 = sp.Matrix([[p, q, r]])
A = sp.Matrix.vstack(r1, r2, r3)
l1 = sp.Matrix([[z, x, 1]])
l2 = sp.Matrix([[a, b, c]])
H0 = sp.Matrix.vstack(l1, l2)
HA0 = sp.Matrix.vstack(l1 * A, l2 * A)
D1 = sp.expand(sp.Matrix.vstack(l1, l2, HA0.row(0)).det().subs(z, x * y))
D2 = sp.expand(sp.Matrix.vstack(l1, l2, HA0.row(1)).det())
print('D1(gate) =', sp.factor(D1))
print('D2 =', sp.factor(D2))
print('D1 poly:', sp.Poly(D1, x, y).terms())
print('D2 poly:', sp.Poly(D2, x, y, z).terms())
