# A 的收尾：工具覆盖表（哪些能用、哪些不能用、为什么）

## 目标

把"逐阶判定工具箱"整理成**可信的状态**：明确每个工具覆盖什么、不覆盖什么、
哪些**不可用**（避免后续误用）。

## 设想与理由

`decide_full`（[attempts/50](50_decide_full_defect.md)）与 `decide_strata` 属于"完整判定"的尝试：
前者因三处约定不一致而错，后者因**双重分层 + Rabinowitsch**（每个组合一次 Gröbner，含 2 个饱和变量）
在实际规模上超时。与其继续堆，不如把**已验证的部分**固定下来，并标清边界。

## 做法

对每个工具做一次"覆盖 × 可靠性"的核对（依据各自的实测输出），整理成表；并把不可用的标注清楚。

## 进展

| 工具 | 方向 | 覆盖 | 状态 |
|---|---|---|---|
| `toeplitz_criterion.py` | $(5b)$（固定增广）| 任意 $n$（有理算术）| ✅ 可用；与 Smith 66/66 |
| `spectral_gcd.py` | $(5b)$（极大子式 gcd）| 任意 | ✅ 可用（独立证书）|
| `consistency_checks.py` | 七条一致性检查 | 任意 | ✅ 可用；新脚本必须调用 |
| `verify_Q1_nullspace.py` | 零空间铅笔（含精确 gcd 版）| 任意 | ✅ 可用；与上两者 6/6 |
| `decide_with_certificate.py` | 逐阶判定（证书式）| 小 $n$ | ✅ 可用：只报 `FEASIBLE`/`INFEASIBLE_*`/`UNKNOWN` |
| `bezout_rank_test.py` | $(*)$ 判据 | 秩恒定的图卡 | ✅ 可用：C4 的第三证书 |
| `rank_stratified.py` | 秩分层 + $(*)$ | **单参数**图卡的可行方向 | ✅ 可用：4 个实例带见证 |
| `chart_gcd_analysis.py` | 逐图卡符号 gcd | 参数 $\le3$ | ✅ 可用（给典型次数与公共因子）|
| `dim_Y.py` | 坏点像闭包维数 | 映射有定义时 | ✅ 可用（C4：$\dim Y=1$）|
| `drop_locus.py` | 跌落候选 | 单参数 | ⚠️ 部分（候选集不完备）|
| `fast_feasible.py` | 满行秩充分判据 | 任意 | ⚠️ 有效但**几乎不触发** |
| `decide_full.py` | 完整判定（分层）| — | ❌ **不可用**（约定不一致）|
| `decide_strata.py` | 完整判定（双重分层）| — | ❌ **不可用**（Gröbner 超时）|

## 最终结论

1. **A 的完成形态**：不是"完整判定器"，而是**"证书式判定 + 明确的覆盖边界"**——
   凡是工具给出的 `FEASIBLE`/`INFEASIBLE` 都带证书（见证或空集），其余一律 `UNKNOWN`；
2. **未完成的部分有明确的失败原因**：`decide_full` 是三处约定不一致（工程）；
   `decide_strata` 是双重分层的 Gröbner 代价（组合学）——两者都已标注，不再使用；
3. **这套工具的净能力**：
   * 固定增广的 $(5b)$：完全可判（三条独立判据）；
   * 逐阶判定：单参数图卡可行方向可判；秩恒定图卡的不可行方向可判（C4）；其余 `UNKNOWN`。

## 放弃原因

"完整逐阶判定器"在纯符号路线上的代价过高（双重分层 × Rabinowitsch），本会话不继续。

## 残留价值

* 一张**工具覆盖表**（可用/部分/不可用 + 依据），可直接用于交接与写作；
* 明确了 `UNKNOWN` 的语义：不是"没做"，而是"没有证书"；
* 为 B（规模测量）提供了正确的入口：B 只需数结构与测时间，不依赖不可用的工具。

## 相关文件

- [tools/verification/](../../../../tools/verification/)（上表所列各脚本）
- [workspace/q1_false/feasibility_geometry/attempts/38_certificates_and_domain.md](38_certificates_and_domain.md)
- [workspace/q1_false/feasibility_geometry/attempts/45_bezout_rank.md](45_bezout_rank.md)
- [workspace/q1_false/feasibility_geometry/attempts/49_rank_stratified_impl.md](49_rank_stratified_impl.md)
- [workspace/q1_false/feasibility_geometry/attempts/50_decide_full_defect.md](50_decide_full_defect.md)
