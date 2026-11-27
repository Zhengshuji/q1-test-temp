# PCC：参数化共同补空间问题（QA22 Q4）

> **对应 docs 条目**：B.13（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

> **定位**：把"给一**族**子空间找一个共同补空间"抽成**独立的判定问题**，以便先研究它的复杂度，
> 而不是一上来就攻 $\mathrm{DEC}(q)$。依据：[QA22 §3 Q4](../../archive/expert_correspondence/QA22_2026-10-31.md)。

## 1. 定义

设 $K$ 是域（$\mathbb C$ 或 $\mathbb R$），$V$ 是 $m$ 维。

**PCC-general（基线）**
> 输入：一条**有理曲线** $J:\mathbb P^1\to\operatorname{Gr}(r,V)$（用 Plücker 坐标的多项式给出）。
> 问：是否存在 $(m-r)$ 维子空间 $W$ 使 $W\cap J_\lambda=0$ 对**所有有限** $\lambda\in\mathbb C$？

**PCC-degree-1（主要目标）**
> 同上，但 $J$ 由**一次矩阵铅笔** $P(\lambda)=P_0+\lambda P_1$ 诱导：
> $J_\lambda=\operatorname{im}P(\lambda)\cap$（固定子空间）——即我们 $\mathrm{DEC}(q)$ 里出现的形状。

**PCC-DEC（最终应用）**
> $J_\lambda=I_\lambda=\operatorname{im}P(\lambda)\cap(H/S)$，其中 $P$ 来自 $A,C,L_0$ 的构造。

## 2. 已知

| 事实 | 出处 |
|---|---|
| **有限**族总有共同补空间（不可约 Grassmannian 上非空开集之交）| 常识；Clark–Shekhtman 的对比 |
| 有限族的**覆盖数** $=k(n-k)+1$ | [Clark–Shekhtman, PAMS 125 (1997)](../../literature/notes/LIT_REVIEW_2026-10-31_QA21_refs.md) |
| **单参数族是临界情形**：坏集并的维数 $\le(\nu-1)+1=\nu=\dim G$ | [A2 §23](../incidence_strata/README.md) |
| $\mathbb P^1$ 上**无**共同补空间（非常值曲线）| [定理 A1](../incidence_strata/README.md) |
| $\mathbb A^1$ 上可行 $\iff\det[W\mid B(\lambda)]$ **非零常数** | [定理 A2](../incidence_strata/README.md) |
| 常数秩下 $\mathcal F=\operatorname{Gr}\cap\mathbb P(K)\setminus\mathbb P(\ker a_0)$，**局部闭** | [定理 A3](../incidence_strata/README.md) |

## 3. $\exists\mathbb R$ 编码（PCC-degree-1）

未知量：$p_W\in\Lambda^{m-r}K$（$W$ 的 Plücker 坐标）、$z$。约束：
1. **Plücker 关系**（二次）；
2. **系数线性方程** $\langle a_j,p_W\rangle=0$（$j=1,\dots,d$）——$a_j$ 由铅笔算出（[coeff_space.py](../../tools/verification/coeff_space.py)）；
3. **非零条件** $\langle a_0,p_W\rangle\,z=1$（Rabinowitsch 技巧）；
4. 实版本：$p_W$ 的实/虚部分开写。

$$ \Longrightarrow\ \text{PCC-degree-1}\in\exists\mathbb R\ \text{（复版本：}\exists\mathbb C\text{ 需另论）} $$

**注意**：这是**上界**；下界（$\exists\mathbb R$-hard？）**未定**。

## 4. 三个明确的问题（都未解决）

**Q-A**：$\mathrm{PCC\text{-}DEC}\le_m\mathrm{PCC\text{-}degree\text{-}1}$ 是否成立？
（即：$I_\lambda$ 这种"铅笔的像与固定子空间之交"是否已经覆盖了所有一次铅笔诱导的族？）

**Q-B**：一次铅笔的**系数空间**
$$\mathcal C(P)=\operatorname{span}\{a_1,\dots,a_d\}\subseteq\Lambda^{m-r}V^*$$
受什么限制？（它是"由可分解族生成"的必然结果——这是本问题的核心代数问题，专家 QA22 §3 Q5 原话。）

**Q-C**：PCC-degree-1 是**多项式可判**还是 **$\exists\mathbb R$-hard**？
- 若能多项式判定 ⟹ $\mathrm{DEC}(q)$ 的固定 $S$ 部分多项式 ⟹ 向 $q1$ 的多项式算法大幅推进；
- 若 $\exists\mathbb R$-hard ⟹ 得到一个**独立的**硬度结果（哪怕还不能完全搬到 $\mathrm{DEC}(q)$）。

## 5. 与 matroid 硬度的关系（专家 QA22 §3 Q5）

matroid $\mathbb R$-可实现性（$\exists\mathbb R$-完全，秩 3）的可行集是
$$\operatorname{Gr}(r,n)\cap\mathbb P(L)\setminus\bigcup_{B\in\mathcal B}\{p_B=0\},$$
即"线性截面 + **多个**非零 Plücker 条件"；而 PCC 目前只有**一个**非零条件 $\langle a_0,p\rangle\ne0$。

$$\boxed{\ \text{差距}：\text{多个非零条件}\ \longleftrightarrow\ \text{单个非零条件}\ }$$

**中间定理（若要攻硬度，先证这个）**：每个带"指定非空开子集"的 Grassmannian 线性截面，
能否经**多项式规模嵌入**表示成"某单个铅笔诱导的常数行列式轨迹"？
- 若**是** ⟹ 直接桥接到 matroid；
- 若**否** ⟹ 反例/结构障碍同样有价值（界定 PCC 模型的表达力）。

## 6. 状态

| 项 | 状态 |
|---|---|
| 定义（三版本） | ✓ 本文 |
| $\exists\mathbb R$ 编码 | ✓ §3（纸面） |
| 有限族结论 | ✓ 引用 Clark–Shekhtman |
| 单参数族临界性 | ✓ [A2 §23](../incidence_strata/README.md) |
| **Q-A / Q-B / Q-C** | **全部开放** |
| 计算工具 | ✓ [coeff_space.py](../../tools/verification/coeff_space.py)（系数形式 + 判据）|
