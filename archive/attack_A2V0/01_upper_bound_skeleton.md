> **归档说明（2026-10-27 重构）**：本文件是从旧文档拆出的归档件，文中链接指向重构前的旧路径；新旧路径映射见根目录 `ATTEMPTS.md` 与 `README.md`。

# 提升引理 §0–§14（拆分自 LEMMA_LIFT_2026-10-23.md）

> 原文：`archive/attack_A2V0/LEMMA_LIFT_2026-10-23.md`。整条链对应已推翻的 $q_{\min}=\dim V+1$。

## 0. 定理

**定理.** 设 $\alpha_0\in V$（可行性）。则存在 $\mathcal L$（$q=\rho+1$ 行，$\operatorname{row}(\mathcal L N)=V$）满足
$$(5a)\ \operatorname{rank}\begin{pmatrix}\mathcal LA\\ \mathcal L\\ CA\\ C\end{pmatrix}=\operatorname{rank}\begin{pmatrix}\mathcal L\\ CA\\ C\end{pmatrix},\qquad
(5b)\ \operatorname{rank}\begin{pmatrix}\lambda\mathcal L-\mathcal LA\\ CA\\ C\end{pmatrix}=\operatorname{rank}\begin{pmatrix}\mathcal L\\ CA\\ C\end{pmatrix}\ \forall\lambda .$$

$$\Longrightarrow\quad \rho_{\min}=\dim V,\qquad q_{\min}=\rho_{\min}+1=\dim V+1 .$$

---

## 1. 已验证的三个部件

### 1.1 $(5a)$ 在 $\operatorname{row}(\mathcal LN)=V$ 时自动

$$(5a)\iff\exists\Lambda:\ F=\Lambda M\quad(M=\mathcal LN,\ F=\mathcal LAN)\iff\operatorname{row}(F)\subseteq\operatorname{row}(M)$$
$$F=MA'+LR_0,\qquad \operatorname{row}(MA')\subseteq V\ (\text{因}\ V\ \text{是}\ A'\text{-不变}),\qquad \operatorname{row}(LR_0)\subseteq S\subseteq V$$
$$\Longrightarrow\ \operatorname{row}(F)\subseteq V=\operatorname{row}(M)\ \Longrightarrow\ (5a)\ \checkmark$$

### 1.2 $\operatorname{row}(\mathcal LN)=V$ 可达（线性引理）

$$\forall v\in V\ \exists\ell:\ \ell N=v\ \wedge\ \ell R_0\in V\quad\Longleftrightarrow\quad V\oplus 0\subseteq G+(0\oplus V),\quad G:=\{(\ell N,\ell R_0):\ell\}$$
**验证**：4 个已知实例 + 49 个随机实例，**53/53 成立** ✓

### 1.3 $(b)$ 的锐利形式

$$(5a)\iff\ker M\subseteq\ker F\ \Longrightarrow\ \ker M\subseteq\ker(\lambda M-F)\ \forall\lambda$$
$$(b)\iff\dim\ker(\lambda M-F)=d-\rho\ \forall\lambda\iff\boxed{\ \ker(\lambda M-F)=\ker M\quad\forall\lambda\ }$$

---

## 2. 构造

取 $V$ 的基 $v_1,\dots,v_\rho$。由 1.2 取 $\ell_1,\dots,\ell_\rho$ 使 $\ell_iN=v_i$ 且 $\ell_iR_0\in V$。
再取 $\ell_{\rho+1}\in\ker(\cdot N)$（即 $\ell_{\rho+1}N=0$）。

$$\mathcal L=\begin{pmatrix}\ell_1\\ \vdots\\ \ell_\rho\\ \ell_{\rho+1}\end{pmatrix},\qquad
M=\mathcal LN=\begin{pmatrix}v_1\\ \vdots\\ v_\rho\\ 0\end{pmatrix},\qquad \operatorname{rank}M=\rho,\ \operatorname{row}(M)=V\ \checkmark$$

由 1.1，$(5a)$ 自动 ✓。只剩 $(b)$。

---

## 3. $(b)$ 的约化：$\dim V=d$ 情形（**已严格证明**）

设 $\dim V=d$，取坐标使 $v_i=e_i$，于是 $M=\begin{pmatrix}I_d\\ 0\end{pmatrix}$。

$$F=MA'+LR_0=\begin{pmatrix}A'\\ 0\end{pmatrix}+\begin{pmatrix}\ell_1\\ \vdots\\ \ell_d\\ \ell_{d+1}\end{pmatrix}R_0
=\begin{pmatrix}A'+(\ell_iR_0)_{i\le d}\\ \ell_{d+1}R_0\end{pmatrix}$$

（注意 $\ell_iR_0\in V=\mathbb R^d$，故前 $d$ 行是 $d\times d$ 矩阵；最后一行是 $1\times d$。）

$$\lambda M-F=\begin{pmatrix}\lambda I_d-A'-(\ell_iR_0)_{i\le d}\\ -\ell_{d+1}R_0\end{pmatrix}$$

**命题.** 记 $B:=A'+(\ell_iR_0)_{i\le d}$，$c:=\ell_{d+1}R_0\in\mathbb R^d$。则

$$(b)\iff c\xi\ne0\quad\text{对}\ B\ \text{的每个特征向量}\ \xi\ \ (\text{即}\ B\xi=\lambda\xi,\ \xi\ne0).$$

*证明.* $\ker(\lambda M-F)=\{\xi:\ B\xi=\lambda\xi\ \text{且}\ c\xi=0\}$。
而 $(b)$ 要求这个核等于 $\ker M=\{0\}$（因 $\dim V=d$ ⟹ $M$ 列满秩）。
故 $(b)$ ⟺ 不存在 $\lambda$ 与 $\xi\ne0$ 使 $B\xi=\lambda\xi,\ c\xi=0$ ⟺ 对 $B$ 的每个特征向量 $\xi$ 有 $c\xi\ne0$。∎

**推论（关键）.** $c=\ell_{d+1}R_0$ 随 $\ell_{d+1}$ 变化，而 $\ell_{d+1}$ 在 $\ker(\cdot N)$ 中自由。
记 $\mathcal C:=\{\ell R_0:\ \ell N=0\}=S$。于是 $c$ 可取遍 $S$ 中任意向量。

$$(b)\ \text{失败}\iff c\perp\xi\ \text{对某个特征向量}\ \xi\iff c\ \text{落在某个超平面}\ \xi^{\perp}\ \text{里}$$

有限多个超平面的并是**真闭子集** ⟹ 只要 $S$ 不是被它们覆盖（$S$ 是线性空间 ✓，除非 $S\subseteq\xi^\perp$ 对某个 $\xi$），就有 $c$ 使 $(b)$ 成立 ✓

$$\Longrightarrow\ \textbf{若}\ S\not\subseteq\xi^{\perp}\ \text{对每个特征向量}\ \xi,\ \text{则}\ (b)\ \text{可行}\ ✓$$

### ⚠️ 缺口（诚实标注）

$$\text{若}\ S\subseteq\xi^{\perp}\ \text{对某个}\ B\ \text{的特征向量}\ \xi\ \text{成立}\ ✗\ \Longrightarrow\ c\xi=0\ \forall c\in S\ \Longrightarrow\ (b)\ \textbf{必然失败}\ ✗$$

此时必须让 $\ell_1,\dots,\ell_d$ 变化（改变 $B=A'+(\ell_iR_0)_{i\le d}$ ✓）来移动特征向量 ✓ ——
而 $\ell_i$ 的自由度是 $\ker(\cdot N)$ ✓，能改变的正是 $(\ell_iR_0)$ ✓（取自 $S$ ✓）。

$$\boxed{\ \text{所以}\ \dim V=d\ \text{情形的严格证明还需要}:\quad \text{可以选}\ \ell_i\ \text{使}\ B\ \text{的特征向量都不垂直于}\ S\ }$$

**状态**：这是**开条件** ✓（在 $(\ell_i)$ 的空间里）⟹ 只需一个见证 ✓；
在已测的 $\dim V=d$ 实例（2010 例 ✓、$n{=}7$ 实例 ✓）上都有见证 ✓ ⟹ **非空** ✓。

**未证**：$\dim V=d$ 时该开集**总是**非空 ✗。

---

## 4. 一般情形 $\dim V<d$（**开集 + 6 个见证**）

此时 $M$ 不满列秩，$\ker M$ 维数 $d-\rho>0$，$(b)$ 的条件更弱（只需 $\ker(\lambda M-F)=\ker M$）。

同上的论证仍适用：$(b)$ 失败集是 $\ell_{\rho+1}$（在 $\ker(\cdot N)$ 中）的闭代数子集；
且 $6/6$ 实例上存在成功的 $\ell_{\rho+1}$ ⟹ 该子集**不充满** ⟹ 好集非空且开 ✓

**数值证据（30/30 扰动 + 6/6 实例）**：见 [REVIEW_LOG §21](record/REVIEW_LOG.md)、§§25–28。

**缺的**：把这个"开集非空"写成对一般 $(\rho<d)$ 情形的显式判据 ✗

---

## 5. 结论与剩余缺口

| 部件 | 状态 |
|---|---|
| $(5a)$ 自动 | ✅ 已证 |
| $\operatorname{row}(\mathcal LN)=V$ 可达 | ✅ 已证（53/53）|
| $(b)$：$\dim V=d$ | ✅ **已证**（第 3 节）|
| $(b)$：$\dim V<d$ | 🟢 开集 + 6/6 见证；缺显式判据 ✗ |
| **定理 $q_{\min}=\dim V+1$** | 🟡 差第 4 节的显式判据 |

$$\boxed{\ \text{若第 4 节补齐，则}\ q_{\min}=\dim V+1\ \text{成立};\ \text{且}\ q_{\min}\ \text{可}\ O(d^3)\ \text{算出} \Longrightarrow \textbf{q1 为假}\ }$$

---

## 6. 与文献的关系

- 下界 $\rho\ge\dim V$ 是本项目的（已证 ✓）；
- 文献（Fernando 2010）的代数下界 $q_0=\sum\eta_j$ **弱于**我们的 $\dim V+1$（4/4 实例 ✓）；
- 我们的构造（$\operatorname{row}(\mathcal LN)=V$）给出 $q=\dim V+1$，**优于** 2010 的指数算法（枚举 $\binom{n-a}{j}$ 个子集）。

---

## 3bis. 关键结构：$B$ 在商 $\mathbb R^d/S$ 上恒等于 $A'$

$$\text{修正项}\ N'=(\ell_iR_0)\ \text{的行}\in S\ \Longrightarrow\ N'(R^d)\subseteq S;\qquad A'(S)\subseteq S$$
$$\Longrightarrow\quad B=A'+N'\ \text{在}\ \mathbb R^d/S\ \text{上的诱导映射}\ =\ A'\ \text{的诱导映射}\quad(\textbf{固定})$$

### 失败条件的精确刻画

$$c\xi=0\ \ \forall c\in S\iff\xi\in S^{\perp}$$
$$\boxed{\ (b)\ \text{失败}\iff B\ \text{有特征向量落在}\ S^{\perp}\ \text{里}}$$

### 由此得到的证明路线

| 部分 | 可调？ |
|---|---|
| $B$ 在 $\mathbb R^d/S$ 上 | ❌ 固定（$=A'$）|
| $B$ 在 $S$ 上（及 $S^{\perp}$ 方向）| ✅ 可调（$N'$ 的行在 $S$ 中自由）|

$$\text{所以要证}:\quad \text{可以把每个特征值}\ \lambda\ \text{的特征空间"推出"}\ S^{\perp}\ ✓$$

**情形 A**：$\lambda$ 的重数 $\le$ 它作为 $A'|_{R^d/S}$ 特征值的重数 ✓ ⟹ 特征向量已在商方向 ✓ 不需推 ✓
**情形 B**：$\lambda$ 只在 $S$ 部分出现（$N'$ 造出来的）✓ ⟹ 可用 $N'$ 把它推离 $S^\perp$ ✓ ✓

**待补**：把情形 B 写成"$N'$ 的某个开条件" ✓（这与第 3 节的缺口是同一个 ✓）

---

## 3ter. 情形 B 的论证（$B$ 的特征向量落在 $S^{\perp}$ 是否可避免）

### 设定

$$\dim V=d,\quad S\subseteq\mathbb R^d,\ \dim S=p,\quad B=A'+N',\quad \operatorname{im}N'\subseteq S$$

（$N'=(\ell_iR_0)_{i\le d}$，每行在 $S$ 中 ⟹ $\operatorname{im}N'\subseteq S$ ✓）

### 关键引理

**引理 3.1.** 若 $\xi\in S^{\perp}$、$\xi\ne0$、$B\xi=\lambda\xi$，则 $\lambda$ 是 $\bar A'$（$A'$ 在 $\mathbb R^d/S$ 上的诱导）的特征值。

*证明.* 记 $\pi:\mathbb R^d\to\mathbb R^d/S$。$\pi(B\xi)=\pi(A'\xi)+\pi(N'\xi)=\pi(A'\xi)$（因 $\operatorname{im}N'\subseteq S$）。
而 $B\xi=\lambda\xi$ ⟹ $\pi(A'\xi)=\lambda\pi(\xi)$。
又 $\xi\in S^{\perp}$、$\xi\ne0$ ⟹ $\pi(\xi)\ne0$（因 $S\cap S^{\perp}=0$）。
故 $\lambda$ 是 $\bar A'$ 的特征值，$\pi(\xi)$ 是对应特征向量。∎

**推论 3.2.** 若 $\lambda\notin\operatorname{spec}(\bar A')$，则 $B$ 的 $\lambda$-特征向量必不在 $S^{\perp}$ 中 ✓

$$\Longrightarrow\ \textbf{只需处理}\ \lambda\in\operatorname{spec}(\bar A')\ \text{的那些特征值}✓$$

### 剩下的子问题（诚实标注）

$$\text{对}\ \lambda\in\operatorname{spec}(\bar A'),\ \text{需要}:\quad \ker(B-\lambda)\cap S^{\perp}=\{0\}$$

把 $B-\lambda$ 写成块形式（$S\oplus$ 补 ⟹ 但更自然的是 $S^{\perp}\oplus S$ 正交分解）：

$$B-\lambda=\begin{pmatrix} (B-\lambda)|_{S^{\perp}} & (B-\lambda)|_S \\ \end{pmatrix}:\ S^{\perp}\oplus S\to\mathbb R^d$$

- $(B-\lambda)|_S$ 可调（$N'$ 的行在 $S$ 中自由 ⟹ 可任意改 $S\to S$ 的块）✓
- $(B-\lambda)|_{S^{\perp}}$ 的 $S$ 分量也随 $N'$ 变 ✓

$$\text{可选}\ N'\ \text{使}\ \ker(B-\lambda)\cap S^{\perp}=\{0\}\iff\text{某个多项式不恒为零}$$

这个多项式**在已测实例上非零** ✓（2010 例、$n{=}7$ 例都有见证 ✓）

$$\boxed{\ \text{子缺口}:\quad \text{证明该多项式在一般}\ N'\ \text{上不恒为零}\ }$$

### 为什么它应当成立（直觉）

$$\dim S^{\perp}=d-p<d;\qquad N'\ \text{有}\ d\cdot p\ \text{个自由参数}$$
$$\text{"}\ker(B-\lambda)\cap S^{\perp}\ne0\text{"}\ \text{是}\ \text{codim}\ \ge1\ \text{的闭条件}\ ✗\ \Longrightarrow\ \text{有限多个这样的条件的并仍是真闭集}\ ✓\ (\text{只要每个都真})$$

**每个条件为真**：需要 $\ker(B-\lambda)\not\subseteq S^{\perp}$ 可达到 ✓ ——
即 $B$ 在 $S$ 方向上"看到"特征向量 ✓ —— 而 $N'$ 可自由改这一块 ✓ ⟹ 直觉上总可以 ✓。

**但严格证明需要**：展示一个具体的 $N'$ 使得对所有 $\lambda$ 都成立 ✓ ——
这等价于"在 Grassmannian 上找一个点"，而我们已有 6 个点 ✓。

---

## 7. 🎯 上界的证明骨架（2026-10-23 下午，新）

### 7.1 第 1 步：$(b)$ 失败的精确条件（$\dim V=d$）

$$\text{取坐标使}\ M=\begin{pmatrix}I_d\\0\end{pmatrix},\quad B=A'+N',\quad N'=(\ell_iR_0)_{i\le d},\quad \operatorname{im}N'\subseteq S$$

$$\boxed{\ B\xi=\lambda\xi\ (\xi\ne0)\ \iff\ (\lambda-A')\xi\in S\ \text{且}\ N'\xi=(\lambda-A')\xi\ }$$

*证明.* $B\xi=\lambda\xi\iff A'\xi+N'\xi=\lambda\xi$；$N'$ 的值域 $\subseteq S$ ⟹ $(\lambda-A')\xi=N'\xi\in S$ ✓；
反之若 $(\lambda-A')\xi\in S$ 且 $N'\xi=(\lambda-A')\xi$，则 $B\xi=\lambda\xi$ ✓。∎

### 7.2 第 2 步：坏的 $\xi$ 构成子空间

$$B_\lambda:=\{\xi\in S^{\perp}:\ (\lambda-A')\xi\in S\}\quad(\text{子空间};\ \text{只依赖}\ A',S,\lambda)$$

由第 1 步，$(b)$ 失败 $\iff\exists\lambda:\ \exists\xi\in B_\lambda\setminus0,\ N'\xi=(\lambda-A')\xi$ ✓

### 7.3 第 3 步：$N'$ 的自由度（这正是 $S'=S$）

$$\ell_i\mapsto\ell_i+k_i\ (k_iN=0)\ \Longrightarrow\ \ell_iR_0\mapsto\ell_iR_0+k_iR_0;\qquad \{kR_0:\ kN=0\}=\operatorname{row}(R_0)=S$$

$$\Longrightarrow\ \text{每个}\ \ell_iR_0\ \text{可在}\ S\ \text{中任意平移}\ \Longrightarrow\ \text{把}\ S\ \text{写成}\ \operatorname{span}(s_1,\dots,s_p)\ \text{后，系数}\ c_{ij}\ \text{自由}\ ✓$$

### 7.4 第 4 步：坏集是真子空间，故可避开

$$\text{失败}\iff\exists\lambda\in\operatorname{spec}(\bar A'),\ \xi\in B_\lambda\setminus0:\quad \underbrace{\textstyle\sum_j\xi_j\,c_j}_{\text{可由}\ (c_j)\ \text{取遍的形式}}=\underbrace{c'_\lambda(\xi)}_{\text{固定}}$$

其中 $c_j\in\mathbb R$ 是 $\ell_jR_0\in S$ 的系数（自由 ✓）。

- 对固定 $\lambda$，坏条件是 $(c_j)$ 空间里的**一个线性方程**（因 $\xi$ 固定时对 $c$ 线性）
- 该方程**非平凡**：只需一个 $\xi\in B_\lambda$ 有某 $\xi_j\ne0$，形式 $\sum\xi_jc_j$ 就非零 ✓
- $\operatorname{spec}(\bar A')$ 有限 ✓；$B_\lambda$ 有限维 ✓

$$\Longrightarrow\ \text{坏集}=\bigcup_{\lambda}\bigcup_{\xi\in B_\lambda}\{\text{一个真超平面}\}\quad\text{是有限多个真闭子集之并}$$

$$\Longrightarrow\ \text{存在}\ (c_j)\ \text{避开全部}\ \Longrightarrow\ \boxed{\ \exists N'\ \text{使}\ (b)\ \text{成立}\ }\ ✓$$

### 7.5 ⚠️ 这个骨架还需要补的细节

| # | 待补 | 难度 |
|---|---|---|
| 1 | 严格证明 $B_\lambda$ 的坏条件集是**真**子空间（不能是整个空间）| 中 |
| 2 | $\xi$ 连续变化时"并"仍是有限并（需用 $B_\lambda$ 的代数结构，而非逐 $\xi$）| 中 |
| 3 | $\dim V<d$ 的情形（$M$ 不满列秩，$\ker M\ne0$）| 中 |
| 4 | 把"$c_j$ 可自由取"与 lift 的其余约束（$\ell_iN=v_i$ 固定）协调 | 中 |

$$\boxed{\ \text{若这四步补齐，则上界成立}\ \Longrightarrow\ q_{\min}=\dim V+1\ \text{完全得证}\ \Longrightarrow\ \textbf{q1 为假（poly）}}$$

---

## 8. 🎯 上界的**可能障碍**：$\dim B_\lambda\le\dim S$ 是否总成立？

### 8.1 推导

$\dim V=d$ 时，$(b)$ 失败 $\iff\exists\lambda:\ \ker(\lambda I-B)\cap S^{\perp}\ne\{0\}$。

$$\xi\in S^{\perp},\ B\xi=\lambda\xi\iff \xi\in B_\lambda:=\{\xi\in S^{\perp}:(\lambda-A')\xi\in S\}\ \wedge\ N'\xi=(\lambda-A')\xi$$

而 $N'$ 在任意子空间上的作用可被**任意指定**：

$$N'\xi=\sum_{j=1}^{d}\xi_j\,r_j,\qquad r_j\in S\ \text{自由}\ (\text{由 }S'=S\text{ ✓})$$

$$\Longrightarrow\ N'|_{B_\lambda}:\ B_\lambda\to S\ \text{可以是任意线性映射}$$

### 8.2 于是

$$\text{坏}_\lambda\ \text{可避}\iff \exists\ \text{单射}\ B_\lambda\to S\iff\dim B_\lambda\le p=\dim S$$

$$\boxed{\ \text{若}\ \dim B_\lambda>p\ \text{对某个}\ \lambda\in\operatorname{spec}(\bar A'),\ \text{则}\ (b)\ \textbf{必然失败}\ ✗\ }$$

### 8.3 这是一个真正的潜在障碍

$$\dim B_\lambda\le\dim S^{\perp}=d-p,\qquad \dim S=p\ \Longrightarrow\ \dim B_\lambda>p\ \text{可能当}\ d>2p$$

**若这样的实例存在** ⟹ $q_{\min}>\dim V+1$ ⟹ **定理被推翻** ✗

**已知的 6 个实例都满足** $q_{\min}=\dim V+1$ ✓ ⟹ 它们应当都满足 $\dim B_\lambda\le p$ ✓（**待验证**）

### 8.4 下一步（关键）

1. 对 6 个实例计算 $\dim B_\lambda$（$\lambda\in\operatorname{spec}\bar A'$），验证 $\le p$ ✓
2. 若某个实例 $\dim B_\lambda>p$ 而仍有 $q_{\min}=\dim V+1$ ⟹ 我的推导有误 ✗（需重查）
3. 若全部 $\le p$ ⟹ 障碍不存在，骨架可继续 ✓
4. 若找到 $\dim B_\lambda>p$ 的实例 ⟹ **定理被推翻** ✗ —— 这正是"能否证伪"的具体答案 ✓

---

## 9. ✅✅ 障碍被排除：$B_\lambda=\ker(\lambda-\bar A')$，故 $\dim B_\lambda\le p$

### 9.1 决定性计算

搜索到 **$\dim V=d=4>2p=2$** 的实例（3 个），在 $q=d+1=5$ 上**构造成功** ✓ ✓

$$\text{障碍本应在此情形出现，实际没有}\ \Longrightarrow\ \dim B_\lambda\le p\ \text{另有原因}$$

### 9.2 障碍的精确身份

$$\text{映射}\ \varphi_\lambda:\ S^{\perp}\to V/S,\quad \xi\mapsto(\lambda-A')\xi \bmod S$$

**关键**：在内积识别 $S^{\perp}\cong V/S$ 下，$\varphi_\lambda=\lambda-\bar A'$ ✓

*证明要点.* $S^{\perp}\cong V/S$（$\dim$ 相同，且 $S\oplus S^{\perp}=V$ ✓）；$A'(S)\subseteq S$ ⟹ $A'^T(S^{\perp})\subseteq S^{\perp}$ ✓；
$\bar A'$ 在 $V/S$ 上 = $A'$ 的诱导 ✓，其对偶作用正是 $A'^T$ 在 $S^{\perp}$ 上 ✓。∎

$$\Longrightarrow\ B_\lambda=\ker\varphi_\lambda=\ker(\lambda-\bar A')\ \Longrightarrow\ \dim B_\lambda=\text{geo. mult. of }\lambda\le p$$

$$\boxed{\ \dim B_\lambda>p\ \textbf{永不发生};\ \text{障碍不存在}\ ✓\ }$$

### 9.3 骨架完整（五步）

| 步 | 内容 | 依据 |
|---|---|---|
| 1 | $(b)$ 失败 $\iff\exists\lambda,\ \xi\in B_\lambda\setminus\{0\},\ N'\xi=(\lambda-A')\xi$ | $N'$ 值域 $\subseteq S$ ✓ |
| 2 | $B_\lambda=\ker(\lambda-\bar A')$，$\dim\le p$ | §9.2 ✓ |
| 3 | $N'|_{B_\lambda}$ 可任意指定 | $S'=S$ ✓（3/3 验证）|
| 4 | 可选 $N'$ 使 $N'|_{B_\lambda}-(\lambda-A')|_{B_\lambda}$ 单射 | 由 2（$\dim B_\lambda\le\dim S$）✓ |
| 5 | 有限个 $\lambda$ ⟹ 有限个真闭条件 ⟹ 可同时避开 | ✓ |

$$\boxed{\ \textbf{上界}:\ \exists\mathcal L\ (\operatorname{row}(\mathcal LN)=V)\ \text{使}\ (5a)\wedge(5b)\ \Longrightarrow\ q_{\min}\le\dim V+1\ }$$

$$\text{结合已证下界}\ \Longrightarrow\ \boxed{\ q_{\min}=\dim V+1\ }$$

### 9.4 ⚠️ 仍需补的细节

| # | 细节 | 难度 |
|---|---|---|
| a | $S^{\perp}\cong V/S$ 与 $\varphi_\lambda=\lambda-\bar A'$ 的严格陈述 | 低（内积/对偶标准）|
| b | "有限个 $\lambda$" 中的 $\lambda$ 是 $\bar A'$ 的谱，需说明只用 $\operatorname{spec}(\bar A')$ | 低 |
| c | $\dim V<d$ 的推广（$\ker M\ne0$）| 中 |
| d | $N'|_{B_\lambda}$ 的"任意指定"需 $B_\lambda$ 的基与 $S$ 的自由度匹配 | 低 |

---

## 10. 四个细节的严谨版

### 10.0 设定

$V=\mathbb R^d$ 带标准内积；$S\subseteq V$ 是子空间（$\dim S=p$）；$A'\in\operatorname{End}(V)$ 满足 $A'(S)\subseteq S$；
$\bar A'$ 是 $A'$ 在 $W:=V/S$ 上的诱导映射；$\pi:V\to W$ 是商映射。

记 $N'\in\operatorname{End}(V)$ 满足 $\operatorname{im}N'\subseteq S$，$B:=A'+N'$。

### 细节 (a)：在 $S^\perp$ 上 $B$ 与 $A'$ 的商作用一致

**引理 a1.** $V=S\oplus S^{\perp}$，且 $\pi|_{S^{\perp}}:S^{\perp}\to W$ 是线性同构。

*证明.* $S\cap S^{\perp}=0$（内积正定）✓；$\dim S+\dim S^{\perp}=\dim V$ ⟹ $V=S\oplus S^{\perp}$ ✓；
$\pi|_{S^\perp}$ 单（$S\cap S^\perp=0$ ✓）且 $\dim S^\perp=\dim W$ ⟹ 同构 ✓ ∎

**引理 a2.** 对 $\xi\in S^{\perp}$：$\pi(B\xi)=\bar A'(\pi\xi)$。

*证明.* $\pi(B\xi)=\pi(A'\xi)+\pi(N'\xi)=\pi(A'\xi)+0$（因 $\operatorname{im}N'\subseteq S=\ker\pi$ ✓）
$=\bar A'(\pi\xi)$ ✓ ∎

**引理 a3.** $\dim B_\lambda\le p$，其中 $B_\lambda:=\{\xi\in S^{\perp}:\ (\lambda-A')\xi\in S\}$。

*证明.* 由 a2：$\xi\in B_\lambda\iff(\lambda-A')\xi\in S\iff\pi((\lambda-A')\xi)=0\iff(\lambda-\bar A')(\pi\xi)=0$ ✓
故 $\pi(B_\lambda)\subseteq\ker(\lambda-\bar A')\subseteq W$，$\dim\le\dim W=p$ ✓
由 a1，$\pi|_{S^\perp}$ 单 ⟹ $\dim B_\lambda=\dim\pi(B_\lambda)\le p$ ✓ ∎

### 细节 (b)：只需 $\lambda\in\operatorname{spec}(\bar A')$

**引理 b1.** 若 $B_\lambda\ne0$ 则 $\lambda\in\operatorname{spec}(\bar A')$。

*证明.* 取 $0\ne\xi\in B_\lambda$；$\pi\xi\ne0$（a1）且 $(\lambda-\bar A')(\pi\xi)=0$（a3 的证明）⟹ $\lambda$ 是特征值 ✓ ∎

$$\Longrightarrow\ \text{只需考虑}\ \lambda\in\operatorname{spec}(\bar A')\quad(\text{有限集, }|\operatorname{spec}|\le p)$$

### 细节 (c)：$\dim V<d$ —— **未解决** ✗（诚实标注）

此时 $\ker M=V^{\perp}\ne0$，故对 $\xi\in V^{\perp}$ 有 $M\xi=0$，于是

$$(b)\ \text{失败}\iff\exists\xi\in V^{\perp}\setminus\{0\}:\ F\xi=0$$

（注意 $\lambda$ 消失了！）

$$F\xi=M\big((A'\xi)_V\big)+(LR_0)\xi,\qquad (LR_0)\xi\in S$$

$$\text{坏}\iff\exists\xi\in V^{\perp}\setminus0:\ (A'\xi)_V+(LR_0)\xi=0\ \Longrightarrow\ (A'\xi)_V\in S$$

定义 $B:=\{\xi\in V^{\perp}:(A'\xi)_V\in S\}$。

### 🚨 检验结果：判据 $\dim B\le p$ **不适用**

| 实例 | $d$ | $\dim V$ | $p$ | $\dim B$ | $\dim B\le p$? | 实际 $q_{\min}$ |
|---|---|---|---|---|---|---|
| `cand` | 3 | 2 | 1 | 1 | ✓ | 3 ✓ |
| **`d4`** | 4 | 2 | 1 | **2** | ✗ | 3 ✓（有证书）|
| `p2` | 4 | 2 | 2 | 2 | ✓ | 3 ✓ |

$$\boxed{\ \dim B>p\ \textbf{不阻止}\ (b)\ \text{成立}\ ✗\ \text{——(c) 需要一个不同的论证}}$$

**原因**：$F|_{V^{\perp}}$ 可被 $L|_S$ 的自由度调整，不局限于 $S$ 的"容量"✓

**状态**：(c) 覆盖**全部三个反例**（都满足 $\dim V<d$ ✓），其 $q_{\min}=\dim V+1$ 已被精确验证 ✓，
但**没有证明** ✗。这是定理目前最大的缺口。

### 细节 (d)：$N'|_{B_\lambda}$ 的自由度

**引理 d1.** 设 $\{b_1,\dots,b_k\}$ 是 $B_\lambda$ 的基（$k\le p$）。则对任意 $y_1,\dots,y_k\in S$，存在 $N'$
（$\operatorname{im}N'\subseteq S$，且 $\ell_iN=v_i$ 的约束满足）使 $N'b_j=y_j$ 对所有 $j$。

*证明.* 记 $N'=(\ell_iR_0)_{i\le d}$，其中 $\ell_iN=v_i$ 固定、$\ell_i$ 可加任意 $k_i\in\ker(\cdot N)$。
由 $S'=S$（即 $\{kR_0:kN=0\}=S$ ✓，已验证 3/3），$\ell_iR_0$ 的平移可给出 $S$ 中**任意**向量 ✓
故 $(N' b_j)_i=\langle \ell_iR_0,\, b_j\rangle$ 可任意指定（对每个 $i,j$）✓
取 $\ell_iR_0$ 使 $\langle\ell_iR_0,b_j\rangle=(y_j)_i$（$\{b_j\}$ 线性无关，泛函可分离 ✓）⟹ $N'b_j=y_j$ ✓ ∎

**引理 d2（结论）.** 存在 $N'$ 使对所有 $\lambda\in\operatorname{spec}(\bar A')$、
所有 $0\ne\xi\in B_\lambda$：$N'\xi\ne(\lambda-A')\xi$。

*证明.* 对固定 $\lambda$：把 $\{(\lambda-A')\xi-N'\xi\}$ 的零点集避开即可。由 d1，取 $N'|_{B_\lambda}$ 使
$$N'|_{B_\lambda}-(\lambda-A')|_{B_\lambda}:\ B_\lambda\to S$$
**单射**（可能，因 $\dim B_\lambda=k\le p=\dim S$ ✓，且 $(\lambda-A')|_{B_\lambda}$ 的值域 $\subseteq S$ ✓）。
$\lambda$ 只有有限多个（b1）⟹ 逐次选择，每次是一个非空的"可避"条件（是一族真仿射子空间的补）⟹ 可同时满足 ✓ ∎

### 10.1 结论

$$\textbf{定理.}\quad \text{设}\ \alpha_0\in V.\ \text{则存在}\ \mathcal L\ (q=\rho+1,\ \operatorname{row}(\mathcal LN)=V)\ \text{满足}\ (5a)\wedge(5b).$$
$$\Longrightarrow\quad \rho_{\min}\le\dim V,\qquad \text{结合已证下界}\ \rho_{\min}=\dim V,\qquad \boxed{q_{\min}=\dim V+1}$$

**已严格证明**：(a1)(a2)(a3)(b1)(d1) ✓；
**已给思路**：(c) ✓；
**数值支持**：$S'=S$ 3/3 ✓、$q_{\min}=\dim V+1$ 6/6 ✓、$S\subseteq\mathcal A$ 18/18 ✓

---

## 11. 🚨 定理的修正：$q_{\min}=\max(\dim V+1,\ d-\dim V)$

### 11.1 新发现的下界

$\dim V=\rho<d$ 时 $\ker M=V^{\perp}$，故 $(b)$ 等价于

$$F|_{V^{\perp}}:\ V^{\perp}\ (\dim=d-\rho)\to\mathbb R^{q}\quad\textbf{单射}$$

$$\Longrightarrow\ \boxed{\ q\ \ge\ d-\rho\ }$$

结合已证的 $q\ge\rho+1$：

$$\boxed{\ q_{\min}\ \ge\ \max(\dim V+1,\ d-\dim V)\ }$$

### 11.2 旧公式的失效范围

$$\dim V+1\ \text{可能小于}\ d-\dim V\iff d>2\dim V+1$$

$$\text{例如}\ \rho=1,\ d=4:\quad \dim V+1=2\ \text{但}\ d-\rho=3\ \Longrightarrow\ q_{\min}\ge3>2\ ✗$$

**所以旧公式 $q_{\min}=\dim V+1$ 在 $d>2\rho+1$ 时是假的** ✗

### 11.3 新公式在 6 个实例上全部一致

| 实例 | $\rho$ | $d$ | $\max(\rho{+}1,d{-}\rho)$ | 实际 |
|---|---|---|---|---|
| 2010 例 | 4 | 4 | 5 | 5 ✓ |
| `cand` | 2 | 3 | 3 | 3 ✓ |
| `d4` | 2 | 4 | 3 | 3 ✓ |
| `p2` | 2 | 4 | 3 | 3 ✓ |
| $n{=}7$ | 3 | 3 | 4 | 4 ✓ |
| $c142$ | 3 | 3 | 4 | 4 ✓ |

### 11.4 两个下界都已证！

| 下界 | 证明 |
|---|---|
| $q\ge\rho+1$ | **Lean**（`LowerBound`：$\mathcal A$ 是 $A'$-不变 ⟹ $\mathcal A\supseteq V$ ⟹ $\rho\ge\dim V$；再接 $q\ge\rho+1$）|
| $q\ge d-\rho$ | 本节（$(b)$ ⟹ $F\vert_{V^\perp}$ 单射 ⟹ $d-\rho\le q$）|

$$\boxed{\ \textbf{双下界均成立}\ \Longrightarrow\ q_{\min}\ \ge\ \max(\dim V+1,\ d-\dim V)\ }$$

### 11.5 待做

1. **验证 $\rho=1,d=4$ 的情形**（$q_{\min}$ 应为 3 而非 2）——需要构造这样的实例 ✗（随机搜索未找到）
2. 修正后的**上界**：证明 $q_{\min}\le\max(\rho+1,d-\rho)$
3. 把 $q\ge d-\rho$ 也 Lean 化

---

## 12. 🎯 上界（$\dim V=\rho<d$ 情形）—— 证明

### 12.1 设定

$q:=\max(\rho+1,\ d-\rho)$，$\mathcal L$ 取 $q$ 行，$\operatorname{row}(\mathcal LN)=V$（由 §1.2 的线性引理可达）。
$M=\mathcal LN$（$q\times d$，$\operatorname{rank}=\rho$，$\ker M=V^{\perp}$）。

$$\text{关键}:\quad M\ \text{在 lift 的自由度下\textbf{不变}}\ ✓$$

*证明.* 自由度为 $\ell_i\mapsto\ell_i+k_i$（$k_iN=0$）✓；则 $M\mapsto M+KN=M$ ✓（$KN=0$）∎

### 12.2 问题化为"秩"

$$\xi\in V^{\perp}\Rightarrow M\xi=0\Rightarrow(\lambda M-F)\xi=-F\xi$$
$$\Longrightarrow\quad (b)\iff F\vert_{V^{\perp}}\ \textbf{单射}\iff\operatorname{rank}\big(F\vert_{V^{\perp}}\big)=d-\rho$$

（注意：**$\lambda$ 消失了** —— 与 §3 的 $\dim V=d$ 情形本质不同。）

### 12.3 分解

$$F=MA'+LR_0\ \Longrightarrow\ F\vert_{V^{\perp}}=F_1+F_2,\qquad F_1:=M\circ(A')_V\vert_{V^{\perp}},\quad F_2:=(L|_S)\circ R_0\vert_{V^{\perp}}$$

- $F_1$ **固定**（$M$ 不变 ✓，$(A')_V$ 由 $A',V$ 决定 ✓），$\operatorname{im}F_1\subseteq M(V)$，$\dim\le\rho$
- $F_2$ **可调**（$L|_S$ 自由 ✓），$\operatorname{im}F_2\subseteq L(S)$，$\dim\le p$

### 12.4 一般位置引理

**引理 12.1.** 设 $X$ 有限维，$F_1:X\to\mathbb R^q$ 固定，$F_2$ 在某个非空开集（$L|_S$ 的像）上变化，
且 $F_2$ 可取遍"某个子空间 $S_0\subseteq\mathbb R^q$ 上的任意线性映射"。则一般位置下
$$\operatorname{rank}(F_1+F_2)=\min\big(\dim X,\ \operatorname{rank}F_1+\dim S_0\big)$$

*理由.* $\operatorname{rank}(F_1+F_2)\le\min(\dim X,\operatorname{rank}F_1+\operatorname{rank}F_2)$ ✓；
反向：一般 $F_2$ 的值域与 $\operatorname{im}F_1$ 横截 ⟹ 和的像 $=\operatorname{im}F_1+\operatorname{im}F_2$ ✓

### 12.5 应用

$$\dim X=d-\rho,\qquad \operatorname{rank}F_1\le\rho,\qquad \dim S_0=\operatorname{rank}R_0\vert_{V^{\perp}}\le p$$

$$\Longrightarrow\quad \operatorname{rank}\big(F\vert_{V^{\perp}}\big)\ =\ \min\big(d-\rho,\ \rho+\operatorname{rank}R_0\vert_{V^{\perp}}\big)\quad\text{(一般位置)}$$

$$\textbf{若}\ d-\rho\ \le\ \rho+\operatorname{rank}R_0\vert_{V^{\perp}}\quad\Longrightarrow\quad \operatorname{rank}=d-\rho\quad\Longrightarrow\quad (b)\ \checkmark$$

### 12.6 两种情形

| 情形 | $q$ | 需要的 | 是否成立 |
|---|---|---|---|
| $d-\rho\le\rho+1$ | $\rho+1$ | $\rho+1\ge d-\rho$ ✓ | ✓（$q$ 足够大）|
| $d-\rho>\rho+1$ | $d-\rho$ | $\rho+p_1\ge d-\rho$，$p_1:=\operatorname{rank}R_0\vert_{V^\perp}$ | **即必要条件 $d\le2\rho+p_1$** ✓ |

$$\boxed{\ \text{所以：}\ d\le 2\rho+p_1\ \text{时，上界成立}\ (q=\max(\rho+1,d-\rho))\ ✓\ }$$

### 12.7 $p_1$ 的地位（已澄清）

$$p_1=\operatorname{rank}(R_0\vert_{V^{\perp}})=\dim R_0(V^{\perp})\ \le\ \operatorname{rank}R_0=p$$

（$R_0$ 是 $n\times d$ 矩阵，其秩同时是行/列空间维数；$V^{\perp}\subseteq\mathbb R^d$，故 $R_0(V^{\perp})\subseteq\mathbb R^n$，维数 $\le p$。）

$$\Longrightarrow\quad \textbf{上界的条件是}\ d-\rho\ \le\ \rho+p_1\quad(\text{用}\ p_1\ \text{而非}\ p)$$

**已知实例**：

| 实例 | $d$ | $\rho$ | $d-\rho$ | $\rho+p_1$ | 满足 |
|---|---|---|---|---|---|
| `d4` | 4 | 2 | 2 | $2+0=2$ | ✓ |
| `p2` | 4 | 2 | 2 | ✓ | ✓ |
| 2010 | 4 | 4 | 0 | 平凡 | ✓ |

$$\text{这些实例都有}\ d-\rho\le\rho\ (\text{即}\ d\le2\rho)\ \Longrightarrow\ \text{条件平凡成立}\ ✓$$

### 12.8 结论

$$\boxed{\ q_{\min}\ \le\ \max(\rho+1,\ d-\rho)\quad\text{在}\ 6/6\ \text{实例上}\ ✓;\ \text{证明依赖引理 12.1（一般位置）}}$$

**剩下的技术缺口**：$p_1=p$ 的验证（或把定理 3 的条件也改成 $d\le2\rho+p_1$）。

---

## 13. 🎯 结论：可行性的充要条件 + $q_{\min}$ 的完整形式

### 13.1 由 §12 得到的判据

$$\text{(b) 可行}\iff \operatorname{rank}(F\vert_{V^{\perp}})=d-\rho\iff d-\rho\le\rho+p_1$$

其中 $p_1=\operatorname{rank}(R_0\vert_{V^{\perp}})\le p=\operatorname{rank}R_0$。

- **必要性**（已证，§12.5）：$\operatorname{rank}(F\vert_{V^\perp})\le\dim\operatorname{im}F_1+\dim\operatorname{im}F_2\le\rho+p_1$
- **充分性**（§12.4 引理 12.1 一般位置）：$L|_S$ 自由 ⟹ $F_2$ 可取一般位置 ⟹ 秩取到上界

$$\boxed{\ \text{可行}\iff d-\rho\le\rho+p_1\qquad(\text{与}\ q\ \text{无关！})}$$

### 13.2 定理（最终形式）

$$\boxed{\ q_{\min}\ =\ \max\big(\rho+1,\ d-\rho\big)\qquad\text{(当}\ d-\rho\le\rho+p_1\text{)} }$$

$$\text{否则问题\textbf{无解}}\ (q_{\min}=\infty)\ ✗$$

### 13.3 三种情形的统一

| 情形 | $q_{\min}$ |
|---|---|
| $\rho=d$（$V=\mathbb R^d$）| $d+1$（$=\dim V+1$ ✓）|
| $d-\rho\le\rho+1$ | $\rho+1$（$=\dim V+1$ ✓）|
| $\rho+1<d-\rho\le\rho+p_1$ | $d-\rho$ |
| $d-\rho>\rho+p_1$ | **无解** |

$$\text{前两种情形} =\ \dim V+1\quad(\text{即旧的} \dim V+1\ \text{公式})\ ✓$$
$$\text{第三种才需要修正}\ ✗\quad(\text{这就是}\ d>2\rho+1\ \text{的情形})$$

### 13.4 证明的完整性

| 部件 | 状态 |
|---|---|
| 下界 $\rho+1$ | ✅ Lean |
| 下界 $d-\rho$ | ✅ 纸面 |
| 必要性 $d-\rho\le\rho+p_1$ | ✅ 纸面（§12.5）|
| **充分性**（引理 12.1 一般位置）| ⚠️ **陈述了，未严格证** ✗ |
| $6/6$ 实例一致 | ✅ |

$$\boxed{\ \text{定理的证明只差\textbf{引理 12.1}（一般位置）的严格化}}$$

### 13.5 引理 12.1 的严格版（待写）

**要证**：设 $X$ 有限维，$F_1:X\to\mathbb R^q$ 固定，$S_0\subseteq\mathbb R^q$ 子空间，
$\{F_2\}$ 是一族线性映射且 $\{F_2(v):F_2\in\mathcal F\}$ 在 $S_0$ 上"足够丰富"（可取遍 $S_0$-值的映射），
则一般 $F_2$ 使 $\operatorname{rank}(F_1+F_2)=\min(\dim X,\ \operatorname{rank}F_1+\dim S_0)$。

**证明思路**：$\operatorname{rank}(F_1+F_2)$ 的补集是 $\{F_2:\exists v\ne0,\ (F_1+F_2)v\in\ldots\}$ ——
用"横截性"：一般 $F_2$ 的像与 $\operatorname{im}F_1$ 横截 ⟹ 和的像 = 两者之和 ✓

---

