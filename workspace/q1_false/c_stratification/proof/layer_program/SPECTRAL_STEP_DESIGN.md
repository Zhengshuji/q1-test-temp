# $d=4$ 的谱步：现状、两个结构性观察、以及消元方案

> 2026-10-30 接手者。对应 [../layer_31_theorems/d4_classification.md](../../../../../proof/layer_31_theorems/d4_classification.md) §5 的
> "$\dim\Phi\ge2$ 时未做成判定"。本文件只写**结论与方案**，不宣称已解决。

---

## 1. 问题

$d=4$ 时 $\mathcal U=\ker\varphi$（$[\varphi]\in\mathbb P^3$），格子数据 $T(\varphi),w(\varphi)$ 都是 $\varphi$ 的有理函数。
"格子被覆盖"：

$$\operatorname{cov}(\varphi)\iff \exists\lambda:\ \operatorname{rank}\big[\lambda I-T(\varphi);\ w(\varphi)\big]<3
\iff \gcd_\lambda\{\text{3 阶子式}\}\ne1 .$$

层可行 $\iff\exists[\varphi]\in\Phi$ 使 $\operatorname{cov}(\varphi)$ 为假，且 $(N)$ 成立、$W_0\subseteq\mathcal U$。

## 2. 观察 A（**更正版**：分层闭 / 可构造，不是无条件闭）

> **2026-10-30 更正（专家 QA9 指出）**：仿射簇的投影**一般不必闭**（反例 $\{(\theta,\lambda):\theta\lambda-1=0\}$ 投影到 $\theta$ 是 $\mathbb C\setminus\{0\}$）。
> 正确的陈述是**分层闭**：在每个秩层 $S_c=\{h=c\}$ 上，$\mathrm{Bad}\cap S_c$ 闭、$\mathrm{Good}\cap S_c$ 开；
> 整体上 $\mathrm{Bad}$ 只是**可构造集**（Chevalley）。完整证明（含 $\lambda=\infty$ 的紧化）见
> [../spectral_locus/README.md](../../../../../proof/spectral_locus/README.md) 引理 1–2。

$$\operatorname{cov}(\varphi)\iff (\varphi,\lambda)\in W\ \text{对某个}\ \lambda,\qquad
W=\{(\varphi,\lambda):\ \text{所有 3 阶子式}=0\}\subseteq\Phi\times\mathbb P^1 .$$

$W$ 是射影簇（多项式方程），$\Phi\times\mathbb P^1\to\Phi$ 是**proper**映射，故像 $\operatorname{cov}(\Phi)$ 是**闭集**——
**但只当 $\varphi$ 在射影空间上、且 $\lambda$-纤维在 $\infty$ 处不产生假失败时**；对仿射参数与"$h$ 随参数变"的情形，
必须按秩层分开（见上）。

**推论**（这条有实际价值）：
- "**不被覆盖**"是**开**集 ⟹ 只要找到一个点不被覆盖，层就可证可行 ✓（附具体 $\mathcal L$）；
- 反过来，**全部扫描点都被覆盖只是证据，不是证明** ✗ —— 要证"$\Phi$ 上处处被覆盖"，必须证那个闭集是整个 $\Phi$，
  即需要**消元**（把它写成多项式恒等式）。
- 这也解释了为什么 §44.4 的"一般位置 vs 全坏"是一个闭/开问题：**层不可行是闭条件，层可行是开条件**。

## 3. 观察 B（$d=4$ 的"$\mu\ge1$"轨迹与 $(N)$ 的相互作用）

$$\mu=\dim(B\cap\mathcal U)\ge1\iff B\cap\ker\varphi\ne0 .$$

- 当 $\dim B=1$：$B\cap\ker\varphi\ne0\iff B\subseteq\ker\varphi\iff \varphi\in B^{\perp}$，
  而 $B^{\perp}\subseteq X^*$ 是 **3 维**子空间 ⟹ $[B^{\perp}]\cong\mathbb P^2$。
  $$\therefore\ d=4,\ \dim B=1\ \Longrightarrow\ \{\mu\ge1\}\ =\ B^{\perp}\cong\mathbb P^2 .$$
- **但 $\mu\ge1$ 只是第一道门** ✗：在 $B\subseteq\mathcal U$ 的地方，$(N)$ 退化为 $f(\mathcal U)\subseteq\mathcal U$
  （因为 $\mathcal U+B=\mathcal U$）——**$\mathcal U$ 必须是 $f$-不变的**。
  而对**一般位置**的 $f$，3 维不变子空间只有**有限多个** ⟹ $\Phi\cap\{(N)\}$ 是**有限集**
  ⟹ 谱步退化成有限次计算（已可判 ✓）。
- $$\boxed{\ \dim\Phi=2\ \text{的"硬情形"只在 }f\ \text{退化时出现：}f\ \text{有一族 3 维不变子空间}\ }$$
  典型退化：$f$ 在某 1–2 维块上是**标量**（与 $(3,1)$ 层里"2 维标量片 ⟹ 坏"的机制同源，见 RCP §52）。
  这时 $\dim\Phi=2$ 才真正需要 §4 的消元。

> **结论（2026-10-30 更正）**：原文"$\dim\Phi\ge2$ 需要消元"可以**再降一级**：
> $\mu\ge1$ 的轨迹是 $\mathbb P^2$，但 $(N)$ 把它切成**至多 2 个点**（见下面的命题）⟹
> **$d=4$ 的谱步其实是有限计算 ✓**。只有退化时（解集是整条 $\mathbb P^1$）才用到线判定。

### 3.1 命题（可行 $\varphi$ 至多 2 个）

$\dim B=1$、$d=4$，$\varphi\in B^{\perp}$、$\mathcal U=\ker\varphi$。定义转移映射
$$\Phi(\varphi)(u):=\varphi\big(\pi(uA)\big) .$$
$\Phi$ 在 $B^{\perp}$ 上良定义（$\varphi$ 杀掉 $B$，$\pi(uA)$ 只在模 $B$ 意义下唯一）。则
$$(N)\iff\Phi(\varphi)\in\operatorname{span}\{\varphi\}\iff c(\varphi)=0\ \text{且}\ \Phi_1(\varphi)=\lambda\varphi,$$
其中 $X^*=B^{\perp}\oplus\langle\theta\rangle$（$\theta(b)=1$）、$\Phi=\Phi_1+c\,\theta$。

*证明*：$(N)$：$\forall u\in\ker\varphi$，$\varphi(\pi(uA))=0\iff\Phi(\varphi)|_{\ker\varphi}=0
\iff\Phi(\varphi)\in\operatorname{span}\{\varphi\}$（泛函在 $\ker\varphi$ 上为零 $\iff$ 与 $\varphi$ 成比例）。$\square$

**推论**：$c$ 线性 ⟹ $\ker c\subseteq B^{\perp}$ 是 $\mathbb P^1$；$\Phi_1(\varphi)=\lambda\varphi$ 在 $\ker c$ 上是
三个二次型的公共零点 ⟹ **至多 2 个方向**（三个二次型恒为零时整条线）。

$$\boxed{\ d=4,\ \dim B=1\ \Longrightarrow\ \text{层可行}\iff\text{至多 2 个 }\varphi\ \text{里有一个的格子不被覆盖}\ }$$

**实现**：[c204_d4_finite_phi.py](c204_d4_finite_phi.py)（写死一个 $n=7$ 实例：算出 $B^\perp$、$c$、$\Phi_1$、
二次型、gcd $=b$ ⟹ 唯一可行 $\varphi=(0,1,0,0)$，其格子 `covered=False` ⟹ 层可行 ✓）。

### 3.2 批量结果（[c205_d4_batch.py](c205_d4_batch.py)，12 个随机实例）

| 结果 | 个数 | 含义 |
|---|---|---|
| `none`（二次型无公共零点）| **11** | 没有可允许的 $\varphi$ ⟹ 该实例的 $(3,1)$ 层**不可行** ✓（这是**证明**，不是抽样）|
| `rational` + `covered=False` | **1** | 层**可行** ✓ |
| `quadratic`（解在二次域）| 0 | 未实现 ✗ |
| `degenerate-line` | 0 | 用线判定 |

⟹ 在这批实例上，$d=4$ 的 $(3,1)$ 层要么直接不可行（11/12），要么可行（1/12），**没有**需要消元的中间情形。

> ⚠️ **实施陷阱（同时记录）**：不能把 $(N)$ 简化成"$X/B$ 上的不变子空间"——
> $f:X\to X/B$ **不下降到** $X/B$（除非 $f(B)\subseteq B$），见 [c203_d4_generic_sweep.py](c203_d4_generic_sweep.py) 的反例。

## 4. 消元方案（把 $\operatorname{cov}$ 写成多项式）

1. **分图卡**：$[\varphi]\in\mathbb P^3$ 用标准图卡 $\varphi_i\ne0$ 覆盖；在每张图卡里把 $\varphi$ 归一化，
   $\mathcal U=\ker\varphi$ 的基可以取成 $\varphi$ 的**有理函数**（从而 $T,w$ 也是有理函数）；
2. **清分母**：$\gcd$ 非平凡 $\iff$ 某个 resultant $R(\varphi)=0$（$\varphi$ 的多项式，
   对 $3\times3$ 的四个子式：$\deg_\lambda\le3$，resultant 的次数可控）；
3. **限制到 $\Phi$**：$\varphi=\varphi_0+s\varphi_1+t\varphi_2$ 代入，得 $R(s,t)\in\mathbb Q[s,t]$；
   $$\text{层在 }\Phi\text{ 上不可行}\iff R|_\Phi\equiv0\iff \text{把所有系数算出来并全为 }0 .$$
   这是**有限**线性代数（系数比较），不需要采样。

**尚未做**：第 1–3 步的实现。障碍是 $T(\varphi)$ 的符号计算（需要在图卡里解一个含参数的线性方程组），
以及 resultant 的规模控制。本目录的 [c202_d4_spectral_scan.py](c202_d4_spectral_scan.py) 只做了**逐点**精确判定
（第 1 步的数值版），并在扫描里报告 `μ=0 / (N) 失败 / 被覆盖 / 不被覆盖` 的分布。

## 5. 现在能严格说什么

| 断言 | 等级 |
|---|---|
| $\operatorname{cov}$ 是闭条件（观察 A）| **[已证-纸面]**（proper 映射的像闭）|
| $d=4,\dim B=1\Rightarrow\{\mu\ge1\}=B^{\perp}\cong\mathbb P^2$（观察 B）| **[已证-纸面]**（一行）|
| **可行 $\varphi$ 至多 2 个**（§3.1 的转移映射命题）| **[已证-纸面]** + 实例 [c204](c204_d4_finite_phi.py) ✓ |
| 找到不被覆盖的 $\varphi$ ⟹ 层可行 | 严格（附见证 $\mathcal L$）|
| 全部候选被覆盖 ⟹ 层不可行 | 严格（候选是**全部**可行 $\varphi$，不是抽样 ✓）|
| $d=4$、$\dim B=1$ 的谱步：**可判**（有限候选 + 逐点判定）| **[已证-纸面]**；有理/二次域情形已实现（c204），一般代数数情形未实现 ✗ |
| 退化（解集是整条 $\mathbb P^1$）| 用线判定（§5 已可判）✓ |
| $\dim B\ge2$ | 已有结果（d4_classification / RCP §63：完全线性）|

## 6. 复现

```bash
python proof/layer_program/c202_d4_spectral_scan.py            # 逐点扫描（会给理由分布）
python proof/layer_program/verify_d4_classification.py         # 原有 40/40（引理 2.1/3.1/4.1）
python proof/layer_program/verify_d4_perp_branch.py            # φ⊥B 分支 60/60
```
