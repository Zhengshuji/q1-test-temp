r"""c293：基族扫描（A3 第一轮）——让 $S$ 动起来。

**检验的命题**：$\exists S\in\operatorname{Gr}(s,D)$ 使固定-$S$ 问题可行？
此前所有工作都固定在单个 $S$ 上（例如 $S=\operatorname{span}(e_3,e_4)$），**从未扫过基族**。

**实例**：第二实例（$n=6$、$p=1$）——$D=G=\operatorname{span}(e_3,e_4,e_5)$（$\dim3$），
这是唯一一个 $\mathcal B_{s,k}=\operatorname{Gr}(2,3)$（真的多点）的实例。

**扫描**：$q\in\{2,3\}$，$s=0..d$（$d=w-q$），枚举 $\operatorname{Gr}(s,3)$ 的全部格点（整数基，RREF 去重），
对每个 $S$ 调 `base_sweep.fixed_S`，记录候选 $U$ 数与可行数。

**用法**：python proof/layer_program/c293_base_sweep.py
**限制**（必读）：这是**有限格点**，结论标 `[精确验证 n/N]`，不能当"所有 $S$"的证明（CLAUDE §7.12）。
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import base_sweep as BS


def r_of(d, s):
    return d - s


def main():
    N = 6
    def unit(i):
        return [Fr(1) if k == i else Fr(0) for k in range(N)]

    C = [[Fr(0)] * N]
    C[0][0] = Fr(1)
    A = [[Fr(0)] * N for _ in range(N)]
    A[0][5] = Fr(1)   # Ae6 = e1
    A[2][2] = Fr(1)   # Ae3 = e3
    A[3][3] = Fr(1)   # Ae4 = e4
    A[1][1] = Fr(1)   # Ae2 = e2
    A[4][4] = Fr(1)   # Ae5 = e5
    L0 = [[Fr(0)] * N]
    L0[0][1] = Fr(1)  # L0 = e2

    geo = BS.geometry(A, C, L0)
    print("第二实例：n=6, p=1, v=%d, w=%d, h=%d, b=%d, dimD=%d"
          % (geo['v'], geo['w'], geo['h'], geo['b'], geo['dimD']))
    D = geo['D']
    print("D 的基:", [[str(x) for x in v] for v in D])

    for q in (3, 2):
        d = geo['w'] - q
        print(f"\n=== q={q}（d={d}）")
        for s in range(0, d + 1):
            if s > geo['dimD']:
                continue
            if r_of(d, s) > 1:
                print(f"  s={s}: r={r_of(d,s)} > 1，U 的枚举太贵，**跳过**（未覆盖）", flush=True)
                continue
            coords = BS.enum_subspaces(geo['dimD'], s, bound=1)
            uc = BS.enum_subspaces(geo['h'] - s, d - s, bound=1) if d > s else [[]]
            n_tested = 0
            n_feas = 0
            witness = None
            for coefs in coords:
                S = []
                for row in coefs:
                    v = [Fr(0)] * N
                    for j, c in enumerate(row):
                        for i in range(N):
                            v[i] += Fr(c) * D[j][i]
                    S.append(v)
                try:
                    out = BS.fixed_S(A, C, L0, geo, d, S, ucoeffs=uc)
                except AssertionError as e:
                    print(f"  s={s}: 断言失败 {e}")
                    continue
                n_tested += 1
                if out['ok']:
                    n_feas += 1
                    if witness is None:
                        witness = (S, out['feasible'][0])
            status = "有可行 S ✓" if n_feas else "全部不可行"
            print(f"  s={s}: 扫 {n_tested} 个 S，可行 {n_feas} 个 -> {status}", flush=True)
            if witness is not None:
                S, feas = witness
                print(f"       见证：S 基 = {[[str(x) for x in v] for v in S]}")
                print(f"             Z 基 = {[[str(x) for x in v] for v in feas['U']]}")
    print("\n（有限格点，结论范围 = 上述枚举；不能推断'所有 S'。）")


if __name__ == '__main__':
    main()
