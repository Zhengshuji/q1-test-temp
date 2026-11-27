# $d=2,e=1$：更正——正确的充分条件是 $\operatorname{row}Z_1\cap\operatorname{row}Z_2=0$

> 2026-11-08。**更正 117**：原稿断言“$V_0Z_2=0\Rightarrow$ 全坏”，证明里用了
> “兼容 $y_i\in\ker Z_2$”——这是**错的**。兼容条件是 $y_iZ_2=-x_iZ_1$，一般非零。
> 正确的充分条件与证明如下。状态：117 的充分方向 **[撤回]**；新充分条件 **[已证-纸面]**。

## 目标

对 $k=\omega+1$、$q=\omega+1$、$d=2$（故 $\operatorname{rank}Z_2=2$），给出“全坏”的**正确**充分条件。

## 设想与理由

* 原稿的错误：$V_0Z_2=0$ 只给出 $V_0\in\ker Z_2$，**不**给出 $y_i\in\ker Z_2$。
  由 $x_iZ_1+y_iZ_2=0$ 得 $y_iZ_2=-x_iZ_1$，一般非零。
* 正确的对象是
  $$Y=\{y\in\mathbb C^k:\ yZ_2\in\operatorname{row}Z_1\},$$
  因为 $V_0Z_2=-U_0Z_1\in\operatorname{row}Z_1$ 且 $y_iZ_2=-x_iZ_1\in\operatorname{row}Z_1$，
  所以 $V_0$ 与所有兼容 $y_i$ 都在 $Y$ 里。
* $Y$ 是 $\operatorname{row}Z_1\cap\operatorname{row}Z_2$ 在 $Z_2$ 下的原像，故
  $$\dim Y=(k-\operatorname{rank}Z_2)+\dim(\operatorname{row}Z_1\cap\operatorname{row}Z_2).$$
  当 $\operatorname{row}Z_1\cap\operatorname{row}Z_2=0$ 时，$\dim Y=k-\operatorname{rank}Z_2=(\omega+1)-2=\omega-1$。

## 做法

**定理（正确的充分条件）**：设 $k=\omega+1$、$q=\omega+1$、$d=2$、$\operatorname{rank}Z_2=2$。
若 $\operatorname{row}Z_1\cap\operatorname{row}Z_2=0$，则每个可容许压缩点都坏。

*证明*：$Y$ 如上，$\dim Y=\omega-1$。$H_A$ 的行 $V_0,y_1,\ldots,y_m$ 全在 $Y$ 里，
故 $\operatorname{rank}H_A\le\omega-1$。在 $\lambda=0$ 处 $P(0)=-H_A$，秩 $<\omega$。$\square$

**对 753 与 138 的核对**：
* 753：$Z_1=0$，故 $\operatorname{row}Z_1=0$，交集为 $0$；定理适用，全坏。✓
* 138：$Z_1\ne0$，$Z_2$ 张成 $\mathbb C^2$，故交集 $=\operatorname{row}Z_1\ne0$；定理**不适用**。
  但 138 的全坏是用别的 $\lambda_0$（$-1$ 与 $0$）证明的（110），所以“充分条件”不是必要的。
* 1081/1327/1491：$Z_1\ne0$，交集非零；不适用，且确实有好点。

## 专家 54 号的简化与不变形式

* 因 $\operatorname{rank}Z_2=\delta$ 且 $Z_2$ 有 $\delta$ 列，$\operatorname{row}Z_2=\mathbb C^\delta$，故
  $$\operatorname{row}Z_1\cap\operatorname{row}Z_2=\operatorname{row}Z_1;$$
  原条件 $\operatorname{row}Z_1\cap\operatorname{row}Z_2=0$ 等价于 $Z_1=0$。
* 更不变的形式：$\dim Y=k-\dim(K\cap\ker A)$（$Y$ 的原像解释），于是
  $$\boxed{\dim(K\cap\ker A)>k-\omega\ \Longrightarrow\ \text{所有可容许点在}\ \lambda=0\ \text{处坏}.}$$
  对 $k=\omega+1$：$\dim(K\cap\ker A)\ge2$。
* 直接证明：若 $v\in K\cap\ker A$，则 $Av=0$；$H_A=LAN$ 的每一行都湮灭 $v$，故
  $\operatorname{rank}H_A\le k-\dim(K\cap\ker A)<\omega$。
* 对好候选的**必要**条件（专家 4.7）：
  $$\dim\big(K\cap\ker(A-\lambda I)\big)\le k-\omega\qquad\forall\lambda.$$

## 进展

* 原 117 的“$V_0Z_2=0\Rightarrow$ 全坏”**撤回**；反例逻辑：$y_iZ_2=-x_iZ_1\ne0$。
* 新充分条件（$\operatorname{row}Z_1\cap\operatorname{row}Z_2=0$）已证；753 适用，138 不适用但仍全坏。
* 这说明“全坏”的机制不止 $\lambda=0$ 一个；138 的 $\lambda_0=-1$ 是另一条。

## 最终结论

* 正确的充分条件是 $\operatorname{row}Z_1\cap\operatorname{row}Z_2=0$（等价于 $\dim Y=\omega-1$）。
* $V_0Z_2=0$ 只是 $V_0\in\ker Z_2$，不足以保证 $y_i\in\ker Z_2$；117 的证明作废。
* 全坏不要求这个条件（138 是反例），所以它只是充分条件；充要条件仍开放。

## 放弃原因

* 没有给出充要条件；138 说明 $\lambda=0$ 机制不是唯一的。
* 只处理 $d=2$、$\operatorname{rank}Z_2=2$。

## 残留价值

* 一次明确的撤回与更正，防止“$y_i$ 在左核里”的错误继续传播。
* 正确的 $Y$ 与原像维数公式，适用于任意 $k=\omega+1$。
* 为 $k>3$ 提供了一条真正可推广的充分条件。

## 相关文件

* [attempts/110](../../c_stratification/attempts/110_d2_all_bad_example.md)（138 的另一个 $\lambda_0$）
* [attempts/116](../../c_stratification/attempts/116_k3_e_positive.md)（$e=1$ 数据）
* [attempts/118](../../c_stratification/attempts/118_k_omega_plus_1_d2_attempt.md)（$k>3$ 的推广尝试）

## 状态

* 117 的充分方向：**[撤回]**（证明错误）。
* 新充分条件：**[已证-纸面]**（$\operatorname{row}Z_1\cap\operatorname{row}Z_2=0$）。
* 充要条件：**[开放]**；138 说明不是必要的。
