> **更正（441）**：本文的充分性**不成立**——构造要 $(x_i,0)\in\mathcal T_W$，而投影条件不保证 $y=0$。
> 正确充分条件是**零配偶条件**（见 [441](441_projection_not_sufficient.md)）。20/24 反例。

# 438 中间层的充分条件：$\pi_1(\mathcal T_W)=\pi_2(\mathcal T_W)=W$ ⟹ 层可行（$m=2\omega$）

> 承接 437（$E_\lambda$ 点态判据）。本轮攻"第二类失败"（全局铅笔问题），
> 结果：**在这个结构里不存在全局障碍**——只要 $\mathcal T_W$ 的两个投影都满射，就有一个**显式构造**。

## 目标

判定：$E_\lambda$ 处处满射时，能否选有限的自由行使铅笔**同时**处处满秩？

## 设想与理由

$E_\lambda(x,y)=\lambda x-y$。若 $\pi_1(\mathcal T_W)=W$ 且 $\pi_2(\mathcal T_W)=W$，则可取
$$(x_1,0),\dots,(x_\omega,0),\quad(0,y_1),\dots,(0,y_\omega),$$
其中 $x_i$、$y_j$ 都是 $W$ 的基。它们给的铅笔行是
$$\lambda x_1,\dots,\lambda x_\omega,\ -y_1,\dots,-y_\omega,$$
即
$$P(\lambda)=\begin{pmatrix}\lambda X\\-Y\end{pmatrix},\qquad X,Y\ \text{可逆},$$
于是
$$\boxed{\operatorname{rank}P(\lambda)=\omega\quad\text{对一切 }\lambda}$$
（$\lambda\ne0$ 时上半块满秩；$\lambda=0$ 时下半块满秩）。**自由行数 $m=2\omega$。**

## 做法

在缩放移位族上取 $\mathcal T_W$ 的基、按上述构造选 $2\omega$ 个可用对，精确算 $\omega$-子式的 $\gcd$（[c384](../../../../tools/verification/c384_sufficiency.py)）。

## 进展

[c384](../../../../tools/verification/c384_sufficiency.py)：缩放移位族
$$A:\ e_i\mapsto e_{i+k},\quad C=(e_{2k+1};\dots;e_{3k})$$
使 $K_0=\operatorname{span}\{e_1..e_k\}$、$\mathcal S=\operatorname{row}[e_1..e_{2k}]$，
于是对任何 $W$ 都有 $\mathcal T_W=W\oplus W$。

| $k$ | $\omega$ | $\dim\mathcal T_W$ | $\gcd$ | 判定 |
|---|---|---|---|---|
| 2 | 1 | 4 | $1$ | **可行** ✓ |
| 3 | 1 | 5 | $1$ | **可行** ✓ |
| 3 | 2 | 7 | $1$ | **可行** ✓ |

**中间层确实可以可行**，而且 $\omega=2$、$k=3$（不是顶层）也做到了 ✓。

## 关键等价（把两类失败合并）

$$\boxed{E_\lambda\ \text{对一切}\ \lambda\ \text{满射}\iff \pi_1(\mathcal T_W)=W\ \text{且}\ \pi_2(\mathcal T_W)=W}$$
（$\lambda=0$ 给 $\pi_2=W$；$\lambda\ne0$ 的联合消去给 $\pi_1=W$；反向显然。）

于是 437 的"点态必要"与这里的"构造充分"**在同一个条件上会合**：

> **层 $\omega$ 在 $W$ 上可行 $\iff$ 两个投影都满射到 $W$**（差一个"固定行补一位"的边界情形）。

## 最终结论

1. **不存在"点态满射但全局无解"的障碍**——至少在这个结构里没有：构造 $[\lambda X;-Y]$ 直接给出单一正则铅笔；
2. 中间层的可行性被**投影条件** $\pi_j(\mathcal T_W)=W$ 刻画（可算、可设计）；
3. 因此中间层**可以**成为硬度的载体：把源问题编码成"这两个投影是否满射"即可。

## 放弃原因

- 没有处理"固定行补一位"的边界：若 $\dim E_\lambda(\mathcal T_W)=\omega-1$ 而固定行恰好补上，
  判据要放宽；这类实例未研究；
- 只验证了移位族（$\mathcal T_W$ 最大）；没有在**投影不满射但固定行可补**的实例上测；
- 没有把 $\pi_j(\mathcal T_W)=W$ 写成 $W$ 的 Grassmann 坐标条件（那是做归约需要的）。

## 残留价值

- **一个显式构造**（$m=2\omega$，$[\lambda X;-Y]$），把"全局障碍"这一类失败**排除**；
- **投影判据**：中间层可行 $\iff$ $\pi_1=\pi_2=W$（差边界情形）——这是可算、可设计的；
- 硬度侧的落脚点：中间层能活，且活的条件是**代数可写的**。

## 下一步

1. 把 $\pi_j(\mathcal T_W)=W$ 写成 $W\in\operatorname{Gr}(\omega,k)$ 的坐标条件（行列式子式），
   看它在 Grassmannian 上是**开集**还是**闭集**——若开，则"可行"是开条件，硬度需要"不可行"的判定；
2. 处理边界情形（固定行补一位）；
3. 试着把某个 NP-难问题编码成"某个 $W$ 使两个投影满射"。

## 相关文件

- [437](437_eval_map_criterion.md)（$E_\lambda$ 判据）
- [436](436_expert106_audit.md)（106 号裁决：反例与 $E_\lambda$）
- [435](435_characteristic_dead.md)（特征族，被本文件与 437 解释）

## 状态

- 充分性构造：**[精确验证]**（$k=2,3$；$\omega=1,2$）。
- 投影等价：**[已证-纸面]**。
- 固定行补位的边界：**[未做]**。
- 归约：**[未做]**。
