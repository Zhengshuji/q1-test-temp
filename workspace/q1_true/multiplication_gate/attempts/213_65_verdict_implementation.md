> **更正（66 号答复，2026-11-09）**：本文件 §4 对专家 6 维模板的否定**撤回**。
> 模板没有错；错误在我们的 $H_A=LAN$ 计算：把列作用 $Ae_i$ 与行作用 $e_i^*A$ 混淆了。
> 用正确的 $A$ 重算，$H_A=(0,e_2,e_1+e_2)$、$\gcd(\lambda^2,\lambda^2-1)=1$，模板通过全部检查。
> 详见 [214](214_66_verdict_template_valid.md)。

# 专家 65 号裁决落实：更正被确认、全局定理加强、模板的不一致

> 2026-11-09。专家 65 号确认 210 的更正（局部泄漏刚性的铅笔步骤不成立），
> 把全局定理加强到 $\omega>0$，给出 $q>\omega$ 必要条件与 $\Delta$ 判据；
> 但所给 6 维可行模板与其自身的 $A,L$ 不一致（H_A 对不上），两种自然链均失败。
> 状态：**M3（更正确认）+ 模板待更正**。

## 目标

落实 65 号答复：确认更正、采纳加强的全局定理与 $q>\omega$、$\Delta$ 判据，核验模板。

## 设想与理由

专家确认反例；并指出：
1. 全局定理可加强为 $A(K_0)\subseteq K_0$、$\omega>0$ ⇒ 不可行（$c=0$ 也包括，唯一例外 $\omega=0$）；
2. 若 $A(V)\subseteq V$ 且 $(5a)$ 成立，则 $H_A=DH$（左因子化），$\Delta:W=\operatorname{im}H\to\mathbb C^q$；
   铅笔好 $\iff$ 不存在 $0\ne w\in W$、$\lambda$ 使 $\Delta w=\lambda w$；
3. 若 $q=\omega$，$\Delta$ 是 $W=\mathbb C^q$ 的自同态，必有特征向量 ⇒ 坏；故 $q>\omega$；
4. 给出 6 维模板（链 $e_2\to e_1\to e_5$）。

## 做法

### 1. 更正确认

210 的反例被独立复核（专家：rank$[C;L]=5=p+q$；我们信里笔误写成 4，已改）。
“局部泄漏刚性 ⇒ 不可行”**撤回**；正确表述：
- 全局 $A(K_0)\subseteq K_0$、$\omega>0$ ⇒ 不可行；
- 局部 $A(V)\subseteq K_0$、$\omega>0$ ⇒ $A(V)\subseteq V$（不含铅笔结论）。

### 2. 全局定理加强

专家指出 $c=0$（$V=0$）也可：$V^\perp=K_0^*$ 非零，左特征向量仍给秩降。
故 205 的正确范围是 **$\omega>0$**（$0<\omega\le k$），唯一例外 $\omega=0$。

### 3. $q>\omega$ 与 $\Delta$ 判据

对 $A(V)\subseteq V$：$\operatorname{row}H_A\subseteq V^\perp=\operatorname{row}H$，故存在 $D$ 使 $H_A=DH$；
$\Delta:W\to\mathbb C^q$ 由 $D$ 在 $W$ 上诱导。铅笔好 $\iff\ker(\Delta-\lambda I)\cap W=0\ \forall\lambda$。
$q=\omega$ 时 $W=\mathbb C^q$，$\Delta$ 有特征向量 ⇒ 坏；故必要 $q>\omega$。

### 4. 模板核验（发现不一致）

专家模板：$n=6$、$C=e_6^*$、$K_0=\operatorname{span}\{e_1,\dots,e_4\}$，
$Ae_1=e_5$、$Ae_2=e_1$、$Ae_3=Ae_4=0$、$Ae_5=e_6$、$Ae_6=0$，
$L_0=e_1^*$、$L=[e_1^*;e_2^*;e_1^*+e_2^*+e_5^*]$，并给出
$$P(\lambda)=\begin{bmatrix}\lambda&-1&0&0\\0&\lambda&0&0\\ \lambda-1&\lambda-1&0&0\end{bmatrix}.$$

**核验结果**：用所给 $A,L$ 计算
$$H_A=LAN=\begin{bmatrix}0&0&0&0\\1&0&0&0\\1&0&0&0\end{bmatrix},$$
与专家写的 $\begin{bmatrix}0&1&0&0\\0&0&0&0\\1&1&0&0\end{bmatrix}$ **不一致**；`check_candidate` 给出 `five_b=False`，
首两列子式为 $\lambda^2,\lambda^2,-\lambda^2$，$\gcd=\lambda^2$（$\lambda=0$ 处秩降）。

两种自然修正也失败：
- 链 $e_1\to e_2\to e_5\to e_6$（$Ae_1=e_2$、$Ae_2=e_5$、$Ae_5=e_6$）：$H_A$ 行 $=e_2,0,e_2$，子式 gcd $\lambda^2$；
- 链 $e_2\to e_1\to e_5$（原文）：$H_A$ 行 $=0,e_1,e_1$，同样 $\lambda^2$。

**结论**：模板的 $P$ 是好的，但没有 $A$（在所列作用/维度下）同时给出该 $P$ 与 $K_0$、$(5a)$。
需要专家更正模板的 $A$ 或 $L$（很可能是链方向/行顺序的笔误）。

### 5. 设计原则（可保留）

- 用**移位链**（quotient 方向 → 泄漏端点），不要把泄漏放在孤立箭头上；
- 链长 ≥2，末端进入泄漏坐标；
- 提升行要包含泄漏坐标（$e_5^*$ 型）；
- 目标仍是“图卡编码算术 + 移位链管谱”。

## 进展

* 210 更正被专家确认（M3）；
* 全局定理加强到 $\omega>0$；$q>\omega$ 与 $\Delta$ 判据采纳；
* 模板核验发现不一致，两种修正均失败；需专家更正。

## 最终结论

* 更正成立；不变子空间 gadget 路线**未死**（专家同意），但模板尚有错误；
* 下一步：把模板的不一致反馈给专家（66 号），并继续按移位链设计。

## 放弃原因

* 未找到与专家 $P$ 匹配的 $A$；
* 未构造算术 gadget。

## 残留价值

* 加强的全局定理与 $q>\omega$ 判据；
* 模板的精确核验（可用于向专家指出笔误）；
* 移位链设计原则。

## 相关文件

* [attempts/210](210_local_leakage_correction.md)（被确认）
* [attempts/205](205_AinvK0_impossible.md)（加强）
* [attempts/211](211_leakage_gadget_attempt.md)（前一次失败）
* [attempts/206](206_lean_pairlift_eigenvector.md)（Lean 内核）

## 状态

* 更正/定理：**[M3（专家确认）]**。
* 模板：**[待更正]**。
