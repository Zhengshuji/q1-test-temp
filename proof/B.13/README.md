# B.13 · 计数判据族

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.13` 条目（§0.1 归并表）。
> **状态：有缺口（专家复核）** —— 修订要求见文末的专家复核意见一节。
> 修订完成前，docs 里该条的等级按"待修"对待。

## 命题

**B.13（a）〔原 B.13〕（incidence variety 的维数与"整族不可行"的覆盖判据；专家 2026-11-04 §5 的建议）**
记 $V=\ker[C;CA]$、$K=\ker[C;L_0]$，并设 $h=n$（此时 $(5a)$ 对**每个** $\mathcal Z\subseteq K$ 自动成立，见 3.4）。
考虑 incidence variety
$$\mathfrak I=\{([x],\lambda,[z]):\ x\in V\setminus0,\ L_0x\ne0,\ z=(\lambda I-A)x\ne0,\ z\in K\}\subseteq\mathbb P(V)\times\mathbb P^1\times\mathbb P(K),$$
及其到 $\mathbb P(K)$ 的投影像 $S$（"坏点直线"全体）。

*命题*：
1. **$\lambda$ 与 $z$ 被 $x$ 决定**：$x\in V$ 时 $C(\lambda x-Ax)=0$ 自动成立，而
   $L_0(\lambda x-Ax)=\lambda L_0x-L_0Ax$，故 $z\in K\iff\lambda L_0x=L_0Ax$。
   * $r=1$：$\lambda=L_0Ax/L_0x$ 唯一确定；* $r\ge2$：仅当 $L_0Ax\in\operatorname{span}\{L_0x\}$（比例性）时有解，
   且解唯一。故 $\mathfrak I$ 是 $\mathbb P(V)$ 上某个**开子集与比例性轨迹之交**上的图，特别地
   $$\dim\mathfrak I\le\dim\mathbb P(V)=n-r_1-1,\qquad \dim S\le\min(n-r_1-1,\ n-p-r-1).$$
2. **覆盖判据**：设 $d=n-p-q$。若 $\dim S\ge q-r$，则 $S$ 与 $\mathbb P(K)$ 的**每个** $\mathbb P^{d-1}$ 相交
   （射影维数定理：$\mathbb P^{d-1}$ 与 $s$ 维子簇在 $\mathbb P^{N}$ 中必交当 $s+(d-1)\ge N$，
   $N=\dim\mathbb P(K)=n-p-r-1$，代入得 $s\ge q-r$）。于是**每个** $\mathcal Z\in\mathrm{Gr}(d,K)$ 都含一条坏点直线，
   $\mathcal Z$ 上必有掉秩 $\lambda$ ⟹ 该阶**整族不可行**。（这正是"遮蔽/incidence"判据，见 §4.6。）
3. **对"$r_1=p+r$"的更正**：$\Phi$ 的**支配性**只要求 $n-r_1-1\ge n-p-r-1\iff r_1\le p+r$，
   **等号不是必要的**；且 Type III 的**逐候选**出现并不要求等号——实测 $n=8,p=3,r=2,q_0=3$ 的实例
   （$r_1=6>p+r=5$，$\dim\mathbb P(V)=1<\dim\mathbb P(K)=2$）**也有** Type III 候选（30 个候选里 1 个）。
   真正需要的是上面的**余维条件** $\dim S\ge q-r$；$r_1=p+r$ 只是使 $\mathbb P(V)$ 与 $\mathbb P(K)$ 等维的特例
   （C4 与另一 $n=7,p=2,r=2$ 实例均属此列）。

*等级*：**第 1 条 [已证-纸面]；第 2 条（覆盖判据）降级为 [条件性]** —— 专家 2026-11-04 §2 指出两个未解决的点：

1. **像未必射影闭**：$\mathfrak I$ 的定义排除了 $L_0x=0$ 与 $(\lambda I-A)x=0$，故其像 $S$ 只是**可构造集**；
   射影维数定理只对**闭**子簇成立。取闭包 $\overline S$ 不修复论证：某个 $\mathbb P^{d-1}$ 可能只与
   $\overline S\setminus S$ 相交，而边界点不给出真正的有限 $\lambda$ 障碍。修法：或证像闭，或证边界点也对应真实障碍。
2. **被排除的两个轨迹不能直接丢掉**：$u\ne0$ 而 $z=0$（此时 $x$ 不在 $K$ 里、对任何 $\mathcal Z$ 都是障碍，
   但没有射影直线 $[z]$）；以及 $u=0$（此时 $\lambda$ 不再被确定，若还有 $v=0$ 则对一切 $\lambda$ 成立，
   是一族 $z$）。二者必须或加假设排除、或作为额外的 incidence 分量计入维数。

**因此**：$P=\{x\in V:v\wedge u=0\}$、$\varepsilon=\dim V-\dim P$、$\dim S\le n-r_1-1-\varepsilon$ 作为
**代数观察**保留；覆盖判据与"整族不可行"的推论标为**条件性**，在主结果中不出现（专家 §Q6 同意见）。
$+$ **[精确验证]**（C4 上 $\dim S=1=q-r$；$n=8,p=3,r=2,q_0=3$ 实例上 $r_1=6$、$\dim\mathbb P(V)=1$、
30 个候选中 1 个 Type III）——这些是**实例核对**，不修复上述两个一般性问题。

**B.13（b）〔原 B.13b〕（比例性轨迹的维数与整族不可行的**精确余维条件**；关于 $\varepsilon$ 的结构按专家 2026-11-04 §Q3 重述）**
记 $U_0=L_0|_V$、$U_1=L_0A|_V$，$\Phi(x)=\begin{pmatrix}U_0x\\U_1x\end{pmatrix}$（$2\times r$ 的线性形式矩阵），则
$$P=\{x\in V:\operatorname{rank}\Phi(x)\le1\},$$
即 $P$ 是**行列式簇 $\{\operatorname{rank}\le1\}\subseteq\mathbb C^{2r}$ 在 $x\mapsto(U_0x,U_1x)$ 下的原像**——
一个**线性截面**。故 $\varepsilon$ 是"比例性行列式轨迹"的余维，可用 Gröbner 基 / Hilbert 多项式**实际计算**
（在 $V$ 的坐标环里计算 $2\times2$ 子式的理想之维数），但**不能**只从 $V$ 上某个算子的 Kronecker 数据读出：
$V=\ker[C;CA]$ 未必 $A$-不变，且该不变量依赖 $U_0,U_1$ 的**联合位置**（专家 §Q3）。
命名建议：称 $\varepsilon$ 为"比例性行列式轨迹的余维"，不用未证实的标准名。

记 $u=L_0x$、$v=L_0Ax$，比例性条件是
$v\wedge u=0$，即**二次形式族**
$$q_{ij}(x):=v_iu_j-v_ju_i=0\quad(i<j)$$
的公共零点集 $P\subseteq V$（仿射锥）。令 $\varepsilon:=\dim V-\dim P\ge0$（比例性条件削减的维数；$r=1$ 时无此条件，$\varepsilon=0$）。
则

$$\dim S\le\dim\mathbb P(P)=\dim P-1=n-r_1-1-\varepsilon,$$
故 B.13 的覆盖判据（$\dim S\ge q-r$，且 $h=n$）成立的必要条件是
$$\boxed{\ q-r+\varepsilon\ \le\ n-r_1-1\ }$$

## 纸面证明

*证明*：$P$ 上的 $x$（且 $L_0x\ne0$）给出唯一的 $\lambda$ 与 $z(x)\in K$，故 $\mathfrak I$ 的像 $S$ 是 $\mathbb P(P)$
的子簇，$\dim S\le\dim\mathbb P(P)=\dim P-1$。代入覆盖判据 $\dim S\ge q-r$。$\square$

**实测（四个实例，全部用精确有理算术核验比例性）**

| 实例 | $\dim V$ | $r_1$ | $q_0$ | 比例性在 $V$ 上恒成立？ | $n-r_1-1$ | $q_0-r$ | 结论 |
|---|---|---|---|---|---|---|---|
| C4（$n=6,p=r=2$）| 2 | 4 | 3 | **是**（$\varepsilon=0$）| 1 | 1 | 等式成立 ⟹ 覆盖可能，**实际发生**（整族不可行）|
| $n=7,p=2,r=2$ | 3 | 4 | 4 | **否** | 2 | 2 | $\varepsilon\ge1$ ⟹ 条件失败 ⟹ 覆盖不可能（只有个别候选失败）|
| $n=8,p=3,r=2$ | 2 | 6 | 3 | **否** | 1 | 1 | 同上 ⟹ 30 个候选里仅 1 个失败 |
| $n=5,p=2,r=1$ | 1 | 4 | 2 | 是（$\varepsilon=0$）| 0 | 1 | 维数不足 ⟹ 覆盖不可能 |

**这与"$r_1=p+r$"无关**：正确的不变量是 $q-r+\varepsilon\le n-r_1-1$，其中 $\varepsilon$ 是 **$A$ 在 $V$ 上的作用**
（比例性二次形式）决定的——正印证专家 §Q6 的话："谱侧取决于 $A$ 在相关子空间上的作用，而不只是维数与交"。


*位置*：本文件 B.13；[docs/08_results.md](../../docs/08_results.md) §4.11；`attempts/60`。

*位置*：本文件 3.4（$h=n\Rightarrow(5a)$ 自动）、§4.6（遮蔽判据）；[docs/08_results.md](../../docs/08_results.md) §4.11。

**B.13（c）〔原 B.13c〕（$(5b)$ 失败的精确几何刻画；把"坏点直线"的说法换成显式条件）** 设 $(5a)$ 成立。则
$$(5b)\ \text{在}\ \mathcal Z\ \text{处失败}\iff\exists x\in V\setminus\mathcal Z\ \text{与}\ \lambda:\ (\lambda I-A)x\in\mathcal Z .$$
*证明*：取 $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$（$(5a)$ 保证存在）。对 $x\in V$ 有 $Cx=CAx=0$。于是
* $x\in V\setminus\mathcal Z\iff\mathcal Lx\ne0$（$\mathcal Lx=0$ 且 $Cx=0$ $\iff x\in\ker[C;\mathcal L]=\mathcal Z$）；
* $C(\lambda x-Ax)=\lambda Cx-CAx=0$，故 $(\lambda I-A)x\in\mathcal Z\iff\mathcal L(\lambda x-Ax)=0$；
* 而 $\mathcal L(\lambda x-Ax)=\lambda\mathcal Lx-\mathcal LAx=(\lambda I-\Lambda)\mathcal Lx$（因 $Cx=CAx=0$）。

右侧于是等价于"$\exists\lambda:\ker(\lambda I-\Lambda)$ 含 $\operatorname{im}\mathcal L$ 中的非零元"，即 B.12 的掉秩条件；
由 B.12 该条件等价于 $(5b)$ 失败。$\square$


*注*：（0）**专家 2026-11-04 独立导出了同一条件**，并建议把它作为整个谱侧论证的**基础定理**
（原话：$(5a)\Rightarrow\bigl[(5b)\text{ 失败}\iff\exists x\in V,\lambda:\ x\notin\mathcal Z,\ (\lambda I-A)x\in\mathcal Z\bigr]$，
"exact, applies beyond the special examples, and directly links the original matrix-pencil condition to the
geometry of admissible nullspaces"）。他还特别提醒：**不能**把"压缩满列秩"的**否定**当成失败——
失败还要求 $P_{\mathcal Z}B_Vu\ne0$（见 B.14 的注）。
（i）**这个等价与文献 Thm 4（零空间铅笔判据）等价**——本条只是把它重述成"跨 $\mathcal Z$ 的一对 $(x,(\lambda I-A)x)$"，
不声称新；新增的是**把 $x\notin\mathcal Z$ 这一必要条件的显式化**（旧"坏点直线"语言遗漏了它），
以及它与 B.12 的桥。
（ii）**"$L_0x\ne0$ 且 $Ax=\lambda x$"的情形自动被覆盖**：此时对**每个** $\mathcal Z$（$\mathcal Z\subseteq\ker L_0$）
都有 $x\notin\mathcal Z$、$(\lambda I-A)x=0\in\mathcal Z$ ⟹ $(5b)$ 处处失败 ⟹ $q_{\min}=\infty$。
在"$(C,A)$ 可观测"的标准假设下该情形为**空**（$V=\ker[C;CA]$ 不含 $A$ 的特征向量）。
**商空间对偶形式（专家 2026-11-04 §9 的建议）**：令
$$J_{\mathcal Z}:V\to X/\mathcal Z,\ x\mapsto x+\mathcal Z,\qquad
T_{\mathcal Z}:V\to X/\mathcal Z,\ x\mapsto Ax+\mathcal Z .$$
则 $(5b)$ 在 $\mathcal Z$ 处失败 $\iff$ 对 $(T_{\mathcal Z},J_{\mathcal Z})$ 存在**广义特征向量**：
$\exists x\in V$，$J_{\mathcal Z}x\ne0$，$T_{\mathcal Z}x=\lambda J_{\mathcal Z}x$。
这把问题从"比例性轨迹上的有理映射"变成"**一对线性映射**的广义特征值问题"，
且 $x\notin\mathcal Z$ 自动由 $J_{\mathcal Z}x\ne0$ 表达——是 C2 路线（逐 $\mathcal Z$ 构造）的合适语言。


并核验 $\operatorname{rank}Q(\lambda_0)=5<h=6$（`tools/verification/drop_certificate.py`；$\lambda_0$ 可为 $1-2\sqrt3$、
$3-2i$ 等无理/复数——再次说明不能只在有理 $\lambda$ 上检验）。

**B.13（d）〔原 B.13d〕（$\varepsilon=0$ 的三情形刻画；专家 2026-11-04 §B/§Q6 给出，本项目核验）** 设
$U_0=L_0|_V$、$U_1=L_0A|_V:V\to\mathbb C^r$，比例性轨迹 $P=\{x\in V:U_0x\wedge U_1x=0\}$，
$\varepsilon=\dim V-\dim P$。因 $V$ 不可约、$P$ 代数，$\varepsilon=0\iff P=V$。且

1. $\operatorname{rank}U_0=0$：条件自动成立；
2. $\operatorname{rank}U_0=1$：$\varepsilon=0\iff\operatorname{im}U_1\subseteq\operatorname{im}U_0$；
3. $\operatorname{rank}U_0\ge2$：$\varepsilon=0\iff U_1=\alpha U_0$ 对某个 $\alpha\in\mathbb C$。

*证明*（专家给出）：
(2) 若 $U_0x\ne0$ 则依赖性迫 $U_1x\in\operatorname{im}U_0$；对 $k\in\ker U_0$ 与使 $U_0x_0\ne0$ 的 $x_0$，
$U_1x_0$ 与 $U_1(x_0+k)$ 都在 $\operatorname{im}U_0$ 中，故 $U_1k\in\operatorname{im}U_0$。反向显然。
(3) 对每个 $U_0x\ne0$ 写 $U_1x=\alpha_xU_0x$；若 $U_0x,U_0y$ 线性无关，对 $x+y$ 用依赖性得 $\alpha_x=\alpha_y$；
再对 $k\in\ker U_0$ 用两个像独立的向量夹逼得 $U_1k=0$；故 $U_1=\alpha U_0$。反向显然。$\square$

*意义*：$\varepsilon=0$（整族覆盖判据的唯一非维数假设）变成**纯秩判据**——不需要 Gröbner 基：
只需算 $\operatorname{rank}(L_0|_V)$ 再查"像包含"或"标量倍数"。对本项目的反例：$\operatorname{rank}U_0=1$，
故其 $\varepsilon=0$ 恰是 $\operatorname{im}(L_0A|_V)\subseteq\operatorname{im}(L_0|_V)$。

随机实例上"$q\equiv0$ on $V$"与三情形判据完全一致，覆盖 $\operatorname{rank}U_0=0/1/\ge2$ 三种）。
*注*：**不能**由此推出"Type III $\Rightarrow\varepsilon=0$"——本项目的 $n=7,p=2,r=2$ 与 $n=8,p=3,r=2$
实例上比例性在 $V$ 上**不**恒成立（$\varepsilon\ge1$），却有逐个候选的 Type III。该推测已撤回。

**B.13（e）〔原 B.13e〕（单-$\lambda$ 覆盖证书：一个可判的整族不可行充分条件）** 设 $\dim V=\dim K=:d_0$，且
$$\exists\lambda_0:\quad (\lambda_0I-A)V=K .$$
则对每个 $d$ 维子空间 $\mathcal Z\subseteq K$（$1\le d\le d_0$）只要 $(\lambda_0I-A)^{-1}\mathcal Z\not\subseteq\mathcal Z$，
$(5b)$ 就在 $\lambda_0$ 处失败；因此若没有 $d$ 维子空间被 $(\lambda_0I-A)^{-1}$ 保持，则该阶**整族不可行**。

*证明*：$(\lambda_0I-A)|_V:V\to K$ 是线性同构（两空间同维、像为 $K$）。取 $z\in\mathcal Z\setminus0$，
令 $x=(\lambda_0I-A)^{-1}z\ne0$；则 $(\lambda_0I-A)x=z\in\mathcal Z$。若 $x\notin\mathcal Z$，由 B.13c 即在 $\lambda_0$ 处掉秩。
若对**所有** $z\in\mathcal Z$ 都有 $x\in\mathcal Z$，则 $(\lambda_0I-A)^{-1}\mathcal Z\subseteq\mathcal Z$，与假设矛盾。$\square$

*推论*：例外集是被 $(\lambda_0I-A)^{-1}$ 保持的 $d$ 维子空间——由广义特征向量张成，**有限**个；
故该证书给出"除有限个 $\mathcal Z$ 外全部失败"，剩下的有限个需逐个核验。

**参考形式（专家 2026-11-04 §1.2；比"13 个二次式"更安全）**：令 $u=\operatorname{vec}(M_1)$、$v=\operatorname{vec}(M_2)$，则
$$\exists\lambda:\ \lambda M_1=M_2\iff\operatorname{rank}[u\ v]\le1\ (u\ne0),\qquad u=0\Rightarrow v=0 .$$
这是"两列向量的比例检验"，**多项式时间可判**（一个标量的线性方程组），因此**不是**硬度的来源；
其多项式方程虽为二次，但未知量只有一维。已核验它与逐列 $2\times2$ 子式 + 列间 $\lambda$ 一致的写法**等价**
（含零列与退化情形，**3000/3000**，`tools/verification/t_star_coverage.py`）。

**充分而非必要（2026-11-04 实测）**：在底座 $n=6,p=r=2,q=3$（$\dim V=\dim K=2$、$V\cap K=0$）的 2983 个实例上，
该证书**充分**推出整族不可行（2981/2981 无误报）；但有 **2** 例整族不可行而证书不成立——
因为整族可以在**不同的** $\lambda$ 处逐 $\mathcal Z$ 失败。故本证书是"显式描述的代数充分轨迹"，
不能当充要条件用，也不能用来刻画整个不可行轨迹。

**例外的更精确来源（2026-11-04 补）**：证明中的例外是"$x\in\mathcal Z$ 对所有 $z$ 成立"。因 $x\in V$、
$\mathcal Z\subseteq K$，只需 $V\cap K=0$ 即**无例外**。而
$$\dim(V\cap K)=\dim\ker[C;CA;L_0]\ \ge\ n-(2p+r),$$
故 $V\cap K=0$ 要求 $2p+r\ge n$；本项目的两个整族反例都恰好落在边界 $2p+r=n$（$n=6,p=r=2$）。
另外 $\dim V=n-r_1\ge n-2p$，故 $\dim V=\dim K=2$ 且 $V\cap K=0$ 的最小可行配置正是 $n=6,p=r=2$——
这解释了为什么两个反例都在这一组参数上。

"$\exists\lambda:(\lambda I-A)V=K$" 当且仅当 $t=2$（10 个整点精确核验）；而 $t=2$ 正是整族不可行的唯一参数值。
即该证书**恰好**刻画了该族里的不可行点。

**B.13（f）〔原 B.13f〕（标量情形的不可行判据 = **一个二次方程**；gadget 构件）** 设 $\dim V=\dim K=1$，$V=\langle v\rangle$、$K=\langle k\rangle$
（$v,k\in\mathbb C^3$ 的情形下用叉积；一般 $n$ 用下面的外积形式）。则"该阶不可行"（$\mathcal Z=K$ 被强制，$d=1$）
$$\iff\ \exists\lambda:\ (\lambda I-A)v\parallel k
\iff\ \bigl((Av)\times k\bigr)\times\bigl(v\times k\bigr)=0\ \text{且}\ v\times k\ne0 .$$
最后一条是**数据里的一个二次方程**（$Av$ 与 $k$、$v$ 与 $k$ 的双线性式再相乘一次；无非是消去 $\lambda$ 的结式）。
*证明*：$\lambda v-Av=\mu k$ 对某个 $\lambda,\mu$ 有解 $\iff$ 向量 $Av$ 与 $k$、$v$ 与 $k$ 的张成条件相容，即
$\exists\lambda:\ \lambda(v\times k)=Av\times k$；对 $\lambda$ 可解 $\iff (Av\times k)\parallel(v\times k)$；
而 $v\times k=0$ 时（$V=K$）该式恒成立但**无信息**（正是 B.13e 的例外情形，此时反例表明该阶可以可行）。$\square$


$\dim V=\dim K=1$ 的 2707 个可容许实例中 2676 个非退化样本上"二次条件 $\iff$ 该阶不可行"完全一致；
另 31 个退化样本 $V=K$ 全部**可行**，与 B.13e 的例外一致）。

**重要限制（2026-11-04 自查）**：在 $\dim V=\dim K=1$ 的**唯一**情形（$n=p+r+1$、且 $\dim V=1$ 迫使 $r_1=n-1$），
$v\in\ker C$、$Av\in\ker C$（因 $CAv=0$）、$k\in\ker C$，而 $\dim\ker C=n-p=r+1$；当 $p=r=1$ 时
$\dim\ker C=2$，三个向量落在 2 维空间里 ⟹ 行列式**恒为零**，条件 $\det[Av,v,k]=0$ **自动成立**
（数值核验：$C=(1,x,0)$、$L_0=(0,0,1)$ 的 372 个实例条件全部恒零）。**注意（2026-11-05 按专家 §B.13f 更正）**：这里"恒为零"的是三向量行列式 $\det[Av,v,k]$（三向量在 2 维空间里），**不是**商铅笔的行列式——后者是非零仿射多项式（有有限根，因此失败），两者不可混同；此前把后者说成"恒为零"是我们的措辞错误，已撤回。此时真正的判据退化为 $v\not\parallel k$
（即 $V\ne K$）。故 B.13f 的"二次方程"在该情形**没有内容**；有内容的 gadget 必须从
$\dim V=\dim K\ge2$（如 $n=4,p=r=1,r_1=2$）开始。

## Lean

* 等级行引用的 Lean 声明：`Criterion.b13c_factor`
* 差在哪里：见等级行括注（内核一般只覆盖代数/维数骨架，矩阵实例化多为纸面）

## 精确验证

* `tools/verification/epsilon_zero_characterization.py`
* `tools/verification/scalar_gadget.py`

## 状态与历史

*等级*：**[已证-纸面]** $+$ **[精确验证]**（四实例的比例性与维数见上表；C4 上已有 $\dim S=q-r=1$ 的独立核验）。
*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`Criterion.b13c_factor`：$F\circ(cI-A)=(cI-\Lambda)\circ F$，即上式"$\mathcal L(\lambda x-Ax)=(\lambda I-\Lambda)\mathcal Lx$"的抽象版）$+$ **[精确验证]**（6 个显式证书）。
*等级*：**[已证-纸面]**（三行推导）$+$ **[精确验证]**：C4 的 $q_0=3$ 阶上对 6 个图卡/参数显式构造 $(x,\lambda_0)$
*等级*：**[已证-纸面]** $+$ **[精确验证 5983/5983]**（`tools/verification/epsilon_zero_characterization.py`；
*等级*：**[已证-纸面]**（三行）+ **[精确验证]**：在新实例的单参数族 $A_{00}=t$ 上，
*等级*：**[已证-纸面]** $+$ **[精确验证 2676/2676]**（`tools/verification/scalar_gadget.py`：$n=3,p=r=1,q=1$、
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。



## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F1 |
| 导出等级 | **L2** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— **Lean 不便**（需射影簇维数与闭像；纤维的代数内核已 Lean 化） |


## 支撑目录

[spectral_locus/](../spectral_locus/README.md)、[eigenvalue_confinement/](../eigenvalue_confinement/README.md)、[incidence_strata/](../incidence_strata/README.md)、[global_incidence/](../global_incidence/README.md)、[observability_chain/](../observability_chain/README.md)、[PCC/](../PCC/README.md)、[type3_second_example/](../type3_second_example/README.md)

（本卷宗只汇总证据；支撑目录里的脚本与文档保持原位。）


## B.13d（Theorem C）：固定候选的入射集在 $\mathbb P(W_K)$ 上（专家第六轮 §4）

### 1. 设定

$\mathcal L:\mathbb C^n\to\mathbb C^q$；$K=\ker[C;CA]$（$k=\dim K$）；
$\mathcal L_K:=\mathcal L|_K:K\to\mathbb C^q$，$W_K=\operatorname{im}\mathcal L_K$（$\omega=\dim W_K$）；
$D:=\ker\mathcal L_K=K\cap\ker\mathcal L$（$d=\dim D$）。由秩-零化度
$$\boxed{k=\omega+d.}$$

### 2. 谱障碍的射影集

$$\mathcal E_K:=\bigl\{[w]\in\mathbb P(W_K):\ \Phi_K(w)\in\mathbb C w\bigr\}
=\bigl\{[w]\in\mathbb P(W_K):\ \Phi_K(w)\wedge\iota_K(w)=0\bigr\}.$$
坐标下这是 $w$ 的一组**齐次二次方程**，故 $\mathcal E_K$ 是 $\mathbb P(W_K)$ 中的射影代数集。
按 B.24 的判据，$(5b)$ 成立 $\iff\mathcal E_K=\varnothing$。

**为什么必须用 $\mathbb P(W_K)$ 而不是 $\mathbb P(K)$**：不同的 $v\in K$ 可以给出同一个 $w=\mathcal Lv$，
而 $v\in D$ 给 $w=0$——后者**不是** $\mathbb P(W_K)$ 的点。用 $\mathbb P(K)$ 会把"永久核方向"混进谱障碍。

### 3. 引理（投影映射与纤维维数）

$\mathcal L_K$ 满射到 $W_K$、核为 $D$，故诱导射影映射
$$\pi:\ \mathbb P(K)\setminus\mathbb P(D)\longrightarrow\mathbb P(W_K),\qquad [v]\longmapsto[\mathcal Lv].$$

**纤维**：给定 $[w]\in\mathbb P(W_K)$，$\pi^{-1}([w])$ 是 $\mathbb P\bigl(\mathcal L_K^{-1}(\mathbb C w)\bigr)$ 的开子集；
而 $\mathcal L_K^{-1}(\mathbb Cw)\supseteq D$ 且商为 $1$ 维，故 $\dim\mathcal L_K^{-1}(\mathbb Cw)=d+1$，于是
$$\boxed{\dim\pi^{-1}([w])=d=k-\omega.}$$
（去掉 $\mathbb P(D)$ 不改变纤维维数。）

### 4. 对旧覆盖估计的影响（**未重推，只给出关系式**）

旧的 B.13a 用的是 $\mathfrak I\subseteq\mathbb P(V)\times\mathbb P(K)\times\mathbb P^1$ 与
$\dim\mathfrak I\le\max\{v,\dim\mathcal B+k-1\}$，环境射影维数是 $k-1$。

按定理 C 的正确环境是 $\mathbb P(W_K)$（维数 $\omega-1$）。两者的关系是：
若旧的入射集恰是某个 $\mathbb P(W_K)$ 上入射集的**拉回**，则其维数**大 $d=k-\omega$**（纤维维数）。
故**不能**把旧估计里的 $k$ 直接换成 $\omega$；必须重推。专家给的三个待查点：
1. 入射条件是否只经由 $w=\mathcal Lv$ 依赖于 $v$？
2. 基轨迹 $\mathcal B$ 是旧 $\mathcal B$ 在 $\pi$ 下的像，还是别的集合？
3. 候选族内 $\omega=\dim W_K(R)$ 是否恒定？若不恒定，须按 $\omega$ **分层**（$\mathbb P(W_K)$ 不构成固定丛）。

**状态**：定理 C 的**固定候选部分（§1–§3）已证**；覆盖维数估计的**族内版本待重推**（上面三点）。


## B.13e：覆盖估计在 $\mathbb P(W_K)$ 上的重推（专家第六轮 §4.3 的第 4 项）

### 1. 一个简化：谱障碍**不需要** $\mathbb P^1$

原先的入射簇带一个参数 $[\alpha:\beta]\in\mathbb P^1$。但在修正后的域上，条件
$$\Phi_K(w)\in\mathbb C w$$
本身已经"自带 $\lambda$"：若 $w\ne0$ 且 $\Phi_K(w)=cw$，则 $c$ 唯一确定。因此
$$\boxed{\mathcal E_K=\bigl\{[w]\in\mathbb P(W_K):\ \Phi_K(w)\wedge\iota_K(w)=0\bigr\}\subseteq\mathbb P(W_K)}$$
**不再需要 $\mathbb P^1$ 因子**。坐标下它由 $\binom{q}{2}$ 个**二次**方程在 $\omega$ 个变量上切出。

### 2. 两个入射集维数的精确关系

设 $\widetilde{\mathcal E}_K:=\pi^{-1}(\mathcal E_K)\subseteq\mathbb P(K)\setminus\mathbb P(D)$，其中
$\pi:\mathbb P(K)\setminus\mathbb P(D)\to\mathbb P(W_K)$ 是 B.13d 的投影映射（纤维维数 $d=k-\omega$）。则
$$\boxed{\dim\widetilde{\mathcal E}_K=\dim\mathcal E_K+d=\dim\mathcal E_K+(k-\omega)}$$
（纤维维数恒定的投影映射的维数公式）。**这就是"两个入射维数之间的关系"**：
旧估计用 $\mathbb P(K)$ 得 $\dim\widetilde{\mathcal E}_K$，新估计用 $\mathbb P(W_K)$ 得 $\dim\mathcal E_K$，两者**差 $k-\omega$**。

### 3. 覆盖判据的族内版本（按 $\omega$ 分层）

设候选族 $\{\mathcal L(R)\}$ 落在**常秩层** $\omega=\operatorname{rank}(\mathcal L(R)|_K)$ 上（专家 §4.3 的第 3 点：
$\omega$ 可能跳变，故必须分层）。在该层上把 $\mathcal E_K$ 与 $\Phi_{K,R}$ 都拉回到**参数空间 × $\mathbb P(W_K)$**，
记总入射簇为 $\mathfrak J$，$p:\mathfrak J\to$ 参数空间、$q:\mathfrak J\to\mathbb P(W_K)$。则

* 若 $p$ 不满，则存在一个候选 $R$ 使 $\mathcal E_K(R)=\varnothing$，即**该候选可行**（覆盖判据）；
* 维数充分条件（在该层 $\omega$ 恒定、$p$ 的纤维维数一致的前提下）：
$$\dim\mathfrak J<\dim(\text{参数空间})\ \Longrightarrow\ p\ \text{不满}.$$
* 与旧估计的换算：$\dim\mathfrak J=\dim\mathfrak J_{W_K}+d$（第 2 条的纤维修正），
  故**不能**把旧估计里的 $k$ 直接替换为 $\omega$。

**状态**：第 1–2 条**已证**；第 3 条是**框架**（$p$ 的纤维维数一致性未证，族的常秩分层未构造）。
它把专家要求的三个待查点归约为一个：**在常秩层上，$p$ 是否等维**。

### 4. 与旧 B.13a 的关系

旧的 $\dim\mathfrak I\le\max\{v,\ \dim\mathcal B+k-1\}$ 是关于 $\mathbb P(K)$ 上带 $\mathbb P^1$ 的入射簇。
在修正后的语言里，正确的对象是 $\mathcal E_K\subseteq\mathbb P(W_K)$（无 $\mathbb P^1$），
而旧估计可以作为 $\mathcal E_K$ 在 $\pi$ 下拉回的**上界**使用（需 $k-\omega$ 的修正）。两条并不矛盾，**旧式是粗的**。

## B.13b：抽象覆盖引理（纸面证明，专家已复核）

**陈述**：设 $V\le E$（$v=\dim V$）、$K\le E$（$k=\dim K\ge1$）、$P_{\alpha,\beta}=\alpha I-\beta A$，
$$\mathfrak I=\bigl\{([x],[z],[\alpha:\beta])\in\mathbb P(V)\times\mathbb P(K)\times\mathbb P^1:\ z\wedge P_{\alpha,\beta}x=0\bigr\},$$
$\operatorname{pr}_z:\mathfrak I\to\mathbb P(K)$ 为 $[z]$ 投影。则
$$\dim\mathfrak I<k-1=\dim\mathbb P(K)\ \Longrightarrow\ \operatorname{pr}_z(\mathfrak I)\ne\mathbb P(K),$$
且像为真闭子集，故存在 $[z]\in\mathbb P(K)$ 使
$$z\wedge(\alpha x-\beta Ax)\ne0\qquad\text{对一切 }0\ne x\in V,\ [\alpha:\beta]\in\mathbb P^1 .$$

*证明*：任意态射的像维数不超过源维数：$\dim\operatorname{pr}_z(\mathfrak I)\le\dim\mathfrak I<k-1=\dim\mathbb P(K)$，
故像不能是整个 $\mathbb P(K)$。又 $\mathfrak I$ 是射影簇乘积中的闭集（B.13a 引理 1），
$\operatorname{pr}_z$ 是射影态射，其像闭，故为**真闭子集**。$\square$

**注（量词）**：$x$ 必须取**非零**；$x=0$ 时 $z\wedge P x=0$ 恒成立。

## B.13c：由基轨迹估计得到的充分条件（纸面证明，专家已复核）

**陈述**：若 $\mathcal B=\varnothing$ 且 $v<k-1$，则存在 $[z]\in\mathbb P(K)$ 避开整个入射族。

*证明*：由 B.13a 的推论，$\mathcal B=\varnothing\Rightarrow\dim\mathfrak I\le v$；
再由 $v<k-1$ 得 $\dim\mathfrak I<k-1$，套用 B.13b 即得。$\square$

**注**：$\mathcal B\ne\varnothing$ 时 B.13a 无法给出 $\dim\mathfrak I<k-1$——
这不是估计的弱点：只要 $\mathcal B$ 有一个点 $([x_0],[\alpha_0:\beta_0])$，就有
$\{([x_0],[z],[\alpha_0:\beta_0]):[z]\in\mathbb P(K)\}\subseteq\mathfrak I$，于是 $\operatorname{pr}_z(\mathfrak I)=\mathbb P(K)$
（投影**满**）。故"$\mathcal B=\varnothing$"是本质条件，不能省。

**无穷远点的正确式子**：$P_{1,0}=I$、$P_{0,1}=-A$，故 $\beta=0$ 时 $[z]=[x]$；
若要写成 $A$ 的方向则应取 $-Ax$（楔积的零性与符号无关，但公式要一致）。

## B.13a：齐次入射簇（完整证明）

**约定**（沿用专家写法，列约定）：$E=\mathbb C^n$、$A:E\to E$ 线性、$V\le E$（$\dim V=v$）为候选行空间、
$K\le E$（$\dim K=k$）为核空间；$P_{\alpha,\beta}:=\alpha I-\beta A$，$(\alpha,\beta)\ne(0,0)$。
（本项目用行约定时，把 $A$ 换成 $A^{\mathsf T}$、$V,K$ 换成其对偶即可，几何结论不变。）

### 定义

$$\mathcal D:=\mathbb P(V)\times\mathbb P^1,\qquad
\mathcal B:=\bigl\{([x],[\alpha:\beta])\in\mathcal D:\ P_{\alpha,\beta}x=0\bigr\},$$
$$\mathfrak I:=\bigl\{([x],[z],[\alpha:\beta])\in\mathbb P(V)\times\mathbb P(K)\times\mathbb P^1:\ z\wedge P_{\alpha,\beta}x=0\bigr\},$$
$$\pi:\mathfrak I\longrightarrow\mathcal D,\qquad \pi([x],[z],[\alpha:\beta]):=([x],[\alpha:\beta]).$$

### 引理 1（闭性）

$\mathfrak I$ 是 $\mathbb P(V)\times\mathbb P(K)\times\mathbb P^1$ 中的**闭**子集。

*证明*：考虑截面
$$\Phi:\mathbb P(V)\times\mathbb P(K)\times\mathbb P^1\longrightarrow \wedge^2 E,\qquad
\Phi([x],[z],[\alpha:\beta]):=z\wedge(\alpha x-\beta A x).$$
它对 $x\mapsto cx$、$z\mapsto dz$ 分别齐次一次（$\Phi\mapsto cd\,\Phi$），故 $\Phi$ 在投影空间中良定义。
"$z\wedge w=0$"$\iff$"$z,w$ 线性相关"$\iff$ 所有的 $2\times2$ 子式为零，是闭条件；故
$\mathfrak I=\Phi^{-1}(0)$ 闭。$\square$

### 引理 2（$\mathcal B$ 之外的纤维维数 $\le0$）

若 $([x],[\alpha:\beta])\notin\mathcal B$（即 $P_{\alpha,\beta}x\ne0$），则 $\pi^{-1}([x],[\alpha:\beta])$ 至多一个点：
由 $z\wedge P_{\alpha,\beta}x=0$ 与 $P_{\alpha,\beta}x\ne0$ 得 $[z]=[P_{\alpha,\beta}x]$；且该点存在当且仅当 $P_{\alpha,\beta}x\in K$。

*证明*：两个非零向量楔积为零 $\iff$ 成比例；比例系数唯一确定 $[z]$；$[z]\in\mathbb P(K)$ 要求 $P_{\alpha,\beta}x\in K$。$\square$

### 引理 3（$\mathcal B$ 之上的纤维维数 $=k-1$）

若 $([x],[\alpha:\beta])\in\mathcal B$（即 $P_{\alpha,\beta}x=0$），则楔积条件自动成立，
$$\pi^{-1}([x],[\alpha:\beta])=\{[x]\}\times\mathbb P(K),$$
维数 $\dim\mathbb P(K)=k-1$。

*证明*：$P_{\alpha,\beta}x=0$ 时 $z\wedge0=0$ 对一切 $[z]$ 成立。$\square$

### 定理（维数估计）

$$\boxed{\dim\mathfrak I\ \le\ \max\{\,v,\ \dim\mathcal B+k-1\,\}},\qquad v=\dim\mathcal V.$$

*证明*：把 $\mathfrak I$ 分成两块：$\mathfrak I_1:=\pi^{-1}(\mathcal B)$ 与 $\mathfrak I_2:=\pi^{-1}(\mathcal D\setminus\mathcal B)$。

* $\mathfrak I_1$ 是 $\mathcal B$ 上的 $\mathbb P(K)$-丛（引理 3 说明纤维恰是整条 $\mathbb P(K)$，且在 $\mathcal B$ 上平凡），故
  $\dim\mathfrak I_1=\dim\mathcal B+(k-1)$。
* $\mathfrak I_2$ 在 $\mathcal D\setminus\mathcal B$ 上的纤维维数 $\le0$（引理 2），故
  $\dim\mathfrak I_2\le\dim(\mathcal D\setminus\mathcal B)+0\le\dim\mathcal D=v$（因 $\dim\mathcal D=(v-1)+1=v$）。
* 两者取并：$\dim\mathfrak I\le\max\{\dim\mathfrak I_1,\dim\mathfrak I_2\}$。$\square$

### 推论（无特征向量时的维数）

若 $A$ 在 $V$ 中没有特征向量，则 $\mathcal B=\varnothing$，于是
$$\dim\mathfrak I\ \le\ v .$$

*证明*：$([x],[\alpha:\beta])\in\mathcal B$ 且 $\beta\ne0$ 时，$\lambda=\alpha/\beta$ 与 $(\lambda I-A)x=0$ 给出 $V$ 中的特征向量；
$\beta=0$（$\alpha\ne0$）时 $P_{\alpha,0}=\alpha I$ 非奇异，$Px=0$ 迫使 $x=0$，与 $[x]$ 合法矛盾。故 $\mathcal B=\varnothing$。$\square$

### 说明：还不是覆盖定理

上面四条给出**入射簇及其纤维的维数上界**，这正是专家所说的"中间估计"。
把它变成"整族不可行的覆盖判据"还需一步：对投影 $\mathfrak I\to\mathbb P(K)$ 做维数比较（若 $\dim\mathfrak I<\dim\mathbb P(K)=k-1$，
则投影不可能满，于是存在未被覆盖的 $[z]$）。**这一步仍未写出**，因此 B.13 整体状态保持"有缺口"，
但 B.13a 本身（引理 1–3 + 定理 + 推论）已完整。

## 专家复核意见（第二轮：接受三段策略，但纤维引理必须修正）

**修正 1：无穷远点。** $\beta=0,\alpha\ne0$ 时 $P(\alpha,0)=\alpha I$，故 $[z]=[x]$（原写 $[Ax]$ 是错的）。

**修正 2：基轨迹必须分离。** 记 $P_{\alpha,\beta}=\alpha I-\beta A$、
$$\mathcal B=\bigl\{([x],[\alpha:\beta])\in\mathbb P(\mathcal V)\times\mathbb P^1:\ P_{\alpha,\beta}x=0\bigr\}$$
（即"$[\alpha:\beta]$ 是 $A$ 在 $\mathcal V$ 中的特征方向"）。入射簇取在 $\mathbb P(\mathcal V)\times\mathbb P(K)\times\mathbb P^1$ 上：
$$\mathfrak I=\bigl\{([x],[z],[\alpha:\beta]):\ z\wedge P_{\alpha,\beta}x=0\bigr\}.$$

**修正 3：纤维不是单点。** 分两层：

| 层 | 纤维 |
|---|---|
| A：$([x],[\alpha:\beta])\notin\mathcal B$（$P_{\alpha,\beta}x\ne0$）| 由楔方程唯一确定 $[z]=[P_{\alpha,\beta}x]$；若 $P_{\alpha,\beta}x\notin K$ 则无点 ⟹ 维数 $\le0$ |
| B：$([x],[\alpha:\beta])\in\mathcal B$（$P_{\alpha,\beta}x=0$）| 楔方程自动成立 ⟹ 纤维是**整个** $\mathbb P(K)$，维数 $k-1$（$k=\dim K$）|

**修正 4：维数估计的正确形式。** 以 $v=\dim\mathcal V$：
$$\dim\mathfrak I\ \le\ \max\{\,v,\ \dim\mathcal B+k-1\,\}.$$
这只是**中间估计**，还不是覆盖定理。

**待证引理 B.13a（专家给定的三段式）**：
1. $\mathfrak I$ 在 $\mathbb P(\mathcal V)\times\mathbb P(K)\times\mathbb P^1$ 中**闭**；
2. $\mathcal B$ 之外，投影 $\mathfrak I\to\mathbb P(\mathcal V)\times\mathbb P^1$ 的纤维维数 $\le0$；
3. $\mathcal B$ 之上，纤维维数 $\le k-1$。

**状态**：三段策略被接受；上面 1–3 的**证明**仍未写出 ⟹ 本条保持"有缺口"，但构造与估计已按专家意见改正。

**下一轮优先级（专家建议）**：先做 **B.13a**（入射构造已足够精确，可独立给一个干净的代数几何证明）。

## B.13 的 Lean 化：可行分解与障碍（2026-11-07）

专家把 B.13 排在第一位，理由是"数学上已近完成、只缺 Lean"。实际拆分后，缺口不在代数而在**几何**：

| 步骤 | 内容 | 可用工具 | 难度 |
|---|---|---|---|
| **L1** | 楔积零的二选一：$z\wedge w=0\iff w\in\mathbb C z\ \vee\ z\in\mathbb C w$（含 $w=0$）| `LinearIndependent.pair_iff` / 外积 API | **低**（可做）|
| **L2** | 纤维二分（B.13a 引理 2/3）：$Mx\ne0$ 时 $\{z\in K: z\wedge Mx=0\}\subseteq\mathbb C(Mx)$ 至一维；$Mx=0$ 时为整个 $K$ | L1 + 子空间 | **低**（可做）|
| **L3** | 入射集闭性（B.13a 引理 1）| 多项式零点集；需把 $\mathbb P(V)\times\mathbb P(K)\times\mathbb P^1$ 建成 `Proj`/簇 | **高** |
| **L4** | 维数估计 $\dim\mathfrak I\le\max\{v,\dim\mathcal B+k-1\}$ | 需要纤维维数定理（`dim f^{-1}(y)`），Mathlib **无** |
| **L5** | 覆盖引理 B.13b（像维数 ≤ 源维数 ⟹ 不满）| 需要射影簇态射的维数定理与闭像定理，Mathlib **无** |

**进展（2026-11-07）**：L1/L2 的代数内核已形式化 —— `B13Fiber.lean` 三条引理（`scalar_unique_of_ne_zero`、`zero_vec_proportional`、`proportional_set_subsingleton`），`lake env lean` 退出码 0，已登记进 `STATEMENT_MAP`。它们覆盖"比例唯一性"（$\mathcal B$ 外纤维至一点）与"零向量退化"（$\mathcal B$ 上整条纤维），但**不**覆盖射影化与维数。

**结论**：L1/L2 的代数部分已完成；L3–L5 需要自行搭一层"射影簇的维数与闭像"基础设施，
是**多会话**工程，而不是一条引理。在当前验收规则下，B.13 只能停在 **L2（M3/F1）**，
除非接受"用线性代数替身替换几何维数论证"（那样它就不是原命题了，我们不这么做）。

**建议**：把 L1/L2 先形式化（它们同时服务 B.13a 的纤维二分与 B.8 之外的其它判据），
L3–L5 作为独立路线在 `workspace/` 立项；不要为了"补齐 B.13"而改写命题。
