> **已撤回（239/专家 72 号）**：本文件的 $(5a)$ 轨迹建立在漏掉 $L_0A$ 的 reduced 矩阵上；完整 $(5a)$ 下该实例无可行 $L$。$(5b)$ 的参数条件仍对 reduced 版本成立，但不再是观测器结论。

# 专家 71 号裁决落实：门的精确 $(5a)$ 轨迹、$(5b)$ 非自动、锚定方向

> 2026-11-09。专家 71 号指出 234/71 的三处实质错误，并用精确反例更正：
> （1）$\det M=ad-bc$ 只是条件等式，需 $(c,d)\ne(0,0)$；
> （2）$(5b)$ **不是**对所有 $L$ 自动，chart 上有显式反例；
> （3）$ad-bc=0$ 不可约，$a=0$ 是其切片的两分量；$l=(0,1,0,0,0)$ **不可行**。
> 状态：**M3（专家裁决）+ 精确复核**。

## 目标

逐条落实更正，确定门的正确地位与下一步。

## 设想与理由

专家给出精确的 $(5a)$ 轨迹与 $(5b)$ 参数条件；我们用 `c237_gate_audit.py` 全部复核。

## 做法：逐条更正

### 1. $\det M=ad-bc$：正确，但 $(5a)$ 需条件

$M_0=[L_0;l;CA;C]$ 的秩：
$$\operatorname{rank}M_0=\begin{cases}4,&(c,d)\ne(0,0),\\3,&(c,d)=(0,0).\end{cases}$$
因此
$$\boxed{(5a)\iff
\begin{cases}ad=bc,&(c,d)\ne(0,0),\\ a=b=0,&(c,d)=(0,0).\end{cases}}$$
即可行轨迹
$$\mathcal F_{5a}=\{ad=bc,\ (c,d)\ne(0,0)\}\ \cup\ \{a=b=c=d=0\}.$$

### 2. chart $a=1$ 上还要求 $y\ne0$

$l=(1,x,y,z,0)$ 时，$(5a)\iff z=xy$ **且** $(y,z)\ne(0,0)$；在 $z=xy$ 上即 $y\ne0$。
所以 chart 不含 $y=0$ 的解（如 $x=0,y=0,z=0$）。

### 3. $(5b)$ 不是自动的

压缩：
$$H=\begin{bmatrix}1&0&0\\a+b&c&d\end{bmatrix},\qquad
H_A=\begin{bmatrix}2&-1&0\\2a-b+c&-a-c&-b-d\end{bmatrix},$$
$$P=\begin{bmatrix}\lambda-2&1&0\\ \lambda(a+b)-2a+b-c&\lambda c+a+c&\lambda d+b+d\end{bmatrix}.$$
子式：
$$\Delta_{12}=c\lambda^2-(b+c)\lambda-(b+c),\quad
\Delta_{13}=(\lambda-2)(b+d(\lambda+1)),\quad
\Delta_{23}=b+d(\lambda+1).$$
精确 $(5b)$ 条件（rank-two 部分）：
$$\boxed{(5b)\iff
\begin{cases}
b\ne0,&d=0,\\
b^2c+b^2d+3bcd+cd^2\ne0,&d\ne0.
\end{cases}}$$

**反例（已验证）**：
- $(a,b,c,d,e)=(1,0,1,0,0)$：$(5a)$ 成立、$(5b)$ 失败（$\lambda^2-\lambda-1$ 的根）；
- $(1,-5,1,-5,0)$：$(5a)$ 成立、$(5b)$ 失败（公根 $\lambda=-2$）。

### 4. 分支与见证的更正

- $ad-bc=0$ 是**不可约**的秩一簇；$a=0$ 切片 $\{bc=0\}$ 才有两分量；
- $l=(0,1,0,0,0)$ **不是** $(5a)$ 见证（$\operatorname{rank}M=4$、$\operatorname{rank}M_0=3$）；
- 真正的边界见证：$l=(0,0,1,1,0)$，$a=0$、$\operatorname{rank}H=2$、$(5a)(5b)$ 都成立。
  所以“强迫 $\operatorname{rank}H=2$”**不能**消除 $a=0$ 分支。

### 5. 门的正确地位

- 这是一个**条件行列式门**（$(c,d)\ne(0,0)$ 时 $(5a)\iff ad=bc$）；
- 不是 sound 归约：completeness（$y=0$ 缺失、$(5b)$ 反例）与 soundness（$a=0$ 边界）都失败；
- 但它是“$(5a)$ 可以编码双线性关系”的**真证据**。

## 下一步（专家建议的顺序）

1. **保留条件引理**：$(c,d)\ne(0,0)\Rightarrow(5a)\iff ad=bc$；不要写成无条件等价；
2. **固定枢轴**：把 residual determinant 做成
   $$\det\begin{bmatrix}1&x\\y&z\end{bmatrix}=z-xy,$$
   其中 $1$ 由 $A,C,L_0$ 固定，而不是 $L$ 的自由坐标；
3. **一致谱守卫**：用一个固定的非零极大子式（移位链的 $(-1)^\omega$），而不是泛型 gcd；
4. **完整见证提取定理**：所有可行 $L$ 都要解码，所有 $(x,y,z)$ 都要能构造 $L$；
5. 单门 sound+complete 后再做变量共享/电路。

## 进展

* 三处更正全部复核（`c237_gate_audit.py` PASS）；
* 精确 $(5a)$ 轨迹与 $(5b)$ 参数条件；
* 明确下一步是“固定枢轴 + 一致谱守卫”。

## 最终结论

* 234/71 的“$(5b)$ 自动、$a=0$ 伪见证”说法撤回；
* 门仍是“条件门”，但这是通往 anchored 门的正确起点；
* 不应继续在当前 5 维构造上调 $a\ne0$，应换固定枢轴架构。

## 放弃原因

* 未构造固定枢轴门；
* 未证 soundness/completeness；
* 未做电路。

## 残留价值

* 精确的 $(5a)/(5b)$ 条件（可复用）；
* 真边界见证（说明 rankH 不管用）；
* 明确的 anchored 设计目标。

## 相关文件

* [attempts/234](234_explicit_gate.md)（已更正）
* [attempts/71 答复](../../../for_expert/archive/71_explicit_gate_branches-answer.md)
* [tools/verification/c237_gate_audit.py](../../../../tools/verification/c237_gate_audit.py)
* [for_expert/71](../../../for_expert/archive/71_explicit_gate_branches.md)

## 状态

* 更正：**[完成，M3]**。
* 固定枢轴门：**[未做]**。
