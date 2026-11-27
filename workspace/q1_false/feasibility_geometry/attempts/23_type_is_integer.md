# 失败类型由整数决定：Type I ⟺ $\dim\pi(V)\ge q+r_1-s_0$

## 目标

把"Type I / Type III"的划分从"要算每个增广"降为**只看几个整数**，并给出公开例子三个阶的统一解释。

## 设想与理由

设 $K=\ker[C;L_0]$、$S=\operatorname{row}[C;L_0]+W$（$W=\operatorname{row}[C;CA]$），
$$s_0:=\dim S .$$
任何 $(5a)$-可行增广（$q$ 行、含 $L_0$）都有 $\mathcal Z^\perp=K^\perp+V$，其中
$V=\operatorname{span}(v_1,\dots,v_t)$、$t=q-r$、$V\cap K^\perp=0$。由 B.11
$$h=\dim(\mathcal Z^\perp+W)=\dim(S+V)=s_0+\dim\pi(V),$$
其中 $\pi:\mathbb C^n\to\mathbb C^n/S$。于是

* $h$ **只依赖整数** $\dim\pi(V)$（它落在 $[\,\max(0,(p+q)-s_0),\ \min(t,\ n-s_0)\,]$）；
* $$\boxed{\text{Type I}\iff h\ge q+r_1\iff \dim\pi(V)\ge q+r_1-s_0 .}$$

特别地，当 $V\cap S=0$（即 $\dim\pi(V)=t=q-r$）时
$$\text{Type I}\iff s_0\ \ge\ r_1+r ,$$
**与具体增广无关**——同一阶上整族的失败类型相同。

## 做法

[type_criterion.py](../../../../tools/verification/type_criterion.py)：对 495 个 $(5a)$-可行样本核验
$h=s_0+t$（在 $V\cap S=0$ 的样本上），并统计 Type I / 非 Type I。

## 进展

| 检验 | 结果 |
|---|---|
| $h=s_0+q-r$（$V\cap S=0$ 的样本）| **495/495 一致**（0 例外）|
| Type I 样本 / 非 Type I 样本 | 135 / 360 |

**公开例子三个阶的统一解释**（$s_0=6$、$r_1=4$、$r=2$、$n=8$）：

| 阶 $q$ | $t=q-r$ | $\dim\pi(V)$ 的上界 $\min(t,n-s_0)$ | $h$ | $q+r_1$ | 类型 |
|---|---|---|---|---|---|
| 3 | 1 | $\min(1,2)=1$ | $6+1=7$ | 7 | **Type I** |
| 4 | 2 | $\min(2,2)=2$ | $6+2=8$ | 8 | **Type I** |
| 5 | 3 | $\min(3,2)=2$ | $\le8$ | 9 | **Type I 不可能** ⟹ 由谱条件决定（可行）| 

即：$q=3,4$ 被整数障碍排除（$h$ 顶到 $q+r_1$），$q=5$ 时 $h\le8<9$，整数障碍消失 ⟹ 谱可行 ⟹ $q_{\min}=5$。

## 最终结论

1. **定理（$h$ 的整数化）**：$h=s_0+\dim\pi(V)$，$s_0=\dim(\operatorname{row}[C;L_0]+W)$；
2. **Type I 判据**：$\dim\pi(V)\ge q+r_1-s_0$；当 $V\cap S=0$ 时退化为 $s_0\ge r_1+r$（**与增广无关**）；
3. 公开例子的阶谱有**纯整数解释**：$q\le4$ 被整数障碍挡、$q\ge5$ 才可能；
4. 这也说明"Type I 的阶"是一个**区间**（$q$ 小的时候），而 Type III 只能在 $h<q+r_1$ 的阶上讨论——
   与 C4 反例（$q_0$ 阶即 Type III）相容。

## 放弃原因

不适用。**未做**：把 $\dim\pi(V)$ 的可达集合（在 $(5a)$ 约束下）完整刻画——这决定"整数障碍何时被避开"。

## 残留价值

* 把失败类型判据降为**整数**（$s_0$、$r_1$、$r$、$\dim\pi(V)$）；
* 给出公开例子阶谱的完整整数解释（不需要谱分析）；
* 与 C4 反例一起，构成"两种障碍"的**可判定划分**：先看 $s_0$ 与 $\dim\pi(V)$，再在 $\delta\ge1$ 的阶上做谱判定。

## 相关文件

- [tools/verification/type_criterion.py](../../../../tools/verification/type_criterion.py)
- [proof/h_formula/README.md](../../../../proof/h_formula/README.md)（B.11）
- [proof/fernando_2gap/](../../../../proof/fernando_2gap/README.md)
- [workspace/q1_false/feasibility_geometry/attempts/22_fernando_failure_type.md](22_fernando_failure_type.md)
