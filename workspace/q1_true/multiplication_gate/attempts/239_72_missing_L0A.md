# 专家 72 号裁决落实：漏掉 $L_0A$ 行——条件门撤回，5 维实例无可行解

> 2026-11-09。专家 72 号指出 234/71 的**根本错误**：$(5a)$ 的 $LA$ 含**两行** $L_0A$ 与 $lA$，
> 而我们的 $M$ 只放了 $lA$，漏了 $L_0A$。补上后：
> $$(5a)\iff b=0,\ d=0,\ c\ne0,$$
> 而在此轨迹上 $(5b)$ 恒失败（$\Delta=c(\lambda^2-\lambda-1)$）。所以该实例**没有任何可行 $L$**，
> 之前的“条件门”与边界见证全部撤回。状态：**M3（专家裁决）+ 精确复核**。

## 目标

落实漏行的更正，撤回无效的门结论，确定正确的 $q=2$ 形式。

## 设想与理由

$(5a)$：$\operatorname{row}(LA)\subseteq\operatorname{row}[L;CA;C]$，其中
$$LA=\begin{bmatrix}L_0A\\lA\end{bmatrix}.$$
$M$ 必须是
$$M_{\rm full}=\begin{bmatrix}L_0A\\lA\\L_0\\l\\CA\\C\end{bmatrix},\qquad
M_0=\begin{bmatrix}L_0\\l\\CA\\C\end{bmatrix},$$
而不是只放 $lA$ 的 5 行矩阵。

## 做法：精确复核

$A$、$C=e_5^*$、$L_0=e_1^*$、$l=(a,b,c,d,e)$。
$S=\operatorname{row}[L_0;CA;C]=\operatorname{span}\{e_1^*,e_2^*,e_5^*\}$，商空间用 $e_3^*,e_4^*$ 表示：
$$u=L_0A\equiv(-1,0),\qquad x=l\equiv(c,d),\qquad v=lA\equiv(-a-c,-b-d).$$
两条件：
$$u\in\operatorname{span}\{x\}\iff c\ne0,\ d=0;$$
$$v\in\operatorname{span}\{x\}\iff b=0.$$
所以
$$\boxed{(5a)\iff b=0,\quad d=0,\quad c\ne0.}$$

### $(5b)$ 在该轨迹上恒失败

$b=d=0$ 时
$$H=\begin{bmatrix}1&0&0\\a&c&0\end{bmatrix},\qquad
H_A=\begin{bmatrix}2&-1&0\\2a+c&-a-c&0\end{bmatrix},$$
$$P=\begin{bmatrix}\lambda-2&1&0\\a\lambda-2a-c&c\lambda+a+c&0\end{bmatrix},$$
唯一可能非零的极大子式
$$\Delta_{12}=c(\lambda^2-\lambda-1).$$
$c\ne0$ ⇒ 有两个复根 ⇒ $\operatorname{rank}P<2$ ⇒ $(5b)$ 失败。

**结论**：
$$\boxed{\text{该 5 维实例不存在满足 }(5a)(5b)\text{ 的 }L.}$$

### 边界见证无效

$l=(0,0,1,1,0)$ 在**完整** $(5a)$ 下：$\operatorname{rank}M_{\rm full}=5$、$\operatorname{rank}M_0=4$，
$(5a)$ **不成立**（精确复核）。所以它不是可行见证。

## 撤回与更正

- 234 的“条件门”只在**漏行**的 $M$ 上成立；它不是观测器门；
- 237 的“$(5a)\iff ad=bc$（在 $(c,d)\ne(0,0)$）”同样漏行，撤回；
- 71/72 的边界见证、$(5b)$ 反例讨论都建立在漏行版本上，已由本条取代；
- 正确的 $q=2$ 形式是
  $$\boxed{u\in\operatorname{span}\{x\},\qquad v\in\operatorname{span}\{x\}}\quad
  (u=[L_0A],\ x=[l],\ v=[lA]\ \text{在 }Q=(\mathbb C^n)^*/S).$$

## 对 anchored 请求的更新

新构造必须同时满足：
1. $\operatorname{rank}M_0=r$ **恒定**（所有参数）；
2. **两行** $L_0A$ 与 $lA$ 都属于 $\operatorname{row}M_0$；
3. 消去固定枢轴块后，残差行列式给出 $z-xy$（Schur 补形式）；
4. 谱用固定非零极大子式守卫。

只测 $lA$ 的行列式（哪怕等于 $ad-bc$）**不能**建立 $(5a)$。

## 进展

* 漏行更正精确复核；
* 5 维实例无可行 $L$；
* 条件门与边界见证撤回；
* 正确的 $q=2$ 商空间形式写出。

## 最终结论

* 234 的门是“漏行矩阵的行列式恒等式”，不是观测器门；
* 该实例整体不可行；
* 下一步必须从**完整的 6 行 $(5a)$**（$L_0A,lA,L_0,l,CA,C$）出发，做恒定秩 + Schur 残差。

## 放弃原因

* 未构造新的完整门；
* 未证 anchored 存在/不存在；
* 未重做 $n\ge6$。

## 残留价值

* 一个决定性的更正（避免在错误门上继续）；
* 正确的 $q=2$ 商空间形式；
* anchored 的四条必要条件。

## 相关文件

* [attempts/234](234_explicit_gate.md)、[237](237_71_verdict.md)（已撤回门结论）
* [72 答复](../../../for_expert/archive/72_conditional_gate_anchored_request-answer.md)
* [proof/refuted R23](../../../../proof/refuted/README.md)

## 状态

* 更正：**[完成，M3]**。
* 新的完整门：**[未做]**。
