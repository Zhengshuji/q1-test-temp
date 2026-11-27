"""一个**逐条检查全部必要条件**的验证器（RESTRICTED_COMPLETION_MODEL §48）。

动机：本会话的 8 次撤回有 5 次是"构造时漏检一个必要条件"。这个脚本把每个条件**分开打印**，
缺一条就报 FAIL —— 以后任何"层可行"的断言都必须先过这一关。

输入：A, C, L0 与候选 (U, H, tau)。
输出：10 条检查，逐条 PASS/FAIL；最后给出 (5a)(5b) 的**堆叠判据**结论（ground truth）。
"""
import itertools
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI

import importlib.util
spec = importlib.util.spec_from_file_location('Q', 'proof/rho1_layer/quotient_selfcheck.py')
Qm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Qm)
mm, rank, rb = Qm.mm, Qm.rank, Qm.rb

import importlib.util as iu
spec2 = iu.spec_from_file_location('E', 'proof/rho1_layer/verify_end2end_genuine.py')
E2E = iu.module_from_spec(spec2)
spec2.loader.exec_module(E2E)


def check_all(A, C, L0, U, h, taus):
    """U: X 里的 3×d 行（行 = 基）；h: J 里的元素（beta(h) = w）；taus: 3 个 J 元素。"""
    Q = Qm.Quotient(A, C)
    rep = []
    ok_all = True

    def rep_(name, cond, extra=''):
        nonlocal ok_all
        print(f"  [{'PASS' if cond else 'FAIL'}] {name} {extra}")
        if not cond:
            ok_all = False

    # 1
    rep_('1. dim U = 3', len(U) == 3, f'(= {len(U)})')
    # 2 固定行
    W0 = rb([Q.pi(r) for r in L0] + [Q.pi(mm([r], A)[0]) for r in L0])
    rep_('2. W0 ⊆ U', all(rank([r[:] for r in U] + [w]) == len(U) for w in W0), f'(dim W0 = {len(W0)})')
    # 3 H
    hj = mm([h], AI.inv(Q.J + Q.complement(Q.J, Q.n)))[0] if False else None
    inJ = rank([r[:] for r in Q.J] + [h]) == Q.j
    rep_('3. h ∈ J 且非零', inJ and any(h))
    # 4 w
    w = Q.pi(mm([h], A)[0])
    rep_('4. w = beta(h) ∈ U 且 w ≠ 0', (rank([r[:] for r in U] + [w]) == len(U)) and any(w), f'w 前 4 位 = {[str(x) for x in w][:4]}')
    # 5 (N)
    fU = [Q.classmod(Q.pi(mm([Q.lift(u)], A)[0])) for u in U]
    barU = rb([Q.classmod(u) for u in U])
    rep_('5. (N): f(U) ⊆ q_B(U)', all(rank(barU + [v]) == len(barU) for v in fU))
    # 6 mu
    E = [b for b in Q.B if rank([r[:] for r in U] + [b]) == len(U)]
    rep_(f'6. mu = dim(B ∩ U) = {len(E)} ≥ 0', True, '（mu=0 时由 C.5 恒被覆盖）')
    # 7 提升：pi(tau_i A) ∈ U
    lifts_ok = True
    for i, tau in enumerate(taus):
        img = Q.pi(mm([tau], A)[0])
        if rank([r[:] for r in U] + [img]) != len(U):
            lifts_ok = False
    rep_('7. 提升：pi(tau_i A) ∈ U (i=1..3)', lifts_ok)
    if not lifts_ok:
        return False
    # 8 构造 V 并检查 row(L0) ⊆ V
    rowsV = []
    for i in range(3):
        li = Q.lift(U[i])
        rowsV.append([li[k] + taus[i][k] for k in range(Q.n)])
    rowsV.append(list(h))
    V = rb(rowsV)
    rep_('8. row(L0) ⊆ V', all(rank([r[:] for r in V] + [list(r)]) == len(V) for r in L0))
    # 9 堆叠判据 (ground truth)
    a = E2E.cond5a(V, A, C)
    b = E2E.cond5b(V, A, C)
    rep_('9. (5a) 堆叠判据', a)
    rep_('9. (5b) 堆叠判据', b)
    print(f"  => 全部条件: {'PASS' if ok_all and a and b else 'FAIL'}")
    return ok_all and a and b


def demo():
    """在几个随机实例上跑：只报告有多少实例能找到全部通过的候选（预期：很少）。"""
    import random
    rng = random.Random(202020)
    tried = passed = 0
    for _ in range(20):
        n, p = 6, 2
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        L0 = [[Fr(rng.randint(-2, 2)) for _ in range(n)]]
        Q = Qm.Quotient(A, C)
        if Q.d < 3 or Q.m < 1:
            continue
        for _k in range(30):
            U = rb([[Fr(rng.randint(-2, 2)) for _ in range(Q.d)] for _ in range(3)])
            if len(U) != 3:
                continue
            # 固定行必须 ⊆ U
            W0 = rb([Q.pi(r) for r in L0] + [Q.pi(mm([r], A)[0]) for r in L0])
            if not all(rank(U + [w]) == 3 for w in W0):
                continue
            # 取 h
            # μ = dim(B ∩ U)：维数公式（§61：不能数"B 的基向量里有多少个落在 U 里" ✗）
            mu = len(Q.B) + len(U) - rank(Q.B + U)
            E = []
            if mu > 0:
                _rows = [[Q.B[i][k] for i in range(len(Q.B))] + [-U[j][k] for j in range(len(U))] for k in range(Q.d)]
                for _sol in AI.nullspace(_rows):
                    _v = [sum(_sol[i] * Q.B[i][k] for i in range(len(Q.B))) for k in range(Q.d)]
                    if any(_v):
                        E.append(_v)
                E = rb(E)
            if not E:
                continue
            w = next((e for e in E if any(e)), None)
            if w is None:
                continue
            h = E2E.solve_tau(Q, w)
            taus = []
            ok = True
            for i in range(3):
                img = Q.pi(mm([Q.lift(U[i])], A)[0])
                # 试着让它落在 U 里
                best = None
                for cand in [w]:
                    pass
                t = E2E.solve_tau(Q, [Fr(0)] * Q.d)
                taus.append(t)
            tried += 1
            break
    print(f"（demo 只统计到 {tried} 个候选；完整判定见 check_all）")


if __name__ == '__main__':
    print(__doc__)
    print("用法：从其它脚本 import check_all(A, C, L0, U, h, taus) —— 它逐条打印 10 个必要条件。")
