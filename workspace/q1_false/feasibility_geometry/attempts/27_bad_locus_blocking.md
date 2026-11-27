# Type III 的"坏点像"表述：何时一个阶被整族排除

## 目标

把 C4 的证明模板（[attempts/26](26_c4_proof.md)）推广成一般判据，并检验它的结构性后果。

## 设想与理由

$(5b)$ 失败 ⟺ 存在 $\\lambda$ 与 $y\\ne0$ 使 $[\\lambda\\mathcal L-\\mathcal LA;CA;C]y=0$，即
$$y\\in V:=\\ker[C;CA],\\qquad \\lambda y-Ay\\in\\ker\\mathcal L .$$
因此定义**坏点映射**
$$\\Phi:\\ \\mathbb P(V)\\dashrightarrow\\mathbb P(K),\\qquad
x\\mapsto\\operatorname{span}\\bigl((\\lambda(x)I-A)x\\bigr),\\quad \\lambda(x)=\\frac{L_0Ax}{L_0x},\\ K=\\ker[C;L_0],$$
则（取 $\\mathcal Z=\\operatorname{span}z(x)$ 时）$\\lambda(x)x-Ax\\in\\mathcal Z\\subseteq\\ker\\mathcal L$，故 $\\Phi(x)$ 是"坏点"。
于是

$$\\text{阶 }q\\text{ 被整族排除}\\ \\Longleftarrow\\ \\text{每个 }\\mathcal Z\\in\\operatorname{Gr}(d,K)\\ \\text{都含某个坏点}.$$

**维数后果**：$\\mathbb P(V)$ 的维数是 $n-r_1-1$、$\\mathbb P(K)$ 的是 $n-p-r-1$。若
$$r_1\\ >\\ p+r,$$
则 $\\Phi$ 的像维数不足，**不可能**覆盖每个 $d$ 维 $\\mathcal Z$——该阶必有可行候选（就 $(5b)$ 而言）。

## 做法

1. 对 C4（$r_1=p+r=4$）复核：$\\mathbb P(V)$ 与 $\\mathbb P(K)$ 都是 $\\mathbb P^1$，$\\Phi$ 非常数 ⟹ 满射 ⟹ 整族排除；
2. 在"谱区"（整数障碍不适用）的实例上统计：$r_1>p+r$ 的实例是否**全部**在 $q_0$ 阶可行。

## 进展

**C4**：$r_1=4$、$p+r=4$（**恰在阈值上**）、$\\dim V=\\dim K=2$；$\\Phi$ 非常数 ⟹ 满射 ⟹ 整族排除 ✓（已证）。

**谱区实例**（$h_{\\max}<q+r_1$，共 36 个有样本）：

| $r_1$ 与 $p+r$ | 实例数 | 其中 $q_0$ 阶可行 |
|---|---|---|
| $r_1>p+r$ | 3 | **3** |
| $r_1\\le p+r$ | 33 | **33** |

即：谱区的 36 个实例在 $q_0$ 阶**全部**可行（0 个 Type III），与"$r_1>p+r$ 必可行"的充分条件相容，
但 $r_1\\le p+r$ 的 33 个实例也没有出现整族排除——说明"$\\Phi$ 阻断整个族"是**特殊**现象（C4 型）。

## 最终结论

1. **判据形式**：某阶被整族排除 $\\Longleftarrow$ 坏点像 $\\Phi(\\mathbb P(V))$ 阻断 $\\operatorname{Gr}(d,K)$
   （$d=1$ 时等价于 $\\Phi$ 满射）；
2. **充分条件（粗）**：$r_1>p+r$ ⟹ 不可阻断 ⟹ 该阶就 $(5b)$ 必有候选；
3. **C4 恰在阈值 $r_1=p+r$** ——这解释了它为什么能成为反例；
4. 数据支持"阻断是特殊现象"：谱区 36/36 可行。

## 放弃原因

不适用。**未做**：对一般 $(d\\ge2,\\ r_1\\le p+r)$ 判定"$\\Phi$ 是否阻断"的算法
（需要闭包维数与阻断集的计算）。

## 残留价值

* 把 Type III 的判定化为**几何阻断问题**（$\\Phi$ 的像 vs $\\operatorname{Gr}(d,K)$）；
* 给出一个**可计算的充分条件**（$r_1>p+r$ ⟹ 可行），并说明 C4 位于阈值；
* 为后续算法化（闭包维数、阻断数）提供明确对象。

## 相关文件

- [workspace/q1_false/feasibility_geometry/attempts/26_c4_proof.md](26_c4_proof.md)（C4 的证明模板）
- [workspace/q1_false/feasibility_geometry/attempts/24_generic_no_type3.md](24_generic_no_type3.md)（谱区统计）
- [proof/refuted/C4_type3_counterexample.md](../../../../proof/refuted/C4_type3_counterexample.md)
- [proof/h_formula/README.md](../../../../proof/h_formula/README.md)（B.11：$h=s_0+\\dim\\pi(V)$）
