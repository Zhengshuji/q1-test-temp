# 445 自查发现**内部矛盾**：$(E)$ 与 $(F)$ 的数据不可信，需回到测试本身

> 本轮本打算证"$\dim\mathcal T_W<2\omega$ ⟹ 不可行"（444 的未证方向）。
> 但写下证明时发现一条**简单论证**与 441/443 的数据冲突，说明**其中一处判据/测试有 bug**。
> 本文件记录这个矛盾、以及它影响的范围。

## 目标

证 444 的未证方向；结果：**先要解决一个内部矛盾**。

## 设想与理由

写证明时先做了一次量级检查，得到一条简单论证（见下）。

## 做法：一条简单的论证

设 $(E)$ 成立：$E_\lambda(\mathcal T_W)=W$ 对一切 $\lambda$。
取 $\mathcal T_W$ 的一组基 $p_1,\dots,p_D$，把它们**全部**作为自由行（需要 $m\ge D=\dim\mathcal T_W$；
每个可用对都能由某个真实行 $r\in\mathbb C^n$ 实现，因为 $\mathcal T_W$ 正是由 $r\mapsto(rN,rAN)$ 生成的像）。
则铅笔的行包含 $E_\lambda(p_1),\dots,E_\lambda(p_D)$，它们的张成正是 $E_\lambda(\mathcal T_W)=W$，故
$$\operatorname{rank}P(\lambda)=\omega\quad\text{对一切 }\lambda .$$

$$\boxed{(E)\ \wedge\ m\ge\dim\mathcal T_W\ \Longrightarrow\ (F)}$$

也就是说：**$(E)$ 与 $(F)$ 之差只可能是行数不够**（$m<\dim\mathcal T_W$）。

## 进展

## 与数据的冲突

| 来源 | 数据 | 与上述论证 |
|---|---|---|
| 441（c385） | 20 例 $(E)$ 真、$(F)$ 假，其中含 $m=4,5$ | **冲突**（若那些实例的 $m\ge\dim\mathcal T_W$） |
| 443（c386） | 1 例 $(E)$ 真、$(Z)$ 假、$(F)$ 真 | 一致 ✓ |

所以：**441 的 20 个"反例"里，至少有一部分是测试 bug**（很可能是 $m<\dim\mathcal T_W$，
或 $(E)$ 的判定写错——例如把"$\pi_1=\pi_2=W$"当成 $(E)$，而 $(E)$ 还要求子式互素）。

## 影响范围（必须回头修）

- [441](../../c_stratification/attempts/441_projection_not_sufficient.md)：$(E)\not\Rightarrow(F)$ 的结论**不可信**；
- [442](../../c_stratification/attempts/442_three_conditions.md)：三条件图景里的"灰色带非空"**不可信**；
- [443](../../c_stratification/attempts/443_gray_band_has_feasible.md)：结论方向与上述论证一致，但依据同一套代码，**待复核**；
- [444](../../c_stratification/attempts/444_threshold_criterion.md)：判据 $\mathcal T_W=W\oplus W$ 依赖的"$\dim<2\omega$ ⟹ 不可行"**未证**，
  且若上述论证成立，则**该判据是错的**（$(E)$ + 足够行数就可能可行，无需 $\mathcal T_W=W\oplus W$）✗。

**保留的**：437 的 $(E)$ 判据（点态必要）；441 的零配偶构造（充分）；439/440 的族分析（各自独立）。

## 最终结论

1. **一条简单论证**表明 $(E)$ + 行数足够 ⟹ 可行 ⟹ 中间层可行性的判据应当**就是 $(E)$ 加行数条件**，
   而不是 444 的 $\mathcal T_W=W\oplus W$；
2. 441 的 20 个"反例"因此**必有一处是 bug**，必须回头查（最可能是 $m$ 与 $\dim\mathcal T_W$ 的关系、
   或 $(E)$ 的实现）；
3. 在查清之前，**441–444 的结论一律降级为待复核**；本线唯一稳固的是 437（$(E)$ 必要）与 441 的构造（$(Z)$ 充分）。

## 放弃原因

- 没有定位 bug（时间用在了写证明上，而证明暴露了矛盾）；
- 没有重新跑 441 的实例并打印 $m$、$\dim\mathcal T_W$、以及"取基作自由行"的直接构造。

## 残留价值

- **一条干净的论证**（$(E)$ + 行数 ⟹ 可行），它把中间层的判据压到"$(E)$ + $m\ge\dim\mathcal T_W$"；
- 明确指出 441–444 的结论**需要复核**，并列出受影响的文件；
- 给下一步一个可执行的清单（重跑并打印中间量，或直接用"基作自由行"的构造验证）。

## 下一步

1. 用**构造性方法**直接判：取 $\mathcal T_W$ 的基当自由行（若 $m$ 够），算 $\gcd$；
2. 若这样得到的判定与"精确 $\tau$-符号"判定不一致 ⟹ 精确判定或 $(E)$ 的实现有 bug；
3. 修好后重跑 441/443/444 的关键实例。

## 相关文件

- [444](../../c_stratification/attempts/444_threshold_criterion.md)、[443](../../c_stratification/attempts/443_gray_band_has_feasible.md)、[442](../../c_stratification/attempts/442_three_conditions.md)、[441](../../c_stratification/attempts/441_projection_not_sufficient.md)（均待复核）
- [437](../../c_stratification/attempts/437_eval_map_criterion.md)（$(E)$，保留）

## 状态

- $(E)$ + 行数 ⟹ 可行：**[已证-纸面]**（简单论证）。
- 441–444 的结论：**[待复核]**。
- bug 定位：**[未做]**。
