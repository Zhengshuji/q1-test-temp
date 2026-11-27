import sys, random, itertools
sys.path.insert(0, "tools/verification")
import sympy as sp
import c335_lambda_movement as m
lam = sp.symbols("lam")

print("=" * 70)
print("c359：no-go 的两块砖")
print("=" * 70)
# 砖 1：层块上 rank H = omega => (5a) 自动成立
k = 3
e = [sp.Matrix([[1 if j == i else 0 for j in range(k)]]) for i in range(k)]
W = [e[0], e[1]]                    # W = span{e1,e2}
H0 = e[0]; HA0 = e[0]               # 固定行（协调）
rng = random.Random(359)
ok = 0
for t in range(20):
    h1 = rng.randint(-2,2)*e[0] + rng.randint(-2,2)*e[1]
    h2 = rng.randint(-2,2)*e[0] + rng.randint(-2,2)*e[1]
    g1 = rng.randint(-2,2)*e[0] + rng.randint(-2,2)*e[1]
    g2 = rng.randint(-2,2)*e[0] + rng.randint(-2,2)*e[1]
    H = sp.Matrix.vstack(H0, h1, h2); HA = sp.Matrix.vstack(HA0, g1, g2)
    if H.rank() != 2: continue
    assert (HA * m.ker_basis(H)).is_zero_matrix, "rank H = omega 时 (5a) 应自动成立"
    ok += 1
print(f"  砖1：层块内 rank H = 2 的点共 {ok} 个，(5a) 全部自动成立 ✓")

# 砖 2：两个仿射线性函数之积是仿射 => 其中一个必为常数
u1, u2, v1, v2 = sp.symbols("u1 u2 v1 v2")
x = 2 + 3*u1 - u2
y = -1 + u1 + 2*u2
prod = sp.expand(x*y)
quad = sp.Poly(prod, u1, u2).coeffs()
deg = sp.Poly(prod, u1, u2).total_degree()
print(f"  砖2：x*y = {prod}，次数 {deg}（>1 ⟹ 非仿射 ⟹ 不退化不可能）")

# 一般性：随机仿射 x,y，若 x*y 是仿射则其一为常数
bad = 0
for _ in range(200):
    a = sp.Matrix([[rng.randint(-2,2)] for _ in range(3)])
    b = sp.Matrix([[rng.randint(-2,2)] for _ in range(3)])
    c1, c2 = rng.randint(-2,2), rng.randint(-2,2)
    X = c1 + a[0,0]*u1 + a[1,0]*u2
    Y = c2 + b[0,0]*u1 + b[1,0]*u2
    P = sp.Poly(sp.expand(X*Y), u1, u2)
    if P.total_degree() <= 1:
        # 只可能当其中一个的线性部分是 0
        if not (sp.simplify(X).is_number or sp.simplify(Y).is_number):
            # 检查线性部分
            if (a[0,0], a[1,0]) != (0, 0) and (b[0,0], b[1,0]) != (0, 0):
                bad += 1
print(f"  砖2 数值扫描：200 组随机仿射对中，'积为仿射但两者都非平凡' 的例数 = {bad}（应为 0）")
assert bad == 0 and ok > 0
print("  两块砖都成立 ✓")
