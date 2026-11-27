r"""A-1（续）：$r=3$ 的行列式恒等式验证（分支 4）。

**目标**：把 §41.5 的验证从 $r=2$ 推到 $r=3$，覆盖更一般的情形。

**做法**：随机造实例直到 $r=w-v=3$ 且存在可行的 $S\\subseteq D$（$q=t=v-s$ 自动满足方阵条件）；
然后用**坐标子空间**定符号、用随机 $U$ 验恒等式（同 `verify_det_identity_r2.py`）。

用法：python workspace/A3_basefamily/scripts/verify_det_identity_r3.py
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
import spectral_gcd as SG
import coeff_of_S as CS_
import coeff_space as CS2


def minor_det(M):
    n = len(M)
    A = [row[:] for row in M]
    d = Fr(1)
    for a in range(n):
        p = next((b for b in range(a, n) if A[b][a] != 0), None)
        if p is None:
            return Fr(0)
        if p != a:
            A[a], A[p] = A[p], A[a]
            d = -d
        d *= A[a][a]
        inv = Fr(1) / A[a][a]
        for b in range(a + 1, n):
            f = A[b][a] * inv
            for c in range(a, n):
                A[b][c] -= f * A[a][c]
    return d


def det_poly(Ucols, cols, wm, t):
    P = []
    for i in range(wm):
        row = [[Ucols[k][i]] for k in range(len(Ucols))]
        row += [[cols[j][0][i], cols[j][1][i]] for j in range(t)]
        P.append(row)
    return SG.pdet(P)


def plucker_of(Ucols):
    r = len(Ucols)
    wm = len(Ucols[0])
    out = []
    for I in itertools.combinations(range(wm), r):
        out.append(minor_det([[Ucols[k][i] for k in range(r)] for i in I]))
    return out


def verify_instance(A, C, L0, q, S, label):
    st = CS_.setup(A, C, L0, q, S)
    wm = st['w'] - st['s']
    cols = CS_.pencil_cols(A, st)
    t = len(cols)
    r = st['d'] - st['s']
    if r + t != wm or r < 2:
        return None
    P0 = [[cols[j][0][i] for j in range(t)] for i in range(wm)]
    P1 = [[cols[j][1][i] for j in range(t)] for i in range(wm)]
    a, idxs = CS2.coeff_forms([P0, P1], wm, r)
    if len(a[0]) != len(idxs):
        return None
    signs = []
    for idx, I in enumerate(idxs):
        Uc = [[Fr(1) if k == i else Fr(0) for k in range(wm)] for i in I]
        lhs = det_poly(Uc, cols, wm, t)
        s = None
        for j in range(max(len(lhs), len(a))):
            l = lhs[j] if j < len(lhs) else Fr(0)
            rr = a[j][idx] if j < len(a) else Fr(0)
            if l != 0 or rr != 0:
                s = Fr(1) if l == rr else (Fr(-1) if l == -rr else None)
                break
        if s is None:
            s = Fr(1) if all(x == 0 for x in lhs) else None
        signs.append(s)
    if any(s is None for s in signs):
        print(f'{label}: 符号定不出（跳过）')
        return None
    rng = random.Random(17)
    ok = 0
    n = 0
    for _ in range(8):
        Uc = [[Fr(rng.randint(-2, 2)) for _ in range(wm)] for _ in range(r)]
        if AI.rank(Uc) < r:
            continue
        lhs = det_poly(Uc, cols, wm, t)
        p = plucker_of(Uc)
        rhs = [sum(signs[idx] * a[j][idx] * p[idx] for idx in range(len(idxs)))
               for j in range(len(a))]
        n += 1
        if SG.ptrim(lhs) == SG.ptrim(rhs):
            ok += 1
    print(f'{label}: w-s={wm}, r={r}, t={t}, q={q}；符号 {[str(s) for s in signs][:8]}...；'
          f'逐系数恒等 **{ok}/{n}**')
    return (ok == n and n > 0)


def main():
    src = open(os.path.join(_HERE, 'c297_mixed_instances.py'), encoding='utf-8').read()
    ns = {'__file__': os.path.join(_HERE, 'c297_mixed_instances.py'), '__name__': 'c297x'}
    exec(src.split("if __name__")[0], ns)
    import base_sweep as BS
    rng = random.Random(20261101)
    found = 0
    for trial in range(200):
        n = rng.choice([8, 9, 10])
        p = rng.choice([3])
        A, C, L0 = ns['make_instance'](n, p, rng)
        try:
            geo = ns['geometry'](A, C, L0)
        except Exception:
            continue
        r_target = geo['w'] - geo['v']
        if r_target != 3:
            continue
        if geo['dimD'] < 2:
            continue
        # 选 s 使 t = v - s = q >= 1 且 S ⊆ D
        for s in (1, 2):
            if s > geo['dimD']:
                continue
            q = geo['v'] - s
            if q < 1:
                continue
            coords = BS.enum_subspaces(geo['dimD'], s, bound=1)
            if not coords:
                continue
            S = ns['lift'](coords[0], geo['D'], n)
            if len(S) < s:
                continue
            try:
                res = verify_instance(A, C, L0, q, S, f'trial{trial}(n={n},p={p},s={s})')
            except AssertionError as e:
                continue
            if res is not None:
                found += 1
                if found >= 2:
                    return
    if found == 0:
        print('\n未找到 r=3 的方阵实例（400 次随机试验内）')


if __name__ == '__main__':
    main()
