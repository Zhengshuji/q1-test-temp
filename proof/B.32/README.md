# B.32 · 终端唯一区：$r_1\le p+1\Rightarrow q_{\min}=n-p$（假设 $(C,A)$ 可观测，故 $n_0=n$）

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.32` 条目（§0.1 归并表）。

## 命题

**B.32（a）〔原 B.27〕（Class I 的 $q_{\min}=n-1$ —— 定理，不再是猜想）** 设 $p=r=1$（$C=c^{\mathsf T}$、$L_0=\ell^{\mathsf T}$）、
$(c,A)$ **可观测**、$\operatorname{rank}[c;\ell]=2$（保证终阶可行；**不需要** $(\ell,A)$ 可观测，专家 2026-11-05 §2）、$\mathcal L$ 可容许（$(5a)$、$\operatorname{rank}[C;\mathcal L]=1+q$、含 $L_0$）。若 $1\le q\le n-2$，则
$$(5b)\ \text{失败};\qquad\text{而 } q=n-1 \text{ 可行（B.18b）}\ \Longrightarrow\ \boxed{q_{\min}=n-1 .}$$

## 纸面证明

*证明*：令 $\mathcal Z=\ker[C;\mathcal L]$、$\mathcal V:=\mathcal Z^\perp$。因 $\mathcal L$ 的行与 $c$ 都在 $\mathcal Z^\perp$ 里，
且 $\operatorname{rank}[C;\mathcal L]=1+q$，故
$$\mathcal V=\operatorname{row}[\mathcal L;c],\qquad \dim\mathcal V=q+1 .$$

$h=\operatorname{rank}[\mathcal L;CA;C]=\dim\bigl(\operatorname{row}[\mathcal L;c]+\langle cA\rangle\bigr)=\dim(\mathcal V+\langle cA\rangle)$，
故 $h\in\{q+1,q+2\}$，且 $h=q+2\iff cA\notin\mathcal V$。

* **情形 A（$cA\notin\mathcal V$）**：$h=q+2=q+r_1$，由 **B.22**（等号障碍）得 $(5b)$ 失败 ✓。
* **情形 B（$cA\in\mathcal V$）**：由 $(5a)$ 与 $\operatorname{row}[\mathcal L;c]=\mathcal V$ 得
  $$\operatorname{row}(\mathcal LA)\subseteq\operatorname{row}[\mathcal L;c;cA]=\mathcal V+\langle cA\rangle=\mathcal V ;$$
  又 $\mathcal V=\operatorname{row}\mathcal L\oplus\langle c\rangle$，故 $\mathcal VA\subseteq\operatorname{row}(\mathcal LA)+\langle cA\rangle\subseteq\mathcal V$，
  即 $\mathcal V$ 是 $A$-不变子空间。于是 $c\in\mathcal V$ 与归纳给出 $cA^k\in\mathcal V$ 对一切 $k\ge0$；
  由 $(c,A)$ 可观测，$\operatorname{span}\{c,cA,\dots\}=\mathbb C^n$，故 $\mathbb C^n\subseteq\mathcal V$，
  $n\le\dim\mathcal V=q+1$，与 $q\le n-2$ 矛盾。故**情形 B 在 $1\le q\le n-2$ 时不可能发生**。

两个情形合并：$q\le n-2$ 且可容许 ⟹ 必为情形 A ⟹ 失败 ✓；$q=n-1$ 时（$d=0$、$\mathcal Z=0$）由 B.18b 可行 ✓。
故 $q_{\min}=n-1$。$\square$

*备注*：
* 证明只用到 $(c,A)$ 的可观测性（不需要 $(\ell,A)$，也不需要 $\mathcal Z\subseteq K$）；
* 关键结构事实是 $\mathcal V=\operatorname{row}[\mathcal L;c]$（**$\mathcal V$ 只依赖 $\mathcal Z$**）与 $h=\dim(\mathcal V+\langle cA\rangle)$；
* 这也解释了为什么整族不可行：情形 A 由 B.22 直接杀掉，情形 B 与维数矛盾。
*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`B27.krylov_le`、`B27.eq_top_of_krylov` 给出情形 B 的归纳与 $\mathcal V=\top$；`B27.no_caseB` 给维数矛盾；情形 A 由 `B22` 的 `exists_root_of_pos_natDegree`；差在行空间实例化与"$(5a)\Rightarrow$ 右乘 $A$ 封闭"）$+$ **[精确验证 2454/2454]**
`tools/verification/b27_check.py`）；结构前提（$\mathcal V=\operatorname{row}[\mathcal L;c]$、$h=\dim(\mathcal V+\langle cA\rangle)$、
"情形 B ⟺ $\mathcal V$ $A$-不变"）另由 **2954/2954** 核验（`b26_class_I_only_Z.py`）。

**B.32（b）〔原 B.29〕（$p=1$、**任意** $r$：$q_{\min}=n-1$）** 设 $p=1$（$C=c^{\mathsf T}$）、$r\ge1$、$\operatorname{rank}[C;L_0]=1+r$、
$(c,A)$ 可观测、$\mathcal L$ 可容许。则对一切 $1\le q\le n-2$，$(5b)$ 失败；$q=n-1$ 可行。故
$$\boxed{q_{\min}=n-1 .}$$

*证明*（与 B.27 同构，只用 $p=1$）：
1. $r_1=\operatorname{rank}[CA;C]\le 2p=2$（$[CA;C]$ 只有 $2$ 行），又 $\ge\operatorname{rank}C=1$；$(c,A)$ 可观测使 $c,cA$ 独立，故 **$r_1=2$**；
2. 由 B.28(1)，$\mathcal V=\mathcal Z^\perp=\operatorname{row}[\mathcal L;c]$、$\dim\mathcal V=q+1$、$c\in\mathcal V$；
3. $W_0=\operatorname{row}[CA;C]=\langle cA,c\rangle$，故 $h=\dim(\mathcal V+W_0)=\dim(\mathcal V+\langle cA\rangle)\in\{q+1,q+2\}$，
   且 $h=q+2\iff cA\notin\mathcal V$；
4. **情形 A**（$cA\notin\mathcal V$）：$h=q+2=q+r_1$，由 **B.22** 得失败 ✓；
5. **情形 B**（$cA\in\mathcal V$）：$W_0\subseteq\mathcal V$，由 B.28(1) 的 $(5a)\iff\mathcal VA\subseteq\mathcal V+W_0$ 得 $\mathcal VA\subseteq\mathcal V$；
   归纳得 $cA^k\in\mathcal V$ 对一切 $k$；可观测性给 $\operatorname{span}\{cA^k\}=\mathbb C^{1\times n}$，故 $n\le q+1$，与 $q\le n-2$ 矛盾 ✓；
6. $q=n-1$（$d=0$、$\mathcal Z=0$）：与 B.18b 同理——$\operatorname{rank}[\mathcal L;C]=n$ 使 $(5a)$ 自动，$(5b)$ 的失败会需要 $V\ni x\ne0$ 且 $x$ 是 $A$ 的特征向量，被可观测性排除 ✓。

*注意*：$r$ **完全不进入**论证——$p=1$ 已决定 $\dim\mathcal V=q+1$、$r_1=2$、$W_0=\langle c,cA\rangle$。
*与 B.28b 的关系*：$r_1-p=2-1=1$，故 $\delta\in\{0,1\}$ **没有中间层**。这说明**中间层需要 $p\ge2$**；
专家 2026-11-05 §5.1 猜测 "$p=1,r=2$ 有 $r_1=3$、$\delta=1$ 的中间情形"——由于 $r_1\le 2p=2$（$[CA;C]$ 只有 $2p$ 行），
该情形**对 $p=1$ 不可能出现**。
*等级*：**[已证-纸面]** $+$ **[精确验证 597/593/589（$r=1,2,3$）全部失败、$q=n-1$ 无样本]**（`tools/verification/p1_general_r.py`）。

**B.32（c）〔原 B.32〕（终端唯一区：$r_1\le p+1$ ⟹ $q_{\min}=n-p$；专家 2026-11-05 §3.1 给出）** 设 $(C,A)$ 可观测、
$\operatorname{rank}[C;L_0]=p+r$、$r_1=\operatorname{rank}[CA;C]$，记 $\rho:=r_1-p$。若 $\rho\le1$（即 $r_1\le p+1$），则
$$\boxed{q_{\min}=n-p .}$$

*证明*：
1. **无中间层**：由 B.28b，$0\le\delta\le\rho$；若 $\rho\le1$ 则不存在整数 $\delta$ 满足 $1\le\delta<\rho$，故中间层为空；
2. **低于终阶不可行**：由 **B.31**（当 $q+p<n$），可行 ⟹ $1\le\delta<\rho$——与 1 矛盾；故 $q\le n-p-1$ 全部不可行；
3. **终阶可行**（$q=n-p$、$d=0$、$\mathcal Z=0$）：取 $U$ 为 $\operatorname{row}L_0$ 的 $(n-p)$ 维扩张且 $U\cap\operatorname{row}C=0$
   （存在，因 $\operatorname{rank}[C;L_0]=p+r$），令 $\mathcal L$ 以 $U$ 的基为行；则 $\operatorname{rank}[C;\mathcal L]=n$，
   $(5a)$ 自动（行空间为整个 $\mathbb C^{1\times n}$）；$(5b)$：在 $T=[C;\mathcal L]$ 的坐标下化为
   $\operatorname{rank}\begin{bmatrix}\lambda I_q-A_{22}\\ A_{12}\end{bmatrix}=q$ 对一切 $\lambda$，由 PBH 等价于 $(C,A)$ 可观测 ✓。
故 $q_{\min}=n-p$。$\square$

*推论*：
* **$p=1$**：$r_1\le 2p=2=p+1$ ⟹ $\rho\le1$ ⟹ $q_{\min}=n-1$ ——**这正是 B.29**，于是 B.29 成为 B.32 的特例；
* $\rho\le p$（因 $r_1\le 2p$），故 $\rho\ge2$ 需要 $p\ge2$ ✓；
* **$\rho\le1$ 是"终端唯一"的充分条件**；$\rho\ge2$ 只是"可能有次终端可行"，不保证。
*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`B32.terminal_only` + `B32.no_intermediate`（终端唯一 + 无中间层的算术））（专家给出，本项目复核；终端可行部分与 B.18b 一致）。
**B.32 的核验**：$\rho\le1$ 的 385 个实例**全部** $q_{\min}=n-p$ ✓；$\rho\ge2$ 的 812 个实例**全部** $q_{\min}<n-p$ ✓。
*等级*：前两行 **[已证-纸面]**；第三行由 B.32 的终阶构造；第四行 **[精确验证 1107/1107]**（`delta_fixed.py`）。

## Lean

* `B31_32_33.lean` —— `B32.no_intermediate`（$\rho\le1$ 时无中间层）、`B32.terminal_only`（次终端全不可行 + 终阶可行 ⟹ 最小阶 = 终阶）
* `B27.lean` —— `krylov_le`、`eq_top_of_krylov`、`no_caseB`（$p=r=1$ 情形 B 的矛盾，即分部 (a) 的内核）
* 差异："次终端不可行"由 B.31 推出那一步是纸面逻辑，内核把它当假设

## 精确验证

* `tools/verification/delta_fixed.py`：$\rho\le1$ 的 **385/385** 实例都有 $q_{\min}=n-p$
* `tools/verification/p1_general_r.py`：$p=1$ 时任意 $r$ 的 597/593/589 个候选全部失败
* `tools/verification/controlled_profile.py`：控制变量族里 $\rho=1$ 例给出 $q_{\min}=4=n-p$



## WSL 侧内核（同步前仅机器可复核）

下面这些内核已在 WSL 的 Lean 工程里编译通过（`lake build MyProof` exit=0），
但**尚未同步到 Windows 侧、也未登记进 `STATEMENT_MAP`**，因此 docs 的等级行暂未把它们计入：

* `B31_32_33.lean`、`B27.lean`（已在 Windows 侧登记）



## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F2 |
| 导出等级 | **L3** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— Lean 已覆盖（内核） |


## 状态与历史

经专家复核（2026-11-05）："终端唯一区"建议提为主定理；(a) 分部（原 B.27）单独复核过。
