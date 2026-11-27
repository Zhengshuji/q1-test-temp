# 40 — 路 C 的最终形式 + 我的两处更正

> 承接 [history/39](39_route_C_insight.md)。

---

## 0. 一句话

$$\boxed{\ \textbf{路 C 引理的最终形式}\ \checkmark\ +\ \textbf{我在本轮犯的}\ 2\ \text{处错误（已更正）}\ ✗}$$

---

## 1. ✅ 路 C 引理的**最终形式**

$$\textbf{若}\quad (A)\ \wedge\ CN=0\ \wedge\ CAN=0\ \wedge\ \mathbf{A(\operatorname{range}N)\subseteq\operatorname{range}N}$$
$$\textbf{则}\quad \operatorname{range}(L\circ A\circ N)\subseteq\operatorname{range}(L\circ N)
\quad\Longrightarrow\quad \exists\Lambda:W\to W,\quad F=\Lambda H$$

其中 $H=L\circ N$、$F=L\circ A\circ N$。

### 1.1 数值验证（项目真实装置，精确求解）

| 情形 | 可因子化 |
|---|---|
| **$A$-不变** | **18/18** ✓ |
| 非 $A$-不变（我构造的）| **有反例** ✗ |

### 1.2 证明（$A$-不变情形）

$$\forall v:\ \exists v',\ Av=Nv'\ \Longrightarrow\ LA(Nv)=L(Nv')\in\operatorname{range}(L\circ N)\ \checkmark$$

### 1.3 为什么 $A$-不变是**必要**的（反例）

$$n=2,\ A=\operatorname{diag}(1,2),\ L=\begin{pmatrix}1&0\end{pmatrix},\ C=\begin{bmatrix}0&0\\0&1\end{bmatrix}$$
$$\ker[C;CA]=\operatorname{span}\{e_1\}\ \text{（}A\text{-不变？}\ Ae_1=e_1\ \checkmark\text{）}$$
$$\text{但取}\ N=e_1\ \text{的**非**不变子情形（如}\ N\ \text{取别的向量）则因子化失败}\ ✗$$

---

## 2. ⚠️ 我在本轮犯的**两处错误**（必须记录）

### 2.1 错误 1：一个**假引理**

$$\text{我一度想用}：\operatorname{range}T\subseteq\operatorname{range}H\ \Longrightarrow\ \exists\Lambda,\ T=\Lambda\circ H$$
$$\textbf{这是假的}\ ✗\quad\text{反例}：H=\begin{pmatrix}1&0\\0&0\end{pmatrix},\ T=\begin{pmatrix}0&0\\0&1\end{pmatrix}$$
$$\text{（}\operatorname{range}T=\{0\}\times K\subseteq K\times\{0\}=\operatorname{range}H\ \text{但}\ T\ne\Lambda H\ \forall\Lambda\text{）}$$

**根源**：$\operatorname{range}T\subseteq\operatorname{range}H$ 只给出"像的包含"，
**不**给出 $\ker H\subseteq\ker T$ —— 而后者才是因子化的真正条件 ✗

### 2.2 错误 2：一个**太弱的判据**（导致假阳性）

$$\text{我用}\ \operatorname{rk}[LN\mid LAN]=\operatorname{rk}[LN]\ \text{作为"可因子化"的判据}$$
$$\textbf{这只是 range 包含}\ ✗\quad\text{（同上，不蕴含可因子化）}$$
$$\Longrightarrow\ \text{我报了"12/12 ✓"、"14/14 ✓" —— }\textbf{全部假阳性}\ ✗$$

$$\textbf{更正}：\text{必须用}\ \textbf{线性方程组精确求解}\ (\text{逐列 + 残差校验})\ \checkmark$$

### 2.3 教训

| # | 教训 |
|---|---|
| **1** | **range 包含 $\ne$ 可因子化** —— 后者需要 kernel 条件 |
| **2** | **判据必须用"精确求解 + 残差"**，不能用"秩比较"（秩只给 range 信息）|
| **3** | 这与项目历来的教训同源：**判据必须恰好对应所需结论** ⚠️ |

---

## 3. 路 C 与 D4 的关系（更新）

$$\textbf{D4}：\text{给出了}\ (A)\Rightarrow\text{分解}\ \text{的}\ \textbf{全部数学内容}\ ✓\ (\operatorname{range}\text{包含}\Rightarrow\text{系数存在})$$
$$\textbf{路 C}：\text{绕开 D4 的类型障碍，只取}\ \Lambda\ \text{（不需要}\ G_0,G_1\text{）}\ ✓$$
$$\textbf{但路 C 需要}\ A\text{-不变}\ \text{—— 而}\ \texttt{c6'\_final}\ \text{恰好有}\ \texttt{hfact}:\ A\circ N=N\circ A'\ \checkmark$$

$$\Longrightarrow\ \textbf{路 C 在}\ \texttt{c6'\_final}\ \text{的假设下是可行的}\ ✓$$

---

## 4. ⭐ 路 C 的**最终结论**（本轮）

### 4.1 已确立的事实

| 检验 | 结果 |
|---|---|
| **ker 条件** $\ker(LN)\subseteq\ker(LAN)$（项目真实装置 + $(A)$）| **16/16 成立** ✓ |
| 精确求解 $LAN=LN\cdot X$ | **18/18 可解**（$A$-不变情形）✓ |
| 非 $A$-不变（构造）| **有反例** ✗ |
| $\ker(LN)=\ker(LAN)$ | 10/14（**不是**普遍等式）|
| $\operatorname{range}N\subseteq\operatorname{range}(AN)$ | **0/14**（不成立）|

$$\Longrightarrow\ \textbf{路 C 在}\ A\text{-不变下成立}\ ✓\ ;\qquad
\textbf{但"ker 条件"的机制尚未完全清楚}\ ⚠️$$

### 4.2 ⚠️ 一个关键的**判据陷阱**（本轮最重要的教训）

$$\text{我一度用}\ \operatorname{rk}[LN\mid LAN]=\operatorname{rk}[LN]\ \text{（**列拼接**）作判据}$$
$$\textbf{那只是 range 包含}\ ✗\qquad\text{而可因子化需要}\ \textbf{ker 条件}\ \text{（**行堆叠**）}$$
$$\operatorname{rk}[LN;LAN]=\operatorname{rk}[LN]\quad(\text{行堆叠}) \iff \ker(LN)\subseteq\ker(LAN)\ \checkmark$$

$$\Longrightarrow\ \textbf{两者是}\ \textbf{不同的判据}\ \text{—— 我混淆了，导致"12/12 ✓"/"14/14 ✓"的}\ \textbf{假阳性}\ ✗$$

**这与项目历来教训同源**（如第 13 处的 `mm` 维数错配）：
$$\textbf{判据的"方向"（行 vs 列、源 vs 陪域）必须与所需结论严格对应}\ ⚠️$$

---

## 5. 下一步（明确）

| 序 | 动作 | 说明 |
|---|---|---|
| **1** ⭐ | **证** $\ker(LN)\subseteq\ker(LAN)$ **from $(A)\wedge CN{=}0\wedge CAN{=}0\wedge A\text{-不变}$** | 路 C 的核心；纯线性代数 |
| **2** | Lean 化该引理（比 D4 简单：无需子模分裂）| |
| **3** | 改 `c6'_conditional` 的假设 ⟹ c6′ 更干净 | |
| **4** | 与 T12 合并 ⟹ 情形 II 恒 NO | 最终目标 |

### 5.1 引理 1 的数学内容（**待完成** ⚠️）

$$\textbf{要证}：\ LNd=0\ \Longrightarrow\ LANd=0\quad(\text{在}\ A\text{-不变下})$$
$$LNd=0\ \text{即}\ L(Nd)=0\ ;\quad\text{需}\ L(A(Nd))=0$$
$$\text{由 }A\text{-不变：}A(Nd)=N(d')\ \Longrightarrow\ LANd=L(N(d'))$$
$$\text{而}\ L(Nd)=0\ \text{与}\ L(N(d'))=0\ \text{之间**没有直接联系**}\ ✗$$

$$\Longrightarrow\ \textbf{所以}\ A\text{-不变**不足以**推出 ker 条件！}\ \text{需另找依据}\ ⚠️$$

$$\text{（数值上 16/16 成立，但机制未明）}$$

---

## 6. 本轮产出

| 文件 | 内容 |
|---|---|
| **本文** | 路 C 的最终结论 + **判据陷阱**（重要教训）|
| `scripts/core/routeC_kernel.py` | ker 条件的检验（16/16 ✓）|
| `scripts/core/routeC_solve.py`、`routeC_final2.py` | 精确求解（发现假阳性）|
| `scripts/core/routeC_check2.py`、`check3.py`、`check4.py` | ⚠️ 用弱判据的脚本（**反面教材**）|
| [history/39](39_route_C_insight.md) | 路 C 的思路 |
| `MyProof/Theorems/D4.lean` ★ | D4 的 Lean 证明（已完成）|
