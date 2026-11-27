r"""c300：A-5 —— $D(K_S)$ 与 $K_S$ 的比较（G3 是否自动成立）。

**问题**（QA25 的中心问题）：
$$D_{\mathrm{adm}}(K_S):=\operatorname{span}\{p_U:\ U\in\operatorname{Gr}(r,E),\ T_S\subseteq U,\ U\cap (G/S)=0,\ p_U\in K_S\}$$
与 $K_S$ 的关系？若 $D_{\mathrm{adm}}(K_S)\subsetneq K_S$，则**线性判据会有假阳性**（G3 障碍真实存在）。

**做法**：
1. 随机实例里找 $h-v\ge 2$（这样 $r=2$ 才可能 $r+t\le m$）；
2. 对给定 $S$：算 $a_j$（`coeff_of_S`），$K_S=\bigcap_{j\ge1}\ker a_j$；
3. 枚举可容许 $U\in\operatorname{Gr}(2,E)$（$T_S\subseteq U$、$U\cap G/S=0$），过滤 $p_U\in K_S$；
4. 算这些 $p_U$ 的秩 = $\dim D_{\mathrm{adm}}$，与 $\dim K_S$ 比较。

**结论类型**：
- 若处处 $\dim D=\dim K_S$ ⟹ G3 无障碍（在这些实例上）；
- 若某处 $\dim D<\dim K_S$ ⟹ **反例**（G3 真实存在）。

用法：python workspace/A3_basefamily/scripts/c300_g3_check.py
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
import base_sweep as BS


def geometry(A, C, L0):
    n = len(A)
    CA = AI.mul(C, A)
    V = AI.nullspace([row[:] for row in (C + CA)])
    W = AI.nullspace([row[:] for row in C])
    H = AI.nullspace([row[:] for row in (C + L0)])
    Vt = [list(x) for x in V]
    Ht = [list(x) for x in H]
    Vperp = AI.nullspace(Vt)
    Hperp = AI.nullspace(Ht)
    G = AI.nullspace(Vperp + Hperp)
    Gperp = AI.nullspace([list(x) for x in G])
    D = AI.nullspace(Gperp + AI.mul(Hperp, A))
    return dict(n=n, w=len(W), h=len(H), v=len(V), b=len(G), dimD=len(D),
                V=V, H=H, G=G, D=D)


def minor_det(M):
    n = len(M)
    if n == 0:
        return Fr(1)
    M = [row[:] for row in M]
    d = Fr(1)
    for i in range(n):
        p = next((r for r in range(i, n) if M[r][i] != 0), None)
        if p is None:
            return Fr(0)
        if p != i:
            M[i], M[p] = M[p], M[i]
            d = -d
        d *= M[i][i]
        inv = Fr(1) / M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] * inv
            for c in range(i, n):
                M[r][c] -= f * M[i][c]
    return d


def plucker_coords(U, m):
    """U: r 个向量（长度 m）。返回 Plücker 坐标（按 r-子集排序）."""
    r = len(U)
    return [minor_det([[U[j][i] for j in range(r)] for i in I])
            for I in itertools.combinations(range(m), r)]


def main():
    rng = random.Random(20261101)
    print("A-5：D_adm(K_S) vs K_S（G3 是否自动成立）\n")
    found = 0
    stats = {"DK": 0, "eq": 0, "fp": 0}
    for trial in range(1200):
        n = rng.choice([7, 8, 9])
        p = rng.choice([2, 3])
        def unit(i):
            return [Fr(1) if k == i else Fr(0) for k in range(n)]
        C = [unit(i) for i in range(p)]
        L0 = [unit(p)]
        A = [[Fr(0)] * n for _ in range(n)]
        for _ in range(n):
            i = rng.randrange(n); j = rng.randrange(n)
            A[i][j] = Fr(rng.choice([-1, 1, 2]))
        try:
            geo = geometry(A, C, L0)
        except Exception:
            continue
        if geo['h'] - geo['v'] < 2:
            continue
        # 取 s = 1、r = 2 ⟹ d = 3 ⟹ q = w - 3
        s, r = 1, 2
        d = s + r
        q = geo['w'] - d
        if q < 1 or geo['dimD'] < s:
            continue
        coords = BS.enum_subspaces(geo['dimD'], s, bound=1)[:3]
        if not coords:
            continue
        for cf in coords:
            S = []
            for row in cf:
                v = [Fr(0)] * n
                for j, c in enumerate(row):
                    for i in range(n):
                        v[i] += Fr(c) * geo['D'][j][i]
                S.append(v)
            try:
                st0 = CS_.setup(A, C, L0, q, S)
            except AssertionError:
                continue
            r0 = st0['d'] - st0['s']
            m = st0['m']
            if m != r0 + st0['t']:
                # 域外：m 行截断对象只在 m=r+t 时良定义；q=t 的方阵域请用 c301
                continue
            try:
                a, P, info = CS_.coeff_forms_balanced(A, C, L0, q, S)
            except Exception:
                continue
            if info['m'] < r + info['t']:
                continue
            # K_S = ∩ ker{a_j}_{j>=1}
            forms = [a[j] for j in range(1, len(a)) if any(x != 0 for x in a[j])]
            Kmat = forms
            dimK = len(a[0]) - (AI.rank(Kmat) if Kmat else 0)
            # T_S 与 G/S 在 row 坐标里
            rows = info['rows']
            st = CS_.setup(A, C, L0, q, S)
            wm = st['w'] - st['s']
            TSc = []
            for sv in S:
                av = [sum(A[i2][k] * sv[k] for k in range(n)) for i2 in range(n)]
                full = CS_._solve_in_basis(st['WB'], av)[st['s']:]
                TSc.append([full[i2] for i2 in rows])
            rkT = AI.rank(TSc) if TSc else 0
            Gc = []
            for g in geo['G']:
                full = CS_._solve_in_basis(st['WB'], g)[st['s']:]
                Gc.append([full[i2] for i2 in rows])
            rkG = AI.rank(Gc) if Gc else 0
            # 枚举**可容许** U ∈ Gr(r, E)
            pts = []
            seen = set()
            for basis in BS.enum_subspaces(m, r, bound=1):
                U = []
                for row in basis:
                    U.append([Fr(c) for c in row])
                if AI.rank(U) != r:
                    continue
                key = BS.rref_canonical(U, m)
                if key in seen:
                    continue
                seen.add(key)
                # admissibility：T_S ⊆ U、U ∩ G/S = 0
                if rkT and AI.rank(U + TSc) > r:
                    continue
                if rkG and AI.rank(Gc + U) != rkG + r:
                    continue
                pU = plucker_coords(U, m)
                if all(x == 0 for x in pU):
                    continue
                if Kmat and any(sum(Kmat[t][k] * pU[k] for k in range(len(pU))) != 0
                                for t in range(len(Kmat))):
                    continue     # 不在 K_S 里
                pts.append(pU)
            dimD_adm = AI.rank(pts) if pts else 0
            found += 1
            # 线性判据 vs 真判据
            lin = (AI.rank(Kmat + [a[0]]) > (AI.rank(Kmat) if Kmat else 0))
            true_ok = any(sum(a[0][k] * pU[k] for k in range(len(pU))) != 0 for pU in pts)
            flag = "**D < K**（G3 障碍！）" if dimD_adm < dimK else ("D = K" if dimK else "K=0")
            if lin != true_ok:
                flag += f"  <<< 假阳性：线性判据={lin}，真判据={true_ok}"
            if lin != true_ok:
                print(f"**假阳性** trial{trial}: n={n} p={p} w={geo['w']} h={geo['h']} v={geo['v']} "
                      f"q={q} dimK={dimK} dimD_adm={dimD_adm} lin={lin} true={true_ok}")
            if dimD_adm < dimK:
                stats['DK'] += 1
            elif dimK:
                stats['eq'] += 1
            if lin != true_ok:
                stats['fp'] += 1
                print(f"  >>> 假阳性：trial{trial} n={n} p={p} q={q} dimK={dimK} dimD={dimD_adm} lin={lin} true={true_ok}")
            if found >= 120:
                print(f"\n统计：D<K {stats['DK']} 个，D=K {stats['eq']} 个，假阳性 {stats['fp']} 个")
                return
    print(f"\n共检查 {found} 个 (实例,S)")


if __name__ == '__main__':
    main()
