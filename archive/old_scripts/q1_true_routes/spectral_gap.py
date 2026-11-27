"""spectral_gap.py — D1 统计：代数部分 vs 谱条件，砍了多少维？

对每个实例（来自 record/layer_audit_seed*.json 与 lit/ 证书）计算：
  n, p, r
  dim E, dim(E cap K), E cap K 是否可行（代数部分达到最优）
  q_min（审计值）, d_true = n-p-q_min
  cut = dim E - d_true        （谱条件砍掉的维数，若代数上界 = dim E）

判据：若 "E cap K 可行"，则 d_alg = dim E，于是
  q_min = r + (dim E - d_true) = r + cut。

用法：
    python q1_true/scripts/spectral_gap.py
"""
import sys
import os
import json
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "scripts", "core"))

from fractions import Fraction as Fr
import audit_independent as AI

mul, rank = AI.mul, AI.rank


def dimv(vs):
    return len(AI.row_basis(vs))


def toF(m):
    return [[Fr(x) for x in row] for row in m]


def load_instances():
    out = []
    for path in sorted(glob.glob(os.path.join(ROOT, "record", "layer_audit_seed*.json"))):
        for rec in json.load(open(path, encoding="utf-8")):
            if rec.get("qmin") is None or "A" not in rec:
                continue
            out.append((rec["name"], toF(rec["A"]), toF(rec["C"]), toF(rec["L0"]), rec["qmin"]))
    # 证书（已知 q_min）
    certs = [("refute_dimV1", "counterexample_refute_dimV1.json", 1),
             ("middle_layer", "certificate_middle_layer.json", 2),
             ("rhostar_lt_dimV", "certificate_rhostar_lt_dimV.json", 2)]
    for name, fn, q in certs:
        p = os.path.join(ROOT, "lit", fn)
        if os.path.exists(p):
            d = json.load(open(p, encoding="utf-8"))
            out.append((name, toF(d["A"]), toF(d["C"]), toF(d["L0"]), q))
    return out


def feasible_L(L, A, E, K, n):
    """L (list of vectors) 是否满足：A(L) ⊆ E 且 A(L)∩K ⊆ L"""
    if not L:
        return True
    Lmat = [[L[j][i] for j in range(len(L))] for i in range(n)]
    AL = mul(A, Lmat)
    ALrows = [[AL[i][j] for i in range(n)] for j in range(len(L))]
    if dimv(ALrows + E) != dimv(E):
        return False
    inter = dimv(ALrows) + dimv(K) - dimv(ALrows + K)
    return inter <= len(L)


def lmax_lb(EK, A, E, K, n, trials=300, seed=0):
    """L_max 的下界：从高维到低维随机采样 E∩K 的子空间"""
    import random as _r
    rng = _r.Random(seed)
    base = EK
    for k in range(len(base), -1, -1):
        if k == 0:
            return 0, True
        for _ in range(trials):
            # k 个随机线性组合
            L = []
            for _ in range(k):
                coeff = [Fr(rng.randint(-2, 2)) for _ in range(len(base))]
                v = [sum((coeff[j] * base[j][i] for j in range(len(base))), Fr(0)) for i in range(n)]
                L.append(v)
            if dimv(L) != k:
                continue
            if feasible_L(L, A, E, K, n):
                return k, (k < len(base))
    return 0, True


def analyze(name, A, C, L0, qmin):
    n, p, r = len(A), len(C), len(L0)
    CA = mul(C, A)
    E = AI.nullspace(AI.vstack([C, L0]))          # ker C cap ker L0
    K = AI.nullspace(AI.vstack([C, CA]))          # ker[C;CA]
    L0k = AI.nullspace(AI.vstack([C, L0, CA]))    # E cap K
    Emat = [[E[j][i] for j in range(len(E))] for i in range(n)]
    Lmat = [[L0k[j][i] for j in range(len(L0k))] for i in range(n)]
    AL = mul(A, Lmat)
    ALrows = [[AL[i][j] for i in range(n)] for j in range(len(L0k))]
    ALE = (dimv(ALrows + E) == dimv(E)) if L0k else True
    ALK = dimv(ALrows) + dimv(K) - dimv(ALrows + K) if L0k else 0
    feasible = ALE and (ALK <= len(L0k))
    Lmax, _ = lmax_lb(L0k, A, E, K, n)
    alg_gap = len(L0k) - Lmax
    spec_cut = (qmin - r) - alg_gap
    return dict(name=name, n=n, p=p, r=r, dimE=dimv(E), dimEK=len(L0k),
                alg_ok=feasible, Lmax=Lmax, alg_gap=alg_gap,
                qmin=qmin, d_true=n - p - qmin, spec_cut=spec_cut,
                q_minus_r=qmin - r)


def main():
    rows = [analyze(*x) for x in load_instances()]
    hdr = (f"{'name':24s} n p r | dimE dimEK Lmax | q_min q-r alg_gap spec_cut")
    print(hdr); print("-" * len(hdr))
    for x in rows:
        print(f"{x['name']:24s} {x['n']} {x['p']} {x['r']} | {x['dimE']:4d} {x['dimEK']:5d} "
              f"{x['Lmax']:4d} | {x['qmin']:5d} {x['q_minus_r']:3d} {x['alg_gap']:7d} {x['spec_cut']:4d}")
    print("-" * len(hdr))
    from collections import Counter
    print(f"实例 {len(rows)}")
    print("q_min - r :", dict(sorted(Counter(x["q_minus_r"] for x in rows).items())))
    print("alg_gap  :", dict(sorted(Counter(x["alg_gap"] for x in rows).items())))
    print("spec_cut :", dict(sorted(Counter(x["spec_cut"] for x in rows).items())))
    bad = [x for x in rows if x["spec_cut"] < 0]
    print(f"spec_cut < 0（搜索/公式不一致）: {len(bad)}")


if __name__ == "__main__":
    main()
