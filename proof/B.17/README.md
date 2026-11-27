# B.17 · 永久核与商铅笔

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.17` 条目（§0.1 归并表）。

## 命题

**B.17（永久核与商铅笔判据；专家 2026-11-04 §2.1/§5 给出，本项目核验）** 设 $\mathcal L$ 满足 $(5a)$、
$\mathcal Z=\ker[C;\mathcal L]$、$S=V\cap\mathcal Z$、$N_{\mathcal Z}(\lambda)=T_{\mathcal Z}-\lambda J_{\mathcal Z}$。则

1. **永久核（两种精确写法，勿混淆）**：① 公共核 $S\subseteq\bigcap_{\lambda\in\mathbb C}\ker N_{\mathcal Z}(\lambda)$（等式需 $(5a)$ + 可容许性，见专家 §2.1）；② 多项式零模 $\ker_{\mathbb C[\lambda]}N_{\mathcal Z}(\lambda)\supseteq S\otimes_{\mathbb C}\mathbb C[\lambda]$。两者是**不同**断言：前者是逐点交，后者是 $\mathbb C[\lambda]$-模；正文分别陈述；
2. **商判据**：
$$(5b)\ \text{成立}\iff\ker N_{\mathcal Z}(\lambda)=S\ \ \forall\lambda
\iff \overline N_{\mathcal Z}(\lambda):V/S\to X/\mathcal Z\ \text{对一切}\ \lambda\ \text{单射};$$
3. **可计算形式**：取 $V'$ 为 $S$ 在 $V$ 中的补（$\dim\rho=\dim V-s$）、$P_{\mathcal Z}$ 满足 $\ker P_{\mathcal Z}=\mathcal Z$，则
$\overline N_{\mathcal Z}(\lambda)$ 的矩阵为 $P_{\mathcal Z}(A-\lambda I)V'$（$(n-d)\times\rho$），它对**一切有限** $\lambda$ 单射
$\iff$ 其 $\rho$ 阶极大子式的 gcd 为**非零常数**（$\rho=0$ 时条件空、自动可行）。


## 与 $P_K$ 的系数级比较（专家第六轮 §3 的第一步）

专家的意见：不要假定两支铅笔等价，先写**系数对**并检验是否存在**常数 intertwining 图**。

### 1. 定义（全部显式）

* $X:=\mathbb C^n$（环境空间）；
* $\mathcal Z:=\ker[C;\mathcal L]$；$S:=V\cap\mathcal Z$，其中 $V:=\operatorname{row}[\mathcal L;C]^{\mathsf T}$；
* $J_{\mathcal Z}:X\to X/\mathcal Z$ 为商映射，$T_{\mathcal Z}:=A(\cdot)+\mathcal Z$，$N_{\mathcal Z}(\lambda):=T_{\mathcal Z}-\lambda J_{\mathcal Z}$；
* $\overline N_{\mathcal Z}(\lambda):V/S\to X/\mathcal Z$ 为 $N_{\mathcal Z}(\lambda)$ 在 $V/S$ 上的诱导映射；
* 坐标形式（B.17 第 3 条）：取 $V'$ 为 $S$ 在 $V$ 中的补、$P_{\mathcal Z}$ 满足 $\ker P_{\mathcal Z}=\mathcal Z$，则
$$\overline N_{\mathcal Z}(\lambda)\ \widehat=\ P_{\mathcal Z}(A-\lambda I)V'\qquad\bigl((n-d)\times\rho_W\bigr).$$

**系数对**（写成 $N_0+\lambda N_1$）：
$$N_0=P_{\mathcal Z}A V',\qquad N_1=-P_{\mathcal Z}V' .$$

另一支铅笔（B.24，域 $W_K=\mathcal LK$）：$P_K(\lambda)=\lambda\iota_K-\Phi_K$，故
$$P_0=-\Phi_K,\qquad P_1=\iota_K .$$

### 2. intertwining 图（专家 §3.1）

要找**常数**线性映射 $a:V/S\to W_K$、$b:X/\mathcal Z\to\mathbb C^q$ 使
$$b\,\overline N_{\mathcal Z}(\lambda)=P_K(\lambda)\,a\qquad\forall\lambda .$$
因两支都是 $\lambda$ 的一次式，等价于**两条常数恒等式**：
$$b\,N_1=P_1\,a=\iota_K a,\qquad b\,N_0=P_0\,a=-\Phi_K a .$$

**一个自然候选**：$b:=\bar{\mathcal L}$，即 $\mathcal L$ 在 $\mathbb C^n/\mathcal Z$ 上诱导的映射——良定义因为
$\mathcal Z=\ker[C;\mathcal L]\subseteq\ker\mathcal L$，故 $\bar{\mathcal L}$ 存在且 $\bar{\mathcal L}N_1=-\bar{\mathcal L}P_{\mathcal Z}V'$。

### 3. 要解的常数线性系统（下一步）

把 $a$（$\rho_W\times\omega$ 个未知量）与 $b$（$\dim(X/\mathcal Z)\times q$ 个未知量）并成一个大未知向量，
两条恒等式给出 $q\rho_W$ 个标量方程（每条 $\rho_W$ 列、$q$ 行）。于是：

* **有解** ⟹ 存在常数 intertwining（此时再谈有限初等因子相等的充分条件，专家 §3.2 的三档：严格等价 > 有限初等因子同 > 无）；
* **无解** ⟹ 专家 §3.3 的第 4 步：找出两支铅笔在定义域/值域上**多出的方向**，看它们是否只贡献奇异块或无穷因子。

**限定**：即使 intertwining 存在，也**不能**直接推出"有限初等因子相同"（专家明确）；需要核与余核的额外信息。


### 5. 对"intertwining 检验"的修正（本轮自查）

上一节把检验写成"找常数 $a,b$ 使 $b\overline N=P_Ka$"。**这个式子单独看是退化的**：

* 它对 $(a,b)$ 是**齐次**的 ⟹ $(a,b)=(0,0)$ 恒为解，故"有解"没有信息量；
* 必须加强，才是有意义的判据。两种加强：
  * **(E1) 严格等价**：要求 $a,b$ **可逆**（即 $\rho_W=\omega$ 且 $q=n-d$，尺寸先要匹配）；
  * **(E2) 单向吸收**：要求 $a$ **单射**且 $bN=P_Ka$ 对一对基成立（等价于 $\operatorname{range}(P_Ka)\subseteq\operatorname{range}(bN)$ 且 $a$ 不把 $V/S$ 压掉）。
* **尺寸必要条件（先查这个）**：严格等价要求两支铅笔同尺寸，即
$$\rho_W=\omega=\dim W_K\quad\text{且}\quad q=n-d,\qquad d=\dim(\mathcal Z).$$
一般情形这两条**不**成立（$P_K$ 是 $q\times\omega$，$\overline N$ 是 $(n-d)\times\rho_W$），
故**严格等价一般不可能**；能期望的只是专家 §3.2 的第二档："有限初等因子相同"。

**结论**：下一步不要直接解齐次系统（必有无穷多解），而应
① 先验尺寸条件；② 若尺寸不匹配，改为比较"去掉多出方向后"的两支铅笔（专家 §3.3 第 4–5 步）。

### 4. 现状

本节的**定义与系数对已钉死**；线性系统的求解与结论**尚未做**（要写一个带校验的探针：
先用 `consistency_checks` 生成可容许实例，再解上述系统）。在此之前不声称两支铅笔等价。

## 纸面证明

*证明*：1. $x\in S$ 时 $x\in\mathcal Z$ 给 $J_{\mathcal Z}x=x+\mathcal Z=0$；由 B.16b 的 $(5a)\Rightarrow A(S)\subseteq\mathcal Z$ 给
$T_{\mathcal Z}x=Ax+\mathcal Z=0$；故 $N_{\mathcal Z}(\lambda)x=0$。
2. 由 B.16(c)，失败 $\iff\exists\lambda:\ker N_{\mathcal Z}(\lambda)\not\subseteq S$；而 1 说 $S\subseteq\ker$ 恒成立，
故 $\neg$失败 $\iff\ker N_{\mathcal Z}(\lambda)=S\ \forall\lambda$。又 $\ker\overline N_{\mathcal Z}=\ker N_{\mathcal Z}/S$，
故"核 $=S$"$\iff$"$\overline N_{\mathcal Z}$ 单射"。
3. 多项式矩阵在一切有限 $\lambda$ 上单射 $\iff$ 极大子式无公共有限根 $\iff$ gcd 为非零常数（行列式因子论证）。
**注意**：这与"法秩满"**不同**（专家 2026-11-04 §2.2）：法秩满只排除**一般** $\lambda$ 的掉秩，不排除有限个 $\lambda$。$\square$


*意义*：这是**统一所有 $s$ 层的一条判据**——$s=0$ 时退化为 $N_{\mathcal Z}$ 本身，$s=\dim V$ 时条件空；
它取代了"$s>0$ 时必须用核判据"的分情形叙述（专家 §2.1 的更正）。

## Lean

* 等级行引用的 Lean 声明：`Criterion.permanent_kernel`、`Criterion.ker_eq_iff`
* 差在哪里：见等级行括注（内核一般只覆盖代数/维数骨架，矩阵实例化多为纸面）

## 精确验证

* `tools/verification/quotient_pencil.py`

## 状态与历史

*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`Criterion.permanent_kernel` 永久核、`Criterion.ker_eq_iff` 判据的核形式；差在"诱导映射 $W/S\to W$ 单射"的商空间表述）$+$ **[精确验证]**（**1513/1513** 个随机可容许 $(\mathcal Z,q)$ 样本上"商铅笔单射"与 B.12 可观性判据完全一致，`tools/verification/quotient_pencil.py`）。
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。



## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F2 |
| 导出等级 | **L3** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— Lean 已覆盖（内核） |


## 支撑目录

无（证据全部在本卷宗内）。

## 专家复核意见（成立）

永久核只用 $(5a)$；$(5b)\iff\ker N_Z(\lambda)=S\ \forall\lambda$ 的等价由精确失败判据得到。

---

## 附：分层判据（原 B.16）

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.16` 条目（§0.1 归并表）。

## 命题

**B.16（a）〔原 B.16〕（按 $\operatorname{rank}(J_{\mathcal Z}|_V)$ 的分层判据；专家 2026-11-04 §9 建议的分层纲领的第一步）**
设 $\mathcal Z\in\mathrm{Gr}(d,K)$ 可容许（$(5a)$ 成立），
$$S:=V\cap\mathcal Z,\qquad s:=\dim S\ (\in\{0,\dots,\min(d,\dim V)\}),$$
$$J_{\mathcal Z}:V\to X/\mathcal Z,\ x\mapsto x+\mathcal Z;\qquad
T_{\mathcal Z}:V\to X/\mathcal Z,\ x\mapsto Ax+\mathcal Z;\qquad
N_{\mathcal Z}(\lambda):=T_{\mathcal Z}-\lambda J_{\mathcal Z}.$$
注意 $\operatorname{rank}(J_{\mathcal Z}|_V)=\dim V-s$，故**按 $s$ 分层 = 按 $\operatorname{rank}(J_{\mathcal Z}|_V)$ 分层**
（也正是 G.1/G.2 编码里那个 $O(n)$ 项析取的参数）。则

* **(a)** $s=\dim V$（即 $V\subseteq\mathcal Z$）⟹ **谱可行**；
* **(b)** $s=0$ ⟹ 失败 $\iff\exists\lambda:\operatorname{rank}N_{\mathcal Z}(\lambda)<\dim V$
  $\iff$ 极大子式 gcd 有正次数（即铅笔有**有限零点**）；
* **(c)** 一般情形：失败 $\iff\exists\lambda:\ker N_{\mathcal Z}(\lambda)\not\subseteq S$。

## 纸面证明

*证明*：(a) 由 B.13c，失败需要 $x\in V\setminus\mathcal Z$；$V\subseteq\mathcal Z$ 时该集合为空。
(b) $\ker J_{\mathcal Z}=V\cap\mathcal Z=S=0$，故 $J_{\mathcal Z}$ 在 $V$ 上单射，于是对 $x\ne0$ 有 $J_{\mathcal Z}x\ne0$；
失败 $\iff\exists\lambda,x\ne0:N_{\mathcal Z}(\lambda)x=0\iff\operatorname{rank}$ 掉；对多项式矩阵，"$\exists\lambda$ 使秩掉"
$\iff$ 极大子式的 gcd 有正次数（B.8 之前的行列式因子论证）。 (c) $x\in\ker N_{\mathcal Z}(\lambda)$ 即
$T_{\mathcal Z}x=\lambda J_{\mathcal Z}x$；失败的附加要求是 $J_{\mathcal Z}x\ne0$，即 $x\notin\mathcal Z$；
而 $\ker N_{\mathcal Z}(\lambda)\subseteq V$，故"存在 $x\in\ker N_{\mathcal Z}(\lambda)\setminus(V\cap\mathcal Z)$"
$\iff\ker N_{\mathcal Z}(\lambda)\not\subseteq S$。$\square$


"gcd 有正次数" 与 B.12 可观性判据完全一致，`tools/verification/stratum_criterion.py`）。
*注（2026-11-04 推定的一步，**已否决**）*：曾猜想"中间层永不失败"，若成立则可把上述三条判据塌缩成 $s=0$ 一条。
该猜想**为假**：存在 $s=1$、$q=1$、$(5a)$ 成立而 $(5b)$ 失败的实例（此时 $U=\mathcal LV=\mathbb C^q$ 必然含特征向量）。
原因是**分层与失败条件并不同构**：$s=\dim V-\dim U$ 只约束 $U$ 的维数，而失败要求 $U$ 含 $\Lambda$ 的特征向量
（B.12）。所以 $s$-分层服务于记账（编码析取、可容许性），不简化谱条件。细节见 `attempts/78`。
*注*：(a) 说明"顶层（$\mathcal Z\supseteq V$）永远可行"——所以整族不可行只能发生在 $s<\dim V$ 的层；
(b) 说明 $s=0$ 层上判据**不需要**额外的 $x\notin\mathcal Z$ 条件（单射保证了它），这是最干净的层。

**B.16（b）〔原 B.16b〕（中间层的结构限制与一个反例）** 设 $\mathcal L$ 满足 $(5a)$、$\mathcal Z=\ker[C;\mathcal L]$、$S=V\cap\mathcal Z$。则

1. **（必要条件）** $A(S)\subseteq\mathcal Z$。即：中间层（$s>0$）上的可容许增广**必须**把 $S$ 映进 $\mathcal Z$；
2. 若还有 $A(S)\subseteq S$（$S\ne0$），则 $S$ 是 $\ker C$ 内的 $A$-不变子空间，与 $(C,A)$ 可观测矛盾；因此中间层上只能断言 $A(S)\subseteq\mathcal Z$ 而 $A(S)\not\subseteq S$——**不**能进一步说 $S$ 是"广义特征向量方向"（专家 2026-11-04 §6.1 的更正）；
3. **（反例）** 存在 $(5a)$-可容许、$s=1$ 的实例，其铅笔 $N_{\mathcal Z}(\lambda)$ 对**所有** $\lambda$ 都**不满列秩**
   （$\operatorname{rank}N_{\mathcal Z}(\lambda)=1<2=\dim V$），但 $(5b)$ **成立**——
   故 B.16(b) 的判据在中间层**无效**，必须用 (c) 的核判据。

*证明*：1. 由 $(5a)$ 存在 $T$ 使 $\mathcal LA=T[\mathcal L;CA;C]$。取 $x\in S$：$\mathcal Lx=0$、$Cx=CAx=0$，故
$(\mathcal LA)x=T[\mathcal Lx;CAx;Cx]=0$，即 $\mathcal L(Ax)=0$；又 $C(Ax)=CAx=0$，于是 $Ax\in\ker[C;\mathcal L]=\mathcal Z$。$\square$
2. 若 $A(S)\subseteq S$ 且 $S\ne0$，则 $S$ 是 $\ker C$ 内的 $A$-不变子空间，与 $\operatorname{rank}\mathcal O(C,A)=n$ 矛盾。
3. 具体实例（$n=p+r+2=6$、$p=r=2$、$\dim V=\dim K=2$、$\dim(V\cap K)=1$）：
$$A=\begin{pmatrix}2&-1&1&-1&1&0\\-2&-2&1&0&-1&1\\-2&0&-2&2&0&2\\0&0&-1&1&-2&2\\0&0&0&1&-2&-2\\-2&1&-1&-1&-2&1\end{pmatrix},\
C=\begin{pmatrix}2&0&1&0&1&2\\1&0&0&-1&0&1\end{pmatrix},\
L_0=\begin{pmatrix}1&0&-1&1&0&1\\1&0&1&0&2&1\end{pmatrix},$$
取 $\mathcal Z=K$（$d=2$）则 $s=1$；$(5a)$ 成立、$\operatorname{rank}\mathcal L=2$，而 $(5b)$ 经 B.12 核验**成立**；
同时 $\operatorname{rank}N_{\mathcal Z}(\lambda)\equiv1$（$\lambda=0,\pm1,\pm2,3$ 全部为 1）。
*意义*：这条反例把"**压缩不满列秩 $\ne$ 谱失败**"从口头提醒变成显式实例（正如专家 2026-11-04 §1.4 所告诫），
并说明中间层必须用核判据。

## Lean

* 等级行引用的 Lean 声明：`Criterion.b16b_mapsTo`、`RowSpace`
* 差在哪里：见等级行括注（内核一般只覆盖代数/维数骨架，矩阵实例化多为纸面）

## 精确验证

* 见等级行给出的精确验证数字。

## 状态与历史

*等级*：**[已证-纸面]** $+$ **[精确验证]**（$s=0$ 层：402 个随机可容许 $(\mathcal Z,q)$ 样本上
*等级*：1、2 **[已证-纸面]** $+$ **[Lean-conditional]**（`Criterion.b16b_mapsTo`：抽象映射层面，矩阵实例化见 `RowSpace`）；3 **[精确验证]**（有理算术）。
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。



## 验证状态

| 维度 | 状态 |
|---|---|
| 纸面证明 | 完整（`## 纸面证明` 一节，可直接用于写论文）|
| 专家复核 | **已复核：成立**（依据 `25_review_checklist-answer.md`）|
| Lean | `[Lean-conditional]` —— 内核覆盖代数/维数骨架，矩阵实例化仍是纸面 |
| 精确验证 | [精确验证] |

## 支撑目录

无（证据全部在本卷宗内）。

## 专家复核意见（成立）

中间层（$0<s<\dim V$）的正确判据是 $\exists\lambda:\ker N_Z(\lambda)\not\subseteq S$，**不能**用 $N_Z(\lambda)$ 满列秩；该判据对固定 $Z$ 可代数判定，但对"$\exists Z$"仍只是半代数可行性。

---

## 附：右零空间与指标（原 B.21）

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.21` 条目（§0.1 归并表）。

## 命题

**B.21（右零空间与指标：$s=n-h$、$\sum_j\eta_j=0$）** 设 $\mathcal L$ 可容许、$S=V\cap\mathcal Z$、$s=\dim S$、
$h=\operatorname{rank}[\mathcal L;CA;C]$、$Q_{\mathcal L}(\lambda)=[\lambda\mathcal L-\mathcal LA;CA;C]$。则

1. **$s=n-h$**。由对偶：$S=V\cap\mathcal Z=W^\perp\cap\mathcal Z$，故 $S^\perp=W+\mathcal Z^\perp$，于是
   $s=n-\dim(W+\mathcal Z^\perp)=n-h$。
2. **右零空间 $=S[\lambda]$**：$Q_{\mathcal L}(\lambda)x(\lambda)=0$（$x\in\mathbb C[\lambda]^n$）$\iff$ $x(\lambda)\in S[\lambda]$。
   证明：$C$ 块与 $CA$ 块逐系数给 $x_i\in V$；$\mathcal L$ 块用 $\mathcal LAy=\Lambda\mathcal Ly$（$y\in V$）化为
   $(\lambda I-\Lambda)\mathcal Lx(\lambda)=0$，而 $\lambda I-\Lambda$ 在 $\mathbb C(\lambda)$ 上可逆，故 $\mathcal Lx(\lambda)=0$，
   即 $x_i\in V\cap\ker\mathcal L=S$。反向：$S[\lambda]$ 显然在右零空间里（用 B.16b 给 $A(S)\subseteq\mathcal Z$）。
3. **推论**：$Q_{\mathcal L}$ 的右最小指标共 $n-h=s$ 个，且**全部为零次**；于是
$$\sum_j\eta_j=0 .$$

*意义*：把等号情形的 Kronecker 记账进一步钉死：$\sum\varepsilon=0$（B.9 第 4 步）、$\sum\eta=0$（本条），
故恒等式 $h=\sum\varepsilon+\sum\eta+d_{\rm fin}+d_\infty$ 在等号时化为
$$d_{\rm fin}+d_\infty=h=q+r_1 .$$
于是等号排除定理等价于 $d_\infty<h$（即：铅笔必有非平凡的有限初等因子）。
**这一点已由 B.22 给出更强结论**：等号时 $d_{\rm fin}=q$、$d_\infty=r_1$，故 $d_\infty=r_1<h=q+r_1$（$q\ge1$）✓。
*附记（错误路线的记录）*：$d_\infty$ **不能**由 $\operatorname{rank}A_0,\operatorname{rank}A_1,h$ 决定——反例
$\begin{pmatrix}1&\lambda\\0&1\end{pmatrix}$（$h=2$、$\operatorname{rank}A_1=1$、$\det\equiv1$ 故 $d_\infty=2$）；
$\nu_\infty:=h-\operatorname{rank}A_1$ 数的是无穷初等因子的**个数**（专家 §Q1.2）。

*等级*：**[已证-纸面]**（1、2、3）；**[精确验证 650/650]**（1 的恒等式）。 $+$ **[Lean-conditional]**（`B21.dim_inf_ker`；差在矩阵翻译）。
*注*：第 1 条 $s=n-h$ 值得单独记住：它说明"交集维数"与"秩亏损"完全对偶。

## 纸面证明

*（证明内联于下方等级行与支撑目录，未单独拆出）*

## Lean

* 无独立 Lean 内核（该条为纸面证明）。

## 精确验证

* 该条暂无独立精确验证脚本（纸面证明 + 支撑目录）。

## 状态与历史

* 等级：见 docs/02 同条目。
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。



## 验证状态

| 维度 | 状态 |
|---|---|
| 纸面证明 | 完整（`## 纸面证明` 一节，可直接用于写论文）|
| 专家复核 | **已复核：成立**（依据 `25_review_checklist-answer.md`）|
| Lean | `[Lean-conditional]` —— 内核覆盖代数/维数骨架，矩阵实例化仍是纸面 |
| 精确验证 | [精确验证 650/650] |

## 支撑目录

无（证据全部在本卷宗内）。

## 专家复核意见（成立）

$s=n-h$ 与右零空间 $=S\otimes\mathbb C[\lambda]$ 都正确；**不需要** $q\ge1$。
