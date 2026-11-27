# 文献：cover 问题这条线（2026-10-24 补查）

> 项目记录里有一句话把 q1 指向了 cover 问题：
> > 「q1 的难点 ⟺ 最小维数 admissible 子空间的计算复杂度」（`../../archive/process_logs/COUNTEREXAMPLE_2026-10-22.md` §4.4）
>
> 这里把这条线的文献查清楚。

---

## 1. Karcanias–Vafiadis (1993)：cover 问题的提出

**On the cover problems of geometric theory**, *Kybernetika* 29(6), 1993（项目存有全文 `lit/Karcanias_Vafiadis_1993_cover.txt`）。

- 把几何控制里的"覆盖"统一成矩阵 pencil 的 **Kronecker 结构分配问题**（KSAP）；
- 分解为 MPAP（增广）与 MPRP（实现）两个子问题；
- 明确写：*"of particular interest are the problems of determining the minimal dimension subspace solutions, when such solution exist"*（p. 550）。

$$\boxed{\ \text{他们只提出"最小维数解"是重要问题，}\textbf{没有给复杂度结论}\ }$$

---

## 2. Varga (2003)：最小动态 cover **可低复杂度计算**

**Reliable algorithms for computing minimal dynamic covers**, CDC 2003（[DLR eLib](https://elib.dlr.de/12000/)）。

摘要原文要点：

> *"Minimal dimension dynamic covers play an important role in solving the structural synthesis problems of **minimum order functional observers**... We propose numerically reliable algorithms to compute two basic types of minimal dimension dynamic covers... based on a special controllability staircase condensed form... The overall algorithm has a **low computational complexity** and is provably numerically reliable."*

$$\boxed{\ \text{最小动态 cover（即条件的 (5a) 部分）有低复杂度算法}\ \Longrightarrow\ \textbf{代数部分是多项式的}\ }$$

**但**：Varga 的 cover 只对应 $(5a)$（admissible / 不变性），**不含 $(5b)$ 的"无零点"**。
项目的 `RESULTS.md` 也记了这一点（"Varga 2004：Type I minimum dynamic cover = admissible 条件，但不含 (b)"）。

---

## 3. 其他相邻文献（均无硬度结论）

| 来源 | 内容 | 与 q1 的关系 |
|---|---|---|
| Trumpf–Helmke–Fuhrmann, *Towards a compactification of the set of conditioned invariant subspaces* | ci 子空间集合的几何（紧化）| 说明 ci 集合是"好"的几何对象 |
| *Almost invariant subspaces and operators*（NSF/JFA）| 近似不变子空间的算子理论 | 不涉及复杂度 |
| *Common invariant subspaces of two matrices*（LAA 1998）| 两矩阵共不变子空间的算法 | 单矩阵情形多项式；无 NP-hard 结论 |
| ELA：*The common invariant subspace problem and Tarski's theorem* | 用 Tarski 消元判可判定性 | **可判定**，非复杂度 |

$$\text{结论：整个相邻文献里，}\textbf{没有任何一篇给出 MIN-ROWS 或其松弛的 NP-hard 结论}$$

---

## 4. 对 q1 的意义

文献把问题切成两半：

$$\underbrace{\text{最小动态 cover}}_{(5a)\ \text{部分：Varga 低复杂度}}\ +\ \underbrace{\text{无零点}}_{(5b)\ \text{部分：无算法}}$$

- 若 $(5b)$ 能"吸收"进 cover 的计算（例如对 cover 的某个参数族检查一次 gcd），则 q1 = 假；
- 若 $(5b)$ 迫使在 cover 的解集里做**组合选择**，则 q1 = 真。

**目前两边都没有证据。** 这就是 q1 仍然开放的原因。
