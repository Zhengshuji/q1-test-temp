# 反例验收协议与搜索策略

## 0. 为什么需要协议

这个项目已经栽过 12 次（见 [CLAUDE.md](../../../CLAUDE.md) 纪律 1–12），其中 4 次是工具 bug、
多次是"搜索没找到就当成不存在"或"随机 114/114 就当成定理"。
证伪方向的价值全在**反例的可信度**，所以先把验收标准写死。

---

## 1. 什么算"反例"

要找的是

$$\exists\ (A,C,L_0),\quad q(\rho^*)>\max(r,\ \rho^*+1),\qquad
\rho^*=\min\{\rho:\ q(\rho)<\infty\}.$$

**必须同时给出**：

1. 实例 $(A,C,L_0)$（有理数，写进 JSON）；
2. $\rho^*$ 的**精确值**（不能是"搜到的最小值"）；
3. 下界证明：**所有** $\operatorname{rank}(\mathcal LN)=\rho^*$ 的解都 $\ge k$ 行（$k>\rho^*+1$）；
4. 上界：存在一个 $k$ 行的解（所以 $q(\rho^*)=k$）。

第 3 条是关键：**"搜索没找到 $\rho^*+1$ 行的解"不算证明**（薄集、搜索深度、采样偏差都可能）。

---

## 2. 三步验收

### 第 1 步：精确复算

$$d,\ \rho_0,\ \dim V,\ \rho^*,\ q(\rho^*)\ \text{全部用有理数精确算}.$$

工具：[`scripts/core/c166_layer_audit.py`](../../../tools/verification/c166_layer_audit.py)（含 $\rho$ 层扫描与紧性判定）。

### 第 2 步：下界证明（人工）

按 $\rho^*$ 的大小选论证方式：

| $\rho^*$ | 下界证明的样子 |
|---|---|
| $1$（$d=1$）| 可完全分类：$q=2$ 时 $(5b)\iff L\nu,LA\nu$ 线性无关（D42 的论证）|
| $1$（$d>1$）| 需分析 $\ker(\lambda M-MA'-N')$ 的维数跳变 |
| 一般 | 用 $(5a)$ 的 ci 结构 + $(5b)$ 的 pencil 条件 |

### 第 3 步：对抗性复核

- 用**另一个**实现（不复用 c166）重算 $(5a),(5b)$；
- $(5b)$ 用子式 gcd（不是 $\lambda$ 采样）；
- 检查 $L=[L_0;R]$ 字面前缀、$\operatorname{rank}(L)=q$；
- 记录到 `candidates/`，通过后复制进 `proof/refuted/certificates/` 并在 `q1_false/attempts/archive_attack_log/` 或 `workspace/` 开新条目。

### 已知限制（重要）

`c166` 的 $q_{\min}$ 是**搜索上界**，不是精确值：解集可能是薄集，随机采样会漏。
实测：对 `certificate_middle_layer.json` 本身（已知 $q=2$ 的解），
`param_scan.py` 在 $t=0$ 处只报到 $q_{\min}=3$ —— 漏掉了证书里的解。

$$\boxed{\ \text{所以：审计报告只能当上界用；"审计说 }q=k\text{" }\ne\ q_{\min}=k\ }$$

任何"层不紧"的结论，必须按 §1 的第 2 步给出下界证明，不能只依赖审计。
扫描时若种子自带已知解（如 `L_2row`），应把它注入候选集，否则 $t=0$ 一行就会失真。

---

## 3. 搜索策略（按优先级）

### S1. 中间层种子的参数化变形

种子：

| 文件 | $n$ | $p$ | $d$ | $\dim V$ | $\rho_0$ | $\rho^*$ |
|---|---|---|---|---|---|---|
| `certificate_middle_layer.json` | 6 | 2 | 2 | 2 | 0 | 1 |
| `certificate_rhostar_lt_dimV.json` | 6 | 2 | 2 | 2 | 1 | 1 |

做法：$A(t)=A_0+tE$、$C(t)=C_0+tF$、$L_0(t)=L_0+tG$，$t$ 取有理网格，逐点跑第 1 步。

判据：记录 $(\rho_0,\dim V,\rho^*,q(\rho^*))$，找 $\rho_0<\rho^*<\dim V$ 且 $q(\rho^*)>\rho^*+1$。

脚本：[`search/param_scan.py`](scans/param_scan.py)。

### S2. 从 $(M,N',A')$ 判据直接设计

紧层要求

$$\ker(\lambda M-MA'-N')=\ker M\quad\forall\lambda .$$

反过来：**先设计** $(A',M,N')$ 使某个 $\xi$ 满足 $M\xi\ne0$ 且 $N'\xi=M(\lambda\xi-A'\xi)$，
再解 $LN=M,\ LR_0=N'$（线性方程，有解性可判），最后补 $(5a)$。

这条路的优点是"先造违例、再找实现"，比盲搜有方向。

### S3. 块结构

把多个小实例沿对角拼，用 $C$ 的交叉项控制可见性。注意 D38/D40 已排除最简单的两种。

---

## 4. 记录格式

`candidates/` 下每个候选一个 JSON：

```json
{
  "name": "...",
  "A": [...], "C": [...], "L0": [...],
  "rho0": 1, "dimV": 2, "rhostar": 1,
  "q_of_rhostar": 3,
  "lower_bound_proof": "文字说明/引理编号",
  "verified_by": ["c166", "independent"],
  "status": "candidate | accepted | rejected"
}
```

---

## 5. 交接

- 本目录找到候选 → 在 [`THE_LEMMA.md`](../attempts/00_the_lemma.md) 的对应引理旁标 `⚠ 有候选反例`，附路径。
- 本目录确认某条构造路线已死 → 写进本文 §3 的"已排除"，避免重复。
- 若 `q1_true/` 先完成归约 → 本目录停止对抗性搜索（q1 已被回答）。
