> **290 补**：把 289 的样本符号化后，偏移 $\alpha,\beta$ 含 $x^2$ 项（$H_A$ 会变成二次），
> 因此 289 只是单点可行；线性可提升的符号族尚未找到。

# 第一个可提升的 $q=5$ 压缩门（样本点 $x=2,y=3,z=6$）

> 2026-11-09。在 285 的 $q=5$ 门上，找到一组压缩数据，
> 同时满足 $(5a)$、$(5b)$，且每个自由行的 $H_A$ 偏移落在 $\\operatorname{span}(u,v)$ 中
> （对应 $E$ 的两行），因此**逐行可提升**。
> 目前只在样本点 $x=2,y=3,z=6$ 验证；符号族与完整 $A$ 待做。
> 状态：**M2 + 精确验证（单点）**。

## 目标

给 285 的 $z=xy$ 门找一组可提升的 $(H,H_A)$。

## 设想与理由

取 $n=8,k=4$、$N=e_1..e_4$、$E$ 只有两行（秩 2，受 $\\ker C$ 限制）。
自由行
$$H_{A,i}=Y_iM+o_i,\\qquad o_i\\in\\operatorname{span}(u,v),$$
其中 $u,v$ 是 $E$ 的两行；这正是逐行可提升的形式。

## 做法：显式数据

样本 $x=2,y=3,z=6$（满足 $z=xy$）。取
$$M=\\begin{bmatrix}
0&-1&-2&1\\\\
-2&-2&1&1\\\\
-2&1&1&-2\\\\
1&-2&2&1
\\end{bmatrix},\\quad
u=(-1,-2,-1,-2),\\quad v=(-2,-2,-1,2).$$
$H$ 与 $H_A$：
$$H=\\begin{bmatrix}
1&0&0&0\\\\1&0&0&0\\\\1&0&0&0\\\\
0&0&1&2\\\\0&0&3&6
\\end{bmatrix},\\qquad
H_A=\\begin{bmatrix}
1&0&0&0\\\\1&0&0&0\\\\
7/4&0&-3/2&-3\\\\
-1&0&13/2&13\\\\
-3&0&39/2&39
\\end{bmatrix}.$$

## 验证（c289 PASS）

- $\\operatorname{rank}H=2$，$\\operatorname{rank}[H;H_A]=2$（$(5a)$）；
- 每个自由行的偏移 $H_{A,i}-Y_iM$ 都在 $\\operatorname{span}(u,v)$ 中（可提升）；
- $P(\\lambda)=\\lambda H-H_A$ 在 $\\lambda=0,1,2,3,-1$ 处秩 2；
- 全部 $2\\times2$ 子式 gcd $=1$（$(5b)$）。

```
rank H = 2 rank[H;HA] = 2
offset 0 = [7/4,1,1/2,-4] in span(u,v): True
offset 1 = [-1,3,3/2,13] in span(u,v): True
offset 2 = [-3,9,9/2,39] in span(u,v): True
ranks P at 0,1,2,3,-1 = [2,2,2,2,2]
gcd of 2x2 minors = 1
PASS
```

## 进展

* 第一个同时满足 $(5a)(5b)$ 且逐行可提升的压缩门（单点）；
* $E$ 秩 2 的偏移足以修正谱；
* 与 288 的 $\\ker C$ 限制一致。

## 最终结论

* 285 门在样本点可提升；
* 关键是偏移 $o_i\\in\\operatorname{span}(u,v)$ 同时修正 $(5a)$ 与 $(5b)$；
* 下一步是把 $x,y,z$ 符号化，并构造完整 $A,C,L_0$。

## 放弃原因

* 只在单点验证；
* 未符号化 $x,y,z$；
* 未构造完整 $A$。

## 残留价值

* 一个可提升的可行点；
* 偏移 $u,v$ 的设计；
* 下一步的符号化模板。

## 相关文件

* [attempts/285](../../../q1_true/rank_gates/attempts/285_q5_gate_target.md)
* [attempts/288](288_lift_rank_bound.md)
* `tools/verification/c289_liftable_gate.py`

## 状态

* 单点门：**[M2 + 精确验证]**。
* 符号族/完整 $A$：**[未做]**。
