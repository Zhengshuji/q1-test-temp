# 文献阅读笔记（2026-10-31 晚，**已读原文 3 篇**）

> 每条：出处 / 读到什么 / 对本项目的影响 / 局限。**已读原文**的标注 ✓。

## 1. Noferini–Van Dooren ✓（PDF 已读，Lemma 5.2 原文核对）

**出处**：LAA 658 (2023) 86–115，`literature/pdf/pencils/On_computing_root_polynomials_and_minimal_bases.pdf`。

**Lemma 5.2（原文）**：
> Let $L(\lambda)\in\mathbb C[\lambda]^{m\times n}$ be a matrix pencil. Then $L(\lambda)$ is right invertible over $\mathbb C[\lambda]$ **if and only if it has no finite eigenvalues and no left minimal indices**. Moreover, in that case, there exists a right inverse having **degree $\le m-1$**.

**对本项目的影响（重要）**：把它应用到 $L=P^{\mathsf T}$（$t$ 行、$q$ 列，$m=t$）：
- **"no finite eigenvalues"** $=$ $P^{\mathsf T}(\lambda)$ 在**每个有限 $\lambda$** 的秩都等于常态秩 $t$ $=$ **$P(\lambda)$ 在 $\mathbb C$ 上处处满列秩** ✓ 正是我们的假设；
- **"no left minimal indices"** $=$ $P^{\mathsf T}$ 的左零空间平凡 $=$ $\operatorname{rank}P=t$ over $\mathbb C(\lambda)$ ✓（满列秩自动成立）；
- 结论：存在右逆 $R$ 使 $P^{\mathsf T}R=I_t$，$\deg R\le t-1$；**转置**得 $X=R^{\mathsf T}$，$XP=I_t$，$\deg X\le t-1$ ✓

$$\boxed{\ \text{引理 2 的路线 A 的假设与结论**逐条对上**——不再是"未经核对的引用"}\ }$$

**局限**：原文未给"no finite eigenvalues"在矩形铅笔下的精确定义；我按"秩在有限 $\lambda$ 上不下降"理解（与我们的"处处满列秩"一致）。

## 2. Clark–Shekhtman II ✓（PDF 已读）

**出处**：Proc. AMS **125** (1997) 251–254，`literature/pdf/algebra/Covering_by_complements_of_subspaces_II.pdf`。

**主定理**：$\gamma(k,n,K)=k(n-k)+1$（$K$ 代数闭），其中 $\gamma$ 是使 $k$ 维子空间族 $E_1,\dots,E_t$ 的**补空间覆盖**全部 $(n-k)$-子空间的最小 $t$。

**关键结构（与我们的完全同构）**：
- $G(k,n)\hookrightarrow\mathbb P(\wedge^k V)$，$E_i=\langle\epsilon_i\rangle$；
- $\phi_i:\wedge^{n-k}V\to\wedge^n V$，$\phi_i(\xi)=\epsilon_i\wedge\xi$，$K(E)=\bigcap_i\ker\phi_i$；
- **Lemma 1**：覆盖 $\iff$ $D(n-k,n)\cap K(E)=\varnothing$（$D$ = 可分解 $(n-k)$-向量）；
- **Lemma 2**：$\dim K(E)=\binom{n}{k}-t$；
- **Lemma 3（下界）**：若 $t\le k(n-k)$，则 $\dim K\ge\binom nk-k(n-k)$，射影维数计数给出 $K'\cap G\ne\varnothing$ ⟹ 矛盾；
- **Lemma 4（上界）**：$\nu=k(n-k)$，$B(F)=\{E:E\cap F\ne0\}$ 的 $\dim=\nu-1$，用 $B(F)^{\nu+1}$ 的并 + $\mathrm{PGL}_n$ 轨道维数计数证明覆盖存在。

**对本项目的影响（重要，两条）**：

1. **"补空间"问题有标准外代数表述**：我们的"$U\cap I_\lambda=0$"就是"$\epsilon_U\wedge\epsilon_{I_\lambda}\ne0$"，
   我们找的可行 $U$ $=$ 落在 $\bigcap_\lambda\ker\phi_\lambda$ 的**补集**里的可分解向量。
   Clark–Shekhtman 处理的是"**有限**族的覆盖"，我们要的是"**单参数族**下的避让"。
2. **有限 vs 单参数的分界被量化了**：
   - 有限族：坏集 $=\bigcup_{i\le t}B(F_i)$，维数 $\le\nu-1$（每个 $B(F)$ 是除子）⟹ **不可能覆盖** $G$；
   - **单参数族**：$B(I_\lambda)$ 随 $\lambda$ 变化，并的维数 $\le(\nu-1)+1=\nu=$ **恰好等于** $\dim G$
     ⟹ **正好落在临界**，覆盖**可能**发生。

$$\boxed{\ \text{除子情形的困难是**结构的**：单参数族恰好把并的维数顶到临界值}\ }$$

**局限**：他们只解有限族；单参数族**未涉及**。但他们的"线性空间 $\cap$ 可分解锥"判据（Lemma 1）与
维数计数（Lemma 3）是我们**可以直接引用**的两件工具。

## 3. Abdelkerim–Coskun ✓（PDF 已读引言 + Example 1.1）

**出处**：JPAA **216** (2012) 800–810，`literature/pdf/Parameter spaces of ... .pdf`。

**读到什么**：
- 超平面 $H\subset\mathbb P(\wedge^2V)$ 对应**反对称矩阵** $Q_H$（$H:\sum a_{ij}e_i\wedge e_j=0$）；
- **$\dim\ker Q_H$ 是决定 $\mathrm{PGL}(n)$ 在 $\mathbb P^*(\wedge^2V)$ 上轨道的**不变量**；
- 轨道 $=S_r\setminus S_{r-1}$，$S_r$ = 使 $G(2,n)\cap H$ 的奇点轨迹含 $\Sigma_{2r,2r}$ 的超平面；
- **$\operatorname{Gr}(2,4)$ 的特例**：$G(2,4)\subset\mathbb P^5$ 是光滑二次超曲面；**超平面截面要么光滑、要么恰好是一个余维 1 的 Schubert 簇 $\Sigma_1(V_2\subset V_4)$**。

**对本项目的影响**：
- 我们的 G3（$(r,m)=(2,4)$）本质是"**多个超平面条件的交**"，而这里是**单个**超平面的完整分类；
- 他们的"$\dim\ker Q_H$"不变量提示：**线性条件的"类型"可完全由线性代数数据刻画**——
  这与我们 §19 的"$\operatorname{rank}(Q|_L)$ 判定"同源；
- 他们的 Example 1.1 确认了 $(2,4)$ 上"非光滑 ⟹ 恰是一个 Schubert 簇"——与我们"退化 ⟹ $\operatorname{span}(X)$ 是超平面"的结论**一致方向**。

**局限**：只处理 $k=2$ 且**单个**超平面；我们的 $L$ 是高余维交，**不能直接套用**。

---

## 总结

| 文献 | 已读 | 对项目的直接影响 |
|---|---|---|
| Noferini–Van Dooren | ✓ 原文 | **引理 2 路线 A 的假设核对完毕**（与我们的假设逐条对应）|
| Clark–Shekhtman II | ✓ 原文 | **外代数表述** + **有限/单参数的分界被量化**（坏集维数 $\nu-1$ vs $\nu$）|
| Abdelkerim–Coskun | ✓ 引言 | $\mathbb P^*(\wedge^2V)$ 的轨道由 $\dim\ker Q_H$ 决定；$(2,4)$ 单超平面截面完全分类 |
| Kim–de Mesmay–Miltzow | 摘要 + §1–2 | matroid 硬度模板（秩 3 即 ∃ℝ-完全）|
| Aprodu–Spiridon | 摘要 | "transversal linear section" 术语与框架 |
