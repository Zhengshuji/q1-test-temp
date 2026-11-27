# Class I 的 $d=1$ 分类：可容许的直线**都在坏像里**（0/44 的采样证据）

## 目标

用 B.18d 的像刻画 + $(5a)$ 的可容许性，做 $d=1$（$q=n-2$）的**充要分类**。

## 设想与理由

$d=1$ 时谱条件只依赖 $z$（B.18c）：$z\in V$ ⟹ 自动成立；$z\notin V$ ⟹ 失败 $\iff z\in\operatorname{im}\psi$。
所以"谱上好"的直线只有一类：**$z\notin V$ 且 $z\notin\operatorname{im}\psi$**。
问题变成：这样的直线能否**可容许**（即存在 $\mathcal L\supseteq\ell$、$\ker[C;\mathcal L]=\langle z\rangle$ 且 $(5a)$ 成立）？

## 做法

tools/verification/class_I_d1.py：伴矩阵实例（$n=5,6,7$），
随机 $z\in K$；用 B.18d 判"$z\in\operatorname{im}\psi$"，用 $z^\perp$ 里的随机行组 $\mathcal L=[\ell;R]$
（保证 $\mathcal Lz=0$、$\operatorname{rank}[C;\mathcal L]=n-1$）测可容许性。

## 进展

| 类别 | 计数 |
|---|---|
| 样本 | 599 |
| **谱上坏**（$z\in V$ 或 $z\in\operatorname{im}\psi$）| 555，**全部可容许** |
| **谱上好**（$z\notin V$ 且 $z\notin\operatorname{im}\psi$）| 44，**可容许者 0** |

$$\boxed{\text{谱上好}\wedge\text{可容许}=0/44}$$

即：**可容许的直线全都落在坏像里**（或落在 $V$ 里），于是 $d=1$ 阶整族失败。

## 最终结论

1. **B.18e（猜想，未证）**：$d=1$ 时若 $\mathcal L$ 满足 $(5a)$ 且 $\ker[C;\mathcal L]=\langle z\rangle$，则
   $z\in V$ 或 $z\in\operatorname{im}\psi$——即 $d=1$ **整族不可行**；
2. 证据：$0/44$（谱上好者无一可容许）+ $555/555$（谱上坏者全部可容许，说明可容许性本身不苛刻）；
3. 若猜想成立，结合 B.18b（$q=n-1$ 必然可行）即得 **$q_{\min}=n-1$**，阶差 $=n-1-q_0$；
4. 证明的难点：把 $(5a)$ 的行空间约束与 $P_w$（B.18d）的条件联立——这是下一步的具体目标。

## 放弃原因

不适用（分类已化到一条猜想；证明待做）。

## 残留价值

* 把 Class I 的 $d=1$ 分类压成**一条**猜想（含明确的联立目标）；
* 两组互补的计数（$0/44$ 与 $555/555$），说明"是 $(5a)$ 与谱条件的**共同作用**"；
* 脚本可复用（换 $n$、换坐标）。

## 相关文件

- `docs/02` B.18b、B.18c、B.18d、B.18e（猜想）
- `tools/verification/class_I_d1.py`、`psi_image_canonical.py`、`membership_test.py`
