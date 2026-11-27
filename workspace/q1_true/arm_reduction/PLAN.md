# arm_reduction · 规划（2026-11-27）

> 目标：ARM(3) → q1 的**翻译引理**（不是完整归约）。本文件记录路线现状、障碍与接下来的三步。

## 路线是什么

Majumdar 2026（arXiv:2602.14037）：ARM(3) 是 $\exists\mathbb R$-完全——给定仿射约束
$\langle A_\ell,X\rangle=b_\ell$ 与 $\operatorname{rank}X\le3$，判定是否存在实 $X$。
可借的三件技术：**违反 $\Rightarrow$ 某个 $4\times4$ 子式满秩**、**gauge block 去歧义**、**composition lemma**。

## 已有结论（来自 196–199、254、390）

1. **载体界**：q1 的自由数据是 $\Phi=R[N\ AN]\in\mathbb C^{m\times d_0}$，$d_0\le n-p$（已证；
   $n=4..10,p=1,2$ 七模式取等）。故**逐行忠实编码任意 $n$ 维 $X$ 不可能**（$p\ge1$）。
2. **约束可传递**：把 $X$ 限制到 $\operatorname{col}M$ 后，$\langle A_\ell,X\rangle=\langle a_\ell,\Phi\rangle$；
   且 $\operatorname{rank}X\le3\iff\operatorname{rank}\Phi\le3$（$X=\Phi M^{+}$）。
3. **仿射控制不足**：q1 只能钉住前 $r_0$ 行（$L_0$），**没有一般线性泛函**。
4. **秩条件对不上**：q1 是 $\operatorname{rank}H=\omega$（等式）+ $(5a)$ 包含 + 谱 $\forall\lambda$；
   没有一条给 $\operatorname{rank}\Phi\le3$。
5. **$X=L$ 不行**：$q=3$ 时秩自动、$q>3$ 时无秩约束；唯一候选接口是 $X=[L;L_{\rm fix}]$ 的**行包含**。

**结论**：门关系只能靠秩条件 gadget，而乘法 gadget 已被证 unsound（306）——ARM 路线与
“sound gadget 是否可能”是同一个关口。

## ChatGPT 评估（2026-11-27）

> 值得再推进一轮，但只做**短程的“行包含接口”检验**；不值得继续泛化乘法门 gadget。

### 三步与失败判据

1. **形式化行包含接口**：$X=[L;L_{\rm fix}]$，构造 q1 实例使可行 $\iff\operatorname{rank}X\le3$，
   且保持 $H$ 满秩与 $(5a)$。
   *失败判据*：行包含只给单向蕴含，或必然引入额外自由行导致伪解。
2. **检验秩约束是否真实存在**：证明 q1 的 $H$、$(5a)$、谱条件能**共同推出** $\operatorname{rank}X\le3$。
   *失败判据*：找到满足全部 q1 条件但 $\operatorname{rank}X>3$ 的系统性反例；或证明没有非平凡上界。
3. **双向翻译定理**：若前两步通过，证 ARM(3) 实例可有效映射为 q1 实例，正反两个方向都成立，
   排除非规范表示与谱条件产生的伪解。
   *失败判据*：反向恢复需要额外的一般仿射泛函，或无法排除非编码解。

### 最省的 no-go 陈述（若第 2 步失败）

> 在当前候选编码 $X=[L;L_{\rm fix}]$ 下，q1 的满秩等式、行空间包含及谱可行性条件不能推出所需的
> $\operatorname{rank}X\le3$；因此该接口不能承载 ARM(3) 的秩约束，除非引入新的秩约束机制。

（这是对该接口的 no-go，不是对所有 ARM(3)→q1 归约的否定。）

## 执行结果（2026-11-27）

第 1 步已做，**接口失败**：[488](attempts/488_arm_interface_rowcount_nogo.md) 证明
$\operatorname{rank}[L;L_0]=\operatorname{rank}L$，而 q1 不约束 $\operatorname{rank}L$
（$L=I_n$ 是可行反例），所以 $X=[L;L_{\rm fix}]$ 不能承载 $\operatorname{rank}X\le3$。

A 项（谱机制）也已做：[489](attempts/489_spectral_rank_forcing.md) 把 $(5b)$ 精确化为
“$Z$ 在 $W$ 上无特征向量”，并说明它不提供秩上界；剩余唯一靶子是**谱秩强制 gadget**
（rank $X\ge4$ ⇒ $Z$ 有特征向量），未构造。

**决定**：ARM 作为**活跃路线关闭**；保留 390/488/489 的 no-go 与靶子记录。若将来有人提出
谱秩强制 gadget 的具体构造，再重开这一个点。

## 下一步（第 1 步，已执行）

1. 写清 $X=[L;L_{\rm fix}]$ 的精确定义（$L_{\rm fix}$ 与 $L_0$ 的关系、$q$ 与 $m$ 的对应）；
2. 先做最小实例：$m=4$、$\operatorname{rank}X\le3$，看 q1 的哪些条件能充当“第 4 行落在前三行张成里”；
3. 用精确算术验证候选构造（不是采样），并记录它失败在哪一条。

## 相关

- [README](README.md)、[STATUS](STATUS.md)
- `attempts/390_arm_translation_analysis.md`（最完整的现状分析）
- `attempts/196–199`、`attempts/254`
- `literature/notes/MAJUMDAR_2026_ARM_ER.md`
