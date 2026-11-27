# 521 块对角组合：520 gadget 的合取是 sound 的

> 2026-11-27。把两个 520 gadget 做块对角组合，检验 ChatGPT 提的第一个问题：
> 组合后是否存在“某条乘法不成立、但整体满足 $(5a)/(5b)$”的实例？
> **结论：不存在。** 块对角组合严格等价于两条约束的合取，且变量共享不破坏 soundness。
> 状态：**[已证-纸面]** + **[精确验证]**。

## 构造

两个 520 gadget：$A_i$（$5\times5$）、$L_i$（$3\times5$），变量 $(x_i,y_i,z_i)$。
令
$$A=A_1\oplus A_2\in\mathbb C^{10\times10},\quad
C=\begin{bmatrix}e_5^{\mathsf T}&0\\0&e_{10}^{\mathsf T}\end{bmatrix}\ (2\times10),\quad
L=L_1\oplus L_2\ (6\times10).$$
则 $CA=(CA_1)\oplus(CA_2)$、$K_0=K_{0,1}\oplus K_{0,2}$、$N=N_1\oplus N_2$，压缩数据
$$H=H_1\oplus H_2,\qquad H_A=H_{A,1}\oplus H_{A,2}.$$

## 定理

整体 q1 可行 $\iff$ $z_1=x_1y_1$ **且** $z_2=x_2y_2$。

**证明.**
- $(5a)$ 逐块成立（每块的 $(5a)$ 恒真，见 520），块对角堆叠后仍成立；
- $(5b)$：$\lambda H-H_A=(\lambda H_1-H_{A,1})\oplus(\lambda H_2-H_{A,2})$，故
  $$\operatorname{rank}(\lambda H-H_A)=\operatorname{rank}P_1(\lambda)+\operatorname{rank}P_2(\lambda),\qquad
  \omega=\omega_1+\omega_2 .$$
  因 $\operatorname{rank}P_i\le\omega_i$，等式 $\forall\lambda$ 成立 $\iff$ 两块各自 $\operatorname{rank}P_i=\omega_i$ $\forall\lambda$；
- 每块由 520 恰好在其乘法成立时满足；故整体 $\iff$ 两条都成立。$\square$

## 精确核验

见 [521_block_composition.py](521_block_composition.py)：

| 情形 | base rank | $(5a)$ | $\lambda=0,1,2,3$ 的秩 |
|---|---|---|---|
| 两条都成立 | 8 | 8 | 8,8,8,8 |
| 仅第一条失败 | 9 | 9 | 9,9,9,9（复根处掉秩，见 520 的 $\lambda^2+12$） |
| 仅第二条失败 | 9 | 9 | 9,9,9,9 |
| 两条都失败 | 10 | 10 | 10,10,10,10 |

（表中“秩”在实 $\lambda$ 采样点相同，但门外块的 $\det$ 有复根，故 $(5b)$ 仍失败——与 520 的证明一致。）

## 变量共享

块对角只固定**位置**；同一个变量可以出现在两个块的条目里（例如 $x_2:=z_1$），
矩阵仍是块对角结构，秩分解与上述证明不变。所以 fan-out/等式**不需要额外的 wiring gadget**：
共享变量 = 在多个块的条目里写同一个符号/表达式。

## 意义

- 520 的 sound gadget 可以**自由合取**，且变量共享自动；
- 这消掉了 303 遗留的“wiring/equality”障碍（至少在无自由行的块对角构造里）；
- 下一步：用“条目 = 输入变量的多项式”把乘法门串成算术电路（$x^2$、$xyz$ 等），验证组合后的 soundness。

## 状态

- 块对角合取：**[已证-纸面]** + **[精确验证]**；
- 算术电路编码：**[未做]**。
