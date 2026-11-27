# 旧框架 → 新框架 对照表

> **为什么有这一页**：项目里并存两套形式化（2026-10-13~21 的旧框架、2026-10-22 起的新框架）。
> 旧文档仍以"已证"口吻陈述，而这些结论**多数在新框架下已被反例推翻**。本页是唯一的对照入口。
>
> **规则**：引用旧结论前必须在本页查状态；状态为 ❌ 的**禁止引用**。

---

## 0. 定位（2026-10-27 决定）

> **旧框架只作参考，不复现。**
> 1. 旧框架里许多环节本身不可靠（20 处自我更正、多处工具 bug，见
>    `archive/process_logs/CLAUDE_旧记忆_2026-10-23前.md` §3/§5）；
> 2. 因此**不要求**把 A1–A20 逐条复现或翻译；
> 3. 能**完整转化且对主线有用**的部分（如 A1 的 4 块形式、A3 的秩恒等式、A5/A8 的 Lean）
>    已经并进新框架（`docs/02`、`proof/`）；
> 4. 其余一律当**历史参考**：需要了解某条旧结论时，在新框架下**重新证/重新测**，
>    并把教训写进 `CLAUDE.md` §10。

---

## 1. 两套框架的对象

| | 旧框架 | 新框架 |
|---|---|---|
| 时间 | 2026-10-13 ~ 10-21 | 2026-10-22 ~ |
| 主记号 | $q_0$、$d_{CA}$、$\mathrm{obs}$、$(A)$、$(S)$、$\Theta$、$\mathcal P$、情形 I/II、支 A/B | $\rho$、$c$、$(5a)$、$(5b)$、$\mathcal J$、$K$、$P(T,B,U_0)$ |
| 目标结论 | $q_{\min}=\mathrm{obs}+1$（等价于 $q_1$ 假）| $q_{\min}=\min\{(\rho+c):\text{可达}\}$，$\rho_{ci}=P$ 已可算 |
| 判定形式 | ETR 型：$\exists\Theta:(\mathrm{A})\wedge(\mathrm{S})\wedge\operatorname{rank}H<q_0$ | 逐层：$\exists(\mathcal U,\mathcal H,\tau)$ 使 $(5a)\wedge(5b)$ |
| 结论清单 | **20 条**（`archive/proof_notes_dimV_line/OLD_20_theorems_A1-A20.md`）| **13 条**（`docs/02`）|
| 现存文档 | `archive/paper_drafts/FINAL.md`、`archive/proof_notes_dimV_line/`、`archive/session_history/` | `docs/`、`proof/`、`workspace/` |

---

## 2. 术语对照

| 旧 | 新 | 说明 |
|---|---|---|
| $\mathrm{obs}=\dim V$，$V=\langle\operatorname{row}R_0\rangle_{A'}$ | 无直接对应；最接近 $\rho$（当 $c=0$）| 新框架里 $c\ge1$ 恒成立，所以旧 $\mathrm{obs}$ 不能直接当 $\rho$ |
| $q_0$ | $q$（行数）| 同一个量 |
| $d_{CA}=\dim\ker[C;CA]$ | $d=n-j$ | 同一个量（$K=\ker[C;CA]$）|
| $(A)$：$\operatorname{row}(\mathcal LA)\subseteq\operatorname{row}(\mathcal L)+\operatorname{row}[C;CA]$ | $(5a)$ | 同一条件（T1 即"4 块"形式）|
| $(S)$：$\operatorname{rank}(\lambda H-F)=\operatorname{rank}H$ | $(5b)$ | 同一条件（经 $H=\mathcal LN_{CA}$、$F=\mathcal LAN_{CA}$）|
| 情形 II（$d_{CA}\ge q_0$）| 无（新框架不按此分层）| 旧的时间复杂分情形 |
| 支 A / 支 B | 无 | 同上 |
| $\alpha_0=L_0N_{CA}$ | $\pi(S)$ 的坐标 | 同类对象 |
| ETR / $\exists\Theta$ | 「层内 $\exists(\mathcal U,\mathcal H,\tau)$」 | 都是存在性代数问题 |

---

## 3. 旧 20 条定理的现状

（编号沿用 `OLD_20_theorems_A1-A20.md`；状态由 2026-10-24 之后的反例/新证明定）

| 旧定理 | 内容（简）| 现状 | 依据 |
|---|---|---|---|
| A1 | $(5a)$ 的 4 块形式 | ✅ **仍成立** | 在新框架里就是 $(5a)$ 的原文；`proof/5a_archive/lean/ABridge.lean`（Lean）|
| A3 | 秩恒等式（铅笔与 $\ker$）| ✅ 仍成立 | 新 B.1 的证明用到同型恒等式 |
| A4 | 阈值 $\{\operatorname{rank}=d_C\}\ne\emptyset$ 的判据 | ⚠️ 只在旧框架内有意义 | 新框架无 $d_C$ 一词 |
| A5 | (A) ⟹ 分解（Lean）| ✅ 仍成立 | `Factor.lean`（Lean）|
| A6 | 充分性（构造）| ⚠️ 条件性 | 依赖旧参数化 |
| A8 | Lean 形式化 | ✅ 仍成立 | `tools/lean/PRecursion*`、`proof/5b_upper_bound/lean/` |
| A9–A18 | 旧框架的结构引理 | ⚠️ 未逐条重核 | 需人工比对（见 §4）|
| **A19** | $\rho\le\mathrm{obs}$ | ⚠️ 旧框架内成立 | 新框架的对应陈述见 `docs/02` A.3 |
| **A20** | $(5a)\wedge(5b)\Rightarrow\alpha_0\in V$ | ❌ **已废** | 新框架下 $\alpha_0\in V$ 既不必要也不充分（$\dim V+1$ 被 $n{=}5$ 反例推翻）|
| 推论 | 可行性 $\iff\alpha_0\in V$ | ❌ **已废** | 同上 |
| 目标 | $q_{\min}=\mathrm{obs}+1$ | ❌ **已废** | `counterexample_refute_dimV1.json`（$q_{\min}=1<2$）|
| 旧公式 | $q_{\min}=\max(r,\rho^*+1)$ | ❌ **已废** | `S=\mathcal J` 族（$q_{\min}=n$）；`proof/refuted/README.md` R3 |
| 变体 q3（$d_{CA}=0$）| $\nu_{\min}=q_0$，多项式可判 | ✅ 仍成立 | `archive/problem_statements/q3.md`；新框架对应 $d=0\Rightarrow q_{\min}=r$（`docs/05` Q6）|

---

## 4. 不复现的部分（决定见 §0）

按 §0 的决定，以下**不做**，只作参考：

1. A9–A18 的逐条翻译（旧证明本身经过多次更正，可靠性不足）；
2. 旧 ETR 论证在新框架下的重述（若要用，应在新框架下重做，而不是翻译）；
3. 旧 73 条 Lean 定理的复用清单（用到的再单独迁移）。

## 5. 使用规则

1. 引用旧结论 → 先查 §3 状态；❌ 的一律不引；
2. 写新文档时**只用新框架记号**；需要提旧结论时写明"（旧框架，见 framework_map）"；
3. 旧框架的**地基**（A1/A3/A5/A8）可以当作已证的技巧复用，但要重新写进 `docs/02` 的对应条目；
4. 旧文档本身不动（它们记录的是当时的状态）。
