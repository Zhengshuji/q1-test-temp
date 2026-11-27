# A3_basefamily/ —— $\exists S$（基族选择）任务

> **主线的哪一半**：A3。$q1$ 现在**唯一**的实质空白。
> 目标：判定是否存在可容许 $S$ 使固定-$S$ 问题可行；若可行，$S$ 怎么找。

## 1. 为什么这是关键

$$q1\ =\ \mathbf{A2}\ +\ \mathbf{A3}$$

而 A2（固定 $S$）在 $r=2$ 上已坍缩为线性代数（见 [A2_fixedS/](../notes/A2_fixedS_README.md)）。所以：

> **2026-11-01 更正**：这里的"线性代数"只指 **C2 线性松弛**（$a_0|_K\ne0$），它**只必要**；
> 精确判据还要求 $p_U$ **可分解**、$U$ **可容许**。$q=t,r=2$ 上 $\dim K\ne0$ 而 $\dim D_{\rm adm}=0$
> 的实例已由 [c301](scripts/c301_g3_square.py) 给出 ⟹ "坍缩为线性"这句话只能对**判据的松弛**成立。

$$\boxed{\ q1\ \text{的复杂度}\ =\ \exists S\ \text{的复杂度}\ }$$

**如果 $\exists S$ 是多项式 ⟹ $q1$ 是多项式；如果它是 $\exists\mathbb R$-hard ⟹ $q1$ 是 hard。**
两条路的胜负**全在这里**。

## 2. 问题的精确形状

- 基空间：$D=G\cap A^{-1}(H)\subseteq\mathcal V$，$S\in\operatorname{Gr}(s,D)$；
- 派生量：$T_S=(A(S)+S)/S$、$B_S=G/S$、$I_\lambda=\operatorname{im}P(\lambda)\cap(H/S)$；
- 判据：**C1（精确）** $=\exists$ 可容许 $U$、$p_U$ 可分解、$p_U\in K$、$a_0(p_U)\ne0$；
  **C2（松弛，只必要）** $=a_0|_K\ne0$。$r=2$ 时 C1 的"可分解"是**斜对称矩阵秩 $\le2$**（$m=3$ 时自动成立、$m\ge4$ 起是真约束）。
  **切勿**把 C2 当 C1 用（2026-11-01 撤回；见 [支1](../../workspace/notes/支1.md) §2 与 [c301](scripts/c301_g3_square.py)）。

所以 $\exists S$ 是：**是否存在 $S$ 使一组（由 $S$ 决定的）齐次线性条件成立**。
这是一个 $\exists$ + 代数条件的混合问题 ⟹ 形式上在 $\exists\mathbb R$ 里；**难度未知**。

## 3. 工作分解

| 编号 | 任务 | 具体产出 | 状态 |
|---|---|---|---|
| **A3-1** | 写出 $a_j(S)$ 对 $S$ 的显式依赖 | 给定 $S$ 的基，用 $A,C,L_0$ 表达 $T_S,B_S,P(\lambda)$，再算系数向量 | 空白 |
| **A3-2** | $\pi_S:\mathcal X_{s,k,\ell}\to\mathcal B_{s,k,\ell}$ 的支配性 | 显式有理截面（首选）或 Jacobian 判据 | 空白 |
| **A3-3** | $\exists S$ 的判定复杂度 | 小情形（$s=1$、$d$ 小）先看是否线性 | 空白 |
| **A3-4** | 把 $q1$ 重述为"$\exists S$ + 线性条件" | 与 [PCC](../../../trash/README.md) 的 Q-A 对齐 | 空白 |

## 4. 已知的相关结果

| 结果 | 出处 |
|---|---|
| 联合入射空间 $\mathcal X_{s,k,\ell}$ 的定义、纤维维数 $(r-k)(m-r)$、非空条件 $r\le h-b$（$\ell=k$）| [proof/global_incidence/](../../../trash/README.md) |
| $(k,\ell)$ 分层与剪枝 $k\le r$、$\ell=k$ | [proof/base_family/](../../../trash/README.md) |
| 三个维数 $d_{\mathrm{alg}}$、$d_{\mathrm{spec}}$、$d_{\mathrm{image}}$ 必须分开 | [A2 §25.1](../../../trash/README.md) |
| $\pi_S$ 的**支配性**从未被研究 | —— |

## 5. 起点建议

1. 先取**最小情形**：$n$ 小、$p=1$、$r=1$，把 $a_j(S)$ 手算出来；
2. 看 $\{a_0,a_1,a_2\}$ 作为 $S$ 的函数是什么（$S$ 在 Grassmannian 上变 ⟹ 系数有理函数）；
3. 问：$a_0(S)\notin\operatorname{span}\{a_1(S),a_2(S)\}$ 是否等价于某个**线性**条件？
   若是 ⟹ $\exists S$ 是线性规划/线性代数 ⟹ $q1$ 多项式（重大突破）；
   若否 ⟹ 得到 $\exists\mathbb R$ 形状的问题，接 A3-3。

## 6. 陷阱（来自项目历史）

- "开集非空" ≠ "处处成立"（CLAUDE §7.4）；
- 薄集不许采样（§7.12）——$\exists S$ 的可行集很可能余维 $\ge1$；
- 秩判据写清"行堆叠"还是"列拼接"（§7.2）；
- 每个结论必须能点到文件（§7.9）。

---

## 7. 进展记录

### 2026-10-31：第一次 $S$-扫描（A3-2 的第一个数据点）

**做了什么**：
- 新模块 [tools/verification/base_sweep.py](../../tools/verification/base_sweep.py)：给定 $(A,C,L_0,d,S)$，
  算 $(r,m,t,k,\ell,\dim B_S)$，枚举可容许的 $U$（$S\subseteq U\subseteq H$、$A(S)\subseteq U$、$U\cap G=S$），
  逐个判 $(A)$（$\operatorname{rank}[Z,AZR]=d$）与 $(S)$（极大子式 gcd，`spectral_gcd_Z`）；带断言。
- 新脚本 [c293](../../proof/layer_program/c293_base_sweep.py)：扫第二实例的 $S$。

**结果**：
| 实例 | 结论 |
|---|---|
| R17（回归）| $q=3$：48 个候选 $U$ 中 **34 个可行**（71%）✓ 与文档的 75% 一致 ⟹ 模块正确 |
| 第二实例 | $q=1..4$ 的已覆盖范围内 **无可行 $S$**；$q=4$ 覆盖完整 ⟹ $q_{\min}=5$（$d=0$ 平凡）——**2026-11-01 撤回：$q=5$ 在 $\lambda=1$ 失败，实例无解（$q_{\min}=\infty$），见 [v2 §4](../../archive/expert_correspondence/REPORT_FOR_EXPERT_2026-11-01_v2_EN.md)** |

**意义**：这是项目**第一次算出具体实例的 $q_{\min}$**——**该结论已撤回**（见上）；$q\le4$ 的已测范围仍为空，但实例整体无解。

**踩的坑**：可容许 $U$ 的约束写成 $U\subseteq V$（应为 $U\subseteq H$），把 R17 的可行解全排除了——
R17 回归才暴露。已修正。

**下一步**：$r\ge2$ 的 $U$ 枚举（$\operatorname{Gr}(r,H/S)$ 的格点太贵）需要构造性方法，而不是枚举。

### 2026-10-31（第二轮）：A3-1 的尝试与卡点

**做了什么**：写 [tools/verification/coeff_of_S.py](../../tools/verification/coeff_of_S.py)——用
$\mathbb C(\lambda)$ 上的有理函数消元算 $I_\lambda$，清分母得 $B(\lambda)$，再用 `coeff_forms` 得 $a_j$。

**结果：失败（已记录卡点）**。
- 有理函数消元本身正确（$I_\lambda$ 的 $\mathbb C(\lambda)$-基算对了，验算过 $Pa=Hb$）；
- 但清分母得到的 $B(\lambda)$ **不是多项式基**：c282 实例上它在 $\lambda=0$ 处秩从 3 掉到 1；
- 判据"$\det[U|B(\lambda)]$ 非零常数"只在**多项式基 + unimodular 框架**下成立（A2 §29.3），
  用这个基会给出**错误**判据（实测：$a_0=0$、$a_3..a_6$ 出现错位系数）。

**正确的下一步**：对 pencil 做**幺模列消元**（多项式带余 + gcd），化成 $[H\mid0]$，取后几列作多项式核基。
这是标准但更重的算法。

**顺带修的 bug**：`lcm` 计算把 $\gcd(\mathrm{lcm}\cdot d, d)$ 当成 $\gcd(\mathrm{lcm}, d)$，导致 lcm 恒为 1（已修）。

**没受影响**：A3-2 的扫描（`c293`）用的是 `spectral_gcd` 直接判据，**不依赖** $a_j$，结论仍有效。

### 2026-10-31（第三轮）：瓶颈已写成给专家的报告

**卡点文档**：[QA24_BOTTLENECK_2026-10-31_EN.md](../../archive/expert_correspondence/QA24_BOTTLENECK_2026-10-31_EN.md)

**要点**：
- 有理函数消元算对了 $I_\lambda$ 的 $\mathbb C(\lambda)$-基，但清分母**不是多项式基**（c282 上 $\lambda=0$ 处秩 3→1）；
- 判据需要**幺模**框架（A2 §29.3），否则行列式带进伪因子；
- **无基判据已可用**：$U\cap I_\lambda=U\cap\\operatorname{im}P$（$U\subseteq H/S$），只要 gcd of minors；
- 给专家的 5 个问题：标准算法、单行情形、判据的框架条件、线性形式是否必要、跳变点处理。

### 2026-10-31（第四轮）：更正判据 + 新卡点

**更正**（A2 §37）：系数判据 `a_0 ∉ span{a_j}` **不充分**，必须加 $K
ot\subseteq G/S$（即 $U\cap G=S$）。
端到端检验（`c298`）发现：假阳性 3/4。正确判据：
$$	ext{可行}\iff K
ot\subseteq G/S\ \wedge\ a_0
otin\operatorname{span}\{a_j\}.$$

**新卡点**（`c299`）：随机实例上 `coeff_of_S.setup` 的内部断言
`H/S 维数 X != Y` 对**几乎全部** $S$ 失败（23249 次跳过）⟹ 修正后的判据**还没有机器验证**。

**可能原因**：`setup` 里 $H/S$ 的基构造（`_solve_in_basis(WB, h)[s:]` + `prune`）在一般实例上不自洽
（c282 这类"好"实例上通过，随机实例上大量失败）。**下一步**：改用更稳健的商空间基构造
（对 `[S | H]` 做行阶梯，取非主元列），并加"每个基向量确实在 $H$ 里"的逐条断言。

**教训**：`c296`/`c297` 里那些"通过"的随机实例，也可能受同一个 bug 影响——它们的结论**应视为不可靠**，
需要用稳健实现重跑。

### 2026-10-31（第五轮）：修了两个根因 bug，但端到端**仍未通过**

**修复**：`coeff_of_S.setup` 与 `c297.geometry` 把子空间的**基**当成了**零化子**（两处：$G$ 与 $D$）。
正确写法：$G=(V^\perp+H^\perp)^\perp$、$D=\{x:G^\perp x=0,\ H^\perp Ax=0\}$。
**所有随机实例的旧结论作废**（$S$ 取自错误的 $D$）。

**c282 回归**：修复后仍通过 ✓（80 个 $U$、0 不一致）。

**c299（修正判据 + 端到端）**：

| 指标 | 结果 |
|---|---|
| 有效 sweep | 51 |
| 混合实例 | 2 |
| 端到端检验 | 4 次，**失败 3 次** |

⟹ 判据 $K\not\subseteq G/S\ \wedge\ a_0\notin\operatorname{span}\{a_j\}$ **仍然充分性不足**（假阳性 3/4）。
补上 $T_S\subseteq U$（$k=1$ 时强制）后**没有改变**结果（那些 $S$ 上 $k=0$，约束是空的）。

**可能的剩余缺口**（下一轮逐一排除）：
1. $U\cap G=S$ 的坐标表达是否与 `check_Z` 的 $Z$ 构造一致；
2. `to_U` 的还原是否真的落在 $H$ 里（应在 `setup` 里断言）；
3. 端到端 harness 本身（`check_Z` 对 $Z=S\oplus U$ 的用法）是否有错——
   用 `feasible_by_minors` 对同一个 $U$ 交叉验证即可分辨。

**当前状态：A3 的系数判据未通过端到端验证，不能作为结论使用。**

### 2026-10-31（第六轮）：问题定位 + 给专家的 QA25

**根因（三处，已修两处半）**：
1. 判据缺 $U\cap G=S$（已加 $K\not\subseteq G/S$）；
2. $G$、$D$ 用"基"代替"零化子"（已修）；
3. **用"删行"代替"换基"**：要只取 $P$ 的 $H/S$ 行，必须先换基使 $H/S$ 成坐标子空间；
   删行会改行列式。c282 恰好 $H/S$ 是坐标子空间 ⟹ 它通过；随机实例不是 ⟹ 假阳性。

**现状**：修 3 之后**仍有假阳性**，但测试脚本的 $U$ 还原没跟着改基 ⟹ 分不清是判据错还是 harness 错。

**文档**：[QA25_COEFFICIENT_CRITERION_2026-10-31_EN.md](../../archive/expert_correspondence/QA25_COEFFICIENT_CRITERION_2026-10-31_EN.md)

**给专家的四个问题**：判据陈述是否正确、有无**无坐标**写法、非平衡情形的正确陈述、工程优先级。

---

## 8. 脚本位置（2026-11-01 整理）

本任务**活跃脚本**在 [`scripts/`](scripts/)：

| 脚本 | 用途 | 状态 |
|---|---|---|
| `c295_bezout.py` | Bézout 证书（QA24 阶段 2）| ✓ 通过（c282）|
| `c296_coeff_sweep.py` | 系数判据扫 $S$ | ⚠️ 结论作废（$D$ 曾算错）|
| `c297_mixed_instances.py` | 随机找混合实例 | ⚠️ 同上 |
| `c298_end_to_end.py` | 端到端验证 | ⚠️ 发现判据不足 |
| `c299_corrected_criterion.py` | 修正判据 + 端到端 | ⚠️ 仍 3/4 假阳性 |

**归档的**（在 `proof/layer_program/`，被 A2 文档引用）：`c290`（坍缩）、`c291`/`c292`（pencil-span）、`c293`（S-扫描，可信）。

## 9. 现在该做什么（QA25 回复的路线 A）

**中心问题**：在 $\mathrm{DEC}(q)$ 的 $K_S$ 上是否总有 $D(K_S)=K_S$（即 G3 是否自动成立）。

**第一步**（便宜、可判定）：在 $r=2$ 的小实例上直接算
$$\dim\operatorname{span}\{p_U:\ U\ \text{可容许},\ p_U\in K_S\}\ \overset{?}{=}\ \dim K_S .$$
不比较布尔值，直接比维数——这才能暴露 G3 障碍。

### 2026-11-01（分支 1，A-1）：判据链的第一张对照表

脚本：[scripts/a1_determinant_identity.py](scripts/a1_determinant_identity.py)（三个判据**全部精确**，不抽样）

| $U$（c282）| det 判据（$q_U$ 常数）| $U\cap\operatorname{im}P=0$（gcd of minors）| `check_Z`（$Z=S\oplus U$ 的 $(A)(S)$）|
|---|---|---|---|
| $(-1,-1,-1,-1)$ | False | False | False |
| $(0,0,0,-1)$（即 $e_8$ 方向）| **True** | **True** | **False** ✗ |

**读法**：
1. det 判据 $\iff$ "$U\cap\operatorname{im}P=0$" ✓（两者一致，说明 adapted-basis + 行列式这一步**实现对了**）；
2. 但两者与 `check_Z` **不一致**：$e_8$ 方向被判可行，而 $Z=S\oplus U$ 的 $(A)(S)$ 失败 ✗。

**这意味着**：要么 `check_Z` 对 $Z=S\oplus U$ 的用法有误，要么 "以 $U$ 为补的 $Z$" 与"满足 $(5b)$ 的 $Z$" 不是同一个东西。
文档记载 c282 有 4 条可行直线（含 $e_8$ 的倍数），所以更可能是**我这里对 `check_Z` 的调用方式**有问题。

**下一步（分支 1 的 A-2）**：先复核 `check_Z` 的语义（它要求 $Z$ 是 $n\times d$ 且 $CZ=0$ 吗？$R$ 是 $\ker(CAZ)$ 吗？），
再用 c282 的**已知可行** $Z$ 做地基检查（必须出现 True）。

### 2026-11-01（分支 1，A-2）：**A2 判据 ≠ DEC(q) 可行**——$(A)$ 是独立约束

**具体反例（c282，$n=8,p=2,q=4$）**：$S=\operatorname{span}(e_5)$，A2 判据选出的可行直线 $U=\operatorname{span}(e_8)$，
于是 $Z=S\oplus U=\operatorname{span}(e_5,e_8)$。逐条核对：

| 条件 | 计算 | 结果 |
|---|---|---|
| $CAZ=0$ | $CA=[e_3;e_4]$，$Z$ 的列 $e_5,e_8$ 在 $e_3,e_4$ 上无分量 | ✓ |
| 于是 $R=\ker(CAZ)=I$ | $(A)$ 退化为 $AZ\subseteq Z$ | — |
| $AZ$ | $Ae_5=e_5$ ✓，$Ae_8=e_7\notin Z$ | **✗** |
| $\operatorname{rank}[Z\mid AZ]$ | $=3$，要求 $=d=2$ | **$(A)$ 失败** |
| $(S)$（极大子式 gcd）| 次数 $=0$ | ✓ |

$$\boxed{\ \text{A2 的"$U$ 避开所有 $I_\lambda$"}\ \ne\ \text{DEC}(q)\text{ 可行——}(A)\text{ 是独立约束}\ }$$

**推论**：
1. A2 文档里"admissibility $\Rightarrow$ $(A)$ 且 $(S)$"这一步**不成立**（至少对 c282 的 $U=e_8$）；
2. 我在 A3 里反复追的"系数判据"只对应 $(S)$ 侧，**永远不会与 `check_Z`（$(A)+(S)$）一致** ✗；
3. `check_Z` 的正确性因此得到确认（它抓到了 A2 判据的漏洞）✓。

**下一步（A-2 的收尾）**：
- 在 A2 里加一条"$(A)$ 条件"的显式判据（$AZ\subseteq Z+\ker(CAZ)$），并检查它能否化成对 $U$ 的线性条件；
- 若不能，则 A2 的"固定 $S$"问题必须重新表述为一个**同时含 $(A)$ 与 $(S)$** 的问题。

### 2026-11-01（分支 1，A-2 续）：$(A)$ 像是**线性**条件，且它杀掉了所有 $(S)$-可行解

脚本：[scripts/a2_condition_A.py](scripts/a2_condition_A.py)（c282：$m=4,r=1,s=1,d=2$，$H/S$ 的 80 个格点）

| 统计 | 数 |
|---|---|
| 扫过的 $u$ | 80 |
| $(A)$ 成立 | **54** |
| $(A)\wedge(S)$ 成立 | **0** |

**两条发现**：

1. **$(A)$ 看起来是线性的**：抽检 $u_1+u_2$ 与 $2u_1$ 都仍满足 $(A)$ ✓（需更多点确认，但方向明确）；
2. **在 c282、$q=4$ 上，$(A)$ 与 $(S)$ 没有交集** ⟹ 该实例 $(S)$-可行但 **DEC(q) 不可行** ✓
   —— 这与 `check_Z` 的判定一致，也与 §A-2 的反例自洽。

**含义**：固定-$S$ 问题的正确判据是
$$\text{可行}\iff\exists U:\ \underbrace{(A)(U)}_{\text{疑为线性}}\ \wedge\ \underbrace{(S)(U)}_{\text{系数判据}}.$$
A2 此前只做了 $(S)$，所以"c282 在 $q=4$ 可行"这个说法**不成立**（它只是 $(S)$-可行）。

**下一步**：
- 用更大的格点确认 $(A)$ 的线性性（若是，则整个固定-$S$ 判据 = 两组线性条件的交 ⟹ 可判定）；
- 把 $(A)$ 写成对 $U$ 的显式线性条件（$AZ\subseteq Z+\ker(CAZ)$ 的坐标形式）。

### 2026-11-01（分支 4 / E-1）：adapted basis 的验证 + 一个新发现的适用条件

**做了**：`scripts/verify_adapted_basis.py`——验证
1. $T$ 可逆、$T^{-1}(H/S)=\operatorname{span}(e_1..e_m)$（c282：**通过** ✓）；
2. 行列式在换基下的缩放 $\det[U_{\rm new}|P_{\rm new}]=\det(T^{-1})\det[U_{\rm old}|P_{\rm old}]$。

**新发现（重要）**：单行列式判据要求 **[U|P] 是方阵**，即
$$r+t=\dim(W/S)=w-s,$$
**不是** $r+t=\dim(H/S)=m$。c282 的 $r+t=4$ 而 $w-s=5$ ⟹ 矩阵是 $5\times4$，
**有 5 个极大子式**，单行列式只是其中一个。

$$\boxed{\ \text{正确判据}=\gcd\text{ of all }(r+t)\text{-minors（}\S27\text{ 的 `feasible_by_minors`），单行列式只在 }r+t=w-s\text{ 时够}\ }$$

这解释了为什么 $a_j$ 判据在 c282 上"碰巧"对（80 点上 0 不一致）——那里的其余子式在这些点上冗余，
但**一般情形不是**。这是 §33–§38 那串错误的**又一个来源**。

### 2026-11-01（分支 1，A-2 结论）：$(A)$ **不是线性的**——更正上一条

用更大的格点做闭包检验（c282，$H/S$ 的格点）：

| 格点 | 点数 | $(A)$ 成立 | 两个 $(A)$ 点之和仍 $(A)$ |
|---|---|---|---|
| bound=1 | 80 | 54 | **4/11** |
| bound=2 | 624 | 500 | **10/16** |

$$\boxed{\ (A)\ \text{对加法\textbf{不封闭}\ }\Longrightarrow\ (A)\ \text{不是线性条件}\ }$$

**更正**：上一节（2026-11-01 A-2 续）说"$(A)$ 看起来是线性的"是**基于 3 个抽检点的错误印象**，
已用 27 次随机配对推翻。

**正确的解释**（纸面）：c282 上 $CAZ=0$，故 $(A)\iff AZ\subseteq Z$，即
$$A(S)\subseteq Z\ \wedge\ A(U)\subseteq Z .$$
$A(S)\subseteq Z$ 恒成立（$Ae_5=e_5$）；而 $A(U)\subseteq S\oplus U$ 意味着 **$A(u)$ 的类与 $u$ 的类共线**
——这是 $u$ 的**二次**条件（$2\times2$ 子式为零）✓ 与"不封闭"一致。

**结论**：固定-$S$ 的判据是
$$\exists u:\ \underbrace{(A)(u)}_{\text{二次}}\ \wedge\ \underbrace{(S)(u)}_{\text{系数判据}}.$$
比"两组线性条件"复杂，但仍是**低次代数条件**，可判定。

**下一步**：把 $(A)$ 的二次形式显式写出（$A(u)$ 与 $u$ 共线 ⟹ Plücker 型二次方程），
再检验它与 $(S)$ 的联合可行集在 c282 上为空（已观察到 0/80，扩到 624 点复核）。

### 2026-11-01（分支 5 / A-5）：$D_{\mathrm{adm}}(K_S)\ne K_S$ —— G3 障碍**真实存在**

**脚本**：[`scripts/c300_g3_check.py`](scripts/c300_g3_check.py)（选 $h-v\ge2$、$r=2$ 的随机实例，
枚举可容许 $U\in\operatorname{Gr}(2,E)$、过滤 $p_U\in K_S$、算 $\dim D_{\mathrm{adm}}$ 与 $\dim K_S$）。

**结果**（共 58 个 (实例,$S$)；只列代表性几例）：

| 现象 | 例 |
|---|---|
| $\dim D_{\mathrm{adm}}=0$ 而 $\dim K_S=2\ldots5$ | trial46/123/144/192/223 |
| $\dim D_{\mathrm{adm}}=\dim K_S$ | trial77（6=6）、trial212（3=3）|

$$\boxed{\ \text{否：}D_{\mathrm{adm}}(K_S)\subsetneq K_S\ \text{确实会发生}\ }$$

⟹ **线性判据（$a_0\notin\operatorname{span}\{a_j\}$）在 $\mathrm{DEC}(q)$ 的结构下没有一般依据**，
与 QA25 的判断一致。

**但**：在 58 个样本里**没有出现假阳性**——每逢 $D_{\mathrm{adm}}<K_S$，都有 $a_0\in\operatorname{span}\{a_j\}$，
两种判据给出相同结论。真正的假阳性需要 $D_{\mathrm{adm}}<K_S$ **且** $a_0\notin\operatorname{span}\{a_j\}$；
随机搜索 58 例未找到（**下一步：定向构造**——例如从 $a_0$ 与 $\{a_j\}$ 的线性关系入手反推实例）。

**结论的等级**：`[精确验证 58/58]`——**不是证明**；但它足以否证"$D(K_S)=K_S$ 恒成立"这一猜想
（一个反例即可，而这里有多个）。

### 2026-11-01（分支 1，A-2 收尾）：$(A)$ 的**实例级刻画**与一个结构事实

**结构事实（精确）**：c282 的 $H/S$ 格点上，$A(u)\in W$ 只有 **26/80** 个；其余 54 个 $A(u)\notin W$
⟹ 我此前的"$CAZ=0$ 总成立"假设**错误**，$R=\ker(CAZ)$ 在多数点上是非平凡的。

**实例级刻画（精确，仅 c282，80 点）**：

| $A(u)\in W$ | $(A)$ | 计数 |
|---|---|---|
| 否 | **成立** | 54 |
| 是 | **不成立** | 26 |

$$\boxed{\ \text{c282 上：}(A)(u)\iff A(u)\notin W\ }$$

**这不是定理**，只是该实例 80 个格点上的**完全相关**；机制是：
$A(u)\in W\Rightarrow CAZ=0\Rightarrow R=I\Rightarrow (A)\iff AZ\subseteq Z$（而 $A(u)\notin Z$ 时失败）；
$A(u)\notin W\Rightarrow R\ne I$，$(A)$ 可由 $R$ 方向满足。

**仍待确认**：
1. 该刻画在 $r\ge2$ 或其它实例上是否还成立（大概率不成立）；
2. $(S)\wedge(A)$ 在 624 点上的联合可行集（此前 80 点上是空）。

### 2026-11-01（分支 1，A-2→A-3）：实例刻画的**反例**与联合可行集

脚本：[scripts/a3_joint_feasible.py](scripts/a3_joint_feasible.py)

| 实例 | 点 | $(A)$ 成立 | $(A(u)\in W,(A))$ 分布 | $(A)\wedge(S)$ |
|---|---|---|---|---|
| c282（$q=4,m=4$）| 80 | 54 | $(F,T)$ 54；$(T,F)$ 26 | 抽检 40 个 $
Rightarrow$ **0** |
| 第二实例（$q=3,m=2$）| 8 | 8 | $(F,T)$ 6；**$(T,T)$ 2** | 抽检 8 个 $
Rightarrow$ **0** |

**两条结论**：

1. **"$(A)(u)\iff A(u)\notin W$" 不成立**（第二实例给出 2 个反例：$A(u)\in W$ 但 $(A)$ 成立）
   ⟹ 它只是 c282 的**实例现象**，不是结构定理 ✓（上一节已标"不是定理"，现在有了反例）；
2. **$(A)\wedge(S)$ 在两个实例的已测格点上都是空集** ⟹ 这两个实例在相应 $q$ 上**都不可行**。
   这与 A3-2 的 $q_{\min}=5$（第二实例；**2026-11-01 撤回：实例无解**，见 [v2 §4](../../archive/expert_correspondence/REPORT_FOR_EXPERT_2026-11-01_v2_EN.md)）不矛盾；也说明 c282 的"4 条 $(S)$-可行直线"确实**不是** DEC(q) 可行。

### 2026-11-01（分支 1，A-3）：三个实例的 $(A)$/$(S)$ 完整对照 + 地基检查

脚本：[scripts/a3_groundcheck_r17.py](scripts/a3_groundcheck_r17.py)（R17）与 [scripts/a3_joint_feasible.py](scripts/a3_joint_feasible.py)

| 实例 | $q$ | 点数 | $(A)$ | $(S)$ | $(A)\wedge(S)$ | 独立性期望 |
|---|---|---|---|---|---|---|
| **R17**（已知可行）| 3 | 26 | 24 | 14 | **12** ✓ | $24\cdot14/26\approx12.9$ ✓ |
| c282 | 4 | 80 | 54 | 26 | **0** ✗ | $54\cdot26/80\approx17.5$ ✗ |
| 第二实例 | 3 | 8 | 8 | 0 | 0 | 0 ✓ |
| 第二实例 | 2 | 8 | 8 | 0 | 0 | 0 ✓ |

**三条结论**：

1. **地基检查通过** ✓：R17 上 $(A)\wedge(S)=12/26$ 非空，且有见证 $u=(-1,-1,-1)$
   ⟹ harness 没有系统性错误，前面那些"空集"是真实的；
2. **"$(A)$ 主导"的猜想错误** ✗：c282 上 $(S)$ 单独就有 26 个，不是 $(A)$ 把一切排除了；
3. **c282 上是反相关**：$(A)$ 与 $(S)$ 若独立应有约 17.5 个联合解，实际 **0**
   ⟹ 两者在 c282 上**结构性地不相容**；而 R17 上则近似独立 ✓（12 vs 12.9）。

**下一个问题**（值得做）：c282 的"$(A)\perp(S)$"是偶然还是可解释的？若是后者，它可能就是 $q_{\min}$ 的
真正来源——而不是任何单一条件。

### 2026-11-01（分支 1，B 路线）：**第一条 Lean 级结果**

文件：[tools/lean/MyProof/R17A.lean](../../../trash/lean_removed_2026-11-19/archive/attempts_2026-10/A3_basefamily/scripts/R17A.lean)（已进回归，**16 文件全绿**）

**内容**：R17 上见证 $Z=\operatorname{span}(e_5,e_6,-e_4-e_7-e_8)$ 的 $(A)$ 条件，化成**具体整数矩阵恒等式**并机器验证：

```lean
theorem R17_A_witness : A * Z * R = Z * Sel     -- AZR 落在 Z 的列空间里（显式系数）
theorem R17_Z_rank   : Z 的 3×3 子式 = !![0,0,-1; 1,0,0; 0,1,0]
theorem R17_det_witness : 该子式.det = -1        -- 非零 ⟹ rank Z = 3 = d
```

**意义**：
1. 分支 1 自开始以来**第一条达到 Lean 级**的结果（此前全是精确验证）；
2. 它把"$(A)$ 条件在具体见证上成立"变成了机器检查的事实；
3. 方法可复用：**任何具体 $Z$ 的 $(A)$ 见证都能这样形式化**（矩阵恒等式 + 子式非零）。

**注意**：这只是**一个实例的一个见证**，不是定理；但它证明了"把 $(A)$ 条件 Lean 化"的可行性。

