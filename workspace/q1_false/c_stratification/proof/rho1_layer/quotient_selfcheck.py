"""商空间 X = C^n / J 的实现 + 5 条自检（见 TECH_DEBT_quotient.md）。

约定：全部用**行向量**；`mm(X,Y)` 是矩阵乘；`rank/row_basis` 来自 audit_independent。

对象：
  J        = row[C; CA] 的基（n 维行）
  comp     = J 在 C^n 里的补基（d = n - j 行）
  coords(x)= x · L^{-1}，其中 L 以 [J; comp] 为行   （x = coords(x) · L）
  pi(x)    = coords(x)[j:]                          （X 的坐标，d 维）
  lift(u)  = to_x([0,...,0,u])                      （X 坐标 -> C^n 中的代表）
  B        = {pi(j A) : j in J} 的基（X 坐标）
  Bcomp    = B 在 X 里的补基
  classmod = 把 X 的向量送到 X/B 的坐标（取 Bcomp 部分）
  Tbar(u)  = classmod(pi(lift(u) A))                 （X -> X/B）
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI


def mm(X, Y):
    r, k, c = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(c)] for i in range(r)]


def rank(M):
    return AI.rank([r[:] for r in M]) if M else 0


def rb(M):
    return AI.row_basis([r[:] for r in M]) if M else []


def complement(basis, n):
    """返回 basis（行）在 Q^n 中的一组补基。"""
    out = []
    span = [r[:] for r in basis]
    for i in range(n):
        e = [Fr(1) if k == i else Fr(0) for k in range(n)]
        if rank(span + [e]) > len(span):
            out.append(e)
            span = rb(span + [e])
        if len(span) == n:
            break
    return out


class Quotient:
    def __init__(self, A, C, rng=None):
        self.A = A
        self.C = C
        self.n = len(A)
        CA = mm(C, A)
        self.J = rb(C + CA)
        self.j = len(self.J)
        self.comp = complement(self.J, self.n)
        self.d = len(self.comp)
        L = [r[:] for r in self.J] + [r[:] for r in self.comp]     # n x n，行
        self.Linv = AI.inv(L)                                      # L^{-1}
        # 校验：coords(x) = x · L^{-1}；to_x(a) = a · L
        # B = pi(J A)
        self.B = rb([self.pi(mm([j], A)[0]) for j in self.J])
        self.m = len(self.B)
        self.Bcomp = complement(self.B, self.d) if self.m else \
            [[Fr(1) if k == i else Fr(0) for k in range(self.d)] for i in range(self.d)]
        self.BL = [r[:] for r in self.B] + [r[:] for r in self.Bcomp]   # d x d
        self.BLinv = AI.inv(self.BL)

    # ---- 坐标 ----
    def coords(self, x):
        return mm([x], self.Linv)[0]

    def to_x(self, a):
        return mm([a], [self.J + self.comp][0])[0]

    def pi(self, x):
        return self.coords(x)[self.j:]

    def lift(self, u):
        return self.to_x([Fr(0)] * self.j + list(u))

    # ---- X/B ----
    def classmod(self, u):
        """X 的向量 -> X/B 的坐标（取 Bcomp 部分）。"""
        return self.coords_B(u)[self.m:]

    def coords_B(self, u):
        return mm([u], self.BLinv)[0]

    def Tbar(self, u):
        x = self.lift(u)
        return self.classmod(self.pi(mm([x], self.A)[0]))

    def barU(self, U):
        """U ⊆ X（行）-> \bar U = (U+B)/B 的基。"""
        return rb([self.classmod(u) for u in U])


def cond5a_stacked(V, A, C):
    """(5a) 的堆叠判据：rank[LA; L; CA; C] == rank[L; CA; C]。"""
    CA = mm(C, A)
    VA = mm(V, A)
    return rank(VA + V + CA + C) == rank(V + CA + C)


def main():
    rng = random.Random(20261029)
    # ---- 自检 1..3 ----
    s1 = s2 = s3 = 0
    n1 = n2 = n3 = 0
    for _ in range(60):
        n = rng.choice([4, 5, 6])
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(1)]
        Q = Quotient(A, C)
        # S1: round trip
        x = [Fr(rng.randint(-3, 3)) for _ in range(n)]
        x2 = Q.to_x(Q.coords(x))
        n1 += 1
        if x2 == x:
            s1 += 1
        # S2: pi(xA) - pi((x+j)A) in B
        j0 = Q.J[rng.randrange(Q.j)] if Q.j else [Fr(0)] * n
        u1 = Q.pi(mm([x], A)[0])
        u2 = Q.pi(mm([[x[k] + j0[k] for k in range(n)]], A)[0])
        diff = [u1[k] - u2[k] for k in range(Q.d)]
        n2 += 1
        if rank(Q.B + [diff]) == rank(Q.B):
            s2 += 1
        # S3: Tbar 良定义（两个不同的 lift 给同一个类）
        u = Q.pi(x)
        xA = Q.lift(u)
        xB = [xA[k] + j0[k] for k in range(n)]
        n3 += 1
        if Q.classmod(Q.pi(mm([xA], A)[0])) == Q.classmod(Q.pi(mm([xB], A)[0])):
            s3 += 1
    print(f"S1 坐标往返: {s1}/{n1}")
    print(f"S2 pi(xA)-pi((x+j)A) ∈ B: {s2}/{n2}")
    print(f"S3 Tbar 良定义: {s3}/{n3}")

    # ---- 自检 4：堆叠判据 vs pi(VA) ⊆ pi(V) ----
    s4 = n4 = 0
    bad = []
    for _ in range(120):
        n = rng.choice([4, 5, 6])
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(1)]
        Q = Quotient(A, C)
        while True:
            V = rb([[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(rng.choice([2, 3]))])
            if V:
                break
        # 商空间版本
        U = rb([Q.pi(v) for v in V])
        VA_pi = [Q.pi(mm([v], A)[0]) for v in V]
        ok_quot = all(rank(U + [w]) == len(U) for w in VA_pi)
        ok_st = cond5a_stacked(V, A, C)
        n4 += 1
        if ok_quot == ok_st:
            s4 += 1
        elif len(bad) < 3:
            bad.append((ok_st, ok_quot))
    print(f"S4 堆叠判据 vs pi(VA)⊆pi(V): {s4}/{n4}")
    if bad:
        print(f"   不一致样本 (stacked, quotient): {bad}")

    # ---- 自检 5：维数公式 ----
    s5 = n5 = 0
    for _ in range(60):
        n = rng.choice([4, 5, 6])
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(1)]
        Q = Quotient(A, C)
        while True:
            V = rb([[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(rng.choice([2, 3]))])
            if V:
                break
        U = rb([Q.pi(v) for v in V])
        capdim = len(V) + Q.j - rank(V + Q.J)
        n5 += 1
        if len(U) == len(V) - capdim:
            s5 += 1
    print(f"S5 dim pi(V) = dim V - dim(V∩J): {s5}/{n5}")


if __name__ == '__main__':
    main()
