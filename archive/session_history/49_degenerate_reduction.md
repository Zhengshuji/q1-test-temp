# 49 — 退化分支的**结构归约**（唯一开放问题）

> 承接 [history/48](48_refutation_scope.md) §7–8。

---

## 0. 一句话

$$\boxed{\ \text{退化}\ (\pi(L_0)=0)\ \Longrightarrow\ \textbf{(5a) 归结为"}\bar W:=\mathrm{span}\{\pi(R)\}\ \text{的}\ \bar A\text{-不变性 + } \pi(L_0A)\in\bar W\text{"}}$$

$$\text{且}\ \textbf{T5a 自动成立}\ \checkmark\qquad\Longrightarrow\ \text{退化分支}\ \textbf{只剩 (5b)} ⚠️$$

---

## 1. ⭐ 结构归约（推导）

### 1.1 记号

$$\pi:\ V^*\to V^*/K^\perp\cong K^*,\quad K=\ker[C;CA],\quad K^\perp=\operatorname{row}[C;CA]$$
$$\textbf{关键}：\pi(\mu)=0\iff\mu\ \text{在}\ K\ \text{上为 0}\iff\mu\in\operatorname{row}[C;CA]\ ✓$$

### 1.2 退化的含义

$$\pi(L_0)=0\iff L_0\ \text{的每一行都在}\operatorname{row}[C;CA]\ \text{中}$$

$$\Longrightarrow\ \operatorname{row}[\mathcal L;C;CA]=\operatorname{row}[R;C;CA]\quad(\mathcal L=[L_0;R])$$
$$\Longrightarrow\ \pi\big(\operatorname{row}[\mathcal L;C;CA]\big)=\mathrm{span}\{\pi(r):r\ \text{为}\ R\ \text{的行}\}=:\bar W$$

### 1.3 **(5a) 的等价形式**（退化时）

$$(5a)\iff\operatorname{row}(\mathcal L A)\subseteq\operatorname{row}[\mathcal L;C;CA]$$
$$\iff\forall\ \text{行}\ \ell\ \text{of}\ \mathcal L:\ \pi(\ell A)\in\bar W$$

$$\text{而}\ \ell=L_0\ \text{的行给出}\ \pi(L_0A)\in\bar W\ ;\quad \ell=R\ \text{的行给出}\ \pi(rA)\in\bar W\ (r\ \text{为}\ R\ \text{的行})$$

$$\Longrightarrow\ \boxed{\ (5a)\iff \pi(L_0A)\in\bar W\ \wedge\ \bar W\bar A\subseteq\bar W\ \ (\text{当}\ A\ \text{不变时}\ \bar A=A'|_K)}$$

### 1.4 ⭐ **T5a 在退化时自动成立**

$$\mathrm{rank}(\mathcal L N_{CA})=\mathrm{rank}\big(\mathcal L|_K\big)\quad(\text{因}\ N_{CA}\ \text{参数化}\ K)$$
$$\mathcal L|_K\ \text{的行}：\ L_0|_K=0\ (\text{退化}\ ✓)\ ;\ R|_K\ \text{至多}\ k\ \text{行}$$
$$\Longrightarrow\ \mathrm{rank}\le k<r+k=q_0\ \Longrightarrow\ \boxed{\textbf{T5a 自动}\ ✓}$$

$$\Longrightarrow\ \text{退化分支}\ \textbf{不需要 T5a 假设}\ !\ \text{只剩}\ (5a)\ \text{与}\ (5b)$$

---

## 2. ⭐⭐ 与 D6 的联系（重要）

### 2.1 退化 + 不变 $A$ ⟹ 最小增广维数 = 最小 $A'$-不变子空间维数

$$\text{需}\ \bar W\ \text{含}\ u:=\pi(L_0A)\ \text{且}\ \bar A\text{-不变}\ ;\quad \dim\bar W\le k$$

$$\Longrightarrow\ k_{\min}=\dim\big(\text{含}\ u\ \text{的最小}\ \bar A\text{-不变子空间}\big)$$

$$\textbf{这正是}\ \text{D6 的模论公式（[history/41](41_D6_structure.md)）}\ \text{的同一对象}\ !$$

$$\text{（D6 中}\ u=\pi(L_0)\ ;\ \text{此处}\ u=\pi(L_0A)\ ——\ \text{退化时}\ \pi(L_0)=0\ \text{故"第一层"被跳过）}$$

### 2.2 由此得到的**新关系**

$$\text{项目的}\ q_0=\sum\eta_j\ \text{与}\ "\text{最小不变子空间维数}"\ \text{在退化分支上}\ \textbf{应当一致}$$
$$\text{—— 这给}\ q_0\ \text{的下界问题（D6）一个}\ \textbf{新的切入角度}\ ⚠️$$

### 2.3 (5b) 的地位

$$\text{(5b) 是}\ \textbf{铅笔条件}：\operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]=r_0\ \forall\lambda$$
$$\text{它比}"\bar W\ \text{不变}"\ \text{强得多（要求}\ \Lambda\ \text{的特征结构配合}\ H）$$

$$\Longrightarrow\ \text{退化分支的 c6′}\ \textbf{等价于}：\text{"最小不变增广 + (5b) 不可同时满足"} ⚠️$$

---

## 3. 当前状态的完整图景

$$\begin{array}{c|c|c}
\text{分支} & \text{c6′} & \text{依据}\\
\hline
\pi(L_0)\ne0\ (\textbf{非退化}) & \textbf{假} & \text{见证（13/13 独立复核）};\ \text{且}\ k=0\ (\textbf{定理})\\
\pi(L_0)=0,\ CA^2=0 & \text{14/14 支持} & \text{项目（对 (5b) 有效）}\\
\pi(L_0)=0,\ \text{非不变} & \text{12/12 未找到反例（弱）} & \text{本轮随机搜索（不决定性）}
\end{array}$$

$$\boxed{\ \textbf{唯一真正的开放问题}：\pi(L_0)=0\ (\text{退化})\ \text{时的 c6′}\ }$$

---

## 4. 严格化的明确路线

| 序 | 动作 | 说明 |
|---|---|---|
| **1** | 在退化情形把 (5a) 写成 $\bar W$ 的不变性问题 | 已推导（§1.3）|
| **2** | 用 `gen_A_system.py`（**构造性**）而非随机搜索枚举 $\bar W$ | 覆盖 (A)-解集，非采样 |
| **3** | 对每个 $\bar W$ 解 (5b)（子式插值，`attack_chart_rigorous.py` 的技术）| **严格**判定 |
| **4** | 若全部失败 ⟹ 退化 c6′ 成立 ⟹ **情形 II 恒 NO（补全）**| |

$$\text{（这是我建议的下一步，}\textbf{未做}）$$

---

## 5. 教训（本轮新增）

$$\boxed{\ \textbf{退化}\ \pi(L_0)=0\ \text{让 T5a 自动成立}\ ——\ \text{这是此前未注意到的结构性简化}\ ✓}$$
$$\boxed{\ \textbf{退化分支与 D6 的最小不变子空间是同一对象}\ ——\ \text{两个方向在此汇合}\ ⚠️}$$

---

## 6. 本轮产出

| 文件 | 内容 |
|---|---|
| **本文** | 退化分支的结构归约 + 与 D6 的联系 |
| `scripts/core/c6_degenerate_5b.py` | 退化 + 非变的 (5b) 测试（12/12 未找到，弱）|
| `scripts/core/c6_theorem_k0.py` | 定理"非退化平行 ⟹ $k{=}0$"验证（6/6）|
| `scripts/core/verify_witness_independent.py` | 见证独立复核（13/13）|
