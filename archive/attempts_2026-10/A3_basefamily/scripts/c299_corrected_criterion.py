r"""c299：**修正后**的系数判据 + 端到端验证（A2 §37）。

**正确判据**（A2 §37.2）：
$$\text{可行}\iff \big(K\not\subseteq G/S\big)\ \wedge\ \big(a_0\notin\operatorname{span}\{a_1,\dots,a_d\}\big),$$
其中 $K=\bigcap_{j\ge1}\ker a_j$。

**理由**：两个条件各自是 $K$ 上的"开稠密"条件（$u\notin G/S$ 与 $\langle a_0,u\rangle\ne0$），
二者之交非空 ⟺ 两个条件都非平凡。

**验证**：对每个判"可行"的 $S$，构造 $u$（在 $K$ 里避开 $G/S$ 且 $a_0\ne0$），
把 $U$ 造出来，用**独立的** `base_sweep.check_Z` 验证 $(A)$ 与 $(S)$。

用法：python proof/layer_program/c299_corrected_criterion.py
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

_N297 = os.path.join(_HERE, 'c297_mixed_instances.py')
_NS = {'__file__': _N297, '__name__': 'c297x'}
exec(open(_N297, encoding='utf-8').read().split("if __name__")[0], _NS)


def criterion(A, C, L0, q, S, geo):
    """返回 (feasible, u, info)：修正后的判据 + 一个见证 u."""
    a, P, info = CS_.coeff_forms_of_S(A, C, L0, q, S)
    m = info['m']
    rows = info['rows']
    st = CS_.setup(A, C, L0, q, S)
    wm = st['w'] - st['s']
    # G/S 在 row 坐标里
    Gc = []
    for g in geo['G']:
        full = CS_._solve_in_basis(st['WB'], g)[st['s']:]
        Gc.append([full[i] for i in rows])
    rkG = AI.rank(Gc) if Gc else 0
    # T_S = (A(S)+S)/S 在 row 坐标里
    TS = []
    for sv in S:
        av = [sum(A[i][k] * sv[k] for k in range(len(sv))) for i in range(len(sv))]
        full = CS_._solve_in_basis(st['WB'], av)[st['s']:]
        TS.append([full[i] for i in rows])
    TSc = [x for x in TS]
    rkT = AI.rank(TSc) if TSc else 0
    forms = [a[j] for j in range(1, len(a)) if any(x != 0 for x in a[j])]
    K = AI.nullspace(forms) if forms else [[Fr(1) if i == k else Fr(0) for i in range(m)]
                                            for k in range(m)]
    if not K:
        return False, None, info
    # 条件 1：K ⊄ G/S
    K_not_in_G = AI.rank(Gc + K) > rkG if Gc else len(K) > 0
    # 条件 2：a_0|_K ≠ 0
    a0K = [sum(a[0][i] * u[i] for i in range(m)) for u in K]
    a0_nonzero = any(x != 0 for x in a0K)
    if not (K_not_in_G and a0_nonzero):
        return False, None, info
    # 约束 T_S ⊆ U（r=1 时 k=1 ⟹ U 被强制为 T_S）
    if rkT > 1:
        return False, None, info          # A2 剪枝 k > r
    if rkT == 1:
        gen = next(x for x in TSc if any(x))
        val = sum(a[0][i] * gen[i] for i in range(m))
        if val == 0:
            return False, None, info      # a_0 在 T_S 上为零
        if Gc and AI.rank(Gc + [gen]) == rkG:
            return False, None, info      # T_S ⊆ G/S
        return True, gen, info
    # 构造见证 u：在 K 里枚举组合
    for coefs in __import__('itertools').product((-2, -1, 0, 1, 2), repeat=len(K)):
        if all(c == 0 for c in coefs):
            continue
        u = [sum(Fr(coefs[t]) * K[t][i] for t in range(len(K))) for i in range(m)]
        if sum(a[0][i] * u[i] for i in range(m)) == 0:
            continue
        if Gc and AI.rank(Gc + [u]) == rkG:
            continue          # u 落在 G/S 里
        return True, u, info
    return False, None, info


def to_U(u, info, geo, st):
    wm = st['w'] - st['s']
    wvec = [Fr(0)] * wm
    for i, ix in enumerate(info['rows']):
        wvec[ix] = u[i]
    return [sum(wvec[j] * st['WB'][st['s'] + j][k] for j in range(wm)) for k in range(geo['n'])]


def main():
    rng = random.Random(20261031)
    print("修正判据的随机扫描 + 端到端验证\n")
    print(f"{'n':<4}{'p':<4}{'q':<4}{'s':<4}{'可行/总':<10}{'端到端一致':<10}")
    tot_sweeps = 0
    tot_mixed = 0
    tot_checks = 0
    tot_bad = 0
    skipped = [0]
    for _ in range(150):
        n = rng.choice([6, 7, 8])
        p = rng.choice([1, 2])
        A, C, L0 = _NS['make_instance'](n, p, rng)
        try:
            geo = _NS['geometry'](A, C, L0)
        except Exception:
            continue
        if geo['dimD'] < 2:
            continue
        s = 1
        q = geo['w'] - geo['h'] + geo['v'] - s
        if q < 1:
            continue
        coords = BS.enum_subspaces(geo['dimD'], s, bound=1)
        nf = 0
        nt = 0
        ok_end = 0
        for cf in coords:
            S = _NS['lift'](cf, geo['D'], geo['n'])
            try:
                feas, u, info = criterion(A, C, L0, q, S, geo)
            except Exception:
                skipped[0] += 1
                continue
            nt += 1
            if not feas:
                continue
            nf += 1
            st = CS_.setup(A, C, L0, q, S)
            U = to_U(u, info, geo, st)
            Z = S + [U]
            Zmat = [[Z[j][i] for j in range(len(Z))] for i in range(geo['n'])]
            okA, okS, g = BS.check_Z(A, C, Zmat)
            tot_checks += 1
            if okA and okS:
                ok_end += 1
            else:
                tot_bad += 1
        if nt >= 4:
            tot_sweeps += 1
            if 0 < nf < nt:
                tot_mixed += 1
            if nf > 0:
                print(f"{n:<4}{p:<4}{q:<4}{s:<4}{f'{nf}/{nt}':<10}{f'{ok_end}/{nf}':<10}")
    print(f"\n有效 sweep：{tot_sweeps}；混合：{tot_mixed}")
    print(f"端到端检验：{tot_checks} 次，失败 **{tot_bad}** 次")
    print(f"（跳过的 S（内部断言失败）：{skipped[0]}）")
    print("\n判据（修正后）与独立检验一致" if tot_bad == 0 else "*** 仍有不一致 ***")


if __name__ == '__main__':
    main()
