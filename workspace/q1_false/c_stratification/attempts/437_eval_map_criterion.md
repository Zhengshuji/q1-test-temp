# 437 $E_\lambda$ 判据：可计算的**点态**必要条件；反例与特征族都被它解释

> 落实 436（专家 106 号）给的正确对象
> $$E_\lambda:\mathcal T_W\to W,\qquad (x,y)\mapsto \lambda x-y .$$
> 本轮把它做成**精确可算**的判据，并在反例与特征族上验证。

## 目标

1. 把 $E_\lambda$ 的满射性写成可算条件；
2. 用它解释：反例为什么可行、程序化特征族为什么不可行；
3. 给出与"$K_0$ 中特征向量"的精确关系。

## 设想与理由

$\mathcal T_W=\mathcal S\cap(W\oplus W)$ 的每一对 $(x,y)$ 给铅笔一行 $\lambda x-y=E_\lambda(x,y)$。
所以铅笔在 $\lambda$ 处的秩**至多**是 $E_\lambda(\mathcal T_W)$ 的维数（加上固定行补的一维）：

$$\operatorname{rank}P(\lambda)\le \dim E_\lambda(\mathcal T_W)+\bigl[\text{固定行}\notin E_\lambda(\mathcal T_W)\bigr].$$

于是：

> **判据（点态必要）.** 层 $\omega$ 在 $W$ 的纤维上可行 ⟹ 对一切 $\lambda$：
> $$\dim E_\lambda(\mathcal T_W)+\bigl[\text{固定行}\notin E_\lambda(\mathcal T_W)\bigr]\ \ge\ \omega .$$
> 特别地，若 $E_\lambda(\mathcal T_W)$ **不满射** $W$（$\dim<\omega$）且固定行补不上，则该层必死，
> 而且**换任何自由行都救不回来**。

**可算化**：取 $\mathcal T_W$ 的基 $p_1,\dots,p_D$，构造 $D\times\omega$ 矩阵
$$M(\lambda)=\bigl(\lambda x_j-y_j\bigr)_{j},$$
则 $E_\lambda$ 满射 $\iff$ $M(\lambda)$ 的 $\omega\times\omega$ 子式**互素**（$\gcd$ 为常数）——纯 $\gcd$ 计算 ✓。

**精确结构**：$\dim E_\lambda(\mathcal T_W)=\dim\mathcal T_W-\dim\bigl(\mathcal T_W\cap\Gamma_\lambda\bigr)$，
其中 $\Gamma_\lambda=\{(x,\lambda x)\}$ 是"乘 $\lambda$ 的图"。而
$$\mathcal T_W\cap\Gamma_\lambda\ \cong\ \bigl\{r:\ rN\in W,\ r(\lambda I-A)N=0\bigr\},$$
即**$(\lambda I-A)N$ 的左零空间与 $W$ 的原像之交**。

## 做法

取 $\mathcal T_W$ 的基、构造 $M(\lambda)$、算 $\omega$-子式的 $\gcd$（[c383](../../../../tools/verification/c383_eval_map.py)）。

## 进展

[c383](../../../../tools/verification/c383_eval_map.py)：

| 实例 | 层 | $\dim\mathcal T_W$ | $M(\lambda)$ 的 $\omega$-子式 $\gcd$ | 满射？ | 与已知判定 |
|---|---|---|---|---|---|
| **反例**（$n=6,p=2$，移位） | $\omega=1$ | 4 | $1$ | **是** ✓ | **可行** ✓ 一致 |
| $B=\operatorname{diag}(1,2,3)$ | $\omega=2$ | 5 | $(\lambda-3)(\lambda-1)$ | **否** | 不可行 ✓ 一致 |
| $B=\operatorname{diag}(1,1,2)$ | $\omega=2$ | 5 | $(\lambda-1)^2$ | **否** | 不可行 ✓ 一致 |

**两件事都被解释了**：

1. 反例里 $\mathcal S$ 满射（$\mathcal S=\mathbb Q^{1\times4}$ ⟹ $\mathcal T_W=W\oplus W$），$E_\lambda$ 处处满射 ⟹ 可行；
2. 程序化特征族里 $E_\lambda$ 在**特征值处**降秩（$\gcd$ 恰是那些 $(\lambda-\mu)$）⟹ **点态**就没有足够的像
   ⟹ 按判据必死 ⟹ 与 435 的"不可行"一致。

## 最终结论

1. **$E_\lambda$ 判据是可算的**（子式 $\gcd$），而且它给的是**点态**必要条件；
2. 它把失败分成两类（正是专家 §Q4 提的两分法）：
   - **点态不满射**（本文件 3 例里的 2 例）：**任何**自由行都救不回 ⟹ 该层在 $W$ 上必死；
   - **点态满射但无单一选择**：这是**全局铅笔问题**（专家 §Q4 的第二机制），本轮没触及；
3. 与特征向量的精确关系：降秩量 $=\dim\{r:rN\in W,\ r(\lambda I-A)N=0\}$——
   这既是"$K_0$ 中特征向量"的推广（那里 $rN$ 可落在 $W$ 里），也说明**不是**每个特征向量都会致层死亡
   （要它的 $rN$ 落在 $W$ 中才行）。

## 放弃原因

- 没有做**充分性**方向（点态满射 + 足够多行 ⟹ 存在正则铅笔？）——那是全局铅笔问题；
- 只测了 1 个反例与 2 个特征族；没有系统枚举；
- 没有把"$rN\in W$"这个条件与 $W$ 的 Grassmann 坐标联系起来。

## 残留价值

- **一个可算的点态判据**（子式 $\gcd$），能快速排除实例；
- **把两类失败分开**（点态 vs 全局），这正是专家要求的两分法；
- 反例与特征族在同一个框架下被解释 ✓。

## 下一步

1. **充分性**：若 $E_\lambda$ 处处满射、且 $m$ 足够大，是否存在正则铅笔？（这是全局问题，
   专家建议先固定 $B,D$ 族、变动 $r_0$ 与 $m$ 做精确 $\gcd$ 实验。）
2. 把点态判据与 $W$ 的 Grassmann 坐标联系起来，看"$E_\lambda$ 满射"在 $\operatorname{Gr}$ 上是什么集合。

## 相关文件

- [436](436_expert106_audit.md)（106 号裁决；$E_\lambda$ 的出处）
- [435](435_characteristic_dead.md)（被本文件解释）
- [434](434_hardness_status.md)（层表，已撤回）
- [433](433_drop_criterion.md)（降秩判据；本文件的判据是它的精确版）

## 状态

- $E_\lambda$ 判据（点态必要）：**[精确验证]**（3 例一致）。
- 与特征向量的关系：**[已写清]**（降秩量 = 左零空间与原像之交）。
- 充分性/全局问题：**[未做]**。
