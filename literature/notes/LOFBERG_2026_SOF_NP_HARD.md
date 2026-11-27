# Löfberg (2026), *Static output-feedback stabilization is NP-hard* — 阅读笔记

> arXiv:2609.16886v1（2026-09-15），单输入多输出（SIMO）静态输出反馈。
> 作者：Johan Löfberg（Linköping University）。
> 读取日期：2026-11-01/02。只记与 $q1$ 有关的内容。

---

## 1. 主要结果

**Thm 1.1**：$\mathsf{SOF}_1(A,B,C):\ \exists K\in\mathbb R^{1\times n},\ A+BKC$ Hurwitz —— **NP-hard**。
从 Betweenness 实例（$n$ 个元素、$m$ 个约束）多项式时间构造
$A\in\mathbb Z^{D\times D}$、$B\in\mathbb Z^{D\times1}$、$C\in\mathbb Z^{n\times D}$，$D=6(m+n)$，
元素 $O(\log L)$ 位；满足性 $\iff\exists K$ 使 $A+BKC$ Hurwitz。

副产品：**"仿射参数化的有理多项式族在有理盒上是否含 Hurwitz 成员"是 NP-hard**。

## 2. 技术核心（值得借鉴的三件）

**（1）通用源三次式**（一个三次式编码一个 betweenness 约束）：

$$q(s;u,v)=s^3+(N+u)s^2+N(N+v)s+\bigl(N^2(N+u+v)+1\bigr),\qquad N=2(n+1).$$

它的 Routh 行列式恰好化简为

$$\Delta=N(N+u)(N+v)-\bigl(N^2(N+u+v)+1\bigr)=Nuv-1 .$$

- 对三元组 $(a,b,c)$：取 $u=x_b-x_a$、$v=x_c-x_b$ ⟹ 稳定性强迫 $N(x_c-x_b)(x_b-x_a)>1$ ⟹ $x_b$ 严格在 $x_a,x_c$ 之间；
- 锚点 $(\mathsf L,i,\mathsf R)$：取 $u=x_i$、$v=N-x_i$ ⟹ 同一公式给出 $Nx_i(N-x_i)>1$ ⟹ $0<x_i<N$（**有界盒**）。

**（2）频率分离聚合**：把 $m+n$ 个"同时稳定"的三次式用**共轭复制 + 大虚部平移**压成**一个**仿射系数多项式，
只保留对 $x$ 常数/线性的项；用 Rouché 定理把各源三次式的局部根数搬到聚合式上。

**（3）去掉辅助盒**：锚点扰动 $h(s)=s(s-N)$ 在右半平面有固定零点 $s=N$；大增益时局部 Rouché 给出右半平面根，
从而排除"盒外伪解"。

最后把聚合式直接实现为 $\det\bigl(sI-(A+BKC)\bigr)$，$K=[x_1\ \cdots\ x_n]$。

## 3. 与我们 $q1$ 的关系

| 项 | 说明 |
|---|---|
| 目标类 | 这条给的是 **NP-hard**（不是 $\exists\mathbb R$-complete）；Liu 的后继给出 $\exists\mathbb R$-complete。**两条都要引**。|
| 编码对象 | 它编码的是**离散选择**（Betweenness 的全序），手法是"三次式的 Routh 行列式 = $Nuv-1$"——用**一个**多项式不等式表达一个三元序关系。|
| 与我们障碍 | 我们 $(5b)$ 不含"根在左半平面"这类**开**条件；它是"极大子式**无公根**"。所以 Löfberg 的"Routh 行列式"路线**不能直接搬**，但"**用一个低次多项式把约束编码进系数**"的思想可以借。|
| 潜在用处 | 若我们的 $(5b)$ 在某层可写成"某个多项式的某个系数非零"，则可用 Löfberg 的"单个三次式 $\Rightarrow$ 单个不等式"手法编码离散选择。**未验证**。|
