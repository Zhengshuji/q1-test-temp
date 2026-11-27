# A2：固定 $S$ 的纤维上的谱可行性（按 QA17 修订）

> **对应 docs 条目**：B.13（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

**目标**：给定可容许 $S\subseteq G=\mathcal V\cap H$，判定纤维中是否存在谱可行的 $U$。
**修订依据**：[QA17](../../archive/expert_correspondence/QA17_2026-10-31.md)。

## 1. 记号与失败条件

$W=\ker C$、$\mathcal V=\ker[C;CA]$、$H=\ker[C;L_0]$、$G=\mathcal V\cap H$、$S\subseteq G$（$s=\dim S$）、
$r=d-s$、$t=v-s$、$m=\dim(H/S)$、$k=\dim T_S$、$B_S=G/S$、$Z=S\oplus U$、$U\subseteq H/S$、$\dim U=r$。

$\pi:W\to W/S$，$P(\lambda):\mathcal V/S\to W/S$，$P(\lambda)(v+S)=\pi(Av-\lambda v)$。

**关键更正（QA17 §1）**：$U$ 活在 $H/S$ 里，而 $P$ 的像在 $W/S$ 里，所以相关的 subspace 是
$$\boxed{I_\lambda:=\operatorname{im}P(\lambda)\cap(H/S),\qquad r_\lambda:=\dim I_\lambda.}$$
谱条件失败 $\iff$
$$\boxed{\ \ker P(\lambda)\ne0\quad\text{或}\quad U\cap I_\lambda\ne0.\ }$$

## 2. 两个**普适**障碍（QA17 §1）

**障碍 A（核）**：若 $\exists\lambda,\ v\notin S$ 使 $P(\lambda)(v+S)=0$，则**任何** $U$ 失败。
*证明*：$T_\lambda(v+S)=0$ 与 $U$ 无关。**等级：[Lean]**（`A2.lean`，`Submodule.mapQ` 非单射）。
**实例**：$Ae_3=e_5,Ae_4=e_6$ ⟹ 120/120 全败。

**障碍 B（$T_S$ 相交）**：若 $\exists\lambda$ 使 $T_S\cap I_\lambda\ne0$，则**任何** $U$ 失败。
*证明*：一切容许 $U\supseteq T_S$，故 $U\cap I_\lambda\ne0$ 自动成立。**等级**：[已证-纸面]（QA17 新增）。

**注**：障碍 A 与 B 独立；任何固定 $S$ 的可行性测试都应先查这两条。

## 3. 命题 1：核障碍（[Lean]）

即 §2 障碍 A。

## 4. 命题 2：$m\ge r+t+1$ ⟹ 可行（一般 $k$，按 QA17 §2 修订）

**假设**：(i) $P(\lambda)$ 对所有 $\lambda$ 单射；(ii) $T_S\cap I_\lambda=0$ 对所有 $\lambda$；(iii) $m\ge r+t+1$。

**结论**：存在容许 $U$ 满足 $(S)$。

*证明*（商掉 $T_S$）：令 $\widetilde H=(H/S)/T_S$（$\dim m-k$）、$\widetilde U=U/T_S$（$\dim r-k$）。
由 (ii)，$I_\lambda$ 在 $\widetilde H$ 中仍为 $r_\lambda$ 维。坏集
$$\widetilde\Sigma_\lambda=\{\widetilde U:\widetilde U\cap\widetilde I_\lambda\ne0\}\subseteq\operatorname{Gr}(r-k,\,m-k)$$
的余维为
$$(m-k)-(r-k)-r_\lambda+1=m-r-r_\lambda+1\ \ge\ m-r-t+1\ \ge\ 2 .$$
$\lambda$ 是单参数族，故**坏集 Zariski 闭包的维数** $\le\dim\operatorname{Gr}-1$（QA17 §2.2：不宣称坏集本身闭，
只宣称其闭包）。于是闭包是真子集。

**实点说明（QA17 §2.2，必须写）**：实 Grassmannian 在复化中是 Zariski 稠密的，真代数子集不能包含全部实点
⟹ 存在**实**可行 $U$。$\square$

**等级**：[已证-纸面]；维数核心另有 **[Lean]**（`A2dim.lean`：$\dim U+\dim I>\dim W\Rightarrow U\cap I\ne0$）。

## 5. 命题 3：全超平面情形的精确判据（QA17 §3）

设 $k=0$、$r=1$，且**每个** $\lambda$ 的 $I_\lambda$ 都是 $H/S$ 的超平面，$I_\lambda=\ker f_\lambda$，
$f_\lambda=\sum_{j=0}^{D}\lambda^j f_j$，$L=\bigcap_{j\ge1}\ker f_j$。则
$$\boxed{\ \text{可行}\iff f_0|_L\ne0\ }$$
*证明*：$u\in L$ ⟹ $p_u(\lambda)=f_\lambda(u)\equiv f_0(u)$ 常数 ⟹ 坏 $\iff f_0(u)=0$；
$u\notin L$ ⟹ $p_u$ 非常数 ⟹ $\mathbb C$ 上有根 ⟹ 坏。$\square$

**技术前提（QA17 §3，必须补）**：需要**多项式的**定义形式 $f_\lambda$，且对每个 $\lambda$ 非零
（不能在每个 $\lambda$ 单独任选）。依据：$\mathbb C[\lambda]$ 是 PID，常数秩代数码族在 $\mathbb A^1$ 上的
annihilator 线丛自由 ⟹ 可取多项式基。**这不自动成立，须作为引理陈述。**

**等级**：[已证-纸面]（给定该引理）；代数核心 **[Lean]**（`A2root.lean`：$\mathbb C$ 上次数 $\ge1$ 的多项式有根）。

### 5.1 实例验证（`c282`，2026-10-31）

**实例**：$n=8$、$p=2$、$q=4$、$C=[e_1;e_2]$、$L_0=e_3$，
$A$：$e_3\mapsto e_1$、$e_4\mapsto e_2$、$e_5\mapsto e_5$、$e_6\mapsto e_4$、$e_7\mapsto e_6$、$e_8\mapsto e_7$。
于是 $\mathcal V=\operatorname{span}(e_5,e_6,e_7,e_8)$（$v=4$）、$h=5$、$S=\operatorname{span}(e_5)$（$s=1$）⟹
$$r=1,\ m=4,\ t=3=m-1\ ✓$$
**假设成立**：$P(\lambda)e_6=e_4-\lambda e_6$、$P(\lambda)e_7=e_6-\lambda e_7$、$P(\lambda)e_8=e_7-\lambda e_8$，
三列对一切 $\lambda$ 独立（上三角结构）⟹ $\operatorname{im}P(\lambda)\subseteq H/S$、$\dim=m-1$ ✓ **每个 $\lambda$ 都是超平面** ✓

**算出的 $f_\lambda$**（在 $H/S$ 基 $(e_4,e_6,e_7,e_8)$ 下）：
$$f_\lambda=-\lambda^3e_4^*-\lambda^2e_6^*-\lambda e_7^*-e_8^* ,$$
$$L=\bigcap_{j\ge1}\ker f_j=\operatorname{span}(e_8),\qquad f_0(e_8)=-1\ne0\ \Longrightarrow\ \textbf{可行}.$$

**独立核对（直接侧）**：对 $H/S$ 中 624 条整数直线 $u$，算 $q_u(\lambda)=\det[u\mid B(\lambda)]$，
可行 $\iff q_u$ 是非零常数：
| 结果 | 数量 |
|---|---|
| 可行 | **4**（恰为 $\operatorname{span}(e_8)$ 的 4 个整数倍数）|
| 不可行 | 620 |
| **与判据不一致** | **0** ✓ |

⟹ 命题 3 的判据在**两个方向**上都被这个实例验证（既预测对了 4 条可行线，也预测对了 620 条不可行线）。

**未覆盖**：整体"不可行"的情形（$f_0|_L=0$）需要 $f_0\in\operatorname{span}\{f_1,\dots,f_t\}$ 且 $f_\lambda$ 处处非零
——本实例没有出现，**未构造**。

## 6. 命题 4：$r=1,k=0$ 的完整分类（QA17 §4）

$d_{\max}=\max_\lambda\dim_{\mathbb P}\mathbb P(I_\lambda)$，$\dim\mathbb P(H/S)=m-1$，入射簇维数 $\le 1+d_{\max}$：

| 情形 | 结论 | 说明 |
|---|---|---|
| $d_{\max}\le m-3$ | **可行** | 坏集闭包维数 $\le m-2<m-1$ |
| $d_{\max}=m-2$，一般 $\lambda$ 给超平面，**且 $\operatorname{rank}P$ 常数** | **命题 3 判据** | 上半连续：一般维数已达最大 ⟹ 例外处不能下降 ⟹ 每个 $\lambda$ 都是超平面。**需 $\operatorname{rank}P$ 常数**——否则例外处可降到 0（QA20 反例：$P(\lambda)=[f+\lambda e_1\mid f+\lambda e_2]$，$\lambda\ne0$ 给 $\operatorname{span}(e_1-e_2)$、$\lambda=0$ 给 $0$）|
| $d_{\max}=m-2$，最大维仅在有限个 $\lambda$ | **可行** | 一般部分 $\le m-2$ + 有限个 $\le m-2$ ⟹ 并 $\le m-2$ |
| $d_{\max}=m-1$ | **不可行** | 某 $\lambda$ 有 $I_\lambda=H/S$ ⟹ 每条线都坏 |

**补充（QA17 §4）：$r=1$、$k=1$ 时 $U$ 唯一**：$T_S\subseteq U$、$\dim U=\dim T_S=1$ ⟹ $U=T_S$；
无纤维可搜，直接构造 $U=T_S$ 并做铅笔检验。

⟹ **固定 $S$ 的整个 $r=1$ 问题可判定**：$k=0$ 用命题 4，$k=1$ 直接检验。
（全局问题仍未解：$S$ 本身还在变。）

**验证**：

| 实例 | 参数 | 纤维采样 | 分类预测 |
|---|---|---|---|
| R17 | $m=3$、$d_{\max}=1=m-2$ | 196 点中 **147 可行（75%）**；坏集 = 两条线 | 可行 ✓ |
| 第二实例 | $m=2$、$d_{\max}=m-1$ | 24 点中 **0 可行** | 不可行 ✓ |

R17 手算：$\lambda\ne0$ 给点 $(-\lambda,0,1)$（线 $w_2=0$）、$\lambda=0$ 给 $\operatorname{span}(e_7,e_8)$（线 $w_1=0$）⟹ 与 49 个失败点吻合 ✓

## 7. 命题 5：一般 $r$（$k=0$）的三分（QA17 §5）

$c_\lambda=m-r-r_\lambda+1$（**$r_\lambda=\dim I_\lambda$**，QA17 §1 的更正）：

| 条件 | 结论 |
|---|---|
| 所有 $c_\lambda\ge2$ | **可行**（命题 2）|
| 某 $c_\lambda\le0$（$r+r_\lambda>m$）| **不可行**（每个 $r$-平面都与 $I_\lambda$ 相交）|
| 某 $c_\lambda=1$ | **除子情形**，未定 |

**$k\ge1$ 的推广（QA17 §7）**：商掉 $T_S$ 后余维**不变**（$m-r-r_\lambda+1$），所以三分对 $k\ge1$ 同样成立。
⟹ **固定 $S$ 的约化定理**：先排除 $T_S\cap I_\lambda\ne0$，余下是 $\dim(m-k)$ 的 Grassmannian 上、维数 $r-k$ 的
子空间问题，Schubert 余维不变。**这使 $k\ge1$ 不需要单独理论。**

## 8. 除子情形（$r\ge2$）：按 QA17 §6 重写

**8.1 多项式基的存在性（须证）**：需多项式矩阵 $B(\lambda)$，$\operatorname{im}B(\lambda)=I_\lambda$ 且
$\operatorname{rank}B(\lambda)=m-r$ 对所有 $\lambda$。依据：$\mathbb C[\lambda]$ 是 PID（常数秩代数码族 ⟹ 自由）。
**但必须先证 $I_\lambda$ 在除子区域确有常数秩、构成子丛**——不自动成立。

**8.2 首项系数的更正（QA17 §6.2）**：设 $B(\lambda)=\sum_{j=0}^{D}\lambda^j B_j$，则
$q_U(\lambda)=\det[U\mid B(\lambda)]$ 的 $\lambda^{Dr}$ 系数是 $\det[U\mid B_D]$。
**但 $B_D$ 不必满列秩**，此时 $\det[U\mid B_D]=0$ 不定义 Schubert 除子。
所以**"最高项给 Schubert 除子"需要额外假设**（例如 $\deg B=1$ 且 $B_1$ 满列秩）。
上一版把这一点写成了无条件的，**已撤回**。

**8.3 正确的表述**：
$$\text{可行}\iff\exists U:\ q_{U,0}\ne0\ \text{且}\ q_{U,j}=0\ (j=1,\dots,Dr),$$
其中 $q_{U,j}$ 是 $q_U$ 的 $\lambda^j$ 系数（$U$ 的 Plücker 坐标的多项式）。这是 Grassmannian 上的**准仿射可行性**，
给不出多项式算法，也不构成归约。

## 9. 状态清单（QA18 更正后）

| 内容 | 纸面 | Lean | 验证 |
|---|---|---|---|
| 障碍 A（核）| ✓ | ✓ `A2.lean` | 120/120 |
| 障碍 B（$T_S$ 相交）| ✓ | — | — |
| 命题 2（一般 $k$、闭包、实点）| ✓ | 维数核心 ✓ `A2dim.lean` | — |
| 命题 3（全超平面）| ✓（+ 多项式基引理）| 代数核心 ✓ `A2root.lean` | — |
| 命题 4（$r=1$ 完整）| ✓ | — | R17 75% + 第二实例 0/24 |
| 命题 5（一般 $r$ 三分）| ✓ | — | — |
| **引理 10.1'**（多项式基，双常数假设）| ✓ | — | 反例见 §10.2 |
| **次数界** | **未证** | — | — |
| 一般/例外判据（§10.4）| ✓ | — | — |
| Plücker 线性性（§11.1）| ✓ | — | — |
| 维数充分条件 | **已撤回**（§11.2）| — | — |
| 共同补空间对偶 | ✓（两处已更正，§11.3）| — | — |
| 除子情形判定 | **开放** | — | — |

**Lean**：`A2.lean`、`A2dim.lean`、`A2root.lean` 退出码均 0；回归 `tools/lean/check_lean.sh` 覆盖 9 个文件。

## 10. A2.3：多项式基（**更正版**）

### 10.1 定理（正确形式）

**引理 10.1'**：设
$$\operatorname{rank}P(\lambda)=\rho\ \ \forall\lambda,\qquad \dim I_\lambda=d\ \ \forall\lambda .$$
则存在多项式矩阵 $B(\lambda)$，使 $\operatorname{im}B(\lambda)=I_\lambda$ 且 $\operatorname{rank}B(\lambda)=d$ 对一切 $\lambda$ 成立。

*证明（QA20 §2 给出的干净论证）*：令 $E_\lambda=\operatorname{im}P(\lambda)$。由 $\operatorname{rank}P$ 常数，
$\{E_\lambda\}$ 是平凡丛 $W\times\mathbb A^1$ 的秩 $\rho$ 代数子丛 $E$。考虑丛映射
$$\phi:E\longrightarrow (W/H)\times\mathbb A^1 .$$
其纤维核 $\ker\phi_\lambda=E_\lambda\cap H=I_\lambda$。由 $\dim I_\lambda\equiv d$ 常数，$\phi$ **秩恒定**，故 $\ker\phi$ 是代数子丛。
于是 $\{I_\lambda\}$ 是子丛；其整体截面模 $\Gamma(\mathbb A^1,I)$ 是有限生成投射 $\mathbb C[\lambda]$-模，
$\mathbb C[\lambda]$ 是 PID 故**自由**；取一组基，它在每个纤维上仍是基 ✓ $\square$

**关键细节**：核是子丛是因为 $\phi$ **秩恒定**（不是"交维数恒定"直接给出）——这一点必须写在论文里。

### 10.2 **两个**常数性假设都是必要的（反例）

**反例**（QA18 §2）：$\mathcal W=\operatorname{span}(e_1,e_2,f)$、$H=\operatorname{span}(e_1,e_2)$、$P(\lambda)=[e_1+\lambda f\mid\lambda e_2]$。
- $\lambda\ne0$：$\operatorname{im}P=\operatorname{span}(e_1+\lambda f,e_2)$ ⟹ $I_\lambda=\operatorname{span}(e_2)$；
- $\lambda=0$：$\operatorname{im}P(0)=\operatorname{span}(e_1)$ ⟹ $I_0=\operatorname{span}(e_1)$。

$\dim I_\lambda\equiv1$ **但子空间在 $0$ 处跳变** ⟹ 无多项式基（$e_1,f$ 坐标须恒零，而 $b(0)$ 须在 $I_0=\operatorname{span}(e_1)$ 里）。

**注**：此例中 $\operatorname{rank}P$ 也从 2 跳到 1 ⟹ 正是"$\operatorname{rank}P$ 常数"这个额外假设排除的情形。
R17 则是另一类跳变：$\operatorname{rank}P\equiv2$ 但 $\dim I_\lambda$ 跳（1→2）⟹ 需要"$\dim I_\lambda$ 常数"这个假设。

**⟹ 两个假设互相独立，缺一不可。**

### 10.3 次数界：**未证明**

Smith 标准形只给"存在"，**不控制次數**：幺模变换的次数不受原矩阵次数约束。
反例（QA18 §3）：$M(\lambda)=\begin{pmatrix}1&0&\lambda^D\\0&\lambda^D&1\end{pmatrix}$ 常数秩 2，核基次数 $2D$ 而非 $D$。

**⟹ 复杂度估计里不得使用任何次数界**；如需，必须用极小基/Forney 指标单独证明。
R17 的实际次数是 1（$B=e_8-\lambda e_4$），只能说明"可能很小"，不能定界。

### 10.4 一般/例外的正确判据（QA18 §4）

设一般 $\lambda$ 上的 $I_\lambda$ 有 $d=m-r$ 维（除子情形的常数秩区），$\Omega=\mathbb C\setminus E$（$E$ 有限）。

$$\boxed{\ \text{可行}\iff\exists U:\ q_U(\lambda)\ne0\ \forall\lambda\in\Omega,\ \text{且}\ U\cap I_{\lambda_j}=0\ (\lambda_j\in E)\ }$$

两个要点：
1. **一般基不必特化到例外纤维**（§10.2 的反例：$B(\lambda)=e_2$ 但 $I_0=\operatorname{span}(e_1)$）；
2. **一般条件不是"$q_U$ 为常数"**，而是"在 $\Omega$ 上非零"（$q_U(\lambda)=\lambda$ 即反例）。

只有当基**满秩延拓到整条仿射线**时，才退化为"$q_U$ 是非零常数"。

---

## 11. A2.4：除子情形（**更正版**）

### 11.1 Plücker 线性性（**成立**）

$q_U(\lambda)=\det[U\mid B(\lambda)]=\sum_j\lambda^jq_{U,j}$，且每个 $q_{U,j}$ 是 $U$ 的 Plücker 坐标的**线性泛函**
（$\det[U\mid\cdot]$ 多线性、换基乘 $\det g$，而 Plücker 坐标正是这类函数的基）。

⟹ 常数秩区的可行条件是
$$\exists\,p\in\operatorname{Gr}(r,m):\ q_{j}(p)=0\ (j\ge1),\ q_0(p)\ne0,$$
即**线性空间与 Grassmannian 的交**，且避开超平面 $\{q_0=0\}$。

### 11.2 维数计数为什么**不可能**给出充分条件（第一项，已解决）

**精确定理**：在常数秩除子情形下，$q_U(\lambda)=\det[U\mid B(\lambda)]$，$U\in L:=\{q_j=0\ (j\ge1)\}$，且
$$U\in L\ \text{时}\ q_U\equiv q_0(U).$$
于是

$$\boxed{\ \text{可行}\iff\exists U\in\operatorname{Gr}\cap L:\ q_0(U)\ne0\iff \operatorname{Gr}\cap L\not\subseteq\{q_0=0\}\ }$$

（两种情况：$q_0(U)\ne0$ ⟹ $q_U$ 非零常数 ⟹ 可行；$q_0(U)=0$ ⟹ $q_U\equiv0$ ⟹ 对所有 $\lambda$ 坏。）

**关键观察**：$\operatorname{Gr}\cap L\subseteq\{q_0=0\}$ **是真实可能的情形**，不是"测度为零的例外"——
它恰好等价于"所有'常体积互补'的 $U$ 都对某个 $\lambda$ 坏"，而这正是不可行。
所以

$$\boxed{\ \text{维数比较 } \dim(\operatorname{Gr}\cap L)>\dim(\operatorname{Gr}\cap L\cap\{q_0=0\})\ \text{一般**不成立**}\ }$$

**⟹ 上一版的"$E<r(m-r)$ ⟹ 可行"是错的，且不可能修补**：$E<r(m-r)$ 只保证 $\operatorname{Gr}\cap L\ne\varnothing$，
而这些点可能**全部**落在 $\{q_0=0\}$ 里。

**正确的充分条件（几条）**：
1. **无方程情形**：若 $q_j\equiv0$（$j\ge1$，即 $I_\lambda=I_0$ 常数），则 $L$ 是整个 Plücker 空间，
   取一般 $U$（$\dim r$）即可避开固定的 $(m-r)$ 维 $I_0$ ⟹ **可行** ✓
2. **显式构造**：任何给出 $U\in\operatorname{Gr}\cap L$ 且 $q_0(U)\ne0$ 的构造都直接给出可行性（R17 的 $u$ 即如此）。

**结论**：第一项（维数计数）的答案是**否定的**——不是"证明不够"，而是**原理上不可能**；
正确的产物是 §11.2 开头的**精确判据**，它已经不是"充分条件"而是等价刻画。

### 11.2b $r=1$ 的**多项式提升判据**（QA20，取代上版两个"常值"判据）

设 $J_\lambda=[v(\lambda)]\subseteq K^*$，其中 $v(\lambda)=\sum_{j=0}^{D}\lambda^jv_j$ 是**处处非零的多项式提升**
（$\mathbb P^{m-1}$ 的 tautological 线丛在 $\mathbb A^1$ 上平凡）。超平面 $\ell$ 避开**实际像** $\iff$
$$\ell(v(\lambda))\ne0\ \ \forall\lambda\in\mathbb C\iff \ell(v_0)+\cdots+\lambda^D\ell(v_D)\ \text{无根}\iff \ell(v_j)=0\ (j\ge1),\ \ell(v_0)\ne0 .$$
这样的 $\ell$ 存在 $\iff v_0\notin\operatorname{span}\{v_1,\dots,v_D\}$。于是

$$\boxed{\ \text{可行}\iff v_0\notin\operatorname{span}\{v_1,\dots,v_D\}\ }$$

**撤回（QA20 §1.1）**：上一版写"$m=2,3$ 时可行 $\iff J_\lambda$ 常值"——**这是错的**。
反例：$m=2$、$J_\lambda=\operatorname{span}(e_1+\lambda e_2)$ 非常值，但 $W=\operatorname{span}(e_2)$ 避开一切有限 $\lambda$ 的 $J_\lambda$ ⟹ 可行。
**错误根源**：把**射影闭包**上的交点当成了**实际像**上的点（$[e_2]$ 属于闭包但从不被取到）。

**检验新判据**：
- $v=e_1+\lambda e_2$：$v_0=e_1\notin\operatorname{span}(e_2)$ ⟹ 可行 ✓（与反例一致）
- $v=\lambda^2(e_1+e_2)+\lambda e_1+e_2$：$v_0=e_2\in\operatorname{span}\{e_1,e_1+e_2\}$ ⟹ **不可行**（每个超平面都相交）
- $m=3$、$v(\lambda)=(1,\lambda,\lambda^2)$：$v_0=(1,0,0)\notin\operatorname{span}\{(0,1,0),(0,0,1)\}$ ⟹ 可行 ✓（$x=0$ 只与闭包交于 $[0:0:1]$，不被取到）

**注意**：判据依赖 $v$ 的**系数向量**，不是曲线的次数——所以没有"次数 $\ge m-1$ 就必相交"这种阈值。

### 11.3 共同补空间对偶（**更正两处**）

$W=U^\perp$、$J_\lambda=I_\lambda^\perp$，则 $U\cap I_\lambda=0\iff W+J_\lambda=(H/S)^*$（✓ 等价正确）。

- **充分条件**：若 $\dim E\le r$（$E=\operatorname{span}_\lambda J_\lambda$），把 $E$ 扩成 $r$ 维 $E'$，
  取 $W$ 为 $E'$ 的 $(m-r)$ 维补 ⟹ $W\cap J_\lambda=0$ ⟹ $W+J_\lambda=K^*$ ✓
  （**上一版写的 $\dim E\le m-r$ 是错的**）
- **不可能端点**：$J_\lambda=K^*$ 时条件**自动成立**；真正不可能的是 $J_\lambda=0$（即 $I_\lambda=H/S$）✓
  （**上一版写反了**）

### 11.4 R17 的精确坏集（**更正**）

$I_\lambda=\operatorname{span}(e_8-\lambda e_4)$（$\lambda\ne0$）、$I_0=\operatorname{span}(e_7,e_8)$。
$u\propto(-\lambda,0,1)$ 要求 $w_2=0$ **且 $w_3\ne0$**，故 $\mathbb P(H/S)$ 上的精确坏集是
$$\{w_2=0,\ w_3\ne0\}\ \cup\ \{w_1=0\}.$$
**不是**两条完整的线。$U=\mathbb Ce_4$（$w=(1,0,0)$）谱上可行，但**不在纤维里**（$U\cap B_S\ne0$，$B_S=\operatorname{span}(e_4)$）；
196 点实验只采纤维内点（$(w_2,w_3)\ne(0,0)$），故 75% 不变 ✓

### 11.5 结论

除子情形**仍然是开放的**：Plücker 线性化是正确的，但
(a) 维数计数不足；(b) 共同补空间的判据只有两个特例；(c) 一般基/例外纤维的衔接未解。

---

## 12. 更正汇总（QA18，2026-10-31 下午）

专家的审阅发现了五处错误，本文档以下各节**以此为准**。

### 12.1 引理 10.1 **是错的**（反例）

**反例**（QA18 §2）：$\mathcal W=\operatorname{span}(e_1,e_2,f)$、$H=\operatorname{span}(e_1,e_2)$、$P(\lambda)=[e_1+\lambda f\mid\lambda e_2]$。
- $\lambda\ne0$：$\operatorname{im}P=\operatorname{span}(e_1+\lambda f,e_2)$ ⟹ $I_\lambda=\operatorname{span}(e_2)$；
- $\lambda=0$：$\operatorname{im}P(0)=\operatorname{span}(e_1)$ ⟹ $I_0=\operatorname{span}(e_1)$。

**$\dim I_\lambda\equiv1$ 但子空间在 $0$ 处跳变** ⟹ 不存在多项式基（$e_1,f$ 坐标必须恒零，但 $b(0)\in\operatorname{span}(e_2)\ne I_0$）。

**修正后的引理 10.1'**：需**两个**假设——$\operatorname{rank}P(\lambda)=\rho$ 常数 **且** $\dim I_\lambda=d$ 常数。
此时 $\operatorname{im}P$ 是秩 $\rho$ 代数子丛，与固定 $H/S$ 的常维交是秩 $d$ 子丛 ⟹ 截面模有限生成投射 ⟹ 自由（PID）⟹ 多项式基。$\square$

### 12.2 引理 10.2 的**次数界未证明**

- **10.2(a) 存在性**：可修（12.1' 的假设下）✓
- **10.2(b) 次数界 $\le\rho d(m-r)$**：**未证明**。Smith 标准形的幺模变换次数不由原矩阵次数控制。
  反例（QA18 §3）：$M(\lambda)=\begin{pmatrix}1&0&\lambda^D\\0&\lambda^D&1\end{pmatrix}$ 常数秩 2，核基次数 $2D$ 而非 $D$。

**结论**：在复杂度估计里**不得**使用该界；需要极小基/Forney 指标理论单独证明。

### 12.3 §10.2 的"一般/例外"判据**不完整**

两个问题：
1. **一般基不必特化到例外纤维**（12.1 的反例：$B(\lambda)=e_2$ 但 $I_0=\operatorname{span}(e_1)$）；
2. **一般条件不是"$q_U$ 为常数"**，而是 $q_U(\lambda)\ne0$ 对 $\lambda\in\Omega=\mathbb C\setminus E$。
   例如 $q_U(\lambda)=\lambda$ 在 $\Omega$ 上非零但不是常数。

**正确形式**：
$$\text{可行}\iff\exists U:\ q_U\ne0\ \text{于}\ \Omega\ \text{上},\ \text{且}\ U\cap I_{\lambda_j}=0\ (j=1,\dots,s).$$
只有当初值基**满秩延拓到整条仿射线**时，才能退化为"$q_U$ 是非零常数"。

### 12.4 §11.2 的维数充分条件**不成立**

$E<r(m-r)$ 只保证 $\mathcal L\cap\operatorname{Gr}\ne\varnothing$，**不保证**交不在超平面 $\{c_0=0\}$ 内。
需要证明 $\mathcal L\cap\operatorname{Gr}\not\subseteq\{c_0=0\}$（比较两个交的维数）——**该不等式未证**。
**§11.2 的充分条件已撤回。**

### 12.5 §11.4 对偶形式的**两处错误**

1. **充分条件错**：应为 $\boxed{\dim E\le r}$（$E=\operatorname{span}_\lambda J_\lambda$），不是 $\dim E\le m-r$。
   证明：若 $\dim E\le r$，把 $E$ 扩成 $r$ 维 $E'$，取 $W$ 为 $E'$ 的 $(m-r)$ 维补 ⟹ $W\cap J_\lambda=0$ ✓
2. **不可能端点反了**：$J_\lambda=K^*$ 时 $W+J_\lambda=K^*$ **自动成立**；真正不可能的是 $J_\lambda=0$
   （即 $I_\lambda=H/S$）——此时 $W+0=W\ne K^*$ ✓

### 12.6 §11.3 的 R17 坏集**需精确化**

$I_\lambda=\operatorname{span}(e_8-\lambda e_4)$ 要求 $u\propto(-\lambda,0,1)$，即 $w_2=0$ **且 $w_3\ne0$**。
所以 $\mathbb P(H/S)$ 上的精确坏集是
$$\{w_2=0,\ w_3\ne0\}\ \cup\ \{w_1=0\},$$
**不是**两条完整的线。$U=\mathbb Ce_4$（$w=(1,0,0)$）谱上可行，但它**不在纤维里**
（$U\cap B_S\ne0$，$B_S=\operatorname{span}(e_4)$）——所以 196 点实验（只采纤维内点，$(w_2,w_3)\ne(0,0)$）不受影响，
75% 的数字不变 ✓。但"两条完整线"的说法**已更正**。

### 12.7 优先级（QA18 §9）

1. **先更正 A2.3/A2.4 的陈述**（本节）；
2. **转 A3**（基族 $\mathcal B_{s,k}$ 与 $S$ 的选择）；
3. 除子情形作为**并行**开放问题，不作为 A3 的前提。

### 11.2c 推广：$r=1$、$m=3$ 的完整答案

$J_\lambda$ 是 $\mathbb P^2$ 中的点，$W$ 是直线（$\dim m-r=2$）。需要一条**避开所有** $J_\lambda$ 的直线。
$\lambda\mapsto J_\lambda$ 是平面有理曲线 $C$。

- $C$ 的次数 $\ge1$：任何直线与 $C$ 相交（$\mathbb C$ 上代数闭，次数 $d$ 的曲线与直线交 $d$ 点，计重数）⟹ **不可行**；
- $C$ 退化为一点（常数）：取不过该点的直线 ⟹ **可行**。

$$\boxed{\ r=1,\ m=3:\quad \text{可行}\iff J_\lambda\ \text{为常值}\iff I_\lambda\ \text{为常值}\ }$$

**与 $m=2$ 的对照**：两个情形给出**同一个**判据（常值 ⟺ 可行），
说明 $r=1$ 的一维情形可能是统一现象：**只要谱族真的在动，就总能被"扫到"**。

**$m\ge4$、$r=1$ 的情形**：$W$ 是超平面；只有当曲线 $C$ 与**每一个**超平面都相交时才不可行
（例如 $C$ 是"处处非退化"的曲线且 $m-1=2$ 即 $m=3$；$m\ge4$ 时存在避开曲线的超平面，多数情形可行）。
**该情形未完全解决**。

## 13. R17 的显式左逆证书（QA19 §2.2，已完成）

两个例子的 $X(\lambda)T_\lambda=I_t$ 均**精确成立**（系数逐项检验，[c268](../layer_program/c268_left_inverse_cert.py)）。

### 例 1（$t=2$）

$S=\operatorname{span}(e_5,e_6)$、$U=\operatorname{span}(e_4+e_7)$；$W/S$ 基 $(e_3,e_4,e_7,e_8)$、$Z/S=\operatorname{span}(e_4+e_7)$，
$W/Z$ 基 $(e_3,e_4,e_8)$：

$$T_\lambda=\begin{pmatrix}-\lambda&0\\-1&-\lambda\\0&1\end{pmatrix},\qquad
X(\lambda)=\begin{pmatrix}0&-1&-\lambda\\0&0&1\end{pmatrix},\qquad \deg X=1=t-1\ \checkmark$$

### 例 2（$t=1$）

$S=\operatorname{span}(e_4,e_5,e_6)$、$Z/S=\operatorname{span}(e_8)$；$W/S$ 基 $(e_3,e_7,e_8)$、$W/Z$ 基 $(e_3,e_7)$：

$$T_\lambda=\begin{pmatrix}-\lambda\\1\end{pmatrix},\qquad X=(0\ \ 1),\qquad \deg X=0\le t-1\ \checkmark$$

（**常数左逆**即可，正如专家预测。）

### 为什么这比 gcd 检验强

- gcd 检验是"某项为 1"的**间接**判据；左逆证书是**直接的恒等式** $X(\lambda)T_\lambda=I_t$；
- 证书只含 $tq\cdot t$ 个系数变量（例 1：$2\cdot3\cdot2=12$ 个），可直接代入验证；
- 次数是**构造出来的**（$\deg X=1$），不是事后估的。

### 11.2b′ 从 $P(\lambda)$、$I_\lambda$ 直接推出提升判据（QA20 §11 要求）

**关键观察**：$r=1$ 的除子情形下 $I_\lambda$ 是 $H/S$ 的**超平面**，故
$$J_\lambda=I_\lambda^\perp=(\ker f_\lambda)^\perp=\operatorname{span}(f_\lambda),$$
即**提升 $v(\lambda)$ 就是定义形式 $f_\lambda$ 本身**——专家的"多项式提升"与命题 3 的 $f_\lambda$ 是**同一个对象**。

**推导链**（$r=1$、常数秩）：

1. $I_\lambda=\operatorname{im}P(\lambda)\cap(H/S)$ 为超平面（$\dim I_\lambda\equiv m-1$）；
2. 由引理 10.1' 的同一论证，$\{I_\lambda\}$ 是超平面子丛 ⟹ 其 annihilator 线丛平凡 ⟹ 存在**多项式** $f_\lambda=\sum_j\lambda^j f_j$，
   $f_\lambda\ne0$ 对一切 $\lambda$，且 $I_\lambda=\ker f_\lambda$；
3. **可行** $\iff\exists u\in H/S:\ f_\lambda(u)\ne0\ \forall\lambda$
   $\iff\exists u:\ \sum_j\lambda^j f_j(u)$ **无根**
   $\iff\exists u:\ f_j(u)=0\ (j\ge1),\ f_0(u)\ne0$
   $\iff f_0\notin\operatorname{span}\{f_1,\dots,f_D\}$（对偶/Farkas：在 $\bigcap_{j\ge1}\ker f_j$ 上为零的泛函恰是 $\operatorname{span}\{f_j\}$）；
4. 而 $f_j$ 就是提升 $v$ 的系数，故第 3 步等价于专家的 $v_0\notin\operatorname{span}\{v_1,\dots,v_D\}$ ✓

$$\boxed{\ \text{命题 3 的判据（$\exists u$，对偶形式）}\ =\ \text{专家的提升判据（$\exists\ell$，原形式）}\ }$$

**这解决了 G.4**：判据对**所有 $m$** 成立（不只 $m=2,3$），且不需要次数阈值。

**例外秩**：若 $\operatorname{rank}P$ 在有限个 $\lambda_j$ 处跳变，则 $f_\lambda$ 可能在 $\lambda_j$ 处退化；
此时须按 §10.4 分段：一般部分用提升判据，例外值单独加 $U\cap I_{\lambda_j}=0$ 的 Schubert 条件。
**该分段形式未完全机械化**（诚实标注）。

## 14. 验证缺口清单（诚实版，2026-10-31）

| 内容 | 纸面 | Lean | 实例 | 缺口 |
|---|---|---|---|---|
| 障碍 A、B | ✓ | A ✓ | 120/120 | — |
| 命题 2（维数核心）| ✓ | ✓ | — | 参数非空假设需写进陈述 |
| 命题 3 代数步骤 | ✓ | ✓ | — | **"多项式族存在"未验证** |
| 命题 4 四分类 | ✓ | ✗ | 两实例 | 需射影维数理论；第 2 行需 $\operatorname{rank}P$ 常数 |
| 引理 10.1' | ✓ | ✗ | — | 子丛论证（专家给）未形式化 |
| **提升判据（§11.2b′）** | ✓ | ✗ | **无** | **尚未在任何实例上检验** |
| R17 左逆证书 | ✓ | ✓ | ✓ | — |

**最紧的缺口**：§11.2b′ 的提升判据**没有任何实例检验**——它刚推出，而此前连续三次错误（§4.1、§8、B.5）
都是"推导看起来对、没有实例核对"造成的。

**已找到的可检验实例**：随机搜索 400 个实例，得到 **2 个**处于"全超平面"区（$m=2$、$\dim I_\lambda\equiv1=m-1$）的候选
（$n=5,p=1$ 与 $n=6,p=1$）——可用于下一步的实例检验。

### 11.2b″ 提升判据的抽象验证（两个方向，2026-10-31）

在抽象层面（$K=\mathbb C^2$、$I_\lambda$ 为超平面、$f_\lambda$ 为其定义形式）已验证判据**双向**成立：

| 例子 | $f_\lambda$ | $f_0\in\operatorname{span}\{f_j\}$ | 判据 | 暴力枚举 $U$ |
|---|---|---|---|---|
| $L_\eta$ 块：$I_\lambda=\operatorname{span}(\lambda,1)$ | $(-1,\lambda)$ | 否 | **可行** | 找到可行 $U$（如 $(-3,0)$、$(-3,1)$）✓ |
| 专家反例：$v=\lambda^2(e_1+e_2)+\lambda e_1+e_2$ | $(\lambda^2+\lambda,\lambda^2+1)$ | 是 | **不可行** | 每个 $u\ne0$ 都有根（$u_1+u_2\ne0$ 时二次有根；$=0$ 时根 $\lambda=1$）✓ |

**⟹ 判据在抽象层面正确**（两个方向都与暴力一致）。

**观察者问题上的实例仍缺**，且有**结构性原因**：
- 若 $\mathcal V/S$ 与目标空间**同维**（方铅笔），首项可逆 ⟹ 在 $\mathbb C$ 上必有特征值 ⟹ 秩**必掉** ⟹ 不可能恒为 $m-1$；
- 所以要落在全超平面区，铅笔必须是**真正矩形的**（有 $L_\eta$ 型奇异块）；
- 这类实例在随机搜索的 $n\le7$、$p\le2$ 范围内**没有出现**（1500 次试验）。

**结论**：判据的验证 =（i）抽象双向验证 ✓；(ii) 代数核 Lean ✓；(iii) 观察者问题的实例 ✗（需针对性的矩形铅笔构造）。

### 11.2b‴ 矩形铅笔实例与判据的**必要修正**（$B_S$ 约束）

**实例**（$n=6$、$p=2$、$r=1$、矩形铅笔，2026-10-31 构造）：
$C=[e_1;e_2]$、$A$ 的行 $(e_3,e_4,0,e_6,\text{(row5)}=e_5,0)$（具体矩阵见 [c272](../layer_program/c272_rect_pencil.py)）、$L_0=e_3$。

$$\mathcal V=\operatorname{span}(e_5,e_6),\quad H=\operatorname{span}(e_4,e_5,e_6),\quad S=\operatorname{span}(e_5),\quad K=H/S=\operatorname{span}(e_4,e_6)$$
$$P(\lambda)e_6=e_4-\lambda e_6\ \Longrightarrow\ I_\lambda=\operatorname{span}(e_4-\lambda e_6)\ (\dim\equiv1=m-1)\ \checkmark$$

**结果**：42 个 $(A)$-可行的 $U$，**全部失败**（$(S)$ 成立 0 个）⟹ **不可行**。

**但判据（不带 $B_S$ 约束）会给出"可行"**：$f_\lambda=(\lambda,1)$，取 $u=(0,1)$ 即 $e_6$ 有 $f_\lambda(e_6)=1\ne0$ 对一切 $\lambda$ ✓
——**然而 $e_6\in B_S=G/S=\mathcal V/S$**，而纤维要求 $U\cap B_S=0$ ⟹ $u=e_6$ **不可用**。

$$\boxed{\ \text{正确判据必须加上 } u\notin B_S:\quad \text{可行}\iff\exists u\in K\setminus B_S,\ f_\lambda(u)\ne0\ \forall\lambda\ }$$

**这解释了此前随机搜索为何找不到实例**：全超平面区需要矩形铅笔（$p\ge2$、$r_1=2p$），而这类实例里 $B_S$ 恰好"堵住"了唯一可行的方向。

**对 G4 的意义**：判据的正确形式是**带 $B_S$ 约束的版本**；专家给的版本（共同补空间问题）缺这一条。
该实例同时说明**两件事**：(i) 矩形铅笔区可以实现；(ii) $B_S$ 约束可以翻转结论。

### 11.2b⁗ 可行性要求 $K/B_S$ 有"余地"（$\dim(H/G)\ge2$）

在上述矩形铅笔实例里，$S=\operatorname{span}(e_5+c e_6)$ 的所有变体都给
$$I_\lambda=\operatorname{span}(e_4-\lambda e_6'),\qquad B_S=\mathcal V/S=\operatorname{span}(e_6'),$$
即 $I_\lambda$ **扫过 $K$ 中除 $B_S$ 外的所有直线**——而"好方向"恰是 $B_S$ ⟹ 无 $u$ 可用 ⟹ 不可行。

**一般观察**：$U$ 必须满足 $U\cap B_S=0$，故真正起作用的是商空间 $K/B_S\cong H/G$。于是

$$\boxed{\ \text{在 }\dim(H/G)=1\text{ 时，}I_\lambda\text{ 只要动起来就扫满，必不可行；}\\ \text{要可行必须有 }\dim(H/G)\ge2\ }$$

而 $\dim(H/G)\le p$（专家 QA17 的 $k\le p$ 同源）⟹ **$p\ge2$ 且 $b\le h-2$ 才能有可行的全超平面实例**。

**这解释了为什么随机搜索（$p\le2$、且多取 $b=h-1$）几乎必然失败**——绝大多数候选的 $\dim(H/G)=1$。

**下一步的构造目标**：$\dim(H/G)=2$（即 $h-b=2$）、$r=1$、$m=3$ 的矩形铅笔实例。

### 11.2b⁘ 全超平面区与 $(A)$-可容许**可能互斥**（实验证据，含警告）

随机搜索（$n\in\{7,8\}$、$p\in\{2,3\}$、2000 次尝试，[c275](../layer_program/c275_search_positive.py)）：

| 统计 | 数量 |
|---|---|
| 落在全超平面区（$\dim I_\lambda\equiv m-1$）| **1006** |
| 其中纤维非空（40 次随机 $U$ 命中 $(A)$）| **0** |

**解释**：$1006$ 个全超平面实例、每个采样 40 个 $U$，**一个都没命中 $(A)$**。

**但必须警告**（CLAUDE §10.1 禁区"薄集不许采样"）：$(A)$ 是**闭条件**，纤维可能是**薄集**，
随机 $U$ 必然错过。所以这 1006/0 **不能**证明互斥，只能说"没有明显的大纤维"。

**若要定论**，必须用**代数判据**（而非采样）判定纤维非空：
$$\exists U:\ \operatorname{rank}[Z,AZR_Z]=d\ \ \text{且}\ \dim I_\lambda\equiv m-1 .$$
这正是 §5 的"命题 2 参数非空条件"的定量版本，目前**没有**实现。

**对 G4 的影响**：若互斥成立，则 G4 的判据在观察者问题里**无实例可陈述**（空真）；
若不成立，则需要构造性的纤维非空判定来找实例。**两种情况都值得知道**，但都需要先有代数判据。

### 11.2b⁙ G4 的**正向实例**（已拿到，2026-10-31）

**关键更正**：$(A)\iff T_S\subseteq U$ 是**线性条件**（核心引理），纤维非空应由**代数条件**
$$T_S\cap B_S=0,\qquad r-k\le(m-k)-\dim(B_S/T_S)$$
判定，**不能**靠随机采样 $U$（上一轮的 1006/0 就是采样造成的假象）。

**修正后**随机搜索（$n\in\{7,8\}$、$p\in\{2,3\}$，[c276](../layer_program/c276_fiber_linear.py)）立即命中：

| trial | $n$ | $p$ | $b$ | $s$ | $m$ | $t$ | $k$ | $\dim I_\lambda$ | $(A)$ | $(S)$ |
|---|---|---|---|---|---|---|---|---|---|---|
| 5 | 7 | 2 | 2 | 1 | 3 | 2 | 1 | **2 = m−1** | ✓ | **✓** |
| 6 | 7 | 2 | 2 | 1 | 3 | 2 | 1 | 2 | ✓ | **✓** |
| 10 | 7 | 2 | 2 | 1 | 3 | 2 | 1 | 2 | ✓ | **✓** |

**意义**：
1. **全超平面区在观察者问题里确实可达且可容许**（推翻上一轮"可能互斥"的猜测）；
2. $k=r=1$ 时 $U=T_S$ 唯一，$(A)$ 自动成立、$(S)$ 直接可验 ✓；
3. 这给出 G4 判据**正向**的实例基础（判据预测可行，实际可行 ✓）。

**教训**：上一轮"1006/0"完全是我自己的采样错误（把线性条件当稀有事件去采样）——正是 CLAUDE §10.1 的禁区。

## 15. G3 的第一步：线性截面的张成（实验）

G3 的判据（专家改述）是：可行 $\iff q_0\notin I(X)_1$，$X=\operatorname{Gr}(r,m)\cap L$。
若 $\operatorname{span}(X)=L$，则 $I(X)_1=L^\perp=\operatorname{span}\{c_j\}$，判据退化为**线性代数**：
$$\text{可行}\iff q_0\notin\operatorname{span}\{c_1,\dots,c_D\}.$$

**实验**（$m=4$、$r=2$，$\operatorname{Gr}(2,4)\subset\mathbb P^5$，随机整数 2-平面采样）：

| 线性条件数 | $L$ 的维数 | 采样点数 | $\operatorname{span}(X)$ 的维数 |
|---|---|---|---|
| 1 | 5 | 1193 | **5** = dim L ✓ |
| 2 | 4 | 97 | **4** = dim L ✓ |
| 3 | 3 | **0** | — |
| 4 | 2 | **0** | — |
| 5 | 1 | **0** | — |

**结论**：
1. **余维 1、2 的截面非退化**（张成整个 $L$）⟹ 判据是线性代数 ✓；
2. **余维 $\ge3$ 的截面是薄集**（曲线/点），随机采样**必然**找不到点——这与 CLAUDE §10.1 的禁区一致；
3. 薄集情形需要**代数方法**（解理想的零点），而那里正是判据可能退化的地方。

**对 G3 的推断**：除子情形的判据在"截面非退化"时就是 $q_0\notin\operatorname{span}\{c_j\}$（可判）；
退化情形需要单独处理，且它对应**薄**的参数集——这可能正是 $q1$ 难度的来源，但目前**没有**定论。

## 16. G3 的第二步：判据的适用域

**观察**：$X=\operatorname{Gr}\cap L$，$L$ 由 $c_1,\dots,c_E$ 切出（$E\le Dr$）。若 $\operatorname{span}(X)=L$，则
$$\text{可行}\iff q_0\notin\operatorname{span}\{c_1,\dots,c_E\}\quad(\text{线性代数})✓$$
若 $\operatorname{span}(X)\subsetneq L$，则 $q_0$ 可能在 $\operatorname{span}(X)$ 上为零而不在 $L$ 上 ⟹ 判据需代数方法。

**何时非退化**：
- **维数计数**：$E<\dim\operatorname{Gr}=r(m-r)$ 时 $X$ 正维，一般情形下 $\operatorname{span}(X)=L$（线性截面的经典性质）；
- **R17 型**（$D=1$、$m-r=2$）：$E=r=1<2$ ✓ 非退化 ⟹ 线性判据 ✓ 与 R17 的超平面分析一致；
- **退化只发生在 $E\ge\dim\operatorname{Gr}$**，即 $D\ge m-r$——这是**薄参数区**。

$$\boxed{\ \text{G3 的判据在 } D<m-r \text{ 时是线性代数（可判）；退化情形 } D\ge m-r \text{ 未解}\ }$$

**现状**：这是 A2 剩下的唯一开放点，而且它已从"除子情形一般 $r$"缩小到"**退化线性截面**"这一薄集。

---

## 17. QA21 带来的三条新结果（2026-10-31 晚）

### 17.1 定理（专家的新几何结果）：$\mathbb P^1$ 上非平凡曲线**没有**共同补空间

设 $V$ 是 $m$ 维复向量空间，$f:\mathbb P^1\to\operatorname{Gr}(r,V)$ 是**非常值**态射。则不存在固定的
$(m-r)$ 维子空间 $W$ 使 $V=f(t)\oplus W$ 对**所有** $t\in\mathbb P^1$。

*证明*（专家给，QA21 §4.3）：令 $\mathcal E\subset V\otimes\mathcal O_{\mathbb P^1}$ 是 tautological 秩 $r$ 丛的拉回，
$\rho:V\to V/W$。则 $\rho|_{\mathcal E}$ 的行列式给岀截面
$$s_W\in H^0\big(\mathbb P^1,\det(\mathcal E)^*\big),$$
且 $s_W(t)\ne0\iff V=f(t)\oplus W$。因 $f$ 非常值，$\deg\det(\mathcal E)^*>0$；正次数线丛上的非零截面必有零点。$\square$

**对本项目的意义**：我们真正的族是 $\mathbb A^1$ 上的（缺少 $\lambda=\infty$）。
所以在 $\mathbb A^1$ 上共同补空间**可以存在**——当且仅当行列式截面的所有零点都落在**被略去的** $\lambda=\infty$ 处，
即"行列式多项式是非零常数"。**这正是命题 3 的判据**，现在有了函子式的几何解释。

**限定**：要求 $f$ 是到**固定** Grassmannian 的态射；若原铅笔的秩跳变，须先处理一般族与例外值（A2 已做）。

### 17.2 $k=s=r$ 时代数可容许性**自动**

$k=s=r$ ⟹ $U=T_S$ ⟹ $Z=S\oplus T_S=S+A(S)$。而 $S\subseteq D$ ⟹ $A(S)\subseteq H$ ⟹ $A(S)\subseteq Z$ 自动 ✓
$$\boxed{\ k=s=r\ \Longrightarrow\ \text{代数条件自动满足，只剩谱条件}\ }$$
（比"开稠密"更强。）

### 17.3 G4（新缺口）：实点论证**不充分**

我原写的"实 Grassmannian 在复化中 Zariski 稠密 ⟹ 真子集不能含全部实点"**只对 Grassmannian 本身成立**，
**不**对任意实线性截面 $X$ 成立：实线性截面可以**有复点而无实点**。

$$\operatorname{Gr}(r,m)(\mathbb R)\ \text{Zariski 稠密}\ \not\Longrightarrow\ X(\mathbb R)\ \text{在}\ X(\mathbb C)\ \text{中稠密}$$

- $r=1$：$\operatorname{Gr}(1,m)=\mathbb P^{m-1}$，非空线性截面本身就是射影线性空间 ⟹ 简单 ✓
- $r\ge2$：需**单独**建立实点存在性（实代数几何）

**状态**：**新缺口 G4，未解决**。

### 17.4 有限族**总有**共同补空间（QA21 §5）

$J_1,\dots,J_N$ 有限时，每个 $\Omega_i=\{W:W\cap J_i=0\}$ 是非空 Zariski 开集，Grassmannian 不可约 ⟹
$\bigcap_i\Omega_i\ne\varnothing$ ⟹ **共同补空间总存在**。

$$\boxed{\ \text{硬度只能来自\textbf{无限参数族}——这正是有理曲线结构重要的原因}\ }$$

### 17.5 PBH 的替代路线（QA21 §4.5）

Noferini–Van Dooren（LAA 658, 2023）Lemma 5.2：$m\times n$ 铅笔的右逆次数界 $\le m-1$。
对 $P(\lambda)^{\mathsf T}$ 应用后转置，得 $R(\lambda)^{\mathsf T}P(\lambda)=I_t$ 且 $\deg\le t-1$ ✓
——**直接**给出左逆证书，无需从 PBH 可观测性重建。**待核对其"有限特征值/左极小指标"约定**。

---

## 19. G3 在 $(r,m)=(2,4)$ 上的**完全解决**（2026-10-31，QA21 里程碑 2）

**设定**：$\operatorname{Gr}(2,4)\subset\mathbb P^5$，Plücker 关系是**单个**二次型
$$Q=p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}.$$
$L$ 由 $E$ 条线性条件切出，$X=L\cap Q$。把 $Q|_L$ 极化得对称矩阵 $M$（$\dim L\times\dim L$，精确有理算术）。

### 19.1 分类（纸面 + `c278` 核对）

| $\operatorname{rank}M$ | $X$ | $\operatorname{span}(X)$ | 判据 |
|---|---|---|---|
| $0$ | $X=L$（$L$ 整条落在 Grassmannian 里）| $L$ | $q_0|_L\ne0$（线性代数）✓ |
| $1$ | $Q|_L=\ell^2$ ⟹ $X=\{\ell=0\}$（$L$ 中的超平面）| $\ker\ell\subsetneq L$ | $q_0|_{\ker\ell}\not\equiv0\iff q_0\notin\operatorname{span}\{\ell\}$（线性代数）✓ |
| $2$ | 两个**不同**超平面的并（$Q|_L$ 分解为两个不同线性因子）| $L$ | $q_0\notin\operatorname{span}\{c_j\}$ ✓ |
| $\ge3$ | **不可约**二次超曲面 | $L$ | $q_0\notin\operatorname{span}\{c_j\}$ ✓ |

$$\boxed{\ \text{在 }(2,4)\text{ 上，G3 \textbf{不}是障碍：三类的 }\operatorname{span}(X)\text{ 都可精确算出（线性代数）}\ }$$

### 19.2 退化何时发生（`c278`，40 例/每个 $E$）

| $E$（线性条件数）| 射影 $\dim L$ | 随机样本中 $\operatorname{rank}M=1$ 的个数 |
|---|---|---|
| 1 | 4 | 0 |
| 2 | 3 | 0 |
| 3 | 2 | 0 |
| 4 | 1 | **1/40** |
| 5 | 0 | （$L$ 是点，$X=L$ 或 $\varnothing$，无退化）|

**结论**：退化**只**在 $E\ge\dim\operatorname{Gr}=4$ 时出现——与 §16 的推断一致 ✓，且此时**可精确判定**（秩 1 的对称矩阵）。

### 19.3 这改变了 A2 的结论

- 上一版把 G3 列为"薄集、**未解**"；现在：**$(2,4)$ 上 G3 已解**（判据仍是线性代数，只是要先把 $Q|_L$ 的秩算出来）；
- **仍未解**：$(r,m)$ 更大、Plücker 关系多于一个二次型的情形（如 $(2,5)$ 有三个二次型），
  此时"$X$ 的张成"不再由单个矩阵的秩决定，需要 Gröbner/根式成员判定。

---

## 20. 除子几何：有理曲线与行列式截面（正式命题，QA21 里程碑 3）

### 20.1 设定

$V$ 是 $m$ 维复向量空间，$f:\mathbb P^1\to\operatorname{Gr}(r,V)$ 是态射；
$\mathcal E\subset V\otimes\mathcal O_{\mathbb P^1}$ 是 tautological 秩 $r$ 丛的拉回，
$\mathcal L:=\det(\mathcal E)^*$ 是次数 $\ge0$ 的线丛。

对 $W\in\operatorname{Gr}(m-r,V)$，令 $\rho:V\to V/W$。则 $\rho|_{\mathcal E}$ 的行列式给岀
$$s_W\in H^0(\mathbb P^1,\mathcal L),\qquad s_W(t)\ne0\iff V=f(t)\oplus W .$$

### 20.2 命题 1（$\mathbb P^1$）：非常值曲线**没有**共同补空间

**命题**：若 $f$ 非常值，则不存在 $W$ 使 $V=f(t)\oplus W$ 对**所有** $t\in\mathbb P^1$。

*证明*：非常值 $f$ 的 Plücker 次数 $>0$ ⟹ $\deg\mathcal L>0$。正次数线丛上的**非零**截面必有零点
（否则 $\mathcal O\to\mathcal L$ 的截面给出次数 $\ge0$ 与 $\deg\mathcal L>0$ 矛盾）；零截面自然处处为零。
故每个 $W$ 都在某点失败。$\square$

### 20.3 命题 2（$\mathbb A^1$）：仿射上的判据

**命题**：设族是 $\mathbb A^1$ 上的（$\lambda\mapsto I_\lambda$），取次数 $\le D$ 的多项式基 $B(\lambda)$（常数秩情形，
引理 10.1'）。则
$$\boxed{\ \exists W:\ W\cap I_\lambda=0\ \ \forall\lambda\in\mathbb C\iff \det[W\mid B(\lambda)]\ \text{是非零常数}\ }$$

*证明*：$s_W(\lambda)=\det[W\mid B(\lambda)]$ 是 $\lambda$ 的多项式。$s_W$ 无根 $\iff$ 在 $\mathbb C$ 上无零点
$\iff$ 是非常数（非常数多项式在 $\mathbb C$ 上有根）$\iff$ 是非零常数。$\square$

**几何解释**：$\mathbb P^1$ 上必有零点（命题 1），但**所有零点都可以落在被略去的** $\lambda=\infty$——
等价于 $s_W$ 是常数。这就是"$\mathbb A^1$ 与 $\mathbb P^1$ 的差别"。

### 20.4 与 A2 命题 3 的对接（$r=1$）

$r=1$ 时 $W=\ker\ell$（超平面），$I_\lambda=\operatorname{span}(v(\lambda))$，
$$\det[W\mid v(\lambda)]=\ell(v(\lambda))=\sum_{j=0}^{D}\lambda^j\ell(v_j).$$
"非零常数" $\iff \ell(v_j)=0\ (j\ge1)$ 且 $\ell(v_0)\ne0$ $\iff v_0\notin\operatorname{span}\{v_1,\dots,v_D\}$
——**正是 §11.2b 的判据** ✓，现在有了线丛解释。

### 20.4b 实例化（`c284`，2026-10-31）

**曲线**：$\operatorname{Gr}(2,4)$ 中的 $f(\lambda)=\operatorname{span}\{(1,0,0,\lambda),(0,1,\lambda,0)\}$，
Plücker 坐标 $(1,\lambda,0,0,-\lambda,-\lambda^2)$，**次数 $2>0$** ⟹ 非常值 ✓

**结果**（2000 个 $W\in\operatorname{Gr}(2,4)$ 的小整数样本）：

| 检查 | 数量 |
|---|---|
| $s_W(\lambda)=\det[W\mid B(\lambda)]$ 是**非零常数**（$\mathbb A^1$ 上可行）| **73** |
| 这些 $W$ 中**仍与 $f(\infty)$ 互补**的 | **0** ✓ |

⟹ **每个 $W$ 都在 $\mathbb P^1$ 的某点失败**（73 个的失败点全在 $\lambda=\infty$）——与命题 1 **一致** ✓
同时验证了命题 2 的判据：$\mathbb A^1$ 上可行 $\iff s_W$ 非零常数 ✓

> **重要（QA22 §2）**：这条曲线在 $\operatorname{Gr}(2,4)$ 中，补空间 $W$ 是 2 维，故 **$r=2$**——
> 所以这是一个 **$r\ge2$ 的谱正例**（抽象意义下）。它**不**由 $\mathrm{DEC}(q)$ 的铅笔导出，
> 所以不能直接搬到原问题；但它**推翻**了"$r\ge2$ 恒不可行"的猜想。

### 20.5 秩跳变与例外值

若 $\operatorname{rank}P(\lambda)$ 跳变，命题 2 的"$B(\lambda)$ 处处满秩"不成立（引理 10.1' 需双常数）。
此时按 §10.2 分离：一般部分用命题 2、例外值 $\{\lambda_j\}$ 逐个加条件 $W\cap I_{\lambda_j}=0$。

### 20.6 与 G3 的关系

命题 2 给出"存在 $W$ 使 $\det$ 为非零常数"的判据，但要把 $W$ 的存在性化成**线性代数**，
需要 $\operatorname{span}(X)=L$（G3）。$(2,4)$ 上已解（§19）；一般 $(r,m)$ 未解。

---

## 21. 反例 G4（实点）：复非空 $⇏$ 实可行（QA21 §2.2；QA22 建议命名）

### 21.1 我原来的论证为什么不够

我写过"实 Grassmannian 在复化中 Zariski 稠密 ⟹ 真代数子集不能含全部实点"。这条**只对 Grassmannian 本身**成立；
对任意**实线性截面** $X=L\cap\operatorname{Gr}$ **不**成立：

$$\operatorname{Gr}(r,m)(\mathbb R)\ \text{Zariski 稠密 in}\ \operatorname{Gr}(r,m)(\mathbb C)\ \not\Longrightarrow\ X(\mathbb R)\ \text{稠密 in}\ X(\mathbb C)$$

### 21.2 反例（`c280`，$\operatorname{Gr}(2,4)$）

Plücker 型 $Q=p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}$ 的对称矩阵签名 $(3,3)$。取
$$L=\operatorname{span}\{p_{12}+p_{34},\ p_{13}-p_{24},\ p_{14}+p_{23}\}$$
则 $Q|_L=\tfrac14(x^2+y^2+z^2)$（**正定**，Gram 矩阵 $=\tfrac14 I_3$，顺序主子式 $\tfrac14,\tfrac1{16},\tfrac1{64}>0$ ✓）。

$$\boxed{\ X(\mathbb R)=L\cap Q(\mathbb R)=\varnothing\quad\text{而}\quad X(\mathbb C)\ne\varnothing\ (\text{如 }(i,1,0))\ }$$

⟹ **G4 确认成立**：A2 的"实点"结论**不能**由 Zariski 稠密推出。

### 21.3 修正后的陈述

| 情形 | 结论 |
|---|---|
| $r=1$ | $\operatorname{Gr}(1,m)=\mathbb P^{m-1}$；非空实线性截面本身就是实射影线性空间 ⟹ 实点**稠密** ✓（**完整**）|
| $r\ge2$，$X(\mathbb R)\ne\varnothing$ | 需**单独**证明（实代数几何）|
| $r\ge2$，可能 $X(\mathbb R)=\varnothing$ | **有反例**（本节）⟹ 必须把"$X(\mathbb R)\ne\varnothing$"作为**显式假设** |

**对 A2 命题 2/4 的影响**：它们陈述的"可行"若指**实** $U$，必须**显式加上**
$$X(\mathbb R)\not\subseteq\{q_0=0\}\quad(\text{实点版本})$$
作为假设；复版本（$X(\mathbb C)\not\subseteq\{q_0=0\}$）不受影响。

**状态**：[已证-纸面] + 反例（`c280`）。

---

> **QA22 建议**：此反例应作为**命名定理**在项目内引用。凡使用"代数几何 ⟹ 实可行"的地方都必须先查 G4。

## 22. 命题 2 的适用域：阈值成立 ⟹ $r\le p-1$（2026-10-31）

**命题**：若命题 2 的阈值 $m\ge r+t+1$ 成立，则
$$\boxed{\ r\ \le\ h-v-1\ \le\ p-r_{L_0}-1\ \le\ p-1\ }$$

*证明*：$m=h-s$、$t=v-s$、$r=w-q-s$。阈值等价于
$$h\ge w-q+v-s+1\iff q\ge w-h+v-s+1 .$$
于是
$$r=w-q-s\ \le\ w-(w-h+v-s+1)-s=h-v-1 .$$
又 $h=n-p-r_{L_0}$ 且 $v=n-\operatorname{rank}[C;CA]\ge n-2p$（$\operatorname{rank}[C;CA]\le2p$），故
$$h-v-1\le(n-p-r_{L_0})-(n-2p)-1=p-r_{L_0}-1\le p-1 .\qquad\square$$

### 22.1 推论：$r\ge2$ 的空白是**结构性**的（当 $p=2$）

$p=2$ 时命题 2 **只**能覆盖 $r\le1$。所以 campaign（`c279`）中"$r\ge2$ 没有谱正例"**不是**采样的偶然：
命题 2 **原理上**给不出 $r\ge2$ 的可行性。

**但这不证明 $r\ge2$ 不可行**——只是说**现有的充分条件覆盖不到**。$r\ge2$ 的谱可行性仍是**开放**的。

### 22.2 机器核对（`c281`）

60 个随机实例 × 所有 $q$，共 325 个 $(\text{实例},q,s)$ 组合；阈值成立的 37 个中，
违反 $r\le p-1$ 的：**0** 个 ✓

### 22.3 对既有实例的对照

| 实例 | $p$ | $r_{L_0}$ | $h$ | $v$ | $h-v-1$ | $p-r_{L_0}-1$ |
|---|---|---|---|---|---|---|
| R17 | 2 | 1 | 5 | 4 | 0 | 0 |
| 第二实例 | 1 | 1 | 4 | 4 | −1 | −1 |
| 第三实例 | 2 | 1 | 5 | 4 | 0 | 0 |

三者都与不等式一致 ✓（R17 的谱正例 $r=1$ 是在**阈值以下**得到的，见 §6 的四分类）。

---

## 23. 与 Clark–Shekhtman 的对接：补空间覆盖问题的标准形式（2026-10-31）

**文献**：W. E. Clark, B. Shekhtman, *Covering by complements of subspaces, II*, Proc. AMS **125** (1997) 251–254.

**他们的结果**：代数闭域上，$k$ 维子空间族 $E_1,\dots,E_t$ 的**补空间覆盖**全部 $(n-k)$-子空间所需的最小 $t$ 是
$$\gamma(k,n)=k(n-k)+1 .$$

**他们的机制**（与本项目**同构**）：
1. $E_i=\langle\epsilon_i\rangle\in\mathbb P(\wedge^kV)$，$\phi_i:\wedge^{n-k}V\to\wedge^nV$，$\phi_i(\xi)=\epsilon_i\wedge\xi$；
2. $K(E)=\bigcap_i\ker\phi_i$ 是**线性子空间**；
3. **Lemma 1**：覆盖 $\iff$ $D(n-k,n)\cap K(E)=\varnothing$（$D$ = 可分解向量）——即**线性空间与 Grassmannian 不相交**；
4. **Lemma 3**：$t\le k(n-k)$ 时 $\dim K\ge\binom nk-k(n-k)$，射影维数计数强制 $K\cap G\ne\varnothing$。

**对本项目的两条直接影响**：

**(a) 我们的条件正是"避开可分解锥"**：$U\cap I_\lambda=0\iff\epsilon_U\wedge\epsilon_{I_\lambda}\ne0$，
所以"可行"$=$ 存在**可分解** $\alpha$ 使 $\alpha\notin\ker\phi_\lambda$ 对一切 $\lambda$。

**(b) 有限与单参数的分界被量化**：
$$\boxed{\ \dim\Big(\bigcup_{i\le t}B(F_i)\Big)\le\nu-1\ (\text{有限族，}\nu=k(n-k))\qquad\text{而}\qquad \dim\Big(\bigcup_{\lambda}B(I_\lambda)\Big)\le\nu\ }$$
前者**严格小于** $\dim G$ ⟹ 有限族**总有**共同补空间；后者**恰好等于** $\dim G$ ⟹ **临界**，覆盖**可能**发生。

**⟹ 除子情形的困难是结构性的**（不是我们方法的缺陷）：单参数族恰好使坏集的维数顶到临界值。
Clark–Shekhtman 的 Lemma 3 与 Lemma 1 是我们可引用的两件工具，但他们**不处理**单参数族。

**局限**：他们解的是有限族；我们的问题是单参数族，**仍是开放的**。

## 24. $(2,5)$ 的 G3：一次结构性观察（2026-10-31）

$(2,5)$ 有 **5 个** Plücker 二次型（对应 $\{1,\dots,5\}$ 的 4-子集），比 $(2,4)$ 的 1 个多，
所以 §19 的"$\operatorname{rank}(Q|_L)$"方法**不能**直接推广。

**一个可归约的子情形**：取
$$L_0=\{p_{15}=p_{25}=p_{35}=p_{45}=0\}$$
（$e_5$ 不参与），则 $L_0\cap\operatorname{Gr}(2,5)=\operatorname{Gr}(2,4)\subset\mathbb P^5$，
且 $L_0$ 恰是 $\mathbb P^9$ 中"只含前 4 维坐标"的 5 维射影空间 ⟹
$$\operatorname{span}(L_0\cap\operatorname{Gr}(2,5))=\operatorname{Gr}(2,4)\ \text{的张成}=L_0\quad✓$$
（$\operatorname{Gr}(2,4)$ 非退化）。

所以**落在某个 $\operatorname{Gr}(2,4)$ 内的截面**可以用 §19 的 $(2,4)$ 理论**完全**分析（再把 $L_0$ 的 4 个条件加上）。

**一般情形**（$L$ 不落在任何 $\operatorname{Gr}(2,4)$ 内）**未解决**，需要：
1. 计算 $I=I_{\operatorname{Gr}}+I_L$ 的**根式**的 1 次部分 $(\sqrt I)_1$；
2. 或对每个候选线性形式用 Rabinowitsch 技巧判 $q\in\sqrt I$。

**现状**：$(2,5)$ 的**一般** G3 **开放**；$(2,4)$ 与"落在 $\operatorname{Gr}(2,4)$ 内"的子情形**已解**。

**为什么不继续攻**（本轮判断）：$(2,5)$ 一般情形需要计算机代数（Gröbner + 根式成员），
而**它是否影响最终复杂度结论**取决于 $D\ge m-r$ 的薄参数区是否真会出现——这一点**尚未**在真实实例中观察到
（campaign `c279` 的 18 个配置里 $D$ 都远小于 $m-r$）。在没有实例驱动的情况下投入 Gröbner 工程，
收益不确定；把它**明确标为开放**并记录方法，比强行给出一个未验证的结论更符合项目纪律。

---

## 25. 系数空间刻画（QA22 的"定理 B"，中心表述）

**设定**：固定可容许 $S$，$B(\lambda)=\sum_{j=0}^{d}\lambda^jB_j$ 是 $I_\lambda$ 的多项式基（常数秩情形），
$$q_U(\lambda)=\det[U\mid B(\lambda)]=\sum_{j=0}^{d}\langle a_j,\,p_U\rangle\lambda^j,$$
其中 $p_U$ 是 $U$ 的 Plücker 点，$a_j$ 是**对偶 Plücker 空间中的固定向量**（由 $B_j$ 决定）。

**定理 B（系数空间刻画）**：令 $K=\bigcap_{j\ge1}\ker a_j\subseteq\mathbb P(\wedge^r(H/S))$，则
$$\boxed{\ \text{谱可行}\iff \operatorname{Gr}\cap\mathbb P(K)\ \not\subseteq\ \mathbb P(\ker a_0)\ }$$
即：**仿射共同补空间轨迹 $=\operatorname{Gr}\cap\mathbb P(K)\setminus\mathbb P(\ker a_0)$**。

*证明*：$U\in\operatorname{Gr}\cap\mathbb P(K)$ ⟺ 所有 $\lambda^{\ge1}$ 系数为零 ⟺ $q_U\equiv\langle a_0,p_U\rangle$ 为常数；
再要求非零 ⟺ $\langle a_0,p_U\rangle\ne0$ ⟺ $p_U\notin\mathbb P(\ker a_0)$。而 $q_U$ 非零常数 ⟺ $U$ 与所有 $I_\lambda$ 不交 ✓（命题 2）。$\square$

**意义（QA22）**：**$\forall\lambda$ 的量词被完全消去**，只剩"线性截面 ∩ Grassmannian" + 一个非零条件。
这与 §11.2 的判据等价，但**表述更中心**：$a_j$ 是**系数对偶向量**，$K$ 是它们的公共核。

**实版本**：还需 $\operatorname{Gr}(\mathbb R)\cap\mathbb P(K)\setminus\mathbb P(\ker a_0)\ne\varnothing$（G4，§21）。

### 25.1 三个维数必须分开（QA22 §4.2）

| 记号 | 含义 | 现状 |
|---|---|---|
| $d_{\mathrm{alg}}=(r-k)(m-r)$ | 代数纤维维数 | ✓ 已算（`c277`）|
| $d_{\mathrm{spec}}=\dim\pi_S^{-1}(S)$（加谱条件后）| 谱可行纤维维数 | **未知**（谱条件是额外方程）|
| $d_{\mathrm{image}}=\dim\overline{\pi_S(X^{\mathrm{spec}})}$ | 投影像的维数 | **未知**（支配性问题）|

$$\boxed{\ d_{\mathrm{alg}}\ \text{不决定}\ d_{\mathrm{spec}}\ \text{或}\ d_{\mathrm{image}}\ }$$
上一版把三者混用，已更正。

---

## 26. 系数空间模块与扫描（QA22 §4.3，2026-10-31）

**模块**：[tools/verification/coeff_space.py](../../tools/verification/coeff_space.py)
（多项式矩阵行列式、系数形式 $a_j$、线性数据、$r=1$ 与 $(2,4)$ 判据）。
**扫描**：`proof/layer_program/c285_coeff_scan.py`。

### 26.1 三个实例（两个正例 + **一个真负例**）

| 实例 | $m$ | $r$ | $\dim$ Plücker | $\deg q_U$ | $\operatorname{rank}\{a_j\}_{j\ge1}$ | $\dim K$ | 判据 | 直接枚举 |
|---|---|---|---|---|---|---|---|---|
| A：`c282` 实例 | 4 | 1 | 4 | 3 | 3 | 1 | **可行** | 可行（4/624 条线）✓ |
| B：二次曲线 | 4 | 2 | 6 | 2 | 2 | 4 | **可行** | 可行（73 个 $W$）✓ |
| C：**负例** | 3 | 1 | 3 | 4 | 2 | 1 | **不可行** | 不可行 ✓ |

$$\boxed{\ \text{三例的系数判据与直接枚举}\ \textbf{全部一致}\ }$$

### 26.2 负例 C 的作用

$v(\lambda)=(1+\lambda^2,\ 1+\lambda,\ -(1+\lambda^2))$，$I_\lambda=v(\lambda)^\perp$。则
$$a_0=a_1+a_2,\qquad K=\ker a_1\cap\ker a_2=\operatorname{span}(1,0,1),\qquad a_0|_K=0 .$$
所以判据给**不可行**——而直接检查：$u=(1,0,1)$ 满足 $\langle u,v(\lambda)\rangle\equiv0$（对所有 $\lambda$ 都坏）；
其余 $u$ 的多项式非常数（有根）⟹ 也是坏。**没有**可行的 $u$ ✓

这正是 §11.2 强调的"$\operatorname{Gr}\cap L$ 可能整体落在 $\{q_0=0\}$ 里"的具体实例——
**判据必须带 $\not\subseteq\{q_0=0\}$ 这一条，否则会误判为可行**。

### 26.3 三个维数（QA22 §4.2）

| 量 | 本扫描的值 |
|---|---|
| $d_{\mathrm{alg}}=(r-k)(m-r)$ | A：$(1-0)(4-1)=3$；B：$(2-0)(4-2)=4$；C：$(1-0)(3-1)=2$ |
| $d_{\mathrm{spec}}$（谱可行纤维维数）| **未算**（需要把 $K$ 与 $\{a_0\ne0\}$ 一起算维数）|
| $d_{\mathrm{image}}$（投影像维数）| **未算** |

**诚实说明**：本扫描只判"存在性"，**没有**算 $d_{\mathrm{spec}}$ 与 $d_{\mathrm{image}}$——
这两项是 QA22 明确要求的，仍待实现。

---

## 27. 定理 A：仿射有理曲线补空间定理（完整表述 + 机器核对）

### 27.1 陈述

设 $f:\mathbb P^1\to\operatorname{Gr}(r,V)$ **非常值**、Plücker 次数 $d>0$；$\mathcal E$ 是 tautological 丛的拉回，
$\mathcal L=\det(\mathcal E)^*$（次数 $d$）。对 $W\in\operatorname{Gr}(m-r,V)$ 记
$$s_W(\lambda)=\det[W\mid B(\lambda)]$$
（仿射坐标下的多项式，$\deg\le d$；$B$ 是 $f$ 的多项式基）。

**定理 A1（$\mathbb P^1$）**：每个 $W$ 都在 $\mathbb P^1$ 的某点失败：
$$\forall W\ \exists t\in\mathbb P^1:\ s_W(t)=0 .$$
*证明*：$s_W$ 是 $\mathcal L$ 的截面，$\deg\mathcal L=d>0$；非零截面必为零点，零截面处处为零。$\square$

**定理 A2（$\mathbb A^1$）**：$W$ 在 $\mathbb A^1$ 上可行（补所有 $f(\lambda)$，$\lambda\in\mathbb C$）$\iff$
$$\boxed{\ s_W\ \text{是非零常数}\iff \operatorname{div}(s_W)=d[\infty]\ }$$
*证明*：$s_W$ 无有限根 $\iff$ 非常数（非常数多项式在 $\mathbb C$ 上有根）$\iff$ 非零常数；而由 A1，零点必须全在 $\infty$，
即 $\operatorname{div}(s_W)=d[\infty]$ ✓ $\square$

**定理 A3（$\mathcal F$ 的结构，常数秩情形）**：
$$\mathcal F=\{W:\operatorname{div}(s_W)=d[\infty]\}=\operatorname{Gr}\cap\mathbb P(K)\setminus\mathbb P(\ker a_0),\qquad K=\bigcap_{j\ge1}\ker a_j,$$
其中 $s_W(\lambda)=\sum_j\langle a_j,p_W\rangle\lambda^j$。**$\mathcal F$ 是局部闭的**（开于闭的线性截面 $\operatorname{Gr}\cap\mathbb P(K)$ 中）。

### 27.2 机器核对（`c287`，两条曲线）

| 曲线 | $d$ | $\mathbb A^1$ 可行的 $W$ | $\mathbb P^1$ 上"无失败"的 $W$ | 仿射可行但不在 $\infty$ 失败 |
|---|---|---|---|---|
| 二次 $\operatorname{span}\{(1,0,0,\lambda),(0,1,\lambda,0)\}$ | 2 | **368** / 6240 | **0** ✓ | **0** ✓ |
| 三次 $\operatorname{span}\{(1,0,0,\lambda^2),(0,1,\lambda,0)\}$ | 3 | **240** / 6240 | **0** ✓ | **0** ✓ |

两个方向上都没有反例：**仿射可行 $\iff$ 非零常数**，且**所有** $W$ 都在 $\mathbb P^1$ 的某点失败
（仿射可行的那些，失败点全在 $\lambda=\infty$）。

### 27.3 未解决

- $\mathcal F$ 的**维数**与**不可约性**（定理 A 建议的下一步）：目前只有"局部闭"与"是 $\operatorname{Gr}\cap\mathbb P(K)$ 的开子集"；
- $\mathcal F$ 的**分支**：$\operatorname{Gr}\cap\mathbb P(K)$ 可能可约（局部闭集不必不可约）。

---

## 28. 斜形式铅笔（QA22 Q7，Case II）——实验与结论

### 28.1 表述

$L\subseteq\Lambda^2V$、$A=L^\perp=\operatorname{span}\{\omega_0,\omega_1\}\subseteq\Lambda^2V^*$。则
$$\mathbb P(L)\cap\operatorname{Gr}(2,V)=\{\text{同时对各 }\omega\in A\text{ 各向同性的 2-平面}\}.$$
**不变量**：$\rho_{\mathrm{gen}}=\max_t\operatorname{rank}(Q_0+tQ_1)$、公共根 $K_A=\ker Q_0\cap\ker Q_1$、
奇异参数 $\{t:\operatorname{rank}(Q_0+tQ_1)<\rho_{\mathrm{gen}}\}$（对 $n=4$ 就是 $\operatorname{pf}(Q_0+tQ_1)$ 的零点）。

### 28.2 实验（`c286`，$n=4$、$\dim A=2$、30 个随机整数铅笔）

| 观察 | 数据 |
|---|---|
| $\operatorname{rank}(Q\|_L)$ | 全为 **2 或 4**（$\dim L=3$ 时）|
| **G3 退化（rank $=1$）** | **0 / 30** |
| $\operatorname{pf}$ 次数分布 | 0：1 个；1：6 个；2：23 个 |
| 公共根 $\dim K_A$ | 多为 0（个别 1）|

### 28.3 结论（诚实版）

$$\boxed{\ n=4\ \text{时余维 2 截面的 G3 完全由 }\S19\text{ 的 }\operatorname{rank}(Q\|_L)\text{ 判定；斜形式不变量没有提供新信息}\ }$$

**为什么 $n=4$ 不够**：$G(2,4)\subset\mathbb P^5$ 只有一个 Plücker 二次型，所以"斜形式系统"与
"$\mathbb P(L)$ 的单个二次型限制"是同一件事（$\S19$ 已解）。

**$n\ge5$ 才是真正的新情形**（$G(2,n)$ 有 $\binom{n}{4}$ 个 Plücker 二次型），但那里
1. 各向同性 2-平面的显式参数化困难；
2. $\operatorname{span}(X)$ 不再由单个矩阵的秩决定。

**状态**：$n\ge5$ 的斜形式铅笔 **未做**（需要更大的计算工具或代数几何定理）。这是 QA22 Q7 的**主要未落实部分**。

---

## 29. 三个新命题（QA23）

### 29.1 命题 1：去掉区分超平面后的维数

设 $X=\operatorname{Gr}\cap\mathbb P(K)$，$F=X\setminus\mathbb P(\ker a_0)$。$F$ 是 $X$ 的**开子集**，故
$$\dim F=\max\{\dim X_i:\ X_i\not\subseteq\mathbb P(\ker a_0)\},$$
其中 $X_i$ 是 $X$ 的不可约分量；**若无这样的分量，则 $F=\varnothing$**（约定 $\dim\varnothing=-\infty$）。

*证明*：$F$ 是 $X$ 中"$a_0\ne0$"的开集；$X=\bigcup X_i$，故 $F=\bigcup_i (X_i\setminus\{a_0=0\})$；
每个 $X_i\setminus\{a_0=0\}$ 在 $X_i$ 中开、非空（当 $X_i\not\subseteq\{a_0=0\}$）、与 $X_i$ 同维 ✓ $\square$

**注意**：**不能**用"期望维数" $\dim\operatorname{Gr}+\dim\mathbb P(K)-\dim\mathbb P(\Lambda^{m-r}V)$ 代替真维数——
线性截面可能非横截。

### 29.2 命题 2：负例的结构刻画

令 $D(K)=\operatorname{span}\{p\in K:\ p\ \text{可分解}\}$（可分解点张成的线性空间）。则
$$\boxed{\ X\subseteq\mathbb P(\ker a_0)\iff a_0|_{D(K)}=0\iff a_0\in D(K)^\perp\ }$$

*证明*：$X=\{\text{可分解 }p\in K\}/\!\sim$，故 $a_0|_X=0\iff a_0$ 在每个可分解点上为零
$\iff a_0$ 在它们的张成 $D(K)$ 上为零 ✓ $\square$

**关键区别**：$a_0|_K=0\Rightarrow a_0|_{D(K)}=0$，但**反之不然**——只有当可分解点**张满** $K$ 时两者等价。
这正是负例 C 的情形：$a_0|_K\ne0$ 但 $a_0|_{D(K)}=0$。

**算法**（专家给）：$a_0\in\sqrt I$，$I=I_{\operatorname{Gr}}+I_K$——**根式成员**，不是普通理想成员。

### 29.3 命题 3：多项式基的**框架不变性**

设 $B'(\lambda)=B(\lambda)U(\lambda)$ 是 $I_\lambda$ 的另一组多项式基，$U$ unimodular（$\det U\in\mathbb C^\times$）。则
$$\det[W\mid B'(\lambda)]=\det[W\mid B(\lambda)]\cdot\det U(\lambda)=\text{const}\cdot\det[W\mid B(\lambda)].$$
故**"$\det[W\mid B(\lambda)]$ 是非零常数"这一判据与基的选取无关** ✓

*注*：若不作 unimodular 限制，$\det U$ 可含非常数因子，会**引入/消去**有限根，判据就不不变了。
**我们的模块用"由极大子式给出的基"，其框架变换是 unimodular 的**（同一子丛的两组基相差一个幺模矩阵）。

### 29.4 机器数据（`c285`，扩展后）

| 实例 | $\dim X$ | $\dim F$ | 分量数 |
|---|---|---|---|
| A（`c282`）| 0 | 0 | 1 |
| B（二次曲线）| 2 | 2 | 1 |
| C（负例）| 0 | **None（$F=\varnothing$）** | 1 |

与判据一致 ✓（C 的 $\dim X=0$ 非空但整体落在 $\ker a_0$ 里 ⟹ $F=\varnothing$）。

### 29.5 仍未做

- $\dim X$ 的**一般**计算（需要 Plücker 理想的分量分解，QC23 §2）；
- $d_{\mathrm{image}}$（需要显式投影，QA23 §4）；
- $n\ge5$ 的"共同各向同性张成"问题（QA23 §3，提法：$\operatorname{span}\{u\wedge v:\omega_0(u,v)=\omega_1(u,v)=0\}=A^\perp$？）。

### 29.2b $(2,4)$ 上的**结构性检测器**（`c288`）

在 $(r,m)=(2,4)$ 上，$I=(Q)+I_K$，$a_0\in\sqrt I$ 可以按 $Q|_K$ 的秩**完全分类**：

| $\operatorname{rank}(Q|_K)$ | $X$ | $a_0\in\sqrt I$ 的条件 |
|---|---|---|
| 0 | $\mathbb P(K)$ | $a_0|_K=0$ |
| **1** | 超平面 $\{L=0\}$ | $a_0|_K\in\operatorname{span}\{L\}$ |
| 2 | 两个不同超平面 | $a_0|_K=0$ |
| $\ge3$ | 不可约二次超曲面 | $a_0|_K=0$ |

$$\boxed{\ \text{故：若 }a_0|_K\ne0\ \text{且}\ a_0|_X=0,\ \text{则必}\ \operatorname{rank}(Q|_K)=1\ }$$

即"$a_0$ 在 $K$ 上不恒零、但在 $X$ 上恒零"这种**负例**，在 $(2,4)$ 上只可能来自**秩 1 的退化二次型**。

**机器核对**（40 个随机 $(2,4)$ 族）：根式判据与暴力搜索**0 不一致** ✓
**诚实说明**：40 例里 $\operatorname{rank}(Q|_K)\in\{2,3\}$，**没有出现秩 1 的实例**——
秩 1 分支是**纸面证明**的，未被实例覆盖。

### 29.2c $(2,4)$ 上 rank 1 **不可能**——判据坍缩为线性代数（2026-10-31）

**命题**：设 $Q$ 是 $\operatorname{Gr}(2,4)\subset\mathbb P^5$ 的 Plücker 型（**非退化**），$K\subseteq\mathbb C^6$ 是 $\dim4$ 的子空间。则
$$\operatorname{rank}(Q|_K)\ \ge\ 4-2\ =\ 2 .$$

*证明*：对称双线性型的限制 $Q|_K$ 的**根**是 $K\cap K^\perp$。由非退化性 $\dim K^\perp=6-4=2$，故
$\dim(K\cap K^\perp)\le2$，于是 $\operatorname{rank}(Q|_K)=4-\dim(K\cap K^\perp)\ge2$ ✓ $\square$

**推论（判据坍缩）**：由 §29.2b 的分类，rank $\ge2$ 时 $a_0\in\sqrt I\iff a_0|_K=0$。而 $a_0|_K=0\iff a_0\in K^\perp=\operatorname{span}\{a_1,a_2\}$。于是
$$\boxed{\ \text{在 }(2,4)\text{ 上：可行}\iff a_0\notin\operatorname{span}\{a_1,a_2\}\ }$$
**即：$\mathbb P(K)\cap\operatorname{Gr}$ 上的"区分超平面"条件是自动的**——不需要检查 $a_0$ 是否在截面中消失，
判据退化为**纯线性代数**。

**机器核对**：
- `c289`：3000 个随机 $(2,4)$ 实例，$\operatorname{rank}(Q|_K)$ 分布 $\{4:2967,\ 3:32,\ 2:1\}$——**无 rank 1、无 rank 0** ✓ 与命题一致；
- `c288`：40 例上根式判据与暴力搜索 **0 不一致** ✓

**注意**：这个坍缩是 $(2,4)$ **特有**的（$\dim K=4$、$K^\perp$ 只有 2 维）。对更大的 $(r,m)$，$K$ 的余维更大，$Q|_K$ 可能退化到 rank 1 甚至 0，负例就**真实存在**（§29.2b 的表就非空）。

---

## 30. 坍缩问题：span(X)=L 何时成立（方向 C，2026-10-31）

**问题**：$X=\\operatorname{Gr}(2,m)\\cap\\mathbb P(K)$（$K$ 由 $D$ 条独立线性条件切出，$\\dim K=\\binom m2-D$），
问 $\\operatorname{span}(X)=\\mathbb P(K)$ 是否成立；若成立，判据退化为线性代数。

### 30.1 一般下界

对单个非退化二次型 $Q$（$N=\\binom m2$ 维）：$\\operatorname{rank}(Q|_K)\\ge\\dim K-\\dim K^\\perp=N-2D$。

### 30.2 改进的采样（**构造性**）

旧版每个 $u$ 只取**一个** $v$；新版取**整个** $V_u=\\bigcap_i\\ker\\omega_i(u,\\cdot)$ 的基
（$\\dim V_u\\ge m-D$），把所有 $u\\wedge v_j$ 都加入 ⟹ 每个 $u$ 贡献 $m-D$ 个方向。
每个点都 `assert` 在 $L$ 里（CLAUDE.md §7.21）。

### 30.3 证书表（`c290`，随机形式，确定性）

| $(r,m)$ | $D=1$ | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| (2,4) | ✓5 | ✓4 | ✓3（26 点）| — | — |
| (2,5) | ✓9 | ✓8 | ✓7 | ✓6（17 点）| — |
| (2,6) | ✓14 | ✓13 | ✓12 | ✓11 | **无样本** |

（数字 = $\\dim L$ = 达到的 span 维数；✓ = 证书。）

$$\\boxed{\\ \\text{对 }(2,m),\\ m\\le6,\\ D\\le m-1\\text{ 的随机情形：}\\operatorname{span}(X)=L\\ \\text{（已证）}\\ }$$

**为什么"达到 $\\dim L$"就是证明**：下界 = 上界 ⟹ 相等；样本点是精确有理点且都断言过在 $L$ 里 ⟹ 证书，不是采样证据。

### 30.4 两个边界现象

**(a) 退化实例（$(2,4)$，$D=3$）**：找到 $\\operatorname{rank}(Q|_K)=1$（$Q|_K=L^2$）的三元形式
$$\\omega_1=(-2,0,0,-1,-1,1),\\quad \\omega_2=(0,0,-2,1,2,-1),\\quad \\omega_3=(-2,-2,0,1,-1,0)$$
此时 $X=\\{L=0\\}\\cong\\mathbb P^1$，$\\dim\\operatorname{span}(X)=2<3=\\dim L$ ⟹ **退化存在，但是非一般的**。

**(b) $(2,6)$，$D=5$：$X$ 为空**。因为 $u\\in V_u$ 恒成立（$\\omega_i(u,u)=0$），而 $m-D=1$ ⟹
一般 $u$ 的 $V_u=\\operatorname{span}(u)$ ⟹ 过 $u$ 没有合法的 2-平面 ⟹ $X=\\varnothing$（或很小）。

### 30.5 结论

$$\\text{对 }(2,m)\\ (m\\le6)\\text{ 与随机形式：}D\\le m-1\\text{ 时 }\\operatorname{span}(X)=L\\text{（除 }D=m-1\\text{ 且 }X\\text{ 可能变空）}$$
**退化是非一般的**（有显式实例），**空截面出现在 $D=m-1$**。

> **过程记录**：初版 `c290` 有 bug——组合系数在**每个坐标**上重抽 ⟹ 采样点不在 $L$ 里，
> 却输出"秩 $=\\binom m2$"的荒谬数据。加入 `assert a·p == 0` 后立刻暴露；修复后数据才可信。

---

## 31. $n=5$ 的 pencil-span（QA23 优先级 4，2026-10-31）

### 31.1 提法（专家原文）

给定交替形式对 $(\omega_0,\omega_1)$，令 $A=\operatorname{span}\{\omega_0,\omega_1\}\subseteq\Lambda^2V^*$，问
$$\operatorname{span}\{u\wedge v:\ \omega_0(u,v)=\omega_1(u,v)=0\}\overset{?}{=}A^\perp .$$
用**齐次**铅笔 $s\omega_0+t\omega_1$（含 $\infty$）。

### 31.2 实验（`c291`，$n=5$，$\dim A^\perp=8$）

五类铅笔、11 个实例，每个都用**构造性采样**（整个 $V_u$）并 `assert` 点在 $L$ 里：

| 类型 | $\operatorname{rank}\omega_0$ | $\operatorname{rank}\omega_1$ | 点数 | span | 结论 |
|---|---|---|---|---|---|
| generic ×3 | 4 | 4 | ~880 | 8 | **证书 ✓** |
| 同余 $A\omega_0A^{\mathsf T}$ ×2 | 4 | 4 | ~880 | 8 | **证书 ✓** |
| 两个 rank 2 ×2 | 2 | 2 | ~890 | 8 | **证书 ✓** |
| 共享核 $e_0$ ×2 | 4/2 | 4 | ~890 | 8 | **证书 ✓** |
| rank 4 + rank 2 ×2 | 4 | 2 | ~890 | 8 | **证书 ✓** |

$$\boxed{\ \text{对 }n=5\text{ 的所有测试铅笔（含低秩、共享核、同余）：}\ \operatorname{span}(X)=A^\perp\ }$$

### 31.3 推论：$r=2$ 时 G3 **不是**障碍

结合 §30（$(2,m)$，$m\le6$，$D\le m-1$ 的随机形式都给出 $\operatorname{span}(X)=L$）：
$$\boxed{\ \text{在 }r=2\text{ 的所有已测情形中，判据都是线性代数（G3 不构成障碍）}\ }$$
**唯一的反例**是**非一般**的：§30.4(a) 的 $(2,4),D=3$ 实例（$\operatorname{rank}(Q|_K)=1$）。

### 31.3b $(2,6)$ 的结构化铅笔（`c292`）

| 类型 | $\operatorname{rank}\omega_0$ | $\operatorname{rank}\omega_1$ | 点数 | span | 结论 |
|---|---|---|---|---|---|
| 共享 2 维核 ×2 | 2/4 | 4/2 | ~1200 | 13 | **证书 ✓** |
| 两个 rank 2 ×2 | 2 | 2 | ~1200 | 13 | **证书 ✓** |
| rank 2 + rank 4 ×2 | 2 | 6 | ~1200 | 13 | **证书 ✓** |

（$\dim L=15-2=13$；随机铅笔已由 `c290` 覆盖。）

⟹ **$(2,6)$ 的铅笔在所有已测结构下都非退化**。

### 31.4 仍未做

- $n\ge6$ 的 pencil-span（$\dim A=2$ 但 $G(2,n)$ 有更多 Plücker 二次型）；
- 奇异铅笔的**系统分类**（Kronecker 标准形）——专家说"更深的理论分支"；
- $r\ge3$ 的情形（完全未触及）。

---

## 32. $\pi_S$ 的支配性：第一个实例的 $S$-扫描（A3 第一轮，2026-10-31）

**背景**：§25–31 全部固定在**一个** $S$ 上。本节第一次让 $S$ 在基族 $\mathcal B_{s,k}$ 里动。

### 32.1 可容许的 $U$（重新推导，修正一处旧错误）

给定 $S\subseteq D$，可容许的 $U$ 满足
$$\boxed{\ S\subseteq U\subseteq H,\quad \dim U=d,\quad A(S)\subseteq U,\quad U\cap G=S\ }$$
**注意**：$U\subseteq H$（不是 $U\subseteq V$）。旧实现写成 $U\subseteq V$，把 R17 的可行 $U$ 全排除了，
经 R17 回归才发现并修正——这是本项目第 5 次"约束写错、结论看起来对"。

### 32.2 判据

对每个 $Z=U$（$n\times d$）：$(A)$ 用 $\operatorname{rank}[Z,AZR]=d$（$R$ 张成 $\ker(CAZ)$）；
$(S)$ 用 `spectral_gcd_Z`（极大子式 gcd）。二者都由 `tools/verification/base_sweep.py` 实现，
并带断言（$S\subseteq D$、维数链、$D$ 的像在 $H$ 里）。

### 32.3 回归：R17（已知可行）

$S=\operatorname{span}(e_5,e_6)$、$q=3$（$d=3$、$r=1$、$m=3$）：
$$\text{候选 }U\ \textbf{48}\text{ 个，可行 }\textbf{34}\text{ 个}\ (71\%)$$
与文档记载的"75% 的 $U$"一致 ✓ —— 机器验证了模块的正确性。

### 32.4 第二实例（$n=6$、$p=1$、$D=G$ 三维）的 $S$-扫描

| $q$ | $d$ | $s$ | $r$ | 扫过的 $S$ | 可行 $S$ |
|---|---|---|---|---|---|
| 4 | 1 | 0,1 | 1,0 | 1, 13 | **0, 0** |
| 3 | 2 | 1,2 | 1,0 | 13, 25 | **0, 0** |
| 2 | 3 | 2,3 | 1,0 | 25, 1 | **0, 0** |
| 1 | 4 | 3 | 1 | 1 | **0** |

**$q=4$ 的覆盖是完整的**（$d=1$ ⟹ $s\in\{0,1\}$，两者都 $r\le1$）⟹

$$\boxed{\ \text{第二实例在 } q=4 \text{ 上对\textbf{所有} } S\subseteq D \text{ 都不可行}\ }$$

而 $q=5$（$d=0$）时 $Z=0$，$(5a)(5b)$ 平凡成立 ⟹ **该实例的 $q_{\min}=5$**（在 $d=0$ 可接受的约定下）。

> **2026-11-01 撤回（专家 Q1 确认）**：$q=5$ 时 $(5b)$ 在 $\lambda=1$ 失败（$e_1,\dots,e_4\in V$ 是 1-特征向量），故本实例**无解**，$q_{\min}=5$ 不成立。证书 [check_qmin5.py](../../archive/proof_audits/review_2026-11-01/check_qmin5.py)；正确维度与商等价定理见 [v2 §2/§4](../../archive/expert_correspondence/REPORT_FOR_EXPERT_2026-11-01_v2_EN.md)。

### 32.5 仍未覆盖

- $q=2$ 的 $s=0,1$（$r=3,2$）与 $q=3$ 的 $s=0$（$r=2$）：$U$ 的枚举是 $\operatorname{Gr}(r,H/S)$，格点太贵，**未扫**；
- $S$ 的枚举只到 $\{-1,0,1\}$ 系数（RREF 去重）；
- 结论标 `[精确验证]`，不是"所有 $S$"的证明。

### 32.6 对 A3 的意义

$S$ **确实**要搜：至少第二实例在 $q\le4$ 上没有"随便哪个 $S$ 都行"这回事。
但同时 $q=4$ 的**完整**覆盖给出了一个真正的 $q_{\min}$——这是项目第一次算出具体实例的最小阶。

---

## 33. $a_j(S)$ 的显式算法——**不需要多项式标架**（A3-1 完成，2026-10-31）

### 33.1 关键观察

$U\subseteq H/S$（A2 的可容许约束）⟹ 在 $[U\mid P(\lambda)]$ 的极大子式里，**只有取 $H/S$ 的那些行才可能非零**
（其余行的 $U$ 列为零）。所以

$$q_U(\lambda)=\det\big[U\mid P_H(\lambda)\big]=\sum_{j}\lambda^j\langle a_j,p_U\rangle,$$

其中 $P_H$ 是 $P(\lambda)$ 限制到 $H/S$ 的 $m$ 行（$m=\dim H/S$，列数 $t=m-r$）。

$$\boxed{\ \text{谱可行}\iff a_0\notin\operatorname{span}\{a_1,\dots,a_d\}\ }$$

**这完全绕开了 QA24 的多项式基障碍**：不需要 $I_\lambda$ 的标架，因为判据直接用 $P_H$。

### 33.2 实现与验证

`tools/verification/coeff_of_S.py` 的 `coeff_forms_of_S`：算出 $a_j$（用 `coeff_space.coeff_forms` 于 $[P_0,P_1]$）。

**c282 实例**（$m=4$、$r=1$、$t=3$）：$\deg q_U=3$，扫 $H/S$ 的 80 个格点 $U$：

| 判据 | 结果 |
|---|---|
| 直接判据（gcd of minors，`feasible_by_minors`）| 可行 **2** 个 |
| 系数判据（$a_0\notin\operatorname{span}\{a_j\}$）| 与之**0 不一致** ✓ |

### 33.3 与 QA24 的关系

- QA24 的 Smith/Hermite 框架：**对固定 $S$ 构造 $I_\lambda$ 的标架**——仍是对的，但**判据不需要它**；
- QA24 的 Bézout 证书（A3-4a）：仍然有用（它把 gcd 条件变成有限方程），但**系数形式更直接**；
- QA24 强调的"固定 $S$ 有框架 $\not\Rightarrow$ 对 $S$ 统一框架"——**现在不再阻塞**，因为 $a_j$ 可以直接由 $P_H$ 给出，
  而 $P_H$ 对 $S$ 的依赖是**显式的**（$S$ 只进入 $W/S$ 与 $H/S$ 的坐标选择）。

### 33.4 仍未解决

- $a_j(S)$ 作为 $S$ 的函数的**显式代数形式**（$S$ 变时坐标基也变，需要写成 Plücker 坐标的多项式）；
- 秩跳变（$I_\lambda$ 维数随 $\lambda$ 变）时 $t$ 可能变——本节的 $P_H$ 恒有 $t$ 列，但 $\operatorname{rank}P_H(\lambda)$ 可能降。

---

## 34. $\exists S$ 的形状：可行集是**构造集**（A3-3，2026-10-31；2026-11-01 降级）

> **2026-11-01 更正**：本节原写"Zariski 开"，只能主张**构造集**（constructible，Chevalley）——
> 投影不必开。见 [支2](../../archive/workspace_notes/支2.md) §3 与 HANDOVER2 §3.2。另：本节"固定 $S$ 可行"
> 一律应读作 **"$(S)$-可行"**（只查了谱条件；$(A)$ 是独立约束，见 [支1](../../archive/workspace_notes/支1.md) §2）。

### 34.1 结构结论

由 §33，固定 $S$ 的 **$(S)$-可行** $\iff a_0(S)\notin\operatorname{span}\{a_1(S),\dots,a_d(S)\}$。这是
$$\operatorname{rank}\big[a_0;a_1;\dots;a_d\big]>\operatorname{rank}\big[a_1;\dots;a_d\big]$$
——一个**行列式非零**的条件。因此

$$\boxed{\ \text{$(S)$-可行 }S\text{ 集}=\bigcup_{\text{某些子式}}\{\det\ne0\}\ \text{是基族 }\mathcal B_{s,k}\text{ 的\textbf{构造集}（不必开）}\ }$$

**推论**：
- 可行集**要么空、要么稠密开**（在 $\mathcal B_{s,k}$ 的某个不可约分量上）；
- "$\exists S$" 因此是"一个开集是否非空"——标准的 $\exists\mathbb R$ 问题；
- 若可行集非空，则**一般 $S$ 都可行** ⟹ $\pi_S$ 支配 ✓（这就是 A3-2 的支配性问题）。

### 34.2 机器数据

| 实例 | $q$ | $s$ | 扫过 $S$ | 可行 $S$ |
|---|---|---|---|---|
| R17（回归，$S$ 唯一）| 3 | 2 | 1 | **1（可行）** ✓ |
| 第二实例 | 4 | 1 | 13 | 0 |
| 第二实例 | 3 | 1 / 2 | 13 / 25 | 0 / 0 |

**与 `c293`（直接枚举 $U$ + `spectral_gcd`）完全一致** ✓——两种独立判据同结论。

### 34.3 诚实说明

- 第二实例在已扫范围内**恒空** ⟹ 它的可行集在 $\mathcal B_{s,k}$ 上是**空的开集**（即补集全空间）——
  与"$q_{\min}=5$"一致（**注**：$q_{\min}=5$ 已于 2026-11-01 撤回；实例实际无解，见 §32.5 的撤回注）；
- 尚未找到"可行集既非空又非全空间"的实例；要有这样的实例才能看清边界（这需要新构造）；
- 结论标 `[已证-纸面]`（开性）+ `[精确验证]`（表格）。

### 34.4 对 A3-4 的意义

$$\exists S\ \text{可行}\iff \text{基族里存在 }S\text{ 使某个行列式非零}$$

这是**有限**的代数条件（行列式是关于 $S$ 的多项式），因此 $\mathrm{DEC}(q)$ 的 $\exists S$ 部分有一个
**显式的 $\exists\mathbb R$ 编码**——不需要 Bézout 证书，也不需要多项式标架。

---

## 35. A3-4：$q1$ 的显式编码——$\exists Z$ 使行列式非零（2026-10-31）

### 35.1 去基化（关键）

§33 的 $a_j$ 用了 $H/S$ 的坐标基（随 $S$ 变）。**去基化**的做法是回到**固定的 $W$**：

由 $U\subseteq H$（A2 的可容许约束）有 $U\cap I_\lambda=U\cap\operatorname{im}P(\lambda)$，而 $Z:=U+S$ 满足
$$Z\subseteq H,\quad S\subseteq Z,\quad \dim Z=d=s+r,\quad Z\cap G=S .$$
于是**固定 $S$ 的 $(S)$-可行** $\iff\exists Z$ 满足上述约束且
$$q_Z(\lambda):=\det[\,Z\mid P(\lambda)\,]\ \text{是非零常数}.$$

这里 $P(\lambda)$ 的列是 $(A-\lambda I)v$，$v$ 跑 $\mathcal V$ 的基——**全程在固定的 $W$ 里，不出现 $S$ 的坐标选择** ✓

$q_Z$ 对 $Z$ 的 Plücker 坐标 $p_Z\in\Lambda^dW$ 是**线性**的：
$$q_Z(\lambda)=\sum_{j=0}^{\deg}\lambda^j\langle a_j,p_Z\rangle,\qquad a_j\in\Lambda^dW^*.$$

### 35.2 编码（A3-4a，显式）

变量：$p_Z$（$\binom{w}{d}$ 个 Plücker 坐标）、$S$ 的 Plücker 坐标（若 $S$ 也作为变量）。

约束：
1. **Plücker 关系**（$Z$ 与 $S$ 各一组，二次）；
2. **结构约束**：$S\subseteq Z\subseteq H$、$\dim$ 固定、$Z\cap G=S$（线性/秩条件）；
3. **判据**：$\langle a_0,p_Z\rangle\ne0$ 且 $\langle a_j,p_Z\rangle=0\ (j\ge1)$。

$$\boxed{\ \mathrm{DEC}(q)\ \text{可行}\iff\exists S\,\exists Z:\ \text{(1)(2)(3)}\ }$$

**规模**：变量 $\binom{w}{d}+\binom{b}{s}$ 个；方程数与 $\deg\le t$ 同阶；全部是**多项式**。
这是 $\exists\mathbb R$ 的直接编码（与 §25 的定理 B 一致，只差去基化）。

### 35.3 诚实说明

- **实现状态**：§33 的 `coeff_forms_of_S` 用 $H/S$ 坐标（对固定 $S$ 正确、已验证）；**去基化的 $a_j$ 尚未实现**
  （需要把 $(d+t)$-子式的和按 $d$-子集重组，比固定补集的 `coeff_forms` 多一层）；
- 这是**编码**，不是复杂度下界；
- $Z\cap G=S$ 是秩条件，写进系统时是"某个子式非零"，与 (3) 的"非零"同型。

---

## 36. 第一个"**部分可行**"的实例（A3-3 的边界，2026-10-31）

### 36.1 系数判据的适用条件（重要）

§33 的系数判据要求 $[U\mid P_H]$ 的列数 $r+t$ 等于 $H/S$ 的维数 $m$：
$$t=m-r\iff v-s=(h-s)-(d-s)\iff \boxed{q=w-h+v-s}$$
**只有一个 $q$ 满足**（对给定 $s$）。其它 $q$ 上 $P_H$ 的列数与 $m$ 不符，判据要退回"gcd of minors"
（`feasible_by_minors`）。这是 §33 的**适用域**，之前没写清楚。

### 36.2 随机搜索（`archive/attempts_2026-10/A3_basefamily/scripts/c297`）

$n\in\{6,7,8\}$、$p\in\{1,2\}$、随机稀疏整数 $A$，取平衡 $q$、$s=1$、扫 $\operatorname{Gr}(1,D)$ 的格点：

| 统计 | 数 |
|---|---|
| 有效 sweep（$\ge4$ 个 $S$）| 26 |
| 全不可行 | 25 |
| 全可行 | 0 |
| **混合** | **1** |

$$\boxed{\ \text{第一个混合实例：}n=7,\ p=2,\ w=5,\ h=4,\ b=2,\ \dim D=3,\ q=3,\ s=1\ \Longrightarrow\ 3/4\ \text{可行}\ }$$

### 36.3 验证

| 检验 | 结果 |
|---|---|
| 可行 $S$ 加 $\pm10\%$ 扰动 | **6/6 仍可行** ✓（开性的证据）|
| 与直接判据（`feasible_by_minors`）对照 | **0 不一致** ✓ |

### 36.4 意义

- 可行集**确实可以是真开子集**（3/4），所以 §34 的"Zariski 开"不是空话；
- 但**混合实例很稀有**（26 个有效 sweep 里只有 1 个）——多数情形要么全可行要么全不可行；
- 这给出 A3-2/A3-3 的一个真实测试点：边界存在，且可行侧是开集。

---

## 37. **更正**：系数判据缺了 $U\cap G=S$ 的约束（2026-10-31，端到端检验发现）

### 37.1 错在哪

§33 写的是"谱可行 $\iff a_0\notin\operatorname{span}\{a_j\}$"。**端到端检验（`archive/attempts_2026-10/A3_basefamily/scripts/c298`）证明这不够**：

在第一个混合实例上，判据说 3 个 $S$ 可行，但把解出的 $u$ 造回 $U$ 后，**独立检验 $(A)$ 与 $(S)$ 全部失败**。

**原因**：$K=\bigcap_{j\ge1}\ker a_j$ 里的 $u$ 只保证 $q_U$ 是常系数多项式，
但 A2 的可容许性还要求 $U\cap G=S$（即 $u\notin G/S$）。若 $K\subseteq G/S$，则**没有**可容许的 $u$。

### 37.2 正确的判据

$$\boxed{\ \text{可行}\iff\exists u\in K\setminus (G/S):\ \langle a_0,u\rangle\ne0\ }$$

- 若 $K\subseteq G/S$：即使 $a_0\notin\operatorname{span}\{a_j\}$ 也**不可行**；
- 否则条件等价于 $a_0$ 在 $K$ 上不恒零且 $K\not\subseteq G/S$ 可同时满足。

### 37.3 为什么之前没发现

- `c293`（A3-2 的扫描）用的是**直接枚举 $U$ + `spectral_gcd`**——它把 $U\cap G=S$ 作为枚举约束，所以**没出错**；
- `archive/attempts_2026-10/A3_basefamily/scripts/c296`/`archive/attempts_2026-10/A3_basefamily/scripts/c297` 用系数判据只判"存在常数 $q_U$"，**漏了另一条约束**——端到端检验才发现。

### 37.4 影响

| 结论 | 是否受影响 |
|---|---|
| A3-2 的扫描数据（第二实例 $q_{\min}=5$）| ❌ 不受影响（用的是直接判据）——**但 $q_{\min}=5$ 已于 2026-11-01 撤回：实例无解（$q_{\min}=\infty$），见 §32.5** |
| §34 "可行集是 Zariski 开集" | 结论仍成立（新条件仍是行列式/线性条件），但**表述要改** |
| §36 的"混合实例" | **作废**——那是系数判据的假阳性，需用直接判据重做 |
| A3-1 的 "$a_j$ 算法" | ✓ 不受影响（$a_j$ 本身算对了）|

**教训**（记进 CLAUDE 纪律）：判据的**每一条约束**都必须进入检验；"存在性"判据尤其容易漏掉可容许性约束。

---

## 38. **重大更正**（QA25 回复，2026-11-01）：可分解性 = G3 才是真正的障碍

### 38.1 撤回的断言

§33 的 "$\text{可行}\iff a_0\notin\operatorname{span}\{a_j\}$" **一般不成立**（§37 的补丁也不够）。

**原因**：$a_0\notin\operatorname{span}\{a_j\}\iff K\not\subseteq\ker a_0$，其中
$K=\bigcap_{j\ge1}\ker a_j\subseteq\Lambda^r E$ 是**线性**子空间；而真正的 $U$ 要求 $p_U$ **可分解**。
$$\underbrace{K\not\subseteq\ker a_0}_{\text{线性代数}}\ne\underbrace{D(K)\not\subseteq\ker a_0}_{\text{真可行性}},\qquad D(K)=\operatorname{span}\{x\in K:x\ \text{可分解}\}.$$
线性判据成立 $\iff D(K)=K$——**这正是 G3**。

### 38.2 为什么 c282 通过

$r=1$ 时 $\Lambda^1E=E$ 的**每个**非零向量都可分解 ⟹ $D(K)=K$ **自动成立** ⟹ 无 G3 障碍。
c282 恰好是 $r=1$ ⟹ 它通过是**结构性的**，不只是坐标问题。

### 38.3 两个更正

**(a) 类型错误**：$K\subseteq\Lambda^r(H/S)$ 与 $G/S\subseteq H/S$ 是**不同空间**，"$K\not\subseteq G/S$" 无意义。
正确写法（$E=H/S$、$B=G/S$、$T=T_S$）：
$$\mathcal F_S=\{U\in\operatorname{Gr}(r,E):\ T\subseteq U,\ U\cap B=0,\ p_U\in\mathbb P(K),\ a_0(p_U)\ne0\},\qquad \text{可行}\iff\mathcal F_S\ne\varnothing,$$
等价地 $X_S\cap\mathbb P(K)\not\subseteq\mathbb P(\ker a_0)$（$X_S$ = 可容许 $U$ 的 Plücker 轨迹）。

**(b) 无坐标写法**：取 $\eta\in\Lambda^tD$，$b(\lambda)=\Lambda^tP(\lambda)(\eta)=\sum_j\lambda^jb_j\in\Lambda^tE$，则
$$q_U(\lambda)=\omega(p_U\wedge b(\lambda))=\sum_j\lambda^j\,\omega(p_U\wedge b_j).$$
换基只把所有 $a_j$ **同乘**一个非零常数 ⟹ 判据与基无关 ✓（但**不消除**可分解性）。

### 38.4 其它修订

- **非平衡情形**：只有 $r+t>m$ 必然不可行；$r+t\le m$ 用 $\gcd$ of $(r+t)$-子式（§27 的 `feasible_by_minors` 已正确）；
- **A3-3**：投影只保证**构造集**（constructible），不是自动 Zariski 开——需额外论证；
- **A3-4**：Bézout 编码是主路线，**不依赖** $a_j$。

### 38.5 现在的中心问题

$$\boxed{\ \text{在 }\mathrm{DEC}(q)\text{ 构造给出的 }K_S\text{ 上，是否总有 }D(K_S)=K_S\ ?\ }$$
若不成立，是否至少有 $a_0(S)\notin D_{\mathrm{adm}}(K_S)^\perp$？——这**就是 G3**，现在与 A3 合并。

---

## 39. **更正**：单行列式判据的适用条件（分支 4 发现，2026-11-01）

$[U\mid P(\lambda)]$ 是 $(w-s)\times(r+t)$ 矩阵。**只有当 $r+t=w-s$（方阵）时**，
"一个行列式"才等价于"全部极大子式"。此前（§33–§38）用的 $r+t=m=\dim(H/S)$ **不是**这个条件。

$$\boxed{\ \text{正确判据}=\gcd\ \text{of all }(r+t)\text{-minors（§27 的 `feasible_by_minors`）}；\ 单行列式只在 }r+t=w-s\text{ 时够.}\ }$$

**c282 的检验**：$r+t=1+3=4$、$w-s=5$ ⟹ 非方阵（5 个极大子式）；单行列式判据在那 80 个点上
"碰巧"与直接判据一致（其余子式冗余），但**一般情形不保证**。

**这是 §33–§38 那串错误的又一个来源**，与可分解性（QA25）**独立**。

**adapted basis**：`coeff_of_S.adapted_basis` 已验证（c282 上 $T^{-1}(H/S)=\operatorname{span}(e_1..e_m)$ ✓，
脚本 `archive/attempts_2026-10/A3_basefamily/scripts/verify_adapted_basis.py`）。

---

## 40. 方阵情形的**验证结果**与结论（分支 4，2026-11-01）

### 40.1 适用条件：$q=t$

$[U\mid P(\lambda)]$ 是 $(w-s)\times(r+t)$。用 $t=v-s$、$r=w-q-s$ 得
$$\boxed{\ r+t=w-q+v-2s,\qquad r+t=w-s\iff q=t\ }$$
（**不是** $q\le t$，也不是 $r+t=m$。**2026-11-01 更正**：原文写"$r+t=w-q$"是笔误——
c282 上 $r=1,t=3$，$r+t=4$ 而 $w-q=2$；见 HANDOVER2 §3.1。）

### 40.2 机器验证（`archive/attempts_2026-10/A3_basefamily/scripts/verify_square_case.py`）

| 实例 | $q$ | $s$ | 方阵? | $T^{-1}(H/S)$ | 换基缩放恒等式 |
|---|---|---|---|---|---|
| 第二实例 | 2 | 2 | ✓（$q=t=2$）| ✓ | **6/6** |
| 第二实例 | 3 | 1 | ✓（$q=t=3$）| ✓ | **6/6** |
| 第二实例 | 2 | 1 | ✗（$q\ne t$）| — | 不适用 |
| R17 | 2 | 1 | ✗（$q\ne t$）| — | 不适用 |

**换基缩放** $\det[U_{\rm new}|P_{\rm new}]=\det(T^{-1})\det[U_{\rm old}|P_{\rm old}]$ 在两个方阵实例上**全部通过** ✓

### 40.3 两个更正

**(a) 截断是错的**：我曾想"只用 $P$ 的前 $m$ 行"（因为 $U$ 的支撑在前 $m$ 个坐标）。**这不对**——
满 $wm\times wm$ 行列式沿 $U$ 的列展开是 $\sum_i u_i C_i$（$C_i$ 涉及 $P$ 的其余行），
不是 $\det[U_{1..m}\mid P_{1..m}]$。机器检验：**0/6** ✗

**(b) adapted basis 不是必需的**：方阵情形下，直接对**完整**的 $\det[U\mid P(\lambda)]$ 展开即可；
换基只把行列式乘一个非零常数（40.2 已验证）。专家 QA25 §3 的 basis-free 公式正是这个意思。

### 40.4 结论

$$\boxed{\ \text{系 数判据}（a_0\notin\operatorname{span}\{a_j\}）\ \text{只在}\ q=t\ \text{时可直接用；判据}=\det[U\mid P(\lambda)]\ \text{为非零常数}.\ }$$

- $q=t$：可用（无需 adapted basis、无需截断）；
- $q\ne t$：$[U\mid P]$ 非方阵 ⟹ 必须用**全部** $(r+t)$-子式的 gcd（§27 的 `feasible_by_minors`）；
- 可分解性（QA25）仍独立存在：即使 $q=t$，$a_0\notin\operatorname{span}\{a_j\}$ 仍只是**充分**条件
  （需要 $D(K)=K$）。

---

## 41. 行列式恒等式的**逐系数验证**（A-1 的核心，分支 4，2026-11-01）

### 41.1 命题

$q=t$（方阵）且 $r=1$ 时：
$$\det\big[U\mid P(\lambda)\big]=\pm\sum_{j=0}^{\deg}\lambda^j\,\langle a_j,u\rangle,$$
其中 $a_j$ 由 `coeff_space.coeff_forms([P0,P1], w-s, 1)` 给出；$\pm$ 是**整体的符号约定**
（列序/Plücker 记号的顺序），与"是否为零/是否为非零常数"无关。

### 41.2 机器验证（`archive/attempts_2026-10/A3_basefamily/scripts/verify_det_identity.py`）

| 实例 | $q$ | $s$ | $w-s$ | $r$ | $t$ | 方阵 | 逐系数恒等 |
|---|---|---|---|---|---|---|---|
| 第二实例 | 2 | 2 | 3 | 1 | 2 | ✓ | **8/8** |
| 第二实例 | 3 | 1 | 4 | 1 | 3 | ✓ | **8/8** |
| c282 | 4 | 1 | 5 | 1 | 3 | ✗（$q\ne t$）| 跳过（判据不适用）|

**这是 A-1 的第一步在 $r=1$、方阵情形下的完成。**

### 41.3 符号的来源

两个实例里 $q=3,s=1$ 给 $-1$、$q=2,s=2$ 给 $+1$。符号由
$\det[U\mid P]$ 的列序与 `coeff_forms` 遍历 Plücker 坐标的次序共同决定，
**是一个 $\pm1$ 的常数**，不是 $\lambda$ 的函数 ⟹ 不影响判据 ✓

### 41.4 剩下的

- $r\ge2$：需把 $[U\mid P]$ 的行列式按 $r$ 个 $U$ 列做多重线性展开（对 $p_U$ 仍线性）；
- $q\ne t$（非方阵）：必须用全部 $(r+t)$-子式的 gcd（§27）；
- 可分解性（§38）：独立于坐标，仍需单独处理。

### 41.5 $r\ge2$：R17（$q=2$、$s=2$，$r=2$、$t=2$、$w-s=4$）的验证

`archive/attempts_2026-10/A3_basefamily/scripts/verify_det_identity_r2.py`：

1. 用**坐标子空间** $U=\operatorname{span}(e_{i_1},e_{i_2})$ 定出每个 Plücker 坐标的符号：
   6 个坐标里 4 个给 $+1$、2 个**恒为零**（无关紧要）⟹ 全部 $+1$ ✓
2. 随机 $U$（$2\times4$ 矩阵、列满秩）：逐系数比较 $\det[U\mid P(\lambda)]$ 与 $\sum_j\lambda^j\langle a_j,p_U\rangle$

$$\boxed{\ \text{逐系数恒等：}\mathbf{8/8}\ }$$

**⟹ A-1 的核心恒等式在 $r=1$（两个实例）与 $r=2$（R17）上都成立**，且**无需任何符号修正**
（`coeff_forms` 的补集/次序约定与 Laplace 展开一致）。

### 41.6 剩下的

- $r\ge3$：未验证（结构上同一展开，但需要更大的实例；$G(3,\cdot)$ 目前没有可用实例）；
- 非方阵（$q\ne t$）：判据退回"全部子式的 gcd" ✓（§27）；
- 可分解性（§38）：独立，仍需单独处理。

### 41.7 $r=3$：验证通过 + 符号是**逐坐标**的

`archive/attempts_2026-10/A3_basefamily/scripts/verify_det_identity_r3.py`（需要 $p\ge3$，因为 $r\le w-v\le p$）：

| 实例 | $n$ | $p$ | $s$ | $w-s$ | $r$ | $t$ | $q$ | 符号 | 逐系数恒等 |
|---|---|---|---|---|---|---|---|---|---|
| trial14 | 8 | 3 | 1 | 4 | 3 | 1 | 1 | 全 $+1$ | **8/8** |
| trial20 | 9 | 3 | 1 | 5 | 3 | 2 | 2 | 一个 $-1$，其余 $+1$ | **8/8** |

**修正 §41.1 的表述**：恒等式应写成
$$\det[U\mid P(\lambda)]=\sum_j\lambda^j\Big(\sum_{|I|=r}s_I\,a_j[I]\,p_U[I]\Big),\qquad s_I=\pm1,$$
$s_I$ 是**逐坐标**的符号（由坐标子空间 $U=\operatorname{span}(e_I)$ 定出），不是整体常数。

**为什么判据不受影响**：$s=(s_I)$ 可逆对角 ⟹
$$a_0\in\operatorname{span}\{a_j\}\iff s\cdot a_0\in\operatorname{span}\{s\cdot a_j\}.$$
所以 "$a_0\notin\operatorname{span}\{a_j\}$" 与符号约定无关 ✓（但**写恒等式时**必须带上 $s_I$）。

### 41.8 结构观察：$r\le p$

$$r=d-s=w-q-s\ \le\ w-v\ \le\ p,$$
第一个不等号用 $s=\dim(Z\cap V)\ge v+d-w=v-q$（因 $V,Z\subseteq W$），第二个用 $v=\dim\ker[C;CA]\ge n-2p=w-p$。
故 $r=3$ 必须有 $p\ge3$——这与 A2 §22 的 $r\le p-1$ 同源。

> **2026-11-01 更正**：原文写"$r=w-v$"，**不是恒等式**（c282：$r=1$ 而 $w-v=2$）；正确式是上式。
> 见 HANDOVER2 §3.1/Q3。同一笔误出现在 §41.7 的括注里（已改）。

### 41.9 判据（不只是恒等式）的验证：方阵、$r=1$

`archive/attempts_2026-10/A3_basefamily/scripts/verify_criterion_square_r1.py` 同时检查**直接侧**与**判据侧**
（含可容许性 $T_S\subseteq U$、$U\notin G/S$）：

| 实例 | 可容许 $u$ | 直接可行 | 判据可行 | 不一致 |
|---|---|---|---|---|
| 第二实例 $q=2,s=2$ | 120 | 0 | 0 | **0**（但**无 True 点 ⟹ 空检验**）|
| 第二实例 $q=3,s=1$ | 600 | 0 | 0 | **0**（同上，空检验）|
| **trial60**（$n=6,p=2,s=2$，$q=1$）| 24 | **4** | **4** | **0** ✓ |

**trial60 是关键**：它是唯一含 **True 点**的方阵 $r=1$ 实例（CLAUDE §10.2 的"地基检查"要求至少一个 True 点）。

$$\boxed{\ \text{方阵、}r=1\text{：}a_j\text{ 判据}=\text{直接判据（含可容许性）——含 True 点，0 不一致}\ }$$

**注意**：$r=1$ 时 $D(K)=K$ 自动成立（QA25 §1.2），所以这里判据是**充要**的；
$r\ge2$ 时它只是**充分**的（G3 障碍真实存在）。

