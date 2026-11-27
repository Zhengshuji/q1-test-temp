# 659 ChatGPT 深入回答的整理：秩 $d$ 模板、行约束与反例

> 2026-11-27。按用户要求让 ChatGPT 给出详细、学术化的回答；本文件整理其定理与证明要点，并做独立核验。
> 状态：**[已证-纸面]**（整理与核验）+ **[开放]**（仿射铅笔问题）。

## 定理 1（秩 $d$ 模板，充分条件）

设 $H=UV$，$U\in\mathbb C^{q\times d}$ 列满秩、$V\in\mathbb C^{d\times k}$ 行满秩，且
$$\operatorname{row}(V)\subseteq S,\qquad VZ'=0,\qquad \operatorname{row}(H_0)\subseteq\operatorname{row}(V).$$
若存在 $B\in\mathbb C^{q\times d}$ 使
$$\operatorname{rank}[U\ \ B]=2d\qquad(\text{等价于 }\operatorname{im}U\cap\operatorname{im}B=0),$$
则可取 $Z$ 使 $ZU=B$，并满足
$$G=ZH-HZ'=BV,\quad \operatorname{row}(G)\subseteq\operatorname{row}(V)\subseteq S,$$
$$\operatorname{rank}(\lambda H-ZH)=d\ \forall\lambda .$$

**证明要点**：$HZ'=UVZ'=0$，故 $G=(ZU)V=BV$。$P(\lambda)=(\lambda U-B)V$；$V$ 行满秩 ⇒
$$\operatorname{rank}P(\lambda)=d\iff\ker(\lambda U-B)=0 .$$
若 $(\lambda U-B)x=0$，则 $\lambda Ux=Bx\in\operatorname{im}U\cap\operatorname{im}B=0$ ⇒ $Ux=0$ ⇒ $x=0$。

**可实现性**：$Z$ 只需在 $\operatorname{im}U$ 上等于 $B U^{+}$，再任意延拓；$H_A=ZH$ 与 $L$ 的相容性由 $G$ 行在 $S$ 内保证（$G=LW$ 可解）。

## 定理 2（一般行约束的充要条件）

对一般 $V$（不要求 $VZ'=0$），存在 $Z$ 使 $\operatorname{row}(ZUV-UVZ')\subseteq S$ $\iff$
$$\ker(V|_K)\subseteq\ker((VZ')|_K),\qquad K=S^\perp .$$
证明：$Gx=0\ \forall x\in K$ ⇔ $B(Vx)=U(VZ'x)$；$B=ZU$ 可任意（$U$ 列满秩），故只需右端在 $Vx$ 上良定义。

## 定理 3（$S\cap\ker Z'^{\mathsf T}\subseteq T_\infty^\perp$）

$v\in S$、$vZ'=0$ ⇒ $v$ 消灭 $T_0=K_\infty\subseteq K$；若 $v$ 消灭 $T_j$，则对 $x=x_0+Z'y$（$y\in T_j\cap K$）：
$$vx=vx_0+vZ'y=0 .$$
故 $v$ 消灭 $T_\infty$。于是
$$\dim\big(S\cap\ker Z'^{\mathsf T}\big)\le k-\dim T_\infty .$$

## 反例 4：651 的条件不充分（$k=1$，$q=r_0=1$）

$S=\mathbb C$、$Z'=0$、$H_0=[1]$：$K=0$、$T_\infty=0$、$d=1$，651 条件全满足。
但 $q=r_0=1$ ⇒ $H=H_0=[1]$，$\operatorname{rank}H=1=q$；$(5a)$ 给 $H_A=zH$，
$$\lambda H-H_A=[\lambda-z]$$
在 $\lambda=z$ 处秩 0 $<1$ ⇒ 不可行。

## 秩 $=$ 行数的障碍（518 的一般形式）

若 $\operatorname{rank}H=q>0$，则 $H_A=ZH$（$(5a)$ 的行包含），$P(\lambda)=(\lambda I_q-Z)H$，
$$\operatorname{rank}P(\lambda)=\operatorname{rank}(\lambda I_q-Z),$$
而 $q\times q$ 复矩阵必有特征值 ⇒ 某 $\lambda$ 掉秩 ⇒ $(5b)$ 失败。故
$$\boxed{\operatorname{rank}H=q>0\ \Rightarrow\ \text{不可行}} .$$

## 开放的“仿射铅笔问题”

给定 $U,V,Z',S$，设 $\ker(V|_K)\subseteq\ker((VZ')|_K)$，令
$$\mathcal B=\{B:\ B(Vx)=U(VZ'x)\ \forall x\in K\}.$$
问：何时存在 $B\in\mathcal B$ 使 $\operatorname{rank}(\lambda U-B)=d\ \forall\lambda$？
等价地，$\mathcal B$ 中是否存在使所有 $d\times d$ 子式的 gcd 为 1 的 $B$。
两个子问题：几何版（$\operatorname{im}B\cap\operatorname{im}U=0$，充分非必要）与精确代数版（gcd=1）。

## 意义

- 定理 1 把 657/658 的秩一构造严格推广到秩 $d$；
- 定理 2 给出一般行约束的线性充要条件；
- 定理 3 把 $S\cap\ker Z'^{\mathsf T}$ 与 $T_\infty$ 上界联系起来；
- 反例 4 说明 651 的三个数值条件不充分（但只是固定 $q$ 的反例）；
- 仿射铅笔问题是连接必要与充分条件的关键缺口。

## 状态

- 定理 1–3：**[已证-纸面]**；
- 反例 4 与秩 $=q$ 障碍：**[已证-纸面]**；
- 仿射铅笔问题：**[开放]**。
