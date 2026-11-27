# 公开例子的失败类型：$q_0$ 与 $q_0+1$ 都是 **Type I**（整数障碍）

## 目标

回答专家 2026-11-03 §Q1 提出的对照问题：

> 文献的两阶差例子，其低阶失败是 Type I（$h\ge q+r_1$）还是 Type III（$h<q+r_1$ 但 $d_{\rm fin}>0$）？
> 若是 Type I，则我们的 C4 反例提供的是**不同机制**，不只是"又一个例子"。

## 设想与理由

公开例子 $n=8,p=r=2,r_1=4,q_0=3$。设 $K=\ker[C;L_0]$（$\\dim4$）、
$S=K^{\\perp}+W=\\operatorname{row}[C;L_0]+\\operatorname{row}[C;CA]$（$\\dim6$），商空间 $\\mathbb C^8/S\\cong\\mathbb C^2$。

$q=3$ 时 $\\mathcal Z\\subseteq K$（$\\dim3$）⟹ $\\mathcal Z^{\\perp}=K^{\\perp}+\\operatorname{span}(v)$（$v\\notin K^{\\perp}$）。
$(5a)$ ⟺ $(\\mathcal Z^{\\perp})A\\subseteq\\mathcal Z^{\\perp}+W=S+\\operatorname{span}(v)$。

关键：在 $\\mathbb C^2$ 中，$\\operatorname{row}C$ 的像的类为 $0$，而 $\\operatorname{row}L_0$ 的像的类为
$$c=(-97/8,\\ -195/4)\\ne0\\quad(\\text{两行同类}) .$$
于是 $(5a)$ 对 $L_0$ 的两行给出 $c\\in\\operatorname{span}(\\operatorname{class}v)$，即 $\\operatorname{class}v\\propto c\\ne0$，
从而 $v\\notin S$，于是
$$h=\\dim(S+\\operatorname{span}v)=6+1=7=q+r_1\\quad\\Longrightarrow\\quad\\textbf{Type I}.$$

## 做法

[fernando_type.py](../../../../proof/fernando_2gap/fernando_type.py)：

1. 算出商空间与类（$c\\ne0$、两行同类）；
2. 把 $(5a)$ 化成 $v$ 的两个**线性**条件（$\\operatorname{class}v\\wedge c=0$、$\\operatorname{class}(vA)\\wedge c=0$），
   解出 $v$（解空间 6 维）；
3. 由 $v$ 构造 $\\mathcal Z^{\\perp}=K^{\\perp}+\\operatorname{span}v$、$\\mathcal Z$ 与**显式**的 3 行增广 $\\mathcal L$；
4. 核验 $(5a)$、$h$、$(5b)$ 与指标数据。

## 进展

```
class(L0_1·A) = class(L0_2·A) = (-97/8, -195/4) ≠ 0
线性条件 rank = 2，解空间维数 = 6
v = (-42919/32067, -55096/10689, 1, 0, 0, 0, 0, 0)
显式 L = [ L0_1 ; L0_2 ; v ]
   (5a) = True；h = 7 = q+r1；q+r1 = 7
   (5b) = False；ε = []；d_fin = 3
```

即：**存在 3 行的 $(5a)$-可行增广**（此前抽样从未找到），而它的 $h=q+r_1=7$，$\\varepsilon=[]$、
$d_{\\rm fin}=3$ ⟹ **Type I**（$m=q+2p-h=0$ ⟹ 无非零左指标 ⟹ $d_{\\rm fin}=s$）。

$q=4$ 的情况：$h=8=q+r_1$（1999/1999 抽样）⟹ 也是 **Type I**（该阶尚未有符号证明）。

## 最终结论

| 例子 | 失败阶 | $h$ 与 $q+r_1$ | 类型 |
|---|---|---|---|
| Fernando 2026 §VII | $q_0=3$ | $h=7=q+r_1$ | **Type I**（已证 + 显式 $L$）|
| Fernando 2026 §VII | $q_0+1=4$ | $h=8=q+r_1$ | **Type I**（1999/1999 抽样）|
| 本项目 C4 反例 | $q_0=3$ | $h=6<7$ | **Type III**（谱障碍）|

⟹ **C4 反例提供的是文献例子没有的机制**：在最小阶上，$h<q_0+r_1$ 却仍失败。

## 放弃原因

不适用（$q_0$ 阶已证；$q_0+1$ 阶的符号证明仍缺，但结论由 1999/1999 支持）。

## 残留价值

* 回答了专家 §Q1 的核心对照问题，并把 C4 的"新"落到了实处；
* 首次给出公开例子在 $q_0$ 阶的**显式** $(5a)$-可行增广（此前抽样 0/2000 未获得）；
* 给出一个可推广的技术：把 $(5a)$ 化成商空间上的线性条件，从而**显式求解**最小阶可行族
  （而不是抽样）——这与 $(5b)$ 无关，但对"最小阶是否可行"的判定是必需的输入。

## 相关文件

- [proof/fernando_2gap/fernando_type.py](../../../../proof/fernando_2gap/fernando_type.py)
- [proof/fernando_2gap/README.md](../../../../proof/fernando_2gap/README.md)
- [proof/refuted/C4_type3_counterexample.md](../../../../proof/refuted/C4_type3_counterexample.md)
- [archive/expert_correspondence/answer_2026-11-03_to_03.md](../../../../archive/expert_correspondence/answer_2026-11-03_to_03.md)（§Q1）
