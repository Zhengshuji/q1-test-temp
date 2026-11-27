# -*- coding: utf-8 -*-
"""b2_shapes.py —— 打印 build_norm_T / W_J 的精确形状，搞清约定"""
import os, io, contextlib, random
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]

_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]; build_norm_T = _t["build_norm_T"]


def WJ_of(t, r, k, s, dC):
    W = [[Fr(1) if j == i else Fr(0) for j in range(dC)] for i in range(r)]
    idx = 0
    for i in range(k):
        row = [Fr(0)] * dC
        row[r + i] = Fr(1)
        for j in range(k, s):
            row[r + j] = t[idx]; idx += 1
        W.append(row)
    return W


def main():
    rng = random.Random(20260204)
    for _ in range(200000):
        Ac = [[Fr(rng.randint(-1, 1)) for _ in range(5)] for _ in range(5)]
        Cc = [[Fr(rng.randint(-1, 1)) for _ in range(5)]]
        Lc = [[Fr(rng.randint(-1, 1)) for _ in range(5)]]
        if rk(Cc) != 1 or rk(Lc) != 1 or rk(Lc + Cc) != 2: continue
        try: Lx, eta = p1(Ac, Cc, Lc)
        except Exception: continue
        if not Lx: continue
        q0 = sum(eta); k = q0 - 1
        if k != 1: continue
        bt = build_norm_T(Ac, Cc, Lc, Lx)
        if bt is None: continue
        dC, s, k2, r2, AT, BAT = bt
        if (r2, k2) != (1, 1) or s != 3: continue
        print("n=5 p=1 r=1 q0=%d k=%d  dC=%d s=%d" % (q0, k, dC, s))
        print("  AT (n×n?) :", len(AT), "×", len(AT[0]))
        print("  BAT(W×?) :", len(BAT), "×", len(BAT[0]), "   ← 应为 k×dC")
        W = WJ_of([Fr(0), Fr(0)], 1, 1, s, dC)
        print("  W_J(Θ)    :", len(W), "×", len(W[0]), "   ← 应为 (r+k)×dC")
        print("  W + BAT   :", len(W + BAT), "×", len((W + BAT)[0]))
        WA = mm(W, AT)
        print("  W·Ā      :", len(WA), "×", len(WA[0]))
        print("  [W;B]     :", len(W) + len(BAT), "×", dC)
        print("  [W;B;WĀ]  :", len(W) + len(BAT) + len(WA), "×", dC)
        print("  rk[W;B]   :", rk(W + BAT))
        print("  (A) 成立？", rk((W + BAT) + WA) == rk(W + BAT))
        return
    print("未找到")


if __name__ == "__main__":
    main()
