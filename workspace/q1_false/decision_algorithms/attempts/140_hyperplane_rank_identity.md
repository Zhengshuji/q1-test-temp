# 双曲秩恒等式：$\ker[P;Q]\cong\ker[v,Av]$（纸面证明 + Lean 计划）

> 2026-11-08。Step 6 优先级 5 的收尾：专家 121 的恒等式
> $$\operatorname{rank}\begin{bmatrix}P\\Q\end{bmatrix}=\delta-2+\operatorname{rank}[v,Av]$$
> 的核等价证明。状态：**M2（纸面）**；Lean 形式化列为下一步。

## 目标

设 $W=\mathbb C^k$、$X=\mathbb C^n$、$U=\mathbb C^\delta$，$N:W\to X$ 单射、$A:X\to X$、
$Z_1,Z_2:U\to W$，$T:W\times W\to X$、$T(v,w)=Nv+ANw$。假设
$$\ker T=\operatorname{im}\begin{bmatrix}Z_1\\Z_2\end{bmatrix},\qquad
N Z_1+A N Z_2=0,\qquad Z_2\ \text{单射}.$$
设 $\sigma\in W\setminus\{0\}$、$v=N\sigma\ne0$，$q:W\to W/\operatorname{span}v$ 为商映射，
$P=qZ_1$、$Q=qZ_2$。证明
$$\ker\begin{bmatrix}P\\Q\end{bmatrix}\cong\ker[v,Av],$$
从而 $\operatorname{rank}[P;Q]=\delta-2+\operatorname{rank}[v,Av]$。

## 设想与理由

* $P u=0\iff Z_1u\in\operatorname{span}v$；$Q u=0\iff Z_2u\in\operatorname{span}v$。
* 对 $u\in\ker[P;Q]$，写 $Z_1u=a\sigma$、$Z_2u=b\sigma$（$a,b$ 唯一，$\sigma\ne0$）。
* 关系 $NZ_1+ANZ_2=0$ 给出 $a v+b Av=0$，即 $(a,b)\in\ker[v,Av]$。
* 反过来，$(a,b)\in\ker[v,Av]$ 给 $(a v,b v)\in\ker T=\operatorname{im}[Z_1;Z_2]$，故存在 $u$。
* $Z_2$ 单射保证 $\psi$ 单射。

## 做法

**引理 1（$\psi$ 良定义且线性）**：对 $u\in\ker[P;Q]$，存在唯一的 $(a,b)\in\mathbb C^2$ 使
$Z_1u=a v$、$Z_2u=b v$。映射 $\psi(u)=(a,b)$ 是线性的：
$$Z_1(u+u')=(a+a')v,\quad Z_2(u+u')=(b+b')v,$$
标量同理；唯一性由 $v\ne0$。

**引理 2（$\psi$ 落到 $\ker[v,Av]$）**：由 $NZ_1u+ANZ_2u=0$，
$$0=N(a\sigma)+A N(b\sigma)=a\,N\sigma+b\,A N\sigma=a v+b Av,\qquad v=N\sigma.$$
（$N$ 线性、$Nv=v$。）故 $[v,Av]\,(a,b)=0$。

**引理 3（$\psi$ 单射）**：若 $\psi(u)=(0,0)$，则 $Z_1u=Z_2u=0$；由 $Z_2$ 单射得 $u=0$。

**引理 4（$\psi$ 满射）**：设 $(a,b)\in\ker[v,Av]$，即 $a v+b Av=0$。则
$$T(a\sigma,b\sigma)=N(a\sigma)+A N(b\sigma)=a v+b Av=0,$$
故 $(a\sigma,b\sigma)\in\ker T=\operatorname{im}[Z_1;Z_2]$，存在 $u$ 使 $Z_1u=a\sigma$、$Z_2u=b\sigma$；
于是 $u\in\ker[P;Q]$ 且 $\psi(u)=(a,b)$。

**定理**：$\psi$ 是线性同构 $\ker[P;Q]\cong\ker[v,Av]$。于是
$$\dim\ker[P;Q]=\dim\ker[v,Av]=2-\operatorname{rank}[v,Av],$$
$$\operatorname{rank}[P;Q]=\delta-\dim\ker[P;Q]=\delta-2+\operatorname{rank}[v,Av].$$

## 进展

* 核等价的四步证明已完成（纸面）。
* 秩恒等式由秩-零化度得出。
* 与 121 的 $\operatorname{rank}Q$ 公式一致：$P$ 的加入使 $\delta-2$ 出现。

## 最终结论

* $\ker[P;Q]\cong\ker[v,Av]$，故 $\operatorname{rank}[P;Q]=\delta-2+\operatorname{rank}[v,Av]$。
* 这是 $c=1$ 定理的代数核心（121 的秩恒等式）。

## 放弃原因

* Lean 形式化未做：需要显式构造 $\psi$（用 $\operatorname{span}v\cong\mathbb C$ 的等价），
  以及 $\ker T=\operatorname{im}[Z_1;Z_2]$ 的假设接口。
* 未给 $\operatorname{rank}Q$ 与 $\operatorname{rank}[P;Q]$ 的联合分层表（112 有实例表）。

## 残留价值

* 完整的纸面证明，可直接用于论文与 Lean 化。
* 明确了 Lean 化的三个部件：$e:\operatorname{span}v\simeq\mathbb C$、$\psi$ 的线性性、满射用 $\ker T$ 假设。

## 相关文件

* [attempts/121](../../c_stratification/attempts/121_hyperplane_vector_bundle.md)（秩恒等式）
* [attempts/122](../../c_stratification/attempts/122_invariant_eigenspace_obstruction.md)（Lean 内核 1）
* [RankQFormula](../../../../trash/lean_removed_2026-11-19/augmentation_lean/RankQFormula.md)（Lean $\operatorname{rank}Q$）
* [Splitting](../../../../trash/lean_removed_2026-11-19/augmentation_lean/Splitting.md)（Lean 分裂）

## 更正（2026-11-08）

* 系数是 $Z_1u=a\sigma$、$Z_2u=b\sigma$（$\sigma\in W$），不是 $Z_1u=av$（$v\in X$）；
  关系是 $N(a\sigma)+A N(b\sigma)=a v+b A v$（$v=N\sigma$）。此前正文有类型错写，已改。
* Lean 化的阻塞点：需要 $e:\operatorname{span}\{\sigma\}\simeq\mathbb C$ 与 $\psi$ 的线性性；
  系数唯一性引理 `coeff_unique` 正在调试（`mem_span_singleton` 的方向与 `sub_eq_zero` 的 `b=a` 方向）。

## 状态

* 纸面证明：**[已证-纸面，M2]**。
* Lean 形式化：**[未做]**（下一步）。
