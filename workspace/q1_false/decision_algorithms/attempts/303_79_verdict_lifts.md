> **311 更正**：303C 的正确量词是 $\exists R:\ (5a)\wedge(5b)\iff x\ne0$；对**固定** $R$，$(5b)\iff xv\ne0$（$v=0$ 时失败）。

> **306 更正**：303 B 只是 full-observer realization，不是 sound q1 gadget：$R=0$ 时 $(5a)(5b)$ 仍成立但不约束 $z=xy$。
> 296 与 303 C 仍是 sound；303 B/297/299/300 需 soundness 分析。

# 79 号裁决落实：乘法门可完整提升，输入非零门存在；288 的“永不满射”撤回

> 2026-11-10。79 号给出三个构造，均已用 `c303` 精确验证：
> 1. $3k$ 维通用提升：$[N\ AN]$ 行满秩 $2k$，任意压缩对可提升；
> 2. 完整观测器的乘法门：$(5a)\iff z=xy$，$(5b)\iff\beta\ne0$，故 $\\exists\\beta,w$ 后 $\\iff z=xy$；
> 3. 输入控制非零门：$(5b)\\iff x\\ne0$（$x$ 是 $A$ 的条目，$K_0$ 固定）。
> 同时更正 288：秩界 $\\operatorname{rank}[N\ AN]\\le n-p$ 正确，但“永不满射”是**错误目标**——
> 映射的靶空间是 $2k$ 维，不是 $n$ 维。
> 状态：**M3（专家构造 + 精确验证）**。

## 目标

落实 79 号，并更正 287/288 的提升结论。

## 设想与理由

79 号给出三个显式构造；先逐条用精确计算验证，再更正 287/288 的提升表述。

## 做法：逐条验证

### 1. 通用提升（c303 A）

取
$$\\mathbb R^{3k}=U\\oplus V\\oplus W,\\quad \\dim U=\\dim V=\\dim W=k,$$
$$C=[I_k\\ 0\\ 0],\\qquad
A=\\begin{bmatrix}0&0&I_k\\\\0&0&0\\\\0&I_k&0\\end{bmatrix}.$$
则 $CA=[0\\ 0\\ I_k]$、$K_0=V$、$N=[0;I_k;0]$、$AN=[0;0;I_k]$，
$$[N\\ AN]=\\begin{bmatrix}0&0\\\\I_k&0\\\\0&I_k\\end{bmatrix},\\qquad
\\operatorname{rank}[N\\ AN]=2k.$$
$r\\mapsto(rN,rAN)$ 的靶空间是 $2k$ 维，秩 $2k$ ⇒ **满射**。
任意 $H_0,H_{A,0},Y,Z$ 取
$$L_0=[0\\ H_0\\ H_{A,0}],\\qquad R=[0\\ Y\\ Z],$$
则 $LN=[H_0;Y]$、$LAN=[H_{A,0};Z]$。精确验证 PASS。

### 2. 完整乘法门（c303 B）

$k=3,n=9,p=3$，固定 $A,C$ 同上。取
$$H=\\begin{bmatrix}e\\\\e\\\\v_x\\\\0\\end{bmatrix},\\qquad
H_A=\\begin{bmatrix}0\\\\e\\\\(0,y,z)\\\\(0,\\beta,w)\\end{bmatrix},\\qquad
e=(1,0,0),\\ v_x=(0,1,x).$$
则
$$\\operatorname{row}H=\\operatorname{span}\\{e,v_x\\},$$
$$(5a)\\iff z=xy,\\quad w=\\beta x.$$
在门上
$$P(\\lambda)=\\begin{bmatrix}\\lambda e\\\\(\\lambda-1)e\\\\(\\lambda-y)v_x\\\\-\\beta v_x\\end{bmatrix},$$
前两行总给 $e$ 方向（$\\lambda$ 与 $\\lambda-1$ 不同时为零），后两行给 $v_x$ 方向当且仅当 $\\beta\\ne0$。
所以
$$(5b)\\iff\\beta\\ne0,$$
于是
$$\\boxed{\\exists\\beta,w:\\ (5a)\\wedge(5b)\\iff z=xy.}$$
这是**完整观测器**（$A,C,L_0,R$ 显式）。精确验证 PASS。

### 3. 输入控制非零门（c303 C）

$$C=[0\\ 0\\ 1],\\qquad
A(x)=\\begin{bmatrix}0&0&0\\\\x&0&0\\\\0&1&0\\end{bmatrix},\\qquad
L_0=[1\\ 0\\ 0],\\qquad R=[u\\ v\\ w].$$
$CA=[0\\ 1\\ 0]$，$K_0=\\operatorname{span}(e_1)$、$N=e_1$（与 $x$ 无关），
$$H=\\begin{bmatrix}1\\\\u\\end{bmatrix},\\qquad
H_A=\\begin{bmatrix}0\\\\xv\\end{bmatrix},\\qquad
P(\\lambda)=\\begin{bmatrix}\\lambda\\\\ \\lambda u-xv\\end{bmatrix}.$$
$\\lambda\\ne0$ 时秩 1；$\\lambda=0$ 时秩 1 当且仅当 $xv\\ne0$。所以
$$\\exists R:\\ (5a)\\wedge(5b)\\iff x\\ne0.$$
这是**完整观测器**，且 $K_0$ 固定、$x$ 只在 $AN$ 中。精确验证 PASS。

## 更正 287/288

- **288 的秩界正确**：$\\operatorname{rank}[N\\ AN]\\le n-p$。
- **288 的“永不满射”错误**：映射靶空间是 $2k$，不是 $n$；$3k$ 构造中秩 $2k$，满射。
- **287 的结论对、前提错**：$[N\\ E]$ 满秩（$n$ 维）确实不可能；但“任意压缩对可提升”是对的，
  机制是 $[N\\ AN]$ 行满秩 $2k$，不是 $[N\\ E]$ 可逆。

## 对 299/300 的影响

79 号指出 299 的谱陈述需要非退化条件
$$\\alpha\\beta\\ne0,\\qquad a\\ne y,$$
否则 $\\gcd$ 可能非常数；原 299 的“自动成立”应加这个条件。
完整乘法门（2）用两个固定锚行替换了 $a\\ne y$ 的隐患，因此更稳。

## 组合的剩余问题

79 号明确：
- 一个全局 $A$ 不是主要障碍（通用提升 + 逐行构造 $F$）；
- **块对角 $A,C$ 不强制块对角 $R$**，所以 297 的“直和 = 合取”只对显示的块对角压缩矩阵成立，
  对无限制 $R$ 的 q1 实例不成立（交叉块项可给出 $J$ 型 offset）；
- 真正缺的是**全局 wiring/equality**：同一变量在不同门中重复出现时必须同一值，且不能有意外交叉解。

## 进展

* 三个专家构造全部精确验证；
* 288 的错误表述更正；
* 299 的非退化条件明确；
* 组合问题定位到 wiring/equality。

## 最终结论

* 乘法门与输入非零门都已有**完整观测器实现**；
* 287 的“提升”结论成立，但机制要改写；
* 297 的直和合取不能直接推广到无限制 $R$；
* 下一步是 wiring/equality gadget，而不是再造孤立门。

## 放弃原因

* 未构造 wiring/equality；
* 未证明归约的 soundness/completeness；
* 未接 $\exists\mathbb R$-hardness。

## 残留价值

* 三个可复用的完整构造；
* 一个重要的更正；
* 明确下一目标。

## 相关文件

* [79 答复](../../../for_expert/archive/79_gadget_composition-answer.md)
* [attempts/288](288_lift_rank_bound.md)
* [attempts/299](299_mixed_gate.md)
* `tools/verification/c303_expert_lifts.py`

## 状态

* 专家构造：**[M3 + 精确验证]**。
* wiring/equality：**[未做]**。
