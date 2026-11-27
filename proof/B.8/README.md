# B.8 · 铅笔的 Smith/Kronecker 结构

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.8` 条目（§0.1 归并表）。

## 命题

**B.8（a）〔原 B.8a〕（Smith 判据；(5b) $\iff$ 无有限初等因子）** 设 $L$ 满足 $(5a)$、$h=\operatorname{rank}[L;CA;C]$。则
$$(5b)\iff d_{\rm fin}=0,$$
其中 $d_{\rm fin}$ 是 $Q_L(\lambda)$ 的 Smith 形中**非零不变因子的次数之和**（等价地：有限初等因子的总大小）。

## 纸面证明

*证明*：设 Smith 形的非零不变因子为 $d_1,\dots,d_h$。在有限 $\lambda_0$ 处秩跌破 $h$，当且仅当某个 $d_i(\lambda_0)=0$；
$\mathbb C$ 上非常数多项式必有根，故"$\operatorname{rank}Q(\lambda)=h$ 对一切 $\lambda\in\mathbb C$"$\iff$ 每个 $d_i$ 是非零常数
$\iff d_{\rm fin}=0$。$\square$


**B.8（b）〔原 B.8b〕（观测器铅笔的 Kronecker 恒等式；2026-11-05 修正）** 设 $\mathcal L$ 满足 $(5a)$、$h=\operatorname{rank}[\mathcal L;CA;C]$。则
$Q_{\mathcal L}$ 的**右最小指标全为零次**（由 B.21：右零空间 $=S[\lambda]$，共 $n-h$ 个），故正确的恒等式是
$$h=\sum_i\varepsilon_i+d_{\rm fin}+d_\infty .$$
*证明*：一般恒等式 $h=\sum\varepsilon+\sum\eta+d_{\rm fin}+d_\infty$ 中 $\sum\eta=0$（B.21）。$\square$
*修正记录*：
* 原版把上式写成 $h=\sum\varepsilon_i+d_{\rm fin}$（即假设 $d_\infty=0$）——**错误**：等号情形下 $d_\infty=r_1>0$（B.22）。
* 原版还说"观测器铅笔无右最小指标"——**也不准确**：它恰有 $n-h$ 个右最小指标，只是**全为零次**（专家 2026-11-05 §Q3）。
* 有用的记账引理（专家 §Q1.2）：$\nu_\infty:=h-\operatorname{rank}A_1$ 数的是无穷初等因子的**个数**（不是总次数）；
  对本铅笔 $A_1=[\mathcal L;0;0]$、秩 $q$，故 $\nu_\infty=r_1$ ✓。**总次数** $d_\infty$ 不能由 $\operatorname{rank}A_0,\operatorname{rank}A_1,h$ 决定
  （专家给了同秩不同 $d_\infty$ 的反例）。

## Lean

* 无独立 Lean 内核（该条为纸面证明）。

## 精确验证

* 该条暂无独立精确验证脚本（纸面证明 + 支撑目录）。

## 状态与历史

*等级*：**[已证-纸面]**（初等；专家 2026-11-05 §Q3 确认此半正确）。
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。





## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F1 |
| 导出等级 | **L2** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— **Lean 不便**（Mathlib 缺 Smith 形；gcd/Bézout 路线可做但工程大） |


## 支撑目录

[5a_archive/](../5a_archive/README.md)、[5b_upper_bound/](../5b_upper_bound/README.md)

（本卷宗只汇总证据；支撑目录里的脚本与文档保持原位。）

## 附录：铅笔的 Smith 判据（原 docs/02 附录 A）

## J. 固定 $U$ 的谱判据 = 行列式因子（Smith 形）

**命题**：$Q(\lambda)$ 为 $a\times b$ 多项式矩阵，$a\ge b$，$\operatorname{rank}_{F(\lambda)}Q=b$（$F$ 为任意域，本项目取 $F=\mathbb C$）。则
$$\operatorname{rank}Q(\lambda)=b\quad\forall\lambda\in\mathbb C
\iff\Delta_b(\lambda):=\gcd\{\text{全部 } b\times b \text{ 极大子式}\}\in F^\times,$$
且 $\Delta_b=d_1d_2\cdots d_b$（Smith 不变因子之积）。

*证明*：$\operatorname{rank}Q(\lambda_0)<b$ $\iff$ 全部 $b\times b$ 子式在 $\lambda_0$ 为零 $\iff$ $\Delta_b(\lambda_0)=0$；
$\mathbb C$ 上非常数多项式必有根 ⟹"无根 $\iff$ 常数"。$\Delta_b$ 与不变因子的关系是 Smith 标准形的标准性质。$\square$

**等级**：[已证-纸面]；实现与"枚举极大子式"路径在 84 个随机矩阵 + 86 个真实铅笔（R17 $q=3,2$、c282 $q=4$、第二实例 $q=2$，含 $q\ne t$ 的矩形情形）上 **0 不一致**，等级 [精确验证]。
**位置**：[tools/verification/poly_smith.py](../../tools/verification/poly_smith.py)、[verify_smith.py](../../tools/verification/verify_smith.py)。

**复杂度（只对精确算术模型成立）**：Smith 形可在 $\mathrm{poly}(a,b,\deg)$ 内算出，故**固定 $U$ 时谱判据是多项式时间**。三点限定：
(i) 需要系数可有效表示（算法实现用 $\mathbb Q$；**定理本身对任意域成立**，本项目取 $\mathbb C$）；
(ii) 界里含系数增长项；
(iii) 这**只覆盖固定 $U$**——$\exists U$（Grassmannian 上的搜索）仍未知，那才是 $q1$ 本体。
引文：Kaltofen–Krishnamoorthy–Saunders (1987) 的并行 Hermite/Smith 算法；Storjohann–Labahn (1997) 的多项式矩阵 Smith 形 Las Vegas 算法。

---

## 专家复核意见（成立）

矩形情形要用**正规秩** $h$ 的第 $h$ 个行列式因子 $\Delta_h$（不是任意的第 $b$ 个）；先述 Smith 形再推行列式因子判据。

## 系数域（专家第四轮 §8.1 的更正）

原陈述写 $\Delta_h\in\mathbb Q^\times$，但原问题的输入是 $A,C\in\mathbb C^{\cdot\times\cdot}$。
正确写法是**对任意域 $F$**（本项目取 $F=\mathbb C$）：

$$\operatorname{rank}Q(\lambda)=h\ \forall\lambda\in\overline F
\iff\Delta_h(\lambda)=\gcd\{\text{全部 } h\times h\text{ 极大子式}\}\in F^\times,$$

其中"非常数多项式必有根"这一步用 $\overline F$ 的代数闭性（$\mathbb C$ 代数闭）。
$\mathbb Q^\times$ 只适用于"输入为有理系数"的算法实现场景，不应作为定理的陈述。


## 第三接口（专家第五轮 Q3）：$\Delta_h$ 作为**精确**判据 + Bézout 证书

专家在 30 号答复 §3 指出：比入射维数（B.13c，只充分）与秩屏障（F.1，只必要）更合适的第三接口，
是**有限初等因子 / 行列式因子**，因为它是**精确**判据。

### (i) 精确判据（本卷宗已证）

对观测器铅笔 $Q_{\mathcal L}(\lambda)$，设法秩为 $h$、$\Delta_h$ 为其全部 $h\times h$ 极大子式的 gcd。则
$$\boxed{(5b)\iff\Delta_h(\lambda)\in\mathbb C^\times}$$
（B.8 取 $F=\mathbb C$；$h$ 为法秩）。**注意**：这里不需要 $\mathcal B=\varnothing$ 之类的额外假设——
这正是它强于 B.13c 的地方；但它也**不给**几何解释，只给代数判据。

### (ii) 与 $d_{\rm fin}$ 的关系（**待钉死**）

专家 §3.1 写 $(5b)\iff d_{\rm fin}=0$（式 (6)）。这条依赖 Kronecker 记账恒等式的**精确形式**；
本项目的 B.8b 曾更正为 $h=\sum_j\varepsilon_j+d_{\rm fin}+d_\infty$（含 $d_\infty$，反例 $[\lambda\ 1]$），
而 B.6 又给出 $d_\infty=h-\operatorname{rank}\mathcal L$ 与"右指标全零"。
**这三条放在一起的自洽性尚未在我们自己的记号下核过**，故本轮只采用 (i) 的 $\Delta_h$ 形式，
$d_{\rm fin}$ 形式标为**待核**（下一步：用 `tools/verification/poly_smith.py` 在随机可容许实例上同时算
$\Delta_h$ 的次数与 Smith 不变因子的次数，核对恒等式）。


**核对进展（结论：未定论，但已定位）**：
1. 首轮在 $n=4$、$q+2p=4$ 的方阵铅笔上得 $d_{\rm fin}=2$、$d_{\rm inf}=4$，与 $d_{\rm fin}+d_\infty=h=4$ 冲突；
2. 用已知小例**标定 Smith 实现**（`smith_calibrate.py`）：$\operatorname{diag}(\lambda,1)$ 给 $d_{\rm fin}=1,d_{\rm inf}=1$；
   $[\lambda\ 1]$ 给 $d_{\rm fin}=0$ —— **实现正确**；
3. 因此偏差在**反转约定**：对行块次数不一致的铅笔，$\mu Q(1/\mu)$ 型反转**不保持** $d_{\rm fin}+d_\infty=h$；
   正确做法是**齐次化** $Q(\alpha,\beta)=\alpha Q_1+\beta Q_0$ 并在 $\mathbb P^1$ 上算不变因子。
在该项完成前，$d_{\rm fin}$ 一侧仍只采用 $\Delta_h$ 形式（B.8 的精确判据）。
另：首轮打印的各实例数值**完全相同**，提示脚本还有别的 bug（行块顺序或矩形 Smith 处理），修好前不引用其数字。


**记账恒等式的正确形式（专家第六轮 §1）**：对一般矩形铅笔，
$$h=\sum_j\varepsilon_j+\sum_i\eta_i+d_{\rm fin}+d_\infty$$
（$\varepsilon$ 右最小指标、$\eta$ **左**最小指标）。我们原来的短式 $h=\sum\varepsilon+d_{\rm fin}+d_\infty$
**只在没有左最小指标时**成立（即 $m=h$，满行法秩）。本项目铅笔有 $q+2p$ 行，法秩不必等于 $q+2p$，
故**不能**直接用短式。另：最小指标**不能**从方阵子式的 Smith 形读出（专家 §1.2）。
参考文献：Gantmacher《The Theory of Matrices》Vol. II；Lancaster–Tismenetsky；Van Dooren (1979)
"The computation of Kronecker's canonical form of a singular pencil"。


## Bézout 次数界（专家第六轮 §6.3 的要求）

要在论文里把 Bézout 编码写成可检验的命题，必须给**显式次数界**并证明。记录我们要证的引理：

**引理（有限族 Bézout 界）** 设 $p_1,\dots,p_N\in\mathbb C[\lambda]$ 满足 $\gcd(p_1,\dots,p_N)=1$，
$D:=\max_i\deg p_i$。则存在 $u_1,\dots,u_N$ 使 $\sum_i u_ip_i=1$ 且
$$\deg u_i\le D\qquad(1\le i\le N).$$
（两两情形：$\deg u_1<\deg p_2$、$\deg u_2<\deg p_1$；多族用逐次 gcd 归纳，每次只与一个 $p_i$ 消，
次数不增。）

**据此的编码规模（专家 §6.3 的两点限定）**：
* 变量数：$R$ 的条目 + $u_i$ 的系数，共 $O\bigl((q-r)n+N\cdot D\bigr)$；
* **规模瓶颈**：$h$-minors 的个数是
$$\binom{m}{h}\binom{n}{h},\qquad m=q+2p,\ n=\dim,$$
可能**指数级**；故 Bézout 编码给出的是**有限**的 $\exists\mathbb R$ 陈述，**不**自动是**多项式规模**；
* $h$ 可能随 $R$ 变 ⟹ 编码须按 $h$ 分层（或固定在常法秩族上）。



## 按法秩 $h$ 的分层（专家第六轮 §6.3 第 3 点：$h$ 随 $R$ 变时怎么办）

$h(\mathcal L)=\operatorname{rank}\begin{bmatrix}\mathcal L\\CA\\C\end{bmatrix}$ 依赖 $R$，故 $\Delta_h$ 的
"下标 $h$"也依赖 $R$。处理办法是**按 $h$ 分层**。三条可证的引理：

**引理 1（层是构造集）** 对每个 $k$，$\mathcal S_k:=\{\mathcal L:\ \operatorname{rank}[\mathcal L;CA;C]=k\}$ 是构造集。
*证明*：$\{\operatorname{rank}\le k\}$ 由全部 $(k{+}1)\times(k{+}1)$ 子式为零定义，是**闭**条件；
$\mathcal S_k=\{\operatorname{rank}\le k\}\setminus\{\operatorname{rank}\le k-1\}$，故是局部闭（构造）集。$\square$

**引理 2（层数多项式）** $h$ 只取 $0,1,\dots,\min(q+2p,n)$，故至多 $\min(q+2p,n)+1\le n+1$ 层。

**引理 3（层上的判据是固定尺寸）** 在 $\mathcal S_k$ 上，$\Delta_h$ 的判据恰是
$$\gcd\{\text{全部 }k\times k\text{ 子式 of }Q_{\mathcal L}(\lambda)\}\in\mathbb C^\times,$$
共 $\binom{q+2p}{k}\binom{n}{k}$ 个子式、每个次数 $\le k$；Bézout 形式的编码规模
$$(q-r)n+(k+1)\binom{q+2p}{k}\binom{n}{k}.$$

**推论（DEC 的分层表述与规模）**
$$\mathrm{DEC}(q)\iff\bigvee_{k=0}^{\min(q+2p,n)}\Bigl[\,\mathcal L\in\mathcal S_k\ \wedge\ \exists u:\ \sum_i u_ip_i^{(k)}(\cdot;R)=1\Bigr],$$
即**有限个（$\le n+1$）构造层上的固定尺寸判定**的析取。由此：

* 每条 $\mathcal S_k$ 上的判定是**固定尺寸**的（与 $R$ 无关的下标 $k$）；
* 规模只在**中间层**（$k\approx n/2$）爆炸（上一节的规模审计）；
* 这给出 G.1 的 $\exists\mathbb R$ 上界的**另一条（模块化）证明**：$\le n+1$ 个分层、每层有限陈述，
  合起来仍是有限的 $\exists\mathbb R$ 陈述——与 G.1 的 chart-free 编码是**同一结论的两条路径**。

**对 $q1$ 的含义（明确写清，不夸大）**：分层把"$h$ 随 $R$ 变"这个障碍**消掉了**（变成有限析取），
但它**不**给出多项式算法：中间层的子式个数仍是指数的，且每层仍要解一个实代数存在性问题。
所以这条只**恢复上界**，不改进它。




## T2 / T3：可容许层上的构造性定理（专家第七轮请求的正题）

### 设定

记 $B(R):=\begin{bmatrix}\mathcal L\\CA\\C\end{bmatrix}$（$m\times n$），$m=q+2p$。对 $0\le k\le\min(m,n)$：

* **可容许层** $\mathcal A_k:=\bigl\{R:\ \operatorname{rank}B(R)=k,\ \operatorname{rank}\begin{bmatrix}\mathcal LA\\B(R)\end{bmatrix}=k\bigr\}$
  （第一条定法秩、第二条就是 $(5a)$）；
* $\Delta_k(R)$：$Q_{\mathcal L}(\lambda)$ 的全部 $k\times k$ 子式的 gcd（$k=0$ 时约定为 $1$，$\mathcal A_0$ 上 $(5b)$ 自动成立）。

### Theorem 2（可容许层上"谱可行"是构造集）

对每个 $k$，
$$\mathcal C_k:=\bigl\{R\in\mathcal A_k:\ \Delta_k(R)\in\mathbb C^\times\bigr\}$$
是 $\mathbb C^{(q-r)\times n}$ 中的**构造集**。

*证明*：
1. $\mathcal A_k$ 是构造集：$\{\operatorname{rank}B\le k\}$ 与 $\{\operatorname{rank}[\mathcal LA;B]\le k\}$ 都是闭的（子式为零），
   与 $\{\operatorname{rank}B\ge k\}$（即 $\{\le k-1\}$ 的补）取交，得局部闭 ✓；
2. 在 $\mathcal A_k$ 上，$\Delta_k(R)\in\mathbb C^\times\iff\gcd(p_1,\dots,p_N)=1$（$p_i$ 为 $k$ 阶子式，
   $\deg\le k$）$\iff$ 存在乘子 $u_i$，$\deg u_i\le k-1$，使 $\sum u_ip_i=1$（**T1**，$D=k-1$）；
3. 把 $u_i=\sum_{j<k}u_{ij}\lambda^j$ 代入并匹配 $\lambda^j$ 的系数，得**线性系统** $M(R)u=b$，
   其条目是 $R$ 的多项式、右端是常数向量的系数；
4. 该系统可解 $\iff\operatorname{rank}[M(R)\mid b]=\operatorname{rank}M(R)$——秩条件，故是构造集 ✓。
5. $\mathcal C_k=\mathcal A_k\cap\{\text{该系统可解}\}$，两个构造集之交 ✓。$\square$

### Theorem 3（有限分层判定描述）

$$\boxed{\ \mathrm{FEAS}=\bigcup_{k=0}^{\min(m,n)}\mathcal C_k\ }$$
且每项 $\mathcal C_k$ 上法秩恒为 $k$、判据是**固定尺寸**的行列式条件。

*证明*：$R$ 可行 $\iff(5a)+ (5b)$；$(5a)\iff R\in\mathcal A_k$（某个 $k$）；$(5b)\iff\Delta_k\in\mathbb C^\times$（在 $\mathcal A_k$ 上，
因 $h=k$ 由 $\operatorname{nrank}=\operatorname{rank}B$ 给出）；故并集即 FEAS ✓。$\square$

### 三个必要的限定

1. **域**：$R$ 取**实数**（观测器问题的原意），$\lambda$ 取复数。于是只得到"**实构造集**"，
   判定仍是实代数问题；复情形（$R\in\mathbb C^{\cdot}$）才有 $\Delta_k\in\mathbb C^\times$ 的纯构造性陈述。
   **两种情形分开写**（专家第七轮 §2.2）。
2. **规模**：$\mathcal C_k$ 的描述规模 $\sim N(D+1)=kN$，$N=\binom{m}{k}\binom{n}{k}$；
   在中间层指数大 ⟹ 这是**结构性**定理，**不**给出多项式算法。
3. **不是硬度结论**：构造性**不**蕴含"比 $\exists\mathbb R$ 容易"；NP-hardness 仍是有效目标（专家 §3）。

## 有界次数 Bézout 引理（专家第七轮 §1.2 的证明，$D=d-1$）

**引理** 设 $\mathbb F$ 无限域，$p_1,\dots,p_N\in\mathbb F[\lambda]$，$\deg p_i\le d$，且 $\gcd(p_1,\dots,p_N)=1$。
则存在 $u_i$ 使
$$\sum_{i=1}^N u_ip_i=1,\qquad \deg u_i\le d-1\ \ (1\le i\le N).$$

*证明*（专家给的构造，本项目照录）：
1. $d=0$ 时某个 $p_i$ 是非零常数，取 $u_i=1/p_i$、其余 $0$ 即可。
2. $d\ge1$：取非零的 $p_1$ 并重编号。若 $p_1$ 是常数，同上。否则设其在代数闭包中的不同根为 $\alpha_1,\dots,\alpha_s$。
   由 $\gcd=1$，每个 $\alpha_j$ 至少有一个 $p_i$（$i\ge2$）在该点非零。
3. 考虑常数线性组合 $g=\sum_{i\ge2}c_ip_i$。对每个 $j$，"$g(\alpha_j)=0$" 是系数空间里的**真线性子空间**；
   有限多个真子空间不能覆盖整个空间（$\mathbb F$ 无限），故可取 $c_i$ 使 $g(\alpha_j)\ne0$ 对所有 $j$ 成立，
   于是 $\gcd(p_1,g)=1$。
4. 扩展欧几里得给 $a,b$ 使 $ap_1+bg=1$，且 $\deg a<\deg g\le d$、$\deg b<\deg p_1\le d$，故 $\deg a,\deg b\le d-1$。
5. 代回 $g$：$ap_1+\sum_{i\ge2}(bc_i)p_i=1$，全部系数多项式次数 $\le d-1$。$\square$

**在本项目的应用**：$d=k$ ⟹ 可取 $D=k-1$（$k\ge1$）；于是 Bézout 变量数是 $kN$ 而不是 $(k+1)N$
（$N=\binom{m}{k}\binom{n}{k}$），系数方程的 $\lambda$ 次数 $\le 2k-1$。$k=0$ 单独约定（$0\times0$ 子式 $=1$，条件自动）。

**这补上了上一轮可构造性论证的缺口**：截断到 $D=k-1$ 是**无损**的，故"$\Delta_k$ 非零常数 $\iff$ 截断后的线性系统可解"成立。


## 分层的**可容许**修正（专家第七轮 §1.4，重要）

上一轮把层写成 $\mathcal S_k=\{\operatorname{rank}[\mathcal L;CA;C]=k\}$。这**不够**：
$\operatorname{nrank}Q_{\mathcal L}=\operatorname{rank}[\mathcal L;CA;C]$ **只在 $(5a)$ 下**成立。

*证明（专家给）*：记 $B=[\mathcal L;CA;C]$。$(5a)$ 说 $\operatorname{row}(\mathcal LA)\subseteq\operatorname{row}B$，
故 $\operatorname{row}Q_{\mathcal L}(\lambda)\subseteq\operatorname{row}B$；反之对 $\lambda\ne0$，
$\mathcal L=\lambda^{-1}\bigl((\lambda\mathcal L-\mathcal LA)+\mathcal LA\bigr)$，右端在 $\operatorname{row}Q_{\mathcal L}(\lambda)$ 中，
连同 $CA,C$ 块得 $\operatorname{row}B\subseteq\operatorname{row}Q_{\mathcal L}(\lambda)$。故
$$\operatorname{rank}Q_{\mathcal L}(\lambda)=\operatorname{rank}B=k\quad(\lambda\ne0).$$

**正确的层**：
$$\boxed{\ \mathcal S_k^{(a)}:=\Bigl\{R:\ \operatorname{rank}B=k,\ \ \operatorname{rank}\begin{bmatrix}\mathcal LA\\B\end{bmatrix}=k\Bigr\}\ }$$
（第二条正是 $(5a)$）。**构造性定理必须写在 $\mathcal S_k^{(a)}$ 上**，否则 $\Delta_k$ 的下标与 $(5b)$ 里的 $h$ 不一致。

**修正后的三条定理（专家 §7 的定理包）**：
1. **Theorem 1**（有界次数 Bézout）：$\gcd$ 是单位 $\iff$ 存在次数 $\le d-1$ 的乘子使 $\sum u_ip_i=1$。
2. **Theorem 2**（可容许层上的构造性）：对每个 $k$，
   $\{R:\operatorname{rank}B=k,\ (5a),\ \Delta_k\in\mathbb C^\times\}$ 是**构造集**。
3. **Theorem 3**（有限分层判定描述）：
   $$\mathrm{FEAS}=\bigcup_{k=0}^{\min(m,n)}\{R:\operatorname{rank}B=k,\ (5a),\ \Delta_k\in\mathbb C^\times\},$$
   $k=0$ 用单独约定。


## 规模判据的**更正**（专家第七轮 §4.1）

上一轮写"$N_{\min}$ 多项式 $\iff\min(h,n-h,m-h)$ 有界"——**错**。反例：$m=\lfloor n/2\rfloor$、$h=m-1$，则
$m-h=1$ 有界，但 $\binom{n}{h}=\binom{n}{m-1}$ **指数大**。

**正确判据**（两个二项式必须**各自**受控）：
$$\boxed{\min(h,\ m-h)=O(1)\quad\text{且}\quad\min(h,\ n-h)=O(1).}$$
即两种边界情形：$h=O(1)$，或"$m-h$ 与 $n-h$ 同时 $O(1)$"。

**对本项目的两段**：
* $q$ 小 ⟹ $m=q+2p$ 有界 ⟹ $h\le m$ 有界 ⟹ $N_{\min}$ 多项式 ✓；
* "$q$ 接近终阶" **单独不够**——须核实是否真的使 $m-h$ 与 $n-h$ 同时有界（要用 $m,n,h,q,p$ 的精确关系，不能从阶数描述推）。

**并且**（专家 §4.3）：不要因为当前编码在中间层指数大，就把复杂度问题缩到常 $k$ 层——
中间层可能正是硬度归约需要的实例。建议分两层写：一般问题（如实说明编码可能指数）+ 边界层的多项式编码结果。

## 常法秩层上的可行性是不是**秩条件**？（$q1$ 的分水岭，本轮给出答案的雏形）

问题：$\{R\in\mathcal S_k:\ \mathcal E_K(R)=\varnothing\}$ 是不是构造集（即由秩条件定义）？

**关键的观察**（直接来自 Bézout 形式）：对固定的 $R\in\mathcal S_k$，把全部 $k\times k$ 子式记为
$p_1(\lambda;R),\dots,p_N(\lambda;R)$（$N=\binom{q+2p}{k}\binom{n}{k}$、$\deg\le k$）。则
$$\Delta_k\ \text{是非零常数}\iff \exists u_1,\dots,u_N\in\mathbb C[\lambda]:\ \sum_i u_ip_i(\lambda;R)=1 .$$
（$\gcd=1$ 的 Bézout 判据；$\mathbb C[\lambda]$ 是 PID，无需代数闭性。）

**把 $u_i$ 截断到次数 $\le D$**（$D$ 为有限 Bézout 界，见上一节），则
$$\sum_i u_ip_i=1$$
是关于 $u$ 的**线性方程组**，系数是 $R$ 的多项式。记其（Bézout/Sylvester 型）矩阵为 $M(R)$，右端为 $b$。于是
$$\boxed{\ \Delta_k\ \text{非零常数}\iff \operatorname{rank}\bigl[M(R)\,\big|\,b(R)\bigr]=\operatorname{rank}M(R)\ }$$
即**可解性是 $R$ 的秩条件**。因此
$$\{R\in\mathcal S_k:\ \Delta_k\ \text{非零常数}\}$$
是 $\mathcal S_k$ 中的**构造集**（有限个"秩 $=j$"条件的布尔组合）。

**这意味着什么（若成立）**
1. DEC 的可行性集合是**构造集**（在 $\mathbb C$ 上），而非真正的半代数集；
2. 于是判定问题落在**代数闭域的存在理论（ECF）**而非 $\exists\mathbb R$——专家第六轮把 DEC-Θ 描述为
   "rational input, real variables"，若变量取**复**（$R\in\mathbb C^{(q-r)\times n}$），则上界可从 $\exists\mathbb R$ 收紧为 ECF；
3. 若变量必须取**实**，则构造集与 $\mathbb R$ 相交仍是构造集（实构造集），判定仍是实代数问题，
   但对象是构造集——比一般半代数集小得多。

**必须讲清的限定（不要当成已证定理）**
* 第一步（Bézout 判据）是**标准**的，但要与上一节的**有限次数界 $D$** 配套，而 $D$ 的显式界尚未逐字证明；
* 第二步（截断到 $D$ 的线性系统与原条件等价）依赖 $D$ 的正确性；
* "$R$ 取 $\mathbb C$ 还是 $\mathbb R$" 决定收紧到 ECF 还是停在实构造集——**这一点要请专家定**；
* 规模：$M(R)$ 的尺寸 ~ $N(D+1)$，在中间层指数大 ⟹ 这是**结构性**结论，不是多项式算法。

**结论（本轮的答案雏形）**：层上的可行性**是**构造集（在 $R$ 取复数时），
因此 $q1$ 的对象更像"构造集非空性"而非"半代数可行性"；但**规模**仍是指数的，
且变量域（复/实）尚未钉死。这两点决定它能不能变成算法。

**下一步的真实问题**：常法秩层上的判定能否化成**秩条件**（而非实代数求解）？若能，$q1$ 假；
若不能，那份"实代数性"就是硬度的来源之一。

### 规模审计结果（`tools/verification/bezout_size_audit.py`）

对 $m=q+2p$、$n$、法秩 $h$，Bézout 编码的规模是
$$\text{vars}=(q-r)n+(h+1)\underbrace{\binom{m}{h}\binom{n}{h}}_{N_{\rm min}},\qquad \#\text{h-minors}=N_{\rm min}.$$

实测（$p=1,r=1$）：

| 情形 | $h$ | $N_{\rm min}$（$n=6/8/10/12$）|
|---|---|---|
| $h=n-1$（余维 1）| $n-1$ | 336 / 960 / 2200 / 4368 |
| $h=n/2$（中间）| $n/2$ | 1120 / 14700 / **199584** / **2774772** |
| $h=q+2p$（本项目典型，$q$ 小）| 小 | 20–252（$n=6..10$）|
| $q$ 接近终阶（$q\approx n-p$）| $n$ | $\binom{m}{n}\binom{n}{n}$ 很小（1–11）|

**结论**：
1. $h$ 由 $\min(h,\ n-h,\ m-h)$ 控制：该量**有界**时 $N_{\rm min}$ 是 $n$ 的多项式；
   $h\approx n/2$ 时由 Stirling 公式**指数级**增长（$n=12$ 已达 $2.77\times10^6$）。
2. 本项目关心两段：$q$ **小**（$h=q+2p$ 小）与 $q$ **接近终阶**（$h=n$）。**两段的 $N_{\rm min}$ 都很小**
   （最多几百），故 **Bézout 编码在这两段是多项式规模的**；
   中间段（$q\approx n/2$）会爆炸。
3. 因此：
   * 对**固定阶判定**（$q$ 给定、常法秩层）Bézout 编码可用，规模可算；
   * 对**一般归约**（$q$ 随 $n$ 变化、$h$ 落在中段）Bézout **不**给多项式规模——
     硬度归约若走这条路，必须把实例族限制在 $h$ 远离 $n/2$ 的层（或改用"单 $\lambda$"接口）。

**状态**：引理本身是经典结论，但**我们尚未逐字证明**（尤其"$\deg u_i\le D$"这一步的归纳要写清）；
规模记账已写出。两项都列入待办，不当作已证。

### (iii) Bézout 证书（专家 §3.5，等价于 (i) 但更适合做 $\exists\mathbb R$ 编码）

设极大子式为 $p_1(\lambda;R),\dots,p_N(\lambda;R)$。则
$$\Delta_h\ \text{是常数}\iff\exists u_1,\dots,u_N\in\mathbb C[\lambda]:\ \sum_{i=1}^N u_i(\lambda)\,p_i(\lambda;R)=1,$$
且当 $\deg p_i\le D$ 时 $u_i$ 的次数可**多项式界定**（逐个做两两 Bézout）。
这把谱条件变成**有限组系数方程**，比"逐图卡的秩检验"更适合整体编码。

### (iv) 三个接口的分工（专家 §3.5 的建议，本项目采纳）

| 接口 | 性质 | 用途 |
|---|---|---|
| F.1 秩屏障 | **必要** | 廉价淘汰整层（$\rho>\min_\lambda r(\lambda)$）|
| B.13c 覆盖判据 | **充分**（需 $\mathcal B=\varnothing$）| 几何式的"整族不可行" |
| **$\Delta_h$ / Bézout** | **精确** | 固定候选可判；参数化后即 AVOID 的精确表述 |
