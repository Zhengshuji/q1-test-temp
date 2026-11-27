# 84 号裁决落实：论文送审意见与修正

> 2026-11-10。专家结论：方向正确、有发表潜力，但**当前不能冻结**。
> 必须先解决：系数域约定、Renegar 位长界、Appendix A.1 的秩论证、Appendix B
> 的编码、\(r=0\) 的多项式时间分支。
> 状态：**M3（专家裁决）**。

## 目标

落实 84 号对论文的审计，区分“已修”和“仍开放”。

## 设想与理由

专家明确把问题分为：
1. 数学正确性（最高优先）；
2. 复杂度认证；
3. 论文准备。

先修可立即修的三项：实观测器约定、Renegar 位长界、A.1 的秩错误；
再记录 \(r=0\) 与 Appendix B 的剩余义务。

## 做法

### 1. 系数域：采用实观测器约定

论文原来写 \(A,C,L_0\in\mathbb C\)，又用实转置 Gram；专家指出
\(\operatorname{im}(MM^{\mathsf T})=\operatorname{im}M\) 对复矩阵不成立
（反例 \(M=[1\ i]\)）。

已改为：

\[
A,C,L_0\in\mathbb Q,\qquad L=[L_0;R]\in\mathbb R^{q\times n},\qquad
\lambda\in\mathbb C.
\]

实转置 Gram、\(rd_0\) 参数计数、Bezout 都一致。

若将来允许复 \(R\)，则实化后自由坐标变为 \(2rd_0\)，Gram 改为共轭转置；
FPT 性不变。论文已写明这一备选。

### 2. Renegar 位长界

专家核到 Renegar 1992 **Part II**（JSC 13, 301–327）：
bit bound 形如
\[
B(\log B)(\log\log B)(sD)^{O(N)}.
\]

因此 Corollary 3b 不再是“条件性”：对 \(r\ge1\)，bit-model FPT 成立。

已改：

- Theorem 3 改为 **bit model**，\(r\ge1\)；
- 增加 Corollary 3a（real-RAM）；
- 删除原先的“只有 `poly(B)` 才成立”的条件性表述；
- Appendix A.5 使用
  \[
  B(\log B)(\log\log B)(sD)^{O(N)}
  \]
  并说明 \(N=\kappa_{\rm obs}+2\omega\)（\(\omega\) 是有限析取，不是实变量）。

**但**：系数位长 \(f(\kappa)\operatorname{poly}(\mathcal L)\) 仍需逐项证明；
论文把它写成“subject to the coefficient-size estimate”。

### 3. Appendix A.1 的秩错误

专家指出“满列秩右乘保持秩”是假的。已改为商空间恒等式：
\[
\operatorname{rank}\begin{bmatrix}J\\ M\end{bmatrix}
=\operatorname{rank}J+\operatorname{rank}(MN),
\qquad N\text{ 是 }\ker J\text{ 的基}.
\]
取 \(J=[C;CA]\)，直接得到
\[
(5a)\iff \operatorname{rank}[H_A;H]=\operatorname{rank}H
\]
与
\[
(5b)\iff \operatorname{rank}(\lambda H-H_A)=\operatorname{rank}H.
\]

### 4. Appendix B：直接秩因子化编码

专家指出原稿的 \(Z\cap\mathcal V\) 分层未定义且不可核。

已改为显式 \(\exists\mathbb R\) 编码：对每个
\(\omega=0,\dots,\min(q,k)\)，引入
\[
X,B,G,U,V,\quad S_0,\dots,S_{2\omega-2},
\]
约束
\[
H=XB,\quad H_A=GB,\quad UX=I_\omega,\quad BV=I_\omega,
\quad S(\lambda)(\lambda X-G)=I_\omega.
\]
变量数 \(O(n^3)\)，次数 \(\le2n\)，\(\omega\) 只有 \(n+1\) 个分支。

### 5. 变量数

Theorem 3/A.5 的变量数从
\(\kappa_{\rm obs}+2\omega+1\) 改为
\[
\kappa_{\rm obs}+2\omega
\]
（\(\omega\) 是离散分支，不是实变量）。

### 6. 保留的判断

- 两条参数化算法保留；
- 论文定位为算法/参数化复杂度；
- 固定 \(q\) 作为第二定理；
- 不回到 unrestricted hardness。

## 进展

* 实观测器约定已写入论文；
* Theorem 3 改为 bit model，\(r\ge1\)；
* A.1 秩论证已修；
* Appendix B 已改为直接编码；
* 变量数已改；
* Renegar Part II 引用已修正。

## 最终结论

论文方向与主要定理获专家认可，但**仍未冻结**。剩余硬缺口：
1. \(r=0\) 的多项式时间判定（不是 \(2\omega-2\) 的次数问题，而是 \(\binom q\omega\)
   枚举不可多项式化）；
2. 系数位长的逐项证明；
3. 固定 \(q\) 的常数与图卡/析取记账。

## 放弃原因

未完成 \(r=0\) 算法与完整系数位长证明；不把条件性结果写成无条件。

## 残留价值

- 实观测器约定统一；
- Renegar bit 界可用于无条件 bit FPT（\(r\ge1\)）；
- A.1 的商空间恒等式是正确的压缩证明；
- Appendix B 有可核的直接编码；
- 专家明确：不要回到硬度，先完成算法论文。

## 相关文件

* [84 答复](../../../for_expert/archive/84_paper_status_and_questions-answer.md)
* [paper/q1_parametric_algorithms.md](../../../../trash/paper_root_2026-11-21/q1_parametric_algorithms.md)
* [paper/COMPLEXITY_AUDIT.md](../../../../trash/paper_root_2026-11-21/COMPLEXITY_AUDIT.md)
* [paper/FREEZE_CHECKLIST.md](../../../../trash/paper_root_2026-11-21/FREEZE_CHECKLIST.md)

## 状态

* 专家裁决落实：**[M3]**。
* \(r=0\)：**[开放]**。
* 系数位长：**[待逐项证明]**。
