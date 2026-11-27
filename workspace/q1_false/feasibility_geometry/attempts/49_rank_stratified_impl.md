# 秩分层落地：在 "$\operatorname{rank}[V|Z]=\rho$" 的层上跑 $(*)$ 判据

## 目标

补上 [attempts/48](48_rank_stratification_needed.md) 诊断出的唯一缺口：**秩跌落**导致极大子式尺寸变化。
做法：按 $\rho=\operatorname{rank}[V|Z]$ 分层，在每层上用**对应尺寸**的极大子式做 $(*)$ 判据。

## 设想与理由

* 层 $\rho$：$\{\text{某个 }\rho\text{-子式}\ne0\}\cap\{(\rho+1)\text{-子式}=0\}$；
* 层上 $(5b)\iff e_0\in\operatorname{col}M_\rho(\theta)$，$M_\rho$ 由 $P_{\mathcal Z}(\lambda)$ 的 $\rho$-子式构成；
* 左零空间给 $C_j^{(\rho)}(\theta)$：$e_0\in\operatorname{col}M_\rho\Rightarrow C_j=0$；
* 单参数图卡上，"候选 $\theta$" = $\{g_i\}\cup\{C_j\}$ 的公共零点（一元 gcd 的根）；
* 若左零空间**为空**（$M_\rho$ 满行秩）⟹ 该层处处 $(5b)$ 成立 ⟹ 取层内任一点即可得见证。

## 做法

[rank_stratified.py](../../../../tools/verification/rank_stratified.py)：对每个图卡、每个 $\rho$（从 $\dim V+d$ 递减）：
建层条件与 $M_\rho$ → 左零空间 → 候选 $\theta$ → 核验（在该点确认在层内、$(5a)$、$(5b)$、七条检查）。

## 进展

| 实例（$q_0$ 阶）| 结果 | 层 / $\theta$ |
|---|---|---|
| $n=5,p=1,r=2$ seed 3003 | **FEASIBLE** | 图卡 (0)、$\rho=3$、$\theta=0$ |
| $n=5,p=1,r=2$ seed 3005 | **FEASIBLE** | 图卡 (1)、$\rho=3$、$\theta=0$ |
| $n=5,p=2,r=1$ seed 3023 | **FEASIBLE** | 图卡 (0)、$\rho=2$、$\theta=0$ |
| $n=6,p=2,r=2$ seed 3027 | **FEASIBLE** | 图卡 (0)、$\rho=3$、$\theta=0$ |
| $n=5,p=1,r=1$ seed 3006 | UNKNOWN | 图卡是**双参数**（本实现只覆盖单参数）|

四个可行见证**全部通过七条一致性检查**。关键点：这些实例在 $\theta=0$ 处的 $\operatorname{rank}[V|Z]$ 比典型值低
（这正是此前固定尺寸版本误判的原因），分层后即可正确判定。

## 最终结论

1. **秩分层有效**：四个此前 `UNKNOWN`/误判的实例现在都给出**带见证的 FEASIBLE**；
2. 分层把"尺寸"问题彻底解决——每层用自己的 $\rho$，不再依赖典型尺寸；
3. **仍缺**：
   * 多参数图卡（$\ge2$ 参数；单参数之外未实现）；
   * **不可行方向**：需在每层上证明 $\{g_i\}\cup\{C_j\}$ 无公共零点（单参数时是一元 gcd 为常数 ✓ 已可实现，
     多参数需 Gröbner / 实量词消去）；
4. 因此逐阶判定现在覆盖：单参数图卡的**可行方向**（带见证）+ C4 型不可行（理想为 $(1)$）。

## 放弃原因

不适用（分层落地）。**未做**：多参数图卡的分层与不可行方向的通用证明。

## 残留价值

* 秩分层的**可运行实现**与四个带见证的可行判定；
* 明确了"尺寸"不再是障碍，剩下的只是**层数 × 参数维数**的组合爆炸与实点求解；
* 与 $(*)$、$X/X_{\rm sp}$、快速满行秩判据共同构成一套**逐阶判定的工具箱**。

## 相关文件

- [tools/verification/rank_stratified.py](../../../../tools/verification/rank_stratified.py)
- [tools/verification/bezout_rank_test.py](../../../../tools/verification/bezout_rank_test.py)
- [workspace/q1_false/feasibility_geometry/attempts/48_rank_stratification_needed.md](48_rank_stratification_needed.md)
- [workspace/q1_false/feasibility_geometry/attempts/47_x_vs_xsp.md](47_x_vs_xsp.md)
