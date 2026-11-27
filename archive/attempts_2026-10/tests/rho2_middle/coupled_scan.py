"""coupled_scan.py — 从 middle_layer 出发的耦合扩展扫描（Q1-FALSE）

目标：造出第一个**真正的中间层 k=2** 实例（dimV=3，q(2)=3，q=2 无解）。

做法：把 n=6 的 middle_layer 扩到 n=7：
    A7 = [[A, x],[y^T, a]],  C7 = [C, c]
扫少量耦合参数（x, y 只取"接到第一个/最后一"两种结构，a ∈ {-1,0,1}，c ∈ {0,1}^2），
对每个候选算 d 与 dim V；命中 dimV=3 的再做精确搜索。

用法：
    python q1_false/tests/coupled_scan.py
"""
import sys
import os
import json
import random
import itertools

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools", "exact_linalg"))

from fractions import Fraction as Fr
import audit_independent as AI
import c162_dimV_formula as M
import c166_layer_audit as LA

mul, rank = AI.mul, AI.rank


def main():
    d0 = json.load(open(os.path.join(ROOT, "lit", "certificate_middle_layer.json"), encoding="utf-8"))
    toF = lambda m: [[Fr(x) for x in row] for row in m]
    A0, C0, L00 = toF(d0["A"]), toF(d0["C"]), toF(d0["L0"])
    n0 = len(A0)
    print(f"base: n={n0} p={len(C0)}")

    hits = 0
    tried = 0
    for xk, yk in itertools.product((0, 1), repeat=2):
        for a in (-1, 0, 1):
            for c in ((0, 0), (1, 0), (0, 1), (1, 1)):
                n = n0 + 1
                A = [[Fr(0)] * n for _ in range(n)]
                for i in range(n0):
                    for j in range(n0):
                        A[i][j] = A0[i][j]
                if xk:
                    A[0][n0] = Fr(1)
                if yk:
                    A[n0][0] = Fr(1)
                A[n0][n0] = Fr(a)
                C = [[Fr(0)] * n for _ in range(len(C0))]
                for i in range(len(C0)):
                    for j in range(n0):
                        C[i][j] = C0[i][j]
                    C[i][n0] = Fr(c[i])
                L0 = [row[:] + [Fr(0)] for row in L00]
                tried += 1
                try:
                    CA = mul(C, A)
                    Nv = AI.nullspace(AI.vstack([C, CA]))
                    if len(Nv) != 3:
                        continue
                    Nmat = [[Nv[j][i] for j in range(3)] for i in range(n)]
                    D = M.reduced_data(A, C, L0)
                    if len(D["V"]) != 3 or not D["inV"]:
                        continue
                    print(f"  dimV=3: x={xk} y={yk} a={a} c={c}", flush=True)
                    # q=2?
                    L2, _ = LA.find_solution(A, C, L0, 2, random.Random(1), 500, Nmat=Nmat)
                    if L2 is not None:
                        print("    q=2 有解 -> 不是 rho*=2")
                        continue
                    L3, rho3 = LA.find_solution(A, C, L0, 3, random.Random(2), 3000,
                                                rho_target=2, Nmat=Nmat)
                    if L3 is None:
                        print("    q=3,rho=2 未搜到")
                        continue
                    ok, det = LA.is_solution(L3, A, C, L0)
                    print(f"    *** 命中 q=3 rho={rho3} 复核={ok} ***")
                    if ok:
                        out = os.path.join(ROOT, "q1_false", "tests", "results")
                        os.makedirs(out, exist_ok=True)
                        json.dump(dict(A=[[str(y) for y in r] for r in A],
                                       C=[[str(y) for y in r] for r in C],
                                       L0=[[str(y) for y in r] for r in L0],
                                       L=[[str(y) for y in r] for r in L3]),
                                  open(os.path.join(out, "middle_k2_coupled.json"), "w",
                                       encoding="utf-8"), ensure_ascii=False, indent=1)
                        hits += 1
                except Exception as e:
                    continue
    print(f"\n扫描 {tried} 个候选，命中 {hits} 个")


if __name__ == "__main__":
    main()
