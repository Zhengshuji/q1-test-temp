# 630 $W\ne0$ 的结构分解：$H$ 与 $G$ 相互独立可控

> 2026-11-27。按 ChatGPT 的建议分析 $W\ne0$（$AK_0\not\subseteq K_0$）——q1_true 仅剩的入口。
> 状态：**[已证-纸面]**（分解）+ **[开放]**（可行性）。

## 分解

$\mathbb C^n=\operatorname{im}N\oplus Y$（$Y=\ker P$，$P$ 沿 $\operatorname{im}N$ 的投影）。
$N:\mathbb C^k\to\operatorname{im}N$ 是嵌入；$A N=N Z'+W$，$W$ 的像在 $Y$ 内（按构造）。

把 $L$ 分成 $L=[L_N\mid L_Y]$（$q\times k$ 与 $q\times\dim Y$）。则
$$H=LN=L_NN,\qquad G=LW=L_Y\,W .$$
（$N$ 的像在 $\operatorname{im}N$，$W$ 的像在 $Y$。）

自由行 $R$ 同时给出 $R_N$ 与 $R_Y$，二者**独立**（$R$ 的行在 $\mathbb C^n$ 的两个分块上互不影响）。
所以：
- 自由行可以任意改变 $H$ 的自由部分（$R_N N$）；
- 自由行可以任意改变 $G$ 的自由部分（$R_Y W$），但只能落在 $\operatorname{row}(W)$ 张成的行空间里。

## 压缩形式

$$\boxed{H_A=HZ'+G,\qquad G=G_0+G_{\rm free},\quad G_0=L_{0,Y}W,\ \operatorname{row}(G_{\rm free})\subseteq\operatorname{row}(W).}$$

固定数据：$Z'$、$W$、$H_0=L_0N$、$G_0=L_{0,Y}W$；自由数据：$H_{\rm free}$、$G_{\rm free}$。

## 可行性问题

$$\exists H_{\rm free},G_{\rm free}:\quad
\ker H\subseteq\ker(HZ'+G)\ \wedge\ \operatorname{rank}(\lambda H-HZ'-G)=\omega\ \forall\lambda .$$

即“**带约束的铅笔完成问题**”：给 $H$ 与 $G$ 的自由度，要求 $\lambda H-(HZ'+G)$ 的秩恒为 $\omega$。

## 关键观察

- $W=0$ 时 $G=G_0=L_0AN=H_A0$ 固定，629 证明只有 $\omega=0$ 可行；
- $W\ne0$ 时 $G$ 可随自由行变化，可能补偿 $H$ 的核、避免特征值掉秩；
- 但 $G$ 的行只能落在 $\operatorname{row}(W)$ 内——这是数据对自由度**唯一**的限制。

## 猜想

- 若 $\operatorname{row}(W)=\mathbb C^k$（$W$ 满行秩），$G$ 的自由度足以完成任意铅笔，q1 可行性可能**恒真**（无 hardness）；
- 若 $\operatorname{row}(W)$ 维数小，$G$ 受限，可能出现数据依赖的不可行——这是唯一可能的 hardness 入口。

## 下一步

1. 对 $\operatorname{row}(W)=\mathbb C^k$ 尝试构造性证明“可行”；
2. 对 $W$ 秩 1 等小情形做符号/数值实验，找数据依赖的不可行例子；
3. 把结论与 629 合并成 q1 的分情形定理。

## 状态

- 分解：**[已证-纸面]**；
- 分情形可行性：**[开放]**。
