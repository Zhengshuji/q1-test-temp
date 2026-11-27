# 50 — ⭐⭐⭐ **A-不变性正是分界线**（本会话的最终结论）

> 承接 [history/47](47_c6p_refuted.md)、[48](48_refutation_scope.md)、[49](49_degenerate_reduction.md)。

---

## 0. 一句话

$$\boxed{\
\begin{array}{ll}
\textbf{(1)} & K\ A\text{-不变}\ \big(K\subseteq\ker(CA^2)\big)\ \Longrightarrow\ \text{(S) 失败}\ \Longrightarrow\ \text{(5b) 失败}\quad(\textbf{Lean 已证})\ ✓\\[3pt]
\textbf{(2)} & K\ \textbf{非}\ A\text{-不变}\ \Longrightarrow\ \text{(5b)}\ \textbf{可以成立}\quad(\textbf{显式见证，13/13 独立复核})\ ✓
\end{array}}$$

$$\Longrightarrow\ \textbf{"A-不变性"就是 c6′ 成立与否的}\ \textbf{精确分界线}\ \checkmark$$

---

## 1. ⭐⭐ 相容性检查（**本会话最关键的验证**）

### 1.1 检查内容

$$\text{Lean 定理}\ \texttt{c6'\_of\_fact\_algclosed}：\ (A)\wedge A\text{-不变}\wedge H\ne0\Longrightarrow\text{(S) 失败}\Longrightarrow\text{(5b) 失败}$$
$$\text{见证}：\text{(5b)}\ \textbf{成立}$$

$$\text{若见证的}\ K\ \text{是}\ A\text{-不变}\ \Longrightarrow\ \textbf{直接矛盾}\ ✗$$

### 1.2 检查结果（`c6_witness_inv.py`，**列拼接判据**）

| 项 | 值 |
|---|---|
| $d_{CA}$ | 4 |
| $\operatorname{rank}N$ | 4 |
| $\operatorname{rank}[N\mid AN]$（**列拼接**）| **5** |
| **$K$ 是 $A$-不变？** | **False** ✓ |
| $CA^2\|_K = 0$？ | **False** ✓ |

$$\Longrightarrow\ \textbf{见证完全落在 Lean 定理的假设之外}\ \Longrightarrow\ \textbf{无矛盾}\ ✓✓$$

$$\textbf{两个结果}\ \textbf{互补且相容}\ \checkmark\quad\text{（一个说"不变⟹失败"，一个说"非不变⟹可行"）}$$

---

## 2. ⚠️ 我追查的一个**险情**（第 4 次 row/column 混淆）

### 2.1 错误推理（我一度以为能无条件证明 c6′）

$$(5a)\ \Longrightarrow\ \pi(\ell A)\in\operatorname{span}\{\pi(\ell')\}$$
$$\text{而}\ \pi(\ell)=\ell N_{CA}=H\ \text{的第 }i\ \text{行}$$
$$\text{我误把"这个 span"当成}\ \operatorname{im}H\ \Longrightarrow\ \operatorname{im}F\subseteq\operatorname{im}H\ \Longrightarrow\ \textbf{无条件 c6}'\ ✗$$

### 2.2 错在哪（`c6_rowcol.py` 的数值判定）

| 空间 | 见证实例 |
|---|---|
| $\operatorname{rowspace}(F)\subseteq\operatorname{rowspace}(H)$ | ✓（**自动**，由 $\Lambda H=F$ —— 无信息）|
| $\operatorname{colspace}(F)\subseteq\operatorname{colspace}(H)$ | **✗** |

$$\textbf{关键}：\operatorname{im}H=\text{列空间}，\text{而}\ \pi(\ell)\ \text{给出的是}\ \textbf{行空间}！$$

$$\text{若我的推理成立}\ \Longrightarrow\ \text{与见证矛盾}\ \Longrightarrow\ \textbf{必有错}\ ✓\ \text{（矛盾法定位了错误）}$$

### 2.3 教训（**第 4 次**！）

$$\boxed{\ \textbf{rowspace}\ne\textbf{colspace}\ ——\ \text{判断"包含"必须写清方向}\ }$$

$$\text{本轮}\ 4\ \text{次：① range vs kernel ② 列拼接 vs 行堆叠 ③ 重复 ④ rowspace vs colspace}$$

$$\text{这正是项目历史上第 13/20/21 处的}\ \textbf{同一类}\ \text{错误} ⚠️⚠️$$

---

## 3. ⭐⭐⭐ 最终的完整图景

$$\begin{array}{c|c|c}
K\ \text{的不变性} & k & \text{c6′（情形 II 平行 ⟹ NO）}\\
\hline
A\text{-不变}\ (K\subseteq\ker CA^2) & \text{任意} & \textbf{真}\quad(\textbf{Lean 已证})\ ✓\\
\text{非不变} & k=0 & \textbf{假}\quad(\text{见证，13/13})\ ✗\\
\text{非不变} & k\ge1 & \textbf{开放}\quad(12/12\ \text{未找到反例，弱证据})\ ⚠️
\end{array}$$

$$\text{补充}：\text{非退化平行}\ \Longrightarrow\ k=0\ (\textbf{定理})，\text{故}\ k\ge1\ \text{时平行}\ \Longrightarrow\ \text{退化}\ (\pi(L_0)=0)$$

---

## 4. 唯一剩余的开放问题（**精确**）

$$\textbf{非 }A\text{-不变}\ +\ \text{退化}\ (\pi(L_0)=0)\ +\ k\ge1\ \text{时，(5b) 是否可能成立？}$$

$$\text{已知}：\text{此类实例中}\ \textbf{T5a 自动成立}\ (\text{history/49 §1.4})，\text{故只剩}\ (5a)\ \text{与}\ (5b)$$

$$\text{已知}：(5a)\iff\bar W:=\operatorname{span}\{\pi(R)\}\ \text{含}\ \pi(L_0A)\ \text{且}\ \bar W\bar A\subseteq\bar W$$

$$\text{证据}：12/12\ \text{未找到}\ (5b)\ \text{解（随机搜索，}\textbf{不决定性}\ ⚠️)$$

$$\text{严格路线（未做）}：\texttt{gen\_A\_system.py}\ \text{枚举}\ \bar W\ +\ \text{子式插值}$$

---

## 5. 本会话的净成果（全部有效）

### 5.1 Lean（**45 条定理，18128 jobs，零 error**）

| 定理 | 内容 |
|---|---|
| `decomp_iff_rank` | $(A)\iff$ 分解（**秩-零化度，无对偶理论**）|
| `decomp_iff_ker` | 分解 $\iff\ker\Theta\le\ker(\mathcal LA)$ |
| `c6'_CA2_algclosed` | $CA^2=0$ ⟹ (S) 失败 |
| **`c6'_of_K_le_ker_CA2`** | **$K\subseteq\ker(CA^2)$ ⟹ (S) 失败（最弱条件）** |

### 5.2 数值/结构

| 结果 | 状态 |
|---|---|
| **非退化平行 ⟹ $k=0$** | ✅ 定理（6/6 验证）|
| **$k{=}0$ 时 c6′ 假** | ✅ 见证（13/13 独立复核）|
| **见证 $K$ 非不变 ⟹ 无矛盾** | ✅ 检查通过 |
| **退化时 T5a 自动** | ✅ 推导 |
| **退化 ⟺ D6 的最小不变子空间** | ✅ 识别 |
| 退化 + 非不变 + $k\ge1$ | ⚠️ 12/12 无返例（弱）|

### 5.3 结论性的一句话

$$\boxed{\ \text{c6′}\ \textbf{在}\ A\text{-不变时成立（已证）}，\text{在非不变且}\ k{=}0\ \textbf{时假（见反例）}，\text{只剩"非不变}+\ k\ge1\ \textbf{开放}\ }$$

---

## 6. 本轮产出

| 文件 | 内容 |
|---|---|
| **本文** | A-不变性 = 分界线 + 相容性检查 + 险情追查 |
| `scripts/core/c6_witness_inv.py` | ⭐ 相容性检查（见证 $K$ **非**不变）|
| `scripts/core/c6_rowcol.py` | ⭐ 险情定位（rowspace vs colspace）|
| `scripts/core/witness_caseII_parallel_YES.json` | 见证 |
| `scripts/core/verify_witness_independent.py` | 见证独立复核（13/13）|
