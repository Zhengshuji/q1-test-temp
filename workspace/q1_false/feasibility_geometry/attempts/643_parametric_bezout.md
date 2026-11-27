# 643 参数化 Bézout 矩阵：$(5b)$ 的有限秩条件

> 2026-11-27。按 ChatGPT 的建议，把 642 的 Bézout 系统写成参数化矩阵，给出 $(5b)$ 的有限秩刻画。
> 状态：**[已证-纸面]** + **[精确验证]**（A/B/638）。

## 构造

固定 $H,Z$（由自由行参数 $\theta$ 决定），$P(\lambda)=\lambda H-ZH$ 的 $\omega$ 阶子式 $f_1,\dots,f_m$，$D=\max\deg f_i$。
Bézout 系统（642）：
$$M(\theta)\,c=b,$$
其中 $c=(a_{i,k})_{i\le m,\,k<D}$，$M$ 的列由 $\lambda^k f_i$ 的系数组成，$b$ 对应常数项 $1$。

## 定理（固定 $\theta$）

$$\operatorname{rank}\big(M(\theta)\big)=\operatorname{rank}\big([M(\theta)\mid b]\big)\iff \gcd(f_1,\dots,f_m)=1\iff (5b).$$

证明：Bézout 恒等式 $\sum_i a_if_i=1$ 的存在性等价于 $\gcd=1$；而它是 $M c=b$ 的可解性。

## 参数化形式

$$\text{可行}\iff\exists\theta:\ \operatorname{rank}M(\theta)=\operatorname{rank}[M(\theta)\mid b].$$
等价地
$$\text{可行}\iff\exists r:\ \operatorname{rank}M(\theta)=r\ \wedge\ \operatorname{rank}[M(\theta)\mid b]=r .$$
这是有限个**行列式子式条件**（determinantal），把 $(5b)$ 的“对所有 $\lambda$”化为有限代数条件。

## 验证

| 实例 | 子式数 | $D$ | 系统秩 | 增广秩 | 可解 |
|---|---|---|---|---|---|
| A（641，可行） | 3 | 2 | 4 | 4 | 是 |
| B（641，不可行） | 4 | 2 | 2 | 3 | 否 |
| 638（可行） | 3 | 2 | 4 | 4 | 是 |

## 意义与局限

- 对固定 $\theta$：多项式大小的线性判定；
- 对参数 $\theta$：$\operatorname{rank}$ 条件给出行列式簇的并，是**有限描述**（与 565 一致），但不自动是多项式时间；
- 与 639 的 $K_\infty$ 上界结合：先用 $K_\infty$ 限制 $\omega$，再对候选 $\omega$ 做 Bézout 秩判定。

## 下一步

1. 研究 $M(\theta)$ 的元素次数与 $\theta$ 的依赖（是否低次、能否用 Sylvester 矩阵避免大 $m$）；
2. 把“秩分层 + Bézout 可解”写成算法框架，分析每层复杂度；
3. 若每层判定多项式，则得到 q1 ∈ P 的候选算法（需总状态数界，见 623/626）。

## 状态

- 定理：**[已证-纸面]**；
- 验证：**[精确验证]**；
- 复杂度：**[开放]**。
