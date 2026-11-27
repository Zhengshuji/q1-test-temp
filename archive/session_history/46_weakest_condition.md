# 46 — c6′ 的**最弱可证条件** + 一般 $A$ 的诚实状态

> 承接 [history/45](45_c6p_complete.md)。

---

## 0. 一句话

$$\boxed{\ \textbf{找到并证明了 c6′ 的最弱条件}：\ K:=\ker C\sqcap\ker(CA)\ \subseteq\ \ker(CA^2)\ }$$
$$\boxed{\ \textbf{一般 }A\ \text{仍未证（也仍未找到反例）—— 这是主线的关键开放点}\ ⚠️}$$

$$\textbf{主库}\ \texttt{lake build}\ \to\ \textbf{Build completed successfully (18128 jobs)}\ ✓$$

---

## 1. ⭐ 最弱条件的推导（本轮的核心贡献）

### 1.1 分解阻碍

$$\text{机制需要}\ A(\operatorname{range}N)\subseteq\operatorname{range}N\quad(K=\operatorname{range}N=\ker C\sqcap\ker(CA))$$
$$\iff A(K)\subseteq\ker C\ \wedge\ A(K)\subseteq\ker(CA)$$

### 1.2 第一部分**自动成立** ✓

$$K\subseteq\ker(CA)\iff A(K)\subseteq\ker C\quad\text{（平凡）}$$

$$\Longrightarrow\ \textbf{新增定理}\ \texttt{maps\_inter\_ker\_into\_ker}：\forall v\in\ker C\sqcap\ker(CA),\ Av\in\ker C\ ✓$$

### 1.3 第二部分才是真正的条件

$$A(K)\subseteq\ker(CA)\iff K\subseteq\ker(CA^2)$$

$$\Longrightarrow\ \boxed{\ A\text{-不变}\iff K\subseteq\ker(CA^2)\ }$$

$$\text{而}\ CA^2=0\ \Longrightarrow\ \ker(CA^2)=V\supseteq K\ \text{（充分但}\textbf{强得多}）$$

### 1.4 新定理

$$\texttt{c6'\_of\_K\_le\_ker\_CA2}:\quad
(A)\wedge K\subseteq\ker(CA^2)\wedge H\ne0\ \Longrightarrow\ \exists\Lambda:\ F=\Lambda H\ \wedge\ \textbf{(S) 失败}$$

$$\text{（代数闭域；}\ K=\ker C\sqcap\ker(CA)\ \text{由参数化}\ N\ \text{给出}）$$

$$\textbf{这严格弱于}\ \texttt{c6'\_CA2\_algclosed}\ \text{（后者要求全局}\ CA^2=0\text{）}\ ✓$$

---

## 2. ⚠️ 一般 $A$：**仍未证**

### 2.1 $K\subseteq\ker(CA^2)$ **不自动成立**

**反例**（循环移位）：
$$C=e_1^*,\quad A=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}$$
$$\ker C=\operatorname{span}\{e_2,e_3\},\quad CA=e_2^*,\quad \ker(CA)=\operatorname{span}\{e_1,e_3\}$$
$$K=\operatorname{span}\{e_3\},\quad CA^2=e_3^*,\quad CA^2e_3=1\ne0$$
$$\Longrightarrow\ K\not\subseteq\ker(CA^2)\ \Longrightarrow\ A(K)\not\subseteq K\ ✗$$

### 2.2 一般 $A$ 下的**并行性反而容易**（重要洞察）

$$\text{给定}\ c，\ \ell(A N_j-cN_j)=0\ (\forall j)\ \text{是}\ \ell\ \text{的}\textbf{齐次线性条件}$$
$$\text{零空间维数}\ \ge\ n-d\ \ge\ 1\ \Longrightarrow\ \textbf{总能取到}\ \ell\ne0\ \text{使}\ \ell N\parallel \ell A N\ ✓$$

$$\Longrightarrow\ \textbf{"真平行是薄集"只在 }A\text{-不变时成立！一般 }A\ \text{时并行性不薄}\ ⚠️$$

### 2.3 但 (A) ∧ T5a 仍是强约束

$$\text{我尝试构造"非 }A\text{-不变 + 并行 + (A) + T5a"的实例}：$$
$$\textbf{60 万次随机搜索未找到 1 个}\ ✗\quad(\texttt{c6\_general\_A.py})$$

$$\text{瓶颈：}\ q_0=\eta\ge3\ \text{（因}\ \ell N\ne0\Rightarrow \ell\notin\operatorname{row}[C;CA]\Rightarrow\eta\ge3\text{）}，$$
$$\text{故需 3+ 行满足 (A) ∧ T5a —— 随机搜索命中率极低}\ ⚠️$$

$$\Longrightarrow\ \textbf{一般 }A\ \text{的状态}：\text{既未证、也未找到反例}\ \boxed{\textbf{开放}}$$

---

## 3. c6′ 的**七种形式**（全部在库中）

| 定理 | 结构假设 | 状态 |
|---|---|---|
| `c6'_conditional` | 分解（需显式 $\Lambda,G_0,G_1$）| ✓ |
| `c6'_of_A` | $(A)$ | ✓ |
| `c6'_of_A_rank_lt` | $(A)$ + $\operatorname{rank}F<\operatorname{rank}H$ | ✓ |
| `c6'_of_ker` | 核条件 | ✓ |
| `c6'_of_fact_algclosed` | $(A)$ + $A$-不变 | ✓ |
| **`c6'_of_K_le_ker_CA2`** 🆕 | $(A)$ + $K\subseteq\ker(CA^2)$ | ✓ **最弱** |
| `c6'_CA2_algclosed` | $(A)$ + $CA^2=0$ | ✓ 端到端 |

---

## 4. 累计资产（**45 条定理**）

$$\texttt{lake build}\ \to\ \textbf{18128 jobs，零 error}\ ✓$$

新增本轮：
| 定理 | 内容 |
|---|---|
| **`c6'_of_K_le_ker_CA2`** | c6′ 的最弱可证条件 |
| **`maps_inter_ker_into_ker`** | $A(\ker C\sqcap\ker CA)\subseteq\ker C$ 自动 |

---

## 5. 与主线的距离（诚实）

$$\underbrace{\text{情形 II 不平行}\Rightarrow\text{NO}}_{\textbf{T12}\ ✓}\ +
\underbrace{K\subseteq\ker(CA^2)\ \text{时平行}\Rightarrow\text{NO}}_{\textbf{c6′}\ ✓}$$
$$\Longrightarrow\ \text{情形 II 在}\ K\subseteq\ker(CA^2)\ \text{时恒 NO}\ \checkmark$$

$$\textbf{一般 }A：\text{开放}\ ⚠️\quad\text{（这决定分支 A 是否有硬度候选）}$$

---

## 6. 下一步（明确）

| 序 | 动作 | 说明 |
|---|---|---|
| **1** ⭐ | **构造**"非 $A$-不变 + 并行 + (A) + T5a"的实例 | 需避开随机搜索（薄集）|
| **2** | 若找到 ⟹ 测 (S)：**成立 ⟹ c6′ 假 ⟹ 分支 A 有硬度** ⭐⭐ | 主线关键 |
| **3** | 若 (S) 恒失败 ⟹ 找一般 $A$ 的替代机制 | |

### 6.1 构造法的思路

$$\text{用}\ \ell = aC + bCA + dCA^2\ \text{（使}\ \eta=2\text{，}q_0=2\text{）}，\text{则}$$
$$\ell|_K=d\,CA^2|_K\ \text{（}C,CA\text{ 在 }K\text{ 上为 0）}$$
$$\text{并行条件}：\ (b-cd)\,CA^2|_K+d\,CA^3|_K=0$$
$$\Longrightarrow\ \text{若}\ CA^3|_K=0\ \text{且}\ b=cd, d\ne0\ \text{即可}\ ✓$$
$$\text{而}\ CA^3|_K=0\ \text{比}\ CA^2|_K=0\ \textbf{更弱}\ \Longrightarrow\ \text{可构造"非不变但并行"的实例}\ ✓$$

$$\textbf{这是明确可行的下一步（未做）}$$
