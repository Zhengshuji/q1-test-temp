# 按专家建议的三项推进：闭包更正、两阶差复现、B.9 加强

## 目标

落实专家 2026-11-02 答复的三项优先任务（§12）：

1. 解决"闭包的唯一性 / $\mathrm{cl}=q_0$"；
2. 复现并分析公开的两阶差例子；
3. 尝试把 B.9 加强成结构判据。

## 设想与理由

1. 专家指出：贪心加入 $xA$（而不是其模 $W$ 的剩余类）**不能**推出最小性；并给出 Eq. (16)–(18) 证明
   $\mathrm{cl}=q_0$（在 $\operatorname{row}L_0\cap\operatorname{row}C=0$ 下）。若实现与理论不符，先查实现。
2. 公开例子（$n=8$、$p=r=2$、$\eta=(2,1)$）是唯一已知的"间隔 2"证据，必须能在本项目复现才能继续用 B.9。
3. 专家的加强路线：$\sum\varepsilon\ge$ 非零左指标个数 $=q+r_1-h$，再与 $\sum\varepsilon=s$ 比较。

## 做法

1. 用 [omega_construct.closure](../../../../tools/verification/omega_construct.py) 的贪心闭包；
2. 复现：[proof/fernando_2gap/verify.py](../../../../proof/fernando_2gap/verify.py)（逐元素录入论文的 $A,C,L$ 与 order-5 增广 $\mathcal L_5$）；
3. 加强：[proof/left_index_count/verify.py](../../../../proof/left_index_count/verify.py) 断言
   $q+r_1-s\le h<q+r_1$（当 $(5b)$ 成立）与 $d_{\rm fin}\le s-(q+r_1-h)$（无条件）。

## 进展

**任务 1（闭包）—— 结论：闭包不是最小值，专家的提醒成立。**

公开例子上：$q_0=3$（功能指标算法）但闭包 $=4$。也就是说贪心加入 $xA$ 会**加多行**——
因为 $xA\in U+W$ 不能推出 $xA\in U$。**权威最小维数是 $q_0=\sum_j\eta_j$**。
（更早那 2/12 个"闭包 > Σηⱼ"的实例，是同一现象，不是记账差异。）

**任务 2（复现）—— 成功。**

| 项 | 值 |
|---|---|
| $\mathcal L_5$（论文给）| $(5a),(5b)$ 成立；$h=8,s=5,r_1=4,\varepsilon=[5],d_{\rm fin}=0$ |
| $q=4$ 抽样 20 个代数可行增广 | $(5b)$ 成立 **0** |
| $q=5$ 抽样 40 个 | $(5b)$ 成立 **40** |

⟹ $\nu_{\min}=q_0+2=5$ 复现；"$q_{\min}\in\{\mathrm{cl},\mathrm{cl}+1\}$"被推翻（[C3](../../../../proof/refuted/C3_gap_can_be_two.md)）。

**任务 3（B.9 加强）—— 得到两条不等式，并在 698 个铅笔上验证。**

$$q+r_1-s\ \le\ h\ <\ q+r_1\qquad((5b)\text{ 的必要条件}),\qquad
d_{\rm fin}\ \le\ s-(q+r_1-h)\quad(\text{无条件}).$$

698 个 $(5a)$-可行铅笔（56 个可观测实例 × 闭包/闭包$+1$/闭包$+2$）：全部断言通过
（B.9 触发 92 次，0 反例；$d_{\rm fin}$ 上界 698/698；$(5b)$ 成立者全部满足区间）。

## 最终结论

* 闭包**不能**作为最小值或唯一性依据（专家 §8.1 正确）；$q_0=\sum_j\eta_j$ 才是权威量；
* 专家的两条加强不等式**成立且有数据支持**，其中 $d_{\rm fin}\le s-(q+r_1-h)$ 是无条件的；
* 公开两阶差例子已复现，可作为回归测试；
* 专家 §Q1 表中的"失败三分类"里，**"$0<k_q<s_q$ ⟹ 失败"这一步不成立**：
  论文的 $\mathcal L_5$ 有 $k_q=q+r_1-h=5+4-8=1<s=5$，却满足 $(5b)$。
  正确的表述是：$k_q>s_q$ ⟹ 失败（由 $s\ge k_q$ 的必要条件）；$k_q\le s_q$ 时计数障碍消失，需看具体指标。

## 放弃原因

"把失败解释成 §5.1 的几何机制"（找 $\lambda$ 与 $v\in\mathcal U\setminus\mathcal Z$、$(\lambda I-A)v\in\mathcal Z$）
本轮**未完成**：脚本在候选有理 $\lambda$ 上找不到秩降，说明坏 $\lambda$ 可能是无理/复的，
需要从有限初等因子的多项式出发（或做符号消元）。已删除草稿，记为待办。

## 残留价值

* 三项任务里两项完成、一项部分完成（不等式加强已落实）；
* 对专家 §Q1 分类的一处更正（有反例）；
* 回归测试 `proof/fernando_2gap`；
* 一条明确的待办：从有限初等因子的**多项式**（而非采样 $\lambda$）出发验证几何机制。

## 相关文件

- [proof/fernando_2gap/](../../../../proof/fernando_2gap/README.md)
- [proof/left_index_count/](../../../../proof/left_index_count/README.md)
- [proof/refuted/C3_gap_can_be_two.md](../../../../proof/refuted/C3_gap_can_be_two.md)
- [tools/verification/omega_construct.py](../../../../tools/verification/omega_construct.py)
