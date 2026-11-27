# 399 层程序 ↔ Paper II 的 $W$-表述：字典成立，但消不掉参数

> 承接 398（统一形式 + "一次判定"的障碍）。按路线 B 试：用 Paper II 的 $W$ 语言消掉 $\exists D$。

## 目标

1. 把定理 1 的 $D$（不变 $c$-子空间）与 Paper II 的 $U=\pi_1(W)$ 对齐；
2. 看能否因此在 $W$-语言里**消掉**"层的枚举"。

## 设想与理由

Paper II 的可行性判据用的是 $W=\operatorname{row}(V\mathsf M)$（$\mathsf M=[N\ AN]$）与
$\pi_2(W)\subseteq\pi_1(W)$、$\dim\pi_\lambda(W)$ 恒定。若我的 $D$ 就是 $\pi_1(W)$ 的零化子，
那么"(5a)"与"$\pi_2\subseteq\pi_1$"应是同一条件，层号也应是 $U$ 的余维——于是层的枚举可能只是
$D$-参数化的产物。

## 做法与核对（`c400`，三例全对）

字典：

$$\boxed{\ U:=\pi_1(W)=\operatorname{row}(VN)\subseteq K^*,\qquad D=\ker H=U^{\perp_K},\qquad c=k-\dim U\ }$$

| 例子 | $q$ | $\omega=\rank H$ | $c$ | $\dim U$ | $D=U^{\perp_K}$? | $(5a)\iff\pi_2\subseteq\pi_1$ | $M(D)\subseteq D$ |
|---|---|---|---|---|---|---|---|
| $c=2$ 可行设计（$D=\operatorname{span}\{e_1{+}e_2,e_3\}$） | 3 | 2 | 2 | 2 | ✓ | ✓ | ✓ |
| $c=1$ 强制设计（$D=e_1$） | 3 | 3 | 1 | 3 | ✓ | ✓ | ✓ |
| 随机 4 行（一般位置） | 4 | 4 | 0 | 4 | ✓ | ✓ | ✓ |

三个量都对上：$D=U^{\perp_K}$、$(5a)$ 就是 Paper II 的 $\pi_2(W)\subseteq\pi_1(W)$、$c=k-\dim U$。
（$M(D)\subseteq D$ 等价于 $U$ 是 $M^*$-不变。）

## 进展与结论

### 1. 层号的含义被澄清

$$c=k-\omega=k-\dim U=\operatorname{codim}_K U .$$

**层号 = 公共投影 $U$ 在 $K$ 里的余维**。这与 $c=1$ 论文的对偶命题（$[a]=\mathbb P(\operatorname{Ann} U)$）
完全一致，并把那个对偶推广到一般 $c$。

### 2. 层分解是 $D$-参数化的产物，不是问题的必要结构

在 $W$-语言里，可行性是**一个**存在式：

$$\exists W:\quad W_0\subseteq W\subseteq\mathcal T,\quad \pi_2(W)\subseteq\pi_1(W),\quad
\dim\pi_\lambda(W)=\dim\pi_1(W)\ \forall\lambda .$$

$\dim U$ 是 $W$ 的函数，不是独立参数。所以"逐层枚举 $c$"在 $W$-语言里**消失了**——
这正是 Paper II 的写法（它从不分层）。

### 3. 但参数没有消失

$\exists U$ 与 $\exists D$ 是**同一个族**的两面对偶（$D=U^{\perp_K}$、$\dim D+\dim U=k$），
所以"消掉 $D$"只是把它改名为 $U$。族仍然是正维的（$\operatorname{Gr}(c,K)$ 或其对偶），
复杂度问题**没有变化**：它正是 Paper II 留下的开放问题。

### 4. B 的实际收获

1. **概念统一**：层号 = 公共投影的余维；层分解 = 按 $\dim U$ 切分同一个 $W$-族；
2. **交叉验证**：我的 $(5a)$ 判据与 Paper II 的 $\pi_2\subseteq\pi_1$ 是同一条件（三例核对），
   说明 393–394 的几何没有偏离文献的压缩语言；
3. **一个反面结论**：试图借 $W$-语言"消掉 $\exists D$"**不可行**（只是换名）；
4. **附带观察**：Paper II 的结构界 $\omega+1\le\dim W\le2\omega$ 给的是 $\dim W$ 与 $\omega$ 的关系，
   **不能**给 $c=k-\omega$ 一个上界 ⟹ 层号仍然可以大到 $k$（与 397 的"层不单调"一致：不能截断）。

## 最终结论

1. **字典成立**（已核对）：$D=U^{\perp_K}$、$(5a)=\pi_2\subseteq\pi_1$、$c=k-\dim U$；
2. **路线 B 不能消掉参数**：$\exists D$ 与 $\exists U$ 同族对偶，改语言不改复杂度；
3. $q1$ 的缺口**仍然是**"对正维族一次性判定"，即 398 定位的那个缺口；
4. 但要记下 B 的正面收获：层号的含义、与 Paper II 的交叉验证、以及"层号无上界"这一结构性事实。

## 放弃原因

- 没有找到把 $\exists U$ 消成 $(5b)$ 的有限条件的办法（不变量理论方向未展开）；
- 没有把 Paper II 的 $W_0\subseteq W\subseteq\mathcal T$ 与我的 $V_0\subseteq V$ 完整对齐（只对齐了 $U$ 与 $D$）；
- 没有分析"$\dim W$ 与 $q$ 的关系"能否给出层号的界（Paper II 的界只约束 $\dim W$）。

## 残留价值

- **一个经过三例核对的字典**（层号 = 公共投影余维），可作为下一篇论文的"与 Paper II 的关系"一节；
- 明确了**路线 B 不可行**（省得以后再试）；
- $q1$ 的缺口定位不变：正维族的一次性判定。

## 相关文件

- [attempts/398](../../decision_algorithms/attempts/398_unified_exists_theta.md)（统一形式与缺口）
- [attempts/397](397_layer_nomonotone.md)（层不单调）
- [attempts/394](../../decision_algorithms/attempts/394_c2_total_charts.md)（$c=2$ 图卡）、[393](393_c2_fibre_and_base.md)（纤维与底）
- [c400](../../../../tools/verification/c400_layer_paperII_dictionary.py)（字典核对）
