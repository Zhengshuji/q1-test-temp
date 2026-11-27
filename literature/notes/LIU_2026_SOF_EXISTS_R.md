# Liu (2026), *Computational complexity of static output feedback stabilization* — 阅读笔记

> arXiv:2610.00390v2（2026-09-30 提交，10-03 修订），21 页，math.OC（93D15, 68Q17, 68Q25）。
> 作者：Zhaobo Liu（深圳大学高等研究院）。
> 读取日期：2026-11-01/02。**本笔记只记与我们 $q1$ 有关的内容**；原文以论文为准。

---

## 1. 主要结果

| 定理 | 内容 |
|---|---|
| **Thm 1** | $\mathsf{SOF}$（有理数据）是 **$\exists\mathbb R$-complete**（确定性多项式多一归约）。**即使限制到双输入、最小（可控可观测）整数系统**仍 $\exists\mathbb R$-complete。 |
| **Thm 2** | 存在绝对常数 $c\ge1$ 与确定性精确算法，在 $(\mathcal L+1)^c(n+1)^{c(\kappa+1)}$ 位操作内判定并给出有理锁定增益。 |
| **Thm 3** | 单输入最小整数系统上**强 NP-hard**（3-SAT 归约）；且可行实例有 $\{-1,1\}$ 增益，对全体元素同时扰动 $\|D\|_{\max}\le\delta_0$（$\delta_0$ 与系统维数无关）仍锁定。 |

## 2. 两个概念（对我们要紧）

**有效增益维数** $\kappa:=mp-\dim\mathcal N_{\rm pole}$，其中

$$\mathcal N_{\rm pole}=\{D\in\mathbb R^{m\times p}:\ p_{K+tD}=p_K\ \text{对一切}\ K,t\}$$

（$p_K(s)=\det(sI-A-BKC)$；$\mathcal N_{\rm pole}$ 是线性子空间）。
$\kappa$ 是"决定特征多项式所需增益线性组合的最少个数"。

**意义**：$\kappa$ 固定 ⟹ 多项式时间精确判定 + 有理综合（即使增益入口很多、冗余很多）。
这与我们的"选子空间带来的自由度"是**同类问题**：把**不改目标对象的自由度**除掉。

## 3. 归约的技术核心（§4.1，最值得我们借鉴的一段）

目标：把方程 $\ell_j(v)^2=h_j(v)$（$\ell_j,h_j$ 为整系数仿射式）编进一个**特征多项式**。

取 $a(s)=\sum_j\ell_j(x)s^{e_j}$、$b(s)=\sum_j h_j(x)s^{2e_j}+\sum_{j<k}c_{jk}s^{e_j+e_k}$，则

$$\det\begin{pmatrix}s^q+a & b\\ -1 & s^q-a\end{pmatrix}=s^{2q}+b-a^2 .$$

取 $c_{jk}=2\ell_j(x)\ell_k(x)$ 消去交叉项，得

$$s^{2q}+\sum_{j=1}^{J}\bigl(h_j(x)-\ell_j(x)^2\bigr)s^{2e_j}.$$

**要点**：$e_j$ 选成使 $2e_j$ 互不相同 ⟹ **残差就是系数**；"方程成立" $\iff$ 这些系数全为零。
再用平方增广 $v_i^2=r_i$、$(v_i+1)^2=r_i+2v_i+1$ 使乘法可编码。

另有两件配套技术：
1. **分离界**：给不可行方程组一个统一的定量缺陷，防止"增益无界大"造成的伪解；
2. **锚点值**：把增益逼进有界盒。

## 4. 与我们 $q1$ 的关系（我的判断）

| 项 | 说明 |
|---|---|
| 目标类 | **确认了专家的判断**：正确目标是 $\exists\mathbb R$-completeness，不是 NP-hardness 本身（论文明确引 ${\rm NP}\subseteq\exists\mathbb R$）。|
| 归约障碍 | 我们的 $(5b)$ 是"极大子式**无公根**"（非零条件），SOF 是"特征多项式 Hurwitz"（根位置）。两者不能直接互换。|
| **可借鉴的形状** | **方阵情形**（$q=t$）下 $(5b)\iff\det[U\mid P(\lambda)]\in\mathbb C^\times$，即"**全部非首项系数为零 + 常数项非零**"。这正是 Liu 的"残差进系数"形状：**等式组 + 一个非零条件**。|
| 一个待验的想法 | 用 Liu 的 $2\times2$ 块把源方程的残差放进 $\det[U\mid P]$ 的**非首项系数**，再用"每层只保留 $\rho$ 阶子式"的结构把 $\kappa$-型冗余消掉。**未验证**，见 `workspace/q1_true/attempts/` 的下一条。|

## 5. 其他

- 论文并列引用了 **Löfberg (2026)**（Betweenness 归约，NP-hard）、**Barkai–Shames (2026)**（Subset Sum）、**Ahmadi et al. (2026)**（3-SAT，强弱两种，含离散时间）——**这四条要一起入库**（见 `literature/SEARCH_LOG.md` 待办）。
- 论文的"有效增益维数"与我们 B 组"秩屏障/层"语言可能可以对照：$\kappa$ 是"不改 $p_K$ 的增益方向"，我们的层是"不改秩的 $\mathcal V$ 方向"。**是否同构，未考证。**
