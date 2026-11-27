"""518 核验：sound 乘法 gadget（n=5,k=3,q=2，E≠0）。
L0 = [[z,x,0,1,0],[1,0,1,0,0]]
A  = [[1,0,0,0,0],[1-y,0,1,0,0],[-2,-1,y-1,0,0],[z,x,0,0,0],[0,0,0,1,0]]
C  = e5^T
"""
import sympy as sp

x, y, z, lam = sp.symbols('x y z lam')

L0 = sp.Matrix([[z, x, 0, 1, 0], [1, 0, 1, 0, 0]])
A = sp.Matrix([[1, 0, 0, 0, 0],
               [1 - y, 0, 1, 0, 0],
               [-2, -1, y - 1, 0, 0],
               [z, x, 0, 0, 0],
               [0, 0, 0, 1, 0]])
C = sp.Matrix([[0, 0, 0, 0, 1]])
N = sp.zeros(5, 3)
for i in range(3):
    N[i, i] = 1

# 压缩数据
H = L0 * N
HA = L0 * A * N

# (5a) 的两个子式
D1 = sp.factor(sp.Matrix([H.row(0), H.row(1), HA.row(0)]).det())
D2 = sp.factor(sp.Matrix([H.row(0), H.row(1), HA.row(1)]).det())
print('D1 =', D1)
print('D2 =', D2)
assert sp.expand(D1 - x * (z - x * y)) == 0
assert sp.expand(D2 - (z - x * y)) == 0
print('(5a): D1=x(z-xy), D2=z-xy  OK')

# 门上 (5b)
Hg = H.subs(z, x * y)
HAg = HA.subs(z, x * y)
P = lam * Hg - HAg
print('P at gate =', P)
minors = []
for i in range(2):
    for j in range(3):
        for k in range(j + 1, 3):
            minors.append(sp.expand(P[i, j] * P[1 - i, k] - P[i, k] * P[1 - i, j]))
minors = [m for m in minors if sp.expand(m) != 0]
g = sp.gcd_list(minors)
print('minors:', [sp.factor(m) for m in minors])
print('gcd =', sp.factor(g))
Q = lam**2 - lam * y + y
assert sp.expand(g + x * Q) == 0 or sp.expand(g - x * Q) == 0
print('(5b) on gate: gcd = +/- x*Q  (expected failure)  OK')
