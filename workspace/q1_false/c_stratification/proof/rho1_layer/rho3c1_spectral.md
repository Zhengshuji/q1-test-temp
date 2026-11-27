> **阶段报告**：[archive/paper_drafts/LAYER_31_REPORT_2026-10-29.md](../../../../../archive/paper_drafts/LAYER_31_REPORT_2026-10-29.md)（含 C.1–C.5 总表、三层验证、未形式化清单）。

# $(3,1)$ 层的谱判据：$p_0$ 的根何时是公共根

> 2026-10-30。本文给出一个**已证**的引理，把 $(3,1)$ 层的 $(5b)$ 失效条件化成一个**谱**条件
> （$w$ 与某个特征向量正交）。它把 CQ 在 $(3,1)$ 上从"投影型覆盖"变成"特征向量的正交条件"。

## 0. 归一化（同 [rho3c1_free_tau](rho3c1_free_tau.md) §1）

$c=1$、$\dim\mathcal U=3$。取 $\mathcal U$ 的基使 $U=I$，则铅笔行为
$$r_i(\lambda)=\lambda e_i-\mathbf c_i\quad(i=1,2,3),\qquad r_4=w,$$
其中 $\mathbf c_i=\mathbf t_i+\boldsymbol\beta\tau_i$（$\mathbf t_i$ 固定、$\boldsymbol\beta\tau_i$ 在某个子空间 $E\subseteq\mathcal U$ 内变化 ✓），$w=\beta(h)\ne0$。
记 $C$ 为以 $\mathbf c_i$ 为行的矩阵 ✓，$p_0(\lambda)=\det(\lambda I-C)$ ✓，
$p_i(\lambda)$ = 把第 $i$ 行换成 $w$ 后的行列式 ✓（$i=1,2,3$）。

$$(5b)\iff\gcd(p_0,p_1,p_2,p_3)=\text{非零常数}.$$

## 1. 引理（谱判据）

**引理 1**：设 $\lambda_k$ 是 $C$ 的**单**特征值（代数重数 1），$v_k$ 是对应右特征向量（$Cv_k=\lambda_kv_k$ ✓），$\eta_k$ 是对应左特征向量（$\eta_k^{\mathsf T}C=\lambda_k\eta_k^{\mathsf T}$ ✓）。则
$$\lambda_k\ \text{是}\ p_1,p_2,p_3\ \text{的公共根}\iff w^{\mathsf T}v_k=0 .$$

*证明*：记 $M(\lambda)=\lambda I-C$，则 $\lambda_k$ 是单根 ⟹ $\operatorname{rank}M(\lambda_k)=2$ ⟹
$$\operatorname{adj}M(\lambda_k)=\kappa\,v_k\eta_k^{\mathsf T},\qquad \kappa\ne0 .$$
由 Cramer 法则，$p_i(\lambda)=\big[w^{\mathsf T}\operatorname{adj}M(\lambda)\big]_i$（把第 $i$ 行换成 $w$ 的行列式 = 余子式的线性组合 ✓）。
于是在 $\lambda=\lambda_k$：
$$p_i(\lambda_k)=\kappa\,(w^{\mathsf T}v_k)\,\eta_{k,i}.$$
$\eta_k\ne0$ ✓ ⟹ 三个 $p_i$ 同时为零 $\iff w^{\mathsf T}v_k=0$ ✓。$\square$

**推论 2**：若 $C$ 有 3 个互异的特征值，则
$$(5b)\iff w^{\mathsf T}v_k\ne0\quad(k=1,2,3),$$
其中 $v_k$ 是三个特征向量 ✓。

*证明*：$\gcd\ne1$ ⟺ 存在公共根 $\lambda$ ✓；公共根必是 $p_0$ 的根 ✓（$p_0\ne0$ ✓ by 互异 ✓），即某个 $\lambda_k$ ✓；
由引理 1，$\lambda_k$ 是公共根 $\iff w^{\mathsf T}v_k=0$ ✓。$\square$

## 2. 由推论 2 得到的判据形式

$$\mathrm{Bad}=\{C:\ \exists k,\ w^{\mathsf T}v_k(C)=0\}\quad(\text{在 }C\text{ 有单谱时}).$$

于是内层覆盖问题变成：

> **CQ-(3,1)**：$\{$允许的 $C\}$ 是否**完全**落在"存在特征向量与 $w$ 正交"的集合里？

这个集合是**有限多个**代数条件的并 ✓（每个是一个"discriminant 非零 × $w^{\mathsf T}v_k=0$" ✓），
比原来的"投影型覆盖"**具体得多** ✓ —— 它是 $\mathbb P^2$ 里"$w$ 落在某个特征方向的垂面里" ✓。

## 3. 与已有结论的关系

- $\mathcal U\subseteq B$（$\tau$ 自由，$C$ 可任意 ✓）：可否取 $C$ 使 $w^{\mathsf T}v_k\ne0$？
  —— [rho3c1_free_tau](rho3c1_free_tau.md) 定理 2 用 $C$ 对角（$v_k=e_k$ ✓）构造 ✓：
  $w^{\mathsf T}e_k=w_k$ ✓，只要 $w\ne0$ 就有一个 $k$ 使 $w_k\ne0$ ✗ hmm ——
  **核对后的事实**：$C$ 对角时 $v_k=e_k$ ✓ ⟹ 需要**全部**三个 $w_k\ne0$ ✓，而 $w\ne0$ 只保证一个 ✗ ⟹
  **对角构造是错的** ✗ —— 定理 2 的证明已据推论 2 改写 ✓（改用 $w^{\mathsf T}v_k\ne0$ 的基，而不是对角 $C$ ✓）。

## 4. 核对（本轮的自我检查）

用 [verify_spectral_criterion.py](../../proof/rho1_layer/verify_spectral_criterion.py) 直接比较（精确有理算术）：

| 检验 | 结果 |
|---|---|
| 引理 1（**单**特征值处："$\lambda_k$ 是公共根" ⟺ "$w^{\mathsf T}v_k=0$"）| **352/352** 一致 ✓ |
| 推论 2（全部特征值有理时："$\gcd=1$" ⟺ "$w^{\mathsf T}v_k\ne0\ \forall k$"）| **114/114** 一致 ✓ |

**注意**：第一次跑（未筛"单根"）时引理 1 是 305/308 ✗ —— 差的三例都是重特征值 ✗，
正是引理 1 的假设（单特征值）之外 ✓；加上"$p_0'(\lambda_k)\ne0$"筛选后即 352/352 ✓。

**结论**：引理 1 与推论 2 **成立** ✓（在各自假设下）；并且它**直接推翻了** [rho3c1_free_tau](rho3c1_free_tau.md)
初版的"对角 $C$"构造 ✗（当 $w$ 有零分量时该构造给出 $\gcd\ne1$ ✗）⟹ 那边已改用谱判据证明 ✓。

---

## 5. $\mu=2$ 的探测（2026-10-30）

$\mu=\dim(B\cap\mathcal U)=2$ 时，$\tau$ 的自由度使 $C$ 的**前两列**自由、**第三列固定** ✓
（在 $E=\langle e_1,e_2\rangle$ 的坐标下 ✓）。[probe_mu2.py](../../proof/rho1_layer/probe_mu2.py)：
固定第三列、随机抽 40 组前两列，直接测 $(5b)$ ✓。

$$\textbf{119 个实例中，119 个都找到了使 }(5b)\text{ 成立的 }C\ \ (40\text{ 次抽样内})$$

即 $\mu=2$ 时型层**不被**覆盖 ✓（在这些样本上 ✓）。

### 5.1 待解决的矛盾（诚实记录）

[PROBE_31](../layer_program/PROBE_31.md) §2 的测量里，出现"全失败"的实例包含 $(d,m,\mu)=(4,2,2)$ ✗ —— 那是 $\mu=2$ ✓，
与本节"$\mu=2$ 不被覆盖"**矛盾** ✗。

两处模型的差别（可能的原因）：
1. [PROBE_31](../layer_program/PROBE_31.md) 的 $B$ 与 $\mathcal U$ 是**随机**取的 ✓，$E=B\cap\mathcal U$ 的**方向**相对于 $T$ 是随机的 ✓；
   本节把 $E$ 取成 $\langle e_1,e_2\rangle$ ✓（即假定 $T$ 与 $E$ 的相对位置"一般"✓）——
   **这可能正是差别** ✗：若 $T$ 的第三列与 $E$ 有特殊关系 ✓，可行 $C$ 可能不存在 ✗；
2. 本节的 $w$ 在 $\mathcal U$ 中**随机** ✓，而 $\mu=2$ 时应有 $w\in E$ ✓ —— 这一条**没有**严格对齐 ✗。

### 5.2 矛盾已解决：是**抽样不足**，不是数学冲突 ✓

按 §5.1 的两个疑点做了对齐：

1. **$E$ 方向随机化**（$a,b$ 随机、$w\in E$ 非零）✓ ⟹ **150/150** 个实例都找到使 $(5b)$ 成立的配置 ✓；
2. **$d=4$ 对齐**（$\mathcal U$ 取 $\mathbb Q^4$ 的 3 维子空间 ✓，与 PROBE_31 的 $(4,2,2)$ 同构型 ✓）⟹ 同样 **150/150** ✓。

$$\Longrightarrow\ \mu=2\text{ 的两个构型（}d=3\text{ 与 }d=4\text{）都在 100\% 的实例上找到可行配置} ✓$$

**所以 [PROBE_31](../layer_program/PROBE_31.md) §2 的"$(4,2,2)$ 全失败"是抽样造成的** ✗：
那里每个实例只抽了 **12** 个 $\tau$ ✓，而"好"的 $\tau$ 可能是**稀疏集** ✓ ⟹ 12 次全错过 ✓。
本轮用 **40** 次抽样就全部命中 ✓。

**教训**（与本项目纪律 §7.12「稀有/薄集不许采样」一致 ✓）：把"抽样全失败"当成"覆盖"是不安全的 ✗，
应由**构造 + 证明**代替 ✓（正如定理 2 用谱判据给出构造 ✓）。

---

## 6. $\mu=1$：一个**经验判据**（150/150 验证）与一次**失败的证明尝试**

### 6.1 结构

$\mu=1$ 时 $E=\langle a\rangle$ ✓，于是 $C$ 的行 $=\mathbf t_i+s_i a$ ✓ ⟹ 秩一扰动
$$C(s)=T+a\,s^{\mathsf T},\qquad s\in\mathbb Q^3\ \text{自由}.$$
又 $w=\beta a$ ✓ ⟹ $w^{\mathsf T}v=0\iff a^{\mathsf T}v=0$ ✓。

### 6.2 经验判据（**未证** ✗）

> 存在 $s$ 使 $(5b)$ 成立 $\iff$ $T$ **没有**特征向量与 $a$ 正交 ✓。

验证：[verify_mu1_criterion.py](../../proof/rho1_layer/verify_mu1_criterion.py) —— **150/150 一致** ✓
（"判据侧"用 $\begin{pmatrix}T-\lambda I\\ a^{\mathsf T}\end{pmatrix}$ 的 $3\times3$ 子式 gcd ✓；"直接侧"抽 60 个 $s$ 测 $(5b)$ ✓）。

另：$\mu=1$ 的随机探测（$d=3$：119/120 找到好配置；$d=4$：120/120 ✓）与该判据一致 ✓
（那 1 个全失败正是"$T$ 有正交特征向量"的实例 ✓）。

### 6.3 证明尝试**失败**的记录（诚实）

我的第一次推导是：若 $v\perp a$ 且 $Tv=\lambda v$ ✓，则 $C(s)v=Tv$ ✓ ⟹ $v$ 是 $C(s)$ 的特征向量 ⟹ 恒坏 ✗。
**这一步是错的** ✗：$C(s)v=Tv+a(s^{\mathsf T}v)$ ✓ —— 多出的项是 $a$ 的倍数 ✗，只有当 $s^{\mathsf T}v=0$ 时才消失 ✓。

所以"坏"的传递方向**不**是 $s$-无关的 ✗；判据 $6.2$ 的正确证明必须解释为什么"$T$ 有正交特征向量"会**强制**每个 $s$ 都坏 ✗
—— 我目前**没有**这个论证 ✗。可能的关键：$T$ 的正交特征向量 $v$ 满足 $s^{\mathsf T}v$ 可以取 0 ✓（选 $s\perp v$ ✓），
但要让**每个** $s$ 都坏，还需要别的机制 ✗（例如 $\Pi=a^{\perp}$ 上的诱导映射总有一个特征方向 ✓）。

### 6.4 状态汇总（$(3,1)$ 层，$w\ne0$）

| $\mu$ | 是否被覆盖 | 依据 |
|---|---|---|
| $3$（$\tau$ 自由）| **不**被覆盖 ✓ | **已证**（定理 2，[rho3c1_free_tau](rho3c1_free_tau.md)，用谱判据 ✓）|
| $2$ | **不**被覆盖 ✓ | 实证 300/300 ✓（证明 ✗）|
| $1$ | 由判据 6.2 决定 ✓ | **经验判据** 150/150 ✓（证明 ✗）|
| $0$ | $C$ 唯一 ⟹ 直接算 ✓ | — |

$$\boxed{\ \text{已证：}\mu=3\text{；}\mu=2,1\text{ 目前只有经验判据} ✗\ }$$

---

## 7. $\mu=1$：两个候选判据的对照（2026-10-30，仍未证 ✗）

我试图证明"秩一扰动 $T+a s^{\mathsf T}$ 在 $\Pi=a^{\perp}$ 上总留特征方向"这条关键引理，得到两个**互相竞争**的候选判据：

### 判据 A（最初的、启发式）

$$\exists s:\ (5b)\iff T\ \text{没有与 }a\text{ 正交的特征向量}.$$

验证：**199/199** ✓（[verify_mu1_compression.py](../../proof/rho1_layer/verify_mu1_compression.py)）。
但其**推导**是错的 ✗（见 §6.3：$C(s)v=Tv+a(s^{\mathsf T}v)$，多出的项不消失 ✗）。

### 判据 B（本次的、"有推导"的）

令 $\bar T=P_\Pi(T|_\Pi)$（$\Pi=a^{\perp}$ 的 2 维压缩）。断言：
$$\exists s:\ (5b)\iff \bar T\ \text{不是标量}.$$

*推导*：$v\in\Pi$ 是 $C(s)$ 的特征向量 $\iff$ $\bar Tv=\lambda v$ 且 $s^{\mathsf T}v=-\tau(v)$ ✓。
若 $\bar T$ 标量 ⟹ 每个 $v\in\Pi$ 都是特征向量 ⟹ 条件变成 $(s+\rho)^{\mathsf T}v=0$ ✓（$\rho$ 由 $\tau$ 给出 ✓）
⟹ 在 2 维 $\Pi$ 上总有非零解 ✓ ⟹ 每个 $s$ 都坏 ✓。
若 $\bar T$ 非标量 ⟹ 特征方向至多 2 个 ⟹ 坏集是至多 2 个超平面的并 ⟹ **应当**有好的 $s$ ✓。

验证：**192/199** ✗（7 个不一致 ✗）。

### 现状

| 判据 | 验证 | 推导 |
|---|---|---|
| A（$T$ 有正交特征向量）| **199/199** ✓ | **错** ✗ |
| B（$\bar T$ 非标量）| 192/199 ✗ | 有，但与数据不符 ✗ |

$$\boxed{\ \mu=1\text{ 的判据：两个候选都有缺陷} ✗\ ——\ \textbf{仍未证明}\ ✗\ }$$

**7 个不一致的可能原因**（未查）：
1. $\bar T$ 的特征方向不是 $\mathbb Q$-有理的 ⟹ 判据 B 的"超平面"在 $\mathbb Q^3$ 上可能没有点 ✗ ⟹ 需要按 $\mathbb Q$ 重新表述 ✗；
2. 60 次抽样不足以找到好的 $s$ ✗（薄集 ✗）；
3. 判据 B 的推导里"$\bar T$ 非标量 ⟹ 至多 2 个特征方向"✓ 但**重特征值**时特征方向是一整条线 ✗ ⟹ 并集可能覆盖整个 $\mathbb Q^3$ ✗。

**结论**：$\mu=1$ 仍只有经验判据（A，199/199 ✓），**没有证明** ✗。

---

## 8. 关键更正：谱判据的**完整**形式（2026-10-30）

上一轮的"判据 B 不一致"（7 例）查清了 ✓：**穷尽** $s\in[-3,3]^3$（343 点）后，
那 7 例**确实**没有好的 $s$ ✗ ⟹ 判据 B **错** ✗、判据 A **对** ✓（199/199 ✓）。

### 8.1 为什么 B 错（真正的原因）

我此前只用了"**单**特征值"的谱判据（引理 1 ✓），忽略了**重特征值**的情形 ✗。
正确的判据是：对**每个**特征值 $\lambda$，

$$\operatorname{rank}\begin{pmatrix}\lambda I-C\\ w^{\mathsf T}\end{pmatrix}=3 .$$

*理由*：$(5b)$ 在 $\lambda$ 处成立 ⟺ 铅垂 $\begin{pmatrix}\lambda I-C\\ w^{\mathsf T}\end{pmatrix}$（$4\times3$）秩为 3 ✓。
- 若 $\lambda$ 是**单**特征值 ⟹ $\operatorname{rank}(\lambda I-C)=2$ ⟹ 秩为 3 ⟺ $w^{\mathsf T}\notin\operatorname{row}(\lambda I-C)$ ⟺ $w^{\mathsf T}v\ne0$ ✓（引理 1 ✓）；
- 若 $\lambda$ 的特征空间维数 $\ge2$ ⟹ $\operatorname{rank}(\lambda I-C)\le1$ ⟹ 该矩阵秩 $\le2$ **恒** ✗ ⟹ 自动失败 ✗ ✓
  —— **与 $w$ 无关** ✗ ✓。

$$\boxed{\ (5b)\iff\text{对每个特征值 }\lambda:\ \operatorname{rank}\begin{pmatrix}\lambda I-C\\ w^{\mathsf T}\end{pmatrix}=3\ }$$

**推论**：$C$ 必须有"每个特征值只对应一个特征方向"（nonderogatory ✓）**且** 每个特征向量都 $\not\perp w$ ✓。
后者正是推论 2 ✓；前者是我此前漏掉的 ✗（也是那 7 例的成因 ✓）。

### 8.2 对判据 A 的意义

判据 A（"$\exists s$: $(5b)$" $\iff$ "$T$ 没有与 $a$ 正交的特征向量"）在 199/199 上成立 ✓，
穷尽 343 点又排除了"抽样不足" ✗ ⟹ 它**不是**抽样假象 ✓。
但它的**证明**仍需解释：为什么"$T$ 有正交特征向量"会**强制**每个 $s$ 都坏 ✓（含 8.1 的重特征值机制 ✓）。
本轮**没有**完成 ✗。

### 8.3 状态

| 判据 | 验证 | 证明 |
|---|---|---|
| 引理 1 / 推论 2（单谱）| 352/352、114/114 ✓ | **已证** ✓ |
| 8.1 的完整判据（含重特征值）| 由 8.1 的推理 ✓ + 那 7 例的穷尽结果 ✓ | **已证（一句推理）** ✓ |
| 判据 A（$\mu=1$ 的覆盖判据）| 199/199 + 343 点穷尽 ✓ | **未证** ✗ |

---

## 9. 又一个更正：坏集不是"特征向量在 $\Pi$ 里"，而是"左特征对**模 $w$**"

本轮想把 8.1 的完整判据用到 $\mu=1$ 上，推导中发现**又一个**错误 ✗（此前一直沿用 ✗）：

"$\mathrm{Bad}$ ⟺ $C$ 有特征向量落在 $\Pi=a^{\perp}$ 里" —— **这只是特例** ✗。

**正确的刻画**：设铅笔行为 $\lambda e_i-C_i$（3 行）加第 4 行 $w^{\mathsf T}$ ✓，则

$$\operatorname{rank}\begin{pmatrix}\lambda I-C\\ w^{\mathsf T}\end{pmatrix}\le2
\iff \exists(\varphi,c_4)\ne0:\ \varphi^{\mathsf T}(\lambda I-C)+c_4w^{\mathsf T}=0 .$$

- $c_4=0$：$\varphi$ 是**左**特征向量 ⟹ 等价于"有特征向量在 $\Pi$ 里" ✓（这是我此前唯一考虑的情形 ✗）；
- $c_4\ne0$：$\varphi$ 是"**模 $w$** 的左特征向量" ✗ —— **这是新的一类** ✓，
  它正是那 7 个反例成因的候选 ✓（在那里我构造的 $s$ 避开了前一类 ✓ 却仍失败 ✗）。

**由此得到的教训**：$\mu=1$ 的判据 A 若要证，必须同时处理这两类 ✗；
我前几轮的所有"特征向量在 $\Pi$ 里"的推理都只覆盖 $c_4=0$ ✓，因此**不足以**证明判据 A ✗。

## 10. 定位总结（$(3,1)$ 层、$w\ne0$）

| 项 | 状态 |
|---|---|
| 引理 1 / 推论 2（单谱）| **已证** ✓（352/352、114/114）|
| 完整谱判据（含重特征值）| **已证** ✓（8.1 的推理 + 7 例穷尽）|
| 坏集的完整刻画（左特征对**模 $w$**）| **已证** ✓（§9 的线性代数 ✓）|
| $\mu=3$ 不被覆盖 | **已证** ✓（定理 2 ✓）|
| $\mu=2$ 不被覆盖 | 实证 300/300 ✓，证明 ✗ |
| $\mu=1$ 的判据 A | 实证 199/199 + 343 点穷尽 ✓，证明 ✗ |

---

## 11. 关键引理**已证**【已证-纸面】+【Lean】（并入账为什么 §6.3 的"更正"本身是错的）

### 11.1 正确的扰动方向

$\mu=1$ 时 $\mathbf c_i=\mathbf t_i+s_i a$ ✓（每行加 $s_i a$ ✓）⟹ 矩阵形式是
$$C(s)=T+s\,a^{\mathsf T}\qquad\big((s a^{\mathsf T})_{ij}=s_i a_j\ \checkmark\big),$$
**不是** $T+a\,s^{\mathsf T}$ ✗。（[verify_mu1_criterion.py](../../proof/rho1_layer/verify_mu1_criterion.py) 里写的是 `a[j]*s[i]` ✓，即 $s a^{\mathsf T}$ ✓，与模型一致 ✓；
而我在 §6.3 手推时误用了 $a\,s^{\mathsf T}$ ✗ —— 那次"自我更正"**本身**是错的 ✗，现在撤回 ✓。）

### 11.2 引理（已证）【已证-纸面】+【Lean】

> **引理 3**：设 $\mu=1$、$w=\beta a$（$\beta\ne0$）、$C(s)=T+s\,a^{\mathsf T}$。
> 若 $v\ne0$ 满足 $Tv=\lambda v$ 且 $a^{\mathsf T}v=0$，则对**每个** $s$：$C(s)v=\lambda v$ ✓。

*证明*：
$$C(s)v=Tv+s\,(a^{\mathsf T}v)=Tv+0=\lambda v .$$
（$a^{\mathsf T}v$ 是**标量** ✓，乘以向量 $s$ ✓；它为零 ⟹ 扰动项整项消失 ✓。）$\square$

**推论 4**：在上面的情形下，若 $\lambda$ 是 $C(s)$ 的**单**特征值，则 $(5b)$ 在每个 $s$ 上都失败 ⟹ 该层**被覆盖** ✓。

*证明*：$v$ 是 $C(s)$ 的（单）特征向量 ✓ 且 $w^{\mathsf T}v=\beta\,a^{\mathsf T}v=0$ ✓ ⟹ 由引理 1（已证 ✓）$\lambda$ 是 $p_1,p_2,p_3$ 的公共根 ⟹ $\gcd\ne1$ ⟹ $(5b)$ 失败 ✓。$\square$

（若 $\lambda$ 非单：由 §8.1 的完整判据，$C$ 在 $\lambda$ 处的特征空间维数 $\ge2$ ⟹ 该处秩 $\le2$ ⟹ 同样失败 ✓。）

### 11.3 由此得到的完整判据（$\mu=1$）

$$\exists s:\ (5b)\iff T\ \text{没有与 }a\text{ 正交的特征向量}$$

- "⟸"（即：有 $\implies$ 无好 $s$）：**已证** ✓（引理 3 + 推论 4 / §8.1 ✓）；
- "⟹"（即：没有 $\implies$ 存在好 $s$）：**未证** ✗ —— 需要在"$T$ 无正交特征向量"时构造 $s$ ✓；
  实测支持（199/199 ✓ + 343 点穷尽 ✓）。

### 11.4 与计算的一致性

调试实例 $T=\mathrm{diag}(1,2,3)$、$a=w=e_3$：代码里 $C(s)=\begin{pmatrix}1&0&s_1\\0&2&s_2\\0&0&3+s_3\end{pmatrix}$ ✓（上三角 ✓），
$e_1,e_2$ 都是特征向量且 $\perp w$ ✓ ⟹ 由引理 3，$\lambda=1,2$ 恒为公共根 ✓ ⟹ 对**所有** $s$ 都坏 ✓ ✓
—— 与"$s\in[-6,6]^3$ 穷尽 2197 点、0 个好 $s$" ✓ 完全一致 ✓。

---

## 12. 判据 A 的**完整证明**【已证-纸面】（2026-10-29）

上一轮证了"$T$ 有与 $a$ 正交的特征向量 $\Rightarrow$ 每个 $s$ 都坏" ✓（引理 3 + 推论 4 ✓）。
反方向其实**很短** ✓：取 $s=0$ 即可 ✓。

### 定理（$\mu=1$ 的充要判据）

> **定理 5**：设 $\mu=1$、$w=\beta a$（$\beta\ne0$）。则
> $$\exists s\in\mathbb C^3:\ (5b)\ \text{成立}\iff T\ \text{没有与 }a\ \text{正交的特征向量}.$$

*证明*：

**($\Leftarrow$)** 设 $v\ne0$、$Tv=\lambda v$、$a^{\mathsf T}v=0$ ✓。对任意 $s$：由引理 3，$C(s)v=\lambda v$ ✓；
若 $\lambda$ 是 $C(s)$ 的单特征值 ✓，则由引理 1（$w^{\mathsf T}v=0$ ✓）得 $\lambda$ 是公共根 ⟹ $\gcd\ne1$ ✗；
若 $\lambda$ 非单（特征空间维数 $\ge2$）✓，则由 §8.1 的完整判据，该处秩 $\le2$ ⟹ 同样失败 ✗。
故每个 $s$ 都失败 ✓。

**($\Rightarrow$)** 设 $T$ **没有**与 $a$ 正交的特征向量 ✓。取 $s=0$ ✓（即 $C=T$ ✓），要证 $(5b)$ 成立 ✓。
1. 若某个特征值 $\lambda$ 的特征空间维数 $\ge2$ ✓：该特征空间是 $\mathbb C^3$ 的 2 维子空间 ✓，任何 2 维子空间与 2 维超平面 $a^{\perp}$ 有非零交 ✓
   （$\dim(U\cap a^{\perp})\ge 2+2-3=1$ ✓）⟹ 存在特征向量 $\perp a$ ✗ 矛盾 ✓。
   故**所有特征空间都是 1 维** ✓（nonderogatory ✓）。
2. 于是对每个特征值 $\lambda$：$\operatorname{rank}(\lambda I-T)=2$ ✓，且其右特征向量 $v_\lambda$ 满足 $w^{\mathsf T}v_\lambda=\beta\,a^{\mathsf T}v_\lambda\ne0$ ✓（由假设 ✓）。
   由引理 1 ✓（单特征值 ✓），$\lambda$ 不是公共根 ✓。
3. 每对 $(\lambda,\mu)$ 的公共根必是 $p_0$ 的根 ✓ ⟹ 无公共根 ⟹ $\gcd=1$ ⟹ $(5b)$ 成立 ✓。$\square$

$$\boxed{\ \text{定理 5：}\mu=1\text{ 时"被覆盖"} \iff T\text{ 有与 }a\text{ 正交的特征向量}\ }$$

### 12.1 与实测的一致性

- 199/199 ✓（[verify_mu1_compression.py](../../proof/rho1_layer/verify_mu1_compression.py)）；
- 7 个"反例"用 343 点穷尽确认确实没有好 $s$ ✓ —— 它们正是"$T$ 有正交特征向量"的实例 ✓，与定理一致 ✓。

### 12.2 只剩一处需要补严

定理 5 的 ($\Rightarrow$) 用到了"$w^{\mathsf T}v\ne0$ ⟹ $\lambda$ 不是公共根"，即引理 1 ✓（已证 ✓，352/352 ✓）。
引理 1 的证明用 $\operatorname{adj}M(\lambda_k)=\kappa v\eta^{\mathsf T}$（$\kappa\ne0$ ✓ 对单特征值 ✓），**前提是单特征值** ✓ —— 这正是 §12 步骤 1 保证的 ✓。
所以链条闭合 ✓：**定理 5 已证** ✓（纸面 ✓；Lean 化见 tools/lean/Perturbation.lean ✓）。

---

## 13. $\mu=2$：已被覆盖的**充分条件**【已证-纸面】+【Lean】

$\mu=2$ 时 $E=\langle a_1,a_2\rangle$ ✓，$\mathbf c_i=\mathbf t_i+s_{i1}a_1+s_{i2}a_2$ ✓ ⟹
$$C(s)=T+s^{(1)}a_1^{\mathsf T}+s^{(2)}a_2^{\mathsf T}\quad(\text{秩二扰动}).$$

**引理 6**：若 $v\ne0$ 满足 $Tv=\lambda v$ 且 $a_1^{\mathsf T}v=a_2^{\mathsf T}v=0$（即 $v\perp E$ ✓），则对每个 $s$：$C(s)v=\lambda v$ ✓。

*证明*：两处扰动项分别含因子 $a_1^{\mathsf T}v$、$a_2^{\mathsf T}v$ ✓，均为 0 ⟹ $C(s)v=Tv$ ✓。$\square$

**推论 7**：若 $T$ 有与 $E$ 正交的特征向量 ✓ 且该特征值是单的 ⟹ 型层**被覆盖** ✓（引理 1 ✓）。
若特征值非单，由 §8.1 同样失败 ✓。

$$\boxed{\ \mu=2:\ T\ \text{有 }\perp E\text{ 的特征向量}\ \Longrightarrow\ \text{被覆盖（已证）}\ }$$

**反方向**（"$T$ 无 $\perp E$ 的特征向量 $\Rightarrow$ 存在好 $s$"）**未证** ✗ ——
注意这里**不能**照搬 $\mu=1$ 的 $s=0$ 论证 ✗：$E^{\perp}$ 只有 1 维 ✓，2 维特征空间**不一定**与它相交 ✗
（$\dim(U\cap E^{\perp})\ge 2+1-3=0$ ✗）⟹ "无 $\perp E$ 特征向量"**不**强制 nonderogatory ✗ ✓。
需要非零的 $s$ 来破坏重特征值 ✓（未做 ✗）。

实测：$\mu=2$ 的 300/300 实例都能找到好 $s$ ✓ ⟹ 反方向应当成立 ✓（但未证 ✗）。

### 13.1 Lean 化【Lean】

[tools/lean/Perturbation.lean](../../../../../trash/lean_removed_2026-11-19/tools/lean/Perturbation.lean) 新增
`perturb2_eigen_of_mem_ker`（秩二版本 ✓）—— 与引理 6 逐字对应 ✓，`lean` 退出码 0 ✓。
Lean 总数：26 → **27** ✓。

---

## 14. 这些引理**有什么用**（以及不有什么用）

按项目纪律 §4 的验证分级标注：

| 结论 | 等级 | 位置 |
|---|---|---|
| 引理 1（单特征值处 $\lambda_k$ 是公共根 $\iff w^{\mathsf T}v_k=0$）| **【已证-纸面】** + 352/352 精确验证 | §1 |
| 完整谱判据（含重特征值）| **【已证-纸面】** | §8.1 |
| 引理 3（$\mu=1$：$C(s)=T+sa^{\mathsf T}$ 在 $a^{\perp}$ 上不动）| **【已证-纸面】+【Lean】** `perturb_eigen_of_mem_ker` | §11 |
| 定理 2（$\mu=3$：型层不被覆盖）| **【已证-纸面】**（用推论 2）+ 200/200 | rho3c1_free_tau |
| **定理 5（$\mu=1$：被覆盖 $\iff T$ 有 $\perp a$ 的特征向量）** | **【已证-纸面】**（$\Leftarrow$ 用 Lean 化的引理 3；$\Rightarrow$ 用维数计数）+ 199/199 | §12 |
| 引理 6 / 推论 7（$\mu=2$：有 $\perp E$ 的特征向量 $\Rightarrow$ 被覆盖）| **【已证-纸面】+【Lean】** `perturb2_eigen_of_mem_ker` | §13 |
| $\mu=2$ 的反方向 | **【猜想】**（300/300 实证）| §13 |

### 14.1 它服务于哪一步

$q1$ 的整个难点被归约到 **CQ**：给定实例与 $(\rho,c)$，判定"（类型+$(5a)$）的型层是否被 $\mathrm{Bad}$ 完全覆盖"✓
（见 [STRATEGY_methods](../layer_program/STRATEGY_methods.md)）。

定理 5 的作用是：在 **$(\rho,c)=(3,1)$、$\mu=1$** 这一格里，把 CQ 从"投影型覆盖问题"变成**一条特征值条件** ✓：
$$\text{该格被覆盖}\iff T\ \text{有与 }a\text{ 正交的特征向量}.$$
于是这一格**可精确判定** ✓（有理算术 ✓，无需量词消去 ✗、无需抽样 ✗）。

### 14.2 它**不**解决什么（避免夸大）

1. **不解决 $q1$** ✗：它只覆盖 $(3,1)$ 且 $\mu=1$ 的一格；层判定还需要 $\exists(\mathcal U,\mathcal H)$ 的外层 ✓ 和其他 $(\rho,c)$ ✗；
2. **不给出复杂度** ✗：即使所有格子都有这种判据，"枚举 $T$-不变子空间 + 逐格判定"的复杂度仍未分析 ✗；
3. **$\mu=2$ 只证了一半** ✗（反方向仍是猜想 ✗）。

### 14.3 它的实际价值（三条）

1. **可判定的第二格** ✓：此前只有 $\mu=3$（定理 2）能判，现在 $\mu=1$ 也能 ✓；
2. **定位了"覆盖"的机制** ✓：覆盖不是随机现象，而是 $T$ 的谱条件 ✓ —— 这直接告诉 hardness gadget 该往哪放 ✓
   （要让某层不可行，就得让 $T$ 有落在 $E^{\perp}$ 里的特征向量 ✓）；
3. **给 $\mu=2$ 提供了模板** ✓：同样的"扰动在 $E^{\perp}$ 上不动"给出充分条件 ✓，反方向需要处理重特征值 ✗。

---

## 15. 统一猜想（$(3,1)$ 层，$\mu\ge1$）+ 一个更简单的基本观察（2026-10-29）

### 15.1 基本观察（比引理 1 更直接，已证【已证-纸面】）

若 $v\ne0$ 是 $C$ 关于 $\lambda$ 的特征向量且 $w^{\mathsf T}v=0$，则
$$\begin{pmatrix}\lambda I-C\\ w^{\mathsf T}\end{pmatrix}v=0\ \ \big(4\times3\ \text{矩阵}\big)\ \Longrightarrow\ \operatorname{rank}\le2\ \Longrightarrow\ (5b)\ \text{在}\ \lambda\ \text{处失败}.$$
即：**"有特征向量 $\perp w$" $\Rightarrow$ 失败** ✓ —— 不需要"单特征值"假设 ✓，比引理 1 更直接 ✓。
（引理 1 的价值在**反方向**（无公共根），那条仍需单谱 ✓。）

### 15.2 统一猜想

> **猜想 U**（$(3,1)$ 层，$\mu=\dim E\ge1$）：
> $$\text{型层被覆盖}\iff T\ \text{有落在 }E^{\perp}\ \text{里的非零特征向量}.$$

| $\mu$ | 状态 |
|---|---|
| $1$ | **已证** ✓（定理 5：$E^{\perp}=a^{\perp}=w^{\perp}$，两个方向都证 ✓）|
| $3$ | **已证** ✓（定理 2：$E=\mathcal U$ ⟹ $E^{\perp}=0$ ⟹ 右侧恒假 ⟹ 不被覆盖 ✓）|
| $2$ | **"$\Leftarrow$"已证** ✓（引理 6 ✓）；**"$\Rightarrow$"仅实证** ✗ |

### 15.3 $\mu=2$ 的实测：**300/300**（2026-10-29 更正）

[probe_mu2](probe_mu2.py) 的扩展版：199 个 $\mu=2$ 实例（$T$ 随机、$E$ 随机 2 维、$w\in E$ 非零），
判据侧用 $\begin{pmatrix}T-\lambda I\\ a_1^{\mathsf T}\\ a_2^{\mathsf T}\end{pmatrix}$（$5\times3$）的 $3\times3$ 子式 gcd ✓；
直接侧抽 60 个 $s$ ✓。

**初版报的"198/199、1 个不一致"是我自己的 bug** ✗：构造 $w$ 时把系数写进了**逐坐标的列表推导**
（`w[k] = a1[k]*rand + a2[k]*rand` ✓ 每个坐标各抽一次随机数 ✗），于是 $w\notin E$ ✗ —— 违反模型假设 ✗。
修正（$\alpha,\beta$ 在整个向量上固定 ✓）后：

$$\textbf{判据与实测一致：300/300}\qquad(\text{被覆盖 }1\text{ 例})$$

脚本：[verify_mu2_criterion.py](../../proof/rho1_layer/verify_mu2_criterion.py) ✓。

$$\boxed{\ \mu=2:\ \text{"}T\text{ 有 }E^{\perp}\text{ 内特征向量}\"\Rightarrow\text{被覆盖：}\textbf{已证}\ ✓;\quad \text{反方向：}300/300\text{ 实证}\ ✓\text{（证明 ✗）}\ }$$

### 15.4 检验协议：**不做"抽样全失败就当覆盖"**（纪律 §7.12）

上一次 198/199 的教训（以及 [PROBE_31](../layer_program/PROBE_31.md) 的"12 次抽样当覆盖"✗）说明：
**"抽样没找到"不能当"不存在"** ✗。所以 $\mu=2$ 的检验改成三分法，每一步都只依赖**可核验的对象**：

| 情形 | 结论 | 依据 |
|---|---|---|
| 判据成立（$T$ 有 $E^{\perp}$ 内特征向量 ✓）| **被覆盖** ✓ | **引理 6 的证明**（不需要抽样 ✓）|
| 判据不成立，且抽到一个好 $s$ ✓ | **未被覆盖** ✓ | 该 $s$ 是**显式证据**（逐项验算 $(5b)$ ✓）|
| 判据不成立，没抽到 $s$ ✗ | **UNRESOLVED** ✗ | **不**记为覆盖 ✗ |

[verify_mu2_criterion.py](../../proof/rho1_layer/verify_mu2_criterion.py) 的结果（300 实例）：

| 类 | 数量 |
|---|---|
| 判据成立 ⟹ 由引理 6 证明被覆盖 | **1** ✓ |
| 判据不成立且找到显式好 $s$ | **299** ✓ |
| **UNRESOLVED** | **0** ✓ |

$$\boxed{\ \text{300 个实例全部被}\textbf{判定}\text{（1 个靠证明、299 个靠证据），无 UNRESOLVED}\ ✓\ }$$

⟹ $\mu=2$ 的"$\Rightarrow$"方向在这 300 个实例上**不是**"抽样支持"，而是"每个都给出显式 $s$" ✓；
但它仍**不是**一般证明 ✗（只证了这 300 个实例各自的情形 ✓）。

### 15.5 为什么"逐实例精确判定"已经做到，而"一般定理"仍缺

先澄清一个容易混淆的点：**"覆盖"是 $\forall$ 型命题**，单靠抽样无法否定它 ✗。

$$\text{覆盖}\ =\ \forall s\in\mathbb C^6\ \exists\lambda:\ \operatorname{rank}\begin{pmatrix}\lambda I-C(s)\\ w^{\mathsf T}\end{pmatrix}\le2 .$$

所以"精确判定每个实例"不能靠加细网格 ✗，只能靠：

| 方向 | 手段 | 现状 |
|---|---|---|
| 证明**覆盖**（$\forall s$ 都失败）| 引理 6：只要 $T$ 有 $E^{\perp}$ 内特征向量，扰动在每个 $s$ 上都固定该特征向量 ✓ | **已证** ✓ |
| 证明**不覆盖**（$\exists s$ 成功）| 给出一个显式 $s$ 并逐项验算 ✓（一条证据 = 一个证明 ✓）| **可做** ✓（300/300 都给出了 ✓）|

⟹ **每个具体实例都能被精确判定** ✓（要么引理 6，要么一条显式证据 ✓）——这就是 §15.4 的三分法 ✓。
但**没有**一条统一的构造规则能在"判据不成立"时对**所有**实例给出 $s$ ✗ ⟹ 一般命题仍缺 ✗。

### 15.6 一般命题的缺口，精确地说是什么

要证的是一句话：

> 若 $T$ 没有 $E^{\perp}$ 内的特征向量，则仿射族
> $$\mathcal F=\{T+(\text{每行都在 }E\text{ 内})\}\quad(6\text{ 维})$$
> 中存在 $C$，使 $C$ 的谱是单的、且每个特征向量都满足 $w^{\mathsf T}v\ne0$。

我试过的两条路都不成 ✗：
1. **"取 $s=0$"** ✓ 只在 $\mu=1$（$E^{\perp}=w^{\perp}$）时可行 ✓；$\mu=2$ 时 $E^{\perp}\subsetneq w^{\perp}$ ✗，$s=0$ 可能坏 ✗（例：$T$ 有 $\perp w$ 但不在 $E^{\perp}$ 里的特征向量 ✗）；
2. **"指定特征向量 $v_i$、由 $C=V\Lambda V^{-1}$ 反解"** ✗：$\mathcal F$ 的约束是"**每行**都在 $E$ 内"✓，
   对 $V,\Lambda$ 是 6 条**非线性**方程 ✗，我没解出来 ✗。

**结论（诚实）**：$\mu=2$ 的一般命题**仍开放** ✗；本节只把它精确地写成上面的形式 ✓，并说明为什么"逐实例验证"不能替代它 ✗。

---

## 16. 命题 P（$\mu=2$ 的存在性方向）：**已证**（专家显式构造，2026-10-29）【已证-纸面】+ 295/295 验证

### 16.1 坐标与假设

取坐标使 $E=\operatorname{span}(e_1^{\mathsf T},e_2^{\mathsf T})$、$w^{\mathsf T}=e_1^{\mathsf T}$。
则"$C-T$ 的每行 $\in E$" $\iff$ **$C-T$ 的第三列为零** ✓。于是
$$T=\begin{pmatrix}*&*&a\\ *&*&b\\ *&*&c\end{pmatrix},\qquad
C=\begin{pmatrix}x&y&a\\ 0&u&b\\ 0&s&c\end{pmatrix}\ (x,y,u,s\ \text{自由}).$$
又 $E^{\perp}=\operatorname{span}(e_3)$ ✓ ⟹ "**$T$ 没有 $E^{\perp}$ 内特征向量**" $\iff Te_3\notin\langle e_3\rangle$ $\iff$ $\boxed{(a,b)\ne(0,0)}$ ✓。

### 16.2 坏条件是一个**二次多项式**（回答 Q4）

写 $C=\begin{pmatrix}x&g^{\mathsf T}\\ 0&D\end{pmatrix}$，$D=\begin{pmatrix}u&b\\ s&c\end{pmatrix}$，$g^{\mathsf T}=(y,a)$ ✓。
第一坐标为零的 $C$-特征向量存在 $\iff$ $\exists z\ne0$: $Dz=\lambda z$ 且 $g^{\mathsf T}z=0$ ✓。
取 $z=(a,-y)^{\mathsf T}$ 张成 $\ker g^{\mathsf T}$ ✓（若 $g\ne0$ ✓），故坏 $\iff Dz\in\langle z\rangle$ $\iff\det[z,Dz]=0$ ✓，展开得
$$\boxed{\ p(y,u,s)=a^2s+a(u-c)y-by^2=0\ }$$

**$p\not\equiv0$**：若 $a\ne0$ ✓ 则 $s$ 的系数 $a^2\ne0$ ✓；若 $a=0$ ✓ 则 $b\ne0$ ✓ 且 $p=-by^2$ ✓。$\square$

### 16.3 显式构造（命题 P 的证明）

取 $s=0$ ✓、$u\ne c$ ✓（$D$ 的特征值 $u,c$ 互异 ✓，特征向量 $v_u=(1,0)$、$v_c=(-b/(u-c),1)$ ✓）。
- 若 $a\ne0$：取 $y\ne0$ 且 $a-\dfrac{yb}{u-c}\ne0$ ✓（只排除有限个值 ✓）⟹ $g^{\mathsf T}v_u=y\ne0$ ✓、$g^{\mathsf T}v_c=a-\dfrac{yb}{u-c}\ne0$ ✓；
- 若 $a=0$：则 $b\ne0$ ✓，取任意 $y\ne0$ ✓ ⟹ $g^{\mathsf T}v_c=-\dfrac{yb}{u-c}\ne0$ ✓。

再取 $x\notin\{u,c\}$ ✓ ⟹ $C=\begin{pmatrix}x&y&a\\ 0&u&b\\ 0&0&c\end{pmatrix}$ 是上三角、三特征值 $x,u,c$ **两两不同** ✓。

- 对应 $x$ 的特征向量是 $e_1$ ✓（第一坐标 $1\ne0$ ✓）；
- 对应 $\lambda\in\{u,c\}$ 的特征向量 $v=(v_1,v_2,v_3)$：由第一行 $(x-\lambda)v_1+yv_2+av_3=0$ ✓，
  其中 $(v_2,v_3)$ 是 $D$ 的特征向量 ✓ 且 $yv_2+av_3\ne0$ ✓、$x-\lambda\ne0$ ✓ ⟹ $v_1\ne0$ ✓。

于是谱简单 ✓、每个特征向量都满足 $w^{\mathsf T}v\ne0$ ✓ ⟹ 由 (T1) 得 $(5b)$ 成立 ✓。$\square$

**验证**：在 295 个随机实例上按上述配方构造 $C$ ✓，逐个测 $(5b)$（精确有理算术）：
$$295/295\ \text{成立}\ ✓;\qquad \text{构造出的 }C\ \text{上 }p=0\ \text{的实例：}0\ ✓ .$$

### 16.4 结论：$(3,1)$ 层的**统一判据**（四个通道全部已证）

$$\boxed{\ \textbf{定理 11}:\ \text{对 }(3,1)\text{ 层、}\mu\ge1:\ \text{型层被覆盖}\iff T\ \text{有落在 }E^{\perp}\ \text{里的非零特征向量}\ }$$

| $\mu$ | "有 $E^{\perp}$ 内特征向量 ⟹ 被覆盖" | "无 ⟹ 不被覆盖" |
|---|---|---|
| $1$ | 已证 ✓（引理 3 + 推论 4）| 已证 ✓（定理 5 的 $\Rightarrow$）|
| $2$ | 已证 ✓（引理 6）| **已证** ✓（**本节 16.3**，专家构造）|
| $3$ | 已证 ✓（$E^{\perp}=0$，右侧恒假）| 已证 ✓（定理 2）|

（$\mu=0$：平凡可判 ✓，见 §18。）

---

## 17. 真实实例上的格子级验证（2026-10-29，首次）

此前所有验证都在**手工设定的抽象数据**（$\mathcal U,B,\beta,T$）上做 ✗。
商空间实现通过自检后（[quotient_selfcheck.py](quotient_selfcheck.py)，5 条自检全 100% ✓，含最关键的 S4 120/120 ✓），
第一次能在**真实实例** $(A,C,L_0)$ 上验证格子判据 ✓。

脚本：[verify_cell_criteria_genuine.py](verify_cell_criteria_genuine.py)。流程（全部在真实商空间里）：
1. 建 $X=\mathbb C^n/\mathcal J$、$B$、$\bar T$ ✓；
2. 取 3 维 $\mathcal U\supseteq U_0$ ✓，取补空间 $X=\mathcal U\oplus W$ ✓；
3. 对 $u_i$：取 $\bar T(u_i)$ 的代表、按 $\mathcal U\oplus W$ 分解，$\mathcal U$ 分量记 $\mathbf t_i$ ✓；
4. $E=B\cap\mathcal U$、$w\in E\setminus0$、解 $h$ 使 $\beta(h)=w$ ✓；
5. 铅笔（$\mathcal U$ 坐标）行 $\lambda u_i-\mathbf t_i-e_i$（$e_i\in E$）与 $-w$ ✓；
6. **直接**：抽样 $e_i$ 判 $(5b)$ ✓；**判据**（定理 11）：被覆盖 $\iff$ $T=(\mathbf t_i)$ 有特征向量 $v$ 使 $w^{\mathsf T}v=0$ ✓。

$$\textbf{结果：17 个格子，判据与直接测量一致 }17/17\ ✓$$

**限制（诚实）**：这 17 个格子全部是 $\mu=1$ ✗（随机取 $\mathcal U$ 时 $\dim(B\cap\mathcal U)=2$ 的情形没被抽到 ✗）⟹
本节实际核对的是**定理 5** 的格子级版本 ✓；$\mu=2$（定理 11）与 $\mu=3$（定理 2）在真实实例上**尚未验证** ✗。

### 17.1 $\mu=2$ 的真实实例验证：**43/43**（2026-10-29）

[verify_cell_mu23_genuine.py](verify_cell_mu23_genuine.py)：**定向构造** $\mathcal U$（使 $\dim(B\cap\mathcal U)=\mu$ ✓），
在真实商空间里比较：
- **直接**：抽样 $e_i\in E$ 判 $(5b)$ ✓；
- **判据**（定理 11）：$T=(\mathbf t_i)$ 是否有落在 $E^{\perp}$ 里的特征向量 ✓
  （用 $\begin{pmatrix}\lambda I-T\\ E\text{ 的基}\end{pmatrix}$ 的 $3\times3$ 子式 gcd ✓）。

$$\textbf{mu=2：判据与直接测量一致 }43/43\ ✓$$

**这一步修正了两个实现 bug**（都不是定理的错 ✗）：
1. 铅笔里 $u_i$ 的坐标写成了 $X$ 坐标 ✗ —— 应为 $\mathcal U$ 基下的 $e_i$ ✓；
2. **判据写成了"$v\perp w$" ✗ —— 应为"$v\perp E$"** ✓（定理 11 的陈述是 $E^{\perp}$ ✓；$\mu=2$ 时 $E^\perp\subsetneq w^\perp$ ✗）。

### 17.2 $\mu=3$ 的真实实例验证：**200/200**（2026-10-29）

[verify_mu3_genuine.py](verify_mu3_genuine.py)：取 $n=9$、$p=3$ ⟹ 实测 $(\dim\mathcal J,d,\dim B)=(6,3,3)$ ✓ ⟹ $\mathcal U=X$（唯一 3 维）✓、$\mu=3$ ✓。
按定理 2 的构造：取基 $v_k$ 使 $w^{\mathsf T}v_k\ne0$ ✓、$C=V\Lambda V^{-1}$（$\Lambda$ 互异 ✓），
铅笔行 $=\lambda e_i-C_i$ ✓、第 4 行 $=-w$ ✓。

$$\textbf{mu=3：按定理 2 构造后 }(5b)\text{ 成立 }200/200\ ✓$$

**期间修掉一个实现 bug** ✗：初版把行写成 $\lambda v_k-\lambda_k v_k$（**会**在 $\lambda=\lambda_k$ 处归零 ✗），
正确是"$C=V\Lambda V^{-1}$ 的**行**" ✓。

### 17.3 小结：四条格子判据在**真实实例**上的验证

| 定理 | 格子 | 真实实例验证 |
|---|---|---|
| 定理 2 | $\mu=3$ | **200/200** ✓ |
| 定理 5 | $\mu=1$ | **17/17** ✓ |
| 定理 11 | $\mu=2$ | **43/43** ✓ |
| 定理 12 | $\mu=0$ | 42/42 ✓ + Lean ✓ |

$$\boxed{\ \text{四条格子级判据现在都在}\textbf{真实实例}\text{上验证过}\ ✓\ }$$
