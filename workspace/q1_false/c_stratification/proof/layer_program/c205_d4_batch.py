r"""$d=4$ 谱步的**批量测试**：对随机实例算"可行 $\varphi$"的候选结构与 `covered`。

对 `d=4`、`dim B=1` 的实例（构造见下），按 [SPECTRAL_STEP_DESIGN.md](SPECTRAL_STEP_DESIGN.md) §3.1：
$$(N)\iff c(\varphi)=0\ \text{且}\ \Phi_1(\varphi)=\lambda\varphi,$$
在 $\ker c\cong\mathbb P^1$ 上"$\Phi_1(\varphi)\parallel\varphi$"= 三个**二元二次型**的公共零点。
本脚本把它们化成 $t$ 的一元多项式（两张图卡 $a=1$、$b=1$），用 gcd 求根，分类：

  * `none`       ：无解（公共零点只有零向量）⟹ 层不可行（该实例的 (3,1) 层没有可允许格子）✗；
  * `rational`   ：有**有理**解 ⟹ 逐个算 `covered`（有理算术，精确）；
  * `quadratic`  ：只有**二次域**解 ⟹ 未实现（记为待办 ✗）；
  * `degenerate` ：二次型全部恒为零 ⟹ 整条 $\mathbb P^1$ 都可行 ⟹ 用线判定（§5 的"两次取值"）。

用法：python proof/layer_program/c205_d4_batch.py [--trials 10] [--seed 5]
"""
import os
import random
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'proof', 'rho1_layer'))
sys.path.insert(0, _HERE)

import audit_independent as AI
import importlib.util as iu
import sympy as sp

spec = iu.spec_from_file_location('Q', os.path.join(_ROOT, 'proof', 'rho1_layer', 'quotient_selfcheck.py'))
Qm = iu.module_from_spec(spec)
spec.loader.exec_module(Qm)
spec2 = iu.spec_from_file_location('C202', os.path.join(_HERE, 'c202_d4_spectral_scan.py'))
C202 = iu.module_from_spec(spec2)
spec2.loader.exec_module(C202)

mm, rank, rb = Qm.mm, Qm.rank, Qm.rb
N = 7


def make_instance(rng):
    A = [[Fr(0)] * N for _ in range(N)]
    # 行 1、2 ∈ <e1,e2,e3>（保证 J = <e1,e2,e3>）
    for r in (0, 1):
        for c in range(3):
            A[r][c] = Fr(rng.randint(-1, 1))
    A[0][2] = Fr(1)                      # 让 e1A = e3（增加一维）
    # 行 3..7：任意，但行 3 要有 X 分量（使 B ≠ 0）
    for r in range(2, N):
        for c in range(3, N):
            A[r][c] = Fr(rng.randint(-2, 2))
    A[2][3] = Fr(1)                      # e3A 的 X 分量 = e4 ⟹ B = <e4>
    C = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)],
         [Fr(0), Fr(1), Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)]]
    return A, C


def analyse(Q, A):
    d = Q.d
    if d != 4 or len(Q.B) != 1:
        return None
    b = Q.B[0]
    e = [[Fr(1) if t == i else Fr(0) for t in range(d)] for i in range(d)]
    fv = [Q.pi(mm([Q.lift(ei)], A)[0]) for ei in e]
    Bperp = rb(AI.nullspace([b]))
    if len(Bperp) != 3:
        return None
    Phi = [[sum(Bperp[j][i] * fv[k][i] for i in range(d)) for k in range(d)] for j in range(3)]
    fb = Q.pi(mm([Q.lift(b)], A)[0])
    c = [sum(Bperp[j][i] * fb[i] for i in range(d)) for j in range(3)]
    # ker c（B^⊥ 坐标）
    xs = rb(AI.nullspace([c])) if any(c) else [[Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(1), Fr(0)]]
    if len(xs) != 2:
        return dict(kind='degenerate-line', why='c≡0 ⟹ 整条 B^⊥')
    # Φ_1 的 3×3 矩阵
    theta = None
    for i in range(d):
        if b[i] != 0:
            theta = [Fr(0)] * d
            theta[i] = Fr(1) / b[i]
            break
    A3 = [[None] * 3 for _ in range(3)]
    for j in range(3):
        psi = [Phi[j][k] - c[j] * theta[k] for k in range(d)]
        y = AI.rref([[Bperp[i][k] for i in range(3)] + [psi[k]] for k in range(d)])[0]
        sol = [Fr(0)] * 3
        for row in y:
            piv = next((t for t in range(3) if row[t] != 0), None)
            if piv is None:
                continue
            sol[piv] = row[3] / row[piv]
        for i in range(3):
            A3[i][j] = sol[i]
    # 二次型（在 a,b 里）
    a_, b_ = sp.symbols('a b')
    xv = [sp.Rational(xs[0][k].numerator, xs[0][k].denominator) * a_ +
          sp.Rational(xs[1][k].numerator, xs[1][k].denominator) * b_ for k in range(3)]
    M3 = sp.Matrix([[sp.Rational(A3[i][j].numerator, A3[i][j].denominator) for j in range(3)]
                    for i in range(3)])
    yv = [sum(M3[i, j] * xv[j] for j in range(3)) for i in range(3)]
    quads = [sp.expand(yv[i] * xv[j] - yv[j] * xv[i]) for (i, j) in [(0, 1), (0, 2), (1, 2)]]
    if all(q == 0 for q in quads):
        # 退化：整条 ker c 都可行 ⟹ 线判定（§5：dim Φ=1 时子式对 t 至多一次 ⟹ 两次取值）
        pts = []
        for tval in (Fr(0), Fr(1)):
            phi = [xs[0][k] + tval * xs[1][k] for k in range(3)]      # B^⊥ 坐标
            phiX = [sum(phi[j] * Bperp[j][k] for j in range(3)) for k in range(d)]
            D = C202.cell_data(Q, A, phiX)
            ok = bool(D and D.get('reason') == 'ok')
            pts.append((str(tval), ok,
                        C202.covered(D['T'], D['w']) if ok else None))
        return dict(kind='degenerate-line', pts=pts)
    g = sp.Poly(quads[0], a_, b_)
    for q in quads[1:]:
        g = sp.gcd(g, sp.Poly(q, a_, b_))
    if g.degree() == 0:
        return dict(kind='none', why='公共零点只有 0')
    sols = sp.solve([sp.Eq(q, 0) for q in quads], [a_, b_], dict=True)
    cands = []
    for sd in sols:
        av = sp.simplify(sd.get(a_, a_)); bv = sp.simplify(sd.get(b_, b_))
        if av.free_symbols and not bv.free_symbols and bv == 0:
            av = sp.Integer(1)
        elif bv.free_symbols and not av.free_symbols and av == 0:
            bv = sp.Integer(1)
        if av.free_symbols or bv.free_symbols:
            continue
        x = [sp.simplify(sp.Rational(av) * sp.Rational(xs[0][k].numerator, xs[0][k].denominator) +
                         sp.Rational(bv) * sp.Rational(xs[1][k].numerator, xs[1][k].denominator))
             for k in range(3)]
        if any(sp.simplify(v).is_rational is False for v in x):
            return dict(kind='quadratic', why='解在二次域')
        phi = [Fr(0)] * d
        for k in range(d):
            phi[k] = sum(Fr(int(sp.nsimplify(x[j]).p), int(sp.nsimplify(x[j]).q)) * Bperp[j][k]
                         for j in range(3))
        cands.append(phi)
    return dict(kind='rational', cands=cands)


def main():
    trials, seed = 10, 5
    if '--trials' in sys.argv:
        trials = int(sys.argv[sys.argv.index('--trials') + 1])
    if '--seed' in sys.argv:
        seed = int(sys.argv[sys.argv.index('--seed') + 1])
    rng = random.Random(seed)
    stats = {'none': 0, 'rational': 0, 'quadratic': 0, 'degenerate-line': 0, 'skip': 0}
    cov_true = cov_false = 0
    for t in range(trials):
        A, C = make_instance(rng)
        Q = Qm.Quotient(A, C)
        r = analyse(Q, A)
        if r is None:
            stats['skip'] += 1
            continue
        stats[r['kind']] += 1
        line = f'  #{t}: {r["kind"]}'
        if r['kind'] == 'degenerate-line':
            line += f'、两点取值 {r["pts"]}'
        if r['kind'] == 'rational':
            line += f'、{len(r["cands"])} 个候选'
            for phi in r['cands']:
                D = C202.cell_data(Q, A, phi)
                if D and D.get('reason') == 'ok':
                    cv = C202.covered(D['T'], D['w'])
                    cov_true += cv
                    cov_false += (not cv)
                    line += f'、covered={cv}'
        print(line)
    print()
    print(f'统计：{stats}')
    print(f'有理候选里：covered=True {cov_true} 个、covered=False {cov_false} 个')
    print('（quadratic 未实现 ✗；none ⟹ 该实例的 (3,1) 层不可行；covered=False ⟹ 层可行 ✓）')


if __name__ == '__main__':
    main()
