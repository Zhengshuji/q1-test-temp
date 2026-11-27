> **补（250）**：$R$ 不能一般地消去：固定 $Q$ 后 $\exists R: (QP)R=I$ 等价于 $QP$ 的
> $\omega$-子式生成单位理想，仍有 $\binom{k}{\omega}$ 个子式。固定 $(q,c)$ 不受影响；
> 固定 $\kappa_{\rm obs}$ 仍需结构化消元。

# 紧凑证书：$(5b)\\iff\\exists Q,R$ 使 $QPR=I_\\omega$

> 2026-11-09。为绕过 248 的“$\\binom{k}{\\omega+1}$ 个子式”障碍，给出一个**紧凑的多项式矩阵证书**：
> $(5b)$ 等价于存在多项式矩阵 $Q(\\lambda)$（$\\omega\\times q$）与 $R(\\lambda)$（$k\\times\\omega$）使
> $$Q(\\lambda)P(\\lambda)R(\\lambda)=I_\\omega.$$
> 这把“所有极大子式 gcd=1”换成了 $\\omega^2$ 个多项式方程，**不枚举子式**。
> 状态：**M2（纸面）**。

## 目标

把 $(5b)$ 写成不含 $\\forall\\lambda$、不含子式枚举的紧凑代数条件。

## 设想与理由

$P(\\lambda)$ 是 $q\\times k$ 的多项式矩阵，$\\operatorname{rank}P=\\omega$ 对所有 $\\lambda$。
$(5b)$ 等价于所有 $\\omega$-子式的理想为单位理想（gcd=1）。
在 PID $\\mathbb C[\\lambda]$ 上，Smith 标准形给出
$$P=U\\begin{bmatrix}D\\\\0\\end{bmatrix}V,\\qquad D=\\operatorname{diag}(d_1,\\dots,d_\\omega),$$
且 $\\gcd$ 所有 $\\omega$-子式 $=d_1\\cdots d_\\omega$。单位理想 $\\iff$ 所有 $d_i\\in\\mathbb C^\\times$。

## 做法：命题与证明

**命题**：设 $P(\\lambda)\\in\\mathbb C[\\lambda]^{q\\times k}$，$\\operatorname{rank}_{\\mathbb C(\\lambda)}P=\\omega$。则
$$(5b)\\iff\\exists Q\\in\\mathbb C[\\lambda]^{\\omega\\times q},\\ R\\in\\mathbb C[\\lambda]^{k\\times\\omega}:
\\quad QPR=I_\\omega.$$

*证明*：
$(\\Rightarrow)$ 若所有 $\\omega$-子式生成单位理想，Smith 标准形中 $D=I_\\omega$（差常数单位）。
取
$$Q=\\begin{bmatrix}I_\\omega&0\\end{bmatrix}U^{-1},\\qquad
R=V^{-1}\\begin{bmatrix}I_\\omega\\\\0\\end{bmatrix},$$
则 $QPR=I_\\omega$。

$(\\Leftarrow)$ 若 $QPR=I_\\omega$，由 Cauchy–Binet，
$$1=\\det(QPR)=\\sum_{|S|=\\omega}\\det(Q_{[\\omega],S})\\det(P_{S,S'})\\det(R_{S',[\\omega]}),$$
即 $1$ 属于所有 $\\omega$-子式生成的理想；故 gcd 为常数。$\\square$

### 对固定 $(q,c)$ 的算法

固定 $(q,c)$ 时 $k\\le q-1+c$ 有界（247），所以 $Q,R$ 的尺寸有界。
把 $Q,R$ 的系数作为未知量（次数由 $P$ 的次数界定），
$$Q(\\lambda)P(\\lambda)R(\\lambda)=I_\\omega$$
是 $\\omega^2$ 个多项式方程；系数比较后得到**多项式个**方程，变量数只依赖 $(q,c)$。
配合 $(5a)$ 的秩方程，得到固定 $(q,c)$ 的常数维实代数系统，量词消去多项式时间。

**关键改进**：不再出现 $\\binom{k}{\\omega+1}$ 个子式；方程数只有 $\\omega^2$。

### 对固定 $\\kappa_{\\rm obs}$ 仍不够

$Q$ 的尺寸 $\\omega\\times q$ 有界（$q$ 有界），但 $R$ 是 $k\\times\\omega$，变量数随 $k$ 增长；
所以 248 的障碍没有被完全绕过。要得到固定 $\\kappa_{\\rm obs}$ 的 XP，
需要进一步消去 $R$（例如用 $P$ 的 Smith 形/子式基）或把 $k$ 纳入参数。

## 进展

* 一个紧凑的 $(5b)$ 证书（$\\omega^2$ 个方程，无子式枚举）；
* 固定 $(q,c)$ 的算法更清晰；
* 明确固定 $\\kappa_{\\rm obs}$ 仍缺一步。

## 最终结论

* $(5b)$ 的紧凑形式是**双边多项式逆** $QPR=I$；
* 固定 $(q,c)$ 可解（247）有了更干净的证书；
* 固定 $\\kappa_{\\rm obs}$ 的 XP 仍需消去 $R$。

## 放弃原因

* 未实现 Smith 标准形/系数求解；
* 未把 $R$ 消去；
* 未做 Lean（多项式矩阵 Smith 形在 Mathlib 中不成熟）。

## 残留价值

* 一个可写进论文的等价刻画；
* 固定 $(q,c)$ 的紧凑证书；
* 明确的下一障碍：消去 $R$。

## 相关文件

* [attempts/247](247_fixed_qc_tractable.md)
* [attempts/248](248_kappa_not_enough.md)
* [docs/05 Q10](../../../../docs/05_open_questions.md)

## 状态

* 命题：**[M2 纸面]**。
* 算法实现：**[未做]**。
