# 607 非平凡 $(5a)$：$H_A=HZ'+G$ 分解，秩 1 逃逸被阻断

> 2026-11-27。按 606 的方向，取 $AN\ne NZ'$，得到一般分解，并分析秩 1 逃逸。
> 状态：**[已证-纸面]**。

## 一般分解

设 $P$ 是沿 $\operatorname{im}N$ 的投影（左逆），令
$$Z'=P\,AN,\qquad W=(I-NP)\,AN\ \ (\text{像在}\ \operatorname{im}N\ \text{之外}),$$
则 $AN=NZ'+W$，于是
$$H_A=LAN=HZ'+\underbrace{LW}_{=:G}.$$

$G=L W$ 是“固定行 + 自由行”经 $W$ 的像；$W\ne0$ 时 $G\ne0$，$(5a)$ 非平凡。

## 具体例子

$n=5$、$N$ 为前 3 坐标、$A e_1=e_4$、$A e_2=e_2$、$A e_3=e_3$。
则 $Z'=\operatorname{diag}(0,1,1)$、$W=[e_4,0,0]$，故
$$G=L W=(L e_4)\,e_1^{\mathsf T}=g\,e_1^{\mathsf T},\qquad g=L e_4 .$$

## 秩 1 逃逸分析

设 $H=u v^{\mathsf T}$，$H_A=u w^{\mathsf T}+g e_1^{\mathsf T}$（$w=Z'^{\mathsf T}v$）。

$(5a)$：对 $x\in v^{\perp}$，
$$H_Ax=u(w\cdot x)+g(e_1\cdot x)\overset{!}{=}0 .$$
- 若 $e_1\notin v^{\perp}$（即 $v_1\ne0$）：$e_1\cdot x$ 随 $x$ 变化，需 $g\parallel u$ 且系数逐点匹配——
  一般 $g$ 不平行于 $u$，故失败；
- 若 $v_1=0$：需 $w\cdot x=0$ 对所有 $x\in v^{\perp}$ ⇒ $w\parallel v$ ⇒ $v$ 是 $Z'$ 的左特征向量。

所以秩 1 的 $H$ 只有在 **$v_1=0$ 且 $v$ 是 $Z'$ 左特征向量** 时才可能满足 $(5a)$——这是低维特例，一般被阻断。

## 结论

- $W\ne0$ 时，全局秩 1 逃逸不再自动成立；
- 但秩 1 仍可能在特殊 $v$ 上存活，需要进一步排除（例如选 $Z'$ 使左特征向量都有 $v_1\ne0$，
  且 $g$ 不平行于任何 $u$）。

## 下一步

1. 选 $Z'$ 使所有左特征向量的第一坐标非零；
2. 计算两块实例的最小秩（数值搜索 $H$ 的秩 2/3 解）；
3. 若 $\min\operatorname{rank}H\ge2$，再谈“每块贡献 1”的可靠编码。

## 状态

- 分解与秩 1 分析：**[已证-纸面]**；
- 两块最小秩：**[未做]**。
