# C4 实例在 $q_0$ 阶**整族不可行**：格拉斯曼层面的证明

## 目标

把 C4 反例从"抽样发现"升级为**证明**：该实例在 $q_0=3$ 阶，**每一个** $(5a)$-可行增广都失败 $(5b)$。

## 设想与理由

数据（[attempts/25](25_type3_not_jordan.md)）显示：C4 在 $q_0$ 阶的可行族是 $\\mathbb P(\\ker[C;L_0])\\cong\\mathbb P^1$ 的**整个**，
且全部失败。要证"整族不可行"，只需证两件事：

**(1) $(5a)$ 在该阶自动成立。** 因为 $h=\\dim(\\mathcal Z^{\\perp}+W)\\le n$，而本实例算得
$$s_0=\\dim(\\operatorname{row}[C;L_0]+\\operatorname{row}[C;CA])=5,\\qquad t=q_0-r=1\\ \\Longrightarrow\\ h=s_0+t=6=n .$$
于是 $\\mathcal Z^{\\perp}+W=\\mathbb C^6$，$(5a)$（即 $(\\mathcal Z^{\\perp})A\\subseteq\\mathcal Z^{\\perp}+W$）对**任意** $\\mathcal Z$ 成立。

**(2) 每个 $\\mathcal Z$ 都有一个"掉秩 $\\lambda$"。** 设 $V=\\ker[C;CA]$（$\\dim2$）。若 $x\\in V$ 满足 $L_0x\\ne0$，
令
$$\\lambda(x):=\\frac{L_0Ax}{L_0x},\\qquad z(x):=(\\lambda(x)I-A)x .$$
则 $Cz(x)=\\lambda Cx-CAx=0$ 且 $L_0z(x)=\\lambda L_0x-L_0Ax=0$，故 $z(x)\\in\\ker[C;L_0]=\\ker(\\mathcal Z^{\\perp})$ 所在的 $K$。
取 $\\mathcal Z=\\operatorname{span}z(x)$（一条直线），则 $(\\lambda(x)I-A)x\\in\\mathcal Z\\subseteq\\ker\\mathcal L$，于是
$$[\\lambda\\mathcal L-\\mathcal LA;\\,CA;\\,C]\\,x=0\\quad\\text{而 }x\\ne0,$$
即 $\\operatorname{rank}Q_{\\mathcal L}(\\lambda(x))<n=h$ ⟹ $(5b)$ 失败。

若映射 $\\varphi:x\\mapsto\\operatorname{span}z(x)$（$\\mathbb P(V)\\to\\mathbb P(K)$）**非常数**，则它（作为 $\\mathbb P^1\\to\\mathbb P^1$
的有理映射，自动延拓为态射）是**满射**，故每个 $\\mathcal Z\\in\\mathbb P(K)$ 都被某个 $x$ 命中 ⟹ 整族失败。

## 做法

直接计算：$V$ 的基取 $(1:t)$，算 $\\lambda(t)$ 与 $z(t)$ 在 $K$ 的基下的坐标。

## 进展

| $t$ | $\\lambda$ | $z$ 的 $K$-坐标 |
|---|---|---|
| $0$ | $17/5$ | $(12/5,\\ 0)$ |
| $1$ | $6$ | $(4,\\ 5)$ |
| $2$ | $5/3$ | $(-4/3,\\ 4/3)$ |
| $-2$ | $3$ | $(4,\\ -4)$ |

至少两个不同的像（如 $[1:0]$ 与 $[1:-1]$）⟹ $\\varphi$ **非常数** ⟹ 满射 ⟹
**每个 $\\mathcal Z$ 都带一个掉秩 $\\lambda$** ⟹ $q_0$ 阶整族失败。

**证书**（[verify_C4_whole_family.py](../../../../proof/refuted/verify_C4_whole_family.py)）：

```
h = s0 + t = 5 + 1 = 6 = n                    ⟹ (5a) 自动（15/15 条直线）
映射像：t=0 → [12/5:0]，t=1 → [4:5]，t=-2 → [4:−4] 等 5 个不同像 ⟹ 非常数 ⟹ 满射
取 Z = span z(x)（t=0）：(5a) ✓、h=6、rank Q(λ)=5 < 6、(5b)=False、d_fin=2
```

## 最终结论

**定理（该实例）**：C4 实例在 $q_0=3$ 阶，每个 $(5a)$-可行增广都满足 $h=6=n$、并在某个 $\\lambda$ 处掉秩，
故 $(5b)$ 全部失败；$q_0$ 不是可行阶。

（配合 [C4](../../../../proof/refuted/C4_type3_counterexample.md) 的既有结论：该实例 $q_{\\min}=4$。）

## 放弃原因

不适用。**未做**：把这个"映射满射性"论证推广成一般判据
（需要对一般的 $(V,K,W,A)$ 判断 $\\varphi$ 是否非常数——这是可判定的，但尚未系统化）。

## 残留价值

* **第一个不依赖抽样的 Type III 例子**（$q_0$ 阶整族不可行，已证）；
* 一个可推广的论证模板：**"$(5a)$ 自动（$h=n$）+ 映射满射 ⟹ 整族失败"**；
* 与 B.11 的 $h=s_0+t$ 结合，可以快速判断"某阶是否被整数障碍挡住"和"谱障碍是否整族"。

## 相关文件

- [proof/refuted/C4_type3_counterexample.md](../../../../proof/refuted/C4_type3_counterexample.md)
- [proof/h_formula/README.md](../../../../proof/h_formula/README.md)（B.11）
- [workspace/q1_false/feasibility_geometry/attempts/25_type3_not_jordan.md](25_type3_not_jordan.md)
- [workspace/q1_false/feasibility_geometry/attempts/23_type_is_integer.md](23_type_is_integer.md)
