r"""B-4：可行 $S$ 集的**开性**——用**可信的直接判据**重做扫描（分支 2）。

**背景**：B-3 证明可行 $S$ 集是构造集（Chevalley），不必然开。B-4 的充分条件是
$\pi|_{\mathcal Y}$ **局部等维**；等价地：可行 $S$ 的小扰动仍可行。

**关键**：此前的随机扫描用的是**已撤回的系数判据**（A2 §38），结论作废。
本脚本改用**可信的直接判据** `base_sweep.fixed_S`（枚举可容许 $U$ + `check_Z` 的 $(A)(S)$）。

**做法**：
1. 随机小实例（$r=1$，$m$ 小）；
2. 扫 $S\\in\\operatorname{Gr}(s,D)$，用 `fixed_S` 判可行；
3. 记混合实例（$0<k<$ 总数）；
4. 对可行 $S$ 做**扰动**（$S\\to S+\\varepsilon\\cdot$随机向量），看是否仍可行 —— 开性的数值证据。

用法：python workspace/B_bezout/scripts/b4_openness.py
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
import base_sweep as BS
import coeff_of_S as CS_


def make_instance(n, p, rng):
    def unit(i):
        return [Fr(1) if k == i else Fr(0) for k in range(n)]
    C = [unit(i) for i in range(p)]
    L0 = [unit(p)]
    A = [[Fr(0)] * n for _ in range(n)]
    for _ in range(n):
        A[rng.randrange(n)][rng.randrange(n)] = Fr(rng.choice([-1, 1, 2]))
    return A, C, L0


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
    print("B-4：用可信判据扫 S，找混合实例并检验开性\n")
    print(f"{'n':<4}{'p':<4}{'q':<4}{'s':<4}{'可行/总':<10}{'扰动后仍可行':<14}")
    sweeps = 0
    mixed = 0
    perturb_ok = 0
    perturb_tot = 0
    for _ in range(15):
        n = rng.choice([6, 7, 8])
        p = rng.choice([1, 2])
        A, C, L0 = make_instance(n, p, rng)
        try:
            geo = BS.geometry(A, C, L0)
        except Exception:
            continue
        if geo['dimD'] < 2:
            continue
        for s in (1,):
            if s > geo['dimD']:
                continue
            for q in (geo['w'] - 2,):
                if q < 1:
                    continue
                d = geo['w'] - q
                if d < s:
                    continue
                r = d - s
                if r > 1:                # U 的枚举太贵
                    continue
                coords = BS.enum_subspaces(geo['dimD'], s, bound=1)
                uc = BS.enum_subspaces(geo['h'] - s, r, bound=1) if r > 0 else [[]]
                nf = 0
                nt = 0
                feas = []
                for cf in coords:
                    S = lift(cf, geo['D'], n)
                    if len(S) < s:
                        continue
                    try:
                        out = BS.fixed_S(A, C, L0, geo, d, S, ucoeffs=uc)
                    except Exception:
                        continue
                    nt += 1
                    if out['ok']:
                        nf += 1
                        feas.append(S)
                if nt < 4:
                    continue
                sweeps += 1
                is_mixed = 0 < nf < nt
                if is_mixed:
                    mixed += 1
                # 开性：对前两个可行 S 扰动
                pok = 0
                ptot = 0
                for S in feas[:2]:
                    for eps in (Fr(1, 10), Fr(-1, 10)):
                        S2 = [list(v) for v in S]
                        S2[0] = [x + eps for x in S2[0]]
                        try:
                            o2 = BS.fixed_S(A, C, L0, geo, d, S2, ucoeffs=uc)
                        except Exception:
                            continue
                        ptot += 1
                        pok += (1 if o2['ok'] else 0)
                perturb_ok += pok
                perturb_tot += ptot
                print(f"  sweep n={n} p={p} q={q} s={s}: {nf}/{nt} 可行, 扰动 {pok}/{ptot}", flush=True)
    print(f"\n有效 sweep：{sweeps}；混合：**{mixed}**")
    print(f"扰动检验：{perturb_ok}/{perturb_tot} 仍可行")
    if mixed == 0:
        print("\n在可信判据下**没有**混合实例 ⟹ 可行集在已测范围内总是'全可行'或'全不可行'，")
        print("这与'开集'一致（开集要么空要么稠密）。")


if __name__ == '__main__':
    main()
