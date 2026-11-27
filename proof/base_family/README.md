# A3：基族 $\mathcal B_{s,k}$ 与 $S$ 的选择

> **对应 docs 条目**：A.1（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

**动机**：A2 解决了"固定 $S$ 时纤维里是否有谱可行 $U$"。剩下的问题是**$S$ 本身怎么选**——
即基族 $\mathcal B_{s,k}=\{S:\ \dim S=s,\ \dim T_S=k,\ S\ \text{可容许}\}$ 的结构。
**依据**：[QA18 §9](../../archive/expert_correspondence/QA18_2026-10-31.md) 的入口建议。

## 1. 入口（专家给）

$$D:=G\cap A^{-1}(H)=\{x\in G:\ Ax\in H\},\qquad \phi:D\to H/G,\quad \phi(x)=Ax+G .$$

**事实 1**：可容许 $S$（满足 $A(S)\subseteq Z\subseteq H$）必满足 $S\subseteq D$。
*证明*：$A(S)\subseteq Z\subseteq H$ ⟹ $S\subseteq A^{-1}(H)$；又 $S\subseteq G$ ⟹ $S\subseteq D$。$\square$

## 2. 分层变量 $K$

**定义**：$K:=S\cap\ker\phi$（即 $S$ 中"$A$ 把像送进 $G$"的部分）。

**事实 2**：$\dim K\ge s-k$，其中 $k=\dim T_S$。
*证明*：$\phi|_S:S\to H/G$ 的核是 $K$，故 $\dim\phi(S)=s-\dim K$。
而 $T_S=(A(S)+S)/S$，且 $T_S$ 在 $H/G$ 中的像正是 $\phi(S)$ ⟹ $k=\dim T_S\ge\dim\phi(S)=s-\dim K$。$\square$

**推论**：$K$ 是 $S$ 中维数 $\ge s-k$、且落在 $D\cap\ker\phi$ 的子空间。
特别地 $k\ge s-\dim(D\cap\ker\phi)$ 时该层**为空**。

## 3. 分层参数化

给定 $K\subseteq D\cap\ker\phi$（$\dim K=\kappa$），$S$ 的结构为
$$S=K\oplus S',\qquad S'\subseteq D,\quad S'\cap\ker\phi=0,\quad \phi(S')\subseteq H/G\ \text{为 }(s-\kappa)\text{ 维}.$$
即 $S'$ 是 $D/\ker\phi\cong\operatorname{im}\phi$ 中的 $(s-\kappa)$ 维子空间（要求 $S'\cap\ker\phi=0$）。

⟹ **$\mathcal B_{s,k}$ 被 $\{K\}$（$D\cap\ker\phi$ 的 Grassmannian 的并）参数化**，每个 $K$ 上的纤维是
$\operatorname{Gr}(s-\kappa,\ \operatorname{im}\phi)\cap\{\text{避开 } D\cap\ker\phi/K\}$。

**这是与 A2 完全同型的"Schubert 型"问题**，只是换到了 $D$ 上。

## 4. 与 A2 的关系

| | A2（固定 $S$）| A3（变 $S$）|
|---|---|---|
| 底层空间 | $H/S$ | $D$（或 $D/\ker\phi$）|
| 选择对象 | $U\subseteq H/S$，$\dim r$ | $S'\subseteq D/\ker\phi$，$\dim s-\kappa$ |
| 约束 | $U\supseteq T_S$、$U\cap B_S=0$ | $S'\cap\ker\phi=0$、$\phi(S')$ 自由 |
| 谱条件 | 由 $U$ 决定 | 由 $S$ **和** $U$ 共同决定 |

## 5. 待解决的问题（A3 的核心）

1. **$D$ 的结构**：$D=G\cap A^{-1}(H)$ 的维数与方程是什么？（$G=\mathcal V\cap H$，$\mathcal V=\ker[C;CA]$）
2. **$\phi$ 的秩**：$\operatorname{rank}\phi=\dim\operatorname{im}\phi\le\dim(H/G)$。
3. **$\mathcal B_{s,k}$ 是否是代数簇、维数多少**：按 §3 的参数化，它是若干 Grassmannian 纤维的并。
4. **$\mathcal B_{s,k}$ 上是否存在谱可行 $S$**：这才是最终问题（A2 给的是每个 $S$ 的条件，需要在其上再优化）。

## 6. 状态

- **事实 1、2**：[已证-纸面]（本节）
- **§3 参数化**：[已证-纸面]（结构分解）
- **§5 的问题**：**全部开放**

## 7. 下一步

1. 算 $D$ 与 $\phi$ 的显式形式（$G=\mathcal V\cap H$ 已知，$A^{-1}(H)$ 可算）；
2. 在 R17 与第二实例上算 $D$、$\phi$、$\mathcal B_{s,k}$ 的维数，与 A2 的结论对照；
3. 看 $\mathcal B_{s,k}$ 是否**本身就是**一个 Grassmannian（若是，A3 就归约到 A2）。

## 8. R17 上的核算（2026-10-31）

$G=\operatorname{span}(e_4,e_5,e_6)$（$\dim3$）、$H=\operatorname{span}(e_4,\dots,e_8)$（$\dim5$）、$H/G$（$\dim2$）由 $e_7,e_8$ 生成。

$A$ 作用：$Ae_4=e_8$、$Ae_5=e_5$、$Ae_6=e_6$、$Ae_3=e_7$、$Ae_7=e_1$、$Ae_8=e_2$。

$$D=G\cap A^{-1}(H)=G\ (\dim3)\quad\text{（三个基向量的像都没有 }e_3\text{ 分量）}$$

$$\phi(e_4)=e_8+G\ne0,\qquad \phi(e_5)=\phi(e_6)=0 .$$

$$\boxed{\ \ker\phi=\operatorname{span}(e_5,e_6)=S\ }$$

于是在 R17 上：$K=S\cap\ker\phi=S$（$\dim K=s=2$），对应的 $k=0$ ✓——与 R17 的 $T_S=0$（$A(S)=S$）**一致**。

**意义**：A3 的入口对象 $(D,\phi)$ 在 R17 上把"$S$ 是 $\ker\phi$ 的子空间"这件事**显式化**了：
$S$ 是 $\ker\phi$ 的 $2$ 维子空间（$\ker\phi$ 本身 $2$ 维，所以 $S=\ker\phi$ 唯一）。
这解释了为什么 R17 的 $S$ 没有选择余地——**基族在该实例上是单点**。

## 9. 第二实例的核算（$n=6$、$p=1$）

$C=e_1$、$Ae_6=e_1$、$Ae_3=e_3$、$Ae_4=e_4$、$Ae_5=e_5$、$Ae_2=e_2$、$L_0=e_2$。
$\mathcal V=\ker[e_1;e_6]=\operatorname{span}(e_2,e_3,e_4,e_5)$（$\dim4$）、$H=\ker[e_1;e_2]=\operatorname{span}(e_3,e_4,e_5,e_6)$（$\dim4$）、
$G=\operatorname{span}(e_3,e_4,e_5)$（$\dim3$）。

$Ae_3=e_3,Ae_4=e_4,Ae_5=e_5\in H$ ⟹ $D=G$（$\dim3$）；而 $H/G$ 只有 $1$ 维，且
$$\phi(e_3)=\phi(e_4)=\phi(e_5)=0\ \Longrightarrow\ \boxed{\ker\phi=D=G\ (\phi\equiv0)}$$

于是在第二实例上：**任何** $S\subseteq G$ 都有 $K=S$（$k=0$），与 R17 情形相同。

## 10. 两个实例的对照

| 实例 | $b=\dim G$ | $\dim(H/G)$ | $\dim D$ | $\ker\phi$ | $\mathcal B_{s,k}$ |
|---|---|---|---|---|---|
| R17 | 3 | 2 | 3 | $\operatorname{span}(e_5,e_6)$（$\dim2$）| 单点（$S=\ker\phi$ 唯一）|
| 第二实例 | 3 | 1 | 3 | $D=G$（$\dim3$）| $G$ 的 Grassmannian $\operatorname{Gr}(2,3)$ |

**观察**：两例都 $k=0$；差别在于 $\ker\phi$ 的大小（2 vs 3），即 $S$ 的可选性（1 个点 vs $\operatorname{Gr}(2,3)$ 的 $\mathbb P^2$）。

**⟹ A3 的第一个结构问题**：$\dim\ker\phi$（$"A$ 把 $G$ 送进 $H$ 的部分"）决定了基族的大小；
$\operatorname{rank}\phi=\dim(H/G)-\dim(\ker\phi/(D\cap G))$ 是关键的整数不变量。

## 11. 第三个实例：$k=1$（"唯一延拓"情形）

**构造**：把 R17 的 $e_5\mapsto e_5$ 改成 $e_5\mapsto e_7$（其余不变）。

> **索引约定坑**：本项目脚本里 $A[i][k]=(Ae_k)$ 的 $e_i$ 分量。所以"$e_5\mapsto e_7$"要写 `A[6][4]=1`，
> 不是 `A[4][6]`——我第一次写反，算出 $k=0$ 并差点得出"构造失败"的结论。

**数据**：$\mathcal V=\ker[e_1;e_2;e_7;e_8]=\operatorname{span}(e_3,e_4,e_5,e_6)$、$H=\operatorname{span}(e_4,\dots,e_8)$、
$G=\operatorname{span}(e_4,e_5,e_6)$、$D=G$；
$$\phi(e_4)=e_8+G,\quad \phi(e_5)=e_7+G,\quad \phi(e_6)=0\ \Longrightarrow\ \ker\phi=\operatorname{span}(e_6),\ \operatorname{rank}\phi=2=\dim(H/G) .$$

$S=\operatorname{span}(e_5,e_6)$：$K=S\cap\ker\phi=\operatorname{span}(e_6)$（$\dim1$），
$$\dim(A(S)+S)=3=s+1\ \Longrightarrow\ k=1\ (=\ s-\dim K\text{，事实 2 取等}) .$$

**这是 $r=1$、$k=1$ 的"唯一延拓"情形**（QA17 §4）：$T_S=\operatorname{span}(e_7\bmod S)\ne0$ 且 $\dim U=1$
⟹ $U=T_S$ **唯一**——没有纤维可搜。

**实测**（$Z=S\oplus\operatorname{span}(e_7)=\operatorname{span}(e_5,e_6,e_7)$，$q=3$）：

| 条件 | 结果 |
|---|---|
| $(A)$：$\operatorname{rank}[Z,AZR]=3/3$ | **True** ✓ |
| $(S)$：极大子式 gcd 次数 $=1$ | **False** ✗ |

⟹ 该实例在 $q=3$ 上**不可行**；用途是验证"$k=1$ 时 $U$ 唯一、直接检验"这条判据 ✓

## 12. 三个实例的分层覆盖

| 实例 | $k$ | $\ker\phi$ | $\mathcal B_{s,k}$ | 谱可行性 |
|---|---|---|---|---|
| R17 | 0 | $\operatorname{span}(e_5,e_6)=S$ | 单点 | ✓（75% 的 $U$）|
| 第二实例 | 0 | $G$ | $\operatorname{Gr}(2,3)$ | ✗（0/24 = **24 个 $U$**，不是 $S$；$S$-扫描见 A2 §32）|
| 第三实例 | **1** | $\operatorname{span}(e_6)$ | $S$ 含 $K$，$U=T_S$ 唯一 | ✗（唯一 $U$ 失败）|

## 13. 结构分析：$D$、$\phi$ 与 $k$ 的精确关系

### 13.1 定义链

$$\psi:G\longrightarrow W/H,\quad \psi(x)=Ax\bmod H,\qquad D=\ker\psi\ \subseteq\ G .$$
$$\phi:D\longrightarrow H/G,\quad \phi(x)=Ax\bmod G .$$

**事实 3**：$\dim D=b-\operatorname{rank}\psi$，其中 $b=\dim G$、$\operatorname{rank}\psi\le\dim(W/H)=w-h$。
**事实 4**：$\operatorname{rank}\phi\le\min(\dim D,\ h-b)$。
**链**：$\ker\phi\subseteq D\subseteq G$。

### 13.2 $k$ 的精确公式

对 $S\subseteq D$（$\dim s$）：
$$k=\dim T_S=\dim A(S)-\dim\big(A(S)\cap S\big).$$
**证明**：$T_S=(A(S)+S)/S\cong A(S)/(A(S)\cap S)$。$\square$

**推论 1**：$k\le\dim A(S)\le s$。
**推论 2**（与事实 2 的关系）：$\dim\phi(S)=s-\dim(S\cap\ker\phi)$，且 $\phi(S)\subseteq T_S$ 的像 ⟹
$$k\ \ge\ s-\dim K,\qquad K=S\cap\ker\phi .$$
**等号条件**：$k=s-\dim K$ 当且仅当 $A(S)\cap S\subseteq \ker\phi\cap S=K$（即 $A(S)$ 与 $S$ 的"额外相交"全落在 $\ker\phi$ 里）。

### 13.3 $\mathcal B_{s,k}$ 的形状

$$\mathcal B_{s,k}=\{S\in\operatorname{Gr}(s,D):\ \dim(A(S)+S)=s+k\}.$$
这是一个**闭条件**（$\dim(A(S)+S)$ 关于 $S$ 上半连续，$\le s+k$ 是闭的；$\ge s+k$ 是开的——所以
$\mathcal B_{s,k}$ 一般**不是**闭的，而是"闭 ∩ 开"的**局部闭**集）。

**维数估计**：$\dim\operatorname{Gr}(s,D)=s(b-s)$；条件 $\dim(A(S)+S)=s+k$ 是"行列式秩"条件，
在每个 $S$ 处余维 $\ge$ ...（未算）。

**结论**：$\mathcal B_{s,k}$ 是**局部闭代数集**（不是闭的），这与 A2 里"谱好集是 Zariski 开"的现象**同型**。

### 13.4 三个实例的数值验证

| 实例 | $b$ | $w-h$ | $\operatorname{rank}\psi$ | $\dim D$ | $h-b$ | $\operatorname{rank}\phi$ | $\dim\ker\phi$ |
|---|---|---|---|---|---|---|---|
| R17 | 3 | 1 | 0 | 3 | 2 | 1 | 2 |
| 第二实例 | 3 | 1 | 0 | 3 | 1 | 0 | 3 |
| 第三实例 | 3 | 1 | 0 | 3 | 2 | 2 | 1 |

**一致性检查**：$\dim\ker\phi=\dim D-\operatorname{rank}\phi$ ✓（3−1=2、3−0=3、3−2=1）✓

## 14. $\mathcal B_{s,k}$ 的维数：一般层与退化层

### 14.1 一般层 $k=s$ 是开的

若 $A|_D$ 单射（$\ker A\cap D=0$），则 $\dim A(S)=s$；一般 $S$ 还使 $A(S)\cap S=0$（当 $2s\le h$），
于是
$$k=s\qquad\text{（一般情形）}.$$
$$\mathcal B_{s,s}=\{S:\ A(S)\cap S=0\}\ \text{是开的、稠密的（$2s\le h$ 时）}.$$
*理由*：$A(S)\cap S=0$ 是"$[A|_S\ S]$ 列满秩"，是开条件；而一般 $S$ 满足它。$\square$

### 14.2 退化层 $k<s$ 是行列式簇

$k<s$ ⟺ $A(S)\cap S\ne0$ ⟺ 存在 $0\ne x\in S$ 使 $Ax\in S$，即 $S$ 含一个**广义特征向量**的循环子空间。
写成行列式条件：
$$\operatorname{rank}\big[\,[A|_S]\mid[S]\,\big]<2s\quad(\text{某 }2s\times2s\text{ 子式的零点}).$$
所以 $\mathcal B_{s,k}$（$k<s$）是 $\operatorname{Gr}(s,D)$ 中的**行列式簇**。

### 14.3 三个实例的层

| 实例 | $s$ | $k$ | 层 |
|---|---|---|---|
| R17 | 2 | 0 | 退化（$A(S)=S$，$A$-不变）|
| 第二实例 | 2 | 0 | 退化（$A(S)=S$）|
| 第三实例 | 2 | 1 | 半退化（$A(S)\cap S=\operatorname{span}(e_6)$，1 维）|

**注意**：三个实例都**不在**一般层 $k=s=2$——这说明**它们都是经过挑选的退化例子**（前两个来自反例构造，
第三个来自"唯一延拓"实验）。一般层的性质（$k=s$、开、稠密）**完全没有被检验过**。

### 14.4 结论与警告

- **一般层**：$k=s$，$\mathcal B_{s,s}$ 开稠密 ✓（纸面）
- **退化层**：行列式簇，维数未算
- **警告**：现有三个实例全在退化层，**不能**用来推断一般情形。需要构造一个 $k=s$ 的实例做对照。

**下一步**：构造 $k=s$ 的实例（取 $S$ 使 $A(S)\cap S=0$），检验 A2 的判据在该层是否成立。

## 15. 两条新结构事实与 $k=s$ 实例

### 15.1 硬剪枝：$k\le r$

$T_S\subseteq U$（一切容许 $U$ 都含 $T_S$）且 $\dim U=r$，故
$$\boxed{\ k\le r\ }$$
否则该类层**直接不可行**。这是比"$q>t$"更早、更便宜的剪枝。

对照 A2：$r=1$ 时只有 $k\in\{0,1\}$ ✓（与 QA17 §4 的 $r=1$ 分析一致）。

### 15.2 R17 的 $k\le1$ 障碍

R17 的 $A$ **逐点固定**平面 $P=\operatorname{span}(e_5,e_6)$。而 $G=P\oplus\operatorname{span}(e_4)$（$\dim3$），$s=2$：
$$\dim S+\dim P=4>\dim G=3\ \Longrightarrow\ S\cap P\ne0 .$$
取 $0\ne x\in S\cap P$：$Ax=x\in S$ ⟹ $A(S)\cap S\ne0$ ⟹ $k<2$。

$$\boxed{\ \text{R17 的基族只在 }k\le1\text{ 层——这解释了为何前三个实例测不到 }k=s\ }$$

### 15.3 $k=s$ 的实例（第三实例 + 合适的 $S$）

第三实例（$e_5\mapsto e_7$）：$A(G)=\operatorname{span}(e_8,e_7,e_6)$，与 $G=\operatorname{span}(e_4,e_5,e_6)$ 只有 $e_6$ 相交。
取 $S=\operatorname{span}(e_4,e_5)$：
$$A(S)=\operatorname{span}(e_8,e_7),\qquad A(S)\cap S=0\ \Longrightarrow\ k=2=s\ ✓$$
（实测 $\dim(A(S)+S)=4$）

**但**：该实例 $r=d-s=3-2=1$，而 $k=2>r=1$ ⟹ 由 15.1 **立即不可行**，不需要任何几何。

### 15.4 结论

- $k\le r$ 是硬剪枝；
- $k=s$ 层只在 $r\ge s$ 时可能出现；
- 要真正检验一般层，需要 $r\ge s$ 的实例（即 $q$ 较小、$d$ 较大），现有实例都不满足。

**下一步**：构造 $r\ge s$ 且 $k=s$ 的实例，那才是 A2 判据在一般层的第一次检验。

## 16. 一般层（$k=s$、$r\ge s$）的第一次抽样

**实例**：第三实例（$e_5\mapsto e_7$）、$q=2$ ⟹ $d=4$、$s=2$、$r=2$、$m=\dim(H/S)=3$、$k=2=s$ ✓
（$r\ge s$ ✓，$r\le h-b=2$ ✓ 边界）

**纤维**：$H/S$（3 维）中避开 $B_S=\operatorname{span}(e_6)$（在 $H/S$ 里是 $e_1$）的 **2 维**子空间，
即线性形式 $c_1x_1+c_2x_2+c_3x_3=0$ 且 $c_1\ne0$。

**抽样**（$c_1\in\{1,-1,2\}$、$c_2,c_3\in\{-1,0,1\}$，共 27 个）：

| 结果 | 数量 |
|---|---|
| 代数可行 $(A)$ | **3**（其余 24 个被 $(A)$ 排除）|
| 其中谱可行 $(S)$ | **0** |

**初步结论**：一般层**不是**自动可行的；且代数可行集在这里**很小**（3/27）。

**系统枚举（2026-10-31 补）**：$c_1\in\{1,2,3\}$、$c_2,c_3\in\{-3,\dots,3\}$，共 **147** 个候选：

| 结果 | 数量 |
|---|---|
| 代数可行 $(A)$ | **3**（144 个被 $(A)$ 排除）|
| 谱可行 $(S)$ | **0** |

**结论**：在 $k=s$ 层，$(A)$ 本身就是**极强的**约束（3/147 ≈ 2%），而三个代数可行点全部 $(S)$ 失败。

**但**：$\mathcal B_{s,k}$ 是代数簇，随机/网格采样会**严重低估**可行集（CLAUDE §7 第 12 条：稀有/薄集不许采样）。
这 147 个点只是纤维的一个网格，**不能**推断"一般层不可行"。正确做法是**符号求解** $(A)$ 在纤维上的解集。

---

## 17. 更正（QA19）：$k=r$ 时 $U=T_S$ 唯一——§16 的网格采错了对象

**专家的定理**（QA19 §2）：若 $k=s=r$，则 $T_S\subseteq U$ 且 $\dim U=\dim T_S=r$ ⟹ $\boxed{U=T_S\text{ 唯一}}$。

**我的 §16 实验错在哪**：我让 $U$ 跑遍 $\operatorname{Gr}(2,H/S)$ 的 147 个网格点，但**没有强制 $T_S\subseteq U$**——
所以那 147 个点里绝大多数根本**不是容许的 $U$**。$(A)$ 拒绝 144 个，正是这个原因（不是"$(A)$ 强"，而是"$U$ 选错了"）。

**正确的核算**（$S=\operatorname{span}(e_4,e_5)$、第三实例）：

| 量 | 值 |
|---|---|
| $A(S)$ | $\operatorname{span}(e_8,e_7)$ |
| $k=\dim T_S$ | **2** |
| $T_S$ | $\operatorname{span}(e_8,e_7)$ |
| $Z=S\oplus T_S$ | $\operatorname{span}(e_4,e_5,e_7,e_8)$（$\dim4$）|
| $(A)$：$\operatorname{rank}[Z,AZR]=4/4$ | **True** ✓ |
| $(S)$：gcd 次数 $=2$ | **False** ✗ |

$$\boxed{\ \text{该 }S\text{ 代数可行（唯一 }U\text{ 就行）、但谱不可行}\ }$$

**结论**：§16 的 "3/147" **作废**；正确说法是"该 $S$ 代数可行、谱不可行"。

---

## 18. $(k,\ell)$ 分层（QA19 §4，取代单一 $k$）

**定义**：$\ell(S)=\operatorname{rank}(\phi|_S)$。**恒等式**：
$$\boxed{\ \dim(T_S\cap B_S)=k-\ell\ }$$
*证明*：$\pi:H/S\to H/G$ 的核是 $B_S$；$\pi|_{T_S}$ 的像是 $\phi(S)$（$\dim\ell$）⟹ 核 $=T_S\cap B_S$ 维数 $k-\ell$。$\square$

**两级剪枝**：
$$\boxed{\ k\le r\quad\text{且}\quad \ell=k\ }$$
- $k>r$：$U$ 装不下 $T_S$ ⟹ 不可行；
- $\ell<k$：$T_S\cap B_S\ne0$ ⟹ 任何 $U\supseteq T_S$ 都与 $B_S$ 相交 ⟹ 不可行；
- $\ell=k$：普适障碍消失（但**不保证** $r$ 维延拓存在）。

**分层**：$\mathcal B_{s,k,\ell}=\{S:\ k(S)=k,\ \operatorname{rank}(\phi|_S)=\ell\}$，且 $\ell\le k\le r$。

### 18.1 $k=s=r$ 的精确判据（QA19 §2）

$$T_S\cap B_S=0\iff \phi|_S\ \text{单射}\iff \operatorname{rank}(\phi|_S)=s .$$
若 $\rho_\phi:=\operatorname{rank}\phi<s$：该层**为空**；若 $\rho_\phi\ge s$：代数可行集在 $\operatorname{Gr}(s,D)$ 中**非空开稠密**。

**第三实例的审计**：$\rho_\phi=2\ge s=2$ ⟹ 按定理，该层应非空开稠密 ✓——与"唯一 $U=T_S$ 代数可行"**一致**，
与 §16 的 3/147 **矛盾**（后者是采样错误）✓

### 18.2 三个不同的集合（QA19 §4 Q3）

| 集合 | 性质 |
|---|---|
| 固定秩层 $\mathcal B_{s,k}$ | 局部闭 |
| $+$ 普适障碍消失（$\ell=k$）| 在上一层中**开**（等价于 $\operatorname{rank}(\phi|_S)=k$）|
| 存在谱可行延拓 $U$ | 前两者的**投影**，只是**可构造**集，不必局部闭 |

## 19. 固定平面障碍的推广（QA19 §3）

定义 $E_\mu=\ker(A-\mu I)\cap G$。若 $S\cap E_\mu\ne0$，则 $A(S)\cap S\ne0$（取 $0\ne x\in S\cap E_\mu$，$Ax=\mu x\in S$）。
维数强制：$s+\dim E_\mu>\dim G$ ⟹ 必有交。更一般地，任取 $A$-不变子空间 $P\subseteq G$，同样的维数论证适用。

R17 的固定平面 $P=\operatorname{span}(e_5,e_6)$ 是 $\mu=1$ 的特征空间特例。

### 19.1 恒等式 $\dim(T_S\cap B_S)=k-\ell$ 的回归验证（2026-10-31）

构造实例（$A$：$e_3\mapsto e_7$、$e_4\mapsto e_6$、$e_5\mapsto e_7$、$e_6\mapsto e_6$；$G=\operatorname{span}(e_4,e_5,e_6)$）：

| $S$ | $k$ | $\ell$ | $\dim(T_S\cap B_S)$（直接算）| $k-\ell$ |
|---|---|---|---|---|
| $\operatorname{span}(e_4,e_5)$ | 2 | 1 | **1** | **1** ✓ |
| $\operatorname{span}(e_4,e_6)$ | 0 | 0 | 0 | 0 ✓ |
| $\operatorname{span}(e_5,e_6)$ | 1 | 1 | 0 | 0 ✓ |

**第一个例子是 $\ell<k$ 的实例**（$k=2,\ell=1$）⟹ 由两级剪枝**立即不可行**（$T_S\cap B_S\ne0$），
不需要任何谱计算。这正是 $(k,\ell)$ 分层比单一 $k$ 更强的地方。

## 20. $r=2$ 的三个层与 A2 的对接

$r=2$ 时 $k\in\{0,1,2\}$（由 $k\le r$）且 $\ell\le k$。三层的纤维结构：

| $k$ | 纤维 | 维数 | 状态 |
|---|---|---|---|
| **2** | $U=T_S$ **唯一** | 点 | **已判定**（单次铅笔检验）|
| **1** | $U=T_S\oplus L$，$L$ 是 $(H/S)/T_S$ 中的**直线** | $\dim\mathbb P(\cdot)$ | A2 的 $r'=1$ 分类可套用 |
| **0** | $U\subseteq H/S$ 的 2 维子空间 | $\operatorname{Gr}(2,\cdot)$ | A2 命题 5 的三分 |

### 20.1 $k=2$：已解决

由 QA19 的定理：$U=T_S$ 唯一，$Z=S\oplus T_S$，直接算 $(A)$ 与 $(S)$。无几何。

**（且 $k=2$ 要求 $\ell=2$，否则被剪枝 2 淘汰。）**

### 20.2 $k=1$：化归到 A2 的 $r=1$

商掉 $T_S$：$\widetilde H=(H/S)/T_S$（维数 $m-1$）、$\widetilde U=U/T_S$（维数 $1$）。
则 $U\cap I_\lambda=0\iff\widetilde U\cap\widetilde I_\lambda=0$，其中 $\widetilde I_\lambda$ 是 $I_\lambda$ 在 $\widetilde H$ 中的像。
**这正是 A2 的 $r=1$ 情形**（命题 4 的四分类）✓——所以 $k=1$ 层被 A2 **完全覆盖**。

### 20.3 $k=0$：A2 命题 5 的三分

$U$ 是 2 维，$\Sigma_\lambda=\{U:U\cap I_\lambda\ne0\}$ 余维 $m-2-r_\lambda+1$：
- 所有 $r_\lambda\le m-3$ ⟹ 可行；
- 某 $r_\lambda\ge m-1$ ⟹ 不可行；
- $r_\lambda=m-2$ ⟹ **除子情形（开放）**。

### 20.4 结论

$$\boxed{\ r=2\ \text{的问题}=\underbrace{k=2}_{\text{已解}}+\underbrace{k=1}_{\text{A2 }r=1\text{ 覆盖}}+\underbrace{k=0}_{\text{除子情形（开放）}}\ }$$

所以 $r=2$ **只剩 $k=0$ 的除子情形**——与 A2 的开放部分**完全相同**，没有新的困难。

#### 20.6 更正（QA20）：递归**不**把一切化归到 $k=2,1,0$

**原结论（过强，已撤回）**：我写过"所有层都归结到 $k=2$（已解）、$k=1$（A2 的 $r=1$）、$k=0$（除子）"。

**专家的更正**：商掉 $T_S$ 后**剩余延拓维数是 $r'=r-k$**，所以：

| 原 $k$ | 剩余维数 $r-k$ | 已知什么 |
|---|---|---|
| $k=r$ | 0 | $U=T_S$ 唯一，单次铅笔检验 ✓ |
| $k=r-1$ | 1 | A2 的 $r=1$ 分析**可能**适用（需其假设）|
| $k\le r-2$ | $\ge2$ | **真正的高维延拓问题仍在** |

**反例（专家给）**：$r=4$、$k=2$ ⟹ $r'=2$——**不能**用"唯一延拓"解决；
$r=4$、$k=1$ ⟹ $r'=3$。

$$\boxed{\ \text{商化降低延拓维数，但一般**不**化归到已解情形}\ }$$

**我的 §20 的 $r=2$ 分解只在 $r=2$ 时成立**（那时 $k=2\Rightarrow r'=0$、$k=1\Rightarrow r'=1$、$k=0\Rightarrow r'=2$）。
一般 $r$ 下必须写成"$k=r$ 已解；其余剩下 $r-k$ 维问题"。

**"递归失败"的准确含义**（专家 §3）：问题类**不**对这个商运算封闭 ⟹ 否定了**朴素的**"对 $r$ 归纳"，
但**不**否定"带更多数据的归纳"（跟踪：投影族的次数、$\dim(I_\lambda\cap T_S)$、秩跳变值、Plücker 张成的维数）。

## 20.5 递归引理（$k<r$ 时化归到更小的 $r$）

**引理**：设 $T_S\subseteq U\subseteq H/S$，$\pi_T:H/S\to\widetilde H:=(H/S)/T_S$。则
$$\boxed{\ U\cap I_\lambda=0\iff \pi_T(U)\cap\pi_T(I_\lambda)=0\ }$$

*证明*：
($\Leftarrow$) 若 $0\ne x\in U\cap I_\lambda$，则 $\pi_T(x)\in\pi_T(U)\cap\pi_T(I_\lambda)$ 且 $\pi_T(x)\ne0$（因 $x\notin T_S$：$x\in U$ 且 $U\cap I_\lambda=0$ ⟹ $x\notin I_\lambda$... 需另证 $x\notin T_S$：$T_S\subseteq U$ 且 $T_S\subseteq I_\lambda$?? 不成立）。
重新论证：($\Leftarrow$) 设 $y\in\pi_T(U)\cap\pi_T(I_\lambda)$，$y\ne0$。则 $y=\pi_T(u)=\pi_T(i)$，$u\in U$，$i\in I_\lambda$。故 $u-i\in T_S\subseteq U$ ⟹ $i=u-(u-i)\in U$ ⟹ $i\in U\cap I_\lambda$ 且 $i\ne0$（若 $i=0$ 则 $u\in T_S\subseteq U$ 且 $y=\pi_T(u)=0$，矛盾）。✓
($\Rightarrow$) 设 $0\ne i\in U\cap I_\lambda$。若 $i\in T_S$：由 $T_S\subseteq U$ 无矛盾，需另处理——但 $T_S\cap I_\lambda$ 已由**剪枝 2**（$\ell=k$）排除，故 $i\notin T_S$ ⟹ $\pi_T(i)\ne0$ ⟹ $\pi_T(i)\in\pi_T(U)\cap\pi_T(I_\lambda)$ 非零 ✓。$\square$

**推论**（递归）：在剪枝 2 之后，问题变为在 $\widetilde H$（$\dim m-k$）中找 $\dim(r-k)$ 的子空间避开族 $\{\pi_T(I_\lambda)\}$。

**新族的结构**：$\dim\pi_T(I_\lambda)=\dim I_\lambda-\dim(I_\lambda\cap T_S)$——**不是**原来的 $r_\lambda$。

**警告**：新族 $\{\pi_T(I_\lambda)\}$ **未必**仍是"铅笔的像与固定子空间的交"，所以递归**不一定**回到同一个问题类型。
这一点决定了"对 $r$ 归纳"能否成立——**目前未定**。

## 21. 机器验证清单（2026-10-31）

对三个实例 × 每个 $G$ 的 2 维坐标子空间（共 9 组），逐条核对：

| 检查 | 结果 |
|---|---|
| 事实 1（$S\subseteq D$）| **9/9 True** ✓ |
| 恒等式 $\dim(T_S\cap B_S)=k-\ell$ | **9/9 相符** ✓ |
| 剪枝 $k\le r$ | 第三实例 $q=3$、$S=\operatorname{span}(e_4,e_5)$ 给出 $k=2>r=1$ ⟹ **剪枝生效** ✓ |
| $k=s=r$ 定理的前提 $\operatorname{rank}\phi\ge s$ | 第三实例：$\operatorname{rank}\phi=2\ge2$ ✓ |

**仍未机器验证的**：

| 陈述 | 状态 |
|---|---|
| 事实 2（$\dim K\ge s-k$）| 纸面（与 $\ell\le k$ 等价，可并入恒等式验证）|
| 事实 3（$k$ 的公式）| 纸面（计算中实际用到）|
| 事实 5（$\mathcal B_{s,k}$ 局部闭）| 纸面（一般性陈述，未做实例检查）|
| 命题 3（全超平面判据）| **无实例**（A2 遗留）|
| 递归引理 | **无实例**（A3 §20.5）|

## 22. Lean 覆盖的最终状态（2026-10-31）

| 陈述 | Lean | 文件 |
|---|---|---|
| 事实 4（$T_S\subseteq U\Rightarrow\dim T_S\le\dim U$，即 $k\le r$）| **✓** | `A3.lean`（`finrank_le_of_le`）|
| 事实 3 的一半（$\dim A(S)\le\dim S$，即 $k\le s$）| **✓** | `A3.lean`（`finrank_map_le_finrank`）|
| $(k,\ell)$ 恒等式的维数核心 $\dim(T\cap B)+\dim(\text{像})=\dim T$ | **✓ 完成** | `A3id.lean`（2026-10-31）|
| 事实 5（$\mathcal B_{s,k}$ 局部闭）| ✗ 纸面 | — |

### 22.1 恒等式的 Lean 完成记录（2026-10-31 晚）

**已完成**：`A3id.lean` 四条引理全部通过（EXIT=0）——
`range_mkQ_comp`、`ker_mkQ_comp`、`finrank_comap_subtype`、`finrank_inter_add_finrank_map_mkQ`。
关键一步是把 `comap = T ⊓ B` 的**直接相等**（类型不同、不可写）换成**构造线性等价** `↥(comap …) ≃ₗ ↥(T ⊓ B)`。

历史记录（当时的卡点）：
```lean
theorem finrank_quotient_sup_add (P Q : Submodule K W) :
    Module.finrank K (↥(P ⊔ Q) ⧸ (Q.comap (P ⊔ Q).subtype))
      + Module.finrank K ↥(P ⊓ Q) = Module.finrank K ↥P
```

**已探明**：
- 语句形状**可通过 elaboration** ✓
- `Submodule.finrank_quotient_add_finrank`（`finrank (M ⧸ N) + finrank N = finrank M`）存在 ✓
- `Submodule.finrank_sup_add_finrank_inf_eq`（`finrank (s⊔t) + finrank (s⊓t) = finrank s + finrank t`）存在 ✓
- `Submodule.comap_inf`、`Submodule.mem_comap` 存在 ✓

**卡点**：`Q.comap (P ⊔ Q).subtype = Q` 是**类型错误**（两边在不同环境里）。

**2026-10-31 进展**：四个关键引理名已确认存在——Submodule.range_subtype、LinearMap.ker_comp、
Submodule.ker_mkQ、Submodule.comap_subtype_self、Submodule.range_mkQ；且
LinearMap.finrank_range_add_finrank_ker (Submodule.mkQ B ∘ₗ T.subtype) **编译通过** ✓。
剩余：把 range 识别为 Submodule.map (Submodule.mkQ B) T（
ange_comp 给的是 map g ⊤，需另证）、
ker 识别为 T ⊓ B（用 comap_subtype_self）。**这是一步之遥，不是概念问题。**

**推荐路线**：用秩-零化度代替商同构——复合 $P\hookrightarrow W\twoheadrightarrow W/Q$ 的核是 $P\cap Q$、像 $\cong(P+Q)/Q$，
再用 `LinearMap.finrank_range_add_finrank_ker`。需要在 Lean 里建立 $P/(P\cap Q)\cong(P+Q)/Q$（第二同构定理），
或直接用 `LinearMap.quotKerEquivRange`。

### 22.2 Lean 总清单（10 个文件，全部 EXIT=0）

`TheoremC/D/E`、`QuotientPencil`、`CoreLemma`、`ExistsRLemmas`、`A2`、`A2dim`、`A2root`、`A3`。
回归：`wsl -e bash tools/lean/check_lean.sh`。

## 23. 更正（QA20）：除子情形**不是**唯一剩余障碍

我曾在报告 §5 里写"除子情形是单一剩余数学障碍"——**过强，已撤回**。

**两个独立的问题**：

| # | 问题 | 状态 |
|---|---|---|
| 1 | **固定 $S$ 的谱可行性**（高维延拓、余维 1 的 Schubert 坏轨迹）| 开放（除子情形是它的一部分）|
| 2 | **基族选择**：找一个 $S$ 既满足代数要求、又使对应谱纤维非空 | 开放，且**不因问题 1 解决而消失** |

**全局问题是一个联合存在式**：
$$\exists S,\ U:\quad S\in\mathcal B_{s,k,\ell},\quad T_S\subseteq U,\quad U\cap B_S=0,\quad \text{谱条件}.$$

固定 $S$ 的纤维定理**不自动**解决对 $S$ 的投影（$"\exists S"$ 部分）。

### 23.1 专家的建议：联合 $(S,U)$ 入射空间

$$\mathcal X_{s,k,\ell}=\left\{(S,U):\ \begin{array}{l}S\in\operatorname{Gr}(s,D),\ \dim T_S=k,\ \operatorname{rank}(\phi|_S)=\ell,\\ T_S\subseteq U,\ \dim U=r,\ U\cap B_S=0\end{array}\right\}$$

**下一里程碑**：在 $\mathcal X_{s,k,\ell}$ 上理解 $(S,U)$ 的**联合几何**（而非分别研究基与纤维），
再加谱条件作为子集。这是通向原判定问题的路线。

### 23.2 $k=s=r$ 定理的正名（QA20 §4）

应命名为 **"$k=s=r$（完全强制）情形下的代数可容许性"**——
它刻画的是**代数**要求（$T_S\cap B_S=0\iff\phi|_S$ 单射），**不**蕴含谱可行。
谱条件仍需对唯一候选 $Z=S\oplus T_S$ 单独检验。

### 23.3 除子情形不会随 $r$ 变大而变易（QA20 §6）

$c_\lambda=m-r-r_\lambda+1$；除子情形 $c_\lambda=1\iff r_\lambda=m-r$。
增大 $r$ **不自动**增大余维——除子条件对每个 $r$ 都可能持续存在。
正确的比较对象是 $\dim\operatorname{Gr}(r,m)=r(m-r)$、族的次数、其 Plücker 像的张成维数三者的**相互作用**。

## 24. B1：语义层的 Lean（QA21 §1.3，2026-10-31）

**新文件 `A3sem.lean`**（已进回归，14 文件全绿）：

| 引理 | 内容 |
|---|---|
| `finrank_inter_add_finrank_map_mkQ` | $\dim(T\cap B)+\dim(\text{map}(\text{mkQ}\,B)\,T)=\dim T$ |
| **`finrank_map_mkQ`** | $\dim\big(\text{map}(\text{mkQ}\,q)\,p\big)=\dim p-\dim(p\cap q)$ |
| **`finrank_TS_and_phi`** | 取 $p=A(S)$：$k=\dim A(S)-\dim(A(S)\cap S)$、$\ell=\dim A(S)-\dim(A(S)\cap G)$，**同一公式** |

**语义对应**（纸面 + 上述引理）：
$$T_S=(A(S)+S)/S=\text{map}(\text{mkQ}\,S)\,A(S),\qquad \phi(S)=(A(S)+G)/G=\text{map}(\text{mkQ}\,G)\,A(S)✓$$

**仍待 Lean 的最后一步**：$T_S\cap B_S$ 的显式识别（$B_S=\text{map}(\text{mkQ}\,S)\,G$）+
模律 $(A+S)\cap G=A+(S\cap G)$（当 $S\le G$）。这两步到位后即可由上面的公式直接推出
$$k-\ell=\dim(A(S)\cap G)-\dim(A(S)\cap S)=\dim(T_S\cap B_S).$$
**现状**：公式层已 Lean，最后的模律识别仍纸面。

## 25. $r\ge2$ 验证 campaign（QA21 §2.3，`c279`，2026-10-31）

**检验的命题**：两条剪枝 $k\le r$、$\ell=k$ 的必要性——判"不可行"时，枚举必须**找不到**代数可行点。

**方法**：18 个配置（2 实例 × 3 个 $S$ × $q\in\{1,2,3\}$），每个配置在纤维里取 ~180 个**一般** $U$
（$r\times m$ 小整数系数矩阵的行空间，**不是**坐标子空间），精确算术算 $(A)$ 与 $(S)$。

| 实例 | $S$ | $q$ | $d$ | $r$ | $k$ | $\ell$ | 剪枝 | 候选 | $(A)$ | $(S)$ |
|---|---|---|---|---|---|---|---|---|---|---|
| R17 | $e_5,e_6$ | 1 | 5 | 3 | 0 | 0 | pass | 171 | 171 | **0** |
| R17 | $e_5,e_6$ | 2 | 4 | 2 | 0 | 0 | pass | 185 | 171 | 5 |
| R17 | $e_5,e_6$ | 3 | 3 | 1 | 0 | 0 | pass | 198 | 195 | **125** |
| R17 | $e_4,e_5$ | 2 | 4 | 2 | 1 | 1 | pass | 185 | 31 | 5 |
| R17 | $e_4,e_5$ | 3 | 3 | 1 | 1 | 1 | pass | 198 | 3 | 0 |
| III | $e_4,e_5$ | 2 | 4 | 2 | 2 | 2 | pass | 185 | 7 | 0 |
| III | $e_4,e_5$ | **3** | 3 | **1** | **2** | 2 | **k>r** | 198 | **0** | **0** |

**关键结论**：

1. **剪枝 $k>r$ 被验证**：III、$S=e_4,e_5$、$q=3$ 时 $k=2>r=1$，198 个候选里**代数可行为 0** ✓
   （与"$U\supseteq T_S$ 且 $\dim U=r$ ⟹ $k\le r$"一致）；
2. **$k$ 越大，$(A)$ 可行点越少**（171 → 31 → 3）：因随机 $U$ 不含 $T_S$，$k\ge1$ 时必须"恰好包含"才通过；
3. **$r=3$ 全部 $(S)$ 失败**（R17 $q=1$：171 个代数可行、**0** 个谱可行）——与"$r$ 大时更难"的直觉一致；
4. **唯一的谱正例仍在 $r=1$**（$q=3$、$k=0$：125/198）。

**诚实评估（已按 QA22 §2 更正）**：

**必须区分两个问题**：
1. **抽象的固定 $S$ 问题**（任意 Grassmannian 有理曲线）：$r\ge2$ **确实可行** ——
   我们在 A2 §20.4b 的二次曲线实例中找到了 **73 个** $W$ 使 $\det[W\mid B(\lambda)]$ 为非零常数，
   那里的 $r=2$ ✓。所以"$r\ge2$ 不可行"的猜想在抽象层面**已被自己的例子推翻**。
2. **由 $\mathrm{DEC}(q)$ 的铅笔导出的族**：本 campaign 的 18 个配置中**没有**谱正例；
   且命题 2 原理上认证不了（$r\le p-1$，A2 §22）。

$$\boxed{\ \text{抽象的 }r\ge2\text{ 可行（有例子）；}\mathrm{DEC}(q)\text{ 导出的 }r\ge2\text{ 未知}\ }$$

**开放问题**因此改为：**哪一类 Grassmannian 有理曲线能由 $\mathrm{DEC}(q)$ 的铅笔实现？**
（专家 QA22 §2 的措辞：abstract pencil-generated family vs family from the full DEC(q) construction。）

### 24.1 语义恒等式**已完成 Lean**（2026-10-31 晚）

`A3sem.lean` 现在包含：

| 引理 | 内容 |
|---|---|
| `inf_sup_of_le` | **模律**：$S\le G\Rightarrow(P\sqcup S)\sqcap G=(P\sqcap G)\sqcup S$ |
| `finrank_map_mkQ` | $\dim\text{map}(\text{mkQ}\,q)\,p=\dim p-\dim(p\cap q)$ |
| `finrank_TS_and_phi` | $k$ 与 $\ell$ 的同一公式 |
| **`dim_TS_inter_BS_add`** | $\dim(T_S\cap B_S)+\dim\phi(S)=\dim T_S$ |

**回归**：14 文件全部 OK ✓

**注意**：`dim_TS_inter_BS_add` 的第三项写成了
`map (mkQ (map (mkQ S) G)) (map (mkQ S) (map A S))`——即"先商 $S$、再商 $G/S$"的像。
它在语义上等于 $\phi(S)=(A(S)+G)/G$（由模律保证），但**这个等式本身没有单独 Lean 化**；
Lean 化的是**加性恒等式**（$\dim(T_S\cap B_S)+\dim(\text{像})=\dim T_S$）。

### 24.2 QA22 要求的"语义减法形式"：**未完成**（2026-10-31）

要证：
```lean
theorem dim_TS_inter_BS_semantic (A : W →ₗ[K] W) (S G : Submodule K W) (h : S ≤ G) :
    finrank (T_S ⊓ B_S) = finrank T_S - finrank (map (mkQ G) (map A S))
```
其中 `T_S := map (mkQ S) (map A S)`、`B_S := map (mkQ S) G`。

**卡点**：需要"**商之商**"的等价 $(M/S)/(G/S)\cong M/G$。已探明 `Submodule.mapQ_comp` 存在（复合律 ✓），
但把 $(M/S)/(G/S)$ 与 $M/G$ **识别为同一类型**的 `LinearEquiv` 在 Mathlib 里未找到现成名字
（`quotQuotEquivQuotOfLe`、`quotientQuotientEquiv`、`quotQuotEquiv` 都**不存在**）。

**现状**：已有 `dim_TS_inter_BS_add`（加性形式，Lean ✓）；**减法形式与语义识别未 Lean 化**。
**下次尝试**：搜 `Submodule.quot*` 系列，或直接构造 `LinearEquiv`（用 `Quotient.lift` 两次）。

### 24.3 减法形式已完成（2026-10-31 深夜）

`A3sem.lean` 新增：

```lean
theorem dim_TS_inter_BS_sub (T B : Submodule K W) :
    finrank (T ⊓ B) = finrank T - finrank (Submodule.map (Submodule.mkQ B) T)
```

即 **$\dim(T\cap B)=\dim T-\dim\bigl((T+B)/B\bigr)$**——把加性形式中的"像"移到右边。
**回归 14 文件全绿** ✓

**仍未 Lean 化的语义一步**：第二项 $(T_S+B_S)/B_S$ 与 $\phi(S)=(A(S)+G)/G$ 的**同构**
（需要"商之商"的 `LinearEquiv`，Mathlib 无现成名字）。它与 §24.2 记录的是同一个卡点。

### 24.4 商之商：**仍未完成**（2026-10-31 深夜）

尝试构造 $\\Phi:((M/S)/(G/S))\\to M/G$（用两次 \texttt{liftQ}）。已解决 \texttt{mk_eq_zero} 需显式传子模；
**新卡点**：\texttt{Submodule.liftQ_apply} 与 \texttt{liftQ_apply_mk} **都不存在**（\texttt{simp} 无进展）。
草稿在 \texttt{trash/lean_scratch/Q3_quotquot_wip.lean}。

**下次**：先 \texttt{#check} 全部 \texttt{Submodule.liftQ*} 引理名，或用 \texttt{Quotient.lift} 直接构造。

### 24.5 商之商的维数：**已完成**（2026-10-31）

`A3sem.lean` 新增：

```lean
theorem finrank_quotQuot (S G : Submodule K W) (h : S ≤ G) :
    finrank ((W ⧸ S) ⧸ Submodule.map (Submodule.mkQ S) G) = finrank (W ⧸ G)
```

**证明**：不用 `LinearEquiv`（API 障碍），改用**两次秩-零化度** + `finrank_map_mkQ` + `omega` ✓
**回归 15 文件全绿** ✓

**语义链条**：`dim_TS_inter_BS_sub` 给 `dim(T_S ∩ B_S) = dim T_S − dim((T_S + B_S)/B_S)`；
而 `finrank_quotQuot`（取 M = A(S)+S+G）把 `(T_S + B_S)/B_S` 的维数与 `(A(S)+G)/G = φ(S)` 联系起来。

**仍纸面的一步**：把 `A(S)+S+G` 写成 Lean 里的项并套用 `finrank_quotQuot`（维数桥梁已 Lean，显式类型组装未做）。
