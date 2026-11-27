# 更正：局部泄漏刚性的铅笔步骤不成立（seed 10 反例）

> 2026-11-09 自查。207 采纳了专家 64 号 §4 的“局部泄漏刚性”：$A(V)\subseteq K_0$、$\omega>0$ ⇒ $A(V)\subseteq V$ ⇒ 铅笔秩降。
> 前两步正确，但**第三步不成立**：它需要全局 $A(K_0)\subseteq K_0$。seed 10 的可行见证给出反例。
> 状态：**M2（更正）**。

## 目标

修正 207/203 中关于“局部泄漏刚性 ⇒ 不可行”的错误结论，并说明对 gadget 路线的影响。

## 设想与理由

207 的局部论证：
1. 每行 $h_i$ 零化 $V$ 与 $A(V)$（$A(V)\subseteq K_0$）⇒ $\operatorname{row}H\subseteq(V+AV)^\perp$；
2. $\omega\le k-\dim(V+AV)$ ⇒ $A(V)\subseteq V$。**这两步正确**。
3. 然后声称“$V$ 不变 ⇒ $V^\perp$ 含左特征向量 ⇒ 铅笔秩降”。**这一步只在 $A(K_0)\subseteq K_0$ 时成立**：
   此时 $H_A=HT$、$P=H(\lambda I-T)$，$T^{\mathsf T}$ 在 $V^\perp$ 上有特征向量。
   仅有 $A(V)\subseteq K_0$ 时，$lA$ 不是 $K_0$ 上的泛函（$Aw$ 可能离开 $K_0$），无法定义 $T$。

## 做法

### 反例：seed 10

seed 10 的已验证见证（七条检查通过）：
$$V=\ker H=W_L=\operatorname{span}\{(-1,-1,1,0),(0,0,0,1)\},\qquad \omega=2.$$
精确计算：
- $A(V)\subseteq K_0$（$Av\in K_0$ 对 $V$ 的基成立）；
- 更强地 $A(V)\subseteq V$（$A v_1=0$、$A v_2=-v_2$，在 $K_0$ 坐标下）；
- 但 $(5a)(5b)$ 成立（见证 $L$ 通过 `check_candidate`）。
所以“$V$ 不变 + $\omega>0$ ⇒ 铅笔秩降”是**假**的；$A(K_0)\not\subseteq K_0$ 时铅笔可以好。

## 更正后的结论

- **正确**：全局 $A(K_0)\subseteq K_0$、$0<\omega<k$ ⇒ 不可行（205，专家确认）；
- **正确**：$A(V)\subseteq K_0$、$\omega>0$ ⇒ $A(V)\subseteq V$（局部不变性）；
- **错误**：局部不变性 ⇒ 铅笔坏；
- **错误**：专家 64 号 §4/§5.1 的“可行正秩 ⇒ $A(V)\not\subseteq K_0$”；
- **因此**：不变子空间乘法 gadget **未必**被堵死——只要 $A(K_0)\not\subseteq K_0$（避开全局定理），
  同时让候选 $V$ 满足 $A(V)\subseteq K_0$（从而不变性方程成立）。

## 对 gadget 路线的影响

新的设计目标：
1. $A(K_0)\not\subseteq K_0$（全局定理不适用）；
2. 存在不变 $V$（$A(V)\subseteq V$）使 $A(V)\subseteq K_0$（泄漏 $J_V=0$ 对该 $V$）；
3. 铅笔在这类 $V$ 上可以好（seed 10 表明局部不变 + 全局泄漏可行）；
4. 构造时需保证 $K_0$ 的维数与 gadget chart 兼容（泄漏块会改变 $K_0=\ker[C;CA]$，需重新安排）。

## 进展

* 更正了 207/203 的局部泄漏结论；
* 给出 seed 10 反例；
* 重新打开“不变子空间 gadget”路线（条件是 $A(K_0)\not\subseteq K_0$）。

## 最终结论

* 局部泄漏刚性只有“不变性”部分成立；铅笔部分需要全局不变；
* 专家的强结论需修正；
* 不变子空间 gadget 仍可能，只要全局 $A(K_0)\not\subseteq K_0$。

## 放弃原因

* 未构造满足 1–4 的 gadget 实例；
* 未研究泄漏块如何改变 $K_0$；
* 未与专家确认该更正。

## 残留价值

* 一个明确的更正与反例；
* 重新打开 gadget 路线的条件；
* 为下一轮构造指明目标。

## 相关文件

* [attempts/207](207_64_verdict_implementation.md)（被更正）
* [attempts/203](203_invariance_theorem.md)
* [attempts/205](205_AinvK0_impossible.md)（全局定理，仍成立）
* [attempts/200](200_multiplication_gadget.md)

## 状态

* 更正：**[已证-纸面 + 精确反例，M2]**。
* 新 gadget 构造：**[未做]**。
