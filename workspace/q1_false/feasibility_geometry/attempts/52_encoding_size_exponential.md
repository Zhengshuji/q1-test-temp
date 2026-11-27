# B：编码规模**指数增长**——"$\exists\mathbb R$ 成员性"这条路走不通

## 目标

按专家 §5.2 的警告（最大子式个数 $N$ 可能组合爆炸），实测 $N$、图卡数、层数随 $n$ 的增长，
判断"子式/Bézout 表示"是否是多项式规模。

## 设想与理由

固定 $p=r=1$、取受控阶 $q=\lfloor n/2\rfloor$（于是 $d\approx n/2-1$、$\dim V=n-r_1$、典型 $r_1=2$），
则：

* $P_{\mathcal Z}$ 是 $n\times\text{ncols}$，$\text{ncols}=\dim V+d\approx 1.5n-3$；
* 极大子式尺寸 $s=\min(n,\text{ncols})=n$（当 $n\ge6$）；
* $$N=\binom{n}{s}\binom{\text{ncols}}{s}=\binom{1.5n-3}{n};$$
* 图卡数 $\binom{k}{d}=\binom{n-2}{\lfloor n/2\rfloor-1}$。

## 做法

[scale_measure2.py](../../../../tools/verification/scale_measure2.py)：只数结构量（无需消元）。

## 进展

| $n$ | $q$ | $d$ | ncols | $s$ | $D$ | 图卡数 | 层数 | $N$ | $\log_2 N$ | $\log_2 N/n$ |
|---|---|---|---|---|---|---|---|---|---|---|
| 6 | 3 | 2 | 6 | 6 | 4 | 6 | 6 | 1 | 0.0 | 0.00 |
| 8 | 4 | 3 | 9 | 8 | 6 | 20 | 8 | 9 | 3.2 | 0.40 |
| 10 | 5 | 4 | 12 | 10 | 8 | 70 | 10 | 66 | 6.0 | 0.60 |
| 12 | 6 | 5 | 15 | 12 | 10 | 252 | 12 | 455 | 8.8 | 0.74 |
| 16 | 8 | 7 | 21 | 16 | 14 | 3 432 | 16 | 20 349 | 14.3 | 0.89 |
| 20 | 10 | 9 | 27 | 20 | 18 | 48 620 | 20 | 888 030 | 19.8 | 0.99 |
| 24 | 12 | 11 | 33 | 24 | 22 | 705 432 | 24 | 3.86e7 | 25.2 | 1.05 |
| 28 | 14 | 13 | 39 | 28 | 26 | 1.04e7 | 28 | 1.68e9 | 30.6 | 1.09 |

**$\log_2 N/n$ 从 0.40 单调升到 1.09**（趋向常数 $\approx1.1$）⟹ $N$ 随 $n$ **指数增长**（底数约 $2^{1.1}\approx2.1$）。
图卡数 $\binom{n-2}{\lfloor n/2\rfloor-1}$ 同样指数（$n=28$ 时已 $10^7$）。

## 最终结论

1. **子式/Bézout 表示不是多项式规模**：$N=\binom{1.5n-3}{n}$ 指数增长，图卡数也指数增长；
2. 因此**"$\mathrm{DEC}(q)\in\exists\mathbb R$"不能由这条路建立**——专家 §5.2 的警告被实测证实；
   要说 $\exists\mathbb R$ 成员性，必须先给出**紧凑表示**（他列的四种可能之一：显式生成元结构 /
   线性组合 + 结式 / 保留铅笔矩阵的隐式表示 / 抽象框架）；
3. 同时也说明：任何多项式算法**不可能**通过"枚举图卡 × 枚举极大子式"实现——必须利用结构
   （例如秩分层本身的多项式描述、或 $(\star)$ 的秩等式在**隐式**矩阵上的判定）；
4. 这**不**回答"$q_{\min}$ 是否 NP-hard"，但它把"上界"这条线收窄了：朴素代数表述的规模是指数的。

## 放弃原因

不适用（测量完成）。**未做**：紧凑表示的构造（专家列的四种可能都未试）。

## 残留价值

* 一张**定量的规模表**（$n=6..28$），可直接回答"编码规模多大"；
* 明确的否定结论：朴素子式表示指数 ⟹ $\exists\mathbb R$ 成员性**未建立**；
* 对算法设计的约束：不能枚举图卡/子式，必须走隐式或结构化的判定。

## 相关文件

- [tools/verification/scale_measure2.py](../../../../tools/verification/scale_measure2.py)
- [docs/08_results.md](../../../../docs/08_results.md) §5（$\exists\mathbb R$ 的 caveat 已按此更新）
- [workspace/for_expert/07_programme_report_and_open_problems-answer.md](../../../for_expert/archive/07_programme_report_and_open_problems-answer.md)（§5.2）
- [proof/dec_q_existsR/bitsize.md](../../../../proof/dec_q_existsR/bitsize.md)（此前只数了变量与次数，未数 $N$）
