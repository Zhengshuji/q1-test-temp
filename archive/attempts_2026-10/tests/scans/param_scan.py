"""param_scan.py — 对紧性引理的对抗性检验（Q1-FALSE 方向）

用法
----
    python q1_false/tests/param_scan.py --seed certificate_middle_layer.json
    python q1_false/tests/param_scan.py --seed certificate_rhostar_lt_dimV.json --grid=-2,-1,0,1,2 --trials 40

注意：--grid 必须用 `=` 形式，否则 argparse 会把 `-2,...` 当成选项。

做什么
------
以 lit/ 里的中间层证书为种子，做 A(t) = A0 + t*E（E 固定随机 ±1 矩阵）的平变，
对每个有理 t 用**精确审计**（c166）算 (rho0, dimV, rho*, q(rho*))，
找 rho0 < rho* < dimV 且 q(rho*) > rho*+1 的候选。

判据与验收见 PROTOCOL.md（同目录）：**"搜不到"不算反例**，本脚本只产出 candidate。

输出
----
q1_false/tests/results/scan_<seed>_<tag>.json
"""
import sys
import os
import json
import random
import argparse
import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools", "exact_linalg"))

from fractions import Fraction as Fr
import c166_layer_audit as LA


def load_seed(name):
    path = name if os.path.isabs(name) else os.path.join(ROOT, "lit", name)
    d = json.load(open(path, encoding="utf-8"))
    toF = lambda m: [[Fr(x) for x in row] for row in m]
    return toF(d["A"]), toF(d["C"]), toF(d["L0"])


def perturb(M, E, t):
    return [[M[i][j] + t * E[i][j] for j in range(len(M[i]))] for i in range(len(M))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", default="certificate_middle_layer.json")
    ap.add_argument("--grid", default="-2,-1,0,1,2")
    ap.add_argument("--trials", type=int, default=40)
    ap.add_argument("--seed-noise", type=int, default=0)
    args = ap.parse_args()

    A0, C0, L00 = load_seed(args.seed)
    n = len(A0)
    rng = random.Random(args.seed_noise)

    # 固定扰动方向（±1），保证可复现
    E = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]

    grid = [Fr(s) for s in args.grid.split(",")]
    print(f"seed = {args.seed}  n={n}  grid={[str(t) for t in grid]}")

    rows = []
    for t in grid:
        A = perturb(A0, E, t)
        name = f"{os.path.basename(args.seed)[:-5]}_t{t}"
        try:
            rec = LA.audit_instance(name, A, C0, L00, random.Random(12345),
                                    args.trials, verbose=True)
        except Exception as e:
            print(f"{name}: ERR {type(e).__name__}: {e}")
            continue
        rec["t"] = str(t)
        rec["seed"] = args.seed
        rows.append(rec)

    # 打印值得注意的行
    print("\n" + "=" * 70)
    interesting = []
    for r in rows:
        dv, r0, rs = r.get("dimV"), r.get("rho0"), r.get("rhostar")
        if dv is None or rs is None:
            continue
        mid = (r0 is not None and r0 < rs < dv)
        loose = r.get("failures")
        if mid or loose:
            interesting.append(r)
            print(f"  注意: {r['name']} rho0={r0} dimV={dv} rho*={rs} "
                  f"q={r['reachable'].get(rs)} failures={len(loose)}")

    tag = datetime.datetime.now().strftime("%H%M%S")
    outdir = os.path.join(ROOT, "q1_false", "tests", "results")
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, f"scan_{os.path.basename(args.seed)[:-5]}_{tag}.json")
    with open(outpath, "w", encoding="utf-8") as fh:
        json.dump(rows, fh, ensure_ascii=False, indent=1)
    print(f"已保存 {outpath}（{len(rows)} 行）")


if __name__ == "__main__":
    main()
