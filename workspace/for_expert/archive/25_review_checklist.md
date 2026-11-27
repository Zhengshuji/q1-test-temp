# 送审清单：24 条尚未复核的命题

这份清单只列**尚未经过你复核**的 24 条主条目（另有 7 条已复核：B.18、B.22、B.25、B.28、B.31、B.32 与 B.12）。

每条给出：陈述（要点）、证明的**关键一步**、现有机器证据、以及**希望你先看哪一点**。

记号与 $(5a)/(5b)$ 的定义沿用前几份报告。每条命题都有独立的"卷宗"（陈述 + 完整纸面证明 + 机器检查记录 + 精确验证数字），需要时可随清单一起寄出。


---


## 第一档：框架与复杂度（$q1$ 直接相关）

| # | 条目 | 陈述要点 | 关键一步 | 现有证据 | 请确认 |
|---|---|---|---|---|---|
| 1 | **A.1** | **A.1（a）〔原 A.0〕（$(5a)$ 的商形式——**再次校正**）** 记 $\mathcal J=\operatorname{row}[C;CA]$、$U=\pi(\mathcal V)$、$B=\pi(\mathcal J A)$。 则 $$(5a)\iff \pi(\mathcal V A)\subseteq\pi(\mathcal V).$$ | 分解的正合性 + 两个下界的可加性（$\min(f+g)$ 与 $\min f+\min g$ 的关系） | `[Lean]`；[精确验证 20/20] | 下界是否只在"$\mathcal L$ 行满秩 + 含 $L_0$"的范围内成立？A.2 里 $c\ge c_0$ 与 $c\ge1$ 能否同时取到？ |
| 2 | **D.1** | **D.1（a）〔原 D.1〕（下界）** $P(A,B,S)\ge\dim S+\dim\frac{AS+S+B}{S+B}$。 | 一步递归 $P=\min\{\dim U: T\subseteq U,\ \Phi(U)\subseteq(U+C)/C\}$ 的正确性与终止性 | `[Lean]`；无独立精确验证脚本（纸面证明已完整，见 `## 纸面证明`） | $\Phi'$ 的良定义与"截面"一步是否隐含 $\mathcal J$-不变性假设？ |
| 3 | **G.1** | **G.1（a）〔原 G.1〕** $\mathrm{DEC}(q)\in\exists\mathbb R$（chart-free 编码；变量/方程 $O(n^3)$、次数 $\le n$、$O(n)$ 个 $s$ 分支）。 *证明要点*：$Z$-表述（无图卡析取）$+$ 核心引理 $\ker(CAZ)=Z\cap\mathcal V$（故 $(A)\iff A(S)\subseteq Z$） $+$ 多项式左逆证书 $X(\lambda)P(\lambda)=I_t$（$\deg X\le t-1$）。 **等级**：[已证-纸面] $+$ 两实例精确验证 $+$ **部分 [Lean]**（`CoreLemma` 的核心引理、`ExistsRLemmas` 的左逆 $\Rightarrow$ 单射；$\exists\mathbb R$ 的**编码规模**不是 Lean 的对象）。  | 把"$\exists\Theta$ 的图卡半代数判定"编码为多项式方程组 | `[Lean]`；[精确验证] | 编码规模 $O(n^3)$ 与次数 $\le n$ 是否在你的编码惯例下成立？ |
| 4 | **F.1** | **F.1（a）〔原 F.1〕（秩屏障）** 设 $\mathcal L$ 是层 $(\rho,c)$ 的任一候选（$\rho=\dim\pi(\mathcal V)$、$c=\dim(\mathcal V\cap\mathcal J)$）。 对 $\lambda_0\in\mathbb C$ 记 $$r(\lambda_0):=\dim\pi\big(\mathbb C^n(\lambda_0I-A)\big)=\operatorname{rank}[\lambda_0I-A;\,C;\,CA]-j .$$ 则：**若 $(5b)$ 在 $\lambda_0$ 处成立，必有 $\rho\le r(\lambda_0)$。** 特别地，若 $\rho>\min_{\lambda}r(\lambda)$，该层**不可行**。 | $(5b)$ 在 $\lambda_0$ 处 $\Rightarrow$ $\dim\pi_J(\mathrm{range}(\lambda_0I-A))\ge\rho$ | `[Lean-conditional]`；[精确验证 1484+113] | 秩屏障是否只能作为"必要条件"使用（即它不可反过来充分）？ |
| 5 | **H.1** | **H.1（a）〔原 H.1〕（商等价定理 Theorem Q）** 设 $Z\subseteq H$、$S=Z\cap V$、$A(S)\subseteq Z$、$U=Z/S$、 $P(\lambda)=(A-\lambda I)|_{V/S}$。则 $$\operatorname{rank}\big[(\lambda I-A)V\mid Z\big]=\dim(V+Z) \iff \operatorname{rank}\big[U\mid P(\lambda)\big]=r+t .$$ | $[U\mid P(\lambda)]$ 的方阵性与 $q=t$ 的等价 | `[Lean]`；[精确验证 18 个 $Z$] | Theorem Q 的假设 $A(S)\subseteq Z$ 是否可由 $(5a)$ 推出，还是必须单列？ |


## 第二档：铅笔与结构定理

| # | 条目 | 陈述要点 | 关键一步 | 现有证据 | 请确认 |
|---|---|---|---|---|---|
| 1 | **B.1** | **B.1（商铅笔）** $(5b)\iff\operatorname{rank}Q_{\mathcal V}(\lambda)=\rho\ \forall\lambda$，$Q_{\mathcal V}(\lambda)=\lambda\pi(\mathcal L)-\pi(\mathcal LA)$。 | 对 $\mathcal J$ 取商后秩条件的等价 | `[Lean]`；无独立精确验证脚本（纸面证明已完整，见 `## 纸面证明`） | 商铅笔的秩是否在 $\lambda$ 处退化时仍与该式一致？ |
| 2 | **B.2** | **B.2（a）〔原 B.2〕（顶层）** 若 $\rho=d$，则 $(5b)\iff(D_W^{\mathsf T},T_W)$ **可观测**。 | PBH 与顶层块的压缩 | `[Lean-conditional]`；[精确验证 35/35] | "顶层"假设 $\rho=d$ 是否只在这一层成立（$\mathcal V$ 满维）？ |
| 3 | **B.3** | **B.3（$\rho=0$ 层）** $\rho=0\iff\mathcal V\subseteq\mathcal J$；此时 $(5a)\iff S\subseteq\mathcal J$ 且 $SA\subseteq\mathcal J$，且 $(5b)$ 自动。 | 直接由 $(5a)$ 得出 | `[Lean]`；无独立精确验证脚本（纸面证明已完整，见 `## 纸面证明`） | $(5a)\iff S\subseteq\mathcal J$ 那一步是否需要 $L_0\ne0$？ |
| 4 | **B.4** | **B.4（$V=\mathbb C^n$ 可行性）** $\mathcal V=\mathbb C^n$ 满足 $(5b)$ $\iff$ $A^{\mathsf T}$ 没有落在 $K=\ker[C;CA]$ 里的特征向量。 **等级**：[已证] $+$ **[Lean]**（`B4FullSpace.b4_iff_no_eigenvector` = 本条陈述；`B4FullSpace.b4_finrank_iff` = 对偶维数判据 $\dim(ME+J)=n\iff\ker M^{\mathsf T}\cap J^{\perp}=0$）。 | 特征向量与核的交 | `[Lean]`；无独立精确验证脚本（纸面证明已完整，见 `## 纸面证明`） | 该判据在 $p\ge2$ 时是否仍只需单特征向量？ |
| 5 | **B.6** | **B.6（a）〔原 B.6〕（右最小指标为零）** 设 $L$ 满足 $(5a)$。则观测器铅笔 $Q_L(\lambda)=[\lambda L-LA;CA;C]$ 的**右最小指标全为 $0$** （右零模有常值基）。只用 $(5a)$，不需要 $(5b)$。 | 按 $\lambda$ 的幂展开 + 反转铅笔 | `[Lean-conditional]`；[精确验证 150/150] | "右零模由常值向量生成"是否等价于右指标全 0（模基 vs 向量基）？ |
| 6 | **B.8** | **B.8（a）〔原 B.8a〕（Smith 判据；(5b) $\iff$ 无有限初等因子）** 设 $L$ 满足 $(5a)$、$h=\operatorname{rank}[L;CA;C]$。则 $$(5b)\iff d_{\rm fin}=0,$$ 其中 $d_{\rm fin}$ 是 $Q_L(\lambda)$ 的 Smith 形中**非零不变因子的次数之和**（等价地：有限初等因子的总大小）。 | Smith 形与极大子式 gcd 的关系 | 无 Lean（纸面）；[精确验证] | $q\ne t$（矩形）时 $\Delta_b=d_1\cdots d_b$ 是否仍成立？ |
| 7 | **B.9** | **B.9（a）〔原 B.9〕（必要条件 $h<q+r_1$）** 设 $\mathcal L$ 行满秩、含 $L_0\ne0$，$h=\operatorname{rank}[\mathcal L;CA;C]$、$r_1=\operatorname{rank}[C;CA]$、$s=\operatorname{rank}\mathcal L$。则 $Q_{\mathcal L}=[\lambda\mathcal L-\mathcal LA;CA;C]$ 有 $2p-r_1$ 个零左指标，非零左指标个数为 $q+r_1-h$；因此 $$(5b)\ \Longrightarrow\ h<q+r_1 .$$ | 交非零 $\Rightarrow$ 秩严格小于和 | `[Lean-conditional]`；[精确验证 56/56] | $L_0\ne0$ 是否是"交非零"的唯一充分条件？ |
| 8 | **B.10** | **B.10（a）〔原 B.10〕（谱障碍的定域）** 设 $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$，$Q_{\mathcal L}=D(\lambda)H$（$H=[\mathcal L;CA;C]$）。则 $$\lambda\notin\operatorname{spec}\Lambda\ \Longrightarrow\ \operatorname{rank}Q_{\mathcal L}(\lambda)=h .$$ | $Q_{\mathcal L}=D(\lambda)H$ 的块结构 | 无 Lean（纸面）；[精确验证 3/3] | 定域性是否依赖 $\Lambda$ 的对角化？ |
| 9 | **B.11** | **B.11（a）〔原 B.11〕（$h$ 的几何公式）** 设 $\mathcal L$ 行满秩、$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$， $\mathcal Z=\ker[C;\mathcal L]$、$W=\operatorname{row}[C;CA]$。则 $$h=\operatorname{rank}[\mathcal L;CA;C]=\dim(\mathcal Z^{\perp}+W),$$ 且 $h=q+r_1-\delta$，$\delta=\dim(\mathcal Z^{\perp}\cap W)-p\ge0$。 | 行空间与商空间的维数记账 | `[Lean-conditional]`；[精确验证] | Type I 的二分是否穷尽 $p=r=1$ 的所有几何型？ |


## 第三档：特殊层与工具性结论

| # | 条目 | 陈述要点 | 关键一步 | 现有证据 | 请确认 |
|---|---|---|---|---|---|
| 1 | **C.1** | **C.1（$S=\mathcal J$ 闭包族）** 若 $\operatorname{row}(L_0)=\mathcal J$ 且 $\langle\mathcal J\rangle_A=\mathbb C^n$，则唯一可行解是 $\mathbb C^n$，$q_{\min}=n$。 | 闭包的极小性 | `[Lean]`；无独立精确验证脚本（纸面证明已完整，见 `## 纸面证明`） | 该结论是否对 $r\ge2$ 仍成立？ |
| 2 | **B.13** | **B.13（a）〔原 B.13〕（incidence variety 的维数与"整族不可行"的覆盖判据；专家  §5 的建议）** 记 $V=\ker[C;CA]$、$K=\ker[C;L_0]$，并设 $h=n$（此时 $(5a)$ 对**每个** $\mathcal Z\subseteq K$ 自动成立，见 3.4）。 考虑 incidence variety $$\mathfrak I=\{([x],\lambda,[z]):\ x\in V\setminus0,\ L_0x\ne0,\ z=(\lambda I-A)x\ne0,\ z\in K\}\subseteq\mathbb P(V)\times\mathbb P^1\times\mathbb P(K),$$ 及其到 $\mathbb P(K)$ 的投影像 $S$（"坏点直线"全体）。 *命题*： 1. **$\lambda$ 与 $z$ 被 … | 入射簇的维数计数 | `[Lean-conditional]`；[精确验证] | 覆盖判据的充分性在 $q\ne t$ 时是否需要额外假设？ |
| 3 | **B.14** | **B.14（一个可判的多项式时间可解类：投影铅笔满列秩）** 设 $B_V$ 为 $V=\ker[C;CA]$ 的基，$P_K$ 为满行秩、 $\ker P_K=K$ 的矩阵（$K=\ker[C;L_0]$）。若 $$\operatorname{rank}\bigl(P_K(\lambda I-A)B_V\bigr)=\dim V\qquad\forall\lambda\in\mathbb C, \tag{T*}$$ 则该实例**在每一阶都谱可行**：任何 $\mathcal Z\subseteq K$、任何 $x\in V$，若 $(\lambda I-A)x\in\mathcal Z\subseteq K$ 则 $P_K(\lambda I-A)x=0$，由 (T*) 得 $x=0$，与 B.13c 要求的 $x\in V\setminus\mathcal Z$ 矛盾。$\square$ *判据实现*：$P_K(\lamb… | $P_K$ 与投影铅笔的构造 | 无 Lean（纸面）；[精确验证] | 该类的定义是否依赖基的选择？ |
| 4 | **B.15** | **B.15（阶差无界：$k$ 个同型副本的直和把阶差乘以 $k$）** 设单副本 $(A_1,C_1,L_{0,1})$ 满足 $$V_1\cap K_1=0\quad\text{且}\quad\exists\lambda_0:\ (\lambda_0I-A_1)V_1=K_1\qquad(\dim V_1=\dim K_1),$$ 并设它在某阶 $q_1$ 有可行的增广 $\mathcal L_1$（如 $q_1=q_{\min}$），且 $d_1=n_1-p_1-q_1=0$。 取 $k$ 重直和 $(A,C,L_0)=(A_1,C_1,L_{0,1})^{\oplus k}$（于是 $n=kn_1$、$p=kp_1$）。则 1. $V=V_1^{\oplus k}$、$K=K_1^{\oplus k}$、$V\cap K=0$，且 $(\lambda_0I-A)V=K$（**同一个** $\lambda_0$）； 2. … | 维数计数 + 有限并的余维 | `[Lean-conditional]`；[精确验证] | 引理对 $\mathbb C$ 上的薄集是否只需"非空开集"？ |
| 5 | **B.16** | **B.16（a）〔原 B.16〕（按 $\operatorname{rank}(J_{\mathcal Z}|_V)$ 的分层判据；专家  §9 建议的分层纲领的第一步）** 设 $\mathcal Z\in\mathrm{Gr}(d,K)$ 可容许（$(5a)$ 成立）， $$S:=V\cap\mathcal Z,\qquad s:=\dim S\ (\in\{0,\dots,\min(d,\dim V)\}),$$ $$J_{\mathcal Z}:V\to X/\mathcal Z,\ x\mapsto x+\mathcal Z;\qquad T_{\mathcal Z}:V\to X/\mathcal Z,\ x\mapsto Ax+\mathcal Z;\qquad N_{\mathcal Z}(\lambda):=T_{\mathcal Z}-\lambda J_{\mathcal Z}.$$ … | 三层判据（$s=0$/中间/$s=\dim V$） | `[Lean-conditional]`；[精确验证] | 中间层的判据是否可判定（还是只有存在性）？ |
| 6 | **B.17** | **B.17（永久核与商铅笔判据；专家  §2.1/§5 给出，本项目核验）** 设 $\mathcal L$ 满足 $(5a)$、 $\mathcal Z=\ker[C;\mathcal L]$、$S=V\cap\mathcal Z$、$N_{\mathcal Z}(\lambda)=T_{\mathcal Z}-\lambda J_{\mathcal Z}$。则 1. **永久核**：$S\subseteq\ker N_{\mathcal Z}(\lambda)$ 对**一切** $\lambda$ 成立； 2. **商判据**： $$(5b)\ \text{成立}\iff\ker N_{\mathcal Z}(\lambda)=S\ \ \forall\lambda \iff \overline N_{\mathcal Z}(\lambda):V/S\to X/\mathcal Z\ \text{对一切… | 永久核的构造 | `[Lean-conditional]`；[精确验证] | 永久核在 $(5a)$ 之外是否还需要 $(5b)$？ |
| 7 | **B.21** | **B.21（右零空间与指标：$s=n-h$、$\sum_j\eta_j=0$）** 设 $\mathcal L$ 可容许、$S=V\cap\mathcal Z$、$s=\dim S$、 $h=\operatorname{rank}[\mathcal L;CA;C]$、$Q_{\mathcal L}(\lambda)=[\lambda\mathcal L-\mathcal LA;CA;C]$。则 1. **$s=n-h$**。由对偶：$S=V\cap\mathcal Z=W^\perp\cap\mathcal Z$，故 $S^\perp=W+\mathcal Z^\perp$，于是 $s=n-\dim(W+\mathcal Z^\perp)=n-h$。 2. **右零空间 $=S[\lambda]$**：$Q_{\mathcal L}(\lambda)x(\lambda)=0$（$x\in\mathbb C[\lambda]^n… | 维数记账 + 右零空间结构 | `[Lean-conditional]`；[精确验证 650/650] | $\eta_j=0$ 的推导是否用到 $q\ge1$？ |
| 8 | **B.23** | **B.23（谱侧的统一因子化：$Q_{\mathcal L}(\lambda)=P(\lambda)H_0$）** 设 $\mathcal L$ 满足 $(5a)$、$\operatorname{rank}\mathcal L=q$； 取 $B\in\mathbb C^{r_1\times n}$ 满行秩且 $\operatorname{row}B=\operatorname{row}[CA;C]$，令 $H_0=[\mathcal L;B]$。由 $(5a)$ 的 $\operatorname{row}(\mathcal LA)\subseteq\operatorname{row}H_0$ 得 $\mathcal LA=KH_0$，记 $K=[K_1\ K_2]$（$K_1$ 为 $q\times q$、$K_2$ 为 $q\times r_1$）。则 $$Q_{\mathcal L}(\lambda)=\begin{bma… | 块三角分解 | `[Lean-conditional]`；[精确验证 8128/8128] | $\det P=\det(\lambda I_q-K_1)$ 是否需要 $K_1$ 的特定形式？ |
| 9 | **B.24** | **B.24（内蕴形式：偏算子 $\Phi$ 的特征向量；专家  §2.1 的改进）** 设 $\mathcal L$ 满足 $(5a)$、 $\operatorname{rank}\mathcal L=q$，$W:=\mathcal LV\subseteq\mathbb C^q$。定义**偏算子** $$\Phi:W\longrightarrow\mathbb C^q,\qquad \Phi(\mathcal Lx):=\mathcal LAx\quad(x\in V).$$ 则 1. **$\Phi$ 良定义**：若 $\mathcal Lx_1=\mathcal Lx_2$（$x_i\in V$），则 $s=x_1-x_2\in S=V\cap\ker\mathcal L$；由 $(5a)$ 的因子化 $\mathcal LA=K_1\mathcal L+K_2B$ 得 $\mathcal LAs=K_… | $\Phi(\mathcal Lx)=\mathcal LAx$ 诱导的特征向量等价 | 无 Lean（纸面）；[精确验证 3453/3453] | $\Phi$ 的良定义是否依赖 $\mathcal L$ 行满秩？ |
| 10 | **K.1** | **K.1（a）〔原 K.1〕** $m=3$：每个非零双向量都可分解（$\mathrm{Gr}(2,3)=\mathbb P(\Lambda^2\mathbb C^3)$）。[已证-纸面] **K.1（b）〔原 K.2〕** $m=4$ 且 $\ell\ge2$：$q|_K$ 是 $\ge2$ 元二次型，$\mathbb C$ 上必有非零零点 ⟹ 必有可分解元； $\ell=1$ 时退化为 $q(p_0)=0$。[已证-纸面] $+$ [精确验证 20/20] $+$ **[Lean-conditional]** （`Isotropy.exists_root_quadratic`：$a\ne0$ 时 $at^2+bt+c$ 在代数闭域有根； `Isotropy.exists_ne_zero_quadraticMap_eq_zero`：$\dim\ge2$ 的二次型有非零零点； `Isotropy.K2_isotropic`：限… | 二次型的各向同性 + 维数计数 | `[Lean-conditional]`；[精确验证 20/20] | $m=4,\ell\ge2$ 的论证在 $\mathbb C$ 上是否需要非退化假设？ |


---

## 请求

1. 请按档位顺序（第一档先）指出**哪一条的证明不成立或有缺口**；我们按你的意见逐条改。

2. 对每条只需给"成立 / 有缺口（指出哪一步）/ 需要额外假设"三者之一。

3. 若某条的**关键一步**你认为需要换证法，请给一句方向即可。

4. 清单里的"现有证据"一栏：`[Lean-conditional]` 表示内核已机器检查但只覆盖代数/维数骨架；无 Lean 表示纯纸面 —— 请把它作为可信度的参考，不要当作证明。
