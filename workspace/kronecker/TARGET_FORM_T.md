# 暂定的"目标形式 T"（Kronecker 结构）

> 依据：专家 2026-11-02（Workstream B 复核）§6 的模板。**第 1–3 条是铅笔理论的一般事实**
> （不要当成观测器理论的新结果）；**第 4 条才是本项目的猜想**。

## 记号

观测器铅笔
$$Q_L(\lambda)=\begin{bmatrix}\lambda L-LA\\ CA\\ C\end{bmatrix},\qquad (q+2p)\times n .$$
$h=\operatorname{rank}[L;CA;C]$；在 $(5b)$ 下 $h$ 就是 normal rank。
$r=h$，$m=q+2p$，$\#\varepsilon=m-r$，$\#\eta=n-r$。

## 第 1 条（一般事实）

$(5b)$ 成立 ⟹ $Q_L$ **没有有限初等因子**。
（常数秩 ⟺ 无有限初等因子；注意：**不**蕴含最小指标为 0。）

## 第 2 条（一般事实）

左右最小指标的**个数**由行/列数与 normal rank 决定：
$$\#\{\varepsilon_j\}=q+2p-h,\qquad \#\{\eta_i\}=n-h .$$

## 第 3 条（一般事实，已核对）

全局恒等式（$\gamma_k$ 为齐次不变因子）
$$\sum_i\eta_i+\sum_j\varepsilon_j+\sum_k\deg\gamma_k=r .$$
在 $(5b)$ 下退化为
$$\boxed{\ \sum_i\eta_i+\sum_j\varepsilon_j+d_\infty=h\ }$$
（$d_\infty$ = 无穷初等因子的总次数）。

**核对状态**：[精确验证]，全部可行样本 ✓

| 样本 | $q$ | $(\rho,c)$ | $h$ | $\eta$ | $\varepsilon$ | $d_\infty$ | 和 |
|---|---|---|---|---|---|---|---|
| §55 | 4 | $(3,1)$ | 5 | $[0]$ | $[4]$ | 1 | $0+4+1=5$ ✓ |
| seed 1001 | 6 | $(4,2)$ | 6 | $\varnothing$ | $[5,1]$ | 0 | $0+6+0=6$ ✓ |
| seed 1010 | 4 | $(3,1)$ | 5 | $[0]$ | $[4]$ | 1 | $5$ ✓ |
| seed 1010 | 5 | $(3,2)$ | 5 | $[0]$ | $[4,1]$ | 1 | $5$ ✓ |

## 第 3.5 条（归一化，已判定）

**结构陈述必须以原始 $Q_L$ 为对象。** 层坐标/商铅笔与原铅笔的关系已核对为
$$\operatorname{rank}Q_L(\lambda)=j+\operatorname{rank}Q_{\rm quot}(\lambda),$$
即**行空间的商（压缩）**，不是严格/幺模等价；Kronecker 不变量**不能**搬（例：$\varepsilon=[4]$ 在商铅笔里变成 $\eta=[3]$）。
证据：[kron_layer_relation.py](../../tools/verification/kron_layer_relation.py)、[README §4.6](README.md)。

## 第 4 条（**猜想**，本项目的目标）

> **猜想 T4**：观测器结构对三元组 $\bigl(\{\eta_i\},\{\varepsilon_j\},d_\infty\bigr)$ 施加了
> **超出第 1–3 条**的额外限制。

候选的具体形式（按可检验性排序）：

- **T4-a（右指标消失）**：**已证** ✓——而且不需要 $(5b)$：只用 $(5a)$ 即可。
  见 [proof/kron_null_module](../../proof/kron_null_module/README.md)（B.6）。证明要点：
  按 $\lambda$ 的幂展开，最高次系数 $v_d$ 满足 $Lv_d=CAv_d=Cv_d=0$，
  由 $(5a')$（$\operatorname{row}(LA)\subseteq\operatorname{row}(L;CA;C)$）得 $LAv_d=0$，
  故 $v_d$ 是常值零向量；减去 $\lambda^dv_d$ 后对次数归纳。
  **精确验证 150/150**（$n=6,7,8$）。
  ⟹ 这一条**不是猜想**，是定理；它与一般铅笔的反例 $[\lambda\ 1]$ 不矛盾（那条没有 $Q_L$ 的分块结构）。
- **T4-b（无穷因子受限）**：**已证** ✓（[proof/t4b_infinite_divisors](../../proof/t4b_infinite_divisors/README.md)，docs/02 B.7）。
  **定理**：$(5a)$（**不需要 $(5b)$**）⟹ 无穷初等因子全是 1 次 ⟹
  $$d_\infty=h-\operatorname{rank}L .$$
  左指标的和**不是** $\operatorname{rank}L$ 的普遍公式：由恒等式得
  $\sum\varepsilon=\operatorname{rank}L-d_{\rm fin}$，只有 $(5b)$（$d_{\rm fin}=0$）时才等于 $\operatorname{rank}L$。
  证明：$LA=XL+Y_1CA+Y_2C$ ⟹ $Q_L$ 严格等价于 $[(\lambda I-X)L;CA;C]$ ⟹ 反转铅笔在 $\mu=0$ 局部等价于
  $[L;\mu CA;\mu C]$ ⟹ 行列式因子 $\Delta_k=\mu^{k-\operatorname{rank}L}$ ⟹ 不变因子 $\mu$ 的一次幂。
  **精确验证 151/151**（$n=6..10$）。

- **T4-c（左侧，专家推荐的**主形式**）**：$$\boxed{\ \sum_j\varepsilon_j=\operatorname{rank}L\ }$$
  由 B.6（$\sum\eta=0$）、B.7（$d_\infty=h-\operatorname{rank}L$）与恒等式
  $\sum\eta+\sum\varepsilon+d_{\rm fin}+d_\infty=h$，**在 $(5b)$ 下**这条成立
  （等价形式是 $\sum\varepsilon=\operatorname{rank}L$）；只用 $(5a)$ 时右边要减去 $d_{\rm fin}$。

## 判定"成功"的标准

任何一条 T4-x 若成立，必须给出：
1. **纸面证明**（或 Lean），且明确用到了 $Q_L$ 的**分块结构 + (5a)**，而不是只用 $(5b)$；
2. 一个**能打挂它的坏输入**的检验（反例脚本）；
3. 与 [RESTRICTED_COMPLETION_MODEL](../../proof/layer_program/RESTRICTED_COMPLETION_MODEL.md) §5 的
   "目标形式 T"（有限条不等式）对齐的表述。

## 相关

- 撤回记录：[proof/refuted R18](../../proof/refuted/README.md)
- 工具：`tools/verification/kronecker_pencil.py`、`observer_pencils.py`、`kron_sweep.py`、`kron_identity_probe.py`
- 纪要：[README.md](README.md)、[attempts/01](attempts/01_kronecker_structure.md)
