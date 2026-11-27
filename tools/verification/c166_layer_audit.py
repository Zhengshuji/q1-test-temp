"""c166_layer_audit.py — 层公式 q(ρ) = max(r, ρ+1) 的可复现审计

为什么有这个脚本
----------------
ATTACK_LOG D33 的结论 "q(ρ)=max(r,ρ+1) 在 69/70 个可达 (实例,ρ) 对上成立"
来自一次**没有保存脚本**的实验；那 1 个失败至今未分类（D33 猜测是搜索深度不足）。

本脚本做三件事，全部用精确有理数：
  1. 对每个实例，按 q 升序搜出 q_min；
  2. 按 ρ 升序搜出 ρ*（最小可达秩），并记录所有可达 ρ；
  3. 对每个可达 ρ，检验 q 是否能压到 max(r, ρ+1)（紧性），
     失败则记录完整的 (A,C,L0,L,ρ,q) 数据，供离线分析。

方法学（吸取项目纪律）
----------------------
- (5b) 必须用精确子式 gcd；随机 λ 只作为**必要条件的快速拒绝器**（不会误杀真解，
  因为真解对所有 λ 都通过；只可能放过假阳性，随后被 gcd 杀掉）。
- 搜索空间用 L=[L0;R]（字面前缀；由行变换不变性，这等价于 row(L0)⊆row(L)）。
- 随机条目取 {-2..2}，避免多行重复。
- 每个失败都带 trials 计数，便于判断"搜索深度"还是"真缺口"。

用法
----
    python c166_layer_audit.py --certs                 # 只跑 lit/ 里的实例
    python c166_layer_audit.py --random 20 --seed 7    # 追加 20 个随机实例
    python c166_layer_audit.py --random 20 --save out.json
"""
import sys
import os
import json
import random
import argparse

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "exact_linalg"))
from fractions import Fraction as Fr

import audit_independent as AI
import c162_dimV_formula as M

mul, rank = AI.mul, AI.rank
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ------------------------------------------------------------------ 基本检查

def _h_of(L, CA, C):
    """h = rank[L; CA; C]（(5b) 的两边共同的秩）"""
    return rank(AI.vstack([L, CA, C]))


def quick_5b(L, LA, CA, C, h, n, lambdas=(2, -3, 5, -7, 11, 13)):
    """(5b) 的必要条件：在若干 λ 上秩必须相等。只用于快速拒绝。"""
    for lam in lambdas:
        rows = [[Fr(lam) * L[i][j] - LA[i][j] for j in range(n)] for i in range(len(L))]
        rows += CA
        rows += C
        if rank(rows) != h:
            return False
    return True


def is_solution(L, A, C, L0):
    """完整判定：L=[L0;R]，rank(L)=q，(5a)，(5b)（精确 gcd）。

    返回 (ok, rho, why)：why ∈ {'ok','rank','5a','5b_quick','5b_exact','gcd_none'}
    """
    if len(L) < len(L0) or L[:len(L0)] != L0:
        return False, None, "prefix"
    if rank(L) != len(L):
        return False, None, "rank"
    CA = mul(C, A)
    LA = mul(L, A)
    # (5a)
    if rank(AI.vstack([LA, L, CA, C])) != rank(AI.vstack([L, CA, C])):
        return False, None, "5a"
    h = _h_of(L, CA, C)
    n = len(A)
    # 快速拒绝
    if not quick_5b(L, LA, CA, C, h, n):
        return False, None, "5b_quick"
    # 精确 gcd
    # 精确 gcd（audit_independent 在退化情形可能断言失败，包一层）
    try:
        g = M.cond5b(L, A, C)
    except Exception:
        return False, None, "gcd_err"
    if g is None:
        return False, None, "gcd_none"
    if g != 0:
        return False, None, "5b_exact"
    Nv = AI.nullspace(AI.vstack([C, CA]))
    Nmat = [[Nv[j][i] for j in range(len(Nv))] for i in range(n)]
    rho = rank(mul(L, Nmat)) if Nv else 0
    return True, rho, "ok"


# ------------------------------------------------------------------ 搜索

def _rand_row(n, rng):
    while True:
        row = [Fr(rng.randint(-2, 2)) for _ in range(n)]
        if any(x != 0 for x in row):
            return row


def sample_L(L0, q, n, rng):
    L = [row[:] for row in L0]
    while len(L) < q:
        L.append(_rand_row(n, rng))
    return L


def find_solution(A, C, L0, q, rng, trials, rho_target=None, Nmat=None):
    """在 q 行里搜一个解；若 rho_target 给定则要求 rank(LN)=rho_target。

    返回 (L, rho) 或 (None, None)。
    """
    n = len(A)
    if Nmat is None:
        Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
        Nmat = [[Nv[j][i] for j in range(len(Nv))] for i in range(n)] if Nv else None
    for t in range(trials):
        L = sample_L(L0, q, n, rng)
        if rank(L) != q:
            continue
        if rho_target is not None:
            if Nmat is None or rank(mul(L, Nmat)) != rho_target:
                continue
        ok, rho, why = is_solution(L, A, C, L0)
        if ok:
            return L, rho
    return None, None


# ------------------------------------------------------------------ 单实例审计

def audit_instance(name, A, C, L0, rng, trials=200, verbose=True):
    n = len(A)
    r = len(L0)
    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    # d=0：K={0}，于是 J=row[C;CA]=R^n（否则 K 非零），(5a)(5b) 对任意满秩 L 自动成立
    if not Nv:
        out = dict(name=name, n=n, p=len(C), r=r, d=0, dimV=0, rho0=0,
                   inV=True, qmin=r, rhostar=0, pred=r, match_formula=True,
                   reachable={0: r}, tight={0: True}, failures=[],
                   A=[[str(x) for x in row] for row in A],
                   C=[[str(x) for x in row] for row in C],
                   L0=[[str(x) for x in row] for row in L0],
                   note="d=0 退化：q_min=r")
        if verbose:
            print(f"{name:22s} n={n} p={len(C)} r={r} d=0（退化）| q_min={r} ρ*=0 ✓")
        return out

    D = M.reduced_data(A, C, L0)
    d = D["d"]
    dimV = len(D["V"])
    Nmat = [[Nv[j][i] for j in range(len(Nv))] for i in range(n)]
    rho0 = rank(mul(L0, Nmat))

    out = dict(name=name, n=n, p=len(C), r=r, d=d, dimV=dimV, rho0=rho0,
               inV=bool(D["inV"]), qmin=None, rhostar=None,
               reachable={}, tight={}, failures=[],
               A=[[str(x) for x in row] for row in A],
               C=[[str(x) for x in row] for row in C],
               L0=[[str(x) for x in row] for row in L0])
    if not D["inV"]:
        if verbose:
            print(f"{name:22s} 不可行 (alpha0 ∉ V)")
        return out

    # --- 每个 ρ 的最小 q（同一份结果同时给出 q_min 与 ρ*）
    found = {}
    for rho in range(0, dimV + 1):
        q_lo = max(r, rho + 1)
        if q_lo > n:
            continue
        got = None
        # 关键层（q 恰为下界）多给几倍 trials，降低"搜索深度"假象
        for q in range(q_lo, n + 1):
            tr = trials * (4 if q == q_lo else 1)
            L, rr = find_solution(A, C, L0, q, rng, tr, rho_target=rho, Nmat=Nmat)
            if L is not None:
                got = (q, L)
                break
        if got is not None:
            found[rho] = got

    if found:
        out["qmin"] = min(q for q, _ in found.values())
        out["rhostar"] = min(found)
        for rho, (q, L) in found.items():
            out["reachable"][rho] = q
            out["tight"][rho] = (q == max(r, rho + 1))
            if not out["tight"][rho]:
                out["failures"].append(dict(rho=rho, q=q, q_lo=max(r, rho + 1),
                                            L=[[str(x) for x in row] for row in L]))
        out["pred"] = max(r, out["rhostar"] + 1)
        out["match_formula"] = (out["pred"] == out["qmin"])
    else:
        out["pred"] = None
        out["match_formula"] = None

    if verbose:
        tight_bad = [rho for rho, t in out["tight"].items() if not t]
        print(f"{name:22s} n={n} p={len(C)} r={r} d={d} dimV={dimV} ρ0={rho0} "
              f"| q_min={out['qmin']} ρ*={out['rhostar']} pred={out['pred']} "
              f"{'✓' if out['match_formula'] else '✗'}"
              + (f" | 不紧: ρ={tight_bad}" if tight_bad else ""))
    return out


# ------------------------------------------------------------------ 实例来源

def cert_instances():
    rows = []
    for fn, key in [("counterexample_refute_dimV1.json", "L"),
                    ("certificate_middle_layer.json", "L_2row"),
                    ("certificate_rhostar_lt_dimV.json", None),
                    ("counterexample_candidate.json", "L"),
                    ("counterexample_d4.json", "L"),
                    ("counterexample_p2.json", "L")]:
        path = os.path.join(ROOT, "proof", "refuted", "certificates", fn)
        if not os.path.exists(path):
            continue
        d0 = json.load(open(path, encoding="utf-8"))
        toF = lambda m: [[Fr(x) for x in r] for r in m]
        rows.append((fn.replace(".json", ""), toF(d0["A"]), toF(d0["C"]), toF(d0["L0"])))
    return rows


def random_instances(m, seed, n_choices=(4, 5, 6), p_choices=(1, 2), r_choices=(1,)):
    rng = random.Random(seed)
    out = []
    for t in range(m):
        n = rng.choice(n_choices)
        p = rng.choice(p_choices)
        r = rng.choice([x for x in r_choices if x <= n] or [1])
        A = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        L0 = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(r)]
        if rank(L0) != r:
            continue
        out.append((f"rand_s{seed}_r{r}_{t}", A, C, L0))
    return out


# ------------------------------------------------------------------ 主流程

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--certs", action="store_true")
    ap.add_argument("--random", type=int, default=0)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--trials", type=int, default=200)
    ap.add_argument("--r", default="1", help="L0 的行数，逗号分隔，如 1,2,3")
    ap.add_argument("--save", default="")
    args = ap.parse_args()

    insts = []
    if args.certs or args.random == 0:
        insts += cert_instances()
    if args.random:
        r_choices = tuple(int(x) for x in args.r.split(","))
        insts += random_instances(args.random, args.seed, r_choices=r_choices)

    results = []
    for name, A, C, L0 in insts:
        try:
            results.append(audit_instance(name, A, C, L0, random.Random(12345), args.trials))
        except Exception as e:
            print(f"{name}: ERR {type(e).__name__}: {e}")

    feas = [r for r in results if r["inV"]]
    with_q = [r for r in feas if r["qmin"] is not None]
    match = [r for r in with_q if r["match_formula"]]
    print("\n" + "=" * 70)
    print(f"可行实例 {len(feas)}；q_min 搜到 {len(with_q)}；两种公式一致 {len(match)}/{len(with_q)}")
    pairs = sum(len(r["reachable"]) for r in with_q)
    tight_ok = sum(1 for r in with_q for t in r["tight"].values() if t)
    print(f"可达 (实例,ρ) 对 {pairs}；紧性 {tight_ok}/{pairs}")
    for r in with_q:
        for f in r["failures"]:
            print(f"  不紧: {r['name']} ρ={f['rho']} q={f['q']} (下界 {f['q_lo']})")

    if args.save:
        with open(args.save, "w", encoding="utf-8") as fh:
            json.dump(results, fh, ensure_ascii=False, indent=1)
        print(f"已保存 {args.save}")


if __name__ == "__main__":
    main()
