# 690 特征值-秩必要条件：$\operatorname{rank}(\mu I-Z')\ge d'-s$
> **更正（692）**：$\operatorname{rank}G\le t=\dim T$（不是 $s$）；条件应为 $\operatorname{rank}(\mu I-Z')\ge d'-t$。测试数据中 $t=s$，表中结论不变；标量 $Z'$ 的结论应写 $d'\le t$。
> **审计注（729）**：661 因 $T=0$ 对 $d>0$ 不可行；本文若沿用“661 实例级不可行/满足 651 却不可行”的表述，以 726/729 为准。



> 2026-11-27。由 $P(\lambda)=\lambda H-HZ'-G$ 在特征值处的秩分解，得到一条新的必要条件；它解释了标量 $Z'$ 的不可行。
> 状态：**[已证-纸面]**。

## 定理

设 $s=\dim S$、$d'=\operatorname{rank}H$。若可行（秩 $d'$），则对 $Z'$ 的每个特征值 $\mu$，
$$\boxed{\operatorname{rank}(\mu I-Z')\ \ge\ d'-s .}$$

**证明**：$P(\mu)=\mu H-HZ'-G=H(\mu I-Z')-G$。$G=LW$ 的行在 $S$，故 $\operatorname{rank}G\le s$；又 $\operatorname{rank}(H(\mu I-Z'))\le\min(d',\operatorname{rank}(\mu I-Z'))$。于是
$$\operatorname{rank}P(\mu)\le\min(d',\operatorname{rank}(\mu I-Z'))+s .$$
若 $\operatorname{rank}(\mu I-Z')<d'-s$，则右端 $<d'$，与 $(5b)$ 的 $\operatorname{rank}P(\mu)=d'$ 矛盾。$\square$

（对非特征值的 $\lambda$，$\lambda I-Z'$ 可逆，$\operatorname{rank}H(\lambda I-Z')=d'$，无额外约束。）

## 推论

1. **标量 $Z'=\mu I$**：$\operatorname{rank}(\mu I-Z')=0$，故需 $d'\le s$。若 $s<k$ 且 $d'=k$（如 $d'=k>s$），**不可行**——这解释了 689 中标量 $Z'$ 的例外。
2. $S=\mathbb C^k$（$s=k$）：条件自动（$d'-k\le0$）。
3. $S=0$（$s=0$）：需 $\operatorname{rank}(\mu I-Z')\ge d'$ 对每个特征值成立。若 $d'=k$，特征值处 $\operatorname{rank}<k=d'$ ⇒ 违反；若 $d'<k$，本条不排除（但 629 用 $K_\infty$ 另行排除 $d'\ge1$）。

## 检验

| 实例 | $Z'$ 的特征值 $\mu$ | $\operatorname{rank}(\mu I-Z')$ | $s$ | $d'$ | $d'-s$ | 结论 |
|---|---|---|---|---|---|---|
| 638 | 0（重数 3） | 1 | 1 | 2 | 1 | 通过 ✓（可行） |
| 661（$q=2$） | 0 | 1 | 1 | 2 | 1 | 通过；不可行由 $m=1$ 解释 |
| 657 | 0 | 1 | 1 | 1 | 0 | 通过 ✓ |
| $Z'=0$、$S=e_1$、$d'=2$ | 0 | 0 | 1 | 2 | 1 | **违反** ⇒ 不可行 |
| $S=0$、$d'=k$ | 任意 | $<k=d'$ | 0 | $k$ | $k$ | **违反** ⇒ 不可行（629 的更一般结论覆盖 $d'\ge1$） |

## 意义

- 这是继 $K_\infty/T_\infty$ 之后的又一条**纯数据**必要条件（只依赖 $Z'$ 与 $s$）；
- 它把“标量 $Z'$、$d'>s$”的不可行性统一进来；
- 与 651 的关系：651 约束 $H$ 的核（$T_\infty$），本条约束 $Z'$ 在特征值处的秩；两者独立，需同时满足。

## 下一步

1. 把本条并入可行性判据（作为预筛选）；
2. 检查是否存在满足本条 + 651 但仍不可行的实例（661 是 $q=2$ 的例子）；
3. 研究等号情形 $\operatorname{rank}(\mu I-Z')=d'-s$ 的结构（可能需要更强的条件）。

## 状态

- 定理：**[已证-纸面]**；
- 例子检验：**[已证-纸面]**（按表）。
