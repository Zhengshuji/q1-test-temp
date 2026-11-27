# 737 猜想 (D) 的证明：$\dim E_H\le\dim(U\cap T)+\operatorname{cls}$

> 2026-11-27。子 agent 的 342 例数值检验（0 反例）提示了精确结构；本文件给出纸面证明。
> 状态：**[已证-纸面]**。

## 定理 (D′)

设 $T\subseteq\mathbb C^k$、$U=\operatorname{row}H$、$M=\mu I-Z'$、$H_i$ 为 $H$ 的第 $i$ 行，
$$F_i=T\cap(U-H_iZ'),\qquad E_H=\operatorname{span}\Big(\bigcup_i F_i\Big),$$
并令
$$\operatorname{cls}:=\operatorname{rank}\begin{bmatrix}HM\\ \text{(基 of }U)\end{bmatrix}-\dim U
=\dim\frac{\operatorname{row}(HM)+U}{U}.$$
若所有 $F_i\ne\varnothing$，则
$$\boxed{\dim E_H\ \le\ \dim(U\cap T)+\operatorname{cls}\ \le\ \dim(U\cap T)+\operatorname{rank}(HM).}$$

**证明**：

1. 由 $M=\mu I-Z'$：$H_iZ'=\mu H_i-H_iM$，且 $H_i\in U$，故
   $$U-H_iZ'=U+H_iM .$$
2. 取 $t_i\in F_i$（非空）。对 $t\in T$：$t\in F_i\iff t+H_iM\in U$；而 $t_i+H_iM\in U$，故
   $$t-t_i\in U\cap T\ \Longrightarrow\ F_i=t_i+(U\cap T).$$
3. 于是
   $$E_H\subseteq (U\cap T)+\operatorname{span}\{t_i\}.$$
4. 由 $t_i\equiv -H_iM\pmod U$，类 $[t_i]\in(\operatorname{row}(HM)+U)/U$，其维数 $\le\operatorname{cls}$。故
   $$\dim E_H\le\dim(U\cap T)+\operatorname{cls}.\qquad\square$$

## 推论（结合 734 的定理 B）

$$d'\ \le\ \operatorname{rank}(HM)+\dim E_H
\ \le\ \operatorname{rank}(HM)+\dim(U\cap T)+\operatorname{cls}
\ \le\ \dim(U\cap T)+2\operatorname{rank}(HM).$$

## 数值检验（子 agent，342 例）

- 随机 $k=3,4$、$T$ 维 2–3、$H$ 秩 2、$Z'$ 随机、$\mu\in\{0,\pm1\}$ 或特征值；
- **0 反例**；且逐组核验了更强的**等式**
  $$\dim E_H=\dim(U\cap T)+\operatorname{cls}\qquad(342/342).$$
- 最小“跨行组合”例子：$k=3$、$H=[[0,0,1],[1,0,0]]$、$Z'=[[0,1,0],[0,0,0],[0,0,0]]$、$\mu=0$：
  $F_1=\{a e_1\}$、$F_2=\{a e_1-e_2\}$，$\dim E_H=2=\dim(U\cap T)(1)+\operatorname{cls}(1)$。

## 意义

- D 从猜想变为定理；
- 734 的定理 B 可升级为
  $$d'\le\operatorname{rank}(HM)+\dim(U\cap T)+\operatorname{cls};$$
- $\operatorname{cls}\le\min(\operatorname{rank}(HM),\ t-\dim(U\cap T))$，是比 $\operatorname{rank}(HM)$ 更细的量；
- 这给出一条依赖 $H$ 方向的、可计算的必要条件。

## 状态

- 定理 (D′)：**[已证-纸面]**；
- 数值：**[精确验证 342/342]**（子 agent）；
- 与 734 合并：**[已证-纸面]**。
