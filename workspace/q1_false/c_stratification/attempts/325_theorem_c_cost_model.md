# 325 定理 C 的成本：整条超平面判定归约到一个 PIT

> 承接 324（分量定理：$\#\le1+\delta$，显式参数化）与 94 号裁决（定理 A/B 可声称，C 未证）。
> 本文件把"generic gcd 的代价"算成一张**显式的成本表**，并指出它可以消掉的那一半（Type I）。

## 目标

把 94 号的**定理 C**（多项式时间）拆到最小：算出每一步的参数个数、次数、位长，指认**唯一的**非平凡难点。

## 设想与理由

324 已把分量写成"显式射影底 + 显式核丛"：
$$\sigma\in B\ (\text{射影线性子空间}),\qquad y_i\in W_\sigma=\ker M(\sigma),\quad M\ \text{线性于}\ \sigma .$$
于是每个分量上的铅笔是 $P_{\sigma,y}(\lambda)=\lambda H-H_A$，其 $\omega$-子式 $m_I(\sigma,y;\lambda)$ 是
$(\sigma,y)$ 的多项式、$\lambda$ 的次数 $\le\omega$。"generic gcd $=1$"就是对这一族多项式做恒等测试。

## 做法：把测试拆成可记账的小步

**(1) 参数与次数。** 记 $b=\dim B$、$d_0=\dim\mathcal T$、$m=q-r_0$、$N_{\min}=\binom{q}{\omega}$。

| 量 | 值 | 说明 |
|---|---|---|
| 分量参数个数 | $b+m\,(d_0-\rho)$ | $\rho=2$（开片）/ $\rho=1$（$F_\lambda$）|
| $m_I$ 对 $\lambda$ 的次数 | $\le\omega$ | $\omega\times\omega$ 子式 |
| $m_I$ 对 $\sigma$ 的次数 | $\le\omega$ | $H,H_A$ 对 $\sigma$ 线性；子式取 $\omega$ 次 |
| $m_I$ 对 $y$ 的次数 | $\le\omega$ | 同上 |
| 子式个数 | $\binom{q}{\omega}$ | 可用 Cauchy–Binet 压到 $\ell$ 量级（项目已有）|

**(2) 三步，全部是线性代数或 PIT。**
- **S1 覆盖**：枚举 $1+\#\{\lambda:E_\lambda\ne\varnothing\}\le1+\delta$ 个分量（324）——**已解决**，纯线性代数。
- **S2 Type I 排除**：若某个 $g_0(\lambda)\in\mathbb C[\lambda]$（$\deg g_0>0$）整除**每一个** $m_I$（在 $\mathbb C[\sigma,y][\lambda]$ 中），
  则该分量必定全坏。检验是**精确除法**：对首一 $g_0$ 取余 $r_I=m_I\bmod g_0$，要求 $r_I\equiv0$——
  除以首一多项式在系数上是**线性**的，所以这是逐系数的恒等测试。
- **S3 剩余（Type III）**：$g_0$ 不整除时，需要判定"generic gcd $=1$"——这就是 **PIT**。

**(3) 为什么 S2 是"能消掉的那一半"。** 104 的 $Z^\circ$ 正是 Type I：$\lambda_0=0$ 处整行塌到固定直线
$\langle V_0\rangle$，故 $\lambda\mid m_I$ 恒成立（一行代数：$\lambda=0$ 时 $P=-H_A$ 的各行都 $\propto V_0$，
故全部 $2$-子式为 $0$）。S2 在这种分量上**不需要**任何 PIT。

**(4) S3 的精确形状（唯一的缺口）。** 需要判定：在分量 $Y$ 上，是否存在点使某个 Bézout 矩阵
$\Phi_D(\sigma,y)$ 的极大子式非零。由 94 号的界可取 $D\le(s-1)\omega$（$s=\binom{q}{\omega}$），
$\Phi_D$ 的尺寸 $\approx (D+1)\omega\times(s(D+1)\omega)$ 量级、条目对 $(\sigma,y)$ 次数 $\le\omega$。
用网格去随机化要对每个参数方向取 $>$ 该次数的点，参数个数 $b+m(d_0-\rho)$ ⟹ **指数**。
所以 S3 的确定性多项式算法 = 这个结构化 PIT 的确定性算法；这正是 94 号 Q1 问的对象。

## 进展

- 成本表已列出（参数个数、三处次数、子式个数）。
- **S1 完全解决**（324）；**S2 是线性代数**（精确除法），在 104 上验证为一行的恒等式；
- **S3 = 唯一的 PIT**，且它的输入族是"线性参数化 + 次数 $\le\omega$"的显式行列式。

## 最终结论

1. 定理 C 的难点**不在几何、不在分量数、也不在域**，而在 **S3 这一个 PIT**。
2. 由此得到两条互斥的推进方式：
   - 若能证明 S3 对这类族是多项式可判（例如：线性参数化下"行列式恒等"有确定性算法），则 **$c=1$ 层 $\in\mathrm P$**；
   - 若 S3 有下界（相对一般 PIT 或某个 $\exists\mathbb R$ 类），那就是**层程序的第一处硬度证据**。
3. 对 $q1$ 的意义：这是唯一一条"非黑即白"的岔路口——两边的结局都直接回答层程序能否走通。

## 放弃原因

- 没有给出 S3 的算法，也没有给出下界（本文件只做归约与记账）。
- S2 的"整除"检验仍需在分量的参数化下做恒等测试（逐系数），严格说那也是一次 PIT，
  但它是**线性**除法产生的、次数低一档的 PIT；与 S3 不是同一难度档。

## 残留价值

- 一张可复核的成本表（写论文或送审时可逐项引用）；
- 把定理 C 的缺口**锁定到一个对象**（S3 的 PIT），而不是"分量 + gcd + 位长"三团雾；
- Type I/III 的划分给出一个**可立即执行**的子算法（S1+S2），它在 104 上已经跑通。

## 相关文件

- [attempts/324](324_hyperplane_component_theorem.md)（分量定理，S1）
- [attempts/322](322_hyperplane_determinism_components.md)（generic-gcd 判据）
- [attempts/323](323_expert94_verdict.md)（94 号裁决：A/B/C）
- [attempts/104](104_p2_constrained_locus.md)（Type I 的例子：$\lambda_0=0$ 塌到 $\langle V_0\rangle$）
- [c332](../../../../tools/verification/c332_104_component_split.py)

## 状态

- S1：**[已证-纸面]**（324）。
- S2：**[已证-纸面]**（精确除法；104 上是恒等式），附注：其"逐系数恒等"仍是低阶 PIT。
- S3：**[未解决]**——即 94 号 Q1。
