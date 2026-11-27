# 路线：$\Phi_R$ 的低维不变量（Task 2 第 2 问）

## 目标

专家 Task 2 的第 2 问：$\Phi_R$ 是否只经由某个**低维不变量**依赖 $R$？
若是，参数化可从 $R\in\mathbb C^{(q-r)\times n}$ 塌到一个更小的空间，直接服务"选候选"的算法。

## 设想与理由

$\Phi_R=\Lambda_R|_{W_R}$，而 $\Lambda_R$ 满足双线性方程
$$\mathcal L_RA=\Lambda_R\mathcal L_R+G_0C+G_1CA,\qquad \mathcal L_R=\begin{bmatrix}L_0\\R\end{bmatrix}.$$
可能的"小不变量"候选：

| 候选 | 是否真的不依赖 $R$ | 说明 |
|---|---|---|
| $\Lambda_R$ 在 $W_R$ 上的限制 | 就是 $\Phi_R$ 本身 | 循环，无降维 |
| 等号情形下的 $K_1$（$Q_{\mathcal L}=P(\lambda)H_0$ 的左上块）| **依赖 $R$** | $K$ 由 $\mathcal LA=KH_0$ 唯一确定，而 $H_0=[\mathcal L_R;B]$ 含 $R$ |
| 商上的作用 $T=\pi A$、$B=\pi(\mathcal J A)$ | **不依赖 $R$** | 但 $\Phi_R$ 显然不是只由 $(T,B)$ 决定（否则 $D.1$ 的 $P$ 就够）|
| $\Phi_R$ 的相似/等价类 | 未定 | 需要先明确允许的等价（保持 $W_R\subseteq\mathbb C^q$ 与 $\iota_R$）|

## 做法（本轮做到的）

1. 把双线性结构写成三条引理（已入 `proof/B.37/README.md` 的 Task 2 一节）：
   分别线性、可容许集是构造集、$\Phi_R$ 的条目是 $R$ 的有理函数。
2. 做**维数记账**（启发式，不是证明）：$\mathcal A$ 的自由度 $\approx(q-r)n$ 减去 $(5a)$ 的秩约束；
   目标空间 $\operatorname{Hom}(W_R,\mathbb C^q)$ 的维数是 $q\rho$。当 $n\gg\rho$ 时
   $(q-r)n\gg q\rho$，故像集是低维子簇——但这只说明"像小"，**不**说明存在**规范**低维不变量。
3. 检验"是否存在规范不变量"的最短路径：在等号情形（$h=q+r_1$）用 $K_1$ 显式算一遍，
   看 $R\mapsto K_1$ 是否单射（若在某子族上单射，则该子族上无降维）。

## 进展

* 双线性结构与构造集：**已证**（B.37 卷宗）。
* 维数记账：**启发式**，且依赖 $(5a)$ 约束的秩（本项目对"可容许集维数"没有精确公式，见 B.28 的分层参数）。
* 等号情形的显式小例：**未做**。原因：本项目的层号记账（$\rho=\dim\pi(\mathcal V)$、$c=\dim S$、$q=\rho+c$）
  在小例上手算极易错（本轮试算过一个 $n=3$ 的候选族，$\rho$ 与 $q$ 的口径对不上，说明必须用
  `tools/ledger` + `tools/verification/consistency_checks.py` 的七条检查生成实例，不能手搓）。

## 最终结论（本轮）

**没有找到**不依赖 $R$ 的低维不变量；能证明的只有"$\Phi_R$ 由 $R$ 有理决定、可容许集是构造集"。
"是否存在规范小不变量"仍开放，且**必须用带校验的实例生成**才能判定——手算小例不可靠。

## 放弃原因（本轮）

不是数学上失败，而是**方法上不成熟**：没有可靠的实例生成器，任何手算小例都可能给出错误的 $\rho/c$
（本轮已出现一次口径不符）。按纪律不把不可靠的计算写进命题。

## 残留价值

1. 三条引理（双线性 / 构造集 / 有理依赖）已入 B.37，可直接引用；
2. 维数记账给了"像小但未必有规范不变量"的判断，对路线 A（硬度）有用：
   若像集维数远小于参数空间，则"避开常数 gcd"更像是一个**低余维**条件，硬度归约需要额外 gadget；
3. 明确了下一步的正确做法：先用 `consistency_checks.check_candidate` 生成并校验实例，再算 $\Phi_R$。

## 相关文件

* `proof/B.37/README.md`（Task 2 一节：三条引理）
* `proof/D.1/README.md`（$\rho_{ci}=P(T,B,U_0)$：为什么 $(T,B)$ 不够）
* `tools/verification/consistency_checks.py`（七条检查，生成实例时必须调用）
* `workspace/kronecker/attempts/01_kronecker_structure.md`（Kronecker 结构方向的既有工作）
