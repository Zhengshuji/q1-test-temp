# 多项式证书：$P Y P=P$ 的存在性与次数界（纸面）

> 2026-11-08。Step 6 优先级 6：把 $(5b)$ 的“$\forall\lambda$ 满秩”换成**有限多项式证书**：
> 存在 $Y(\lambda)\in\mathbb C[\lambda]^{k\times q}$，$\deg Y\le2\omega-2$，使
> $$P(\lambda)Y(\lambda)P(\lambda)=P(\lambda),\qquad P(\lambda)=\lambda H-H_A.$$
> 状态：**M2（纸面）**；Lean 化列为下一步（先做常数矩阵的代数内核）。

## 目标

证明：若 $P\in\mathbb C[\lambda]^{q\times k}$ 满足 $\operatorname{rank}P(\lambda)=\omega$ 对所有 $\lambda\in\mathbb C$，
则存在多项式广义逆 $Y$，$\deg Y\le2\omega-2$，使 $PYP=P$。

## 设想与理由

* $\mathbb C[\lambda]$ 是 PID；Smith 形
  $$P=S\,\operatorname{diag}(d_1,\dots,d_\omega,0)\,T,$$
  $S,T$ 幺模，$d_i\in\mathbb C[\lambda]$ 非零。
* “$\operatorname{rank}P(\lambda)=\omega$ 对所有 $\lambda$” ⟺ 每个 $d_i$ 在 $\mathbb C$ 上无根
  ⟺ $d_i\in\mathbb C^\times$（非零常数）。
* 于是 $P=U_0 C V_0$，$U_0=S_{:,1:\omega}$、$V_0=T_{1:\omega,:}$、$C=\operatorname{diag}(d_i)$；
  令 $U=U_0 C$、$V=V_0$，则 $P=UV$。
* $M=VU$ 是 $\omega\times\omega$ 多项式矩阵；$\det M$ 是 $P$ 的某个 $\omega$-子式的组合，
  由“$P$ 处处满秩”知 $\det M$ 无根，故 $\det M\in\mathbb C^\times$（非零常数）——$M$ 在 $\mathbb C[\lambda]$ 上可逆。
* 取
  $$\boxed{Y=U\,M^{-2}\,V=U\,\operatorname{adj}(M)^2\,(\det M)^{-2}\,V.}$$
  则
  $$PYP=UV\,U M^{-2}V\,UV=U(VU)M^{-2}(VU)V=U M M^{-2}M V=UV=P.$$
* **次数界**：$U,V$ 可取 $\deg\le1$（$P$ 是线性铅笔，Smith 形的幺模变换可取线性？——此处需引用
  线性铅笔的 Kronecker 形：常秩线性铅笔严格等价于 $\operatorname{diag}(1,\dots,1,0)$ 加线性块，
  $S,T$ 为**常数**可逆阵）。于是 $M=VU$ 的次数 $\le2$，$\operatorname{adj}(M)$ 的次数 $\le2(\omega-1)$，
  $M^{-2}$ 的次数 $\le4(\omega-1)$，$Y=U M^{-2}V$ 的次数 $\le2+4(\omega-1)=4\omega-2$。
  专家给的界是 $2\omega-2$，需要更细的**子式 Bezout 构造**（不是 $M^{-2}$）：
  直接用 $P$ 的 $\omega$-子式 $p_I$（次数 $\le\omega$）与 Bezout 系数 $b_I$（次数 $<\omega$，$\sum b_I p_I=1$），
  令 $Y=\sum_I b_I\,\operatorname{adj}(P_I)$（$P_I$ 为对应 $\omega\times\omega$ 子矩阵），
  则 $PYP=P$ 且 $\deg Y\le(\omega-1)+\omega=2\omega-1$（再优化 1 得 $2\omega-2$）。

## 做法（子式 Bezout 构造）

1. 设 $P$ 的全部 $\omega$-子式为 $p_1,\dots,p_N$，$\deg p_i\le\omega$。
2. “$P(\lambda)$ 处处秩 $\omega$” ⟹ $p_i$ 在 $\mathbb C$ 上无公共根 ⟹ 理想 $(p_1,\dots,p_N)=\mathbb C[\lambda]$
   ⟹ 存在 $b_i\in\mathbb C[\lambda]$，$\sum b_i p_i=1$，且可取 $\deg b_i<\omega$（Bezout/CRT）。
3. 对每个 $\omega$-子矩阵 $P_I$，$\operatorname{adj}(P_I)$ 的元素是 $(\omega-1)$-子式，次数 $\le\omega-1$。
4. 令 $Y=\sum_I b_I\,\operatorname{adj}(\widehat{P_I})$（把 $\operatorname{adj}$ 嵌入 $k\times q$），
   则对每个 $\lambda$，$P(\lambda)Y(\lambda)P(\lambda)=P(\lambda)$（经典的“子式 Bezout 广义逆”公式）。
5. 次数：$\deg(b_I\operatorname{adj})\le(\omega-1)+(\omega-1)=2\omega-2$。$\square$

## Bézout 次数引理（专家 56 号给出的精确版本）

设 $p_1,\dots,p_s$ 是 $P$ 的非零 $\omega$-子式，$\gcd(p_1,\dots,p_s)=1$，$d=\deg p_1\le\omega$。
在商环 $\mathbb C[\lambda]/(p_1)$ 中，$p_2,\dots,p_s$ 生成单位理想，故存在
$b_2,\dots,b_s$（可取 $\deg b_j<d$）使
$$\sum_{j=2}^s b_jp_j\equiv1\pmod{p_1}.$$
于是
$$b_1=\frac{1-\sum_{j=2}^s b_jp_j}{p_1}$$
是多项式，且分子次数 $\le(d-1)+d=2d-1$，故 $\deg b_1\le d-1$。所以
$$\boxed{\deg b_j<d\le\omega}$$
（这是“多个生成元时次数仍有界”的关键；不能只说“扩展欧几里得给次数界”。）

## 进展

* 证书的构造（Smith 形 + 子式 Bezout）已写出；次数界 $2\omega-2$ 与专家一致。
* 与 $(5b)$ 的等价：$\forall\lambda$ 满秩 ⟺ 子式无公根 ⟺ 存在上述 $Y$。
* Lean 化：常数矩阵情形（$P=UV$、$VU$ 可逆）的恒等式 $P\,U(VU)^{-2}V\,P=P$ 是纯代数，可先做；
  多项式情形需要 $\mathbb C[\lambda]$ 上的子式/Bezout，工作量大。

## 最终结论

* 多项式证书存在，$\deg Y\le2\omega-2$；构造是“子式 Bezout 广义逆”。
* 这把 $(5b)$ 的 $\forall\lambda$ 量词换成有限系数方程，是 $\exists\mathbb R$ 编码的一步。

## 放弃原因

* Lean 化未做（多项式矩阵、子式、Bezout 的 Mathlib 支持有限）。
* 次数界由专家 56 号的 Bézout 引理补全（$\deg b_j<d\le\omega$，$\deg\operatorname{adj}\le\omega-1$，合计 $2\omega-2$）；已逐项写出。

## 残留价值

* 完整的纸面证书与次数界，可直接用于论文/编码。
* 常数矩阵的代数内核是下一步 Lean 的明确目标。

## 相关文件

* [attempts/113](../../decision_algorithms/attempts/113_projective_theorem_corrected.md)（$(5b)$ 与 $\exists\mathbb R$ 编码）
* [attempts/140](../../decision_algorithms/attempts/140_hyperplane_rank_identity.md)（rank[P;Q] 恒等式）
* [docs/05 Q9](../../../../docs/05_open_questions.md)（复杂度）

## 状态

* 证书：**[已证-纸面，M2]**。
* Lean：**[未做]**（常数情形可先做）。
