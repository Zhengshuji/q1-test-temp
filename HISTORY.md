# HISTORY · 项目是怎么走到这里的：一条压缩链、两次撤回与当前前沿

> **用途**：本文记录**项目发展脉络**（怎么一步步走向 $q1$），是**项目叙事 + 论文叙述框架**。与 `STATUS.md` 互补：STATUS 讲“现在在哪、下一步试什么”，本文讲“怎么走到这里、哪些结论被撤回”。
> 它回答三个问题：项目最初想做什么、为什么转向、现在手里有什么。
> 每次有实质进展（新定理、撤回、专家裁决）后更新第 8–10 节；第 1–7 节是历史，只在发现史实错误时改。
>
> **更新日期**：2026-11-10。**维护**：每次实质进展后更新第 7–8 节与第 11 节；第 1–6 节是历史。
> **可靠性标记**：M0 未证 · M1 实验 · M2 纸面 · M3 独立复核/专家 · M4 文献定理；
> F0 无形式化 · F1 辅助 · F2 核心 · F3 字面。`[Lean]` 只在 `tools/lean/STATEMENT_MAP.md` 有声明名时使用。

---

## 0. 一页图（当前）

```
q1（∃Θ 的判定复杂度）—— 仍开放
│
├─ 文献已解决（不重证）
│   存在性、阶谱、逐阶充要、最小阶=最小谱可行阶、构造
│
├─ 压缩链（项目的结构基础）
│   R  ──►  (H, H_A)  ──►  Z : W → C^q  ──►  块判据 / gcd
│   (第一次)            (第二次)
│
├─ 算法侧（最成熟）
│   固定 (q,c)  ──►  有界维实代数
│   固定 κ_obs   ──►  Gram 证书 + 实 QE（M2，待写细）
│   固定 q       ──►  sketch（缺参数化消去引理）
│
├─ 硬度/表达力（探索中）
│   秩门：q=2 关闭；q=4 的“不可能”已撤回；q=5 只有搜索边界
│   谱门：2×1 非零 gadget 已完整落地（296）—— 第一个正结果
│   乘法门：未构造；这是 hardness 的关键缺口
│
└─ 已撤回：四个闭式、217、234/239、270、279、282/283/284/292/293、287
```

**一句话**：项目的主线不是“算更多例子”，而是**把 $R$ 压成 $(H,H_A)$、把 $(H,H_A)$ 压成 $W$ 上的 $Z$**；
文献解决刻画后，剩下的是 $\exists\Theta$ 的复杂度。当前最成熟的是算法侧（固定 $\kappa_{\rm obs}$ 的 Gram 证书）；
硬度侧的第一个可落地 gadget 是 296 的 $2\times1$ 非零门。

---

## 1. 起点：公式时代及其失败

问题（[docs/00](docs/00_problem.md)）：

$$(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\ \forall\lambda .$$

最早的直觉是 $q_{\min}$ 由少数不变量决定，于是有四个闭式：

| 闭式 | 结果 |
|---|---|
| $q_{\min}=\dim V+1$ | 被 $n=5$ 反例推翻 |
| $q_{\min}=d+\max(c_0,1)$ | 被三份证书推翻 |
| $q_{\min}=\max(r+\varepsilon,\rho^*+1)$ | 被一族反例推翻 |
| $F_3:\max(r+\varepsilon,\rho^*+\max(c_0,1))$ | 被 $n=4$ 反例推翻 |

全部收在 [proof/refuted/README.md](proof/refuted/README.md)。

**收获不是公式，而是结构判断**：$q_{\min}$ 不是少数不变量的函数；可行集是**按 $\omega=\operatorname{rank}H$ 分层的并**。
策略从“求闭式”变成“固定一层，研究这一层”。

---

## 2. 第一次压缩：$R\mapsto(H,H_A)$

固定 $\omega$，令
$$K_0=\ker[C;CA],\qquad k=\dim K_0,\qquad N\ \text{为基},$$
$$H=LN,\qquad H_A=LAN.$$

这一步把 $R$ 的 $m=q-r_0$ 行压进两个 $q\times k$ 矩阵。两个条件变成：

- $(5a)$：存在 $\Lambda,G_0,G_1$ 使 $LA=\Lambda L+G_0C+G_1CA$，等价于
  $\ker(L,C,CA)\subseteq\ker(LA)$（[B.17](proof/B.17/README.md)）；
- $(5b)$：$\lambda H-H_A$ 的 $\omega$-子式没有公根（[B.8](proof/B.8/README.md)、[B.24](proof/B.24/README.md)）。

关键是核包含
$$\ker H\subseteq\ker H_A,$$
它保证诱导映射
$$Z:W=\operatorname{im}H\longrightarrow\mathbb C^q,\qquad Z(Hx)=H_Ax$$
良定义。选 $\mathbb C^q=W\oplus W'$，写 $Z=(A_W;B_\perp)$，得到**块判据**（[B.24](proof/B.24/README.md)）：

$$\boxed{\text{bad}\iff\exists\,0\ne y\in\ker B_\perp,\ A_Wy\in\mathbb C y .}$$

一句话：**$(5a)$ 是“定义域”条件，$(5b)$ 是“$Z$ 在 $W$ 上没有部分特征向量”**。

---

## 3. 第二次压缩：$(H,H_A)\mapsto Z$，坏 = 闭集 + gcd

在固定秩层（$\operatorname{rank}H=\omega$、$\ker H\subseteq\ker H_A$）上，坏集
$$\mathcal B=\{(\sigma,R):\exists\lambda,\ \operatorname{rank}(\lambda H-H_A)<\omega\}$$
是**闭**的：把 $\lambda$ 齐次化到 $\mathbb P^1$，无穷远处矩阵为 $H$、秩恰为 $\omega$，
投影 $\mathbb P^1$ 紧合（[B.24](proof/B.24/README.md)）。

> 每个不可约分量上，要么全坏，要么好点 Zariski 开稠密；由 $\mathbb C(X)$ 上 $\omega$-子式的
> generic determinant divisor 判定（B.24 定理 A）。

这一步把“逐点找 $R$”变成“在函数域上算一个 gcd”。

---

## 4. 文献已经解决的部分（项目不重证）

2026-09 的两篇论文（Fernando）给出**逐阶完整刻画**：存在性、阶谱、每阶充要条件、
最小阶 = 最小谱可行阶，以及构造。见 [docs/07](docs/07_literature_review.md)。

唯一还开放的是
$$\exists\Theta\ \text{（图卡}\times\text{半代数）的判定复杂度},$$
即 $q1$。

项目保留的复杂度结果：

| 结果 | 状态 | 依据 |
|---|---|---|
| $\mathrm{DEC}(q)\in\exists\mathbb R$ | M3 | **Paper I**, Theorem 5 |
| 块判据（坏 $\iff$ 部分特征向量）| M3 | **Paper I**, Claims 5 / 11 |
| $k=\omega$ 的 RP 上界（条件性）| M2 | 本地（[101](workspace/q1_false/c_stratification/attempts/101_rp_k_omega.md)） |

---

## 5. 低 $c$ 分类：结构基础

$c=k-\omega=\dim\ker H$。

- **$c=0$ 不可能**：$H$ 方阵可逆时 $\det P$ 是非常数多项式，必有根（[186](workspace/q1_false/c_stratification/attempts/186_61_verdict_implementation.md)）。
- **$c=1$ 二分**：$W_L\subseteq D$ 时超平面引理 + 特征线给出不可行（[182](workspace/q1_false/c_stratification/attempts/182_c1_infeasibility_lemma.md)/[183](workspace/q1_false/c_stratification/attempts/183_c1_eigenlines.md)）；
  $W_L\not\subseteq D$ 时可容许真空（[188](workspace/q1_false/c_stratification/attempts/188_c1_outside_D.md)），但铅笔可结构性坏；外点空/非空开放（[193](workspace/q1_false/c_stratification/attempts/193_c1_O2_reduction.md)）。
- **$c=2$ forced-plane**：逐行 $b_i$ 被 forced 0 $\iff$ $e_b\in\operatorname{rowspace}(\mathrm{Des}_i)$；
  实例 16/21 在 $\mathsf P_{\mathrm{ind}}$ 下全 $q$ 不可行（[184](workspace/q1_false/c_stratification/attempts/184_q4_excluded.md)、[185](workspace/q1_false/c_stratification/attempts/185_seeds_infeasible_all_q.md)）。
- **求解器**：四层（几何/压缩行/提升/谱），精确证书，三态输出（[180](workspace/q1_false/c_stratification/attempts/180_uniform_stratum_solver.md)）。
- **一般 $c$ 的分量界**：不变部分用循环向量（[149](workspace/q1_false/c_stratification/attempts/149_general_c_component_bound.md)），
  非不变部分归到 $B_{u,v}$ 的 Bézout 界（[171](workspace/q1_false/c_stratification/attempts/171_Buv_rank_strata.md)）。

结论是**可计算的/结构性的**：低 $c$ 几何可精确描述，为 gadget 设计提供约束，但不直接给 $q1$ 的复杂度。

---

## 6. 刚性与 gadget 阶段（2026-11 上旬）

文献解决刻画后，主线转向**硬度/表达力**。

### 6.1 铅笔判据与小算法

- O1 块判据：坏 $\iff$ $A_*$ 的某个特征向量被 $B_*$ 吞掉；正确表述是
  $$\ker(A_*-\lambda I)\cap\ker B_*=\{0\}\ \forall\lambda$$
  （[191](workspace/q1_false/c_stratification/attempts/191_c1_pencil_criterion.md)）；
- 固定候选上的 gcd/块算法（[192](workspace/q1_false/decision_algorithms/attempts/192_c1_pencil_block_algorithm.md)）。

### 6.2 刚性

- **全局刚性**：$A(K_0)\subseteq K_0$ 且 $\omega>0$ $\Rightarrow$ 不可行
  （[203](workspace/q1_true/multiplication_gate/attempts/203_invariance_theorem.md)、[205](workspace/q1_true/multiplication_gate/attempts/205_AinvK0_impossible.md)）；
- **局部泄漏**：$A(V)\subseteq K_0$ 只迫使 $A(V)\subseteq V$，**不**导致铅笔坏；seed 10 是反例
  （[210](workspace/q1_true/multiplication_gate/attempts/210_local_leakage_correction.md)）；
- 217 的“$\omega=2,q=3$ 不可能”被专家 10 维族推翻（[228](workspace/q1_true/multiplication_gate/attempts/228_68_69_verdict.md)、R22）。

### 6.3 一致谱与提升

- 过滤链 + **单位子式**：$\operatorname{rank}P_X(\lambda)=\omega$ 对所有 $X,\lambda$
  （[215](workspace/q1_true/multiplication_gate/attempts/215_67_verdict_uniform_spectral.md)）；
- 固定核 + 提升方向的可行族（[224](workspace/q1_true/multiplication_gate/attempts/224_fixed_kernel_lift_family.md)），
  但提升参数是开条件，不能编码算术（[225](workspace/q1_true/multiplication_gate/attempts/225_lift_params_cannot_encode.md)）。

### 6.4 乘法门的尝试与撤回

- reduced 行列式恒等式：只取 $lA$ 的矩阵 $M=[lA;L_0;l;CA;C]$ 上 $\det M=ad-bc$（[234](workspace/q1_true/multiplication_gate/attempts/234_explicit_gate.md)）；
- 补上 $L_0A$ 后，该实例 $(5a)\iff b=0,d=0,c\ne0$，而 $(5b)$ 的极大子式
  $\Delta=c(\lambda^2-\lambda-1)$ 恒有复根 ⇒ 无可行 $L$（[239](workspace/q1_true/multiplication_gate/attempts/239_72_missing_L0A.md)、R23）；
- 结论：条件门/边界见证作废；正确目标是完整 6 行 $(5a)$ + 恒定 $\operatorname{rank}M_0$ + 两行包含 + Schur 残差。

---

## 7. 2026-11-09/10 前沿：秩门的兴衰与谱门的第一个正结果

这一段是**最近两天**的主线，也是论文叙事里“从秩门转向谱门”的转折。

### 7.1 秩门的最后几次尝试

1. **$q=4$ 的 rank-one 门**：压缩层构造出
   $$\operatorname{rank}H=3\iff r_{11}r_{22}-r_{12}r_{21}=0,$$
   甚至找到同时满足 $(5a)(5b)$ 的压缩数据；但它**不可提升**：$(H_A)_2$ 混用了第一自由行的数据，
   违反逐行 $r_iAN$ 依赖（[281](workspace/q1_true/rank_gates/attempts/281_q4_gate_not_liftable.md)）。
2. **一个错误的“结构定理”**：曾证明 $\omega\le r=q-r_0$，并据此宣布 $q=4$ 不可能（[282](workspace/q1_false/decision_algorithms/attempts/282_omega_le_r.md)）。
   78 号审计指出：$(5a)$ 只给 $L_0A\in\operatorname{row}[L_0;R;CA;C]$，含 $R$，所以
   $H_{A,0}=M_0H_0+M_1Y$，不一定是 $M H_0$；相交情形的推理也错。
   **该定理与 283/284/292/293 全部降级/撤回**（[295](workspace/q1_true/multiplication_gate/attempts/295_78_audit_corrections.md)）。
3. **$q=5$ 的 $z=xy$ 门**：压缩层成立（[285](workspace/q1_true/rank_gates/attempts/285_q5_gate_target.md)），
   但 $Y_1=e_1$ 时 $\lambda=1$ 掉秩，$Y_1\ne e_1$ 时无二次门（[292](workspace/q1_false/decision_algorithms/attempts/292_y1_dichotomy.md)）；
   2000 例搜索无可行。**这是搜索边界，不是关闭定理。**

**当前判断**：秩门的“不可能性”叙事已撤回；$q=4$、$q=5$ 都重新开放。
继续做 rank 门需要真正的符号消元，而不是随机搜索。

### 7.2 提升判据（保留的正确结果）

$$N,AN\subseteq\ker C\ \Rightarrow\ \operatorname{rank}[N\ AN]\le n-p<n.$$
所以 $R\mapsto(RN,RAN)$ 永不满射；每个压缩行对必须逐行满足
$$\boxed{(H_i,H_{A,i})\in\operatorname{row}[N\ AN].}$$
这是所有 gadget 的硬门槛（[288](workspace/q1_false/decision_algorithms/attempts/288_lift_rank_bound.md)）。

### 7.3 谱门的第一个完整落地（296）

78 号给出压缩 $2\times1$ gadget：
$$H=\begin{bmatrix}1\\0\end{bmatrix},\quad H_A=\begin{bmatrix}0\\f\end{bmatrix},\quad P(\lambda)=\begin{bmatrix}\lambda\\-f\end{bmatrix},$$
并问它能否逐行提升。答案是**能**（[296](workspace/q1_true/multiplication_gate/attempts/296_nonzero_gadget_observer.md)）：

取
$$n=3,\ p=1,\ q=2,\ r_0=1,\ r=1,\ k=1,\ \omega=1,$$
$$C=\begin{bmatrix}0&0&1\end{bmatrix},\quad
A=\begin{bmatrix}0&0&0\\1&0&0\\0&1&0\end{bmatrix},\quad
L_0=\begin{bmatrix}1&0&0\end{bmatrix},\quad
R(f)=\begin{bmatrix}0&f&0\end{bmatrix}.$$
则
$$K_0=\operatorname{span}(e_1),\quad N=e_1,\quad
H=\begin{bmatrix}1\\0\end{bmatrix},\quad H_A=\begin{bmatrix}0\\f\end{bmatrix},$$
且
$$(5a)\ \text{对所有 }f\text{ 成立},\qquad (5b)\iff f\ne0.$$
`c296` PASS。

**意义**：这是第一个完整的、逐行可提升的 $(5b)$ 非零 gadget，回答了 78 号的核心问题。
它不是乘法门，只编码“某参数非零”；但这是 $\exists\mathbb R$ 归约中与等式配合的另一半。

**wiring 障碍（305）**：304 的列重合是逐行的；乘法门的输出 $z$ 与输入 $y$ 在同一行，复制整行 $H_2=(H_A)_1$ 会强制 $y_1=1$，破坏乘法；复制单坐标没有机制。需要 copy/format gadget $(0,y,z)\to(0,1,z)$。

**wiring 判据（304）**：若 $AN_j=N_l$，则对所有 $L$，$H_{A,j}=H_l$；这是 copy/wire 原语，但每 wire 使 $\operatorname{rank}[N\ AN]$ 至少降 1。

**移动端口（310）**：$W\ni v_x=e2+x e3$ ⇒ $e3\in W$；固定 $E_2\subset\operatorname{span}(e1,e3)$ 被 $W$ 包含（交二维），带外方向则交线固定；移动端口需 $E_2$ 依赖 $x$，固定数据给不出。

**论文冻结阶段（2026-11-10）**：进入论文与 Lean 基座建设。新建 WSL `Q1Paper` 工程；论文只保留算法与结构结果（6 Lemma + 4 Theorem）；硬度/gadget 归档为项目材料。

**83 号裁决（315）**：q1 的 P/∃R-完全/参数化中间三结局均未排除；两条参数化算法均获认可；硬度最佳源 ARM(3)，其次 matroid；参数化下界只做 $q$-W[1]；主线 Phase A 算法论文，Phase B 一个 ARM 翻译实验，Phase C 参数化下界。

**82 号裁决（314）**：两条算法均获认可；固定 $q$ 用 $G=FX$（变量 $2q\omega$，次数 1）；FPT 补 $r=0$ 的 polynomial left-inverse 分支；硬度暂停局部 gate。

**固定 $\kappa_{\rm obs}$ FPT 骨架（313）**：压缩参数化 $\kappa=rd_0$；Gram $(5a)$；Bezout 次数；$B^{\mathsf T}Bx=e_0$ 索引；Cauchy–Binet；变量 $\kappa+2\omega+1$，$q$ 只进多项式。c313 精确验证索引。

**固定 $q$ 骨架（312）**：$H=XB$、$B_J=I$、$H_A=FXB$；自由行 $D$-约束对 $B$ 线性；秩一致性消去 $B$；$(5b)$ 只依赖 $F,X$；变量 $O(q^2)$，固定 $q\in P$（XP，$L^{O(q^2)}$）。c311/c312 精确验证。

**81 号裁决（311）**：port rigidity 只是条件性 no-go（固定子空间可有移动端口）；303C 的正确量词是 $\exists R\iff x\ne0$；固定 $q$ 有新算法 $H=XB$ + 秩一致性消去；路线优先 FPT，固定 $q$ 第二，硬度次要。

**port rigidity（309）**：$E_1=\operatorname{span}(e1,e2)$、$E_2=\operatorname{span}(e1,e3)$，若 $W\supseteq E_1$、$\dim W=3$、$W\cap E_2=\operatorname{span}(e1)$，则矛盾；固定局部子空间排除额外行但冻结 $W$，乘法需要移动端口。

**soundness–表达力二分（308）**：$H_0$ 满秩 $k$ ⇒ $\operatorname{rank}H=k$、$\operatorname{im}H$ 固定、$(5a)$ 线性，sound 但无乘法；$H_0$ 不满秩 ⇒ 自由行可升秩，303/80 的 bypass 由此产生。sound + 乘法需要局部子空间交/global incidence。

**soundness 义务（307）**：sound q1 gate 需 C（completeness）、S（所有可行 $R$ 解码）、R（秩层强制）。固定 $H_{A,0}\notin\operatorname{row}H_0$ 可排除 $R=0$，但自由行可跳到满秩使 $(5a)$ 空条件；rank forcing 不足以强制乘法。

**80 号审计（306）**：303 的乘法门只是 full-observer realization，不是 sound q1 gadget——$R=0$ 时 $(5a)(5b)$ 仍成立但不约束 $z=xy$。296 与 303 的输入非零门仍 sound；297 直和、299/300 压缩块需 soundness 分析。80 号给出跨行 shift 与射影线构造，但双门串联仍只在压缩层成立。

**79 号裁决（303）**：$3k$ 维通用提升使 $[N\ AN]$ 行满秩 $2k$，任意压缩对可提升；完整乘法门 $(5a)\iff z=xy$、$(5b)\iff\beta\ne0$；输入非零门 $(5b)\iff x\ne0$。但块对角 $A,C$ 不强制 $R$ 块对角，297 的直和合取只对压缩矩阵成立；剩余目标是 wiring/equality。

**直和（297）**：两个 296 块对角，得到
$$(5b)\iff f_1\ne0\ \wedge\ f_2\ne0,$$
$(5a)(5b)$ 按块分解。这是“非零条件的合取”，仍不是乘法门。

**固定 $x$ 的二分（301）**：$x\in H_0$ 时 $(5a)$ 只是线性关系；$x\in Y$ 时是见证变量。$H$ 层不能兼得“输入固定 + 乘积”；要 hardness 必须让 $x$ 通过 $N(A)$ 系数编码进入。

**共享 $x$ 双输出（300）**：$q=4,\omega=2$，两行 $H_{A,2}=(0,y_1,z_1)$、$H_{A,3}=(0,y_2,z_2)$ 同属 $\operatorname{span}(h_1,h_2)$，故 $(5a)\iff z_1=xy_1,z_2=xy_2$；$(5b)$ 由支撑行 $\alpha h_1+\beta h_2$ 保持。变量仍是见证变量。

**混合块（299）**：$q=3,\omega=2$，
$$H=\begin{bmatrix}1&0&0\\0&1&x\\0&0&0\end{bmatrix},\quad
H_A=\begin{bmatrix}a&0&0\\0&y&z\\\alpha&\beta&w\end{bmatrix},$$
$(5a)\iff z=xy,w=\beta x$，$(5b)$ 在门上自动成立。但变量是见证变量，不是输入固定的变量；这是“条件关系”块，不是硬度门。

---

## 8. 当前成果清单（按可靠性）

### 8.1 可靠/可引用

| 结果 | 状态 | 依据 |
|---|---|---|
| 两次压缩与块判据 | M3 | **Paper I**, Claims 2 / 4 / 5 |
| $\mathrm{DEC}(q)\in\exists\mathbb R$ | M3 | **Paper I**, Theorem 5 |
| 全局刚性 $A(K_0)\subseteq K_0,\omega>0$ 不可行 | M3 | 本地（205） |
| 低 $c$ 分类与求解器 | M2/M3 | 本地（182–185、180） |
| 提升判据 $\operatorname{rank}[N\ AN]\le n-p$ | M2 | 本地（288） |
| $2\times1$ 非零 gadget 完整实现 | M2 + 精确验证 | 本地（296） |
| 非零 gadget 直和（合取）| M2 + 精确验证 | 本地（297） |
| 混合块 $(5a)$ 强制 $z=xy$ | M2 + 精确验证 | 本地（299） |
| 完整乘法门/输入非零门 | M3 + 精确验证 | 本地（303） |
| 固定 $q$ XP / 固定 $\ell$ FPT | — | **Paper I**, Theorems 1 / 2 |
| 共享 $x$ 双输出 | M2 + 精确验证 | 本地（300） |
| 固定 $x$ 的二分 | M2 分析（负）| 本地（301） |
| 固定 $\kappa_{\rm obs}$ 的 Gram 证书 | — | **Paper I**, Claim 11 |
| 固定 $(q,c)$ 有界维 | 本项目独立结果 | 本地（247、261）；Paper I 的 XP/FPT 覆盖更强版本 |

### 8.2 条件性/待补

| 结果 | 缺什么 |
|---|---|
| 296 的组合 | 多个非零 gadget + 等式约束 → 算术门 |
| $q=5$ 秩门 | 完整符号族/消元，或严格 no-go |

### 8.3 已撤回/降级（不要引用为定理）

| 旧结论 | 撤回原因 |
|---|---|
| 四个闭式 | 反例 |
| 217 $\omega=2,q=3$ 不可能 | 专家 10 维族 |
| 234/239 条件乘法门 | 漏 $L_0A$，补上后无可行 $L$ |
| 251 coupled-plane 只线性 | 专家 75 的 $2+2$ Plücker 反例 |
| 270 非零 gadget | $H=fH_0$ 使 $\operatorname{rank}H$ 随 $f$ 变 |
| 279 固定行不变性 | $H_A=FH$ 是行组合，不推出列空间不变 |
| 282 $\omega\le r$ | $L_0A$ 可用 $R$；相交情形错 |
| 283/284/292/293 | 依赖 282/284，降级 |
| 287 提升满射 | $N,AN\subseteq\ker C$，秩 $\le n-p$ |

---

## 9. 论文叙述框架（可直接按此写）

### 9.1 如果是**算法论文**（当前最成熟）

1. Introduction：$q1$ 与文献已解决的刻画；本文处理固定参数。
2. Preliminaries：$(5a)(5b)$、$K_0,N,H,H_A$、块判据。
3. 压缩：$R\mapsto(H,H_A)$；固定秩层；提升判据。
4. **固定 $\kappa_{\rm obs}$ 的 FPT**：Gram 证书 + Cauchy–Binet + 实 QE（277/278；补细节）。
5. 固定 $(q,c)$ 的有界维算法（247/261）。
6. 固定 $q$ 的讨论与缺口（参数化消去）。
7. 实验/证书：c278、c296。
8. Open：固定 $q$、变 $\kappa$。

### 9.2 如果是**硬度论文**（还早）

1. Introduction：$\exists\mathbb R$ 上界；缺的是归约。
2. 压缩与提升判据：为什么“压缩门”不等于“观测器门”。
3. 非零 gadget（296）：完整的 $(5b)\iff f\ne0$。
4. 乘法门：要构造 $z=xy$；当前只有压缩层，未落地。
5. 组合：等式（$(5a)$）+ 非零（$(5b)$）→ 算术电路。
6. 结论：$\exists\mathbb R$-hard；当前缺口在第 4 步。

### 9.3 如果是**结构论文**

1. 压缩链与块判据。
2. 低 $c$ 分类、刚性、分量界。
3. $\exists\mathbb R$ 成员与可计算性边界。
4. 不作为硬度声明。

**建议**：当前先按 9.1 写算法论文；硬度部分把 296 作为“第一个可落地组件”记录，不宣称归约。

---

## 10. 维护规则（每次实质进展后）

1. **第 7 节**：追加/改写当前前沿（不超过 1 页），保留“哪些是搜索边界、哪些是定理”。
2. **第 8 节**：更新三张表（可靠/条件/撤回）；撤回项必须留一行，不删。
3. **第 9 节**：只在论文结构变化时改；不要每次小进展都重写。
4. **第 11 节更正表**：新撤回加一行。
5. 每次更新后跑
   `python tools/hygiene/audit_layout.py`、`audit_retractions.py`，四道门全绿再提交。
6. 本文只写**项目叙事与状态**；具体证明细节仍放 `attempts/`、`proof/`、`docs/`。

---

## 11. 更正表（更新到 2026-11-10）

| 旧说法 | 更正 | 影响 |
|---|---|---|
| $q_{\min}=4$（$n=5$ 约束例）| $q_{\min}=2$ | 层 $\ne$ 阶；$q_{\min}$ 要对 $\omega$ 取并 |
| “可对角化 $\Rightarrow$ 铅笔好” | 特征空间单射判据 | 191 的错误 |
| 局部泄漏 $\Rightarrow$ 不可行 | 只给 $A(V)\subseteq V$；seed 10 反例 | 210 |
| 65/213 的“模板不一致” | 模板成立（$LAN$ 行列作用混淆）| 214 |
| $\omega=2,q=3$ 不可能 | 专家 10 维族 | 217 撤回（R22）|
| no-drop 不能编码秩一 | 234 的否证无效（漏 $L_0A$，239）| 233 恢复为未决 |
| reduced $\det M=ad-bc$ 是观测器门 | 漏 $L_0A$；补上后无可行 $L$ | 239、R23 |
| 共享 $f$ 是 $(5b)$ 的必要条件 | 反例；只是充分条件 | 271/276 |
| $\det\pi(Y)=0$ 等价于 rank 3 | 只给 rank $\le3$；需非零 | 275/276 |
| 固定 $\kappa_{\rm obs}$ FPT（旧 Bezout）| $q$ 不受控；改用 Gram 证书 | 261/277 |
| $\omega\le r$ 与吸收性 | $L_0A$ 可用 $R$；相交情形错 | 282 撤回、295 |
| $q=4$ 不可能 | 依赖 282 | 283/295 降级 |
| $q=5$ rank 门关闭 | 只是搜索边界 | 293/295 降级 |
| 270 非零 gadget | $H=fH_0$ 使 $H$ 掉秩 | 294 撤回 |
| 287 提升满射 | $N,AN\subseteq\ker C$ | 288 撤回 |

---

## 12. 阅读顺序（给接手者/汇报对象）

1. 本文（10 分钟，知道项目怎么走到这里）。
2. [STATUS.md](STATUS.md)（当前一页纸）。
3. [docs/00](docs/00_problem.md)、[docs/01](docs/01_notation.md)（问题与记号）。
4. [docs/07](docs/07_literature_review.md)（文献已解决什么）。
5. [docs/02](docs/02_theorems_proven.md)（可靠命题）。
6. 需要细节时再进 `attempts/`：296（非零 gadget）、277/278（FPT）、288（提升判据）、205（刚性）。
7. 需要历史教训时看 [09_work_inventory.md](workspace/support/project_management/09_work_inventory.md)、[11_usable_and_route.md](workspace/support/project_management/11_usable_and_route.md)。
