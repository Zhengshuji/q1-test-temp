# 327 三分的实测：第 3 类（根随 $v$ 移动）真实存在

> 承接 326 的三分表与 c334 的核对。本文件在 $B=\mathbb P^2$ 的实例上把三分**测出来**。
> 验证：[c335](../../../../tools/verification/c335_lambda_movement.py)。

## 目标

判定：$\Lambda(v)=\{\lambda:\dim\{u\in K_0:(\lambda I-A)u\in\operatorname{span}(v,Av)\}\ge2\}$
随 $v$ 的行为属于哪一类（固定根 / 有限覆盖 / 真移动）。这决定 325 的 S3 能否用有限检查代替。

## 设想与理由

要让 $v$ 真的动起来，需要 $\dim B\ge1$。取 $r_0=0$（无固定行），则 $B=\mathbb P(K_0)=\mathbb P^2$。
$q=3$、$m=3$、$n=5$，故 $k=3$、$\omega=2$（超平面层）。$A$ 取整数矩阵（c335 里列出）。

对每个 $v$：$U(v)=\operatorname{span}(v,Av)$，$Q$ 为 $U^\perp$ 的基，$M(\lambda)=Q(\lambda I-A)N$（$3\times3$）；
$\Lambda(v)$ 取 $M$ 的 $2$-子式 gcd 的零点。**同时**用直接构造的 $L$（3 行张满 $U^\perp$）算
$\lambda H-H_A$ 的 $2$-子式 gcd 作对照。

## 做法与结果

10 个随机 $v\in K_0$（全部 $\dim U=2$、$\operatorname{rank}H=2$、$(5a)$ 成立）：

| 检查 | 结果 |
|---|---|
| $\gcd_M$ vs $\gcd_{\text{pencil}}$ | **10/10 完全相同**（再验 326 的引理） |
| 不同 gcd 的个数 | **8**（10 个样本里 8 个不同的 monic 二次） |
| 不同零点集的个数 | **8** |
| 全部样本的 gcd 次数 | 恒为 2（都是 monic 二次） |

例：$v_0\mapsto\lambda^2+3\lambda+3$（根 $-3/2\pm\sqrt3 i/2$）；$v_1\mapsto\lambda^2+\lambda/2$（根 $-1/2,0$）；
$v_7\mapsto\lambda^2+3\lambda/5$（根 $-3/5,0$）；$v_9\mapsto\lambda^2+2\lambda/3+1/6$。

**结论：第 3 类存在。** 根确实随 $v$ 移动，且不同 $v$ 的 gcd 之间没有公共因子
（例如 $\lambda^2+\lambda/2$ 与 $\lambda^2+3\lambda+3$ 互素），所以 325 的 **S2（固定公因子）在这类分量上失效**。

## 进展

1. **三分落定**：第 1 类（固定根，104 的 $Z^\circ$）与第 3 类（本例）都真实出现；第 2 类（有限覆盖）未见。
2. **谱形式再验**：$\gcd_M=\gcd_{\text{pencil}}$ 在 10 个不同 $v$ 上完全相同——强证据支持 326 的引理（非特征层）。
3. **对 S3 的判断**：第 3 类的存在说明 **S2 不能闭合定理 C**；要判"整支全坏"，必须处理移动根，即 S3 的 PIT。

## 最终结论

1. **不能**指望"有限次 Type I 检查"解决 $c=1$；第 3 类必须正面对待。
2. 但实测暴露了一个**可能的替代靶子**：10 个样本的 **gcd 次数恒为 2**。若"次数在整个分量上恒定"是可证的
   （例如由一个秩恒等式或 $\det M\equiv0$ 型退化给出），那么"全坏"就可以用**次数的下界**来证明，
   而不必**找出** $\lambda(v)$——这仍然是 PIT，但目标从"求公共根"降级为"证次数恒定"。
   这是一个明确的、可检验的命题（下一步）。
3. 诚实边界：10 个样本全坏只是**证据**（随机点落在坏集上），**不是**"$Z^\circ$ 全坏"的证明；
   后者仍需 generic gcd。

## 放弃原因

- 没有证明"gcd 次数在分量上恒定"（只有观测）；
- 没有判定 $F_\lambda$（特征分量）是否存在、是否可行——因此**这个实例的层可行性尚未定论**；
- 没有测第 2 类是否可能出现（未构造出有限覆盖的例子）。

## 残留价值

- 一个**反例式的存在性结论**：第 3 类存在 ⟹ S2 不够 ⟹ 谱形式不能单独绕开 PIT。这直接修正了 326 结尾的乐观猜测。
- 一个**可检验的新靶子**："gcd 次数在分量上恒定" ⟹ 全坏可用次数下界证（不需要找根）。
- c335 可复跑，10 个 $v$ 的 gcd 与零点都打印在案。

## 相关文件

- [attempts/326](../../decision_algorithms/attempts/326_eigenvector_form_of_badness.md)（谱形式引理与三分）
- [attempts/325](325_theorem_c_cost_model.md)（S3 = PIT；S2 = Type I）
- [attempts/324](324_hyperplane_component_theorem.md)（分量结构）
- [c334](../../../../tools/verification/c334_spectral_form_check.py)（引理的实例核对）
- [c335](../../../../tools/verification/c335_lambda_movement.py)（本文件）

## 补充：$\det M\equiv0$ 与次数恒为 2（结构原因）

实测后又查了原因，结果比预期的干净：

**命题（一行）.** 设 $Q$ 为 $U^\perp$ 的基（行），$M(\lambda)=Q(\lambda I-A)N$（**注意 $M$ 是 $(n-2)\times k$，未必方**）。则
$$Qv=QAv=0\ \Longrightarrow\ M(\lambda)\,c_v=0\quad(\forall\lambda),$$
其中 $c_v$ 是 $v$ 在 $N$ 下的坐标。故 $\operatorname{rank}M(\lambda)\le k-1$ 对一切 $\lambda$ 成立。

*证明.* $M(\lambda)c_v=Q(\lambda I-A)Nc_v=Q(\lambda v-Av)=\lambda Qv-QAv=0$。$\square$

> **更正（专家 95 号）**：初版写"$\det M\equiv0$"。只有当 $n-2=k$（$M$ 是方阵，例如 E2 的 $3=3$）时才成立；
> 一般应写**秩界** $\operatorname{rank}M\le k-1$。已按此改正。

两个后果：
1. 非特征层（$\dim U=2$、$\operatorname{row}L=U^\perp$）上坏 $\iff\operatorname{rank}M(\lambda)\le\omega-1$；
   而 $M$ 恒有核方向 $c_v$ ⟹ 换成"最后一列是 $v$"的基之后 $M=[\widetilde M\ 0]$，
   坏性等价于**商铅笔** $\widetilde M$ 的降秩（见 [328](../../decision_algorithms/attempts/328_quotient_pencil_theorem.md)）。
2. **实测**：换 6 个**随机** $A$ 复核，秩界全部成立、$\deg\gcd$ **恒为 2**。
   所以"次数为 2"不是 E3 那个 $A$ 的假象。（但**不能**据此推断"全分量次数恒定"——专家 95 号给了反例，
   见 [328](../../decision_algorithms/attempts/328_quotient_pencil_theorem.md) §3(b)。）

## 状态

- 第 3 类存在：**[精确验证]**（10 个 $v$，8 个不同 gcd，根集各不相同）。
- $\gcd_M=\gcd_{\text{pencil}}$：**[精确验证 10/10]**。
- "次数恒定"：**观测，未证**。
- 该实例的层可行性：**未定**（需 generic gcd 或 $F_\lambda$ 的判定）。
