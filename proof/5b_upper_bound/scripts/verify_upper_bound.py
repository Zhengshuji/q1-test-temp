r"""
verify_upper_bound.py -- 独立检查 (5b) 的上界与修正后的 cond_5b

本脚本做三件事：

1. 矩阵形式的上界：对随机 Lam, H, lam，检查
       rank(lam*H - Lam*H) <= rank(H).
2. 约化铅笔 + 对角 Lambda 的**完整** (5b) 检验：
   Lambda 取对角（特征值已知为 lams），F = Lambda*M。
   此时铅笔只能在 lam = lams[i] 处降秩，故"逐个检查这些 lam"是完整的；
   把 cond_5b(M,F) 与这个精确结果对比。
3. cond_5b 的回归：假阳性用例、rho=0 用例、合法 (5b) 用例。

跑法：
    python proof/5b_upper_bound/scripts/verify_upper_bound.py
"""
import os
import sys
import random
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_CORE = os.path.abspath(os.path.join(_HERE, "..", "..", "..", "scripts", "core"))
if _CORE not in sys.path:
    sys.path.insert(0, _CORE)

from exact_gcd import cond_5b, cond_5b_diagnose, _rank  # noqa: E402


def matmul(X, Y):
    n, k, m = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(m)]
            for i in range(n)]


def scalar_mul(c, X):
    return [[c * x for x in row] for row in X]


def sub(X, Y):
    return [[X[i][j] - Y[i][j] for j in range(len(X[0]))]
            for i in range(len(X))]


def rand_mat(rng, q, d, lo=-2, hi=2):
    return [[Fr(rng.randint(lo, hi)) for _ in range(d)] for _ in range(q)]


def diag(lams):
    n = len(lams)
    return [[lams[i] if i == j else Fr(0) for j in range(n)] for i in range(n)]


def check_matrix_upper_bound(trials=200, q=4, d=3, seed=20261021):
    rng = random.Random(seed)
    for _ in range(trials):
        Lam = rand_mat(rng, q, q)
        H = rand_mat(rng, q, d)
        lam = Fr(rng.randint(-3, 3))
        lhs = sub(scalar_mul(lam, H), matmul(Lam, H))
        assert _rank(lhs) <= _rank(H), "matrix upper bound failed"
    print("[1] matrix upper bound: %d/%d OK" % (trials, trials))


def check_cond_5b_diagonal(trials=60, q=4, d=3, seed=20261022):
    rng = random.Random(seed)
    ok = 0
    for _ in range(trials):
        lams = [Fr(rng.randint(-2, 2)) for _ in range(q)]
        Lam = diag(lams)
        M = rand_mat(rng, q, d)
        F = matmul(Lam, M)
        rho = _rank(M)
        # Lambda is diagonal: (5b) can only fail at lam in lams.
        # Checking every diagonal entry is therefore a complete exact test.
        exact = True
        for lam in lams:
            P = sub(scalar_mul(lam, M), F)
            if _rank(P) != rho:
                exact = False
                break
        got = cond_5b(M, F)
        assert got == exact, (
            "cond_5b mismatch: got=%s exact=%s rho=%d lams=%s"
            % (got, exact, rho, lams))
        ok += 1
    print("[2] cond_5b vs exact diagonal-Lambda test: %d/%d OK" % (ok, trials))


def check_regressions():
    # false positive: normal rank 2 > rho = 1
    M3 = [[Fr(1), Fr(0)], [Fr(0), Fr(0)]]
    F3 = [[Fr(0), Fr(0)], [Fr(0), Fr(1)]]
    d3 = cond_5b_diagnose(M3, F3)
    assert d3["upper_ok"] is False and d3["ok"] is False
    print("[3] false-positive case rejected: OK (%s)" % d3)

    # rho = 0: (5b) <=> F = 0
    M0 = [[Fr(0), Fr(0)], [Fr(0), Fr(0)]]
    F0 = [[Fr(0), Fr(0)], [Fr(0), Fr(0)]]
    assert cond_5b(M0, F0) is True
    assert cond_5b(M0, F3) is False
    print("[4] rho=0 case: OK")

    # a genuine (5b): 3x2 M, F = Lambda*M, no rank drop
    M5 = [[Fr(1), Fr(0)], [Fr(0), Fr(1)], [Fr(0), Fr(0)]]
    F5 = [[Fr(0), Fr(0)], [Fr(1), Fr(0)], [Fr(0), Fr(1)]]
    d5 = cond_5b_diagnose(M5, F5)
    assert d5["ok"] is True
    print("[5] genuine (5b) case accepted: OK (%s)" % d5)


def main():
    print("=" * 70)
    print("(5b) 上界与 cond_5b 的独立检查")
    print("=" * 70)
    check_matrix_upper_bound()
    check_cond_5b_diagonal()
    check_regressions()
    print("-" * 70)
    print("全部通过 ✓")


if __name__ == "__main__":
    main()
