# `decide_full`（分层 + $(*)$ 的完整判定）：**未打通**，记录缺陷

## 目标

把 [attempts/49](49_rank_stratified_impl.md) 的单参数可行判定，扩成"任意参数 + 不可行方向也判"的完整逐阶判定。

## 设想与理由

对每个 $\rho$ 层：理想 $I_\rho=(g,C_j)$ 的 Gröbner 基 $=[1]$ ⟹ 该层空；否则用 Rabinowitsch 找层内点。
若所有层都空 ⟹ 该图卡不可行。这应该能同时给出可行见证与不可行证书。

## 做法

[decide_full.py](../../../../tools/verification/decide_full.py)：实现上述流程（含 `try_point` 取有理点、
七条一致性检查、预算 CAP_MINORS=40）。

## 进展

**当前状态：不可用。** 所有被测实例都返回 `UNKNOWN`，且原因暴露两处实现缺陷：

1. **左零空间被算成空**（`auto-but-no-point`）：在 C4 的 $\rho=3$ 层上，本模块得到的
   $M_\rho$ 左零空间为空（"满行秩"），而 [bezout_rank_test.py](../../../../tools/verification/bezout_rank_test.py)
   在**同一层、同一尺寸**上得到左零维数 2 且 $C_j\ne0$，理想为 $(1)$。两者矛盾，
   说明本模块的极大子式集合（或 $D$ 的取值）与已验证版本不一致——最可能是
   `pen_minors` 与 `build_minors` 在"非零过滤 / D 的取法"上不同（例如把在 $(\theta,\lambda)$ 上非零、
   但在 $\lambda$ 上退化的子式混入，改变了 $M$ 的形状）。
2. **`try_point` 在 `gens` 为空时不搜索**（直接用 `sp.solve([], tam)` ⟹ 无候选），
   于是"层内处处可行"的情形也拿不到见证。

## 最终结论

1. `decide_full` **未打通**，不应作为判定工具使用；本轮的产出是**缺陷定位**，不是结果；
2. **已验证可用的**仍是两件：
   * [bezout_rank_test.py](../../../../tools/verification/bezout_rank_test.py)：C4 的第三个独立证书（理想 $(1)$）；
   * [rank_stratified.py](../../../../tools/verification/rank_stratified.py)：单参数图卡的可行方向（4 个带见证的实例）；
3. 修复方向明确：让 `decide_full` 复用 `bezout_rank_test.build_minors` 的**同一套**子式构造与 $D$ 约定，
   并让 `try_point` 在无等式约束时按"抽样 + 层条件"取点。

## 放弃原因

实现层面（子式集合与 $D$ 的约定不一致、空约束时的取点缺失）。属于**工程缺陷**，不是数学障碍。

## 残留价值

* 一个**明确的缺陷定位**：两个模块对"极大子式集合"的处理不一致，这是此前若干矛盾输出的共同原因；
* 提醒：在把多个符号工具串起来之前，必须先统一"子式枚举 / 次数界 / 尺寸"三个约定——
  这与 CLAUDE §10.1（"矩阵乘法不检查维数"）是同一类风险。

## 相关文件

- [tools/verification/decide_full.py](../../../../tools/verification/decide_full.py)
- [tools/verification/bezout_rank_test.py](../../../../tools/verification/bezout_rank_test.py)
- [tools/verification/rank_stratified.py](../../../../tools/verification/rank_stratified.py)
- [workspace/q1_false/feasibility_geometry/attempts/49_rank_stratified_impl.md](49_rank_stratified_impl.md)
