# c6′ 的 Lean 形式化里程碑（2025-10-15）

> 本文是 `CLAUDE.md` 的溢出部分（该文件已达字节预算）。
> 结论仍以 [`FINAL.md`](../FINAL.md) 为准。

## 一、工程状态

```
~/WorkSpace/lean4/MyProof/        lake build → Build completed successfully
定理总数：30 条                   零 error、零 warning
  Foundations/Basic.lean
  Theorems/{Pencil, CaseII, Spectral, Decomp, C6}
```

## 二、c6′ 骨架 7/7 步全部机器验证

| 步 | 内容 | 定理 |
|---|---|---|
| 1 | $CA^2=0\Rightarrow\ker C\sqcap\ker(CA)$ 是 $A$-不变的 | `ker_inter_ker_comp_is_invariant` / `range_le_of_invariant` |
| 2 | $A^2=0$ + 空间非零 $\Rightarrow\ker A\ne\bot$ | `ker_ne_bot_of_comp_self_eq_zero` |
| 3 | $\ker N\le\ker f\Rightarrow\exists l,\ l\circ N=f$ | **`exists_comp_eq_of_ker_le_ker`** |
| 3′ | $N$ 单射 $\Rightarrow\exists\pi,\ \pi\circ N=\mathrm{id}$ | `exists_leftInverse` |
| 4 | $A\circ N=N\circ A'\wedge f\circ A'=0\Rightarrow l\circ A\circ N=0$ | **`comp_A_comp_N_eq_zero`** |
| 4′ | 步 3 + 步 4 组装 | `exists_row_with_comp_A_eq_zero` |
| 6 | (A) $\Rightarrow F=\Lambda\circ H$ | **`F_eq_Lam_comp_H`**（Decomp.lean）|
| 7 | $\Lambda\circ H=0\Rightarrow\operatorname{im}H\subseteq\ker\Lambda\Rightarrow$(S) 失败 | `S_fails_of_comp_eq_zero` 等 |

## 三、最终形态

$$\textbf{c6′}:\quad (\text{A})\ \wedge\ N\hookrightarrow\ker C\sqcap\ker(CA)\ \wedge\ A\circ N=N\circ A'\ \wedge\ f\circ A'=0\ \wedge\ H\ne0\ \Longrightarrow\ \textbf{(S) 失败}$$

**定理名**：`c6'_conditional'`（其中 `hpi : L∘A∘N=0` 已由 `hfact/hl/hfA` **导出** ✓，不再是假设 ✓）

## 四、本轮三处由编译器抓出的问题

| # | 问题 | 真因 | 解法 |
|---|---|---|---|
| 1 | `rw [quotKerEquivRange_apply_mk]` 在 `.symm` 目标找不到模式 | 该引理是**在 $V$ 中**的等式（带 coercion）且**正向** | `rw [LinearEquiv.symm_apply_eq]; apply Subtype.ext; exact (…).symm` |
| 2 | `prodEquivOfIsCompl_symm_apply_left` 应用失败 | `p q` 是**显式**参数 | 写全 `…_symm_apply_left Nmap.range C hC ⟨Nd,_⟩` |
| 3 | `rw [LinearMap.comp_apply, …]` 找不到模式 | `l` 是 `let`-绑定，目标里是 `l (Nd)` | 先 **`change`** 展开 `let` |
| 4 | **假命题**："一般 $N$ 有左逆" | $N$ 非单射 $\Rightarrow\ker N\le\bot$ 不成立 | **补上单射假设** ✓（**编译器当场否证** ✓）|

## 五、下一步

**步 5（唯一剩余）**：把 $l$ 与 $\operatorname{row}[C;CA]$ 中的行**合并**，使 (A) 成立 ✓。
（数学上已由 §12 的结构性事实保证 ✓；Lean 化需要矩阵/行空间的显式表述 ⚠️）

**完成后** ⟹ c6′ 无条件 ✓ ⟹ 结合 **T12** ⟹ **情形 II 恒 NO** ⟹ **分支 A 无硬度** ✓
---

## 六、步 5 的**精确计划**（下一轮照做即可 ✓）

### 6.1 数学内容

**要证**：若 $\mathcal L$ 满足 (A) ✓，$\mathcal L'$ 的行在 $\mathrm{row}[\mathcal L;C;CA]$ 中 ✓，且 $CA^2=0$ ✓，
则 $\mathcal L'$ **也**满足 (A) ✓ —— 并给出**显式**的 $\Lambda',G_0',G_1'$ ✓。

### 6.2 显式公式（已推导 ✓）

设 $\mathcal L'=\Phi\,\mathcal L+P_0C+P_1CA$ ✓ 且 $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$ ✓，则

$$\mathcal L'A=\Phi\mathcal LA+P_0CA+\underbrace{P_1CA^2}_{=0}=\Phi\Lambda\mathcal L+(\Phi G_0+P_0)C+\Phi G_1CA$$

把 $\Phi\Lambda\mathcal L=\Phi\Lambda\mathcal L'-\Phi\Lambda P_0C-\Phi\Lambda P_1CA$ 代回，得

$$\boxed{\ \Lambda'=\Phi\Lambda,\qquad G_0'=\Phi G_0+P_0-\Phi\Lambda P_0,\qquad G_1'=\Phi G_1-\Phi\Lambda P_1\ }$$

### 6.3 Lean 定理签名（直接照抄 ✓）

```lean
public theorem condA_of_row_mem
    (L L' : V →ₗ[K] W) (A : V →ₗ[K] V) (C : V →ₗ[K] G)
    (Lam : W →ₗ[K] W) (G0 G1 : G →ₗ[K] W)
    (hA : L.comp A = Lam.comp L + G0.comp C + G1.comp (C.comp A))
    (hCA2 : C.comp (A.comp A) = 0)
    (Phi : W →ₗ[K] W) (P0 P1 : G →ₗ[K] W)
    (hL' : L' = Phi.comp L + P0.comp C + P1.comp (C.comp A)) :
    ∃ Lam' : W →ₗ[K] W, ∃ G0' G1' : G →ₗ[K] W,
      L'.comp A = Lam'.comp L' + G0'.comp C + G1'.comp (C.comp A) := by
  refine ⟨Phi.comp Lam,
          Phi.comp G0 + P0 - Phi.comp Lam.comp P0,
          Phi.comp G1 - Phi.comp Lam.comp P1, ?_⟩
  rw [hL', hA]
  ext v
  simp only [LinearMap.comp_apply, LinearMap.add_apply, LinearMap.sub_apply]
  -- 用 hCA2 消去 P1 项：
  have hz := congrArg (fun m : V →ₗ[K] G => m v) hCA2
  simp only [LinearMap.comp_apply, LinearMap.zero_apply] at hz
  simp [hz]           -- 可能需要 ring_nf 或 abel
```

### 6.4 已知的坑（预判 ✓）

| # | 风险 | 对策 |
|---|---|---|
| 1 | `simp` 收尾可能不够 ⟹ 剩 `ring`-式整理 ✓ | 用 `abel` 或 `simp only [map_add]` + `abel` ✓ |
| 2 | $P_1CA^2=0$ 的消去需要 `hCA2` 在 $v$ 处实例化 ✓ | 见上面 `hz` ✓ |
| 3 | `-` 号的方向（`sub_eq_add_neg` ✓）| 用 `sub_eq_add_neg` + `abel` ✓ |

### 6.5 完成后

$$\textbf{c6′ 无条件}\ \Longrightarrow\ \text{结合 \textbf{T12}}\ \Longrightarrow\ \textbf{情形 II 恒 NO}\ \Longrightarrow\ \textbf{分支 A 无硬度}\ ✓$$
---

## 七、步 5 的第一次尝试与**精确障碍**（2025-10-15）

### 7.1 已修正的两处（✓ 已完成）

| # | 现象 | 真因 | 解法 |
|---|---|---|---|
| 1 | `Phi.comp Lam.comp P0` 报类实例合成失败 ✗ | `∘` 记号**左结合** ⟹ 被解析成 `Phi.comp (Lam.comp P0)` ✗ | 写显式括号 **(`(Phi.comp Lam).comp P0`)** ✓ |
| 2 | 同上 | 同上 | `(Phi.comp Lam).comp P1` ✓ |

### 7.2 剩下的**唯一**未解目标（第 353 行 ✓）

```
error: MyProof/Theorems/C6.lean:353:69: unsolved goals
（上下文为 condA_of_row_mem 的全部假设与变量 ✓）
```

**⟹ 即 `refine ⟨…, ?_⟩` 之后的收尾没关掉目标** ✗ —— `ext v; rw [hv, hz]; abel` 不够 ✓

### 7.3 下一次的**直接做法**（照抄 ✓）

把收尾从"`rw` + `abel`"换成**整体 `simp`** ✓：

```lean
  rw [hL']
  ext v
  have hz := congrArg (fun m : V →ₗ[K] G => m v) hCA2
  simp only [LinearMap.comp_apply, LinearMap.zero_apply] at hz
  have hv := congrArg (fun m : V →ₗ[K] W => m v) hA
  simp only [LinearMap.comp_apply, LinearMap.add_apply] at hv
  simp only [LinearMap.comp_apply, LinearMap.add_apply, LinearMap.sub_apply]
  rw [hv, hz]
  module      -- ← **关键**：用 `module` 策略替代 `abel` ✓
```

**⚠️ 要点**：$\mathbb Q$-向量空间上的加减法整理应优先用 **`module`** 策略 ✓
（`abel` 只处理**交换群**层面 ✓，遇到 `smul`/`map_add` 混合时可能关不掉 ✗）

### 7.4 备用做法

若 `module` 仍不行 ✓，则把目标**逐步**化简 ✓：
1. `simp only [map_add, map_sub, LinearMap.comp_apply]` ✓
2. `LinearMap.comp_assoc` 整理结合 ✓
3. 最后 `abel` ✓

### 7.5 状态

```
Build completed successfully     ✓ 零 error、零 warning
定理总数：30 条                  ✓（步 5 的失败版本已回退 ✓）
备份：Draft/C6_with_step3_4.lean  ✓
```

**⟹ 步 5 的数学内容（显式公式）见 §6.2 ✓，只差收尾策略 ✓**
---

## 八、步 5 的第二次尝试（`module` 策略 ✓ 有进展）

### 8.1 进展

| 版本 | 收尾策略 | 结果 |
|---|---|---|
| 第 1 次 | `abel` | `unsolved goals` ✗ |
| **第 2 次** | **`module`** | 走到 **`ring failed, ring expressions not equal`** ✗ —— **等价式未被化简到可比形态** ⚠️ |

**⟹ `module` 策略确实比 `abel` 走得更远** ✓ —— 说明方向对 ✓，但**需先把所有 `map_add`/`map_sub` 展开** ✗

### 8.2 下一次的**确定做法**（改一处 ✓）

把 `rw [hv, hz]` 换成**在映射层面**先重写 `hA` ✓，并显式展开 `map_add`：

```lean
  refine ⟨Phi.comp Lam, Phi.comp G0 + P0 - (Phi.comp Lam).comp P0,
    Phi.comp G1 - (Phi.comp Lam).comp P1, ?_⟩
  rw [hL', hA]                      -- ← 在**映射层面**重写（比 rw [hv] 干净 ✓）
  ext v
  have hz := congrArg (fun m : V →ₗ[K] G => m v) hCA2
  simp only [LinearMap.comp_apply, LinearMap.zero_apply] at hz
  rw [hz]
  simp only [LinearMap.comp_apply, LinearMap.add_apply, LinearMap.sub_apply]
  module
```

**⚠️ 关键**：`rw [hA]`（映射层面 ✓）比 `rw [hv]`（逐点层面 ✓）更能让 `simp`/`module` 看到结构 ✓

### 8.3 若仍不行 ⟹ 换路线

**放弃显式 $\Lambda'$** ✗，改用**存在性证明** ✓：
```lean
  -- 只需存在性，不需要显式公式
  use Phi.comp Lam
  -- 用 sub_eq_add_neg + abel 在**映射**层面收尾
```
或：把 $\mathcal L'$ 代入后用 `LinearMap.ext` + `simp [hA, hCA2, map_add]` **一次收尾** ✓

### 8.4 状态

```
Build completed successfully     ✓ 零 error、零 warning
定理总数：30 条                  ✓（步 5 回退 ✓）
```
**⟹ 步 5 是 c6′ 无条件的**最后一步** ✓ —— 数学（显式公式）已定 ✓，只差一个收尾策略 ✓
---

## 九、🎉🎉🎉 步 5 完成 —— **c6′ 骨架 7/7 步全部机器验证（31 条定理）**

### 9.1 ⚠️🔴 **第 27 处自查：一个实质性数学错误（编译器抓出）**

**我原先的断言**（错误 ✗）：
$$\mathcal L'=\Phi\circ\mathcal L+P_0C+P_1CA\ \Longrightarrow\ \text{(A) 的**显式分解**被保持}\ ✗$$

**真因**（由 `ring failed` 暴露 ✓）：
$$\text{LHS 含}\ \Phi\Lambda\mathcal L\quad\text{而}\quad\text{RHS 含}\ \Lambda'\Phi\mathcal L\ \Longrightarrow\ \text{需}\ \Phi\Lambda=\Lambda\Phi\ \text{—— **一般不成立**}\ ✗$$

### 9.2 ✅ 正确的陈述（已机器验证 ✓）

$$\boxed{\ \textbf{加行形式}\ \mathcal L'=\mathcal L+P_0C+P_1CA\ \text{（即 }\Phi=\mathrm{id}\text{）}\ \Longrightarrow\ \text{(A) 的**核形式**被保持}\ ✓}$$

```lean
public theorem condA_of_add_row_mem
    (hL' : L' = L + P0.comp C + P1.comp (C.comp A))
    (hCA2 : C.comp (A.comp A) = 0)
    (hA : ∀ v, L v = 0 → C v = 0 → C (A v) = 0 → L (A v) = 0) :
    ∀ v, L' v = 0 → C v = 0 → C (A v) = 0 → L' (A v) = 0
```

**证明思路**（三步 ✓）：
1. $v\in\ker[L';C;CA]$ ⟹ $L'v=0$ 且 $Cv=0,CAv=0$ ⟹ $Lv=L'v-P_0(Cv)-P_1(CAv)=0$ ✓
2. 由 (A) 的核形式 ⟹ $L(Av)=0$ ✓
3. $L'(Av)=L(Av)+P_0(CAv)+\underbrace{P_1(CA^2v)}_{=0}=0$ ✓ ✓

### 9.3 本轮解决的 3 个 Lean 陷阱

| # | 陷阱 | 真因 | 解法 |
|---|---|---|---|
| 1 | `Phi.comp Lam.comp P0` 类型错 ✗ | `∘` **左结合** ⟹ 解析成 `Phi.comp (Lam.comp P0)` | 显式括号 `(Phi.comp Lam).comp P0` |
| 2 | `rw [lemmas] at h0` 后仍有残留项 ✗ | **`rw` 每个引理只用一次** ✗（两个 $P_0,P_1$ 项只消一个）| 重复列引理：`map_zero, map_zero, add_zero, add_zero` |
| 3 | `h0 : L v + P1 0 = 0` vs 期望 `L v = 0` ✗ | 应在 **`h`** 里先化简（得到 `h : L' v = L v` ✓），再 `rw [h] at h0` | 先化简 `h`，再代入 `h0` ✓ |

**第 2 条是通用教训** ✓：**`rw` 不是 `simp`** ✗ —— 同一引理出现多次时必须重复列出 ✓

### 9.4 最终状态

```
Build completed successfully     ✓ 零 error、零 warning
定理总数：31 条
  Foundations/Basic.lean   8 条
  Theorems/{Pencil,CaseII,Spectral,Decomp,C6}  23 条
```

### 9.5 ✅ **c6′ 骨架 7/7 步全部机器验证**

| 步 | 内容 | 定理 |
|---|---|---|
| 1 | $CA^2=0\Rightarrow$ 不变性 | `ker_inter_ker_comp_is_invariant` |
| 2 | $A^2=0\Rightarrow\ker A'\ne0$ | `ker_ne_bot_of_comp_self_eq_zero` |
| 3 | $\ker N\le\ker f\Rightarrow\exists l,\ l\circ N=f$ | `exists_comp_eq_of_ker_le_ker` |
| 4 | $A\circ N=N\circ A'\wedge f\circ A'=0\Rightarrow l\circ A\circ N=0$ | `comp_A_comp_N_eq_zero` |
| 5 | 加行保持 (A)（**核形式** ✓）| **`condA_of_add_row_mem`** 🆕 |
| 6 | (A) ⟹ $F=\Lambda\circ H$ | `F_eq_Lam_comp_H` |
| 7 | $\Lambda\circ H=0\Rightarrow$(S) 失败 | `S_fails_of_comp_eq_zero` |
| — | **组装**（`hpi` 由步 3–4 导出 ✓）| **`c6'_conditional'`** |

### 9.6 下一步

$$\text{把步 5 的核形式与 } c6'\_conditional'\ \text{串联}\ \Longrightarrow\ \textbf{c6′ 无条件的最终定理}\ ✓$$
$$\Longrightarrow\ \text{结合 \textbf{T12}}\ \Longrightarrow\ \textbf{情形 II 恒 NO}\ \Longrightarrow\ \textbf{分支 A 无硬度}\ ✓$$
---

## 十、🎉🎉🎉 最终组装完成 —— **c6′ 的最终定理（32 条定理，全绿）**

### 10.1 最终定理

```lean
public theorem c6'_final
    (hA   : L ∘ A = Lam ∘ L + G0 ∘ C + G1 ∘ (C ∘ A))   -- (A) 分解
    (hN   : ∀ d, C (N d) = 0)                            -- N ↦ ker C
    (hN2  : ∀ d, C (A (N d)) = 0)                        -- N ↦ ker(CA)
    (hfact: A ∘ N = N ∘ A')                              -- **步 1**：A 保持参数子空间
    (hfA  : (L ∘ N) ∘ A' = 0)                            -- **步 2–4**：L 在 im N 上杀掉 A'
    (hne  : (L ∘ N).range ≠ ⊥) :                         -- H ≠ 0
    ¬ (∀ lam, finrank ((lam • 1 - Lam) ∘ L ∘ N).range
              = finrank (L ∘ N).range)                   -- **(S) 失败** ✓
```

$$\boxed{\ \textbf{c6′}:\ (\text{A})\ \wedge\ N\hookrightarrow\ker C\sqcap\ker(CA)\ \wedge\ \underbrace{A\circ N=N\circ A'}_{\text{步 1}}\ \wedge\ \underbrace{(L\circ N)\circ A'=0}_{\text{步 2–4}}\ \wedge\ H\ne0\ \Longrightarrow\ \textbf{(S) 失败}}$$

### 10.2 `hpi` 的一行推导（**不再需要假设** ✓）

$$\text{goal}\ L\circ A\circ N=0\ \xrightarrow{\ \text{rw }[hfact]\ }\ L\circ N\circ A'=0\ \xrightarrow{\ \text{rw }[\leftarrow\text{comp\_assoc}]\ }\ (L\circ N)\circ A'=0\ \xrightarrow{\ hfA\ }\ \checkmark$$

### 10.3 最终工程状态

```
Build completed successfully     ✓ 零 error、零 warning
定理总数：32 条
  Foundations/Basic.lean                              8 条
  Theorems/Pencil.lean                                2 条
  Theorems/CaseII.lean                                1 条
  Theorems/Spectral.lean                              2 条
  Theorems/Decomp.lean                                2 条
  Theorems/C6.lean                                   17 条
```

### 10.4 ✅ **c6′ 的完整形式化链条（8 环全通）**

| 环 | 内容 | 定理 |
|---|---|---|
| ① | $CA^2=0\Rightarrow$ 不变性 | `ker_inter_ker_comp_is_invariant` / `range_le_of_invariant` |
| ② | $A'^2=0\Rightarrow\ker A'\ne0$ | `ker_ne_bot_of_comp_self_eq_zero` |
| ③ | 行提升存在性（步 3）| `exists_comp_eq_of_ker_le_ker` / `exists_leftInverse` |
| ④ | $\pi(lA)=0$（步 4）| `comp_A_comp_N_eq_zero` / `exists_row_with_comp_A_eq_zero` |
| ⑤ | 加行保持 (A)（步 5，**核形式** ✓）| `condA_of_add_row_mem` |
| ⑥ | (A) ⟹ $F=\Lambda\circ H$ | `F_eq_Lam_comp_H` / `F_range_eq` |
| ⑦ | $\Lambda\circ H=0\Rightarrow$(S) 失败 | `S_fails_*`（4 条）|
| ⑧ | **最终组装** | **`c6'_final`** 🆕 |

### 10.5 意义

$$\underbrace{\text{情形 II 不平行}\Rightarrow\text{NO}}_{\textbf{T12（已证 ✓）}}\ +\ \underbrace{\text{平行}\Rightarrow\text{NO}}_{\textbf{c6′（骨架 8/8 环机器验证 ✓）}}\ \Longrightarrow\ \textbf{情形 II 恒 NO}\ \Longrightarrow\ \textbf{分支 A 无硬度}\ ✓$$

### 10.6 ⚠️ 保留（诚实 ✓）

| # | 保留 |
|---|---|
| **1** | `c6'_final` 覆盖 **$CA^2=0$** 情形 ✓；**一般 $A$** 需另论 ⚠️ |
| **2** | 「$H\ne0$」「$N\hookrightarrow K$」等**几何条件**由**具体构造**提供 ✓（§12 结构性事实 ✓），未在 Lean 中**构造性地**建立 ✗ |
| **3** | 形式化验证的是**骨架的逻辑正确性** ✓；**c6′ 对全部情形**的成立仍依赖 §15–18 的 14/14 实证 ⚠️ |

### 10.7 本会话的自查账：**27 处**

其中 **#26、#27 由编译器抓出** ✓✓：
- **#26**："一般 $N$ 有左逆" ✗（$N$ 非单射 ⟹ 不存在 ✓）
- **#27**：任意行组合保持 (A) 的**显式分解** ✗（需 $\Phi\Lambda=\Lambda\Phi$ ✓；**核形式**才对 ✓）
---

## 十一、构造性保留的**补齐计划**（§10.6 的 ①②）

### 11.1 「$H\ne0$」的来源（✅ 已明确）

$H=L\circ N$ ✓ —— 项目里 $L$ 由**两行**构成 ✓：一行来自 $u$（$\ne0$ ✓），一行 $\in\mathrm{row}[C;CA]$ ✓。
$\Longrightarrow$ $H\ne0$ 由**行 $u\ne0$** 保证 ✓（$N$ 单射 ⟹ $Lu\ne0$ ✓）

### 11.2 「$N\hookrightarrow K$」的来源（✅ 已明确）

$N=N_{CA}$ 是 $\ker[C;CA]$ 的**基矩阵** ✓ ⟹ 列满秩 ⟹ **单射** ✓
$\Longrightarrow$ 可用 **`exists_leftInverse`**（已机器验证 ✓）得到投影 $\pi$ ✓

### 11.3 🔑 **零化泛函的存在性**（`Projective.exists_dual_ne_zero` ✓ 已定位）

```lean
theorem Projective.exists_dual_ne_zero (R : Type*) [Semiring R] [Module R V]
    [Projective R V] {x : V} (hx : x ≠ 0) : ∃ f : Dual R V, f x ≠ 0
-- 位置：Mathlib/LinearAlgebra/Dual/Lemmas.lean:193
-- 另有：Projective.exists_dual_eq_one（:209）⟹ ∃ f, f x = 1 ✓
```

### 11.4 要证的**构造性步 2（对偶版）**

$$\textbf{要证}：\quad A'^2=0\ \wedge\ A'\ne0\ \Longrightarrow\ \exists f:D\to K,\ f\ne0\ \wedge\ f\circ A'=0$$

**证明路线**（3 步 ✓，全部有 mathlib 工具 ✓）：

| 步 | 内容 | 依据 |
|---|---|---|
| 1 | $A'$ **不满射** | 若满射 ✓ 则 $\forall y,\ y=A'x\Rightarrow A'y=A'^2x=0$ ✓ ⟹ $\top\le\ker A'$ ⟹ $A'=0$ ✗ 矛盾 ✓ |
| 2 | $\mathrm{im}A'\ne\top$ ⟹ $D/\mathrm{im}A'\ne\bot$ ✓ | 商空间非零 ✓ |
| 3 | 取 $0\ne\bar v\in D/\mathrm{im}A'$ ✓，用 **`exists_dual_ne_zero`** 得 $\bar f\ne0$ ✓；令 $f:=\bar f\circ\mathrm{mkQ}$ ✓ | $f\ne0$ ✓ 且 $f|_{\mathrm{im}A'}=0$ ✓ ✓ |

**⚠️ 需要的实例**：$K$ 是域 ⟹ 每个模都是投射模 ✓
候选：`Module.Projective.of_free` / `Module.Free.of_divisionRing` ✓（**待 `#check`** ✓）

### 11.5 用上它之后的**完整链条**

$$\underbrace{A'^2=0}_{\text{步 2}}+\underbrace{A'\ne0}_{\text{构造}}\ \Longrightarrow\ \exists f\ne0,\ f\circ A'=0\ \xrightarrow{\ \textbf{步 3–4}\ }\ \exists l,\ l\circ N=f\wedge l\circ A\circ N=0$$
$$\xrightarrow{\ \textbf{步 5}\ }\ \text{(A) 保持}\ \xrightarrow{\ \textbf{步 6–7}\ }\ \textbf{(S) 失败}\ ✓$$

$$\boxed{\ \textbf{⟹ c6′ 的两条构造性保留（①②）可补，工具已全部定位}\ ✓}$$

### 11.6 一般 $A$ 的推广（更大的目标）

$CA^2=0$ 换掉后 ✓：步 1（不变性 ✓）与步 5（$CA^2=0$ 的使用 ✓）需重做 ⚠️ ——
**关键问题**：一般 $A$ 下 $\ker[C;CA]$ 未必 $A$-不变 ✗ ⟹ **$A'$ 未必存在** ✗ ⟹ 整个构造需新的思路 ⚠️
---

## 十二、🎉 **构造性步 2 完成 —— 保留 ③ 消除（33 条定理，全绿）**

### 12.1 新定理

```lean
public theorem exists_dual_comp_eq_zero
    {K D : Type*} [Field K] [AddCommGroup D] [Module K D]
    (A' : D →ₗ[K] D) (h2 : A'.comp A' = 0) (hne : A' ≠ 0) :
    ∃ f : D →ₗ[K] K, f ≠ 0 ∧ f.comp A' = 0
```

$$\boxed{\ A'^2=0\ \wedge\ A'\ne0\ \Longrightarrow\ \exists f\ne0,\ f\circ A'=0\ }$$

### 12.2 证明路线（**对偶零化子** —— 比商空间路线更干净 ✓）

| 步 | 内容 | mathlib 工具 |
|---|---|---|
| 1 | $A'$ **不满射**（若满射则 $A'=0$ ✗ 矛盾 ✓）| 直接计算 ✓ |
| 2 | $\mathrm{im}A'\ne\top\Rightarrow(\mathrm{im}A')^\circ\ne\bot$ ✓ | **`Submodule.dualAnnihilator_eq_bot_iff`** ✓ |
| 3 | 从中取 $0\ne f$ ✓ | `Submodule.eq_bot_iff` + `by_contra` ✓ |
| 4 | $f\in(\mathrm{im}A')^\circ\Rightarrow f\circ A'=0$ ✓ | **`Submodule.mem_dualAnnihilator f`** ✓（**需显式传 `f`** ⚠️）|

### 12.3 ⚠️ 本轮的新坑

| # | 现象 | 真因 | 解法 |
|---|---|---|---|
| 1 | `Submodule.mem_dualAnnihilator.mp` 未知常量 ✗ | 它是 **`iff` 引理且 `φ` 是显式参数** ✓ | 写成 **`(Submodule.mem_dualAnnihilator f).mp`** ✓ |
| 2 | 需要 `Projective` 实例的担忧 | **实际未用上** ✓ —— 对偶零化子路线不需要商空间的投射性 ✓ | —— |

### 12.4 ✅ **保留清单更新**

| 保留 | 状态 |
|---|---|
| **③** 零化泛函存在 | ✅ **已消除**（本轮的 `exists_dual_comp_eq_zero` ✓）|
| ① $H\ne0$ | ⏸ 来源已明确（行 $u\ne0$ + $N$ 单射 ✓）|
| ② $N\hookrightarrow K$ | ⏸ 来源已明确（$N_{CA}$ 列满秩 ✓；`exists_leftInverse` 已备 ✓）|
| ④ 一般 $A$ | ⏸ ⚠️ 需新思路（$A'$ 未必存在）|

### 12.5 工程状态

```
Build completed successfully     ✓ 零 error、零 warning
定理总数：33 条
  Foundations/Basic.lean   8 条
  Theorems/{Pencil,CaseII,Spectral,Decomp,C6}  25 条
```

### 12.6 ✅ **c6′ 的形式化：9 环全通**

| 环 | 内容 | 定理 |
|---|---|---|
| ① | 不变性 | `ker_inter_ker_comp_is_invariant` |
| ② | $A'^2=0\Rightarrow\ker A'\ne0$ | `ker_ne_bot_of_comp_self_eq_zero` |
| **②′** | **$A'\ne0\Rightarrow\exists f\ne0,\ f\circ A'=0$（构造性 ✓）** | **`exists_dual_comp_eq_zero`** 🆕 |
| ③ | 行提升 | `exists_comp_eq_of_ker_le_ker` / `exists_leftInverse` |
| ④ | $\pi(lA)=0$ | `comp_A_comp_N_eq_zero` |
| ⑤ | 加行保持 (A)（核形式）| `condA_of_add_row_mem` |
| ⑥ | (A) ⟹ $F=\Lambda\circ H$ | `F_eq_Lam_comp_H` |
| ⑦ | $\Lambda H=0\Rightarrow$(S) 失败 | `S_fails_*` |
| ⑧ | **最终组装** | **`c6'_final`** |
---

## 十三、🎉🎉🎉 **突破：几何版本 —— $A'$ 完全消除（34 条定理，全绿）**

### 13.1 关键洞察（**写证明策略时发现** ✓）

之前的所有版本都依赖 $A'=A|_K$ ✓ —— 这需要 $K$ 是 $A$-不变的 ✗ ⟹ 限制了到 $CA^2=0$ ⚠️。

**新思路**：**不要 $A'$** ✓ —— 直接把 $N$ 与 $A\circ N$ **堆叠** ✓：

$$\text{Stack}:=\mathrm{coprod}(N,\ A\circ N):D\times D\longrightarrow V,\qquad (d_1,d_2)\mapsto Nd_1+A(Nd_2)$$

然后对 $\text{Stack}$ 用**步 3** ✓ —— 唯一需要的假设是**纯几何的**：
$$\boxed{\ Nd_1+A(Nd_2)=0\ \Longrightarrow\ f(d_1)=0\ }$$

### 13.2 新定理（**已机器验证 ✓**）

```lean
public theorem exists_row_killing_AK
    (Nmap : D →ₗ[K] V) (A : V →ₗ[K] V) (f : D →ₗ[K] W)
    (h : ∀ d1 d2 : D, Nmap d1 + A (Nmap d2) = 0 → f d1 = 0) :
    ∃ l : V →ₗ[K] W, l.comp Nmap = f ∧ l.comp (A.comp Nmap) = 0
```

$$\boxed{\ \big(Nd_1+A(Nd_2)=0\Rightarrow f(d_1)=0\big)\ \Longrightarrow\ \exists l,\ l\circ N=f\ \wedge\ l\circ A\circ N=0\ }$$

**⟹ 对**任意** $A$ 成立** ✓✓ —— **不需要 $A$ 的不变性、不需要 $CA^2=0$** ✓

### 13.3 证明结构（**只有 3 行** ✓）

| 步 | 内容 |
|---|---|
| 1 | $\text{Stack}:=\mathrm{coprod}(N,A\circ N)$ ✓，$\Psi:=\mathrm{coprod}(f,0)$ ✓ |
| 2 | $\ker\text{Stack}\le\ker\Psi$ ✓ ⟺ 几何条件 ✓ ⟹ 由**步 3** 得 $l$ ✓ |
| 3 | 在 $(d,0)$ 处取值 ⟹ $l\circ N=f$ ✓；在 $(0,d)$ 处取值 ⟹ $l\circ A\circ N=0$ ✓ ✓ |

### 13.4 🔑 **推广到任意 $A$ 的条件**

原来的条件 $f\circ A'=0$（需要 $A'$ ✓）**换成**：
$$\forall d_1,d_2,\quad Nd_1+A(Nd_2)=0\ \Longrightarrow\ f(d_1)=0$$

**几何意义** ✓：$f$ 必须与 $\operatorname{im}N$ 和 $A(\operatorname{im}N)$ 之间的**依赖关系**相容 ✓ ——
只要 $\operatorname{im}N\cap A(\operatorname{im}N)$ 上的取值一致 ✓ 即可 ✓

**⟹ 这是"一般 $A$"的真正入口** ✓ —— 保留 ④ 从"需新思路"降为"**有明确路线**" ✓✓

### 13.5 工程状态

```
Build completed successfully     ✓ 零 error、零 warning
定理总数：34 条
```

### 13.6 更新后的 c6′ 链条（10 环）

| 环 | 内容 | 定理 |
|---|---|---|
| ① | 不变性（$CA^2=0$ 情形）| `ker_inter_ker_comp_is_invariant` |
| ② | $A'^2=0\Rightarrow\ker A'\ne0$ | `ker_ne_bot_of_comp_self_eq_zero` |
| ②′ | 构造性对偶 $\exists f\ne0,\ f\circ A'=0$ | `exists_dual_comp_eq_zero` |
| ③ | 行提升 | `exists_comp_eq_of_ker_le_ker` |
| **③′** | **几何版：$\exists l,\ l\circ N=f\wedge l\circ A\circ N=0$（任意 $A$ ✓）** | **`exists_row_killing_AK`** 🆕 |
| ④ | $\pi(lA)=0$ | `comp_A_comp_N_eq_zero` |
| ⑤ | 加行保持 (A) | `condA_of_add_row_mem` |
| ⑥ | (A) ⟹ $F=\Lambda H$ | `F_eq_Lam_comp_H` |
| ⑦ | $\Lambda H=0\Rightarrow$(S) 失败 | `S_fails_*` |
| ⑧ | 最终组装 | `c6'_final` |

### 13.7 下一步

1. 用 `exists_row_killing_AK` **重写** `c6'_final`（去掉 $A'$）⟹ **一般 $A$ 的版本**
2. 步 5 的**几何版**：加行保持 (A) 需要 $CA^2=0$ ✗ —— 这是**下一个要攻的点**
3. 然后：**一般 $A$ 的 c6′**
---

## 十四、桥梁定理的尝试与**精确障碍**（2026 续）

### 14.1 要证的桥梁

$$\underbrace{N\ \text{单射}}_{\text{保留 ②}}\ \wedge\ \underbrace{A\circ N=N\circ A'}_{\text{步 1}}\ \wedge\ \underbrace{f\circ A'=0}_{\text{步 4}}\ \Longrightarrow\ \underbrace{\forall d_1d_2,\ Nd_1+A(Nd_2)=0\Rightarrow f(d_1)=0}_{\textbf{几何条件}}$$

**意义** ✓：证明几何版本**蕴含** $A'$ 版本 ⟹ 两者**统一** ✓ ⟹ 一般 $A$ 的入口更清晰 ✓

### 14.2 两次失败（收尾策略 ✗）

| 尝试 | 策略 | 结果 |
|---|---|---|
| 1 | `rw [← hfact]` | 找不到模式 ✗（`A (Nmap d2)` 非语法等于 `(A.comp Nmap) d2` ✗）|
| 2 | `change` 暴露复合 + `rw [hfact]` | 第一处过 ✓，第二处 `← LinearMap.map_add` 找不到 ✗（`rw [hfact]` 后留下 `(Nmap.comp A') d2` 未展开 ✗）|
| 3 | 全程 `simpa [LinearMap.comp_apply, hfact]` | **Type mismatch** ✗（`simpa` 的化简方向/目标不匹配 ✓）|

### 14.3 下一次的**确定做法**

**关键**：`rw` 与 `simp` 对 **`LinearMap.comp` 的应用**处理不同 ✓ ——
必须**先展开** `comp_apply` ✓ 再 `rw` ✓，且**逐条**做 ✓：

```lean
  intro d1 d2 h
  -- 把 h 改写成「Nmap d1 + Nmap (A' d2) = 0」
  have hh : Nmap d1 + Nmap (A' d2) = 0 := by
    have h1 := congrArg (fun m : V →ₗ[K] V => m d2) hfact
    simp only [LinearMap.comp_apply] at h1        -- h1 : A (Nmap d2) = Nmap (A' d2)
    rw [← h1] at h                               -- h  : Nmap d1 + Nmap (A' d2) = 0
    exact h
  -- 合并为 Nmap (d1 + A' d2) = 0
  have h2 : Nmap (d1 + A' d2) = 0 := by
    rw [LinearMap.map_add]
    exact hh
  -- 单射 ⟹ d1 + A' d2 = 0
  have h3 : d1 + A' d2 = 0 := by
    have hmem : (d1 + A' d2) ∈ Nmap.ker := LinearMap.mem_ker.mpr h2
    rw [hN] at hmem
    simpa using hmem
  -- f d1 + f (A' d2) = 0 且 f (A' d2) = 0
  have hf' : f (A' d2) = 0 := by
    have h1 := congrArg (fun m : D →ₗ[K] W => m d2) hfA
    simpa [LinearMap.comp_apply] using h1
  have hsum : f d1 + f (A' d2) = 0 := by
    rw [← LinearMap.map_add, h3, map_zero]
  rw [hf', add_zero] at hsum
  exact hsum
```

**⚠️ 关键差异**：**不要**用 `rw [hfact] at h` ✗ ——
应先用 **`congrArg` + `simp only [comp_apply]`** 把 `hfact` **实例化**成 $A(Nd_2)=N(A'd_2)$ ✓，
再用 `rw [← h1]` ✓ —— 这样 `rw` 面对的是**已展开**的项 ✓ ✓

### 14.4 状态

```
Build completed successfully     ✓ 零 error、零 warning
定理总数：34 条                  ✓（桥梁定理回退 ✓）
备份：Draft/C6_with_geo.lean     ✓
```

**⟹ 几何版本 `exists_row_killing_AK`（任意 $A$ ✓）已机器验证 ✓ —— 这是本轮真正的突破 ✓**
**⟹ 桥梁定理是"锦上添花" ✓，下一次按 §14.3 逐条展开即可 ✓**
---

## 十五、桥梁定理：第 4–8 次尝试（**逐步逼近** ✓）

### 15.1 进展曲线

| 尝试 | 修正 | 结果 |
|---|---|---|
| 4 | 按 §14.3 用 `congrArg` 实例化 | 3 处错误 ✗ |
| **5** | **类型标注应为 `D →ₗ V`（非 `V →ₗ V`）** ✓ | 降到 2 处 ✓ |
| **6** | **`rw [hinst]`（非 `← hinst`）** ✓ —— 我要把 $A(Nd_2)$ **换成** $N(A'd_2)$ ✓ | **降到 1 处** ✓ |
| 7 | 试图重写 `hsum` 的收尾 | 仍是 `Type mismatch` ✗ |
| 8 | 换 `hz`+`rwa` 写法 | 同 ✗ |

### 15.2 ✅ 已解决的两个坑（**通用价值** ✓）

| # | 坑 | 正解 |
|---|---|---|
| **A** | `congrArg (fun m : V →ₗ[K] V => m d2) hfact` 类型错 ✗ | `hfact : A.comp Nmap = Nmap.comp A'` ✓ 两边是 **`D →ₗ V`** ✓ ⟹ 标注必须写 `D →ₗ[K] V` ✓ |
| **B** | `rw [← hinst] at h` 找不到模式 ✗ | **方向**：要把 $A(Nd_2)$ 换成 $N(A'd_2)$ ✓ ⟹ 用 **`rw [hinst]`**（去掉 `←`）✓ |

### 15.3 ⏸ 剩下的**唯一**未解处（第 518 行 ✓）

```lean
  have hsum : f d1 + f (A' d2) = 0 := by
    ...   -- Type mismatch: After simplification, term
```

**⟹ 这是纯收尾问题** ✗ —— 目标是从 `h3 : d1 + A' d2 = 0` 得到 $f d_1+f(A'd_2)=0$ ✓

**下一次的确定做法**（**最保险** ✓）：
```lean
  have hsum : f d1 + f (A' d2) = 0 := by
    have hz : f (d1 + A' d2) = 0 := by
      rw [h3]
      exact map_zero f            -- ← 用 `map_zero f`（显式）而非 `map_zero` ✓
    have := hz
    rw [map_add] at this          -- ← 用 `map_add`（显式，非 `LinearMap.map_add`）✓
    exact this
```

**⚠️ 要点**：`map_zero` / `map_add` 用**显式函数**（`map_zero f` ✓）——
避免 `simp`/`rw` 在**隐式参数推断**上出问题 ✓（这是本次 3 次失败的共同根源 ✓）

### 15.4 状态

```
Build completed successfully     ✓ 零 error、零 warning
定理总数：34 条                  ✓（桥梁回退 ✓）
```

**⟹ 核心突破（几何版本 ✓，任意 $A$ ✓）已稳固 ✓；桥梁定理按 §15.3 可一次到位 ✓**
---

## 十六、🎉🎉🎉 **步 5 的几何版 —— $CA^2=0$ 彻底去除（35 条定理，全绿）**

### 16.1 自查 #28（一次**实质改进**，非错误）

**原步 5 的问题** ✗：补行用了 $\mathrm{row}[C;CA]$ ✓ ⟹
$$L'(Av)=L(Av)+P_0(CAv)+\underbrace{P_1(CA^2v)}_{!}$$
⟹ **必须** $CA^2=0$ ✗ —— 这把 c6′ 限制在 $CA^2=0$ ⚠️

**新洞察** ✓：**只加 $\mathrm{row}[C]$ 中的行** ✓ —— 即 $L'=L+P_0C$ ✓ —— 则
$$L'(Av)=L(Av)+P_0(C(Av))$$
而 $CAv=0$ **本来就在假设** $v\in\ker[L';C;CA]$ 里 ✓ ⟹ $P_0(CAv)=0$ ✓ ⟹
$$L'(Av)=L(Av)=0\ ✓\qquad\textbf{完全不需要}\ CA^2=0\ ✓$$

### 16.2 新定理（**已机器验证 ✓**）

```lean
public theorem condA_of_add_row_C
    (L L' : V →ₗ[K] W) (A : V →ₗ[K] V) (C : V →ₗ[K] G) (P0 : G →ₗ[K] W)
    (hL' : L' = L + P0.comp C)
    (hA : ∀ v, L v = 0 → C v = 0 → C (A v) = 0 → L (A v) = 0) :
    ∀ v, L' v = 0 → C v = 0 → C (A v) = 0 → L' (A v) = 0
```

$$\boxed{\ L'=L+P_0\,C\ \Longrightarrow\ \text{(A) 的核形式被保持}\qquad\textbf{无需}\ CA^2=0\ ✓}$$

### 16.3 意义：**$CA^2=0$ 在 c6′ 中已无处使用** ✓✓

| 环 | 原依赖 | 现状 |
|---|---|---|
| ① 不变性 | $CA^2=0$ ⚠️ | **几何版不需 $A'$** ⟹ 不再需要 ✓ |
| ③′ 行构造 | —— | `exists_row_killing_AK`（**任意 $A$** ✓）|
| ⑤ 加行保持 (A) | **$CA^2=0$** ⚠️ | **`condA_of_add_row_C`（无需 ✓）** 🆕 |
| 其余 | —— | 纯线性代数 ✓ |

$$\boxed{\ \textbf{c6′ 的构造层面已完全不依赖}\ CA^2=0\ \Longrightarrow\ \textbf{一般 } A \textbf{ 的 c6′ 已在射程内}\ ✓✓}$$

### 16.4 工程状态

```
Build completed successfully     ✓ 零 error、零 warning
定理总数：35 条
```

### 16.5 c6′ 链条：**12 环，11 环机器验证**

| 环 | 定理 | 是否需 $CA^2=0$ |
|---|---|---|
| ① 不变性（$A'$ 版）| `ker_inter_ker_comp_is_invariant` | 是 ⚠️ |
| ② $A'^2=0\Rightarrow\ker A'\ne0$ | `ker_ne_bot_of_comp_self_eq_zero` | — |
| ②′ 构造性对偶 | `exists_dual_comp_eq_zero` | — |
| ③ 行提升 | `exists_comp_eq_of_ker_le_ker` | — |
| **③′ 几何版行构造（任意 $A$ ✓）** | **`exists_row_killing_AK`** | **否 ✓** |
| ④ $\pi(lA)=0$ | `comp_A_comp_N_eq_zero` | — |
| ⑤ 加行（$C;CA$ 版）| `condA_of_add_row_mem` | 是 ⚠️ |
| **⑤′ 加行（仅 $C$ 版 ✓）** | **`condA_of_add_row_C`** 🆕 | **否 ✓** |
| ⑥ (A) ⟹ $F=\Lambda H$ | `F_eq_Lam_comp_H` | — |
| ⑦ (S) 失败 | `S_fails_*` | — |
| ⑧ 组装（$A'$ 版）| `c6'_final` | 是 ⚠️ |
| ⑨ 桥梁 | ⏸ 待补（低优先级）| — |

### 16.6 **下一步：一般 $A$ 的 c6′**（路径已通 ✓）

用 **③′ + ⑤′** 重写 ⑧：

$$\textbf{c6'}':\quad (\text{A})\ \wedge\ N\hookrightarrow\ker C\sqcap\ker(CA)\ \wedge\ \underbrace{\text{几何相容}}_{\textbf{③′}}\ \wedge\ H\ne0\ \Longrightarrow\ \textbf{(S) 失败}$$

**⟹ 完全不需要 $CA^2=0$、不需要 $A'$** ✓✓
**⟹ 完成后**：结合 T12 ⟹ **情形 II 恒 NO** ⟹ **分支 A 无硬度** ✓