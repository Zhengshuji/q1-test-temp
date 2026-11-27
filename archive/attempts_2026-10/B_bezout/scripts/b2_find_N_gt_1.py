r"""B-1 补充：寻找 **$N>1$** 的实例（通用 Bézout 版本的必要检验）。

**为什么需要**：B-1 在已测实例上都有 $N=1$（gcd 判据退化为单个多项式）。通用 Bézout 证书
$\sum_i g_if_i=1$（$N\ge2$）**从未被检验**。

**$N>1$ 的条件**：
1. $r+t<\dim(W/S)$，即 $N=\binom{w-s}{r+t}\ge2$；
2. 至少两个子式**非零**——这要求 $[U\mid P]$ 的列**不**全落在某个坐标子空间里，
   即 $\operatorname{im}P\not\subseteq H/S$（否则含"外面那一行"的子式全零）。

**做法**：随机实例 + 正确几何（零化子构造）+ 条件筛选 + 逐 $U$ 算子式。

用法：python workspace/B_bezout/scripts/b2_find_N_gt_1.py
"""
import itertools
import os
import random
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import coeff_of_S as CS_
import bezout_cert as BC
import base_sweep as BS
import spectral_gcd as SG


def geometry(A, C, L0):
    """正确的几何（零化子构造），返回 V,W,H,G,D 与维数."""
    n = len(A)
    CA = AI.mul(C, A)
    V = AI.nullspace([r[:] for r in (C + CA)])
    W = AI.nullspace([r[:] for r in C])
    H = AI.nullspace([r[:] for r in (C + L0)])
    Vp = AI.nullspace([list(x) for x in V])
    Hp = AI.nullspace([list(x) for x in H])
    G = AI.nullspace(Vp + Hp)
    Gp = AI.nullspace([list(x) for x in G])
    D = AI.nullspace(Gp + AI.mul(Hp, A))
    return dict(n=n, V=V, W=W, H=H, G=G, D=D,
                v=len(V), w=len(W), h=len(H), b=len(G), dimD=len(D))


def lift(coefs, D, n):
    out = []
    for row in coefs:
        v = [Fr(0)] * n
        for j, c in enumerate(row):
            for i in range(n):
                v[i] += Fr(c) * D[j][i]
        out.append(v)
    return out


def main():
    rng = random.Random(20261101)
    print("寻找 N>1 且 gcd 是单位 的实例（非平凡 Bézout 证书）\n")
    print(f"{'n':<4}{'p':<4}{'w':<4}{'v':<4}{'h':<4}{'b':<4}{'q':<4}{'s':<4}{'r':<4}{'t':<4}{'wm':<4}{'N':<4}{'非零子式':<8}")
    found = 0
    for _ in range(600):
        n = rng.choice([6, 7, 8])
        p = rng.choice([1, 2])
        def unit(i):
            return [Fr(1) if k == i else Fr(0) for k in range(n)]
        C = [unit(i) for i in range(p)]
        L0 = [unit(p)]
        A = [[Fr(0)] * n for _ in range(n)]
        for _ in range(n):
            A[rng.randrange(n)][rng.randrange(n)] = Fr(rng.choice([-1, 1, 2]))
        try:
            geo = geometry(A, C, L0)
        except Exception:
            continue
        if geo['dimD'] < 1:
            continue
        for s in (1, 2):
            if s > geo['dimD']:
                continue
            for q in range(1, geo['w']):
                d = geo['w'] - q
                r = d - s
                t = geo['v'] - s
                wm = geo['w'] - s
                if r < 1 or t < 1:
                    continue
                if r + t >= wm:
                    continue          # 平衡或超出 ⟹ N=1
                # 取一个 S
                coords = BS.enum_subspaces(geo['dimD'], s, bound=1)[:3]
                for cf in coords:
                    S = lift(cf, geo['D'], n)
                    if len(S) < s:
                        continue
                    try:
                        st = CS_.setup(A, C, L0, q, S)
                        cols = CS_.pencil_cols(A, st)
                    except Exception:
                        continue
                    m = st['m']
                    if len(cols) != t:
                        continue
                    # 取一个一般位置的 U（HS 的组合）
                    HS = st['HS']
                    u = [sum(Fr((i + 1)) * HS[i][k] for i in range(m)) for k in range(wm)]
                    Uc = [u]
                    if r > 1:
                        if m < r:
                            continue
                        Uc = [HS[i] for i in range(r)]
                    info = BC.analyse(Uc, cols, wm, r)
                    _degs = [SG.pdeg(f) for f in info['fs']]
                    if info['N'] > 1 and info['is_unit'] and min(_degs) >= 1:
                        print(f"{n:<4}{p:<4}{geo['w']:<4}{geo['v']:<4}{geo['h']:<4}{geo['b']:<4}"
                              f"{q:<4}{s:<4}{r:<4}{t:<4}{wm:<4}{info['N']:<4}"
                              f"{str(info['deg_g']):<8}  <-- 找到")
                        print(f"     证书验证: ok={info['cert_ok']}  deg(gs)={info['cert_degree']} "
                              f"bound={info['bound']}  子式次数={[SG.pdeg(f) for f in info['fs']]}")
                        ok, acc = BC.verify_certificate(info['fs'], info['gs'], target=[Fr(1)])
                        print(f"     sum g_i f_i == 1 ? {ok}   (实际: {[str(x) for x in acc]})")
                        found += 1
                        if found >= 3:
                            return
    if not found:
        print("\n未找到 N>1 且可行的实例（300 次随机试验内）。")
        print("=> 若在更广的参数范围内也找不到，说明'单个行列式'可能是**结构性**的，")
        print("   那么通用 Bézout 证书在本项目中**永远用不上**——这是有价值的结论。")
    else:
        print(f"\n共找到 {found} 个 N>1 的实例")


if __name__ == '__main__':
    main()
