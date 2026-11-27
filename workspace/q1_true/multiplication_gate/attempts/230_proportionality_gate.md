# (5a) 行列式门（二）：比例型门的额外子式与结构错配

> 2026-11-09。尝试用“商空间比例”实现锚定门：
> $lA\in\operatorname{span}\{R,l\}$，在商空间 $Q=X/R$ 中 $l\mapsto(1,x)$、$lA\mapsto(y,z)$，
> 则比例条件给出 $\det[[1,x],[y,z]]=0\iff z=xy$。精确计算发现：$l$ 的 $R$-分量会带来额外子式。
> 状态：**精确计算（负结果）**。

## 目标

构造一个 $(5a)$ 门，使子式理想恰为 $\langle z-xy\rangle$。

## 设想与理由

取 $R=\operatorname{span}\{L_0,CA,C\}$，商空间 $Q=X/R$。
若 $l$ 在 $Q$ 的像是 $(1,x)$、$lA$ 的像是 $(y,z)$，则
$$lA\in\operatorname{span}\{R,l\}\iff (y,z)\parallel(1,x)\iff z=xy.$$

## 做法

取 $n=6$、$C=e_6^*$、$L_0=e_3^*+e_4^*$、
$$A\text{ 的行}: -e_1^*,\ 0,\ 0,\ e_1^*,\ e_2^*,\ e_5^*,$$
$l=(1,x,1,1+y,z,0)$。则 $lA=(y,z,0,0,0,0)$、$Q=\operatorname{span}\{e_1,e_2\}$。

计算 $M=[lA;L_0;l;CA;C]$ 的 $5\times5$ 子式：
$$z-xy,\qquad y^2,\qquad yz.$$
即 $(5a)$ 的条件是 $z=xy$ **且** $y^2=yz=0$，不是单纯的门。

### 原因

$lA$ 的 $R$-分量为零，而 $\lambda l$ 的 $R$-分量为 $\lambda(1,1+y,z)$；
用 $R$ 的行去消，需要
$$-\lambda\cdot1,\ -\lambda(1+y),\ -\lambda z$$
同时落在 $\operatorname{span}\{L_0,CA\}$ 中；
$L_0=e_3+e_4$ 只给 $e_3,e_4$ 的**相等**组合，于是出现 $y^2=0$。

## 结论

* 比例型门在 $l$ 含 $R$-分量时必然带额外方程；
* 若把变量放在 $R$ 外，则 $lA$ 无法产生对应的商分量（$A$ 是线性的）；
* 因此需要**不同**的门实现：固定枢轴 + 秩条件（Schur 补的行列式），而不是商空间比例。

## 进展

* 精确算出额外子式 $y^2,yz$；
* 定位结构错配（$R$-分量 vs 商分量）；
* 明确下一方向：枢轴块 + Schur 补的**行列式**，不是比例。

## 最终结论

* 比例型 $(5a)$ 门不可行（至少在这个最小设置下）；
* 需要 Schur 补/固定枢轴，使唯一的可变子式是门。

## 放弃原因

* 未构造 Schur 枢轴；
* 未证 soundness；
* 只测了 $n=6$、$q=2$。

## 残留价值

* 一个明确的失败机制；
* 对“比例 vs 行列式”的区分；
* 为 Schur 设计提供教训。

## 相关文件

* [attempts/229](229_gate_seed.md)
* [attempts/228](228_68_69_verdict.md)
* [for_expert 68/69 answer](../../../for_expert/archive/68_69-answer.md)

## 状态

* 负结果：**[精确计算]**。
* Schur 门：**[未做]**。
