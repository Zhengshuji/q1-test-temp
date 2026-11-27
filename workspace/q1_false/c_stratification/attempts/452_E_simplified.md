> **已撤回（478）**：$(E)\iff\pi_2(\mathcal T_W)=W$ **不成立**——$E_\lambda$ 的像是
> $\{(\lambda x-y)\}$，**不是**两个投影之和（$x,y$ 由同一个 $r$ 耦合）。准确核验：$\lambda=i$ 时
> $\dim\pi_\lambda(\mathcal T_W)=1<\omega$。必须回到完整的铅笔秩条件（$\gcd$）。见 [478](../../decision_algorithms/attempts/478_E_lambda_coupled.md)。

# 452 (E) 的简化：$E_\lambda(\mathcal T_W)=W\ \forall\lambda\iff\pi_2(\mathcal T_W)=W$（不需要 $\gcd$）

> 承接 449（(R)∧(E) 命题）与 451（split 塌缩）。本轮做一件更基础的事：
> 重新检查 $(E)$，发现它等价于**一个子空间等式**，$\gcd$ 是多余的。

## 目标

简化 $(E)$ 的判定。

## 设想与理由

$E_\lambda(x,y)=\lambda x-y$，故
$$E_\lambda(\mathcal T_W)=\lambda\pi_1(\mathcal T_W)+\pi_2(\mathcal T_W)\quad(\text{Minkowski 和}).$$
- 取 $\lambda=0$：$E_0(\mathcal T_W)=-\pi_2(\mathcal T_W)$ ⟹ $(E)\Rightarrow\pi_2=W$ ✓；
- 反之若 $\pi_2(\mathcal T_W)=W$，则对一切 $\lambda$ 有 $E_\lambda\supseteq\pi_2=W$ ✓ ⟹ $(E)$ ✓。

于是

$$\boxed{(E)\iff\pi_2(\mathcal T_W)=W}$$

——**一个子空间等式**，不需要子式 $\gcd$，也不需要 $\lambda=\infty$ 的齐次化 ✓（我之前 449 里写"$\gcd$ 是 (E) 的判定"是**多余的**：$\gcd$ 只在需要检查"$\lambda$ 很大时秩不降"时才用，而这里 $\pi_2=W$ 已经保证了对**一切** $\lambda$）。

## 做法与结果

**修正后的中间层命题**（替代 449 的版本）：

> 固定相容 $W$、$m\ge\dim\mathcal T_W$。层 $\omega$ 在 $W$ 上可行 $\iff$
> $$\textbf{(R)}\ \operatorname{span}\bigl(V_0\cup\pi_1(\mathcal T_W)\bigr)=W,
> \qquad\textbf{(E$'$)}\ \pi_2(\mathcal T_W)=W .$$

**为什么与 449 一致**：449 的 $(E)$ 是 $E_\lambda(\mathcal T_W)=W\ \forall\lambda$，本文件证明它 $\iff$ (E$'$) ✓；
449 的证明（必要/充分）逐字照搬，只是把 "$E_\lambda$ 满射" 换成 "$\pi_2=W$" ✓。

## 进展（三点推论）

1. **判定简化**：中间层的可行性 = **两个子空间等式**（$\pi_2=W$、$\operatorname{span}(V_0\cup\pi_1)=W$），
   都是**秩条件**、多项式可算 ✓；不需要 $\gcd$、不需要齐次化 ✓；
2. **与我早先的"$\pi_1=\pi_2=W$"猜想的关系**：我曾在 437 把 $(E)$ 等价成 $\pi_1=\pi_2=W$——**过强** ✗
   （真正只需 $\pi_2=W$，$\pi_1$ 由 (R) 另行约束）；这解释了我后来看到的"$(E)$ 真而 $\pi_1\ne W$"的实例 ✓；
3. **影子问题变清楚**：$\exists W$ 变成
$$\exists W:\ \pi_2(\mathcal T_W)=W\ \text{且}\ \operatorname{span}(V_0\cup\pi_1(\mathcal T_W))=W,$$
   两个条件都是"投影**等于** $W$"——这正是 split 设计里被 $\Phi$ 与 $K_1$ 钉死的那种形式 ✓。

## 最终结论

1. **$(E)$ 的判定从 $\gcd$ 降为子空间等式**（$\pi_2=W$）；
2. 中间层判据 = 两个子空间等式；
3. 于是"$\exists W$"的形状更清楚了：要找 $W$ 使其**两个投影都恰好等于它自己**；
4. 对硬度：判据越简单，越像是可判的——方向仍指 $\mathrm P$。

## 放弃原因

- 没有验证"$\pi_2=W$ 且 (R)"与精确 $\gcd$ 判定在实例上的一致性（纯推导，但推导是两行的）；
- 没有处理 $m<\dim\mathcal T_W$ 的情形；
- 没有回答一般 $\mathcal S$ 的 $\exists W$（仍是唯一开放问题）。

## 残留价值

- **一次实质简化**：把 $(E)$ 从 $\gcd$ 降为子空间等式，且指出 449 的 $\gcd$ 是多余的；
- 修正了 437 里"$(E)\iff\pi_1=\pi_2=W$"的过强表述；
- 让 $\exists W$ 的形状变成"两个投影都等于 $W$"，与 split 设计的塌缩形式一致。

## 下一步

在一般 $\mathcal S$ 上做 $\exists W$：$\pi_2(\mathcal T_W)=W$ 与 $\pi_1$-span $=W$ 是两个"秩达最大"的条件，
在 Grassmannian 上分别是**开**还是**闭**条件？若是闭，则可行集闭 ⟹ 有限枚举型；若是开，则要查其补集。

## 相关文件

- [449](449_expert107_audit.md)（(R)∧(E)，本文件简化其 $(E)$）
- [437](437_eval_map_criterion.md)（过强的等价，已在此更正）
- [451](../../decision_algorithms/attempts/451_split_collapse.md)（split 设计下的塌缩）

## 状态

- $(E)\iff\pi_2=W$：**[已证-纸面]**（两行推导）。
- 中间层判据（两个子空间等式）：**[已证-纸面]**。
- 一般 $\mathcal S$ 的 $\exists W$：**[未解]**。
