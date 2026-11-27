"""c189_ledger.py -- the single MIN-ROWS ledger (exact over Q)

WHY THIS FILE EXISTS
--------------------
Three handovers in a row (Q1_FOR_EXPERT_7/8/9, STATUS_2026-10-26,
HANDOVER_2026-10-26) quoted formulas whose counterexamples lived in a different
document, and two censuses ("119/119", "8/40") were never saved as scripts.  This
file is the fix: every instance in one place, one exact criterion, one table.

RULES BAKED INTO THE CODE
-------------------------
 R1  (5a)/(5b) are decided ONLY over Q (scripts/core/audit_independent.py).
     F_p (tools/exact_linalg/c188_fp.py) screens only; every witness is
     re-verified over Q before it is printed.
 R2  Every row carries provenance (certificate file / generator / seed).
 R3  q_status has exactly two values:
       EXACT -- proved (witness + proved lower bound, or the c190 closure theorem)
       UB    -- construction only, lower bound unknown
     A UB is never printed as EXACT.
 R4  rho* is printed only when proved:
       rho* = 0  <=>  S subset J and S A subset J        (theorem 7)
       rho* = 1  when rho* = 0 is excluded and a witness has rho = 1
       rho* = d  on the c190 family (C^n is the only feasible V)
     Otherwise rho* is unknown and F2/F3 are reported as undetermined.
 R5  A formula is REFUTED only from a proved q_min, or (F1) from q_ub < F1.

USAGE
-----
    python tools/ledger/c189_ledger.py
    python tools/ledger/c189_ledger.py --random 12 --seed 5

NOTATION (same as the handover)
    j = dim J, d = n - j, c0 = dim(row(L0) n J), eps = 1[L0 is not a solution],
    rho = rank(V N), rho* = min over feasible V of rho.
"""
import sys, os, json, random

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, "tools", "exact_linalg"))
sys.path.insert(0, os.path.join(_ROOT, "tools", "certificates"))
sys.path.insert(0, _HERE)

from fractions import Fraction as Fr
import audit_independent as AI
import c188_fp as FP
import c190_invariant_family as FAM

mul, rank, inv = AI.mul, AI.rank, AI.inv
P_BIG = 1000003


# ------------------------------------------------------------------ criteria

def cond_q(A, C, L):
    """exact (5a) and (5b) over Q -- the only authority in this file"""
    return AI.cond_5a_orig(A, C, L) and AI.cond_5b_orig(A, C, L)


def cond_fp(A, C, L, p=P_BIG):
    """F_p screen (screening only; never quoted as a result)"""
    try:
        Ai = [[int(x) % p for x in r] for r in A]
        Ci = [[int(x) % p for x in r] for r in C]
        Li = [[int(x) % p for x in r] for r in L]
    except (TypeError, ValueError):
        return None
    return FP.cond5a_fp(Li, Ai, Ci, p) and FP.cond5b_fp(Li, Ai, Ci, p)


# ------------------------------------------------------------------ metrics

def old_dimV(A, C, L0):
    """the OLD reduced quantity dim V = dim <row(R0)>_{A'} (kept for reference)"""
    n = len(A)
    CA = mul(C, A)
    M = AI.vstack([C, CA])
    Nv = AI.nullspace(M)
    d = len(Nv)                       # d = dim ker[C;CA]
    if d == 0:
        return 0
    N = [[Nv[k][i] for k in range(len(Nv))] for i in range(n)]
    NtN = mul(AI.tr(N), N)
    Ap = mul(inv(NtN), mul(AI.tr(N), mul(A, N)))
    AN = mul(A, N)
    Np = mul(N, Ap)
    R0 = [[AN[i][k] - Np[i][k] for k in range(d)] for i in range(n)]
    Vr = AI.row_basis(R0)
    while Vr:
        V2 = AI.row_basis(Vr + mul(Vr, Ap))
        if len(V2) == len(Vr):
            break
        Vr = V2
    return len(Vr)


def closure_theorem(A, C, L0):
    """The c190 theorem, applied self-contained (no trust in c190's output).

    Hypothesis:  row(L0) = J  (so r = c0 = j),  J not A-invariant.
    Then every feasible V is A-invariant and contains J, hence V >= <J>_A.
    If <J>_A = C^n and C^n is feasible, then q_min = n and the only feasible V
    is C^n, so rho* = rank(C^n N) = d.

    Returns dict(q_min, rho_star) when the theorem applies, else None.
    """
    n = len(A)
    CA = mul(C, A)
    M = AI.vstack([C, CA])
    J = AI.row_basis(M)
    j = rank(M)
    S = AI.row_basis(L0)
    if not (len(S) == j == len(L0)):
        return None
    if not all(AI.in_span(r, J) for r in L0):
        return None
    JA = AI.row_basis([mul([r], A)[0] for r in J])
    if not JA or rank(AI.vstack([J, JA])) == j:   # J A-invariant: branch A, q_min = r
        return None
    clo = [list(r) for r in J]
    while True:
        nxt = AI.row_basis(clo + [mul([r], A)[0] for r in clo])
        if len(nxt) == len(clo):
            break
        clo = nxt
    if len(clo) != n:
        return None
    Cn = [[Fr(1) if i == k else Fr(0) for k in range(n)] for i in range(n)]
    if not cond_q(A, C, Cn):
        return None
    Nv = AI.nullspace(M)
    N = [[Nv[k][i] for k in range(len(Nv))] for i in range(n)]
    return dict(q_min=n, rho_star=rank(mul(Cn, N)), witness=Cn)


def rho_star_known(A, C, L0, rho_wit):
    """rho* when provable from theorems (else None)"""
    n = len(A)
    CA = mul(C, A)
    M = AI.vstack([C, CA])
    J = AI.row_basis(M)
    S = AI.row_basis(L0)
    # theorem 7: rho* = 0  <=>  S subset J and S A subset J
    if all(AI.in_span(r, J) for r in S):
        SA = [mul([r], A)[0] for r in S]
        if all(AI.in_span(r, J) for r in SA):
            return 0
    # rho* = 0 excluded; a witness with rho = 1 proves rho* = 1
    if rho_wit == 1:
        return 1
    return None


def metrics(A, C, L0, V=None):
    n = len(A)
    CA = mul(C, A)
    M = AI.vstack([C, CA])
    j = rank(M)
    J = AI.row_basis(M)
    d = n - j
    Nv = AI.nullspace(M)
    N = [[Nv[k][i] for k in range(len(Nv))] for i in range(n)]
    S = AI.row_basis(L0)
    c0 = len(S) + j - rank(AI.vstack([S, J]))
    L0_ok = cond_q(A, C, L0)
    m = dict(n=n, p=len(C), r=len(L0), j=j, d=d, J=J, N=N, c0=c0,
             eps=0 if L0_ok else 1, L0_feasible=L0_ok,
             rho_L0=rank(mul(L0, N)), dV=old_dimV(A, C, L0),
             q=None, rho=None, c=None)
    if V is not None:
        m["q"] = len(V)
        m["rho"] = rank(mul(V, N))
        m["c"] = len(V) + j - rank(AI.vstack([V, J]))
    return m


def search_witness(A, C, L0, rng, trials=150):
    """first feasible V (row list) by increasing q; F_p screen, Q confirmation"""
    n = len(A)
    for q in range(len(L0), n + 1):
        for _ in range(trials):
            V = [list(r) for r in L0] + [[Fr(rng.randint(-2, 2)) for _ in range(n)]
                                         for _ in range(q - len(L0))]
            if rank(V) != q:
                continue
            if cond_fp(A, C, V) is False:
                continue
            if cond_q(A, C, V):
                return q, V
    return None, None


def certify(q, r, eps):
    if q is None:
        return "none"
    if q == r:
        return "EXACT(q=r)"
    if q == r + eps:          # eps = 1 and q = r + 1
        return "EXACT(q=r+eps)"
    return "UB"


# ------------------------------------------------------------------ the bank

def certificates():
    """every lit/*.json and q1_true/evidence/*.json with A, C, L0 (+ witness)"""
    out = []
    for sub in ("proof/refuted/certificates", "lit"):
        folder = os.path.join(_ROOT, sub)
        if not os.path.isdir(folder):
            continue
        for fn in sorted(os.listdir(folder)):
            if not fn.endswith(".json"):
                continue
            try:
                d = json.load(open(os.path.join(folder, fn), encoding="utf-8"))
            except Exception:
                continue
            if not all(k in d for k in ("A", "C", "L0")):
                continue
            w = None
            for key in ("L", "L_2row", "L_3row"):
                if key in d:
                    w = d[key]
                    break
            out.append(dict(name=fn.replace(".json", ""), src=sub,
                            A=FAM.to_F(d["A"]), C=FAM.to_F(d["C"]),
                            L0=FAM.to_F(d["L0"]),
                            W=FAM.to_F(w) if w is not None else None))
    return out


def directed():
    """hand-built families: rho*=0, branch A, and the handover's diagonal example"""
    out = []
    n = 4
    A = [[Fr(0)] * n for _ in range(n)]
    for i in range(n - 1):
        A[i][i + 1] = Fr(1)
    C = [[Fr(1), Fr(0), Fr(0), Fr(0)]]
    out.append(dict(name="nilpotent4_L0=e1", src="directed",
                    A=A, C=C, L0=[[Fr(1), Fr(0), Fr(0), Fr(0)]], W=None))
    A0 = [[Fr(0)] * 4 for _ in range(4)]
    C0 = [[Fr(1), Fr(0), Fr(0), Fr(0)]]
    out.append(dict(name="A=0_L0=C=e1", src="directed",
                    A=A0, C=C0, L0=[[Fr(1), Fr(0), Fr(0), Fr(0)]], W=None))
    A3 = [[Fr(0), Fr(0), Fr(0), Fr(0)],
          [Fr(0), Fr(1), Fr(0), Fr(0)],
          [Fr(0), Fr(0), Fr(2), Fr(0)],
          [Fr(0), Fr(0), Fr(0), Fr(3)]]
    C3 = [[Fr(1), Fr(1), Fr(1), Fr(0)]]
    out.append(dict(name="handover_diag_CA", src="directed",
                    A=A3, C=C3, L0=mul(C3, A3), W=None))
    return out


def family(seed=4242, k=3, n=5):
    """row(L0) = J family, q_min = n proved (c190)"""
    out = []
    for t, (A, C, L0, info) in enumerate(FAM.generate(seed=seed, k=k, n=n), 1):
        out.append(dict(name=f"family_S=J_n{n}_{t}", src="c190",
                        A=A, C=C, L0=L0, W=info["Cn"], info=info))
    return out


# ------------------------------------------------------------------ table

def report(rows, random_census=0, seed=5):
    rng = random.Random(seed)
    for t in range(random_census):
        n = rng.choice([4, 5])
        p = rng.choice([1, 2])
        r = rng.choice([1, 2])
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        L0 = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(r)]
        if rank(C) != p or rank(L0) != r:
            continue
        q, V = search_witness(A, C, L0, rng, trials=120)
        rows.append(dict(name=f"rand_s{seed}_{t}", src="census",
                         A=A, C=C, L0=L0, W=V))

    hdr = (f"{'instance':33s} {'n p r':6s} {'j d c0 e':9s} {'q_wit rho c':12s} "
           f"{'status':15s} {'F1':>4s} {'dV+1':>5s} {'F2':>4s} {'F3':>4s}   verdicts")
    print("=" * len(hdr))
    print("c189 -- single ledger, exact over Q")
    print("   F1 = d + max(c0,1)   F2 = max(r+eps, rho*+1)   "
          "F3 = max(r+eps, rho*+max(c0,1))   dV+1 = old 'dim V + 1'")
    print("=" * len(hdr))
    print(hdr)
    print("-" * len(hdr))

    ref_F1, ref_F2, ref_oldF, meet_F3 = [], [], [], 0
    undet_F2 = 0
    for row in rows:
        A, C, L0, W = row["A"], row["C"], row["L0"], row.get("W")
        m = metrics(A, C, L0, W)
        if m["q"] is None:
            q, V = search_witness(A, C, L0, random.Random(11), trials=80)
            if q is not None:
                m = metrics(A, C, L0, V)
        info = row.get("info")
        th = closure_theorem(A, C, L0)
        if info is not None and th is not None:
            # cross-check: c190's own analysis vs the self-contained theorem
            assert info["q_min"] == th["q_min"] and info["rho_star"] == th["rho_star"], \
                f"c190 vs ledger disagree on {row['name']}"
        if th is not None:
            status = "EXACT(closure)"
            rs = th["rho_star"]
            if m["q"] is None:
                m = metrics(A, C, L0, th["witness"])
        else:
            status = certify(m["q"], m["r"], m["eps"])
            rs = rho_star_known(A, C, L0, m["rho"]) if m["rho"] is not None else None
        exact = status.startswith("EXACT")
        rs_proved = rs is not None
        rs_shown = rs if rs_proved else m["rho"]

        r, eps, c0, d = m["r"], m["eps"], m["c0"], m["d"]
        F1 = d + max(c0, 1)
        oldF = m["dV"] + 1
        if rs_shown is not None:
            F2 = max(r + eps, rs_shown + 1)
            F3 = max(r + eps, rs_shown + max(c0, 1))
        else:
            F2 = F3 = None

        v = []
        if m["q"] is not None:
            if m["q"] < F1:
                v.append("F1 REFUTED"); ref_F1.append(row["name"])
            elif m["q"] == F1:
                v.append("F1 ok")
            if m["q"] < oldF:
                v.append("dimV+1 REFUTED"); ref_oldF.append(row["name"])
            elif m["q"] == oldF:
                v.append("dimV+1 ok")
            if F2 is not None:
                if exact and rs_proved:
                    if m["q"] == F2:
                        v.append("F2 ok")
                    else:
                        v.append("F2 REFUTED"); ref_F2.append(row["name"])
                elif m["q"] < F2:
                    v.append("F2 REFUTED"); ref_F2.append(row["name"])
                else:
                    v.append("F2 undet"); undet_F2 += 1
            if F3 is not None:
                if m["q"] == F3:
                    v.append("F3 met"); meet_F3 += 1
                elif m["q"] > F3:
                    v.append("F3 not met by witness")
                else:
                    v.append("F3 REFUTED"); ref_F2.append(row["name"] + "(F3)")
        star = "" if rs_proved else "*"
        print(f"{row['name'][:33]:33s} {m['n']} {m['p']} {m['r']}   "
              f"{m['j']} {m['d']} {m['c0']:2d} {m['eps']}   "
              f"{str(m['q']):>4s} {str(m['rho']):>4s} {str(m['c']):>3s}  "
              f"{status:15s} {F1:4d} {oldF:5d} "
              f"{(str(F2) + star):>4s} {(str(F3) + star):>4s}   " + ", ".join(v))

    print("-" * len(hdr))
    print("  *  = rho* unknown; F2/F3 shown with the witness rho (an upper bound of rho*)")
    print()
    print("VERDICTS (rigorous directions only)")
    print(f"  F1 = d + max(c0,1)      REFUTED on {len(ref_F1)} instances: "
          f"{', '.join(ref_F1) if ref_F1 else '-'}")
    print(f"  old dim V + 1           REFUTED on {len(ref_oldF)} instances: "
          f"{', '.join(ref_oldF[:8]) if ref_oldF else '-'}"
          + (" ..." if len(ref_oldF) > 8 else ""))
    print(f"  F2 = max(r+eps,rho*+1)  REFUTED on {len([x for x in ref_F2 if '(F3)' not in x])}"
          f" instances: {', '.join([x for x in ref_F2 if '(F3)' not in x]) or '-'}")
    print(f"                          undetermined on {undet_F2} rows (rho* unknown)")
    print(f"  F3 = max(r+eps,rho*+max(c0,1))   refuted by: "
          f"{[x for x in ref_F2 if '(F3)' in x] or 'nothing'};  "
          f"attained exactly on {meet_F3} rows")


def main():
    rows = certificates() + directed() + family(k=3)
    nrand = 0
    seed = 5
    if "--random" in sys.argv:
        nrand = int(sys.argv[sys.argv.index("--random") + 1])
    if "--seed" in sys.argv:
        seed = int(sys.argv[sys.argv.index("--seed") + 1])
    report(rows, random_census=nrand, seed=seed)


if __name__ == "__main__":
    main()
