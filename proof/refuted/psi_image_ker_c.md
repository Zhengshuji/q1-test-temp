# 撤回：猜想 $\operatorname{im}\psi=\ker c$ 为假（专家反例，已核验）

## 被撤回的猜想

> 对 $p=r=1$、$(c,A)$ 与 $(\ell,A)$ 均可观测，有 $\operatorname{im}\psi=\ker c$，其中
> $\psi(x,\lambda)=(\lambda I-A)x$、$x\in V=\ker[c;cA]$。

## 专家反例（2026-11-05）

$$A=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix},\qquad c=\begin{pmatrix}1&0&0\end{pmatrix},\qquad
\ell=\begin{pmatrix}0&1&0\end{pmatrix}.$$

核验（本项目用精确算术复算，全部一致）：

| 检查 | 结果 |
|---|---|
| $(c,A)$ 可观测 | ✓（$\mathcal O = I_3$）|
| $(\ell,A)$ 可观测 | ✓ |
| $\operatorname{rank}[c;\ell]$ | $2$ ✓ |
| $V=\ker[c;cA]$ | $\operatorname{span}\{e_3\}$ |
| $K=\ker[c;\ell]$ | $\operatorname{span}\{e_3\}$ |
| $\ker c$ | $\operatorname{span}\{e_2,e_3\}$ |
| $Ae_3$ | $e_2$ |
| $\operatorname{im}\psi$ | $\{0\}\cup\{ae_2+be_3: a\ne0\}$ |
| $e_3\in\operatorname{im}\psi$ | **否**（精确判据：极大子式 gcd 次数 0）|

故 $\operatorname{im}\psi\ne\ker c$：$\operatorname{im}\psi$ 是 $\ker c$ 中的**稠密真子集**（还缺 $e_3$ 方向）。

## 我的错误（两处）

1. **维数界写错**：我写 $\dim\operatorname{im}\psi\le n-2$，实际是 $\le(n-2)+1=n-1=\dim\ker c$
   （定义域是 $V\times\mathbb C$）。这个错误正好掩盖了"像可能填满也可能不填满"的问题。
2. **把"稠密"当成"相等"**：数值上 534/534 个随机 $w$ 都是成员，但随机采样落在**稠密子集**上，
   永远看不到被排除的方向（本项目的第 12 条纪律：薄集/稠密真子集不能靠采样发现）。

## 该实例的 $q_{\min}$（顺带核验）

* $q=1$（$d=1$）：唯一候选 $\mathcal L=\ell$，$\operatorname{rank}[C;\mathcal L]=2\ne 3$，$(5a)$ **失败** ⟹ 该阶不可行；
* $q=2=n-1$（$d=0$）：$\mathcal L=[\ell;e_1]$ 与 $[\ell;e_1+e_2+e_3]$ 都满足 $(5a)$ 与 $(5b)$ ⟹ **可行**。

故该实例仍有 $q_{\min}=2=n-1$ ✓（反例只推翻"像=ker c"这个引理，不推翻本实例的 $q_{\min}$）。

## 改正后的目标（采纳专家 §7 的建议）

$$w\in\operatorname{im}\psi\ \text{的精确刻画（见 docs/02 B.18d）},\qquad
\text{并以}\ \mathbb P(K)\setminus\mathbb P(K\cap V)\subseteq\mathbb P(\operatorname{im}\psi)\ \text{作为 }d=1\ \text{的整族条件}.$$

（原写法 "$K\setminus\{0\}\subseteq\operatorname{im}\psi$" 过强：$S=0$ 才排除 $V$ 内的方向，且 $(5a)$ 必须另行处理。）

## 等级

反例：**[精确验证]**（有理算术，逐项核验上表）。
