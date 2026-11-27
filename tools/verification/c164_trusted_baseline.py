"""
c164_trusted_baseline.py — 可信基线验证器

目的
----
2026-10-23/24 的搜索中出现了四个工具 bug，每一个都让错误结论看起来像被验证过：
  1. 采样 λ 验证 (5b)          → 应改为精确 gcd
  2. 带过滤的搜索验证"对所有解" → 过滤本身隐含结论
  3. row_basis 把 L0 的行替换掉  → 应保留 L0 的字面行
  4. ρ* 搜索漏了 row(L0) ⊆ row(L) 约束

本脚本把所有检查集中到一处，并**逐项打印**每一条被检查的约束，
使"结论"与"检查"一一对应，无法再悄悄漏掉。

用法
----
    python c164_trusted_baseline.py            # 跑证书 + 目标实例
    python c164_trusted_baseline.py --random 30 # 再跑随机实例
"""
import sys
import os
import json
import random
import itertools

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "exact_linalg"))
from fractions import Fraction as Fr
import audit_independent as AI
import c162_dimV_formula as M

mul, rank = AI.mul, AI.rank
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ---------------------------------------------------------------- 基础检查

def check_prefix(L, L0):
    """要求 L 的前 len(L0) 行**逐字**等于 L0（问题的字面要求：L = [L0; R]）"""
    r = len(L0)
    if len(L) < r:
        return False
    return all(L[i] == L0[i] for i in range(r))


def check_rowspan(L, L0):
    """较弱的要求：row(L0) ⊆ row(L)"""
    return len(AI.row_basis(AI.row_basis(L0) + L)) == len(AI.row_basis(L))


def check_5a(L, A, C):
    """(5a)：精确秩判定"""
    return M.cond5a(L, A, C)


def check_5b(L, A, C):
    """(5b)：精确 GCD（返回 True/False/None）"""
    r = M.cond5b(L, A, C)
    if r is None:
        return None          # 所有子式恒为零（病态）
    return r == 0


def check_solution(L, A, C, L0, strict=True):
    """完整检查一个候选解，返回 (ok, 明细)"""
    detail = {}
    detail["prefix_L0"] = check_prefix(L, L0)
    detail["rowspan_L0"] = check_rowspan(L, L0)
    detail["5a"] = check_5a(L, A, C)
    detail["5b"] = check_5b(L, A, C)
    detail["rank_L"] = rank(L) == len(L)
    need = detail["prefix_L0"] if strict else detail["rowspan_L0"]
    ok = bool(need and detail["5a"] and detail["5b"] and detail["rank_L"])
    return ok, detail


# ---------------------------------------------------------------- 精确的 q_min

def cond5b_exact_if_small(L, A, C):
    """与 check_5b 相同，仅为可读性保留"""
    return check_5b(L, A, C)


def search_qmin(A, C, L0, trials=300, strict=True):
    """搜索 q_min。只用 (5a) 做快速筛选，最后用精确 (5b) 确认。"""
    n = len(A)
    r = len(L0)
    for q in range(r, n + 1):
        for _ in range(trials):
            L = [row[:] for row in L0]
            while len(L) < q:
                L.append([Fr(random.randint(-1, 1)) for _ in range(n)])
            if rank(L) != q:
                continue
            ok, detail = check_solution(L, A, C, L0, strict=strict)
            if ok:
                return q, L
    return None, None


def search_qdeg(A, C, L0, maxq=5):
    """退化解（rank(LN)=0）的最小 q；显式枚举含 L0 字面行的组合"""
    n = len(A)
    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    if not Nv:
        return None, None
    d = len(Nv)
    Nmat = [[Nv[j][i] for j in range(d)] for i in range(n)]
    KerN = AI.nullspace(AI.tr(Nmat))
    if not KerN:
        return None, None
    r = len(L0)
    # 生成元：L0 的字面行 + KerN 的基
    gens = [row[:] for row in L0] + [k[:] for k in KerN]
    for q in range(r, min(maxq, len(gens)) + 1):
        for comb in itertools.combinations(range(r, len(gens)), q - r):
            idx = list(range(r)) + list(comb)
            L = [gens[i][:] for i in idx]
            if not check_prefix(L, L0):
                continue
            if rank(L) != q:
                continue
            if rank(mul(L, Nmat)) != 0:
                continue
            ok, _ = check_solution(L, A, C, L0, strict=True)
            if ok:
                return q, L
    return None, None


def search_rhostar(A, C, L0, dimV, trials=250):
    """最小 ρ≥1 使 (ρ+1) 行、rank(LN)=ρ 的解存在；**含 L0 字面行**"""
    n = len(A)
    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    if not Nv:
        return None, None
    d = len(Nv)
    Nmat = [[Nv[j][i] for j in range(d)] for i in range(n)]
    r = len(L0)
    for rho in range(1, min(dimV, n - r) + 1):
        q = r + max(1, rho + 1 - r)
        q = max(r, rho + 1)
        for _ in range(trials):
            L = [row[:] for row in L0]
            while len(L) < q:
                L.append([Fr(random.randint(-1, 1)) for _ in range(n)])
            if rank(L) != q:
                continue
            if rank(mul(L, Nmat)) != rho:
                continue
            ok, _ = check_solution(L, A, C, L0, strict=True)
            if ok:
                return rho, L
    return None, None


# ---------------------------------------------------------------- 主流程

def toF(rows):
    return [[Fr(x) for x in r] for r in rows]


def report_instance(name, A, C, L0, trials=250):
    D = M.reduced_data(A, C, L0)
    print(f"\n{'='*66}\n{name}")
    print(f"  n={len(A)}  p={len(C)}  r={len(L0)}  d={D['d']}  dimV={len(D['V'])}  p_rank={len(D['S'])}")
    print(f"  α₀=L₀N ∈ V ? {D['inV']}   （可行性）")
    if not D["inV"]:
        print("  → 不可行，跳过")
        return None
    qmin, Ls = search_qmin(A, C, L0, trials)
    print(f"  q_min（搜索上界）= {qmin}")
    if Ls is not None:
        ok, det = check_solution(Ls, A, C, L0)
        print(f"    解明细: {det}")
    qd, Ld = search_qdeg(A, C, L0)
    print(f"  q_deg（退化解）= {qd}")
    rs, Lr = search_rhostar(A, C, L0, len(D["V"]))
    print(f"  ρ* = {rs}")
    # 候选公式
    cands = [x for x in (qd, (rs + 1 if rs else None)) if x is not None]
    pred = min(cands) if cands else None
    print(f"  预测 min(q_deg, ρ*+1) = {pred}   与实际一致? {pred == qmin}")
    return dict(name=name, n=len(A), p=len(C), r=len(L0), d=D["d"], dV=len(D["V"]),
                qmin=qmin, qdeg=qd, rhostar=rs, pred=pred, match=(pred == qmin))


def main():
    random.seed(20251024)
    rows = []

    # 1) 两个证书
    certs = [
        ("cert: refute_dimV1", "counterexample_refute_dimV1.json", "L"),
        ("cert: middle_layer", "certificate_middle_layer.json", "L_2row"),
    ]
    for name, fn, lkey in certs:
        path = os.path.join(ROOT, "proof", "refuted", "certificates", fn)
        if not os.path.exists(path):
            print(f"{name}: 证书文件缺失 {path}")
            continue
        d0 = json.load(open(path, encoding="utf-8"))
        A, C, L0, L = toF(d0["A"]), toF(d0["C"]), toF(d0["L0"]), toF(d0[lkey])
        ok, det = check_solution(L, A, C, L0)
        print(f"\n{'='*66}\n{name}\n  {fn}")
        print(f"  完整检查: {det}")
        print(f"  → 是合法解? {ok}")
        D = M.reduced_data(A, C, L0)
        print(f"  q={len(L)}   dimV={len(D['V'])}   q < dimV+1 ? {len(L) < len(D['V'])+1}")

    # 2) 六个目标实例（若在 lit 里）
    for fn, nm in [("counterexample_candidate.json", "cand"),
                   ("counterexample_d4.json", "d4"),
                   ("counterexample_p2.json", "p2")]:
        path = os.path.join(ROOT, "proof", "refuted", "certificates", fn)
        if not os.path.exists(path):
            continue
        d0 = json.load(open(path, encoding="utf-8"))
        A, C, L0 = toF(d0["A"]), toF(d0["C"]), toF(d0["L0"])
        r = report_instance(nm, A, C, L0, trials=150)
        if r:
            rows.append(r)

    # 3) 随机实例
    if "--random" in sys.argv:
        i = sys.argv.index("--random")
        m = int(sys.argv[i + 1]) if i + 1 < len(sys.argv) else 20
        A10 = None
        for t in range(m):
            n = random.choice([4, 5, 6])
            p = random.choice([1, 2])
            A = [[Fr(random.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
            C = [[Fr(random.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
            L0 = [[Fr(random.randint(-1, 1)) for _ in range(n)]]
            if rank(L0) != 1:
                continue
            try:
                r = report_instance(f"rand{t}", A, C, L0, trials=120)
            except Exception as e:
                print(f"rand{t}: {type(e).__name__}")
                continue
            if r:
                rows.append(r)

    # 4) 汇总
    if rows:
        print(f"\n{'='*66}\n汇总（{len(rows)} 个随机实例）")
        print(f"  公式 min(q_deg, ρ*+1) 一致: {sum(1 for r in rows if r['match'])}/{len(rows)}")
        miss = [r for r in rows if not r["match"]]
        for r in miss[:6]:
            print(f"    不一致: {r}")


if __name__ == "__main__":
    main()
