# 479 自由行预算版判据 (FW)：**证明成立**（必要性 + 充分性 + 行数精确性）

> 承接专家对 109 的审阅：① kernel lemma 原文写错（需 $(5a)'+(5b)'$）；② 固定 $W$ 判据带 $m\ge\dim\mathcal T_W$ 的假设，
> 不覆盖任意 $q$。本文件修正 ①、**证明** ② 的 (FW) 版本。

## 目标

1. 修正 kernel lemma；
2. 证明 (FW)：固定 $W$、任意自由行预算 $m$ 下的完整判据；
3. 行数精确性（最小自由行数 = $\min\dim(\mathcal U/\mathcal W_0)$）。

## 设想与理由

**kernel lemma 的更正**（专家的反例：$H=(1\ 0)$、$H_A=(0\ 0)$）：
仅 $(5a)'$ 只给 $\ker H\subseteq\ker H_A$ ✗。正确版本：

> **Kernel lemma.** 在 $(5a)'$ 与 $(5b)'$ 同时成立时，$\ker H=\ker H_A$。

*证明.* $(5b)'$ 取 $\lambda=0$ 给 $\operatorname{rank}H_A=\omega=\operatorname{rank}H$；
与 $\operatorname{row}H_A\subseteq\operatorname{row}H$ 合起来得 $\operatorname{row}H_A=\operatorname{row}H$ ⟹ 核相等 ✓。$\square$

（**注意**：后续凡用 $\ker H=\ker H_A$ 之处，都必须引用**完整**条件，不能只引 $(5a)'$ ✓。）

## 做法

把判据从"取 $\mathcal U=\mathcal T_W$"改成"在 $\mathcal W_0\subseteq\mathcal U\subseteq\mathcal T_W$ 中选 $\mathcal U$"，
再用 Paper I 的行对实现性把 $\mathcal U$ 的基元素提升为自由行。

## 进展

（见下文"做法与结果：(FW)"。）

## 做法与结果：(FW)

记号：$\mathcal W_0=\operatorname{row}[L_0N\ \ L_0AN]\subseteq\mathcal S$（固定行对空间），$V_0=\operatorname{row}(L_0N)$。

> **定理 (FW).** 固定 $\omega$ 维 $W\subseteq V$，$m\ge0$ 为自由行数。则存在 $m$ 行 $R$ 使层 $\omega$ 可行 $\iff$
> $$\exists\,\mathcal U:\quad \mathcal W_0\subseteq\mathcal U\subseteq\mathcal T_W,\quad
> \dim(\mathcal U/\mathcal W_0)\le m,\quad
> \textbf{(R)}\ \operatorname{span}(V_0\cup\pi_1(\mathcal U))=W,\quad
> \textbf{(E)}\ \pi_\lambda(\mathcal U)=W\ \ \forall\lambda .$$

**必要性.** 给定设计，令 $\mathcal U$ 为 $[L_0;R]$ 全部行对 $(rN,rAN)$ 的张成。则
$\mathcal W_0\subseteq\mathcal U$ ✓；每一行对都属于 $\mathcal T_W$（$x=rN\in\operatorname{row}H=W$、$y=rAN\in W$ 由 $(5a)'$）✓⟹$\mathcal U\subseteq\mathcal T_W$；
$\dim(\mathcal U/\mathcal W_0)\le m$（$m$ 个自由行）✓；
$(R)$：$\operatorname{span}(V_0\cup\pi_1(\mathcal U))=\operatorname{row}H=W$ ✓；
$(E)$：$\pi_\lambda(\mathcal U)$ 恰是铅笔行空间 $=\operatorname{row}(\lambda H-H_A)=W$ ✓。

**充分性.** 取 $\mathcal U$ 的一个基，其中前 $s_0$ 个张成 $\mathcal W_0$；其余 $\le m$ 个元素记为 $u_1,\dots,u_t$，
每个 $u_j=(r_jN,r_jAN)$ 由某行 $r_j$ 实现（$\mathcal S=\operatorname{row}[N\ AN]$ 的定义）✓。
把 $r_1,\dots,r_t$ 作为自由行、补零行至 $m$（补零不改变 $H,H_A$ 的行空间）✓。则
- $\operatorname{row}H=\operatorname{span}\pi_1(\mathcal U)$，由 $(R)$ 得 $\operatorname{rank}H=\omega$ ✓；
- 铅笔行空间 $=\pi_\lambda(\mathcal U)$，由 $(E)$ 得 $\operatorname{rank}(\lambda H-H_A)=\omega\ \forall\lambda$ ✓；
- $(5a)'$：$H_A$ 的行 $=\pi_2(\mathcal U)$；$(E)$ 取 $\lambda=0$ 给 $\pi_0(\mathcal U)=-\pi_2(\mathcal U)=W=\operatorname{row}H$ ⟹ 包含 ✓。

**行数精确性.** 上述构造所需自由行数恰为 $\dim(\mathcal U/\mathcal W_0)$（补零不增秩）⟹
$$q_{\min}=r_0+\min\{\dim(\mathcal U/\mathcal W_0):\ \mathcal U\ \text{满足 (FW) 的 (R)(E)}\}.$$

## 最终结论

1. **(FW) 成立**，且**不需要** "$m\ge\dim\mathcal T_W$" 这一假设 ✓ ——它被 $\dim(\mathcal U/\mathcal W_0)\le m$ 取代；
2. 原 (R)(E) 判据是 (FW) 在 $m\ge\dim(\mathcal T_W/\mathcal W_0)$ 时的**特例**（取 $\mathcal U=\mathcal T_W$）✓；
3. **行数精确性**给出 $q_{\min}$ 的新表达式，与 Paper I/II 的 $q_{\min}=r_0+t_{\min}$ 一致 ✓；
4. 于是中间层研究不再局限于"最大可用行对空间"，而是**在行数约束下选择 $\mathcal U$** ✓ ——正是专家指出的关键一步。

## 放弃原因

- 没有把 $D_I(X)$ 参数化扩展到"在 $\ker D_I$ 内再选子空间 $\mathcal U$"（阶段 3）；
- 没有处理 $\mathcal W_0$ 与 $\mathcal U$ 的相容性是否还需额外条件（如 $\mathcal W_0$ 的秩）；
- 没有做 $\mathcal U$ 选择的复杂度分析（阶段 4）。

## 残留价值

- **(FW) 的完整证明**（必要/充分/行数精确）——专家指定的最高优先目标；
- **kernel lemma 的正确版本**（需完整条件，含反例）；
- $q_{\min}$ 的新表达式，与 Paper I/II 对接。

## 下一步

阶段 3：在 $D_I(X)$ 的核空间里再引入 Grassmann 参数，描述候选 $\mathcal U$，把 (R) 变成秩条件、
(E) 变成 $(\lambda,X)$ 铅笔的最大子式 $\gcd$ 条件，并检查 leading-coefficient 引理能否移植。

## 相关文件

- [109](../../../for_expert/109_chain_from_papers.md)（被审阅的总览件）
- [470](470_explicit_R_E.md)（$D_I$ 显式判据，需并入 (FW)）
- [478](../../decision_algorithms/attempts/478_E_lambda_coupled.md)（(E) 的耦合性）
- [469](469_D_I_general.md)（正合列）

## 状态

- kernel lemma（更正版）：**[已证-纸面]**。
- (FW)：**[已证-纸面]**（必要/充分/行数精确）。
- 阶段 3（$\mathcal U$ 的 Grassmann 参数化）：**[未做]**。
