# 673 $D_d$ 与“秩 $<2d$ 但可解”的实验

> 2026-11-27。用 [673_Dd_experiment.py](673_Dd_experiment.py) 检查 672 的“满秩充分条件”与退化层的可解性。
> 状态：**[精确验证]**（有限随机抽样，仅作观察，不作定理）。

## 实验

$d=2$、$q=k=3$、$H=\operatorname{diag}(1,1,0)$。对随机整数 $Z\in\{-2,\dots,2\}^{3\times3}$（300 组），
构造 $P=\lambda H-ZH$、2-子式族 $f_i$、$M\in\mathbb C^{4\times2m}$，检查
$$\operatorname{rank}M\ \text{与}\ \operatorname{rank}[M\mid e_0].$$

**结果**：
- 638 的 $Z$：$m=3$，$\operatorname{rank}M=4$，可解 ✓；
- 其余 300 组中，**没有**出现 $\operatorname{rank}M<4$ 且可解的样例（0 例）。

另用随机秩 2 的 $H$（3×3，200 组中 26 个秩 2）配随机 $Z$：同样 **0 例**“秩 $<4$ 且可解”。

## 观察

在这个小族里，“$(5b)$ 成立”似乎总伴随 $\operatorname{rank}M=2d$（满秩）。
若这一现象普遍成立，则 672 的满秩条件就不是“充分但非必要”，而是**等价**（在 $d=2$、$m\ge2$ 时）。

**但这只是抽样，不能当定理**：641B 的 $M$ 秩为 2 且不可解，说明秩 $<2d$ 的层确实存在，只是没找到可解点；
也可能存在更巧的 $Z$ 使秩 3 且可解。

## 待证/待查

1. 是否存在 $d=2$、$\operatorname{rank}M=3$、$e_0\in\operatorname{col}M$ 的实例？
2. 若不存在，能否证明“$d=2$ 且 $m\ge2$ 时，$e_0\in\operatorname{col}M\Rightarrow\operatorname{rank}M=4$”？
3. 661 的 $m=1$ 是退化层的极端（无 $2d$-子式），其不可行性已由 $\det P$ 非常数解释。

## 状态

- 实验：**[精确验证]**（有限抽样）；
- “满秩 ⇔ 可解”：**[猜想]**。
