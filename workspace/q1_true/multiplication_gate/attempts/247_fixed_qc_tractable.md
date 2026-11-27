> **补（248）**：固定 $\kappa_{\rm obs}$ **不**自动给 XP：$q,\omega$ 有界，但 $k$ 可随 $n$ 增长，
> 秩条件需要 $\binom{k}{\omega+1}$ 个子式。安全的多项式定理是固定 $(q,c)$（本文件）。

# 固定 $(q,c)$ 的可解性：$k\\le q-1+c$，压缩问题降为常数维

> 2026-11-09。Experiment A 的定理化：由谱判据 $\\omega\\le q-1$ 得
> $k=\\omega+c\\le q-1+c$。所以**固定 $q$ 与 $c$** 时，压缩矩阵 $H,H_A$ 的尺寸有界，
> 可行性化为一组**常数个变量、常数个多项式**的实代数问题；用实量词消去可在多项式时间判定。
> 状态：**M2（纸面）+ 数值核对**。

## 目标

给出 74 号 Experiment A 的第一个定理：固定 $(q,c)$ 的可解性。

## 设想与理由

74 号的特征向量判据给出 $\\omega\\le q-1$；而 $c=k-\\omega$。两者相加即得 $k$ 的上界。
$H,H_A$ 是 $q\\times k$；$k$ 有界 ⇒ 压缩数据有界。自由行 $R$ 只通过 $RN,RAN$ 进入，
而 $R\\mapsto(RN,RAN)$ 的像维数是 $\\kappa_{\\rm obs}=r\\operatorname{rank}[N,AN]$，也有界。

## 做法

### 1. 引理（谱判据）

$(5a)$ ⇒ 存在 $F$ 使 $H_A=FH$，$P(\\lambda)=(\\lambda I-F)H$。$(5b)$ 等价于
$\\operatorname{im}H\\cap E_\\lambda(F)=\\{0\\}$ 对所有特征值成立。因此
$$\\omega=\\operatorname{rank}H\\le q-1.$$

### 2. 定理（固定 $(q,c)$）

设 $q$ 与 $c=k-\\omega$ 固定。则
$$\\boxed{k=\\omega+c\\le q-1+c},$$
所以 $k$ 是只依赖 $(q,c)$ 的常数。

进一步，$H=H_0+RN$、$H_A=H_{A,0}+RAN$，其中 $H_0=L_0N$、$H_{A,0}=L_0AN$ 固定；
自由部分由
$$\\mathcal T(R)=(RN,RAN)\\in\\mathbb C^{r\\times k}\\times\\mathbb C^{r\\times k}$$
给出，其像的维数
$$\\kappa_{\\rm obs}=r\\operatorname{rank}[N,AN]\\le r\\cdot2k\\le (q-r_0)\\cdot2(q-1+c)$$
也有界。

于是可行性等价于：存在 $X,Y$ 属于固定线性子空间 $\\operatorname{im}\\mathcal T$，使
$$\\operatorname{rank}\\begin{bmatrix}H_{A,0}+Y\\\\H_0+X\\end{bmatrix}=\\operatorname{rank}(H_0+X),$$
且 $P(\\lambda)=\\lambda(H_0+X)-(H_{A,0}+Y)$ 的极大子式 gcd 为 1。

变量数 $\\le2\\kappa_{\\rm obs}$ 是常数；多项式个数/次数只依赖 $(q,c)$。
由实量词消去（Basu–Pollack–Roy）可在 $\\operatorname{poly}(n,\\text{bit size})$ 时间判定。

### 3. 数值核对

`tools/verification/c247_fixed_qc.py`：
- 244：$q=3,c=1$ ⇒ $k\\le3$，实际 $k=3$；
- 228：$q=3,c=2$ ⇒ $k\\le4$，实际 $k=4$；
- 234：$q=2$（不可行），$k=3$，$c$ 未定义。

## 进展

* 固定 $(q,c)$ 的常数维归约（纸面）；
* $k\\le q-1+c$ 的简单上界；
* 与 $\\kappa_{\\rm obs}$ 的关系：固定 $(q,c)$ ⇒ $\\kappa_{\\rm obs}$ 也有界。

## 最终结论

* **固定 $(q,c)$ 时 $q1$ 在 P**（理论算法；量词消去常数巨大）；
* 固定 $c$ **单独不够**：244 的 $c=1$ 但 $\\kappa_{\\rm obs}=10$，228 的 $c=2$ 但 $\\kappa_{\\rm obs}=14$，
  且 $k$ 随 $n$ 增长；需要 $q$ 或 $\\kappa_{\\rm obs}$ 作为额外参数；
* 这给出一个明确的参数化层级：
  $$\\text{固定 }(q,c)\\ \\Rightarrow\\ \\text{固定 }\\kappa_{\\rm obs}\\ \\Rightarrow\\ \\text{固定维数实代数}.$$

## 放弃原因

* 未实现量词消去算法（只给复杂度论证）；
* 未证 fixed $\\kappa_{\\rm obs}$ 单独可解（公式规模可能随 $k$ 增长）；
* 未处理实点/复点与比特长细节。

## 残留价值

* 一个可写进论文的定理（固定 $(q,c)$ 可解）；
* 参数化层级的清晰表述；
* 解释为什么“固定 $c$”不够。

## 相关文件

* [attempts/246](../../rank_gates/attempts/246_74_verdict.md)
* `tools/verification/c247_fixed_qc.py`
* [docs/05 Q9](../../../../docs/05_open_questions.md)


**Lean 内核**：`tools/lean/MyProof/KappaObs.lean`（`finrank_ker_pairMap` 等，pairMap 的秩-零化度；`lake env lean` EXIT 0，axioms 仅 propext/choice/quot）。矩阵实例与“$r$ 行相乘”由纸面 + `c248_kappa_check.py`（90 例）覆盖。

## 状态

* 定理：**[M2 纸面]**。
* 算法实现：**[未做]**。
