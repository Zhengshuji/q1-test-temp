# 400 更正：$\rho$ 被重载（393/394 的 $\dim T_D$ 写错）；重根分量采样全坏

> 承接 393–399。本轮做 A 的有界目标（$c=2$ 重根分量上可行性是否随 $D$ 变）时，
> 数值把 393/394 里一处**记号重载**暴露出来：$\rho$ 同时被当作 $\rank H$ 与 $n-k$。

## 目标

1. 修正 393/394 的 $\dim T_D$ 与纤维维数公式；
2. 在 $c=2$ 的**重根分量**（$\operatorname{Gr}(2,E_\lambda)$，正维）上采样，看可行性是否随 $D$ 变。

## 设想与理由

393 写"$\dim T_D=\rho-r(D)$"，同时又写"$c:=k-\rho$、$t:=q-\rho$"。但
$T_D=K^\perp\cap(A_{21}D)^\perp\subseteq K^\perp$，而 $\dim K^\perp=n-k$——**不是** $\rank H$。
两者只有在 $n-k=\rank H$ 时才相等（$c=1$ 的 $q=k$ 情形恰好如此），所以错误一直没暴露。

正确的量应分开写：

$$\boxed{\ \rho_{\rm amb}:=n-k=\dim K^\perp,\qquad \rho:=\rank H=\dim\pi_K(V)=k-c\ }$$

于是
$$\dim T_D=\rho_{\rm amb}-r(D),\qquad
\dim\mathcal F_D^{\rm split}=(t-w_0)\bigl(\rho_{\rm amb}-r(D)-t\bigr),\qquad
\text{非空}\iff w_0\le t\le\rho_{\rm amb}-r(D).$$

**核对**：$n=8,k=4$（$\rho_{\rm amb}=4$）：

| 例子 | $r$ | $t$ | $\dim T_D$（公式） | 脚本实测 |
|---|---|---|---|---|
| c399 的 $c=2$ 可行设计（$D=\operatorname{span}\{e_1{+}e_2,e_3\}$） | 1 | 1 | 3 | 3 ✓ |
| c401 的重根分量样本（$M=\operatorname{diag}(1,1,1,2)$） | 2 | 1 | 2 | 2 ✓ |

（c401 的 $M$ 是 $\operatorname{diag}(1,1,1,2)$，故 $E_1$ 是 3 维、$\operatorname{Gr}(2,E_1)$ 是 2 维正维分量。）

## 做法：重根分量采样

`c401`：12 个随机 $D\in\operatorname{Gr}(2,E_1)$（坐标系数在 $\{-2,\dots,2\}$ 内随机）与随机
$W\subseteq T_D$（1 维），逐例算 $\omega=\rank H$ 与 $\omega$ 阶极大子式的 gcd 次数。

## 进展

**结果**：12/12 全部为 $(r,\omega,\gcd)=(2,2,2)$——即 $\omega=2$（$c=2$ ✓）、gcd 次数 2（**不可行**）。

- **稳定性**：整个采样里结论不变（都坏），支持"常秩层内结论一致"的预期；
- 但 $r$ 12 次都等于 2（$A_{21}|_{E_1}$ 在 $E_1$ 上满秩 2），所以只覆盖了 $r=2$ 这一层，
  **没有**触及 $r=0,1$ 的层；
- 样本量 12 远不足以支撑"整层都坏"的断言（纪律 12：薄集不许采样）。

## 最终结论

1. **393/394 的公式已更正**：用 $\rho_{\rm amb}=n-k$；$\rho=\rank H$ 是另一个量（$c=k-\rho$）。
   这是记号事故，不是数学错误——但会让人把 $\dim T_D$ 算错，故已在 393/394 就地改正；
2. **重根分量上的采样**没有发现可行点，也没有发现结论随 $D$ 变化；样本只覆盖 $r=2$ 层；
3. "常秩层内一次判定"仍**只是预期**，未证。

## 放弃原因

- 没有做 $r=0,1$ 层的采样（需要构造 $A_{21}|_{E_1}$ 秩亏的实例，即让 $A_{21}$ 在 $E_1$ 上退化）；
- 没有做符号计算（$\operatorname{Gr}(2,3)$ 是 2 参数，多变量 gcd 代价高）；
- 因此"分量内是否均匀"仍未定。

## 残留价值

- **一处真正的记号更正**（$\rho$ 重载），附两个数值核对；393/394 已改；
- 重根分量的第一个采样表（12 例全坏，$r=2$ 层）；
- 明确了下一步要造的实例形状：$A_{21}$ 在重根特征空间上**秩亏**，才能进到 $r=0,1$ 层。

## 相关文件

- [attempts/393](../../c_stratification/attempts/393_c2_fibre_and_base.md)、[394](394_c2_total_charts.md)（$\rho_{\rm amb}$ 已改）
- [attempts/399](../../c_stratification/attempts/399_layer_paperII_dictionary.md)（$\rho=\rank H=\dim U$ 的字典）
- [c401](../../../../tools/verification/c401_c2_repeated_component.py)、[c399](../../../../tools/verification/c399_c2_feasible_q3.py)
