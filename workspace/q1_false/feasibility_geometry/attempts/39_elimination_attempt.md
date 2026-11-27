# §8.1 的正面进攻：消元器、单参数完整判定，以及一个未解决的 bug

> ## 2026-11-03 更正（重要）
>
> 本文原先声称"发现真 bug：`L_from_Z`/`ker_cols` 在退化点给出与给定 $\mathcal Z$ 不一致的 $\mathcal L$"——
> **该说法错误**。重新逐点检查后确认：`ker_cols` 与 `L_from_Z` 都正确（$\operatorname{rank}[C;\mathcal L]=4$、
> $\dim\ker[C;\mathcal L]=1$、$Z^\perp=\operatorname{row}[C;\mathcal L]$ 全部相符）。
>
> 真正的 bug 在**我新写的** `Residual_matrix` 里：$(5a)$ 要求 $xA\in\mathcal Z^{\perp}+W$（**行向量右乘** $A$），
> 列向量形式是 $A^{\mathsf T}v$；我写成了 $Av$。修正后：
>
> | 实例 | 消元判定 | 网格 |
> |---|---|---|
> | seed 3003, $q=3$ | yes | 找到 |
> | seed 3005, $q=3$ | yes | 找到 |
> | seed 3011, $q=3$ | yes | 找到 |
> | seed 3000, $q=2$ | yes（$h=n$）| 找到 |
>
> **4/4 一致**。因此"此前网格计数可能被高估"的担心**不成立**；`attempts/31,37` 的计数不受影响。
> 这正是 CLAUDE §7 规则 2（"秩判据写清行堆叠还是列拼接"）与 §10.1（"矩阵乘法不检查维数"）反复警告的陷阱。
>
> 下文保留原始记录（含错误结论），以保留尸检。



## 目标

按专家 §8.1 的要求（"在图卡上解多项式秩约束，并证明代数集被完全描述"）做**真正的完整判定**，
替代"有理网格"。

## 设想与理由

两条路：

1. **Gröbner/Buchberger**：把 $(5a)$ 写成图卡参数 $\\Theta$ 的多项式方程组，判理想是否为单位理想
   （$\\mathbb C$ 上无解 $\\iff 1\\in I$）。这是通用的完整判定。
2. **单参数图卡**（$d(k-d)=1$）：条件是一元多项式，**存在性可精确判定**且"无解"是证书
   （子式 gcd 为非零常数）。

## 做法

### (A) Buchberger（[elimination.py](../../../../tools/verification/elimination.py)）

自实现：多项式字典表示（有理系数）、lex 序、S-多项式、正规形约化、单位理想检测、预算上限。
$(5a)$ 的方程用 $M(\\Theta)=[(\\mathcal Z^{\\perp})A\\ |\\ \\mathcal Z^{\\perp}\\ |\\ W]$ 的 $(h_0+1)$-子式，
$\\mathcal Z^{\\perp}$ 的基取 $K^{\\perp}$ 的固定基 $+$ $K\\cdot\\begin{pmatrix}-\\Theta^{\\mathsf T}\\\\ I\\end{pmatrix}$。

**结果（限制）**：子式次数 $=h_0+1$（我们的实例 $h_0=4\\!\\sim\\!7$），变量 2–4 个；
纯 Python Buchberger 在这种规模上**爆炸**（实测在公开例子 $q=3$ 上 10 分钟未终止）。
估算：$n=6$ 时 $h_0\\approx6$ ⟹ 7 次子式、60 余个方程、2–4 变量 ⟹ 远超本实现的预算。

### (B) 单参数图卡（[complete_small.py](../../../../tools/verification/complete_small.py)）

$d(k-d)=1$（即 $\\operatorname{Gr}(1,2)=\\mathbb P^1$）时：
$$(5a)\\iff \\operatorname{rank}M(\\theta)=h\\iff\\text{所有 }(h_0+1)\\text{-子式在 }\\theta\\text{ 处为零},$$
每个子式是次数 $\\le h_0+1$ 的一元多项式；插值后求 gcd：**非常数 ⟹ 存在 $\\theta$**，**常值 ⟹ certified 无解**。
（先核验 $h$ 在采样点恒定，否则返回 `unknown`。）

## 进展

| 实例 | $q$ | 图卡 | 消元判定 | 网格 |
|---|---|---|---|---|
| $n=5,p=1,r=2$ seed 3003 | 3 | 全部 | **yes**（某图卡子式 gcd 次数 1）| 找到 |
| seed 3005 | 3 | 全部 | **yes** | 找到 |
| $n=5,p=2,r=1$ seed 3000 | 2 | 全部 | **yes**（$h=n$，$(5a)$ 自动）| 找到 |
| seed 3011 | 3 | 全部 | **no（certified）** | **找到** ← **冲突** |

**冲突定位**：$n=5,p=1,r=2$、seed 3011、$q=3$、$d=1$、$k=2$、$\\theta=0$、$rows=(0,)$ 处
`condA` 为真，但按定义 $\\operatorname{rank}M=5>4=h$，即 $(5a)$ 应当为假。追查发现：
用 `L_from_Z` 由该 $\\mathcal Z$ 构造的 $\\mathcal L$，其**实际** $\\ker[C;\\mathcal L]$ 与给定的 $\\mathcal Z$ 不一致
（`ker_cols` 在该退化情形返回了零向量）。随机普查 110 个 $(Z,\\mathcal L)$ **未复现**该现象，
故这是**特定退化点**（$d=1$、$h$ 在邻域变化）上的缺陷。

## 最终结论

1. **通用完整判定（Buchberger）在本仓库不可行**：系统规模（$h_0+1$ 次子式、数十方程、2–4 变量）
   超出纯 Python 实现的能力；这是"为什么不能"的明确记录（而非放弃）。
2. **单参数图卡的完整判定已实现且可用**：4 个实例中 3 个与网格一致，1 个暴露冲突。
3. **冲突是一个真 bug**：`L_from_Z`/`ker_cols` 在退化点会给出与给定 $\\mathcal Z$ 不一致的 $\\mathcal L$，
   使 `condA` 判据失真。**此前所有基于 `L_from_Z` 的"网格命中"计数都可能是高估**（需重跑）。
4. 因此 §8.1 的目标**未完成**：完成它需要 (i) 一个能处理这些规模的消元后端（CAS），或
   (ii) 修掉退化点 bug 并把单参数方法推广到多参数（沿纤维分解）。

## 放弃原因

通用消元在纯 Python 上不可行（规模已量化）；单参数方法受限于一个未修的退化 bug。

## 残留价值

* 一个可用的 Buchberger 实现（小系统）+ 明确的"不可行规模"证据；
* **单参数图卡的精确判定**（可复用于任何 $d(k-d)=1$ 的情形）；
* 一个**真 bug 的定位**（退化点 $L$ 与 $Z$ 不一致），它直接威胁此前所有网格计数——这比多做几个实验更有价值。

## 相关文件

- [tools/verification/elimination.py](../../../../tools/verification/elimination.py)
- [tools/verification/complete_small.py](../../../../tools/verification/complete_small.py)
- [workspace/for_expert/06_state_corrections_and_assessment-answer.md](../../../for_expert/archive/06_state_corrections_and_assessment-answer.md)（§8.1）
- [tools/verification/decide_with_certificate.py](../../../../tools/verification/decide_with_certificate.py)（证书式结论，上一轮）

## 下一步的具体算法（双参数空集证书，已设计未实现）

对 $\dim\operatorname{Gr}=2$ 的图卡（参数 $\theta_1,\theta_2$）：

1. 采样确定 $h_0$（要求恒定）；子式 $p_i(\theta_1,\theta_2)$ 的次数上界 $s=h_0+1$；
2. **固定 $\theta_1=v$**，对每个子式在 $\theta_2=0,\dots,s$ 上取值并插值，得一元多项式 $p_i(v,\cdot)$；
3. 对每对 $(i,j)$ 用 Sylvester 行列式求 $R_{ij}(v)=\operatorname{Res}_{\theta_2}\bigl(p_i(v,\cdot),p_j(v,\cdot)\bigr)\in\mathbb Q$；
4. 对 $\theta_1$ 插值得 $R_{ij}(\theta_1)$（次数 $\le 2s^2$，故需 $2s^2+1$ 个 $v$ 值）；
5. $g=\gcd_{i<j}R_{ij}$：**非零常数 ⟹ 方程组无解（certified 空集）**；非常数只给候选 $\theta_1$（不证有解）。

代价估算：子式数 $\times\,(2s^2+1)\,\times\,(s+1)$ 次 $s\times s$ 行列式。$s=5$、子式 5 个 ⟹ 约 $1.5\times10^3$ 次 $5\times5$ 行列式，可接受。
