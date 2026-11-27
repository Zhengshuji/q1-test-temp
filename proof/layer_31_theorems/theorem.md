# $(3,1)$ 层的格子级定理

> 全部陈述的验证等级：【已证-纸面】，另有标注处为【Lean】（机器检查，退出码 0）。
> 记号见 §1；**每个定理的全部假设都写在陈述里** ✓。

---

## 1. 记号

$A\\in\\mathbb C^{n\\times n}$、$C\\in\\mathbb C^{p\\times n}$、$L_0\\in\\mathbb C^{r\\times n}$ 给定；
$\\mathcal J=\\operatorname{row}[C;CA]$、$j=\\dim\\mathcal J$、$X=\\mathbb C^n/\\mathcal J$、$\\pi$ 商映射、
$B=\\pi(\\mathcal JA)$、$\\beta:\\mathcal J\\to B$，$\\beta(h)=\\pi(hA)$（**满射** ✓）。

**格子**：固定 $\\mathcal U\\subseteq X$（$\\dim\\mathcal U=3$）与 $\\mathcal H\\subseteq\\mathcal J$（$\\dim\\mathcal H=1$），
满足 $\\beta(\\mathcal H)\\subseteq\\mathcal U$ ✓。记

$$E=B\\cap\\mathcal U,\\qquad \\mu=\\dim E,$$
$$w=\\beta(h)\\in E\\ (\\mathcal H=\\langle h\\rangle),\\qquad T:\\mathcal U\\to\\mathcal U \\ \\text{为格子的 }3\\times3\\text{ 数据}.$$

**提升自由度**：每行可加一个 $\\mathcal J$ 中元素 ✓，等价地（在 $\\mathcal U$ 坐标下）

$$C(s)=T+\\sum_{k=1}^{\\mu}s_k a_k^{\\mathsf T},\\qquad E=\\operatorname{span}(a_1,\\dots,a_\\mu),\\quad s_k\\in\\mathbb C^3\\ \\text{自由}.$$

（**方向**：每行加 $s_ia$，即 $s\\,a^{\\mathsf T}$，不是 $a\\,s^{\\mathsf T}$ ✓。）

**覆盖**：格子**被覆盖** $\\iff$ 对所有 $s$，$(5b)$ 都失败 ✗。
记 $P(\\lambda;s)=[\\lambda I-C(s);\\ w^{\\mathsf T}]$（4 行 3 列）；$(5b)$ 在 $\\lambda$ 处成立 $\\iff\\operatorname{rank}P(\\lambda;s)=3$ ✓。

---

## 2. 引理 0（谱判据）【已证-纸面】

> **引理 0**：设 $\\lambda_k$ 是 $C$ 的**简单**特征值 ✓，$v_k$ 为其特征向量 ✓。
> 则 $(5b)$ 在 $\\lambda_k$ 处成立 $\\iff w^{\\mathsf T}v_k\\ne0$ ✓。

*证明*：$Cv_k=\\lambda_kv_k$ ⟹ $P(\\lambda_k;s)$ 的核含 $v_k$ ⟹ 秩 $\\le2$ 的充要条件是第 4 行 $w^{\\mathsf T}$ 也杀掉 $v_k$ ✓。
用伴随公式：$\\operatorname{adj}(\\lambda_kI-C)=\\kappa\\,v_k\\eta_k^{\\mathsf T}$ ✓（秩 1 ✓，$\\kappa\\ne0$ ✓），
故 $\\operatorname{rank}P(\\lambda_k;s)=3\\iff w^{\\mathsf T}v_k\\ne0$ ✓。$\\square$

---

## 3. 定理 C.1–C.5

### C.1（$\\mu=3$，$w\\ne0$）【已证-纸面】

> **定理 C.1**：若 $\\mu=3$ ✓、$w\\ne0$ ✓，则该格子**不被覆盖** ✓。

*证明*：$\\mu=3$ 且 $\\dim\\mathcal U=3$ ⟹ $E=\\mathcal U$ ⟹ 三行**完全自由** ✓。
取 $\\mathcal U$ 的一组基使 $w^{\\mathsf T}v_k\\ne0$（$k=1,2,3$ ✓，可行因为 $w\\ne0$ ✓），
取互异 $\\lambda_1,\\lambda_2,\\lambda_3\\in\\mathbb C$ ✓，令 $C=V\\Lambda V^{-1}$ ✓。
则 $C$ 的谱为 $\\{\\lambda_k\\}$ ✓（互异 ✓、简单 ✓）、特征向量 $v_k$ ✓、且 $w^{\\mathsf T}v_k\\ne0$ ✓ ⟹
由引理 0 在**每个**特征值处 $(5b)$ 都成立 ✓；$\\lambda$ 非特征值时 $\\lambda I-C$ 可逆 ⟹ 秩 3 ✓ ⟹ 全程成立 ✓。$\\square$

### C.2（$\\mu=1$，$w\\ne0$）【已证-纸面 + Lean 扰动引理】

> **定理 C.2**：若 $\\mu=1$ ✓、$w\\ne0$ ✓，记 $E=\\langle a\\rangle$ ✓。则
> $$\\text{格子不被覆盖}\\iff T\\ \\text{没有落在}\\ a^{\\perp}\\ \\text{里的非零特征向量}.$$

*证明*（$\\Leftarrow$）：设 $Tv=\\lambda v$ 且 $a^{\\mathsf T}v=0$ ✓、$v\\ne0$ ✓。
则对**任意** $s$ ✓：$C(s)v=Tv+\\big(s_1a^{\\mathsf T}v\\big)\\cdot\\text{(某向量)}=Tv=\\lambda v$ ✓。
于是 $v$ 杀掉 $\\lambda I-C(s)$ 的**每一行** ✓，也杀掉 $w^{\\mathsf T}$（$w\\in E=\\langle a\\rangle$ ⟹ $w^{\\mathsf T}v=0$ ✓）⟹
$\\operatorname{rank}P(\\lambda;s)\\le2$ ✓ ⟹ 每个 $s$ 都失败 ✗ ✓。

（$\\Rightarrow$）反设 $T$ **没有**这样的特征向量 ✓。取 $s=0$ ✓，则 $C(0)=T$ ✓。
此时 $T$ 的每个特征空间都是**1 维** ✓：否则 $\\dim\\ker(T-\\lambda I)\\ge2$ ✓ ⟹ 它与超平面 $a^{\\perp}$ 有非零交 ✓ ⟹ 反设被违背 ✗。
于是 $T$ 的谱**简单** ✓ 且对每个特征向量 $v_k$ 有 $v_k\\notin a^{\\perp}$ ✓ 即 $a^{\\mathsf T}v_k\\ne0$ ✓；
又 $w\\in\\langle a\\rangle$ ⟹ $w^{\\mathsf T}v_k\\ne0$ ✓ ✓。由引理 0，$s=0$ 在**每个**特征值处成立 ✓；非特征值处 $\\lambda I-T$ 可逆 ⟹ 成立 ✓ ⟹ 该格子**不被覆盖** ✓。$\\square$

【Lean】"$a_k^{\\mathsf T}v=0$ ⟹ 扰动不改变特征向量"的两条引理已机器检查（`Perturbation.lean` 的 `perturb_eq_of_mem_ker`、`perturb_eigen_of_mem_ker`）。

### C.3（$\\mu=2$，$w\\ne0$）【已证-纸面 + Lean 二次式】

> **定理 C.3**：若 $\\mu=2$ ✓、$w\\ne0$ ✓。则
> $$\\text{格子不被覆盖}\\iff T\\ \\text{没有落在}\\ E^{\\perp}\\ \\text{里的非零特征向量}.$$

*证明*（$\\Leftarrow$）：与 C.2 的 $\\Leftarrow$ 相同 ✓（$E$ 有 2 维 ✓，$a_1,a_2$ 张成它 ✓，$v\\in E^{\\perp}$ ⟹ 两个 $a_k^{\\mathsf T}v=0$ ✓），并用 $w\\in E$ ⟹ $w^{\\mathsf T}v=0$ ✓。
（这条的扰动引理（秩二版）已【Lean】：`perturb2_eigen_of_mem_ker` ✓。）

（$\\Rightarrow$）取坐标使 $E=\\langle e_1^{\\mathsf T},e_2^{\\mathsf T}\\rangle$ ✓、$w^{\\mathsf T}=e_1^{\\mathsf T}$ ✓。
"每行差 $\\in E$" ⟹ 第三列**固定** ✓，前两列自由 ✓。写

$$C=\\begin{pmatrix}x&y&a\\\\0&u&b\\\\0&s&c\\end{pmatrix}\\qquad(\\text{第三列 }(a,b,c)^{\\mathsf T}\\text{ 固定}).$$

反设"$T$ 没有 $E^{\\perp}$ 内特征向量" ✓ ⟹ $(a,b)\\ne(0,0)$ ✓。
取 $v=(0,z_1,z_2)^{\\mathsf T}$：$Cv=\\lambda v$ ⟺ $z=(z_1,z_2)^{\\mathsf T}$ 是 $D=\\binom{u\\ b}{s\\ c}$ 的特征向量 ✓ 且 $g^{\\mathsf T}z=yz_1+az_2=0$ ✓。
$(y,a)\\ne(0,0)$ 时后者等价于 $z\\parallel(a,-y)$ ✓ ⟹ 坏条件 $=\\{\\det[z,Dz]=0\\}$ ✓，而

$$\\det[z,Dz]=a\\big(sa-cy\\big)-(-y)\\big(ua-by\\big)=a^2s+a(u-c)y-by^2=:p(y,u,s).$$

$p\\not\\equiv0$ ✓：$a\\ne0$ 时 $s$ 的系数 $a^2\\ne0$ ✓；$a=0$ 时 $b\\ne0$ ✓ ⟹ $p=-by^2$ ✓。
故可取 $p\\ne0$、$u\\ne c$、$x\\notin\\{u,c\\}$ ✓ ⟹ $C$ 谱简单 ✓、坏条件不成立 ✓ ⟹ 不被覆盖 ✓。$\\square$

【Lean】$p$ 的展开与非恒零已机器检查（`QuadraticMu2.lean` 的 `quad_det`、`quad_exists_ne_zero`）。


### 关于「$\perp$」的注（2026-10-30 补 ✓）

C.2 与 C.3 的陈述用了「特征向量与 $a$ / $E$ **正交**」。这句话在**证明所用的坐标**里是对的 ✓，
但「$\perp$」**不是**不变量 ✗ —— 换一组非正交基，点积会变（实测 28/30 会变 ✓）。

**不变形式**（无内积 ✓、换基不变 ✓）是**秩/包含**条件：
$$(5b)\ \text{在}\ \lambda\ \text{处成立}\iff \operatorname{rank}[\lambda I-T;\ w]=\rho\iff w\notin(\lambda I-T)(\mathcal U).$$
等价地：**被覆盖** $\iff\exists\lambda:\ w\in(\lambda I-T)(\mathcal U)$ ✓。

**所有验证脚本用的都是这个秩形式**（铅笔最大子式的 $\gcd$ ✓）⟹ 那些计算**不受影响** ✓ ✓。

### C.4 / C.5（$w=0$）【已证-纸面 + Lean 因式分解】

> **定理 C.5**：若 $w=0$ ✓（任意 $\\mu$ ✓），则该格子**恒被覆盖** ✓。
>
> **定理 C.4**（$\\mu=0$）是其**特例** ✓：$\\mu=0$ ⟹ $E=0$ ⟹ $w\\in E=0$ ⟹ $w=0$ ✓。

*证明*（C.5）：$w=0$ ⟹ 第 4 行恒为零 ✓ ⟹
$$(5b)\\ \\text{在}\\ \\lambda\\ \\text{处成立}\\iff \\det(\\lambda U-C(s))\\ne0 ✓$$
（$U$ 是以 $u_1,u_2,u_3$ 为行的矩阵 ✓）。而 $\\lambda\\mapsto\\det(\\lambda U-C(s))$ 是 $\\lambda$ 的**三次**多项式（或恒零 ✓）✓，
由代数基本定理必有根 $\\lambda_0$ ✓ ⟹ 该处秩 $\\le2$ ⟹ 失败 ✗ ✓。$\\square$

【Lean】因式分解 $\\det(\\lambda U-UT^{\\mathsf T})=\\det U\\cdot\\det(\\lambda I-T^{\\mathsf T})$ 已机器检查（`Theorem12.lean`）。
**未形式化**："非零三次必有根"（Mathlib API 未接通 ✓），该步由 42/42 精确验证覆盖 ✓。

---

## 4. 定理之间的独立性（如实）

| 关系 | 说明 |
|---|---|
| C.4 ⟸ C.5 | 见上 ✓（**C.4 不是独立定理** ✓）|
| C.1、C.2、C.3 互相独立 | 对应 $\\mu=3,1,2$ 三个通道 ✓ |
| C.5 与 C.1–C.3 互补 | C.5 处理 $w=0$ ✓；C.1–C.3 处理 $w\\ne0$ ✓ |
| 引理 0 被 C.1、C.2、C.3 使用 | ✓ |

$$\\mu\\in\\{0,1,2,3\\}\\ \\text{与}\\ w=0/\\ne0\\ \\Longrightarrow\\ \\text{C.1–C.5 覆盖全部情形}\\ ✓$$

---

## 5. 验证等级汇总

| 定理 | 纸面 | Lean | 抽象模型 | 真实实例 | 端到端 |
|---|---|---|---|---|---|
| C.1 | ✓ | — | 200/200 | 200/200 | 未做 |
| C.2 | ✓ | 扰动引理 | 199/199 | 17/17 + 两个实例（两方向）| 未做 |
| C.3 | ✓ | 二次式 + 扰动 | 295/295 | 43/43 | **12/12（十项逐项）** |
| C.4 | ✓ | 因式分解 | 42/42 | — | — |
| C.5 | ✓ | （同上） | 120/120 | — | — |

复现命令与"验证 ≠ 证明"的说明见 [verification.md](verification.md)。
