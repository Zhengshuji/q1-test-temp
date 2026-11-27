# $\dim W_L=c+1$ 的可行实例：$n=6$、$k=4$、$q=3$、$\dim W_L=3$

> 2026-11-08。按 167 的判据构造出一个 $\dim W_L=3$ 的真实实例，$L$ 通过七条检查。
> 这验证了 166 的“$V$ 不被 forced、在 $\operatorname{Gr}(2,W_L)$ 上枚举”的分支确实存在可行点。
> 状态：**精确验证 + 纸面构造**。

## 目标

构造 $(A,C,L_0)$，满足 $n=6$、$p=1$、$r=1$、$k=4$、$c=2$、$\omega=2$、$q=3$、$\dim W_L=3$，
并给出满足 $(5a)(5b)$ 的 $L$。

## 设想与理由

按 167：$\dim W_L=3\iff L_0N$ 是特征向量（$\lambda_0$）；需要 $d_C\ge1$、$W_\Gamma\ne0$、
$\lambda_0$ 处 $P_1\notin W_\Gamma$。取 $\lambda_0=1$。

## 做法

$n=6$，$C=e_1^{\mathsf T}$，$L_0=e_3^{\mathsf T}$，
$$A e_1=e_2,\quad A e_2=e_1,\quad A e_3=e_3+e_2,\quad A e_4=e_4,\quad A e_5=e_5,\quad A e_6=3e_6+e_2.$$
则
- $K_0=\ker[C;CA]=\ker[e_1;e_2]=\operatorname{span}\{e_3,e_4,e_5,e_6\}$，$k=4$；
- $L_0N=e_3^*$、$L_0AN=(A e_3)|_{K_0}=e_3^*$（$e_2$ 在 $K_0$ 上为零）⟹ 秩 1，
  $$W_L=\ker e_3^*=\operatorname{span}\{e_4,e_5,e_6\},\qquad \dim W_L=3;$$
- $d_C=\operatorname{rank}[C;CA]-\operatorname{rank}C=2-1=1$；
- $CA^2N=\operatorname{row}_2(A)|_{K_0}=e_3^*+e_6^*\ne0$，$W_\Gamma=\operatorname{span}\{e_3^*+e_6^*\}$。

取 $V=\operatorname{span}\{e_4,e_5\}\subset W_L$，$\operatorname{Ann}(V)=\operatorname{span}\{e_3^*,e_6^*\}$，
$h_0=e_3^*$、$u_1=e_6^*$；$P_1=\lambda_0u_1-(A e_6)|_{K_0}=e_6^*-3e_6^*=-2e_6^*\notin W_\Gamma$ ✓。
$g_2=e_2$ 给出 $\Gamma(g_2)=e_3^*+e_6^*\in W_\Gamma$，且给 $L$ 增加 $e_2$ 方向（保证 $\operatorname{rank}[C;L]=4$）。

**见证**：
$$L=\begin{bmatrix}
0&0&1&0&0&0\\
0&0&1&0&0&1\\
0&1&1&0&0&1
\end{bmatrix}.$$

## 验证

`python tools/verification/c2_dimWL3_witness.py` 输出：
```
k = 4
dim W_L = 3
rank[C;L]=4 ✓ · dim ker=2 ✓ · CZ=LZ=0 ✓ · (5a)=True ✓ · h=4=法秩 ✓ · gcd/Toeplitz 一致（(5b) 成立）✓ · 域=有理 ✓
PASS
```

## 进展

* 构造出 $\dim W_L=3$ 的可行实例（$q=3$），$L$ 通过七条检查；
* 验证了 167 的判据（$d_C\ge1$、$W_\Gamma\ne0$、$P_1\notin W_\Gamma$）是可实现的；
* 说明 166 的“枚举 $V$”分支确实有可行点（不是空分支）。

## 最终结论

* $\dim W_L>c$ 的实例存在且可行；167 的判据与构造配方有效；
* 这补上了 166 的未测分支（存在性层面；算法在该实例上的运行仍可另测）。

## 放弃原因

* 未把该实例接入 166 工具（工具当前只吃 seeds；可另加从 $(A,C,L_0)$ 入口）；
* 未验证 166 的枚举在该实例上确实找到同一 $L$（存在性由见证直接确认）。

## 残留价值

* 一个精确的 $\dim W_L=3$ 可行见证，可用于回归测试；
* 167 判据的实例化。

## 相关文件

* [attempts/167](167_dimWL3_existence_criterion.md)（判据）
* [attempts/166](../../decision_algorithms/attempts/166_c2_general_algorithm.md)（算法）
* [tools/verification/c2_dimWL3_witness.py](../../../../tools/verification/c2_dimWL3_witness.py)

## 166 算法接入（2026-11-08）

工具 [c2_q3_algorithm.py](../../../../tools/verification/c2_q3_algorithm.py) 增加了从 $(A,C,L_0)$ 直接运行的入口
`run_from_data`，并把本实例加入 `__main__`。运行输出：
```
dimWL3 FOUND {'V': 1, 'forced': 0, 'good': 1, 'fail': 0}
```
即：在 $\operatorname{Gr}(2,W_L)$ 的枚举中，第一个 $V$ 就通过判据并构造出满足七条检查的 $L$。
这验证了 166 的“$V$ 不被 forced”分支在真实 $\dim W_L=3$ 实例上可用。

## 状态

* 实例与见证：**[精确验证 1/1]**。
* 接入 166：**[已完成]**（`run_from_data`，输出 `dimWL3 FOUND`）。
