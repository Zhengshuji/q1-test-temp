# 精确提升完成定理（含固定 $L_0$）：仿射形式与构造

> 2026-11-08。按 00 号复核的 Priority 1，把 151 的判据写成**含固定 $L_0$** 的完整定理：
> 仿射提升空间、兼容方程、$E'_C$ 与 $\mathcal T_V$ 两个版本、构造算法。状态：**M2（纸面）**。

## 目标

给定 $C\in\mathbb C^{p\times n}$（设 $\operatorname{rank}C=p$；否则以 $\operatorname{rank}C$ 代 $p$）、
$L_0\in\mathbb C^{r\times n}$（秩 $r$）、$N=N_K\in\mathbb C^{n\times k}$ 为 $K_0=\ker[C;CA]$ 的基，
以及压缩对 $(H,H_A)\in\mathbb C^{q\times k}\times\mathbb C^{q\times k}$，满足

1. $H_0=L_0N$（顶部 $r$ 行固定）；
2. $\operatorname{rank}H=\omega$，$V=\ker H$；
3. $\ker H\subseteq\ker H_A$（可容许）；
4. $\operatorname{rank}[C;L_0]=p+r$。

求 $L=[L_0;R]$ 使
$$LN=H,\qquad LAN=H_A,\qquad \operatorname{rank}[C;L]=p+q.$$

## 设想与理由

$L^{(0)}$ 为任一满足 $L^{(0)}N=H$、顶部为 $L_0$ 的参考提升（底部行解 $RN=H_1$ 即可）。
所有保持 $H$ 的提升是
$$L=L^{(0)}+G,\qquad G=\begin{bmatrix}0_{r\times n}\\G_b\end{bmatrix},$$
其中 $G_b$ 的行取自 $\operatorname{row}[C;CA]$（这些行湮灭 $K_0$，故 $GN=0$）。

**保持 $H_A$** 需要 $GAN=0$，即 $G_b$ 的行属于
$$\mathcal G'=\{g\in\operatorname{row}[C;CA]:\ gAN=0\}.$$
**只在 $V$ 上兼容**（不保持整对）则只需
$$G_bAN\big|_V=-\big(L^{(0)}AN\big)\big|_V.$$

## 做法

### 定义

$$\Gamma:\operatorname{row}[C;CA]\longrightarrow\mathbb C^{1\times k},\quad g\longmapsto gAN;\qquad
E'_C=\ker\Gamma/\operatorname{row}C,\quad d'_C=\dim E'_C.$$
$$\mathcal T_V:G_b\longmapsto G_bAN\big|_V,\qquad
d'_C(V)=\dim\ker\mathcal T_V\quad(\text{在 }G_b\text{ 的行空间上}).$$
注意 $\mathcal T_V$ 只看 $V$ 上的限制，故 $\ker\mathcal T_V\supseteq\ker\Gamma$，从而 $d'_C(V)\ge d'_C$。

### 定理 A（保持压缩对）

设 $(H,H_A)$ 可提升（存在 $L$ 同时满足 $LN=H$、$LAN=H_A$；等价于 $[H\,|\,H_A]$ 的行在
$\operatorname{row}[N\,|\,AN]$ 中），且 $\operatorname{rank}[C;L_0]=p+r$。则存在底部 $G_b$ 使
$$L=L^{(0)}+G_b\ \text{满足}\ LN=H,\ LAN=H_A,\ \operatorname{rank}[C;L]=p+q$$
**当且仅当**
$$\boxed{q-\omega\le d'_C.}$$

*证明*。取 $\mathbb C^q/\operatorname{row}C$ 中的行类。$q$ 个压缩行在 $K_0$ 上的限制给出 $\overline H:\mathbb C^q\to K_0^*$，
$\ker\overline H^*$ 的维数为 $q-\omega$。每个依赖 $a$ 的提升类落在
$E_C=\operatorname{row}[C;CA]/\operatorname{row}C$；要保持 $H_A$，必须落在 $E'_C$。
顶部行固定，且 $H_0=L_0N$ 满行秩 $r$，故顶部依赖为零（$a_{\rm top}=0\Rightarrow a_{\rm top}^{\mathsf T}H_0=0\Rightarrow a_{\rm top}=0$）；
于是 $\ker\overline H^*$ 到“底部行组合”的投影是单射。底部 $m=q-r$ 行的修正 $g_i\in\mathcal G'$ 实现映射
$$\ker\overline H^*\longrightarrow E'_C,\qquad a\longmapsto\sum_i a_{{\rm bot},i}[g_i].$$
该映射可单射 $\iff$ $q-\omega\le\dim E'_C=d'_C$（取 $g_i$ 使像在 $E'_C$ 中张成所需维数）。
单射 $\iff$ 行类模 $C$ 独立 $\iff$ $\operatorname{rank}[C;L]=p+q$。$\square$

### 定理 B（只在 $V$ 上兼容）

若只要求 $L$ 使 $(5a)$ 在 $V$ 上成立（即 $GAN|_V=-L^{(0)}AN|_V$），而不要求保持整个 $H_A$，则
仿射方程的解集（若非空）是 $G_b^{(0)}+\ker\mathcal T_V$，且存在这样的 $L$ 兼满足
$\operatorname{rank}[C;L]=p+q$ **当且仅当**
$$\boxed{q-\omega\le d'_C(V).}$$
（证明同 A，只是把 $E'_C$ 换成 $\ker\mathcal T_V$。）

### 构造（算法步骤）

1. 选 $H$（$\ker H=V$，顶部 $=L_0N$），取参考提升 $L^{(0)}$（底部解 $RN=H_1$）。
2. 若用定理 A：计算 $E'_C$ 的基 $G'$；用 $L=L^{(0)}+X G'$，选 $X$ 使完成映射单射（解一个线性方程）。
3. 若用定理 B：解仿射方程 $G_bAN|_V=-L^{(0)}AN|_V$，在解空间中选 $G_b$ 使完成映射单射。
4. 回代检验 $(5a)$、$(5b)$（gcd）。

$q=\omega+1$ 时 $q-\omega=1$：定理 A 只需 $d'_C\ge1$，定理 B 只需 $d'_C(V)\ge1$。

## 实现中发现的进一步约束（2026-11-08）

在合成实例上跑 v2 算法（ω=q−1、$W_L$ 优先、仿射方程 + 齐次补秩）时发现：

1. **$H_A$ 不是自由的**：对 $H$ 的每一行 $h$，其提升 $r$ 的 $LAN$ 等于 $hAN$ 加上看不见修正
   $gAN$；而 $g\in\operatorname{row}[C;CA]$ 的修正只落在 $\operatorname{im}\Gamma=\operatorname{span}(CA^2N)$ 方向。
   因此 $H_A$ 的“强制部分”是 $HAN$，$gAN$ 只能改一个方向。可容许性不仅是 $V\subseteq\ker H_A$，
   而是 $V\subseteq\ker(HAN+GAN)$，其中 $GAN$ 受限于 $\operatorname{im}\Gamma$。
2. **顶部行的特征值可造成必坏**：若 $L_0N$ 是 $A$ 的特征向量（$L_0AN=\lambda_0L_0N$），
   则 $P(\lambda_0)$ 的顶部行消失；若其余压缩行在 $\lambda_0$ 不能补足秩，
   且看不见方向都在 $\operatorname{row}[C;CA]$ 内（无法提供 $\lambda_0$ 处的新方向），则该 $V$ 必坏。
   这解释了合成例中 $t=2$、顶部行为特征向量时找不到见证。

**算法含义**：正确管线应把 $H_A$ 写成 $HAN+\Gamma(X)$，先解 $V\subseteq\ker(HAN+\Gamma(X))$ 的线性条件，
再解秩完成；不能把 $H_A$ 当作自由变量。

## 专家 58 号的更强形式（$\Psi$ / $Z_{
m pair}$）

把提升写成单个线性映射 $\Psi:\mathcal X^*/S_C	o K_0^*\oplus K_0^*$、$\Psi(ar g)=(gN,gAN)$；
其核是 $E'_C$（$d'_C=\dim E'_C$）。对给定的压缩对 $z_1,\dots,z_q$，令
$$Z_{
m pair}:\mathbb C^q\longrightarrow K_0^*\oplus K_0^*,\qquad lpha\longmapsto\sum_ilpha_i z_i.$$
则存在保持 $L_0$、独立模 $S_C$ 的提升 $\iff$
$$oxed{d'_C\ge\dim\ker Z_{
m pair}}.$$
在 $(5a)$ 下 $\operatorname{rank}Z_{
m pair}=\omega$，故化为 $q-\omega\le d'_C$。
前提：(i) 每个 $z_i\in\operatorname{im}\Psi$（pair realizability）；(ii) $L_0$ 行独立模 $S_C$。
这个形式把“先数看不见方向”换成“核维数 + 单射扩张”，比定理 A/B 更严格，且给出构造：
在 $\ker Z_{
m pair}$ 上取单射到 $E'_C$，再在补空间任选提升。

## 进展

* 定理 A/B 的陈述与证明已写出（按 00 号复核的框架，含固定 $L_0$）。
* 明确了“可提升”的兼容条件：$[H\,|\,H_A]$ 的行在 $\operatorname{row}[N\,|\,AN]$ 中。
* 两个判据：$q-\omega\le d'_C$（保持整对）与 $q-\omega\le d'_C(V)$（只在 $V$ 上兼容）。

## 最终结论

* 提升完成问题有精确的仿射线性判据，且**固定 $L_0$** 被显式处理；
* $d'_C(V)\ge d'_C$ 说明“只在 $V$ 上兼容”是更弱的条件，算法上可能更优；
* $q=\omega+1$ 的完成只需一维自由度。

## 放弃原因

* 未处理 $C$ 非满行秩的一般情形（用 $\operatorname{rank}C$ 代 $p$，细节未写）；
* 未实现/未精确验证；未 Lean 化。

## 残留价值

* 这是 00 号复核所说的“唯一逻辑瓶颈”的纸面解；
* 可直接接到 $c=2$ 六层参数化（144/143）上，形成完整算法。

## 相关文件

* [attempts/151](../../decision_algorithms/attempts/151_lift_completion_theorem.md)（初版 + $gAN$ 更正）
* [attempts/114](114_lifting_lemma.md)（旧 lifting，仅 $\operatorname{rank}[L_0;R]$）
* [attempts/143](143_c2_rigorous_parameterization.md)（六层参数化）

## 状态

* 定理 A/B：**[已证-纸面，M2]**。
* 一般 $\operatorname{rank}C<p$、实现/验证/Lean：**[未做]**。
