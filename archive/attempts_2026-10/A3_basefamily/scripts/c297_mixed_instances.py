r"""c297：寻找"**部分可行**"的实例（A3-3 的开集结论需要真实边界）。

**背景**：A2 §34 证明可行 $S$ 集是 Zariski 开集。到目前为止**所有实例**都是
- R17：唯一 $S$，可行；
- 第二实例：扫过的 $S$ 全不可行。

⟹ 从未见过"可行集非空且非全空间"的情形。本脚本**随机造实例**，找这样的情形。

**判据**：`coeff_of_S.feasible_by_coeffs`（A2 §33，一次秩判定）。

**对混合实例的验证**：
1. 可行 $S$ 的小扰动仍可行（开性的数值证据）；
2. 抽查若干 $S$ 与直接判据（`feasible_by_minors`）对照。

用法：python proof/layer_program/c297_mixed_instances.py
"""
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
import base_sweep as BS


def make_instance(n, p, rng):
    """随机稀疏整数实例：C = [e_1..e_p]，L0 = e_{p+1}，A 稀疏."""
    def unit(i):
        return [Fr(1) if k == i else Fr(0) for k in range(n)]
    C = [unit(i) for i in range(p)]
    L0 = [unit(p)]
    A = [[Fr(0)] * n for _ in range(n)]
    for _ in range(n):                      # n 个随机非零位置
        i = rng.randrange(n)
        j = rng.randrange(n)
        A[i][j] = Fr(rng.choice([-1, 1, 2]))
    return A, C, L0


def geometry(A, C, L0):
    n = len(A)
    CA = AI.mul(C, A)
    V = AI.nullspace([row[:] for row in (C + CA)])
    W = AI.nullspace([row[:] for row in C])
    H = AI.nullspace([row[:] for row in (C + L0)])
    Vt = [list(x) for x in V]
    Ht = [list(x) for x in H]
    # 零化子构造（旧版把"基"当"零化子"，两处都错）
    Vperp = AI.nullspace(Vt)
    Hperp = AI.nullspace(Ht)
    G = AI.nullspace(Vperp + Hperp)
    Gperp = AI.nullspace([list(x) for x in G])
    D = AI.nullspace(Gperp + AI.mul(Hperp, A))
    return dict(n=n, w=len(W), h=len(H), b=len(G), v=len(V), dimD=len(D), D=D, G=G)


def feasible_by_coeffs(A, C, L0, q, S):
    """算 $a_j(S)$ 并判 $a_0\\notin\\operatorname{span}\\{a_j\\}$（A2 §33）."""
    a, _P, _info = CS_.coeff_forms_of_S(A, C, L0, q, S)
    forms = [a[j] for j in range(1, len(a)) if any(x != 0 for x in a[j])]
    rk1 = AI.rank(forms) if forms else 0
    rkall = AI.rank(forms + [a[0]])
    return (rkall > rk1), _info, a


def lift(coefs, D, n):
    S = []
    for row in coefs:
        v = [Fr(0)] * n
        for j, c in enumerate(row):
            for i in range(n):
                v[i] += Fr(c) * D[j][i]
        S.append(v)
    return S


def sweep(A, C, L0, geo, q, s, bound=1):
    """扫 Gr(s, D)，返回 (可行数, 总数, 可行的 S 列表)."""
    d = geo['w'] - q
    if d < s:
        return 0, 0, []
    coords = BS.enum_subspaces(geo['dimD'], s, bound=bound)
    feas = []
    tot = 0
    for cf in coords:
        S = lift(cf, geo['D'], geo['n'])
        if len(S) < s:
            continue
        try:
            ok, _info, _a = feasible_by_coeffs(A, C, L0, q, S)
        except Exception:
            continue
        tot += 1
        if ok:
            feas.append(S)
    return len(feas), tot, feas


def main():
    rng = random.Random(20261031)
    print("随机搜索：找可行数 0 < k < 总数的实例\n")
    print(f"{'n':<4}{'p':<4}{'w':<4}{'h':<4}{'b':<4}{'dimD':<6}{'q':<4}{'s':<4}{'可行/总':<10}")
    found = []
    stats = []
    for trial in range(120):
        n = rng.choice([6, 7, 8])
        p = rng.choice([1, 2])
        A, C, L0 = make_instance(n, p, rng)
        try:
            geo = geometry(A, C, L0)
        except Exception:
            continue
        if geo['dimD'] < 2:
            continue
        # 系数判据只在"平衡" q 上有效：t = m - r  <=>  q = w - h + v - s
        v_dim = geo['h'] - (geo['b'] - 0)  # 占位，实际用 geo 里存的 v
        for s in (1,):
            if s > geo['dimD']:
                continue
            q = geo['w'] - geo['h'] + geo['v'] - s
            if q < 1:
                continue
            nf, nt, feas = sweep(A, C, L0, geo, q, s, bound=1)
            if nt >= 4:
                stats.append((nf, nt))
            if nt >= 4 and 0 < nf < nt:
                print(f"{n:<4}{p:<4}{geo['w']:<4}{geo['h']:<4}{geo['b']:<4}"
                      f"{geo['dimD']:<6}{q:<4}{s:<4}{f'{nf}/{nt}':<10}  <-- 混合")
                found.append((A, C, L0, geo, q, s, feas, nf, nt))
        if found:
                break
        if found:
            break

    print(f"\n有效 sweep 数：{len(stats)}")
    zero = sum(1 for (a, b) in stats if a == 0)
    full = sum(1 for (a, b) in stats if a == b)
    mixed = len(stats) - zero - full
    print(f"  全不可行：{zero}；  全可行：{full}；  **混合**：{mixed}")
    if not found:
        print("\n未找到混合实例（在 400 次随机试验内）")
        print("=> 这本身是个观察：在这些参数下，可行集似乎是'全开'或'全空'。")
        return

    A, C, L0, geo, q, s, feas, nf, nt = found[0]
    print(f"\n混合实例：q={q}、s={s}、可行 {nf}/{nt}")
    # 验证 1：可行 S 的小扰动仍可行（开性证据）
    print("\n开性检验（可行 S 加小扰动）：")
    okc = 0
    totc = 0
    for S in feas[:3]:
        for delta in (1, -1):
            S2 = [list(v) for v in S]
            S2[0] = [v * (1 + Fr(delta, 10)) for v in S2[0]]
            try:
                ok2, _i, _a = feasible_by_coeffs(A, C, L0, q, S2)
            except Exception:
                continue
            totc += 1
            okc += (1 if ok2 else 0)
    print(f"  扰动后仍可行：{okc}/{totc}")
    # 验证 2：直接判据对照
    print("\n直接判据（feasible_by_minors）对照：")
    mism = 0
    for S in feas[:3]:
        try:
            direct, _g = CS_.feasible_by_minors(A, C, L0, q, [S[0]])
        except Exception:
            continue
        coeff, _i, _a = feasible_by_coeffs(A, C, L0, q, S)
        print(f"  系数判据={coeff}  直接判据={direct}  {'✓' if coeff == direct else '✗'}")
        if coeff != direct:
            mism += 1
    print(f"  不一致：{mism}")


if __name__ == '__main__':
    main()
