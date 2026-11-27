# $\\kappa_{\\rm obs}$ 的实际含义：它**确实**控制 $k$（修正 248/250）

> 2026-11-09。专家 75 号指出 248 的维度论断有误：
> 因为 $N$ 满列秩 $k$，$\\operatorname{rank}[N,AN]\\ge k$，所以
> $$\\kappa_{\\rm obs}=r\\operatorname{rank}[N,AN]\\ge rk.$$
> 当 $r\\ge1$ 时 $k\\le\\kappa_{\\rm obs}$。因此**固定 $\\kappa_{\\rm obs}$ 必然固定 $k$**，
> 248/250 的“$k$ 可随 $n$ 增长而 $\\kappa_{\\rm obs}$ 固定”是错的。
> 状态：**修正（M2）**。

## 目标

修正有效观测器维数与 $k$ 的关系，重新评估固定 $\\kappa_{\\rm obs}$ 的可解性。

## 设想与理由

专家指出：$N$ 是 $n\\times k$ 满列秩，$[N,AN]$ 含 $N$ 的列，故
$$\\operatorname{rank}[N,AN]\\ge k.$$
于是
$$\\kappa_{\\rm obs}=r\\operatorname{rank}[N,AN]\\ge rk.$$
只要 $r\\ge1$，就有 $k\\le\\kappa_{\\rm obs}$；又 $r\\le\\kappa_{\\rm obs}$（当 $\\operatorname{rank}[N,AN]\\ge1$），
所以 $q=r+r_0\\le\\kappa_{\\rm obs}+r_0$ 也有界。

## 做法：修正后的结论

### 1. 固定 $\\kappa_{\\rm obs}$ 控制一切尺寸

- $k\\le\\kappa_{\\rm obs}$；
- $r\\le\\kappa_{\\rm obs}$；
- $q\\le\\kappa_{\\rm obs}+r_0$；
- $\\omega\\le q-1$ 也有界；
- 极大子式个数 $\\binom{k}{\\omega+1}$ 只依赖 $\\kappa_{\\rm obs}$。

所以 248 的“子式个数随 $k$ 增长”在固定 $\\kappa_{\\rm obs}$ 下**不成立**。
249 的证书 $QPR=I_\\omega$ 在固定 $\\kappa_{\\rm obs}$ 下也是有限维的；
250 的“消去 $R$ 的障碍”不再是必要步骤。

### 2. 可能的算法层级

固定 $\\kappa_{\\rm obs}$ ⇒ 所有尺寸有界 ⇒ 常数维实代数问题。
若 249 的 $Q,R$ 有只依赖尺寸的次数界（专家 75 号的 Proposed bounded-degree lemma），
则量词消去给出
$$f(\\kappa_{\\rm obs})\\operatorname{poly}(\\mathcal L)$$
的 **FPT** 型算法，而不只是 XP。目前还差：
- $Q,R$ 的次数界；
- 比特复杂度/实点处理；
- 证书的实系数实现。

### 3. 与固定 $(q,c)$ 的关系

固定 $(q,c)$ ⇒ $k\\le q-1+c$、$r\\le q$，故
$$\\kappa_{\\rm obs}=r\\operatorname{rank}[N,AN]\\le r\\cdot2k\\le 2q(q-1+c)$$
有界。所以固定 $(q,c)$ 是固定 $\\kappa_{\\rm obs}$ 的特例；
反方向不成立（固定 $\\kappa_{\\rm obs}$ 可以允许 $q$ 有界但 $c$ 变化），
但两者都给出有限维问题。

### 4. 数值核对

244：$r=2$、$\\operatorname{rank}[N,AN]=5$、$\\kappa_{\\rm obs}=10$、$k=3\\le10$；
228：$\\kappa_{\\rm obs}=14$、$k=4\\le14$。
与 $\\kappa_{\\rm obs}\\ge rk$ 一致。

## 进展

* 修正了 248/250 的核心论断；
* 固定 $\\kappa_{\\rm obs}$ 重新成为有希望的参数（可能 FPT）；
* 249 证书在固定 $\\kappa_{\\rm obs}$ 下可用。

## 最终结论

* 固定 $\\kappa_{\\rm obs}$ **确实**控制 $k$ 与子式个数；
* 下一步是证明 249 的次数界，给出 FPT/XP 算法；
* 250 的“消去 $R$”不再是必要路线。

## 放弃原因

* 未证次数界；
* 未实现量词消去/比特复杂度；
* 未处理实点。

## 残留价值

* 一个正确的参数化层级；
* 明确的下一步（次数界 + FPT）。

## 相关文件

* [attempts/246](../../rank_gates/attempts/246_74_verdict.md)
* [attempts/249](249_compact_certificate.md)
* [75 答复](../../../for_expert/archive/75_process_check_and_arm3-answer.md)

## 状态

* 修正：**[M2 纸面]**。
* FPT：**[待证次数界]**。
