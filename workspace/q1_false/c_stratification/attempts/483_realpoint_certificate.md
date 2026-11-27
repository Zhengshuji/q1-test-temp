# 483 实点证书定理：$V(\mathbb R)$ 中的点**确实**给出真实的实数观测器设计

> 承接专家对 482 的修正：3D 的正确目标是 **$V(\mathbb R)\ne\varnothing$**（原始设计允许实矩阵），
> $\mathbb Q$-点只是**构造性证书**。本文件给出对应定理，并写清适用范围（**只给充分性**）。

## 目标

1. 建立 $p\in V(\mathbb R)\Rightarrow$ 真实实数设计（经 (FW)）；
2. 区分 (Q)(ℝ)(ℂ) 三个命题与其蕴含方向；
3. 明确本定理**不**声称"所有可行设计都在 $V$ 内"。

## 做法

把 (FR) 的充分性、(R) 的秩条件、481 引理 B 第一部分的 Bézout 清分母、以及 (FW) 的提升串起来；点域用三条单向蕴含处理。

## 进展

（见下文定理与其证明。）

## 设想与理由

三个命题只有单向蕴含：
$$\text{(Q)}\ V(\mathbb Q)\ne\varnothing\ \Longrightarrow\ \text{(R)}\ V(\mathbb R)\ne\varnothing\ \Longrightarrow\ \text{(C)}\ V(\mathbb C)\ne\varnothing,$$
反向不成立（$V(x^2-2)$：$\mathbb Q$-点空、$\mathbb R$-点非空；$V(x^2+1)$：$\mathbb C$-点非空、$\mathbb R$-点空）✓。
所以"找不到有理点"**不能**推出"没有实数设计" ✗；而 $V(\mathbb C)\ne\varnothing$ 也**不能**推出实数设计存在 ✗。

## 定理（实点证书，充分性）

设
- $\mathcal B$ 为某不可约参数分支（Grassmann 卡坐标 $X,Y$ 上的 $\mathbb Q$-局部闭集），
- $\mathcal B_R=\{\operatorname{rank}X_1=\omega\}\cap\mathcal B$，
- $D\in R\setminus\{0\}$ 为 481 引理 B 中清分母所得（第一部分用它做 Bézout 清分母），
- $V=\mathcal B_R\cap\{D\ne0\}$。

> **定理.** 若 $p\in V(\mathbb R)$，则在该 $p$ 处由 (3A) 得到的 $\mathcal U=\mathcal U(p)$ 满足 (R) 与 (E)，
> 从而由 (FW) 充分性存在**实**自由行 $R\in\mathbb R^{m\times n}$（$m\ge\dim(\mathcal U/\mathcal W_0)$）使层 $\omega$ 可行；
> 若 $p\in V(\mathbb Q)$，则 $R$ 可取**有理**，且自由行可由有理坐标显式提升得到。

*证明.*
1. $p\in\mathcal B_R$ ⟹ $\operatorname{rank}X_1(p)=\omega$ ⟹ 由 3B（[480](480_grassmann_parameterization_of_FW.md)）得 (R) $\pi_1(\mathcal U)=W$ ✓；
2. $D(p)\ne0$ ⟹ 由 481 引理 B 第一部分的 Bézout 清分母恒等式 $D=\sum_J A_Jf_J$，在 $p$ 处得
   $\sum_J A_J(p)f_J(p)=D(p)\ne0$ ⟹ 特化后的最大子式**生成单位理想** ⟹ 无公共复根 ⟹ (E) $\operatorname{rank}P(\lambda;p)=\omega\ \forall\lambda$ ✓；
3. 由 (FW)（[479](479_fixed_W_with_row_budget.md)）充分性：取适配 $\mathcal W_0$ 的基，把 $\dim(\mathcal U/\mathcal W_0)=t\le m$ 个元素实现为自由行并补零 ⟹ 得到设计 ✓；
4. 若 $p$ 有理解，则 $\mathcal U$、其基、以及每个 $(rN,rAN)$ 的提升都可取有理 ⟹ $R$ 有理 ✓（$\mathcal S=\operatorname{row}[N\ AN]$ 的定义给出行 $r$）。$\square$

## 适用范围（必须写死的三条）

1. **只给充分性**：$p\in V(\mathbb R)\Rightarrow$ 可行；**不**声称所有可行设计都落在 $V$ 内 ✗
   （特殊点、其它秩层、其它卡都可能另有可行点）；
2. **$V(\mathbb R)=\varnothing$ 不推出不可行** ✗：这只说明该证书路线在该分支上失效；
3. **"层可行"的层级不同**：本定理给的是**固定 $W$、固定 $\mathcal U$** 的可行；整层的判定仍需 $\exists W$ 与 $\exists\mathcal U$。

## 最终结论

1. **实点证书定理成立**（充分性），且 $\mathbb Q$-点给出可构造的有理见证 ✓；
2. 三个点域命题的蕴含方向与两个反例写清（$x^2-2$、$x^2+1$）✓；
3. 3D 的正确目标据此改为 **$V(\mathbb R)\ne\varnothing$**，而 $\mathbb Q$-点是**更强的证书**（可精确输出）✓；
4. **未解决**：$V(\mathbb R)$ 何时必然非空（这是整条链的最后关口）。

## 放弃原因

- 没有给出 $V(\mathbb R)\ne\varnothing$ 的可判定条件；
- 没有处理 $V(\mathbb R)$ 非空但无 $\mathbb Q$-点的情形（如 $x^2-2$ 型）；
- 没有做例外集（$D=0$）分析（留给 484）。

## 残留价值

- **实点证书定理**及其证明（把 3A/3B/481引理B第一部分/(FW) 串起来）；
- 三个点域命题的蕴含图与两个标准反例；
- 明确"充分性、非必要性"的边界。

## 下一步（484）

例外集分析：$Z=\mathcal B_R\cap\{D=0\}$ 上，公共因子可能在特化时降次 ⟹
重启秩分层 + gcd 判定；要回答"泛型不可行是否等于整个分支不可行"（专家指出：**不等于**）。

## 相关文件

- [482](482_stage3D_realpoints.md)（被修正：$\mathbb R$ 而非 $\mathbb Q$）
- [481](481_pencil_gcd_and_specialization.md)（引理 B，已补分母条件）
- [480](480_grassmann_parameterization_of_FW.md)（3A/3B）
- [479](479_fixed_W_with_row_budget.md)（(FW)）

## 状态

- 实点证书定理：**[已证-纸面]**。
- $V(\mathbb R)\ne\varnothing$ 的判定：**[未做]**。
- 例外集分析：**[未做]**（484）。
