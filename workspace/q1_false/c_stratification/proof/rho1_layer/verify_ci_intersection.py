"""条件不变子空间对**交**是否封闭？—— 答案是 **否**（2026-10-29 专家给出反例，已核对）。

历史教训：本脚本的旧版本用 `close(U) = U + U A` 迭代生成子空间，那生成的是 **A-不变** 子空间，
而 A-不变**确实**对交封闭 => 旧的 44/44 是在真子类上做的**空测试** ✗。
本版本：
  (1) 先跑专家反例（必须得到 False）；
  (2) 再在随机 c.i. 子空间（用**正确**的闭包迭代，见 §26.3 已撤回 hmm —— 这里用随机 c.i. 子空间对）上统计。
"""
import random, sys
from fractions import Fraction as Fr
sys.path.insert(0, 'tools/exact_linalg')
import audit_independent as AI
import importlib.util
spec = importlib.util.spec_from_file_location('Q', 'proof/rho1_layer/quotient_selfcheck.py')
Qm = importlib.util.module_from_spec(spec); spec.loader.exec_module(Qm)
mm, rank, rb = Qm.mm, Qm.rank, Qm.rb


def is_ci(U, A, B):
    return rank(mm(U, A) + U + B) == rank(U + B)


def counterexample():
    """专家反例：C^3, B = span(e1), A e2 = e3; U = span(e2,e3), V = span(e2, e1+e3)."""
    A = [[Fr(0), Fr(0), Fr(0)], [Fr(0), Fr(0), Fr(1)], [Fr(0), Fr(0), Fr(0)]]
    B = [[Fr(1), Fr(0), Fr(0)]]
    U = [[Fr(0), Fr(1), Fr(0)], [Fr(0), Fr(0), Fr(1)]]
    V = [[Fr(0), Fr(1), Fr(0)], [Fr(1), Fr(0), Fr(1)]]
    rows = [[U[i][k] for i in range(len(U))] + [-V[j][k] for j in range(len(V))] for k in range(3)]
    inter = []
    for sol in AI.nullspace(rows):
        v = [sum(sol[i] * U[i][k] for i in range(len(U))) for k in range(3)]
        if any(v):
            inter.append(v)
    I = rb(inter)
    return (is_ci(U, A, B), is_ci(V, A, B), is_ci(I, A, B), [[str(x) for x in r] for r in I])


def main():
    u, v, i, Irows = counterexample()
    print(f"专家反例：U c.i.={u}（应 True）, V c.i.={v}（应 True）, U∩V={Irows}, (U∩V) c.i.={i}（应 False）")
    assert u and v and not i, "反例核对失败！"
    print("=> 条件不变子空间**不**对交封闭 ✗（旧的 44/44 是 A-不变子类上的空测试）")


if __name__ == '__main__':
    main()
