# 429 $k=2,\omega=1$ 的活跃集分类定理：空 / 单点 / 开——**无孤立多点**

> 落实 105 号答复的 Q5（他建议先做 $k=2,\omega=1$，把它作为"全局开性"的第一个非平凡实例）。
> 结论：**这一层不存在"多个孤立活跃点"**，且全局开性在此成立（在非平凡分支上）。
> 关键是他的 (13)：谱正则性化成一个**标量线性多项式族**的 $\gcd$。

## 目标

证明 $k=2$、$\omega=1$ 时活跃集的**完全分类**：
$$\mathcal X_{\mathrm{act}}\in\{\varnothing,\ \text{单点},\ \text{（$d=0$ 时）Zariski 开集}\}.$$

## 设想与理由

由 428 的 Proposition 1，相容轨迹是 $\operatorname{Gr}(\omega-d,k-d)=\operatorname{Gr}(1-d,2-d)$：
- $d=2$：空；
- $d=1$：$\operatorname{Gr}(0,1)=$ **单点**；
- $d=0$：$\operatorname{Gr}(1,2)=\mathbb P^1$（整条）。

所以稠密情形只有 $d=0$。两种情形分别处理。

## 做法

### 记号

$W_z=\operatorname{span}\{(1,z)\}\subset\mathbb C^2$（$z\in\mathbb C$，另加 $z=\infty$ 对应 $\operatorname{span}\{(0,1)\}$）。
若 $h\in W_z$ 则 $h=\alpha(1,z)$，记 $\alpha=\alpha(h)$；同理 $\beta=\beta(g)$。

### 谱条件的显式形式（105 号 (13)）

铅笔
$$P(\lambda)=\begin{pmatrix}\lambda\alpha_1-\beta_1\\ \vdots\\ \lambda\alpha_r-\beta_r\end{pmatrix}(1,z)$$
的秩为 1 对一切 $\lambda$ 成立 $\iff$ 这些**标量线性多项式**没有公共根
$$\iff \gcd_j(\lambda\alpha_j-\beta_j)=1 .$$
而对线性多项式 $\lambda\alpha-\beta$、$\lambda\alpha'-\beta'$：
$$\text{有公共根}\iff \alpha\beta'-\alpha'\beta=0 .$$
于是（零对 $(\alpha,\beta)=(0,0)$ 给出零多项式，对 $\gcd$ 无约束）

$$\boxed{\text{活跃}\iff \dim\operatorname{span}\{(\alpha_j,\beta_j):(\alpha_j,\beta_j)\ne0\}\ \ge\ 2}$$

——即"存在两行，其 $(\alpha,\beta)$ 不成比例"。

### 情形 $d=1$（钉死）

相容轨迹只有一个 $W$，故 $\mathcal X_{\mathrm{act}}\subseteq\{\text{该点}\}$：**至多单点** ✓。

### 情形 $d=0$（整个 $\mathbb P^1$）

此时所有固定对为零，铅笔只由自由行给出。自由行的对 $(\alpha(\tau),\beta(\tau))$ 是纤维参数 $\tau$ 的**线性**函数，
故它们的像是一个子空间
$$F(z)\subseteq\mathbb C^2 .$$
由上面的判据，
$$\mathcal X_{\mathrm{act}}=\{z:\ \dim F(z)\ge2\}\quad(\text{因固定对为零，只剩自由行}) .$$
而 $\dim F(z)\ge2$ 是"某个 $2\times2$ 子式非零"——**Zariski 开条件** ✓。于是
$$\mathcal X_{\mathrm{act}}=\text{开集}\quad(\text{或空}) .$$

（注：$d=0$ 意味着 $L_0[N\ AN]=0$，由 [422](422_trivial_layer.md) 这些实例在 $\omega=0$ 层**恒可行**，
所以它们对归约无用；但它们仍是"全局开性能否被打破"的反例候选，而答案是**不能**。）

## 进展（定理）

> **定理（$\mathbb P^1$ 活跃集分类）.** 设 $k=2$、$\omega=1$。则
> $$\mathcal X_{\mathrm{act}}=\varnothing\quad\text{或}\quad\text{一个点}\quad\text{或（仅当 }d=0\text{）}\mathbb P^1\text{ 的 Zariski 开子集}.$$
> 特别地，**不存在两个或更多孤立活跃点**；在 $d\ne0$ 的分支上活跃集是**闭的**（至多单点），
> 在 $d=0$ 的分支上是**开的**。

**推论**：105 号 Q1 的"全局开性"在 $k=2,\omega=1$ 上成立（非平凡分支上是"至多单点"这一更强结论）；
105 号 Theorem D（分量复杂度）在这一层也**不成立**——没有分量可数。

## 验证

[c376](../../../../tools/verification/c376_p1_classification.py)：对两个实例（$d=1$ 与 $d=0$）在 $z\in\{\infty,0,1,2,-1,\tfrac12,-2\}$ 上，
把**判据**（$\dim\operatorname{span}\{(\alpha,\beta)\}\ge2$）与**直接检验**（在 $T_z$ 内采样、算极大子式 $\gcd$）对照：

| 实例 | $d$ | 相容的 $z$ | 活跃 | 判据与直接检验 |
|---|---|---|---|---|
| d1 | 1 | 仅 $z=0$（唯一 $W$） | 无 | **一致** |
| d0 | 0 | 全部 | 无（空集） | **一致** |

两例中判据与直接检验**无一处不符** ✓。

## 最终结论

1. **$k=2,\omega=1$ 被完全分类**：空 / 单点 / 开；
2. "多活跃点"必须到 $\omega\ge2$ 才可能出现（与 [421](421_omega1_excluded.md) 一致，但现在有完整证明）；
3. 这条定理**不需要算 $\gcd$**——它来自判据的结构（$\alpha\beta'-\alpha'\beta$ 与秩条件），
   比数值扫描强得多（105 号也强调"generic 是代数陈述，须在函数域上判"）。

## 放弃原因

- 没有做 $d=0$ 分支的**实拓扑**分析（105 号提醒：Zariski 开 $\ne$ 实连通）；
- 没有把"开集的具体形状"（哪些 $z$ 让 $\dim F(z)=2$）显式算出来；
- 没有开始 $\operatorname{Gr}(2,3)$（下一步）。

## 残留价值

- **一条完整分类定理**（可写进下一步报告）；
- 明确"孤立多点只可能在 $\omega\ge2$"，从而把问题**干净地**推到下一层；
- 展示了 105 号 (13) 的用法：谱条件在这一层退化成**标量**条件，容易完全分类。

## 下一步

$\operatorname{Gr}(2,3)$（$\omega=2$、$k=3$）：按 105 号 §27 的配方——
$W_q=\ker q^{\mathsf T}$、$\mathcal T_{W_q}=\ker\left(\begin{bmatrix}q^{\mathsf T}&0\\0&q^{\mathsf T}\end{bmatrix}\big|_{\mathcal S}\right)$，
在常秩层上用结式消去 $\lambda$，得到 $q$ 的多项式条件，再看它的实拓扑。

## 相关文件

- [428](../../decision_algorithms/attempts/428_expert105_audit.md)（105 号裁决与 Proposition 1）
- [421](421_omega1_excluded.md)（$\omega=1$ 钉死，本定理的特例）
- [422](422_trivial_layer.md)（$d=0$ 的平凡性）
- [417](../../decision_algorithms/attempts/417_expert104_audit.md)（三判据）

## 状态

- 分类定理：**[已证-纸面]**（证明用 428 的 Proposition 1 + 105 号的 (13)）。
- $d=0$ 的开集形状：**[未算]**。
- $\operatorname{Gr}(2,3)$：**[未做]**。
