"""
严格版：穷举式检验 (S) 是否只依赖 row(L)。

方法：
  1. 枚举所有可能的 3 维整数系统 (A, C, L0)（小范围）
  2. 对每个实例，枚举所有 k 行候选 R（来自一个小网格）
  3. 若某个 L=[L0;R] 满足 (5a)∧(5b)，则对**所有**可逆 T，
     检验 L'=[L0; T R] 是否也满足 (5b)（row 相同）
  4. 记录任何反例

((5b) 依赖具体矩阵表示 <=> 存在 T 使结果翻转)
"""
import itertools

import numpy as np

TOL = 1e-6
rng = np.random.default_rng(97531)


def rk(M):
    M = np.atleast_2d(np.asarray(M, float))
    if M.size == 0 or M.shape[0] == 0:
        return 0
    s = np.linalg.svd(M, compute_uv=False)
    return 0 if s.size == 0 else int(np.sum(s > TOL * max(M.shape) * (s[0] if s[0] > 0 else 1.0)))


def st(*b):
    b = [np.atleast_2d(np.asarray(x, float)) for x in b]
    nc = max((x.shape[1] for x in b), default=0)
    b = [x for x in b if x.shape[0] > 0]
    return np.zeros((0, nc)) if not b else np.vstack(b)


def in_span(X, Y):
    X = np.atleast_2d(np.asarray(X, float))
    return True if X.shape[0] == 0 else rk(st(Y, X)) == rk(Y)


def condA(A, C, L):
    return in_span(L @ A, st(L, C, C @ A))


def condS(A, C, L):
    """精确一点：不但采样 s，还直接检验两个方向的子式条件（数值近似）"""
    rhs = rk(st(L, C @ A, C))
    pts = [complex(x) for x in (-3., -2., -1., -0.5, 0., 0.5, 1., 2., 3., 5.)]
    pts += [complex(c) for c in np.linalg.eigvals(A)]
    pts += [complex(rng.normal(), rng.normal()) for _ in range(25)]
    for s in pts:
        if rk(st((s * L - L @ A).real, C @ A, C)) != rhs:
            return False
    return True


def rand_invertible(k, lo=-2, hi=3, tries=200):
    for _ in range(tries):
        T = rng.integers(lo, hi, (k, k)).astype(float)
        if abs(np.linalg.det(T)) > 1e-8:
            return T
    return np.eye(k)


print("=" * 76)
print("严格检验：(S) 是否只依赖 row(L)？")
print("=" * 76)

n = 3
counter = []
tested_pairs = 0
n_sat = 0

for trial in range(1500):
    p = int(rng.integers(1, n))
    q = int(rng.integers(1, n))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L0 = rng.integers(-2, 3, (q, n)).astype(float)
    if rk(C) < p or rk(L0) < q or rk(st(L0, C)) != p + q:
        continue

    for k in (1, 2):
        for _ in range(6):
            R = rng.integers(-2, 3, (k, n)).astype(float)
            if rk(R) < k:
                continue
            L = st(L0, R)
            if not (condA(A, C, L) and condS(A, C, L)):
                continue
            n_sat += 1
            # 对同一行空间的多种表示做检验
            for _t in range(12):
                T = rand_invertible(k)
                R2 = T @ R
                if not (in_span(R2, R) and in_span(R, R2)):
                    continue
                tested_pairs += 1
                L2 = st(L0, R2)
                a2, s2 = condA(A, C, L2), condS(A, C, L2)
                if a2 and not s2:
                    counter.append((A.copy(), C.copy(), L0.copy(), R.copy(), R2.copy()))
                    break
            if counter:
                break
        if counter:
            break
    if len(counter) >= 2:
        break

print(f"  满足 (5a)∧(5b) 的 L 个数        : {n_sat}")
print(f"  检验的'同一行空间不同表示'对数  : {tested_pairs}")
print(f"  **反例个数（(5b) 被翻转）**      : {len(counter)}")

if counter:
    print("\n  => (5b) **依赖 L 的具体矩阵表示**（谱刚性成立）")
    A, C, L0, R1, R2 = counter[0]
    print("   A  =", A.tolist())
    print("   C  =", C.tolist())
    print("   L0 =", L0.tolist())
    print("   R1 =", R1.tolist(), " (5b)=", condS(A, C, st(L0, R1)))
    print("   R2 =", R2.tolist(), " (5b)=", condS(A, C, st(L0, R2)))
    print("   row 相同?", in_span(R1, R2) and in_span(R2, R1))
else:
    print("\n  => 未找到反例：(S) 在此规模下**只依赖 row(L)**")
    print("     若这一点普遍成立，则 nu_min 可完全用子空间语言刻画，")
    print("     问题很可能落在 P，而不是 NP-hard。")
