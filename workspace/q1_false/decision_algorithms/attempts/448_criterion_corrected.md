# 448 再更正：判据不是"$\dim\mathcal T_W=2\omega$"，而是 $(E)$；$\dim=2\omega-1$ 也能满足 $(E)$

> 承接 447（判据 $\mathcal T_W=W\oplus W$，21/21 数据）。本轮写证明时构造出**解析反例**：
> 存在 $\dim\mathcal T_W=2\omega-1$ 的子空间满足 $(E)$ ⟹ 447 的判据**假**。

## 目标

证 447 的必要方向（$\dim<2\omega$ ⟹ 不可行）。结果：**它是错的**。

## 设想与理由

先猜"$\dim<2\omega$ ⟹ $(E)$ 失败"，于是去找反例。

## 做法（反例）

取 $\omega=2$、$W=\mathbb C^2$，令 $\mathcal T=\ker\varphi\subseteq W\oplus W$，其中
$$\varphi(x,y)=\alpha(x)+\beta(y),\qquad \alpha,\beta\in W^*,\quad \alpha\notin\operatorname{span}\{\beta\}.$$
则 $\dim\mathcal T=2\omega-1=3$。考察 $E_\lambda(\mathcal T)$ 何时不是整个 $W$：这等价于存在 $0\ne\gamma\in W^*$ 使
$(\lambda\gamma,-\gamma)\perp\mathcal T$，即 $(\lambda\gamma,-\gamma)\in\operatorname{span}\{\varphi\}$，于是
$$\lambda\gamma=c\alpha,\quad -\gamma=c\beta\ \Longrightarrow\ \alpha=-\lambda\beta\ \Longrightarrow\ \alpha\in\operatorname{span}\{\beta\}\ \text{✗}.$$
所以**对一切 $\lambda$**，$E_\lambda(\mathcal T)=W$ ✓，即 $(E)$ 成立——**尽管 $\dim\mathcal T=2\omega-1<2\omega$** ✗。

由 446 的等价（$m\ge\dim\mathcal T_W$ 时 $(E)\iff(F)$），该实例的层 $\omega$ 是**可行**的 ✓。

## 进展（更正）

1. **447 的判据（$\dim=2\omega$）假**：$\dim=2\omega-1$ 也能满足 $(E)$ ⟹ 也能可行；
2. **真正的判据**就是 $(E)$ 加行数条件：
$$\boxed{\text{层 }\omega\text{ 在 }W\text{ 上可行}\iff E_\lambda(\mathcal T_W)=W\ \forall\lambda\ \text{且}\ m\ge\dim\mathcal T_W}$$
   其中 $(E)$ 由 $M(\lambda)=(\lambda x_j-y_j)$ 的 $\omega$-子式互素判定（可算）✓；
3. 447 那 20 个"$\dim<2\omega$ ⟹ 不可行"的样本，其 $(E)$ **本来就是假**（$\gcd$ 非常数）——
   所以它们是"$(E)$ 假 ⟹ 不可行"的例子，**不是**"$\dim<2\omega$ ⟹ 不可行"的证据 ✗。

## 最终结论

1. **判据 = $(E)$ + 行数**（可算，多项式：$\omega$-子式的 $\gcd$）；
2. 中间层因此**多项式可判**；
3. 与顶层（子式 $\gcd$ + 秩补全阈值）、$\omega=0$（闭式）合起来：**三层全部可算** ⟹
   $q1$ 看起来在 $\mathrm P$，**硬度无立足点**；
4. 我这条线上**已撤回四次**（441 的 $(E)\not\Rightarrow(F)$、442 的灰色带、444/447 的维数判据、
   435 的中间层恒不可行）——共同原因是"把弱化条件当真条件"或"族太特殊"。

## 放弃原因

- 反例只对 $\omega=2$ 显式写出；一般 $\omega$ 的推广（$\mathcal T=\ker\varphi$ 的高余维版本）未写；
- 没有把"$(E)$ + 行数"写成完整的**层算法**（含 $\exists W$ 的搜索）；
- 固定行补一位的边界未处理。

## 残留价值

- **一个解析反例**，纠正了 447 的判据；
- **正确的判据**（$(E)$ + 行数），且它是**可算的**；
- 明确了 $q1$ 的方向性结论（看起来 $\in\mathrm P$）。

## 下一步

把"$\exists W$ 使 $(E)$ 成立"写成算法：遍历 $W$（Grassmannian）不可能，但 $(E)$ 是 $\mathcal T_W$ 的条件，
而 $\mathcal T_W=\mathcal S\cap(W\oplus W)$——需要找 $W$ 使 $\mathcal S\cap(W\oplus W)$ 的两个投影都满射
**且**子式互素。这是下一步的具体算法问题。

## 相关文件

- [447](../../c_stratification/attempts/447_criterion_summary.md)、[444](../../c_stratification/attempts/444_threshold_criterion.md)（判据，已更正）
- [446](446_bug_located.md)（$(E)\iff(F)$）
- [437](../../c_stratification/attempts/437_eval_map_criterion.md)（$(E)$）

## 状态

- 447 的判据：**[已撤回，有解析反例]**。
- 正确判据（$(E)$ + 行数）：**[已证-纸面]**（充分 + 必要）。
- 层算法：**[未写]**。
