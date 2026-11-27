# 08 · 结果汇总（给写作与对外沟通用）

> 本文是**结果的收敛版**：只列已经站得住的陈述、它们的等级、以及一句话证明或指针。
> 与 `02_theorems_proven.md` 的区别：02 按命题编号（A.x / B.x）组织，本文按**写作/叙述**组织
> （两个机制 + 精确判据 + 反例），并且**只收当前仍成立的**陈述。
> 检验分四级：`[已证-纸面]` / `[精确验证 n/N]` / `[Lean]` / `[猜想]`。
>
> **2026-11-26 依赖规则**：Paper I / Paper II 覆盖的结论（压缩、沙包、结构界、$\exists\mathbb R$ 上界、
> 固定阶与 FPT、最小阶与谱下界）在对外写作中优先引论文；本文保留**论文未覆盖**的旧框架 $(\rho,c)$
> 结果、反例与进一步探索得到的固定成果——它们仍是本项目的独立结果，按各自等级标注。冲突时以论文为准。

---

## 1. 问题与定位

给定 $(A,C,L_0)$，求最小 $q$ 与 $R$，使 $\mathcal L=[L_0;R]$（$q$ 行）满足
$$(5a)\ \operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]=\operatorname{rank}[\mathcal L;CA;C]\ \forall\lambda\in\mathbb C .$$
$q1$（$q_{\min}$ 的计算复杂度）**开放**。

**定位**（2026-10-30 起、2026-11-03 明确）：文献已给出存在性、阶谱、逐阶充要、构造；$(5a)$ 只作**定义域**。
本项目在 $(5b)$、阶谱、**阶差**上工作：现在问题被切成"**维数障碍**（已数字化）"与"**谱障碍**（开放）"两半。

记号：$W=\operatorname{row}[C;CA]$、$r_1=\dim W$、$V=\ker[C;CA]$、$K=\ker[C;L_0]$、
$S=\operatorname{row}[C;L_0]+W$、$s_0=\dim S$、$\mathcal Z=\ker[C;\mathcal L]$（$d=n-p-q$）、
$h=\operatorname{rank}[\mathcal L;CA;C]$、$n_0=\operatorname{rank}\mathcal O_C$。

---

## 2. 精确判据（已证 / 已引用）

| # | 陈述 | 等级 | 位置 |
|---|---|---|---|
| 2.1 | $(5b)\iff d_{\rm fin}=0\iff\sum_j\varepsilon_j=\operatorname{rank}\mathcal L$（$\varepsilon_j$ 为 $Q_{\mathcal L}$ 的左最小指标）| [已证-纸面] | `02_theorems_proven.md` B.6–B.8；`proof/left_index_count` |
| 2.2 | 固定增广的 Toeplitz 判据：$(5b)\iff\nu_s=(s+1)m-s$，$s=\operatorname{rank}\mathcal L$、$m=q+2p-h$；序列由 $\nu_d-2\nu_{d-1}+\nu_{d-2}$ 恢复 | [已证-纸面] + [精确验证 66/66]（对 Smith 路径）| `proof/toeplitz_criterion` |
| 2.3 | $(5b)$ 只需在 $\operatorname{spec}\Lambda$ 上检查（$Q_{\mathcal L}=D(\lambda)H$，$D$ 在其外可逆）；坏 $\lambda$ 可为**复根** | [已证-纸面] + [精确验证 3/3] | `proof/eigenvalue_confinement`（B.10）|
| 2.4 | 零空间铅笔判据：$(5b)\iff\operatorname{rank}[(\lambda I-A)V\ \ Z]=\operatorname{rank}[V\ \ Z]\ \forall\lambda$ | **引用**文献（Thm 4） | `03_theorems_cited.md`；实现见 `tools/verification/verify_Q1_nullspace.py`（与 2.2 交叉 6/6）|
| 2.6 | **谱条件的可观性归约（专家 2026-11-04 §3）**：$(5b)\iff\mathcal L(\ker[C;CA])$ 不含 $\Lambda$ 的非零特征向量$\iff(E,\Lambda)$ 可观测 $\iff\operatorname{rank}[E;E\Lambda;\dots;E\Lambda^{q-1}]=q$ ⟹ **给定候选的谱检验 = 一个 $q$ 维可观性秩计算（多项式时间）** | [已证-纸面] + [精确验证 44/44] | `docs/02` B.12；`tools/verification/observability_test.py` |
| 2.5 | 整数障碍的几何形式：$h=\dim(\mathcal Z^\perp+W)=s_0+\dim\pi(V')$ | [已证-纸面]（两行）+ [精确验证 495/495、360/360] | `proof/h_formula`（B.11）|

## 3. 维数障碍与整族一致（本文档的主结果之一）

**定义**：某阶的失败是**维数型的**，当且仅当 $h\ge q+r_1$。

| # | 陈述 | 等级 |
|---|---|---|
| 3.1 | **（2026-11-04 重写为无条件式）** $h=s_0+q-\dim(R\cap S)$，其中 $R=\operatorname{row}\mathcal L$、$S=\operatorname{row}[C;L_0]+W$；故 $h\le s_0+q-r$，等号 $\iff\mathcal Z^\perp\cap S=C\oplus L_0$ | [已证-纸面] + [精确验证 35/35、54/54] |
| 3.2 | **推论**：Type I $\iff R\cap W=0$；而在 $s_0=r_1+r$（这是 Type I **可能**的唯一情形，因 $s_0\le r_1+r$）时 Type I $\iff R\cap S=L_0$ | [已证-纸面] + [精确验证（Type I ⟺ $R\cap W=0$ 无反例）] |
| 3.3 | **无条件推论**：$s_0<r_1+r$ ⟹ 任何 $\mathcal L$ 都**不是** Type I（计数障碍在该阶不可能触发，与 $\mathcal L$ 无关）| [已证-纸面] + [精确验证：$s_0<r_1+r$ 的 39 个样本中 Type I 出现 0 次] |
| 3.4 | 若 $h=n$ 则该阶 $(5a)$ **自动成立**（$\mathcal Z^\perp+W=\mathbb C^n$）| [已证-纸面] + [精确验证 117/117] |

**注意（2026-11-04 更正）**：原 3.1/3.2 用了一个**没有内蕴定义**的 $V'$（"图表新增部分"）与假设 $V'\cap S=0$；
专家指出该假设不可独立检验。现已换成上面的**无条件**形式（$h=s_0+q-\dim(R\cap S)$，只用到
$S=\operatorname{row}[C;L_0]+W$、$R=\operatorname{row}\mathcal L$ 与 $\operatorname{row}L_0\subseteq R$），
$V'$ 与那条假设**不再使用**。

**应用（公开例子）**：$n=8$、$p=r=2$、$r_1=4$、$q_0=3$、$s_0=6=r_1+r$（故 Type I 在**每一阶都可能**）。
$q=3$：$h=7=q+r_1$ ⟹ 全部 Type I（**已证**，虽无显式 $\mathcal L$ 可行性之争，但障碍确定）；
$q=4$：486/486 全为 $h=8=q+r_1$ ⟹ 全部 Type I；
$q=5$：存在 $R$ 使 $R\cap W=0$（显式 5 行见证）⟹ 可行。故 $q_{\min}=5$，整阶谱由计数解释。

## 4. 谱障碍：整族不可行的精确例子（主结果之二）

| # | 陈述 | 等级 |
|---|---|---|
| 4.1 | 存在 $n=6$、$p=r=2$、$q_0=3$、$r_1=4$ 的实例：$h=6<7$ 且**每个** $q_0$ 阶可行增广都失败 $(5b)$ | [已证-纸面] + 证书 |
| 4.2 | 该实例 $s_0=5$、$t=1$ ⟹ $h=6=n$ ⟹ $(5a)$ 自动（用 3.3）| [已证-纸面] |
| 4.3 | 比例性：$L_0Ax$ 与 $L_0x$ 对 $x\in V$ 总成比例（$2\times2$ 行列式在 $V$ 上恒零）⟹ $\lambda(x)$ 合法 | [已证-纸面] + 证书（极化恒等式：基 + 基和）|
| 4.4 | 坏点映射 $\Phi:\mathbb P(V)\to\mathbb P(K)$ 非平凡 ⟹ 满射 ⟹ 整族掉秩 | **降级为条件性**（专家 2026-11-04：① 需先引用 4.3 的比例性；② $L_0\|_V$ 秩为 **1**，公式在 $\mathbb P(V)$ 上有无定义点，开子集上的映射不能直接用完备性）——定理本身由**三套代数证明**支撑（见 4.7、4.7b 与逐图卡 gcd），不依赖几何论证 |
| 4.5 | 该实例 $q=4$ 全可行 ⟹ $q_{\min}=4$ | [精确验证]（补构造扫描）|
| 4.6 | 一般充分条件：若 $h=n$ 且 $\dim\overline{\Phi(\mathbb P(V))}\ge q-r$，则该阶无解 | [已证-纸面]（射影维数定理）|
| 4.7b | **第三种独立证明**（专家建议的判据）：Bézout 系数矩阵 $M(\theta)$ 的左零空间给出 $C_j(\theta)=y_j^{\mathsf T}e_0$，$(C_j)=(1)$ ⟹ 无 $\theta$ 使 $e_0\in\operatorname{col}M$ ⟹ $(5b)$ 处处失败（C4 两图卡均为 $(1)$）| [精确计算（sympy）] | `tools/verification/bezout_rank_test.py`；`attempts/45` |
| 4.7 | **第二种独立证明**（纯代数）：逐图卡算极大子式在 $\mathbb Q(\theta)[\lambda]$ 中的 gcd，两图卡一般点 $\deg=2$、例外点 $\deg=1$ ⟹ 所有 $\theta$ 都失败 | [精确计算（sympy）] | `tools/verification/chart_gcd_analysis.py`；`attempts/41` |

**适用范围**（必须写清）：$4.6$ 需要 (i) $h=n$；(ii) 坏点映射有定义（$z(x)\in K$，$r\ge2$ 时是 2 方程 1 未知数，
通常不成立）；(iii) 用像**闭包**时需保证交点在像内（曲线情形自动）。随机实例上 (i) 仅 3/22 满足（3/3 判对）。

## 4.8 逐阶判定的**符号闭环**（对参数 ≤3 的图卡）

由 sympy 实现（`tools/verification/decide_symbolic.py`）：逐图卡算 $P_{\mathcal Z}(\lambda)$ 极大子式在
$\mathbb Q(\theta)[\lambda]$ 中的 gcd；$\deg_\lambda=0$ ⟹ 代入有理 $\theta$ 得见证（过七条一致性检查）；
所有图卡 $\deg\ge1$ ⟹ gcd 证书。**不使用网格**。已知结果：C4 的 $q_0$ 阶 INFEASIBLE（例外点已逐个核验：$\deg=1$，掉落轨迹为空）；
公开例子 $q=5$ FEASIBLE（$\theta=0$ 的 5 行见证）。

**注意（2026-11-03 更正）**：图卡上"一般 $\theta$ 下 $\deg_\lambda\gcd\ge1$"**不能**推出"所有 $\theta$ 都失败"——
gcd 的次数会在特殊 $\theta$ 上**掉落**。据专家 §3.3/§3.5 建议，这里只记录为**观察**（不当作定理）：

> **观察（最低阶专门化现象）**：与被测实例对照后应分**两类**——
> * **一般可行**（在某个分支上典型 gcd 的 $\lambda$ 次数为 0）：该分支上**一般** $\theta$ 谱可行；
>   注意 **不能**由此推出"每点可行"——逐点需另验 $M_\rho$ 满行秩（专家 2026-11-03 §3.6/§4.4）；
>   我们此前对 seed 3023、3027 说"处处可行"**说过头了**，应改为"一般可行"；
> * **一般失败**（典型 gcd 次数 $\ge1$）：$X_{\rm sp}\subsetneq X$，可行点被限制在"专门化后 gcd 次数掉到 0"的轨迹上
>   （$n=6$ 反例上该轨迹为**空**）。
>
> 因此"$q_0$ 阶可行集总是薄"**不成立**；薄性只在第二类出现。该二分目前只是**观察**，未证明。
>
> **形状更正（专家 §3.5）**：可行集一般只是 **constructible**，不必开、不必闭。
> 反例：$f=\theta\lambda+1$、$g=2\theta\lambda+2$ 的好集是 $\{\theta=0\}$（闭集）。
> 正确的组织方式是**按代数可容许族的不可约分支**：每个分支上"典型确定性除子次数"决定一般谱可行，
> 一般不可行分支上的例外可行点是构造性且在该分支中不稠密。

也不应声称"可行集是有限确定集"：它只是 **constructible**；"典型 gcd 次数"必须说明是哪个参数空间的典型点
（整图卡 vs 代数可容许子簇）。C4 的例外点上 $\deg=1\ne0$，故其不可行性成立（并有第三个证明，见 4.7b）。

## 4.9 逐阶判定的**现役工具**：$\theta$ 上的行列式消元

把 $(5a)$（用辅助矩阵 $T$ 的列空间包含）、层条件、$(5b)$（Bézout 秩等式）都化成 $\theta$ 的多项式条件
（$T,u$ 线性、在 $\mathbb Q(\theta)$ 上消去），再做 Gröbner：基 $=[1]$ ⟹ 该图卡典型层无可行点。

实测（$q_0$ 阶，26 个实例，约 19 s）：**15 FEASIBLE（带见证、过七条检查）+ 9 INFEASIBLE（常数图卡，完整）+ 2 UNKNOWN**。
C4 的两图卡都给出 $[1]$ ⟹ 其第四个独立证明。边界：一般图卡的不可行结论只到**典型层**
（`INFEASIBLE_TYPICAL`），秩跌落点未覆盖。

## 4.10 $q_{\min}$ 的上界表与阶差的经验规律

见证优先的扫描（构造 $\mathcal L$ 后核 $(5a)$、$(5b)$、七条检查）覆盖 89 个实例（$n=5,6,7$）仅需 **48 秒**：

| 结果 | 数量 |
|---|---|
| 得到 $q_{\min}$ 上界（带见证）| **74** |
| 无见证（`NO_WITNESS`，**不是**不可行证明）| 15 |

阶差 $q_{\min}-q_0$：**0 有 55 例、1 有 18 例、2 有 1 例**；且与 $r$ 强相关：

| 组 | 平均阶差 |
|---|---|
| $r=2$ | 0.00–0.12 |
| $r=1$ | 0.40–0.50 |

即 $r=2$ 的实例几乎总是 $q_{\min}=q_0$。

**更精确的算术形式（$[已证]$ 充分方向）**：由 B.9（$(5b)\Rightarrow h<q+r_1$）与整族一致，
在 $V'\cap S=0$ 时 Type I $\iff s_0\ge r_1+r$。而
$$s_0=\dim(\operatorname{row}[C;L_0]+W)=(p+r)+r_1-\dim(\operatorname{row}[C;L_0]\cap W),$$
故
$$s_0\ge r_1+r\iff\dim(\operatorname{row}[C;L_0]\cap W)=p\iff \operatorname{row}L_0\cap W\subseteq\operatorname{row}C .$$
于是
$$\operatorname{row}L_0\cap W\subseteq\operatorname{row}C\ \Longrightarrow\ q_0\ \text{阶不可行}\ \Longrightarrow\ q_{\min}>q_0 .$$

**2026-11-04 更正（专家 §10.1 指出后复核）**：此前把该条件写成
"$\dim(\operatorname{row}L_0\cap W)\le p$" 是**错的**（两者不等价；且因 $\operatorname{row}C\subseteq W$，
一个非零的 $\operatorname{row}L_0\cap W$ 反而指向"非 Type I"）。用 89 个实例的实测复核
（`tools/verification/gap_criterion_check.py`）：

| 判据 | 命中 | 假阳性 | 漏 | 真阴性 |
|---|---|---|---|---|
| 旧：$\dim(\operatorname{row}L_0\cap W)\le p$ | 19 | **55** | 0 | 0 |
| 新：$\operatorname{row}L_0\cap W\subseteq\operatorname{row}C$（$\iff s_0=r_1+r$）| 18 | **0** | 1 | 55 |

即旧形式**几乎无信息**（55 个假阳性），新形式无假阳性。

## 4.11 Type III（谱障碍）：现状

**定义**：$h<q+r_1$（故不属 Type I）、$k\le s$（故不属"计数不足"）、但 $d_{\rm fin}>0$。
由 B.9b，"计数不足"一类是空的，所以 **$(5b)$ 的失败只有 Type I 与 Type III 两类**。

| 项 | 状态 |
|---|---|
| 给定 $\mathcal L$ 的判定 | ✅ **完全可判**（三条独立的精确判据）：Toeplitz 零度 $\nu_s=(s+1)m-s$、极大子式 gcd、零空间铅笔秩条件；互校 66/66 与 6/6 |
| 全族反例（$A$ 侧）| ✅ **C4**：$n=6$、$p=r=2$、$q_0=3$，每个可容许 $Z$ 都 Type III（$d_{\rm fin}=2$），**四套独立证明**；阶差 1 |
| **第二个整族 Type III 实例（阶差 2，已证）** | ✅ 反向构造 + 符号证书：$n=6,p=r=2$，$q_0=2$ 为 Type I、$q=3$ 为**整族** Type III（两张卡 $\gcd=\lambda+2$、首项系数 1、共同根 $\lambda=-2$ 与 $\theta$ 无关 ⟹ **跌落 locus 为空**）、$q=4$ 有显式见证 ⟹ $q_{\min}=4$，阶差 2 | [已证-纸面] + [精确验证] | `proof/type3_second_example/`、`attempts/63` |
| **阶差可加（两副本数据点）** | ⚠️ 证据：gap-2 实例与自身直和（$n=12$）后 $q_0=4=2+2$、$q_{\min}=8$、阶差 $4=2+2$；$q=4..7$ 共 1820 个候选**无可行点**，$q=8$ 有块对角见证。Lemma B（上界）已核；Lemma A（下界）未证（需排除混合增广）| 精确验证（采样，无证明）| `attempts/71`、`tools/verification/two_copy_gap.py` |
| **单-$\lambda$ 机制的轨迹 + 沿一条形变线的观测** | ⚠️ **谨慎表述（专家 2026-11-04 §1.1）**：已证的是"单-$\lambda$ 证书（$\exists\lambda:(\lambda I-A)V=K$）是一个显式代数充分轨迹"；沿 $A_{00}=t$ 的**一条**形变线上只有 $t=2$ 不可行（其余 23/26 可行），但这**不**证明整个不可行轨迹的余维——**余维仍开放**。该线上 $\varepsilon=0$ 恒成立（$U_1=(-t-4)U_0$）⟹ $\varepsilon=0$ 不蕴含整族不可行 | 精确验证（10 个 $t$ × 26 候选）；余维未证 | `attempts/64`、`docs/02` B.13e |
| **$\varepsilon=0$ 的三情形刻画（B.13d）** | ✅ **已证**：$\operatorname{rank}U_0=0$ 自动；$=1$ 时 $\iff\operatorname{im}U_1\subseteq\operatorname{im}U_0$；$\ge2$ 时 $\iff U_1=\alpha U_0$。故 $\varepsilon=0$ 是**纯秩判据**（不需 Gröbner）。**已撤回**："Type III $\Rightarrow\varepsilon=0$"——我们的 $n=7,2,2$ 与 $n=8,3,2$ 实例 $\varepsilon\ge1$ 却有 Type III 候选 | [已证-纸面] + 5983/5983 | `docs/02` B.13d |
| Type III 的**整族**判据（B.13/B.13b）| ✅ **已证**：$h=n$ 时，若坏点像的维数 $\dim S\ge q-r$ 则整族不可行；而 $\dim S\le n-r_1-1-\varepsilon$（$\varepsilon$ = 比例性轨迹的余维），故必要条件为 $q-r+\varepsilon\le n-r_1-1$。C4 是 $\varepsilon=0$ 且取等的情形（实测唯一满足者）| `docs/02` B.13、B.13b |
| Type III 何时发生 | ⚠️ **只有经验规律 + 一个已证的覆盖判据**：随机实例 1501 个谱区样本中 **0** 例；结构化族 45 个谱区样本中 17 例。**2026-11-04 更正**：此前说"Type III 只在 $r_1=p+r$"是**错的**——实测 $n=8,p=3,r=2,q_0=3$ 的实例 $r_1=6>p+r=5$ 仍有 Type III 候选（30 中 1）；真正相关的是**余维条件** $\dim S\ge q-r$（$S$ = 坏点直线的像，见 `docs/02` **B.13** 的覆盖判据）|
| 逐阶判定工具 | ⚠️ 见 §4.8/§4.9：`joint_theta` 在 26 个实例上 24 个给出证书化结论；`witness_scan` 89 实例 48 s 给 74 个上界；但**一般图卡的不可行只到"典型层"** |
| 一般判据（$\exists$ 谱可行增广）| ❌ **没有**：无多项式算法、无归约；秩跌落点（gcd 掉落到 0 的 locus）未刻画（需子结式）|
| 编码规模 | ❌ 指数（$N=\binom{1.5n-3}{n}$），故朴素 $\exists\mathbb R$ 路线不成立 |

**一句话**：Type III 的"单点判定"已完全解决，"整族/一般判据"只有 C4 这一个整族定理与经验规律。

### 4.11.0 专家 2026-11-04 对"$r_1=p+r$"的反驳与正确提法

我们曾把"Type III 只在 $r_1=p+r$ 出现（4/4）"当作候选定理。专家指出：若坏点映射 $\Phi:\mathbb P(V)\dashrightarrow\mathbb P(K)$
是**支配**的，维数条件只给
$$\dim\mathbb P(V)=n-r_1-1\ \ge\ \dim\mathbb P(K)=n-p-r-1\iff r_1\le p+r,$$
**不**强制等号；且 $r>1$ 时比例性条件 $L_0Ax\in\operatorname{span}\{L_0x\}$ 额外削减定义域，实际的
incidence 域可能维数更小。正确提法是研究**incidence variety**
$$\mathscr I=\{([x],[z],\lambda):x\in V,\ z\in K,\ (\lambda I-A)x\in\operatorname{span}(z),\ \text{非零条件}\}$$
到 $\mathbb P(K)$ 的投影的支配性，并且**第一步要证的是 incidence 域的维数上界**（若 $\le\dim\mathbb P(K)$，
等号才成为支配的必要条件）。**因此在证出该维数界之前，$r_1=p+r$ 只能写成"等维边界上的观察"，不是定理。**

### 4.11.1 专家 2026-11-04 给出的 Type III 不变量（尚未实现）

* **逐分支的典型不变量**：固定可容许簇的一个不可约分支 $Y$ 并在其上固定秩层，令
  $$g_Y:=\deg\gcd\bigl(\text{$P_y(\lambda)$ 的极大子式}\bigr)\in\mathbb Z_{\ge0}\quad(\text{在 }\mathbb C(Y)[\lambda]\text{ 上取 gcd}),$$
  则 $g_Y=0$ ⟺ 该分支的典型点无有限谱障碍；$g_Y>0$ ⟺ 典型点有。
  **注意**：专门化会改变 gcd 的次数——$g_Y>0$ 的分支仍可能含"专门化后 gcd 变成常数"的例外可行点。
  这正是我们此前把"典型次数"误当"处处"的根源。
* **实例（我们的计算）**：C4 的两个图卡上 $g_Y=2$（一般点 $\deg_\lambda\gcd=2$，例外点 $1$），正是"$g_Y>0$ 但存在例外可行点"的边界情形在 C4 上**不发生**（例外点仍 $\deg=1\ne0$）——与逐图卡符号 gcd 的结论（`attempts/41`）一致。
* **精确的整族不变量**：相对有限因子轨迹
  $$\mathscr D_Y=\{(y,\lambda):\operatorname{rank}P_y(\lambda)<\operatorname{normalrank}P_y\},$$
  它到 $Y$ 的投影就是谱失败轨迹；$y$ 谱可行 ⟺ 该点的纤维为空。
* **比"constructible"更锐（已证，B.10b）**：在 $\Lambda$ 可正则选取的图卡、固定秩层
  $\Sigma=\{\operatorname{rank}[V|Z]=\rho,\ h=h_0,\ (5a)\}$ 上，坏 $\lambda$ 必满足 $\det(\lambda I-\Lambda(\theta))=0$（B.10），
  于是谱失败轨迹是 $\{(\theta,\lambda)\in\Sigma\times\mathbb P^1:\ \operatorname{rank}P<\rho,\ \det(\lambda I-\Lambda)=0\}$
  的投影；$\mathbb P^1\to\mathrm{pt}$ 紧合 ⟹ 投影闭 ⟹ **层上失败集闭、可行集开**。
  **但**跨层（不同 $\rho$ 或 $h$）取并时只是 constructible——两种陈述不矛盾，关键是"层内"。见 `docs/02` B.10b。

## 5. 不作声称（写在最前面避免误读）

* 维数恒等式（2.5）是初等的；**可能新的是 $h=s_0+q-\dim(R\cap S)$（B.11c）与"$s_0<r_1+r$ 时无 Type I"这一无条件排除**。
* 谱反例（4.1）分离了两种机制，但**不是**分类。
* **无复杂度结论**：既无多项式算法、也无归约。
  **关于 $\exists\mathbb R$ 成员性（2026-11-04 更正之更正）**：这一条我们先后写错过两次，现在定稿如下。
  * **成立**（G.1，[已证-纸面]）：每个固定阶 $q$ 的 $\mathrm{DEC}(q)\in\exists\mathbb R$，且编码是**多项式规模**：
    结构化左逆 $X(\lambda)P(\lambda)=I_t$（对 $X$ 系数线性、$t^2q=O(n^3)$ 个未知数、$\deg X\le t-1\le n$，
    次数界用 Noferini–Van Dooren 的铅笔右逆判据），退化层用 **$O(n)$ 项**"$s=\dim(Z\cap\mathcal V)$"析取
    $+$ 在商 $V/S$ 上做左逆处理 —— **不需要**广义逆或 Smith 酉模的次数控制。
  * **之前的错**：2026-11-03 我们按"列出全部极大子式的非结构化 Bézout $\sum u_im_i=1$"估规模，
    得到 $N=\binom{1.5n-3}{n}$ 指数（实测 $\log_2N/n\to1.09$）就宣布"$\exists\mathbb R$ 路线作废"——
    那是**另一个写法**的规模，不适用于 G.1 的编码。该错误已在 `docs/02` G.1 与 `attempts/58` 顶部
    标注；指数规模数据仅作为"非结构化变体"的说明保留。
  * **更短的编码（G.2，2026-11-04）**：用可观性归约（B.12）可把谱条件换成一个 $q$ 维可观性秩检验的证书，变量/约束 $O(q^3+qn)$、次数 $\le2$、对 $s=\operatorname{rank}\mathcal L(V)$ 作 $q+1$ 项析取；已在两个已知见证上显式构造全部辅助变量并通过 16 条约束。比 G.1 的 Bézout 左逆编码更短（不需要 $t^2q$ 个系数与 NVD 次数界）。
* **仍未定**：$\exists\mathbb R$-hard 与多项式算法（$q1$ 本体）。
* 随机族上的"整数障碍是唯一障碍"只是**小样本观察**（$n\le9$），按专家意见降为猜测。

## 6. 与文献的关系

| 内容 | 归属 |
|---|---|
| 存在性、阶谱 $[q_0,n_0-p]$、$q_{\min}=\min\Sigma_{FO}$、终点阶谱可行（$q_{\min}\le n_0-p$）| 文献（Thm 7 等）|
| 逐阶充要（零空间铅笔、图卡参数化）| 文献（Thm 4/5/6）|
| 整数障碍的几何化与**整族一致** | 本项目（未见于文献，见 3.2）|
| 整族谱不可行的精确例子 | 本项目（4.1）|
| Toeplitz 判据 | 专家建议、本项目证明（2.2）|

## 7. 指针

* 命题索引：[02_theorems_proven.md](02_theorems_proven.md)；引用定理：[03_theorems_cited.md](03_theorems_cited.md)
* 开放问题：[05_open_questions.md](05_open_questions.md)
* 工作清单（做过什么、别再重复）：[09_work_inventory.md](../workspace/support/project_management/09_work_inventory.md)
* 对外短 note 草稿（已废弃）：[archive/paper_drafts/workspace_2026-11/paper_draft/00_note_draft.md](../archive/paper_drafts/workspace_2026-11/paper_draft/00_note_draft.md)
