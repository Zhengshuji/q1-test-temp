# $k=\omega+1$、$d=2$ 的充分全坏定理（$k>3$ 的第一步）

> 2026-11-08。转入 $k>3$（专家 53 号 Priority 2）。朴素推广（“兼容 $y$ 在 $\ker Z_2$ 里”）是**错的**
> （$y_iZ_2=-x_iZ_1\ne0$）；正确的充分条件是 $\operatorname{row}Z_1\cap\operatorname{row}Z_2=0$，
> 证明对**任意** $k=\omega+1$ 成立。状态：**M2（纸面）**；充分不必要。
>
> **更强的形式见 [attempts/122](122_invariant_eigenspace_obstruction.md)**：
> $\dim(K\cap\ker A)>k-\omega\Rightarrow$ 全坏（任意 $k,\omega$）；本文件的
> $\operatorname{row}Z_1\cap\operatorname{row}Z_2=0$ 是其特例（$Z_1=0$）。

## 目标

证明：

> **定理**：设 $k=\omega+1$、$q=\omega+1$、$d=2$（故 $\operatorname{rank}Z_2=2$）。
> 若 $\operatorname{row}Z_1\cap\operatorname{row}Z_2=0$，则每个可容许压缩点都坏。

这是 110/117 中 $Z_1=0$ 情形的推广：$Z_1=0$ 时交集为 $0$，定理适用。

## 设想与理由

* 朴素推广：$V_0Z_2=0\Rightarrow V_0\in\ker Z_2$，然后假设 $y_i\in\ker Z_2$——
  **错**，因为 $y_iZ_2=-x_iZ_1$ 一般非零。
* 正确的对象：
  $$Y=\{y\in\mathbb C^k:\ yZ_2\in\operatorname{row}Z_1\}.$$
  $V_0Z_2=-U_0Z_1\in\operatorname{row}Z_1$，$y_iZ_2=-x_iZ_1\in\operatorname{row}Z_1$，
  故 $V_0$ 与所有兼容 $y_i$ 都在 $Y$ 里。
* $Y$ 是 $\operatorname{row}Z_1\cap\operatorname{row}Z_2$ 在 $Z_2$ 下的原像：
  $$\dim Y=(k-\operatorname{rank}Z_2)+\dim(\operatorname{row}Z_1\cap\operatorname{row}Z_2).$$
  当交集为 $0$ 时，$\dim Y=k-2=\omega-1$。

## 做法

**第一步：$\operatorname{rank}Z_2=2$。** $\ker T\to$ 第二坐标的投影是单射（$(v,0)\in\ker T\Rightarrow v=0$），
$d=2$ 时像维数 $=2$。

**第二步：$\dim Y=\omega-1$。** 由上面的原像公式，交集 $0$ 时
$\dim Y=(k-2)+0=(\omega+1)-2=\omega-1$。

**第三步：$\lambda=0$ 处掉秩。** $H_A$ 的行 $V_0,y_1,\ldots,y_m$ 全在 $Y$ 里，
故 $\operatorname{rank}H_A\le\dim Y=\omega-1$。而 $P(0)=-H_A$，故
$$\operatorname{rank}P(0)\le\omega-1<\omega .$$
所以每个可容许点坏。$\square$

**与实例的关系**：
* 753：$Z_1=0$，交集 $0$，定理适用 → 全坏 ✓。
* 138：$Z_1\ne0$、$Z_2$ 张成 $\mathbb C^2$，交集 $=\operatorname{row}Z_1\ne0$，定理**不适用**；
  但它用别的 $\lambda_0$（$-1$ 与 $0$）全坏（110），说明条件**不必要**。
* 1081/1327/1491：$Z_1\ne0$，交集非零，不适用；确实有好点。
* $k=4$ 的四个实例（seed 60/103/146/318）的 $Z_1$ 都非零，交集非零；定理不适用，
  它们的行为需要其它 $\lambda_0$ 或别的论证（未做）。

## 进展

* 定理已证（任意 $k=\omega+1$，$d=2$，交集 $0$）。
* 这是第一个**真正 $k>3$** 的结果：证明中没有用到 $k=3$，只用了
  $\dim\ker Z_2=\omega-1$ 与原像维数。
* 但它只是充分条件；138 说明交集非零时也可能全坏（用别的 $\lambda_0$）。

## 最终结论

* **充分条件**：$\operatorname{row}Z_1\cap\operatorname{row}Z_2=0\Rightarrow$ 全坏（任意 $k=\omega+1$）。
* **不必要**：138 是交集非零但全坏的例子（$\lambda_0=-1$）。
* 完整的 $k>3$ 分类需要处理交集非零时的其它 $\lambda_0$；这是开放的。

## 放弃原因

* 只证了充分方向；交集非零的 $k=4$ 实例未分析。
* 没有给出 $k>3$ 的充要条件或分量分解。

## 残留价值

* 第一个不依赖 $k=3$ 的全坏定理；证明只用维数 $k-2=\omega-1$。
* 明确记录了朴素推广的错误（$y_iZ_2=-x_iZ_1$）。
* 为 $k>3$ 的后续工作划出边界：交集为 $0$ 可证；交集非零要看别的 $\lambda_0$。

## 相关文件

* [attempts/110](110_d2_all_bad_example.md)（138 的另一个 $\lambda_0$）
* [attempts/117](../../decision_algorithms/attempts/117_d2_e1_v0z2_criterion.md)（更正后的充分条件）
* [attempts/116](116_k3_e_positive.md)（$e=1$ 数据）
* [attempts/113](../../decision_algorithms/attempts/113_projective_theorem_corrected.md)（determinantal 框架）

## 状态

* 定理：**[已证-纸面，M2]**（充分条件，任意 $k=\omega+1$）。
* 不必要性：**[精确验证/已证]**（138 的 $\lambda_0=-1$）。
* 未做：交集非零的 $k>3$；充要条件；分量分解。
