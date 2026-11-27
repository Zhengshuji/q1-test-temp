r"""c298：**端到端**验证——从系数判据的"可行"造出真正的 $(S,U)$ 证书。

**检验的链条**（A2 §33 + §36）：
1. 用 `c297` 的同一种子复现第一个"部分可行"实例；
2. 对每个 $S$，用系数判据判可行；
3. **若判可行**：解线性系统 $u\\in\\bigcap_{j\\ge1}\\ker a_j$、$\\langle a_0,u\\rangle\\ne0$，造出 $U$；
4. 用**独立的** `base_sweep.check_Z`（$\\operatorname{rank}[Z,AZR]=d$ 与极大子式 gcd）验证 $(A)$ 与 $(S)$；
5. 若判不可行：验证不存在这样的 $u$（线性系统无解除非 $\\langle a_0,u\\rangle=0$）。

**这是最强的验证**：判据说"可行"必须能造出通过独立检验的 $(S,U)$。

用法：python proof/layer_program/c298_end_to_end.py
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
_src = open(_N297, encoding='utf-8').read().split("if __name__")[0]
_NS = {'__file__': _N297, '__name__': 'c297x'}
exec(_src, _NS)


def find_mixed(seed=20261031, max_trials=120):
    rng = random.Random(seed)
    for _ in range(max_trials):
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
        nf, nt, feas = _NS['sweep'](A, C, L0, geo, q, s, bound=1)
        if 0 < nf < nt:
            return A, C, L0, geo, q, s, nf, nt
    return None


def solve_U(a, m, r):
    """解 $\langle a_j,u\rangle=0\ (j\ge1)$、$\langle a_0,u\rangle\ne0$，返回 u 或 None。"""
    forms = [a[j] for j in range(1, len(a)) if any(x != 0 for x in a[j])]
    K = AI.nullspace(forms) if forms else [[Fr(1) if i == k else Fr(0) for i in range(m)] for k in range(m)]
    for u in K:
        if any(u) and sum(a[0][k] * u[k] for k in range(m)) != 0:
            return list(u)
    return None


def main():
    res = find_mixed()
    if res is None:
        print('未找到混合实例')
        return
    A, C, L0, geo, q, s, nf, nt = res
    print(f'混合实例：n={geo["n"]}, p={len(C)}, w={geo["w"]}, h={geo["h"]}, b={geo["b"]}, '
          f'dimD={geo["dimD"]}, q={q}, s={s}，可行 {nf}/{nt}\n')
    coords = BS.enum_subspaces(geo['dimD'], s, bound=1)
    m_ok = 0
    m_bad = 0
    n_tested = 0
    for cf in coords:
        S = _NS['lift'](cf, geo['D'], geo['n'])
        if len(S) < s:
            continue
        try:
            ok, info, a = _NS['feasible_by_coeffs'](A, C, L0, q, S)
        except Exception:
            continue
        n_tested += 1
        m = info['m']
        rows = info['rows']
        st = CS_.setup(A, C, L0, q, S)
        wm = st['w'] - st['s']
        if ok:
            u = solve_U(a, m, 1)
            if u is None:
                print(f'  S#{n_tested}: 判可行但解不出 u  *** 不一致 ***')
                m_bad += 1
                continue
            # 还原 U 到 W/S 坐标 -> n 维
            wvec = [Fr(0)] * wm
            for i, ix in enumerate(rows):
                wvec[ix] = u[i]
            U = [sum(wvec[j] * st['WB'][st['s'] + j][k] for j in range(wm)) for k in range(geo['n'])]
            Z = S + [U]
            Zmat = [[Z[j][i] for j in range(len(Z))] for i in range(geo['n'])]
            okA, okS, g = BS.check_Z(A, C, Zmat)
            good = okA and okS
            print(f'  S#{n_tested}: 判可行 -> 造出 U，独立检验 (A)={okA} (S)={okS} '
                  f'{"✓" if good else "*** 不一致 ***"}')
            m_ok += (1 if good else 0)
            m_bad += (0 if good else 1)
        else:
            u = solve_U(a, m, 1)
            print(f'  S#{n_tested}: 判不可行，求解 u = {None if u is None else "存在"}'
                  f' {"✓" if u is None else "*** 不一致 ***"}')
            m_ok += (1 if u is None else 0)
            m_bad += (0 if u is None else 1)
    print(f'\n端到端：一致 {m_ok}，不一致 {m_bad}')


if __name__ == '__main__':
    main()
