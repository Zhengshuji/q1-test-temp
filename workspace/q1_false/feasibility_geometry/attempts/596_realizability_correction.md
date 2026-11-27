# 596 重要更正：$H_A$ 不能取 $ZH$——594/595 的抽象铅笔不可实现

> 2026-11-27。复查 594/595 的“$H_A=ZH$”时发现：在 q1 里 $H_A=LAN$ 由**同一个** $A$ 决定，
> 不能自由令 $H_A=ZH$。正确的可实现形式是**右铅笔** $P=H(\lambda I-Z')$。
> 状态：**[已证-纸面]**。

## 可实现性约束

$H=LN$、$H_A=LAN$。若要 $H_A=HZ'$，需要
$$LAN=HZ'=LNZ'\quad\forall L\ \Longrightarrow\ AN=NZ' .$$
即 $A$ 在 $\operatorname{im}N$ 上的作用等于 $Z'$。此时
$$H_A=HZ',\qquad P(\lambda)=H(\lambda I-Z') .$$
这是**右**铅笔（$H$ 在左），不是 594 的 $P=(λI-Z)H$。

## 后果：$H$ 可逆时 $(5b)$ 自动成立

若 $H$ 行满秩（$\ker H=0$），则 $H(\lambda I-Z')$ 的秩恒为 $\operatorname{rank}H=\omega$——
**对所有 $\lambda$ 自动成立**，没有门。

所以 594 的构造（$H=\begin{bmatrix}r_1&z&0\\1&r_2&0\\0&0&1\end{bmatrix}$）在可实现形式下：
- 门外 $r_1r_2\ne z$：$H$ 可逆 ⇒ $(5b)$ 自动成立 ⇒ **可行**；
- 门上：$H$ 奇异，$(5b)$ 可能反而失败。

即门的极性完全相反，$H_A=ZH$ 的“乘积等式门”**不成立**。

## 594/595 的定位

- 594 的铅笔分析（$P=(λI-Z)H$）数学上自洽，但**不对应任何 q1 实例**；
- 595 的块对角合取同样基于该抽象铅笔，**不能直接用于 q1**；
- 两者保留为“抽象铅笔”的记录，已加注更正；真正的 gadget 必须在右铅笔下重做。

## 正确的设计空间

右铅笔下 $P=H(\lambda I-Z')$：
- 要门，必须 $H$ **始终奇异**（否则 $(5b)$ 自动成立）；
- 秩条件
  $$\operatorname{rank}\big(H(\lambda I-Z')\big)=\operatorname{rank}H\quad\forall\lambda$$
  等价于 $\ker H\cap\operatorname{im}(\lambda I-Z')=\{0\}$ 之类的条件；
- 因此 $H$ 的核（依赖 $R$）与 $Z'$ 的广义特征空间（固定）之间的碰撞才是门的来源。

## 下一步

在右铅笔、$H$ 恒奇异的约束下重做：
1. 取 $H=\begin{bmatrix}r_1&z&0\\1&r_2&0\\0&0&0\end{bmatrix}$（零行，$\operatorname{rank}$ 由 $2\times2$ 块决定），
   $Z'$ 幂零 Jordan；计算 $\operatorname{rank}(H(\lambda I-Z'))$；
2. 检查可行集能否等于 $r_1r_2=z$ 或 $\ne$；
3. 通过后再谈块对角合取。

## 状态

- 可实现性更正：**[已证-纸面]**；
- 594/595：**已标注“不可实现于 q1”**；
- 右铅笔重做：**[未做]**。
