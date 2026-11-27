# Paper I：算法与 FPT 部分的待修清单（2026-11-17，来自 diag-iv）

> 给执行子代理：**只改 `paper/current/paper_I_dec.tex`**。不得改动数学结论、不得改 `\label` 名称、
> 不得重排编号。每条都给了行号与修法；改完必须编译通过（0 error / 0 undefined ref / 0 overfull）。

## A. 记号冲突与未定义记号（最严重）

**A1. $Z(Y)$ 指两个不同矩阵。** line ~1016："chart matrix $[E_0;\,[I_t\mid Y]E_Q]$"，line ~1022："$Z(Y)$ the window matrix of Lemma window for $\lambda H(Y)-H_A(Y)$"。两者维数不同（前者是 $W$ 的图卡矩阵，后者是系数窗口矩阵）。
→ 把图卡矩阵改名为 $Z_{\rm ch}(Y)$（或 $W(Y)$），窗口矩阵保留 $Z$。凡引用"the row space of $Z(Y)$"处（~1066）必须指图卡矩阵。

**A2. $E_0$、$E_Q$ 从未定义**（仅出现在 1017、1073）。→ 在使用处前加一句定义：$E_0$ 是 $W_0$ 在 $\mathbb R^{2k}$ 中的行基，$E_Q$ 是商 $\mathcal V/W_0$ 的坐标选取矩阵；或改为文字描述而不引入符号。

**A3. $H_A(Y)$ 未定义**（1022）：$H_A$ 侧应是 $G(Y)$。→ 改。

**A4. 图卡矩阵的块尺寸说错了**：现在写 "the two $t\times\ell$ blocks"，但该矩阵的行空间含 $W_0$，两块应是 $(s_0+t)\times\ell$。→ 改，并说明 (5a) 必须用**完整**的 $H=LN$、$H_A=LAN$（含 $L_0$ 的行）。

## B. 数学缺口

**B1. $U\subseteq S$ 从未证明，却被两处当作 Lemma struct 的推论使用**（~1052、~1058，另有 ~753 的 Cauchy–Binet 段落）。
→ 在 §III 的 subspace-reduction 小节里加一句（并在上述两处改引它）：
"By Lemma~\ref{lem:compression}(iv), a feasible $W$ satisfies $\operatorname{rank}H_A=\operatorname{rank}H$, so $\operatorname{row}H_A=\operatorname{row}H$; hence $\pi_1(W)=\pi_2(W)=\operatorname{row}H_A\subseteq\operatorname{row}(AN)=S$."
（正确性已核实：(5a) 给 row $H_A\subseteq$ row $H$，(5b) 给等秩，故相等；row$(LAN)\subseteq S$。）

**B2. $\sigma$ 未定义且不是多项式**（~1020–1021、~1090–1091）：文中从未出现"singular value"。实代数判定需要多项式。
→ 改为初等对称多项式：$\operatorname{rank}H=\omega$ 用 $e_\omega(HH^{\mathsf T})>0$；$\operatorname{rank}[H;G]\le\omega$ 用 $e_{\omega+1}([H;G][H;G]^{\mathsf T})=0$。与 §IV 的 $e_\omega(X^{\mathsf T}X)$ 记号一致。

**B3. 第 (vi) 步结论不成立**（~1124–1126）：漏了算法里的两个提前返回（$q<q_0$、$W_0=0$）与"补零行到 $q$ 行"。
→ 在该步显式列出：$r=0$ 走 §VII；$W_0=0$ 直接可行；$q<q_0$ 不可行；一般情形由 (iv)(v) 覆盖，且由 Lemma sandwich 的逆 + Lemma monotone 补零行得到恰好 $q$ 行的观测器。

**B4. 六步顺序不合逻辑**：(i) 用了 $t\le2\ell$，而它在 (iii) 才证。
→ 把"维数界与 $U\subseteq S$"提到最前（新 (i)），其余顺延；保持 `\emph{(i)}`… 形式。

**B5. (iv) 的量词错误**（~1062）："Every $W$ with $W_0\subseteq W\subseteq\mathcal V$ maps to a subspace of dimension $t$" 只对 $\dim(W/W_0)=t$ 成立。
→ 加假设。

**B6. 表与公式自相矛盾**：`tab:fptcount` 说 "polynomials per branch $O(\ell^2)$"，而 `eq:nvar` 说 $s=2\omega+O(1)\le2\ell+O(1)$。
→ 统一为 `eq:nvar` 的 $s=2\omega+O(1)$，表中该行改为 "$s=2\omega+O(1)\le2\ell+O(1)$"。

**B7. Thm 12 的计数**：$s=O(k)\cdot O(k)+O(1)$ 里的加性项应是 $O(k)$ 而非 $O(1)$（$Z^{\mathsf T}Zx=e_0$ 有 $2\omega$ 行）。
→ 改成 $s=O(k^2)+O(k)=O(k^2)$，结论不变。

**B8. 交叉引用错**：~915 与 ~1399 说 coefficient-size lemma 在 Section `sec:fpt`，实际在 Appendix `app:bits`。
→ 改引用。

## C. 编辑级（顺手做）

**C1. `thm:fixedq` 证明里 `align` 的 4 行无 label 也无引用**（~906–911）→ `align*`。
**C2. `eq:charts` 只被引用 1 次** → 可留（它是图数界的定义处），但如改成 `equation*` 需同时把引用处改成文字。
**C3. `tab:fptcount` 目前嵌在证明中间** → 移到证明之后（表格不是论证的一部分）。
**C4. `lem:rankcons` 证明开头**复述"$Mb=c$ 相容当且仅当 $c\in\operatorname{im}M$"（这是定义）→ 删，直接引秩判据。
**C5. `lem:window` 缺 $\omega\ge1$ 假设**（其两个兄弟引理都有）→ 补。
**C6. `lem:bezout` 缺 $s\ge1$ 假设**（空族的结论为假）→ 补。
**C7. `prop:gram` 陈述缺 $\omega=\operatorname{rank}H$ 与 (5a) 的前提**（它引 compression(iii) 的等价形式）→ 在陈述里补一句。
**C8. `lem:rankcons` 的量词约定 $e_j=0$（$j>$ 尺寸）需明说** → 补一句。

## 验收

```
cd workspace\_scratch\cur1
copy paper\current\paper_I_dec.tex p.tex
pdflatex -interaction=nonstopmode p.tex   (两遍，先删 p.aux)
```
检查：`Output written`、`^!` 计数 0、`Reference .* undefined` 0、`Overfull` 0；
另外确认 `grep -c "E_0\|E_Q\|sigma_"` 的结果符合预期（B2/A2 处理后不应再有未定义的 $\sigma$）。
