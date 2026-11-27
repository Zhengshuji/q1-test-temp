"""515b：l1=(z,0,x) 的第二族解：b=aq/p, c=a(r-1)/p，检查 D2。"""
import sympy as sp

x, y, z = sp.symbols('x y z')
a, p, q, r = sp.symbols('a p q r')
r1 = sp.Matrix([[1, 0, 0]])
r2 = sp.Matrix([[1 - y, 0, 1]])
r3 = sp.Matrix([[p, q, r]])
A = sp.Matrix.vstack(r1, r2, r3)
l1 = sp.Matrix([[z, 0, x]])
l2 = sp.Matrix([[a, a * q / p, a * (r - 1) / p]])
HA0 = sp.Matrix.vstack(l1 * A, l2 * A)
D1 = sp.expand(sp.Matrix.vstack(l1, l2, HA0.row(0)).det())
D2 = sp.expand(sp.Matrix.vstack(l1, l2, HA0.row(1)).det())
print('D1 =', sp.factor(D1))
print('D2 =', sp.expand(D2))
print('D2 z-coeff =', sp.expand(D2).coeff(z, 1))
