# 专家对 108 号的答复（要点存档）

> 用户在会话中直接粘贴了完整评审正文；本文件是**结构化要点存档**（不是逐字全文），
> 逐条落实见 [attempts/463](../../q1_false/decision_algorithms/attempts/463_expert108_audit.md)。

## 1. 认可

- **固定 $W$ 的 (R)(E) 判据**是整份报告最值得保留的结果；它把耦合的两个条件**分开**了：
  (R) 管行空间生成（$\operatorname{rank}H=\omega$）、(E) 管谱条件。
- **(E) 的化简正确**：$E_\lambda=\lambda\pi_1+\pi_2$，$\lambda=0$ 给 $\pi_2=W$，反向显然 ⟹
  $(E)\iff\pi_2(\mathcal T_W)=W$ ✓，且**没有隐藏的谱假设**。
- **(R) 不能省** ✓（$\mathcal T_W=\{0\}\oplus W$ 的反例）；谱条件管第二分量、行秩管第一分量，
  是**两个不同的几何约束**，不能互替。
- 纠错方向（"中间层并非必然不可行"等）**正确**。

## 2. 记号冲突（必须立即改）

我写 $W\subseteq V$ 且 $\dim W=\omega$，又写 $\omega+1\le\dim W\le2\omega$——**矛盾** ✗。
Paper I 的界约束的是 $\widehat W=\operatorname{row}[H\ H_A]\subseteq V\oplus V$，不是 $V$ 里的 $W$。
建议改名为：$U\subseteq V$（$\dim U=\omega$）、$\mathcal T_U=\mathcal S\cap(U\oplus U)$、
$\widehat W=\operatorname{row}[H\ H_A]$，且 $\widehat W\subseteq\mathcal T_U$（一般**不相等**）。

## 3. chartwise 判定**还不是定理**（最关键的缺口）

- **Bézout 论证过强**：清分母后得到 $D(X)=\sum a_i(X)f_i(X,\lambda)$，其中 $D$ 是**非零多项式**而**不是 1**；
  $D(X_0)=0$ 处不能保证互素 ⟹ 函数域互素只保证**某个开集**，不是"整卡" ✗。
- 这也正是 Paper III 需要 **full-rank leading-coefficient lemma** 的原因（排除 $\lambda$-次数同时下降）。
- **实点问题**：即使泛型点可行，相应开集未必含实点 ⟹ 需要实代数几何处理。
- **他建议的更简单路线（重要）**：在固定秩层上取 $\mathcal T_W$ 的基 $Z(X)=[Z_1(X);Z_2(X)]$，则
  $$(R)\iff\operatorname{rank}\begin{bmatrix}H_0\\Z_1(X)\end{bmatrix}=\omega,\qquad
  (E)\iff\operatorname{rank}Z_2(X)=\omega,$$
  **同一不可约参数层上的两个泛型秩条件**，两者各给非空开集，不可约性保证交非空 ✓。
  —— 比最大子式 $\gcd$ 简单得多，可能是真正的突破口。但必须限定在**同一不可约层**上。

## 4. 对五问的答复

- **Q1**：几何上的泛型秩思路**可推广**到任意 $\omega$；Paper III 的 **$\gcd$ 论证不可照搬**
  （超平面层有 $\dim\ker H=1$ 的特殊结构，中间层 $\dim\ker H=k-\omega>1$）。
- **Q2**：chart 数 $\binom{k-d}{\omega-d}\le n^{O(\ell)}$ ⟹ 给出的是 **XP**，**不是 FPT**；
  不能声称优于 Paper I 的 $\exp(O(\ell^2\log(\ell+2)))\operatorname{poly}(L)$。
  单 chart 的位复杂度（有理基、符号秩、次数与系数增长、分支处理、实点）**未估**。
- **Q3**：**不要**选 0–1 线性可行性（它是 NP-难，不是自然的 $\exists\mathbb R$-难目标）。
  更匹配的是**受约束的子空间配置实现**问题（$\dim(W\cap U_i)=a_i$ 型），并须证明能嵌入**同一个** $W$ 的两个条件。
- **Q4**：(R) 适合编码**生成/包含**，(E) 适合编码**交/投影满射**；但**两者必须同一个 $W$**，
  分别存在不能合并。归约目标是 $\exists W:\operatorname{rank}F_1(W)=a\wedge\operatorname{rank}F_2(W)=b$。
- **Q5**：优先做**命题 A（固定秩层的泛型秩判据 + 实点条件）**；再做 B（复杂度）、最后 C（硬度归约）。

## 5. 两处表述澄清

- **fibrewise rigidity** 的表述要精确：应写成"固定 $W$ 后允许的自由行对构成 $\mathcal T_W$；
  满足行秩要求的选择构成开集；当 $m\ge\dim\mathcal T_W$ 时存在可行选择 $\iff$ (R)(E)"，
  而不是"Zariski 开 ⟹ 不能再加约束"。
- **实验只支持猜想**：需升级为精确有理算术测试，覆盖六种情形（不同 chart 的差异、$\operatorname{rank}M(q)$ 在卡内变化、
  只有 (R)、只有 (E)、两者分别可行但无共同解、可行集只在低维秩层）——尤其后两种能检验耦合是否处理正确。

## 6. 他建议的三命题

- **命题 A**：固定秩层上的泛型秩判据（含实点稠密性）；
- **命题 B**：中间层算法的位复杂度（chart 数、秩层与分支数、单分支代价、总体界；明确 XP/FPT）；
- **命题 C**：若算法受阻，再找从已知 $\exists\mathbb R$-难子空间实现问题到 (R)(E) 的归约。

**最终判词**：报告是"一次很好的理论纠偏"，(R)(E) 的分离"可能比直接研究最大子式 gcd 更有利于揭示中间层结构"；
但**不要把 constructible、泛型点可判定、每卡一次计算、多项式时间当成同一件事**。
