# 249 的显式证书：$QPR=I_2$（244 的铅笔）

> 2026-11-09。为 249 的紧凑证书给出一个**可机器检查的实例**：
> 对 244 的 $3\\times3$ 铅笔 $P(\\lambda)$（秩 2），构造 $Q$（$2\\times3$）与 $R(\\lambda)$（$3\\times2$）使
> $$QPR=I_2.$$
> 验证脚本 `c252_compact_cert.py` PASS。状态：**M2 + 精确验证**。

## 目标

把 249 的“$\\exists Q,R:QPR=I_\\omega$”从等价命题落成一个具体证书。

## 设想与理由

找一个 $Q$，使 $QP$ 有一个**常数非零**的 $2\times2$ 子式；该子块可逆，直接构造 $R$。

## 做法

244 的铅笔：
$$P(\\lambda)=\\begin{bmatrix}
0&0&\\lambda\\\\
\\lambda-3&2\\lambda-6&-1\\\\
3\\lambda-3&6\\lambda-6&\\lambda-3
\\end{bmatrix}.$$
取
$$Q=\\begin{bmatrix}1&2&-1\\\\-2&2&2\\end{bmatrix}.$$
则
$$M=QP=\\begin{bmatrix}
-\\lambda-3&-2\\lambda-6&1\\\\
8\\lambda-12&16\\lambda-24&-8
\\end{bmatrix}.$$
它的第 0、2 列构成
$$S=\\begin{bmatrix}-\\lambda-3&1\\\\8\\lambda-12&-8\\end{bmatrix},\\qquad \\det S=36\\in\\mathbb C^\\times.$$
把 $S^{-1}$ 放进 $R$ 的第 0、2 行（第 1 行取 0）：
$$R=\\begin{bmatrix}
-2/9&-1/36\\\\
0&0\\\\
1/3-2\\lambda/9&-\\lambda/36-1/12
\\end{bmatrix},$$
则 $QPR=I_2$（精确）。

## 验证

`tools/verification/c252_compact_cert.py`：
- $\\operatorname{rank}P=2$、$\\det P=0$；
- $\\det S=36$；
- $QPR=I_2$；
- $P$ 的全部 $2\\times2$ 子式 gcd $=1$（$(5b)$ 成立）。

输出：`PASS`。

## 进展

* 249 的等价命题有了显式证书；
* 说明“常数非零子式 ⇒ 右逆”这一方向可直接构造，不需要 Smith 标准形。

## 最终结论

* $QPR=I$ 是可操作的证书形式；
* 固定 $(q,c)$ 的算法可直接用它（$P$ 尺寸有界）；
* 固定 $\\kappa_{\\rm obs}$ 的障碍仍是 $R$ 的 $k\\omega$ 变量（250）。

## 放弃原因

* 未给出一般算法（只给一个实例）；
* 未消去 $R$；
* 未接 $(5a)$ 的完整系统。

## 残留价值

* 一个可视化的证书；
* 验证了 249 的构造方向；
* 可作为固定 $(q,c)$ 算法的测试用例。

## 相关文件

* [attempts/249](249_compact_certificate.md)
* [attempts/250](250_eliminate_R_barrier.md)
* `tools/verification/c252_compact_cert.py`

## 状态

* 实例证书：**[M2 + 精确验证]**。
* 一般算法：**[未做]**。
