# 411 专家 109 号审计：可实现性要补维数不等式；II.5 的有理图卡**撤回**

> 送审件 [109](../../../for_expert/archive/109_c2_package.md)（已归档），答复
> [109-reply](../../../for_expert/archive/109_c2_package-reply.md)。
> 总评："real advance over 108"，**$W\mapsto\Phi(W)$ 的像约化是"strongest new result"、应作为项目中心**；
> 但两处必须修：**(1)** 可实现性缺**精确维数不等式**；**(2)** II.5 的有理主分解图卡**不成立**。

## 目标

1. 落实他的两处必修 + 六处措辞/假设收紧；
2. 把他给的 **Theorem 3（精确可实现性）** 与 **Theorem 4（约化可行性判据）** 补成正式陈述与证明；
3. 撤回 II.5 的"一般有理图卡"声明，改成"几何描述（$\mathbb Q$-定义）"与"算法（单谱有限分类）"两条分开。

## 设想与理由

他的两条修正是**实质**的：

- 我原来只写"可实现性是线性的（$\Phi_0\subseteq\Phi\subseteq\varphi(T)$ + 维数记账）"——**维数记账没写**，
  而它决定了哪些 $\Phi$ 能被 $t$ 维 $W$ 实现，不是装饰；
- II.5 里我用"$\ker f(M)$ + $[v]\mapsto\operatorname{span}\{v,Mv\}$"声称覆盖一般情形，
  他给了两个反例：**Jordan 块**（$\operatorname{span}\{e_1,e_2\}\subseteq J_3(a)$ 不在 $\ker(M-aI)$ 里）、
  **三次不可约因子有三个实根**（两条实特征直线之和不是 $\mathbb Q$-点）。

## 做法

逐条对照他 §8 的修订表与 §9 的定理层级，先补定理，再改各卷宗的陈述。

## 进展

### A. 两处必修（这是本轮的核心）

**定理 3（精确可实现性；专家 §2.2）.** 设 $\varphi:T\to D^\circ$ 线性、$W_0\subseteq T$、
$\Phi_0:=\varphi(W_0)$、$w_0=\dim W_0$，$\bar\varphi:T/W_0\to D^\circ/\Phi_0$ 为诱导映射。
给定子空间 $\Phi\subseteq D^\circ$，存在 $W$ 满足
$$W_0\subseteq W\subseteq T,\quad \dim W=t,\quad \varphi(W)=\Phi$$
当且仅当

$$\boxed{\ \Phi_0\subseteq\Phi\subseteq\varphi(T),\qquad
\dim\Phi-\dim\Phi_0\ \le\ t-w_0\ \le\ \dim\ker\bar\varphi+\dim\Phi-\dim\Phi_0.\ }$$

*证明.* 令 $S:=W/W_0\subseteq T/W_0$，则 $\dim S=t-w_0$ 且 $\bar\varphi(S)=\Phi/\Phi_0$。
($\Rightarrow$) 显然 $\Phi/\Phi_0\subseteq\bar\varphi(T/W_0)$；$\dim S\ge\dim\bar\varphi(S)=\dim(\Phi/\Phi_0)$；
$S\subseteq\bar\varphi^{-1}(\Phi/\Phi_0)$ ⟹ $\dim S\le\dim\ker\bar\varphi+\dim(\Phi/\Phi_0)$ ✓。
($\Leftarrow$) 取 $S_0\subseteq\bar\varphi^{-1}(\Phi/\Phi_0)$ 使 $\bar\varphi(S_0)=\Phi/\Phi_0$、$\dim S_0=\dim(\Phi/\Phi_0)$
（取一组原像即可），再在 $\bar\varphi^{-1}(\Phi/\Phi_0)$ 内扩到维数 $t-w_0$（上界保证可行）；
$S:=S_0\oplus(\text{扩展部分})$，$W$ 为 $S$ 在 $T$ 中的原像 ✓。$\square$

（另记：$\dim\ker\bar\varphi+\dim\Phi-\dim\Phi_0=\dim T-w_0-\rank\varphi+\dim\Phi$。）

**定理 4（约化可行性判据；专家 §6.1）.** 记 $P_D(\lambda):=\lambda H_K-(H_A)_K$、
$r_D(\lambda):=\dim\operatorname{row}P_D(\lambda)$、$\omega=\rank H$。则对固定的 $D$：

$$\exists W\ (W_0\subseteq W\subseteq T_D,\ \dim W=t)\ \text{使 }(5b)\iff
\exists\Phi\subseteq D^\circ\ \text{满足定理 3 且}\ \dim\bigl(\operatorname{row}P_D(\lambda)+\Phi\bigr)=\omega\ \ \forall\lambda,$$

后者等价于

$$\dim\Phi-\dim\bigl(\Phi\cap\operatorname{row}P_D(\lambda)\bigr)=\omega-r_D(\lambda)\quad\forall\lambda.$$

*证明.* 由像约化（$W$-消去）$\operatorname{row}(\lambda H-H_A)=\operatorname{row}P_D(\lambda)+\Phi(W)$；
再用 $\dim(A+B)=\dim A+\dim B-\dim(A\cap B)$ ✓。$\square$

**这两条就是专家 §9 的 Theorem 3 与 Theorem 4**，现在有了完整证明。

### B. $c=2$ 的正确结论：**至多一个射影直线分量**

原写"坍缩到至多一条 $\mathbb P^1$"。正确说法（专家 §2.3）：有效 $\Phi$ 空间是
$\{0\}\cup\mathbb P(D^\circ)\cup\{D^\circ\}$ 的**子集**，由 $\Phi_0$、$t$、$\varphi(T_D)$ 决定：

| $\dim\Phi_0$ | 可能的 $\Phi$ |
|---|---|
| 0 | $\{0\}$、任一过原点的直线（$\mathbb P^1$）、$D^\circ$ |
| 1 | 只有 $\Phi_0$ 本身，或 $D^\circ$ |
| 2 | 只有 $D^\circ$ |

再加 $\Phi\subseteq\varphi(T_D)$ 与定理 3 的维数不等式，可能进一步缩小。
**所以"至多一个射影直线分量"，不是"总有一条 $\mathbb P^1$ 可用"。**

### C. 一处必须补的限定：$\deg_s\le1$ 只对**像直线参数化**成立

专家 §5.1：$\deg_s m_i\le1$ 成立，**前提是图卡参数化的是像直线** $\Phi(s)=\operatorname{span}(\phi_0+s\phi_1)$
（此时**只有一行**随 $s$ 变，而极大子式对行是多线性的）；若直接参数化 $W$，可能有多行随 $s$ 变，
次数界不成立。**这是像约化定理给出的性质，不是原 Grassmannian 纤维的通用性质**——论文必须写明。

### D. II.5 的撤回（专家 §4）

我原来声称"用 $\mathbb Q$-主分解 $\ker f(M)$ + $[v]\mapsto\operatorname{span}\{v,Mv\}$ 覆盖一般情形"。
**不成立**，两个反例：

1. **Jordan 块**：$M=\begin{pmatrix}a&1&0\\0&a&1\\0&0&a\end{pmatrix}$，$D=\operatorname{span}\{e_1,e_2\}$ 不变，
   但 $D\not\subseteq\ker(M-aI)=\operatorname{span}\{e_1\}$；若改用广义主分量 $\ker f(M)^r$，
   也**不是**每个 2-平面都不变；
2. **$\deg f\ge3$ 且全实根**：对应的不变子空间含"两条实特征直线之和"，这些**不必是 $\mathbb Q$-点**；
   而算法判的是**实**点（不是有理点），所以有理参数化不覆盖所有实分量。

**改为两条分开**（专家 §4.3）：

- **目标 A（几何描述）**：$\mathcal I_2(M)=\{D:M(D)\subseteq D\}$ 由 $\mathbb Q$-多项式方程定义——
  这给出 $\mathbb Q$-模型，但**不**声称每个实分量都被有理参数化；
- **目标 B（算法）**：按 $M|_D$ 的实 Jordan 型分层，或在定义方程上用实代数方法。
  **对 $c=2$ 的单谱定理，只需要单谱的有限分类**（$\binom{k_{\mathbb R}}{2}+$共轭对数），
  不需要解决非单谱的参数化。

### E. II.3 的三处收紧（专家 §3）

1. **UFD**：坐标环不一定是 UFD。限定为**有理图卡** $A=F[x_1,\dots,x_d]_S$（多项式环的局部化），此时是 UFD；
2. **满秩假设过强**：正确的是"**某个**极大子式在 $x$ 处保持其一般 $\lambda$-次数"，
   等价（铅笔情形）于 $\rank H(x)=\omega$。理由：$\operatorname{lc}(G)(x)=0$ 会迫使**所有**
   $\operatorname{lc}(m_i)(x)=0$，所以只要一个保持次数即可；
3. **闭性要按固定次数陈述**：$\{\deg\gcd\ge d\}$ 的闭性应在**固定次数**的轨迹上（或用齐次化），
   否则首项系数消失导致的次数下降会让朴素陈述出问题；
4. 建议拆成**三条引理**（UFD 下的整除性、满秩点的次数保持、Zariski 稠密给实点）。

### F. 其余裁决

| 项 | 裁决 |
|---|---|
| II.1(a)(b) | ✓ 正确（保留；把逻辑依赖写显式：先给完整等价，再推 Grassmann 描述） |
| II.4(i)(ii) | ✓ 在行约定下正确（$W$ 行是 $-\varphi_w$，符号不影响行空间）；**要加一句** $K_0^*\simeq\mathbb R^k$ 的坐标识别 |
| II.2 | 大体正确；**主分类改以单谱情形为主**，多重 Jordan 块不要暗示完整分类 |
| II.6 | 架构 ✓；但**位复杂度未证**：需（i）$D$ 的精确表示（特征值/向量可能是代数数）、(ii) 高度多项式增长、(iii) $\rank\varphi/\Phi_0/$不等式的精确判定、(iv) $\mathbb Q(s)[\lambda]$ 上 gcd 的复杂度、(v) 实图卡有效性。"一个 gcd"不是位复杂度界 |
| II.7 | 只作研究纲领（不是已证的推广）；**$\lfloor c^2/4\rfloor$ 比 $O(c^2)$ 更准** |
| 命名 | 新定理应叫 **Split-layer image reduction theorem**，并注明**不**适用于非 split 设计 |

### G. 研究优先级（专家 §10）

1. **补完消去定理**（可实现性不等式 + 约化判据 + 行空间恒等式的一般矩阵证明）；
2. **补完 $c=2$ 算法**（限单谱、代数数表示、gcd 的多项式界、实图卡与秩条件）；
3. **修一般底几何**（用定义方程，或用实 Jordan 型分层；分开几何与算法）；
4. **Q-B**（研究移动行空间 $\operatorname{row}P_D(\lambda)$ 与 $\Phi$ 的交互）。

## 最终结论

1. **像约化被确认为项目中心**（"strongest new result"），并升级为三条定理（像约化、精确可实现性、约化可行性）；
2. **两处必修已补**：定理 3（维数不等式）与定理 4（约化判据），都有完整证明；
3. **II.5 撤回**：有理主分解不覆盖一般情形（Jordan 块 + 三次因子两个反例），改为"几何描述/算法"两条；
4. **II.3 收紧**：UFD 图卡、$\rank H(x)=\omega$ 的可接受点、固定次数的子结式；
5. $\deg_s\le1$ 只对像直线参数化成立，必须写明；
6. $c=2$ 只能说"至多一个射影直线分量"。

## 放弃原因

- 没有补 II.6 的**位复杂度**（专家列了五项，本轮只确认了架构）；
- 没有给"行空间恒等式的一般矩阵证明"（仍只有纸面 + 单卡核对）；
- 没有处理 Q-B。

## 残留价值

- **定理 3 与定理 4 的完整证明**（专家 §9 的 Theorem 3/4）；
- **II.5 的撤回与替代方案**（几何描述 vs 算法分层），并指出"单谱定理不需要一般参数化"；
- 一套**精确的措辞规范**（split-layer 命名、像直线参数化、至多一个 $\mathbb P^1$ 分量、$\rank H(x)=\omega$）；
- $\lfloor c^2/4\rfloor$ 这个更准的界。

## 相关文件

- 专家问答：[109 与回复](../../../for_expert/archive/)
- 卷宗：[405](405_real_generic_point.md)（判据）、[406](../../c_stratification/attempts/406_eliminate_W.md)（像约化）、[407](407_effective_charts.md)（图卡，已撤回）、[408](../../c_stratification/attempts/408_c2_complexity.md)（复杂度）、[410](../../c_stratification/attempts/410_general_c.md)（一般 $c$）
