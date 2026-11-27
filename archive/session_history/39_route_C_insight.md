# 39 — D4 完成后的桥接：障碍的精确定位 + ⭐ **路 C 的关键洞察**

> 承接 [history/37](37_D4_progress.md)、[38](38_bridge_obstacle.md)。

---

## 0. 一句话

$$\boxed{\ \textbf{D4 已完成}\ ✓\ ;\quad \textbf{桥接障碍精确定位}\ ✓\ ;\quad ⭐\ \textbf{路 C（改假设为}\ F=\Lambda H\text{）是关键突破口}\ }$$

---

## 1. ✅ D4 已完成（回顾）

`MyProof/Theorems/D4.lean`（**0 error**，已并入主库 **18118 jobs**）：
$$T,S_1,S_2,S_3:P\to V,\quad\operatorname{range}T\subseteq\textstyle\sum\operatorname{range}S_i
\Longrightarrow\exists\Lambda,G_0,G_1:\ \mathbf{P\to P},\ T=S_1\Lambda+S_2G_0+S_3G_1$$

---

## 2. 🔴 桥接障碍的**精确形式**（本轮）

$$\textbf{D4}：\Lambda,G_0,G_1\ \textbf{陪域相同}\ (\text{都是}\ P)$$
$$\textbf{(A) 的分解}：\Lambda:W\to W,\quad \mathbf{G_0:W\to G},\quad \mathbf{G_1:W\to G}\ \textbf{陪域各异}$$

$$\text{根源}：(A)\ \text{中三个映射是}\ \mathcal L:W\to W,\ C:W\to G,\ CA:W\to G$$
$$\text{要让}\ G_0C\ \text{有定义，}G_0\ \text{必须是}\ G\to W\ ——\text{与}\ \Lambda:W\to W\ \text{不同}$$

$$\boxed{\ \textbf{障碍}：\text{D4 的框架是"同一对空间"上的 range 之和 ⟹ 系数同陪域}；}$$
$$\qquad\ \text{而 }(A)\ \text{的分解需要"陪域各异"（因为}\ C,CA\ \text{的陪域与}\ \mathcal L\ \text{不同）}}$$

**这与 [history/38](38_bridge_obstacle.md) 的记录一致**，但**更本质**（是陪域而非源空间的问题）。

---

## 3. ⭐ 关键洞察（本轮最重要的发现）

### 3.1 `c6'_conditional` 到底**怎么用**分解？

看 `Theorems/C6.lean` 的证明：
```lean
have hFH := F_eq_Lam_comp_H ... hA hN hN2   -- F = Λ ∘ H
have hzero : Lam.comp (L.comp Nmap) = 0 := hFH ▸ hpi
exact S_fails_of_comp_eq_zero ... hzero hne
```

$$\text{即：分解}\ (A)\ \text{只被用来推出}\ \mathbf{F=\Lambda H}\ ;\quad G_0,G_1\ \text{仅用于"消去}\ CN=CAN=0$$

### 3.2 ⟹ **路 C：把假设改为 "$\exists\Lambda,\ F=\Lambda H$"**

$$\textbf{注意}：\ F=L\,A\,N\ \text{与}\ H=L\,N\ \text{都是可计算的矩阵，}$$
$$\textbf{而}\ \Lambda\ \text{只以"}\ F=\Lambda H\ \text{"的方式出现} \Longrightarrow\ \text{分解中} G_0,G_1\ \text{完全不需要}\ \checkmark$$

$$\Longrightarrow\ \textbf{把 c6′ 的假设}\ \texttt{hA}\ \text{换成}\ \exists\Lambda,\ F=\Lambda H
\ \Longrightarrow\ \textbf{绕开桥接障碍}\ \checkmark$$

### 3.3 为什么这仍然"够用"

$$\text{数学上}：\ \exists\Lambda,\ F=\Lambda H\ \text{是}\ (A)\ \text{的}\ \textbf{必要条件}\ \text{（由分解右乘}\ N\ \text{得到）}$$
$$\text{且}\ \textbf{充分}：\ \text{c6′ 的结论只依赖这一条}\ \checkmark$$

$$\text{但}：\ \text{要证"}\ \exists\Lambda,F=\Lambda H\ \text{"}\ \textbf{仍需要分解}\ \text{——除非能从 (A) 直接推出它}$$

### 3.4 ⭐ 更进一步：能否**直接从 (A)** 推出 $\exists\Lambda,\ F=\Lambda H$？

$$(A)：\operatorname{range}(L\circ A)\subseteq\operatorname{range}L+\operatorname{range}C+\operatorname{range}(C\circ A)\quad(\text{原空间})$$
$$\text{限定到}\ \ker N\ \text{上}：\text{由于}\ CN=CAN=0\ \text{（}N\ \text{映到}\ \ker C\sqcap\ker(CA)\text{）}$$
$$\Longrightarrow\ \text{在}\ \operatorname{range}N\ \text{上，}(L\circ A)\ \text{的像含于}\ \operatorname{range}L\ \text{在}\ N\ \text{上的限制} + 0 + 0$$

$$\Longrightarrow\ \textbf{只需证"}\ \operatorname{range}(L\circ A\circ N)\subseteq\operatorname{range}(L\circ N)\ \text{"}
\ \Longrightarrow\ \exists\Lambda,\ F=\Lambda H\ \checkmark$$

$$\textbf{而这是}\ \textbf{两列矩阵的 range 包含}\ \text{——}\text{可用}\ \texttt{Submodule}.\texttt{le\_iff} + \text{线性代数}\ \text{直接处理}\ \checkmark$$

---

## 4. 下一步（明确）

| 序 | 动作 | 说明 |
|---|---|---|
| **1** ⭐ | **证** $\operatorname{range}(L\circ A\circ N)\subseteq\operatorname{range}(L\circ N)$ **from (A)** | 这是路 C 的**核心引理**；纯线性代数 |
| **2** | 用它得 $\exists\Lambda,\ F=\Lambda H$（**不需要** $G_0,G_1$）| 绕过桥接障碍 ✓ |
| **3** | 把 `c6'_conditional` 的 `hA` 换成该假设 ⟹ **c6′ 的形式更干净** | |
| **4** | 结合 T12 ⟹ 情形 II 恒 NO | 最终目标 |

### 4.1 引理 1 的数学内容

$$N\ \text{映到}\ \ker C\sqcap\ker(CA)\ \Longrightarrow\ CN=0,\ CAN=0$$
$$(A)：\operatorname{range}(LA)\subseteq\operatorname{range}L+\operatorname{range}C+\operatorname{range}(CA)$$
$$\text{取}\ y\ \text{在}\ \operatorname{range}N\ \text{上}：\ LAy=L(Ay)$$
$$\text{若}\ Ay\in\ker C\sqcap\ker(CA)\ \text{（即}\ Ay\in\operatorname{range}N\text{）}，\text{则}\ CAy=0,\ Cy=0\ \text{对}\ y\in\operatorname{range}N$$
$$\Longrightarrow\ LAy\in\operatorname{range}L\ \Longrightarrow\ \operatorname{range}(LA|_{\operatorname{range}N})\subseteq\operatorname{range}(L|_{\operatorname{range}N})\ \checkmark$$

$$\textbf{即}：\operatorname{range}(L\circ A\circ N)\subseteq\operatorname{range}(L\circ N)\ \checkmark$$

### 4.2 ⚠️ 需要的前提

$$\text{上面的推导用了}\ \mathbf{A(\operatorname{range}N)\subseteq\operatorname{range}N}\ (\text{即}\ \operatorname{range}N\ \text{是}\ A\text{-不变的})$$
$$\text{这正是}\ \texttt{c6'\_final}\ \text{的假设}\ \texttt{hfact}:\ A\circ N=N\circ A'\ \text{（即"}\ A\ \text{保持参数化子空间"）}\ ✓$$
$$\text{且}\ C\circ A\circ N=0\ \text{（即}\ \texttt{hN2}）\ ✓$$

$$\Longrightarrow\ \textbf{引理 1 在}\ \texttt{c6'\_final}\ \text{的假设下成立}\ \checkmark$$

---

## 5. 本轮产出

| 文件 | 内容 |
|---|---|
| **本文** | 障碍的精确定位 + **路 C 的关键洞察** + 引理 1 的数学内容 |
| `scripts/lean/C6_bridge.lean` | 障碍的 Lean 文档（0 error）|
| `scripts/lean/C6_dual.lean` | 直和类型测试（0 error）|
| `MyProof/Theorems/D4.lean` ★ | D4 的 Lean 证明（已并入主库）|
| [DIRECTIONS.md](docs/DIRECTIONS_2026-10-18.md) | 所有方向的索引 |
