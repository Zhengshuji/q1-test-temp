# 谱条件的几何：把 O1 修正成正确的引理（2026-10-30，回应专家 QA9）

> **对应 docs 条目**：B.13（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

> 背景：我们在给专家的报告里写了"incidence 簇闭 ⟹ 投影闭 ⟹ (14b) 是开条件"（观察 O1）。
> 专家指出：**仿射簇的投影一般不必闭**（例：$\{(\theta,\lambda):\theta\lambda-1=0\}$ 投影到 $\theta$ 是 $\mathbb C\setminus\{0\}$）。
> 本文件把这个观察修正为**对本文铅笔成立**的引理，并给出证明；同时给出 (14b) 的 Bézout 表述 ⟹ $\mathrm{DEC}\text{-}\Theta\in\exists\mathbb R$。
>
> 记号（P2，arXiv:2609.37992 Thm 5/6）：固定阶 $q$、$d=n-p-q$、$h(\Theta)=\operatorname{rank}[V\mid Z(\Theta)]$，
> $$P_{\Theta}(\lambda)=[(\lambda I-A)V\mid Z(\Theta)],\qquad (14b):\ \operatorname{rank}P_\Theta(\lambda)=h(\Theta)\ \ \forall\lambda\in\mathbb C .$$
> 其中 $Z(\Theta)=K_LW_I(\Theta)$，$W_I(\Theta)=P_I^{\mathsf T}\binom{I_d}{\Theta}$，$\Theta\in\mathbb R^{(m_L-d)\times d}$；
> $V$ 的列张成 $\ker[C;CA]$（固定）。

## 1. 引理 1（$\lambda=\infty$ 处没有"假失败"）—— **必须在 $(A)$ 下陈述**（2026-10-30 更正）

记 $\mathcal V=\operatorname{col}V$（$\dim=n-r_1$）。对固定 $\Theta$，写 $Z=Z(\Theta)$、$h=\operatorname{rank}[V\mid Z]$。

**引理 1**（假设 $(A)$）：存在 $R>0$（依赖 $\Theta$），使得 $|\lambda|>R$ 时 $\operatorname{rank}P_\Theta(\lambda)=h$。

> **为什么必须加 $(A)$**（专家 QA10 的反例）：取 $V=[e_1,e_2]$、$Z=[e_1]$、$Ae_1=e_3$、$Ae_2=0$。
> 则 $\operatorname{rank}[V\mid Z]=2$，但 $P(\lambda)=[\lambda e_1-e_3,\ \lambda e_2,\ e_1]$ 的**一般秩是 3**；
> $\lambda\to\infty$ 时秩**变大**而不是稳定到 $h$。所以单靠"列空间收敛"不够。

*证明（用 $(A)$）*：由 $(A)$（$\operatorname{rank}[Z,AZR_Z]=d$、$Z$ 列满秩）得 $AZR_Z\subseteq\operatorname{im}Z$。
对 $x\in S=\mathcal V\cap\operatorname{im}Z$：$x=Z\alpha$ 且 $CAZ\alpha=0$ ⟹ $\alpha=R_Z\beta$ ⟹ $Ax=AZR_Z\beta\in\operatorname{im}Z$。
于是 $(\lambda I-A)x=\lambda x-Ax\in\operatorname{im}Z$ 对所有 $\lambda$ 成立，
故 $v\mapsto(\lambda I-A)v+\operatorname{im}Z$ 在 $S$ 上为零，$\operatorname{rank}P_\Theta(\lambda)\le\dim(\mathcal V+Z)=h$ 对所有 $\lambda$。
另一方面 $h\times h$ 子式的 $\lambda$-首项系数非零（$\operatorname{rank}[V\mid Z]=h$），
故 $\operatorname{rank}P_\Theta(\lambda)=h$ 对充分大的 $|\lambda|$ ✓。$\square$

**推论**：在 $\Omega^\star_I=\{\Theta:(14a)\}$ 上（那里 $\operatorname{rank}P_\Theta(\lambda)\le h$），“脏”的 $\lambda$ 集合**有界**；
即用 $\mathbb P^1$ 紧化不会把 $\lambda=\infty$ 误算成失败。

> **紧化的正确做法**（专家 QA10 §2.2）：不要直接齐次化 $[(tI-sA)V\mid sZ]$（$\infty$ 处给 $[tV\mid0]$、秩是 $\dim V$ 而非 $h$）；
> 应改用**商铅笔** $\lambda\iota-\bar A$（见 [proof/h_bound/README.md](../h_bound/README.md) 的 Theorem D）再紧化。

## 2. 引理 2（修正后的 O1：不是"闭"，而是"分层闭/可构造"）

**引理 2**：对每个整数 $c$，令 $S_c=\{\Theta:\ h(\Theta)=c\}$（局部闭的分层）。则在 $S_c$ 上
$$\mathrm{Bad}_c:=\{\Theta\in S_c:\ \exists\lambda\in\mathbb C,\ \operatorname{rank}P_\Theta(\lambda)\le c-1\}$$
是 $S_c$ 中的**闭集**；于是 $\mathrm{Good}_c:=S_c\setminus\mathrm{Bad}_c$ 在 $S_c$ 中是**开集**。

*证明*：$W_c=\{(\Theta,\lambda)\in \Omega^\star_I\times\mathbb C:\ \operatorname{rank}P_\Theta(\lambda)\le c-1\}$ 是闭集（子式方程）。
由引理 1，$|\lambda|\gg1$ 时 $\operatorname{rank}P_\Theta(\lambda)=h(\Theta)=c>c-1$，故 $W_c$ 的 $\lambda$-纤维有界。
取 $W_c$ 在 $\Omega^\star_I\times\mathbb P^1$ 中的闭包 $\overline{W_c}$；由引理 1，$\overline{W_c}$ 在 $\lambda=\infty$ 处没有点
（那里秩 $=c$），故 $\overline{W_c}=W_c$ 作为 $\mathbb P^1$-闭集，而 $\Omega^\star_I\times\mathbb P^1\to\Omega^\star_I$ 是 proper，
像 $\mathrm{Bad}_c$ 闭。$\square$

**结论（修正的 O1）**：
$$\text{“}(14b)\text{ 失败”是 \textbf{可构造集}（Chevalley），在每个秩层 }S_c\text{ 上是闭的；}\ \text{它不是无条件闭的。}$$
专家举的 $\theta\lambda-1$ 反例正对应"$h$ 随 $\Theta$ 变化"或"$\lambda=\infty$ 处秩降"的情形；在我们的铅笔里后者不会发生（引理 1）。

**对一般点归约的影响**（专家 §3）：因此正确的表述是**分层 + 逐分量**的：
$$\exists\Theta\in\Omega^\star_I\ \text{满足 }(14b)\iff \exists c,\ \exists\ \text{不可约分量 }X\subseteq S_c\ \text{使}\ X\not\subseteq\mathrm{Bad}_c .$$
在**实**参数上还需要专家 §3.1 的条件（$X$ 定义在 $\mathbb R$ 上、$X(\mathbb R)$ 在 $X$ 中 Zariski 稠密），否则复不可约性说明不了实可行性（反例 $x^2+y^2=0$）。

## 3. 引理 3（Smith 形式证书）与定理：$\mathrm{DEC}\text{-}\Theta\in\exists\mathbb R$

> 专家建议用 Bézout 恒等式消掉 $\forall\lambda$。对**多个**极大子式直接列 Bézout 会引入"子式个数"；
> 正确的矩阵版是**一次多项式等价**（Smith 形式），它把"$\forall\lambda$ 秩 $=h$"变成**一个**多项式恒等式。

**引理 3（Smith 证书）**：$P_\Theta(\lambda)$ 为 $n\times m$ 铅笔（$m=n-r_1+d$），$h=\operatorname{rank}[V\mid Z]$。则在 $(14a)$ 下
$$(14b)\ \Big(\operatorname{rank}P_\Theta(\lambda)=h\ \forall\lambda\Big)
\iff \exists U\in\mathbb R[\lambda]^{n\times n},\ V\in\mathbb R[\lambda]^{m\times m},\ \deg U,\deg V\le D:\quad
U(\lambda)P_\Theta(\lambda)V(\lambda)=\begin{pmatrix}I_h&0\\0&0\end{pmatrix},\quad \det U,\ \det V\in\mathbb R\setminus\{0\}.$$

*证明*：
$(\Leftarrow)$：$U,V$ 的行列式是非零常数 ⟹ 可逆 ⟹ $\operatorname{rank}P=\operatorname{rank}\operatorname{diag}(I_h,0)=h$ 对所有 $\lambda$ ✓。
$(\Rightarrow)$：$\operatorname{rank}P(\lambda)=h$ 对所有 $\lambda\in\mathbb C$ ⟹ $P$ 在 $\mathbb R[\lambda]$ 上的 Smith 形式是 $\operatorname{diag}(1,\dots,1,0,\dots,0)$（$h$ 个 $1$）⟹ 存在幺模 $U,V$ 把它变成该常数矩阵 ✓。
次数界：**未证（这是 ∃R 证明的唯一剩余缺口）**。标准 Smith 算法逐列/逐行做初等变换，
已知可给出 $\deg U,\deg V\le O(h^2)$ 一类的多项式界，但那需要引用"算法正确性 + 次数估计"的标准结果，
本项目尚未独立证明。[QA11](../../archive/expert_correspondence/QA11_2026-10-30.md) 里专家也把这列为待补项。

**为什么不用 Bézout 证书**：$\gcd(f_1,\dots,f_s)=1$ 的 Bézout 系数 $a_i$（$\deg a_i<\deg f_i$）次数有经典界，
但极大子式的个数 $s=\binom{m}{h}$ 可能指数大 ⟹ 证书**不是多项式大小**。Smith 证书只有 $n^2+m^2$ 个多项式 ✓。

### 左逆证书：$t-1$ 的次数界（专家 QA13 给出，2026-10-31 验证）

商铅笔 $T_\lambda=\lambda\iota-\bar A$（$q\times t$）满足 $\operatorname{rank}\iota=t$（列满秩）。
专家给出（PBH/可观测性论证）：

$$(S)\iff\exists X(\lambda)\in\mathbb R[\lambda]^{t\times q}:\ X(\lambda)T_\lambda=I_t,\qquad \deg X\le t-1 .$$

**证明思路**：常数行变换把 $\iota$ 化为 $\binom{I_t}{0}$，$T_\lambda$ 化为 $\binom{\lambda I_t-B}{-D}$；
满列秩 $\forall\lambda$ ⟺ PBH 可观测性 ⟺ $\mathcal O=[D;DB;\dots;DB^{t-1}]$ 列满秩
⟹ 存在常数 $G_k$ 使 $\sum_k G_kDB^k=I_t$ ⟹ 显式构造 $X$（次数 $\le t-1$）。

**数值验证**（[c254](../../proof/layer_program/c254_left_inverse.py)）：随机 $t=3$、$m=5$、$\operatorname{rank}E=3$、
满列秩铅笔，解线性方程组得 $\deg\le t-1$ 的左逆，$X(\lambda)P(\lambda)=I$ 在 $\lambda=0,1,2,-1$ 全部成立，**4/4** ✓。

**注**：由 $X_{t-1}E=0$ 与 $E$ 列满秩得 $X_{t-1}=0$，所以实际可到 $\deg\le t-2$；$t-1$ 是安全界。

⟹ **证书规模 $O(qt^2)$ 个系数、$O(qt^2+qt)$ 个方程** ⟹ 多项式大小 ✓。这是 $\exists\mathbb R$ 上界的收口候选。

### 引理 3′（次数界）—— **状态：未证**

**陈述**：设 $P(\lambda)=P_0+\lambda P_1$（$\deg\le1$，$n\times m$），Smith 形式为 $\operatorname{diag}(I_h,0)$。
则存在幺模 $U,V$ 使 $UPV=\operatorname{diag}(I_h,0)$ 且 $\deg U,\deg V\le(n+m)^2$。

**依据**：标准 Smith 算法（逐次 GCD 消元）的次数估计；$\deg P\le1$、不变因子全为 $1$ 时增长最慢。

**缺口（如实记录）**：本项目**尚未独立证明**。需要 (a) 算法正确性（标准结果），(b) 每步次数增长的核算。
这是 $\exists\mathbb R$ 证明的**唯一**剩余缺口。

### 已证的子情形：$n=h$（方铅笔）**不需要** Smith 证书

当 $P$ 是**方阵**（$n=h$，即 $r_1=d$）时，$(S)\iff\det P(\lambda)$ 是**非零常数**（$h+1$ 个多项式等式）✓ [已证]。
一般情形（$n>h$ 的"高"铅笔或 $N_c>h$ 的"宽"铅笔）需要 $\gcd$ 全部 $h\times h$ 极大子式 $=1$，
子式个数 $\binom{n}{h}$ / $\binom{N_c}{h}$ 可能指数大 ⟹ 才需要 Smith 证书（多项式大小）。
这与 [proof/h_bound](../h_bound/README.md) 的"顶层定律"一致：顶层（$\mathcal V\cap Z=0$，$h=N_c$）结构简单，
难度集中在薄层。

**定理（Phase I）**：$\mathrm{DEC}\text{-}\Theta\in\exists\mathbb R$。

*编码*：变量 = $\Theta$、辅助 $Z'$（$d\times n$，编码 $\operatorname{rank}Z=d$）、$R$（编码 $\operatorname{im}R=\ker(CAZ)$，按 $r=\operatorname{rank}(CAZ)$ 分层）、
$U,V$ 的系数（$\approx n^2D+m^2D$ 个）。条件全是多项式等式/不等式：
$$CZ=0,\ L_0Z=0,\ Z'Z=I_d,\ CAZ\,R=0,\quad U(\lambda)P_\Theta(\lambda)V(\lambda)\equiv\operatorname{diag}(I_h,0),\quad \det U\ne0,\ \det V\ne0 .$$
$\operatorname{rank}=c$ 的层用 $\le n$ 个值的有限析取 + 分解编码；公式大小多项式 ✓。

三点说明（回应专家 §9）：
- **不需要图卡枚举**：直接用 P2 Thm 5 的 $Z$ 表述（图卡只是几何/一般点工具），公式里没有 $\binom{m_L}{d}$ 项 ✓；
- **$\forall\lambda$ 消失**：$UPV\equiv$ 常数是多项式**恒等式**；$\lambda$ 不再被量化，"$\lambda\in\mathbb C$"的约定也不再需要 ✓；
- **实/复**：$U,V$ 的系数取实，恒等式按系数比较 ⟹ 纯实问题 ✓（与"输入有理、未知实、恒等式在 $\mathbb C[\lambda]$ 上成立"等价）。

**结论**：把专家 §5 的"Bézout 上界"落成 **引理 + 定理**（只是上界；$\exists\mathbb R$-hard 未证）。

## 4. 现在能严格说什么

| 断言 | 等级 |
|---|---|
| 引理 1（$\lambda=\infty$ 处秩 $=h$）| **[已证-纸面]**（本文件 §1）|
| 引理 2（Bad 可构造；每层上闭；Good 每层开）| **[已证-纸面]**（本文件 §2）|
| 引理 3（Smith 证书 ⟹ $\mathrm{DEC}\text{-}\Theta\in\exists\mathbb R$）| **[已证-纸面]**（本文件 §3）|
| 一般点归约（复几何）| **需不可约性 + 分量逐一检验**（未证 ✗）|
| 一般点归约（实几何）| **需 $X(\mathbb R)$ 稠密**（未证 ✗；专家 §3.1）|
| 多项式时间 | **未证** ✗（专家 §4.2：消元/分量分解都不是多项式）|
| $\exists\mathbb R$-hard | **未证** ✗ |

## 5. 对项目的直接后果

1. 我们的"O1 是开条件"必须改成"**分层开 / 可构造**"——已在 [../layer_program/SPECTRAL_STEP_DESIGN.md](../layer_program/SPECTRAL_STEP_DESIGN.md) 加更正。
2. 一般点归约不能作为"多项式算法"的依据（专家 §4.2）；它至多给出**可判定性**。
3. **Phase I 已完成**（本文件 §3）：引理 3 + 定理"$\mathrm{DEC}\text{-}\Theta\in\exists\mathbb R$"（含 $Z$-表述、无图卡枚举、$\forall\lambda$ 消去）。
   下一步按 Phase II：$\Omega^\star_I$ 的几何（不可约性、实点稠密、all-bad 例子）。

## 6. 复现（数值旁证，不是证明）

```bash
python proof/spectral_locus/verify_smith_check.py   # 点数旁证：L_{0,1} 处处满秩、L_{0,0} 在 λ=−5 降秩
python proof/layer_program/c209_paper2_example.py   # 复算 P2 例子的 q0=3、n0=8
python tools/verification/spectral_gcd.py           # 精确 gcd 工具自检（L_{0,0} → λ+5）
```

## 7. all-bad 的实例与**精确**判据（2026-10-30）

**(a) 教训**：不能用"有限个实 $\lambda$ 上秩不降"代替 $(14b)$。P2 例子在 $q=4$ 上：
用 $\lambda\in[-8,8]$ 采样判出"$(S)$ 通过 432/486"，而**精确极大子式 gcd** 显示**全部失败**
（公根是复根/非整数）⟹ 已写进 [CLAUDE §10.1](../../CLAUDE.md) 禁区。

**(b) 精确工具**：[tools/verification/spectral_gcd.py](../../tools/verification/spectral_gcd.py)
（有理系数多项式、子式行列式、Euclid gcd）；自检：P1 的 $L_{0,0}$ 给出 $\lambda+5$ ✓。

**(c) all-bad 核查**（[c212_allbad_exact.py](../layer_program/c212_allbad_exact.py)）：P2 的例子
- $q=4$：$486$ 个 $(A)$-采样点中抽查 24 个，**精确 $(S)$ 全部失败** ⟹ all-bad；
- $q=5$：抽查 24 个，**全部成立** ⟹ 可行。

$$\text{与 P2 的 }\nu_{\min}=5\text{ 一致 ✓（[精确验证 24/24 + 24/24]；未覆盖全部 }\Theta\text{）}$$

这说明 **all-bad 是真实机制、不是坐标假象**（专家 QA9 §3.3 的判断成立），因此"$\Omega^\star\subseteq B$"可以作为硬度归约的候选结构。

## 8. $\Omega^\star$ 的分层结构（对专家 Phase II 问题 B 的部分回答）

固定图卡，记 $r(\Theta):=\operatorname{rank}(CAZ(\Theta))$，$Z=Z_I(\Theta)$。

**引理 4（顶层自动）**：若 $r(\Theta)=d$，则 $(14a)$ **自动成立**。

*证明*：$r=d$ ⟹ $\ker(CAZ)=0$ ⟹ $R_Z$ 是 $d\times0$ 的空矩阵 ⟹ $[Z,AZR_Z]=Z$，而 $\operatorname{rank}Z=d$ ✓。$\square$

**推论**：$\Omega^\star=\bigcup_{r=0}^{d} S_r$，其中 $S_r=\{\Theta:\operatorname{rank}(CAZ)=r\}\cap\{\operatorname{rank}[Z,AZR_Z]=d\}$；
**$S_d=\{\operatorname{rank}(CAZ)=d\}$ 是开稠密集，在其上只剩 $(S)$ 要检验。**

⟹ 这是"$\Omega^\star$ 显式参数化"的第一步：**顶层不需要解任何方程**，
一般点检验（修正版 O2）在 $S_d$ 上直接可用；只有 $r<d$ 的层需要处理秩条件。

**实例核对**（[c213_strata.py](../layer_program/c213_strata.py)，P2 的例子）：

| 阶 | $d$ | 采样点 | $r=\operatorname{rank}(CAZ)$ | $(A)$ 成立 |
|---|---|---|---|---|
| $q=4$ | 2 | 486 | **全部 $r=2=d$** | **486/486**（自动）✓ |
| $q=3$ | 3 | 108 | 全部 $r=2<d$ | 0/108（$(A)$ 是非平凡的秩条件）|

即 $q=4$ 时 $\Omega^\star$ 就是整个 $\Theta$-空间（顶层），而 $q=3$ 时 $\Omega^\star$ 是余维 1 的薄集 —— 与"$q=4$ 的 all-bad 发生在整个顶层"（§7）吻合：
$S_d$ 整个落在 bad 集里 ⟹ 该阶不可行。**这正是 all-bad 的结构性解释。**

## 9. 复现（$\Omega^\star$ 分层）

```bash
python proof/layer_program/c213_strata.py   # q=4：r=d 全部 (A) 自动；q=3：r<d，(A) 非平凡
```

## 10. 顶层上的随机化判定（单侧误差）

记 $U=\{\Theta:\operatorname{rank}(CAZ)=d\}$（**开稠密**），bad 集 $B=\{\Theta\in U:(14b)\text{ 失败}\}$。

由引理 2（$B$ 每层闭）与引理 4（$U$ 上 $(A)$ 自动），在 $U$ 上：
$$B\ \text{闭},\qquad U\setminus B\ \text{开};\qquad U\not\subseteq B\ \Longrightarrow\ U\setminus B\ \text{非空开}.$$

**命题（随机化，单侧）**：若 $U\not\subseteq B$，则均匀随机 $\Theta\in U$ 落在 $U\setminus B$ 的概率 $\ge 1-D/|S|$
（$D$ 为"bad 消元多项式"的次数上界，Schwartz–Zippel）。因此

> **算法**：随机取有理 $\Theta$（检查 $\operatorname{rank}(CAZ)=d$），用**精确极大子式 gcd** 判 $(S)$。
> - 命中 ⟹ **可行**（给定 $Z$ + gcd 常数 = 完整见证，**单侧无误**）；
> - 连续 $k$ 次不命中 ⟹ "顶层全坏"成立的概率 $\ge 1-(D/|S|)^k$。

**复杂度**：在给定 $\Theta$ 处判 $(S)$ 可由 Smith 标准形在**多项式时间**完成（Kannan–Bachen；本仓库的
[spectral_gcd.py](../../tools/verification/spectral_gcd.py) 用"全部极大子式"实现，子式个数指数级，只适合小 $n$）。
**局限**：这是**单侧**结论——"可行"是证明，"全坏"只是概率证据；要把"全坏"变成定理，必须证 bad 消元多项式 $\equiv0$（消元，非多项式时间）。

**实例**（[c214_top_stratum.py](../layer_program/c214_top_stratum.py)，P2 例子）：

| 阶 | 顶层采样 | $(S)$ 成立 | 结论 |
|---|---|---|---|
| $q=5$ | 20 | **20** | **可行**（见证：图卡 $(1)$、$\Theta=[1;-2;6]$）✓ |
| $q=4$ | 20 | 0 | 顶层全坏（概率证据）|

与 P2 的 $\nu_{\min}=5$ 一致 ✓；且 $q=4$ 的"全坏"现在有了**机制解释**（整个 $S_d$ 落在 $B$ 里）。

## 11. 复现（顶层随机化判定）

```bash
python proof/layer_program/c214_top_stratum.py   # q=5 命中 20/20（可行）；q=4 命中 0/20
```

