"""515：对候选 l1 形状做符号消元：D1(gate)=0 的通解 + D2 的 z 系数。"""
import sympy as sp

x, y, z, lam = sp.symbols('x y z lam')
A1, A2, A3 = sp.symbols('A1 A2 A3')
a, b, c, p, q, r = sp.symbols('a b c p q r')
r1 = sp.Matrix([[1, 0, 0]])
r2 = sp.Matrix([[1 - y, 0, 1]])
r3 = sp.Matrix([[p, q, r]])
A = sp.Matrix.vstack(r1, r2, r3)
l1 = sp.Matrix([[A1, A2, A3]])
l2 = sp.Matrix([[a, b, c]])
HA0 = sp.Matrix.vstack(l1 * A, l2 * A)
D1g = sp.expand(sp.Matrix.vstack(l1, l2, HA0.row(0)).det().subs(z, x * y))
D2 = sp.expand(sp.Matrix.vstack(l1, l2, HA0.row(1)).det())

shapes = {
    '(z,y,1)': (z, y, 1),
    '(z,0,x)': (z, 0, x),
    '(z,1,x)': (z, 1, x),
    '(1,z,x)': (1, z, x),
    '(z,y,x)': (z, y, x),
}
for name, sh in shapes.items():
    d1 = sp.expand(D1g.subs({A1: sh[0], A2: sh[1], A3: sh[2]}))
    d2 = sp.expand(D2.subs({A1: sh[0], A2: sh[1], A3: sh[2]}))
    poly = sp.Poly(d1, x, y)
    eqs = [sp.expand(coeff) for _, coeff in poly.terms()]
    sol = sp.solve(eqs, [b, c, q, p], dict=True)
    print('===', name, 'eqs:', len(eqs), 'sol:', sol[:2] if sol else None)
    if sol:
        s0 = sol[0]
        d2s = sp.expand(d2.subs(s0))
        print('   D2 =', sp.factor(d2s))
