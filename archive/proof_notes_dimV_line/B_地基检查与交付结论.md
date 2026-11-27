# 17 — 地基检查（A）与当前可交付结论（D）

> 本文执行规划中的 **A（复查地基）** 与 **D（整理只含已证部分的报告）**。
> 规则：任何结论必须与已有判据做**独立对照**（含至少一个 True 点与 False 点）后才写入。

---

# A. 地基检查

## A1. (S) 的约化 —— ✅ **自查从零推导，成立**

**定理（新证）**：设 $N_{CA}$ 的列张成 $\ker[C;CA]$，$H=\mathcal L N_{CA}$，$F=\mathcal L AN_{CA}$。则

$$(\text{S})\iff\operatorname{rank}(\lambda H-F)=\operatorname{rank}H\quad\forall\lambda .$$

**证明**：用秩恒等式 $\operatorname{rank}[X;Y]=\operatorname{rank}Y+\operatorname{rank}(X|_{\ker Y})$（对任意 $X,Y$ 同列数）：
$$\operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[CA;C]+\operatorname{rank}\big((\lambda L-LA)N_{CA}\big)
=\operatorname{rank}[CA;C]+\operatorname{rank}(\lambda H-F),$$
$$\operatorname{rank}[CA;C;L]=\operatorname{rank}[CA;C]+\operatorname{rank}(LN_{CA})=\operatorname{rank}[CA;C]+\operatorname{rank}H .$$
两式相减，$[CA;C]$ 项**相消**，得证。$\square$

**推论（q3 的根基）**：$N_{CA}$ 为空（即 $\operatorname{rank}[C;CA]=n$，$d_{CA}=0$）时两边都只剩 $\operatorname{rank}[CA;C]$，
故 $(\text{S})$ **自动成立**。**q3（$\nu_{\min}=q_0$）的根基成立**——我此前的怀疑是多余的。

> **附注**：这条把此前对 P1 的**引用**变成了**自己的证明**，地基更稳。

## A2. 三块约化 (A)_red vs 原始 4 块 (A)_raw —— ✅ **287/287 一致**

- (A)_raw：$\operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C]$（对由参数化重建的 $\mathcal L$）。
- (A)_red：$\operatorname{rank}[W_J;B_{A,T};W_J\bar A_T]=\operatorname{rank}[W_J;B_{A,T}]$。
- **重构方式（关键）**：L=[L_0; (W_J(Θ)T^-1M_C)的后 k 行]
  （把前 $r$ 行换成真的 $L_0$；**不可**整体用 $W_JT^{-1}M_C$，其前 $r$ 行是 $L_0N_CM_C\ne L_0$）。

**结果**（`scripts/core/reliable_S_test.py` 内置检查）：14 个实例、287 个 $\Theta$
（**含 $\Theta=0$ 这个 True 点**与一般有理 False 点）：

(A)_raw=(A)_red 在全部 287 点成立，且 True 点计数完全相同

> **自查记录**：我先前一次得到 "25/26、rawT=0" 是**脚本 bug**（用了错误的重构）；
> 改用正确重构后完全一致。**这正是"独立对照"规则救了一次**。

## A3. P1 参数化定理（Theorem 3）—— ⚠️ 仍为引用，但已部分被 A2 间接验证

A2 表明：按该参数化重建出的 $\mathcal L$ 确实满足原始 4 块 (A)（在 $(\text{A})_{red}$ 成立时），
故参数化的**必要性方向**与 (A) 相容 ✓。**其完备性（覆盖所有最小 (A)-增广）未独立验证**，仍作引用。

---

# D. 当前**可交付**结论（只含已证 / 已精确计算者）

## D1. 已严格证明

| 编号 | 内容 | 依据 |
|---|---|---|
| **T1** | (5a) 是 **4 块**形式，且 $\iff(\text{A})$ | 坐标级 PDF 重建 + A2 的 287/287 |
| **T2** | $(\text{S})\iff\operatorname{rank}(\lambda H-F)=\operatorname{rank}H$ | **A1（自证）** |
| **T3** | 精确阈值：$\{\operatorname{rank}[W_J;B]=d_C\}\ne\emptyset\iff k+\dim(E+\mathrm{row}B_{A,T})\ge d_C$ | 引理 1（泛位置，含证明）+ 推论 1.1 |
| **T4** | 秩满 $\Rightarrow(\text{A})$；秩满集开；故 $\Omega^\star$ **满测度** | 引理 2、3 |
| **T5** | $(\text{S})\iff\operatorname{im}H$ 不含 $T$ 的特征向量 | 引理 5′ |
| **T5′（本轮新得，已证）** | 由 (A)，$\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$，而 $CN_{CA}=CAN_{CA}=0$，故 $F=\mathcal L AN_{CA}=\Lambda H$，即 $P_{\mathcal L}(\lambda)=(\lambda I-\Lambda)H$。**铅笔完全由 (A)-关系中的 $\Lambda$ 决定**，$(\text{S})\iff\operatorname{im}H$ 不含 $\Lambda$ 的特征向量 | 一行代数 |
| **T5″（❌ 已撤回）** | ~~若 $\operatorname{rank}H<q_0$，则 $(\operatorname{im}H)^\perp$ 是 $\Lambda^{T}$-不变~~ —— **错**。$F=\Lambda H$ 只给"$y^{T}\Lambda H=0\Rightarrow y^{T}F=0$"（**方向相反**）；$y^{T}H=0\Rightarrow y^{T}\Lambda H=0$ **不成立**，否则即等价于 $\operatorname{im}H$ 为 $\Lambda$-不变——那正是要证的结论，循环论证。**若 T5″ 成立则 (C2) 必被推翻**（$\operatorname{im}H$ 不变 ⟹ 含特征向量 ⟹ (S) 必失败），而数值为 486/486 的 (S) 成立 ⟹ 矛盾 ⟹ T5″ 错 | **撤回（第 9 处更正）** |
| **T6** | $d_{CA}\ge q_0\Rightarrow(\text{S})$ 恒假 $\Rightarrow\Sigma^{(S)}\subseteq\{\operatorname{rank}H<q_0\}$（真闭，零测） | 定理 B |
| **T7** | $d_{CA}=1\Rightarrow$ **(S) 在见证处开** $\Rightarrow$ **BPP** | 定理 C（**已更正**，见下） |
| **T8** | $2\le d_{CA}<q_0$：**无条件二分**——(a) BPP，或 (b) 解集落在真闭代数集（零测）上 | 定理 A（引理 8 + 跳变集零测 + 满测度） |
| **T9** | 跳变集零测：$\mathcal N^c\subseteq\{\operatorname{rank}H<\beta_{\max}\}$ | 引理（最高秩层开） |

## D2. 已精确计算（非证明，但精确算术验证）

| 结果 | 数据 |
|---|---|
| 铅笔既约形式 $\big((\text{A})\iff\forall i:q_i\in\mathrm{row}P\big)$ | 31/31 × 8 实例（含 True 点） |
| $(1,3)$ 情形解数 | **恰好 2**（判别式，10/10 实例） |
| 情形 II：$(\text{A})∧(\text{S})$ | **0/200** |
| 情形 I：$(\text{A})∧(\text{S})$ | **87/87 = 100%** |
| 情形 I：扰动不变性 | **12/12 × 9 实例** |
| $\operatorname{rank}H=d_{CA}$ 在所有 $(\text{A})$-点 | **287/287** |
| $(\star''')$ 决定性实验 | **56/56** |

## D3. 未定

| 缺口 | 说明 |
|---|---|
| **q1 真伪** | 完全未定 |
| $d_{CA}\ge q_0$ 的**复杂度** | 只证零测；是否存在别的 BPP 算法未知（**硬度首要候选**） |
| 支 B（$2p+q_0<n$） | 解数多项式界未证 |
| $(\star''')$ | 只决定 T8 落哪一支（数值落 (a)） |
| P1 参数化的**完备性** | 引用 |

## D3.5 ⚠️ 定理 C（$d_{CA}=1$）的**陈述更正**（结论不变）

**原陈述（错）**：$d_{CA}=1$ 时失败 $\iff H\wedge F=0$（声称 $H=0$ 时亦成立）。

**错在哪**：漏了 $H=0$ 的情形。逐项重推（$H,F$ 皆为列，$\operatorname{rank}\in\{0,1\}$）：

| 情形 | $(\text{S})$ 成立的条件 |
|---|---|
| $H\ne0$ | $\lambda H-F\ne0\ \forall\lambda\iff F\not\parallel H\iff \boxed{H\wedge F\ne0}$ |
| $H=0$ | $\operatorname{rank}F=0\iff\boxed{F=0}$ |

**⟹ 失败集** $=\{H\ne0,\ H\wedge F=0\}\cup\{H=0,\ F\ne0\}$ —— **不是闭集**：
其闭包为 $\{H\wedge F=0\}$，而 $H=F=0$ 在闭包中却**不在**失败集里。故 $(\text{S})$ **不是** Zariski-开。

**但结论（BPP）仍成立**，理由改为：
> 取见证。若 $H\ne0$，则见证处 $H\wedge F\ne0$，而 $\{H\wedge F\ne0\}$ 是**开邻域**
> （其中恒有 $H\ne0$ 且 $H\wedge F\ne0$ ⟹ ⊆ $(\text{S})$）⟹ 见证集含非空开集 ⟹ 正测度 ⟹ **BPP** ✓
> 若 $H\equiv0$：$(\text{S})\iff F\equiv0$，恒真或恒假，判定平凡 ✓

**⟹ T7 的结论不变，但陈述与证明已更正。**（本会话第 **8** 处更正，记录以免再被误用。）

---

## D3.6 🔴 **范围限定**（必须与所有 $\Theta$ 相关结论一并引用）

**全部基于 $\Theta$ 参数化的结论**（三块约化、引理 1–8、定理 A/B/C、定理 D1/D2，
以及数值 486/486、87/87、287/287 等）**都以 P1 的参数化图卡为前提**：

(P1 图卡条件)   rank(R N_C K)=k,   K=ker (L_0N_C) 的基.

**原因**：P1 的 $W_J=\begin{bmatrix}I_r&0\\0&[I_k|\Theta]\end{bmatrix}$ 底部块恒为秩 $k$，
故该参数化**只能表示"商空间中 $k$ 行独立"的增广**。

**确实存在落在图卡之外的实例**：取 $L_0=C A^m$ 造出的实例
（$n{=}5,p{=}1,r{=}1$，$\eta=[3]$，$q_0=3$，$k=2$）满足 H1–H4 且 `condA(Lx)=True`，
但 $\operatorname{rank}(RN_CK)=1<2$ ⟹ **无法进入参数化**。

⟹   上述所有结论仅在图卡内成立，不得声称为全体实例的定理。

**⚠️ 相关纠正（本会话第 10 处）**：曾推断
"$\operatorname{rank}(RN_CK)<k\Rightarrow$ 非最小 $\Rightarrow\eta$ 高估"——**该推断错误**：
$\operatorname{rank}(RN_CK)$ 度量 $R$ 在**子空间** $\ker C\cap\ker L_0$ 上的作用，
**子空间上相关 $\ne$ 全局相关**，故**不能**推出非最小性。**未证实 $q_0$ 有误。**

**仍未解决的核对**：$q_0=\sum\eta_j$ 缺少**独立**验证路径。
早前笔记里的闭式 $k_{\min}=\dim Z-\dim V$ 经本轮核对**与 $q_0$ 不是同一个量**
（`history/scripts/P2_check_q0.py`：全部实例 $\dim Z=n$，而 $q_0$ 在 1–4 间变化）。

### D3.6.1 ⚠️ 为什么下界**原理上**难以独立验证（必须记录）

- **上界**可独立验证：`p1` 给出的 $L_x$ 有恰好 $q_0$ 行且 `condA=True` ✓
- **下界**（"没有更少行的增广"）**无法**用暴力/随机法验证：
  - `P2b/P2c`（枚举轨道行 $\{CA^k,L_0A^k\}$ 的子集）**不完备** ——
    最小增广的行**可以是这些轨道行的线性组合**，故该搜索会**高估**最小值
    （实测：报"最小 3 > $q_0=2$"，与 `p1` 的 2 行可行解矛盾 ⟹ 证明搜索不完备）；
  - `P2d`（加入 300 个随机方向/实例）**0 命中** ⟹
    **可行 $w$ 的集合是 $\mathbb{R}^n$ 中的真代数子集（零测）**，随机采样必然错过。

⟹   下界只能引用 P1 的 Theorem 2（q_0=Ση_j），本项目未独立验证。

**这是本项目最重要的单点依赖**：$q_0$ 是全项目阈值表述的核心，却只有**一个来源**。

### D3.6.2 四步验证计划的执行结果

| 步骤 | 内容 | 结果 |
|---|---|---|
| **P1** | 定位 conic 检验 0 命中的真因 | ✅ `rank(R N_C K) = 1 < k = 2`（P1 图卡前提被违反） |
| **P2** | 独立核对 $q_0=\sum\eta_j$ | ⚠️ **完成但结论有限**：闭式候选与 $q_0$ 不是同一量；暴力/随机法**原理上无法给下界**；**未发现矛盾**；纠正了第 10 处过度推断 |
| **P3** | B-1（(C2) 的 $k\ge2$ conic 检验） | ❌ **未完成** —— 需要的 $k\ge2$ 实例全部落在 P1 图卡之外 |
| **P4** | 文档更新 | ✅ 本文件 + `proof/20` + README |

## D4. 已撤回 7 项（**不得引用**）
旧引理 4（$\Omega^\star$ 闭）、旧引理 5（(S) 一般 Zariski-开）、引理 7（逐层闭）、猜想 (S0)、
旧 `condS`、"$(A)\iff$ 秩满"、"**P1: q1 的 NP-hard 断言为假**"（ETR 本身即 NP-hard）。

## D5. 交付的一句话

> **q1 未解决。已确定的是**：
> **(i) 硬度的唯一可能来源在 (5b)/(S) 侧**；
> **(ii) 精确阈值是 $k+\dim(E+\mathrm{row}B_{A,T})\ge d_C$**；
> **(iii) 当 $d_{CA}=1$ 时不是 NP-hard（BPP）；当 $2\le d_{CA}<q_0$ 时无条件二分；当 $d_{CA}\ge q_0$ 时 (S) 零测、采样必然失效（复杂度未定，且这是硬度首要候选）**；
> **(iv) 所有结论以 P1 参数化为前提，未见机器验证或独立复核。**
