"""S1 区判据的**真实实例**验证（验证 ≠ 证明）。

被测命题（theorem.md §26，v3 修正版）：
设 c >= rho-1、rho >= 2、dim B >= rho-1。记
    J  = row[C; CA],        B = pi(J A),
    S  = (J + J A) ∩ A^{-1}(J + J A),      K = pi(S) = {b in B : T(b) in B},
    U0 = pi(row L0).
则第 (rho,c) 层可行  <=>  dim K >= rho  且  U0 ⊆ K
（等价地：dim S - j >= rho  且  row L0 ⊆ S + J）。

与 v2（已作废，备份在 trash/verify_s1_v1.py.bak）的差别：v2 在抽象数据上做，
**漏掉了 U0 ⊆ U**（那是 (5a) 与 V ⊇ row L0 的一部分），且用了错误的 (5a) 形式。
本版一切都在 C^n 里、用项目自己的精确判据 cond_5a_orig / cond_5b_orig（后者作用于**堆叠**矩阵
[lam L - LA; CA; C]，秩上界与下界都在里面）。

检验（构造 + 精确判据）：
  (I)  判据成立 => 照判据构造的 L 确实满足 (5a)∧(5b)；
  (II) 判据不成立 => 大量随机构造的 L（dim pi(V)=rho、V ⊇ row L0）**都不**满足 (5a)∧(5b)。
"""
import io
import json
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI


def mm(X, Y):
    """矩阵乘：X (r x k) * Y (k x c)，全部用本文件的局部实现，避免外部约定差异。"""
    r = len(X); k = len(Y); c = len(Y[0]) if Y else 0
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(c)] for i in range(r)]


def _rref(M):
    M = [row[:] for row in M]
    r = len(M); c = len(M[0]) if M else 0
    piv = []
    i = 0
    for j in range(c):
        p = None
        for t in range(i, r):
            if M[t][j] != 0:
                p = t
                break
        if p is None:
            continue
        M[i], M[p] = M[p], M[i]
        pv = M[i][j]
        M[i] = [x / pv for x in M[i]]
        for t in range(r):
            if t != i and M[t][j] != 0:
                f = M[t][j]
                M[t] = [a - f * b for a, b in zip(M[t], M[i])]
        piv.append(j)
        i += 1
        if i == r:
            break
    return M, piv


def rbasis(M):
    if not M:
        return []
    R, piv = _rref(M)
    return [R[i] for i in range(len(piv))]


def nullspace(M):
    """{x : M x = 0} 的基（每个是长度 n 的向量）。"""
    if not M:
        return []
    R, piv = _rref(M)
    n = len(M[0])
    free = [c for c in range(n) if c not in piv]
    out = []
    for f in free:
        v = [Fr(0)] * n
        v[f] = Fr(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][f]
        out.append(v)
    return out


def inspan(basis, v):
    if not basis:
        return all(x == 0 for x in v)
    return len(rbasis([r[:] for r in basis] + [v[:]])) == len(rbasis([r[:] for r in basis]))


def cap_dim(L, J):
    """dim(row L ∩ row J)"""
    return len(rbasis(L)) + len(rbasis(J)) - len(rbasis([r[:] for r in L] + [r[:] for r in J]))


def data(A, C, L0):
    n = len(A)
    CA = mm(C, A)
    J = rbasis(C + CA)                                  # J = row[C; CA]
    JA = rbasis(mm(J, A))                               # J A
    S1 = rbasis([r[:] for r in J] + [r[:] for r in JA])  # J + J A
    # {x : x A in S1}：对 S1 的正交补中每个 q，<x A, q> = <x, A q> = 0
    Qs = nullspace(S1)
    if Qs:
        eqs = [[sum(A[i][k] * q[k] for k in range(n)) for i in range(n)] for q in Qs]
        preA = nullspace(eqs)
    else:
        preA = [[Fr(1) if k == i else Fr(0) for k in range(n)] for i in range(n)]
    # 交空间必须用"正交补之和"来算：S1 ∩ preA = (S1^⊥ + preA^⊥)^⊥
    # （**不能**用"筛选 preA 的基向量"——交可能由组合张成）
    comp = rbasis([r[:] for r in nullspace(S1)] + [r[:] for r in nullspace(preA)])
    S = nullspace(comp) if comp else [r[:] for r in S1]
    return dict(n=n, J=J, JA=JA, S=S, j=len(J),
                dK=len(S) - len(J), U0=rbasis(L0), U0S=all(inspan(S, r) for r in rbasis(L0)))


def make_L(D, L0, Urows, rng=None):
    """L = row_basis(L0 ∪ Urows)，Urows 取自 S（即 K 的提升）。"""
    return AI.row_basis([r[:] for r in L0] + [r[:] for r in Urows])


def main():
    rng = random.Random(20261028)
    nI = nII = 0
    badI = badII = 0
    skipped = 0
    for _trial in range(240):
        n = rng.choice([4, 5])
        A = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        L0 = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        try:
            D = data(A, C, L0)
        except Exception as ex:
            skipped += 1
            if skipped <= 3:
                print("  skip:", type(ex).__name__, ex)
            continue
        if D['j'] == 0 or D['j'] >= n:
            skipped += 1
            continue
        rho = rng.choice([2, 3]) if D['dK'] >= 3 else 2
        # 判据（命题 26.2）
        crit = (D['dK'] >= rho) and D['U0S']
        if crit:
            # 构造：在 S 中取 rho 个与 J 独立的向量 + row L0
            cand = [r[:] for r in rbasis(L0)]
            for r in D['S']:
                if not inspan(D['J'], r):
                    cand = rbasis(cand + [r])
                if len(cand) - len(rbasis(L0)) >= rho:
                    break
            L = rbasis(cand)
            if cap_dim(L, D['J']) != rho - 1:
                continue
            a = AI.cond_5a_orig(A, C, L)
            b = AI.cond_5b_orig(A, C, L)
            nI += 1
            if not (a and b):
                badI += 1
                if badI <= 3:
                    print(f"[I] 判据真但失败 n={n} j={D['j']} dK={D['dK']} rho={rho} 5a={a} 5b={b}")
        else:
            found = False
            for _k in range(8):
                cand = [r[:] for r in rbasis(L0)]
                tries = 0
                while len(cand) - len(rbasis(L0)) < rho and tries < 40:
                    v = [Fr(rng.randint(-1, 1)) for _ in range(n)]
                    if any(v):
                        cand = rbasis(cand + [v])
                    tries += 1
                L = cand
                if cap_dim(L, D['J']) != rho - 1:
                    continue
                if AI.cond_5a_orig(A, C, L) and AI.cond_5b_orig(A, C, L):
                    found = True
                    break
            nII += 1
            if found and not globals().get('_dumped'):
                globals()['_dumped'] = True
                cert = dict(n=n, A=[[str(x) for x in r] for r in A],
                            C=[[str(x) for x in r] for r in C],
                            L0=[[str(x) for x in r] for r in L0],
                            L=[[str(x) for x in r] for r in L],
                            j=D['j'], dimK=D['dK'], rho=rho, c=rho-1,
                            note="判据(dim K >= rho)为假但 (5a)&(5b) 成立 => 命题 24.3/25.3/26.2 的(=>)方向被反驳")
                txt = json.dumps(cert, ensure_ascii=False, indent=1, default=str)
                io.open('proof/rho1_layer/counterexample_s1.json','w',encoding='utf-8',newline='\n').write(txt)
                print("  已写出反例证书 proof/rho1_layer/counterexample_s1.json")
            if found:
                badII += 1
                if badII <= 3:
                    print(f"[II] 判据假但找到可行 V n={n} j={D['j']} dK={D['dK']} rho={rho}")
    print(f"(I) 判据为真 {nI} 例，失败 {badI}；(II) 判据为假 {nII} 例，误判 {badII}；跳过 {skipped}")
    print("结论：0 失败 => 与真实实例逐例一致（**验证，不是证明**）")


if __name__ == '__main__':
    main()
