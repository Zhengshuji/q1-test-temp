# 判据矩阵、复核记录与经验结论（原 docs/02 的非命题内容）

本文件收留原先混在 `docs/02_theorems_proven.md` 里的三类内容：
（i）参考表（判据矩阵 I.1–I.5）；（ii）复核记录；（iii）纯经验/精确验证结论（B.30/B.34/B.35/B.36）。
按 CLAUDE §2/§5.1，它们不属于"已证命题"，故移出 docs。

## 附录 B：判据矩阵（原 `## I.`）

## I. 判据矩阵（判据 × 域 × 强度 × 证据）

> 这是交接文档 §3 的**固化版**。**不知道域就会用错判据**——上一阶段正是这样错的。

| # | 判据 | 适用域 | 对 $(S)$ 的强度 | 依据 | 等级 |
|---|---|---|---|---|---|
| I.1 | 全部 $(r+t)$-子式的 gcd 是非零常数 | 任意 $q$（$r+t\le w_m$；$r+t>w_m$ 恒不可行）| **充要** | B.1 + H.1 | [已证-纸面] |
| I.2 | 单个 $\det[U\mid P(\lambda)]$ 是非零常数 | **仅 $q=t$**（$r+t=w_m$，方阵）| **充要** | H.2 + Laplace 恒等式 | [已证-纸面] + [精确验证] |
| I.3 | 系数判据 C1：$p_U\in K$、$a_0(p_U)\ne0$，且 $p_U$ 可分解、$U$ 可容许 | $q=t$ | **充要** | §3.2 的 C1 | [已证-纸面]（$r\le3$）+ [精确验证] |
| I.4 | 线性松弛 C2：$a_0|_K\ne0$ | 任意 $q$ | **只必要**（C1 ⟹ C2）；$q\ne t$ 时对 $(S)$ 不必需 | §3.2 的 C2 | [已证-纸面] |
| I.5 | 行列式因子 $\Delta_{r+t}$ 是常数（Smith 形）| 任意 $q$ | 与 I.1 同一个量 | §J | [已证-纸面] + [精确验证] |

**三条容易踩的（每条都有实例）**

1. $q\ne t$ 时"单个 $\det$"**不存在**（非方阵）⟹ 用它否定可行性不合法（支 5 的 58 例，2026-11-01 撤回）。
2. $m=r+t$ **不是**方阵条件：方阵 $\iff r+t=w_m\iff q=t$；$m=r+t\iff h=w$（$L_0\subseteq\operatorname{row}C$ 的退化情形）。
   用 $m$ 行对象当 $\det[U\mid P]$ 只在 $H=W$ 时正确（H.2 与 CLAUDE §10.1）。
3. 均匀条件 $D_{\rm adm}(K)=K$ **不成立**：$q=t,r=2$ 上已有 $\dim K\ne0$ 而 $\dim D_{\rm adm}=0$ 的实例
   （12 个 $S$、60 个可容许 $U$），所以 I.4 不能替代 I.3。

## 附录 C：复核记录（原 `## 附：复核`）

## 附：复核

精确算术的实例复核（**验证，不是定理**）在 [proof/README.md](../../../../proof/README.md)。

**A.0（$(5a)$ 的商形式——**再次校正**）** 记 $\mathcal J=\operatorname{row}[C;CA]$、$U=\pi(\mathcal V)$、$B=\pi(\mathcal J A)$。
则
$$(5a)\iff \pi(\mathcal V A)\subseteq\pi(\mathcal V).$$

*证明*：$(5a)\iff\operatorname{row}(\mathcal L A)\subseteq\operatorname{row}\mathcal L+\mathcal J$，两边取 $\pi$。$\square$

**要点（曾两次写错）**：$\pi(xA)$ 在 $X=\mathbb C^n/\mathcal J$ 上**不是良定义的单值映射**，因为 $A(\mathcal J)\not\subseteq\mathcal J$；
这里的偏差恰好是 $B=\pi(\mathcal J A)$。因此正确说法是：

**与此相关的只有单向蕴含**：令 $\overline T:X/B\to X/B$ 由 $A$ 诱导（良定义，因为 $B=\pi(\mathcal J A)$）、
$\overline U=(U+B)/B$，则

$$\overline T(\overline U)\subseteq\overline U\iff\pi(\mathcal V A)\subseteq U+B,$$

而 $(5a)$ 是 $\pi(\mathcal V A)\subseteq U$ —— **更强**。于是只有
$$(5a)\ \Longrightarrow\ \overline T(\overline U)\subseteq\overline U .$$
**反向不成立**：此点由专家 2026-10-30 指出，但**本项目从未复现其反例**；按专家 2026-11-04 §8 的建议，
该否定陈述**先从证明链中撤下**，仅作为"待复核的记录"保留（若复现出来再写回）。
因此本文只使用上面的**单向蕴含**；"枚举 $\overline T$-不变子空间能否替代 $(5a)$"这个问题**保持开放**，
不作断言。$(5a)$ 依赖 $\mathcal V$ 的提升（在层框架里等价于 $\tau\in\mathcal A$，$\mathcal A$ 仿射）✓ ——
这一点不依赖上述否定陈述（它来自 $(5a)\iff\pi(\mathcal V A)\subseteq U$ 与 $U$ 只记录 $\pi(\mathcal V)$ 的维数）。

*等级*：**[已证-纸面]** + **[Lean]**（`A0Row.five_a_row_iff`：$\operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C]\iff\operatorname{row}(\mathcal LA)\le\operatorname{row}[\mathcal L;CA;C]$，即本条的第一步；`A0Row.rank_eq_of_rowSpace_le`：包含 $\Rightarrow$ 秩等式。**差异**：不含再往后的商形式 $\pi(\mathcal V A)\subseteq\pi(\mathcal V)$）。

---

## 附录 D：$(3,1)$ 层格子级判据（原第二处 `## C.`）

## C. $(3,1)$ 层的四条**格子级**判据（2026-10-29）

> **冻结版定理包**：[proof/layer_31_theorems/](../../../../proof/layer_31_theorems/README.md)（C.1–C.5 连同全部假设与证明 ✓；本节保留为索引）。

> 记号见 [01_notation](../../../../docs/01_notation.md)：$\mathcal J$、$X=\mathbb C^n/\mathcal J$、$\pi$、$B=\pi(\mathcal J A)$；
> 层 $(\rho,c)=(3,1)$；一个**格子** = 固定 $(\mathcal U,\mathcal H)$（$\dim\mathcal U=3$、$\mathcal H\subseteq\mathcal J$ 一维、$\beta(\mathcal H)\subseteq\mathcal U$）；
> $E=B\cap\mathcal U$、$\mu=\dim E$；$\tau$ 的自由度使每行可加 $E$ 中元素，故 $C=T+\sum_{k}s_ka_k^{\mathsf T}$（$T$ 以 $\mathbf t_i$ 为行）。
> 格子被**覆盖** ⟺ 所有 $\tau$ 都使 $(5b)$ 失败。

**定理 C.1（$\mu=3$）**：若 $E=\mathcal U$（即 $\mathcal U\subseteq B$）**且 $w\ne0$**，则格子**不被覆盖** ✓。

**定理 C.2（$\mu=1$）**：若 $w\ne0$，则格子不被覆盖 $\iff$ $T$ **没有**与 $a$ 正交的特征向量（$E=\langle a\rangle$）✓。
（**真实实例的状态**（2026-10-30 更正）✗→✓：§52.7 那个 $n=6$ 实例**其实 $w=0$**
——$H=\langle e_5\rangle$、$w=\beta(e_5)=\pi(e_6)=0$ ⟹ 归 **C.5**（恒被覆盖），**不是** C.2 的实例；
修正后的 [verify_mu1_covered_instance.py](../../../../proof/rho1_layer/verify_mu1_covered_instance.py) 三组一致 ✓。
**两个方向现在都有真实实例**（2026-10-30）："被覆盖"见
[verify_mu1_w_ne_0_instance.py](../../../../proof/rho1_layer/verify_mu1_w_ne_0_instance.py)（判据 gcd 次数 $=2$、直接验 25/25）；
"不被覆盖"见 [verify_mu1_w_ne_0_not_covered.py](../../../../proof/rho1_layer/verify_mu1_w_ne_0_not_covered.py)
（判据 gcd 次数 $=0$，且 $\mathcal L=[e_1;e_2;e_3;e_6]$ 满足 $(5a)\wedge(5b)$）。
旧的两个 $\mu=1$ 脚本：一个（`verify_mu1_instance_cell.py`）的 $E$ 取成 $B\setminus U$、且把 $a$ 当 $w$，
已标为不可引用 ✗；C.2 的**纸面证明**不受影响 ✓。）

**定理 C.3（$\mu=2$）**：若 $w\ne0$，则格子不被覆盖 $\iff$ $T$ **没有**落在 $E^{\perp}$ 里的非零特征向量 ✓。

**定理 C.4（$\mu=0$）**：格子**恒被覆盖**（恒不可行）✓。

**定理 C.5（任意 $\mu$，$w=0$）**：若 $w=0$，则格子**恒被覆盖** ✓（与 $\mu$ 无关）。

*证明*：$w=0$ ⟹ 第 4 行恒为零 ⟹ 铅笔秩 = 前三行的秩 ⟹ $(5b)$ ⟺ $\det(\lambda U - C)\ne0$ 对一切 $\lambda$ ✓；
而该行列式是 $\lambda$ 的**三次**多项式（或恒为零）⟹ 由代数基本定理必有根 ⟹ 该处秩降 ⟹ 失败 ✓。$\square$
（2026-10-29 专家指出：C.1–C.3 的陈述漏了 $w\ne0$ ✗；本条补上缺口 ✓。精确验证：$w=0$ 的 120 个格子无一可行 ✓。）

- **证明**：[rho3c1_spectral.md](../../../../proof/rho1_layer/rho3c1_spectral.md)（引理 1、定理 2、定理 5、定理 11）
  与 [RESTRICTED_COMPLETION_MODEL.md](../../../../proof/layer_program/RESTRICTED_COMPLETION_MODEL.md)（定理 2、19）。
- **等级**：**【已证-纸面】**；其中三处已 **Lean** 化：C.4 的因式分解（`Theorem12.lean`）、C.3 的二次式与其非恒零（`QuadraticMu2.lean`）、C.2/C.3 的扰动引理（`Perturbation.lean`）。
- **验证**（[VERIFICATION_STATUS](../../../../proof/rho1_layer/VERIFICATION_STATUS.md)）：
  - 抽象模型：C.1 200/200、C.2 199/199、C.3 295/295、C.4 42/42 ✓；
  - **真实实例**：C.1 200/200、C.2 17/17、C.3 43/43 ✓；
  - **端到端**（判据 ⟹ 构造出真正的 $\mathcal V$，并用堆叠判据验 $(5a)\wedge(5b)$）：
    **C.3（$\mu=2$）12/12，且每条实例都逐项检查 10 个条件** ✓ ——
    $\dim\mathcal U=3$、$W_0\subseteq\mathcal U$、$w\ne0$、$(N)$、$\mu\ge1$、
    **$\operatorname{row}(L_0)\subseteq\mathcal V$**、$\dim\mathcal V=4$、类型 $(3,1)$、$(5a)$、$(5b)$
    （[verify_end2end_fixed.py](../../../../proof/rho1_layer/verify_end2end_fixed.py) ✓）。
    **C.1、C.2 的端到端未做** ✗。

> **更正说明（2026-10-29）**：此前记录的端到端数字（$\mu=1$ 12/12、$\mu=2$ 60/60、$\mu=3$ 12/12）
> **验证不完整** ✗ —— 它们没有检查 $\operatorname{row}(L_0)\subseteq\mathcal V$，而用任意截面构造的
> $\mathcal V$ 一般**不含** $L_0$ ✗（把它并入后 $\dim\mathcal V$ 从 4 变 5、类型从 $(3,1)$ 变 $(3,2)$ ✗）。
> 取截面时令 $s(u_0):=\ell_0$ 即修复 ✓；用修法重跑得 **12/12 且 10 条全 PASS** ✓，全部落在 $\mu=2$ ✓。
> 旧的三个数字**作废** ✗。

> **边界**：以上都是**格子级**（给定 $(\mathcal U,\mathcal H)$）✓。**层级别**（$\exists(\mathcal U,\mathcal H)$）**没有** iff 判据 ✗ ——
> 曾写过的定理 8、13 因"$T$ 随格子变"而被撤回 ✗（见 RESTRICTED_COMPLETION_MODEL §21）；
> "条件不变子空间对交封闭 / 有最小元"也已被专家反例推翻 ✗（同文件 §30）。

## 附录 E：$\delta$ 三分与阶差（原 B.30 / B.34 / B.35 / B.36，经验/精确验证）

**B.36（控制变量实验：同一 $A$、同一 $L_0$、只变 $C$ 的支撑 ⟹ 阶差只由 $\rho$ 决定；谱延迟为零）** 取
$n=6$、$p=2$、$A=\operatorname{diag}(1,\dots,6)$（谱互异）、$L_0$ 固定；$C$ 的两行分别支撑在互不相交的两组坐标上，
故可观测指标为两段长度 $(\mu_1,\mu_2)$、$\Delta_k=\#\{i:\mu_i\ge k+1\}$、$r_k=\sum_i\min(k+1,\mu_i)$：

| $C$ | 支撑 | $\Delta$ 剖面 | $q_0$ | $r_1$ | $\rho$ | $q_{\rm geom}$ | $q_{\rm spec}$ | $q_{\min}$ |
|---|---|---|---|---|---|---|---|---|
| $C_{33}$ | $(3,3)$ | $(2,2)$ | 2 | 4 | 2 | 3 | 3 | **3** |
| $C_{42}$ | $(4,2)$ | $(2,1,1)$ | 2 | 4 | 2 | 3 | 3 | **3** |
| $C_{24}$ | $(2,4)$ | $(2,1,1)$ | 2 | 4 | 2 | 3 | 3 | **3** |
| $C_{51}$ | $(5,1)$ | $(1,1,1,1)$ | 3 | 3 | **1** | **$\infty$**（无中间层）| $\infty$ | **4 $=n-p$** |

*定义*：$q_{\rm geom}$、$q_{\rm spec}$ **只统计次终端**（$q+p<n$）的中间层候选，$\rho=1$ 时中间层为空故为 $\infty$；$q_{\min}$ 含终阶，故 $\rho=1$ 时为 $n-p$（专家 §2 指出的口径问题，已改）。
*三条结论*：
1. 在 $n,p,r,\rho$ **固定**、$A$ 与 $L_0$ **固定**、只有剖面不同（$(2,2)$ vs $(2,1,1)$）时，$q_{\min}$ **相同**（都为 3）
   ⟹ **该族里阶差只由 $\rho$ 决定**，与剖面的后段无关（支持"$\rho$-only"猜想而**不支持**剖面依赖版）；
2. $\rho=1$ 的 $C_{51}$ 给出 $q_{\min}=4=n-p$ ⟹ **B.32 的终端唯一性在该族里被独立确认** ✓；
3. 四例都有 $q_{\rm geom}=q_{\rm spec}$ ⟹ **谱延迟为零**：几何允许的候选没有被谱条件再筛掉，
   故按专家 §3.4 的分解 $q_{\min}-q_0=(q_{\rm geom}-q_0)+(q_{\rm spec}-q_{\rm geom})$ 的第二项在此族中为 0。
*等级*：**[精确验证]**（`tools/verification/controlled_profile.py`；单族四例，非定理）。

**B.35（两阶段流程：几何筛选对 B.31 是**可靠**的；以及 $\Delta$ 剖面与阶差）** 记
$$r_k=\operatorname{rank}[C;CA;\dots;CA^k],\qquad \Delta_k:=r_k-r_{k-1}\ (k\ge1),\qquad \Delta_1=\rho .$$

1. **两阶段流程的可靠性**（专家 §5.3/§5.4 的建议，已实现）：先用 B.31 的几何条件 $1\le\delta<\rho$（或终阶偏 $q+p\ge n$）
   筛掉候选，再跑谱检验。在 599 个实例、3400 个可容许候选上：
   * 筛后谱检验量 $=1905$，即原来的 **56.0%**（省 44%）；
   * **筛掉的候选里没有一个可行**（$0$ 个反例）⟹ B.31 的筛选**不会丢掉可行解** ✓；
   * 可行计数筛前筛后一致（$1905=1905$）✓。
2. **$\Delta$ 剖面与阶差**（专家 §8.2 方向的初步数据，$\rho=2$）：
   * 剖面 $(2,2)$（$n=6$，即 $r=(2,4,6)$）：766 个实例，阶差**恒为 1**；
   * 剖面 $(2,2,1)$（$n=7$，$r=(2,4,6,7)$）：733 个实例，阶差 $\in\{1,2\}$，平均 **1.50**。
   ⟹ 同一 $\rho$ 下，后续秩增长分布不同，阶差分布也不同（与专家 §8.2 的猜测一致），但 $n$ 也同时变化，需进一步控制变量。
*等级*：1 **[精确验证]**（可跑的筛选器，0 反例）；2 **[精确验证]**（初步数据，非定理）。
*注（bug 记录）*：初版剖面脚本把 $r_k$ 算成 $\operatorname{rank}[C;CA^k]$（漏了中间的 $CA^j$），得到"$\Delta_k=0$ 却有可观测性"的
矛盾结果；改为逐次堆叠后正确。

**B.34（最窄中间层 $r_1=p+2$：$\delta=1$ 层全可行、阶差 $\le2$；**[精确验证]**）** 设 $\rho=r_1-p=2$（即 $r_1=p+2$）。
此时中间层只有一个值 $\delta=1$（由 $0\le\delta\le\rho$），约化铅笔尺寸由 B.33 给出为 $(p+q)\times(q-1)$。在 $n=6,7$ 的
745 个实例上（$p\in\{2,3\}$、$r\in\{1,2\}$、$(C,A)$ 与 $(L_0,A)$ 均可观测）：

| 量 | 结果 |
|---|---|
| $\delta=2=\rho$ 层（等号）| **0 可行 / 742**（与 B.22 一致 ✓）|
| $\delta=1$ 层（唯一中间层）| **745 可行 / 745** |
| $\delta=0$ 层（终阶）| 745 可行 / 745 |
| $q_{\min}-q_0$ | $0$：3 例，$1$：543 例，$2$：**199 例** |
| $q_{\min}<n-p$ | **745/745** |

*解读*：
1. $\rho=2$ 时**次终端总是可行**（$q_{\min}<n-p$ 全成立），与 B.32 的 $\rho\le1$ 情形形成对照；
2. 中间层（$\delta=1$）在本次样本里**全部可行**——但 B.30 的薄集现象说明这只是"几乎总可行"，不是定理；
3. 阶差**不超过 2**（$0/1/2$），比 Class I 的 $n-1-q_0$ 小得多。
*猜想（待证）*：$\rho=2$ 时 $q_{\min}-q_0\le2$；一般 $\rho$ 时阶差有界（$\le$ 某个只依赖 $\rho$ 的函数）。
*等级*：**[精确验证 745/745]**（`tools/verification/narrow_intermediate.py`）。

**B.30（$\delta$ 三分；2026-11-05 用**修正后的 $\delta$ 公式**重扫）** 在 B.28b 的记号下，
$$\delta(\mathcal V)=h-\dim\mathcal V=h-(q+p)\qquad(\text{维数恒等式}),\qquad 0\le\delta\le\rho:=r_1-p .$$

| 层 | 结论 | 依据 |
|---|---|---|
| $\delta=\rho$ | **绝不可行**（等号 $h=q+r_1$）| **B.22**（已证）|
| $\delta=0$ 且 $q+p<n$ | **绝不可行**（$\operatorname{row}(CA)\subseteq\mathcal V$ ⟹ $\mathcal VA\subseteq\mathcal V$ ⟹ 可观测性 ⟹ $n\le q+p$）| **B.28(3)**（已证）|
| $\delta=0$ 且 $q+p=n$ | 可行（**终阶**，$\mathcal V=\mathbb C^{1\times n}$）| B.32 的终阶构造 |
| $1\le\delta<\rho$ | **可行**（本次扫描 **1107/1107** 全可行）| **[精确验证]**（非定理）|

*修正记录（2026-11-05）*：先前脚本把 $\delta$ 算成了 $\dim(\operatorname{row}(CA)\cap\mathcal V)$（**交维数**），与 $\delta$ 相差
$\dim\operatorname{row}(CA)$；用正确公式 $\delta=h-(q+p)$ 重扫后上表才正确（此前"$\delta=0$ 层 0 可行"的样本其实是 $\delta=\rho$ 的等号层 ✓，
结论方向未受影响）。
*精确数据*（$n=6,7$；记 $\rho=r_1-p$）：$(p,r,r_1)=(2,1,4)$：$\delta=0$ 216 全可行（**均终阶**）、$\delta=\rho$ 216 全不可行、中间层 216 全可行；
$(2,2,4)$：192 / 192（不可行）/ 192；$(3,1,6)$：208 / 107（不可行）/ 416；$(3,2,6)$：196 / — / 283。