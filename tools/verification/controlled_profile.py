"""controlled_profile.py —— 专家 2026-11-05 §4.2/§3.4 的**控制变量实验**

固定 $A$（对角、谱互异）、固定 $L_0$、固定 $n,p,r$，只改 $C$ 的**支撑**，从而只改可观测指标的后段：

* $C_{33}$：两行分别支撑在 $\\{1,2,3\\}$ 与 $\\{4,5,6\\}$ ⟹ 指标 $(3,3)$ ⟹ $\\Delta=(2,2)$；
* $C_{42}$：两行分别支撑在 $\\{1,2,3,4\\}$ 与 $\\{5,6\\}$ ⟹ 指标 $(4,2)$ ⟹ $\\Delta=(2,1,1)$。

两者都有 $n=6$、$p=2$、$r_1=4$、$\\rho=2$。分别测：

$$q_{\\rm geom}=\\min\\{q:\\ \\text{存在可容许的中间层 }(1\\le\\delta<\\rho)\\text{ 候选}\\},$$
$$q_{\\rm spec}=\\min\\{q:\\ \\text{存在可容许的中间层候选且 }(5b)\\text{ 成立}\\},$$
并记录 $q_{\\min}$ 与 $q_0$。

用法：python -u tools/verification/controlled_profile.py
"""

import os
import sys
import itertools
from fractions import Fraction
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import decide_symbolic as DS              # noqa: E402
import observability_test as OT           # noqa: E402

F = Fraction
N = 6
A = [[F(0) for _ in range(N)] for _ in range(N)]
for i in range(N):
    A[i][i] = F(i + 1)                    # 谱 = {1,...,6}，互异
L0 = [[F(1), F(2), F(-1), F(3), F(1), F(-2)],
      [F(2), F(-1), F(1), F(1), F(-2), F(3)]]


def make_C(support1):
    """两行：第一行支撑在前 support1 个坐标，第二行支撑在其余坐标。"""
    row1 = [F(1) if i < support1 else F(0) for i in range(N)]
    row2 = [F(0) if i < support1 else F(1) for i in range(N)]
    return [row1, row2]


def profile(A_, C_, n, p):
    rk = []
    stacked = [list(x) for x in C_]
    prev = LQ.rank(stacked)
    out = []
    Ak = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for k in range(1, n + 1):
        Ak = LQ.mul(Ak, A_)
        stacked = stacked + [list(x) for x in LQ.mul(C_, Ak)]
        r = LQ.rank(stacked)
        out.append(r - prev)
        prev = r
        if r == n:
            break
    return tuple(out)


def scan(A_, C_, L0_, rng_seed=7):
    import random
    rng = random.Random(rng_seed)
    n, p, r = len(A_), len(C_), len(L0_)
    CA = LQ.mul(C_, A_)
    r1 = LQ.rank([list(x) for x in CA] + [list(x) for x in C_])
    rho = r1 - p
    K = ZG.ker_cols([list(x) for x in C_] + [list(x) for x in L0_])
    if not (K and K[0]):
        return None
    k = len(K[0])
    q0 = Q0.eta_and_q0(A_, C_, L0_)[0]
    q_geom = q_spec = q_min = None
    for q in range(q0, n - p + 1):
        d = n - p - q
        if d < 0 or d > k:
            continue
        cands = []
        if d == 0:
            need = n - p - r
            for _ in range(200):
                extra = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(need)]
                Lc = [list(x) for x in L0_] + extra
                if LQ.rank([list(x) for x in C_] + Lc) != n:
                    continue
                cands.append(Lc)
                break
        else:
            for rows in itertools.combinations(range(k), d):
                Z = DS.Z_from_theta(A_, C_, L0_, q, rows, [F(0)] * (d * (k - d)))
                if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                    continue
                try:
                    Lc = ZG.L_from_Z(A_, C_, L0_, Z, q)
                except AssertionError:
                    continue
                if Lc is not None:
                    cands.append(Lc)
        for Lc in cands:
            if not LQ.condA(A_, C_, Lc):
                continue
            h = LQ.rank([list(x) for x in Lc] + [list(x) for x in CA] + [list(x) for x in C_])
            Vd = LQ.rank([list(x) for x in Lc] + [list(x) for x in C_])
            delta = h - Vd
            # q_geom 只统计**次终端**的中间层候选（终阶另列），避免 rho=1 时把终阶误记为 q_geom
            sub_terminal = (q + p < n)
            intermediate = sub_terminal and (1 <= delta < rho)
            if intermediate and q_geom is None:
                q_geom = q
            V = ZG.ker_cols([list(x) for x in C_] + [list(x) for x in CA])
            ok = True if not (V and V[0]) else bool(OT.observability_ok(A_, C_, Lc)[0])
            if ok:
                if intermediate and q_spec is None:
                    q_spec = q
                if q_min is None:
                    q_min = q
    return dict(q0=q0, q_geom=q_geom, q_spec=q_spec, q_min=q_min, rho=rho, r1=r1)


def main():
    for sup, name in ((3, 'C_{33}'), (4, 'C_{42}'), (2, 'C_{24}'), (5, 'C_{51}')):
        C = make_C(sup)
        prof = profile(A, C, N, 2)
        res = scan(A, C, L0)
        print(f'{name}: 支撑=({sup},{N-sup})，Δ 剖面={prof}，' +
              (f'q0={res["q0"]}，r1={res["r1"]}，ρ={res["rho"]}，'
               f'q_geom={res["q_geom"] if res["q_geom"] is not None else "∞（无中间层）"}，'
               f'q_spec={res["q_spec"] if res["q_spec"] is not None else "∞"}，q_min={res["q_min"]}' if res else '扫描失败'))


if __name__ == '__main__':
    main()
