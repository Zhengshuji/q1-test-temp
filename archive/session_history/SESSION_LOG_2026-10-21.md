# 会话日志（2026-10-20 → 22）

> 这是从 [OPEN_PROBLEM.md](../OPEN_PROBLEM.md) §12–§13 移出的**过程记录**。
> 它包含方向、任务清单、禁区、会话总账——**结论请以 OPEN_PROBLEM 与 proof/ 为准**。

---
## §12 下一步的两条方向（2026-10-20 记录）

### 方向 1（优先）：证明 $\rho_{\min}$ 公式里"(b)-liftable"的那一半

$$\text{待证命题}\ :\quad \Lambda_{\mathcal A}\ \text{不良定义}\ \Longrightarrow\ \Phi^\infty(\operatorname{span}\{\alpha_0,r\})\ \text{可 lift}$$

| 已确立 | 内容 |
|---|---|
| 下界方向 | 任何 admissible 的 $\mathcal A\supseteq\{\alpha_0,s\}$ 都包含某个候选（$\Phi^\infty$ 是最小闭包）|
| 数值 | $d=2,3,4$ 共 103 例 0 反例（[proof/P](../proof/P_rho_min公式重验_2026-10-20.md)）|
| $d=2$ | $\rho_{\min}\in\{1,2\}$，且 $\rho=1\iff$ P7 —— **可由 P7 + P1 推出**（[proof/Q](../proof/Q_d2_定理_2026-10-20.md)）|
| 必要条件 | $(b)\Rightarrow vG\ne0$（$v$ 张成 $\ker M^{\mathsf T}$），883 例 0 反例，**不充分** |

$$\textbf{若证成}\ \Longrightarrow\ \rho_{\min}\ \text{有闭式}\ \Longrightarrow\ q_{\min}\in\mathrm{P}\ \Longrightarrow\ \textbf{q1 为假}$$

**技术障碍**：一般 $d$ 下需在 lift 参数上做**符号消元**（resultant/Gröbner），
项目历史上已记为平台期（`DIRECTIONS.md` D1）。$d=2$ 的严格版见 [proof/Q](../proof/Q_d2_定理_2026-10-20.md)。

#### 🆕 2026-10-20 深夜进展：**跳层定理**（[proof/R](../proof/R_跳层定理_2026-10-20.md)）

$$\text{在 (a0) }\beta_0=c\alpha_0,\ \text{(r) }\operatorname{rank}(AN-cN)=d,\ \text{(u) }\dim U=1,\ \text{(o) }\mathrm{obs}=d\ \text{下：}$$
$$\boxed{\ q_{\min}\in\{2,\ \mathrm{obs}+1\}\quad(\text{中间层全部不可行})\ }$$

证明：$\ker\psi\subseteq V_{\mathcal A}$（$\psi=AN-cN$）+ $\dim\varphi_c\le2\rho-d\le\rho-1$（$\rho\le d-1$）+ 第一行 $c\alpha_0-\beta_0=0$。

* 验证：$d{=}3$（210 次）、$d{=}4$（$q{=}3,4$ 全败、$q{=}5$ 全成）
* **边界**：$\dim U=\dim S'$；$p{=}1$ 时 $\dim U=1$（跳层），$p\ge2$ 时 $\dim U\ge2$ ⟹ **跳层失效**
  （实测 $p{=}2$：$q=3$ 成功 30/30、40/40）

#### ✅ 最终经验定律（替代已被证伪的"三值猜想"）

> ⚠️ **"$q_{\min}\in\{2,3,\mathrm{obs}+1\}$" 已被证伪**：$(p{=}2,d{=}4)$ 上 $q{=}3$ 失败（0/30）、
> $q{=}4$ 成功（6/6）。见 [proof/R](../proof/R_跳层定理_2026-10-20.md) §7.1。

$$\boxed{\ q_{\min}=\begin{cases}2 & \text{P7 成立}\\[2pt] \max\big(3,\ d+2-p\big) & \text{否则}\end{cases} }$$

| $(p,d)$ | 公式 | 实测 |
|---|---|---|
| $(1,3),(1,4),(1,5)$ | $4,5,6$ | ✓ ✓ ✓ |
| $(2,3),(2,4)$ | $3,4$ | ✓ ✓ |
| $(3,3),(3,4)$ | $3,3$ | ✓ ✓ |

$$\textbf{7/7 一致（未证）};\qquad \rho_{\min}=d+1-p\ \Longleftrightarrow\ \dim(\mathcal A\cap S)=1\ \text{且}\ \mathcal A+S=\mathbb{R}^d$$

**结构猜想（双向证据）**：

$$\text{可 lift}\ \Longrightarrow\ \mathcal A+S=\mathbb{R}^d\ \text{且}\ \mathcal A\cap S\ne0$$
$$\text{证据}：24/24\ \text{个可 lift 的 3 维}\ \mathcal A\ \text{都满足};\quad 25\ \text{个坏平面} \times 3\ \text{个}\ q = 75\ \text{次全败}$$

$$\Longrightarrow\ \text{若两端都证成}\ \Longrightarrow\ q_{\min}\in\mathrm{P}\ \Longrightarrow\ \textbf{q1 为假}$$

### 方向 2：NP-hard 归约（与方向 1 互斥的另一侧）

$$\text{目标}\ :\ \text{从已知 NP-hard 问题归约到}\ "q_{\min}\le k"\ \text{的判定}$$

**硬约束**（不能违反，否则归约无效）：

$$N^{\mathsf T}R_0=0\ ;\qquad \operatorname{row}(R_0)\subseteq\operatorname{row}(N)\ ;\qquad S\ \text{的满射性}$$

即 $A',R_0$ **不是**独立可取的矩阵——它们由 $(A,C)$ 决定。

**现状**：无进展。若要动，建议从"$\rho\le2$ 的判定"入手（$\mathrm{Gr}(2,d)$ 上的双线性条件，$\exists\mathbb{R}$ 型）。

### 方向 3（兜底）：把已知结构写成定理链

若 1、2 都推不动，则至少把
$$\text{P7}\ \Rightarrow\ q_{\min}\le2\ \text{可判}\ ;\qquad \rho_{\min}\le\mathrm{obs}\ ;\qquad \text{分层 }2/3/\mathrm{obs}+1$$
整理成一篇自洽的短论文（素材已在 `proof/` 与 `PAPER.md`）。

---

## §13 会话总账（2026-10-20 → 21，**下次从这里接**）

### 13.1 一句话现状

$$\boxed{\ \text{若 }"\ q_{\min}=2\ \text{或}\ \max(3,\ d+2-p)\ "\ \text{成立}\ \Longrightarrow\ q_{\min}\in\mathrm{P}\ \Longrightarrow\ \textbf{q1 为假}\ }$$

该定律有 **8 个 $(p,d)$ 组合（精确有理数验证）**支撑。**维数恒等式与弱下界已证**（[proof/S](../proof/S_维数下界定理_2026-10-21.md)）：

$$\dim\{\ell N:\ell\in V_{\mathcal A}\}=2\rho-d+p-|\mathcal A\cap S|\ \Longrightarrow\ \rho\ge d-p+|\mathcal A\cap S|\ \overset{|\mathcal A\cap S|\ge1}{\ge}\ d-p+1$$

✅ **$|\mathcal A\cap S|\ge1$ 已于 2026-10-21 证明**（S §5.1d）。

#### 🆕 2026-10-22 结构性突破：下界的一条**等价形式**

$$\text{下界}\ \rho\ge d-p+|\mathcal A\cap S|\quad\Longleftrightarrow\quad \mathcal A+S=\mathbb{R}^d\quad\Longleftrightarrow\quad (L\text{-}1)$$

（三者等价，见 S §1.4–1.5；**所以不能"先证 (L-1) 再得下界"——那是循环**。）

$$\boxed{\ \textbf{正确的证明目标}:\quad \text{若存在 lift 且}\ \mathcal A+S\ne\mathbb{R}^d\ ,\ \text{则}\ \textbf{P7 成立（}\rho=1\text{ 的 lift 存在）}\ }$$

$$\Longleftrightarrow\quad \text{P7 假}\ \Longrightarrow\ \text{每个 liftable 的}\ \mathcal A\ \text{都有}\ \mathcal A+S=\mathbb{R}^d\ \Longrightarrow\ \rho\ge d-p+1$$

**为什么这条不平凡**：它不是说"$\mathcal A+S=\mathbb{R}^d$ 自动成立"（假的，P7 分支就是反例），
而是"**非饱和的 lift 必可压到一行**"。

**证据**（S §1.8–1.9）：所有搜过的非饱和构型（$\mathcal A\supseteq S$ 的 25 个平面、$\mathcal A=S$、P7 假实例的系统扫描）**一次也没 lift 成功**。

剩余缺口：**上界（可达性）**（数值 12/12、6/6、4/4）**+ 上述压缩构造的证明**。

### 13.2 本轮新增（按可信度）

| 级别 | 内容 | 文档 |
|---|---|---|
| **已证（新）** | 维数恒等式 $\dim\{\ell N\}=2\rho-d+\dim S'-|\mathcal A\cap S'|$ ⟹ $\rho\ge d-p+|\mathcal A\cap S|$（弱下界；$|\mathcal A\cap S|\ge1$ 未证）| [S](../proof/S_维数下界定理_2026-10-21.md) |
| **已证** | 计数条件 $\dim V_{\mathcal A}\ge n-2(d-\rho)$；$\Rightarrow q=\rho+1$ 需 $n\ge2d-2\rho$ | [K](../proof/K_维数计数_2026-10-20.md) |
| **已证（条件性）** | 跳层定理：在 (a0)(r)(u)(o) 下 $q_{\min}\in\{2,\mathrm{obs}+1\}$ | [R](../proof/R_跳层定理_2026-10-20.md) |
| **已证** | $d=2$：$\rho_{\min}=1\iff$P7，否则 $2$ | [Q](../proof/Q_d2_定理_2026-10-20.md) |
| **反例** | **P6b 假**（$n{=}5,q{=}3,\rho{=}2$，三套实现复核）| [I](../proof/I_P6b_反例_2026-10-20.md) |
| **数值定律** | $q_{\min}=2$ 或 $\max(3,d+2-p)$，**8/8** $(p,d)$ 组合 | [R](../proof/R_跳层定理_2026-10-20.md) §7.2、[S](../proof/S_维数下界定理_2026-10-21.md) §7 |
| **上界猜想** | $\mathcal A_L=\operatorname{span}\{\alpha_0,\beta_0\}+L$ 对**任意**线 $L\subseteq S$ 可 lift（**99/99**）| [S](../proof/S_维数下界定理_2026-10-21.md) §7.2 |
| **独立复核** | P1/A19/P4b（618 例 0 违规）；$\rho_{\min}$ 公式（103 例）| [G](../proof/G_独立复核_2026-10-20.md)、[P](../proof/P_rho_min公式重验_2026-10-20.md) |

### 13.3 下次的具体任务（按优先）

1. 🆕 **形式化任务清单（2026-10-22 记录）**：
   | 编号 | 任务 | 状态 |
   |---|---|---|
   | F1 | T2 的 (i) 良定义 | ✅ `WellDefined.lean` |
   | F2 | T2 的 (iii)+(iv) 特征值⟹降秩 | ✅ `EigenRankDrop.lean` |
   | F3 | T2 的**行族形式**（消掉矩阵翻译）| ✅ `RowFamily.lean`（9056 jobs）|
   | F4 | (L-2) 的维数引理 $\dim\varphi^{-1}(T)=\dim T+\dim\ker\varphi$ | ⏳ **卡在 API**：缺 `comap` 子类型的 finrank 保持引理 |
   | F5 | §1.5 的代数核心 $(vA')\cdot w$ | ✅ `DotVecMul.lean` |
   | F6 | 完整的 T2 组装（含矩阵） | ⏸ 需 F3 |

2. **上界的显式构造**：固定 $L\subseteq S$，参数化 $(\mathcal L,\Lambda)$ 的仿射解空间，证明 $(b)$ 非空。
   线索：$\Lambda$ 的最后一列全零（块三角）——见 [S](../proof/S_维数下界定理_2026-10-21.md) §7.3。
   这是**最后一个缺口**；证成即 $q_{\min}=d+2-p$ 为定理 ⟹ **q1 为假**。
2. **一般 $S'$**：把定理按 $\dim S'$ 表述（$S'=S$ 实测 30/30，但需证明或明确假设）。
3. **方向 2**（NP-hard 归约）：若定律成立则自然失效；**在定律定型前不应投入**。

### 13.4 禁区（本轮踩过）

| 禁区 | 后果 |
|---|---|
| 用"$\dim((\mathcal AA'+S)\cap\mathcal A)$"当 $\lambda=c$ 降秩的判据 | 只是必要条件，误判 4/5 实例 |
| 把 $\lambda=c$ 的行写成 $f_i=\ell_iAN$ | 实际是 $\ell_i(AN-cN)$，错了两次 |
| 把 $\dim\{\ell AN:\ell N\in\mathcal A\}$ 当 $V_{\mathcal A}$ 的像 | 漏了 $\ell AN\in\mathcal A$ |
| 断言"$\beta_0\parallel\alpha_0\Rightarrow$ 无 $q=3$" | 被 $\operatorname{rank}(AN-cN)=d-1$ 的反例推翻 |
| 用 $S$ 而非 $S'$ 写维数公式 | 只在 $S'=S$ 时成立（实测 30/30，但需作为条件）|
| 把"三值猜想 $\{2,3,\mathrm{obs}+1\}$"当结论 | 已被 $(p{=}2,d{\ge}4)$ 的 0/30 推翻 |
| **用随机 $\lambda$ 采样判 $(b)$** | $(b)$ 的失败集是**有限点集**，采样必漏 ⟹ 系统性**假阳性**（`c156`，已废）。**只能用 $\rho$ 阶子式的 gcd** |
| 预设 $\Lambda_{\mathcal A}$ 的形状（如幂零）来构造 | 实测真实解里 $\Lambda_{\mathcal A}$ **满秩**、特征多项式**无固定形状**（[proof/S](../proof/S_维数下界定理_2026-10-21.md) §7.0d/e）|

### 13.5 🆕 两个 Gap（2026-10-22 记录）

$$\textbf{Gap 1（硬）}:\quad \mathcal A+S\ne\mathbb{R}^d\ \wedge\ \text{存在解}\ \Longrightarrow\ \exists\ \rho=1\ \text{的解（P7）}$$

- **等价性**：(L-1)、下界 $\rho\ge d-p+1$、$\mathcal A+S=\mathbb{R}^d$ 三者等价（§1.4–1.5），故无"先证 (L-1)"的路线；
- **证据**：所有搜过的非饱和构型（25 平面 / $\mathcal A=S$ / 12 次系统扫描）**0 命中**；
- **详细说明（自足、可直接转发）**：[`proof/T_Gap1_非饱和lift.md`](../proof/T_Gap1_非饱和lift.md)
- **状态**：❌ 未证，无新想法

$$\textbf{Gap 2（软）}:\quad \text{上界的}\ (b)\ \text{在一个 18 维 lift 仿射空间里\textbf{非空}}$$

- $(a)$ 型约束线性（含 0），但 $\operatorname{rank}M=\rho$ 与 $(b)$ 是**开条件**，需证非空；
- **证据**：随机点上 $(a)\wedge(b)$ 成立 90–100%（4 实例、130 次）；
- ✅ **已给出显式构造**（S §7.11）：$\Lambda v_i=a_i+\eta_il$、$\ell_i=v_iN^++k_i$（$k_iN=0$、$k_iR_0=\Lambda v_i+c_il-v_iA'-v_iN^+R_0$）
- **验证**：随机 $(\eta,c)$ **12/12**；固定 $(\eta,c)\in\{0,1\}^3$ **25/25**；固定参数跨实例 **6/6**
- **状态**：🟡 构造已显式、数值全过；**仍缺**"$(b)$ 对所有实例成立"的证明
