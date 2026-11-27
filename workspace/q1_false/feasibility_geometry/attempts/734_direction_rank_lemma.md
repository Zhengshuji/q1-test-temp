# 734 方向性补偿空间秩引理（ChatGPT 的 (B)/(C)，已证）

> 2026-11-27。证明 $d'\le\operatorname{rank}(H(\mu I-Z'))+\dim E_H$，并验证 733 取等。
> 状态：**[已证-纸面]**。

## 定理 B（方向性补偿空间秩引理）

设可行（秩 $d'$）、$U=\operatorname{row}H$、$T=\{lW:lN=0\}$，且 $ZH=HZ'+G$、$G$ 行在 $T$。定义
$$E_H=\operatorname{span}\Big(\bigcup_{i=1}^q\big(T\cap(U-H_iZ')\big)\Big).$$
则对任意 $\mu$，
$$\boxed{d'\ \le\ \operatorname{rank}\big(H(\mu I-Z')\big)+\dim E_H .}$$

**证明**：

1. 由 $G_i=Z_iH-H_iZ'$：$G_i\in T$（题设）且 $G_i\in U-H_iZ'$（$Z_iH\in U$）。故
   $$G_i\in T\cap(U-H_iZ')\ \Longrightarrow\ \operatorname{row}(G)\subseteq E_H\ \Longrightarrow\ \operatorname{rank}G\le\dim E_H .$$
2. $P(\mu)=H(\mu I-Z')-G$，故
   $$\operatorname{rank}P(\mu)\le\operatorname{rank}\big(H(\mu I-Z')\big)+\operatorname{rank}G .$$
3. 可行性给 $\operatorname{rank}P(\mu)=d'$，合并即得。$\square$

## 推论 C（标量特征值）

若 $Z'=\mu I$，则 $H(\mu I-Z')=0$，定理 B 给
$$\boxed{d'\le\dim E_H\le\dim(U\cap T)}$$
（因 $H_iZ'=\mu H_i\in U$，故 $T\cap(U-H_iZ')=T\cap U$，$E_H\subseteq U\cap T$）。

这正是 726（$a\ge1$）的强化：标量情形需 $d'\le a$。

## 733 的检验（取等）

733：$Z'$ 的特征值 $\mu=1\pm\sqrt2$，$H(\mu I-Z')$ 的秩 $1$；$U=\mathbb{C}^2$（$k=2$），$T=\operatorname{span}\{e_1\}$，故
$$E_H=T,\qquad \dim E_H=1 .$$
定理 B：$d'=2\le1+1=2$ ✓ **取等**——与 695 的取等一致。

## 意义

- $E_H$ 依赖 $H$ 的方向（而非只依赖 $t$），是比 690/695 更细的筛选；
- 它解释了“$t$ 大不代表可补偿”：若 $T$ 的方向与 $U-H_iZ'$ 无交，$E_H$ 可以很小；
- 标量情形 $d'\le\dim(U\cap T)$ 是 726 的严格强化（$a$ 而非 $t$）。

## 与 732 的关系

732 的 $d'\le t$ 已被 733 推翻；定理 B 用 $E_H$（依赖 $H$）替代 $t$，避免了该反例（733 中 $E_H=T$、$t=1$，等式成立）。

## 下一步

1. 研究 $E_H$ 的“一般大小”：对随机相容 $H$，$\dim E_H$ 与 $t$ 的关系；
2. 标量 $Z'$ 的 $d'\le\dim(U\cap T)$ 是否可加强为充分（在什么附加条件下）；
3. 把定理 B 加入预筛选链。

## 状态

- 定理 B：**[已证-纸面]**；
- 推论 C：**[已证-纸面]**；
- 733 取等：**[精确验证]**。
