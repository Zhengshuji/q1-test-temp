# 78 号审计更正：$\\omega\\le r$ 未证，$q=4$ 重新开放；FPT 与 $2\\times1$ gadget 保留

> 2026-11-09。78 号审计否定了 282 的核心定理：
> 由 $(5a)$ 只能得到
> $$L_0A\\in\\operatorname{row}[L_0;R;CA;C],$$
> 不能把 $R$ 去掉。因此
> $$H_{A,0}=M_0H_0+M_1Y,$$
> 不一定是 $M H_0$。
> 另外 282 的“相交情形”推理错误：$U\\cap V\\ne0$ 不推出 $U\\subseteq V$。
> 状态：**282/283/284/292/293 降级；288、277、2×1 gadget 保留**。

## 目标

按 78 号审计更正结构性结论。

## 设想与理由

78 号指出 282 的  $H_{A,0}=M H_0$ 不成立；先逐条撤回，再明确保留项。

## 做法：逐条更正

### 1. 282 的 $\\omega\\le r$ 未证

- $L_0A$ 的行可以在 $[L_0;R;CA;C]$ 中，含 $R$ 的贡献；
- 所以 $H_{A,0}=M H_0$ 不成立，特征值掉秩论证不能用；
- 相交情形：$d>0$ 只给 $\\omega=a+b-d\\le a+b-1$，不推出 $\\omega\\le b$。

**结论**：$\\omega\\le r$、吸收性、$q=4$ 不可能性都**未证**。

### 2. 依 282 的推论全部降级

- 283（$q=4,r_0=1$ 二分）依赖 282，降级为未证；
- 284（秩窗口 $\\operatorname{rank}H_0<\\omega<r$）依赖 282，降级；
- 292（$Y_1$ 两难）依赖 284/292 的窗口，降级为“在该参数化内的观察”；
- 293（$q=5$ rank 门收束）只是搜索边界，不是定理。

### 3. 保留的部分

- **288**：$\\operatorname{rank}[N\\ AN]\\le n-p$，因为 $N,AN\\subseteq\\ker C$；正确；
- **逐行提升判据**：
  $$(H_i,H_{A,i})\\in\\operatorname{row}[N\\ AN]$$
  是精确充要条件；
- **277 的 Gram 证书**：核心正确，但需：
  - 系数索引修正：$B_{(i,j),t}=c_{i,t-j}$，
    $$(B^{\\mathsf T}B)_{t,t'}=\\sum_{j=0}^{\\omega-1}S_{t-j,t'-j};$$
  - 分离 $\\omega=0$；
  - 写清比特复杂度。
- **2×1 谱 gadget**：
  $$H=\\begin{bmatrix}1\\\\0\\end{bmatrix},\\quad
  H_A=\\begin{bmatrix}0\\\\f\\end{bmatrix},\\quad
  P(\\lambda)=\\begin{bmatrix}\\lambda\\\\-f\\end{bmatrix},$$
  则
  $$(5b)\\iff f\\ne0.$$
  这是正确的压缩 gadget；但还不是观测器实现，需要过
  $(1,0),(0,f)\\in\\operatorname{row}[N\\ AN]$。

### 4. 谱 gadget 的目标要改

正确目标不是“极大子式 gcd 为标量 $f$”，而是
$$\\text{极大子式在 }\\lambda\\text{ 有公根}\\iff f=0.$$
即参数控制“公根是否存在”，不是公因子。

## 进展

* 撤回 282 及其推论；
* 保留 288、逐行判据、Gram FPT、2×1 gadget；
* 修正谱 gadget 的目标。

## 最终结论

* Route A 的 rank 门回到开放状态；
* 固定 $\\kappa_{\\rm obs}$ 的 FPT 是当前最成熟的主线；
* $2\\times1$ 谱 gadget 是最小模型，下一步是它的逐行实现。

## 放弃原因

* 未修复 282；
* 未实现 2×1 gadget；
* 未写 FPT 的完整比特复杂度。

## 残留价值

* 一次重要的结构定理撤回；
* 明确的保留清单；
* FPT 作为主线的依据。

## 相关文件

* [78 答复](../../../for_expert/archive/78_status_and_rank_bounds-answer.md)
* [attempts/282](../../../q1_false/decision_algorithms/attempts/282_omega_le_r.md)（撤回）
* [attempts/288](../../../q1_false/decision_algorithms/attempts/288_lift_rank_bound.md)
* [attempts/277](../../../q1_false/decision_algorithms/attempts/277_gram_fpt.md)

## 状态

* 更正：**[完成，M3]**。
* 282：**[撤回]**。
