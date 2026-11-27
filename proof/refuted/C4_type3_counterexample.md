# C4 —— 猜想 T 被推翻：$q_0$ 阶存在 $h<q_0+r_1$ 但 $d_{\rm fin}>0$ 的增广

## 被推翻的陈述

**T**（本项目 2026-11-02 提出，2026-11-03 报给专家）：在 $q=q_0$ 处
$$(5b)\iff h<q_0+r_1 .$$
等价说法：最小阶上的失败**总是**零指标型（Type I）。

## 反例（精确、可复现）

$n=6$、$p=2$、$r=2$，
$$A=\begin{pmatrix}1&1&&&&\\&1&&&&\\&&2&1&&\\&&&2&&\\&&&&1&1\\&&&&&1\end{pmatrix}$$
（三个 $2\times2$ Jordan 块：特征值 $1,2,1$，全部为重复特征值），
$$C=\begin{pmatrix}0&0&1&1&1&1\\1&0&0&0&0&0\end{pmatrix},\qquad
L_0=\begin{pmatrix}0&0&8&20&1&4\\1&3&0&0&0&0\end{pmatrix}.$$

则 $r_1=\operatorname{rank}[C;CA]=4$、$q_0=3$（功能指标算法），且
$$L=\begin{pmatrix}0&0&8&20&1&4\\1&3&0&0&0&0\\0&0&1/4&1&0&0\end{pmatrix}$$
满足：

| 检查 | 结果 |
|---|---|
| $(5a)$ | ✓ |
| $\operatorname{row}L_0\subseteq\operatorname{row}L$ | ✓ |
| $\operatorname{rank}L=q_0=3$ | ✓ |
| $h=\operatorname{rank}[L;CA;C]$ | $6$ |
| $h<q_0+r_1$ | $6<7$ ✓（**B.9 不适用**）|
| $k=q+r_1-h$ | $1\le s=3$（**Type II 不适用**）|
| 左指标 $\varepsilon$ | $[1]$ |
| $d_{\rm fin}=s-\sum\varepsilon$ | $2>0$ ⟹ **$(5b)$ 失败** |

**三重核验**（[verify_C4_type3.py](verify_C4_type3.py)）：
1. Toeplitz/Smith 路径：`five_b = False`、`d_fin = 2`；
2. 零空间判据 $P(\lambda)=[(\lambda I-A)V\mid Z]$：极大子式 gcd 次数 $=2>0$（有有限公共根）；
3. 逐条 `assert`：$(5a)$、包含性、秩 $=q_0$。

## 坏 $\lambda$ 的定位

对反例候选直接扫有理 $\lambda$（$\operatorname{rank}Q_{\mathcal L}(\lambda)<h$）：

| 候选 | $d_{\rm fin}$ | 秩降的有理 $\lambda$ |
|---|---|---|
| #1（本文主反例）| 2 | $5/3$ 与 $3$ |
| #2 | 2 | $1$（重根）|

即障碍可以**精确定位到有理特征值**上（[type3_bad_lambda.py](../../tools/verification/type3_bad_lambda.py)），
不需要特征多项式或有理根定理。

## 机制（B.10）：坏 $\lambda$ 必在 $\operatorname{spec}\Lambda$ 内

由 $Q=D(\lambda)H$ 与 $D$ 的可逆性（$\lambda\notin\operatorname{spec}\Lambda$ 时）立得
$(5b)$ 只需在 $\operatorname{spec}\Lambda$ 上检查（见 [proof/eigenvalue_confinement](../eigenvalue_confinement/README.md)）。
三个反例候选的核对：坏 $\lambda$ 全部落在 $\operatorname{spec}\Lambda$ 里；其中一个候选的坏根是**复根**
（$\lambda^2-5\lambda+7$），说明"只扫有理 $\lambda$"会漏。

## 意义

* **T 是错的**：$q_0$ 阶的失败**不**总能由零指标障碍（B.9）解释；存在独立的"有限初等因子型"障碍
  （Type III）；
* 这回答了专家 2026-11-03 §Q1/§Q6 的问题：他建议的**定向搜索**（结构化 $A$：重复特征值/Jordan 块、
  $p\ge3$）立刻给出反例——我们此前 175 个"无反例"样本只是**实例族太窄**（无 Jordan 结构、$p\le2$）；
* 因此"$q_{\min}>q_0$ 由 $h\ge q_0+r_1$ 刻画"是**错的**，最小阶的判定必须包含真正的谱分析。

## 为什么之前的 175 个样本没发现

先前的实例全部来自随机/稀疏 $A$（或有理稀疏小整数），**没有重复特征值与 Jordan 块**，
且 $p\le2$。专家在 §Q6 明确指出应当用结构化 $A$ 与 $p\ge3$——按此执行后第一次扫描即命中。

## 复现

```bash
python proof/refuted/verify_C4_type3.py
```

预期输出包含：`✓ 猜想 T 被推翻：q0 阶存在 h<q0+r1 但 d_fin>0 的增广（Type III）`。

## 该实例在 $q_0$ 阶**整族不可行**（已证）

**命题**：该实例在 $q_0=3$ 阶，**每个** $(5a)$-可行增广都失败 $(5b)$。

*证明*。两步。

1. **$(5a)$ 自动**：$s_0=\dim(\operatorname{row}[C;L_0]+\operatorname{row}[C;CA])=5$、$t=q_0-r=1$，由 B.11
   $h=s_0+t=6=n$，故 $\mathcal Z^{\perp}+W=\mathbb C^6$，$(5a)$ 对任意 $\mathcal Z$ 成立。
2. **每个 $\mathcal Z$ 都有掉秩 $\lambda$**：设 $V=\ker[C;CA]$（$\dim2$）。对 $x\in V$ 且 $L_0x\ne0$，令
   $\lambda(x)=L_0Ax/L_0x$、$z(x)=(\lambda(x)I-A)x$。则 $Cz(x)=0$、$L_0z(x)=0$，故
   $z(x)\in\ker[C;L_0]$；取 $\mathcal Z=\operatorname{span}z(x)$，则
   $(\lambda I-A)x=z(x)\in\mathcal Z\subseteq\ker\mathcal L$，于是
   $[\lambda\mathcal L-\mathcal LA;CA;C]\,x=0$（$x\ne0$），即 $\operatorname{rank}Q_{\mathcal L}(\lambda)<h$。
   映射 $x\mapsto\operatorname{span}z(x)$（$\mathbb P(V)\to\mathbb P(\ker[C;L_0])$）**非常数**
   （$t=0$ 与 $t=-2$ 的像分别为 $[12/5:0]$ 与 $[4:-4]$），故作为 $\mathbb P^1\to\mathbb P^1$ 的有理映射满射，
   每个 $\mathcal Z$ 都被某个 $x$ 命中。$\square$

*等级*：**[条件性-纸面]** + **[精确验证]**（[verify_C4_whole_family.py](verify_C4_whole_family.py)：
$h=6=n$、15/15 条直线 $(5a)$ 成立、映射 5 个不同像、单个 $\mathcal Z$ 上 $\operatorname{rank}Q(\lambda)=5<6$）。

> **2026-11-04 专家审阅：本几何论证有两处缺口，故降级为"条件性"**（定理本身仍成立，见下）。
>
> 1. **比例性**：$\lambda(x)=L_0Ax/L_0x$ 是 $\mathbb C^2$ 中**向量**的比，需先证
>    $L_0Ax\in\operatorname{span}\{L_0x\}$。这不是 $x\in\ker[C;CA]$ 的推论，而是本实例的特殊性质；
>    它另有独立证明（$2\times2$ 行列式在 $V$ 上恒零，由基与基和的极化恒等式，见
>    [docs/08](../../docs/08_results.md) §4.3）。该步成立，但本文 Step 2 未引用。
> 2. **定义域**：$L_0x\ne0$ 未必在整个 $\mathbb P(V)$ 上成立——实测 $L_0|_V$ 的秩为 **1**（$\dim V=2$），
>    故存在非零 $x_0\in V$ 使 $L_0x_0=0$，该点公式无定义。于是 $\mathbb P^1$ 的完备性**不能**直接使用
>    （开子集上的映射可以不满射，专家给出的反例：$\mathbb A^1\hookrightarrow\mathbb P^1$ 的像不闭）。
>    补完需显式延拓并证明"每个目标直线都有**原定义域内**的原像"，或直接核验可能被漏掉的那条目标直线。
>
> **补救与现状**：定理由**三套代数证明**独立支撑（逐图卡符号 gcd、Bézout 左零空间、$\theta$ 上的行列式消元），
> 它们覆盖全部 $\mathcal Z$，逻辑上不需要几何论证；故本节几何部分只作为**独立性检查**保留，
> 修补前**不**作为证明引用。待补：被漏掉的目标直线（$x_0$ 的极限像）的定性。

## 第二种证明：逐图卡符号 gcd（不依赖射影论证）

对 $P_{\mathcal Z}(\lambda)=[(\lambda I-A)V\,|\,Z(\theta)]$ 的极大子式，在 $\mathbb Q(\theta)[\lambda]$ 中求 gcd：

| 图卡 | $\deg_\lambda\gcd$（一般 $\theta$）| 公共因子 | 例外 $\theta$ | 例外点上的 $\deg$ |
|---|---|---|---|---|
| $(0)$ | **2** | $\dfrac{4\lambda^2\theta-5\lambda^2-20\lambda\theta+22\lambda+28\theta-17}{4\theta-5}$ | $5/4$ | **1**（$\lambda-6$）|
| $(1)$ | **2** | $\dfrac{5\lambda^2\theta-4\lambda^2-22\lambda\theta+20\lambda+17\theta-28}{5\theta-4}$ | $4/5$ | **1**（$\lambda-6$）|

⟹ 两个图卡在**所有** $\theta$ 上都有 $\deg\ge1$（一般点 2、例外点 1）⟹ 每个可行增广都失败 $(5b)$。
工具：[chart_gcd_analysis.py](../../tools/verification/chart_gcd_analysis.py)；记录：
[workspace/q1_false/feasibility_geometry/attempts/41_symbolic_chart_gcd.md](../../workspace/q1_false/feasibility_geometry/attempts/41_symbolic_chart_gcd.md)。

## 该实例的阶差：$q_{\min}=4$（阶差 1）——**含显式 $q=4$ 见证**

> **2026-11-04 专家要求补上见证**（否则只证了 $q_{\min}>3$、没证 $\le4$）。以下是显式的 4 行见证
> （$\mathcal L=[L_0;R]$，$R$ 为随机有理行），通过七条一致性检查：

$$\mathcal L=\begin{pmatrix}
0&0&8&20&1&4\\
1&3&0&0&0&0\\
-1&-2&0&2&-3&-3\\
3&1&-3&-1&1&-3
\end{pmatrix}$$

检查结果：$\operatorname{rank}[C;\mathcal L]=6=p+q$ ✓、$\dim\ker[C;\mathcal L]=0=d$ ✓、$CZ=\mathcal LZ=0$ ✓、
$(5a)=$真 ✓、$h=6=$法秩 ✓、gcd 与 Toeplitz 一致（$(5b)$ **成立**）✓、系数域为有理 ✓。
注意 $h=6<q+r_1=8$：$q=4$ 阶**不是** Type I，这是"非计数型"的可行点，与 $q_0$ 阶的谱障碍形成对照。

## 阶差 = 1 的扫描记录

在同一实例上往上扫：

| 阶 $q$ | 代数可行 | $(5b)$ 成立 | $h$ | $q+r_1$ |
|---|---|---|---|---|
| 3（$=q_0$）| 194 | **0** | $6=n$ | 7 |
| 4 | 400 | **400** | 6 | 8 |

（$q=4$ 时 $d=0$，改由直接构造补得到 $400$ 个候选。）

⟹ 该实例 $q_{\min}=4$，且 $q_0$ 阶的失败是**谱障碍**（Type III，$\delta=1$）。

## 相关

- [B.9](../left_index_count/README.md)（零指标障碍，仍成立；只是**不**是唯一的障碍）
- [attempts/08](../../workspace/q1_false/feasibility_geometry/attempts/08_failure_types.md)（提出 T 的那一轮）
- [attempts/09](../../workspace/q1_false/feasibility_geometry/attempts/09_T_proof_attempt.md)（T 的证明尝试，随之作废为历史）
- [tools/verification/type3_structured.py](../../tools/verification/type3_structured.py)（定向搜索）

**覆盖完备性（回应专家 2026-11-04 §8.1 的 Risk 1）**：我们用 $\binom{k}{d}$ 个**标准坐标图卡**
（每个由"取定 $d$ 个坐标 $S$、其余 $k-d$ 个坐标为参数 $\theta$"给出）参数化 $\operatorname{Gr}(d,K)$。
这些图卡的并**覆盖整个** $\operatorname{Gr}(d,K)$（对任何 $d$ 维子空间都存在一个 $d$ 元坐标集 $S$，
使其到 $S$ 的投影是同构），因此本文件的符号计算（在 $\mathbb Q(\theta)[\lambda]$ 上，**不**采样）
覆盖了**全部**可容许 $\mathcal Z$——不是"网格搜索"。再用 $(5a)$ 的可容许性约束取子集，结论不变。

**符号验证的假设与例外（回应专家 2026-11-04 §6.2 的六点要求）**

1. **图卡为何覆盖整个可容许 Grassmannian**：我们对每个 $d$ 元坐标集 $S\subseteq\{1,\dots,k\}$ 取标准图卡
   $\{\mathcal Z:\text{到 }S\text{ 的投影是同构}\}$；这些图卡之并是整个 $\operatorname{Gr}(d,K)$，再与 $(5a)$ 可容许性取交。
2. **图卡参数化**：$\mathcal Z=K\!\cdot\!W$，$W=[I_d\mid\Theta]$（$S$ 处为单位块，其余 $d(k-d)$ 个位置为参数
   $\theta$）。$W$ 恒满秩 $d$（单位块保证），故图卡内每一点都对应一个 $d$ 维子空间。
3. **分母与排除轨迹**：$W$ 的元素只有 $1$ 与 $\theta$，**没有分母**；因此不存在"分母为零"的例外轨迹。
4. **gcd 与换卡不变**：极大子式 gcd 是铅笔的固有量（相差单位），与图卡选取无关；故逐卡计算再并起来是合法的。
5. **$\mathbb Q(\theta)$ 上的恒等式与例外参数**：
   * 本实例的 gcd 恰为 $\lambda+2$——**首一、与 $\theta$ 无关**，故它对**每个** $\theta$（含特殊值）都给出同一个公共根
     $\lambda=-2$，**没有**"specialization 改变结论"的例外；
   * 另一实例（$q_0=3$）的一般 gcd 次数为 $2$，其完整论证由三套代数证明之一给出：$\theta$-only 的
     Gröbner 消元得到基 $[1]$（空集证书），该论证不依赖"一般 $\theta$"。
6. **例外参数的处理**：见第 5 条——本文件的两个整族结论都不依赖"除有限个 $\theta$ 外"这种弱形式。

**有限域/数值**：全部计算在 $\mathbb Q$ 上精确进行（有理数 + 单变量多项式 gcd），无浮点、无采样 $\lambda$。
