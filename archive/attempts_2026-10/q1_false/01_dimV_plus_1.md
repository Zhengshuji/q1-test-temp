# 路线 1：$q_{\min}=\dim V+1$

## 目标
证明 $q_{\min}=\dim V+1$，其中 $V=\langle S\rangle_{A'}$ 是 $S=\operatorname{row}(R_0)$ 在 $A'$ 下的不变闭包。

## 设想与理由
- 下界：$q\ge\rho+1$（Lean `LowerBound`：$\mathcal A$ 是 $A'$-不变 ⟹ $\mathcal A\supseteq V$ ⟹ $\rho\ge\dim V$）。
- 上界：构造 $\mathcal L$ 使 $\operatorname{rank}(\mathcal LN)=\dim V$ 且 $(5b)$ 成立（§21 两步构造 + §29 的 $\dim B\le p$）。

## 做法
[archive/attack_A2V0/](../../../archive/attack_A2V0) 的分段文件（`LEMMA_LIFT` 拆成 5 份）+ `ATTACK_LOG` 拆出的 D1–D9。

## 进展（按时间）
| 时间 | 事件 |
|---|---|
| 2026-10-23 | 上界骨架成形（§7–§13）；发现并排除障碍 $\dim B_\lambda\le\dim S$（§9）|
| 2026-10-23 晚 | **自我更正**：$(b)$ 的方向写反（§15/§16），撤回 `max(dim V+1, d−dim V)` |
| 2026-10-23 深夜 | 把缺口压成一条：$A^2V_0\subseteq V_0$（§41–§46），2293/2293 精确验证 |
| 2026-10-24 02:20 | **被 $n{=}5$ 反例推翻**：$q{=}1<\dim V+1{=}2$（证书 `counterexample_refute_dimV1.json`）|

## 最终结论
**推翻**。崩点：Gap A（$S\not\subseteq\mathcal A$），即"$\dim V$"根本不是下界的一部分。

## 放弃原因
缺口 $A^2V_0\subseteq V_0$ 从未被证明，而反例证明它（连同整个公式）是假的。

## 残留价值
- 下界 $q\ge\rho+1$ 仍然成立（并被吸收进 [docs/02](../../../docs/02_theorems_proven.md) A.2）。
- 6 个 Lean 模块（`LowerBound`/`Closure`/`DimIdentity`/`Admissible`/`Lemma31`/`WellDefined`）—— 见 [tools/lean/](../../../tools/lean/README.md) 与 `archive/old_scripts/lean/`。
- "四个工具 bug"的教训（CLAUDE.md 纪律 5）。

## 相关文件
- 证明草稿：[archive/attack_A2V0/01_upper_bound_skeleton.md](../../../archive/attack_A2V0/01_upper_bound_skeleton.md) 等 5 份
- 攻击日志：[archive/attack_A2V0/ATTACK_LOG.md](../../../archive/attack_A2V0/ATTACK_LOG.md)（及 `q1_false/attempts/archive_attack_log/` 的 7 份拆分）
- 证书：[proof/refuted/certificates/](../../../proof/refuted/certificates)