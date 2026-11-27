"""512 核验：输入控制乘法门的 (5a)/(5b)（压缩模型 N=I3）。
L0=[[z,x,0],[1,0,1]]，A=[[1,0,0],[1-y,0,1],[-2,-1,y-1]]。
"""
import sympy as sp

x, y, z, lam = sp.symbols('x y z lam')
L0 = sp.Matrix([[z, x, 0], [1, 0, 1]])
A = sp.Matrix([[1, 0, 0], [1 - y, 0, 1], [-2, -1, y - 1]])

H0 = L0
HA0 = L0 * A

D1 = sp.factor(sp.Matrix([L0.row(0), L0.row(1), HA0.row(0)]).det())
D2 = sp.factor(sp.Matrix([L0.row(0), L0.row(1), HA0.row(1)]).det())
print('D1 =', D1)
print('D2 =', D2)
assert sp.expand(D1 - x * (z - x * y)) == 0
assert sp.expand(D2 - (z - x * y)) == 0
print('(5a): D1 = x(z-xy), D2 = z-xy  OK')

# 门上 z = xy
Hz = H0.subs(z, x * y)
HAz = HA0.subs(z, x * y)
print('rank H (generic x!=0) =', Hz.rank())
P = lam * Hz - HAz
minors = []
for i in range(2):
    for j in range(3):
        for k in range(j + 1, 3):
            minors.append(sp.expand(P[i, j] * P[1 - i, k] - P[i, k] * P[1 - i, j]))
minors = [m for m in minors if sp.expand(m) != 0]
print('minors:', [sp.factor(m) for m in minors])
g = sp.gcd_list(minors)
print('gcd =', sp.factor(g))
Q = lam**2 - lam*y + lam + 1  # alpha=-1
assert sp.expand(g + x * Q) == 0 or sp.expand(g - x * Q) == 0
print('(5b) on gate: gcd = +/- x*Q  (expected failure)  OK')
