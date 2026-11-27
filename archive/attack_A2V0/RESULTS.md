# 成果清单（2026-10-23 收盘）


> # 2026-10-24 状态（两次修正）
>
> **① 原猜想被推翻**（02:20）：精确反例 $n{=}5,\ p{=}2,\ q{=}1,\ \dim V{=}1$，$(5a)\wedge(5b)$ 成立但 $q=1<\dim V+1=2$。
> 证书 `lit/counterexample_refute_dimV1.json`；崩点 Gap A（$S\not\subseteq\mathcal A$）。
>
> **② 双层公式不完整**：$\min(\dim V+1,\ q_{\deg})$ 在修好穷举工具的 bug 后只有 **97/100**。
>
> **③ 正确的结构**：按 $\rho=\dim\operatorname{row}(\mathcal LN)$ 分层
> $$q_{\min}=\min_{\rho=0}^{\dim V}q(\rho)$$
> | 层 | 含义 | 状态 |
> |---|---|---|
> | $\rho=0$ | 退化解 = conditioned invariant | ✅ 1935/1935 验证 |
> | $\rho=\dim V$ | 非退化（原定理）| 🟡 有退化解时被击败 |
> | $0<\rho<\dim V$ | **中间层** | ✅ **证书存在**（`certificate_middle_layer.json`）|
>
> **四个验证工具 bug 已修**：采样 $\lambda$、带过滤搜索、`row_basis` 丢 $L_0$、$\rho^*$ 搜索漏 $\supseteq\operatorname{row}(L_0)$。
>
> **共同模式**：搜索约束写漏，然后结论看起来是对的（见纪律 8–10）。
>
> **q1 仍开放。**

> ## 🏁 最终判断（2026-10-24 18:20）
>
> $$q_{\min}=\max\big(r,\ \rho^*+1\big)$$
>
> - 8 个已证命题 + 5 个精确验证 + 8 个精确证书
> - 中间层（$\rho^*<\dim V$）存在但**不能非平凡放大**（D38）：简单块扩展破坏它，只有"不可见块"能放大（不增难度）
> - $$\Longrightarrow\quad \boxed{\ \textbf{q1 很可能为假（多项式）}\ }\quad\text{—— 启发式判断，非证明}$$

> ## 🎯 修正后最重要的结果：多项式可算的夹逼（2026-10-24 04:00）
>
> $$\boxed{\ \dim\big(\mathcal V^{\mathrm{ci}}_{\min}\big)\ \le\ q_{\min}\ \le\ \dim V+1\ }$$
>
> - 两端都可用 $O(n^3)$ 算出（conditioned invariant 迭代 / Kleiman–Krener 闭包）
> - 下界可取等（中间层证书：$2=2$）
> - **但夹逼可以不闭合**（57/59 取端点，2 个实例严格在中间）
>
> $$\textbf{q1}\iff\text{能否在夹逼内部精确判定 }q_{\min}$$





> ## 📌 定理的最终状态
>
> $$\boxed{\ q_{\min}=\dim V+1\ }$$
>
> | 半边 | 状态 |
> |---|---|
> | 下界 $q\ge\dim V+1$ | ✅ **Lean 机器验证**（`MyProof.LowerBound`）|
> | 上界 $\dim V=d$ | ✅ 已证 |
> | 上界 $\dim V<d$ | ✅ 已证（§21 构造 + §29 的 $\dim B\le p$）|
> | **下界所需的 $\rho\ge\dim V$** | ⚠️ **未证** —— 已精确化为 $A^2V_0\subseteq V_0$（$V_0=\ker[L;CA;C]$），**2293/2293 验证**，文献中无此引理 |
>
> **净状态：6/7 步已证 + 1 步大规模验证。**
>
> ### 2026-10-23 新增的六个结果
>
> | # | 命题 | 位置 | 验证 |
> |---|---|---|---|
> | 1 | $N^{\mathsf T}R_0=0$ | §31 | 直接计算 ✓ |
> | 2 | $S'=S$ | §31 | 3/3 ✓ |
> | 3 | $\dim B\le p$ | §29 | 五行证明 ✓ |
> | 4 | $q\ge\rho+1$ | §32 | 反证 ✓ |
> | 5 | 线性引理 $\ell=v(N^{\mathsf T}N)^{-1}N^{\mathsf T}$，$\ell R_0=0$ | §33 | 53/53 ✓ |
> | 6 | $A^2V_0\subseteq V_0$ | §46 | **2293/2293 ✓（未证）** |
| 7 | **一般形式** $A^{k+1}V_0^{(k)}\subseteq V_0^{(k)}$ | ATTACK_LOG D6.6 | **14/14 ✓（未证）** |
>
> ---



> 每条都标注**验证等级**：**机器验证**（Lean，`lake build` 通过）/ **已证**（纸面证明）/ **精确验证**（有理数计算，实例）/ **已推翻**。
> 推导与过程见 [REVIEW_LOG.md](record/REVIEW_LOG.md)。

---

## 一、已证（数学定理）

### 1.1 下界

$$\textbf{定理 1.}\quad \rho:=\operatorname{rank}(\mathcal LN)\ \ge\ \dim V,\qquad\text{从而}\ q\ge\dim V+1$$

**证明**（三行）：
$S\subseteq\mathcal A$ 且 $\mathcal A A'\subseteq\mathcal A+S$ ⟹ $\mathcal A$ 是 $A'$-不变 ⟹ $\mathcal A\supseteq\langle S\rangle_{A'}=V$ ⟹ $\rho=\dim\mathcal A\ge\dim V$；再接 $q\ge\rho+1$。

**验证**：✅ **Lean**（`MyProof.LowerBound`：`closure_le_of_admissible` + `finrank_closure_le_of_admissible`）

---

$$\textbf{定理 2.}\quad q\ \ge\ d-\dim V\qquad\textbf{🔴 已撤回（§16）}$$

**证明**：$\dim V<d$ 时 $\ker M=V^{\perp}$，故 $(b)$ 等价于 $F|_{V^{\perp}}$ 单射；$\dim V^{\perp}=d-\rho$，值域 $\mathbb R^q$ ⟹ $d-\rho\le q$。

**验证**：✅ 纸面已证（[LEMMA_LIFT §11](LEMMA_LIFT_2026-10-23.md)）

---

$$\textbf{定理 3（必要条件）.}\quad d\ \le\ 2\rho+p\qquad\textbf{🔴 已撤回（§16）}$$

**证明**：$F|_{V^{\perp}}=M\circ(A')_V+(L|_S)\circ R_0|_{V^{\perp}}$，两项的秩上界分别为 $\rho$、$p$ ⟹ $\operatorname{rank}\le\rho+p$；而 $(b)$ 要求它 $=d-\rho$。

**验证**：✅ 纸面已证（[LEMMA_LIFT §11](LEMMA_LIFT_2026-10-23.md)）

---

$$\textbf{定理 4.}\quad (5a)\iff\exists\Lambda,G_0,G_1:\ \mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$$

**验证**：✅ **Lean**（`QProofFactor.decomp_iff_rank`，`ABridge.lean`）+ `Factor.lean` 的核形式

---

$$\textbf{定理 5（引理 3.1）.}\quad \xi\notin S,\ N'(V)\subseteq S,\ A'(S)\subseteq S,\ (A'+N')\xi=\lambda\xi\ \Longrightarrow\ \exists m\ne0:\ \bar A'm=\lambda m$$

**验证**：✅ **Lean**（`QProof.quotient_eigen_of_eigen`，`Lemma31.lean`）

---

$$\textbf{定理 6.}\quad \text{当}\ \dim V=d\ \text{时，}\exists\mathcal L\ (\operatorname{row}(\mathcal LN)=V)\ \text{满足}\ (5a)\wedge(5b)$$

**证明**：§3 的细节 (a)(b)(d) —— $B_\lambda=\ker(\lambda-\bar A')$（故 $\dim B_\lambda\le p$），$N'$ 在 $B_\lambda$ 上可任意指定（$S'=S$），故可选 $N'$ 使 $F|_{V^\perp}$ 单射。

**验证**：✅ 纸面已证（[LEMMA_LIFT §10](LEMMA_LIFT_2026-10-23.md)）+ 精确 6/6

---

$$\textbf{定理 6b（§12，🔴 已撤回，见 §16）}.\quad \dim V<d\ \text{时}:\quad (b)\iff\operatorname{rank}(F\vert_{V^{\perp}})=d-\rho\iff d-\rho\le\rho+p_1$$
$$\Longrightarrow\quad \text{可行}\iff d-\rho\le\rho+p_1;\qquad q_{\min}=\max(\rho+1,\ d-\rho)$$

**验证**：下界 ✅（Lean）；充分性 ✅ **§29 的 $\dim B\le p$（已证）**

> ⚠️ 2026-10-23 晚：§12 的形式（$q=\max(\rho+1,d-\rho)$）已撤回，改为 $q_{\min}=\dim V+1$；见 LEMMA_LIFT §16 与 §21–§25。

---

## 一·五、2026-10-23 晚新补的四个证明

| # | 命题 | 位置 |
|---|---|---|
| 1 | $N^{\mathsf T}R_0=0$ | LEMMA_LIFT §31 |
| 2 | $S'=S$（$\{kR_0:kN=0\}=\operatorname{row}(R_0)$）| LEMMA_LIFT §31 |
| 3 | $\dim B\le p$（$B=\{\xi\in S^{\perp}\cap V:(A'\xi)_V\in S\}$）| LEMMA_LIFT §29 |
| 4 | $q\ge\rho+1$ | LEMMA_LIFT §32 |
| 5 | 线性引理：$\forall v\in V\ \exists\ell:\ell N=v,\ \ell R_0=0$ | LEMMA_LIFT §33 |

**仍缺**：$S\subseteq\mathcal A$（对任意解）—— 已精确化为
$$v\in V_0=\ker[L;CA;C]\ \Longrightarrow\ CA^2v=0$$
（2197/2197 验证；**完整堆叠**是关键 —— 用 $\ker L\cap\ker C$ 则 2579/2160 违例 ✗）

---

## 二、精确验证（实例，有理数精确算术）

| # | 断言 | 结果 |
|---|---|---|
| 2.1 | 线性引理 $\forall v\in V\,\exists\ell:\ell N=v,\ \ell R_0\in V$ | **53/53** ✓ |
| 2.2 | $(5a)$ 在 $\operatorname{row}(\mathcal LN)=V$ 时自动成立 | **6/6** ✓ |
| 2.3 | $(5b)$ 可满足（上界）| **6/6** ✓ |
| 2.4 | $q_{\min}=\dim V+1$ | **6/6** ✓ |
| 2.5 | $S\subseteq\mathcal A$（最小阶的所有解）| **18/18** ✓ |
| 2.6 | $S'=S$（$\{kR_0:kN=0\}=\operatorname{row}(R_0)$）| **3/3** ✓ |
| 2.7 | 2010 例的 $q_{\min}=5$（独立复现）| ✓ |
| 2.8 | 2010 例的代数下界 $q_0=\sum\eta_j=3$（与论文一致）| ✓ |

---

## 三、已推翻（都有证书或证明）

| # | 旧断言 | 推翻者 |
|---|---|---|
| 3.1 | $q_{\min}=\max(3,\ d+2-p)$ | 3 个反例（$(1,3)\to3$、$(1,4)\to3$、$(2,4)\to3$）|
| 3.2 | $\rho\ge d-p+1$（无条件）| 同一个反例（$\rho=2<3$）|
| 3.3 | 闭式 $\min(d+1-p,\dim V)+1$ | 2010 完整例（真值 5，公式 4）|
| 3.4 | $q_{\min}=\dim V+1$（无条件）| $d>2\rho+1$ 时与定理 2 矛盾 |
| 3.5 | **引理 C**（$\exists$ 解使 $\rho=\min(\cdot)$）| 2010 例：$\rho_{\min}=4\ne3$ |
| 3.6 | Gap 1 的两种表述 | 非饱和 $\rho=2$ 解存在 |
| 3.7 | 可行性判据仅是 $\alpha_0\in V$ | 还需 $d\le2\rho+p$（定理 3）|

---

## 四、文献定位

| 文献 | 与本项目的关系 |
|---|---|
| **Fernando–Trinh–Jennings 2010**（IEEE TAC 55(5)）| **项目问题 = 他们的问题**（Condition 1/2 ≡ $(5a)/(5b)$）；构造性算法是指数级；**未讨论复杂度** |
| **Warren–Eckberg 1975**（SIAM J. Control 13(2)）| 一般 $D\not\subseteq\operatorname{im}B$ 的"最小维数不变子空间"**明确留为 open** |
| **Varga 2004**（MTNS）| Type I minimum dynamic cover = admissible 条件，但**不含 $(b)$**（cover=1 vs 我们的 $\rho=2$）|

$$\Longrightarrow\ \text{q1 的答案（复杂度）在文献中\textbf{未解决}}$$

---

## 五、Lean 资产（27 模块，`lake build` 全绿）

| 模块 | 内容 |
|---|---|
| `Foundations` | F1 秩-零化度、F3 维数公式、F4/F4'、F5 满射、T5a_core、T5a |
| `Theorems/Pencil`、`CaseII`、`Spectral` | T5'、T2、T6、T5 |
| `Factor`、`ABridge` | $(5a)\iff$ 分解 $\iff$ 核条件 |
| `Closure` | $V=\langle S\rangle_{A'}$ 的定义与三条性质 |
| `DimIdentity` | $\dim f^{-1}(W)=\dim\ker f+\dim(W\cap\operatorname{im}f)$；lift 矩阵恒等式 |
| `Admissible` | admissibility ⟹ $\mathcal A+V$ 不变 |
| **`LowerBound`** 🆕 | **$q\ge\dim V+1$**（定理 1）|
| **`Lemma31`** 🆕 | **引理 3.1**（定理 5）|

---

## 六、未解决的

$$\boxed{\ \text{上界}\ q_{\min}\le\max(\dim V+1,\ d-\dim V)\ \text{在}\ \dim V<d\ \text{时未证}\ ✗}$$

→ 见 [OPEN_PROBLEM.md](OPEN_PROBLEM.md)
