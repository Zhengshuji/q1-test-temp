# 463 专家 108 号：记号冲突 + "整卡"论证过强；他给了更简单的泛型秩路线

> 送审件 [108](../../../for_expert/archive/108_middle_layer_decision.md)（已归档），
> 答复要点 [108-reply](../../../for_expert/archive/108_middle_layer_decision-reply.md)。
> **总评**：判据与 $(E)$ 的化简被认可（"最值得保留的结果"）；但**记号冲突**、
> **chartwise 判定还不是定理**，且他给出了一条**更简单的替代路线**。

## 目标

逐条落实：记号改名、(R)(E) 的严谨化、撤回"整卡"、采用他的泛型秩命题、记录 Q1–Q5 裁决。

## 设想与理由

审计型回复。这次的关键是**两处硬错**（记号冲突、Bézout 论证过强），以及**一条更好的路线**。

## 做法与结果

### 1. 记号冲突（必须立即改）

我写 $W\subseteq V$、$\dim W=\omega$，又写 $\omega+1\le\dim W\le2\omega$ —— **自相矛盾** ✗。
Paper I 的界约束的是 $\widehat W=\operatorname{row}[H\ H_A]\subseteq V\oplus V$，不是 $V$ 里的行空间。

**改名（采纳）**：

| 旧 | 新 | 含义 |
|---|---|---|
| $W\subseteq V$ | $U\subseteq V$，$\dim U=\omega$ | 第一分量行空间 |
| $\mathcal T_W$ | $\mathcal T_U=\mathcal S\cap(U\oplus U)$ | 可用压缩行对空间 |
| （无） | $\widehat W=\operatorname{row}[H\ H_A]\subseteq\mathcal T_U$ | 实际设计产生的行对空间（**一般 $\ne\mathcal T_U$**） |

⟹ $\omega+1\le\dim\widehat W\le2\omega$（界针对 $\widehat W$）✓；而 $\dim\mathcal T_U$ 是"构造自由行所需行数"的界，
两者**不是同一个量** ✓。

### 2. 撤回"整卡"（Bézout 论证过强）

我写"函数域 $\gcd=1$ ⟹ 该卡每点可行"——**过强** ✗。
清分母后得到的是 $D(X)=\sum a_i(X)f_i(X,\lambda)$，$D$ 是**非零多项式而非 $1$**；
$D(X_0)=0$ 处不能保证互素 ⟹ 函数域互素只给**某个非空开集** ✓。
这正是 Paper III 需要 **full-rank leading-coefficient lemma** 的原因。

⟹ 461/462 的"每卡一次计算"必须降级为"**每卡一个非空开集**"，并**加上实点条件**。

### 3. 他给的更简单路线（本轮最重要的收获）

在固定秩层上取 $\mathcal T_U$ 的基 $Z(X)=\begin{bmatrix}Z_1(X)\\Z_2(X)\end{bmatrix}$，则

$$\textbf{(R)}\iff\operatorname{rank}\begin{bmatrix}H_0\\Z_1(X)\end{bmatrix}=\omega,\qquad
\textbf{(E)}\iff\operatorname{rank}Z_2(X)=\omega .$$

**同一不可约参数层上的两个泛型秩条件**：各给一个非空 Zariski 开集，不可约性 ⟹ 交仍非空 ✓。
—— 比最大子式 $\gcd$ 简单得多，**且不需要 leading-coefficient 引理** ✓。

**注意**：这给的是"代数闭包上的存在性"；要得到**实**设计存在，还需实点稠密性（他的命题 A）。

### 4. Q1–Q5 裁决（要点）

| 问 | 裁决 |
|---|---|
| Q1 | 泛型秩思路**可推广**到任意 $\omega$；Paper III 的 **$\gcd$ 论证不可照搬**（超平面层有 $\dim\ker H=1$） |
| Q2 | chart 数 $\binom{k-d}{\omega-d}\le n^{O(\ell)}$ ⟹ **XP，不是 FPT**；**不能**声称优于 Paper I 的 FPT；单 chart 位复杂度未估 |
| Q3 | **不要**选 0–1 线性可行性（NP-难，非自然 $\exists\mathbb R$-难）；选**受约束的子空间配置实现**问题 |
| Q4 | (R) 编码生成/包含、(E) 编码交/投影；但**必须同一个 $U$**，分别存在不能合并 |
| Q5 | 优先**命题 A**（固定秩层泛型秩判据 + 实点），再 B（复杂度），最后 C（硬度） |

### 5. 两处表述澄清

- **fibrewise rigidity** 的措辞要精确：固定 $U$ 后允许的自由行对构成 $\mathcal T_U$；满足行秩要求的选择构成开集；
  $m\ge\dim\mathcal T_U$ 时存在可行选择 $\iff$ (R)(E)。**不是**"Zariski 开 ⟹ 不能再加约束"。
- **实验只支持猜想**：需升级为精确有理算术测试，覆盖六种情形（不同 chart、$\operatorname{rank}M(q)$ 卡内变化、
  仅 (R)、仅 (E)、分别可行但无共同解、可行集只在低维秩层）。

## 进展

1. 记号已改名（$U$ / $\mathcal T_U$ / $\widehat W$）；
2. "整卡"撤回，正确表述为"每卡一个非空开集 + 实点条件"；
3. 采用他的泛型秩命题作为**下一步的主命题**（命题 A）；
4. 五问裁决全部记录。

## 最终结论

1. **判据（R)(E) 成立**、(E) 化简正确、(R) 不可省 ✓——这是保留的核心；
2. **两处硬错已改**：记号冲突、"整卡"过强；
3. **下一步的唯一瓶颈**：命题 A（固定秩层的泛型秩判据 + 实点稠密性）；
4. **复杂度**：即使做成，给的是 **XP**（$n^{O(\ell)}$），不是 FPT——不能与 Paper I 的 FPT 争长短；
5. **硬度**：放弃 0–1 可行性，改找**受约束子空间配置**的已知 $\exists\mathbb R$-难版本。

## 放弃原因

- 没有写出命题 A 的证明（只采纳了形式）；
- 没有做六种情形的精确有理算术测试；
- 没有开始子空间配置的归约。

## 残留价值

- **一条更简单的技术路线**（两个泛型秩条件 + 不可约性），比 $\gcd$ 路线干净；
- 记号与表述的修正，避免把 $\widehat W$ 与 $\mathcal T_U$ 混为一谈；
- 明确 XP vs FPT 的分界，防止夸大。

## 下一步

写命题 A：在固定秩层的不可约分支上，证明"$\exists X$ 使两个秩条件成立 $\iff$ 两个函数域秩条件成立"，
并补实点稠密性（或给出反例说明实点缺失）。

## 相关文件

- [108](../../../for_expert/archive/108_middle_layer_decision.md)、[108-reply](../../../for_expert/archive/108_middle_layer_decision-reply.md)
- [461](../../c_stratification/attempts/461_whole_chart.md)（被本文件撤回"整卡"）
- [462](../../c_stratification/attempts/462_chart_check.md)（实验，仅支持猜想）
- [452](../../c_stratification/attempts/452_E_simplified.md)（(E) 化简，被认可）

## 状态

- 记号改名：**[完成]**。
- "整卡"：**[已撤回]**。
- 命题 A：**[未写]**。
- 复杂度（XP vs FPT）：**[已定界]**。
