# Class I 的 $q_{\min}=n-1$ —— 从猜想变成定理（B.26 + B.27）

## 目标

证明 Class I（$p=r=1$、$(c,A)$ 可观测）的 $q_{\min}=n-1$，即"$1\le q\le n-2$ 时任何可容许 $\mathcal L$ 都失败"。

## 设想与理由

关键是把 Class I 的条件都压到 $\mathcal Z$（或其正交补 $\mathcal V=\mathcal Z^\perp$）上：

* **B.26**：$\mathcal V=\operatorname{row}[\mathcal L;c]$（故 $\dim\mathcal V=q+1$ 且只依赖 $\mathcal Z$）；
  $h=\dim(\mathcal V+\langle cA\rangle)\in\{q+1,q+2\}$，其中 $h=q+2\iff cA\notin\mathcal V$；
  $(5a)\iff\mathcal VA\subseteq\mathcal V+\langle cA\rangle$（$cA\in\mathcal V$ 时即 $\mathcal V$ $A$-不变）。
* 于是二分：
  * **情形 A**（$cA\notin\mathcal V$）：$h=q+2=q+r_1$ ⟹ **B.22**（等号障碍）直接给失败 ✓；
  * **情形 B**（$cA\in\mathcal V$）：$(5a)$ ⟹ $\mathcal V$ $A$-不变 ⟹ $cA^k\in\mathcal V$ 对一切 $k$ ⟹
    由 $(c,A)$ 可观测，$\mathbb C^n=\operatorname{span}\{cA^k\}\subseteq\mathcal V$ ⟹ $n\le q+1$，与 $q\le n-2$ 矛盾 ⟹
    **情形 B 不可能** ✓。

## 做法

1. 证明 B.26（四条结构事实）并数值核验（2954/2954）；
2. 证明 B.27（$q_{\min}=n-1$）并数值核验（2454/2454：$1\le q\le n-1$ 的可容许样本全部是情形 A 且全部失败）；
3. 把 B.18e 的"猜想"注与 STATUS 的表述升级为定理。

## 进展

| 项 | 结果 |
|---|---|
| **B.26（已证）** | $\mathcal V=\operatorname{row}[\mathcal L;c]$、$h=\dim(\mathcal V+\langle cA\rangle)\in\{q+1,q+2\}$、$(5a)$ 的行空间判据、情形 B ⟺ $\mathcal V$ $A$-不变 |
| **B.27（已证）** | $1\le q\le n-2$ 且可容许 ⟹ $(5b)$ 失败；配合 B.18b（$q=n-1$ 可行）得 **$q_{\min}=n-1$** |
| 精确验证 | B.26：**2954/2954**；B.27：**2454/2454**（情形 A 全部失败，情形 B 零样本）|
| 依赖 | 只用到 $(c,A)$ 的可观测性；不需要 $(\ell,A)$ 可观测、不需要 $\mathcal Z\subseteq K$ |
| 文档 | B.18e 的"猜想"注与 STATUS 升级为定理 |

## 最终结论

1. **Class I 的 $q_{\min}=n-1$ 是定理**，不再是猜想；
2. 证明的机制很清楚：**等号情形（情形 A）由 B.22 杀掉；非等号情形（情形 B）被"$\mathcal V$ 必须 $A$-不变 + 可观测性"挤死**；
3. 这也解释了为什么"整族不可行"：同一 $\mathcal Z$ 的所有 $\mathcal L$ 行为一致（B.26），所以问题只在 $\mathcal Z$ 上；
4. 与专家的判断一致：他认为 $d\ge2$ 是"下一个实质推进最可能出现的地方"，而实际上一旦把条件压到 $\mathcal Z$，证明只有半页。

## 放弃原因

不适用。

## 残留价值

* **B.26/B.27**：Class I 的完整答案（$q_{\min}=n-1$）+ 一个干净的两情形机制；
* 两个精确验证脚本（2954/2954、2454/2454）；
* 一条方法论：先证"条件只依赖哪个对象"，再在这个对象上做维数二分。

## 相关文件

- `docs/02` B.26、B.27（新）、B.18e（注升级）
- `STATUS.md`
- `tools/verification/b26_class_I_only_Z.py`、`b27_check.py`
- 专家答复：`workspace/for_expert/archive/19_spectral_pair_and_class_I-answer.md`（§6 的提醒正是缺口所在）

## 续：B.27 的 Lean 内核（`B27.lean`）

新增 `tools/lean/MyProof/B27.lean`，**exit=0、0 error 0 warning**，三条声明：

| 声明 | 对应 |
|---|---|
| `K27.krylov_le`（实为 `B27.krylov_le`）| 若 $c\in S$ 且 $S$ 对"右乘 $A$"封闭，则 $\operatorname{span}\{cA^k\}\le S$（情形 B 的归纳步骤）|
| `B27.eq_top_of_krylov` | Krylov 张成 $=\top$（可观测性）⟹ $S=\top$ |
| `B27.no_caseB` | $d=q+1$、$d=n$、$q+2\le n$ ⟹ False（维数矛盾）|

差在哪里：行空间 $\mathcal V=\operatorname{row}[\mathcal L;c]$ 的实例化、"$(5a)\Rightarrow$ 右乘 $A$ 封闭"（B.26 第 3 条）
仍是纸面 + 精确验证（2954/2954、2454/2454）。

STATEMENT_MAP 现 **183 声明 / 173 条目 / 0 问题**；覆盖率表 B.27 行升级为 **✓ [Lean-conditional]**。

## 专家 2026-11-05 的复核：**B.27 通过**（"Main theorem correct / Class I minimum order resolved"）

他的具体意见与落实：
1. **B.26(1)(2)(4) 全部正确**；并指出 B.26(3) 有更简证明：由 $\mathcal V=\operatorname{row}\mathcal L\oplus\langle c\rangle$（直和）得
   $\mathcal VA=\operatorname{row}(\mathcal LA)+\langle cA\rangle$，而 $(5a)$ 恰为 $\operatorname{row}(\mathcal LA)\subseteq\mathcal V+\langle cA\rangle$
   ⟹ 两者合并即得。**已采用**（替换原证明）。
2. **约定**：$\mathcal Z^\perp$ 应明确为**代数零化子**而非 Hermite 正交补。**已加约定说明**。
3. **假设写全**：$\operatorname{rank}[c;\ell]=2$ 是终阶可行（B.18b）所需的；并明确 **不需要** $(\ell,A)$ 可观测。
   **已在 B.27 陈述中写明**。
4. **B.27 判定**：两情形穷尽且都成立；"lower-bound proof is complete"；建议把 B.27 提为主定理。
5. 他的答复在"我还看到一个应当先抽出来的推广"处**被截断**（原文止于 $\boxed{$），推广部分未收到——需另行索取。

**另记**：他给出的终阶可行证明与我们的 B.18b 一致（$(\mathcal Z=0)$ 时失败需 $0\ne x\in\ker c$ 且 $Ax=\lambda x$，由 PBH 被可观测性排除）。

## 专家 2026-11-05 的**完整版**复核（answer2，725 行）——含他承诺的推广

**完整性评估**：Q1–Q5 全部答复，另加 §6（技术细节）与 §7（polished statement）。
仅两处截断：§4 的 "Part I Section 1" 中 $\mathcal Z=\cdots$ 一行、§7 末尾的 $\boxed{$；另有 1–2 处笔误
（$\operatorname{row}$ 写成 $\operatorname$）。数学内容完整。

**他给出的推广（§2）已收录为 B.28 + B.28b**：
* **B.28（一般 $(p,r)$ 的子空间归约）**：$\mathcal V=\mathcal Z^\perp=\operatorname{row}[\mathcal L;C]=U\oplus R$、$\dim\mathcal V=q+p$；
  $(5a)\iff\mathcal VA\subseteq\mathcal V+W_0$；$h=q+p+r_1-\dim(\mathcal V\cap W_0)$；**不变子空间排除**：
  $q+p<n$ 且可容许 ⟹ $\operatorname{row}(CA)\not\subseteq\mathcal V$。
* **B.28b（分层参数 $\delta$）**：$\delta=\dim(\operatorname{row}(CA)/(\operatorname{row}(CA)\cap\mathcal V))$，$h=q+p+\delta$，
  $0\le\delta\le r_1-p$；等号 ⟺ $\delta=r_1-p$（B.22）、不变排除 $\delta=0$、**未决 = 中间层** $1\le\delta<r_1-p$。
  Class I 的 $r_1-p=1$ ⟹ **无中间层**，这就是它能一次二分解决的**结构原因**。

**他对下一步的建议（Q5）**：先 $p=1,r=2$（保留单输出循环坐标，$r_1$ 可达 3 ⟹ $\delta=1$ 是第一个真正的新情形），
再 $p=2,r=1$（多输出可观测几何）；暂不直接攻一般复杂度，先把问题分成
**verification（给定 $\mathcal Z$ 判 $(5b)$）** 与 **synthesis（$\exists$ 可容许 $\mathcal Z$）**。

**他的其余意见**：B.27 拆成"下界定理 + 终阶可行定理"再合成推论；精确验证只作旁证（需说明图卡覆盖）；
Lean 标 `[Lean-conditional]` 是对的；论文排序按"子空间归约 → 计数/谱 → 等号障碍 → Class I"，
且**不要把计数不等式说成完整刻画**。
