r"""
verify_5a.py -- (5a) 三种等价形式的独立检查

检查：
  (5a) 的 4 块秩形式  rank[LA; L; CA; C] = rank[L; CA; C]
  (A) 的行包含形式    row(LA) ⊆ row(L, CA, C)          （库的 condA）
  核条件形式          ker[L; CA; C] ⊆ ker(LA)

以及 p1 给出的最小 (A)-增广：
  rows(Lx) = q0 = sum(eta)，且 (5a) 成立。

用法：
    python proof/5a_archive/scripts/verify_5a.py
"""
import os
import io
import sys
import random
import contextlib
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_CORE = os.path.abspath(os.path.join(_HERE, "..", "..", "..", "scripts", "core"))

# 用项目的标准做法加载库（避免库文件末尾的 demo 打印）
_NS = {}
with open(os.path.join(_CORE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _NS)

rk = _NS["rk"]
mm = _NS["mm"]
ker_basis = _NS["ker_basis"]
p1 = _NS["p1"]
condA = _NS["condA"]


def rank4(L, A, C):
    """rank[LA; L; CA; C]"""
    return rk(mm(L, A) + L + mm(C, A) + C)


def rank3(L, A, C):
    """rank[L; CA; C]"""
    return rk(L + mm(C, A) + C)


def condA_direct(L, A, C):
    """4 块秩形式。"""
    return rank4(L, A, C) == rank3(L, A, C)


def condA_kernel(L, A, C):
    """核条件：ker[L; CA; C] ⊆ ker(LA)。"""
    K = ker_basis(L + mm(C, A) + C)
    if not K or not K[0]:
        return True
    return rk(mm(mm(L, A), K)) == 0


def rand_instance(rng, n=5, p=1, r=1):
    for _ in range(200):
        A = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        L0 = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(r)]
        if rk(C) != p or rk(L0) != r or rk(L0 + C) != r + p:
            continue
        N = ker_basis(C + mm(C, A))
        if not N or not N[0]:
            continue
        return A, C, L0
    return None


def main():
    print("=" * 72)
    print("(5a) 三种等价形式 + p1 最小增广的独立检查")
    print("=" * 72)

    rng = random.Random(20261021)
    n_true = n_false = 0
    n_inst = 0
    n_p1 = 0

    for t in range(12):
        inst = rand_instance(rng)
        if inst is None:
            continue
        A, C, L0 = inst
        n_inst += 1

        # 1) p1 的最小 (A)-增广
        with contextlib.redirect_stdout(io.StringIO()):
            Lx, eta = p1(A, C, L0)
        q0 = sum(eta)
        assert len(Lx) == q0, "p1: rows(Lx)=%d != q0=%d" % (len(Lx), q0)
        assert condA(A, C, Lx), "p1: minimal augmentation fails (5a)"
        assert condA_direct(Lx, A, C), "p1: 4-block form disagrees"
        assert condA_kernel(Lx, A, C), "p1: kernel form disagrees"
        n_p1 += 1

        # 2) 随机的 L（含 (5a) 成立与不成立的样本）
        for k in range(4):
            R = [[Fr(rng.randint(-1, 1)) for _ in range(len(A))] for _ in range(k)]
            L = [row[:] for row in L0] + R
            a = condA(A, C, L)
            b = condA_direct(L, A, C)
            c = condA_kernel(L, A, C)
            assert a == b == c, (
                "t=%d k=%d: condA=%s direct=%s kernel=%s" % (t, k, a, b, c))
            if a:
                n_true += 1
            else:
                n_false += 1

    print("实例数：%d；p1 最小增广检查：%d" % (n_inst, n_p1))
    print("随机 L 样本：(5a) 成立 %d，不成立 %d" % (n_true, n_false))
    assert n_true > 0 and n_false > 0, "地基检查：必须同时有 True 与 False 样本"
    print("-" * 72)
    print("三种形式一致；p1 的 q0=sum(eta) 与 (5a) 均通过 ✓")


if __name__ == "__main__":
    main()
