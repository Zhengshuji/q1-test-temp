# 谱区（整数障碍不适用）的统计：**1501/1501 全部可行**，Type III 为 0

> **2026-11-03 更正**：本文把 Type III 归因于"$A$ 的谱退化（重复特征值/Jordan 块）"是**错的**。
> 扰动实验（$A+t\cdot\operatorname{diag}(1..6)$，$t=1,2,5$，特征值互异）**不能**消除 C4 的 Type III
> （115/115 仍失败）。正确的对照是"谱退化集在可行族上是否 = 全集"：C4 是全集、随机实例是空集。
> 见 [attempts/25](25_type3_not_jordan.md)。

## 目标

上一轮把失败类型降为整数：**Type I 不可能**当且仅当
$$s_0+\min(t,\,n-s_0)<q+r_1,\qquad s_0=\dim(\operatorname{row}[C;L_0]+W),\ t=q-r .$$
本档筛出这种"谱区"的 $(\\text{实例},q)$ 对，看**谱条件是否总是成立**。

## 设想与理由

若在谱区里 $(5b)$ 总是成立，那么"$q_{\min}$"就完全由整数决定（第一个让整数障碍消失的阶），
$q1$ 也就基本解决（至少对这类实例）。反之，若谱区里也有失败（Type III），那 Type III 才是真正的难点。

## 做法

[spectral_regime.py](../../../../tools/verification/spectral_regime.py)：
89 个功能可观测实例（$n=5,6,7$、$p,r\\in\\{1,2\\}$、10 seed），在 $q=q_0$ 处：

1. 算 $s_0,r_1,t$ 与 $h_{\\max}=s_0+\\min(t,n-s_0)$，判"整数区"（$h_{\\max}\\ge q+r_1$）还是"谱区"；
2. 谱区内用 $Z$-参数化抽 60 个候选，筛 $(5a)$，判 $(5b)$。

## 进展

| 项 | 数 |
|---|---|
| 实例 | 89 |
| 整数区（Type I 可能）| 22 |
| **谱区（Type I 不可能）** | **67** |
| 谱区样本（$(5a)$-可行）| **1501** |
| 其中 $(5b)$ 成立 | **1501** |
| 其中 Type III（$h<q+r_1$ 但 $d_{\\rm fin}>0$）| **0** |

典型行（谱区）：

| 实例 | $q_0$ | $s_0$ | $r_1$ | $t$ | $h_{\\max}$ | $q+r_1$ | 样本 | 成功 |
|---|---|---|---|---|---|---|---|---|
| 7/2/1 seed 3005 | 1 | 3 | 3 | 0 | 3 | 4 | 56 | **56** |
| 7/2/2 seed 3000 | 4 | 5 | 4 | 2 | 7 | 8 | 57 | **57** |
| 7/2/2 seed 3003 | 2 | 4 | 3 | 0 | 4 | 5 | 56 | **56** |

## 最终结论

1. **在随机整数实例上，谱区里 $(5b)$ 恒成立**（1501/1501，0 例外）——
   即 **整数障碍是"一般实例"的唯一障碍**；
2. 这与 C4 反例形成鲜明对照：C4 的实例（$A$ 含三个 $2\\times2$ Jordan 块、重复特征值）在谱区仍失败（Type III）。
   而结构化族里 45 个谱区样本中有 17 个 Type III；
3. 因此 Type III 是**非一般**现象，与 $A$ 的谱退化（重复特征值 / Jordan 结构）相关——
   这与专家 2026-11-03 §Q1 的措辞（"frequently observed in the tested structured families"）一致，
   而本档把它加强为：**在随机实例里它不出现**；
4. 推论（经验陈述，未证）：对**一般**实例，
$$q_{\\min}=\min\{q:\ s_0+\min(q-r,\ n-s_0)\ge q+r_1\ \text{不成立}\},$$
即"第一个整数障碍消失的阶"——这对一般实例是**纯整数判定**。

## 放弃原因

不适用。**未证**：上述"一般实例"陈述；以及 Type III 与谱退化的必然联系（只知相关）。

## 残留价值

* 一个**定量二分**：随机实例（1501 样本）里 Type III 为 0；结构化实例里为 17/45；
* 若"一般实例"陈述能被证明（例如用 Sard/横截性），$q_{\\min}$ 对一般实例就能纯整数计算——
  这是目前离 $q1$ 最近的路线；
* 明确把难例（$A$ 有重复特征值）单独分离出来。

## 相关文件

- [tools/verification/spectral_regime.py](../../../../tools/verification/spectral_regime.py)
- [workspace/q1_false/feasibility_geometry/attempts/23_type_is_integer.md](23_type_is_integer.md)
- [proof/refuted/C4_type3_counterexample.md](../../../../proof/refuted/C4_type3_counterexample.md)
- [tools/verification/type3_structured.py](../../../../tools/verification/type3_structured.py)（结构化族的 17/45）
