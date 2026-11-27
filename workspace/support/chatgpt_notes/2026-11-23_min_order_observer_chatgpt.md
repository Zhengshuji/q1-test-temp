# ChatGPT：最小阶功能观测器研究进展

> 来源：ChatGPT 网页版（本机 Edge 插件浏览器），对话标题「最小阶观测器进展」，2026-11-23。
> 提问：最小阶功能观测器的研究有什么最新进展？请给出近两年的代表性工作、关键判据和仍未解决的问题，回答尽量完整。
> **AI 生成内容，未经核实，不能作为文献依据；文中引用需回查原文。**

---
# 最小阶功能观测器研究的最新进展：理论判据、优化方法与计算复杂性（2024—2026）

## 一、研究现状与总体判断

最小阶功能观测器（Minimum-Order Functional Observer, MOFO）的研究处于一个值得关注的阶段：传统控制理论已经建立了相当成熟的功能观测器存在性条件、结构化设计方法和降阶实现理论，但对于**如何严格确定最小观测器阶数，以及如何有效求解最小阶设计问题**，仍然存在值得深入研究的理论和算法问题。

首先，需要区分三个不同的问题：

1. **存在性问题（Existence）**：给定系统和待估计的状态函数，是否存在阶数为 \(q\) 的功能观测器？
2. **最小阶数问题（Minimum-order determination）**：满足功能估计要求的最小观测器阶数是多少？
3. **最优实现问题（Optimal synthesis）**：在最小阶数下，如何构造满足稳定性、可观测性和实现约束的观测器？

这三个问题在已有文献中经常被放在同一框架下讨论，但它们的数学难度并不相同。

特别需要指出：**最小代数阶数不一定等于最小稳定功能观测器阶数。** 一个观测器可能满足代数上的可实现条件，却无法满足所要求的渐近稳定性条件。因此，不能仅凭一个秩条件就认定已经解决了最小阶功能观测器问题。

对于近两年的研究，我建议重点考察四条主线：

- 功能观测器存在性与最小阶数的代数刻画；
- 基于矩阵铅笔、有限零点和多项式矩阵的稳定性判据；
- 基于子空间、Grassmann 流形和不变子空间的结构化设计；
- 固定阶数可行性与最小阶数问题的计算复杂性。

下面将这些问题分别展开，并区分已经建立的理论、近年值得关注的研究方向以及尚未解决的问题。

## 二、近两年的代表性研究工作

这里将时间范围设为 2024 年 1 月至 2026 年 11 月 23 日。需要区分正式发表的期刊论文与尚处于预印本阶段的工作。尤其是 2026 年的两篇论文，目前应按照 arXiv 预印本引用，不能直接视为已经经过期刊同行评审的成果。

### 2.1 2024 年：Descriptor 系统的功能观测器存在性条件

**论文 1**

Juhi Jaiswal, Thomas Berger, Nutan Kumar Tomar,

*Existence conditions for functional ODE observer design of descriptor systems revisited.*

Journal of the Franklin Institute, 361(8), 106848, May 2024.

DOI: [10.1016/j.jfranklin.2024.106848](https://doi.org/10.1016/j.jfranklin.2024.106848)

这篇论文研究的是线性时不变 Descriptor 系统中的功能 ODE 观测器设计问题。

一般 Descriptor 系统表示为

\[
E\dot{x}=Ax+Bu,
\]

\[
y=Cx.
\]

与常规状态空间系统不同，这里 \(E\) 不一定可逆，因此系统可能包含代数约束、无穷特征值以及非标准动态结构。

论文的主要贡献包括：

1. 对已有的功能 ODE 观测器存在性条件进行了推广。
2. 提出了更加宽松的代数充分条件。
3. 直接利用系统系数矩阵构造观测器参数。
4. 给出了阶数不超过待估计功能维数的观测器构造方法。

**对最小阶问题的意义**

这篇论文的重要性在于，它说明功能观测器的存在性研究可以不局限于标准状态空间模型。

但是需要注意：

- 论文主要研究 Descriptor 系统的功能 ODE 观测器存在性和构造。
- 它没有建立一般意义上的最小阶数优化理论。
- 阶数不超过功能维数的构造结论，不等价于最小阶数的精确刻画。

因此，这篇论文更适合作为功能观测器代数存在性理论的补充，而不是最小阶功能观测器问题的直接解决方案。

### 2.2 2025 年：功能可观测性和功能观测器设计的统一框架

**论文 2**

Mohamed Darouach, Tyrone Fernando,

*On functional observability and functional observer design.*

Automatica, 173, Article 112115, March 2025.

DOI: [10.1016/j.automatica.2025.112115](https://doi.org/10.1016/j.automatica.2025.112115)

这是近两年值得重点关注的工作之一。

该论文重新讨论了 Functional Observability 的定义和判据，并研究了具有极点配置能力的功能观测器设计。

其核心思想是：不必要求整个系统完全可观测，只需要待估计的状态函数能够从输入输出信息中重构。

对于系统

\[
\dot{x}=Ax+Bu,\qquad y=Cx,
\]

待估计量为

\[
z=Lx.
\]

经典状态可观测性要求

\[
\operatorname{rank}
\begin{bmatrix}
C\\
CA\\
\vdots\\
CA^{n-1}
\end{bmatrix}=n.
\]

而功能可观测性只要求

\[
\operatorname{rank}
\begin{bmatrix}
\mathcal O_C\\
\mathcal O_L
\end{bmatrix}
=
\operatorname{rank}(\mathcal O_C),
\]

其中

\[
\mathcal O_C=
\begin{bmatrix}
C\\CA\\\vdots\\CA^{n-1}
\end{bmatrix},
\qquad
\mathcal O_L=
\begin{bmatrix}
L\\LA\\\vdots\\LA^{n-1}
\end{bmatrix}.
\]

换言之，

\[
\operatorname{row}(\mathcal O_L)
\subseteq
\operatorname{row}(\mathcal O_C).
\]

这意味着即使整个状态不可观测，只要所需功能量可以从输出历史中恢复，仍然可能存在功能观测器。

论文进一步研究了不同阶数的功能观测器构造，并将其与极点配置联系起来。

**这项工作的主要价值**

它把以下几个概念联系起来：

- Functional Observability；
- Functional Detectability；
- Reduced-order Functional Observer；
- Pole Placement；
- Observer-based Control。

特别是，作者讨论了当阶数为 \(r\) 的观测器不能构造时，增加辅助功能维数，继续寻找更高阶观测器的可能性。

这对最小阶研究很重要，因为它说明：

\[
q=r
\]

并不总是可行，但这并不意味着必须直接采用完整的降阶 Luenberger 观测器。

中间阶数的功能观测器可能存在。

这也是 2026 年最小阶数完整刻画工作的一个重要理论背景。

### 2.3 2025 年：Functional Observability、结构功能可观测性与传感器配置

**论文 3**

Yuan Zhang, Tyrone Fernando, Mohamed Darouach,

*Functional Observability, Structural Functional Observability and Optimal Sensor Placement.*

IEEE Transactions on Automatic Control, 70(3), 1592–1607, March 2025.

DOI: [10.1109/TAC.2024.3462558](https://doi.org/10.1109/TAC.2024.3462558)

这篇论文与最小阶功能观测器问题有密切联系，但研究目标并不相同。

其主要贡献是：

1. 建立功能可观测性与功能可检测性的新判据。
2. 提出 Modal Functional Observability。
3. 建立结构功能可观测性的图论刻画。
4. 研究最少传感器配置问题。
5. 对相关传感器选择问题给出 NP-hard 性证明，并建立具有近似保证的贪心算法。

其中最值得注意的是复杂性结果。

作者证明，从候选传感器集合中选择最少数量的传感器以实现功能可观测性，在一般情况下是 NP-hard 的。

但是，这里必须严格区分：

\[
\boxed{
\text{最少传感器配置}
\ne
\text{最小阶功能观测器设计}
}
\]

两者具有相似的优化结构，但决策变量和约束条件不同。

前者选择的是测量矩阵 \(C\) 的行，后者通常是在 \(A,C,L\) 给定时寻找辅助矩阵 \(R\)，使得增广功能矩阵

\[
\mathcal L=
\begin{bmatrix}
L\\R
\end{bmatrix}
\]

能够构造满足要求的观测器。

因此，这篇论文的 NP-hard 结果不能直接作为最小阶功能观测器问题 NP-hard 的证明。

不过，它提供了非常有价值的研究方法：利用图论结构、子模函数以及组合优化分析功能可观测性相关问题。

### 2.4 2025 年：强功能观测器的存在性

**论文 4**

Michael Di Loreto, Damien Eberard,

*On the existence of strong functional observer.*

arXiv:2502.03917, February 2025.

链接：[arXiv:2502.03917](https://arxiv.org/abs/2502.03917)

这项工作研究了 Strong Functional Observer。

它与传统功能观测器的一个重要区别是：估计对象可以同时包含状态函数和输入函数，而且要求估计误差对初始状态及输入具有相应的收敛性质。

论文提出了相应的必要充分存在性条件，并通过 Functional Detectability 及其推广进行刻画。

其研究价值在于拓展了功能观测器的适用范围。

但它并不是针对传统无输入重构要求的最小阶功能观测器优化问题，因此不能将其存在性定理直接转换成传统 MOFO 的最小阶数判据。

### 2.5 2025 年：部分可检测性与 Descriptor 系统的广义功能观测器

**论文 5**

Juhi Jaiswal, Thomas Berger, Nutan Kumar Tomar,

*Partial detectability and generalized functional observer design for linear descriptor systems.*

Franklin Open, 10, Article 100238, March 2025.

DOI: [10.1016/j.fraope.2025.100238](https://doi.org/10.1016/j.fraope.2025.100238)

该论文研究线性 Descriptor 系统中的 Partial Detectability。

主要结果包括：

- 给出部分可检测性的必要充分秩判据。
- 利用 Wong sequences 给出几何刻画。
- 建立部分可检测性与广义功能估计器存在性之间的联系。
- 证明部分可检测性本身并不足以保证广义功能观测器存在，还需要额外的代数条件。

这里有一个重要的理论启示：

**可检测性条件与观测器可实现条件并不总是等价。**

即使系统在所关注的方向上具有某种可检测性，也可能因为观测器结构的限制而无法构造相应的估计器。

这与最小阶功能观测器中的代数条件和谱条件必须分别考虑的思想是一致的。

### 2.6 2025 年：功能可控性与广义分离原理

**论文 6**

Tyrone Fernando, Mohamed Darouach,

*Functional Controllability, Functional Stabilisability, and the Generalised Separation Principle.*

IEEE Transactions on Automatic Control, 2025/2026 年发表记录。

DOI: [10.1109/TAC.2025.3634469](https://doi.org/10.1109/TAC.2025.3634469)

这篇工作研究 Functional Controllability、Functional Stabilisability，以及广义分离原理。

其主要意义是建立功能可观测性和功能可控性之间的对偶关系，并进一步研究在系统不完全可控、不可观测的情况下，如何进行功能观测器与功能控制器的联合设计。

它并不直接解决最小阶观测器问题，但对于将最小阶功能观测器理论推广到功能观测器控制系统具有重要意义。

---

## 三、2026 年的关键进展：最小阶功能观测器的完整刻画

在我检索到的近两年工作中，2026 年 9 月的两篇预印本与最小阶功能观测器问题的关系最直接。

它们值得单独分析，因为研究重点已经从传统的存在性条件转向：

- 最小代数可行阶数；
- 最小阶增广结构；
- 指定阶数的完整可行性；
- 最小稳定观测器阶数；
- 所有可行阶数的完整刻画。

### 3.1 论文 7：A Minimum-Order Functional Observer Beyond the Darouach and Luenberger Constructions

Tyrone Fernando,

*A Minimum-Order Functional Observer Beyond the Darouach and Luenberger Constructions.*

arXiv:2609.33615, September 27, 2026.

链接：[arXiv:2609.33615](https://arxiv.org/abs/2609.33615)

与最小阶问题直接相关

这篇论文是近两年最值得重点阅读的工作之一。

#### （1）研究动机

经典功能观测器设计主要涉及两种结构：

- Darouach 功能观测器，阶数通常为待估计功能的独立维数 \(r\)；
- Reduced-order Luenberger observer，阶数为 \(n-p\)（在完全可观测且输出独立的标准情形下）。

但是，两者并不能覆盖所有可能的最小阶功能观测器。

论文指出：

即使 Darouach 阶数的观测器不存在，也不意味着所有功能观测器都不存在。

同时，也不意味着必须重构全部未测量状态方向。

因此，最小阶数可能严格处于两个经典阶数之间。

#### （2）Functional Observability Indices

论文引入 Functional Observability Indices。

设

\[
\dot x=Ax+Bu,\qquad y=Cx,\qquad z=Lx.
\]

通过考察

\[
C,\ CA,\ CA^2,\ldots
\]

和

\[
L,\ LA,\ LA^2,\ldots
\]

所生成的行空间，构造一组有序的独立行。

具体地，将 \(C\) 和 \(L\) 的各行作为生成元：

\[
g_1,\ldots,g_{p+r}.
\]

按照递增的 \(A\) 次幂逐层检查：

\[
g_1,\ldots,g_{p+r};
\]

\[
g_1A,\ldots,g_{p+r}A;
\]

\[
g_1A^2,\ldots,g_{p+r}A^2;
\]

依此类推。

每次只保留能够增加当前矩阵秩的行。

对于功能矩阵 \(L\) 的第 \(j\) 行，定义对应的 Functional Observability Index：

\[
\eta_j.
\]

论文证明，满足代数观测器存在条件的最小功能维数为

\[
\boxed{
q_0=\sum_{j=1}^{r}\eta_j.
}
\]

其中

\[
r\leq q_0\leq n-p.
\]

这给出了一个重要的下界：

\[
\boxed{q_{\min}\geq q_0.}
\]

需要特别强调，\(q_0\) 是满足代数条件的最小阶数，而不一定是最终的最小稳定观测器阶数。

#### （3）代数条件与谱条件分离

该论文将观测器存在性分解为两个条件。

代数条件：

\[
\operatorname{rank}
\begin{bmatrix}
\mathcal LA\\
\mathcal L\\
CA\\
C
\end{bmatrix}
=
\operatorname{rank}
\begin{bmatrix}
\mathcal L\\
CA\\
C
\end{bmatrix}.
\tag{A}
\]

谱条件：

\[
\operatorname{rank}
\begin{bmatrix}
\lambda\mathcal L-\mathcal LA\\
CA\\
C
\end{bmatrix}
=
\operatorname{rank}
\begin{bmatrix}
\mathcal L\\
CA\\
C
\end{bmatrix}.
\tag{S}
\]

这里

\[
\mathcal L=
\begin{bmatrix}
L\\R
\end{bmatrix}.
\]

对于任意复数 \(\lambda\)，条件 (S) 对应任意极点配置能力。

如果只要求渐近稳定，则可以将谱条件的检验区域限制为

\[
\Omega_S=\{\lambda\in\mathbb C:
\operatorname{Re}\lambda\geq0\}.
\]

也就是说，只需要排除无法通过观测器参数配置而消除的非稳定区域特征值。

#### （4）一个非常重要的结论：最小阶增广矩阵可能不唯一

假设已经确定

\[
q_0=\sum_{j=1}^{r}\eta_j.
\]

这并不意味着达到 \(q_0\) 的增广矩阵 \(\mathcal L\) 是唯一的。

可能存在多个满足条件 (A) 的增广矩阵：

\[
\mathcal L_1,\mathcal L_2,\ldots
\]

但它们的谱条件满足情况不同。

例如：

\[
\mathcal L_1:
\quad (A)\text{ 成立},\quad(S)\text{ 不成立},
\]

而

\[
\mathcal L_2:
\quad (A)\text{ 成立},\quad(S)\text{ 成立}.
\]

因此，不能通过随意构造一个最小代数增广矩阵，再检验它是否满足谱条件，就判断最小阶观测器是否存在。

必须考察整个最小代数可行增广族。

论文对此给出了完整的最小代数阶增广族刻画，以及最小代数阶数同时满足谱条件的必要充分条件。

这是非常值得重视的理论进展。

### 3.2 论文 8：Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger

Tyrone Fernando,

*Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger.*

arXiv:2609.37992, September 29, 2026.

链接：[arXiv:2609.37992](https://arxiv.org/abs/2609.37992)

最直接涉及逐阶完整判据

这篇论文进一步将前一篇论文的最小阶分析推广到所有可能的阶数。

其核心问题是：

假设最小代数阶数 \(q_0\) 无法满足谱条件，那么是否可以增加阶数，构造一个稳定功能观测器？

如果可以，应该如何确定下一个可行阶数？

论文给出了系统的逐阶刻画。

#### （1）最小阶数区间

设

\[
n_0=\operatorname{rank}(\mathcal O_C).
\]

在功能可观测条件下，论文给出代数可行阶数的区间：

\[
\boxed{
q_0\leq q\leq n_0-p.
}
\]

其中：

\[
q_0=\sum_{j=1}^{r}\eta_j
\]

是最小代数可行阶数，而

\[
n_0-p
\]

是由功能可观测性决定的上界。

当系统完全可观测时，

\[
n_0=n,
\]

因此上界退化为经典降阶 Luenberger 观测器阶数：

\[
q_{\max}=n-p.
\]

#### （2）代数可行阶数不存在间断

论文的 Theorem 2 给出一个重要结论：

如果系统功能可观测，那么对于每一个满足

\[
q_0\leq q\leq n_0-p
\]

的整数 \(q\)，都存在满足代数条件 (A) 的增广矩阵。

而所有

\[
q<q_0
\]

均不满足代数条件。

这意味着代数可行阶数具有无间隙性质：

\[
\boxed{
\Sigma_A=
\{q_0,q_0+1,\ldots,n_0-p\}.
}
\]

注意，这个结论只针对代数可行性。

它并不意味着谱可行阶数同样没有间隙。

也就是说：

\[
q\in\Sigma_A
\]

不一定推出

\[
q\in\Sigma_{FO}.
\]

其中

\[
\Sigma_{FO}
=
\{q:\text{存在同时满足 (A)、(S) 的观测器}\}.
\]

这是理解论文结论时必须把握的区别。

#### （3）利用原始状态空间中的零空间参数化

这是论文最重要的技术贡献之一。

定义

\[
V=\ker
\begin{bmatrix}
C\\CA
\end{bmatrix}
\]

的一个满列秩基矩阵。

对于给定的阶数 \(q\)，论文通过满列秩矩阵 \(Z\) 参数化与观测器对应的零空间结构。

固定阶数下，代数条件可以转化为：

\[
CZ=0,
\]

\[
LZ=0,
\]

以及相应的秩条件：

\[
\operatorname{rank}
\begin{bmatrix}
Z&AZR_Z
\end{bmatrix}
=d,
\]

其中

\[
\operatorname{im}R_Z=\ker(CAZ).
\]

与此同时，谱条件可以写成矩阵铅笔秩条件：

\[
\boxed{
\operatorname{rank}
\begin{bmatrix}
(\lambda I-A)V&Z
\end{bmatrix}
=
\operatorname{rank}
\begin{bmatrix}
V&Z
\end{bmatrix},
\quad\lambda\in\Omega_S.
}
\]

这一表达式非常有价值。

因为它将原来涉及未知增广矩阵 \(\mathcal L\) 的观测器设计问题，转化为原始状态空间中关于子空间 \(Z\) 的判定问题。

这有利于：

- 建立固定阶数的判定算法；
- 利用矩阵铅笔理论分析谱条件；
- 研究 Grassmann 流形上的可行子空间；
- 研究所有可行阶数的集合；
- 分析固定阶数问题的计算复杂性。

#### （4）完整可行阶数谱

论文进一步定义了不同阶数的可行增广族，并给出所有可行阶数的完整刻画。

其 Theorem 9 给出的基本形式是：

\[
\boxed{
\Sigma_{FO}(L)
=
\left\{
q_k:
\mathfrak Z_{d_k}^{AS}(L)\neq\varnothing
\right\}.
}
\]

这里 \(\mathfrak Z_{d_k}^{AS}(L)\) 表示相应阶数下同时满足代数条件和谱条件的参数集合。

因此，最终最小阶数可以表示为

\[
\boxed{
q_{\min}
=
\min\Sigma_{FO}(L).
}
\]

#### （5）两篇论文之间的关系

| 比较项目 | 2609.33615 | 2609.37992 |
|---|---|---|
| 核心问题 | 最小代数阶数及其谱可行性 | 所有阶数的可行性 |
| Functional Observability Indices | 是 | 沿用 |
| 最小代数阶数 \(q_0\) | 建立 | 沿用 |
| 最小代数增广族 | 完整刻画 | 作为基础 |
| 任意固定阶数 | 主要研究最小代数阶 | 完整刻画 |
| 代数可行阶数无间隙 | 非核心 | 明确证明 |
| 原始状态空间零空间参数化 | 基础构造 | 进一步系统化 |
| 完整可行阶数谱 | 最小阶数判定 | 系统刻画 |

**总体评价：**

2609.33615 解决了“最小代数可行阶数是多少，以及这一阶数下是否能满足谱条件”的问题。

2609.37992 则进一步研究“每一个指定阶数是否存在可行观测器，以及全部可行阶数构成什么集合”。

从最小阶功能观测器的结构理论来看，这两篇工作构成了近年最直接的一组研究成果。

但必须注意，它们建立的是结构性必要充分刻画，并不自动意味着已经得到多项式时间算法，也没有自动解决一般情形下的计算复杂性问题。

---

## 四、现阶段最重要的数学判据

综合以上研究，最小阶功能观测器问题可以归纳为以下几个层次的判据。

### 4.1 功能可观测性判据

首先判断目标功能是否能够从输入输出信息中恢复。

对于标准 LTI 系统：

\[
\dot x=Ax+Bu,\qquad y=Cx,\qquad z=Lx,
\]

功能可观测性的条件是：

\[
\boxed{
\operatorname{rank}
\begin{bmatrix}
\mathcal O_C\\
\mathcal O_L
\end{bmatrix}
=
\operatorname{rank}(\mathcal O_C).
}
\]

等价地：

\[
\operatorname{row}(\mathcal O_L)
\subseteq
\operatorname{row}(\mathcal O_C).
\]

如果这一条件不成立，那么无论增加多少观测器状态，都不能在通常的功能可观测定义下实现目标。

### 4.2 代数可实现性判据

引入增广功能矩阵：

\[
\mathcal L=
\begin{bmatrix}
L\\R
\end{bmatrix}.
\]

要求：

\[
\operatorname{rank}
\begin{bmatrix}
\mathcal LA\\
\mathcal L\\
CA\\
C
\end{bmatrix}
=
\operatorname{rank}
\begin{bmatrix}
\mathcal L\\
CA\\
C
\end{bmatrix}.
\]

这意味着增广功能空间在系统动态作用下具有适当的闭合关系。

通过 Functional Observability Indices 可以得到：

\[
\boxed{
q_0=\sum_{j=1}^{r}\eta_j.
}
\]

因此：

\[
q_{\min}\geq q_0.
\]

这个下界来自代数结构，而不是来自稳定性要求。

### 4.3 谱可行性判据

代数条件成立之后，还需要检查观测器误差动态是否可以满足指定的谱要求。

对于任意极点配置，要求：

\[
\operatorname{rank}
\begin{bmatrix}
\lambda\mathcal L-\mathcal LA\\
CA\\
C
\end{bmatrix}
=
\operatorname{rank}
\begin{bmatrix}
\mathcal L\\
CA\\
C
\end{bmatrix},
\qquad \forall\lambda\in\mathbb C.
\]

对于渐近稳定的连续时间观测器，要求：

\[
\operatorname{rank}
\begin{bmatrix}
\lambda\mathcal L-\mathcal LA\\
CA\\
C
\end{bmatrix}
=
\operatorname{rank}
\begin{bmatrix}
\mathcal L\\
CA\\
C
\end{bmatrix},
\qquad \forall\operatorname{Re}\lambda\geq0.
\]

这一条件的本质是排除不可配置的非稳定模态。

### 4.4 矩阵铅笔判据

通过零空间表示，可以进一步将谱条件转化为：

\[
\operatorname{rank}
\begin{bmatrix}
(\lambda I-A)V&Z
\end{bmatrix}
=
\operatorname{rank}
\begin{bmatrix}
V&Z
\end{bmatrix}.
\]

这实际上将功能观测器设计与矩阵铅笔的有限特征值、秩亏损以及多项式矩阵的左可逆性联系起来。

在你所研究的最小阶问题中，这一判据尤其重要，因为它提供了从观测器矩阵设计到子空间参数化的桥梁。

### 4.5 判据之间的逻辑关系

  
    **功能可观测性**

    目标功能是否能够被重构
  
  
    
  
  
    **代数可实现性**

    确定最小代数阶数 \(q_0\) 和可行增广族
  
  
    
  
  
    **谱可行性**

    检验矩阵铅笔在指定区域内的秩条件
  
  
    
  
  
    **最小阶功能观测器**

    \[
    q_{\min}=\min\Sigma_{FO}
    \]
  

需要强调：第一步是功能可观测性的前置条件，第二步确定代数下界，第三步决定该阶数是否真正满足动态要求。三者不能互相替代。

## 五、仍然没有解决的核心问题

这是整个研究领域最值得关注的部分。

现有文献已经给出了相当丰富的结构判据，但从理论刻画到真正可执行的最小阶数算法，仍然存在明显距离。

我认为至少有以下八个重要问题。

### 5.1 固定阶数可行性问题的计算复杂性尚未得到充分解决

给定

\[
(A,C,L,q),
\]

考虑决策问题：

\[
\operatorname{DEC}(q):
\]

是否存在一个阶数为 \(q\) 的功能观测器？

等价地，是否存在适当的增广矩阵

\[
\mathcal L=
\begin{bmatrix}
L\\R
\end{bmatrix}
\]

使得条件 (A) 和 (S) 同时成立？

现有文献提供了必要充分的代数和谱判据，但这并没有回答：

- DEC(q) 是否属于 P？
- DEC(q) 是否是 NP-hard？
- DEC(q) 是否属于 \(\exists\mathbb R\)？
- DEC(q) 是否具有 \(\exists\mathbb R\)-完全性？
- 是否存在针对 \(q\) 的固定参数算法？

尤其要区分以下两个命题：

\[
\text{存在有限的代数判据}
\]

与

\[
\text{存在多项式时间判定算法}.
\]

前者并不意味着后者。

这正是目前最值得进一步研究的理论方向之一。

### 5.2 最小阶数问题是否具有多项式时间算法？

假设已经能够解决固定阶数问题：

\[
\operatorname{DEC}(q).
\]

那么最小阶数可以通过：

\[
q_{\min}
=
\min\{q:\operatorname{DEC}(q)=\mathrm{YES}\}
\]

确定。

由于代数可行阶数存在区间：

\[
q_0\leq q\leq n_0-p,
\]

因此最多需要检查有限个阶数。

但是，这只说明搜索范围有限，并不能保证整体计算复杂度是多项式的。

关键原因是：

1. 每个固定阶数都可能对应大量候选子空间。
2. 候选子空间可能需要多个 Grassmann 图卡进行覆盖。
3. 每个候选子空间都必须满足谱条件。
4. 即使单个候选的谱条件可以有效检验，也不代表能够有效确定是否存在一个满足条件的候选。

因此，真正需要研究的是：

\[
\boxed{
\text{如何在不枚举全部候选增广矩阵的情况下，判定是否存在可行子空间？}
}
\]

这是从结构理论走向算法理论的关键一步。

### 5.3 谱可行阶数是否具有单调性？

这是一个特别重要的问题。

代数可行阶数具有无间隙性质：

\[
\Sigma_A=
\{q_0,\ldots,n_0-p\}.
\]

但谱可行阶数是否也具有类似性质？

例如，是否有：

\[
q\in\Sigma_{FO}
\Longrightarrow
q+1\in\Sigma_{FO}?
\]

如果成立，那么：

\[
\Sigma_{FO}
=
\{q_{\min},q_{\min}+1,\ldots,n_0-p\}.
\]

如此一来，最小阶数搜索就可以利用二分思想。

但如果不成立，则可能出现：

\[
\Sigma_{FO}=\{q_0,q_0+2,q_0+5\}.
\]

这时，传统的单调搜索算法就不适用。

这里需要特别谨慎：

代数条件的单调扩展不能自动推出谱条件的单调扩展。

即使某个阶数存在稳定观测器，也需要严格证明增加一个辅助功能方向之后，仍然可以构造满足相同谱要求的观测器。

这一问题值得单独研究。

### 5.4 最小阶增广族的几何结构是什么？

假设最小代数阶数已经确定：

\[
q_0=\sum_j\eta_j.
\]

那么全部满足代数条件的最小阶增广矩阵构成一个参数集合：

\[
\mathfrak L_{q_0}^{A}.
\]

真正的问题是：

\[
\mathfrak L_{q_0}^{FO}
=
\left\{
\mathcal L\in\mathfrak L_{q_0}^{A}:
\mathcal L\text{ 满足谱条件}
\right\}
\]

何时非空？

其几何结构如何？

是否为不可约代数簇？

是否具有多个连通分支？

是否可以得到维数公式？

是否存在可直接构造的参数化？

这些问题在理论上都很有价值。

尤其是，当代数可行族包含多个分支时，某些分支可能全部无法满足谱条件，而另一些分支却存在可行解。

因此，只研究某一个典型增广矩阵是不够的。

### 5.5 一般情形下的精确算法仍然不足

现有工作提供了秩判据和子空间参数化，但仍需要研究如何把它们转化为有效算法。

可能的方向包括：

- 基于 Grassmann 流形的优化算法；
- 基于实代数几何的可行性判定；
- 基于多项式矩阵的精确秩检验；
- 基于矩阵铅笔的特征值分析；
- 基于分层结构的参数空间搜索；
- 基于不变量和规范形的降维算法。

特别是，需要区分数值算法与精确算法。

数值算法可能通过随机初始化、局部优化等方法找到可行解，但这不能证明不存在其他可行解。

对于最小阶数问题，如果要证明某个阶数不可行，就需要具有完备性的判定方法。

### 5.6 数值稳定性与鲁棒最小阶设计

传统的谱条件主要讨论特征值是否位于指定区域。

但是实际系统中，矩阵存在测量误差和参数不确定性：

\[
A=A_0+\Delta A.
\]

即使某个观测器满足：

\[
\operatorname{Re}\lambda_i<0,
\]

如果特征值距离虚轴非常近，或者相应的矩阵铅笔高度病态，那么系统可能对微小扰动十分敏感。

因此，还需要研究：

\[
\min q
\]

同时满足：

\[
\text{稳定性约束},
\]

\[
\text{鲁棒性约束},
\]

\[
\text{数值条件数约束}.
\]

这实际上是一个比传统最小阶数问题更复杂的优化问题。

### 5.7 Descriptor、时滞、网络化和未知输入系统中的最小阶问题

2024—2026 年的研究已经开始将功能观测器推广到更多系统类别。

例如，2026 年的工作：

Hieu Trinh, Phan Thanh Nam, Tyrone Fernando,

*Existence and Design of Functional Observers for Time-Delay Systems with Delayed Output Measurements.*

arXiv:2603.09395, March 2026.

研究了状态时滞和输出测量时滞不一致时的功能观测器设计，并提出了不同结构的观测器及相应的代数存在性条件。

但这类工作主要拓展了功能观测器的系统模型和设计条件。

它们并没有自动解决相应系统中的全局最小阶数优化问题。

未来可以研究：

- Descriptor 系统的最小阶功能 ODE 观测器；
- 时滞系统的最小阶功能观测器；
- 未知输入条件下的最小阶功能观测器；
- 网络化系统中的分布式最小阶功能观测器；
- 非线性系统中的最小维数功能估计器。

### 5.8 最小阶数与观测器性能之间的关系

阶数最小并不意味着性能最优。

例如，两个观测器可能分别具有阶数：

\[
q_1<q_2,
\]

但是高阶观测器可能具有：

- 更快的收敛速度；
- 更大的稳定裕度；
- 更好的抗噪声性能；
- 更低的参数敏感性；
- 更简单的实现结构。

因此，未来可以将最小阶设计推广为多目标优化：

\[
\min_{\mathcal L,q}
\left(
q,\,
J_{\mathrm{stab}},\,
J_{\mathrm{robust}},\,
J_{\mathrm{noise}}
\right).
\]

这里的关键不是简单增加性能指标，而是研究不同性能约束对可行阶数集合的影响。

---

## 六、研究成果的横向比较

为了避免将相关但不同的问题混为一谈，下面总结近两年主要研究成果的实际贡献。

| 研究工作 | 核心理论贡献 | 是否直接解决最小阶问题 |
|---|---|---|
| Jaiswal et al. (2024) | Descriptor 功能 ODE 观测器存在性 | 部分相关 |
| Darouach & Fernando (2025) | 功能可观测性及极点配置设计 | 重要基础 |
| Zhang et al. (2025) | 结构功能可观测性、最少传感器配置 | 否 |
| Di Loreto & Eberard (2025) | Strong Functional Observer 存在性 | 扩展问题 |
| Jaiswal et al. (2025) | 部分可检测性及广义功能观测器 | 部分相关 |
| Fernando & Darouach (2025) | 功能可控性及广义分离原理 | 扩展问题 |
| Fernando (2026a) | 最小代数阶数及最小阶增广族 | **是** |
| Fernando (2026b) | 固定阶数及全部可行阶数谱 | **是** |
| Trinh et al. (2026) | 时滞系统功能观测器设计 | 扩展问题 |

这里最重要的结论是：

**2025 年的研究主要在扩展功能可观测性和功能观测器的结构理论；2026 年的两篇工作则更加直接地研究最小阶数及其逐阶可行性。**

不过，已有成果的主要优势在于数学结构刻画，而不是计算复杂性和高效算法。

---

## 七、参考文献与进一步阅读

下面列出建议优先阅读的文献，按照与最小阶问题的直接相关程度排序。

**第一组：最小阶数直接相关**

1. Fernando, T. (2026). *A Minimum-Order Functional Observer Beyond the Darouach and Luenberger Constructions*. arXiv:2609.33615. [论文链接](https://arxiv.org/abs/2609.33615)

2. Fernando, T. (2026). *Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger*. arXiv:2609.37992. [论文链接](https://arxiv.org/abs/2609.37992)

**第二组：功能可观测性和设计理论**

3. Darouach, M., & Fernando, T. (2025). On functional observability and functional observer design. *Automatica*, 173, 112115. DOI: 10.1016/j.automatica.2025.112115.

4. Zhang, Y., Fernando, T., & Darouach, M. (2025). Functional Observability, Structural Functional Observability and Optimal Sensor Placement. *IEEE Transactions on Automatic Control*, 70(3), 1592–1607. DOI: 10.1109/TAC.2024.3462558.

5. Fernando, T., & Darouach, M. (2025). Functional Controllability, Functional Stabilisability, and the Generalised Separation Principle. DOI: 10.1109/TAC.2025.3634469.

**第三组：扩展系统模型与存在性条件**

6. Jaiswal, J., Berger, T., & Tomar, N. K. (2024). Existence conditions for functional ODE observer design of descriptor systems revisited. *Journal of the Franklin Institute*, 361(8), 106848.

7. Di Loreto, M., & Eberard, D. (2025). On the existence of strong functional observer. arXiv:2502.03917.

8. Jaiswal, J., Berger, T., & Tomar, N. K. (2025). Partial detectability and generalized functional observer design for linear descriptor systems. *Franklin Open*, 10, 100238.

9. Trinh, H., Nam, P. T., & Fernando, T. (2026). Existence and Design of Functional Observers for Time-Delay Systems with Delayed Output Measurements. arXiv:2603.09395.

---

## 八、结合最小阶功能观测器计算复杂性研究，最值得推进的方向

如果把研究目标从传统的控制器设计进一步推进到数学理论与计算复杂性，我认为目前有一个非常明确的研究机会：

\[
\boxed{
\text{最小阶功能观测器的结构刻画已经取得进展，但其计算复杂性仍有待系统研究。}
}
\]

这里我建议将研究划分成四个层次。

### 8.1 第一层：固定阶数判定问题

首先严格定义：

\[
\operatorname{DEC}(q):
\]

输入为有理数矩阵

\[
A\in\mathbb Q^{n\times n},\quad
C\in\mathbb Q^{p\times n},\quad
L\in\mathbb Q^{r\times n}
\]

以及整数 \(q\)。

问题是：

是否存在一个阶数为 \(q\) 的功能观测器，使得：

1. 估计目标可以被正确重构；
2. 观测器满足相应的代数实现条件；
3. 观测误差动态满足稳定性要求。

这里首先要明确采用哪一种谱要求：

- 任意极点配置；
- 渐近稳定；
- 指定区域内稳定。

这三种问题不能直接视为同一个决策问题。

### 8.2 第二层：建立复杂性上界

可以尝试将固定阶数问题转化为实代数可行性问题。

例如，将未知矩阵 \(R\) 或零空间参数矩阵 \(Z\) 作为变量。

对秩条件：

\[
\operatorname{rank}(M)=k
\]

可以利用以下多项式约束表达：

- 所有 \(k+1\) 阶子式为零；
- 至少存在一个 \(k\) 阶子式非零。

非零约束可以通过辅助变量和多项式等式编码。

对于谱条件，则需要更加谨慎。

如果采用多项式矩阵左逆判据，可以尝试将谱可行性转化为有限维多项式约束。

例如，若

\[
P(\lambda)=\lambda U-G
\]

是一个具有 \(\omega\) 列的多项式矩阵，那么要求它在复数域上处处满列秩，可以通过最大阶子式的多项式最大公因式条件刻画：

\[
\gcd\{\text{所有 }\omega\times\omega
\text{ 子式}\}=1.
\]

在适当的矩阵维数和非退化条件下，还可以利用多项式左逆：

\[
X(\lambda)P(\lambda)=I_\omega.
\]

需要注意：不能直接将对所有复数 \(\lambda\) 的无穷多个秩约束，当作一个有限个数值点的检验问题。必须证明有限代数编码与原始谱条件等价。

如果能够完成这一转化，就有机会建立：

\[
\operatorname{DEC}(q)\in\exists\mathbb R.
\]

这将给出一个明确的计算复杂性上界。

### 8.3 第三层：寻找 NP-hard 或 \(\exists\mathbb R\)-hard 归约

这是最有理论价值、同时也最困难的一步。

建议优先考虑以下经典问题：

| 来源问题 | 可能的归约思路 |
|---|---|
| Existential Theory of the Reals | 将多项式方程编码进可行子空间参数 |
| Real Quadratic Feasibility | 利用 Grassmann 图卡上的二次秩约束 |
| Polynomial Matrix Completion | 将未知矩阵参数映射为多项式矩阵秩条件 |
| Subspace Intersection | 将交空间维数约束编码为增广空间条件 |

这里特别推荐研究：

\[
\text{Grassmannian feasibility}
\longrightarrow
\text{Functional Observer Feasibility}.
\]

原因在于，最小阶功能观测器本身就涉及子空间选择、交空间维数和矩阵铅笔秩条件。

不过，必须注意一个关键障碍：

不能只证明某个辅助代数问题可以编码到一个形式相似的秩条件中。必须保证构造出的 \(A,C,L\) 确实满足整个功能观测器问题的其他约束，并且归约在 YES/NO 两个方向都成立。

### 8.4 第四层：参数化复杂性与特殊情形算法

即使一般问题是 NP-hard 或 \(\exists\mathbb R\)-hard，也不代表所有系统都难以处理。

值得寻找以下特殊情形：

- \(q=q_0\)；
- \(q=q_0+1\)；
- \(r=1\)；
- \(\dim\ker[C;CA]\) 较小；
- \(A\) 可对角化；
- \(A\) 具有较简单的 Jordan 结构；
- 增广子空间只有有限个可能的结构类型。

例如，可以尝试建立：

\[
O^*(f(q)\operatorname{poly}(n))
\]

形式的固定参数算法。

也可以研究：

\[
O^*(f(t)\operatorname{poly}(n)),
\]

其中 \(t\) 是某个关键子空间的余维数或秩参数。

这里需要区分参数化算法与普通枚举算法：只有当多项式因子中的指数与参数无关时，才能称为 FPT 算法。

---

## 九、最终判断：目前最值得关注的五个开放问题

我将上述问题按照理论价值和研究可操作性进行排序。

| 优先级 | 开放问题 | 研究价值 |
|---|---|---|
| 1 | 固定阶数 DEC(q) 的计算复杂性 | 极高 |
| 2 | 谱可行阶数是否具有单调性 | 极高 |
| 3 | 最小阶增广族的几何结构 | 极高 |
| 4 | 最小阶数的精确算法及参数化算法 | 高 |
| 5 | 鲁棒性约束下的最小阶设计 | 高 |

其中，我认为第 1、2、3 项之间具有很强的内在联系。

例如：

- 几何结构决定候选增广族的复杂程度；
- 谱条件决定这些候选族中哪些部分真正可行；
- 计算复杂性决定能否有效找到或排除可行部分。

这三个问题可以构成一条完整的理论研究路线。

## 十、对当前研究方向的具体建议

结合你此前一直在研究的固定阶数 DEC(q)、最小阶数 MIN(k)、零空间参数化和矩阵铅笔判据，我建议不要再把主要精力放在重复证明已经建立的代数存在性判据上。

更值得做的是下面这条路线：

  建议的研究路线
  
    
      **固定阶数问题的严格形式化**

      建立 DEC(q) 的完整输入、输出和谱要求，明确有理输入、精确秩和稳定性条件。
    
    
      **代数化与有限维编码**

      将子空间参数、秩约束和多项式矩阵左可逆性统一转化为有限维代数系统。
    
    
      **计算复杂性上界**

      尝试证明 DEC(q) 属于 \(\exists\mathbb R\)，并明确编码规模和多项式次数。
    
    
      **复杂性下界**

      寻找从标准困难问题到 DEC(q) 的多项式时间归约，争取建立 NP-hard 或 \(\exists\mathbb R\)-hard。
    
    
      **最小阶数算法**

      在复杂性结果基础上研究 FPT、特殊矩阵结构和可高效判定的参数区间。
    
  

有三个问题尤其值得优先研究：

**问题 A：**

\[
\boxed{
\operatorname{DEC}(q)
\text{ 是否为 }\exists\mathbb R\text{-complete？}
}
\]

这是一个具有明确理论意义的问题。如果能够得到完整证明，就能为固定阶功能观测器设计建立一个严格的复杂性分类。

**问题 B：**

\[
\boxed{
q\in\Sigma_{FO}
\Longrightarrow q+1\in\Sigma_{FO}
\quad\text{是否成立？}
}
\]

如果不成立，能否构造一个最小维数的反例？如果成立，又需要什么附加条件？

这将直接影响最小阶数算法的设计。

**问题 C：**

\[
\boxed{
\text{最小阶增广族的谱可行子集具有怎样的代数几何结构？}
}
\]

这是连接观测器理论与实代数几何的一个重要切入点。

---

## 总结

截至 2026 年 11 月，可以作出以下判断：

1. **结构理论方面：** 2025 年的功能可观测性研究以及 2026 年的两篇最小阶预印本，已经使功能观测器从经典 Darouach 和 Luenberger 两种结构扩展到更加一般的中间阶数框架。

2. **数学判据方面：** Functional Observability Indices、代数秩条件、谱秩条件和矩阵铅笔刻画，构成了目前最重要的理论工具。

3. **最小阶数方面：** 已经可以将最小代数阶数写为
   \[
   q_0=\sum_j\eta_j,
   \]
   但真正的最小观测器阶数还需要在全部代数可行增广族中检验谱可行性。

4. **算法方面：** 有限维参数化和必要充分判据并不等价于高效算法。一般固定阶数判定的计算复杂性、谱可行阶数的单调性以及完整的精确算法，仍然是重要研究方向。

5. **最值得突破的方向：** 我认为是固定阶数功能观测器决策问题的计算复杂性，尤其是建立严格的 \(\exists\mathbb R\) 上界与困难性下界，并进一步研究最小阶数问题的参数化算法。

**最重要的研究定位是：不要把已经得到的最小阶结构刻画直接当作最小阶问题已经解决。结构上的必要充分条件回答的是“什么情况下存在”，计算复杂性研究回答的则是“能否有效判断存在”。这两者之间仍然有相当大的理论空间。**

从论文创新性的角度看，如果能够在已有逐阶结构理论的基础上，进一步完成 DEC(q) 的复杂性分类，或者证明谱可行阶数具有某种新的结构性质，将比单纯增加一组新的秩判据更有可能形成独立且有分量的理论贡献。

文献范围说明：上述综述覆盖 2024—2026 年 11 月可检索的代表性成果，不意味着穷尽所有相关期刊、会议和预印本。2026 年两篇直接研究最小阶数的工作仍应按预印本状态引用。复杂性方面的开放问题是基于现有结果作出的研究判断，而不是对所有文献均未解决的绝对断言。
