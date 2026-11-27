# 层程序（$c=1$ 部分）：完整状态

> **对应 docs 条目**：C.1（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

> 这是 $c=1$ 这一支的**总览**，把 [proof/rho1_layer/theorem.md](../rho1_layer/theorem.md) §9–§19 串成一篇可独立阅读的文档。
> 写作原则：每条都标等级；**没证的地方明说没证**（纪律 18）。

---

## 0. 为什么只看 $c=1$

$$q_{\min}=\min\{(\rho+c):(\rho,c)\ \text{可达}\},\qquad \rho_{ci}=P(T,B,U_0)\ \text{已可算}\ (O(n^4)).$$

层程序的目标是逐层判定"$(\rho,c)$ 是否可达"。
$c=1$ 是 $c$ 的下界（[docs/02](../../docs/02_theorems_proven.md) A.2：$c\ge\max(c_0,1)$），
所以 $(k,1)$ 层是**最先可能可行**的层，也是把层程序跑通的最小测试。

---

## 1. 基本形状

固定 $(\mathcal U,\mathcal H)$：$\dim\mathcal U=k$、$\mathcal H=\langle h\rangle$、$w=\beta(h)\in B$。$Q_{\mathcal V}(\lambda)$ 的行是
$$\lambda u_i-r_i(\tau)\ (i=1,\dots,k),\qquad -w .$$

$$(5b)\iff \operatorname{rank}Q_{\mathcal V}(\lambda)=k\quad\forall\lambda\iff\text{全部 }k\times k\text{ 子式无公根}.$$

---

## 2. 已证的定理（按逻辑顺序）

| # | 命题 | 等级 | 位置 |
|---|---|---|---|
| T1 | $(5b)$ 失败 $\iff\exists\lambda$ 与 $\dim\le k-1$ 的 $W_0\ni w$ 装下所有行 | [已证] | theorem.md 引理 14.1 |
| T2 | 固定 $W_0$ 时 $\{(\tau,\lambda):\lambda u_i-r_i\in W_0\}$ 是**仿射**的 | [已证] | 引理 14.2 |
| T3 | $\mathrm{Bad}=\bigcup_{W_0}\pi_\tau(\mathfrak S_{W_0})$：Grassmannian 上一族仿射集的并 | [已证] | 定理 14.3 |
| T4 | $k=2$ 时 $W_0=\langle w\rangle$ **唯一** ⟹ $\mathrm{Bad}$ **仿射** | [已证] | 推论 14.4 |
| T5 | $k\ge3$ 时 $W_0=\langle w,x\rangle$ 不唯一 ⟹ $\mathrm{Bad}$ 是投影 | [已证] | 推论 14.5 |
| T6 | $(2,1)$：$\exists\tau\in\mathcal A\setminus\mathrm{Bad}\iff\dim\mathrm{Bad}<\dim\mathcal A$ | [已证] | 定理 10.1 |
| T7 | $(2,1)$，$w\ne0$：失败 $\iff\exists\lambda:\lambda u_i-r_i\in\langle w\rangle$（坏集仿射） | [已证] | 定理 9.10 |
| T8 | $(2,1)$，$w=0$：该 $(\mathcal U,\mathcal H)$ **恒不可行**（首一二次必有根）| [已证] | 定理 9.12 |
| T9 | Bézout 线性化：$\exists\tau:\rank\Phi_D(\tau)$ 满 $=$ 存在极大子式在 $\mathcal A$ 上不恒零 | [已证]（⟸ 方向）| 引理 17.1 |
| T10 | $m=2$ 时 $\rank\Phi_D=D+\max\deg q_j+1$ ⟹ $\gcd=1\Rightarrow$ 行满秩（$D\ge d$）| [已证] | 定理 18.1/推论 18.2 |
| T11 | $m\ge3$ 的同款断言 | **[已证]** 定理 27.2（对 $m$ 归纳 + 单调性；界 $2d(m-1)$）；[精确验证 195/195] | §27 |

---

## 3. 逻辑路径

$$\underbrace{(2,1)\ \text{完整可判}}_{\text{T6–T8}}\qquad
\underbrace{(k,1)\ \text{要}\ \text{T9}+\text{T11}}_{\text{缺 T11}}$$

- **$(2,1)$**：$W_0$ 唯一 ⟹ 坏集仿射 ⟹ "$\mathcal A\subseteq\mathrm{Bad}$" 是两个仿射子空间的包含 ⟹ 线性代数 ⟹ 多项式。
  再加 $w=0$ 的排除（T8），$(2,1)$ 层**完全结束**。
- **$(k,1)$，$k\ge3$**：坏集是投影 ⟹ 直接判定是 $\forall\exists$ 型。**绕过办法**（T9）：不用 $\mathrm{Bad}$ 的方程，
  直接选 Bézout 乘法映射 $\Phi_D$ 的一个极大子式 $\Delta$，判"$\Delta$ 在 $\mathcal A$ 上是否恒零"——系数比较，与次数无关。
  T9 的"⟸"已证；T9 需要的"⟹"就是 T11（$\gcd=1\Rightarrow$ 某 $D$ 满秩）。

---

## 4. 唯一的缺口（T11）

**待证引理**：设 $p_1,\dots,p_m\in\mathbb C[\lambda]$、$\deg\le d$、$\gcd=1$。则 $D\ge D_0(d,m)$ 时
$$\dim\{(a_j):\textstyle\sum_j a_jp_j=0,\ \deg a_j\le D\}=(m-1)(D+1)-d .$$

**已做**：$m=2$ 完整证明（定理 18.1）。
**已查**：$m=3,4$ 的 192 个样本（$d\le3$，$D=0..5$）在 $D\ge d$ 时全部满秩（3 个失败都在 $D=0<d$）。
**未做**：$m\ge3$ 的证明。缺的是 **syzygy 模的 Hilbert 函数**：
$\mathrm{Syz}$ 是自由模（$0\to\mathrm{Syz}\to R^m\to R\to0$ 分裂），但**分级**不平凡——
Koszul 关系生成它，而它们之间有"第二 syzygy"，所以 Koszul 计数只是高估（§19.2 有手算反例）。

---

## 5. 这一支对 $q1$ 的意义

| 情形 | 结论 |
|---|---|
| T11 成立 | 所有 $(k,1)$ 层多项式可判 ⟹ $c=1$ 的层程序闭环 ⟹ 对 $q1$ 的"假"提供了**一个完整分支** |
| T11 为假 | 那 $(k,1)$ 层的判定需要别的方法；$q1$ 的"强 hard"路线仍开放 |

**注意范围**：即使 $c=1$ 全部解决，$c\ge2$ 的层仍未处理（那里 $\mathcal H$ 的维数 $\ge2$，$W_0$ 的自由度更大）。
所以 $c=1$ 闭环**不等于** $q1$ 解决；它的价值是：**给出第一个"整层可判"的非平凡例子**，为 $c\ge2$ 提供模板。

---

## 6. 文件

| 文件 | 内容 |
|---|---|
| [../rho1_layer/theorem.md](../rho1_layer/theorem.md) | 全部证明：§9–§13（$(2,1)$）、§14（$(k,1)$ 结构）、§15–§16（次数与结）、§17–§19（Bézout 与缺口）|
| [../rho1_layer/README.md](../rho1_layer/README.md) | 状态摘要 |
| `../rho1_layer/verify.py` | T7 的逐点复核（1605/1605，**验证非证明**）|
| `../rho1_layer/verify_conv114.py` | 猜想 11.4 的反例（5/5，**验证非证明**）|
| `../rho1_layer/strat_d3.py` | $d=3$ 分层实验（**验证非证明**）|

---

## 7. 补记（§20）：$(5b)$ 的拆分

$$(5b)\iff\underbrace{\text{全部}(k+1)\times(k+1)\text{子式}\equiv0}_{(\mathrm{b})\ \text{闭条件，完全多项式}}\ \wedge\ \underbrace{\text{全部}k\times k\text{子式无公根}}_{(\mathrm{a})\ \text{开条件，需 T11}}$$

| 命题 | 等级 |
|---|---|
| $(\mathrm{b})$ 的判定 = 系数比较（线性代数）| [已证] 命题 20.1 |
| **充分判据**：某两个 $k\times k$ 子式互素（在 $\mathcal A$ 上某点）⟹ 层可行 | [已证] 定理 20.2（用 T10）|
| 全组互素（$(\mathrm{a})$ 的完整判定）| 需 T11 |

---

## 8. 一般 $(\rho,c)$（§21）：一个已证的"线性可判"判据

**定理 21.4（已证）** 允许的容器 $W_0$（$\dim\le\rho-1$、$\supseteq\beta(\mathcal H)$）是**单点** $\iff\dim\beta(\mathcal H)=\rho-1$。

**推论 21.5（已证）** 当 $\dim\beta(\mathcal H)=\rho-1$ 时，$\mathrm{Bad}$ 仿射、$\mathrm{Bad}\subseteq\mathcal A$，于是
$$\exists\tau\in\mathcal A\setminus\mathrm{Bad}\iff\dim\mathrm{Bad}<\dim\mathcal A .$$

| 层 | $b=\dim\beta(\mathcal H)$ vs $\rho-1$ | 线性可判？ |
|---|---|---|
| $(2,1),w\ne0$ | $1=1$ | ✓（$(2,1)$ 的**一般来源**）|
| $(3,2)$ | $2=2$ | **✓** |
| $(k,1),k\ge3$ | $1<k-1$ | ✗（需 Bézout/T11）|
| $c\ge\rho-1$ 的层 | 可取等号 | **✓**（$\mathcal H$ 可选）|

$$\boxed{\ \dim\beta(\mathcal H)=\rho-1\ \text{的层，判定 = 维数比较（线性代数）}\ }$$

---

## 9. 层判据总表（2026-10-29 定稿）

记号：$\mathsf L(\rho,c)$ = "第 $(\rho,c)$ 层可行"；$j=\dim\mathcal J$、$d=n-j$；$\beta(h)=\pi(hA)$；
$\mathcal A$ 是固定 $(\mathcal U,\mathcal H)$ 后 $\tau$ 的仿射可行集；$\mathrm{Bad}$ 是 $(5b)$ 的失效集。

| 层 / 情形 | 判据 | 等级 | 位置 |
|---|---|---|---|
| $\rho=0$ | $\mathcal V\subseteq\mathcal J$，$(5b)$ 自动 | **[已证]** | docs/02 B.3 |
| $\rho=d$ | $(D_W^{\mathsf T},T_W)$ **可观测**（PBH）| **[已证]** + 65/65 | proof/top_layer_observability |
| $\rho=d$ 且 $c_0=1$ | $v_W$ 是 $T_W$ 的**循环向量** | **[已证]** + 35/35 | proof/cyclic_vector_criterion |
| $(2,1)$，$w\ne0$ | $\mathrm{Bad}$ 仿射 ⟹ $\exists\tau\in\mathcal A\setminus\mathrm{Bad}\iff\dim\mathrm{Bad}<\dim\mathcal A$ | **[已证]** + 1605/1605 | theorem.md §9.10/§10.1 |
| $(2,1)$，$w=0$ | **恒不可行** | **[已证]** + 423/423 | theorem.md §9.12 + verify_9_12.py |
| $c\ge\rho-1$、$\dim\beta(\mathcal H)=\rho-1$、**固定** $(\mathcal U,\mathcal H)$ | $\mathrm{Bad}$ 仿射、$\mathrm{Bad}\subseteq\mathcal A$ ⟹ 可行 $\iff\dim\mathrm{Bad}<\dim\mathcal A$（$O(n^3)$）| **[已证]** + 200 例（0 mix）| theorem.md 定理 29.1 + verify_29_1.py |
| $c\ge\rho-1$、**固定** $(\mathcal U,\mathcal H)$、$\dim\beta(\mathcal H)<\rho-1$ | 容器不唯一 ⟹ 只知"$\dim\beta(\mathcal H)$ 取最大不劣"（单调性）| 部分 | theorem.md §25.1 |
| $(3,1)$、$\mathcal U\subseteq B$（$\tau$ 自由）、$w\ne0$ | 型层**不被**覆盖 ⟹ 可行（构造 $C$ 对角互异）| **[已证]** + 200/200 | [rho3c1_free_tau.md](../rho1_layer/rho3c1_free_tau.md) |
| **层级别**（$\exists(\mathcal U,\mathcal H)$）| **无判据** ✗ | 开放 | theorem.md §28.3 |
| $\tau$ 量词 | "某极大子式在 $\mathcal A$ 上不恒零" = **有限**代数判据 ✓；$\rho$ 固定时多项式 ✓，$\rho$ 随 $n$ 增长时规模指数级 ✗（2026-10-29 更正）| 部分 | theorem.md §17/§27 |
| 复杂度 | 可判定（$\exists\mathbb C$-消去）✓；能否多项式 ✗ | 开放 | theorem.md §30 |

### 已排除的"判据"（不要重试）

| 曾以为是判据的东西 | 否证方式 |
|---|---|
| $\dim K\ge\rho$（$K=\{b\in B:T(b)\in B\}$）| 精确反例（$n{=}4,\rho{=}2,c{=}1$）|
| 任何只看 $(\rho,c,\mu,\nu)$ 的判据 | $(3,1,1,0)$：354 可行 / 160 不可行 |
| 任何只看 $(\rho,\mu,\nu,\kappa)$ 的判据（$\kappa$ 为 $E$ 的零方向维数）| 4 个组合全部分歧 |

$$\boxed{\ \text{层程序的难点}=\exists(\mathcal U,\mathcal H)\ \text{（Grassmannian 搜索）},\ \text{且它不可能由任何秩型不变量决定}\ }$$

> **技术债**：商空间 $X=\mathbb C^n/\mathcal J$ 尚未实现 ✗ —— 见 [TECH_DEBT_quotient.md](TECH_DEBT_quotient.md)。
