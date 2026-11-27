# forced-plane 判据的精确证书：seeds 10/16/21（专家 60 号 Priority 3）

> 2026-11-08。按专家 60 号建议，把 165 的 $b$-强制判据做成**输出证书**：
> 每个底部行给出“被强制 0”的行空间表示 $\alpha$，或“未被强制”的核向量 $x$（$b\ne0$）。
> 状态：**精确验证 3/3**。

## 目标

对 seeds 10/16/21，逐底部行输出可机器核对的两类证书之一：
- (A) $\alpha$ 使 $e_b=\alpha^{\mathsf T}\mathrm{Des}_i$（证明 $b_i$ 在所有可容许解上为 0）；
- (B) $x\in\ker(\mathrm{Des}_i)$ 且 $b_i\ne0$（证明 $b_i$ 不被强制 0）。

## 设想与理由

165 的判据是 $e_b\in\operatorname{rowspace}(\mathrm{Des}_i)$（齐次方程时）。这个判据可以直接给出
**短证书**：$\alpha$ 或 $x$，都可用一条矩阵乘法核对。专家 60 号特别建议把这一步算法化并输出证书。

## 做法

工具：[tools/verification/c2_forced_certificates.py](../../../../tools/verification/c2_forced_certificates.py)

对每个 seed、每个底部行：
1. 构造 $\mathrm{Des}_i$（$2\times(2+\dim\operatorname{row}[C;CA])$）；
2. 解 $\mathrm{Des}_i^{\mathsf T}\alpha=e_b$：可解则输出 $\alpha$，并核对 $\alpha^{\mathsf T}\mathrm{Des}_i=e_b$；
3. 否则解 $\mathrm{Des}_i x=0$、$b=1$ 的联立系统，输出 $x$，并核对 $x\in\ker\mathrm{Des}_i$、$b\ne0$。

## 结果

```
--- seed 10 ---
  row 0: NOT forced, x=(0,1,0,0,0)
  row 1: NOT forced, x=(0,1,0,0,0)
--- seed 16 ---
  row 0: FORCED, alpha=(-1,0)
  row 1: FORCED, alpha=(-1,0)
--- seed 21 ---
  row 0: FORCED, alpha=(-1,0)
  row 1: FORCED, alpha=(-1,0)
```

**解读**：
- seeds 16/21：$\alpha=(-1,0)$ 给出 $b=-\mathrm{Des}_{i,0}$，即 $b_i$ 被第一条可容许方程强制为 0；
  两行都如此 $\Rightarrow$ $H$ 秩 $1<\omega=2$ $\Rightarrow$ **不可行**（证书式证明）；
- seed 10：$x=(0,1,0,0,0)$ 是核向量且 $b=1\ne0$，故 $b_i$ 不被强制 0；这与已给出的完整 $L$ 见证一致。

## 进展

* $b$-强制判据的证书已实现并核对（3/3）；
* seeds 16/21 的不可行现在有**短证书**（$\alpha=(-1,0)$），不再依赖“采样失败”；
* seed 10 的非强制证书与完整见证互相印证。

## 最终结论

* forced-plane 判据（齐次情形）可以输出**行空间/核向量证书**；
* 16/21 的不可行有证书；10 的可行有见证；
* 这正是专家 60 号 Priority 3 要求的“算法输出证书”。

## 放弃原因

* 未把证书接入 166 工具的常规输出（目前是独立脚本）；
* 未处理仿射情形（专家提醒的额外条件）；
* 未 Lean 化。

## 残留价值

* 三个实例的短证书，可直接贴进论文/回信；
* 验证了 165 的判据在真实数据上可执行。

## 相关文件

* [attempts/165](../../c_stratification/attempts/165_c2_forced_plane_criterion.md)（判据）
* [attempts/166](166_c2_general_algorithm.md)（算法）
* [tools/verification/c2_forced_certificates.py](../../../../tools/verification/c2_forced_certificates.py)
* [tools/verification/c2_seed10_witness.py](../../../../tools/verification/c2_seed10_witness.py)

## 状态

* 证书：**[精确验证 3/3]**。
* 仿射情形/Lean：**[未做]**。
