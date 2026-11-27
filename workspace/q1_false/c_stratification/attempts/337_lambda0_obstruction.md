# 337 $\lambda=0$ 障碍：命题、推论，以及"全坏可以有多个固定根"

> 承接 336（反例：$K_0$ 含特征向量但整条纤维全坏）与 96 号"三 regime / 可观测性"的框架。
> 本文件把 336 的机制写成命题，并给出**第二批反例**：$\lambda=0$ 不是唯一的障碍。

## 目标

1. 把 336 的 $\lambda=0$ 障碍写成一般命题与推论。
2. 检验"$\operatorname{rank}(A|_{K_0})=k$"是否是修正判据——并用实验否掉它。

## 设想与理由

$(5b)$ 要求 $\operatorname{rank}P(\lambda)=\omega$ 对**每个** $\lambda$；特别 $\lambda=0$ 时是
$\operatorname{rank}H_A=\omega$，这是**与谱无关的纯线性代数条件**。而
$$\operatorname{rank}H_A=\dim(A K_0)-\dim(A K_0\cap V^\perp).$$
所以只要某条"交集下界"被强制，整层就直接不可行。

## 做法

### 命题（$\lambda=0$ 障碍）

> **命题.** 临界模式（$k=\omega+1$、$n-2-p=k-1$）里，设层点是 $(v,V)$（$V\subseteq v^\perp$、$\dim(V\cap K_0)=\omega$）。
> 若 $v\in A K_0$，则
> $$\operatorname{rank}H_A\le\dim(A K_0)-1 .$$
> 因此**若 $\dim(A K_0)=\omega$**，则该层点（以及所有此类点）在 $\lambda=0$ 处就已违反 $(5b)$。

*证明.* $V\subseteq v^\perp$ ⟹ $V^\perp\supseteq\operatorname{span}(v)$；$v\in A K_0$ ⟹ $A K_0\cap V^\perp\supseteq\operatorname{span}(v)\ne0$
⟹ $\dim(A K_0\cap V^\perp)\ge1$ ⟹ $\operatorname{rank}H_A=\dim(A K_0)-\dim(\cdot)\le\dim(A K_0)-1$。$\square$

**推论.** 临界模式里，若层点的核方向 $v$ 是**非零特征值**的特征向量（$Av=\lambda_0v$，$\lambda_0\ne0$），
则 $v=A(v/\lambda_0)\in A K_0$，于是
$$\text{可行}\ \Longrightarrow\ \dim(A K_0)\ge\omega+1=k .$$
所以 $\operatorname{rank}(A|_{K_0})<k$ 的实例，**该层直接不可行**——无需任何谱计算。

> **$v\notin A K_0$ 时的正确条件（97 号审计 §8）**：回到恒等式本身，
> $$\dim(A K_0)-\dim(A K_0\cap V^\perp)=\omega .$$
> 由此只得到 $\dim(A K_0)\ge\omega$（**必要不充分**）：$A K_0\cap V^\perp$ 仍可能非零。
> 所以 "$v\in A K_0$" 是拿到更强下界 $\dim(A K_0)\ge\omega+1$ 的关键情形。

### 实验：$\operatorname{rank}(A|_{K_0})=k$ 是否就够？

60 个随机实例（$Ae_1=\lambda_0e_1$，$\lambda_0\ne0$，$C=e_5^{\mathsf T}$），每个取 8 个随机层点：

- $\operatorname{rank}(A|_{K_0})$ **全部等于 3**（$=k$）——因为 $\lambda_0\ne0$ 迫使 $e_1\in A K_0$，而随机 $A$ 在 $K_0$ 上满秩；
- 54 个实例出现好点，**6 个实例 8 个样本全坏**。

把 6 个疑例的样本加到 24 个，**仍然全坏**（23–24 个坏样本）。抽检其中一个：

$$\text{rank}(A|_{K_0})=3,\qquad \operatorname{rank}H_A=2\ (\lambda=0\ \text{过关}),\qquad
\gcd\equiv\lambda+2 .$$

**公共根固定在 $\lambda=-2$。** 所以障碍不止 $\lambda=0$ 一种：**任何"固定根"都能使整条纤维全坏**。

## 进展

1. $\lambda=0$ 障碍已是**命题**（含证明），推论给出可判的充分不可行条件：$\operatorname{rank}(A|_{K_0})<k$。
2. **$\operatorname{rank}(A|_{K_0})=k$ 不是充分条件**——实验给出 6 个反例（24 样本全坏），抽检的那个障碍在 $\lambda=-2$。
3. 与 96 号的框架对得上：**可行 $\iff$ 约简铅笔可观测**（这是 $(5b)$ 的换述，不是新判据）。
   但"全坏"的机制**不止一种**：可以是某个固定的 $\lambda_0$ 让整条纤维掉秩（本文件与 336），
   也可以是**公共根随参数移动**——[327](327_lambda_movement_experiment.md) 的实例里 10 个 $v$ 给出 8 个
   互素的二次、零点各不相同，而样本全坏。**后者没有固定根**，所以"逐 $\lambda$ 查固定根"抓不到它。

## 最终结论

1. **固定根分析给出的是"不可行"的充分证书**：找到一个 $\lambda_0$ 及一个恒零的秩条件，就能当场
   证明该纤维（甚至整层）不可行——便宜、而且与谱计算无关。
   但它**不是判据**：全坏可以没有固定根（327 的移动根反例）。
2. **完整判据只有 322 那一条**：分量可行 $\iff$ generic gcd $=1$（$\mathbb C(Y)[\lambda]$ 上）。
   它的代价就是 325 的 S3（PIT）。
3. $\lambda=0$ 那一档现在有定理（命题 + 推论）；这是**否定侧**的进展，不是"判据"。
4. 纤维充分性猜想**双重失败**：$K_0$ 含特征向量不够，连 $\operatorname{rank}(A|_{K_0})=k$ 也不够。

## 放弃原因

- **一处自我更正**：初版把"逐 $\lambda$ 查固定根"写成了判据（"可行 $\iff$"）。这是错的：
  (i) $(5b)$ 是 $\exists y\forall\lambda$，而"对每个 $\lambda$ 存在某点"是 $\forall\lambda\exists y$，量词反了；
  (ii) 全坏可以没有固定根（327 的移动根），所以逐 $\lambda$ 检查连"全坏"都不完备。
  已改为"固定根 = 不可行的**充分证书**"。
  **教训**：新结论必须与既有记录交叉检查——327 的移动根写在两轮之前，本轮初稿却把它漏掉了。
- 只抽检了一个"$\lambda=-2$"的实例，没有给出"固定根 $\lambda_0$"的一般命题（应与 0 的情形同型，但未写）。
- 没有给出存在固定根的**判定**算法（未刻画哪些 $\lambda$ 会成为固定根）。
- 6 个疑例只有"24 样本全坏"的证据（坏集闭 + 开集稠密使这证据很强，但仍非证明）。

## 残留价值

- 一个带证明的 $\lambda=0$ 命题 + 可判的充分不可行条件（$\operatorname{rank}(A|_{K_0})<k$）；
- **第二批反例**（6/60），并指出全坏的机制不止 $\lambda=0$；
- 把"固定根"这一种机制讲清楚（含 $\lambda=0$ 的定理），并明确它**只是否定侧的充分证书**——
  全坏也可以没有固定根（327 的移动根）。

## 相关文件

- [attempts/336](336_fibre_sufficiency_counterexample.md)（第一个反例：$\lambda=0$）
- [attempts/335](335_expert96_verdict.md)（96 号裁决与 Conjecture）
- [attempts/331](331_eigenvector_criterion.md)（被判据为必要条件）
- [attempts/328](../../decision_algorithms/attempts/328_quotient_pencil_theorem.md)（商铅笔与可观测性）
- [c341](../../../../tools/verification/c341_fibre_sufficiency_counterexample.py)

## 状态

- $\lambda=0$ 命题与推论：**[已证-纸面]**。
- 第二批反例（6 个全坏实例 + $\lambda=-2$ 的抽检）：**[精确验证，样本级]**。
- "固定根"的一般刻画与判定：**[未做]**。
