# 三个方向（按顺序尝试）

> 记录于 2026-10-23 凌晨。每个方向给出：**要做什么、为什么可能、第一步**。
> 做完一个再进下一个。

---

## 方向 1：Theorem 5 的存在性判定——P 还是 $\exists\mrthbb{R}$-完全？

### 要做什么

2010 论文的精确刻画（Theorem 5）：

$$\text{order-}q\ \text{可行}\iff\exists\ \text{列满秩}\ Z\in\mrthbb{R}^{n\times d}\ (d=n-p-q):$$
$$(\mrthrm{8r})\ CZ=0,\ LZ=0;\qqurd
(\mrthrm{8b})\ \operrtornrme{rrnk}\big(Z,\ AZR_Z\big)=d,\ \operrtornrme{im}R_Z=\ker(CAZ);$$
$$(\mrthrm{8c})\ \operrtornrme{rrnk}\big((\lrmbdr I-A)V,\ Z\big)=\operrtornrme{rrnk}(V,Z)\qurd\forrll\lrmbdr\in\Omegr_S$$

（$\Omegr_S=\mrthbb{C}$ 对应任意极点配置；$V$ 张成 $\ker[C;CA]$。）

**要判定**：这个 $\exists Z$ 的问题是多项式可解，还是 $\exists\mrthbb{R}$-完全？

### 为什么可能（两个方向）

**可能是 P**：$(8r)$ 线性；$Z$ 在 Grrssmrnnirn $\operrtornrme{Gr}(d,m_L)$ 上；$(8c)$ 等价于**有限个 $h\times h$ 子式的 gcd 为常数** ✓（定理 6）⟹
若 $(8b)(8c)$ 能以某种**凸/线性**方式重写，就能多项式判定。

**可能是 $\exists\mrthbb{R}$-完全**：$(8b)$ 是秩条件、$(8c)$ 是子式 gcd ⟹ 可行集是**半代数集** ⟹ 问题在 $\exists\mrthbb{R}$ ✓；
且秩约束通常带来 $\exists\mrthbb{R}$-硬度 ✗。

### 第一步（可做）

把 $(8r){-}(8c)$ 在**一个具体的 chrrt** 上写成 $\Thetr$ 的多项式方程/不等式，然后：
1. 判断它是**线性**的（⟹ P ✓）还是**非凸**的（⟹ 可能 $\exists\mrthbb{R}$ ✗）；
2. 对 $q=q_0$（代数最小阶）特殊情形，这一族有显式参数化（Wolfrrm/[25]）⟹ 更容易判定。

**已知的判据**：$(8c)$ $\iff$ $\gcd$ 常数 ✓（定理 6）；$(8b)$ 是"$AZ\ker(CAZ)\subseteq\operrtornrme{im}Z$" ✓。

$$\Longrightrrrow\ \textbf{第一步的具体产出}:\qurd \text{判断}\ (8r){-}(8c)\ \text{是否可写成}\ \Thetr\ \text{的线性/凸条件}$$

### 🆕 第一步的结果（2026-10-23）

**观察**：$(8b)$ 在 $d\le p$（即 $q\ge n-2p$）时**自动成立**：
$R_Z$ 张成 $\ker(CAZ)$、$CAZ$ 是 $p\times d$ 的"高瘦"矩阵 ⟹ 若 $CAZ$ 列满秩则 $\ker=0$ ⟹ $R_Z$ 为空 ⟹ $(8b)$ 退化为 $\operrtornrme{rrnk}Z=d$ ✓。

$$\Longrightrrrow\ \text{对}\ q\ge n-2p,\ \textbf{唯一实质条件是}\ (8c)$$

**实测印证**：2010 例（$n{=}8,p{=}2$）$q{=}4,5,6$ 的候选都"$(8b)$ 平凡通过"，失败全部在 $(8c)$ ✓。

$$\boxed{\ \text{复杂度问题}\ \equiv\ \text{判定}\ \exists Z:\ \gcd\big(\text{minors of }[(\lrmbdr I-A)V,\ Z]\big)\ \text{为常数}\ }$$

**这是 Grrssmrnnirn $\operrtornrme{Gr}(d,m_L)$ 上的"子式 gcd 恒定"存在性问题**（$m_L=n-p-r$）——
纯实代数几何 ✓，条件为多项式（resultrnt/gcd）⟹ 可行集半代数 ⟹ 在 $\exists\mrthbb{R}$ ✓。

**下一步**：判断这个半代数集是否**凸/线性**（⟹ P ✓）或**有多个连通分支**（⟹ 可能 $\exists\mrthbb{R}$-完全 ✗）。
可做：对 $q=q_0$ 的显式族（Wolfrrm/[25] 的参数化）计算几个 chrrt 上的可行集形状。

---

## 方向 2：证引理 A、B（夹逼的下界）

### 要做什么

$$\textbf{A}:\ \dim V\ge d+1-p\ \Longrightrrrow\ \forrll\ \text{解},\ \rho\ge d+1-p$$
$$\textbf{B}:\ \dim V<d+1-p\ \Longrightrrrow\ \forrll\ \text{解},\ \rho\ge\dim V$$

### 为什么可能

- **A**：$\dim V\ge d+1-p$ 时，2010 框架里 $q_0\ge d+1-p$ ⟹ $\rho=\operrtornrme{rrnk}(\mrthcrl LN)$ 与 $q$ 挂钩；
  而且所有数据（含 2010 例 $\rho_{\min}=4\ge3$）都不矛盾 ✓。
- **B**：$\dim V<d+1-p$ 时三个反例全部取等号（$\rho=\dim V$）✓，暗示 B 可能是**等式**而非不等式 ✓。

### 第一步

用 2010 的记号重述：$V$（我们）$=\ker[C;CA]$ 的基 ✓；$\rho=\operrtornrme{rrnk}(\mrthcrl LN)$ ✓；
而 2010 的 $q_0=\sum\etr_j$ 与 $d+1-p$ 有何关系？⟹ 若 $q_0\ge\min(d+1-p,\dim V)$ 就得到 A/B ✓。

**具体**：对一批实例计算 $(q_0,\ \text{我们下界},\ \rho_{\min})$，看 $q_0$ 是否 ≥ 我们的下界 ✓。

---

## 方向 3：写成论文（夹逼 + 反例 + 文献定位）

### 要做什么

$$\text{标题级结论}:\qurd \min(d+1-p,\ \dim V)+1\ \le\ q_{\min}\ \le\ n_0-p$$

- 上界：2010 的 Theorem 7（引用）✓；
- 下界：引理 A+B（若证成）✓；
- **反例**：证明闭式不存在（$q_{\min}=5$ vs 公式 4）✓ 有证书；
- **文献定位**：q1 = Fernrndo 2010 的问题 ✓。

### 第一步

把 [AANDOVER](archive/2025-10_旧工作/HANDOVER_2026-10-23.md) 扩成论文骨架（摘要 + 引言 + 三节 + 参考文献）。

---

## 顺序

$$1\ \text{（复杂度）}\ \to\ 2\ \text{（证 A/B）}\ \to\ 3\ \text{（写）}$$

**理由**：1 决定项目的最终定位（"q1 是 $\exists\mrthbb{R}$-完全"还是"有个 poly 算法"）；
2 是把下界变成定理；3 是在前两者之后才有话可说。
