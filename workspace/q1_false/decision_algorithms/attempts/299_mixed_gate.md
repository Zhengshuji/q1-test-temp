> **306 更正**：本文件是压缩块；含零自由行，未做 soundness 分析，不能直接称 q1 门。

> **303 补**：79 号指出本文件的谱陈述需要非退化条件 $\alpha\beta\ne0$、$a\ne y$；
> 否则 $\gcd$ 可能非常数。完整乘法门改用两个固定锚行，避免 $a\ne y$ 隐患。

# 混合块：$(5a)$ 强制 $z=xy$，$(5b)$ 自动——但变量仍是见证变量

> 2026-11-10。在 296/297 的非零块之后，尝试“$(5a)$ 等式 + $(5b)$ 非零”的混合块。
> 构造出一个 $q=3,\\omega=2$ 的压缩块：
> $$H=\\begin{bmatrix}1&0&0\\\\0&1&x\\\\0&0&0\\end{bmatrix},\\qquad
> H_A=\\begin{bmatrix}a&0&0\\\\0&y&z\\\\\\alpha&\\beta&w\\end{bmatrix},$$
> 并证明
> $$(5a)\\iff z=xy,\\ w=\\beta x,\\qquad (5b)\\ \\text{在门上自动成立}.$$
> **限制**：$x,y,z,w$ 都是 $L$ 的见证变量，不是输入固定的变量；所以这是一个“条件关系”块，
> 不是硬度门。
> 状态：**M2 + 精确验证（条件关系）**。

## 目标

把非零块与一个等式块组合，得到 $(5a)$ 强制 $z=xy$、$(5b)$ 仍成立的压缩结构。

## 设想与理由

取 $q=3$、$k=3$、$\\omega=2$：
$$h_1=(1,0,0),\\qquad h_2=(0,1,x),\\qquad h_3=(0,0,0).$$
$\\operatorname{row}H=\\operatorname{span}(h_1,h_2)$。若
$$H_{A,2}=(0,y,z),$$
则 $(5a)$ 要求
$$(0,y,z)\\in\\operatorname{span}(h_1,h_2)
\\iff z=xy.$$
这就是一个行列式型的乘法关系。

为了让 $(5b)$ 不掉秩，$H_A$ 的另外两行取
$$H_{A,1}=a h_1,\\qquad H_{A,3}=\\alpha h_1+\\beta h_2.$$
在 $\\lambda=a$ 时第一行消失，但 $H_{A,3}$ 仍有 $\\alpha h_1$ 分量；
在 $\\lambda=y$ 时第二行消失，但 $H_{A,3}$ 仍有 $\\beta h_2$ 分量；
所以铅笔始终秩 2。

## 做法：显式矩阵

$$H=\\begin{bmatrix}1&0&0\\\\0&1&x\\\\0&0&0\\end{bmatrix},\\qquad
H_A=\\begin{bmatrix}a&0&0\\\\0&y&z\\\\\\alpha&\\beta&w\\end{bmatrix}.$$

$(5a)$：$H_{A,1}=a h_1$ 自动；$H_{A,2}\\in\\operatorname{span}(h_1,h_2)$ 给
$$z=xy;$$
$H_{A,3}=\\alpha h_1+\\beta h_2$ 给
$$w=\\beta x.$$
所以
$$(5a)\\iff z=xy,\\ w=\\beta x.$$

在门 $z=xy,w=\\beta x$ 上，
$$P(\\lambda)=\\begin{bmatrix}
\\lambda-a&0&0\\\\
0&\\lambda-y&(\\lambda-y)x\\\\
-\\alpha&-\\beta&-\\beta x
\\end{bmatrix}.$$
它的 $2\\times2$ 子式 gcd 为 1（c299 验证），且 $\\det P\\equiv0$；
所以 $\\operatorname{rank}P=2$ 对所有 $\\lambda$，$(5b)$ 自动成立。

## 验证（c299）

- $\\operatorname{rank}H=2$（$x$ 一般）；
- $(5a)$ 的秩条件等价于 $z=xy$、$w=\\beta x$；
- 在门上，$P$ 的 $2\\times2$ 子式 gcd $=1$；
- $\\lambda=a$ 与 $\\lambda=y$ 处仍秩 2。

## 限制（关键）

$x,y,z,w$ 都是 $L$ 的**见证变量**。对任意 $x,y$，总可以选 $z=xy$ 使 $(5a)$ 成立；
所以这个块不约束输入，只描述“见证变量之间可以满足乘法关系”。
它不能直接作为硬度门：硬度需要变量由输入固定，或至少不能被见证自由选择。

## 进展

* 一个 $(5a)$ 强制乘法、$(5b)$ 自动的压缩块；
* 精确 gcd 验证；
* 明确了“见证变量自由”这一概念障碍。

## 最终结论

* 混合块的代数结构成立；
* 但它不是硬度门：乘法关系发生在见证变量之间；
* 下一步必须解决“变量由输入固定/共享”的问题，否则任何见证都能满足等式。

## 放弃原因

* 未把变量接到输入；
* 未构造硬度归约；
* 未处理逐行提升。

## 残留价值

* 一个可复用的混合块；
* 明确的自由见证障碍；
* 与专家 69 号“free witness obstruction”一致。

## 相关文件

* [attempts/296](../../../q1_true/multiplication_gate/attempts/296_nonzero_gadget_observer.md)
* [attempts/297](../../../q1_true/multiplication_gate/attempts/297_direct_sum_gadgets.md)
* `tools/verification/c299_mixed_gate.py`

## 状态

* 混合块：**[M2 + 精确验证]**。
* 输入固定/硬度：**[未做]**。
