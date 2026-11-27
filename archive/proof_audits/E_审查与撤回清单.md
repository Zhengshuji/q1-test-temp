# 13 — 支 A 证明的严格审查

> 对分支 A（$2p+q_0\ge n\ \Rightarrow$ 判定 ∈ BPP）的证明链**逐步复核**。
> 结论：**发现 1 条引理是错的（但不需要），1 个必需步骤未证出（真实缺口）**。
> 因此支 A **不能**称为"已完全证明"，必须降级。

---

## 0. 支 A 的原始证明链（待审）

| 步 | 内容 |
|---|---|
| S0 | 约化到 P1 的三块形式：(A) ⟺ $\mathrm{rank}[W_J;B;W_J\bar A_T]=\mathrm{rank}[W_J;B]$ |
| S1 | 引理 1（泛位置）：$\max_{\mathcal S\in\mathfrak F}\dim(\mathcal S+\mathrm{row}B)=\min(d_C,k+\dim V)$ |
| S2 | 推论 1.1：$\{\mathrm{rank}=d_C\}\ne\emptyset\iff k+\dim V\ge d_C$ |
| S3 | 引理 2：$\{\mathrm{rank}=d_C\}\subseteq\Omega^\star$ |
| S4 | 引理 3：$\{\mathrm{rank}=d_C\}$ 是开集 |
| S5 | 引理 4：$\Omega^\star$ 是 Zariski-闭集 |
| S6 | 引理 5：$\Sigma^{(S)}$ 是 Zariski-开集 |
| S7 | 合成：$\Omega^\star$ 满测度；$\Sigma_{q_0}=\Omega^\star\cap\Sigma^{(S)}$ 满测度或空 ⟹ BPP |

---

## 1. S1 引理 1（泛位置）—— ✅ 正确（但我的原始证明有一处疏漏，已修正）

**陈述**：$\mathfrak F=\{\mathcal S\in Gr(q_0,d_C):E\subseteq\mathcal S\}$，$V=E+\mathrm{row}(B_{A,T})$。则
$$\max_{\mathcal S\in\mathfrak F}\dim(\mathcal S+\mathrm{row}B)=\min\big(d_C,\ k+\dim V\big).$$

**复核**：

1. 分解 $\mathcal S=E\oplus\mathcal S'$，$\mathcal S'\subseteq E^{\complement}$（固定补空间，$\dim E^{\complement}=s$），$\dim\mathcal S'=k$。
   *合理性*：$\dim(\mathcal S\cap E^{\complement})=\dim\mathcal S-\dim E=k$ ✓。
2. $\mathcal S+\mathrm{row}B=E+\mathcal S'+\mathrm{row}B=\mathcal S'+V$ ✓。
3. **上界**：$\dim(\mathcal S'+V)=k+\dim V-\dim(\mathcal S'\cap V)\le\min(d_C,\,k+\dim V)$ ✓。

**我原先的疏漏**：可达性一步我直接引用了"两子空间泛相交"的公式 $\dim(\mathcal S\cap V)=\max(0,k+\dim V-d_C)$。
但这里 $\mathcal S'$ **被限制在 $E^{\complement}$ 内**，所以正确的公式是
$$\dim(\mathcal S'\cap V)=\dim\big(\mathcal S'\cap(V\cap E^{\complement})\big)=\max\big(0,\ k+\dim(V\cap E^{\complement})-s\big)$$
（对 $Gr(k,E^{\complement})$ 中泛位置的 $\mathcal S'$）。

**修正后的核算**：因 $E\subseteq V$ 且 $E\cap E^{\complement}=0$，有
$$V=E\oplus(V\cap E^{\complement})\ \Longrightarrow\ \dim(V\cap E^{\complement})=\dim V-r .$$
代入：
$$k+\dim(V\cap E^\complement)-s=k+\dim V-r-s=k+\dim V-d_C .$$
所以两种算法**一致**：
$$\dim(\mathcal S'+V)=k+\dim V-\max(0,k+\dim V-d_C)=\min(d_C,\,k+\dim V)\quad\checkmark$$

**结论**：引理 1 **正确**，可达性成立（在标准的"泛位置取到最小交维"事实上）。
⚠️ 该事实本身是标准结果（incidence variety 是 proper closed 集），我**引用而未证明**。

---

## 2. S2 推论 1.1 —— ✅ 正确

$\mathrm{rank}[W_J;B]=\dim(\mathrm{row}W_J+\mathrm{row}B)=\dim(\mathcal S+\mathrm{row}B)$（$\mathrm{row}W_J=\mathcal S$）。
故 $\{\mathrm{rank}=d_C\}\ne\emptyset\iff\exists\mathcal S:\dim(\mathcal S+\mathrm{row}B)=d_C\iff k+\dim V\ge d_C$ ✓（由引理 1）。

---

## 3. S3 引理 2 —— ✅ 正确但**平凡**

$\mathrm{rank}[W_J;B]=d_C$ 意味着 $\mathrm{row}[W_J;B]=\mathbb{R}^{d_C}$（行数 $\ge d_C$），
故 $\mathrm{row}(W_J\bar A_T)\subseteq\mathbb{R}^{d_C}=\mathrm{row}[W_J;B]$ ⟹ (A) ✓。
**注意**：这里 **必须** 先用 S0 的三块形式；S0 不是平凡步骤（见 §7）。

---

## 4. S4 引理 3 —— ✅ 正确

$\{\mathrm{rank}\ge d_C\}$ 是开集：它是 $\{$所有 $d_C$ 阶子式 $=0\}$ 的补集，而后者闭 ✓。

---

## 5. S5 引理 4 —— ❌ **错误！必须撤回**

**我原先的陈述**：$\Omega^\star=\{\Theta:(\text{A})\}$ 是 Zariski-闭集。
**我原先的"证明"**：$(\text{A})\iff\exists Z:ZM=N$；集合 $\{(M,N):\exists Z,ZM=N\}$ 是线性映射 $(Z,M)\mapsto(M,ZM)$ 的像，故为线性子空间，故闭。

**错误所在**：映射 $(Z,M)\mapsto(M,ZM)$ 是**双线性**的，**不是线性**的！其像一般**不是**线性子空间。

**反例（决定性）**：取 $M=(a)$（$1\times1$）、$N=(b)$（$1\times1$）。则
- $a\ne0$ 时 $\mathrm{row}M=\mathbb{R}\supseteq\mathrm{row}N$ ⟹ 条件成立；
- $a=0$ 时需 $b=0$。

所以该集合 $=\{a\ne0\}\cup\{(0,0)\}$，**既不是闭集，也不是代数集**（其 Zariski 闭包是整个平面）。

引理 4 是假的

**幸运的是**：支 A 的论证**不需要**引理 4（见 §8）。
但此前我在别处（讨论 $<n$ 情形时）用过"$\Omega^\star$ 闭"，那里必须一并撤回。

---

## 6. S6 引理 5 —— ⚠️ **未证出！这是支 A 的真实缺口**

**我的陈述**：$\Sigma^{(S)}$ 是 Zariski-开集。

**我原先的"证明"**：
1. $P_{\mathcal L}(\lambda)=(\lambda I-T_{\mathcal L})H$，故除有限个 λ 外 $\mathrm{rank}P(\lambda)=\mathrm{rank}H=:h$；
   于是所有 $(h{+}1)$ 阶子式在无穷多点为零 ⟹ **恒为零多项式**（这一步 ✅ 正确）。
2. 所以 $(S)\iff\mathrm{rank}P(\lambda)\ge h\ \forall\lambda\iff\gcd_\lambda(\Delta_1,\dots,\Delta_{N_h})=1$，
   其中 $\Delta_i$ 为 $h$ 阶子式。
3. $\mathbb{C}[\lambda]$ 是 PID ⟹ $\gcd=1\iff1\in(\Delta_i)\iff$ Sylvester 型矩阵某极大子式 $\ne0$ ⟹ **开**。

**问题所在（第 3 步的关键前提）**：
h=rankH(Θ) 依赖于 Θ!
于是"$h$ 阶子式"这组多项式**随 $\Theta$ 变化**，第 2–3 步给出的不是**一个**开条件，而是

Σ^(S)=cup_ρ(rankH=ρ_局部闭 ∩ ρ 阶子式无公共根_该层内的开集)

即 $\Sigma^{(S)}$ 是**构造集（constructible）**，而**构造集不必是开集**。

**为什么这重要**：BPP 论证需要"$\Sigma^{(S)}$ 非空 ⟹ $\Sigma^{(S)}$ 在欧氏拓扑下**稠密**"（这样才能与开稠密的 $\{$rank 满$\}$ 相交）。
- 若 $\Sigma^{(S)}$ 是 Zariski-开，则非空即为稠密 ✓；
- 若只是构造集，则可能非空但不稠密（例如退化为一个点）✗。

支 A 在这一点上有一个真实的、未补上的缺口

**等价的更清晰形式（我本轮推出的，但仍未解决开性）**：
由 $P(\lambda)=(\lambda I-T)H$ 知 $\mathrm{rank}P(\lambda)<\mathrm{rank}H$ 只能发生在 $T$ 的特征值处，且
$$\mathrm{rank}P(\lambda)=\mathrm{rank}H\iff \mathrm{im}H\cap\ker(\lambda I-T)=\{0\}$$
⟹   (S) ⟺  「T 的任一特征向量都不落在 imH 中」
（$\lambda H-F$ 是**线性铅笔**，这给了它 Kronecker 标准形的语言。）
**但 $T$ 与 $H$ 同时依赖 $\Theta$，故"无特征向量落在 $\mathrm{im}H$ 中"的开性仍不显然。**

---

## 7. S0 约化（P1 三块形式）—— ⚠️ **引用 + 数值校准，不是我的证明**

$(\text{A})\iff\mathrm{rank}[W_J;B;W_J\bar A_T]=\mathrm{rank}[W_J;B]$ 是 **P1 的式 (20)**。
我做的是：**按 P1 §VII 的原始算例逐条校准**（$\alpha=[1,2,3,1],\eta=[3,1],q_0=4$，(A)=True ✓）。
**这是"可信的引用 + 校准"，不是独立证明。** 应如实标注。

---

## 8. S7 合成 —— ✅ **不需要引理 4**，但需要引理 5

**我原先的合成**用了引理 4；但复核后发现**不需要**：

1. $\{\mathrm{rank}=d_C\}\subseteq\Omega^\star$（引理 2）✓
2. $\{\mathrm{rank}=d_C\}$ 是开集（引理 3）✓，且其补集 $\{\mathrm{rank}<d_C\}$ 是**真** Zariski-闭集
   （因 $\{\mathrm{rank}=d_C\}\ne\emptyset$，由推论 1.1 + 阈值），故测度零 ⟹ $\{\mathrm{rank}=d_C\}$ **满测度** ✓
3. 由 1、2：**$\Omega^\star\supseteq$ 满测度集 ⟹ $\Omega^\star$ 满测度** ✓ （**无需 $\Omega^\star$ 闭**）
4. **需要**：$\Sigma^{(S)}$ 非空 ⟹ 稠密（即引理 5）⟹ $\Omega^\star\cap\Sigma^{(S)}\supseteq\{\mathrm{rank}=d_C\}\cap\Sigma^{(S)}$
   是**非空开集**（两开集之交）⟹ **正测度** ⟹ 重复随机检验 $O(\mathrm{poly})$ 次 ⟹ **BPP** ✓

**所以支 A 的合成是成立的，前提是引理 5（$\Sigma^{(S)}$ 是 Zariski-开）为真。**

---

## 10. ⭐⭐ 第二轮审查：引理 5 在 $d_{CA}\ge q_0$ 时是**假的**

### 10.1 (S) 的精确等价形式（推导）

由 $P_{\mathcal L}(\lambda)=(\lambda I-T_{\mathcal L})H$（P1 Lemma）与 $\mathrm{rank}(MH)=\dim(M(\mathrm{im}H))$：

$$\mathrm{rank}P_{\mathcal L}(\lambda)=\dim\big((\lambda I-T)(\mathrm{im}H)\big)$$

⟹   (S) ⟺  ∀ λ: (λ I-T) 在 imH 上单射
 ⟺  imH 不含 T 的任何特征向量

（等价地：$\mathrm{im}H\cap\ker(\lambda I-T)=\{0\}\ \forall\lambda$。）

### 10.2 关键推论：$d_{CA}\ge q_0$ 时 $\Sigma^{(S)}=\emptyset$（一般位置）

$H=\mathcal L N_{CA}$ 是 $q_0\times d_{CA}$。
- 若 $d_{CA}\ge q_0$：$\operatorname{rank}H=q_0$（**行满秩是一般位置**）⟹ $\mathrm{im}H=\mathbb{C}^{q_0}$，
  即像空间是**整个空间**；
- 而 $T$ 是 $q_0\times q_0$ 复矩阵，**必有特征值**（代数基本定理），特征向量 $v\ne0$ 落在 $\mathbb{C}^{q_0}=\mathrm{im}H$ 中；
- 于是取 $w$ 使 $Hw=v\ne0$，有 $(\lambda I-T)Hw=0$，故 $\mathrm{rank}P(\lambda)<q_0=\operatorname{rank}H$
  ⟹ **(S) 失败**。

⟹   Σ^(S) ⊆ rankH<q_0  (当  d_CA ≥  q_0 时是真闭集)
  ⟹  Σ^(S) 不是开集，且测度为零

引理 5 在  d_CA ≥  q_0  的区域是假的

**这直接命中支 A 的合成**：BPP 论证需要"$\Sigma^{(S)}$ 非空 ⟹ 与开稠密集 $\{$rank 满$\}$ 交于正测度"。
在 $d_{CA}\ge q_0$ 区域 $\Sigma^{(S)}$ 是零测集 ⟹ **论证失效**。

### 10.3 ⭐ 由此得到一个**新的二分**，且正好呼应用户早先的"扩维"观察

| 区域 | $H$ 的形状 | $\operatorname{rank}H$ | (S) | 结论 |
|---|---|---|---|---|
| **$d_{CA}<q_0$** | 高瘦 | $\le d_{CA}<q_0$ | 一般位置**可能成立** | 支 A 的适用区（但引理 5 仍未证） |
| **$d_{CA}\ge q_0$** | 方/宽 | $=q_0$ 一般位置 | **恒假** | $\nu_{\min}>q_0$，**必须升阶** |

**第二种情形正是用户一开始指出的"$q_0$ 不保证谱可行、需要扩维"**（见 CLAUDE.md §0.1），
也正面呼应 P2 的阶谱主题。**这是本轮唯一真正的正面成果。**

### 10.4 ⚠️ 同时发现：我的 `condS` 实现**不可靠**

`check_lemma5_counterexample.py` 的实测结果与 10.2 的理论推导**矛盾**：

| 实测 | 数量 |
|---|---|
| $\operatorname{rank}H=q_0$ 的实例 | 104 个，其中 (S) 报"成立" **84** 个 |
| $\operatorname{rank}H<q_0$ 的实例 | 296 个，其中 (S) 报"成立" 296 个 |

按 10.2，(S) 在 $\operatorname{rank}H=q_0$ 时应**恒假**，却报了 84 个"成立"
⟹ **`condS` 有缺陷**：它只在 **$A$ 的特征值** + 一批有理数处检验 λ，
而 (S) 必须在 **$T$（$=\Lambda$）的特征值**处检验，两者**无必然关系**。

⟹   所有基于 condS 的数值结论都必须重做
（包括此前的 "(A)∧(S) 命中率 100%"——**这些数值支持不可信**。）

---

## 11. 审查总结（两轮合并）

| 步 | 状态 |
|---|---|
| S0 约化到三块形式 | ⚠️ 引用 P1 式 (20) + 数值校准 |
| S1 引理 1（泛位置） | ✅ 正确（含修正后的可达性证明） |
| S2 推论 1.1 | ✅ 正确 |
| S3 引理 2 | ✅ 正确（依赖 S0） |
| S4 引理 3 | ✅ 正确 |
| S5 引理 4（$\Omega^\star$ 闭） | ❌ **假，撤回**（双线性映射的像不是线性子空间；反例 $M=(a),N=(b)$） |
| **S6 引理 5（$\Sigma^{(S)}$ 开）** | ❌ **在 $d_{CA}\ge q_0$ 时假**（§10.2）；$d_{CA}<q_0$ 时**仍未证** |
| S7 合成 | ⚠️ 逻辑本身正确，但因 S6 失败而**不成立** |
| 数值支持 | ❌ **不可信**（condS 有缺陷） |

### 支 A 的最终诚实状态

支 A：未证明 —— 引理 5 在  d_CA ≥  q_0  时被证伪，在  d_CA<q_0  时未证；数值支持亦不可信

## 12. ⭐⭐⭐ 第三轮：可靠 (S) 判据下的分情形实验，**理论被证实**

### 12.1 可靠 (S) 判据（替换此前不可靠的 condS）

$$(\text{S})\iff \operatorname{rank}P(\lambda)=\operatorname{rank}H\ \ \forall\lambda,\qquad P(\lambda)=\lambda H-F$$

**可执行的严格判据**：
1. $\rho:=\operatorname{rank}H$（= $P(\lambda)$ 的一般秩）；
2. 若 $\rho=0$：$(\text{S})\iff P\equiv0$；
3. 否则取 $P(\lambda)$ 的**全部 $\rho$ 阶子式**（各为 $\lambda$ 的多项式），算它们的 **gcd**；
   $(\text{S})\iff$ gcd 是非零常数。

实现：`scripts/core/reliable_S_test.py`（严格有理算术 + 多项式欧几里得）。
**不再使用**只在 $A$ 的特征值处采样的旧 condS。

### 12.2 分情形实验（$2p+q_0\ge n$ 且 $k\ge1$，每实例 40 个一般有理 $\Theta$ 采样）

| 情形 | 实例数 | (A) 命中 | **(A)∧(S) 命中** |
|---|---|---|---|
| **$d_{CA}<q_0$** | 8 | 47/47 | **47/47 = 100%** |
| **$d_{CA}\ge q_0$** | 6 | 240/240 | **1/240** |

**⟹ 完美印证 §10.2 的理论推导**：
- $d_{CA}\ge q_0$ ⟹ 一般 $\operatorname{rank}H=q_0$ ⟹ $\operatorname{im}H=\mathbb{C}^{q_0}$ ⟹ $(\text{S})$ 恒假
  ⟹ $(A)∧(S)$ **零测** ✓（实测 1/240，那个 1 值得进一步查——见 §12.4）
- $d_{CA}<q_0$ ⟹ $\operatorname{im}H$ 是真子空间 ⟹ 一般位置无特征向量落入 ⟹ $(A)∧(S)$ **满测度** ✓（实测 100%）

### 12.3 ⭐ 分支 A 的**正确陈述**（修正版，分情形）

情形 I： d_CA<q_0 且 2p+q_0 ≥  n  ⟹  判定 ∈  BPP

- 依据：$\Omega^\star$ 满测度（引理 1–3，已证）+ $(A)∧(S)$ 满测度（§12.2 强数值支持）
  ⟹ 单点随机检验双向可靠 ⟹ BPP。
- **仍缺**：$(A)∧(S)$ 满测度的**解析证明**（引理 5 在 $d_{CA}<q_0$ 版本）。

情形 II： d_CA ≥  q_0  ⟹  BPP 论证失效（Σ^(S) 零测）

- 一般点 $(\text{S})$ 恒假（§10.2，**已证**）；故随机采样**关于 (S) 完全无信息**。
- 只能寄望于零测闭集 $\{\operatorname{rank}H<q_0\}$ 上的代数判定。

### 12.4 ⚠️ 那个 1/240 值得注意

在某个 $d_{CA}\ge q_0$ 实例中出现了 **1/40** 命中。若它真实，则
$\Sigma_{q_0}$ 在情形 II 中**非空但零测** —— 这正是"**零测但非空**"现象（教训 #15），
意味着情形 II **不能**简单判为 NO，需要显式代数求解。
（也可能是该 $\Theta$ 恰好使 $\operatorname{rank}H<q_0$，属结构退化点。）

---

## 13. ⭐ 对 q1 的启发

### 13.1 硬度的**唯一可能来源**被进一步压缩

| 区域 | 判定 | 依据 |
|---|---|---|
| $\operatorname{rank}[C;CA]=n$（$d_{CA}=0$） | 多项式，$\nu_{\min}=q_0$ | q3（已证） |
| $d_{CA}<q_0$ 且 $2p+q_0\ge n$ | **BPP** | §12.3（强数值 + 部分证明） |
| $d_{CA}\ge q_0$ | 零测代数判定 | §10.2（已证 (S) 恒假） |
| $2p+q_0<n$ | 未决（支 B） | — |

**⟹ 若 q1 的 "NP-hard" 为真，硬度必须来自最后两行之一。**

### 13.2 但这两种来源都**不像**能给出 NP-hard

1. **情形 II（$d_{CA}\ge q_0$）**：其判定是"**是否存在 $\Theta$ 使一个多项式系统有解**"——
   这是**代数/实数存在性**问题，典型复杂度类是 $\exists\mathbb{R}$ 或 **PSPACE**，
   **不是** NP-hard 的典型来源（除非有专门归约）。而且这里没有**离散选择**结构。
   > 这与 CLAUDE.md §4 路线 γ 的警告一致：**不要把连续参数搜进去，否则落到 ∃ℝ**。

2. **阶谱（扩维，q_now）**：$q$ 从 $q_0$ 扫到 $n_0-p$，是**一维的整数区间**，
   长度为 $O(n)$ ⟹ 至多 $O(n)$ 次单阶判定 ⟹ **不产生组合爆炸**。

### 13.3 由此得到的三个可检验预测

> ⚠️ **2026-10-20 注**：这三条是当年的**预测**，其中 P1 与 P3 **已被后续结果修正**：
> 可行性确实 $\in\mathrm{P}$（$\iff\alpha_0\in V$，两侧已证），但**最小化**未解决；
> 且 $\rho\ge\mathrm{obs}$ 已被反例推翻（$n{=}7,\rho{=}1,\mathrm{obs}{=}3$），
> 故"$q_{\min}=\mathrm{obs}+1-r$"不成立。见 [`../OPEN_PROBLEM.md`](../OPEN_PROBLEM.md)、[`../RESULTS.md`](../RESULTS.md)。

- **P1**：q1 的 NP-hard 断言**为假**（判定是多项式的，或至少是 BPP/代数可判的）。〔⚠️ 已被修正，见上〕
- **P2**：即使为真，也无法从**(5a) 的行选择**或**候选族**归约得到
  （前者多项式——README §2；后者不提供硬度——q2）。
- **P3**：真正的难点是情形 II 的**零测代数判定**，那是 ∃ℝ 味道的问题，
  **不是** NP-hard，因此"NP-hard"这个说法**方向就错了**。

### 13.4 对后续工作的建议（按性价比排序）

1. **先证 $d_{CA}<q_0$ 版的引理 5**（情形 I 的满测度）——目标最窄，数值已是 47/47。
2. **再攻情形 II**：先判断那 1/240 是否真实（若真实，问题变成"零测集上的代数判定"）；
   若 $\operatorname{rank}H\equiv q_0$ 可证，则该区答案恒 NO，**多项式可判**。
3. **最后回到支 B**（$2p+q_0<n$），那才是完全未开垦的部分。


