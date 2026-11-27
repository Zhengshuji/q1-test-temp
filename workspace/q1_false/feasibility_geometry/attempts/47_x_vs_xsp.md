# $X$ 与 $X_{\rm sp}$ 的结构：**两类**实例，而不是"总是薄"

> **2026-11-03 更正（专家 §4.4–§4.5）**：
> 1. 本文说的"seed 3023 / 3027 处处可行"**过强**——$\deg_\lambda\gcd=0$ 与 $M$ 满行秩都是**一般位置**性质，
>    逐点可行需要另验；正确说法是"一般可行"。
> 2. 可行集的形状一般只是 **constructible**（不必开/不必闭）；专家给了反例 $f=\theta\lambda+1$、$g=2\theta\lambda+2$
>    （好集 $\{\theta=0\}$ 是闭集）。
> 3. 正确的组织方式是**按代数可容许族的不可约分支**逐支讨论"典型确定性除子次数"。

## 目标

按专家 §3.3 的建议，先算代数可容许簇 $X=\{\theta:(5a)\}$，再看谱可行子集
$X_{\rm sp}=\{\theta: e_0\in\operatorname{col}M(\theta)\}$，判断"薄性"是不是结构性质。

## 设想与理由

专家指出两个"典型点"不能混：**整图卡的典型点**与**$X$ 上的典型点**。本脚本对单参数图卡直接算：

* $X$：(5a) 的 $(h_0+1)$-子式（单参数时是一元多项式）；
* $X_{\rm sp}$：$[M(\theta)\mid e_0]$ 的 $(\rho+1)$-子式（$\rho$ = $M$ 的典型秩），
  并特判 $\rho=$ 行数（此时 $e_0$ 自动在列空间）；
* 另给"典型 gcd 的 $\lambda$ 次数"。

## 做法

[x_vs_xsp.py](../../../../tools/verification/x_vs_xsp.py)：实例 → 逐图卡算上面三个量并打印因式分解。

## 进展

**第一类：典型 gcd 次数 $=0$（一般位置可行）**

| 实例 | 图卡 | $h_0$ | $X$ | $\rho$（行数）| $X_{\rm sp}$ |
|---|---|---|---|---|---|
| $n=5,p=2,r=1$ seed 3023，$q_0=2$ | (0)、(1) | $5=n$ | 整个 𝔸¹（$(5a)$ 自动）| $2$（$=2D$）| **整个图卡** |
| $n=6,p=2,r=2$ seed 3027，$q_0=3$ | (0)、(1) | $6=n$ | 整个 𝔸¹ | $4$（$=2D$）| **整个图卡** |

（$\rho=$ 行数 ⟹ $M$ 满行秩 ⟹ $e_0$ 自动落在列空间 ⟹ $(5b)$ 处处成立。）

**第二类：典型 gcd 次数 $\ge1$（一般位置失败）**：C4（两图卡 $\deg=2$，$X_{\rm sp}=\varnothing$）、
以及 [attempts/43](43_drop_locus.md) 的 6 个 $q_0$ 实例——可行点只出现在 gcd 跌落轨迹上。

## 最终结论

1. **"薄"不是普遍现象**：实例分两类——
   * **一般可行**（典型 gcd 次数 0，$M$ 满行秩）：$X_{\rm sp}=X$，可行集是开的；
   * **一般失败**（典型 gcd 次数 $\ge1$）：$X_{\rm sp}\subsetneq X$，可行点被限制在**跌落轨迹**上（C4 上是空集）；
2. 因此此前"$q_0$ 阶可行集总是薄集"的说法**过强**，应改为：
   *"当典型 gcd 有正次数时，可行点被限制在跌落轨迹上；当它为 0 时可行集是整个代数可容许集"*；
3. 与 $(*)$ 判据的关系：$\rho=$ 行数时 $(*)$ 自动成立（无需再判）；$\rho<$ 行数时才需要用左零空间/子式判。

## 放弃原因

不适用（结构刻画完成）。**未做**：多参数图卡的 $X$ 的分支分解（需消元，预算受限）。

## 残留价值

* 一个**二分**的结构陈述（一般可行 vs 一般失败），比"薄集"更准确、也更可操作；
* 两个被证的具体事实：seed 3023 与 seed 3027 在 $q_0$ 阶**处处可行**（$M$ 满行秩）；
* 更正了 docs/08 §4.8 里"可行集 = 跌落轨迹"的过度概括（只在第二类成立）。

## 相关文件

- [tools/verification/x_vs_xsp.py](../../../../tools/verification/x_vs_xsp.py)
- [tools/verification/bezout_rank_test.py](../../../../tools/verification/bezout_rank_test.py)
- [docs/08_results.md](../../../../docs/08_results.md) §4.8（已同步更正）
- [workspace/q1_false/feasibility_geometry/attempts/43_drop_locus.md](43_drop_locus.md)
- [workspace/for_expert/07_programme_report_and_open_problems-answer.md](../../../for_expert/archive/07_programme_report_and_open_problems-answer.md)（§3.3–§3.5）
