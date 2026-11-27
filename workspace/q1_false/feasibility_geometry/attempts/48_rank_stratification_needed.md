# 快速充分判据的边界：**秩跌落太常见**，"满行秩 ⟹ 可行"几乎不触发

## 目标

按上一轮的思路，做一个**多项式时间可判的充分条件**：若 Bézout 矩阵 $M(\theta)$ 在某 $\theta$ 上**满行秩**
（$\operatorname{rank}=2D$），则 $e_0$ 自动落在列空间 ⟹ $(5b)$ 成立 ⟹ 该阶可行（再核 $(5a)$ 与七条检查）。

## 设想与理由

这是专家 $(*)$ 的直接推论，只需数值秩（有理算术），不需要符号消元——若能常用，就是一个**部分算法**。

## 做法

[fast_feasible.py](../../../../tools/verification/fast_feasible.py)：逐图卡、在若干有理 $\theta$（$0,\pm1,\pm2,3,\pm1/2,3/2,5/2$）
上算 $\operatorname{rank}M(\theta)$，满 $2D$ 就取见证并核验。

## 进展

在 $q_0$ 阶的 8–24 个实例上，**几乎没有触发满行秩**：统计 `UNKNOWN` 8/8、23/24（仅 1 个触发）。

**原因（关键）**：$\operatorname{rank}[V|Z]$ 在特殊 $\theta$ 上会**跌落**（例如 $n=5,p=1,r=2$ seed 3003 在 $\theta=0$ 处
从 4 掉到 3），此时"极大子式"的**尺寸**也随之从 4 变成 3——
* 若用固定尺寸（$\dim V+d$），$M(\theta)$ 在那些点上是错的（我实测：该见证点上 $\operatorname{rank}M(0)=0$、
  $\operatorname{rank}[M|e_0]=1$，按 $(*)$ 会误判为 $(5b)$ 失败，而 Toeplitz 与零空间铅笔都判它成立）；
* 若用**专门化后的**尺寸，就必须对"秩的取值"做**有限析取**——这正是专家说的那一步，仍未实现。

## 最终结论

1. **充分判据成立但触发率极低**：$\operatorname{rank}M=2D$ 在这些实例上几乎不出现；
2. **根本障碍是"秩跌落"**：$V\cap\mathcal Z\ne0$ 在特殊 $\theta$ 上很常见，使极大子式的尺寸变化；
   $(*)$ 判据（以及 [attempts/47](47_x_vs_xsp.md) 的两类划分）**只在秩恒定的图卡上有效**
   （seed 3023、3027 是秩恒定的例子，已用于那一轮）；
3. 因此"$\mathrm{DEC}(q)$ 的部分算法"目前**没有**：能判的只有秩恒定图卡；
4. **下一步就是秩分层**：对图卡按 $\operatorname{rank}[V|Z]$ 的取值分层（每层是行列式条件），
   在每层上用对应尺寸的极大子式做 $(*)$ 判据——这应能覆盖绝大多数实例。

## 放弃原因

充分判据的触发率不足以支撑"部分算法"；必须先做秩分层。

## 残留价值

* 一个**可判但稀薄**的充分条件（满行秩 ⟹ 可行）及其实现；
* 明确诊断出**真正的技术瓶颈**：秩跌落导致极大子式尺寸变化（而不是"gcd 次数"本身）；
* 两个秩恒定实例（seed 3023、3027）与一个反例点（seed 3003 的 $\theta=0$）作为回归素材。

## 相关文件

- [tools/verification/fast_feasible.py](../../../../tools/verification/fast_feasible.py)
- [tools/verification/bezout_rank_test.py](../../../../tools/verification/bezout_rank_test.py)
- [workspace/q1_false/feasibility_geometry/attempts/47_x_vs_xsp.md](47_x_vs_xsp.md)
- [workspace/for_expert/07_programme_report_and_open_problems-answer.md](../../../for_expert/archive/07_programme_report_and_open_problems-answer.md)（§6 的"有限析取"）
