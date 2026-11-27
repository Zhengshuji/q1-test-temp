# 第二个整族 Type III 反例（阶差 2）——完整证书

> **对应 docs 条目**：B.13（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

**结论**：下列 $(A,C,L_0)$（$n=6$、$p=r=2$）满足
$$q_0=2,\qquad q=2\ \text{为 Type I 失败},\qquad q=3\ \text{对每个}\ \mathcal Z\ \text{都失败（Type III）},\qquad q=4\ \text{可行},$$
故 $q_{\min}=4$，阶差 $=2$。

## 0. 数据

$$A=\begin{pmatrix}
2&1&2&-1&2&-1\\
2&-2&1&-2&1&1\\
12&-8&-1&0&1&-1\\
6&-4&-2&2&2&-1\\
-2&1&0&2&1&2\\
1&-1&0&1&0&-1\end{pmatrix},\qquad
C=\begin{pmatrix}0&0&0&1&2&-2\\0&0&-1&1&-2&2\end{pmatrix},\qquad
L_0=\begin{pmatrix}-6&9&8&-11&-2&-28\\7&-8&-4&11&25&20\end{pmatrix}$$

基本量：$(C,A)$ 可观测（$n_0=6$）、$L_0$ 可观测、$\operatorname{rank}[C;L_0]=4=p+r$、$r_1=4$、$q_0=2$、
$V=\ker[C;CA]$ 有 $\dim V=2$、$K=\ker[C;L_0]$ 有 $\dim K=2$、$\dim(V\cap K)=0$。

## 1. 阶 $q=2$（$d=2=k$，$\mathcal Z$ 被强制为 $K$）

此时 $\mathcal Z=K$ 唯一。计算得 $h=\operatorname{rank}[\mathcal L;CA;C]=6$，而 $q+r_1=6$，
故为 **Type I**（$h\ge q+r_1$），由 B.9b 的等价（Type II 为空、$(5b)$ 失败）该阶**不可行**。
（该阶只有一个候选，无需符号论证。）

## 2. 阶 $q=3$（$d=1<k=2$，正维参数族）

$\mathcal Z=\langle z(\theta)\rangle\subseteq K$，两张图卡（$K$ 的两行分别置 1）、每卡一个自由参数 $\theta$。

**判据（B.13c）**：该阶失败 $\iff\exists x\in V\setminus\mathcal Z$、$\lambda$：$(\lambda I-A)x\in\mathcal Z$。
因 $\dim(V\cap K)=0$，任何 $x\in V\setminus0$ 都自动满足 $x\notin\mathcal Z\subseteq K$。

**符号计算**：令 $M(\theta,\lambda)=(I-P_z)(\lambda I-A)V$（$6\times2$，$P_z$ 为到 $z(\theta)$ 的投影），
则失败 $\iff\operatorname{rank}M\le1\iff$ 全部 15 个 $2\times2$ 子式为零。把子式看成 $\mathbb Q(\theta)[\lambda]$ 的元素：

| 图卡 | 非零子式个数 | $\gcd$ 次数 | 共同根 $r(\theta)$ | 全部子式在 $\lambda=r(\theta)$ 处恒零 | 首项系数 |
|---|---|---|---|---|---|
| $(0)$ | 14 | **1** | $\boldsymbol{-2}$（与 $\theta$ 无关）| **是** | 1 |
| $(1)$ | 14 | **1** | $\boldsymbol{-2}$（与 $\theta$ 无关）| **是** | 1 |

因 $\gcd=\lambda+2$（首一、与 $\theta$ 无关）整除全部子式，**对每个** $\theta$（有理或无理）都有
$\operatorname{rank}M(\theta,-2)\le1$，于是存在 $x\in V\setminus0$ 使 $(-2I-A)x\in\langle z(\theta)\rangle$，
即掉秩发生在 $\lambda=-2$。**跌落 locus 为空** ⟹ 该阶对每个 $\mathcal Z$ 都失败，且是 Type III
（$h=6<q+r_1=7$，见下）。

## 3. 阶 $q=4$（$d=0$，$\mathcal Z=0$ 强制）

显式见证（$[L_0;R]$，$R$ 为后两行）：

$$R=\begin{pmatrix}0&1&4&-4&3&-1\\-4&-2&-3&1&3&-1\end{pmatrix}$$

七条一致性检查全部通过：$\operatorname{rank}[C;\mathcal L]=6$、$\dim\ker[C;\mathcal L]=0=d$、
$C\mathcal Z=\mathcal L\mathcal Z=0$、$(5a)$ 成立、$h=6$ 等于法秩、$\gcd$ 与 Toeplitz 一致（$(5b)$ 成立）、
系数为有理数。注：$h=6<q+r_1=8$，故该可行点**不是**计数型。

## 4. 复现

```
python -u tools/verification/drop_locus_new_instance.py   # 第 1-2 节：符号 gcd、r(θ)=−2、逐 θ 核验
python -u tools/verification/reverse_construct.py         # 该实例的构造来源（86/86 个实例同类现象）
```

## 5. 与第一个实例（$n=6,p=r=2$、$q_0=3$、阶差 1）的关系

| | 第一个（C4）| 本文（新）|
|---|---|---|
| $q_0$ | 3 | 2 |
| 失败类型 | $q_0$ 阶纯 Type III | $q_0$ 阶 **Type I**，$q_0+1$ 阶 Type III |
| 阶差 | 1 | **2** |
| 整族证明 | 逐图卡符号 gcd（一般次数 2，跌落 locus 空）| 符号 gcd 次数 1、共同根**常数** $\lambda=-2$、跌落 locus 空 |
| 构造性 | 搜索得到 | **反向构造**，86/86 个实例同类 |

后者在两点上更强：阶差更大；两种失败机制在同一实例上相继出现。

## 6. 等级

* $q=2$：**[已证-纸面]**（唯一的 $\mathcal Z$，精确算术）+ **[精确验证]**；
* $q=3$：**[已证-纸面]**（B.13c + 符号 gcd 整除性，$\gcd=\lambda+2$、首项系数 1 ⟹ 对一切 $\theta$ 成立）
  + **[精确验证]**（$\theta=-8..8$ 两卡共 34 个候选，无一可行）；
* $q=4$：**[精确验证]**（显式见证 + 七条检查）。

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
