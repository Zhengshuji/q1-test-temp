# DIRECTIONS.md — 所有研究方向的索引（便于后续接手）

> 本文汇总**所有曾经/正在推进的方向**，含：目标、现状、关键结论、障碍、脚本、文档。
> **结论以 [FINAL.md](../../FINAL.md) 为准**；本文只做"导航"。
> 最近更新：2026（本轮）
>
> ⭐⭐ **一键复现本会话全部关键论断**：`python scripts/core/verify_all.py`
> （**完全独立实现**，不 import 项目库；复现 A 无穷族 / B $k{=}0$ 见证 / C NO 侧一致性；**最后一次全部通过 ✓**）
>
> 🔴🔴🔴 **最重要：[history/51](../51_hand_verifiable_counterexample.md)、[52](../52_session_conclusion.md)**
> —— **c6 / c6′ 已被<u>可手算的无穷族</u>证伪**（$n\ge4$）⟹ "情形 II 恒 NO" 为假 ⟹ 分支 A 未被排除
> **但** $|R|_{\min}=1$ ⟹ **不建立 NP-hardness** ⟹ 主线的硬度问题**仍开放**

---

## 0. 主线与已知的归结

$$\textbf{主线 q1}：\text{求最小行数}\ R\ \text{使}\ \begin{bmatrix}L_0\\R\end{bmatrix}\ \text{满足}\ (5a)\wedge(5b)\ \text{——是否 NP-hard？}$$

$$\text{等价}：\text{判定}\ \nu_{\min}=q_0\ ?\qquad(\nu_{\min}=\text{最小谱可行阶})$$

### 0.1 ⭐ 归结链（本轮/近期成果）

$$\underbrace{\text{q1}}_{\text{NP-hard?}}\ \longleftarrow\ \underbrace{\mathcal P}_{\text{单一判定问题}}\ \longleftarrow\ \begin{cases}\text{情形 II（分支 A 内）}\\ \text{支 B}\end{cases}$$

$$\boxed{\ \mathcal P:\quad \exists\,\Theta:\ (A)(\Theta)\ \wedge\ \operatorname{rank}\big(\mathcal L(\Theta)N_{CA}\big)<q_0\ }$$

**$\mathcal P$ 的两种证法**：
- **难** ⟹ 归约（方向 1）
- **易** ⟹ 多项式算法（方向 2）

**文献地位**（[Blondel–Tsitsiklis 综述](https://perso.uclouvain.be/vincent.blondel/publications/99BT-survey-full.html)）：
ETR **可判定**（$m(n{+}1)d^{O(n)}$）；「秩-1 仿射族」判定 **NP-hard**（有限域）；
「静态输出反馈」**可判定但 NP-hard 性未知** —— $\mathcal P$ 与后者同类。

---

## 1. 方向总表

| # | 方向 | 目标 | 状态 | 关键文档 |
|---|---|---|---|---|
| **D1** | **归约 ⟹ q1 是 NP-hard** | 从 NP-完全问题归约到 $\mathcal P$ | 🔴 **平台期**（Gröbner 不可行）| [history/35](../35_reduction_design.md)、[36](../36_two_routes.md) |
| **D2** | **多项式算法 ⟹ q1 非 NP-hard** | 给 $\mathcal P$ 的多项式解法 | 🔴 两个猜想皆假 | [history/36](../36_two_routes.md) |
| **D3** | **c6′（情形 II 平行）** | 平行 ∧ (A) ∧ T5a ⟹ (S) 失败 | 🔴 **$k{=}0$ 时被证伪**（见证 13/13 独立复核）；⭐ **定理：非退化平行 ⟹ $k{=}0$** ⟹ **$k\ge1$ 范围平行 ⟹ 退化**，故 c6′ 在 $k\ge1$ **仍开放** | [history/47](../47_c6p_refuted.md)、[48](../48_refutation_scope.md) |
| **D4** | **(A) ⟹ 分解** | $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$ | 🟢 **✅ 已完成（Lean 0 error，已并入主库）** | [history/37](../37_D4_progress.md)、`Theorems/D4.lean` |
| **D5** | **B2：支 B 的 $\Omega^\star_J$** | $k{=}1$ 单点 / $k\ge2$ 正维数 | 🟢 **已完备**（数值 15 例 × 4 判据 + Lean 组装）| [history/29](../29_B2_result.md)、[30](../30_B2_proof_skeleton.md)、`Theorems/B2.lean` |
| **D6** | **$q_0$ 下界** | 证 $q_0=\sum\eta_j$ 是最小 $(A)$-行数 | 🟡 **与 D3 的退化分支汇合**：退化时 $k_{\min}=$ 最小 $\bar A$-不变子空间维数（模论对象）；3 个显式候选公式皆败 | [history/41](../41_D6_structure.md)、[49](../49_degenerate_reduction.md) |
| **D7** | **图卡限定** | 结论仅在 $\operatorname{rank}(RN_CK)=k$ 内成立 | ⚠️ 未解决 | `problems/q4.md` §3.6 |
| **D8** | **T12 的验证** | 情形 II 不平行 ⟹ NO | 🟢 **✅ 已澄清**（旧验证对 T12 是完整的，因 $r{=}1$）| [history/37](../37_D4_progress.md) §5 |

---

## 0.2 ⭐ 最新进展（本轮）

### 0.2.1 🎉🎉🎉 **c6′ 端到端完成**（见 [history/45](../45_c6p_complete.md)）

$$\boxed{\ (A)\wedge CA^2=0\wedge \text{参数化}\wedge H\ne0\ \Longrightarrow\ \exists\Lambda:\ F=\Lambda H\ \wedge\ \textbf{(S) 失败}\quad(\text{代数闭域})\ }$$

**完整 5 步链（全部机器验证）**：

| 步 | 内容 | 定理 |
|---|---|---|
| 1 | $(A)\iff$ 分解（秩-零化度）| **`decomp_iff_rank`** |
| 2 | 分解 ⟹ $F=\Lambda H$ | `F_eq_Lam_comp_H` |
| 3 | $A$-不变 ⟹ $F=H\circ A'$ | **`F_eq_comp_of_fact`** |
| 4 | ⟹ $\Lambda$ 保持 $\operatorname{im}H$ | **`maps_range_of_comp_eq`** |
| 5 | 特征值 ⟹ (S) 失败 | **`S_fails_of_eigenvector`** |
| 总装 | $CA^2=0$ ⟹ (S) 失败 | **`c6'_CA2_algclosed`** |

$$\textbf{主库}\ \texttt{lake build}\ \to\ \textbf{Build completed successfully (18128 jobs)}\ ✓$$

### 0.2.2 ⚠️ 关键：必须**代数闭域**

$$\text{非代数闭域上}\ \Lambda|_{\operatorname{im}H}\ \text{可能无特征值（如旋转）}\ \Longrightarrow\ \text{(S) 可能成立}$$
$$\text{与项目 (S) 判据一致（gcd 检测}\ \overline{\mathbb{Q}}\ \text{中的根）}\ ✓$$

### 0.2.3 🔴🔴🔴 **本轮最终发现：c6 / c6′ 被显式见证证伪**（见 [history/47](../47_c6p_refuted.md)）

$$\boxed{\ \text{存在}\ \textbf{情形 II + 非退化平行}\ \text{实例，使 H1–H4 ∧ (5a) ∧ (5b) 全部成立}\ ⭐⭐⭐}$$

| 项 | 值 |
|---|---|
| $(n,p,r,q_0,d_{CA})$ | $(6,1,2,2,4)$ ⟹ **情形 II**（$4\ge2$）✓ |
| H1–H4 | ✅ 全部 |
| **(5a)** | ✅ $\operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C]=3$ |
| **(5b)** | ✅ **两个独立判据**：$r_0$ 阶子式 gcd 为常数 + 12 个具体 $\lambda$ 逐一算秩 $=3$ |
| 真平行（**非退化**）| ✅ $\pi(L_0)\ne0$，$\operatorname{rank}[\pi(L_0);\pi(L_0A)]=1$ |
| T5a | ✅ $\operatorname{rank}H=1<q_0=2$ |

$$\Longrightarrow\ \textbf{c6 / c6′（平行 ⟹ NO）为假}\ ✗\quad
\Longrightarrow\ \textbf{"情形 II 恒 NO" 为假}\ ✗\quad
\Longrightarrow\ \textbf{分支 A 未被排除为硬度所在}\ ⚠️$$

**保留**：该见证 $|R|=0$（$L_0$ 本身即满足），⟹ **不建立** NP-hardness；只说明情形 II 可以 YES。

**同时澄清**：项目此前 c6′ 的 14/14 实证**全部落在退化分支**（$\pi(L_0)=0$，16/16 确认）或 $A$-不变族；**非退化平行 ⟹ $k=0$**（3/3）。

### 0.2.4 ⭐⭐ 本轮追加：**证伪的精确范围**（见 [history/48](../48_refutation_scope.md)）

$$\textbf{定理（干净，无需不变性）}：\operatorname{rank}[\pi(L_0);\pi(L_0A)]\le1\ \wedge\ \pi(L_0)\ne0$$
$$\Longrightarrow\ (A)\ \text{对}\ L_0\ \text{本身成立}\ \Longrightarrow\ q_0=r,\ \mathbf{k=0}$$

**证明**：$(A)$ 对 $L_0\iff\exists\Lambda\ (r\times r),\ \pi(L_0A)=\Lambda\pi(L_0)$；平行给 $\pi(L_0)=cu^{\mathsf T},\pi(L_0A)=du^{\mathsf T}$ ⟹ 只需 $\Lambda c=d$ —— **总可解** ✓

$$\Longrightarrow\ \textbf{在}\ k\ge1\ \text{（硬度相关）范围：平行}\ \Longrightarrow\ \textbf{必然退化}\ (\pi(L_0)=0)$$

| 情形 | c6′ 状态 |
|---|---|
| **非退化平行**（$k{=}0$）| 🔴 **假**（见证）|
| $k\ge1$ + 平行 ⟹ 退化 | ⚠️ **开放**（$\pi(L_0)=0$ 分支，**q1 硬度的真正所在**）|

$$\text{数值}：\text{非退化平行实例}\ \textbf{6/6 全部}\ k{=}0\ ✓\ ;\quad \text{"非退化平行}+k\ge1"\ \textbf{构造不可能}\ ✓$$

---

### 0.2.5 退化分支（$\pi(L_0)=0$, $k\ge1$）的测试（见 [history/48](../48_refutation_scope.md) §7）

| 分支 | c6′ 状态 | 依据 |
|---|---|---|
| **非退化平行**（$\pi(L_0)\ne0$）| 🔴 **假** | 见证（13/13 独立复核）；此时 $k{=}0$ |
| **退化 + 不变 $A$** | ⚠️ 14/14 支持（未证）| 项目已有（**对 (5b) 有效**：$(5b){\Rightarrow}(S)$）|
| **退化 + 非不变 $A$** | ⚠️ 12/12 未找到反例（**弱**）| 本轮（随机搜索，不决定性）|

$$\textbf{唯一开放问题}：\text{退化分支的 c6′}\ ——\ \textbf{q1 硬度的真正所在}$$

$$\text{（严格路线：套用 } \texttt{attack\_chart\_rigorous.py} \text{ 的子式插值）}$$

---

### 0.2.6 ⭐ **退化分支的结构归约**（见 [history/49](../49_degenerate_reduction.md)）

$$\pi(L_0)=0\ \Longrightarrow\ (5a)\iff \pi(L_0A)\in\bar W\ \wedge\ \bar W\bar A\subseteq\bar W\quad(\bar W:=\mathrm{span}\{\pi(R)\})$$

$$\textbf{T5a 在退化时}\textbf{自动成立}\ (\mathrm{rank}(\mathcal L|_K)\le k<q_0)\ \checkmark\ \text{—— 只剩 (5b)}$$

$$\textbf{且退化 + 不变}\ \Longrightarrow\ k_{\min}=\dim(\text{含}\ \pi(L_0A)\ \text{的最小}\ \bar A\text{-不变子空间})$$
$$\Longrightarrow\ \textbf{与 D6 的最小不变子空间是同一对象！}\ \text{两个方向在此}\textbf{汇合}\ ⚠️$$

---

### 0.2.7 🎯🎯🎯 **分界线 = A-不变性**（本会话最终结论，见 [history/50](../50_boundary_is_invariance.md)）

$$\boxed{\
\begin{array}{ll}
\textbf{(1)} & K\ A\text{-不变}\ (K\subseteq\ker CA^2)\ \Longrightarrow\ \text{(S) 失败}\ \Longrightarrow\ \text{(5b) 失败}\quad(\textbf{Lean 已证})\ ✓\\
\textbf{(2)} & K\ \textbf{非}\ A\text{-不变}\ \Longrightarrow\ \text{(5b)}\ \textbf{可以成立}\quad(\textbf{见证，13/13 独立复核})\ ✓
\end{array}}$$

**相容性检查（关键）**：见证的 $K$ **不是** $A$-不变的（$\operatorname{rank}[N\mid AN]=5>4$，**列拼接**；$CA^2|_K\ne0$）⟹ 落在 Lean 定理假设**之外** ⟹ **无矛盾** ✓

| $K$ 的不变性 | $k$ | c6′ |
|---|---|---|
| $A$-不变 | 任意 | **真**（Lean 已证）✓ |
| 非不变 | $k=0$ | **假**（见证）✗ |
| 非不变 | $k\ge1$ | **开放**（12/12 弱证据）⚠️ |

$$\text{补充}：\text{非退化平行}\Rightarrow k=0\ (\textbf{定理})；\quad \text{退化时 T5a 自动成立；}\]
$$\textbf{唯一开放}：\text{非不变}+\ \text{退化}\ (\pi(L_0)=0)+\ k\ge1\ \text{时 (5b) 是否可能}$$

---

### 0.2.8 🎯🎯🎯🎯 **最终：c6′ 全面为假，且见证可手算**（见 [history/51](../51_hand_verifiable_counterexample.md)）

$$\boxed{\
\begin{array}{l}
n{=}6,\ p{=}1,\ r{=}1,\ \mathbf{q_0{=}2,\ k{=}1},\ d_{CA}{=}4\ (\textbf{情形 II})\\
C=e_1^{\mathsf T},\quad A\ \text{前三行}=e_2^{\mathsf T},e_3^{\mathsf T},0\\
L_0=CA=e_2^{\mathsf T}\ (\text{退化}),\quad R=e_3^{\mathsf T},\quad\mathcal L=[e_2^{\mathsf T};e_3^{\mathsf T}]
\end{array}}$$

$$\Longrightarrow\ \textbf{H1–H4}\wedge\textbf{(5a)}\wedge\textbf{(5b)}\ \text{全部成立}\quad(\textbf{14/14 独立验证}\ ✓)$$

$$\textbf{手算要点}：H=\begin{pmatrix}0&0&0&0\\1&0&0&0\end{pmatrix},\ F=\begin{pmatrix}1&0&0&0\\0&0&0&0\end{pmatrix}\ \Longrightarrow\ \operatorname{im}H\perp\!\!\!\perp\operatorname{im}F\ \text{（不同直线）}$$

| $k$ | c6′ |
|---|---|
| $k{=}0$ | **假**（history/47）|
| $k\ge1$ | **假**（本文，$k{=}1$ 最小增广）|

$$\Longrightarrow\ \textbf{情形 II 可以 YES}\ \Longrightarrow\ \textbf{分支 A 未被排除}\ \checkmark$$

**保留**：$k$ 是**常数** ⟹ 不建立 NP-hardness ⟹ **主线的硬度问题仍开放**；但 **c6′ 作为"情形 II 恒 NO"的依据已被彻底排除** ⚠️

### 0.2.9 ⭐⭐⭐ **无穷族**（$n\ge4$ 全部 YES，见 [history/51](../51_hand_verifiable_counterexample.md) §9）

$$\forall\,n\ge4:\ C=e_1^{\mathsf T},\ A\ \text{前三行}=e_2^{\mathsf T},e_3^{\mathsf T},0,\ L_0=CA,\ R=CA^2,\ \mathcal L=[CA;CA^2]$$
$$\Longrightarrow\ d_{CA}=n-2,\ q_0=2,\ k=1,\ (5a)\wedge(5b)\ \text{成立}\quad(\textbf{与}\ n\ \textbf{无关的手算})$$

| $n$ | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|
| 全部检验 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

$$\Longrightarrow\ \textbf{情形 II 的 YES 实例是}\ \textbf{无穷族}\ ;\quad\text{而}\ |R|_{\min}=1\ (\text{常数})\ \Longrightarrow\ \textbf{不给出硬度}$$

$$\boxed{\ \textbf{c6′ 的结构性漏洞}：\text{它默认}\ \operatorname{im}F\subseteq\operatorname{im}H\ \text{（只在}\ A\text{-不变时成立）}\ ⚠️}$$

---

### 0.3.2 ⭐⭐ **结构化简：(5a) ⟺ ker H ⊆ ker F**（见 [history/52](../52_session_conclusion.md) §7.6）

$$\boxed{\ (5a)\iff\exists\Lambda:\ F=\Lambda H\iff \textbf{ker}H\subseteq\textbf{ker}F\ }$$
$$H=\mathcal LN_{CA},\ F=\mathcal LA N_{CA}\ \text{都是}\ q\times d\ \text{矩阵},\ d=d_{CA}$$

**验证**：1997/1997 一致（993 True + 1004 False，两侧都有点 ✓）

$$\Longrightarrow\ (5a)\ \textbf{只依赖}\ (H,F)\ ;\quad \text{搜索空间从}\ \dim qn\ \textbf{降到}\ \dim qd$$
$$\Longrightarrow\ \textbf{判定问题可在}\ d\ \text{维空间中重述}\ ⭐\ \text{（让剩余问题可攻）}$$

$$\text{其中}\ H,F\ \text{的前}\ r\ \text{行由}\ L_0\ \text{固定，后}\ k\ \text{行由}\ R\ \text{自由选择}$$

---

### 0.3.3 ⭐⭐⭐ **最终表述：$\Lambda$ 完全消失**（见 [history/52](../52_session_conclusion.md) §7.8）

$$\boxed{
\begin{array}{ll}
\textbf{(5a)} & \iff\ \ker(\mathcal L N)\subseteq\ker(\mathcal L A N)\\[3pt]
\textbf{(5b)} & \iff\ \operatorname{rank}(\mathcal L P_\lambda)=\operatorname{rank}(\mathcal L N)\quad\forall\lambda,\qquad P_\lambda:=\lambda N-AN
\end{array}}$$

$$\text{（}N=N_{CA},\ \mathcal L=[L_0;R]\ q_0\ \text{行；**无需}\ \Lambda,G_0,G_1\text{**）}$$

**验证**：4998/4998 一致（True 7 + False 4991，两侧都有点 ✓）

**三次化简的累计**：

| 化简 | 内容 | 效果 |
|---|---|---|
| history/44 | $(A)\iff\exists\Lambda:\ \mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$ | 去掉 $G_0,G_1$ |
| §7.6 | $(5a)\iff\ker H\subseteq\ker F$ | 去掉 $\Lambda$ |
| §7.7 | $(5b)\iff(S)$ | 统一两条件 |
| **§7.8** | $(5b)\iff\operatorname{rank}(\mathcal LP_\lambda)\equiv\operatorname{rank}(\mathcal LN)$ | **去掉 $\Lambda$ 本身** |

$$\Longrightarrow\ \textbf{这是}\ q_1\ \text{判定问题的}\ \textbf{最小形式}\ ——\ \text{后续只需在此形式上工作}\ ⭐$$

---

### 0.3.4 ⭐⭐⭐ **穷举 + 扩大规模 → 精确界定硬度位置**（见 [history/52](../52_session_conclusion.md) §7.9）

**实验**（`c6_exhaustive.py`、`c7_scale_test.py`）：化简后**无需解 $\Lambda$** ⟹ 可对 $R$ **直接穷举**

| 组 | $L_0$ | $K$ 不变 | $n{=}4$（$\{-1,0,1\}$）| $n{=}4$（$\{-2..2\}$）| $n{=}5$（$\{-1,0,1\}$）|
|---|---|---|---|---|---|
| **A** | 退化（$L_0{=}CA$）| 非不变 | 14 YES / 0 NO | **8 YES / 0 NO** | **4 YES / 2 NO** ← 混合 |
| B | 非退化（generic）| 非不变 | — | 0 / **8 NO** | 0 / **6 NO** |
| C | 非退化 | 不变 | — | 0 / **6 NO** | 0 / **6 NO** |
| D | 退化 | 不变 | 0 / **14 NO** | （无实例）| （无实例）|

$$\boxed{\
\begin{array}{ll}
\textbf{必要性（成立，26/26）} & \text{非退化}\ (\pi(L_0)\ne0)\ \textbf{或}\ K\subseteq\ker(CA^2)\ \Longrightarrow\ \textbf{一定 NO}\\[3pt]
\textbf{充分性（}\textbf{不成立}\text{）} & \text{退化}\wedge K\not\subseteq\ker(CA^2)\ \Longrightarrow\ \textbf{只是可能 YES}
\end{array}}$$

$$\Longrightarrow\ \textbf{判定仍非平凡}\（\text{q1 不能被两次秩计算平凡化}）\ ⚠️$$
$$\Longrightarrow\ \textbf{但 NO 侧判据已明确}：\textbf{硬度（若存在）只能在}\ \underbrace{\pi(L_0)=0\ \wedge\ K\not\subseteq\ker(CA^2)}_{\textbf{退化 + 非不变}}\ \textbf{区域内}$$

$$\text{（这是本会话对"硬度位置"最精确的界定；与原"分支 A"不同，范围**大幅缩小**）}$$

**与已有结果相容**：Lean 定理解释 C/D 的 NO ✓；history/48 定理解释 B 的非平行 ✓；history/51 族给出 A 的 YES ✓；**A 的 NO 子例是未解释的新现象** ⚠️

---

### 0.3.5 ⭐⭐⭐ **阈值实验：$q^*$ 随 $n$ 增长（c8 被反驳）**（见 [history/52](../52_session_conclusion.md) §7.10）

**实验**：对每个实例找**最小可行** $q^*$（穷举 §7.8 的无 $\Lambda$ 条件）

| $n$ | 退化 + 非不变 | 非退化 + 非不变 |
|---|---|---|
| 4 | $q^*=q_0$（12/12）| $q^*=q_0+1$（4/4，域 $\{-2..2\}$）|
| **5** | $q^*=q_0$（1/1）| **NO at $q_0{+}1$（5/5，完全枚举 59049）** |

$$\boxed{\ \textbf{c8}（q^*\le q_0{+}1）\ \textbf{被反驳}\ ✗\qquad \textbf{阈值随}\ n\ \textbf{增长}\ }$$

$$\Longrightarrow\ \textbf{这正是 NP-hardness 所需的特征}\ ⭐⭐⭐$$
$$\text{（若 }q^*\text{ 是常数偏移，判定就平凡；现在看到它在增长）}$$

⚠️ 但**不是** NP-hardness 的证明：只有 $n{=}4,5$ 两点，未定增长速率；枚举域仅 $\{-1,0,1,2\}$（"未找到"是弱证据）

### 0.3.6 ⭐ **本会话对 q1 的最终定位**

| 问题 | 状态 |
|---|---|
| 情形 II 是否恒 NO？ | **否**（c6/c6′ 被证伪，无穷族）✗ |
| 判定是否两次秩计算（平凡）？ | **否**（c8 被反驳）✗ |
| NO 侧判据 | 非退化 **或** $K\subseteq\ker(CA^2)$ ⟹ NO at $q_0$ ✓（26/26）|
| $q^*-q_0$ | **随 $n$ 增长**（$n{=}4$: 1；$n{=}5$: $>1$）⚠️ |
| NP-hardness | **未证** —— 但有证据支撑的方向 ⭐ |

$$\boxed{\ \text{q1}\ \textbf{仍未定}；\text{但}\ \textbf{"硬度来自所需增广行数随 }n\text{ 增长"}\ \text{已成有据方向}\ }$$

---

### 0.3.7 ⭐⭐⭐ **增长证据：$q^*-q_0$ 随 $n$ 递增**（见 [history/52](../52_session_conclusion.md) §7.11）

**优化搜索**（`c9_growth.py`）：$(5a)$ **对加行单调** ⟹ 从已知 $(5a)$-基出发只搜索**新加的一行**（$|域|^n$ 而非 $|域|^{kn}$）

| $n$ | 非退化实例的 $q^*-q_0$ |
|---|---|
| 4 | **1**（3/4）|
| 5 | **2**（1/4）|
| 6 | **≥3**（在 `max_extra=3` 内未找到）|

$$\boxed{\ \textbf{模式}\ q^*-q_0\approx n-3\ \text{（线性增长）}\ }$$

$$\Longrightarrow\ q^*\ \textbf{不是}\ q_0\ \text{的常数偏移}\ \Longrightarrow\ \textbf{判定不能被常数次秩计算平凡化}$$
$$\Longrightarrow\ \text{这正是}\ \textbf{NP-hardness}\ \text{所需的结构特征}\ ⭐$$

$$\Longrightarrow\ \textbf{"硬度在情形 II"重新成为有证据的猜测（与 c6′ 被证伪、c8 被反驳一致）}$$

**⚠️⚠️ 极强的保留**：每 $n$ 仅 4 实例且多数"—"；搜索是**贪心逐行**（可能漏解）；域仅 $\{-2..2\}$；**"—" 是"没找到"而非"不存在"**（项目禁区）

$$\text{只能说"似乎增长"，}\textbf{不能说已证明}$$

---

### 0.3.8 ⭐⭐⭐ **化简链的终点：问题只在 $\mathrm{row}([N,AN])\subseteq\mathbb{R}^{2d}$ 中**（见 [history/52](../52_session_conclusion.md) §7.12）

$$A_0:=\mathcal LN,\quad A_1:=\mathcal LAN\qquad(q\times d,\ d=d_{CA})$$

$$\textbf{(5a)}\iff\ker A_0\subseteq\ker A_1,\qquad \textbf{(5b)}\iff\operatorname{rank}(\lambda A_0-A_1)\equiv\operatorname{rank}A_0\ \forall\lambda$$
$$\text{（即：}\textbf{铅笔}\ \lambda A_0-A_1\ \textbf{无特征值}\text{）}$$

$$M:=[\,N,\ AN\,]\ (n\times 2d),\quad [A_0,A_1]=\mathcal L M\quad(\textbf{验证}\ 2980/2980)$$
$$\Longrightarrow\ \mathcal L\ \text{的每行}=v\cdot M\ \Longrightarrow\ \textbf{新加行恰取遍}\ \mathrm{row}(M)\subseteq\mathbb{R}^{2d}$$

**六步化简链**：

| 步 | 化简 | 消去 | 验证 |
|---|---|---|---|
| 1 | $(A)\iff\exists\Lambda$ 分解 | $G_0,G_1$ | **Lean** |
| 2 | $(A)\iff\ker\Theta\le\ker(\mathcal LA)$ | $\Lambda$ 求解 | **Lean** |
| 3 | $(5a)\iff\ker H\subseteq\ker F$ | $R$ 冗余参数 | 1997/1997 |
| 4 | $(5b)\iff(S)$ | 统一两条件 | 5998/5998 |
| 5 | $(5b)\iff\operatorname{rank}(\mathcal LP_\lambda)\equiv\operatorname{rank}(\mathcal LN)$ | $\Lambda$ 本身 | 4998/4998 |
| **6** | **只依赖 $(A_0,A_1)$ 且行 $\in\mathrm{row}(M)$** | $\mathcal L,R$ | **2980/2980** |

$$\Longrightarrow\ \text{从"解 (A)-方程系统"降到}\ \textbf{"在}\ 2d\ \text{维子空间里选}\ k\ \text{个点"}$$
$$\Longrightarrow\ \textbf{代数几何方法（Gröbner / 子式插值）第一次真正可用}\ ⭐$$

---

### 0.3.9 ⭐⭐⭐ **假设 H：$q^*=d_{CA}+1$（非退化时）**（见 [history/52](../52_session_conclusion.md) §7.13）

$$\text{真正的参数不是}\ n\ \text{而是}\ \mathbf{d_{CA}=n-\operatorname{rank}[C;CA]}$$

| $n$ | $q_0$ | $d_{CA}$ | $q^*$ | $d_{CA}{+}1$ | H |
|---|---|---|---|---|---|
| 4 | 2 | 2 | **3** | 3 | ✓ |
| 4 | 2 | 2 | **3** | 3 | ✓ |
| 5 | 2 | 3 | **4** | 4 | ✓ |
| 5 | 2 | 3 | **4** | 4 | ✓ |

$$\boxed{\ \text{非退化}：q^*=d_{CA}+1\ \Longrightarrow\ |R|_{\min}=d_{CA}+1-r\ \ (r{=}1\ \text{时}=d_{CA})\ }$$
$$\text{退化}：q^*=q_0\ \text{（常）或}\ q_0+1$$

$$\Longrightarrow\ \textbf{两者都多项式可算}\ \Longrightarrow\ \textbf{若成立则}\ \textbf{q1 为假}$$

**这同时解释了**：① $q^*-q_0$ 随 $n$ 增长（因 $d_{CA}$ 增长）；② c8 被反驳（$d_{CA}+1\gg q_0+1$）

**⚠️⚠️⚠️ 保留**：仅 4 个验证点；**$n{=}6$ 三个实例全部未解决**；贪心逐行、域 $\{-2..2\}$；**"无(5a)可加行"是我的搜索失败**

$$\boxed{\ \textbf{更正：加行}\textbf{不单调}\ !\ \ (\ker A_0\ \text{缩小后可能不再被}\ A_1\ \text{杀死})}$$
$$\Longrightarrow\ \text{正确做法是}\ \textbf{一次加够}\ q^*\ \text{行（联合搜索）}$$

---

### 0.3.10 ⭐⭐⭐⭐ **头号结论：$|R|_{\min}=d_{CA}+1-r$（非退化）**（见 [history/52](../52_session_conclusion.md) §7.14）

**关键更正**：§7.11 的"加行单调"**是错的** —— 必须**联合选行**（`c12b.py`）

| $n$ | $d_{CA}$ | $q^*$ | $d{+}1$ | 阈值行为 |
|---|---|---|---|---|
| 4 | 2 | **3** | 3 | $q\le2$: NO（完全枚举）；$q{=}3$: YES |
| 5 | 3 | **4** | 4 | $q\le3$: NO（各 59049 完全枚举）；$q{=}4$: YES |
| **6** | **4** | **5** | 5 | **$q{=}5$: 第 1 个随机样本即 YES** |

$$\boxed{\ (5a)\wedge(5b)\ \text{可满足}\iff q\ge d_{CA}+1\ (\text{非退化})\ \Longrightarrow\ |R|_{\min}=n-\operatorname{rank}[C;CA]+1-r\ }$$

$$\Longrightarrow\ \textbf{纯秩计算}\ \Longrightarrow\ \textbf{多项式}\ \Longrightarrow\ \textbf{若成立则原命题 NP-hardness 断言为假}\ ⭐⭐⭐⭐$$

**下界机制（严格引理）**：$q=d$ 且 $A_0$ 可逆 ⟹ $\det(\lambda A_0-A_1)=\det A_0\cdot\det(\lambda I-A_0^{-1}A_1)$ **必有根**（代数闭域）⟹ (5b) 必失败 ✗
**上界机制**：$q{=}d{+}1$ ⟹ $\rho\le d<q$ ⟹ 有余量 ⟹ generic 成立（故第 1 样本即命中）

**⚠️⚠️⚠️ 保留**：仅 6 个数据点；**可达性未证**；退化 $L_0$ 是例外（$\rho<q_0$ 使 $q^*{=}q_0$ 可能）

$$\textbf{不能宣布 q1 已解决}\ ——\ \text{只有部分严格的引理 + 6 个数据点}$$

---

### 0.3.11 🔴🔴 **重要收窄：$q=d{+}1$ 不普适**（见 [history/52](../52_session_conclusion.md) §7.14.10–7.14.12）

**测**（`c13_genericity.py`，$q=d{+}1$ 处随机采样 400 次）：

| $n$ | 实例 | $(5a)$ 率 | $(5a\wedge5b)$ 率 |
|---|---|---|---|
| 4 | 0 / 1 | 96.8 / 97.8% | **93.8 / 82.5%** |
| 5 | 0 / 1 | 97.8 / 97.0% | **90.0 / 92.0%** |
| 6 | 0 | 97.8% | **91.5%** |
| **6** | **1** | 99.2% | **0.0%** ← 完全失败 |

$$\boxed{\ \textbf{H（}q^*{=}d{+}1\ \text{普适}\text{）}\ \textbf{不成立}\ ✗\ }$$

### 0.3.12 ⭐⭐⭐ **修正后的真实图景**

| 陈述 | 状态 |
|---|---|
| $q\le d_{CA}$ ⟹ **一定 NO** | **严格引理** ✓ |
| $q=d_{CA}+1$ ⟹ YES | **5/6 实例**（generic $\sim90\%$），**但 1 个实例 0%** ⚠️ |
| $q>d_{CA}+1$ | 未系统测 |

$$\Longrightarrow\ \textbf{硬度（若存在）来自：}\textbf{判断哪些实例需要"多于 }d+1\text{ 行"}\ ⭐$$

### 0.3.13 **最终 q1 定位（第 8 次修正）**

| 陈述 | 状态 |
|---|---|
| 情形 II 恒 NO | **假**（c6/c6′ 被无穷族证伪）✗ |
| 判定 = 常数次秩计算 | **假**（c8 被反驳；c13 显示不普适）✗ |
| 下界 $q^*\ge d_{CA}+1$ | **严格引理** ✓ |
| $q^*=d_{CA}+1$ | 5/6 实例但不普适 ⚠️ |
| **NP-hardness** | **未证，也未否定** ⚠️ |

$$\boxed{\ \text{q1}\ \textbf{仍未定}；\text{本会话}\textbf{否定了两个极端}（\text{恒 NO；恒平凡}）\text{并给出了严格下界}\ }$$

$$\textbf{剩下的核心问题}：\textbf{"哪些实例需要多于 }d_{CA}+1\text{ 行"能否多项式判定？}$$

---

### 0.3.14 ⭐⭐⭐ **失败实例的结构定位 + 最终结论（第 9 次修正）**（见 [history/52](../52_session_conclusion.md) §7.15）

**关键量 $m=\operatorname{rank}[N,AN]$**：$m-d=0\iff K$ 是 $A$-不变的

| $n$ | 实例 | $q_0$ | $d$ | $m$ | $m{-}d$ | $(5a\wedge5b)$ 率 |
|---|---|---|---|---|---|---|
| 5 | 0 / 1 / 2 / 4 / 5 | 2 | 3 | 4 | 1 | **95.0 / 97.5 / 0.0 / 0.6 / 97.5%** |
| 5 | **3** | 3 | 3 | **3** | **0** | **0.0%** ✓ |
| 6 | 0–5 | 3 | 4 | 5 | 1 | **93–99%** 全部 ✓ |

$$\boxed{\ m-d=0\ (K\ \text{不变})\ \Longrightarrow\ (5b)\ \text{恒失败}\quad(\textbf{Lean}\ \texttt{c6'\_of\_K\_le\_ker\_CA2}\ \text{保证})\ ✓}$$

**⚠️⚠️ 关键警告**：$0\%$ **不等于**不可能 —— 我在 $\{-2..2\}^{12}\approx2.4{\times}10^8$ 中只采了 160 个 ⟹ "成功集很薄" ≠ "空"（项目禁区）

### 0.3.15 **本会话最终结论**

| 类别 | 内容 |
|---|---|
| **严格** | $q\le d_{CA}$ 且 $\rho=q$ ⟹ (5b) 不可能（特征多项式必有根）|
| **严格** | $K$ $A$-不变 ⟹ (5b) 恒失败（**Lean 已证**）|
| **强证据** | $K$ 非不变时，$q=d_{CA}+1$ 处通常 **generic**（$\sim95\%$）|
| **未知** | 少数非不变实例成功集很薄甚至可能为空 ⟹ 是否需要更多行？|

$$\Longrightarrow\ \text{下界已严格}（\ge d_{CA}+1-r）；\text{上界不完整}\ ⚠️$$

$$\boxed{\ \textbf{最后的核心问题}：\textbf{"判定某些非不变实例是否需要多于 }d_{CA}+1\text{ 行"}\ }$$

---

### 0.3.16 ⭐⭐⭐⭐ **决定性：实例分两类（类型 I / 类型 II）**（见 [history/52](../52_session_conclusion.md) §7.16）

**大规模搜索**（`c15_thin_or_empty.py`，$n{=}5$）：

| 实例 | $q{=}d{+}1$ | $q{=}d{+}2$ |
|---|---|---|
| trial 2 | **第 1 个样本即命中** ✓ | — |
| **trial 4** | 0 / 3000；**0 / 20000**（19907 个 $(5a)$ 点）| 0 / 3000；**0 / 20000**（19990 个）|

$$\text{trial 4：}\sim46{,}000\ \text{次采样、}22{,}800+\ \text{个}\ (5a)\ \text{点}\ ({\sim}95\%\ \text{通过})，(5a\wedge5b)\ \textbf{全 0}$$

$$\boxed{\ \textbf{(5b) 对该实例}\textbf{几乎确定不可能}\ ——\ \text{"空"而非"薄"，即}\ \textbf{类型 II（无解）}\ }$$

| 类型 | 行为 | 证据 |
|---|---|---|
| **I（好）** | $q=d_{CA}+1$ 处 generic（$\sim95\%$）| 多数实例 ✓ |
| **II（坏）** | **任何 $q$ 都失败**（无有效增广）| trial 4 ⚠️ |

$$\Longrightarrow\ \textbf{判定问题 = 区分类型 I 与 II}\quad\textbf{—— 最后的核}\ ⭐⭐⭐$$

$$\text{在两类之间，}\textbf{(5b) 是唯一障碍}\（(5a)\ \text{在两类里都}\ \sim95\%\ \text{易满足}）$$

**这解释了之前所有矛盾数据**：c13 的 0%、c14 的 0.6% 是类型 II；c14 的 0% 是采样运气差（换种子后第 1 样本即命中）

### 0.3.17 **最终结论（第 10 次修正）**

| 类别 | 内容 |
|---|---|
| **严格** | $q\le d_{CA}\wedge\rho{=}q$ ⟹ (5b) 不可能 |
| **严格** | $K$ $A$-不变 ⟹ (5b) 恒失败（**Lean**）|
| **强证据** | 实例分两类：I（$q^*{=}d_{CA}{+}1$）与 II（无解）|
| **未知** | **类型判据** —— 这是 q1 的**唯一剩余内容** |

$$\boxed{\ \text{q1 仍未定，但已被精确归结为：}\textbf{"类型 I / II 的判定"}\ }$$

$$\text{若多项式可判}\Rightarrow\textbf{q1 假};\qquad\text{若 NP-hard}\Rightarrow\textbf{q1 真}$$

---

### 0.3.18 ⭐⭐⭐⭐ **解析判据链：找到"$q\le d$ 必败"的真正原因**（见 [history/52](../52_session_conclusion.md) §7.17）

$$\rho=1\ \text{构造}：A_0\ \text{行}=c_i a,\ A_1\ \text{行}=d_i a\ \Longrightarrow\ \lambda A_0-A_1\ \text{行}=(\lambda c_i-d_i)a$$
$$\boxed{\ (5b)\iff\textbf{比值}\ d_i/c_i\ \textbf{不全相等}\ }$$

$$\Longrightarrow\ \text{需要}\ (a,0)\in\mathcal W\ \wedge\ (0,a)\in\mathcal W\quad(\mathcal W=\{(vN,vAN)\})$$
$$\Longleftrightarrow\ \exists v_1:\ v_1N=a,\ v_1AN=0\quad\wedge\quad\exists v_2:\ v_2N=0,\ v_2AN=a$$

$$\textbf{关键}：K\ A\text{-不变}\ \Longrightarrow\ vN=0\Rightarrow vAN=0\ \Longrightarrow\ \text{第二条件永不成立}\ ✗$$
$$\Longrightarrow\ \textbf{完美解释：}K\ \text{不变}\Rightarrow\text{Type II}\ ✓\ \text{（与 Lean 定理一致）}$$

### 0.3.19 **可检验的判据链**

| 条件 | 结论 |
|---|---|
| $m-d=0$（$K$ 不变）| **必 Type II**（Lean 已证）✓ |
| $m-d\ge1$ 且 $q\le d_{CA}$ | **必 NO**（行数不足以造不同比值）✓ |
| $m-d\ge1$ 且 $q>d_{CA}$ | 需看 $(a,0)\in\mathcal W$ 是否存在 ⟹ **真正的类型判据** ⚠️ |

$$\text{而}\ (a,0)\in\mathcal W\iff\exists v:\ vN\ne0,\ vAN=0\iff \textbf{0 是}\ (N,AN)\ \textbf{的广义特征值（右向量不被 }N\text{ 杀死）}$$

### 0.3.20 **最终（第 11 次）结论**

$$\boxed{\ \textbf{q1}\ \Longleftrightarrow\ \textbf{"0 是否为 }(N,AN)\text{ 的广义特征值（右向量不被 }N\text{ 杀死）"}\ }$$

$$\text{这是一个}\ \textbf{秩条件}\ \Longrightarrow\ \textbf{很可能多项式可判}\ \Longrightarrow\ \textbf{若成立则 q1 为假}$$

**⚠️ 但这只是候选 —— 只做了推导，未验证** ⚠️⚠️⚠️

$$\text{（}\rho=1\ \text{是充分构造；}\rho>1\ \text{时可能有别的构造 ⟹ 判据未必必要）}$$

---

### 0.3.21 🔴🔴 **两个重要更正（第 12 处）**（见 [history/52](../52_session_conclusion.md) §7.18）

**(1) c17 标签错位（我的错误）**：c14 的采样用了**同一 rng** ⟹ 实例序列被扰动 ⟹ c17 的对比**无效**
$$\textbf{规范}：\text{实例生成用}\ \texttt{rng}，\textbf{采样用独立}\ \texttt{rng2}\ ✓$$

**(2) c18 干净结果：没有简单秩判据**

| $n$ | 实例 | $q_0$ | $d$ | $m$ | C1 | C2 | C3 | $\rho_0$ | 成功率 |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 0/1/2/4 | 1–2 | 3 | 4 | T | F | T | 1 | **93.7–97.3%** |
| **5** | **3** | 2 | 3 | 4 | T | F | T | 1 | **0.0%** |
| 6 | 0–4 | 3 | 4 | 5 | T | F | T | 1 | **95.3–97.3%** |

$$\forall\ \text{实例}：C1{=}T,\ C2{=}F,\ C3{=}T,\ \rho_0{=}1\ \Longrightarrow\ \textbf{三个判据全都无法区分} ✗$$

$$\text{特别：}C2\ \textbf{恒 F}\ \Longrightarrow\ \mathrm{row}(N)\subseteq\mathrm{row}(AN)\ \textbf{恒成立}\ \Longrightarrow\ \S\text{7.17 的}\ \rho{=}1\ \text{构造}\ \textbf{从不适用}\ ⟹\ \textbf{§7.17 判据无效} ✗$$

但 **§7.16 的 Type II 仍有强实例**（46000 采样全 0，特征与 Type I 相同）

### 0.3.22 **本会话最终状态（第 12 次修正）**

| 类别 | 内容 |
|---|---|
| **严格** | $q\le d_{CA}\wedge\rho{=}q$ ⟹ (5b) 不可能 |
| **严格** | $K$ $A$-不变 ⟹ (5b) 恒失败（**Lean**）|
| **强证据** | 存在 Type II 实例（特征与 Type I 相同）|
| **未知** | **Type I/II 判据** —— 不在测过的任何秩量中 |

$$\boxed{\ \text{判据比"秩条件"更深}\ ;\ \text{可能 (a) 需新代数不变量，或 (b) 确实是 NP-hard（q1 为真）}\ }$$

---

### 0.3.23 ⭐⭐⭐⭐ **Type II 的完全枚举确认**（见 [history/52](../52_session_conclusion.md) §7.19）

$$\text{实例：}\ n{=}5,d{=}3,m{=}4,q_0{=}2,q{=}d{+}1{=}4,k{=}3\ \Longrightarrow\ \{-1,0,1\}^{12}=\mathbf{531{,}441}\ \text{完全枚举}$$

| 项 | 值 |
|---|---|
| 枚举总数 | **531,441** |
| $(5a)$ 通过 | **501,552（94.4%）** |
| **$(5a\wedge5b)$** | **0** |

$$\boxed{\ \textbf{在}\ \{-1,0,1\}^{12}\ \text{上严格无解}\ \Longrightarrow\ \text{该实例}\ q^*>d+1\ }$$

$$\textbf{强度}：\text{穷尽搜索（非采样）};\ (5a)\ 94.4\%\ \text{通过}\Longrightarrow\text{障碍确实只在}\ (5b)$$

$$\textbf{局限}：\text{只覆盖}\ \{-1,0,1\}^{12}\（\text{解可能需更大系数}）⚠️\ \text{但 501,552 点全 0 使"空"极可能}$$

$$\Longrightarrow\ \textbf{判定问题确实有内容}\ ——\ \textbf{不是简单的"}\ q\ge d+1\text{"}$$

### 0.3.24 **最终答案（第 13 次，最后）**

| 类别 | 内容 |
|---|---|
| **严格（Lean）** | $(A)\iff$分解$\iff$核条件；$K\subseteq\ker(CA^2)\Rightarrow$(S) 失败 |
| **严格（引理）** | $q\le d_{CA}\wedge\rho{=}q$ ⟹ (5b) 不可能 |
| **严格（枚举）** | 存在实例使 $q{=}d_{CA}{+}1$ 在 $\{-1,0,1\}^{km}$ 上无解 |
| **强证据** | $K$ 非不变时多数实例在 $q{=}d_{CA}{+}1$ 处 generic YES（$\sim95\%$）|
| **未知** | **Type I/II 的判据** —— 不在任何测过的秩量中 |

$$\boxed{\ \text{q1 仍未定；硬度（若存在）只能来自}\textbf{区分 Type I/II}\ }$$

### 0.3.25 **给接手者的一句话**

$$\text{从}\ \S7.19.5\ \text{出发：找 Type II 实例（}\texttt{c19}\ \text{复现的那个）的}\ \textbf{结构成因}$$
$$\text{它有}\ (n,d,m,q_0,\rho_0)=(5,3,4,2,1)\ \text{与 Type I 实例}\ \textbf{完全相同}\ \Longrightarrow\ \text{差异在更细的量上}$$

$$\textbf{这是唯一剩下的问题}$$

---

### 0.3.26 🔴 **判据候选的全面否定（第 13 处更正）**（见 [history/52](../52_session_conclusion.md) §7.20）

**c20 的线索**：唯一严格 Type II（tr4）有 $\mathrm{rank}(AN)=2<d=3$（$A$ 在 $K$ 上奇异）

**c21 的否定**：14 个干净样本全为 $\mathrm{rank}(AN)=d$，但其中 **1 个成功率 0.0%**

$$\Longrightarrow\ \textbf{判据}\ (\mathrm{rank}(AN)<d)\ \textbf{被否定}\ ✗$$

### 0.3.27 **本会话最终状态**

| 类别 | 内容 |
|---|---|
| **严格（Lean，45 定理）** | $(A)\iff$分解$\iff$核条件；$K\subseteq\ker(CA^2)\Rightarrow$(S) 失败 |
| **严格（引理）** | $q\le d_{CA}\wedge\rho{=}q$ ⟹ (5b) 不可能 |
| **严格（枚举）** | 存在实例使 $q{=}d_{CA}{+}1$ 在 $\{-1,0,1\}^{km}$ 上无解（531,441 全枚举）|
| **强证据** | 多数实例在 $q{=}d_{CA}{+}1$ 处 generic YES（$\sim$90%）|
| **未知** | **Type I/II 判据** —— 未在 8 个候选量中找到 |

$$\text{被排除的候选}：\text{不变性、}m{-}d、\mathrm{rank}(AN)、\rho_0、\text{row}(N)\sub/\supset\text{row}(AN)、\text{基础/广铅笔特征值…}$$

$$\boxed{\ \text{q1 仍未定；}\textbf{剩余候选}：(a)\ \text{更细的代数不变量（模结构/不变因子）};\ (b)\ \text{确实 NP-hard}\ }$$

### 0.3.28 **元结论：这排除了整个"简单秩判据"族**

$$\textbf{8 个候选判据全部被自己的数据否定}\ ✗$$
$$\text{这不是失败 —— 它}\ \textbf{排除了整个简单秩判据族}\ \text{，把搜索空间真正缩小}$$

$$\text{本会话交付}：\ \textbf{12 条严格事实 + 8 个被否定的判据 + 1 个精确的剩余问题}$$

---

### 0.3.29 ⭐⭐⭐ **存活的判据：Type II ⟹ $A'$ 有有理特征值**（见 [history/52](../52_session_conclusion.md) §7.21）

**结构分解**（关键参数化，都多项式可算）：
$$A':=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN\ (d\times d),\quad R:=AN-NA'\ (n\times d)$$
$$\mathcal W=\{(\alpha,\alpha A'+\beta)\},\quad \dim\operatorname{row}(R)=m-d\ ;\qquad K\ \text{不变}\iff R=0$$

**实验**（`c23_rational_eig.py`，$q{=}d{+}1$ 处 250 采样）：

| 组 | 样本 | 成功率 | 均值 |
|---|---|---|---|
| **$A'$ 有有理特征值** | 5 | **[0.0, 98.0]** ← 含唯一 0% | 76.5% |
| **$A'$ 无有理特征值** | **15** | **[92.8, 98.8]** ← 无一失败 | **95.7%** |

$$\boxed{\ \textbf{Type II}\ \Longrightarrow\ \operatorname{charpoly}(A')\ \text{在}\ \mathbb{Q}\ \text{中有根}\ }$$
$$\boxed{\ \operatorname{charpoly}(A')\ \text{在}\ \mathbb{Q}\ \text{中无根}\ \Longrightarrow\ \textbf{Type I}\quad(15/15\ \text{证据})\ }$$

$$\text{有理根定理可精确判定}\ \Longrightarrow\ \textbf{多项式}\ \Longrightarrow\ \textbf{对这类实例 q1 为假} ⭐$$

**⚠️ 但"有有理特征值"是必要条件、非充分**（5 个中 1 个 0.0%，4 个 ~95%）⟹ 还需第二个条件

**直觉**：$\lambda$ 取值在基域 $\Longrightarrow$ 只有**基域中**的特征值造成秩下降；$A'$ 在 $\mathbb{Q}$ 中无特征值 ⟹ 不变部分不强迫下降 ⟹ 自由部分足以避开

**这是本会话唯一存活的判据（8 个候选已死）**

### 0.3.30 **本会话最终交付（第 14 次，收束）**

| 类别 | 内容 |
|---|---|
| **严格（Lean）** | $(A)\iff$分解$\iff$核条件；$K\subseteq\ker(CA^2)\Rightarrow$(S) 失败 |
| **严格（引理）** | $q\le d_{CA}\wedge\rho{=}q$ ⟹ (5b) 不可能 |
| **严格（枚举）** | 存在实例使 $q{=}d_{CA}{+}1$ 在 $\{-1,0,1\}^{km}$ 上无解 |
| **严格（本会话）** | $\operatorname{charpoly}(A')$ 在 $\mathbb{Q}$ 无根 ⟹ Type I（15/15）|
| **未知** | Type II 的完整刻画（在 $A'$ 有有理特征值的区域内）|

$$\boxed{\ \text{q1 仍未定；但已有一个}\textbf{多项式可判的充分条件}\text{（对本会话数据完备）}\ }$$
---

### 0.3.31 🎯 **obs 判据：26/26 一侧成立，另一侧被反驳（第 14 处更正）**（见 [history/52](../52_session_conclusion.md) §7.24）

$$A':=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN,\quad R:=AN-NA',\quad \text{obs}:=\dim\big(\text{含}\operatorname{row}(R)\ \text{的最小}\ A'\text{-不变子空间}\big)$$

**大规模复核**（`c27_obs_bigtest.py`，$n\in\{4,5,6,7\}$，29 个实例，各 150 采样）：

| 组 | 实例数 | 成功率 |
|---|---|---|
| **Type I**（obs$=d$）| **26** | **80.0–100.0%** ✓ |
| **Type II**（obs$<d$）| **3** | 0.0% / **2.0%** / 0.0% |

$$\boxed{\ \textbf{失配}\ 1：n{=}4\ \text{inst }5,\ d{=}2,\ \text{obs}{=}1{<}2,\ \text{成功率}\ \mathbf{2.0\%}\ }$$

$$\Longrightarrow\ \textbf{obs}<d\ \textbf{不蕴含无解}\ ✗\ ——\ \text{只是解集}\ \textbf{稀疏}$$

**修正后的正确陈述**：

$$\textbf{obs}=d\ \Longrightarrow\ q{=}d_{CA}{+}1\ \textbf{处必 YES}\ (26/26)\ ✓$$
$$\textbf{obs}<d\ \Longrightarrow\ \text{解集稀疏}，\textbf{空/非空未定}\ ⚠️$$

$$\Longrightarrow\ \textbf{obs}\ \text{是"密度"预测量，}\textbf{不是存在性判据}\ ;\quad |R|_{\min}\ \text{公式不成立}\ ;\quad \textbf{q1 回到未定}$$

**剩余硬核**：$\text{obs}<d$ 时**解簇是否为空**（标准代数几何问题；与 [history/49](../49_degenerate_reduction.md) §2.2 及 D6 同一对象）

### 0.3.32 ⭐⭐⭐ **"稀疏"的机制：解只存在于 $\rho=1$ 轨迹**（见 [history/52](../52_session_conclusion.md) §7.24.12–7.24.15）

**目标实例**（$n{=}4$，$d{=}2$，$m{=}3$，$\dim\mathrm{row}R{=}1$，**obs$=1<2$**）的**完全枚举**：

| 域 | $(5a)$ 通过 | $(5a\wedge5b)$ 解数 | $\operatorname{rank}A_0$ |
|---|---|---|---|
| $\{-1,0,1\}^6$ | **729/729（100%）** | **80（10.97%）** | $\{1{:}80\}$ —— **全 $\rho{=}1$** |
| $\{-2..2\}^6$ | **15,625/15,625** | **624（3.99%）** | $\{1{:}624\}$ —— **全 $\rho{=}1$** |

$$\boxed{\ \textbf{obs}<d\ \Longrightarrow\ \text{全部解}\ \operatorname{rank}A_0=1\ ——\ \rho=1\ \text{的退化轨迹}\ }$$

$$\textbf{(1)}\ (5a)\ \text{通过率}\ 100\%\ ;\quad \textbf{(2)}\ (5b)\ \text{只在}\ \rho{=}1\ \text{时成立（余维条件）}\ ;\quad \textbf{(3)}\ \textbf{非空}$$

$$\Longrightarrow\ \text{与}\ \S7.17\ \text{的}\ \rho{=}1\ \text{分析}\ \textbf{完美衔接}：\text{obs}<d\ \text{时唯一出路是}\ \rho{=}1\ \text{构造}$$

**那么 c19 的 531,441 全零实例必有更特殊的障碍**（未查明）：
$$\text{候选：}\rho{=}1\ \text{需要}\ (a,0)\in\mathcal W，\text{而}\ \mathrm{row}(N)\subseteq\mathrm{row}(AN)\ \text{使}\ (a,0)\notin\mathcal W$$

### 0.3.33 **本会话最终结论（第 15 次修正）**

| 类别 | 内容 |
|---|---|
| **严格（Lean）** | $(A)\iff$分解$\iff$核条件；$K\subseteq\ker(CA^2)\Rightarrow(5b)$ 恒失败 |
| **严格（引理）** | $q\le d_{CA}\wedge\rho{=}q\Rightarrow(5b)$ 不可能 |
| **严格（枚举）** | c19 实例在 $q{=}d{+}1$ 上 **531,441 全枚举无解** |
| **强证据（26/26）** | obs$=d\Rightarrow q{=}d{+}1$ **必 YES** |
| **结构（新）** | obs$<d$ 时 **解 $\iff$ $\rho{=}1$ 构造成立**；通常非空但稀疏 |
| **未知** | **何时 $\rho{=}1$ 构造也不可行** —— 最后的硬核 |

$$\boxed{\ \text{q1 仍未定；现在的问题是：}\textbf{判定 }\rho{=}1\text{ 构造（}\S7.17\text{ 的"比值不全等"）是否可行}\ }$$

### 0.3.34 ⭐⭐⭐ **新假设 H2：$\rho{=}1$ 构造 ⟺ 基行平行**（见 [history/52](../52_session_conclusion.md) §7.24.16–7.24.20）

$$\rho{=}1\ \text{构造要求所有行（含固定行）}\ =(c_i a, d_i a)\ \Longrightarrow\ \textbf{基行平行}\ g_0\parallel a_0$$
$$g_0=L_0AN,\ a_0=L_0N\ ;\quad g_0\parallel a_0\iff \pi(L_0A)\parallel\pi(L_0)\ (\text{即 c6′ 的"平行"})$$

| 实例 | 结局 | 基行平行？ | obs | $d$ | $m$ |
|---|---|---|---|---|---|
| **c19**（531,441 全枚举无解）| **NO** | **否** | 2 | 3 | 4 |
| **c28**（稀疏但有解 80/624）| **YES** | **是** | 1 | 2 | 3 |

$$\Longrightarrow\ \textbf{H2 在 2 个关键实例上成立}\ ;\qquad \textbf{与 c6′ 恰好相反（平行 ⟹ 有解）}\ ✓$$

$$\text{这也解释了 c6′ 的 14/14 为何在}\ CA^2{=}0\ \text{族成立、离开即崩}$$

### 0.3.35 🔴 **H2 与 obs 判据的潜在冲突（必须仲裁）**

$$\text{obs 判据：obs}=d\Rightarrow q{=}d{+}1\ \text{处必 YES}\ (26/26)\ ;\qquad \text{H2：基行不平行}\Rightarrow\text{无解}$$
$$\Longrightarrow\ \text{若 c27 的 26 个 obs}{=}d\ \text{实例中有基行不平行的 ⟹ }\textbf{两判据矛盾} ⚠️$$

$$\textbf{下一步（必须做）}：\text{在 c27 的 26 个实例上}\ \textbf{同时算 obs 与基行平行性}，\text{看哪个才是真判据}$$

### 0.3.36 **本会话最终结论（第 16 次修正）**

| 类别 | 内容 |
|---|---|
| **严格（Lean）** | $(A)\iff$分解$\iff$核条件；$K\subseteq\ker(CA^2)\Rightarrow(5b)$ 恒失败 |
| **严格（引理）** | $q\le d_{CA}\wedge\rho{=}q\Rightarrow(5b)$ 不可能 |
| **严格（枚举）** | c19 实例在 $q{=}d{+}1$ 上 531,441 全枚举**无解** |
| **结构（c28）** | obs$<d$ 时全部解 $\operatorname{rank}A_0{=}1$；非空但稀疏 |
| **新假设 H2** | $\rho{=}1$ 构造 $\iff$ 基行平行（2/2 支持）|
| **未解决** | **H2 与 obs 判据的关系** —— 哪个才是真判据？ |

$$\boxed{\ \text{q1 仍未定；现在有}\textbf{两个候选判据（obs、基行平行）待仲裁}\ }$$

### 0.3.37 🔴🔴 **仲裁结果：H2 被反驳；obs 判据成立**（见 [history/52](../52_session_conclusion.md) §7.24.21–7.24.24）

**`c30_arbitrate.py`**（在 c27 的 29 个实例上同时算 obs 与基行平行性）：

| 判据 | 正确率 |
|---|---|
| **obs 判据**（obs$=d$ ⟺ YES）| **28 / 29** ✓ |
| **H2（基行平行）** | **3 / 29** ✗ |
| 两判据不同 | **27 / 29** |

$$\boxed{\ \textbf{H2 被反驳}\ ✗\ ——\ \textbf{基行平行不是必要条件}\ }$$
$$\text{反例：}n{=}5\ \text{inst }1：\ \text{obs}{=}3{=}d,\ \text{基行不平行},\ \text{成功率}\ 95.8\%\ ✓\ \Longrightarrow\ \rho\ge2\ \text{构造更常用}$$

**obs 判据的当前状态**：29 个实例对 **28** 个；唯一失配是"稀疏但非空"（obs$<d$ 但 1.7%）
$$\Longrightarrow\ \textbf{obs 是"密度的强预测"}：\text{obs}{=}d\Rightarrow\text{必 YES（累计 52/52 单侧无失败）};\ \text{obs}{<}d\Rightarrow\text{通常空，偶尔稀疏非空}$$

**⚠️** §7.24.12 的"全部解 $\rho{=}1$"是**实例特有**，不能外推；obs$<d$ 的稀疏机制**仍未查明**

### 0.3.38 **本会话最终结论（第 17 次修正）**

| 类别 | 内容 |
|---|---|
| **严格（Lean）** | $(A)\iff$分解$\iff$核条件；$K\subseteq\ker(CA^2)\Rightarrow(5b)$ 恒失败 |
| **严格（引理）** | $q\le d_{CA}\wedge\rho{=}q\Rightarrow(5b)$ 不可能 |
| **严格（枚举）** | c19 实例在 $q{=}d{+}1$ 上 531,441 全枚举**无解** |
| **强证据（52/52）** | obs$=d\Rightarrow q{=}d{+}1$ 处 **必 YES** |
| **已知例外** | obs$<d$ 但稀疏非空（$2.0\%$、$1.7\%$）|
| **已反驳** | H2（基行平行）3/29 ✗ |
| **未知** | obs$<d$ 时**空与稀疏的判别** —— 唯一剩余 |

$$\boxed{\ \text{q1 仍未定；}\textbf{obs 是最强的预测量（52/52 单侧）}，\text{其"空性"侧仍需代数判定}\ }$$

### 0.3.39 🎯🎯🎯 **H3 完全成立：obs$=d$ ⟺ 存在满秩解**（见 [history/52](../52_session_conclusion.md) §7.24.25–7.24.28）

**完全枚举**（$q{=}d{+}1$；$n{=}4$ 用 $\{-1,0,1\}^6$，$n{=}5$ 用 $\{0,1\}^{12}$）：

| 实例 | obs | 解数 | $\rho{=}\operatorname{rank}(LN)$ 分布 | 满秩解 |
|---|---|---|---|---|
| $n{=}4$ t=0 | **$2=d$** | **456** | **$\{2{:}456\}$** | **456** ✓ |
| $n{=}4$ t=1 | $1<2$ | 0 | — | **0** |
| $n{=}4$ t=5 | $1<2$ | 80 | $\{1{:}80\}$ | **0** |
| $n{=}5$ t=0 | **$3=d$** | **2058** | **$\{3{:}2058\}$** | **2058** ✓ |
| $n{=}5$ t=7 | $2<3$ | 336 | $\{2{:}336\}$ | **0** |

$$\boxed{\ \textbf{obs}=d_{CA}\iff\exists\ \text{满秩解}\ (\rho=d_{CA})\iff\ker(LN)=0\ }$$

### 0.3.40 ⭐⭐⭐ **机制（obs 判据的完整解释）**

$$\text{obs}=d\ \Longrightarrow\ \text{解集含}\ \textbf{Zariski-开集}\ \{\rho=d\}\qquad(\text{解集是开的})$$
$$\text{obs}<d\ \Longrightarrow\ \text{解集}\subseteq\{\rho<d\}\ \text{（闭的退化轨迹）}\qquad(\text{解集是薄的})$$

$$\Longrightarrow\ \text{完全解释成功率：obs}{=}d\ \text{时}\ 62.6\%/50.2\%;\ \text{obs}{<}d\ \text{时}\ 11\%/8.2\%/0\%$$

### 0.3.41 **obs 判据的最终精确形式**

$$\boxed{\
\begin{array}{ll}
\textbf{obs}=d_{CA} & \Longrightarrow\ q{=}d_{CA}{+}1\ \text{处}\ \textbf{必 YES（解集含开集）}\qquad \textbf{52/52}\ \text{无失败}\\
\textbf{obs}<d_{CA} & \Longrightarrow\ \text{解集}\subseteq\{\rho<d_{CA}\}\ \text{（薄）};\ \textbf{是否空未定}
\end{array}}$$

$$\text{obs}=\dim\big(\text{含}\operatorname{row}(R)\ \text{的最小}\ A'\text{-不变子空间}\big),\quad R=AN-NA'$$

$$\Longrightarrow\ \textbf{判定} = \underbrace{\text{obs 计算}}_{O(d^3)} + \underbrace{\text{obs}{<}d\ \text{时}\ \{\rho{<}d\}\ \text{上解的存在性}}_{\textbf{唯一剩余}}$$

### 0.3.42 **本会话最终结论（第 18 次修正）**

| 类别 | 内容 |
|---|---|
| **严格（Lean）** | $(A)\iff$分解$\iff$核条件；$K\subseteq\ker(CA^2)\Rightarrow(5b)$ 恒失败 |
| **严格（引理）** | $q\le d_{CA}\wedge\rho{=}q\Rightarrow(5b)$ 不可能 |
| **严格（枚举）** | c19 实例在 $q{=}d{+}1$ 上 531,441 全枚举**无解** |
| **强证据（52/52）** | obs$=d\Rightarrow$ 必 YES |
| **机制（H3，5/5）** | obs$=d\iff\exists$ 满秩解 $\iff\ker(LN)=0$；解集含开集 |
| **结构** | obs$<d\Rightarrow$ 解集 $\subseteq\{\rho<d\}$（薄）|
| **唯一剩余** | $\{\rho<d\}$ 上解的存在性（空/非空）|

$$\boxed{\ \text{q1 仍未定；}\textbf{obs 判据已有机制（H3）}，\text{只剩退化轨迹上的存在性}\ }$$

### 0.3.43 ⭐ **$\rho{=}1$ 的精确条件**（见 [history/52](../52_session_conclusion.md) §7.24.29–7.24.31）

$$\rho{=}1\ \text{时}\ A_0=c\,u^{\mathsf T},A_1=d\,u^{\mathsf T}\ \Longrightarrow\ \operatorname{rank}(\lambda A_0-A_1)=1\iff\textbf{比值}\ d_i/c_i\ \textbf{不全相等}$$
$$\text{固定行}\ \Longrightarrow\ \boxed{\gamma_0\parallel\alpha_0\ (\text{基行平行})}\ \textbf{必要}$$

**验证**（$n{=}4$ 完全枚举）：

| 实例 | obs | 平行 | $\rho{=}1$ 解 | 满秩解 |
|---|---|---|---|---|
| t=0 | **2** | N | **0** | **456** |
| t=1 | 1 | Y | **0** | 0 |
| t=5 | 1 | Y | **80** | 0 |

$$\text{存在}\ \rho{=}1\ \text{解}\Rightarrow\text{平行}\ (3/3)\ \checkmark\ ;\quad \text{反向不成立（t=1 平行但 0 解）}$$

### 0.3.44 ⚠️ **合成判据 "obs$=d$ ∨ 平行" 被否**

$$\text{反例}：\text{t=1}\ (\text{obs}{<}d,\ \text{平行})\ \text{却}\ \textbf{0 解}\ ✗$$

### 0.3.45 **本会话最终结构（第 19 次修正）**

| 条件 | 结论 |
|---|---|
| **obs$=d_{CA}$** | $\exists$ 满秩解 $\Rightarrow$ **YES**（52/52 + H3 5/5）|
| **obs$<d_{CA}$** | 解 $\subseteq\{\rho<d\}$；$\rho{=}1$ 要求基行平行，但平行**不保证**有解；还需"比值不全相等" |
| **唯一剩余** | **obs$<d$ 且基行平行时，$\rho{=}1$ 构造何时可行？** |

$$\boxed{\ \text{q1 仍未定；剩余问题已缩小到}\ \textbf{一个具体的构造可行性判定}\ }$$

### 0.3.46 ⭐⭐⭐⭐ **$\rho{=}1$ 的精确判据（3/3 验证）**（见 [history/52](../52_session_conclusion.md) §7.24.32–7.24.34）

**推导**：

$$\text{固定行}\Longrightarrow\ \text{基行平行}\ \gamma_0\parallel\alpha_0$$
$$\text{自由行需}\ d_i\alpha_0-c_i\alpha_0A'\in\operatorname{row}(R)\ ;\ \text{用}\ \alpha_0A'=d_0\alpha_0-\beta_0\ \text{得}\ (d_i-c_id_0)\alpha_0+c_i\beta_0$$
$$\Longrightarrow\ \text{要么}\ d_i=c_id_0\ (\text{比值全等}\Rightarrow(5b)\ \text{失败}),\ \text{要么}\ \alpha_0\in\operatorname{row}(R)$$

$$\boxed{\ \rho{=}1\ \text{可行}\iff\textbf{基行平行}\ \wedge\ \alpha_0=L_0N\in\operatorname{row}(R)\ }$$

**验证**：

| 实例 | 平行 | $\alpha_0\in\operatorname{row}R$ | $\rho{=}1$ 解 | 判据预 | 一致 |
|---|---|---|---|---|---|
| t=0 | N | N | 0 | 无解 | ✓ |
| t=1 | **Y** | **N** | **0** | **无解** | ✓ |
| t=5 | Y | **Y** | **80** | **有解** | ✓ |

$$\textbf{3/3}\ \checkmark\ ;\quad \text{两条件都}\ \textbf{多项式可判}\ \Longrightarrow\ \rho{=}1\ \text{分支}\ \textbf{完全判定}$$

### 0.3.47 **完整的判定图景（第 20 次修正）**

| 条件 | 结论 |
|---|---|
| **obs$=d_{CA}$** | $\exists$ 满秩解 $\Rightarrow$ **YES**（52/52 + H3 5/5）|
| **obs$<d_{CA}$**，$\rho{=}1$ | 可行 $\iff$ 基行平行 $\wedge$ $\alpha_0\in\operatorname{row}(R)$（**3/3**）|
| **obs$<d_{CA}$**，$\rho\ge2$ | **未判定** —— 唯一剩余 |

$$\Longrightarrow\ \textbf{若}\ \text{obs}{<}d\ \text{时只能有}\ \rho{=}1\ \text{解}\ \Longrightarrow\ \text{判定}\ \textbf{多项式}\ \Longrightarrow\ \textbf{q1 为假}$$

$$\textbf{剩余全部}\ =\ \text{是否存在}\ (\text{obs}{<}d)\wedge(\rho{=}1\ \text{不可行})\wedge(\text{仍有}\ \rho{\ge}2\ \text{解})\ \text{的实例？}$$

$$\text{已知：t=1（平行，}\alpha_0\notin\mathrm{row}R\text{）在}\ q{=}3\ \text{上}\ \rho{=}1,2\ \text{都无解；c19 全枚举无解}$$

### 0.3.48 🔴 **合成判据被否（21/22）；发现 $\rho\ge2$ 的解存在**（见 [history/52](../52_session_conclusion.md) §7.24.35–7.24.39）

**被检验的合成判据**：
$$\text{YES at}\ q{=}d{+}1\ \overset{?}{\iff}\ \text{obs}=d\ \vee\ (\text{基行平行}\wedge\alpha_0\in\operatorname{row}R)$$

**结果**（22 实例，$n\in\{4,5,6\}$）：一致 **21**，**不一致 1**

**唯一反例**：
$$n{=}5\ \text{t=7}:\ d{=}3,\ \text{obs}{=}2{<}3,\ \text{平行}=Y,\ \alpha_0\notin\operatorname{row}R,\ \text{成功率}\ \mathbf{3.0\%}$$
$$\Longrightarrow\ \rho{=}1\ \text{不可行仍有解}\ \Longrightarrow\ \textbf{解来自}\ \rho{=}2$$

### 0.3.49 ⚠️ **obs 判据的最终状态：只有单侧**

$$\boxed{\ \textbf{obs}=d_{CA}\ \Longrightarrow\ q{=}d_{CA}{+}1\ \text{处必 YES}\qquad(\text{累计}\ \mathbf{52/52})\ }$$
$$\textbf{obs}<d_{CA}\ \Longrightarrow\ \text{解}\subseteq\{\rho<d\};\ \text{存在性}\ \textbf{依赖}\ \rho,\ \textbf{不可由 obs 判定}$$
$$\Longrightarrow\ \textbf{obs}\ \text{是}\ \textbf{充分条件（单侧）}，\text{不是充要条件}\ ✗$$

### 0.3.50 **本会话最终状态（第 21 次修正）**

| 类别 | 内容 | 状态 |
|---|---|---|
| **Lean（45 定理）** | $(A)\iff$分解$\iff$核条件；$K\subseteq\ker(CA^2)\Rightarrow(5b)$ 恒失败 | ✅ 严格 |
| **引理** | $q\le d_{CA}\wedge\rho{=}q\Rightarrow(5b)$ 不可能 | ✅ 严格 |
| **枚举** | c19 在 $q{=}d{+}1$ 上 531,441 全枚举**无解** | ✅ 严格 |
| **强证据（52/52）** | obs$=d\Rightarrow$ 必 YES | ⚠️ 单侧 |
| **机制（H3）** | obs$=d\iff\exists$ 满秩解 $\iff\ker(LN)=0$ | ⚠️ 单侧 |
| **判据（$\rho{=}1$，3/3）** | 可行 $\iff$ 平行 $\wedge$ $\alpha_0\in\operatorname{row}R$ | ✅ |
| **新发现** | $\rho{=}2$（$<d$）的解**存在**（n=5 t=7，3%） | ✅ |
| **已反驳** | obs 充要性、合成判据、H2、obs 强形式 | ✗ |
| **未定** | $\{\rho<d\}$ 上解的存在性（$\rho\ge2$ 分支）| ⚠️ |

$$\boxed{\ \textbf{q1 仍未定}。\text{判定}\ \textbf{不是}\ \text{由 obs 单独决定；}\{\rho<d\}\ \text{的分层结构是唯一剩余}\ }$$

### 0.3.51 ⭐ **方法论总结**

$$\textbf{21 处修正，其中 12 处是猜想/判据被自己的数据推翻}\ ;\qquad \textbf{0 处是"已证结论"被推翻}\ \checkmark$$

$$\text{被推翻的判据}：\text{不变性、}m{-}d\text{、}\mathrm{rank}(AN){<}d\text{、}\rho_0\text{、row 包含、铅笔特征值、}A'\ \text{有理谱、}A'\ \text{实谱、obs 充要、obs 强形式、加行单调、H2、合成判据}$$

### 0.3.52 ⭐⭐⭐ **$\{\rho<d\}$ 的分层结构（$n{=}5$ t=7 完全枚举确认）**（见 [history/52](../52_session_conclusion.md) §7.24.40–7.24.42）

**目标实例**：$n{=}5$，$d{=}3$，$m{=}4$，$e{=}1$，obs$=2{<}3$，平行$=Y$，$\alpha_0\notin\operatorname{row}R$

**$\{0,1\}^{12}$ 完全枚举**（4096 点）：$(5a)$ 通过 3144 ；**解 336（8.20%）**；$\rho$ 分布 $=\boxed{\{2{:}336\}}$

$$\boxed{\ \textbf{全部解都}\ \rho{=}2\ ——\ \text{既非}\ \rho{=}1\ (\text{不可行}),\ \text{也非}\ \rho{=}3{=}d\ }$$

### 0.3.53 ⭐⭐⭐ **分层结构（本会话最终图景）**

| $\rho$ | 存在性条件 | 状态 |
|---|---|---|
| $d$ | **obs$=d$**（$\iff\ker(\mathcal LN)=0$）| **已判定**（52/52 + H3 5/5）|
| $1$ | 基行平行 $\wedge$ $\alpha_0\in\operatorname{row}R$ | **已判定**（3/3）|
| $2$ | **未明**（$n{=}5$ t=7 有 336 个，全 $\rho{=}2$）| **未判定** |
| $\vdots$ | | |
| $d{-}1$ | **未明** | **未判定** |

$$\Longrightarrow\ \textbf{判定} = \bigvee_{\rho=1}^{d}\big(\rho\ \text{层的存在性}\big)\ ——\ \text{逐层的代数问题}$$

$$\textbf{已完成}：\rho{=}d\ (\text{obs}),\ \rho{=}1\ (\text{平行}\wedge\alpha_0\in\mathrm{row}R)\quad;\qquad \textbf{剩余}：\rho=2,\dots,d{-}1$$

$$\text{对}\ d\le2\ \text{只有两层}\ \Longrightarrow\ \textbf{完全可判}\ \Longrightarrow\ \textbf{q1 在}\ d\le2\ \text{时为假}\ ⚠️\ (\text{待严格化})$$

### 0.3.54 **q1 的最精确状态**

$$\boxed{\ \textbf{q1 未定}。\text{判定}\ \textbf{不是}\ \text{单一 obs 条件，而是}\ \textbf{逐层}\ (\rho{=}1..d)\ \text{存在性的并}\ }$$

### 0.3.55 ⭐⭐⭐⭐ **定律：$\operatorname{rank}(\text{解})=\text{obs}$**（见 [history/52](../52_session_conclusion.md) §7.24.43–7.24.47）

**$n{=}5$ t=7 的 $\{-1,0,1\}^{12}$ 完整枚举**（531,441 点，750 s）：
$$(5a)\ \text{通过}\ 473{,}877\ ;\quad \textbf{解}\ 16{,}848\ (3.17\%)\ ;\quad \rho\ \text{分布}=\boxed{\{2{:}16{,}848\}}$$

| 实例 | $d$ | **obs** | 观到的 $\rho$ | $\rho=\text{obs}$？ |
|---|---|---|---|---|
| $n{=}4$ t=0 | 2 | **2** | 2 | ✓ |
| $n{=}4$ t=5 | 2 | **1** | 1 | ✓ |
| $n{=}5$ t=0 | 3 | **3** | 3 | ✓ |
| $n{=}5$ t=7 | 3 | **2** | 2 | ✓ |

$$\boxed{\ \operatorname{rank}\big(\text{任何解}\big)=\text{obs}\qquad(\mathbf{4/4})\ }$$

**统一了此前全部观察**：
$$\text{obs}=d\Rightarrow\rho=d\ (\text{满秩})\Rightarrow\text{解集含开集}\Rightarrow\text{高成功率}\ ✓$$
$$\text{obs}<d\Rightarrow\rho=\text{obs}\ (\textbf{固定秩亏})\Rightarrow\text{薄}\ ✓$$
$$\text{obs}<d\ \text{的"分层"}\ \textbf{不是}\ \rho=1,2,\dots\ \text{各层，而是}\ \textbf{唯一一层}\ \rho=\text{obs}\ !$$

### 0.3.56 **判定问题的大幅简化**

$$\textbf{obs}\ \text{有闭式}\ (O(d^3))\ ;\quad \rho=\text{obs}\ \text{层}\ \textbf{秩固定}$$
$$\Longrightarrow\ \textbf{判定} = \textbf{一个固定秩的代数簇是否为空}\ ——\ \text{标准代数几何问题}$$

$$\text{已知：}\text{obs}=d\Rightarrow\text{非空}\ (52/52)\ ;\qquad \text{obs}<d\Rightarrow\ \textbf{有时空（c19, t=1）有时非空（80; 16,848）}$$

$$\textbf{唯一剩余}：\ \text{obs}<d\ \text{时}\ \rho{=}\text{obs}\ \text{层}\ \textbf{何时空？}$$

### 0.3.57 **机制猜想（$\rho=\text{obs}$）**

$$\text{设}\ V=\langle\operatorname{row}R\rangle_{A'},\ \dim V=\text{obs};\ \text{所有}\ \beta\in V$$
$$\text{模}\ V：\ \bar\alpha(\lambda I-\bar A')\ \Longrightarrow\ \text{要 (5b) 须}\ \dim(\text{span}\,\bar\alpha)=\text{obs}\ \Longrightarrow\ \rho=\text{obs}$$
$$\text{而}\ \text{obs}<d\Rightarrow\bar A'\ \textbf{有基域特征值}\ \Longrightarrow\ \text{存在秩降}\ \Longrightarrow\ \text{需额外条件}\ !$$

### 0.3.58 🎯🎯🎯🎯🎯 **统一判据（本会话最终成果，23/23）**（见 [history/52](../52_session_conclusion.md) §7.24.48–7.24.53）

$$\boxed{\ \textbf{YES at}\ q{=}d_{CA}{+}1\iff\alpha_0=L_0N\ \in\ V:=\big\langle\operatorname{row}(R)\big\rangle_{A'}\ }$$

$$\text{其中}\ V\ \text{是}\ \textbf{含}\ \operatorname{row}(R)\ \text{的最小}\ A'\text{-不变子空间},\quad A'=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN,\ R=AN-NA'$$

| 验证器 | 实例 | 结果 |
|---|---|---|
| `c36_alpha0_in_V.py` | **22** | 21 直接吻合 + 1 个"反例"是**阈值假象**（t=7 已知 16,848 解，判据预测 YES 正确）|
| `c37_c19_check.py` | **1** | c19：$\alpha_0=(0,1,-2)\notin V$ ⟹ 预测 NO ⟹ 与 531,441 枚举**一致** ✓ |

$$\boxed{\ \textbf{23 / 23}\ \checkmark\ }$$

### 0.3.59 ⭐⭐⭐⭐⭐ **它统一了全部此前观察**

$$\text{obs}=d\Rightarrow V=\mathbb{R}^d\Rightarrow\alpha_0\in V\ \textbf{自动}\Rightarrow\textbf{恒 YES}\Rightarrow\textbf{解释 52/52}\ ✓$$
$$\rho{=}1\ (\text{obs}{=}1)\Rightarrow V=\operatorname{row}R\Rightarrow\text{判据}=\alpha_0\in\operatorname{row}R\Rightarrow\textbf{与 c32 一致}\ ✓$$
$$\operatorname{rank}(\text{解})=\text{obs}=\dim V\Rightarrow\textbf{与定律一致}\ ✓$$
$$\text{obs}<d\Rightarrow V\ \text{真}\Rightarrow\text{实质条件}\Rightarrow\text{有时 NO（c19, t=1）有时 YES（t=5, t=7）}\ ✓$$

### 0.3.60 ⭐⭐⭐⭐ **后果：q1 为假**

$$\alpha_0\ \text{一次乘法}\ ;\quad V=\big\langle\operatorname{row}R\big\rangle_{A'}\ \text{不变闭包}\ O(d^3)\ ;\quad \text{判定}=\text{秩比较}\ \Longrightarrow\ \textbf{多项式}$$

$$\boxed{\ \textbf{最小行数与判定都多项式}\ \Longrightarrow\ \textbf{q1 为假（NP-hardness 不成立）}\ }$$

**⚠️ 保留**：23 实例（非证明）；$n\le6,r{=}1,p{=}1$；1% 与 0% 在 100 采样下难区分；**未给机制证明**

### 0.3.61 **机制草图**

$$\alpha_0\in V\ \Longrightarrow\ \text{所有行在}\ V\oplus V\ \Longrightarrow\ \text{模}\ V\ \text{铅笔恒零}\ \Longrightarrow\ \text{秩}\le\dim V\ \text{且可达}\ \Longrightarrow\ (5b)\ \text{成立}\ ✓$$
$$\alpha_0\notin V\ \Longrightarrow\ \text{模}\ V\ \text{含}\ \bar\alpha_0(\lambda I-\bar A')\ \text{项}\ \Longrightarrow\ \text{某}\ \lambda\ \text{处秩降}\ \Longrightarrow\ (5b)\ \text{失败}$$
$$\text{（缺口：}\bar A'\ \text{的特征值须在}\ \mathbb{Q}\ ;\ \text{但}\ V\ \text{是全部闭包}\ \Longrightarrow\ \text{可能保证）}$$

### 0.3.62 **本会话最终结论（第 23 次修正）**

| 类别 | 内容 |
|---|---|
| **严格（Lean 45 定理）** | $(A)\iff$分解$\iff$核条件；$K\subseteq\ker(CA^2)\Rightarrow(5b)$ 恒失败 |
| **严格（引理）** | $q\le d_{CA}\wedge\rho{=}q\Rightarrow(5b)$ 不可能 |
| **严格（枚举）** | c19 在 $q{=}d{+}1$ 上 531,441 **无解**；t=7 有 **16,848 解** |
| **定律（4/4）** | $\operatorname{rank}(\text{解})=\text{obs}$ |
| **统一判据（23/23）** | **YES $\iff$ $\alpha_0=L_0N\in\langle\operatorname{row}R\rangle_{A'}$** |
| **后果** | 判定**多项式** $\Longrightarrow$ **q1 为假** |

$$\boxed{\ \text{q1 有了明确的候选答案：}\textbf{NP-hardness 不成立}\ ;\ \text{判据需}\ \textbf{证明}\ \text{与}\ \textbf{更大规模复核}\ }$$

### 0.3.63 ⭐⭐⭐⭐ **充分性的化归：整个判定 ⟸ 一条引理**（见 [history/52](../52_session_conclusion.md) §7.24.54–7.24.55）

**归约**：若 $\alpha_0\in V$（$\dim V=\text{obs}$），把问题限制到 $V$：
$$V\cong\mathbb{R}^{\text{obs}},\ A'_V=A'|_V,\ \operatorname{row}R\subseteq V\ \Longrightarrow\ \beta_i\ \text{在}\ V\ \text{内}$$
$$V\ \text{是}\ \textbf{全部}\ \text{闭包}\ \Longrightarrow\ \text{归约后}\ \operatorname{obs}'=\dim V=d'\ \textbf{（满）}$$

$$\boxed{\ \textbf{充分性}\iff\text{仅需}\ \big(\operatorname{obs}=d\Rightarrow\text{YES}\big)\ }$$

**数值验证**（`c38_reduction_check.py`）：

| 实例 | $d$ | obs | $\dim V$ | 原成功率 | 归约后 | obs$'$=d$'$ |
|---|---|---|---|---|---|---|
| $n{=}4$ t=0 | 2 | 2 | 2 | 96% | **93%** | ✓ |
| $n{=}4$ t=5 | 2 | 1 | 1 | 86% | **94%** | ✓ |
| $n{=}5$ t=0 | 3 | 3 | 3 | 94% | **97%** | ✓ |
| **$n{=}5$ t=7** | 3 | 2 | 2 | **0%** | **83%** | ✓ |

$$\boxed{\ \text{t=7 的}\ 0\%\to 83\%\ \Longrightarrow\ \text{归约后确实是"满"情形}\ \checkmark\ }$$

### 0.3.64 **本会话的最终理论状态**

| 类别 | 内容 |
|---|---|
| **严格（Lean 45 定理）** | $(A)\iff$分解$\iff$核条件；$K\subseteq\ker(CA^2)\Rightarrow(5b)$ 恒失败 |
| **严格（引理）** | $q\le d_{CA}\wedge\rho{=}q\Rightarrow(5b)$ 不可能 |
| **严格（枚举）** | c19 531,441 **无解**；t=7 **16,848 解（全 $\rho{=}2$）** |
| **定律（4/4）** | $\operatorname{rank}(\text{解})=\text{obs}$ |
| **统一判据（23/23）** | **YES $\iff$ $\alpha_0=L_0N\in\langle\operatorname{row}R\rangle_{A'}$** |
| **归约（4/4）** | 充分性 $\iff$ $\boxed{\operatorname{obs}=d\Rightarrow\text{YES}}$（唯一剩余）|

$$\boxed{\ \textbf{q1 的判定已化归为一条引理}：\ \operatorname{obs}=d\Rightarrow\text{存在解}\ }$$

$$\text{若成立（52/52 + H3 5/5 支持）}\ \Longrightarrow\ \textbf{判定多项式}\ \Longrightarrow\ \textbf{q1 为假}$$

### 0.3.65 🎯🎯🎯🎯🎯 **充分性的构造性证明**（见 [history/52](../52_session_conclusion.md) §7.24.56–7.24.59）

**显式构造**（$q{=}d{+}1$ 行 = 1 固定 + $d$ 自由）：

$$\alpha_i=e_i\ (\text{可行：}L\mapsto LN\ \text{满射}),\quad A_0=I_d\ \Longrightarrow\ \ker A_0=0\ \Longrightarrow\ \boxed{\textbf{(5a)}\ \textbf{自动}}$$
$$A_1=A'+B,\ B\ \text{的行}=\ell_iR\ (\ell_iN=e_i)\ ;\qquad \boxed{\textbf{(5b)}\iff\operatorname{charpoly}(A_1)\ \text{无有理根}}$$

**验证**（`c39_construction.py`）：

| 实例 | $d$ | obs | 无根率 | $(5a)$ | $(5b)$ |
|---|---|---|---|---|---|
| $n{=}4$ t=0 | 2 | 2 | **97%** | True | True |
| $n{=}4$ t=2 | 2 | 2 | **88%** | True | True |
| $n{=}4$ t=3 | 2 | 2 | **80%** | True | True |
| $n{=}5$ t=0 | 3 | 3 | **90%** | True | True |
| $n{=}5$ t=1 | 3 | 3 | **88%** | True | True |

### 0.3.66 ⭐⭐⭐⭐⭐ **存在性的经典依据（pole placement）**

$$\operatorname{charpoly}(A'+\Lambda R)\ \textbf{可任意配置}\iff(A'^{\mathsf T},R^{\mathsf T})\ \textbf{可控}$$
$$\iff\bigcap_k\ker(RA'^k)=0\iff\big\langle\operatorname{row}R\big\rangle_{A'}=\mathbb{R}^d\iff\boxed{\ \textbf{obs}=d_{CA}\ }$$

$$\Longrightarrow\ \text{取}\ d\ \text{次不可约}\ p\ (\text{Eisenstein})\ \Longrightarrow\ \exists\Lambda:\ \operatorname{charpoly}=p\ \textbf{无有理根}\ \Longrightarrow\ (5b)\ ✓$$

$$\boxed{\ \textbf{obs}=d\ \Longrightarrow\ \text{YES}\quad\textbf{已构造性证明}\ }$$

### 0.3.67 **判据的证明状态（精确）**

$$\boxed{\
\begin{array}{ll}
\textbf{充分（}\Leftarrow\textbf{）} & \alpha_0\in V\Rightarrow\text{YES}\qquad \textbf{已证（归约 + pole placement）}\ ✓\\
\textbf{必要（}\Rightarrow\textbf{）} & \alpha_0\notin V\Rightarrow\text{NO}\qquad \textbf{仅实证}（23/23）\ ⚠️
\end{array}}$$

$$\text{充分性} = \underbrace{\text{归约到}\ V}_{\text{obs}'=d'} + \underbrace{A_0=I + \text{pole placement}}_{\text{本轮}}$$

### 0.3.68 **本会话最终结论（第 24 次修正）**

| 类别 | 内容 |
|---|---|
| **严格（Lean 45 定理）** | $(A)\iff$分解$\iff$核条件；$K\subseteq\ker(CA^2)\Rightarrow(5b)$ 恒失败 |
| **严格（引理）** | $q\le d_{CA}\wedge\rho{=}q\Rightarrow(5b)$ 不可能 |
| **严格（枚举）** | c19 531,441 **无解**；t=7 **16,848 解（全 $\rho{=}2$）** |
| **定律（4/4）** | $\operatorname{rank}(\text{解})=\text{obs}$ |
| **充分性（已证）** | $\alpha_0\in\langle\operatorname{row}R\rangle_{A'}\Rightarrow$ **YES** |
| **必要性（实证）** | $\alpha_0\notin V\Rightarrow$ **NO**（23/23）|
| **后果（若必要性得证）** | 判定多项式 $\Rightarrow$ **q1 为假** |

$$\boxed{\ \text{q1 的充分性已证；只剩必要性}\ (\alpha_0\notin V\Rightarrow\text{NO})\ \text{的证明}\ }$$

### 0.3.69 🔴🔴 **必要性的机制是错的（第 25 处更正）**（见 [history/52](../52_session_conclusion.md) §7.24.60–7.24.62）

**我此前的机制**（0.3.57）：$\alpha_0\notin V$ ⟹ 模 $V$ 含 $\bar\alpha_0(\lambda I-\bar A')$ ⟹ $\bar A'$ 在商上有有理特征值 ⟹ 秩降

**检验**（`c40_quotient_spec.py`）：

| 实例 | obs | $\alpha_0\in V$ | rat.roots($A'$) | rat.roots($\bar A'$) |
|---|---|---|---|---|
| $n{=}4$ t=0 | 2 | Y | `[]` | — |
| $n{=}4$ t=1 | 1 | **N** | `[]` | **`[]`** ⚠️ |
| $n{=}4$ t=5 | 1 | Y | `[]` | `有根` |
| **c19** | 2 | **N** | `[]` | **`[]`** ⚠️ |

$$\boxed{\ \text{两个}\ \alpha_0\notin V\ \text{实例（均 NO）的}\ \bar A'\ \textbf{都无有理特征值}\ \Longrightarrow\ \textbf{机制不适用}\ ✗}$$
$$\text{而}\ t{=}5\ (\alpha_0\in V,\ \textbf{YES})\ \text{的}\ \bar A'\ \textbf{有}有理根\ \Longrightarrow\ \text{商的谱与判据}\ \textbf{无关}$$

$$\Longrightarrow\ \textbf{必要性的机制}\ \textbf{仍未查明}\ ⚠️$$

### 0.3.70 **本会话最终精确状态（第 25 次修正）**

| 类别 | 内容 |
|---|---|
| **已证（Lean 45 定理）** | $(A)\iff$分解$\iff$核条件；$K\subseteq\ker(CA^2)\Rightarrow(5b)$ 恒失败 |
| **已证（引理）** | $q\le d_{CA}\wedge\rho{=}q\Rightarrow(5b)$ 不可能 |
| **已证（枚举）** | c19 531,441 **无解**；t=7 **16,848 解（全 $\rho{=}2$）** |
| **已证（充分性）** | $\alpha_0\in\langle\operatorname{row}R\rangle_{A'}\Rightarrow$ **YES**（构造 + pole placement）|
| **定律（4/4）** | $\operatorname{rank}(\text{解})=\text{obs}$ |
| **判据（23/23）** | **YES $\iff$ $\alpha_0\in V$** |
| **仅实证** | **必要性**（$\alpha_0\notin V\Rightarrow$ NO）；**机制未查明** |
| **已反驳** | 必要性机制（商的谱）；另有 14 个判据 |

$$\boxed{\ \text{q1}\ \textbf{充分性已证};\ \text{必要性仅实证（23/23）且机制未知}\ }$$

### 0.3.71 **本会话净收获**

1. **化简到 $2d$ 维**（六步链，各 400/400 可复现）
2. **Lean 45 条定理**（零 error）
3. **c6/c6′ 被可手算无穷族证伪** ⟹ 分支 A 未被排除
4. **定律 $\operatorname{rank}(\text{解})=\text{obs}$**；**统一判据 YES $\iff$ $\alpha_0\in V$**（23/23）
5. **充分性已证**（构造 + pole placement）；必要性仅实证
6. **25 处自我更正**，其中 **16 处是猜想/判据被自己的数据推翻**；**0 处已证结论被推翻**

### 0.3.72 🔴🔴🔴 **重要更正：「23/23」是误导的（第 26 处）**（见 [history/52](../52_session_conclusion.md) §7.24.63–7.24.66）

**本轮**（`c41_necessity_hard.py`，22 实例各 300 采样）：

| 组 | 实例数 | 成功率 |
|---|---|---|
| $\alpha_0\in V$（YES）| **21** | 0.7–98.0% |
| $\alpha_0\notin V$（NO）| **1** | **0.0%** |

$$\textbf{反例}\ 0\ ——\ \text{但}\ \textbf{只有 1 个}\ \alpha_0\notin V\ \text{实例}\ ⚠️$$

### 0.3.73 ⭐ **为何 $\alpha_0\notin V$ 罕见**

$$\text{obs}=d\ \Longrightarrow\ V=\mathbb{R}^d\ \Longrightarrow\ \alpha_0\in V\ \textbf{自动}$$
$$\Longrightarrow\ \textbf{obs}=d\ \text{的实例只检验}\ \textbf{充分性}，\textbf{不检验必要性}$$

### 0.3.74 **必要性证据的真实清单**

$$\textbf{真正检验必要性的实例：仅 2 个}$$
$$\textbf{①}\ n{=}4\ \text{t=1}:\ 0/300 + 0/120\ ;\qquad \textbf{②}\ \textbf{c19}:\ \textbf{0/531,441}\ \textbf{（完整枚举）} ⭐$$

$$\boxed{\ \text{「23/23」应更正为：}\ \textbf{充分性}\ 21/21\ \textbf{（强）};\ \textbf{必要性}\ \textbf{2/2}\ \textbf{（薄弱）}\ }$$

### 0.3.75 **本会话最终精确状态（第 26 次修正）**

| 类别 | 内容 |
|---|---|
| **已证（Lean 45 定理）** | $(A)\iff$分解$\iff$核条件；$K\subseteq\ker(CA^2)\Rightarrow(5b)$ 恒失败 |
| **已证（引理）** | $q\le d_{CA}\wedge\rho{=}q\Rightarrow(5b)$ 不可能 |
| **已证（枚举）** | c19 531,441 **无解**；t=7 **16,848 解（全 $\rho{=}2$）** |
| **已证（充分性）** | $\alpha_0\in V\Rightarrow$ **YES**（构造 + pole placement）；21/21 实证无失败 |
| **定律（4/4）** | $\operatorname{rank}(\text{解})=\text{obs}$ |
| **判据** | YES $\iff$ $\alpha_0\in V$；**必要性仅 2 个实例** |
| **已反驳** | 必要性机制（商的谱）；另有 14 个判据 |

$$\boxed{\ \text{q1 仍未定}:\ \textbf{充分性已证};\ \textbf{必要性仅 2 实例（c19 穷尽）且机制未知}\ }$$

$$\Longrightarrow\ \textbf{下一步最该做}：\textbf{造更多}\ (\text{obs}<d\ \wedge\ \alpha_0\notin V)\ \text{的实例}\ \text{检必要性}\ ⚠️$$

### 0.3.76 ⭐⭐⭐⭐ **定向构造：5 个 (obs$<d$ ∧ $\alpha_0\notin V$) 实例全部 NO**（见 [history/52](../52_session_conclusion.md) §7.24.67–7.24.69）

**构造法**（`c42_construct_alpha0_out.py`）：

$$\text{①取}\ (A,C)\ \text{使}\ \text{obs}<d\ ;\ \textbf{②}V\ \text{真}\Rightarrow\text{generic}\ \alpha_0\notin V\ ;\ \textbf{③}\text{解}\ L_0N=\alpha_0\ ;\ \textbf{④}q{=}d{+}1\ \text{上完全枚举}$$

**结果**：

| 实例 | $d$ | obs | $\alpha_0\in V$ | 枚举 | 解数 |
|---|---|---|---|---|---|
| trial 0 | 2 | 1 | **N** | 729 | **0** |
| trial 1 | 2 | 1 | **N** | 729 | **0** |
| trial 7 | 2 | 1 | **N** | 729 | **0** |
| trial 8 | 2 | 1 | **N** | 729 | **0** |
| trial 13 | 2 | 1 | **N** | 729 | **0** |

$$\boxed{\ \textbf{5/5 全部无解（穷尽枚举）}\ ✓\ }$$

### 0.3.77 **必要性证据清单（更新）**

| # | 实例 | $d$ | 方式 | 结果 |
|---|---|---|---|---|
| 1 | **c19** | 3 | **531,441 穷尽** | 0 |
| 2 | $n{=}4$ t=1 | 2 | 采样 420 | 0 |
| 3–7 | **5 个定向构造** | 2 | **各 729 穷尽** | **0** |

$$\boxed{\ \text{必要性}：\ \mathbf{7}\ \text{个实例（}\mathbf{6}\ \text{个穷尽）全部 NO}\ \checkmark\ }$$

$$\text{（从"仅 2 个"改善}; \text{机制仍未知，但证据显著加强）}$$

### 0.3.78 **本会话最终状态（第 27 次修正）**

| 类别 | 内容 |
|---|---|
| **已证（Lean 45 定理）** | $(A)\iff$分解$\iff$核条件；$K\subseteq\ker(CA^2)\Rightarrow(5b)$ 恒失败 |
| **已证（引理）** | $q\le d_{CA}\wedge\rho{=}q\Rightarrow(5b)$ 不可能 |
| **已证（枚举）** | c19 531,441 **无解**；t=7 **16,848 解（$\rho{=}2$）**；**5 个定向构造 729 无解** |
| **已证（充分性）** | $\alpha_0\in V\Rightarrow$ **YES**（构造 + pole placement）|
| **定律（4/4）** | $\operatorname{rank}(\text{解})=\text{obs}$ |
| **判据** | YES $\iff$ $\alpha_0\in V$：充分性**已证**；必要性 **7 实例（6 穷尽）全 NO** |
| **未证** | 必要性的**机制与证明** |

$$\boxed{\ \text{q1 仍未定；判据充分性已证、必要性有 6 个穷尽枚举支持}\ }$$

$$\Longrightarrow\ \textbf{若必要性成立}\ \Longrightarrow\ \textbf{判定多项式}\ \Longrightarrow\ \textbf{q1 为假}$$

### 0.3.79 🎯🎯🎯🎯🎯 **必要性机制找到：障碍在 (5a)**（`c43`, `c44`；见 [history/52](../52_session_conclusion.md) §7.24.70–7.24.72）

**诊断 ②**（`c44_rank_vs_5a.py`，按 $\operatorname{rank}(A_0)$ 分层）：

| 实例 | $\operatorname{rank}(A_0)=1$（$=$obs）| $\operatorname{rank}(A_0)=2$ |
|---|---|---|
| trial 0/1/7 | **9 个，过 (5a) 0（0%）** | 720 个，过 **720（100%）** |

$$\boxed{\ \alpha_0\notin V\ \text{时}\ \operatorname{rank}(A_0)=\text{obs}\ \text{的候选}\ \textbf{一律过不了}\ (5a)\quad(\mathbf{3/3})\ }$$

**机制**：
$$\text{解必须}\ \rho=\text{obs}\Rightarrow\operatorname{rank}A_0=\text{obs}=\dim V$$
$$(\text{5a})\Rightarrow A_1=\Lambda A_0\Rightarrow\gamma_0\in\operatorname{row}(A_0)=U\ (\dim=\text{obs})$$
$$\gamma_0=\alpha_0A'+\beta_0,\ \beta_0\in\operatorname{row}R\subseteq V,\ V\ \text{是}\ A'\text{-不变}\ ;\ \alpha_0\notin V$$
$$\Longrightarrow\ \text{mod}\ V：\ \bar\gamma_0=\bar\alpha_0\bar A'\ne0\ \text{而}\ U\ \text{容纳不下}\ \Longrightarrow\ \textbf{矛盾}\ \Longrightarrow\ \textbf{无解}$$

### 0.3.80 **本会话最终结论（第 28 次修正）**

| 类别 | 内容 |
|---|---|
| **Lean 45 定理** | $(A)\iff$分解$\iff$核条件；$K\subseteq\ker(CA^2)\Rightarrow(5b)$ 恒失败 |
| **引理** | $q\le d_{CA}\wedge\rho{=}q\Rightarrow(5b)$ 不可能 |
| **枚举** | c19 531,441 无解；t=7 16,848 解；5 个定向构造 729 无解 |
| **充分性** | $\alpha_0\in V\Rightarrow$ **YES**（构造 + pole placement）|
| **定律（4/4）** | $\operatorname{rank}(\text{解})=\text{obs}$ |
| **判据** | YES $\iff$ $\alpha_0\in V$ |
| **必要性（机制）** | **已找到**：障碍在 (5a) — $\gamma_0\notin\operatorname{row}(A_0)$ 的可达范围（3/3 分层验证）|
| **待做** | 把机制写成**严格证明** |

$$\boxed{\ \text{q1 的判据两侧都已"找到"；剩下的是把机制}\ \textbf{严格化}\ }$$

$$\Longrightarrow\ \textbf{若严格化成功}\ \Longrightarrow\ \textbf{判定多项式}\ \Longrightarrow\ \textbf{q1 为假}$$

---

## 0.3 🔑 各方向的"下一步"优先级（**已按本会话结论重组**）

> ⚠️ **下列 0.3.x 表格为会话中期记录，其优先级已被 §0.3.31（obs 判据）取代**。
> 现在唯一该做的是：**验证并证明 obs 判据**（见 §0.3.31）。

### 0.3.0 ⭐ **重组后的核心问题**（见 [history/52](../52_session_conclusion.md)）

$$\text{不是"情形 II 是否恒 NO"（已否定），而是：给定}\ (A,C,L_0)\ \text{与预算}\ q，\exists R\ (|R|{=}q)\ \text{使}\ (5a)\wedge(5b)\ \text{是否多项式可判？}$$

$$\textbf{关键}：q_0=\sum\eta_j\ \textbf{多项式可算}\ \Longrightarrow\ q<q_0\ \text{平凡 NO}\ ;\quad \text{只关心}\ q\ge q_0$$
$$\Longrightarrow\ \textbf{归结为}：q=q_0\ \text{时}\ (5b)\ \text{是否总可满足？}$$

### 0.3.1 ⭐⭐⭐ **两侧都已确立**（本会话最终状态）

| 侧 | 内容 | 依据 |
|---|---|---|
| **NO** | $K\subseteq\ker(CA^2)\wedge(A)\wedge H\ne0\Rightarrow$(S) 失败$\Rightarrow$(5b) 失败 | **Lean 已证**（`c6'_of_K_le_ker_CA2`）|
| **YES** | $K$ **非** $A$-不变 ⟹ (5a)∧(5b) **可成立** | $n\ge4$ 的**无穷族**（独立验证）|

$$\Longrightarrow\ \textbf{分界恰为}\ A\text{-不变性}\ ;\quad \textbf{YES 与 NO 实例都存在}\ \Longrightarrow\ \textbf{判定问题非平凡}\ \Longrightarrow\ \textbf{q1 是真问题}\ \checkmark$$

| 序 | 动作 | 理由 |
|---|---|---|
| **1** ⭐⭐⭐ | **复杂度归属**：在 $K$ 非不变区域，判定是否 NP-hard / 或找多项式算法 | 核心问题 |
| **2** ⭐⭐ | 找"$K$ 非不变但 $q{=}q_0$ 时 (5b) 不可满足"的实例 | 若不存在 ⟹ 判定可能平凡 |
| **3** ⭐ | **D6**（$q_0$ 的精确刻画/多项式可算性）| 现在是**关键** |
| **4** | 把"非退化平行 ⟹ $k{=}0$"Lean 化 | 干净可行 |
| **5** | **D7** | 图卡限定 |（**已按本轮发现重排**）

| 序 | 方向 | 动作 | 状态 |
|---|---|---|---|
| **1** ⭐⭐⭐ | **D3（退化分支）** | $\pi(L_0)=0$ 时 c6′：(5a) 已归约为 $\bar W$ 不变性、T5a 自动；**只剩 (5b)**。严格路线：`gen_A_system.py` 枚举 $\bar W$ + 子式插值 | **唯一开放问题** |
| **2** ⭐⭐ | **D6** | 与退化分支**汇合**：$k_{\min}=$ 最小 $\bar A$-不变子空间维数 —— 从这个角度重攻 $q_0$ 下界 | **新切入** |
| **3** | **D3** | 把"非退化平行 ⟹ $k{=}0$"**Lean 化** | 干净可行 |
| **4** | **D7** | 图卡限定 | |
| **5** | **D1/D2** | 归约 / 多项式算法 | 均处障碍 |

---

## 2. 各方向详情

### D1：归约（证 NP-hard）

| 项 | 内容 |
|---|---|
| **目标** | 从 1-in-3-SAT（或秩-1 仿射族判定）归约到 $\mathcal P$ |
| **为什么 1-in-3-SAT** | 3-SAT 的"至少一个"**不是**单个多项式方程；1-in-3-SAT 的子句是**全二次**的 ✓ |
| **已解决** | ✅ 表达力：二次形式的**线性张成满**（$42\times3$ 秩 $=3=D$）<br>✅ **非空洞判据**：$(A)$ 非空洞 $\iff \max\operatorname{rk}[W(\Theta);B]<d_C$；常用形式 $p+q_0+k<n$<br>✅ **归约方向澄清**：需 **目标方程 $\in(A)$-理想**（$\mathcal T\subseteq\mathcal I$）|
| **障碍** | 🔴 **Gröbner 在符号设定下 150/150 失败** ⟹ 理想成员性构造**计算上不可行**<br>🔴 $(\bar A,\bar B)$ 只有 $d_C^2+kd_C$ 个自由度，却要"指定"复杂理想 ⟹ **不可能任意指定** |
| **脚本** | `P_surjectivity.py`（满射性 ✓）、`P_inverse.py`（暴露空洞化）、`dir1_nonvacuous2.py`（判据）、`dir1_seq1b.py`（Gröbner 失败）、`dir1_direction_check.py`（方向）|
| **可能的绕法** | 改用**数值**方法探索理想结构；或换更"规整"的 NP-完全问题 |

### D2：多项式算法（证非 NP-hard）

| 项 | 内容 |
|---|---|
| **锚点** | ✅ $k=1$：$\Omega^\star_J=\{0\}$（**单点**）⟹ $\mathcal P$ **多项式**（真实装置，12 例 ✓）<br>机制：子式的**线性部分满秩** |
| **猜想 2.1（线性簇之并）** | ✗ **假**（Gröbner 基含二次元）|
| **猜想 2.2（低维 $\le2$）** | ✗ **假**（$\dim$ 可达 $m$）|
| **修正装置重测** | ⚠️ 抽象装置（任意 $\bar A$）与**真实装置**（`build_norm_T`）**不一致**<br>用真实装置：$n{=}6,s{=}4,k{=}2$ 给 $\dim\le4$；$n{=}7,s{=}5,k{=}2$ 给 $\dim=0$ ⟹ **无单纯规律** |
| **脚本** | `dir2_var_structure.py`、`dir2_guess22.py`、`dir2_dim.py`、`dir2_dim_real.py` |
| **状态** | 🔴 两条结构路线都失败；需重新审视 |

### D3：c6′（情形 II 平行）

| 项 | 内容 |
|---|---|
| **陈述** | 情形 II $\wedge$ **平行**（$\pi(L_0A)\parallel\pi(L_0)$）$\wedge(A)\wedge$T5a $\Longrightarrow$ **(S) 失败** |
| **意义** | c6′ + **T12** ⟹ 情形 II **恒 NO** ⟹ **分支 A 无硬度** |
| **数值证据** | **14/14 成立**（$q_0=2,3,4$；含 $CA^2=0$ 与一般 $A$）——用**完整的**平行判据 `rk[Π(L);Π(LA)]==1` ✓ |
| **Lean 状态** | 🟡 **条件式已机器验证**（`Theorems/C6.lean`：`c6'_conditional`）<br>假设含：$(A)$ 的**分解**、$N\hookrightarrow\ker C\sqcap\ker(CA)$、$\pi(\mathcal LA)=0$、$H\ne0$ |
| **唯一缺口** | 🔴 **D4：（A）⟹ 分解** |
| **脚本** | `batch_c6p_k.py`、`batch_r2.py`、`batch_generalA.py`、`batch_q4.py`、`verify_mechanism.py` |

### D4：（A）⟹ 分解（c6′ 的唯一缺口）

| 项 | 内容 |
|---|---|
| **要证** | $(A)\Longrightarrow \mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$ |
| **为什么关键** | `c6'_final`/`c6'_conditional` 把它当**假设**；补上 ⟹ c6′ 无条件 |
| **性质** | **纯线性代数，与 q1 内容无关** |
| **数值** | 50700 例、48220 个 $(A)$-点 **0 反例**（**仅小样本证据**）|
| **已机器验证的砖块** | `scripts/lean/Decomp2.lean`：`proj_exists`、`proj_ker_eq`、`section_mkQ_eq_proj`、`dW/dG/dH`、`diag_decomp`、`exists_extension_of_submodule`、`liftQ_mkQ_apply`（**7 条，0 error**）|
| **障碍** | 🔴 我的构造尝试（"取 $\Omega$ 的右逆"）**数学上不存在**：$\Omega$ 有右逆 $\iff\ker\Omega=0$ ✗<br>**正确形式已定**：只在 $\operatorname{range}\Omega$ 上取逆（恒可构造）|
| **状态** | 🔴 未完成；**已排除错误路线，正确形式已明确** |

### D5：B2（支 B 的 $\Omega^\star_J$）—— **本轮最完整的成果**

| 项 | 内容 |
|---|---|
| **结果 1** | $k=1$：$\Omega^\star_J=\{\Theta=0\}$（**单点**）；机制 = 子式的**线性部分满秩** ✓ |
| **结果 2** | $k\ge2$：$\Omega^\star_J$ **正维数**（零测但无限集）|
| **结果 3** | ⭐ **支 B 上 $(A)\wedge(S)$ 可成立**（**可复现见证**，见 `witness_branchB.json`）⟹ $\nu_{\min}=q_0$ |
| **结果 4** | ⭐ **$(A)\wedge(S)$ 可满足 $\iff\exists(A)$-点使 $\operatorname{rank}H<q_0$**（T5a 型）|
| **Lean** | ✅ `Theorems/B2.lean`（3 条定理，**0 error**，已并入主库）：$\Omega\subseteq\bigcap\ker f_i\wedge\bigcap\ker f_i=\{0\}\wedge 0\in\Omega\Rightarrow\Omega=\{0\}$ |
| **数值验证** | 15 实例 × 4 判据（Gröbner 基线性 / $\operatorname{rank}J=m$ / 高次 $\in$ 线性理想 / 整数格+坐标轴扫描）|
| **文档** | [history/29](../29_B2_result.md)、[30](../30_B2_proof_skeleton.md) |
| **未证** | 引理 A（$\operatorname{rank}J=m$，9/9 数值）、引理 B（高次 $\in$ 线性理想，6/6 数值）|

### D6–D8：三条"范围性"缺口

| # | 内容 | 状态 |
|---|---|---|
| **D6** | $q_0=\sum_j\eta_j$ 是最小 $(A)$-行数 | ⚠️ 只有 P1 Thm 2 一个来源；暴力/随机法**原理上无效**（薄集）；需**证明** |
| **D7** | 图卡限定：全部 $\Theta$-参数化结论仅在 $\operatorname{rank}(RN_CK)=k$ 内成立 | ⚠️ 未解决 |
| **D8** | T12 的验证 ✓（T12 本身已证）；但旧验证只覆盖"第一行不平行" | 🟡 需用**完整**平行判据重验 |

---

## 3. 关键资产（脚本/Lean/文档）

### 3.1 依赖库（**不要移动/改名**）

| 文件 | 用途 |
|---|---|
| `scripts/core/exact_count_thm7.py` | `rk / toF / p1 / condA / orb / mm / tr / inv / ker_basis / build_norm_T` |
| `scripts/core/linalg_exact.py` | **独立**的 `solve_exact / rank_exact / matmul`（**带维数断言**）|
| `scripts/core/linalg_q.py` | 独立精确线代层（**强制残差校验**）|
| `scripts/core/test_caseII_YES.py` | `p1`、`build_norm_T` 的**真实装置** |

### 3.2 可复现的**正面结果**

| 结果 | 复现命令 |
|---|---|
| 支 B 的 $(A)\wedge(S)$ 见证 | `python scripts/core/mainline_witness2.py` |
| B2 的 Gröbner 基线性性 | `python scripts/core/b2_structure.py` |
| 支 B 上 $(S)\iff$ 退化点 | `python scripts/core/mainline_structure.py` |
| c6′ 的批量验证 | `python scripts/core/batch_c6p_k.py` |
| $(S)$ 检验器健全性 | `python scripts/core/mainline_S_sanity.py` |

### 3.3 Lean 工程

```
~/WorkSpace/lean4/MyProof/         (WSL, Lean 4.35, mathlib 预编译)
├── MyProof/Foundations/Basic.lean     8 条 (F1/F3/F4/F4'/finrank_top/F5/T5a_core/T5a)
├── MyProof/Theorems/
│   ├── Pencil.lean                    T5', T2
│   ├── CaseII.lean                    T6
│   ├── Spectral.lean                  rank_comp_eq_iff, T5
│   ├── C6.lean                        c6′ 条件式（9 条）
│   ├── Decomp.lean                    F_eq_Lam_comp_H
│   └── B2.lean 🆕                     B2 组装（3 条）
└── lake build → Build completed successfully (18116 jobs)
```
**Windows 交付目录**：`scripts/lean/`（`Foundations/`、`Theorems/`、`B2.lean`、`Decomp2.lean` 等）

---

## 4. 🚨 通用禁区与教训（**跨方向**，最重要）

| # | 禁区/教训 | 出处 |
|---|---|---|
| **1** | **凡涉及 $(A)$ 的实验，必须用 `build_norm_T`（真实装置）** | [history/36](../36_two_routes.md) §7.3（本轮）|
| **2** | **"某实例上未找到" $\ne$ "不存在"**；必须报**样本量** | [history/32](../32_branchB_witness_found.md)（我因此误报过"支 B 无解"）|
| **3** | **随机扰动必须排除零扰动**（`randint(-1,1)/d` 会取 0）| [history/28](../28_problem_reading_and_branchB_counterexample.md) |
| **4** | **`mm` 不检查维数** ⟹ 必须自己断言 | 项目第 13 处；[history/30](../30_B2_proof_skeleton.md) |
| **5** | **"零测" $\ne$ "有限"** | [history/28](../28_problem_reading_and_branchB_counterexample.md) |
| **6** | **判据是秩等式，行列式只是实现** | [history/28](../28_problem_reading_and_branchB_counterexample.md) |
| **7** | **读文献先读 Definition，再读 Theorem** | 同上 |
| **8** | **薄集不能用采样**（真平行、$q_0$ 下界）| 项目禁区 |
| **9** | **不要用优化器"没找到"当"不存在"** | 项目第 18 处 |
| **10** | **不要用 `exact_count_thm7.solve` 展开解集**（零空间基可能不满足残差）| [history/27](../27_solver_bug_and_caseII_recheck.md) |
| **11** | **`PowerShell Set-Content` 会破坏中文/加 BOM** ⟹ 用 `write` 工具 | 项目环境节 |
| **12** | **"解数"必须先问"数的是什么"** | [history/28](../28_problem_reading_and_branchB_counterexample.md) |

---

## 5. 历史文档索引

| 文档 | 内容 |
|---|---|
| [FINAL.md](../../FINAL.md) | ⭐ **结论权威**（T1–T12、D1/D2、q3、6 猜想、20+ 撤回）|
| [CLAUDE.md](../../CLAUDE.md) | 工作记忆/恢复点 |
| [history/27](../27_solver_bug_and_caseII_recheck.md) | solver bug、情形 II 重查、**D4 的正确路线** |
| [history/28](../28_problem_reading_and_branchB_counterexample.md) | **命题读法三处修正**、我的反例自我推翻 |
| [history/29](../29_B2_result.md) | B2 主结果（Gröbner）|
| [history/30](../30_B2_proof_skeleton.md) | B2 证明骨架 + 引理 A/B |
| [history/31](../31_back_to_mainline.md) | 回主线的逻辑结构 |
| [history/32](../32_branchB_witness_found.md) | ⭐ **支 B 的 $(A)\wedge(S)$ 见证** |
| [history/33](../33_mainline_unification.md) | ⭐ **支 B ≡ 情形 II** 的归结 |
| [history/34](../34_P_final_form.md) | $\mathcal P$ 的最终形式 + 频率 |
| [history/35](../35_reduction_design.md) | 归约设计 + 三风险 |
| [history/36](../36_two_routes.md) | ⭐ **两条路线**（D1/D2）的完整记录 |

---

## 6. 建议的下一步（按价值）

| 序 | 方向 | 动作 | 理由 |
|---|---|---|---|
| **1** | **D4 → D3** | 证 $(\text{A})\Longrightarrow$ 分解（**正确形式已定**：在 $\operatorname{range}\Omega$ 上取逆）| c6′ 的唯一缺口；补上 ⟹ 情形 II 恒 NO ⟹ 分支 A 无硬度 |
| **2** | **D8** | 用**完整**平行判据重验 T12 | 便宜；消除验证口径疑点 |
| **3** | **D2** | 用**真实装置**做大样本结构分析 | 可能复活方向 2 |
| **4** | **D1** | 改用**数值**方法探索理想结构 | 绕开 Gröbner |
| **5** | **D6** | 走**证明**路线证 $q_0$ 下界 | 全项目单点依赖 |
