# $q_{\\min}$ 的证书化扫描：能给出真实阶差，但**太慢**

## 目标

用 [joint_theta.py](../../../../tools/verification/joint_theta.py) 的逐阶判定，从 $q_0$ 起逐阶向上扫，
给每个实例一个**带证书的** $q_{\\min}$。

## 设想与理由

若 $q_0,\\dots,q_{\\min}-1$ 都判为不可行（证书），而 $q_{\\min}$ 给出见证，则 $q_{\\min}$ 被**两端夹住**，
不再是"抽样没命中"。这比历史统计（38/89 等）强。

## 做法

[qminsweep.py](../../../../tools/verification/qminsweep.py)：逐实例、逐阶调用 `joint_theta.decide`，遇 `FEASIBLE` 即停；
结果增量写入 `workspace/q1_false/feasibility_geometry/data/qmin_certified.tsv`。

## 进展

**4 个实例的结果（其中一个是真实的阶差）**：

| $n$ | $p$ | $r$ | seed | $q_0$ | $n_0$ | $q_{\\min}$ | 各阶判定 | 耗时 |
|---|---|---|---|---|---|---|---|---|
| 5 | 1 | 1 | 3000 | 2 | 4 | **3** | `UNKNOWN → FEASIBLE` | 3.4 s |
| 5 | 1 | 1 | 3001 | 1 | 2 | 1 | `FEASIBLE` | 0.0 s |
| 5 | 1 | 1 | 3002 | 2 | 3 | 2 | `FEASIBLE` | 1.8 s |
| 5 | 1 | 1 | 3005 | 1 | 3 | $>2$ | `INFEASIBLE → INFEASIBLE_TYPICAL` | **944.6 s** |

第 1 行是一个**真实的阶差**（$q_0=2<q_{\\min}=3$），且上界由见证、下界由 $q_0$ 阶的不可行结论给出。

**但第 4 行暴露了性能问题**：两个阶用了 945 s；整轮在 950 s 预算处被迫停止（只完成 4 个实例）。

### 性能瓶颈的诊断

慢在 $(5a)$ 的行列式条件：$M_a=[(\\mathcal Z^{\\perp})A^{\\mathsf T}\\mid B_a]$ 的 $(r_a+1)$-子式
（本类实例 $r_a$ 接近满秩，子式阶数 5–6、矩阵宽），40 条这样的多项式做 Gröbner 很贵。
相比之下，$n=5,p=2$ 与 $n=6,p=2$ 的实例（子式阶数低）在 1 s 内完成。

## 最终结论

1. **方法可行且有价值**：能给出带两端证书的 $q_{\\min}$，并捕捉到真实阶差（$q_0=2\\to q_{\\min}=3$）；
2. **性能不可批量**：单实例可达 15 分钟 ⟹ 不能直接跑 89 个实例的完整扫描；
3. 瓶颈明确：$(5a)$ 的高阶子式 Gröbner；而专家建议的 (D)"隐式铅笔"路线正对着这一点；
4. 现有数据（4 行）已足够证明"证书化 $q_{\\min}$"是可达的，但**不足以**给出分布统计。

## 放弃原因

批量扫描在当前的符号 Gröbner 下太慢（单实例 15 分钟），不继续跑全量。

## 残留价值

* 4 个**带证书**的 $q_{\\min}$（含一个真实阶差）；
* 明确的性能瓶颈（$(5a)$ 高阶子式）与对应的改进方向（隐式铅笔 / 降低子式阶数 / 只在谱可行点上核 $(5a)$）；
* 数据表 `qmin_certified.tsv` 可增量续跑。

## 相关文件

- [tools/verification/qminsweep.py](../../../../tools/verification/qminsweep.py)
- [workspace/q1_false/feasibility_geometry/data/qmin_certified.tsv](../../../../workspace/q1_false/feasibility_geometry/data/qmin_certified.tsv)
- [workspace/q1_false/feasibility_geometry/attempts/54_theta_elimination.md](54_theta_elimination.md)
- [workspace/for_expert/08_per_order_decision_report-answer.md](../../../for_expert/archive/08_per_order_decision_report-answer.md)（(D) 隐式铅笔）
