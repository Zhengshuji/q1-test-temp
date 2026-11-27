# 335 专家 96 号裁决：非特征层全坏升为**定理**，判据降为临界维度的推论

> 送审件 [96](../../../for_expert/archive/96_hyperplane_pattern_result.md)（已归档），
> 答复 [96-reply](../../../for_expert/archive/96_hyperplane_pattern_result-reply.md)。
> 96 号做了一件关键的事：**把 329 里"非常值二次"那个缺口直接证掉了**，而且不需要判别式。

## 目标

1. 落实 96 号 Q1 的统一证明（非特征层全坏）。
2. 落实 Q2 对符号证书含义的限定（"几乎所有 $t$"，不是"每个 $t$"）。
3. 落实 Q3：判据不是普遍的，而是**临界维度**的推论；给出三 regime。
4. 记录 Q4 的 Theorem 2 / Conjecture 与 Q5 的下一步。

## 设想与理由

96 号的总判断：96 号报告"在 94–95 之上实质推进"，并指出：

> **有效 $2\times2$ 行列式自动是二次、且首项系数非零**——不需要随机实验、不需要判别式、不需要 PIT。

## 做法：逐条落实

### 1. Q1：非特征层全坏的统一证明（专家的论证）

把 $C$ 显式放进 $Q$ 的基里。因为 $U\subseteq K_0\subseteq\ker C$，有 $C\in U^\perp$，故可取
$$Q=\begin{bmatrix}C\\Q_1\\Q_2\end{bmatrix}.$$
又 $CN=CAN=0$，故 $C(\lambda I-A)N\equiv0$，于是 $M=Q(\lambda I-A)N$ 的**第一行恒零**。
再把 $K_0$ 的基取成 $\widehat N=[N_1\ \ v]$；由 $Qv=QAv=0$ 得 $Q(\lambda I-A)v\equiv0$，故**最后一列恒零**。
删掉这两个强制零方向，有效铅笔是
$$B(\lambda)=\begin{bmatrix}Q_1(\lambda I-A)N_1\\Q_2(\lambda I-A)N_1\end{bmatrix}=\lambda X-G,\qquad
X=\begin{bmatrix}Q_1N_1\\Q_2N_1\end{bmatrix}\in\mathbb Q^{2\times2}.$$
由 $\operatorname{rank}(QN)=\omega=2$ 且 $\ker(QN)$ 恰是 $v$ 的坐标方向，$QN$ 在补空间上单射 ⟹
$$\boxed{\operatorname{rank}X=2}.$$
于是 $\det B(\lambda)=\lambda^2\det X+\text{（$\le1$ 次项）}$，$\det X\ne0$ ⟹ $\deg_\lambda\det B=2$ ⟹
$\det B$ 有复根 $\lambda_*$ ⟹ $\operatorname{rank}B(\lambda_*)<2=\omega$ ⟹ $(5b)$ 失败。$\square$

**关键点**：不需要判别式；**重根也算根**。这比 329 的"实例级 + 判别式非零"强得多。

**推广（三 regime）**：$n-2-p$ 与 $k-1$ 的比较

| 情形 | 非特征层的性质 |
|---|---|
| $n-2-p<k-1$ | **自动坏**（秩界）；无需任何特征值论证 |
| $n-2-p=k-1$ | **必坏**：约简铅笔是方阵、首项系数可逆 ⟹ $\det$ 次数恰为 $k-1\ge1$ ⟹ 有复根。本报告的模式正是这一档（$5-2-1=2=k-1$），且结论对任意方阵 $r\times r$ 都成立 |
| $n-2-p>k-1$ | 约简铅笔是**高**矩阵，秩界不迫使降秩；归一化后等价于**可观测性**。非特征点**可能好** |

### 2. Q2：符号证书的确切含义（必须改口径）

$\gcd=1$ 在 $\mathbb Q(t)[\lambda]$ 上 ⟹ 存在 $b_i\in\mathbb Q[t,\lambda]$ 与 $0\ne d\in\mathbb Q[t]$ 使
$$\sum_i b_i(t,\lambda)m_i(t,\lambda)=d(t).$$
凡 $d(t_0)\ne0$ 的特化都**好** ⟹ **除有限个 $t$ 外全好**，特别地**存在有理好点**。
但**不能**说"每个 $t$ 都好"（特化可以制造公因子）。
**333 里"每一条 $t$ 都好"的措辞必须改正。**

对一般 $A$：五个实例**不**给 universal-$A$ 定理（只能给 generic-$A$）。特化方向不可逆；
专家建议：**直接构造**好的特征纤维行空间，而不是靠 universal PIT。

### 3. Q3：判据不是普遍原则，是临界维度的推论

**不能**把"$K_0$ 含特征向量"当作一般判据。正确的普遍形式是

$$\boxed{\text{可行性}\iff\text{某个可容许层含有一个"约简铅笔可观测"的点}}$$

- 临界档（$=k-1$）：非特征点全坏 ⟹ 只剩特征纤维可能可行（这正是本模式）；
- 富余档（$>k-1$）：非特征点本身可能好 ⟹ 特征向量不再是必要条件。

### 4. Q4：可以声称什么

**Theorem 2（临界模式的超平面归约）**：在 $n=5,p=1,q=3,r_0=0$、$\operatorname{rank}[C;CA]=2$、$\dim K_0=3$ 下，
1. 非特征核方向的每个层点都违反 $(5b)$（**统一证明**）；
2. 故 $E=\varnothing$ ⟹ 层不可行；
3. $E\ne\varnothing$ 时，层可行 $\iff$ 某个特征纤维含谱可行点；
4. 对展示的实例与另外五个测试实例，符号单参数证书给出这样的点。

前三条是定理；第四条是**计算证据**，不是 universal 定理。

**Conjecture（临界模式的纤维充分性）**：满足上述假设的每个有理输入，若 $K_0$ 含 $A$ 的特征向量，
则对应特征纤维含**有理**谱可行行空间。

> **该猜想已被反例否定（[336](336_fibre_sufficiency_counterexample.md)）**：实例
> $A=\begin{pmatrix}2&2&-1&0&0\\0&-2&1&0&1\\0&1&-2&0&-1\\0&0&0&0&2\\0&-1&2&0&-1\end{pmatrix}$、$C=e_5^{\mathsf T}$ 中
> $e_1$ 是 $K_0$ 的特征向量，但 $\dim(A K_0)=\omega=2$ 且 $e_1\in A K_0$ ⟹ 任何层点
> $\operatorname{rank}H_A\le1<\omega$ ⟹ $(5b)$ 在 $\lambda=0$ 即失败 ⟹ 整条纤维全坏（c341：20/20）。
> 缺失的条件：$\operatorname{rank}H_A=\omega$（$\lambda=0$ 的秩）。

**复杂度**：特征向量判定多项式时间；**一旦猜想成立**，本模式的判定就是多项式时间（判据即特征向量存在性）。

### 5. Q5：下一步

专家的顺序：① **在当前模式上把 $A$ 一般化**（最短路径到完整定理；负面已定，只差纤维充分性）；
② 高维特征空间（$\dim\ker(A-\lambda_0I)\cap K_0\ge2$）；③ 再进 $n=6,p=1,q=4$。
他建议下一份报告专门攻**纤维充分性**（构造性，而不是 PIT）。

## 进展

- 329 的"非常值"缺口**已闭合**（统一证明）；
- 331 的判据**降级**为临界模式的推论，并补上三 regime；
- 333 的"每个 $t$ 都好"**改为**"除有限个 $t$ 外都好；足以给出有理好点"；
- 328 的"$\operatorname{rank}X=k-1$"由"前提 + 实例核对"升为**引理**（专家证明）；
- STATUS/ATTEMPTS/ROADMAP 同步。

## 最终结论

1. **本模式的负面侧现在是定理**（不依赖任何计算）。
2. 正面侧只剩一个干净的猜想（纤维充分性）；一旦证明，本模式得到**多项式时间判定**。
3. 判据的普遍形式是三 regime 的"可观测性"表述，不是"特征向量存在"。

## 放弃原因

- 没有攻纤维充分性（专家建议作为下一份报告的主题）；
- 没有做高维特征空间与 $n=6$ 的模式。

## 残留价值

- 一个统一的负面定理（含三 regime 的结构判据 $n-2-p$ vs $k-1$）；
- 符号证书的正确口径（"除有限个 $t$ 外"）；
- 一个干净、可攻的猜想（纤维充分性）与它的复杂度含义。

## 相关文件

- 送审件：[96](../../../for_expert/archive/96_hyperplane_pattern_result.md)
- 答复：[96-reply](../../../for_expert/archive/96_hyperplane_pattern_result-reply.md)
- [attempts/329](329_forced_relations_quotient_pencil.md)（强制关系；"非常值"缺口已闭合）
- [attempts/331](331_eigenvector_criterion.md)（判据；已降级）
- [attempts/333](333_eigen_fibre_symbolic_certificate.md)（符号证书；口径已改）
- [attempts/328](../../decision_algorithms/attempts/328_quotient_pencil_theorem.md)（商铅笔；$\operatorname{rank}X$ 已是引理）
- [c339](../../../../tools/verification/c339_symbolic_eigen_certificate.py)、[c340](../../../../tools/verification/c340_family_symbolic_certificate.py)

## 状态

- 负面定理：**[已证-纸面]**（专家 96 号）。
- 正面侧：**计算证据 + 猜想**。
- 判据：**仅临界模式**。

## 专家复核意见（裁决）

| 问题 | 96 号裁决 | 落实 |
|---|---|---|
| Q1 非常值性 | **自动成立**：$\operatorname{rank}X=2$ ⟹ $\det B$ 是次数恰为 2 的多项式 ⟹ 有复根；判别式无关、重根也算根 | 已作为统一证明写入 §1；329 缺口闭合 |
| Q2 符号证书 | 只证"除有限个 $t$ 外好"，但足以给出**有理好点**；五实例不构成 universal-$A$ | 333 口径已改；记录 Target A/B 之别 |
| Q3 判据普遍性 | **不是**普遍原则，是 $n-2-p=k-1$ 的推论；普遍形式是"某层含可观测约简铅笔的点" | 331 已降级并补三 regime |
| Q4 进展 | 是；写成 Theorem 2 + Conjecture；复杂度：猜想成立 ⟹ 多项式时间 | 已写入本文件 |
| Q5 下一步 | ① 当前模式一般化 $A$ ② 高维特征空间 ③ $n=6$ | 已记入 ROADMAP |
